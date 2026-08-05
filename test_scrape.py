# -*- coding: utf-8 -*-
"""핵심 로직 자체 점검 — 네트워크·LLM 없이 실행: python test_scrape.py"""
import json
import tempfile
from datetime import datetime, timedelta
from pathlib import Path

import scrape
from scrape import (TextWithLinks, build_reminders, dedupe_new, item_id,
                    make_record, normalize_date)


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
