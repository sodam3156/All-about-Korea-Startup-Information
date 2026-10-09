# All-about-Korea-Startup-Information

세종 청년창업 기관 공지 · 정부 지원사업 공고 · 스타트업 뉴스를 **매일 14:00 KST에 자동 수집**하는 저장소.
GitHub Actions가 수집→중복제거→상세저장→아래 대시보드 갱신→텔레그램 브리핑까지 수행한다 (git-scraping — 서버·DB·API 비용 없음).

**완전 규칙 기반**: 소스마다 공식 API/RSS 또는 정규식 파서를 쓴다(LLM 미사용, 고정비 $0). 대신 사이트가 개편되면 파서가 조용히 0건을 낼 수 있어, 같은 소스가 **연속 2회 이상 0건**이면 `data/source_health.json`에 기록하고 다이제스트에 "⚠️ 소스 점검 필요"로 경고한다 — 이게 규칙 기반의 유일한 약점(개편에 안 깨지는 AI 추출 대비)을 메우는 피드백 루프다.

<!-- AUTO:START -->

_자동 갱신: 2026-10-09 (KST)_

## 마감 임박 지원사업

| 마감 | 공고 | 기관 | 출처 |
|---|---|---|---|
| 2026-10-09 | [2026년 실리콘밸리 GTM(Go-To-Market) 프로그램 창업기업 모집공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179294) | 창업진흥원 실리콘밸리사무소장 | K-Startup 사업공고 |
| 2026-10-09 | [2026-11회 호남권 엔젤투자 피칭룸 in 전남광주](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179265) | 한국엔젤투자협회 호남권 엔젤투자허브 | K-Startup 사업공고 |
| 2026-10-09 | [2026 대전로컬창업포럼 참가자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179436) | 주식회사 온랩 | K-Startup 사업공고 |
| 2026-10-11 | ['애자일 피보팅: 시장의 변화를 기회로 만드는 기술창업 전략'](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179295) | 주식회사 이노시아 | K-Startup 사업공고 |
| 2026-10-11 | [2026년 서울창업센터 관악 X SK에코플랜트 오픈이노베이션 프로그램 참여기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179347) | 서울창업센터 관악 | K-Startup 사업공고 |
| 2026-10-11 | [2026 제2회 반려동물 창업 아이디어 경진대회 참가자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179323) | (사)한국반려동물산업협회 | K-Startup 사업공고 |
| 2026-10-11 | [2026 DMC 이노베이션 캠프 경진대회 (DIC2026)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179399) | ㈜디엠씨산학진흥재단 | K-Startup 사업공고 |
| 2026-10-11 | [2026년 SaaS 전환지원센터xAWS SaaS 현대화 교육 4회차 참가자 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179371) | 정보통신산업진흥원, SaaS 전환지원센터 | K-Startup 사업공고 |
| 2026-10-11 | [2026 극지 데이터 융합 스케일업 프로그램](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179357) | 극지연구소 | K-Startup 사업공고 |
| 2026-10-11 | [2026년 세종 한글 상품 박람회 및 세종 한글 술술 축제](https://ccei.creativekorea.or.kr/sejong/service/program_view.do?no=10584&sMenuType=00040001&cntry_nm=sejong) | 세종창조경제혁신센터 지원프로그램 | 세종창조경제혁신센터 지원프로그램 |
| 2026-10-12 | [신약개발 실증지원 네트워크](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179195) | 비엑스플랜트 | K-Startup 사업공고 |
| 2026-10-12 | [2027년도 초격차 스타트업 프로젝트 기술 사업화 및 투자유치 주관기관 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179287) | 중소벤처기업부 장관 | K-Startup 사업공고 |
| 2026-10-12 | [[GBSA] 2026 판교스타트업 투자교류회 제 3차 투자교류회](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179283) | ㈜내비온파트너스 | K-Startup 사업공고 |
| 2026-10-12 | [2026년 웰컴 투 팁스 4차 참가기업 모집 (강원권)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179341) | (주)로우파트너스 | K-Startup 사업공고 |
| 2026-10-12 | [2026 대전 재도전 네트워킹 데이 「Re-Boot Networking Day」](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179342) | 대전창조경제혁신센터 | K-Startup 사업공고 |
| 2026-10-12 | [2026년 제4회 ICT콤플렉스 스타트업 투자상담회 참가기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179329) | ICT콤플렉스 | K-Startup 사업공고 |
| 2026-10-12 | [디캠프 10월 오피스아워 #벤처투자·#사업협력 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179319) | 재단법인 은행권청년창업재단 | K-Startup 사업공고 |
| 2026-10-12 | [창업특강 : AI시대에 창업한다는 것](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179315) | 관악구청 | K-Startup 사업공고 |
| 2026-10-12 | [[서울핀테크랩] 2026 핀테크 스타트업의 유럽 시장 진출 전략](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179311) | 서울핀테크랩 | K-Startup 사업공고 |
| 2026-10-12 | [2026년 B the B 뷰티 기반 융복합 콘텐츠 전시(다운타운) 팝업 참여기업 모집(3차)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179410) | (재)서울경제진흥원 | K-Startup 사업공고 |

## 스타트업 뉴스

| 날짜 | 제목 | 출처 |
|---|---|---|
| 2026-10-09 | [한글날 100주년, 글꼴에서 코딩까지…네이버·산돌·셈틀이 넓히는 한글의 쓰임](https://www.venturesquare.net/1118645/) | 벤처스퀘어 |
| 2026-10-09 | [시리즈벤처스, 부울경 스타트업 11곳 글로벌 투자자 앞에 세웠다…FLY ASIA서 IR 데모데이 개최](https://www.venturesquare.net/1118688/) | 벤처스퀘어 |
| 2026-10-09 | [100만 명 홀린 ‘부캉이’…편의점 매출 76% 뛰고 소주·AI 서비스까지 등장](https://www.venturesquare.net/1118676/) | 벤처스퀘어 |
| 2026-10-07 | [힘펠, 출산·육아 지원에 장기근속 휴가까지…경기도 ‘가족친화 기업’ 선정](https://www.venturesquare.net/1118465/) | 벤처스퀘어 |
| 2026-10-07 | [중고나라, 택배 보내러 안 나가도 된다…‘문앞택배’ 판매자 44% 한 달 만에 이용](https://www.venturesquare.net/1118450/) | 벤처스퀘어 |
| 2026-10-07 | [부산에서 아시아로, 세계로…‘FLY ASIA 2026’, 해양 AI·투자·협력의 장 열었다](https://www.venturesquare.net/1118473/) | 벤처스퀘어 |
| 2026-10-08 | [유이크, 라이즈와 4번째 전속모델 계약…팝업 4000명 방문 이어 립밤 협업 제품 출시](https://www.venturesquare.net/1118503/) | 벤처스퀘어 |
| 2026-10-08 | [마스오토, 자율주행 트럭 8개 노선 운영 경험 美 교통부와 공유…강릉 ITS 세계총회 참가](https://www.venturesquare.net/1118481/) | 벤처스퀘어 |
| 2026-10-08 | [[VS 기획] MIT가 그린 ‘건설 AI 지도’…설계부터 조달까지 산업 문법 바뀐다](https://www.venturesquare.net/1118343/) | 벤처스퀘어 |
| 2026-10-08 | [두나무, “시세 조회에 API 키 필요 없다”…업비트 계정 대여 신종 사기 경고](https://www.venturesquare.net/1118560/) | 벤처스퀘어 |
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
