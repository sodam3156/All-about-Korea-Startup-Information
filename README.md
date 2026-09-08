# All-about-Korea-Startup-Information

세종 청년창업 기관 공지 · 정부 지원사업 공고 · 스타트업 뉴스를 **매일 14:00 KST에 자동 수집**하는 저장소.
GitHub Actions가 수집→중복제거→상세저장→아래 대시보드 갱신→텔레그램 브리핑까지 수행한다 (git-scraping — 서버·DB·API 비용 없음).

**완전 규칙 기반**: 소스마다 공식 API/RSS 또는 정규식 파서를 쓴다(LLM 미사용, 고정비 $0). 대신 사이트가 개편되면 파서가 조용히 0건을 낼 수 있어, 같은 소스가 **연속 2회 이상 0건**이면 `data/source_health.json`에 기록하고 다이제스트에 "⚠️ 소스 점검 필요"로 경고한다 — 이게 규칙 기반의 유일한 약점(개편에 안 깨지는 AI 추출 대비)을 메우는 피드백 루프다.

<!-- AUTO:START -->

_자동 갱신: 2026-09-08 (KST)_

## 마감 임박 지원사업

| 마감 | 공고 | 기관 | 출처 |
|---|---|---|---|
| 2026-09-08 | [[Try Everything 2026] 서울시 글로벌 창업행사 사전등록 신청](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178756) | 재단법인 서울경제진흥원 | K-Startup 사업공고 |
| 2026-09-08 | [[SBS문화재단x한투AC] Media'X' challenge 2026 ｜ 총 5.2억원 상당 상금 및 크레딧 지급](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178863) | 한국투자액셀러레이터 | K-Startup 사업공고 |
| 2026-09-08 | [2026년 하반기 D-테스트베드 참여자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178949) | 한국핀테크지원센터 | K-Startup 사업공고 |
| 2026-09-08 | [서울창업허브 공덕 x Saint Clair - 유럽 진출 토크 콘서트](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179026) | (재)서울경제진흥원 | K-Startup 사업공고 |
| 2026-09-08 | [[강동구 청년해냄센터] 전문분야 창업멘토링 9월 참가자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178999) | 강동구 청년해냄센터 | K-Startup 사업공고 |
| 2026-09-08 | [2026 강원랜드 상생형 창업·벤처기업 지원사업](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179044) | 한국생산성본부 | K-Startup 사업공고 |
| 2026-09-08 | [청년창업 IR 경진대회](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179101) | 달서구 청년창업지원센터 | K-Startup 사업공고 |
| 2026-09-08 | [2026 경기 고양 MICE 연계 창업리그 참가자 모집 공고 (모집기간 연장)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179095) | (재)고양국제박람회재단 | K-Startup 사업공고 |
| 2026-09-09 | [「민관협력 오픈이노베이션 지원」2026년 '규제자유특구 지원' 창업기업 모집공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178975) | 중소벤처기업부장관 | K-Startup 사업공고 |
| 2026-09-09 | [2026년 WoW!메이커스 IR클리닉 참여기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178992) | 수원대학교 WoW!메이커스 | K-Startup 사업공고 |
| 2026-09-09 | [[경과원 X 노션] &apos;노션으로 만드는 스타트업 AI OS&apos; 특강 참여자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179030) | 경기도경제과학진흥원 | K-Startup 사업공고 |
| 2026-09-09 | [중동상황대응 [수출위기극복 및 대체시장 개척] 심화컨설팅](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179017) | 서울경제진흥원 | K-Startup 사업공고 |
| 2026-09-09 | [2026년도 ｢서울 관광스타트업 육성 지원(상생협력) 사업｣ 공모](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179008) | 서울특별시장 | K-Startup 사업공고 |
| 2026-09-09 | [2026년 『고양시 투자 레벨업 프로그램 NEXT ROUND』 참가기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179003) | 고양산업진흥원 | K-Startup 사업공고 |
| 2026-09-09 | [2026년 충북 바이오 오픈이노베이션 사업 참여 스타트업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178998) | 오송첨단의료산업진흥재단 | K-Startup 사업공고 |
| 2026-09-09 | [[서울여자대학교 창업보육센터] 신규 입주기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179056) | 서울여자대학교 창업보육센터 | K-Startup 사업공고 |
| 2026-09-09 | [2026 서울 오픈이노베이션 인사이트 데이](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179028) | (주)마크앤컴퍼니 | K-Startup 사업공고 |
| 2026-09-09 | [관악 마케팅 지원 참여자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179076) | 관악구청 | K-Startup 사업공고 |
| 2026-09-09 | [스타트업 자금조달 WEEK (투자) 프로그램 참가기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179074) | 서강대학교 판교캠퍼스사업단 | K-Startup 사업공고 |
| 2026-09-10 | [2026년 CAU Tech-Connecting Day [중앙대학교 기술세미나 및 기술상담회]](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178924) | 중앙대학교 창업보육센터(다빈치) | K-Startup 사업공고 |

## 스타트업 뉴스

| 날짜 | 제목 | 출처 |
|---|---|---|
| 2026-09-07 | [불꽃이 뜨는 날, 사옥 문을 연다…에버스핀의 5년째 ‘고객 동행’](https://www.venturesquare.net/1111410/) | 벤처스퀘어 |
| 2026-09-07 | [한 번의 후원이 10년 동행으로…SAP코리아·전인지, 2027년까지 파트너십 연장](https://www.venturesquare.net/1111430/) | 벤처스퀘어 |
| 2026-09-07 | [원료부터 양극재까지 공급망 잇는다…코스모신소재, 피노에 150억 원 투자](https://www.venturesquare.net/1111433/) | 벤처스퀘어 |
| 2026-09-07 | [기기 안에 들어간 AI, 모델 구조도 함께 노출된다…쿤텍·ETRI ‘선택적 보호’ 기술 개발](https://www.venturesquare.net/1111446/) | 벤처스퀘어 |
| 2026-09-07 | [연구실 원천기술, 투자시장과 만난다…라플라스·ETRI 딥테크 6곳 피칭](https://www.venturesquare.net/1111449/) | 벤처스퀘어 |
| 2026-09-07 | [북미 3곳 찍고 유럽 첫 고객…엠로 ‘케이던시아’, 에너지 공급망에 들어간다](https://www.venturesquare.net/1111460/) | 벤처스퀘어 |
| 2026-09-07 | [AI 강국의 조건은 생태계 순환…스타트업얼라이언스, 국회에 12개 정책과제 제안](https://www.venturesquare.net/1111473/) | 벤처스퀘어 |
| 2026-09-07 | [AI 말라리아 진단, 개별 병원 넘어 국가 체계로…노을 ‘마이랩’ 베냉 공공조달](https://www.venturesquare.net/1111478/) | 벤처스퀘어 |
| 2026-09-07 | [CCTV부터 출입통제까지 한 화면에…버카다, 현대차 사옥서 AI 물리보안 시연](https://www.venturesquare.net/1111495/) | 벤처스퀘어 |
| 2026-09-07 | [제주 스타트업 투자에서 바이오·우주로…JDC, 베트남과 미래산업 협력 논의](https://www.venturesquare.net/1111503/) | 벤처스퀘어 |
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
