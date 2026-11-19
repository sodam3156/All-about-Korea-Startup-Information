# All-about-Korea-Startup-Information

세종 청년창업 기관 공지 · 정부 지원사업 공고 · 스타트업 뉴스를 **매일 14:00 KST에 자동 수집**하는 저장소.
GitHub Actions가 수집→중복제거→상세저장→아래 대시보드 갱신→텔레그램 브리핑까지 수행한다 (git-scraping — 서버·DB·API 비용 없음).

**완전 규칙 기반**: 소스마다 공식 API/RSS 또는 정규식 파서를 쓴다(LLM 미사용, 고정비 $0). 대신 사이트가 개편되면 파서가 조용히 0건을 낼 수 있어, 같은 소스가 **연속 2회 이상 0건**이면 `data/source_health.json`에 기록하고 다이제스트에 "⚠️ 소스 점검 필요"로 경고한다 — 이게 규칙 기반의 유일한 약점(개편에 안 깨지는 AI 추출 대비)을 메우는 피드백 루프다.

<!-- AUTO:START -->

_자동 갱신: 2026-11-19 (KST)_

## 마감 임박 지원사업

| 마감 | 공고 | 기관 | 출처 |
|---|---|---|---|
| 2026-11-19 | [[서초창업스테이션] 서리풀 소상공인 창업 클리닉(11월) - 소상공인 1:1 컨설팅](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179586) | 서초창업스테이션 | K-Startup 사업공고 |
| 2026-11-19 | [국민대학교 청년도약 인재양성 부트캠프 참가자 모집(AI 실무교육)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179559) | 국민대학교 글로벌창업벤처대학원 | K-Startup 사업공고 |
| 2026-11-19 | [[온라인·무료] 코딩·사업자 없이 여는 내 강의·전자책 판매 사이트](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179702) | 스쿨모아 주식회사 | K-Startup 사업공고 |
| 2026-11-19 | [2027년 팁스 추천 화성산업진흥원 성장 자원 확보 패키지 지원 프로그램 신청 안내](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179732) | 화성산업진흥원 | K-Startup 사업공고 |
| 2026-11-19 | [제79회 단디벤처포럼 [2026 단디벤처 투자로드쇼] 1:1 투자상담회·IR 피칭기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179754) | 단디벤처포럼 | K-Startup 사업공고 |
| 2026-11-19 | ['딸깍 한 번으로 완성하는 AI 업무 자동화' 실전 워크숍 참여자 모집 (『신한 스퀘어브릿지』 11월 브릿지 클럽)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179752) | 신한금융희망재단 | K-Startup 사업공고 |
| 2026-11-19 | [2026년 경희대학교 캠퍼스타운 제6회 데모데이: 刮目相對괄목상대](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179690) | 경희대학교 (서울)앵커사업단 캠퍼스타운센터 | K-Startup 사업공고 |
| 2026-11-19 | [2026 인수창업 설명회 - 당신의 성장을 지원합니다.](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179774) | 주식회사 디유파트너스 | K-Startup 사업공고 |
| 2026-11-19 | [2026 강남구 미래산업 기반 기업 활성화 지원사업 데모데이 참관](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179771) | 더인벤션랩 | K-Startup 사업공고 |
| 2026-11-19 | [제79회 단디벤처포럼 [2026 단디벤처 투자로드쇼] 일반참가자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179811) | 단디벤처포럼 | K-Startup 사업공고 |
| 2026-11-19 | [2026 광명시 기업박람회 (GM TECH EXPO 2026)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179804) | 광명시청 | K-Startup 사업공고 |
| 2026-11-20 | [선문대학교 맞춤형 창업멘토링 참가자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179614) | 조슈아파트너스(주) | K-Startup 사업공고 |
| 2026-11-20 | [2026년 초기창업패키지 SM엔터테인먼트 오픈이노베이션 밋업 CultureTech Challenge](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179661) | 씨엔티테크(주) | K-Startup 사업공고 |
| 2026-11-20 | [2027년도 초기창업·창업도약 패키지 사업 신규 주관기관 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179660) | 중소벤처기업부 장관 | K-Startup 사업공고 |
| 2026-11-20 | [2026 맞춤형 창업과정 교육생 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179688) | 김해시중장년기술창업센터장 | K-Startup 사업공고 |
| 2026-11-20 | [2026 제4차 노원사회적경제지원센터 입주기업 신규 공모](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179700) | 노원사회적경제지원센터 | K-Startup 사업공고 |
| 2026-11-20 | [2027년 청년 쿡 비즈니스·푸드테크 센터 스타트업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179687) | 서울특별시 | K-Startup 사업공고 |
| 2026-11-20 | [NEST G밸리 4기 입주기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179733) | 신용보증기금 스케일업금융센터 | K-Startup 사업공고 |
| 2026-11-20 | [임팩트 페스타 2026 참관객 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179745) | 서울소셜벤처허브 | K-Startup 사업공고 |
| 2026-11-20 | [[행사 안내] 2026 경기도 R&D 성과공유회](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179763) | 주식회사 내비온파트너스 | K-Startup 사업공고 |

## 스타트업 뉴스

| 날짜 | 제목 | 출처 |
|---|---|---|
| 2026-11-19 | [삼삼엠투, 국토부 ‘우수 부동산서비스사업자’ 인증…단기임대 거래·소비자 보호체계 인정](https://www.venturesquare.net/1129938/) | 벤처스퀘어 |
| 2026-11-19 | [삼쩜삼, 환급 서비스 중심으로 앱 개편…월세 계약서 AI 점검 기능도 도입](https://www.venturesquare.net/1129949/) | 벤처스퀘어 |
| 2026-11-19 | [로가, 식물성 콜라겐 기술로 대통령표창 쾌거…대만 독점 협력·미국 시장 진출 추진](https://www.venturesquare.net/1129962/) | 벤처스퀘어 |
| 2026-11-19 | [피처링, 유튜브 공식 데이터 연동…시청자 관심사·브랜드 협업 이력까지 분석](https://www.venturesquare.net/1129959/) | 벤처스퀘어 |
| 2026-11-19 | [파라택시스이더리움, 10억원 규모 자사주 취득 결정…주주환원 정책 이어간다](https://www.venturesquare.net/1129987/) | 벤처스퀘어 |
| 2026-11-19 | [오디바이스, 2027학년도 AI 정시 합격예측 ‘입시캐스트’ 출시…100여 개 대학 전형 분석](https://www.venturesquare.net/1129989/) | 벤처스퀘어 |
| 2026-11-19 | [휴민랩스, 630억원 시리즈A 투자 유치…한국에 피지컬 AI 로봇 배치 인프라 구축한다](https://www.venturesquare.net/1130000/) | 벤처스퀘어 |
| 2026-11-19 | [[VS 현장] “기술은 개발했는데, 어떻게 지킬 것인가”…판교에 모인 스타트업들의 IP 생존 전략](https://www.venturesquare.net/1130008/) | 벤처스퀘어 |
| 2026-11-19 | [초기투자액셀러레이터협회, 부산서 ‘LunchSAI’ 개최…LP 관리·펀드 운영 실무 공유](https://www.venturesquare.net/1130024/) | 벤처스퀘어 |
| 2026-11-19 | [한국주택정보, 관리비를 건물 경쟁력 지표로…AI 자동화 넘어 일본 시장 진출](https://www.venturesquare.net/1130023/) | 벤처스퀘어 |
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
