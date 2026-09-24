# All-about-Korea-Startup-Information

세종 청년창업 기관 공지 · 정부 지원사업 공고 · 스타트업 뉴스를 **매일 14:00 KST에 자동 수집**하는 저장소.
GitHub Actions가 수집→중복제거→상세저장→아래 대시보드 갱신→텔레그램 브리핑까지 수행한다 (git-scraping — 서버·DB·API 비용 없음).

**완전 규칙 기반**: 소스마다 공식 API/RSS 또는 정규식 파서를 쓴다(LLM 미사용, 고정비 $0). 대신 사이트가 개편되면 파서가 조용히 0건을 낼 수 있어, 같은 소스가 **연속 2회 이상 0건**이면 `data/source_health.json`에 기록하고 다이제스트에 "⚠️ 소스 점검 필요"로 경고한다 — 이게 규칙 기반의 유일한 약점(개편에 안 깨지는 AI 추출 대비)을 메우는 피드백 루프다.

<!-- AUTO:START -->

_자동 갱신: 2026-09-24 (KST)_

## 마감 임박 지원사업

| 마감 | 공고 | 기관 | 출처 |
|---|---|---|---|
| 2026-09-25 | [[국비지원] AI 기반 서비스 개발·사업화 1인 창업가 캠프 7기 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178831) | 넥스트러너스 주식회사 | K-Startup 사업공고 |
| 2026-09-25 | [연구개발특구진흥재단 X 현대차증권 Corporate Venture Connect 오픈이노베이션 배치프로그램 참가기업 모집공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179098) | 연구개발특구진흥재단 | K-Startup 사업공고 |
| 2026-09-25 | [2026 천안 C-STAR Awards 기술/투자 상담회 참여기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179163) | 주식회사 킹고스프링 | K-Startup 사업공고 |
| 2026-09-26 | [앤틀러코리아 ANTLER INCEPTION 참여 기업 모집 | Build Money-making AI](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179189) | 앤틀러코리아 | K-Startup 사업공고 |
| 2026-09-27 | [하드웨어 제조 고민, 현직 엔지니어가 1:1 무료 진단합니다.](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179112) | 인탑스(주) | K-Startup 사업공고 |
| 2026-09-27 | [Midnight Korea Hackathon 2026 & Privacy Night 참가 안내](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179179) | 서울핀테크랩 | K-Startup 사업공고 |
| 2026-09-27 | [2026년 서경대학교 창업보육센터 입주기업 모집(3차)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179220) | 서경대학교 창업보육센터 | K-Startup 사업공고 |
| 2026-09-27 | [OCEANˈS TAP 해양 OI 리버스피칭 및 OI 밋업 참여기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179259) | 주관기관 | K-Startup 사업공고 |
| 2026-09-27 | [2026 글로컬 Angelwave IR Camp](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179282) | 한국엔젤투자협회 호남권 엔젤투자허브 | K-Startup 사업공고 |
| 2026-09-27 | [강남구 개포동지역 ㈜오피스허브 1인 창조기업 지원센터 입주기업 모집(1인실,2인실)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179249) | ㈜오피스허브 1인 창조기업 지원센터 | K-Startup 사업공고 |
| 2026-09-28 | [[서초창업스테이션] 서리풀 소상공인 창업 클리닉(9월) - 소상공인 1:1 컨설팅](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179048) | 서초창업스테이션 | K-Startup 사업공고 |
| 2026-09-28 | [[투자연계&사업화] 더인벤션랩 2026 엣지업 크리에이터스 4기 AX/LX Challenge 모집공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179038) | 더인벤션랩 | K-Startup 사업공고 |
| 2026-09-28 | [2026년 하반기 서울창업허브 성수 입주기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179187) | 서울경제진흥원 | K-Startup 사업공고 |
| 2026-09-28 | [2026년 강동 K-ISS멘토링센터 4차 교육 및 튜토링 과정 투자 유치 전략과 IR 피칭 스킬업](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179180) | 주식회사 이노시아 | K-Startup 사업공고 |
| 2026-09-28 | [2026년 대전 스타트업스쿨 스타트업 리딩클래스 (5회차 ㅣ 예비 및 초기창업자가 1년 안에 가장 후회하는 3가지)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179257) | 대전창조경제혁신센터 | K-Startup 사업공고 |
| 2026-09-28 | [연구개발특구진흥재단 × 대구창조경제혁신센터 「2026 이노폴리스 오픈이노베이션 밋업데이」참여기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179223) | 연구개발특구진흥재단 | K-Startup 사업공고 |
| 2026-09-28 | [2026년 하반기 경기도여성창업보육센터 입주기업 모집 연장공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179289) | 경기도일자리재단 남부사업본부장 | K-Startup 사업공고 |
| 2026-09-28 | [제7회 원주권 스타트업 커뮤니티 데이 참가자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179273) | 상지대학교 벤처창업본부  | K-Startup 사업공고 |
| 2026-09-29 | [2026 투자 유치 세미나 - 투자사 관점에서 보는 투자유치를 위한 실전 전략](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179224) | 서울창업허브 창동 | K-Startup 사업공고 |
| 2026-09-29 | [[인천] 2026년 IP창업존 51기 교육(모두의창업 연계과정) 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179271) | 인천지식재산센터 | K-Startup 사업공고 |

## 스타트업 뉴스

| 날짜 | 제목 | 출처 |
|---|---|---|
| 2026-09-23 | [케어닥, 시니어 돌봄 ‘보호’에서 일상으로…학교형 데이케어·AI·로봇 확산](https://www.venturesquare.net/1115971/) | 벤처스퀘어 |
| 2026-09-23 | [인핸스·GS칼텍스, 83만대 설비에 숙련자 노하우 연결…‘제조 암묵지 AI’ 개발](https://www.venturesquare.net/1115974/) | 벤처스퀘어 |
| 2026-09-23 | [이소영표 중기부 출범…코스포·벤처기업협회·이노비즈협회 축하 메시지 “규제혁신 기대”](https://www.venturesquare.net/1115987/) | 벤처스퀘어 |
| 2026-09-24 | [[안변의 스타트업 법률 노트] 계약서에 사인했다고 끝이 아니다…캐시워크애즈·엔비티 최대주주 분쟁이 남긴 것](https://www.venturesquare.net/1115997/) | 벤처스퀘어 |
| 2026-09-24 | [메타, AI가 안경 속으로 들어왔다…‘뮤즈’ 탑재하고 연내 100개 글래스 옵션](https://www.venturesquare.net/1116003/) | 벤처스퀘어 |
| 2026-09-24 | [위제이, 공장 지붕 찍으면 태양광 규모 계산…AI로 해외 RE100까지 연결](https://www.venturesquare.net/1116011/) | 벤처스퀘어 |
| 2026-09-24 | [충남콘텐츠진흥원·씨엔티테크, 대학생 창업팀 10곳 키운다…최종 5팀에 400만원](https://www.venturesquare.net/1116022/) | 벤처스퀘어 |
| 2026-09-24 | [노타, 로봇 AI 판단 7배 빨라졌다…NPU·GPU 맞춤 최적화로 작업속도 3배](https://www.venturesquare.net/1116031/) | 벤처스퀘어 |
| 2026-09-24 | [에스트래픽, LA 지하철 18개역 요금시스템 맡는다…100억원 유지보수 계약](https://www.venturesquare.net/1116039/) | 벤처스퀘어 |
| 2026-09-22 | [아카마이코리아, AI 인프라 코어에서 엣지까지…“연산은 분산하고 보안은 겹겹이”](https://www.venturesquare.net/1115807/) | 벤처스퀘어 |
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
