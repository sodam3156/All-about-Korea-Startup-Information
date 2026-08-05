# -*- coding: utf-8 -*-
"""한국 스타트업 정보 수집 파이프라인 (git-scraping).

매일 1회 실행: 수집 → dedupe → 상세 수집 → README 갱신 → 텔레그램 다이제스트.
데이터는 data/items.jsonl(목록), data/details/{id}.md(상세), data/status.jsonl(진행 상태).
헤르메스는 raw.githubusercontent.com 에서 이 파일들을 직접 읽는다.

환경변수:
  ANTHROPIC_API_KEY   필수에 가까움 — 게시판 추출·상세 정리·다이제스트에 사용. 없으면 해당 단계 스킵.
  DATA_GO_KR_KEY      선택 — K-Startup 공공데이터 API. 없으면 그 소스만 스킵.
  TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID  선택 — 없으면 다이제스트를 stdout에만 출력.
"""
import hashlib
import json
import os
import re
import sys
from datetime import datetime, timedelta, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin
from xml.etree import ElementTree

import requests

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
ITEMS_PATH = DATA / "items.jsonl"
STATUS_PATH = DATA / "status.jsonl"
DETAILS_DIR = DATA / "details"
README_PATH = ROOT / "README.md"

KST = timezone(timedelta(hours=9))
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) startup-info-bot"}
MODEL = "claude-haiku-4-5"  # 추출·요약용 경량 모델 (플랜에서 확정)
CATEGORIES = ["지원사업", "공지", "뉴스", "행사"]
DETAIL_CATEGORIES = {"지원사업", "공지"}  # 지원서 작성 재료가 되는 것만 상세 수집
MAX_DETAILS_PER_RUN = 10  # ponytail: 첫 실행 폭주 방지용 상한, 밀린 건 다음 실행이 처리

# 소스 추가 = 여기 한 줄. type: kstartup_api | ccei_json | rss | board(HTML→LLM)
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
        "type": "board",
        "url": "https://ccei.creativekorea.or.kr/sejong/service/program_list.do",
        "category": "지원사업",
    },
    {
        "name": "세종테크노파크 사업공고",
        "type": "board",
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
        "posted": posted or None,
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
    """HTML → 텍스트. <a href>는 [텍스트](절대URL)로 보존해 LLM이 항목 URL을 뽑을 수 있게 한다."""

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
    def convert(cls, html_text: str, base_url: str, limit: int = 16000) -> str:
        p = cls(base_url)
        p.feed(html_text)
        text = re.sub(r"\n{3,}", "\n\n", "".join(p.out))
        text = re.sub(r"\s+\]\(", "](", text)  # [텍스트 ](url) → [텍스트](url)
        return text[:limit]


# ---------------------------------------------------------------- LLM (Claude)
def anthropic_client():
    if not (os.environ.get("ANTHROPIC_API_KEY") or os.environ.get("ANTHROPIC_AUTH_TOKEN")):
        return None
    import anthropic

    return anthropic.Anthropic()


EXTRACT_SCHEMA = {
    "type": "object",
    "properties": {
        "items": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "title": {"type": "string"},
                    "url": {"type": "string"},
                    "org": {"type": "string"},
                    "category": {"type": "string", "enum": CATEGORIES},
                    "posted": {"type": ["string", "null"]},
                    "deadline": {"type": ["string", "null"]},
                },
                "required": ["title", "url", "org", "category", "posted", "deadline"],
                "additionalProperties": False,
            },
        }
    },
    "required": ["items"],
    "additionalProperties": False,
}


def llm_json(client, prompt: str, schema: dict, max_tokens: int = 8192):
    resp = client.messages.create(
        model=MODEL,
        max_tokens=max_tokens,
        output_config={"format": {"type": "json_schema", "schema": schema}},
        messages=[{"role": "user", "content": prompt}],
    )
    text = next(b.text for b in resp.content if b.type == "text")
    return json.loads(text)


def llm_text(client, prompt: str, max_tokens: int = 2048) -> str:
    resp = client.messages.create(
        model=MODEL,
        max_tokens=max_tokens,
        messages=[{"role": "user", "content": prompt}],
    )
    return next((b.text for b in resp.content if b.type == "text"), "")


def extract_board_items(client, page_text: str, source: dict) -> list:
    """게시판 페이지 텍스트에서 게시글 목록을 스키마로 추출 — 사이트별 셀렉터 대신 이 함수 하나."""
    prompt = (
        f"아래는 '{source['name']}' 게시판 페이지를 텍스트로 변환한 것이다. "
        "게시글 목록(공고/공지)만 추출하라. 메뉴·페이지네이션·푸터는 제외. "
        f"category는 {CATEGORIES} 중 게시글 성격에 맞는 것(기본값 '{source['category']}'). "
        "url은 본문 내 [텍스트](URL) 형태에서 해당 게시글의 절대 URL을 그대로 사용. "
        "posted(게시일)와 deadline(접수 마감일)은 YYYY-MM-DD로, 알 수 없으면 null.\n\n"
        + page_text
    )
    data = llm_json(client, prompt, EXTRACT_SCHEMA)
    return data.get("items", [])


# ---------------------------------------------------------------- fetch (소스 타입별)
def fetch_kstartup(source: dict) -> list:
    key = os.environ.get("DATA_GO_KR_KEY")
    if not key:
        print("  DATA_GO_KR_KEY 없음 — K-Startup API 스킵")
        return []
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
            posted=normalize_date(pick(row, "pbanc_rcpt_bgng_dt", "reg_dt")),
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
            org=row.get("WRITER") or source["name"],
            posted=normalize_date(row.get("REG_DATE")),
        ))
    return out


def fetch_rss(source: dict) -> list:
    from email.utils import parsedate_to_datetime  # RFC822 pubDate는 정규식 말고 이걸로

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
        out.append(make_record(
            source["name"], source["category"], title, link,
            org=source["name"], posted=posted,
        ))
    return out


def fetch_board(source: dict, client) -> list:
    if client is None:
        print(f"  ANTHROPIC_API_KEY 없음 — {source['name']} (board) 스킵")
        return []
    r = requests.get(source["url"], headers=UA, timeout=30)
    r.raise_for_status()
    text = TextWithLinks.convert(r.text, source["url"])
    items = extract_board_items(client, text, source)
    out = []
    for it in items:
        if not it.get("title") or not it.get("url"):
            continue
        out.append(make_record(
            source["name"], it.get("category") or source["category"],
            it["title"], urljoin(source["url"], it["url"]),
            org=it.get("org") or source["name"],
            posted=normalize_date(it.get("posted")), deadline=it.get("deadline"),
        ))
    return out


def collect(client) -> list:
    """모든 소스 수집. 한 소스가 죽어도 나머지는 계속."""
    fetchers = {
        "kstartup_api": lambda s: fetch_kstartup(s),
        "ccei_json": lambda s: fetch_ccei_json(s),
        "rss": lambda s: fetch_rss(s),
        "board": lambda s: fetch_board(s, client),
    }
    records = []
    for source in SOURCES:
        try:
            got = fetchers[source["type"]](source)
            print(f"[{source['name']}] {len(got)}건")
            records.extend(got)
        except Exception as e:  # ponytail: 소스 단위 격리 — 수집 실패가 전체를 죽이면 데이터 유실
            print(f"[{source['name']}] 실패: {e}", file=sys.stderr)
    return records


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
def fetch_detail(client, rec: dict) -> bool:
    r = requests.get(rec["url"], headers=UA, timeout=30)
    r.raise_for_status()
    text = TextWithLinks.convert(r.text, rec["url"], limit=24000)
    body = llm_text(client, (
        "아래는 지원사업/공지 상세 페이지를 텍스트로 변환한 것이다. "
        "지원서 작성에 필요한 정보를 마크다운으로 정리하라. 섹션: "
        "## 개요 / ## 지원대상 / ## 지원내용 / ## 접수기간 / ## 신청방법 / ## 문의처 / ## 첨부파일. "
        "첨부파일 섹션에는 본문 내 [텍스트](URL) 중 첨부(hwp/pdf/zip 등) 링크를 그대로 나열. "
        "페이지에 없는 섹션은 '정보 없음'으로. 내용을 지어내지 마라.\n\n" + text
    ), max_tokens=3000)
    if not body.strip():
        return False
    DETAILS_DIR.mkdir(parents=True, exist_ok=True)
    md = (f"# {rec['title']}\n\n- 출처: {rec['source']}\n- 기관: {rec['org']}\n"
          f"- 원문: {rec['url']}\n- 마감: {rec['deadline'] or '미상'}\n\n{body}\n")
    (DETAILS_DIR / f"{rec['id']}.md").write_text(md, encoding="utf-8")
    rec["detail"] = f"data/details/{rec['id']}.md"
    return True


def fetch_details(client, new_records: list):
    if client is None:
        return
    targets = [r for r in new_records if r["category"] in DETAIL_CATEGORIES][:MAX_DETAILS_PER_RUN]
    for rec in targets:
        try:
            fetch_detail(client, rec)
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


# ---------------------------------------------------------------- 다이제스트 (알림)
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


def send_digest(client, new_records: list, items: list, status_map: dict):
    reminders = build_reminders(items, status_map)
    if not new_records and not reminders:
        print("신규·리마인드 없음 — 다이제스트 미발송")
        return
    listing = "\n".join(
        f"- [{r['category']}] {r['title']} ({r['org']}, 마감 {r['deadline'] or '미상'}) {r['url']}"
        for r in new_records[:40]
    )
    if client:
        digest = llm_text(client, (
            "너는 세종에서 활동하는 1인 창업가의 정보 비서다. 아래 신규 수집 항목을 브리핑 1건으로 요약하라. "
            "우선순위: ①마감 임박 지원사업 ②세종·청년 대상 ③그 외. 항목당 한 줄(제목·마감·URL), "
            "주목할 상위 3건을 먼저, 나머지는 카테고리별로 묶어 간단히. 인사말 없이 본문만.\n\n" + (listing or "(신규 없음)")
        ), max_tokens=1500)
    else:
        digest = "오늘의 신규 수집:\n" + (listing or "(없음)")
    if reminders:
        digest += "\n\n⏰ 진행 중 공고 마감 임박:\n" + "\n".join(reminders)
    digest = f"📋 스타트업 정보 브리핑 {datetime.now(KST).strftime('%m/%d')}\n\n{digest}"

    token, chat_id = os.environ.get("TELEGRAM_BOT_TOKEN"), os.environ.get("TELEGRAM_CHAT_ID")
    if token and chat_id:
        resp = requests.post(
            f"https://api.telegram.org/bot{token}/sendMessage",
            json={"chat_id": chat_id, "text": digest[:4000], "disable_web_page_preview": True},
            timeout=30,
        )
        print(f"텔레그램 발송: {resp.status_code}")
    else:
        print("--- 다이제스트 (텔레그램 미설정) ---")
        print(digest)


# ---------------------------------------------------------------- main
def main():
    client = anthropic_client()
    if client is None:
        print("경고: ANTHROPIC_API_KEY 없음 — 게시판 추출·상세·다이제스트 요약 스킵", file=sys.stderr)

    existing = load_jsonl(ITEMS_PATH)
    status_map = load_status()

    new_records = dedupe_new(collect(client), existing)
    print(f"신규 {len(new_records)}건 / 기존 {len(existing)}건")

    fetch_details(client, new_records)
    append_items(new_records)
    all_items = existing + new_records
    render_readme(all_items, status_map)
    send_digest(client, new_records, all_items, status_map)


if __name__ == "__main__":
    main()
