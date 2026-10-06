# All-about-Korea-Startup-Information

세종 청년창업 기관 공지 · 정부 지원사업 공고 · 스타트업 뉴스를 **매일 14:00 KST에 자동 수집**하는 저장소.
GitHub Actions가 수집→중복제거→상세저장→아래 대시보드 갱신→텔레그램 브리핑까지 수행한다 (git-scraping — 서버·DB·API 비용 없음).

**완전 규칙 기반**: 소스마다 공식 API/RSS 또는 정규식 파서를 쓴다(LLM 미사용, 고정비 $0). 대신 사이트가 개편되면 파서가 조용히 0건을 낼 수 있어, 같은 소스가 **연속 2회 이상 0건**이면 `data/source_health.json`에 기록하고 다이제스트에 "⚠️ 소스 점검 필요"로 경고한다 — 이게 규칙 기반의 유일한 약점(개편에 안 깨지는 AI 추출 대비)을 메우는 피드백 루프다.

<!-- AUTO:START -->

_자동 갱신: 2026-10-06 (KST)_

## 마감 임박 지원사업

| 마감 | 공고 | 기관 | 출처 |
|---|---|---|---|
| 2026-10-06 | [2026 LX세미콘 x 충남창조경제혁신센터 Nexus Connect 오픈이노베이션 밋업 데이](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179190) | (재)충남창조경제혁신센터 | K-Startup 사업공고 |
| 2026-10-06 | [2026 마포 청년 창업 아이디어 경진대회(MAPO NEXT STAGE)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179252) | 마포청년창업취업지원센터 나루 | K-Startup 사업공고 |
| 2026-10-06 | [「민관협력 오픈이노베이션 지원」 '공공데이터 활용 지원' 공공기관 제안형(Top-Down) 창업기업 모집공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179232) | 중소벤처기업부장관 | K-Startup 사업공고 |
| 2026-10-06 | [2026. 하반기 도봉구 외식업 창업 교육생 모집공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179286) | 도봉구청  | K-Startup 사업공고 |
| 2026-10-06 | [동국대학교 창업보육센터(서울) 신규 입주기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179296) | 동국대학교 창업보육센터 | K-Startup 사업공고 |
| 2026-10-06 | [[경희창업보육센터(서울)] 2026년 하반기 신규 입주기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179345) | 경희창업보육센터 | K-Startup 사업공고 |
| 2026-10-06 | [[강동구 청년해냄센터] 전문분야 창업멘토링 10월 참가자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179330) | 강동구 청년해냄센터 | K-Startup 사업공고 |
| 2026-10-06 | [청년의 아이디어가 브랜드가 되는 과정 | RE:CREATE 성수 인사이트포럼 「성수, 브랜드의 전성시대」 참가자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179317) | 성동청년 창업이룸센터 | K-Startup 사업공고 |
| 2026-10-06 | [2026년 여성CEO 비즈니스 아카데미 강원권역 시즌 2](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179298) | 한국여성경제인협회 | K-Startup 사업공고 |
| 2026-10-06 | [[모집공고] 「시장·고객 발굴(Market to Tech) 프로그램」 참가자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179406) | 프로그램 운영사무국 | K-Startup 사업공고 |
| 2026-10-06 | [[서울과학기술대학교]3D프린터 장비교육](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179405) | 서울과학기술대학교 | K-Startup 사업공고 |
| 2026-10-06 | [★★ 2026년 가톨릭대학교 창업보육센터 입주기업 모집 공고 ★★](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179343) | 가톨릭대학교 창업보육센터 | K-Startup 사업공고 |
| 2026-10-07 | [[숭실대학교 캠퍼스타운] 2026 석·박사급 실험실 창업스쿨(유형2) 참여자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179054) | 숭실대학교 캠퍼스타운사업단 | K-Startup 사업공고 |
| 2026-10-07 | [2026년 투자 유치 역량 강화 특강](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179183) | 동대문구 창업지원센터 | K-Startup 사업공고 |
| 2026-10-07 | [2026년 민간 산림복지 창업 아카데미[2차] 참가자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179276) | 한국산림복지진흥원 | K-Startup 사업공고 |
| 2026-10-07 | [2026년 블록체인 기업성장허브 입주기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179303) | 한국인터넷진흥원 | K-Startup 사업공고 |
| 2026-10-07 | [구로구 청년창업지원센터 일반 창업교육(하반기: 4회차): 온라인 마케팅 실전 가이드](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179300) | 구로구 청년창업지원센터 | K-Startup 사업공고 |
| 2026-10-07 | [창업 초보를 위한 창업 A-Z 교육](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179247) | 하우그로우 원격평생교육원 | K-Startup 사업공고 |
| 2026-10-07 | [로컬창업캠프 2기](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179314) | 관악구청 | K-Startup 사업공고 |
| 2026-10-07 | [2026 전북-수도권 기업 『투자 & 비즈니스 라운드』](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179349) | 쿠키미디어(주) | K-Startup 사업공고 |

## 스타트업 뉴스

| 날짜 | 제목 | 출처 |
|---|---|---|
| 2026-10-05 | [‘모두의 IR’ 다음은 진짜 투자…6만3000명 ‘모두의 창업’의 두 번째 시험대](https://www.venturesquare.net/1117839/) | 벤처스퀘어 |
| 2026-10-05 | [인포시즈, 보안 로그 0.068%만 LLM이 다시 본다…그래프 AI ‘GOS’ 출시](https://www.venturesquare.net/1117848/) | 벤처스퀘어 |
| 2026-10-05 | [아이싸이, 움직이는 해군 함정서 SAR 위성정보 바로 받았다…‘ISR Cell’ 함상 운용](https://www.venturesquare.net/1117851/) | 벤처스퀘어 |
| 2026-10-05 | [브이씨루트, 지방 스타트업에 ‘지역 의무투자 펀드’ 먼저 찾는다…159개·2.3조원 매칭](https://www.venturesquare.net/1117858/) | 벤처스퀘어 |
| 2026-10-05 | [네이버페이·하나은행·서울신보, 골목상권에 687.5억원 보증…청년 사업자 한도 130% 우대](https://www.venturesquare.net/1117871/) | 벤처스퀘어 |
| 2026-10-06 | [부산창조경제혁신센터, K스타트업 11곳 오사카·고베로…GSE 2026서 일본 기업과 사업 연결](https://www.venturesquare.net/1117886/) | 벤처스퀘어 |
| 2026-10-06 | [네이버, 1926년 한글 점자부터 2003년 가계부까지…한글날 100년 기록 꺼냈다](https://www.venturesquare.net/1117901/) | 벤처스퀘어 |
| 2026-10-06 | [AI스페라, 자산 찾는 ASM 넘어 ‘어떤 위협부터 막을지’ AI가 추린다…싱가포르서 AITEM 공개](https://www.venturesquare.net/1117908/) | 벤처스퀘어 |
| 2026-10-06 | [넷플릭스, K콘텐츠 더빙 비중 40% 넘었다…멕시코서 ‘언어 장벽’ 넘는 현지화 조명](https://www.venturesquare.net/1117914/) | 벤처스퀘어 |
| 2026-10-06 | [원프레딕트, 공장마다 다시 만들던 AI ‘공통 모듈’로…7368억원 국가 피지컬AI 사업 참여](https://www.venturesquare.net/1117936/) | 벤처스퀘어 |
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
