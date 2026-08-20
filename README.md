# All-about-Korea-Startup-Information

세종 청년창업 기관 공지 · 정부 지원사업 공고 · 스타트업 뉴스를 **매일 14:00 KST에 자동 수집**하는 저장소.
GitHub Actions가 수집→중복제거→상세저장→아래 대시보드 갱신→텔레그램 브리핑까지 수행한다 (git-scraping — 서버·DB·API 비용 없음).

**완전 규칙 기반**: 소스마다 공식 API/RSS 또는 정규식 파서를 쓴다(LLM 미사용, 고정비 $0). 대신 사이트가 개편되면 파서가 조용히 0건을 낼 수 있어, 같은 소스가 **연속 2회 이상 0건**이면 `data/source_health.json`에 기록하고 다이제스트에 "⚠️ 소스 점검 필요"로 경고한다 — 이게 규칙 기반의 유일한 약점(개편에 안 깨지는 AI 추출 대비)을 메우는 피드백 루프다.

<!-- AUTO:START -->

_자동 갱신: 2026-08-20 (KST)_

## 마감 임박 지원사업

| 마감 | 공고 | 기관 | 출처 |
|---|---|---|---|
| 2026-08-20 | [2026년 28청춘창업소 액셀러레이팅 창업 역량강화교육](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178804) | 고양산업진흥원 | K-Startup 사업공고 |
| 2026-08-20 | [제 2회 판다밋업 : AI 반도체 글로벌 파트너십 Innovation Bridge](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178791) | 경기도 4차산업혁명센터 | K-Startup 사업공고 |
| 2026-08-20 | [[대전관광공사] 2026 대전·세종 관광 창업 역량강화교육 및 창업경진대회 참가자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178823) | 대전관광공사 | K-Startup 사업공고 |
| 2026-08-20 | [2026 예술기업 상생혁신(오픈이노베이션) 지원사업 참여기업 공모](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178857) | (재)예술경영지원센터 | K-Startup 사업공고 |
| 2026-08-20 | [2026년 제2회 사회서비스 투자 교류회 행사 및 참석자 모집 안내](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178908) | (주)엠와이소셜컴퍼니 | K-Startup 사업공고 |
| 2026-08-21 | [2026 KB스타터스 전문가 세미나](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178748) | 서울창조경제혁신센터 | K-Startup 사업공고 |
| 2026-08-21 | [2026년 재도전 아이디어 경진대회 참가자 모집 (~08.21)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178738) | (재)대전창조경제혁신센터  | K-Startup 사업공고 |
| 2026-08-21 | [[창원산업진흥원] CES2027 참가기업 지원사업 참가기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178679) | (재)창원산업진흥원장 | K-Startup 사업공고 |
| 2026-08-21 | [2026년 전주 로컬브랜딩 아이디어 해커톤 참가팀 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178675) | 전주시지역소통협력센터 | K-Startup 사업공고 |
| 2026-08-21 | [[숭실대학교 캠퍼스타운] 2026 숭실 스타트업 아카데미 8월 참여자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178666) | 숭실대학교 캠퍼스타운사업단 | K-Startup 사업공고 |
| 2026-08-21 | [2026년 28청춘창업소 액셀러레이팅 프로그램 전문가 멘토링 2차](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178815) | 고양산업진흥원 | K-Startup 사업공고 |
| 2026-08-21 | [2026 빅웨이브 글로벌(일본5차) - ILS2026 참여기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178794) | 인천창조경제혁신센터 대표이사 | K-Startup 사업공고 |
| 2026-08-21 | [중견기업 스타트업 동행라운지(참여 스타트업 모집)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178784) | 한국산업지능화협회  | K-Startup 사업공고 |
| 2026-08-21 | [2026년 하반기 DDP B the B(비더비) 뷰티테크·뷰티 디바이스 전시·체험 및 테스트베드 지원기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178775) | 재단법인 서울경제진흥원 | K-Startup 사업공고 |
| 2026-08-21 | [[인천] 2026년 IP창업존 50기 교육생 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178767) | 인천지식재산센터 | K-Startup 사업공고 |
| 2026-08-21 | [2026년 대전 스타트업 원스톱 지원센터 아카데미 1차](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178838) | 대전창조경제혁신센터 | K-Startup 사업공고 |
| 2026-08-21 | [[2026년 지역창업페스티벌 연계] 2026 스타트업 코리아 투자위크(SIW) 투자사, 유관기관, 스타트업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178826) | 대전창조경제혁신센터 | K-Startup 사업공고 |
| 2026-08-21 | [2026년 초기창업패키지 로켓십 IR 경진대회 참가기업 모집 (1회차: AI·빅데이터)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178824) | 씨엔티테크(주) | K-Startup 사업공고 |
| 2026-08-21 | [2026년 기술기반 창업 스케일업 지원 액셀러레이팅 프로그램 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178819) | (주)티비즈 | K-Startup 사업공고 |
| 2026-08-21 | [2026년 서울시 기후테크 3D프린팅 장비 활용 교육](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178813) | 서울기후테크산업지원센터장 | K-Startup 사업공고 |

## 스타트업 뉴스

| 날짜 | 제목 | 출처 |
|---|---|---|
| 2026-08-19 | [NFC 외길로 글로벌 기업의 문을 열다…박광범 쓰리에이로직스 대표의 23년 뚝심](https://www.venturesquare.net/1106614/) | 벤처스퀘어 |
| 2026-08-19 | [팁스 선정 베이직스킨랩, 약물전달 기술로 에포드 신제품 2종 개발](https://www.venturesquare.net/1107042/) | 벤처스퀘어 |
| 2026-08-19 | [디플리, 영국서 항만 설비의 ‘이상음’ 듣는다…리슨 AI 독점 판매 계약](https://www.venturesquare.net/1107051/) | 벤처스퀘어 |
| 2026-08-19 | [입 모양 넘어 감정·전신 동작까지…클레온, 휴먼 AI 인터페이스 기술 확장](https://www.venturesquare.net/1107058/) | 벤처스퀘어 |
| 2026-08-19 | [“서랍 속에 쌓이는 영양제 없게”…정지원 알고케어 대표가 ‘매일 먹게’ 만든 방법](https://www.venturesquare.net/1106429/) | 벤처스퀘어 |
| 2026-08-19 | [[VS현장] 보고서 쓰고, 물건 나르고, 공장 돌리고…‘일하는 AI’로 채워진 AI 서밋 서울 & 엑스포 2026 현장](https://www.venturesquare.net/1107030/) | 벤처스퀘어 |
| 2026-08-19 | [인도네시아 빌더 6명, 12주간 제품 개발…샤드랩 21일 발리서 성과 공개](https://www.venturesquare.net/1107078/) | 벤처스퀘어 |
| 2026-08-19 | [유이크, 성수 팝업서 쿨링패드 단독세트 공개…9월 무신사 뷰티 홍대점 입점](https://www.venturesquare.net/1107085/) | 벤처스퀘어 |
| 2026-08-19 | [집 고치는 동안 갈 곳 없지 않도록…삼삼엠투, 취약가정 임시주거 2년째 지원](https://www.venturesquare.net/1107092/) | 벤처스퀘어 |
| 2026-08-19 | [사우나 직후 10분을 스킨케어 루틴으로…로딕, 4단계 리커버리 리추얼 공개](https://www.venturesquare.net/1107099/) | 벤처스퀘어 |
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
