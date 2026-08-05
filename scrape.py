# -*- coding: utf-8 -*-
"""한국 스타트업 정보 수집 파이프라인 (git-scraping, 완전 규칙 기반 — API 비용 $0).

매일 1회 실행: 수집 → dedupe → 상세 수집 → README 갱신 → 텔레그램 다이제스트.
데이터는 data/items.jsonl(목록), data/details/{id}.md(상세), data/status.jsonl(진행 상태).
헤르메스는 raw.githubusercontent.com 에서 이 파일들을 직접 읽는다.

LLM을 쓰지 않는다 — 소스마다 공식 API/RSS 또는 정규식 파서. 사이트 개편으로 파서가
깨지면(연속 2회 이상 0건) data/source_health.json에 기록하고 다이제스트에 경고를 띄운다
(ponytail: 정규식 파서는 조용히 깨지는 게 진짜 리스크 — 이 체크가 "고장 감지 피드백 루프").

환경변수 (둘 다 선택 — 없어도 전체 파이프라인 정상 동작):
  DATA_GO_KR_KEY      K-Startup 공공데이터 API. 없으면 그 소스만 스킵.
  TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID  없으면 다이제스트를 stdout에만 출력.
"""
import hashlib
import json
import os
import re
import sys
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin
from xml.etree import ElementTree

import requests

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
ITEMS_PATH = DATA / "items.jsonl"
STATUS_PATH = DATA / "status.jsonl"
HEALTH_PATH = DATA / "source_health.json"
DETAILS_DIR = DATA / "details"
README_PATH = ROOT / "README.md"

KST = timezone(timedelta(hours=9))
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) startup-info-bot"}
CATEGORIES = ["지원사업", "공지", "뉴스", "행사"]
DETAIL_CATEGORIES = {"지원사업", "공지"}  # 지원서 작성 재료가 되는 것만 상세 수집
MAX_DETAILS_PER_RUN = 10  # ponytail: 첫 실행 폭주 방지용 상한, 밀린 건 다음 실행이 처리
HEALTH_ALERT_THRESHOLD = 2  # 연속 이 횟수 이상 0건이면 "파서 깨짐" 경고

# 소스 추가 = 여기 한 줄 + fetch_* 함수 하나. type이 COLLECT의 dispatch 키와 대응.
SOURCES = [
    {"name": "K-Startup 사업공고", "type": "kstartup_api", "category": "지원사업"},
    {
        "name": "세종창조경제혁신센터 소식",
        "type": "ccei_json",
        "url": "https://ccei.creativekorea.or.kr/sejong/json/info/prList.json",
        "category": "뉴스",
    },
    {
        "name": "세종창조경제혁신센터 지원프로그램",
        "type": "ccei_program",
        "url": "https://ccei.creativekorea.or.kr/sejong/json/service/programLists.json",
        "category": "지원사업",
    },
    {
        "name": "세종테크노파크 사업공고",
        "type": "sjtp_board",
        "url": "https://sjtp.or.kr/bbs/board.php?bo_table=business01",
        "category": "지원사업",
    },
    {"name": "벤처스퀘어", "type": "rss", "url": "https://www.venturesquare.net/feed", "category": "뉴스"},
]


# ---------------------------------------------------------------- 공통 유틸
def now_kst() -> str:
    return datetime.now(KST).strftime("%Y-%m-%d %H:%M")


def item_id(url: str) -> str:
    return hashlib.sha1(url.strip().encode()).hexdigest()[:12]


def pick(d: dict, *keys, default=None):
    """API 응답 필드명이 문서와 다를 때를 대비해 후보 키를 순서대로 시도."""
    for k in keys:
        v = d.get(k)
        if v not in (None, ""):
            return v
    return default


def make_record(source: str, category: str, title: str, url: str, org: str,
                posted=None, deadline=None) -> dict:
    return {
        "id": item_id(url),
        "source": source,
        "category": category if category in CATEGORIES else "공지",
        "title": " ".join(str(title).split()),
        "url": url.strip(),
        "org": org or source,
        "posted": normalize_date(posted),
        "deadline": normalize_date(deadline),
        "detail": None,
        "scraped_at": now_kst(),
    }


def normalize_date(s):
    """'2026.08.24', '20260824', '2026-08-24 18:00' 등을 YYYY-MM-DD로. 실패 시 None."""
    if not s:
        return None
    m = re.search(r"(20\d{2})[.\-/년\s]*(\d{1,2})[.\-/월\s]*(\d{1,2})", str(s))
    if not m:
        return None
    y, mo, d = m.groups()
    try:
        return datetime(int(y), int(mo), int(d)).strftime("%Y-%m-%d")
    except ValueError:
        return None


class TextWithLinks(HTMLParser):
    """HTML → 텍스트. <a href>는 [텍스트](절대URL)로 보존해 첨부파일 링크가 살아있게 한다."""

    def __init__(self, base_url: str):
        super().__init__(convert_charrefs=True)
        self.base = base_url
        self.out = []
        self._href = None
        self._skip = 0  # script/style 중첩 깊이

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self._skip += 1
        elif tag == "a" and not self._skip:
            href = dict(attrs).get("href", "")
            if href and not href.startswith(("javascript:", "#", "mailto:")):
                self._href = urljoin(self.base, href)
                self.out.append("[")
        elif tag in ("tr", "li", "br", "p", "div") and not self._skip:
            self.out.append("\n")

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self._skip = max(0, self._skip - 1)
        elif tag == "a" and self._href:
            self.out.append(f"]({self._href}) ")
            self._href = None

    def handle_data(self, data):
        if not self._skip and data.strip():
            self.out.append(data.strip() + " ")

    @classmethod
    def convert(cls, html_text: str, base_url: str, limit: int = 8000) -> str:
        p = cls(base_url)
        p.feed(html_text)
        text = re.sub(r"\n{3,}", "\n\n", "".join(p.out))
        text = re.sub(r"\s+\]\(", "](", text)  # [텍스트 ](url) → [텍스트](url)
        return text[:limit]


# ---------------------------------------------------------------- fetch (소스 타입별)
# 반환값 규약: 리스트(빈 리스트 포함) = 시도했음(헬스 체크 대상). None = 설정 누락 등으로
# 의도적 스킵(헬스 체크 제외) — 이 구분이 없으면 키 미설정을 "파서 고장"으로 오인한다.
def fetch_kstartup(source: dict):
    key = os.environ.get("DATA_GO_KR_KEY")
    if not key:
        print("  DATA_GO_KR_KEY 없음 — K-Startup API 스킵")
        return None
    r = requests.get(
        "https://apis.data.go.kr/B552735/kisedKstartupService01/getAnnouncementInformation01",
        params={"serviceKey": key, "page": 1, "perPage": 100, "returnType": "json"},
        headers=UA, timeout=30,
    )
    r.raise_for_status()
    rows = r.json().get("data", [])
    out = []
    for row in rows:
        title = pick(row, "biz_pbanc_nm", "intg_pbanc_biz_nm", "pbanc_nm", "title")
        url = pick(row, "detl_pg_url", "detlPgUrl", "pbanc_url")
        if not title or not url:
            continue
        out.append(make_record(
            source["name"], source["category"], title, url,
            org=pick(row, "pbanc_ntrp_nm", "excInstNm", "sprv_inst", default="창업진흥원"),
            posted=pick(row, "pbanc_rcpt_bgng_dt", "reg_dt"),
            deadline=pick(row, "pbanc_rcpt_end_dt", "pbanc_ddln_dt"),
        ))
    return out


def fetch_ccei_json(source: dict) -> list:
    r = requests.post(
        source["url"], data={"pn": 1},
        headers={**UA, "X-Requested-With": "XMLHttpRequest"}, timeout=30,
    )
    r.raise_for_status()
    out = []
    for row in r.json().get("result", {}).get("list", [])[:40]:
        title, url = row.get("TITLE"), row.get("LINK_URL")
        if not title or not url:
            continue
        out.append(make_record(
            source["name"], source["category"], title, url,
            org=row.get("WRITER") or source["name"], posted=row.get("REG_DATE"),
        ))
    return out


def _parse_ccei_programs(payload: dict) -> list:
    """programLists.json 응답 파싱만 담당 — 네트워크 없이 테스트 가능."""
    rows = []
    for row in payload.get("result", {}).get("list", []):
        title, seq = row.get("PROGRAM_TITLE"), row.get("SEQ")
        if not title or not seq:
            continue
        url = (f"https://ccei.creativekorea.or.kr/sejong/service/program_view.do"
               f"?no={seq}&sMenuType=00040001&cntry_nm=sejong")
        rows.append({"title": title, "url": url,
                     "posted": row.get("C_SDATE") or row.get("REG_DATE"),
                     "deadline": row.get("C_EDATE")})
    return rows


def fetch_ccei_programs(source: dict) -> list:
    """세종창경 지원프로그램 — programLists.json AJAX (UI가 쓰는 것과 동일한 파라미터)."""
    r = requests.post(
        source["url"],
        data={"sMenuType": "00040001", "pn": 1, "pagePerContents": 50, "cntry_nm": "sejong"},
        headers={**UA, "X-Requested-With": "XMLHttpRequest"}, timeout=30,
    )
    r.raise_for_status()
    return [make_record(source["name"], source["category"], row["title"], row["url"],
                         org=source["name"], posted=row["posted"], deadline=row["deadline"])
            for row in _parse_ccei_programs(r.json())]


_SJTP_ROW_RE = re.compile(r'<tr class="[^"]*">(.*?)</tr>', re.S)
_SJTP_TITLE_RE = re.compile(r'<a href="([^"]+wr_id=\d+)">([^<]+)</a>')
_SJTP_ORG_RE = re.compile(r"<span>주관기관</span>\s*<p>([^<]*)</p>")
_SJTP_PERIOD_RE = re.compile(r"<span>신청기간</span>\s*<p>([^<]*)</p>")


def _parse_sjtp_rows(html_text: str) -> list:
    """<tr> 안 <ul class="bo_title"> 목록 정규식 파싱만 담당 — 네트워크 없이 테스트 가능."""
    rows = []
    for block in _SJTP_ROW_RE.findall(html_text):
        m = _SJTP_TITLE_RE.search(block)
        if not m:
            continue
        url, title = m.group(1).replace("&amp;", "&"), m.group(2).strip()
        org_m, period_m = _SJTP_ORG_RE.search(block), _SJTP_PERIOD_RE.search(block)
        posted = deadline = None
        if period_m:
            parts = [p.strip() for p in period_m.group(1).split("~")]
            posted = parts[0] if parts else None
            deadline = parts[1] if len(parts) > 1 else None
        rows.append({"title": title, "url": url,
                     "org": org_m.group(1).strip() if org_m else None,
                     "posted": posted, "deadline": deadline})
    return rows


def fetch_sjtp_board(source: dict) -> list:
    """세종테크노파크 사업공고 — 정적 HTML."""
    r = requests.get(source["url"], headers=UA, timeout=30)
    r.raise_for_status()
    return [make_record(source["name"], source["category"], row["title"], row["url"],
                         org=row["org"] or source["name"], posted=row["posted"], deadline=row["deadline"])
            for row in _parse_sjtp_rows(r.text)]


def fetch_rss(source: dict) -> list:
    r = requests.get(source["url"], headers=UA, timeout=30)
    r.raise_for_status()
    root = ElementTree.fromstring(r.content)
    out = []
    for it in root.iter("item"):
        title = it.findtext("title", "").strip()
        link = it.findtext("link", "").strip()
        if not title or not link:
            continue
        try:
            posted = parsedate_to_datetime(it.findtext("pubDate", "")).strftime("%Y-%m-%d")
        except (ValueError, TypeError):
            posted = None
        out.append(make_record(source["name"], source["category"], title, link,
                                org=source["name"], posted=posted))
    return out


FETCHERS = {
    "kstartup_api": fetch_kstartup,
    "ccei_json": fetch_ccei_json,
    "ccei_program": fetch_ccei_programs,
    "sjtp_board": fetch_sjtp_board,
    "rss": fetch_rss,
}


# ---------------------------------------------------------------- 소스 헬스 체크 (고장 감지)
def load_health() -> dict:
    if not HEALTH_PATH.exists():
        return {}
    return json.loads(HEALTH_PATH.read_text(encoding="utf-8"))


def save_health(health: dict):
    DATA.mkdir(exist_ok=True)
    HEALTH_PATH.write_text(json.dumps(health, ensure_ascii=False, indent=2), encoding="utf-8")


def update_health(health: dict, name: str, items) -> dict:
    """items가 None이면 의도적 스킵이라 카운트하지 않는다. 빈 리스트가 연속되면 스트릭 증가,
    한 건이라도 나오면 0으로 리셋 — 이 스트릭이 임계치를 넘으면 파서가 깨졌다고 본다."""
    if items is None:
        return health
    prev = health.get(name, {})
    streak = 0 if items else prev.get("streak", 0) + 1
    health[name] = {"streak": streak, "last_ok": now_kst() if items else prev.get("last_ok")}
    return health


def collect() -> tuple:
    """모든 소스 수집. 한 소스가 죽어도(예외) 나머지는 계속 — 예외도 헬스 스트릭에 반영."""
    health = load_health()
    records, broken = [], []
    for source in SOURCES:
        name = source["name"]
        try:
            got = FETCHERS[source["type"]](source)
        except Exception as e:  # ponytail: 소스 단위 격리 — 한 소스 실패가 전체를 죽이지 않음
            print(f"[{name}] 실패: {e}", file=sys.stderr)
            got = []
        if got is None:
            continue
        print(f"[{name}] {len(got)}건")
        records.extend(got)
        health = update_health(health, name, got)
        if health[name]["streak"] >= HEALTH_ALERT_THRESHOLD:
            broken.append((name, health[name]["streak"], health[name]["last_ok"]))
    save_health(health)
    return records, broken


# ---------------------------------------------------------------- 저장소 (jsonl)
def load_jsonl(path: Path) -> list:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def load_status() -> dict:
    """append-only status.jsonl → id별 마지막 레코드가 유효."""
    latest = {}
    for rec in load_jsonl(STATUS_PATH):
        if rec.get("id"):
            latest[rec["id"]] = rec
    return latest


def dedupe_new(records: list, existing: list) -> list:
    seen = {r["url"] for r in existing} | {r["id"] for r in existing}
    fresh, batch_seen = [], set()
    for r in records:
        if r["url"] in seen or r["id"] in seen or r["id"] in batch_seen:
            continue
        batch_seen.add(r["id"])
        fresh.append(r)
    return fresh


def append_items(records: list):
    DATA.mkdir(exist_ok=True)
    with ITEMS_PATH.open("a", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


# ---------------------------------------------------------------- 상세 수집 (지원서 작성 재료)
def fetch_detail(rec: dict) -> bool:
    """LLM 정리 없이 원문 텍스트를 그대로 저장 — 링크(첨부 포함)는 [텍스트](URL)로 보존."""
    r = requests.get(rec["url"], headers=UA, timeout=30)
    r.raise_for_status()
    text = TextWithLinks.convert(r.text, rec["url"], limit=6000)
    if not text.strip():
        return False
    DETAILS_DIR.mkdir(parents=True, exist_ok=True)
    md = (f"# {rec['title']}\n\n- 출처: {rec['source']}\n- 기관: {rec['org']}\n"
          f"- 원문: {rec['url']}\n- 마감: {rec['deadline'] or '미상'}\n\n"
          "## 원문 (자동 추출, 미가공)\n\n" + text + "\n")
    (DETAILS_DIR / f"{rec['id']}.md").write_text(md, encoding="utf-8")
    rec["detail"] = f"data/details/{rec['id']}.md"
    return True


def fetch_details(new_records: list):
    targets = [r for r in new_records if r["category"] in DETAIL_CATEGORIES][:MAX_DETAILS_PER_RUN]
    for rec in targets:
        try:
            if fetch_detail(rec):
                print(f"  상세 저장: {rec['title'][:40]}")
        except Exception as e:
            print(f"  상세 실패 ({rec['url']}): {e}", file=sys.stderr)


# ---------------------------------------------------------------- README 대시보드
def md_row(r, status_map):
    st = status_map.get(r["id"], {}).get("status", "")
    st_txt = f" `{st}`" if st else ""
    return f"| {r['deadline'] or '-'} | [{r['title']}]({r['url']}){st_txt} | {r['org']} | {r['source']} |"


def render_readme(items: list, status_map: dict):
    today = datetime.now(KST).strftime("%Y-%m-%d")
    open_biz = sorted(
        [r for r in items if r["category"] == "지원사업" and (r["deadline"] or "") >= today],
        key=lambda r: r["deadline"],
    )[:20]
    in_progress = [r for r in items if status_map.get(r["id"], {}).get("status")
                   in ("검토", "지원예정", "초안", "제출")]
    recent = lambda cat, n: [r for r in reversed(items) if r["category"] == cat][:n]

    lines = [f"\n_자동 갱신: {today} (KST)_\n", "## 마감 임박 지원사업\n",
             "| 마감 | 공고 | 기관 | 출처 |", "|---|---|---|---|"]
    lines += [md_row(r, status_map) for r in open_biz] or ["| - | 수집된 공고 없음 | - | - |"]
    if in_progress:
        lines += ["\n## 진행 중인 공고\n", "| 마감 | 공고 | 기관 | 출처 |", "|---|---|---|---|"]
        lines += [md_row(r, status_map) for r in in_progress]
    for title, cat, n in [("최신 공지", "공지", 10), ("행사·데모데이", "행사", 10), ("스타트업 뉴스", "뉴스", 10)]:
        rows = recent(cat, n)
        if rows:
            lines += [f"\n## {title}\n", "| 날짜 | 제목 | 출처 |", "|---|---|---|"]
            lines += [f"| {r['posted'] or '-'} | [{r['title']}]({r['url']}) | {r['source']} |" for r in rows]

    auto = "\n".join(lines)
    readme = README_PATH.read_text(encoding="utf-8") if README_PATH.exists() else ""
    start, end = "<!-- AUTO:START -->", "<!-- AUTO:END -->"
    if start not in readme:
        readme = readme.rstrip() + f"\n\n{start}\n{end}\n"
    readme = re.sub(
        re.escape(start) + r".*?" + re.escape(end),
        start + "\n" + auto.replace("\\", "\\\\") + "\n" + end,
        readme, flags=re.S,
    )
    README_PATH.write_text(readme, encoding="utf-8")


# ---------------------------------------------------------------- 다이제스트 (알림, 규칙 기반)
def build_reminders(items: list, status_map: dict) -> list:
    today = datetime.now(KST).date()
    out = []
    for r in items:
        st = status_map.get(r["id"], {}).get("status")
        if st in ("검토", "지원예정", "초안") and r["deadline"]:
            try:
                dday = (datetime.strptime(r["deadline"], "%Y-%m-%d").date() - today).days
            except ValueError:
                continue
            if 0 <= dday <= 7:
                out.append(f"[D-{dday}][{st}] {r['title']} (마감 {r['deadline']}) {r['url']}")
    return out


def format_digest(new_records: list, reminders: list, broken: list) -> str:
    lines = [f"📋 스타트업 정보 브리핑 {datetime.now(KST).strftime('%m/%d')}"]
    if broken:
        lines.append("\n⚠️ 소스 점검 필요")
        lines += [f"- {name}: {streak}일 연속 0건 (마지막 정상: {last_ok or '기록 없음'}) "
                   "— 사이트 구조가 바뀌었을 수 있음, 파서 확인 필요"
                   for name, streak, last_ok in broken]
    if new_records:
        biz = sorted((r for r in new_records if r["category"] == "지원사업"),
                     key=lambda r: r["deadline"] or "9999")
        rest = [r for r in new_records if r["category"] != "지원사업"]
        if biz:
            lines.append("\n🆕 신규 지원사업")
            lines += [f"- [{r['deadline'] or '마감미상'}] {r['title']} ({r['org']}) {r['url']}" for r in biz[:15]]
        if rest:
            lines.append(f"\n🆕 그 외 신규 ({len(rest)}건)")
            lines += [f"- [{r['category']}] {r['title']} {r['url']}" for r in rest[:15]]
    if reminders:
        lines.append("\n⏰ 진행 중 공고 마감 임박")
        lines += reminders
    return "\n".join(lines)


def send_digest(new_records: list, items: list, status_map: dict, broken: list):
    reminders = build_reminders(items, status_map)
    if not new_records and not reminders and not broken:
        print("신규·리마인드·이상 없음 — 다이제스트 미발송")
        return
    digest = format_digest(new_records, reminders, broken)
    sent = False

    token, chat_id = os.environ.get("TELEGRAM_BOT_TOKEN"), os.environ.get("TELEGRAM_CHAT_ID")
    if token and chat_id:
        resp = requests.post(
            f"https://api.telegram.org/bot{token}/sendMessage",
            json={"chat_id": chat_id, "text": digest[:4000], "disable_web_page_preview": True},
            timeout=30,
        )
        print(f"텔레그램 발송: {resp.status_code}")
        sent = True

    webhook = os.environ.get("DISCORD_WEBHOOK_URL")
    if webhook:
        # UA 없이 보내면 Cloudflare가 403(1010)으로 차단 — 다른 fetch와 같은 UA 재사용
        resp = requests.post(webhook, json={"content": digest[:2000]}, headers=UA, timeout=30)
        print(f"디스코드 발송: {resp.status_code}")
        sent = True

    if not sent:
        print("--- 다이제스트 (텔레그램·디스코드 미설정) ---")
        print(digest)


# ---------------------------------------------------------------- main
def main():
    existing = load_jsonl(ITEMS_PATH)
    status_map = load_status()

    records, broken = collect()
    new_records = dedupe_new(records, existing)
    print(f"신규 {len(new_records)}건 / 기존 {len(existing)}건")

    fetch_details(new_records)
    append_items(new_records)
    all_items = existing + new_records
    render_readme(all_items, status_map)
    send_digest(new_records, all_items, status_map, broken)


if __name__ == "__main__":
    main()
