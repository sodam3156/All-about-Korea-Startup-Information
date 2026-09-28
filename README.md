# All-about-Korea-Startup-Information

세종 청년창업 기관 공지 · 정부 지원사업 공고 · 스타트업 뉴스를 **매일 14:00 KST에 자동 수집**하는 저장소.
GitHub Actions가 수집→중복제거→상세저장→아래 대시보드 갱신→텔레그램 브리핑까지 수행한다 (git-scraping — 서버·DB·API 비용 없음).

**완전 규칙 기반**: 소스마다 공식 API/RSS 또는 정규식 파서를 쓴다(LLM 미사용, 고정비 $0). 대신 사이트가 개편되면 파서가 조용히 0건을 낼 수 있어, 같은 소스가 **연속 2회 이상 0건**이면 `data/source_health.json`에 기록하고 다이제스트에 "⚠️ 소스 점검 필요"로 경고한다 — 이게 규칙 기반의 유일한 약점(개편에 안 깨지는 AI 추출 대비)을 메우는 피드백 루프다.

<!-- AUTO:START -->

_자동 갱신: 2026-09-28 (KST)_

## 마감 임박 지원사업

| 마감 | 공고 | 기관 | 출처 |
|---|---|---|---|
| 2026-09-28 | [[서초창업스테이션] 서리풀 소상공인 창업 클리닉(9월) - 소상공인 1:1 컨설팅](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179048) | 서초창업스테이션 | K-Startup 사업공고 |
| 2026-09-28 | [[투자연계&사업화] 더인벤션랩 2026 엣지업 크리에이터스 4기 AX/LX Challenge 모집공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179038) | 더인벤션랩 | K-Startup 사업공고 |
| 2026-09-28 | [2026년 하반기 서울창업허브 성수 입주기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179187) | 서울경제진흥원 | K-Startup 사업공고 |
| 2026-09-28 | [2026년 강동 K-ISS멘토링센터 4차 교육 및 튜토링 과정 투자 유치 전략과 IR 피칭 스킬업](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179180) | 주식회사 이노시아 | K-Startup 사업공고 |
| 2026-09-28 | [2026년 대전 스타트업스쿨 스타트업 리딩클래스 (5회차 ㅣ 예비 및 초기창업자가 1년 안에 가장 후회하는 3가지)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179257) | 대전창조경제혁신센터 | K-Startup 사업공고 |
| 2026-09-28 | [연구개발특구진흥재단 × 대구창조경제혁신센터 「2026 이노폴리스 오픈이노베이션 밋업데이」참여기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179223) | 연구개발특구진흥재단 | K-Startup 사업공고 |
| 2026-09-28 | [2026년 하반기 경기도여성창업보육센터 입주기업 모집 연장공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179289) | 경기도일자리재단 남부사업본부장 | K-Startup 사업공고 |
| 2026-09-28 | [제7회 원주권 스타트업 커뮤니티 데이 참가자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179273) | 상지대학교 벤처창업본부  | K-Startup 사업공고 |
| 2026-09-29 | [2026 투자 유치 세미나 - 투자사 관점에서 보는 투자유치를 위한 실전 전략](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179224) | 서울창업허브 창동 | K-Startup 사업공고 |
| 2026-09-29 | [[인천] 2026년 IP창업존 51기 교육(모두의창업 연계과정) 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179271) | 인천지식재산센터 | K-Startup 사업공고 |
| 2026-09-29 | [「서울소셜벤처허브」2026년 ‘허브 멤버스’ 입주사 추가모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179270) | 서울소셜벤처허브 | K-Startup 사업공고 |
| 2026-09-29 | [‘2026년 글로컬 창업사관학교 액셀러레이팅’ 참여기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179308) | 국립순천대학교 창업지원단장국립순천대학교 창업지원단장 | K-Startup 사업공고 |
| 2026-09-29 | [[창업BuS x Station C] 2026년 강원BRIDGE 배치프로그램 2차 창업기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179305) | 재단법인 강원창조경제혁신센터 | K-Startup 사업공고 |
| 2026-09-29 | [청년창업 거주지원시설(창업하여家) 입주자 3차 모집(연장)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179292) | (재)광주테크노파크 | K-Startup 사업공고 |
| 2026-09-29 | [2026년 제2회 테크플러스 스테이지 입주기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179291) | (재)광주테크노파크 | K-Startup 사업공고 |
| 2026-09-30 | [남서울대학교 창업보육센터 입주기업 모집 (천안소재)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178706) | 남서울대학교 창업보육센터 | K-Startup 사업공고 |
| 2026-09-30 | [「2026년 강소특구 이노테크 발굴 및 창업지원사업」예비 창업자 사업화 지원 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178786) | 한국전력공사 강소특구 육성사업단장, 나주 강소특구 공동연구기관장 | K-Startup 사업공고 |
| 2026-09-30 | [2026년 중소기업 동행교육](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178817) | 근로복지공단 인재개발원 | K-Startup 사업공고 |
| 2026-09-30 | [취약분야 상시 컨설팅 9월 참가자 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178948) | 강동구 청년해냄센터 | K-Startup 사업공고 |
| 2026-09-30 | [2026년 한국외대 창업보육센터 입주기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179002) | 한국외국어대학교연구산학협력단 | K-Startup 사업공고 |

## 스타트업 뉴스

| 날짜 | 제목 | 출처 |
|---|---|---|
| 2026-09-27 | [포시에스, 이름·서명란까지 AI가 알아서 만든다…전자서식 자동 완성 기술 특허](https://www.venturesquare.net/1116304/) | 벤처스퀘어 |
| 2026-09-27 | [네이버클라우드, DB·서버 접속 한곳서 통제한다…개인정보 접근기록 자동 관리 ‘DSAC’ 출시](https://www.venturesquare.net/1116307/) | 벤처스퀘어 |
| 2026-09-27 | [“버려지는 열로 습도 잡고 전력 56% 줄였다”…김보선 클레네어 대표가 바꾸는 산업용 공조](https://www.venturesquare.net/1113680/) | 벤처스퀘어 |
| 2026-09-28 | [오케스트로, VM웨어 바꾼 뒤가 더 중요하다…장애 이력부터 물리망까지 추적](https://www.venturesquare.net/1116323/) | 벤처스퀘어 |
| 2026-09-28 | [서울대기술지주, 엔비디아 밖에서도 로봇 AI 돌린다…바이스트라타 투자](https://www.venturesquare.net/1116329/) | 벤처스퀘어 |
| 2026-09-28 | [제이앤피메디, FDA 제출 전부터 전략 짠다…의료기기 미국 진출 웨비나 2회 개최](https://www.venturesquare.net/1116341/) | 벤처스퀘어 |
| 2026-09-28 | [부산창조경제혁신센터, 바운스 10주년…기업 25곳·투자사 30곳과 스타트업 연결](https://www.venturesquare.net/1116350/) | 벤처스퀘어 |
| 2026-09-28 | [딥브레인AI, 상담 인력 부족한 중소기업에 AI 아바타 투입…4개 업종서 실증](https://www.venturesquare.net/1116353/) | 벤처스퀘어 |
| 2026-09-28 | [극지연구소·콜즈다이나믹스, 빙하·해류·극한생물 데이터로 사업할 스타트업 찾는다](https://www.venturesquare.net/1116365/) | 벤처스퀘어 |
| 2026-09-28 | [부산창경·AXMOS·NC AI, 부산 제조기업 데이터 밖으로 안 보낸다…현장형 AI 공동 개발](https://www.venturesquare.net/1116373/) | 벤처스퀘어 |
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
