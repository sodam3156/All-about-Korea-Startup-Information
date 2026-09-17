# All-about-Korea-Startup-Information

세종 청년창업 기관 공지 · 정부 지원사업 공고 · 스타트업 뉴스를 **매일 14:00 KST에 자동 수집**하는 저장소.
GitHub Actions가 수집→중복제거→상세저장→아래 대시보드 갱신→텔레그램 브리핑까지 수행한다 (git-scraping — 서버·DB·API 비용 없음).

**완전 규칙 기반**: 소스마다 공식 API/RSS 또는 정규식 파서를 쓴다(LLM 미사용, 고정비 $0). 대신 사이트가 개편되면 파서가 조용히 0건을 낼 수 있어, 같은 소스가 **연속 2회 이상 0건**이면 `data/source_health.json`에 기록하고 다이제스트에 "⚠️ 소스 점검 필요"로 경고한다 — 이게 규칙 기반의 유일한 약점(개편에 안 깨지는 AI 추출 대비)을 메우는 피드백 루프다.

<!-- AUTO:START -->

_자동 갱신: 2026-09-17 (KST)_

## 마감 임박 지원사업

| 마감 | 공고 | 기관 | 출처 |
|---|---|---|---|
| 2026-09-17 | [2026년 제대군인 창업 경진대회 참가자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178931) | 국가보훈부 | K-Startup 사업공고 |
| 2026-09-17 | [「모두의 창업 프로젝트」통합 모집공고 2차](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178952) | 중소벤처기업부 | K-Startup 사업공고 |
| 2026-09-17 | [「2026 투자유치 프로그램: 멘토링」참가기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179064) | 수원도시재단 | K-Startup 사업공고 |
| 2026-09-17 | [[용인시산업진흥원] 2026년 용인 오픈이노베이션 교류회 4회차(AI)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179099) | 알파브라더스 | K-Startup 사업공고 |
| 2026-09-17 | [[부산울산경남센터] 사회적협동조합 설립인가 및 경영공시 교육 안내 (9.16.(수), 9.17.(목) - 온라인병행)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179083) | 한국사회적기업진흥원 부산울산경남센터 | K-Startup 사업공고 |
| 2026-09-17 | [2026년 웰컴 투 팁스 3차 참가기업 모집 (동남권)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179126) | (주)로우파트너스 | K-Startup 사업공고 |
| 2026-09-17 | [2026 서울창업허브 공덕 9월 허브아워 - 투자, 수출 컨설팅](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179152) | (재)서울경제진흥원 | K-Startup 사업공고 |
| 2026-09-17 | [2026년 SVC Seoul 인턴십 프로그램 학생인턴 모집공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179200) | 창업진흥원 | K-Startup 사업공고 |
| 2026-09-17 | [[서초창업스테이션] 9월 1:1 전문 분야 컨설팅 - IR 덱 디자인 고도화, 세무회계](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179169) | 서초창업스테이션 | K-Startup 사업공고 |
| 2026-09-17 | [베트남 테크페스트(TECHFEST 2026) K-스타트업 통합관 참가기업 모집공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179192) | 창업진흥원장 | K-Startup 사업공고 |
| 2026-09-18 | [[숭실대학교 캠퍼스타운] 2026 숭실 스타트업 아카데미 9월 참여자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178890) | 숭실대학교 캠퍼스타운사업단 | K-Startup 사업공고 |
| 2026-09-18 | [2026년 하반기 벤처확인 도전기업 일대일 비대면 밋업 참여기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178947) | (주)엠비즈플래닛 산하 혁신기술경영인증지원센터 | K-Startup 사업공고 |
| 2026-09-18 | [2026년 안산정보산업진흥센터(경기TP안산창업보육센터) 제3차 신규 입주자 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179172) | (재)경기테크노파크 | K-Startup 사업공고 |
| 2026-09-18 | [2026 서울AI로봇쇼 피지컬 AI 포럼 참관객 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179158) | (재)서울경제진흥원 | K-Startup 사업공고 |
| 2026-09-18 | [성남 기후테크 UpSkill 아카데미 Vol.2 - 비즈니스모델 개발과 기술사업화](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179125) | 도시혁신그룹 무브먼트 주식회사 | K-Startup 사업공고 |
| 2026-09-18 | [로컬임팩트는 왜 확장되지 않는가? | 신한금융희망재단 × 제3회 대한민국 사회적가치 페스타](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179176) | 신한금융희망재단 | K-Startup 사업공고 |
| 2026-09-18 | [[서초창업스테이션] 9월 창업 교육 - 스타트업을 위한 온라인 판로개척](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179167) | 서초창업스테이션 | K-Startup 사업공고 |
| 2026-09-18 | [2026년 재도전 마인드업(힐링캠프) 참여자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179260) | 중소벤처기업진흥공단 | K-Startup 사업공고 |
| 2026-09-18 | [창업·벤처 녹색융합클러스터 그린아이디어랩(비상주오피스) 청년 이용자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179235) | 한국환경산업기술원 | K-Startup 사업공고 |
| 2026-09-20 | [[환경재단] 2027 어스샷 상 혁신 환경 솔루션 공모](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178997) | 환경재단 | K-Startup 사업공고 |

## 스타트업 뉴스

| 날짜 | 제목 | 출처 |
|---|---|---|
| 2026-09-16 | [인핸스, 512억원 시리즈C 유치…고객사였던 LG·포스코·롯데 계열사 주주로](https://www.venturesquare.net/1114540/) | 벤처스퀘어 |
| 2026-09-16 | [킵코퍼레이션 이뿌다, 샤오홍슈·더우인 타고 중국 공략…현지 MCN Yisong과 맞손](https://www.venturesquare.net/1114547/) | 벤처스퀘어 |
| 2026-09-16 | [리필드, 약국 다음은 창고형 할인점…트레이더스 전국 24개점 입점](https://www.venturesquare.net/1114550/) | 벤처스퀘어 |
| 2026-09-16 | [어니스트AI, 같은 리스크에 대출 승인율 18%p 높인다…카카오페이와 특판 대출](https://www.venturesquare.net/1114558/) | 벤처스퀘어 |
| 2026-09-16 | [경기콘텐츠진흥원, 블록 조립으로 시니어 인지훈련…부천서 8주 Re·Build 실증](https://www.venturesquare.net/1114565/) | 벤처스퀘어 |
| 2026-09-16 | [로켓툴즈, AI 어디에 쓸지부터 찾는다…이커머스 브랜드 AX 컨설팅 출시](https://www.venturesquare.net/1114577/) | 벤처스퀘어 |
| 2026-09-17 | [크라우드웍스, 피지컬 AI 시대 어떤 인재 뽑나…VLA 데이터 직무 취업 전략 공유](https://www.venturesquare.net/1114584/) | 벤처스퀘어 |
| 2026-09-17 | [캐치테이블, 야장 검색 10.7배 뛰었다…을지로 넘어 제주·성수·정자로](https://www.venturesquare.net/1114587/) | 벤처스퀘어 |
| 2026-09-17 | [경기혁신센터, 대·중견기업 11곳이 찾는 기술부터 물었다…스타트업 26곳 정밀 매칭](https://www.venturesquare.net/1114598/) | 벤처스퀘어 |
| 2026-09-17 | [그로우매치, 우리 아이 어떤 치료가 맞을까…AI로 발달치료사 1만5960명 매칭](https://www.venturesquare.net/1114601/) | 벤처스퀘어 |
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
