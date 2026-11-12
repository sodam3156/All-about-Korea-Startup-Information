# All-about-Korea-Startup-Information

세종 청년창업 기관 공지 · 정부 지원사업 공고 · 스타트업 뉴스를 **매일 14:00 KST에 자동 수집**하는 저장소.
GitHub Actions가 수집→중복제거→상세저장→아래 대시보드 갱신→텔레그램 브리핑까지 수행한다 (git-scraping — 서버·DB·API 비용 없음).

**완전 규칙 기반**: 소스마다 공식 API/RSS 또는 정규식 파서를 쓴다(LLM 미사용, 고정비 $0). 대신 사이트가 개편되면 파서가 조용히 0건을 낼 수 있어, 같은 소스가 **연속 2회 이상 0건**이면 `data/source_health.json`에 기록하고 다이제스트에 "⚠️ 소스 점검 필요"로 경고한다 — 이게 규칙 기반의 유일한 약점(개편에 안 깨지는 AI 추출 대비)을 메우는 피드백 루프다.

<!-- AUTO:START -->

_자동 갱신: 2026-11-12 (KST)_

## 마감 임박 지원사업

| 마감 | 공고 | 기관 | 출처 |
|---|---|---|---|
| 2026-11-12 | [[숭실대학교 캠퍼스타운] 생성형 AI 활용 기초 및 업무 자동화 과정 참여자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179458) | 숭실대학교 캠퍼스타운사업단 | K-Startup 사업공고 |
| 2026-11-12 | [2026년 남구다운 청년 창업 지원사업 통합공고(수정)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179486) | (사)대구경북고용복지연구원 | K-Startup 사업공고 |
| 2026-11-12 | [[해수부] 2026년 해양수산 통합데모데이 참가자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179533) | 부산지역대학연합기술지주(주) | K-Startup 사업공고 |
| 2026-11-12 | [[도봉구청년창업센터] 2026 도봉 오픈 창업 스쿨 - 2027 NEXT STAGE](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179635) | 도봉구 청년창업센터장 | K-Startup 사업공고 |
| 2026-11-12 | [「2026 KOSAㆍ아이티센글로벌ㆍ더존비즈온 공동 IR DAY」참가기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179648) | KOSA · 아이티센글로벌 · 더존비즈온 | K-Startup 사업공고 |
| 2026-11-12 | [[온라인·무료] 재고·코딩·PG심사 없이, 오늘 여는 내 쇼핑몰](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179651) | 스쿨모아 주식회사 | K-Startup 사업공고 |
| 2026-11-12 | [[로컬창업트랙 2기]기억되는 브랜드가 되는 법](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179678) | 관악구청 | K-Startup 사업공고 |
| 2026-11-12 | [전북핀테크지원센터 「핀테크 라이징 스타 챌린지」참가자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179746) | (재)전북창조경제혁신센터 | K-Startup 사업공고 |
| 2026-11-13 | [한양대학교 ERICA 캠퍼스혁신파크 산학연혁신허브 입점자 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179441) | 한국토지주택공사 | K-Startup 사업공고 |
| 2026-11-13 | [[무료 AI 역량강화 교육] 글로벌 공공조달 AX 전략 전문가 과정 (선착순 모집)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179497) | (주)글로벌창업연구소 | K-Startup 사업공고 |
| 2026-11-13 | [AI 활용 소상공인 및 전통시장 매니저 실무 역량 과정 참가자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179552) | 경남지방중소벤처기업청 | K-Startup 사업공고 |
| 2026-11-13 | [2027년 상반기 「IBK창공(創工)」혁신창업기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179542) | IBK기업은행  | K-Startup 사업공고 |
| 2026-11-13 | [제6차 해양수산 투자기관협의회(정기IR) 참여기업 모집공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179615) | 해양수산과학기술진흥원 | K-Startup 사업공고 |
| 2026-11-13 | [[2027 Dream Play] LGD 스타트업 육성프로그램 9기 참가기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179603) | 엔슬파트너스 | K-Startup 사업공고 |
| 2026-11-13 | [NCI 민/관/학 창업포럼(2026 강북창업포럼) 참관객 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179649) | 강북청년창업마루 | K-Startup 사업공고 |
| 2026-11-13 | [2026 년 홍익대 아트앤디자인테크 창업보육센터 입주기업 모집(2 차) 공고문](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179665) | 홍익대학교 아트앤디자인테크 창업보육센터 | K-Startup 사업공고 |
| 2026-11-13 | [2026년 5차 국립공주대학교 창업보육센터 입주기업 모집 연장공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179691) | 국립공주대학교 산학협력단 | K-Startup 사업공고 |
| 2026-11-13 | [2026 포스코기술투자 TIPS Scout 참여 스타트업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179686) | 파트너스라운지(유) | K-Startup 사업공고 |
| 2026-11-13 | [[포항연합기술지주] 대경권 캠퍼스 IR 챔피언십](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179670) | (주) 포항연합기술지주 | K-Startup 사업공고 |
| 2026-11-13 | [청년 창업의 꿈, 『성동청년 창업이룸센터』 입주자 모집 공고【10차】](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179712) | 서울특별시 성동구청장 | K-Startup 사업공고 |

## 스타트업 뉴스

| 날짜 | 제목 | 출처 |
|---|---|---|
| 2026-11-12 | [블루포인트, 양자 QX 스케일업 3년 성과 공개…5개국 고객 확보·후속투자 161억원](https://www.venturesquare.net/1127844/) | 벤처스퀘어 |
| 2026-11-12 | [유이크, 라이즈 ‘리틀라이즈’ 캐릭터 립밤 출시…3년 협업 이어간다](https://www.venturesquare.net/1127847/) | 벤처스퀘어 |
| 2026-11-12 | [더화이트커뮤니케이션, 고객 상담부터 CRM까지 연결하는 AI 플랫폼 ‘이지아이’ 출시](https://www.venturesquare.net/1127904/) | 벤처스퀘어 |
| 2026-11-12 | [AI를 도입하는 시대에서 성과를 만드는 시대로…아이벡스 프론티어 2026](https://www.venturesquare.net/1127921/) | 벤처스퀘어 |
| 2026-11-12 | [차즘 운영사 디자인앤프랙티스, 우리금융 ‘시너지 스타상’ 수상…전략적 투자 성과 인정](https://www.venturesquare.net/1127920/) | 벤처스퀘어 |
| 2026-11-12 | [알스퀘어, 카드매출 데이터로 건물·매장 경쟁력 분석…상업용 부동산 투자 판단 정교화](https://www.venturesquare.net/1127940/) | 벤처스퀘어 |
| 2026-11-12 | [카카오벤처스, 힉스필드와 손잡았다…초기 스타트업에 AI 영상 제작 지원](https://www.venturesquare.net/1127943/) | 벤처스퀘어 |
| 2026-11-12 | [리필드·아모레퍼시픽·한국콜마·코스맥스, 논문으로 증명하는 K뷰티 경쟁력](https://www.venturesquare.net/1127953/) | 벤처스퀘어 |
| 2026-11-12 | [초기투자액셀러레이터협회, 홍콩 메가쇼서 소상공인 해외 진출 지원…261건 수출 상담 성과](https://www.venturesquare.net/1127960/) | 벤처스퀘어 |
| 2026-11-12 | [EO·초기투자액셀러레이터협회, ‘BOLD SEOUL 2026’ 개최…창업가·투자자 역삼에 모인다](https://www.venturesquare.net/1127967/) | 벤처스퀘어 |
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
