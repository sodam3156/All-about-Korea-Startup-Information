# All-about-Korea-Startup-Information

세종 청년창업 기관 공지 · 정부 지원사업 공고 · 스타트업 뉴스를 **매일 14:00 KST에 자동 수집**하는 저장소.
GitHub Actions가 수집→중복제거→상세저장→아래 대시보드 갱신→텔레그램 브리핑까지 수행한다 (git-scraping — 서버·DB·API 비용 없음).

**완전 규칙 기반**: 소스마다 공식 API/RSS 또는 정규식 파서를 쓴다(LLM 미사용, 고정비 $0). 대신 사이트가 개편되면 파서가 조용히 0건을 낼 수 있어, 같은 소스가 **연속 2회 이상 0건**이면 `data/source_health.json`에 기록하고 다이제스트에 "⚠️ 소스 점검 필요"로 경고한다 — 이게 규칙 기반의 유일한 약점(개편에 안 깨지는 AI 추출 대비)을 메우는 피드백 루프다.

<!-- AUTO:START -->

_자동 갱신: 2026-09-16 (KST)_

## 마감 임박 지원사업

| 마감 | 공고 | 기관 | 출처 |
|---|---|---|---|
| 2026-09-16 | [2026 모험·도전적 AI 스타트업 투자대상 발굴 경진대회](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179037) | 엠와이소셜컴퍼니 | K-Startup 사업공고 |
| 2026-09-16 | [싱가포르 현지 진출 지원 국내 블록체인 기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179068) | 한국인터넷진흥원 | K-Startup 사업공고 |
| 2026-09-16 | [[2026 마포청년축제: MAP-O] 스피드(30분) 창업 멘토링](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179103) | 마포청년창업취업지원센터 나루 | K-Startup 사업공고 |
| 2026-09-16 | [K-이커머스 미국 진출의 모든 것: 크라우드펀딩부터 Shopify·글로벌 결제까지 세미나 참여기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179181) | (주)펀딩인사이더 | K-Startup 사업공고 |
| 2026-09-16 | [구로구 청년창업지원센터 일반 창업교육(하반기: 3회차): 서울시 청년이 활용 가능한 창업지원 정책](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179139) | 구로구 청년창업지원센터 | K-Startup 사업공고 |
| 2026-09-16 | [BIXPO 2026 스타트업 성장지원 프로그램 참가기업 모집(에너지·기후테크·융복합 분야 100개사)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179129) | (사)코리아스타트업포럼 | K-Startup 사업공고 |
| 2026-09-16 | [「성남하이테크밸리 복합문화센터」 (예비)창업기업 입주 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179088) | 성남산업진흥원 | K-Startup 사업공고 |
| 2026-09-16 | [대학생 창업자가 투자를 유치하며 겪었던 이야기들(#고객이 원하는 시장을 찾는 방법) - 제9차 벤처스타트업 아카데미](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179202) | DDM 청년창업센터 유니콘 | K-Startup 사업공고 |
| 2026-09-16 | [2026 아스트라제네카-서울바이오허브 글로벌 오픈이노베이션 참여기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179174) | 한국과학기술연구원 서울바이오허브사업단장 | K-Startup 사업공고 |
| 2026-09-16 | [한국기술교육대학교 오픈이노베이션 프로그램 참여기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179213) | 한국기술교육대학교 앵커사업단 | K-Startup 사업공고 |
| 2026-09-16 | [AI 기반 지역관광 문제해결 프로젝트 (역사문화형) AI 배리어프리 부문 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179203) | 한국관광공사 트래블 X-Lab | K-Startup 사업공고 |
| 2026-09-16 | [한양대학교 ERICA 분야별 전문가 1:1상담회(경영파트) 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179262) | 한양대학교 ERICA 혁신스타트업지원센터 | K-Startup 사업공고 |
| 2026-09-17 | [2026년 제대군인 창업 경진대회 참가자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178931) | 국가보훈부 | K-Startup 사업공고 |
| 2026-09-17 | [「모두의 창업 프로젝트」통합 모집공고 2차](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178952) | 중소벤처기업부 | K-Startup 사업공고 |
| 2026-09-17 | [「2026 투자유치 프로그램: 멘토링」참가기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179064) | 수원도시재단 | K-Startup 사업공고 |
| 2026-09-17 | [[용인시산업진흥원] 2026년 용인 오픈이노베이션 교류회 4회차(AI)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179099) | 알파브라더스 | K-Startup 사업공고 |
| 2026-09-17 | [[부산울산경남센터] 사회적협동조합 설립인가 및 경영공시 교육 안내 (9.16.(수), 9.17.(목) - 온라인병행)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179083) | 한국사회적기업진흥원 부산울산경남센터 | K-Startup 사업공고 |
| 2026-09-17 | [2026년 웰컴 투 팁스 3차 참가기업 모집 (동남권)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179126) | (주)로우파트너스 | K-Startup 사업공고 |
| 2026-09-17 | [2026 서울창업허브 공덕 9월 허브아워 - 투자, 수출 컨설팅](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179152) | (재)서울경제진흥원 | K-Startup 사업공고 |
| 2026-09-17 | [2026년 SVC Seoul 인턴십 프로그램 학생인턴 모집공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179200) | 창업진흥원 | K-Startup 사업공고 |

## 스타트업 뉴스

| 날짜 | 제목 | 출처 |
|---|---|---|
| 2026-09-15 | [병뚜껑의 이취, AI가 가려낸다…일리아스AI, 일본 제조현장서 3개월 PoC](https://www.venturesquare.net/1113923/) | 벤처스퀘어 |
| 2026-09-15 | [제주시부터 울릉·남해까지…가을 바닷길 렌터카 최대 2만2000원 할인](https://www.venturesquare.net/1113931/) | 벤처스퀘어 |
| 2026-09-15 | [한 번의 IR을 다음 투자 미팅으로…대구 스타트업 6개사, 수도권 VC 만났다](https://www.venturesquare.net/1113934/) | 벤처스퀘어 |
| 2026-09-15 | [좋은 기술을 ‘투자자의 언어’로…대구 스타트업 8개사, IP 전략 들고 IR 무대](https://www.venturesquare.net/1113946/) | 벤처스퀘어 |
| 2026-09-15 | [전자책 서재도 ‘꾸미는 공간’으로…리디, 책장 커버·통합검색 개편](https://www.venturesquare.net/1113953/) | 벤처스퀘어 |
| 2026-09-15 | [베트남이 끌고 라이브가 밀었다…쇼피 9.9서 한국 셀러 판매량 7배](https://www.venturesquare.net/1113956/) | 벤처스퀘어 |
| 2026-09-15 | [도면이 공장 데이터로 이어질 때…위즈코어, IMTS서 CAD·제조 AI 연결](https://www.venturesquare.net/1113964/) | 벤처스퀘어 |
| 2026-09-15 | [이익보다 ‘함께 행복한 기업’…행복한경영대학 20기 CEO 83명 입학](https://www.venturesquare.net/1113971/) | 벤처스퀘어 |
| 2026-09-15 | [임플란트 품질, 표면 잔여물까지 본다…덴티스 AXEL 독일 인증](https://www.venturesquare.net/1113982/) | 벤처스퀘어 |
| 2026-09-15 | [풍력 목표를 실제 발전소로…KGCCI, 한·독 200명과 ‘실행 조건’ 논의](https://www.venturesquare.net/1113989/) | 벤처스퀘어 |
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
