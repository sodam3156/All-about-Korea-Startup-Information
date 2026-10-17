# All-about-Korea-Startup-Information

세종 청년창업 기관 공지 · 정부 지원사업 공고 · 스타트업 뉴스를 **매일 14:00 KST에 자동 수집**하는 저장소.
GitHub Actions가 수집→중복제거→상세저장→아래 대시보드 갱신→텔레그램 브리핑까지 수행한다 (git-scraping — 서버·DB·API 비용 없음).

**완전 규칙 기반**: 소스마다 공식 API/RSS 또는 정규식 파서를 쓴다(LLM 미사용, 고정비 $0). 대신 사이트가 개편되면 파서가 조용히 0건을 낼 수 있어, 같은 소스가 **연속 2회 이상 0건**이면 `data/source_health.json`에 기록하고 다이제스트에 "⚠️ 소스 점검 필요"로 경고한다 — 이게 규칙 기반의 유일한 약점(개편에 안 깨지는 AI 추출 대비)을 메우는 피드백 루프다.

<!-- AUTO:START -->

_자동 갱신: 2026-10-17 (KST)_

## 마감 임박 지원사업

| 마감 | 공고 | 기관 | 출처 |
|---|---|---|---|
| 2026-10-18 | [2026 강동구 창업가 네트워킹 데이 참가 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179388) | 강동구 청년해냄센터 | K-Startup 사업공고 |
| 2026-10-18 | [「2026 전북특구 이노폴리스 캠퍼스(액셀러레이팅 지원) 사업」배치프로그램 4기 참여기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179367) | 연구개발특구진흥재단 | K-Startup 사업공고 |
| 2026-10-18 | [2026 D-Global 딥테크 스케일업 세미나 참가 기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179494) | 조슈아파트너스(주) | K-Startup 사업공고 |
| 2026-10-19 | [2026년 대한민국 물산업 혁신 창업대전(Startup Water 2026) 참가자(팀) 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178976) | 기후에너지환경부 | K-Startup 사업공고 |
| 2026-10-19 | [UNIST 연구자-예비창업자 팀빌딩 프로그램](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179358) | 울산과학기술원(UNIST) | K-Startup 사업공고 |
| 2026-10-19 | [영도 창업오피스 크립톤 1:1 멘토링 입주기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179424) | 크립톤 부산센터 | K-Startup 사업공고 |
| 2026-10-19 | [2026년「강남 취‧창업허브센터」8차 입주 기업 신규 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179435) | 서울특별시 강남구청 | K-Startup 사업공고 |
| 2026-10-19 | [2026 Invest Seoul Partners Night](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179515) | 서울투자진흥재단 | K-Startup 사업공고 |
| 2026-10-19 | [THE RIGHT SESSION: 한국투자액셀러레이터 바른동행 Info-Day](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179493) | 한국투자액셀러레이터 | K-Startup 사업공고 |
| 2026-10-20 | [제3회 AI 및 기술기반 창업 트렌드 세미나 참가자 모집 (AI 비즈니스 실전 전략 : 멀티모달·에이전트 AX·AI 거버넌스)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179236) | 경기창조경제혁신센터 | K-Startup 사업공고 |
| 2026-10-20 | [이타카앤파트너스 조용민 대표 초청 특강 - 내가 투자한 스타트업과 성공하는 창업가의 3가지 비밀](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179426) | 경기도·경기도경제과학진흥원 | K-Startup 사업공고 |
| 2026-10-20 | [2026년 웰컴 투 팁스 6차 참가기업 모집 (전북권)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179466) | (주)로우파트너스 | K-Startup 사업공고 |
| 2026-10-20 | [2026년 웰컴 투 팁스 5차 참가기업 모집 (호남권)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179464) | (주)로우파트너스 | K-Startup 사업공고 |
| 2026-10-20 | [2026 생물자원 활용 창업벤처 지원을 위한 기업 간담회 (3회차) 참여기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179445) | 탭엔젤파트너스 | K-Startup 사업공고 |
| 2026-10-20 | [2026년 창업기업(예비창업자) 사업고도화 창업교육 참여자 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179437) | 통영시장 | K-Startup 사업공고 |
| 2026-10-20 | [제46회 창업가정신포럼](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179425) | (재)경기창조경제혁신센터  | K-Startup 사업공고 |
| 2026-10-20 | [[대전창조경제혁신센터] 2026 대전 제조파트너스 매칭데이 참가자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179482) | 대전창조경제혁신센터 | K-Startup 사업공고 |
| 2026-10-20 | [2026-5회 호남 엔젤리더스포럼 in 전남광주](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179475) | 한국엔젤투자협회 호남권 엔젤투자허브 | K-Startup 사업공고 |
| 2026-10-20 | [2026년 프로젝트 창업 인큐베이팅 : 2027 모두의 창업 선정 프로젝트](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179446) | 2026년 프로젝트 창업 인큐베이팅 운영사무국 | K-Startup 사업공고 |
| 2026-10-20 | [가죽·패션 제품개발 협업사업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179507) | 서울시 강동가죽제조지원센터 | K-Startup 사업공고 |

## 스타트업 뉴스

| 날짜 | 제목 | 출처 |
|---|---|---|
| 2026-10-16 | [엑시나, SK하이닉스와 AI 메모리 기술 협력…‘OCP 글로벌 서밋’서 CXL 기반 추론 솔루션 공개](https://www.venturesquare.net/1120582/) | 벤처스퀘어 |
| 2026-10-16 | [엔젤로보틱스, 창업자 공경철 대표 경영 복귀…피지컬 AI 중심 기술 전략 강화](https://www.venturesquare.net/1120589/) | 벤처스퀘어 |
| 2026-10-16 | [스포티파이, 하츠투하츠 단독 퍼포먼스 영상 공개…K팝 아티스트 글로벌 팬덤 연결](https://www.venturesquare.net/1120588/) | 벤처스퀘어 |
| 2026-10-16 | [테스티파이, 생성형 AI로 소프트웨어 테스트 자동화…‘G-스타 오디션’ 1위 기술 공개](https://www.venturesquare.net/1120601/) | 벤처스퀘어 |
| 2026-10-16 | [쓰리빌리언, AI 유전체 분석 속도 4배 높였다…희귀질환 진단 연구 4건 공개했다](https://www.venturesquare.net/1120605/) | 벤처스퀘어 |
| 2026-10-16 | [KOSA·TTA, 피지컬 AI 국제표준 선점 나선다…로봇·센서·데이터 통합 기준 마련](https://www.venturesquare.net/1120630/) | 벤처스퀘어 |
| 2026-10-16 | [경남창조경제혁신센터, 제조 현장 바꿀 피지컬 AI 스타트업 3개사 투자유치 지원한다](https://www.venturesquare.net/1120633/) | 벤처스퀘어 |
| 2026-10-16 | [경남창조경제혁신센터, 지역 스타트업 수출 실무부터 AI 마케팅까지…글로벌 진출 역량 강화](https://www.venturesquare.net/1120640/) | 벤처스퀘어 |
| 2026-10-16 | [에이아이매틱스, AI 운전자 점수 관리로 졸음운전 99.7% 감소…화물차 시장 공략](https://www.venturesquare.net/1120639/) | 벤처스퀘어 |
| 2026-10-16 | [라이너, AI로 일상 속 통념 검증하는 연구공모전 개최…14세 이상 누구나 참여](https://www.venturesquare.net/1120656/) | 벤처스퀘어 |
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
