# All-about-Korea-Startup-Information

세종 청년창업 기관 공지 · 정부 지원사업 공고 · 스타트업 뉴스를 **매일 14:00 KST에 자동 수집**하는 저장소.
GitHub Actions가 수집→중복제거→상세저장→아래 대시보드 갱신→텔레그램 브리핑까지 수행한다 (git-scraping — 서버·DB·API 비용 없음).

**완전 규칙 기반**: 소스마다 공식 API/RSS 또는 정규식 파서를 쓴다(LLM 미사용, 고정비 $0). 대신 사이트가 개편되면 파서가 조용히 0건을 낼 수 있어, 같은 소스가 **연속 2회 이상 0건**이면 `data/source_health.json`에 기록하고 다이제스트에 "⚠️ 소스 점검 필요"로 경고한다 — 이게 규칙 기반의 유일한 약점(개편에 안 깨지는 AI 추출 대비)을 메우는 피드백 루프다.

<!-- AUTO:START -->

_자동 갱신: 2026-08-19 (KST)_

## 마감 임박 지원사업

| 마감 | 공고 | 기관 | 출처 |
|---|---|---|---|
| 2026-08-19 | [[글로벌] 2026 BIOHEALTH GLOBAL BRIDGE : JOHNS HOPKINS / HIKMA 프로그램 참가기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178743) | 서울창조경제혁신센터 | K-Startup 사업공고 |
| 2026-08-19 | [2026년 여성CEO 비즈니스 아카데미 서울권역 시즌 2](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178741) | 한국여성경제인협회 | K-Startup 사업공고 |
| 2026-08-19 | [2026년 제3차 창업지원센터 입주기업 모집공고(~8/19, 수 16시까지)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178708) | 용인시산업진흥원 | K-Startup 사업공고 |
| 2026-08-19 | [[서초창업스테이션] 서리풀 소상공인 창업 클리닉(8월) - 소상공인 1:1 컨설팅](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178690) | 서초창업스테이션 | K-Startup 사업공고 |
| 2026-08-19 | [경기 서부권 기술사업화 세미나](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178670) | 가톨릭대학교 | K-Startup 사업공고 |
| 2026-08-19 | [구로구 청년창업지원센터 일반 창업교육(반기: 1회차): 정부지원사업 효율적인 활용 방법](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178769) | 구로구 청년창업지원센터 | K-Startup 사업공고 |
| 2026-08-19 | [Se7en on the table 전문가 멘토링 프로그램 참가기업 모집 (~08.19)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178837) | 서강대학교 판교캠퍼스사업단 | K-Startup 사업공고 |
| 2026-08-19 | [「2026년 로봇 기반 공간컴퓨팅 창업지원사업」예비창업자(팀) 모집 추가공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178833) | (재)대구테크노파크 | K-Startup 사업공고 |
| 2026-08-19 | [[킹고스프링] KINGO LIPS SPRINGBOARD PROGRAM 5기 모집공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178859) | 주식회사 킹고스프링 | K-Startup 사업공고 |
| 2026-08-19 | [2026 YUnicorn 지역정주형 창업스쿨 참여자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178889) | 영남대학교 YUnicorn창업지원단 | K-Startup 사업공고 |
| 2026-08-19 | [2026년 8월 크립톤 IR피칭 & 오피스아워 신청 접수](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178907) | 크립톤 부산센터 | K-Startup 사업공고 |
| 2026-08-19 | [2026 KU AI Nest AI 창업 실전 교육 프로그램](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178895) | 건국대학교 | K-Startup 사업공고 |
| 2026-08-20 | [2026년 28청춘창업소 액셀러레이팅 창업 역량강화교육](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178804) | 고양산업진흥원 | K-Startup 사업공고 |
| 2026-08-20 | [제 2회 판다밋업 : AI 반도체 글로벌 파트너십 Innovation Bridge](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178791) | 경기도 4차산업혁명센터 | K-Startup 사업공고 |
| 2026-08-20 | [[대전관광공사] 2026 대전·세종 관광 창업 역량강화교육 및 창업경진대회 참가자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178823) | 대전관광공사 | K-Startup 사업공고 |
| 2026-08-20 | [2026 예술기업 상생혁신(오픈이노베이션) 지원사업 참여기업 공모](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178857) | (재)예술경영지원센터 | K-Startup 사업공고 |
| 2026-08-20 | [2026년 제2회 사회서비스 투자 교류회 행사 및 참석자 모집 안내](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178908) | (주)엠와이소셜컴퍼니 | K-Startup 사업공고 |
| 2026-08-21 | [2026 KB스타터스 전문가 세미나](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178748) | 서울창조경제혁신센터 | K-Startup 사업공고 |
| 2026-08-21 | [2026년 재도전 아이디어 경진대회 참가자 모집 (~08.21)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178738) | (재)대전창조경제혁신센터  | K-Startup 사업공고 |
| 2026-08-21 | [[창원산업진흥원] CES2027 참가기업 지원사업 참가기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178679) | (재)창원산업진흥원장 | K-Startup 사업공고 |

## 스타트업 뉴스

| 날짜 | 제목 | 출처 |
|---|---|---|
| 2026-08-18 | [알리바바 클라우드, 국내 세 번째 데이터센터 열었다…승부수는 ‘AI 풀스택’](https://www.venturesquare.net/1106663/) | 벤처스퀘어 |
| 2026-08-18 | [중기부, AI 서비스 혁신기업 175곳 선정…수산물 가격·간병·화재 위험 예측한다](https://www.venturesquare.net/1106764/) | 벤처스퀘어 |
| 2026-08-18 | [글로벌 팁스 선정 딥인사이트, 현실 공간을 AI 학습 데이터로 바꾼다](https://www.venturesquare.net/1106800/) | 벤처스퀘어 |
| 2026-08-18 | [드라마 ‘협상의 기술’ 현실판 주인공…13억달러 M&A 딜메이커, 우앤파트너스 우준호 대표](https://www.venturesquare.net/1106807/) | 벤처스퀘어 |
| 2026-08-18 | [한국어·운전면허·직무교육 한곳에…위픽코퍼레이션, 외국인 정착 교육 연결한다](https://www.venturesquare.net/1106823/) | 벤처스퀘어 |
| 2026-08-18 | [800만 이용자 유심사, 고윤정 새 얼굴로…통신·이동 묶은 여행 서비스 재정비](https://www.venturesquare.net/1106830/) | 벤처스퀘어 |
| 2026-08-18 | [자동차 공장에서 물류센터로…클레로보틱스, AI 빈피킹에 62억원 투입](https://www.venturesquare.net/1106837/) | 벤처스퀘어 |
| 2026-08-18 | [규칙은 시스템에, 추론은 LLM에…신한투자증권이 설계한 금융 AI 에이전트](https://www.venturesquare.net/1106840/) | 벤처스퀘어 |
| 2026-08-18 | [1억2000만회 웹툰 작가가 세운 IP 스튜디오…크릿벤처스, 엑스텐스튜디오 투자](https://www.venturesquare.net/1106847/) | 벤처스퀘어 |
| 2026-08-18 | [조달 60일에서 10일 이내로…리벨리온 ATOM-Max, 혁신제품 지정](https://www.venturesquare.net/1106855/) | 벤처스퀘어 |
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
