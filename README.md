# All-about-Korea-Startup-Information

세종 청년창업 기관 공지 · 정부 지원사업 공고 · 스타트업 뉴스를 **매일 14:00 KST에 자동 수집**하는 저장소.
GitHub Actions가 수집→중복제거→상세저장→아래 대시보드 갱신→텔레그램 브리핑까지 수행한다 (git-scraping — 서버·DB·API 비용 없음).

**완전 규칙 기반**: 소스마다 공식 API/RSS 또는 정규식 파서를 쓴다(LLM 미사용, 고정비 $0). 대신 사이트가 개편되면 파서가 조용히 0건을 낼 수 있어, 같은 소스가 **연속 2회 이상 0건**이면 `data/source_health.json`에 기록하고 다이제스트에 "⚠️ 소스 점검 필요"로 경고한다 — 이게 규칙 기반의 유일한 약점(개편에 안 깨지는 AI 추출 대비)을 메우는 피드백 루프다.

<!-- AUTO:START -->

_자동 갱신: 2026-10-26 (KST)_

## 마감 임박 지원사업

| 마감 | 공고 | 기관 | 출처 |
|---|---|---|---|
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
| 2026-10-27 | [[동대문구 창업지원센터] 10월 메이커스페이스(레이저커터, 3D프린팅) 교육 일정](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179420) | 동대문구 창업지원센터 | K-Startup 사업공고 |
| 2026-10-27 | [2027년도 관광기업지원센터(서울) 신규 입주기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179465) | 한국관광공사 | K-Startup 사업공고 |
| 2026-10-27 | [Applications Now Open: 2026 OASIS-6 Global Startup Challenge 「2026 외국인 창업대전(OASIS-6)」 참가자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179459) | 글로벌창업이민센터(한국능률협회컨설팅) | K-Startup 사업공고 |
| 2026-10-27 | [[무료|150석 한정] 딥테크 창업가 컨퍼런스 d.day : founders summit 참가자 모집 10/29](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179527) | 재단법인 은행권청년창업재단 | K-Startup 사업공고 |
| 2026-10-27 | [2026 관광기업 동반성장 기술역량 강화교육](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179574) | 한국관광공사 | K-Startup 사업공고 |
| 2026-10-27 | [2026 문화예술 창업교육의 모든 것.zip 2기 참여자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179506) | 성북구 청년공간 길이음 | K-Startup 사업공고 |
| 2026-10-27 | [[강원ICT융합연구원] 강원 미래산업 AX혁신과 지산학연 신사업 발굴 포럼](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179592) | 강원ICT융합연구원 | K-Startup 사업공고 |
| 2026-10-28 | [동국대학교 BMC창업보육센터(고양)신규 입주기업 모집공고(2026년 6차)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179360) | 동국대학교 BMC창업보육센터 | K-Startup 사업공고 |

## 스타트업 뉴스

| 날짜 | 제목 | 출처 |
|---|---|---|
| 2026-10-25 | [5만명 가르친 건축 스타트업, 이제 집을 바꾼다…렉터스 박상근 대표](https://www.venturesquare.net/1117989/) | 벤처스퀘어 |
| 2026-10-25 | [“AI가 추천하는 브랜드를 설계한다”… 스토어링크, AI 마케팅 플랫폼으로 전환](https://www.venturesquare.net/1122669/) | 벤처스퀘어 |
| 2026-10-26 | [아날로그에이아이 이재준 대표, ‘계산하는 메모리’로 초저전력 AI 반도체에 도전](https://www.venturesquare.net/1122655/) | 벤처스퀘어 |
| 2026-10-26 | [아임웹, AI가 실행하고 개발자가 판단하는 협업 방식 공유…첫 기술 밋업 개최](https://www.venturesquare.net/1122630/) | 벤처스퀘어 |
| 2026-10-26 | [허드슨에이아이, 더빙 제작부터 품질 검수까지 AI로 통합…콘텐츠 현지화 자동화 기술 공개](https://www.venturesquare.net/1122716/) | 벤처스퀘어 |
| 2026-10-26 | [메디리타, 멀티오믹스 AI로 신약 후보물질 발굴부터 효능 예측까지](https://www.venturesquare.net/1122700/) | 벤처스퀘어 |
| 2026-10-26 | [브이유에스, 폐기물 수거차량에 AI 계량 기술 적용…딥테크 팁스 선정](https://www.venturesquare.net/1122720/) | 벤처스퀘어 |
| 2026-10-26 | [젠엑시스, 서울창조경제혁신센터와 손잡고 스타트업 투자금 회수·재투자 연결](https://www.venturesquare.net/1122724/) | 벤처스퀘어 |
| 2026-10-26 | [리멤버, 17개 산업 CEO 300명 모아 AI 도입 전략 공유…첫 ‘디시전 메이커스 서밋’ 개최](https://www.venturesquare.net/1122742/) | 벤처스퀘어 |
| 2026-10-26 | [두나무앤파트너스, 우주 데이터센터 스타클라우드 투자…23억 달러 기업가치 인정](https://www.venturesquare.net/1122747/) | 벤처스퀘어 |
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
