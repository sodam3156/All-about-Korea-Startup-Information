# All-about-Korea-Startup-Information

세종 청년창업 기관 공지 · 정부 지원사업 공고 · 스타트업 뉴스를 **매일 14:00 KST에 자동 수집**하는 저장소.
GitHub Actions가 수집→중복제거→상세저장→아래 대시보드 갱신→텔레그램 브리핑까지 수행한다 (git-scraping — 서버·DB·API 비용 없음).

**완전 규칙 기반**: 소스마다 공식 API/RSS 또는 정규식 파서를 쓴다(LLM 미사용, 고정비 $0). 대신 사이트가 개편되면 파서가 조용히 0건을 낼 수 있어, 같은 소스가 **연속 2회 이상 0건**이면 `data/source_health.json`에 기록하고 다이제스트에 "⚠️ 소스 점검 필요"로 경고한다 — 이게 규칙 기반의 유일한 약점(개편에 안 깨지는 AI 추출 대비)을 메우는 피드백 루프다.

<!-- AUTO:START -->

_자동 갱신: 2026-09-02 (KST)_

## 마감 임박 지원사업

| 마감 | 공고 | 기관 | 출처 |
|---|---|---|---|
| 2026-09-02 | [[LH한국토지주택공사] 판교 제2테크노밸리 기업성장센터(F2블록) 산업시설 입주기업 추가 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178785) | 한국토지주택공사 경기남부지역본부 | K-Startup 사업공고 |
| 2026-09-02 | [『BOUNCE 2026』 &apos;스타트업 오픈이노베이션 페스타&apos; 참여 스타트업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178883) | 부산창조경제혁신센터 | K-Startup 사업공고 |
| 2026-09-02 | [디캠프 9월 오피스아워 #벤처투자·#사업협력 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178938) | 재단법인 은행권청년창업재단 | K-Startup 사업공고 |
| 2026-09-02 | [구로구 청년창업지원센터 일반 창업교육(하반기: 2회차): 스타트업 재무 (feat. 합법적인 절세방안)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178973) | 구로구 청년창업지원센터 | K-Startup 사업공고 |
| 2026-09-02 | [2026년도 &apos;빅웨이브(BiiG WAVE)&apos; IR 사업 2회차 바이오 특화 IR 참여기업 모집공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178966) | 인천창조경제혁신센터 | K-Startup 사업공고 |
| 2026-09-02 | [[차세대융합기술연구원] 2026 제조 스타트업 멘토링 Meet-up Day](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178962) | 차세대융합기술연구원 | K-Startup 사업공고 |
| 2026-09-02 | [2026 관악S밸리 성장 지원 세미나 3회](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178961) | (재)관악중소벤처진흥원 | K-Startup 사업공고 |
| 2026-09-02 | [2026 제조 스타트업 멘토링 데이](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178991) | 볼트앤너트 | K-Startup 사업공고 |
| 2026-09-02 | [「2026년 제3회 부기테크 투자쇼」상담회 참가기업 모집공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179025) | 부산기술창업투자원 | K-Startup 사업공고 |
| 2026-09-02 | [2026 4대 과학기술원 창업리그 통합 결선, GRAVITY (9/3 목)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179041) | (주)스파크랩 | K-Startup 사업공고 |
| 2026-09-03 | [2026년 창업진흥원 정책 아이디어 공모전](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178709) | 창업진흥원 | K-Startup 사업공고 |
| 2026-09-03 | [[한국투자액셀러레이터] 바른동행 3차 모집｜선발 시 최대 5억원 투자](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178844) | 한국투자액셀러레이터 | K-Startup 사업공고 |
| 2026-09-03 | [2026년 지역 혁신 Start-up Demo Day](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178900) | 차세대융합기술연구원 | K-Startup 사업공고 |
| 2026-09-03 | [충북 제37기(26년 4기) IP창업존 특화과정((예비)창업자 및 「모두의 창업」선정자 대상) 교육생 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178888) | 충북지식재산센터장 | K-Startup 사업공고 |
| 2026-09-03 | [[도봉구 청년창업센터] 2026 도봉 청년창업 아이디어 경진대회 참가자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178914) | 도봉구 청년창업센터장 | K-Startup 사업공고 |
| 2026-09-03 | [2026년 Tokyo PMF·GTM 프로그램 창업기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178953) | 창업진흥원장 | K-Startup 사업공고 |
| 2026-09-03 | [2026년 서울지식재산센터 소상공인 지식재산 인식제고 & 창업 교육 안내 (9/3, 9/11)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179034) | 서울경제진흥원 | K-Startup 사업공고 |
| 2026-09-03 | [2026 이화여대 모두의 창업 2기 프로젝트 사업설명회](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179016) | 이화여자대학교  창업지원단 | K-Startup 사업공고 |
| 2026-09-03 | [[추가모집] 2026 창업경진대회 모의투자자 모집(~9.3. 14:00)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179065) | 강북청년창업마루 | K-Startup 사업공고 |
| 2026-09-04 | [2026년 라이브커머스 플랫폼을 활용한 쇼호스트 교육생 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178766) | 경기도경제과학진흥원 | K-Startup 사업공고 |

## 스타트업 뉴스

| 날짜 | 제목 | 출처 |
|---|---|---|
| 2026-09-01 | [위성도 ‘5년 내 폐기’ 시대…스페이스랩, 저독성 추력기로 시드 투자 유치](https://www.venturesquare.net/1110174/) | 벤처스퀘어 |
| 2026-09-01 | [국가 AI 모델, 국민 서비스까지 가볍게 돌린다…노타 ‘모두의 AI’ 참여](https://www.venturesquare.net/1110186/) | 벤처스퀘어 |
| 2026-09-01 | [100일 걸리던 임상 데이터 표준화, 30일대로…제이앤피메디 ‘프리 갈리앵 코리아’ 최종 후보](https://www.venturesquare.net/1110190/) | 벤처스퀘어 |
| 2026-09-01 | [러닝하다 줍깅, 등산하며 클린 하이킹…당근, 동네모임으로 기후행동 잇는다](https://www.venturesquare.net/1110198/) | 벤처스퀘어 |
| 2026-09-01 | [4년 만에 매출 15배…바이트랩, 포브스 아시아 ‘100대 유망기업’ 선정](https://www.venturesquare.net/1110201/) | 벤처스퀘어 |
| 2026-09-01 | [산업도시 울산에 500억원 벤처 모펀드…지역 스타트업에 자금 흐른다](https://www.venturesquare.net/1110048/) | 벤처스퀘어 |
| 2026-09-01 | [[VS기획] JP모간에서 읽은 2026 글로벌 헬스케어 트렌드, K-스타트업은 준비됐나](https://www.venturesquare.net/1108818/) | 벤처스퀘어 |
| 2026-09-02 | [씨엔티테크·네이버클라우드, 초기 스타트업과 협업 찾는다…오픈이노베이션 밋업 모집](https://www.venturesquare.net/1110234/) | 벤처스퀘어 |
| 2026-09-02 | [송정 주민 공간이 워케이션 거점으로…부산창경, 지역 상권과 연결한다](https://www.venturesquare.net/1110237/) | 벤처스퀘어 |
| 2026-09-02 | [바이오미, 슈퍼박테리아 겨냥 마이크로바이옴 치료제 첫 환자 투여](https://www.venturesquare.net/1110244/) | 벤처스퀘어 |
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
