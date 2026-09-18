# All-about-Korea-Startup-Information

세종 청년창업 기관 공지 · 정부 지원사업 공고 · 스타트업 뉴스를 **매일 14:00 KST에 자동 수집**하는 저장소.
GitHub Actions가 수집→중복제거→상세저장→아래 대시보드 갱신→텔레그램 브리핑까지 수행한다 (git-scraping — 서버·DB·API 비용 없음).

**완전 규칙 기반**: 소스마다 공식 API/RSS 또는 정규식 파서를 쓴다(LLM 미사용, 고정비 $0). 대신 사이트가 개편되면 파서가 조용히 0건을 낼 수 있어, 같은 소스가 **연속 2회 이상 0건**이면 `data/source_health.json`에 기록하고 다이제스트에 "⚠️ 소스 점검 필요"로 경고한다 — 이게 규칙 기반의 유일한 약점(개편에 안 깨지는 AI 추출 대비)을 메우는 피드백 루프다.

<!-- AUTO:START -->

_자동 갱신: 2026-09-18 (KST)_

## 마감 임박 지원사업

| 마감 | 공고 | 기관 | 출처 |
|---|---|---|---|
| 2026-09-18 | [[숭실대학교 캠퍼스타운] 2026 숭실 스타트업 아카데미 9월 참여자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178890) | 숭실대학교 캠퍼스타운사업단 | K-Startup 사업공고 |
| 2026-09-18 | [2026년 하반기 벤처확인 도전기업 일대일 비대면 밋업 참여기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178947) | (주)엠비즈플래닛 산하 혁신기술경영인증지원센터 | K-Startup 사업공고 |
| 2026-09-18 | [2026년 안산정보산업진흥센터(경기TP안산창업보육센터) 제3차 신규 입주자 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179172) | (재)경기테크노파크 | K-Startup 사업공고 |
| 2026-09-18 | [2026 서울AI로봇쇼 피지컬 AI 포럼 참관객 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179158) | (재)서울경제진흥원 | K-Startup 사업공고 |
| 2026-09-18 | [성남 기후테크 UpSkill 아카데미 Vol.2 - 비즈니스모델 개발과 기술사업화](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179125) | 도시혁신그룹 무브먼트 주식회사 | K-Startup 사업공고 |
| 2026-09-18 | [로컬임팩트는 왜 확장되지 않는가? | 신한금융희망재단 × 제3회 대한민국 사회적가치 페스타](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179176) | 신한금융희망재단 | K-Startup 사업공고 |
| 2026-09-18 | [[서초창업스테이션] 9월 창업 교육 - 스타트업을 위한 온라인 판로개척](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179167) | 서초창업스테이션 | K-Startup 사업공고 |
| 2026-09-18 | [2026년 재도전 마인드업(힐링캠프) 참여자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179260) | 중소벤처기업진흥공단 | K-Startup 사업공고 |
| 2026-09-18 | [창업·벤처 녹색융합클러스터 그린아이디어랩(비상주오피스) 청년 이용자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179235) | 한국환경산업기술원 | K-Startup 사업공고 |
| 2026-09-20 | [[환경재단] 2027 어스샷 상 혁신 환경 솔루션 공모](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178997) | 환경재단 | K-Startup 사업공고 |
| 2026-09-20 | [[숭실대학교 캠퍼스타운] 숭실대 캠퍼스타운 x 에네이 클라우드 AX전환 PBL과정 참여자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179117) | 숭실대학교 캠퍼스타운사업단 | K-Startup 사업공고 |
| 2026-09-20 | [2026년 서강비즈니스센터 입주기업 모집(~9/20)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179198) | 서강대학교 창업지원단 | K-Startup 사업공고 |
| 2026-09-20 | [[고양시×스타필드 고양] 2026 고양 스타트업 팝업스토어 참가기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179191) | 고양시장 | K-Startup 사업공고 |
| 2026-09-20 | [2026년 과천시 지식정보타운 무상임대 입주기업(과천크리에이션타워) 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179228) | 과천시 창업지원센터 | K-Startup 사업공고 |
| 2026-09-20 | [2026년 과천시 지식정보타운 무상임대 입주기업(과천상상자이타워) 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179227) | 과천시 창업지원센터 | K-Startup 사업공고 |
| 2026-09-21 | [2026년 GovTech 창업경진대회](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178968) | 정보통신산업진흥원 | K-Startup 사업공고 |
| 2026-09-21 | [인천스타트업파크 부스트 스타트업 SCEWC 2026 참가기업 모집공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179104) | (재)인천테크노파크 원장 | K-Startup 사업공고 |
| 2026-09-21 | [2026 고양시 청년 창업가 네트워킹 및 선배 창업가 특강](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179185) | 고양산업진흥원 | K-Startup 사업공고 |
| 2026-09-21 | [2026년 패션기업 연말 맞춤형 제품 제작·프로모션 지원사업 참여기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179157) | 서울경제진흥원 | K-Startup 사업공고 |
| 2026-09-21 | [청년 창업 인사이트 밋업](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179134) | 관악구청 | K-Startup 사업공고 |

## 스타트업 뉴스

| 날짜 | 제목 | 출처 |
|---|---|---|
| 2026-09-18 | [위얼라이브, 매출 2년 새 7.7배 성장…시리즈A 투자로 아시아 공연 IP 확장](https://www.venturesquare.net/1114983/) | 벤처스퀘어 |
| 2026-09-18 | [AI스페라, 취약점 뜨면 영향받는 자산 AI가 찾는다…AITEM에 MS 파운드리 적용](https://www.venturesquare.net/1114991/) | 벤처스퀘어 |
| 2026-09-18 | [카카오벤처스, AI 창업가 한곳에 모았다…템프서울 열고 상하이 빌더와 연결](https://www.venturesquare.net/1115005/) | 벤처스퀘어 |
| 2026-09-18 | [로브로스, 휴머노이드 36대 생산·18대 판매…제조 AI 전환 성과로 산업부 장관 표창](https://www.venturesquare.net/1115015/) | 벤처스퀘어 |
| 2026-09-18 | [오케스트로 클라우드·KT, AI 서비스부터 GPU·데이터센터까지 묶는다…5개 분야 공동 사업](https://www.venturesquare.net/1115018/) | 벤처스퀘어 |
| 2026-09-18 | [휘슬, 여주서 주정차 단속 알림 시작…추석 귀성객도 별도 가입 없이 이용](https://www.venturesquare.net/1115026/) | 벤처스퀘어 |
| 2026-09-18 | [당근, 러닝 기록도 꾸며서 인증한다…달린 거리 쌓는 로컬러너스 챌린지](https://www.venturesquare.net/1115033/) | 벤처스퀘어 |
| 2026-09-18 | [루닛, 전 세계 1만개 의료기관에 AI 공급…타임 세계 최고 헬스테크 기업 선정](https://www.venturesquare.net/1115045/) | 벤처스퀘어 |
| 2026-09-18 | [어센트 AI, 가전 검색 13.9% 줄었는데 침구청소기는 63.6% 늘었다…소형·위생·구독 부상](https://www.venturesquare.net/1115052/) | 벤처스퀘어 |
| 2026-09-18 | [부산창경, 스타트업 5곳 시민 실증에서 해외 바이어까지…WSCE서 84.7억원 상담](https://www.venturesquare.net/1115062/) | 벤처스퀘어 |
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
