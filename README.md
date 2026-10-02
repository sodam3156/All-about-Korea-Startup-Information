# All-about-Korea-Startup-Information

세종 청년창업 기관 공지 · 정부 지원사업 공고 · 스타트업 뉴스를 **매일 14:00 KST에 자동 수집**하는 저장소.
GitHub Actions가 수집→중복제거→상세저장→아래 대시보드 갱신→텔레그램 브리핑까지 수행한다 (git-scraping — 서버·DB·API 비용 없음).

**완전 규칙 기반**: 소스마다 공식 API/RSS 또는 정규식 파서를 쓴다(LLM 미사용, 고정비 $0). 대신 사이트가 개편되면 파서가 조용히 0건을 낼 수 있어, 같은 소스가 **연속 2회 이상 0건**이면 `data/source_health.json`에 기록하고 다이제스트에 "⚠️ 소스 점검 필요"로 경고한다 — 이게 규칙 기반의 유일한 약점(개편에 안 깨지는 AI 추출 대비)을 메우는 피드백 루프다.

<!-- AUTO:START -->

_자동 갱신: 2026-10-02 (KST)_

## 마감 임박 지원사업

| 마감 | 공고 | 기관 | 출처 |
|---|---|---|---|
| 2026-10-02 | [2026년 영등포 청년 창업 도약 아카데미](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179116) | 서울창조경제혁신센터 | K-Startup 사업공고 |
| 2026-10-02 | [2026년 바이오벤치마킹스쿨(BBS) 16기 수강자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179145) | 주식회사 비티비벤처스 | K-Startup 사업공고 |
| 2026-10-02 | [「충북 제조창업 마스터 매칭 프로그램」 참여기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179288) | 충북창조경제혁신센터, 충북Pro메이커센터, 충부테크노파크 | K-Startup 사업공고 |
| 2026-10-02 | [2026년 초기창업패키지 로켓십 IR 경진대회 참가기업 모집 (2회차: 콘텐츠·플랫폼)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179246) | 씨엔티테크(주) | K-Startup 사업공고 |
| 2026-10-02 | [2026년 1차 홍릉벤처밸리 창업보육센터 입주기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179215) | 키스트이노베이션 | K-Startup 사업공고 |
| 2026-10-02 | [[창업] 창업가를 위한 가격 전략 실전](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179310) | 마포청년창업취업지원센터 나루 | K-Startup 사업공고 |
| 2026-10-02 | [[코레일유통/본사] 제12차 청년창업 제휴사업자 모집공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179313) | 코레일유통(주) | K-Startup 사업공고 |
| 2026-10-02 | [(모집연장)2026년 튀르키예 이스탄불 식품 박람회 참가기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179332) | 서울경제진흥원 | K-Startup 사업공고 |
| 2026-10-02 | [인수창업(ETA) 실증 지원을 위한 인수자의 실사지원 프로그램](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179321) | 주식회사 디유파트너스 | K-Startup 사업공고 |
| 2026-10-04 | [2026 「Go to Market」동남권 창업기업 온라인 판로개척 교육 참가자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179339) | 경상국립대학교 창업중심대학사업단 | K-Startup 사업공고 |
| 2026-10-05 | [2026년 강북창업지원센터 하반기 신규 입주기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179092) | 강북청년창업마루 | K-Startup 사업공고 |
| 2026-10-05 | [2026년 10월 크립톤 IR피칭 & 오피스아워 신청 접수](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179304) | 크립톤 부산센터 | K-Startup 사업공고 |
| 2026-10-05 | [2026 옥천군 로컬 크리에이터 아카데미](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179354) | (주)렛츠 | K-Startup 사업공고 |
| 2026-10-05 | [2026년 성북구 중장년 기술창업센터 입주기업 모집공고(3차)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179320) | 성북구중장년기술창업센터장 | K-Startup 사업공고 |
| 2026-10-06 | [2026 LX세미콘 x 충남창조경제혁신센터 Nexus Connect 오픈이노베이션 밋업 데이](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179190) | (재)충남창조경제혁신센터 | K-Startup 사업공고 |
| 2026-10-06 | [2026 마포 청년 창업 아이디어 경진대회(MAPO NEXT STAGE)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179252) | 마포청년창업취업지원센터 나루 | K-Startup 사업공고 |
| 2026-10-06 | [「민관협력 오픈이노베이션 지원」 '공공데이터 활용 지원' 공공기관 제안형(Top-Down) 창업기업 모집공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179232) | 중소벤처기업부장관 | K-Startup 사업공고 |
| 2026-10-06 | [2026. 하반기 도봉구 외식업 창업 교육생 모집공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179286) | 도봉구청  | K-Startup 사업공고 |
| 2026-10-06 | [동국대학교 창업보육센터(서울) 신규 입주기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179296) | 동국대학교 창업보육센터 | K-Startup 사업공고 |
| 2026-10-06 | [[경희창업보육센터(서울)] 2026년 하반기 신규 입주기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179345) | 경희창업보육센터 | K-Startup 사업공고 |

## 스타트업 뉴스

| 날짜 | 제목 | 출처 |
|---|---|---|
| 2026-10-01 | [대화의 기록을 ‘다음 대화의 근거’로… 리버스마운틴 김경민 대표가 만드는 원온원](https://www.venturesquare.net/1116492/) | 벤처스퀘어 |
| 2026-10-01 | [앰플몬스터, 일본 돈키호테 100곳에 들어간다…NMN·PDRN 4종 오프라인 확대](https://www.venturesquare.net/1117500/) | 벤처스퀘어 |
| 2026-10-02 | [크라우드웍스, 사람이 로봇 움직이면 학습 데이터로 바꾼다…‘AI Festa 2026’서 시연](https://www.venturesquare.net/1117524/) | 벤처스퀘어 |
| 2026-10-02 | [수이·오픈애셋, 증권·펀드 토큰화 ‘공통 언어’ 만든다…OTAS 표준 개발](https://www.venturesquare.net/1117533/) | 벤처스퀘어 |
| 2026-10-02 | [관악연구소, 금융권 ‘누구부터 관리할지’ AI가 제안한다…서울대기술지주 3억원 투자](https://www.venturesquare.net/1117536/) | 벤처스퀘어 |
| 2026-10-02 | [코드잇, 강남역 16개 층 통째로 교육공간 만든다…첫 오프라인 거점 ‘텐엑스 강남’](https://www.venturesquare.net/1117542/) | 벤처스퀘어 |
| 2026-10-02 | [쓰리빌리언, 미국 첫 임상검사실 구축 맡길 전문가 영입…CLIA·CAP 인증 추진](https://www.venturesquare.net/1117549/) | 벤처스퀘어 |
| 2026-10-02 | [케어닥, 안양·남양주 시니어하우징에 694억원 PF…누적 조달 1000억원 넘어](https://www.venturesquare.net/1117552/) | 벤처스퀘어 |
| 2026-10-02 | [크릿벤처스, ‘오딘’ CTO가 세운 제이드래곤게임즈에 투자…신작 MMORPG 개발](https://www.venturesquare.net/1117561/) | 벤처스퀘어 |
| 2026-10-02 | [알스퀘어, 성수서 베리시 두 번째 매장 연결…300평·4층 복합공간 출점 자문](https://www.venturesquare.net/1117573/) | 벤처스퀘어 |
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
