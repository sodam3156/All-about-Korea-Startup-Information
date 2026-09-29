# All-about-Korea-Startup-Information

세종 청년창업 기관 공지 · 정부 지원사업 공고 · 스타트업 뉴스를 **매일 14:00 KST에 자동 수집**하는 저장소.
GitHub Actions가 수집→중복제거→상세저장→아래 대시보드 갱신→텔레그램 브리핑까지 수행한다 (git-scraping — 서버·DB·API 비용 없음).

**완전 규칙 기반**: 소스마다 공식 API/RSS 또는 정규식 파서를 쓴다(LLM 미사용, 고정비 $0). 대신 사이트가 개편되면 파서가 조용히 0건을 낼 수 있어, 같은 소스가 **연속 2회 이상 0건**이면 `data/source_health.json`에 기록하고 다이제스트에 "⚠️ 소스 점검 필요"로 경고한다 — 이게 규칙 기반의 유일한 약점(개편에 안 깨지는 AI 추출 대비)을 메우는 피드백 루프다.

<!-- AUTO:START -->

_자동 갱신: 2026-09-29 (KST)_

## 마감 임박 지원사업

| 마감 | 공고 | 기관 | 출처 |
|---|---|---|---|
| 2026-09-29 | [2026 투자 유치 세미나 - 투자사 관점에서 보는 투자유치를 위한 실전 전략](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179224) | 서울창업허브 창동 | K-Startup 사업공고 |
| 2026-09-29 | [[인천] 2026년 IP창업존 51기 교육(모두의창업 연계과정) 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179271) | 인천지식재산센터 | K-Startup 사업공고 |
| 2026-09-29 | [「서울소셜벤처허브」2026년 ‘허브 멤버스’ 입주사 추가모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179270) | 서울소셜벤처허브 | K-Startup 사업공고 |
| 2026-09-29 | [‘2026년 글로컬 창업사관학교 액셀러레이팅’ 참여기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179308) | 국립순천대학교 창업지원단장국립순천대학교 창업지원단장 | K-Startup 사업공고 |
| 2026-09-29 | [[창업BuS x Station C] 2026년 강원BRIDGE 배치프로그램 2차 창업기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179305) | 재단법인 강원창조경제혁신센터 | K-Startup 사업공고 |
| 2026-09-29 | [청년창업 거주지원시설(창업하여家) 입주자 3차 모집(연장)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179292) | (재)광주테크노파크 | K-Startup 사업공고 |
| 2026-09-29 | [2026년 제2회 테크플러스 스테이지 입주기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179291) | (재)광주테크노파크 | K-Startup 사업공고 |
| 2026-09-30 | [남서울대학교 창업보육센터 입주기업 모집 (천안소재)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178706) | 남서울대학교 창업보육센터 | K-Startup 사업공고 |
| 2026-09-30 | [「2026년 강소특구 이노테크 발굴 및 창업지원사업」예비 창업자 사업화 지원 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178786) | 한국전력공사 강소특구 육성사업단장, 나주 강소특구 공동연구기관장 | K-Startup 사업공고 |
| 2026-09-30 | [2026년 중소기업 동행교육](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178817) | 근로복지공단 인재개발원 | K-Startup 사업공고 |
| 2026-09-30 | [취약분야 상시 컨설팅 9월 참가자 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178948) | 강동구 청년해냄센터 | K-Startup 사업공고 |
| 2026-09-30 | [2026년 한국외대 창업보육센터 입주기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179002) | 한국외국어대학교연구산학협력단 | K-Startup 사업공고 |
| 2026-09-30 | [창업부트캠프 바이오큐브 17차 교육 신청 안내](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179020) | 한국바이오협회 | K-Startup 사업공고 |
| 2026-09-30 | [2026 대덕특구 딥테크 혁신성장 플랫폼(전략기술 발굴 및 매칭) (9/1 ~ 9/30)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179057) | 연구개발특구진흥재단 | K-Startup 사업공고 |
| 2026-09-30 | [2026 벤처확인 인증준비기업 맞춤형 무료 진단 지원사업](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179052) | (주)엠비즈플래닛 산하 혁신기술경영인증지원센터 | K-Startup 사업공고 |
| 2026-09-30 | [국내 특허(IP) 보유기업 투자&사업화 스케일업 지원사업](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179049) | (주)엠비즈플래닛 산하 혁신기술경영인증지원센터 | K-Startup 사업공고 |
| 2026-09-30 | [해외진출 기업 대상 AI 통역 서비스 「아네스노트」 이용권 지원 (9월)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179047) | 주식회사 팀제로코드 | K-Startup 사업공고 |
| 2026-09-30 | [2026년도 한국도로공사 청년 AI 스타트업 지원 시범사업](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179035) | 한국도로공사 | K-Startup 사업공고 |
| 2026-09-30 | [[롯데장학재단]「2026년 제3회 신격호 롯데 청년기업가대상」모집공고 (~9/30)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179058) | 롯데장학재단 | K-Startup 사업공고 |
| 2026-09-30 | [(창업공모전) 2026 여성벤처 성장 챌린지 참가자 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179105) | 한국여성벤처협회장 | K-Startup 사업공고 |

## 스타트업 뉴스

| 날짜 | 제목 | 출처 |
|---|---|---|
| 2026-09-28 | [“양자컴퓨터, 한국에서 함께 만들겠다”…콴델라가 韓 제조업에 손 내민 이유](https://www.venturesquare.net/1116489/) | 벤처스퀘어 |
| 2026-09-28 | [[VS기획] 화재 줄인 물 기반 배터리로 AI 데이터센터 공략하는 폼·에오스·코스모스랩의 3사 3색 전략](https://www.venturesquare.net/1116209/) | 벤처스퀘어 |
| 2026-09-29 | [네이버, 멕시코 AI 생태계 공략…정부·기업 만나 공공AX·소버린AI 협력 논의](https://www.venturesquare.net/1116513/) | 벤처스퀘어 |
| 2026-09-29 | [프레인글로벌, AI 검색 시대 B2B 고객은 어떻게 찾나…LG AI연구원·두산·SK바사 사례 공개](https://www.venturesquare.net/1116552/) | 벤처스퀘어 |
| 2026-09-29 | [딥세일즈, ‘살 가능성 높은’ 해외 바이어 AI가 먼저 찾는다…딥테크 팁스 선정](https://www.venturesquare.net/1116559/) | 벤처스퀘어 |
| 2026-09-29 | [부산창경, 아이는 바다·숲 체험 부모는 업무…부산서 ‘가족형 워케이션’ 운영](https://www.venturesquare.net/1116567/) | 벤처스퀘어 |
| 2026-09-29 | [디엘지, 한국 기업 이탈리아 진출 때 현지 로펌 다시 찾을 필요 줄인다…AMAM Legal과 파트너십](https://www.venturesquare.net/1116570/) | 벤처스퀘어 |
| 2026-09-29 | [와디즈파트너스, 환동해 소셜벤처 10곳 키운다…최소 1곳에 1억원 이상 투자](https://www.venturesquare.net/1116582/) | 벤처스퀘어 |
| 2026-09-29 | [BARC, 연세의료원에 기부…재활의학과 의사들이 만든 신발에서 의료 나눔으로](https://www.venturesquare.net/1116589/) | 벤처스퀘어 |
| 2026-09-29 | [코딩 테스트 표준 만든 그렙, ‘AI 역량 평가’와 글로벌 시험감독으로 2028년 IPO 도전](https://www.venturesquare.net/1116597/) | 벤처스퀘어 |
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
