# All-about-Korea-Startup-Information

세종 청년창업 기관 공지 · 정부 지원사업 공고 · 스타트업 뉴스를 **매일 14:00 KST에 자동 수집**하는 저장소.
GitHub Actions가 수집→중복제거→상세저장→아래 대시보드 갱신→텔레그램 브리핑까지 수행한다 (git-scraping — 서버·DB·API 비용 없음).

**완전 규칙 기반**: 소스마다 공식 API/RSS 또는 정규식 파서를 쓴다(LLM 미사용, 고정비 $0). 대신 사이트가 개편되면 파서가 조용히 0건을 낼 수 있어, 같은 소스가 **연속 2회 이상 0건**이면 `data/source_health.json`에 기록하고 다이제스트에 "⚠️ 소스 점검 필요"로 경고한다 — 이게 규칙 기반의 유일한 약점(개편에 안 깨지는 AI 추출 대비)을 메우는 피드백 루프다.

<!-- AUTO:START -->

_자동 갱신: 2026-10-19 (KST)_

## 마감 임박 지원사업

| 마감 | 공고 | 기관 | 출처 |
|---|---|---|---|
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
| 2026-10-21 | [파주청년창업지원센터 하반기 청년 창업아카데미 참여기업/팀 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179318) | 파주시, (재)경기테크노파크 | K-Startup 사업공고 |
| 2026-10-21 | [[서초창업스테이션] 서리풀 소상공인 창업 클리닉(10월) - 소상공인 1:1 컨설팅](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179370) | 서초창업스테이션 | K-Startup 사업공고 |
| 2026-10-21 | [2026년 제3차 I-PLEX광주 입주기업 모집공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179442) | (재)광주테크노파크 | K-Startup 사업공고 |

## 스타트업 뉴스

| 날짜 | 제목 | 출처 |
|---|---|---|
| 2026-10-19 | [부스터스 이퀄베리, 미국 얼타뷰티 입점…오프라인 월평균 매출 10배 성장](https://www.venturesquare.net/1120890/) | 벤처스퀘어 |
| 2026-10-19 | [클레온, 삼성 무안경 3D 디스플레이에 대화형 AI 적용…서울역 ‘AI 역무원’ 시범 운영](https://www.venturesquare.net/1120893/) | 벤처스퀘어 |
| 2026-10-19 | [스파크랩, AI 창업팀 76곳 육성…10주 만에 첫 매출 10개 팀·신규 고객 확보 24개 팀](https://www.venturesquare.net/1120904/) | 벤처스퀘어 |
| 2026-10-19 | [스페이스브이, 단기임대 플랫폼 ‘삼삼엠투’ 거래액 4500억원 돌파…서울시 우수기업 인증](https://www.venturesquare.net/1120910/) | 벤처스퀘어 |
| 2026-10-19 | [지엔테크놀로지스, 선박 철 구조물 활용한 무선통신 기술로 글로벌 시장 확대](https://www.venturesquare.net/1120552/) | 벤처스퀘어 |
| 2026-10-19 | [주빅, 40억원 규모 스케일업 팁스 선정…바이오의약품 마이크로니들 양산기술 고도화](https://www.venturesquare.net/1120918/) | 벤처스퀘어 |
| 2026-10-19 | [블루포인트·한국원자력협력재단, 원자력 딥테크 스타트업 6개 팀 투자유치 무대 마련](https://www.venturesquare.net/1120928/) | 벤처스퀘어 |
| 2026-10-19 | [마크앤컴퍼니, 스타트업 성장 데이터로 이직 판단 돕는다…‘혁신의숲 career’ 출시](https://www.venturesquare.net/1120930/) | 벤처스퀘어 |
| 2026-10-19 | [더파운더즈, 북미 세포라 1200개 매장 진출한 ‘프롬랩스’ 글로벌 마케팅 인재 채용](https://www.venturesquare.net/1120938/) | 벤처스퀘어 |
| 2026-10-19 | [플럭스, OLED 증착 기술로 차세대 배터리용 금속 음극 맞춤 제작](https://www.venturesquare.net/1120843/) | 벤처스퀘어 |
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
