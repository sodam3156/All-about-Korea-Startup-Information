# All-about-Korea-Startup-Information

세종 청년창업 기관 공지 · 정부 지원사업 공고 · 스타트업 뉴스를 **매일 14:00 KST에 자동 수집**하는 저장소.
GitHub Actions가 수집→중복제거→상세저장→아래 대시보드 갱신→텔레그램 브리핑까지 수행한다 (git-scraping — 서버·DB·API 비용 없음).

**완전 규칙 기반**: 소스마다 공식 API/RSS 또는 정규식 파서를 쓴다(LLM 미사용, 고정비 $0). 대신 사이트가 개편되면 파서가 조용히 0건을 낼 수 있어, 같은 소스가 **연속 2회 이상 0건**이면 `data/source_health.json`에 기록하고 다이제스트에 "⚠️ 소스 점검 필요"로 경고한다 — 이게 규칙 기반의 유일한 약점(개편에 안 깨지는 AI 추출 대비)을 메우는 피드백 루프다.

<!-- AUTO:START -->

_자동 갱신: 2026-09-21 (KST)_

## 마감 임박 지원사업

| 마감 | 공고 | 기관 | 출처 |
|---|---|---|---|
| 2026-09-21 | [2026년 GovTech 창업경진대회](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178968) | 정보통신산업진흥원 | K-Startup 사업공고 |
| 2026-09-21 | [인천스타트업파크 부스트 스타트업 SCEWC 2026 참가기업 모집공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179104) | (재)인천테크노파크 원장 | K-Startup 사업공고 |
| 2026-09-21 | [2026 고양시 청년 창업가 네트워킹 및 선배 창업가 특강](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179185) | 고양산업진흥원 | K-Startup 사업공고 |
| 2026-09-21 | [2026년 패션기업 연말 맞춤형 제품 제작·프로모션 지원사업 참여기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179157) | 서울경제진흥원 | K-Startup 사업공고 |
| 2026-09-21 | [청년 창업 인사이트 밋업](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179134) | 관악구청 | K-Startup 사업공고 |
| 2026-09-21 | [2026 강원권 LIPS 민간운영사 연합 INVESTOR DAY 9월 참여기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179128) | (재)강원창조경제혁신센터 | K-Startup 사업공고 |
| 2026-09-21 | [2026년 창업준비 아카데미 참여자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179122) | (주)크립톤 전북지사 | K-Startup 사업공고 |
| 2026-09-21 | [서울디자인런 2026 - 투자를 준비해야 할 때는?](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179238) | (주)오픈놀 | K-Startup 사업공고 |
| 2026-09-21 | [2026년 시흥창업캠프](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179272) | 재단법인 시흥산업진흥원장 | K-Startup 사업공고 |
| 2026-09-21 | [[부산대학교병원]「의료·헬스케어 스타트업 인큐베이터 사업」국내전시회(공동관) 참가지원 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179269) | 부산대학교병원장 | K-Startup 사업공고 |
| 2026-09-21 | [2026 홍콩 메가쇼(Mega Show Hong Kong 2026) 참가기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179243) | 서울경제진흥원 | K-Startup 사업공고 |
| 2026-09-22 | [2026 광명시 기업박람회 (GM TECH EXPO 2026) 참여기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179109) | 광명시청 | K-Startup 사업공고 |
| 2026-09-22 | [2026 부산 창업기획자 전문인력 양성과정 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179069) | (재)부산기술창업투자원 | K-Startup 사업공고 |
| 2026-09-22 | [[2026 SK임팩트부스터 데이] SK와 스타트업이 만드는 협력의 시작점, 9/22 SK임팩트부스터 데이에 초대합니다](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179166) | 마크앤컴퍼니 | K-Startup 사업공고 |
| 2026-09-22 | [2026 한·독 바이오·헬스케어 온라인 사전 세미나](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179124) | 123 Factory | K-Startup 사업공고 |
| 2026-09-22 | [2026년 스타트업 96 입주 예비창업자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179199) | (재)대전일자리경제진흥원장 | K-Startup 사업공고 |
| 2026-09-22 | [2026년 튀르키예 이스탄불 식품 박람회 참가기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179229) | 서울경제진흥원 | K-Startup 사업공고 |
| 2026-09-22 | [[글로벌 인재] 2026 이공계 GKS 대학원생 산학프로젝트 및 인턴십 참여기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179275) | 충남대학교 미래창업원 | K-Startup 사업공고 |
| 2026-09-22 | [바이오스타 2.0 예비창업자 모집 공고 및 설명회 개최](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179256) | 한국과학기술연구원 | K-Startup 사업공고 |
| 2026-09-23 | [[창업] 고객 경험(CX) 설계 실전](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178956) | 마포청년창업취업지원센터 나루 | K-Startup 사업공고 |

## 스타트업 뉴스

| 날짜 | 제목 | 출처 |
|---|---|---|
| 2026-09-20 | [“속도 늦추자”면서 데이터센터는 확대…AI 기업들의 엇갈린 셈법](https://www.venturesquare.net/1115306/) | 벤처스퀘어 |
| 2026-09-20 | [[컬처슬로건 탐방기] 데이블 – AI 시대에 일 잘하는 방법](https://www.venturesquare.net/1115319/) | 벤처스퀘어 |
| 2026-09-21 | [유이크, 피부 관리 뒤 무거운 크림 부담 줄였다…저점도 장벽 로션 출시](https://www.venturesquare.net/1115318/) | 벤처스퀘어 |
| 2026-09-21 | [강북삼성병원·자이메드, 검진 때 찍은 의료영상 AI로 다시 본다…질환 위험 조기 선별 협력](https://www.venturesquare.net/1115331/) | 벤처스퀘어 |
| 2026-09-21 | [스탠리, 2.3kg 체인톱부터 제설용 살포기까지…20V 정원공구 3종 출시](https://www.venturesquare.net/1115338/) | 벤처스퀘어 |
| 2026-09-21 | [케어링, 추석에 부모님 냉장고·약봉투 살펴보세요…돌봄 징후 10가지 알린다](https://www.venturesquare.net/1115345/) | 벤처스퀘어 |
| 2026-09-21 | [울산창조경제혁신센터, 청년 아이디어 12팀 실제 제품으로…로컬기업과 협업 기회 연다](https://www.venturesquare.net/1115360/) | 벤처스퀘어 |
| 2026-09-21 | [펀진·육군교육사령부, AI로 미래 전투실험 고도화…무인체계·클라우드까지 협력](https://www.venturesquare.net/1115367/) | 벤처스퀘어 |
| 2026-09-21 | [딥브레인AI, 고민 말하기 어려운 청소년에 AI 아바타 먼저…상담 연결 문턱 낮춘다](https://www.venturesquare.net/1115377/) | 벤처스퀘어 |
| 2026-09-21 | [정보통신산업진흥원·한국엔젤투자협회, AICT 스타트업 국내외 진출 지원 협약](https://www.venturesquare.net/1115380/) | 벤처스퀘어 |
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
