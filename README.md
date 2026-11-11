# All-about-Korea-Startup-Information

세종 청년창업 기관 공지 · 정부 지원사업 공고 · 스타트업 뉴스를 **매일 14:00 KST에 자동 수집**하는 저장소.
GitHub Actions가 수집→중복제거→상세저장→아래 대시보드 갱신→텔레그램 브리핑까지 수행한다 (git-scraping — 서버·DB·API 비용 없음).

**완전 규칙 기반**: 소스마다 공식 API/RSS 또는 정규식 파서를 쓴다(LLM 미사용, 고정비 $0). 대신 사이트가 개편되면 파서가 조용히 0건을 낼 수 있어, 같은 소스가 **연속 2회 이상 0건**이면 `data/source_health.json`에 기록하고 다이제스트에 "⚠️ 소스 점검 필요"로 경고한다 — 이게 규칙 기반의 유일한 약점(개편에 안 깨지는 AI 추출 대비)을 메우는 피드백 루프다.

<!-- AUTO:START -->

_자동 갱신: 2026-11-11 (KST)_

## 마감 임박 지원사업

| 마감 | 공고 | 기관 | 출처 |
|---|---|---|---|
| 2026-11-11 | [구로구 청년창업지원센터 일반 창업교육(하반기: 6회차): 발표평가 자료 작성 및 발표 요령](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179590) | 구로구 청년창업지원센터 | K-Startup 사업공고 |
| 2026-11-11 | [[롯데벤처스] LOTTE OPEN INNOVATION DAY 참관객 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179580) | 롯데벤처스 | K-Startup 사업공고 |
| 2026-11-11 | [2026 의왕시 청년e-Room 창업아이디어 공모전 참가자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179565) | 의왕시청 | K-Startup 사업공고 |
| 2026-11-11 | [「2026년 강원연구개발특구육성(R&D)사업」 강원 특구 배치 프로그램 1기 참여기업 모집공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179596) | 재단법인 강원창조경제혁신센터 | K-Startup 사업공고 |
| 2026-11-11 | [예비 초기 스타트업을 위한 창업 교육 프로그램 러닝메이트 9기 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179621) | 재단법인 오렌지플래닛 창업재단 | K-Startup 사업공고 |
| 2026-11-11 | [[ZUZU X 마크앤컴퍼니 집중검토] 딥테크·소부장 Pre-Seed ~ Pre-A 투자 검토 모집 (찾아가는 GF)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179657) | (주) 코드박스 Kodebox | K-Startup 사업공고 |
| 2026-11-11 | [2026년 위치정보 보호조치 교육 (7차)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179679) | (주) 아이전스 | K-Startup 사업공고 |
| 2026-11-11 | [2026년 대전 테스트베드 연계사업 공모](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179677) | 한국수자원공사 | K-Startup 사업공고 |
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

## 스타트업 뉴스

| 날짜 | 제목 | 출처 |
|---|---|---|
| 2026-11-10 | [[부산에서 발굴한 초기스타트업 ➁] 이용은 데이터스피라 대표 “돌체앤가바나가 선택한 기술, QR코드 뒤에 답이 있습니다”](https://www.venturesquare.net/1126950/) | 벤처스퀘어 |
| 2026-11-10 | [6개 스타트업에서 469개 기업으로…권혁빈 CVO와 서상봉 오렌지플래닛 센터장이 지켜온 12년의 창업 지원 철학](https://www.venturesquare.net/1127413/) | 벤처스퀘어 |
| 2026-11-11 | [비대면진료 30일 처방은 평생 한 번?…원산협이 제기한 규제의 역설](https://www.venturesquare.net/1127498/) | 벤처스퀘어 |
| 2026-11-11 | [인텔리즈, 숙련자의 검사 노하우를 AI로 구현하다…불량 검출 넘어 자율제조로](https://www.venturesquare.net/1127514/) | 벤처스퀘어 |
| 2026-11-11 | [제이솔루션 정진수 대표, 버려진 실리콘에 ‘팽창할 공간’을 설계하다](https://www.venturesquare.net/1127523/) | 벤처스퀘어 |
| 2026-11-11 | [암세포의 ‘멈춤’ 신호를 뒤집다…카바이오테라퓨틱스 이헌주 대표의 CAR-T 도전](https://www.venturesquare.net/1127530/) | 벤처스퀘어 |
| 2026-11-11 | [두나무 D-CON 2026, 디지털자산 제도화의 갈림길…“속도냐, 유연성이냐”](https://www.venturesquare.net/1127500/) | 벤처스퀘어 |
| 2026-11-11 | [제주창조경제혁신센터, 로컬기업 16개사에 200억 원 구매의향 확보…수출계약 16억 원](https://www.venturesquare.net/1127507/) | 벤처스퀘어 |
| 2026-11-11 | [매쉬업벤처스, 259억 원 민간펀드 결성…AI·딥테크 극초기 투자 확대](https://www.venturesquare.net/1127549/) | 벤처스퀘어 |
| 2026-11-11 | [티비지파트너스, 초고령사회 겨냥한 ‘롱제비티랩’ 출범…헬스케어·에이지테크 스타트업 모집](https://www.venturesquare.net/1127564/) | 벤처스퀘어 |
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
