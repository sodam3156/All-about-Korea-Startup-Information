# All-about-Korea-Startup-Information

세종 청년창업 기관 공지 · 정부 지원사업 공고 · 스타트업 뉴스를 **매일 14:00 KST에 자동 수집**하는 저장소.
GitHub Actions가 수집→중복제거→상세저장→아래 대시보드 갱신→텔레그램 브리핑까지 수행한다 (git-scraping — 서버·DB·API 비용 없음).

**완전 규칙 기반**: 소스마다 공식 API/RSS 또는 정규식 파서를 쓴다(LLM 미사용, 고정비 $0). 대신 사이트가 개편되면 파서가 조용히 0건을 낼 수 있어, 같은 소스가 **연속 2회 이상 0건**이면 `data/source_health.json`에 기록하고 다이제스트에 "⚠️ 소스 점검 필요"로 경고한다 — 이게 규칙 기반의 유일한 약점(개편에 안 깨지는 AI 추출 대비)을 메우는 피드백 루프다.

<!-- AUTO:START -->

_자동 갱신: 2026-10-29 (KST)_

## 마감 임박 지원사업

| 마감 | 공고 | 기관 | 출처 |
|---|---|---|---|
| 2026-10-29 | [2027년 초격차 스타트업 프로젝트 정부 첫 실증·구매 주관기관 모집공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179428) | 중소벤처기업부 장관 | K-Startup 사업공고 |
| 2026-10-29 | [[용인시산업진흥원] 1인 창조기업 지원센터 제4차 신규 입주기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179476) | 용인시산업진흥원장 | K-Startup 사업공고 |
| 2026-10-29 | [2026 창업교육 <광명 스타트업 점프업 클래스 모집>](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179473) | 광명시 창업지원센터 | K-Startup 사업공고 |
| 2026-10-29 | [한국과학기술지주 출연(연) 기술사업화 유망기업 투자 대상 공개 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179471) | 한국과학기술지주 | K-Startup 사업공고 |
| 2026-10-29 | [2026년 5차 국립공주대학교 창업보육센터 입주기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179463) | 국립공주대학교 산학협력 | K-Startup 사업공고 |
| 2026-10-29 | [[서울경제진흥원] 세계최대 이동통신 전시회 MWC 2027 – 4YFN 서울기업관 참가기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179495) | 서울경제진흥원 | K-Startup 사업공고 |
| 2026-10-29 | [글로벌 진출을 위한 법인 전략과 창업가 네트워킹 「To Flip or Not to Flip 참가자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179534) | The Bridge Circle (TBC) | K-Startup 사업공고 |
| 2026-10-29 | [[온라인·무료] 재고·코딩·PG심사 없이, 오늘 여는 내 쇼핑몰](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179521) | 스쿨모아 주식회사 | K-Startup 사업공고 |
| 2026-10-29 | [2026년도 투자기업 발굴 플랫폼 빅웨이브(BiiG WAVE) IR사업 3회차 초격차 분야 IR 참여기업 모집공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179568) | 인천창조경제혁신센터  | K-Startup 사업공고 |
| 2026-10-29 | [기업 판로 지원 프로그램 수혜기업 모집(~10/29)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179566) | 경북대학교 스타트업지원센터장 | K-Startup 사업공고 |
| 2026-10-29 | [TIPS · LIPS를 준비하는 스타트업을 위한 IR 전략 - 제10차 DDM 벤처스타트업 아카데미](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179564) | DDM청년창업센터 유니콘 | K-Startup 사업공고 |
| 2026-10-29 | [2026년 남동발전 상생형 창업벤처기업 지원사업 참가기업 모집공고(연장)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179576) | (재)경남창조경제혁신센터 | K-Startup 사업공고 |
| 2026-10-29 | [[모집] 글로컬 미래도시 혁신 프로그램 참가팀 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179556) | 서울시립대학교 창업지원단(캠퍼스타운사업) | K-Startup 사업공고 |
| 2026-10-30 | [뉴패러다임인베스트먼트 2026년 하반기 아기유니콘 성장 프로그램 기업모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179132) | (주)뉴패러다임인베스트먼트 | K-Startup 사업공고 |
| 2026-10-30 | [2026년 국가철도공단 창업·벤처기업 지원사업 희망기업 모집공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179209) | 국가철도공단 | K-Startup 사업공고 |
| 2026-10-30 | [취약분야 상시 컨설팅 10월 참가자 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179268) | 강동구 청년해냄센터 | K-Startup 사업공고 |
| 2026-10-30 | [한국기술교육대학교 오픈이노베이션 프로그램 참여기업 모집 안내(엠아이텍 재공고·아이티센글로벌 공고)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179374) | 한국기술교육대학교 앵커사업단 | K-Startup 사업공고 |
| 2026-10-30 | [2026년 스타 IR 데모데이 참여기업 모집공고(6차)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179419) | 스타에셋파트너스 주식회사 | K-Startup 사업공고 |
| 2026-10-30 | [2026년 전남광주 제3기「지역자원 연계 청년창업 지원사업」 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179500) | 전남정보문화산업진흥원 | K-Startup 사업공고 |
| 2026-10-30 | [2026년 석탄전환지역 기업이전 사업](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179491) | 강원대학교 KNU창업혁신원장 | K-Startup 사업공고 |

## 스타트업 뉴스

| 날짜 | 제목 | 출처 |
|---|---|---|
| 2026-10-28 | [KAYTUS, AI 데이터센터 현장 유지보수 서비스 출시…장애 복구 평균 48시간에서 12시간으로](https://www.venturesquare.net/1123833/) | 벤처스퀘어 |
| 2026-10-28 | [애딧앤아크, 인스타그램 콘텐츠 맥락 분석하는 ‘애딧 렌즈’로 중기부 AI 솔루션 선정](https://www.venturesquare.net/1123842/) | 벤처스퀘어 |
| 2026-10-28 | [마이프차, 토스플레이스·당근·배민·카카오와 프랜차이즈 마케팅 전략 공유…’FMS26′ 개최](https://www.venturesquare.net/1123849/) | 벤처스퀘어 |
| 2026-10-28 | [런드리고, 5100만 벌 세탁 데이터 분석…가을 아우터 세탁 빨라지고 ‘조용한 럭셔리’ 강세](https://www.venturesquare.net/1123856/) | 벤처스퀘어 |
| 2026-10-28 | [아이벡스, 포브스코리아 ‘대한민국 AI 50’ 선정…제조 현장에 적용한 피지컬 AI 기술력 인정](https://www.venturesquare.net/1123858/) | 벤처스퀘어 |
| 2026-10-28 | [크래프톤, 사용 마친 업무용 PC 351세트 재생 기부…지역사회 디지털 접근성 지원](https://www.venturesquare.net/1123870/) | 벤처스퀘어 |
| 2026-10-28 | [피처링, 1800만 인플루언서 데이터 기반 AI 에이전트 공개…마케팅 실무 자동화 확대](https://www.venturesquare.net/1123877/) | 벤처스퀘어 |
| 2026-10-28 | [부산창경, 부산중기청·동명대·16개 진로교육지원센터와 청소년 창업교육 협력](https://www.venturesquare.net/1123885/) | 벤처스퀘어 |
| 2026-10-28 | [제주창경, 동의모감·마케마케 선정…제주 천연자원 활용한 두피 케어 제품 실증](https://www.venturesquare.net/1123891/) | 벤처스퀘어 |
| 2026-10-28 | [중기부, K-수출전략품목 188개 선정…올리브영·무신사 등과 글로벌 시장 공략](https://www.venturesquare.net/1123898/) | 벤처스퀘어 |
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
