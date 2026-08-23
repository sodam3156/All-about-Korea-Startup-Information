# All-about-Korea-Startup-Information

세종 청년창업 기관 공지 · 정부 지원사업 공고 · 스타트업 뉴스를 **매일 14:00 KST에 자동 수집**하는 저장소.
GitHub Actions가 수집→중복제거→상세저장→아래 대시보드 갱신→텔레그램 브리핑까지 수행한다 (git-scraping — 서버·DB·API 비용 없음).

**완전 규칙 기반**: 소스마다 공식 API/RSS 또는 정규식 파서를 쓴다(LLM 미사용, 고정비 $0). 대신 사이트가 개편되면 파서가 조용히 0건을 낼 수 있어, 같은 소스가 **연속 2회 이상 0건**이면 `data/source_health.json`에 기록하고 다이제스트에 "⚠️ 소스 점검 필요"로 경고한다 — 이게 규칙 기반의 유일한 약점(개편에 안 깨지는 AI 추출 대비)을 메우는 피드백 루프다.

<!-- AUTO:START -->

_자동 갱신: 2026-08-23 (KST)_

## 마감 임박 지원사업

| 마감 | 공고 | 기관 | 출처 |
|---|---|---|---|
| 2026-08-23 | ['스타트업 SEO 마케팅 전략' 비대면 교육 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178704) | 서울핀테크랩 | K-Startup 사업공고 |
| 2026-08-23 | [서대문구-서울시립대학교 창업지원센터 입주기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178697) | 서울시립대학교 창업보육센터장 | K-Startup 사업공고 |
| 2026-08-23 | [KAC 한국공항공사 창업 인큐베이팅 프로그램 참여자를 모집합니다. - "CRAFT YOUR RUNWAY!"](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178830) | 한국공항공사 | K-Startup 사업공고 |
| 2026-08-23 | [예비 중장년 기업의 사업계획 기반의 생성형AI활용 및 바이브 코딩(초급)역량강화 교육(2차)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178864) | 성북구 중장년 기술창업센터 | K-Startup 사업공고 |
| 2026-08-24 | [2026년 모두의 창업 글로벌 프로그램 주관기관 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178779) | 중소벤처기업부 | K-Startup 사업공고 |
| 2026-08-24 | [[서울과학기술대학교]SLA 3D프린터 장비교육](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178754) | 서울과학기술대학교 | K-Startup 사업공고 |
| 2026-08-24 | [2026년 세종 스타트업 원스톱 지원센터 아카데미 2차](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178726) | (주) 렛츠 | K-Startup 사업공고 |
| 2026-08-24 | [『2026 오픈웨이브 with 한진』참여기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178796) | 재단법인 인천창조경제혁신센터 | K-Startup 사업공고 |
| 2026-08-24 | [2026년 구미시 스타트업 필드 3차 입주기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178772) | 구미전자정보기술원 | K-Startup 사업공고 |
| 2026-08-24 | [2026 강원권 LIPS 민간운영사 연합 INVESTOR DAY 8월 참여기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178762) | (재)강원창조경제혁신센터 | K-Startup 사업공고 |
| 2026-08-24 | [2026 Startup for All Global(Silicon Valley) Program Public Announcement for Program Service Provider](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178848) | KISED Silicon Valley Office | K-Startup 사업공고 |
| 2026-08-24 | [2026 한국관광공사 관광기업지원센터 관광기업 역량강화 3차 교육](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178763) | 한국관광공사 관광기업지원센터(서울) | K-Startup 사업공고 |
| 2026-08-24 | [2026년 강북창업지원센터 8월 창업교육 프로그램 참가자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178904) | 강북청년창업마루 | K-Startup 사업공고 |
| 2026-08-24 | [2026 아트코리아랩 AI+기술융합 오픈이노베이션(2차) 참여기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178881) | 예술경영지원센터 | K-Startup 사업공고 |
| 2026-08-25 | [[숭실대학교 캠퍼스타운] 2026 석·박사급 실험실 창업스쿨(유형1) 참여자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178673) | 숭실대학교 캠퍼스타운사업단 | K-Startup 사업공고 |
| 2026-08-25 | [2026년 대전 스타트업스쿨 스타트업 리딩클래스 (3회차 ㅣ ESG와 기후테크를 활용한 스타트업 투자유치 전략)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178820) | 대전창조경제혁신센터 | K-Startup 사업공고 |
| 2026-08-25 | [2026년 민간 산림복지 창업·성장 패키지 FOR:SEED [예비창업패키지] 2차 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178806) | 한국산림복지진흥원  | K-Startup 사업공고 |
| 2026-08-25 | [Request for Proposals (RFP) for the 2026 Startup for All Global (New York) Program](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178847) | KISED | K-Startup 사업공고 |
| 2026-08-25 | [2026년 2기 서울 AI 허브 멤버십 기업 모집 안내](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178879) | 서울 AI 허브 | K-Startup 사업공고 |
| 2026-08-25 | [제3회 「S.Challenge IR」 AXˑDX 분야 창업기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178861) | 서울지방중소벤처기업청, 서울창조경제혁신센터 | K-Startup 사업공고 |

## 스타트업 뉴스

| 날짜 | 제목 | 출처 |
|---|---|---|
| 2026-08-22 | [“사고 막는 AI보다 생명을 살리는 골든타임”…김경목 별따러가자 대표가 만든 이동안전망](https://www.venturesquare.net/1098969/) | 벤처스퀘어 |
| 2026-08-22 | [[최앤리의 스타트업 법률 가이드] 창업자 지분은 마음대로 팔 수 있을까…우선매수권부터 드래그얼롱까지](https://www.venturesquare.net/1105278/) | 벤처스퀘어 |
| 2026-08-21 | [[AI 시대 리더의 대화법] AI가 만든 보고서에 판단이 없다면…리더가 건네야 할 4가지](https://www.venturesquare.net/1107676/) | 벤처스퀘어 |
| 2026-08-21 | [AI 에이전트가 결제까지…더즌, 구글 클라우드·솔라나 해커톤 심사](https://www.venturesquare.net/1107711/) | 벤처스퀘어 |
| 2026-08-21 | [로봇 아이돌부터 월드투어까지…갤럭시코퍼레이션, ‘GALAXY ROBOT PARK’서 피지컬 AI 로드맵 공개](https://www.venturesquare.net/1107719/) | 벤처스퀘어 |
| 2026-08-22 | [민원 접수 전 위험도 예측…포티투마루, 화성시 도시데이터플랫폼 참여한다](https://www.venturesquare.net/1107736/) | 벤처스퀘어 |
| 2026-08-22 | [도로의 실시간 변화를 읽는 지도…웨이즈원, LDM 기술 공개·정책지원 2027년까지](https://www.venturesquare.net/1107744/) | 벤처스퀘어 |
| 2026-08-22 | [약국 데이터가 정책 연구로…비알피커넥트·의약품정책연구소 맞손](https://www.venturesquare.net/1107753/) | 벤처스퀘어 |
| 2026-08-22 | [일본 도심형 캡슐호텔 국내 첫선…트윈미디어, ‘퍼스트 캐빈 명동’ 직판 기반 구축](https://www.venturesquare.net/1107756/) | 벤처스퀘어 |
| 2026-08-22 | [물 위 태양광, 모듈별로 이상 감지…K-water 충주댐지사·커널로그 MLPE 실증](https://www.venturesquare.net/1107769/) | 벤처스퀘어 |
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
