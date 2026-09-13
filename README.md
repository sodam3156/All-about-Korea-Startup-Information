# All-about-Korea-Startup-Information

세종 청년창업 기관 공지 · 정부 지원사업 공고 · 스타트업 뉴스를 **매일 14:00 KST에 자동 수집**하는 저장소.
GitHub Actions가 수집→중복제거→상세저장→아래 대시보드 갱신→텔레그램 브리핑까지 수행한다 (git-scraping — 서버·DB·API 비용 없음).

**완전 규칙 기반**: 소스마다 공식 API/RSS 또는 정규식 파서를 쓴다(LLM 미사용, 고정비 $0). 대신 사이트가 개편되면 파서가 조용히 0건을 낼 수 있어, 같은 소스가 **연속 2회 이상 0건**이면 `data/source_health.json`에 기록하고 다이제스트에 "⚠️ 소스 점검 필요"로 경고한다 — 이게 규칙 기반의 유일한 약점(개편에 안 깨지는 AI 추출 대비)을 메우는 피드백 루프다.

<!-- AUTO:START -->

_자동 갱신: 2026-09-13 (KST)_

## 마감 임박 지원사업

| 마감 | 공고 | 기관 | 출처 |
|---|---|---|---|
| 2026-09-13 | [2026년 부산 핀테크허브 입주기업 모집공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178945) | (사)글로벌핀테크산업진흥센터 | K-Startup 사업공고 |
| 2026-09-13 | [중앙대-금천구 창업 협력공간(창업교육스튜디오) 입주자 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179042) | 중앙대학교 산학협력단 | K-Startup 사업공고 |
| 2026-09-13 | [중앙대-금천구 창업 협력공간(혁신지원거점센터) 입주자 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179040) | 중앙대학교 산학협력단 | K-Startup 사업공고 |
| 2026-09-13 | [2026년 28청춘창업소 액셀러레이팅 창업 역량강화교육: 투자유치 및 IR 전략](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179090) | 고양산업진흥원 | K-Startup 사업공고 |
| 2026-09-13 | [2026년 SaaS 전환지원센터xAWS SaaS 현대화 교육 3회차 참가자 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179082) | 정보통신산업진흥원, SaaS 전환지원센터 | K-Startup 사업공고 |
| 2026-09-14 | [[무료 AI 역량강화 교육] 생성형 AI 기반 무역 컴플라이언스 및 관세·ESG 리스크 최적화](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178798) | (주)글로벌창업연구소 | K-Startup 사업공고 |
| 2026-09-14 | [2026년 모두의 창업 글로벌 재외국민 프로그램 참여자 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178896) | 중소벤처기업부 | K-Startup 사업공고 |
| 2026-09-14 | [2026년 6회차 지식재산권 무료 초청교육 수요조사](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178885) | 한국특허정보원 | K-Startup 사업공고 |
| 2026-09-14 | [광명업사이클아트센터 2026년 하반기 가상오피스 지원기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178930) | 광명시 | K-Startup 사업공고 |
| 2026-09-14 | [제2회 도봉 창업 포럼 (NCI 민.관.학 창업 포럼) : 대전환의 시대, 기술과 사회적 가치가 여는 창업의 새로운 기회(기조강연 : 과학크리에이터 궤도)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178980) | 도봉구 청년창업센터장 | K-Startup 사업공고 |
| 2026-09-14 | [2026년 구미시 스타트업 필드 4차 입주기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179019) | 구미전자정보기술원 | K-Startup 사업공고 |
| 2026-09-14 | [2026년 9월 동네창업학교 교육생 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179050) | 충남신용보증재단 | K-Startup 사업공고 |
| 2026-09-14 | [2026년 온디바이스AI 제품개발·제조 및 기술지원 기업모집공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179063) | 한국전자정보통신산업진흥회 | K-Startup 사업공고 |
| 2026-09-14 | [2026년 세종 스타트업 원스톱 지원센터 아카데미 3차](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179036) | 세종창조경제혁신센터 | K-Startup 사업공고 |
| 2026-09-14 | [[창업 교육] 투자자가 보는 기업 가치와 IR 전략](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179119) | 광진경제허브센터 | K-Startup 사업공고 |
| 2026-09-14 | [2026년 제4차 국립공주대학교 창업보육센터 입주기업 모집 연장공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179097) | 국립공주대학교 산학협력 | K-Startup 사업공고 |
| 2026-09-14 | [2026「판교 창업존」입주기업 및 투자사·협력기관 2차 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179084) | 경기창조경제혁신센터 | K-Startup 사업공고 |
| 2026-09-14 | [2026년 초기창업기업 마케팅 AX 지원 프로그램 「AD:START」 1기 참여기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179079) | 이미지팩토리 | K-Startup 사업공고 |
| 2026-09-14 | [[모집기간 연장] 2026 현대모비스 CSV 오픈 이노베이션 참여 기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179159) | (주)엠와이소셜컴퍼니 | K-Startup 사업공고 |
| 2026-09-14 | [SURF 2026 INCHEON (인천스타트업위크) 사전 등록 및 비즈니스 밋업 신청 오픈](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179156) | 인천창조경제혁신센터 | K-Startup 사업공고 |

## 스타트업 뉴스

| 날짜 | 제목 | 출처 |
|---|---|---|
| 2026-09-12 | [[기고] AI 시대 공공행정, 기술 도입에서 ‘현장 문제 해결’로…송석언 JDC 이사장](https://www.venturesquare.net/1112754/) | 벤처스퀘어 |
| 2026-09-12 | [21개 문항으로 최근 6개월 살핀다…트로스트, 성인 ADHD 자가점검 출시](https://www.venturesquare.net/1113123/) | 벤처스퀘어 |
| 2026-09-12 | [40개 세션, 2초 안에 언어 장벽 넘었다…엑스엘에이트, 트라이에브리싱 통번역](https://www.venturesquare.net/1113134/) | 벤처스퀘어 |
| 2026-09-12 | [서울 AI 스타트업, 타이베이서 시장성 검증한다…양 도시 혁신거점 연결](https://www.venturesquare.net/1113141/) | 벤처스퀘어 |
| 2026-09-12 | [말하고 더빙하고 영상 만든다…이스트소프트, 페르소에이아이 해외 판로 확장](https://www.venturesquare.net/1113144/) | 벤처스퀘어 |
| 2026-09-12 | [브랜드의 말을 공간으로 옮기는 법…스위트스팟, 성수서 실무 세션 연다](https://www.venturesquare.net/1113157/) | 벤처스퀘어 |
| 2026-09-12 | [담보 대신 기술력 본다…기보, 코스타리카형 기술금융 체계 구축](https://www.venturesquare.net/1113165/) | 벤처스퀘어 |
| 2026-09-12 | [무상 서비스 거절하자 ‘별점 테러’…중기부·플랫폼 6개사 해법 논의](https://www.venturesquare.net/1113168/) | 벤처스퀘어 |
| 2026-09-12 | [“기술 발견 넘어 세계로 보낸다”…서울, AI 스타트업 글로벌 성장판 키웠다](https://www.venturesquare.net/1113236/) | 벤처스퀘어 |
| 2026-09-12 | [의정부의 문제, 스타트업이 푼다…경콘진 ‘로컬 스타트업 챌린지’ 10개사 선발](https://www.venturesquare.net/1113243/) | 벤처스퀘어 |
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
