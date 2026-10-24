# All-about-Korea-Startup-Information

세종 청년창업 기관 공지 · 정부 지원사업 공고 · 스타트업 뉴스를 **매일 14:00 KST에 자동 수집**하는 저장소.
GitHub Actions가 수집→중복제거→상세저장→아래 대시보드 갱신→텔레그램 브리핑까지 수행한다 (git-scraping — 서버·DB·API 비용 없음).

**완전 규칙 기반**: 소스마다 공식 API/RSS 또는 정규식 파서를 쓴다(LLM 미사용, 고정비 $0). 대신 사이트가 개편되면 파서가 조용히 0건을 낼 수 있어, 같은 소스가 **연속 2회 이상 0건**이면 `data/source_health.json`에 기록하고 다이제스트에 "⚠️ 소스 점검 필요"로 경고한다 — 이게 규칙 기반의 유일한 약점(개편에 안 깨지는 AI 추출 대비)을 메우는 피드백 루프다.

<!-- AUTO:START -->

_자동 갱신: 2026-10-24 (KST)_

## 마감 임박 지원사업

| 마감 | 공고 | 기관 | 출처 |
|---|---|---|---|
| 2026-10-24 | [ANTLER | 2026 앤틀러 글로벌 리쿠르팅데이 참가자 모집(10.24.)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179423) | 앤틀러코리아 | K-Startup 사업공고 |
| 2026-10-24 | [2026 시흥시 청년창업가 네트워킹 행사 참가자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179480) | 시흥시청 | K-Startup 사업공고 |
| 2026-10-25 | [2026년 대전 스타트업 원스톱 지원센터 아카데미 3회차](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179211) | 대전창조경제혁신센터 | K-Startup 사업공고 |
| 2026-10-25 | [현직 엔지니어와 함께하는 하드웨어 스타트업 제품화 실무 코칭](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179407) | 인탑스(주) | K-Startup 사업공고 |
| 2026-10-25 | [[푼타컴퍼니]로컬 인디브랜드 성장을 위한 국내 및 글로벌 성장 프로그램 참가 기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179366) | 주식회사 푼타컴퍼니 | K-Startup 사업공고 |
| 2026-10-25 | [[벙커샷 컴퍼니] Pre-Seed 컴퍼니빌딩 프로그램 2026년 4기 참가기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179427) | (주)벙커샷컴퍼니 | K-Startup 사업공고 |
| 2026-10-25 | [2026년 하반기 과천시 창업지원센터 스마트오피스 입주기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179529) | 과천시 창업지원센터 | K-Startup 사업공고 |
| 2026-10-25 | [[2026 에코스타트업 Green IR DAY] 참관 신청](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179553) | 마크앤컴퍼니 | K-Startup 사업공고 |
| 2026-10-26 | [코리아 핀테크 위크 2026 「핀테크 스타트업 1:1 투자 밋업」 참여기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179012) | 한국성장금융투자운용 | K-Startup 사업공고 |
| 2026-10-26 | [2026년 제6회 SDGs 소셜벤처 챔피언십 참가자 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179241) | 사단법인 한국지속가능소셜벤처협회 | K-Startup 사업공고 |
| 2026-10-26 | [2026년 7회차 지식재산 무료 초청교육 수요조사](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179376) | 한국특허정보원 | K-Startup 사업공고 |
| 2026-10-26 | [2026년 대전 스타트업스쿨 스타트업 리딩클래스 (6회차 ㅣ 나에게 맞는 투자자 찾는 실전 노하우)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179440) | 대전창조경제혁신센터 | K-Startup 사업공고 |
| 2026-10-26 | [[서초창업스테이션] 10월 창업 교육 프로그램 - 창업아이템 찾기 : 문제에서 시작 된 창업아이템 찾기](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179432) | 서초창업스테이션 | K-Startup 사업공고 |
| 2026-10-26 | [[광운대캠퍼스타운] AI 첫걸음 아카데미 (HELLO AI!) 참가자 모집 (선착순마감)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179429) | 광운대학교 캠퍼스타운 | K-Startup 사업공고 |
| 2026-10-26 | [2026년 광명 글로컬 데모데이 참관객 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179456) | 씨엔티테크 | K-Startup 사업공고 |
| 2026-10-26 | [[소담스퀘어 당산] 온라인 판매를 위한, 디지털 전환 이해 및 판매 채널 분석](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179523) | (주)오픈놀 | K-Startup 사업공고 |
| 2026-10-26 | [2026 TIPS SSU Final IR Day](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179578) | 주식회사 킹고스프링 | K-Startup 사업공고 |
| 2026-10-26 | [「2026 기업지원실 운영」 지역 환경기업 육성 프로그램 참여기업 수정 모집공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179560) | (재)전라남도환경산업진흥원 | K-Startup 사업공고 |
| 2026-10-27 | [[무료 AI 역량강화 교육]생성형 AI 기반 글로벌 무역·물류 데이터 분석 및 공급망 최적화 과정 (대전)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179171) | (주)글로벌창업연구소 | K-Startup 사업공고 |
| 2026-10-27 | [2026 정주영 창업경진대회: 무한(INFINITE)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179245) | 아산나눔재단 | K-Startup 사업공고 |

## 스타트업 뉴스

| 날짜 | 제목 | 출처 |
|---|---|---|
| 2026-10-23 | [스튜디오메타케이, 신용보증기금 프리아이콘 선정…AI 콘텐츠·IP 사업화 확대](https://www.venturesquare.net/1122384/) | 벤처스퀘어 |
| 2026-10-23 | [넘즈에이아이, 젠슨 황 엔비디아 GTC 기조연설에 등장…정형 데이터 AI 모델 ‘코실로’ 주목](https://www.venturesquare.net/1122390/) | 벤처스퀘어 |
| 2026-10-23 | [스타팅파트너스, 더존비즈온과 소기업 AI 채용 서비스 협업…동행라운지 25대 1 경쟁률 통과](https://www.venturesquare.net/1122393/) | 벤처스퀘어 |
| 2026-10-23 | [와디즈, AI 기반 펀딩 성과 관리 시스템 ‘메이커 인텔리전스’ 출시…매일 개선 전략 제안](https://www.venturesquare.net/1122404/) | 벤처스퀘어 |
| 2026-10-23 | [경기창조경제혁신센터, AI 스타트업 4개사 싱가포르 진출 지원…오라클과 글로벌 로드쇼 개최](https://www.venturesquare.net/1122413/) | 벤처스퀘어 |
| 2026-10-23 | [라프디, 창업도약패키지 AI 인재 실증형 선정…어필리에이트 마케팅 자동화 기술 개발](https://www.venturesquare.net/1122419/) | 벤처스퀘어 |
| 2026-10-23 | [젠엑시스, K-바이오랩허브 스타트업 5개사 투자유치 지원…데모데이 앞두고 IR 피칭워크숍 개최](https://www.venturesquare.net/1122425/) | 벤처스퀘어 |
| 2026-10-23 | [이모션웨이브·이엘티비, AI 기반 K-Food 실감형 콘텐츠 공동 제작…6개국 시장 공략](https://www.venturesquare.net/1122429/) | 벤처스퀘어 |
| 2026-10-23 | [블루포인트, 대덕 양자기업 4개사 미국 아이온큐·IBM 기술교류 지원…글로벌 공급망 진입 모색](https://www.venturesquare.net/1122442/) | 벤처스퀘어 |
| 2026-10-23 | [IBK기업은행, IBK창공 대전 10기 데모데이 개최…스타트업 12개사 투자유치 나서](https://www.venturesquare.net/1122456/) | 벤처스퀘어 |
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
