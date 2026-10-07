# All-about-Korea-Startup-Information

세종 청년창업 기관 공지 · 정부 지원사업 공고 · 스타트업 뉴스를 **매일 14:00 KST에 자동 수집**하는 저장소.
GitHub Actions가 수집→중복제거→상세저장→아래 대시보드 갱신→텔레그램 브리핑까지 수행한다 (git-scraping — 서버·DB·API 비용 없음).

**완전 규칙 기반**: 소스마다 공식 API/RSS 또는 정규식 파서를 쓴다(LLM 미사용, 고정비 $0). 대신 사이트가 개편되면 파서가 조용히 0건을 낼 수 있어, 같은 소스가 **연속 2회 이상 0건**이면 `data/source_health.json`에 기록하고 다이제스트에 "⚠️ 소스 점검 필요"로 경고한다 — 이게 규칙 기반의 유일한 약점(개편에 안 깨지는 AI 추출 대비)을 메우는 피드백 루프다.

<!-- AUTO:START -->

_자동 갱신: 2026-10-07 (KST)_

## 마감 임박 지원사업

| 마감 | 공고 | 기관 | 출처 |
|---|---|---|---|
| 2026-10-07 | [[숭실대학교 캠퍼스타운] 2026 석·박사급 실험실 창업스쿨(유형2) 참여자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179054) | 숭실대학교 캠퍼스타운사업단 | K-Startup 사업공고 |
| 2026-10-07 | [2026년 투자 유치 역량 강화 특강](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179183) | 동대문구 창업지원센터 | K-Startup 사업공고 |
| 2026-10-07 | [2026년 민간 산림복지 창업 아카데미[2차] 참가자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179276) | 한국산림복지진흥원 | K-Startup 사업공고 |
| 2026-10-07 | [2026년 블록체인 기업성장허브 입주기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179303) | 한국인터넷진흥원 | K-Startup 사업공고 |
| 2026-10-07 | [구로구 청년창업지원센터 일반 창업교육(하반기: 4회차): 온라인 마케팅 실전 가이드](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179300) | 구로구 청년창업지원센터 | K-Startup 사업공고 |
| 2026-10-07 | [창업 초보를 위한 창업 A-Z 교육](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179247) | 하우그로우 원격평생교육원 | K-Startup 사업공고 |
| 2026-10-07 | [로컬창업캠프 2기](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179314) | 관악구청 | K-Startup 사업공고 |
| 2026-10-07 | [2026 전북-수도권 기업 『투자 & 비즈니스 라운드』](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179349) | 쿠키미디어(주) | K-Startup 사업공고 |
| 2026-10-07 | [2026년도 한국가스공사 에너지 창업·벤처기업 육성사업](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179344) | 한국가스공사 | K-Startup 사업공고 |
| 2026-10-07 | [서울디자인런 2026 - 실패하지 않는 브랜딩 A to Z](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179334) | (주)오픈놀 | K-Startup 사업공고 |
| 2026-10-07 | [2026년 제 5회 김해 스타트업 IR「G-row UP! IR Stage」 오픈리그](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179333) | 김해의생명산업진흥원 | K-Startup 사업공고 |
| 2026-10-07 | [[창업BuS x Station C] 2026년 강원BRIDGE 배치프로그램 2차 창업기업 모집 연장공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179401) | 재단법인 강원창조경제혁신센터 | K-Startup 사업공고 |
| 2026-10-07 | [상지대학교 창업보육센터 입주기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179379) | 상지대학교 창업보육센터 | K-Startup 사업공고 |
| 2026-10-08 | [[임팩트스퀘어] 롯데케미칼 자원순환 스타트업 지원 프로그램 &apos;프로젝트루프소셜 5기&apos; 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179242) | (주)임팩트스퀘어 | K-Startup 사업공고 |
| 2026-10-08 | [2026 Innopolis×LG Open Innovation Meet-up Day](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179250) | 와이앤아처 주식회사 | K-Startup 사업공고 |
| 2026-10-08 | [2026 제10회 G밸리창업경진대회 참가기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179309) | 한국산업단지공단 | K-Startup 사업공고 |
| 2026-10-08 | [2026 서초AICT 데모데이 참가기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179328) | 서초AICT 운영센터 | K-Startup 사업공고 |
| 2026-10-08 | [제 22기 K-water 협력스타트업 모집공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179322) | K-water 기후테크혁신처장 | K-Startup 사업공고 |
| 2026-10-08 | [2026년 한수원 우문현답 현장 클리닉센터 지원사업 「원전·에너지 분야 선택형 과제」참여기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179380) | (사)경기중소벤처기업연합회 | K-Startup 사업공고 |
| 2026-10-08 | [[온라인] chatGPT로 만드는 내 퍼스널 브랜딩 플랫폼 만들기 | 바이브코딩 실전 클래스](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179368) | 스쿨모아 주식회사 | K-Startup 사업공고 |

## 스타트업 뉴스

| 날짜 | 제목 | 출처 |
|---|---|---|
| 2026-10-06 | [컬리, 김치도 ‘작게 사서 바로 먹는다’…소용량 포장김치 거래액 39% 증가](https://www.venturesquare.net/1118196/) | 벤처스퀘어 |
| 2026-10-06 | [클레온, 영업·면접 상대 AI로 만들어 반복 연습…‘롤핏 스튜디오’ 출시](https://www.venturesquare.net/1118195/) | 벤처스퀘어 |
| 2026-10-06 | [문페이·KB국민카드, 외국인 스테이블코인 결제 실험…국내 가맹점 연결 PoC 추진](https://www.venturesquare.net/1118199/) | 벤처스퀘어 |
| 2026-10-06 | [마키나락스, 인터넷 끊긴 해군 함정서 AI가 교범 찾는다…포항함 ‘장비운용 AI 참모’ 실증](https://www.venturesquare.net/1118203/) | 벤처스퀘어 |
| 2026-10-06 | [시큐리티스코어카드, 벤더 보안 설문부터 조치·재검증까지 AI가 잇는다…‘타이탄 AI’ 공개](https://www.venturesquare.net/1118216/) | 벤처스퀘어 |
| 2026-10-06 | [누리하우스, 뉴욕 K뷰티 팝업을 ‘시즌제 플랫폼’으로…해시드와 VC 컨퍼런스도 연다](https://www.venturesquare.net/1118232/) | 벤처스퀘어 |
| 2026-10-06 | [헥토데이터, 여권 찍고 얼굴 비추면 본인확인…글로벌 고객용 인증 API 확대](https://www.venturesquare.net/1118231/) | 벤처스퀘어 |
| 2026-10-06 | [“잘 팔리는 화장품보다 ‘팔릴 구조’를 본다”…정다연 모스트 대표의 K-뷰티 미국 공략법](https://www.venturesquare.net/1118237/) | 벤처스퀘어 |
| 2026-10-06 | [혁신의숲, 이력서에 스타트업 성장 데이터 붙인다…‘공고분석·커리어맵’ 14일 공개](https://www.venturesquare.net/1118259/) | 벤처스퀘어 |
| 2026-10-06 | [넥스원소프트, 해외카드로 고속·시외버스 바로 예매…‘버스타고’에 넥스비 3DS 적용](https://www.venturesquare.net/1118263/) | 벤처스퀘어 |
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
