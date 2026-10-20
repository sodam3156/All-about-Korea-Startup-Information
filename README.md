# All-about-Korea-Startup-Information

세종 청년창업 기관 공지 · 정부 지원사업 공고 · 스타트업 뉴스를 **매일 14:00 KST에 자동 수집**하는 저장소.
GitHub Actions가 수집→중복제거→상세저장→아래 대시보드 갱신→텔레그램 브리핑까지 수행한다 (git-scraping — 서버·DB·API 비용 없음).

**완전 규칙 기반**: 소스마다 공식 API/RSS 또는 정규식 파서를 쓴다(LLM 미사용, 고정비 $0). 대신 사이트가 개편되면 파서가 조용히 0건을 낼 수 있어, 같은 소스가 **연속 2회 이상 0건**이면 `data/source_health.json`에 기록하고 다이제스트에 "⚠️ 소스 점검 필요"로 경고한다 — 이게 규칙 기반의 유일한 약점(개편에 안 깨지는 AI 추출 대비)을 메우는 피드백 루프다.

<!-- AUTO:START -->

_자동 갱신: 2026-10-20 (KST)_

## 마감 임박 지원사업

| 마감 | 공고 | 기관 | 출처 |
|---|---|---|---|
| 2026-10-20 | [제3회 AI 및 기술기반 창업 트렌드 세미나 참가자 모집 (AI 비즈니스 실전 전략 : 멀티모달·에이전트 AX·AI 거버넌스)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179236) | 경기창조경제혁신센터 | K-Startup 사업공고 |
| 2026-10-20 | [이타카앤파트너스 조용민 대표 초청 특강 - 내가 투자한 스타트업과 성공하는 창업가의 3가지 비밀](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179426) | 경기도·경기도경제과학진흥원 | K-Startup 사업공고 |
| 2026-10-20 | [2026년 웰컴 투 팁스 6차 참가기업 모집 (전북권)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179466) | (주)로우파트너스 | K-Startup 사업공고 |
| 2026-10-20 | [2026년 웰컴 투 팁스 5차 참가기업 모집 (호남권)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179464) | (주)로우파트너스 | K-Startup 사업공고 |
| 2026-10-20 | [2026 생물자원 활용 창업벤처 지원을 위한 기업 간담회 (3회차) 참여기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179445) | 탭엔젤파트너스 | K-Startup 사업공고 |
| 2026-10-20 | [2026년 창업기업(예비창업자) 사업고도화 창업교육 참여자 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179437) | 통영시장 | K-Startup 사업공고 |
| 2026-10-20 | [제46회 창업가정신포럼](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179425) | (재)경기창조경제혁신센터  | K-Startup 사업공고 |
| 2026-10-20 | [[대전창조경제혁신센터] 2026 대전 제조파트너스 매칭데이 참가자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179482) | 대전창조경제혁신센터 | K-Startup 사업공고 |
| 2026-10-20 | [2026-5회 호남 엔젤리더스포럼 in 전남광주](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179475) | 한국엔젤투자협회 호남권 엔젤투자허브 | K-Startup 사업공고 |
| 2026-10-20 | [2026년 프로젝트 창업 인큐베이팅 : 2027 모두의 창업 선정 프로젝트](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179446) | 2026년 프로젝트 창업 인큐베이팅 운영사무국 | K-Startup 사업공고 |
| 2026-10-20 | [가죽·패션 제품개발 협업사업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179507) | 서울시 강동가죽제조지원센터 | K-Startup 사업공고 |
| 2026-10-21 | [파주청년창업지원센터 하반기 청년 창업아카데미 참여기업/팀 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179318) | 파주시, (재)경기테크노파크 | K-Startup 사업공고 |
| 2026-10-21 | [[서초창업스테이션] 서리풀 소상공인 창업 클리닉(10월) - 소상공인 1:1 컨설팅](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179370) | 서초창업스테이션 | K-Startup 사업공고 |
| 2026-10-21 | [2026년 제3차 I-PLEX광주 입주기업 모집공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179442) | (재)광주테크노파크 | K-Startup 사업공고 |
| 2026-10-21 | [구로구 청년창업지원센터 일반 창업교육(하반기: 5회차): 투자를 위한 비즈니스 모델 수립 전략](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179457) | 구로구 청년창업지원센터 | K-Startup 사업공고 |
| 2026-10-21 | [바이오/헬스케어 기업들을 위한 「2026 혁신신약살롱 마곡」 참여 안내](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179492) | (재)서울경제진흥원 | K-Startup 사업공고 |
| 2026-10-21 | [2026 충남창업마루나비 하반기 입주기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179524) | 충남창조경제혁신센터 | K-Startup 사업공고 |
| 2026-10-22 | [2026년 강북창업지원센터 10월 창업 교육 및 그룹상담 프로그램 참가자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179418) | 강북청년창업마루 | K-Startup 사업공고 |
| 2026-10-22 | [쇼미더임팩트 시즌6 참가자 모집 [IMPACT IR 경연대회]](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179375) | 충남사회적경제지원센터장 | K-Startup 사업공고 |
| 2026-10-22 | [[강동구 청년해냄센터] 2026 모의창업스쿨 2차 교육 참가자 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179460) | 강동구 청년해냄센터 | K-Startup 사업공고 |

## 스타트업 뉴스

| 날짜 | 제목 | 출처 |
|---|---|---|
| 2026-10-19 | [데브디, MYSC 후속 투자 유치…월세 카드결제 ‘집업페이’ 상업용 임대료 시장 확대](https://www.venturesquare.net/1121168/) | 벤처스퀘어 |
| 2026-10-19 | [매쉬업벤처스, 딥테크 투자 확대…AI·신소재·에너지·우주 스타트업 5곳 소개](https://www.venturesquare.net/1121175/) | 벤처스퀘어 |
| 2026-10-19 | [크린토피아, IFS 창업박람회서 1천만원대 창업 모델 공개…상권 분석·가맹 혜택 제공](https://www.venturesquare.net/1121177/) | 벤처스퀘어 |
| 2026-10-19 | [지브라 테크놀로지스, 레드닷 디자인 어워드 3관왕…AI 모바일·웨어러블·스캐너 수상](https://www.venturesquare.net/1121189/) | 벤처스퀘어 |
| 2026-10-19 | [아이스타트업랩·마음인베스트먼트, 개인투자조합 결성…인하대·청년 창업기업 투자 지원](https://www.venturesquare.net/1121196/) | 벤처스퀘어 |
| 2026-10-19 | [엘핀, 위치인증·블록체인 결합한 ‘워크플러스’ 개발…출퇴근·외근 기록 통합 관리](https://www.venturesquare.net/1121207/) | 벤처스퀘어 |
| 2026-10-19 | [[VS 기획] 데이터센터는 황금알 낳는 부동산일까…AI 열풍 속 개발 리스크 따져보니](https://www.venturesquare.net/1118800/) | 벤처스퀘어 |
| 2026-10-19 | [“책 한 권이 AI 데이터가 되면 가격도 달라진다”…전병욱 멘탯 대표가 찾은 출판의 새 시장](https://www.venturesquare.net/1121235/) | 벤처스퀘어 |
| 2026-10-20 | [스템덴, 치수줄기세포 활성화 기술로 상아질 재생 치료제 개발](https://www.venturesquare.net/1121198/) | 벤처스퀘어 |
| 2026-10-20 | [티인테크놀로지, X-ray 방사선 노출 저감 위한 초고압 전원모듈 개발](https://www.venturesquare.net/1120849/) | 벤처스퀘어 |
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
