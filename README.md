# All-about-Korea-Startup-Information

세종 청년창업 기관 공지 · 정부 지원사업 공고 · 스타트업 뉴스를 **매일 14:00 KST에 자동 수집**하는 저장소.
GitHub Actions가 수집→중복제거→상세저장→아래 대시보드 갱신→텔레그램 브리핑까지 수행한다 (git-scraping — 서버·DB·API 비용 없음).

**완전 규칙 기반**: 소스마다 공식 API/RSS 또는 정규식 파서를 쓴다(LLM 미사용, 고정비 $0). 대신 사이트가 개편되면 파서가 조용히 0건을 낼 수 있어, 같은 소스가 **연속 2회 이상 0건**이면 `data/source_health.json`에 기록하고 다이제스트에 "⚠️ 소스 점검 필요"로 경고한다 — 이게 규칙 기반의 유일한 약점(개편에 안 깨지는 AI 추출 대비)을 메우는 피드백 루프다.

<!-- AUTO:START -->

_자동 갱신: 2026-11-18 (KST)_

## 마감 임박 지원사업

| 마감 | 공고 | 기관 | 출처 |
|---|---|---|---|
| 2026-11-18 | [2026 논산시 사회적경제 창업 아카데미 참여자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179591) | 논산시 사회적경제통합지원센터 | K-Startup 사업공고 |
| 2026-11-18 | [2026 서울창업허브 창동 데모데이 참관 신청](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179562) | 서울창업허브 창동 | K-Startup 사업공고 |
| 2026-11-18 | [경기과학기술대학교 창업보육센터 입주기업 모집 9차](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179623) | 경기과학기술대학교 창업보육센터 | K-Startup 사업공고 |
| 2026-11-18 | [<2026년 AI 활용 온라인 플랫폼 제작 교육> 참여자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179680) | 충북Pro메이커센터 | K-Startup 사업공고 |
| 2026-11-18 | [2026 서구토탈창업아카데미 참가자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179638) | 온랩 | K-Startup 사업공고 |
| 2026-11-18 | [2026 KOREA LBS Day(~11.17)｜선도기업·투자자·전문가와 만나는 1:1 비즈니스 미팅](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179683) | 한국능률협회컨설팅 | K-Startup 사업공고 |
| 2026-11-18 | [2026년도 제4차 북부창업아카데미 및 북부창업멘토링 DAY 참가자 모집(주제 : 2027 정부지원사업 합격을 위한 실전 전략)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179741) | 북부여성새일센터 | K-Startup 사업공고 |
| 2026-11-18 | [2026년 경기스타트업플랫폼 온라인 밋업위크(4차) 투자자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179747) | 주식회사 내비온파트너스 | K-Startup 사업공고 |
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

## 스타트업 뉴스

| 날짜 | 제목 | 출처 |
|---|---|---|
| 2026-11-17 | [킵코퍼레이션, 외국인 환자 응대 솔루션 ‘킵커넥트’ 공개…다국어 예약·상담 통합 지원](https://www.venturesquare.net/1129520/) | 벤처스퀘어 |
| 2026-11-17 | [튜링, 대학생 AI 에이전트 ‘파이’ 출시…시험 준비부터 조별과제까지 지원](https://www.venturesquare.net/1129523/) | 벤처스퀘어 |
| 2026-11-18 | [패스트파이브, AI·보안 등 스타트업 8개사 선정…최대 6개월 사무공간 지원한다](https://www.venturesquare.net/1129549/) | 벤처스퀘어 |
| 2026-11-18 | [아산나눔재단, 비영리스타트업 9개 팀에 총상금 1억 원…모스픽·사이트스페이스 대상 수상](https://www.venturesquare.net/1129551/) | 벤처스퀘어 |
| 2026-11-18 | [마크비전, 월 13만 원부터 위조상품 대응…중소 브랜드용 AI 보호 서비스 출시](https://www.venturesquare.net/1129554/) | 벤처스퀘어 |
| 2026-11-18 | [스미스, 소속 아티스트 그렉과 일본 니가타서 문화교류…현지 학생 50여 명과 음악 워크숍](https://www.venturesquare.net/1129565/) | 벤처스퀘어 |
| 2026-11-18 | [와디즈 ‘삼무서점’, 4주간 19억 원 펀딩…’각시탈’ 완전판·’토지’ 소장판 인기](https://www.venturesquare.net/1129575/) | 벤처스퀘어 |
| 2026-11-18 | [미미박스 ‘누니 립오일’, 올해 글로벌 매출 747억 원 전망…미국 타깃 1778개 매장 진출](https://www.venturesquare.net/1129591/) | 벤처스퀘어 |
| 2026-11-18 | [리브라이블리 지창대 대표, 벤처창업진흥 유공 장관표창…AI 기반 시니어 통합돌봄 성과 인정](https://www.venturesquare.net/1129596/) | 벤처스퀘어 |
| 2026-11-18 | [마이크로소프트, AI 에이전트를 기업 운영의 중심으로…이그나이트 2026서 ‘프론티어 생태계’ 공개](https://www.venturesquare.net/1129604/) | 벤처스퀘어 |
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
