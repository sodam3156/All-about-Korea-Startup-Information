# All-about-Korea-Startup-Information

세종 청년창업 기관 공지 · 정부 지원사업 공고 · 스타트업 뉴스를 **매일 14:00 KST에 자동 수집**하는 저장소.
GitHub Actions가 수집→중복제거→상세저장→아래 대시보드 갱신→텔레그램 브리핑까지 수행한다 (git-scraping — 서버·DB·API 비용 없음).

**완전 규칙 기반**: 소스마다 공식 API/RSS 또는 정규식 파서를 쓴다(LLM 미사용, 고정비 $0). 대신 사이트가 개편되면 파서가 조용히 0건을 낼 수 있어, 같은 소스가 **연속 2회 이상 0건**이면 `data/source_health.json`에 기록하고 다이제스트에 "⚠️ 소스 점검 필요"로 경고한다 — 이게 규칙 기반의 유일한 약점(개편에 안 깨지는 AI 추출 대비)을 메우는 피드백 루프다.

<!-- AUTO:START -->

_자동 갱신: 2026-10-23 (KST)_

## 마감 임박 지원사업

| 마감 | 공고 | 기관 | 출처 |
|---|---|---|---|
| 2026-10-23 | [2026년 스마트 혁신가전 유공자 포상 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179307) | 한국전자정보통신산업진흥회 | K-Startup 사업공고 |
| 2026-10-23 | [2026년 제2차 대전센터 여성BI 입주기업 모집공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179338) | (재)여성기업종합지원센터 대전센터장 | K-Startup 사업공고 |
| 2026-10-23 | [2026년 하반기 남동구 청년창업지원센터 입주기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179411) | 남동구 청년창업지원센터 | K-Startup 사업공고 |
| 2026-10-23 | [2026년 위치정보 보호조치 교육 (6차)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179393) |  (주)아이전스 | K-Startup 사업공고 |
| 2026-10-23 | [[ 칠곡군 중장년 기술창업센터]제3차 Pre-인큐베이팅 창업교육 수강생 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179381) | 칠곡군중장년기술창업센터 | K-Startup 사업공고 |
| 2026-10-23 | [경기창업혁신공간 서부권 「스담스담」(오픈 네트워킹) 3회차](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179416) | 경기도경제과학진흥원 | K-Startup 사업공고 |
| 2026-10-23 | [[서초창업스테이션] 10월 1:1 전문 분야 컨설팅 - 지식재산권/특허 전략, 브랜딩 전략](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179434) | 서초창업스테이션 | K-Startup 사업공고 |
| 2026-10-23 | [2027년 K-water 해외시장개척단 참여기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179477) | K-water 기후테크혁신처장 | K-Startup 사업공고 |
| 2026-10-23 | [2026년 초기창업패키지 로켓십 IR 경진대회 참가기업 모집 (3회차: 기후·ESG)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179474) | 씨엔티테크(주) | K-Startup 사업공고 |
| 2026-10-23 | [2026 산업단지 오픈이노베이션프로그램 KICXUP 챌린지 & 로컬 스타트업 2차 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179496) | 한국산업단지공단 | K-Startup 사업공고 |
| 2026-10-23 | [2026년 나주형 청년 에너지 창업 사관학교(직·주·락·비) 사업 1차 수행기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179519) |  (재)전남테크노파크 | K-Startup 사업공고 |
| 2026-10-23 | [[서울과학기술대학교] SLA3D프린터 장비교육](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179518) | 서울과학기술대학교 | K-Startup 사업공고 |
| 2026-10-23 | [2026-9회 충청권 엔젤투자 피칭룸 프로그램 참가기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179516) | (사)한국엔젤투자협회 충청권 엔젤투자허브 | K-Startup 사업공고 |
| 2026-10-23 | [[광운대캠퍼스타운] AI+X Connect Forum](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179505) | 광운대학교 캠퍼스타운 | K-Startup 사업공고 |
| 2026-10-23 | [Tech Discovery 실험실창업 경진대회 참가자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179483) | 주식회사 단국대학교 기술지주회사 | K-Startup 사업공고 |
| 2026-10-23 | [2026년 G-Bridge 레전드 액셀러레이팅 패키지 프로그램](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179467) | 대구대학교 앵커사업단 | K-Startup 사업공고 |
| 2026-10-24 | [ANTLER | 2026 앤틀러 글로벌 리쿠르팅데이 참가자 모집(10.24.)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179423) | 앤틀러코리아 | K-Startup 사업공고 |
| 2026-10-24 | [2026 시흥시 청년창업가 네트워킹 행사 참가자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179480) | 시흥시청 | K-Startup 사업공고 |
| 2026-10-25 | [2026년 대전 스타트업 원스톱 지원센터 아카데미 3회차](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179211) | 대전창조경제혁신센터 | K-Startup 사업공고 |
| 2026-10-25 | [현직 엔지니어와 함께하는 하드웨어 스타트업 제품화 실무 코칭](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179407) | 인탑스(주) | K-Startup 사업공고 |

## 스타트업 뉴스

| 날짜 | 제목 | 출처 |
|---|---|---|
| 2026-10-22 | [티오더, 월 최대 100만 명 참여하는 인터랙티브 광고 확대…브랜드 맞춤형 게임 콘텐츠 도입](https://www.venturesquare.net/1122119/) | 벤처스퀘어 |
| 2026-10-22 | [두나무, 강남 ‘업비트 라운지’ 새단장…ESG 체험·디지털자산 정보·고객 상담 결합](https://www.venturesquare.net/1122129/) | 벤처스퀘어 |
| 2026-10-22 | [프리윌린, AI 영어 문제은행 ‘잉글리시플랫’ 공개…3주 만에 교육기관 2808곳 가입](https://www.venturesquare.net/1122133/) | 벤처스퀘어 |
| 2026-10-22 | [브릴스, K Connect AI 산업통상부장관 표창…북미·유럽 수출 누적 2034만달러](https://www.venturesquare.net/1122144/) | 벤처스퀘어 |
| 2026-10-22 | [버티브, AI 데이터센터 전력·액체 냉각 기술 공유…마스터클래스에 업계 관계자 160명 참석](https://www.venturesquare.net/1122147/) | 벤처스퀘어 |
| 2026-10-22 | [창업진흥원·한인도 총영사관, 실리콘밸리서 스타트업 교류 행사 개최…투자·기술협력 모색](https://www.venturesquare.net/1122159/) | 벤처스퀘어 |
| 2026-10-22 | [미스터마인드, AI 돌봄로봇으로 치매 어르신 응급상황 대응…119 연계해 병원 이송](https://www.venturesquare.net/1122164/) | 벤처스퀘어 |
| 2026-10-22 | [필리데이, 전문의 설계 리포좀 제품 ‘트리포좀’ 3종 출시…커큐민·퀘르세틴·베르베린 적용](https://www.venturesquare.net/1122169/) | 벤처스퀘어 |
| 2026-10-22 | [마우저, 일렉트로니카 2026서 휴머노이드 로봇 공개…뮌헨공대 로보틱스 기술 시연](https://www.venturesquare.net/1122179/) | 벤처스퀘어 |
| 2026-10-22 | [팔로알토 네트웍스, PHP 취약점에 2200만 인스턴스 노출 경고…AI 시대 가상 패치 대응 강조](https://www.venturesquare.net/1122181/) | 벤처스퀘어 |
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
