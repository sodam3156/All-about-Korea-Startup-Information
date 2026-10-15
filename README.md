# All-about-Korea-Startup-Information

세종 청년창업 기관 공지 · 정부 지원사업 공고 · 스타트업 뉴스를 **매일 14:00 KST에 자동 수집**하는 저장소.
GitHub Actions가 수집→중복제거→상세저장→아래 대시보드 갱신→텔레그램 브리핑까지 수행한다 (git-scraping — 서버·DB·API 비용 없음).

**완전 규칙 기반**: 소스마다 공식 API/RSS 또는 정규식 파서를 쓴다(LLM 미사용, 고정비 $0). 대신 사이트가 개편되면 파서가 조용히 0건을 낼 수 있어, 같은 소스가 **연속 2회 이상 0건**이면 `data/source_health.json`에 기록하고 다이제스트에 "⚠️ 소스 점검 필요"로 경고한다 — 이게 규칙 기반의 유일한 약점(개편에 안 깨지는 AI 추출 대비)을 메우는 피드백 루프다.

<!-- AUTO:START -->

_자동 갱신: 2026-10-15 (KST)_

## 마감 임박 지원사업

| 마감 | 공고 | 기관 | 출처 |
|---|---|---|---|
| 2026-10-15 | [2026년 하반기 화성시 벤처인증 비용 지원사업](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178737) | (재)화성산업진흥원 | K-Startup 사업공고 |
| 2026-10-15 | [26년 10월 스타트업 언론 홍보 지원사업 참가사 모집 공고(1차)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179361) | 스타트업 데일리 | K-Startup 사업공고 |
| 2026-10-15 | [[부산울산경남센터] 사회적협동조합 설립인가 및 경영공시 교육 안내 (10.14.(수), 10.15.(목) - 온라인병행)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179337) | 한국사회적기업진흥원 부산울산경남센터 | K-Startup 사업공고 |
| 2026-10-15 | [(Plug in: Tokyo) 일본 도쿄 Startup JAPAN expo 2026 참여 스타트업 모집(~10/15)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179326) | (재)부산창조경제혁신센터 | K-Startup 사업공고 |
| 2026-10-15 | [[강동구 청년해냄센터] 고덕비즈밸리 강동U1센터 청년창업공간 입주기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179402) | 강동구 청년해냄센터 | K-Startup 사업공고 |
| 2026-10-15 | [[숭실대학교 캠퍼스타운 x 스팩스페이스] 생성형 AI활용 사업계획서 마스터링 과정 참여자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179372) | 숭실대학교 캠퍼스타운사업단 | K-Startup 사업공고 |
| 2026-10-15 | [모두의 창업 등 정부지원사업 완벽 대비! 「1:1 맞춤형 창업 멘토링」 참가자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179422) | 강남구여성능력개발센터 | K-Startup 사업공고 |
| 2026-10-15 | [(창업도시조성프로젝트)울산 벤처빌더 플랫폼(Step1) 참여팀 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179469) | (재)울산창조경제혁신센터 | K-Startup 사업공고 |
| 2026-10-16 | [2026년 전시회 부스 지원 참여 소상공인 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179217) | 중소상공인희망재단 | K-Startup 사업공고 |
| 2026-10-16 | [ETRI 기술활용 신사업 모델 공모전](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179280) | 에트리홀딩스 | K-Startup 사업공고 |
| 2026-10-16 | [2026년 특허출원·등록 비용 바우처 지원사업 14차(하반기 7차)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179356) | (사)한국중소기업발전협회 | K-Startup 사업공고 |
| 2026-10-16 | [2026 경기도 ESG 인식확산 교육 (5~7회차) 참여자 모집 안내](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179325) | ESGi 이에스지아이 | K-Startup 사업공고 |
| 2026-10-16 | [[창업] 창업가를 위한 IR 피칭 기초 부스팅](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179414) | 마포청년창업취업지원센터 나루 | K-Startup 사업공고 |
| 2026-10-16 | [트레일 신산업 로컬창업지원 참여기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179396) | (주)크립톤 전북지사 | K-Startup 사업공고 |
| 2026-10-16 | [2026년 한신대학교 창업보육센터 신규 창업기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179377) | 한신대학교 창업보육센터 | K-Startup 사업공고 |
| 2026-10-16 | [TechGALA 2026 한국 스타트업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179438) | (주)플린토파트너스 | K-Startup 사업공고 |
| 2026-10-16 | [2026년 서울 라이프스타일 거점(일본) 진출사업 참여기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179454) | 서울경제진흥원 | K-Startup 사업공고 |
| 2026-10-16 | [2026 오세아니아 전략시장 진출 사업 참여기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179453) | 서울경제진흥원 | K-Startup 사업공고 |
| 2026-10-16 | [[제주창조경제혁신센터]「상시매칭 오픈이노베이션 플랫폼」&apos;에코프로 계열사&apos;&apos;수요과제 매칭 스타트업 모집 (~10/16)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179487) | 제주창조경제혁신센터 | K-Startup 사업공고 |
| 2026-10-18 | [2026 강동구 창업가 네트워킹 데이 참가 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179388) | 강동구 청년해냄센터 | K-Startup 사업공고 |

## 스타트업 뉴스

| 날짜 | 제목 | 출처 |
|---|---|---|
| 2026-10-15 | [파라택시스이더리움, 이더리움 42억원어치 추가 취득…총 보유량 1만1729개로 확대](https://www.venturesquare.net/1120019/) | 벤처스퀘어 |
| 2026-10-15 | [씨엔티테크·경기북부 청년창업사관학교, 수도·강원권 스타트업 10개사 투자 IR 개최](https://www.venturesquare.net/1120018/) | 벤처스퀘어 |
| 2026-10-15 | [부산창조경제혁신센터, ‘모두의 창업’ 지역오디션 개최…29명 중 12명 선발](https://www.venturesquare.net/1120022/) | 벤처스퀘어 |
| 2026-10-15 | [윗유, 틱톡코리아와 미국 틱톡샵 진출 지원…국내 브랜드 10개사 집중 육성](https://www.venturesquare.net/1120030/) | 벤처스퀘어 |
| 2026-10-15 | [그린다, 스케일업 팁스 특화형 선정…SAF 원료 대량생산 기술에 최대 30억원 지원](https://www.venturesquare.net/1120043/) | 벤처스퀘어 |
| 2026-10-15 | [더벤처스, 미국 K-베이커리 카페 ‘스모킹 타이거’ 시드 투자…5개 주 이상 진출 추진](https://www.venturesquare.net/1120046/) | 벤처스퀘어 |
| 2026-10-15 | [딥엑스 NPU, 라즈베리 파이 공식 뉴스룸 소개…3W 전력으로 비전·언어 AI 구현](https://www.venturesquare.net/1120048/) | 벤처스퀘어 |
| 2026-10-15 | [미미박스 누니, 일본 라쿠텐 립오일 랭킹 1위…로프트 입점으로 오프라인 공략](https://www.venturesquare.net/1120061/) | 벤처스퀘어 |
| 2026-10-15 | [에이슨, 미세전류 뷰티 디바이스 ‘루바’ 첫 팝업 완판…백화점 유통 확대 추진](https://www.venturesquare.net/1120062/) | 벤처스퀘어 |
| 2026-10-15 | [틱톡, ‘틱톡 서밋 코리아 2026’ 개최…AI 광고부터 K브랜드 해외 진출까지](https://www.venturesquare.net/1120074/) | 벤처스퀘어 |
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
