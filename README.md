# All-about-Korea-Startup-Information

세종 청년창업 기관 공지 · 정부 지원사업 공고 · 스타트업 뉴스를 **매일 07:00 KST에 자동 수집**하는 저장소.
GitHub Actions가 수집→중복제거→상세저장→아래 대시보드 갱신→텔레그램 브리핑까지 수행한다 (git-scraping — 서버·DB·API 비용 없음).

**완전 규칙 기반**: 소스마다 공식 API/RSS 또는 정규식 파서를 쓴다(LLM 미사용, 고정비 $0). 대신 사이트가 개편되면 파서가 조용히 0건을 낼 수 있어, 같은 소스가 **연속 2회 이상 0건**이면 `data/source_health.json`에 기록하고 다이제스트에 "⚠️ 소스 점검 필요"로 경고한다 — 이게 규칙 기반의 유일한 약점(개편에 안 깨지는 AI 추출 대비)을 메우는 피드백 루프다.

<!-- AUTO:START -->

_자동 갱신: 2026-08-05 (KST)_

## 마감 임박 지원사업

| 마감 | 공고 | 기관 | 출처 |
|---|---|---|---|
| 2026-08-07 | [[2026-061호] 2026년 세종테크노파크 본관동 입주기업 비즈니스 고도화 지원 프로그램 참여기업 모집 2차 공고](https://sjtp.or.kr/bbs/board.php?bo_table=business01&wr_id=1988) | 세종테크노파크 | 세종테크노파크 사업공고 |
| 2026-08-10 | [[2026-060호]2026년 세종 지역특화 프로젝트 레전드50+2.0 기업진단 및 컨설팅 참여기업 모집](https://sjtp.or.kr/bbs/board.php?bo_table=business01&wr_id=1987) | (재)세종테크노파크 | 세종테크노파크 사업공고 |
| 2026-08-14 | [[2026-063호] 2026년 정보보호 기업육성(사업화) 지원사업 모집공고](https://sjtp.or.kr/bbs/board.php?bo_table=business01&wr_id=1989) | (재)세종테크노파크 | 세종테크노파크 사업공고 |
| 2026-08-14 | [[2026-064호] 세종 지역특화산업 기업 정보보호 신규 비즈니스 모델 전략 수립 지원기업 모집공고](https://sjtp.or.kr/bbs/board.php?bo_table=business01&wr_id=1990) | (재)세종테크노파크 | 세종테크노파크 사업공고 |
| 2026-08-28 | [[2026-047호] 2026년 디지털 콘텐츠 산업 규제개혁 어드바이저 참여기업 모집 공고](https://sjtp.or.kr/bbs/board.php?bo_table=business01&wr_id=1972) | 정보통신산업진흥원 | 세종테크노파크 사업공고 |
| 2026-09-06 | [[2026-059호] 2026 세종국제만화영상전(SICACO) 모집 공고](https://sjtp.or.kr/bbs/board.php?bo_table=business01&wr_id=1985) | 세종테크노파크 | 세종테크노파크 사업공고 |
| 2026-12-31 | [창업-BuS in 세종, 수요투자 라운드 참여기업 모집](https://ccei.creativekorea.or.kr/sejong/service/program_view.do?no=10434&sMenuType=00040001&cntry_nm=sejong) | 세종창조경제혁신센터 지원프로그램 | 세종창조경제혁신센터 지원프로그램 |
| 2026-12-31 | [대국민 창업 오디션「모두의 창업」](https://ccei.creativekorea.or.kr/sejong/service/program_view.do?no=10358&sMenuType=00040001&cntry_nm=sejong) | 세종창조경제혁신센터 지원프로그램 | 세종창조경제혁신센터 지원프로그램 |
| 2026-12-31 | [세종 스타트업 원스톱 지원센터] 2025년 12월 창업 상담 예약 신청 안내](https://ccei.creativekorea.or.kr/sejong/service/program_view.do?no=10228&sMenuType=00040001&cntry_nm=sejong) | 세종창조경제혁신센터 지원프로그램 | 세종창조경제혁신센터 지원프로그램 |
| 2026-12-31 | [[2026-003호] 2026년도 세종테크노파크 본관동 입주기업 상시모집 공고](https://sjtp.or.kr/bbs/board.php?bo_table=business01&wr_id=1928) | 세종테크노파크 | 세종테크노파크 사업공고 |
| 2026-12-31 | [2026년 세종RISE센터 분야별 전문가 모집 공고](https://sjtp.or.kr/bbs/board.php?bo_table=business01&wr_id=1936) | (재)세종테크노파크 세종RISE센터 | 세종테크노파크 사업공고 |
| 2026-12-31 | [[2026-020호] 2026년 기술닥터제 지원사업 참여기업 모집공고](https://sjtp.or.kr/bbs/board.php?bo_table=business01&wr_id=1942) | (재)세종테크노파크 | 세종테크노파크 사업공고 |
| 2026-12-31 | [[2026-049호] 세종테크밸리 첨단기업 유치 임차료 지원사업 참여기업(임차기업) 모집 수정 공고](https://sjtp.or.kr/bbs/board.php?bo_table=business01&wr_id=1974) | 세종특별자치시 | 세종테크노파크 사업공고 |

## 스타트업 뉴스

| 날짜 | 제목 | 출처 |
|---|---|---|
| 2026-08-04 | [코스포 10년, 스타트업의 발자취 담는다…다음 10년 향한 캠페인 본격화](https://www.venturesquare.net/1103559/) | 벤처스퀘어 |
| 2026-08-04 | [K-자율주행, 중동 첫 대형 수출…에이투지, UAE에 110억 원 공급 계약](https://www.venturesquare.net/1103567/) | 벤처스퀘어 |
| 2026-08-04 | [토스 최연소 PO가 다시 창업했다…AI 광고 스타트업 ‘애딧앤아크’ 시드 투자 유치](https://www.venturesquare.net/1103574/) | 벤처스퀘어 |
| 2026-08-04 | [건물 데이터에서 설비 데이터까지…알스퀘어 RA, 영업 플랫폼으로 진화](https://www.venturesquare.net/1103577/) | 벤처스퀘어 |
| 2026-08-04 | [조선소 용접 로봇에도 피지컬 AI…마키나락스, HD한국조선해양과 이상탐지 실증](https://www.venturesquare.net/1103588/) | 벤처스퀘어 |
| 2026-08-04 | [맥스서밋 2026 성료…AI 시대 마케팅의 마지막 경쟁력은 ‘축적된 자산’](https://www.venturesquare.net/1103478/) | 벤처스퀘어 |
| 2026-08-05 | [잠드는 순간 산리오와 여행 시작…허슬러즈, 게임형 수면 앱 한·일 동시 출시](https://www.venturesquare.net/1103625/) | 벤처스퀘어 |
| 2026-08-05 | [AI 통번역 입은 올리브영…플리토, 외국인 쇼핑 경험 바꾼다](https://www.venturesquare.net/1103633/) | 벤처스퀘어 |
| 2026-08-05 | [AI 마케팅·펨테크에 베팅…씨엔티테크, 시그마인·이사벨라 시드 투자](https://www.venturesquare.net/1103636/) | 벤처스퀘어 |
| 2026-08-05 | [딜, ARR 15억달러 돌파…AI 보안 기업 인수로 글로벌 HR 플랫폼 경쟁력 강화](https://www.venturesquare.net/1103648/) | 벤처스퀘어 |
<!-- AUTO:END -->

## 데이터 구조

| 파일 | 내용 |
|---|---|
| `data/items.jsonl` | 수집된 전체 목록. 1줄 = 공고 1건: `{id, source, category(지원사업\|공지\|뉴스\|행사), title, url, org, posted, deadline, detail, scraped_at}` |
| `data/details/{id}.md` | 지원사업·공지의 상세 페이지 원문(자동 추출, 미가공 텍스트 — 첨부파일 링크 포함) — **지원서 작성 재료** |
| `data/status.jsonl` | 공고별 진행 상태. append-only, **id별 마지막 줄이 유효**: `{id, status(검토\|지원예정\|초안\|제출\|선정\|탈락), memo, updated_at}` |
| `data/source_health.json` | 소스별 연속 0건 스트릭. `{"소스명": {"streak": N, "last_ok": "..."}}` — N≥2면 다이제스트에 경고 |

## 에이전트(헤르메스) 연동

공개 저장소라 인증 없이 raw URL로 읽는다:

```
목록:   https://raw.githubusercontent.com/sodam3156/All-about-Korea-Startup-Information/main/data/items.jsonl
상세:   https://raw.githubusercontent.com/sodam3156/All-about-Korea-Startup-Information/main/data/details/{id}.md
상태:   https://raw.githubusercontent.com/sodam3156/All-about-Korea-Startup-Information/main/data/status.jsonl
```

**"이 공고 지원서 써줘" 흐름**: items.jsonl에서 공고 선택 → `detail` 경로의 md(원문 그대로, 미가공)를 읽고 헤르메스가 직접 정리해 초안 작성 → status.jsonl에 `{"id":"...","status":"초안","memo":"...","updated_at":"..."}` 한 줄 append 후 push (또는 GitHub Contents API PUT). 사람이 GitHub 웹에서 직접 편집해도 된다.

상태를 기록해두면 다음 날 브리핑이 **마감 D-7 이내 진행 중 공고를 자동 리마인드**한다.

## 설정 (저장소 Settings → Secrets and variables → Actions)

전부 **선택**이다 — 아무것도 등록하지 않아도 K-Startup을 뺀 나머지 소스는 정상 수집되고 브리핑은 Actions 로그에 출력된다. 유료 API 키는 어디에도 없다.

| Secret | 용도 | 없으면 |
|---|---|---|
| `DATA_GO_KR_KEY` | [공공데이터포털](https://www.data.go.kr) "K-Startup 조회서비스" 활용신청(무료) 후 발급되는 서비스키 | K-Startup 소스만 스킵 |
| `TELEGRAM_BOT_TOKEN` / `TELEGRAM_CHAT_ID` | 일일 브리핑 발송 (@BotFather로 봇 생성, 무료) | 브리핑을 Actions 로그에만 출력 |

## 소스 추가

`scrape.py`의 `SOURCES`에 한 줄 + `FETCHERS`에 대응하는 `fetch_*(source)` 함수 하나. 공식 API/RSS가 있으면 그걸 쓰고, 없으면 정규식으로 목록을 파싱한다(예: `fetch_sjtp_board`). 새 파서를 붙이면 사이트가 개편됐을 때도 `source_health.json`이 자동으로 잡아준다 — 별도 모니터링 코드 불필요.

로컬 실행: `pip install -r requirements.txt && python scrape.py` / 자체 점검: `python test_scrape.py`
