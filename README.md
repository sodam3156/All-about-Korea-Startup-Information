# All-about-Korea-Startup-Information

세종 청년창업 기관 공지 · 정부 지원사업 공고 · 스타트업 뉴스를 **매일 14:00 KST에 자동 수집**하는 저장소.
GitHub Actions가 수집→중복제거→상세저장→아래 대시보드 갱신→텔레그램 브리핑까지 수행한다 (git-scraping — 서버·DB·API 비용 없음).

**완전 규칙 기반**: 소스마다 공식 API/RSS 또는 정규식 파서를 쓴다(LLM 미사용, 고정비 $0). 대신 사이트가 개편되면 파서가 조용히 0건을 낼 수 있어, 같은 소스가 **연속 2회 이상 0건**이면 `data/source_health.json`에 기록하고 다이제스트에 "⚠️ 소스 점검 필요"로 경고한다 — 이게 규칙 기반의 유일한 약점(개편에 안 깨지는 AI 추출 대비)을 메우는 피드백 루프다.

<!-- AUTO:START -->

_자동 갱신: 2026-10-30 (KST)_

## 마감 임박 지원사업

| 마감 | 공고 | 기관 | 출처 |
|---|---|---|---|
| 2026-10-30 | [뉴패러다임인베스트먼트 2026년 하반기 아기유니콘 성장 프로그램 기업모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179132) | (주)뉴패러다임인베스트먼트 | K-Startup 사업공고 |
| 2026-10-30 | [2026년 국가철도공단 창업·벤처기업 지원사업 희망기업 모집공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179209) | 국가철도공단 | K-Startup 사업공고 |
| 2026-10-30 | [취약분야 상시 컨설팅 10월 참가자 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179268) | 강동구 청년해냄센터 | K-Startup 사업공고 |
| 2026-10-30 | [한국기술교육대학교 오픈이노베이션 프로그램 참여기업 모집 안내(엠아이텍 재공고·아이티센글로벌 공고)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179374) | 한국기술교육대학교 앵커사업단 | K-Startup 사업공고 |
| 2026-10-30 | [2026년 스타 IR 데모데이 참여기업 모집공고(6차)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179419) | 스타에셋파트너스 주식회사 | K-Startup 사업공고 |
| 2026-10-30 | [2026년 전남광주 제3기「지역자원 연계 청년창업 지원사업」 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179500) | 전남정보문화산업진흥원 | K-Startup 사업공고 |
| 2026-10-30 | [2026년 석탄전환지역 기업이전 사업](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179491) | 강원대학교 KNU창업혁신원장 | K-Startup 사업공고 |
| 2026-10-30 | [2026 영등포구 라이브커머스 판로성장 프로그램](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179444) | 에이블브릿지 | K-Startup 사업공고 |
| 2026-10-30 | [2026 FAST TRACK 농식품 데모데이](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179602) | 씨엔티테크 | K-Startup 사업공고 |
| 2026-10-30 | [성남 중장년 기술창업센터 입주기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179607) | 성남산업진흥 | K-Startup 사업공고 |
| 2026-10-31 | [2026년 청주미래누리터(공공지식산업센터) 입주기업 모집공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179173) | (사)한국산업진흥협회 | K-Startup 사업공고 |
| 2026-10-31 | [2026년 하반기 벤처확인 도전기업 일대일 비대면 밋업 참여기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179301) | (주)엠비즈플래닛 산하 혁신기술경영인증지원센터 | K-Startup 사업공고 |
| 2026-10-31 | [해외진출 기업 대상 AI 통역 서비스 「아네스노트」 이용권 지원 (10월)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179351) | 주식회사 팀제로코드 | K-Startup 사업공고 |
| 2026-10-31 | [2026년 10월 초기 창업기업 대상 벤처기업 인증 행정자문&전략 수립 기업모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179392) | 박준범행정사사무소 | K-Startup 사업공고 |
| 2026-10-31 | [출연연, 대학 연구소기업 Business Development 프로그램 참여 예비창업자 모집 (10월)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179387) | 연구개발특구진흥재단 | K-Startup 사업공고 |
| 2026-10-31 | [2026 벤처확인 인증준비기업 맞춤형 무료 진단 지원사업](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179382) | (주)엠비즈플래닛 산하 혁신기술경영인증지원센터 | K-Startup 사업공고 |
| 2026-10-31 | [충북대학교 『글로벌(G)테크벤처센터(BI) 』 입주기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179478) | 충북대학교 글로벌(G)테크벤처센터 | K-Startup 사업공고 |
| 2026-10-31 | [2026년 특허출원·등록 비용 바우처 지원사업 15차(하반기 8차)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179470) | (사)한국중소기업발전협회 | K-Startup 사업공고 |
| 2026-10-31 | [2026 강원권 LIPS 민간운영사 연합 INVESTOR DAY 11월](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179450) | (재)강원창조경제혁신센터 | K-Startup 사업공고 |
| 2026-10-31 | [26년 10월 스타트업 언론 홍보 지원사업 참가사 모집 공고(2차)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179526) | 스타트업 데일리 | K-Startup 사업공고 |

## 스타트업 뉴스

| 날짜 | 제목 | 출처 |
|---|---|---|
| 2026-10-29 | [부산창조경제혁신센터, 11월 W-DAY 운영…AI 자동화부터 브랜드 성장까지](https://www.venturesquare.net/1124174/) | 벤처스퀘어 |
| 2026-10-29 | [KOSA, 뉴욕대 연계 AI 기업 미국 진출 프로그램 상시 접수…2027년 참가기업 사전 발굴](https://www.venturesquare.net/1124199/) | 벤처스퀘어 |
| 2026-10-29 | [SAP, 기업용 AI 에이전트 개발·운영 통합…업무 실행 중심 ‘쥴 워크’ 강화](https://www.venturesquare.net/1124208/) | 벤처스퀘어 |
| 2026-10-29 | [패스트파이브, 위탁운영으로 공유오피스 66개 지점 확대…연내 3곳 이상 추가](https://www.venturesquare.net/1124215/) | 벤처스퀘어 |
| 2026-10-29 | [알스퀘어디자인, AI 시대 오피스 변화 전망…고정 좌석보다 집중·협업 공간 중요해진다](https://www.venturesquare.net/1124217/) | 벤처스퀘어 |
| 2026-10-29 | [젠스파크, 스마트건설 AI 경연 후원…청년 기술인에 생성형 AI 교육·크레딧 지원](https://www.venturesquare.net/1124227/) | 벤처스퀘어 |
| 2026-10-29 | [터리낙스, 모발 성장 속도 측정 기술로 ‘2026 대한민국 우수특허 대상’ 수상](https://www.venturesquare.net/1124229/) | 벤처스퀘어 |
| 2026-10-29 | [메가존클라우드·KISTI, 슈퍼컴퓨터 ‘한강’과 양자컴퓨터 연계…산업별 양자 AI 활용 논의](https://www.venturesquare.net/1124241/) | 벤처스퀘어 |
| 2026-10-29 | [뉴로클, AI 비전검사 소프트웨어 5.0 출시…학습 시간 최대 79% 단축](https://www.venturesquare.net/1124250/) | 벤처스퀘어 |
| 2026-10-29 | [모인, NICE인프라와 ATM 해외송금 실증…앱 가입 없이 58개국 송금 지원](https://www.venturesquare.net/1124253/) | 벤처스퀘어 |
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
