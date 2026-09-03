# All-about-Korea-Startup-Information

세종 청년창업 기관 공지 · 정부 지원사업 공고 · 스타트업 뉴스를 **매일 14:00 KST에 자동 수집**하는 저장소.
GitHub Actions가 수집→중복제거→상세저장→아래 대시보드 갱신→텔레그램 브리핑까지 수행한다 (git-scraping — 서버·DB·API 비용 없음).

**완전 규칙 기반**: 소스마다 공식 API/RSS 또는 정규식 파서를 쓴다(LLM 미사용, 고정비 $0). 대신 사이트가 개편되면 파서가 조용히 0건을 낼 수 있어, 같은 소스가 **연속 2회 이상 0건**이면 `data/source_health.json`에 기록하고 다이제스트에 "⚠️ 소스 점검 필요"로 경고한다 — 이게 규칙 기반의 유일한 약점(개편에 안 깨지는 AI 추출 대비)을 메우는 피드백 루프다.

<!-- AUTO:START -->

_자동 갱신: 2026-09-03 (KST)_

## 마감 임박 지원사업

| 마감 | 공고 | 기관 | 출처 |
|---|---|---|---|
| 2026-09-03 | [2026년 창업진흥원 정책 아이디어 공모전](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178709) | 창업진흥원 | K-Startup 사업공고 |
| 2026-09-03 | [[한국투자액셀러레이터] 바른동행 3차 모집｜선발 시 최대 5억원 투자](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178844) | 한국투자액셀러레이터 | K-Startup 사업공고 |
| 2026-09-03 | [2026년 지역 혁신 Start-up Demo Day](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178900) | 차세대융합기술연구원 | K-Startup 사업공고 |
| 2026-09-03 | [충북 제37기(26년 4기) IP창업존 특화과정((예비)창업자 및 「모두의 창업」선정자 대상) 교육생 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178888) | 충북지식재산센터장 | K-Startup 사업공고 |
| 2026-09-03 | [[도봉구 청년창업센터] 2026 도봉 청년창업 아이디어 경진대회 참가자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178914) | 도봉구 청년창업센터장 | K-Startup 사업공고 |
| 2026-09-03 | [2026년 Tokyo PMF·GTM 프로그램 창업기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178953) | 창업진흥원장 | K-Startup 사업공고 |
| 2026-09-03 | [2026년 서울지식재산센터 소상공인 지식재산 인식제고 & 창업 교육 안내 (9/3, 9/11)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179034) | 서울경제진흥원 | K-Startup 사업공고 |
| 2026-09-03 | [2026 이화여대 모두의 창업 2기 프로젝트 사업설명회](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179016) | 이화여자대학교  창업지원단 | K-Startup 사업공고 |
| 2026-09-03 | [[추가모집] 2026 창업경진대회 모의투자자 모집(~9.3. 14:00)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179065) | 강북청년창업마루 | K-Startup 사업공고 |
| 2026-09-04 | [2026년 라이브커머스 플랫폼을 활용한 쇼호스트 교육생 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178766) | 경기도경제과학진흥원 | K-Startup 사업공고 |
| 2026-09-04 | [2026년 광주 IP(지식재산)디딤돌 IP창업존 62기(26년 4기) 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178913) | 한국발명진흥회 광주지부(광주지식재산센터) | K-Startup 사업공고 |
| 2026-09-04 | [[광운대학교] 『모두의 창업 프로젝트 2기』지역별 사업 설명회 통합 안내](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178911) | 광운대학교 NCI창업패키지사업단 | K-Startup 사업공고 |
| 2026-09-04 | [2026년도 딥테크 특화 창업중심대학 추천형 창업기업 모집공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178985) | 중소벤처기업부 | K-Startup 사업공고 |
| 2026-09-04 | [2026년 서울창업허브 창동 투자 특화 프로그램 - IR 라운드(2회차)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178965) | 서울창업허브 창동 | K-Startup 사업공고 |
| 2026-09-04 | [(~ 9/4 마감) 2026년도 재도전응원본부 재창업 특화교육ㆍ컨설팅 프로그램 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179013) | 중소벤처기업진흥공단 | K-Startup 사업공고 |
| 2026-09-04 | [2026년 한전KPS 창업벤처기업 육성 지원사업 참여기업 모집안내](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179062) | 한국전기산업진흥회 에너지밸리기업개발원 | K-Startup 사업공고 |
| 2026-09-04 | [[인천대학교] 모두의창업 프로젝트(2차) 모집홍보 교육 『AI와 함께하는 BM 스쿨』](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179053) | 인천대학교 | K-Startup 사업공고 |
| 2026-09-04 | [BOUNCE 2026 글로벌 오피스아워 참여 스타트업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179051) | (재)부산창조경제혁신센터 | K-Startup 사업공고 |
| 2026-09-04 | [2026년 서울지식재산센터 IP디딤돌 IP창업존 33기 교육생 모집(2026년 2차)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179107) | 재단법인 서울경제진흥원 | K-Startup 사업공고 |
| 2026-09-06 | [[2026-059호] 2026 세종국제만화영상전(SICACO) 모집 공고](https://sjtp.or.kr/bbs/board.php?bo_table=business01&wr_id=1985) | 세종테크노파크 | 세종테크노파크 사업공고 |

## 스타트업 뉴스

| 날짜 | 제목 | 출처 |
|---|---|---|
| 2026-09-02 | [경남 창업기업 20곳에 영상·제품사진…G-Space@East, 맞춤 제작 지원](https://www.venturesquare.net/1110445/) | 벤처스퀘어 |
| 2026-09-02 | [2027년 TIPS 도전할 소셜벤처 찾는다…큐네스티, IR 데모데이 참가 모집](https://www.venturesquare.net/1110455/) | 벤처스퀘어 |
| 2026-09-02 | [크리에이터의 창업 전환 돕는다…크리에이터벤처스튜디오, ‘크벤스 AI’ 공개](https://www.venturesquare.net/1110458/) | 벤처스퀘어 |
| 2026-09-02 | [생성형 AI는 쓰되 민감정보는 막는다…야타브, 제1금융권에 ‘AI-DLP’ 구축](https://www.venturesquare.net/1110469/) | 벤처스퀘어 |
| 2026-09-02 | [손 전체 접촉 데이터 읽는다…원익로보틱스, 5지 로봇핸드 ‘V6 F’ 출시](https://www.venturesquare.net/1110498/) | 벤처스퀘어 |
| 2026-09-02 | [“컵을 쏟는 순간까지 모은다”… 엑스와이지 황성재 대표가 노리는 정제되지 않은 현장 데이터](https://www.venturesquare.net/1109612/) | 벤처스퀘어 |
| 2026-09-03 | [고객 문제 해결해야 과금…세일즈포스가 꺼낸 ‘에이전틱 컨택센터’](https://www.venturesquare.net/1110517/) | 벤처스퀘어 |
| 2026-09-03 | [제주 분산에너지, ESS·EV·AI로 해법 찾는다…리드투랩 세미나 개최](https://www.venturesquare.net/1110520/) | 벤처스퀘어 |
| 2026-09-03 | [데이터는 알스퀘어, 현장은 예원…베트남 리모델링 시장 공동 공략한다](https://www.venturesquare.net/1110531/) | 벤처스퀘어 |
| 2026-09-03 | [코스닥 3곳·직접 창업 4곳…민트벤처파트너스, 투자와 벤처스튜디오 병행](https://www.venturesquare.net/1110541/) | 벤처스퀘어 |
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
| `TELEGRAM_BOT_TOKEN` / `TELEGRAM_CHAT_ID` | 일일 브리핑 발송 (@BotFather로 봇 생성, 무료) | 텔레그램 미발송 |
| `DISCORD_WEBHOOK_URL` | 일일 브리핑 발송 (채널 설정 → 연동 → 웹후크, 무료) | 디스코드 미발송 |

텔레그램·디스코드 중 하나만 설정해도 되고 둘 다 설정하면 둘 다로 온다. 둘 다 없으면 Actions 로그에만 출력.

## 소스 추가

`scrape.py`의 `SOURCES`에 한 줄 + `FETCHERS`에 대응하는 `fetch_*(source)` 함수 하나. 공식 API/RSS가 있으면 그걸 쓰고, 없으면 정규식으로 목록을 파싱한다(예: `fetch_sjtp_board`). 새 파서를 붙이면 사이트가 개편됐을 때도 `source_health.json`이 자동으로 잡아준다 — 별도 모니터링 코드 불필요.

로컬 실행: `pip install -r requirements.txt && python scrape.py` / 자체 점검: `python test_scrape.py`
