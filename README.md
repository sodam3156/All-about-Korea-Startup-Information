# All-about-Korea-Startup-Information

세종 청년창업 기관 공지 · 정부 지원사업 공고 · 스타트업 뉴스를 **매일 14:00 KST에 자동 수집**하는 저장소.
GitHub Actions가 수집→중복제거→상세저장→아래 대시보드 갱신→텔레그램 브리핑까지 수행한다 (git-scraping — 서버·DB·API 비용 없음).

**완전 규칙 기반**: 소스마다 공식 API/RSS 또는 정규식 파서를 쓴다(LLM 미사용, 고정비 $0). 대신 사이트가 개편되면 파서가 조용히 0건을 낼 수 있어, 같은 소스가 **연속 2회 이상 0건**이면 `data/source_health.json`에 기록하고 다이제스트에 "⚠️ 소스 점검 필요"로 경고한다 — 이게 규칙 기반의 유일한 약점(개편에 안 깨지는 AI 추출 대비)을 메우는 피드백 루프다.

<!-- AUTO:START -->

_자동 갱신: 2026-11-08 (KST)_

## 마감 임박 지원사업

| 마감 | 공고 | 기관 | 출처 |
|---|---|---|---|
| 2026-11-08 | [2026년 청년 어촌창업 아이디어 공모전](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179448) | 한국어촌어항공단 | K-Startup 사업공고 |
| 2026-11-08 | [의정부 FIT데이(Demo Day) 2회차 기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179447) | 경기창조경제혁신센터 | K-Startup 사업공고 |
| 2026-11-08 | [서울동부여성발전센터 창업센터 2027년 신규 입주기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179561) | 서울동부여성발전센터 | K-Startup 사업공고 |
| 2026-11-08 | [2026 별별상상 스타트업 챌린지](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179676) | 주식회사 툰즈 | K-Startup 사업공고 |
| 2026-11-09 | [동국대학교 창업보육센터(서울) 신규 입주기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179598) | 동국대학교 창업보육센터 | K-Startup 사업공고 |
| 2026-11-09 | [2026년 안산정보산업진흥센터(경기TP안산창업보육센터) 제4차 신규 입주자 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179606) | (재)경기테크노파크 | K-Startup 사업공고 |
| 2026-11-09 | [[서초창업스테이션] 11월 창업 교육 프로그램 - 초기 스타트업을 위한 브랜드 만들기](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179622) | 서초창업스테이션 | K-Startup 사업공고 |
| 2026-11-09 | [서울디자인재단 「2026 서울디자인런 포럼」 참가 신청](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179637) | (주)오픈놀 | K-Startup 사업공고 |
| 2026-11-09 | [[숭실대학교 캠퍼스타운] 스타트업 인턴십 참여기업 모집(외국인 유학생 인턴형)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179669) | 숭실대학교 캠퍼스타운사업단 | K-Startup 사업공고 |
| 2026-11-09 | [대덕 원스톱 Bridge 연계 제 108회 대전창업포럼 참가 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179664) | (재)대전창조경제혁신센터 | K-Startup 사업공고 |
| 2026-11-09 | [[ 모 집 ] GVC AI Platform Startup Enabling Program 및 스마트워크·쇼핑몰 창업지원 및 AI 전환 지원](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179681) | 글로벌벤처센터 | K-Startup 사업공고 |
| 2026-11-09 | [2026년 스타트업 법률지원사업 전남광주통합특별시 법률상담회 참여기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179708) | 창업진흥원 원스톱지원실 | K-Startup 사업공고 |
| 2026-11-09 | [2026년 중동 상황 대응 규격 컨설팅 지원사업「수혜기업 모집」](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179723) | 서울경제진흥원 | K-Startup 사업공고 |
| 2026-11-09 | [[벤처기업협회] 2026년 예비창업패키지 특화분야(소셜벤처)「임팩트스타 IR 데모데이」개최 (11/10)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179735) | 벤처기업협회 | K-Startup 사업공고 |
| 2026-11-10 | [[무료 AI 역량강화 교육]생성형 AI 기반 무역 컴플라이언스 및 관세·ESG 리스크 최적화(부산)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179251) | (주)글로벌창업연구소 | K-Startup 사업공고 |
| 2026-11-10 | [2026년도 양자산업 QX 네트워킹 포럼 「Quantum Horizon」 참가 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179455) | 블루포인트파트너스 | K-Startup 사업공고 |
| 2026-11-10 | [(경남센터) 2026년 제9회 제대군인 창업 워크숍 개최 안내](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179520) | 국가보훈부 | K-Startup 사업공고 |
| 2026-11-10 | [[GBSA] 2026 판교스타트업 투자교류회 제 4차 투자교류회](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179554) | ㈜내비온파트너스 | K-Startup 사업공고 |
| 2026-11-10 | [2026 TEL VENTURE CAPITAL X 충남창조경제혁신센터 Nexus Connect 투자 밋업 데이](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179543) | (재)충남창조경제혁신센터 대표이사 | K-Startup 사업공고 |
| 2026-11-10 | [G밸리의료기기개발지원센터 글로벌역량강화 교육프로그램 참가자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179545) | 한국과학기술연구원 | K-Startup 사업공고 |

## 스타트업 뉴스

| 날짜 | 제목 | 출처 |
|---|---|---|
| 2026-11-07 | [[AI 시대 리더의 대화법] AI로 FAQ 40개 만들었는데 성과평가는 C…팀장은 무엇을 설명해야 할까](https://www.venturesquare.net/1126531/) | 벤처스퀘어 |
| 2026-11-08 | [[VS 기획] AI는 진화하는데 정부는 산업화 시대에…토니블레어연구소가 제안한 ‘국가 재설계’](https://www.venturesquare.net/1126542/) | 벤처스퀘어 |
| 2026-11-06 | [[김지현의 Scale-Up Note] 스케일업을 위한 회사의 목어(木魚)는 깨어 있는가](https://www.venturesquare.net/1126473/) | 벤처스퀘어 |
| 2026-11-07 | [“진료실에서 발견한 여성 건강의 정보 격차”…아르카디안 정선화 대표가 생리대를 만든 이유](https://www.venturesquare.net/1126514/) | 벤처스퀘어 |
| 2026-11-05 | [경북창조경제혁신센터, 소셜벤처 11개사 판별 완료…9개사 사업화 지원](https://www.venturesquare.net/1126176/) | 벤처스퀘어 |
| 2026-11-05 | [팀매버릭스 서창우 대표 “7번의 실패 끝에 찾은 기회, 누구나 콘텐츠로 사업하는 시대”](https://www.venturesquare.net/1126008/) | 벤처스퀘어 |
| 2026-11-06 | [텍사스 인스트루먼트, 산업용 이더넷 통합 모듈 공개…하드웨어 교체 없이 3개 프로토콜 지원](https://www.venturesquare.net/1126248/) | 벤처스퀘어 |
| 2026-11-06 | [더즌, 3분기 누적 순이익 94억원·8.7% 증가…외환거래 솔루션 매출 14.9% 성장](https://www.venturesquare.net/1126250/) | 벤처스퀘어 |
| 2026-11-06 | [대전창조경제혁신센터, 일본 VC 대전 초청…딥테크 스타트업 5개사 투자·기술협력 논의](https://www.venturesquare.net/1126257/) | 벤처스퀘어 |
| 2026-11-06 | [기술보증기금·부산시·BNK금융그룹, 기후테크 기업에 150억원 금융지원](https://www.venturesquare.net/1126260/) | 벤처스퀘어 |
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
