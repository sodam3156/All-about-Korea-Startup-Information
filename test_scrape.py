# -*- coding: utf-8 -*-
"""핵심 로직 자체 점검 — 네트워크 없이 실행: python test_scrape.py"""
import json
import tempfile
from datetime import datetime, timedelta
from pathlib import Path

import scrape
from scrape import (TextWithLinks, build_reminders, dedupe_new, format_digest,
                    item_id, make_record, normalize_date, update_health,
                    _parse_ccei_programs, _parse_sjtp_rows)


def test_normalize_date():
    assert normalize_date("2026.08.24") == "2026-08-24"
    assert normalize_date("2026-08-24 18:00") == "2026-08-24"
    assert normalize_date("접수기간: 2026년 8월 5일까지") == "2026-08-05"
    assert normalize_date("20268") is None
    assert normalize_date(None) is None
    assert normalize_date("2026.13.99") is None  # 존재하지 않는 날짜


def test_text_with_links():
    html = ('<html><script>var x=1;</script><body><table>'
            '<tr><td><a href="/bbs/view.php?id=3">모집 공고</a></td><td>2026.08.01</td></tr>'
            '</table></body></html>')
    text = TextWithLinks.convert(html, "https://ex.com/bbs/list.php")
    assert "[모집 공고](https://ex.com/bbs/view.php?id=3)" in text
    assert "var x=1" not in text


def test_dedupe():
    a = make_record("src", "지원사업", "공고 A", "https://ex.com/1", "기관")
    a_dup = make_record("src", "지원사업", "공고 A(재수집)", "https://ex.com/1", "기관")
    b = make_record("src", "지원사업", "공고 B", "https://ex.com/2", "기관")
    fresh = dedupe_new([a_dup, b, b], existing=[a])
    assert [r["url"] for r in fresh] == ["https://ex.com/2"]  # 기존 중복·배치 내 중복 모두 제거


def test_status_latest_wins(tmp_path=None):
    with tempfile.TemporaryDirectory() as td:
        p = Path(td) / "status.jsonl"
        rows = [{"id": "abc", "status": "검토", "updated_at": "1"},
                {"id": "abc", "status": "제출", "updated_at": "2"},
                {"id": "xyz", "status": "초안", "updated_at": "1"}]
        p.write_text("\n".join(json.dumps(r) for r in rows), encoding="utf-8")
        orig = scrape.STATUS_PATH
        scrape.STATUS_PATH = p
        try:
            latest = scrape.load_status()
        finally:
            scrape.STATUS_PATH = orig
        assert latest["abc"]["status"] == "제출"  # append-only: 마지막 레코드가 유효
        assert latest["xyz"]["status"] == "초안"


def test_parse_sjtp_rows():
    # 실제 sjtp.or.kr 게시판에서 확인한 마크업 그대로 (행 2개로 non-greedy 경계도 같이 검증)
    html = """
    <tr class="">
        <td class="td_num2">638</td>
        <td class="td_subject">
            <ul class="bo_title">
                <li><span>사업명</span><p><a href="https://sjtp.or.kr/bbs/board.php?bo_table=business01&amp;wr_id=1936">2026년 세종RISE센터 분야별 전문가 모집 공고</a></p></li>
                <li><span>주관기관</span><p>(재)세종테크노파크 세종RISE센터</p></li>
                <li><span>시행기관</span><p>※ 집중모집기간(~'26.3.23)</p></li>
                <li><span>신청기간</span><p>2026-03-10 ~ 2026-12-31</p></li>
            </ul>
        </td>
    </tr>
    <tr class="">
        <td class="td_num2">637</td>
        <td class="td_subject">
            <ul class="bo_title">
                <li><span>사업명</span><p><a href="https://sjtp.or.kr/bbs/board.php?bo_table=business01&amp;wr_id=1942">[2026-020호] 기술닥터제 지원사업 모집공고</a></p></li>
                <li><span>주관기관</span><p>(재)세종테크노파크</p></li>
                <li><span>신청기간</span><p>2026-03-23 ~ 2026-12-31</p></li>
            </ul>
        </td>
    </tr>
    """
    rows = _parse_sjtp_rows(html)
    assert len(rows) == 2  # non-greedy 경계 — 두 행이 하나로 뭉개지지 않아야 함
    assert rows[0]["url"] == "https://sjtp.or.kr/bbs/board.php?bo_table=business01&wr_id=1936"  # &amp; → &
    assert rows[0]["title"] == "2026년 세종RISE센터 분야별 전문가 모집 공고"
    assert rows[0]["org"] == "(재)세종테크노파크 세종RISE센터"
    assert rows[0]["posted"] == "2026-03-10" and rows[0]["deadline"] == "2026-12-31"
    assert rows[1]["url"].endswith("wr_id=1942")


def test_parse_ccei_programs():
    payload = {"result": {"size": 1, "list": [{
        "PROGRAM_TITLE": "창업-BuS in 세종, 수요투자 라운드 참여기업 모집",
        "SEQ": "10434", "C_SDATE": "2026.04.30", "C_EDATE": "2026.12.31", "REG_DATE": "2026.04.30",
    }]}}
    rows = _parse_ccei_programs(payload)
    assert len(rows) == 1
    assert rows[0]["url"] == ("https://ccei.creativekorea.or.kr/sejong/service/program_view.do"
                               "?no=10434&sMenuType=00040001&cntry_nm=sejong")
    assert rows[0]["deadline"] == "2026.12.31"  # make_record가 normalize_date로 정규화하는 원시값


def test_parse_ccei_programs_skips_incomplete():
    payload = {"result": {"list": [{"PROGRAM_TITLE": "제목만 있고 SEQ 없음"}]}}
    assert _parse_ccei_programs(payload) == []


def test_update_health():
    h = {}
    h = update_health(h, "A", [])
    assert h["A"]["streak"] == 1
    h = update_health(h, "A", [])
    assert h["A"]["streak"] == 2  # 연속 2회 0건 — 임계치(HEALTH_ALERT_THRESHOLD=2) 도달
    h = update_health(h, "A", [{"x": 1}])
    assert h["A"]["streak"] == 0  # 정상 수집되면 리셋
    h2 = update_health({}, "B", None)
    assert "B" not in h2  # 의도적 스킵(None)은 헬스 기록 자체를 남기지 않음


def test_format_digest_broken_warning():
    digest = format_digest([], [], broken=[("세종테크노파크 사업공고", 2, "2026-08-03 07:00")])
    assert "소스 점검 필요" in digest and "세종테크노파크 사업공고" in digest
    assert format_digest([], [], broken=[]) == format_digest([], [], broken=[])  # 이상 없으면 경고 섹션 없음
    assert "소스 점검 필요" not in format_digest([], [], broken=[])


def test_reminders():
    soon = (datetime.now(scrape.KST) + timedelta(days=3)).strftime("%Y-%m-%d")
    far = (datetime.now(scrape.KST) + timedelta(days=30)).strftime("%Y-%m-%d")
    items = [
        make_record("s", "지원사업", "임박+검토중", "https://ex.com/a", "기관", deadline=soon),
        make_record("s", "지원사업", "임박+상태없음", "https://ex.com/b", "기관", deadline=soon),
        make_record("s", "지원사업", "여유+검토중", "https://ex.com/c", "기관", deadline=far),
    ]
    status = {item_id("https://ex.com/a"): {"status": "검토"},
              item_id("https://ex.com/c"): {"status": "검토"}}
    rems = build_reminders(items, status)
    assert len(rems) == 1 and "임박+검토중" in rems[0]  # 진행 중 + D-7 이내만


if __name__ == "__main__":
    for name, fn in sorted(globals().items()):
        if name.startswith("test_"):
            fn()
            print(f"ok {name}")
    print("모든 체크 통과")
