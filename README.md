# All-about-Korea-Startup-Information

세종 청년창업 기관 공지 · 정부 지원사업 공고 · 스타트업 뉴스를 **매일 14:00 KST에 자동 수집**하는 저장소.
GitHub Actions가 수집→중복제거→상세저장→아래 대시보드 갱신→텔레그램 브리핑까지 수행한다 (git-scraping — 서버·DB·API 비용 없음).

**완전 규칙 기반**: 소스마다 공식 API/RSS 또는 정규식 파서를 쓴다(LLM 미사용, 고정비 $0). 대신 사이트가 개편되면 파서가 조용히 0건을 낼 수 있어, 같은 소스가 **연속 2회 이상 0건**이면 `data/source_health.json`에 기록하고 다이제스트에 "⚠️ 소스 점검 필요"로 경고한다 — 이게 규칙 기반의 유일한 약점(개편에 안 깨지는 AI 추출 대비)을 메우는 피드백 루프다.

<!-- AUTO:START -->

_자동 갱신: 2026-08-21 (KST)_

## 마감 임박 지원사업

| 마감 | 공고 | 기관 | 출처 |
|---|---|---|---|
| 2026-08-21 | [2026 KB스타터스 전문가 세미나](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178748) | 서울창조경제혁신센터 | K-Startup 사업공고 |
| 2026-08-21 | [2026년 재도전 아이디어 경진대회 참가자 모집 (~08.21)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178738) | (재)대전창조경제혁신센터  | K-Startup 사업공고 |
| 2026-08-21 | [[창원산업진흥원] CES2027 참가기업 지원사업 참가기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178679) | (재)창원산업진흥원장 | K-Startup 사업공고 |
| 2026-08-21 | [2026년 전주 로컬브랜딩 아이디어 해커톤 참가팀 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178675) | 전주시지역소통협력센터 | K-Startup 사업공고 |
| 2026-08-21 | [[숭실대학교 캠퍼스타운] 2026 숭실 스타트업 아카데미 8월 참여자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178666) | 숭실대학교 캠퍼스타운사업단 | K-Startup 사업공고 |
| 2026-08-21 | [2026년 28청춘창업소 액셀러레이팅 프로그램 전문가 멘토링 2차](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178815) | 고양산업진흥원 | K-Startup 사업공고 |
| 2026-08-21 | [2026 빅웨이브 글로벌(일본5차) - ILS2026 참여기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178794) | 인천창조경제혁신센터 대표이사 | K-Startup 사업공고 |
| 2026-08-21 | [중견기업 스타트업 동행라운지(참여 스타트업 모집)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178784) | 한국산업지능화협회  | K-Startup 사업공고 |
| 2026-08-21 | [2026년 하반기 DDP B the B(비더비) 뷰티테크·뷰티 디바이스 전시·체험 및 테스트베드 지원기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178775) | 재단법인 서울경제진흥원 | K-Startup 사업공고 |
| 2026-08-21 | [[인천] 2026년 IP창업존 50기 교육생 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178767) | 인천지식재산센터 | K-Startup 사업공고 |
| 2026-08-21 | [2026년 대전 스타트업 원스톱 지원센터 아카데미 1차](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178838) | 대전창조경제혁신센터 | K-Startup 사업공고 |
| 2026-08-21 | [[2026년 지역창업페스티벌 연계] 2026 스타트업 코리아 투자위크(SIW) 투자사, 유관기관, 스타트업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178826) | 대전창조경제혁신센터 | K-Startup 사업공고 |
| 2026-08-21 | [2026년 초기창업패키지 로켓십 IR 경진대회 참가기업 모집 (1회차: AI·빅데이터)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178824) | 씨엔티테크(주) | K-Startup 사업공고 |
| 2026-08-21 | [2026년 기술기반 창업 스케일업 지원 액셀러레이팅 프로그램 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178819) | (주)티비즈 | K-Startup 사업공고 |
| 2026-08-21 | [2026년 서울시 기후테크 3D프린팅 장비 활용 교육](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178813) | 서울기후테크산업지원센터장 | K-Startup 사업공고 |
| 2026-08-21 | [제10회 소셜벤처 혁신경연대회 참여기업 모집 (~8/21 16:00)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178811) | (주)엠와이소셜컴퍼니 | K-Startup 사업공고 |
| 2026-08-21 | [강남구 개포동지역 ㈜오피스허브 1인 창조기업 지원센터 입주기업 모집(1인실,2인실)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178877) | ㈜오피스허브 1인 창조기업 지원센터 | K-Startup 사업공고 |
| 2026-08-21 | [2026년 창업 준비 아카데미 [원석 발굴 창업캠프 2차] 참가자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178852) | 광운대학교 NCI창업패키지사업단 | K-Startup 사업공고 |
| 2026-08-21 | [2026년 남동발전 창업·Start-UP 서포터스 지원사업 참가기업 모집공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178836) | (재)경남창조경제혁신센터 | K-Startup 사업공고 |
| 2026-08-21 | [성남 기후테크 UpSkill 아카데미 Vol.1 - 기후테크 시장 현황과 투자트렌드](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178882) | 도시혁신그룹 무브먼트 주식회사 | K-Startup 사업공고 |

## 스타트업 뉴스

| 날짜 | 제목 | 출처 |
|---|---|---|
| 2026-08-20 | [인수 대신 새 법인으로 규제 문턱 넘었다…비트고코리아, 국내 VASP 수리](https://www.venturesquare.net/1107433/) | 벤처스퀘어 |
| 2026-08-20 | [페이커가 에이블리 신입사원으로…T1 웹예능·한정 굿즈 동시 공개](https://www.venturesquare.net/1107438/) | 벤처스퀘어 |
| 2026-08-20 | [에이블리 광고가 설치·구매로 이어졌나…에어브릿지, MMP 첫 연동](https://www.venturesquare.net/1107449/) | 벤처스퀘어 |
| 2026-08-20 | [문서를 읽는 데서 업무를 끝내는 AI로…한국딥러닝, ‘무개입률’ 승부](https://www.venturesquare.net/1107456/) | 벤처스퀘어 |
| 2026-08-20 | [볶음기·세척기·면삶기 한 화면에서…프리키친랩, LG전자·블루포인트 시드투자](https://www.venturesquare.net/1107463/) | 벤처스퀘어 |
| 2026-08-20 | [소스코드 외부 전송 없이 AI 코딩…팀스파르타, ‘AI 서밋 서울 2026’서 AX 포트리스 공개](https://www.venturesquare.net/1107471/) | 벤처스퀘어 |
| 2026-08-20 | [172억뷰 ‘아기상어’ 영상 속 소년, 솔로 아티스트로…첫 싱글 ‘WAVE’](https://www.venturesquare.net/1107479/) | 벤처스퀘어 |
| 2026-08-20 | [계약서 서식·법률 용어 그대로…하비, 문서 번역 엔진으로 딥엘 채택](https://www.venturesquare.net/1107482/) | 벤처스퀘어 |
| 2026-08-20 | [환급 먼저, 이용료는 나중…삼쩜삼 금액 변동 문의 60% 줄었다](https://www.venturesquare.net/1107493/) | 벤처스퀘어 |
| 2026-08-20 | [문서 만들고 복지 신청 돕는 AI…제논, ‘모두의 제나’ 9월 출시](https://www.venturesquare.net/1107500/) | 벤처스퀘어 |
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
