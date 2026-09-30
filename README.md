# All-about-Korea-Startup-Information

세종 청년창업 기관 공지 · 정부 지원사업 공고 · 스타트업 뉴스를 **매일 14:00 KST에 자동 수집**하는 저장소.
GitHub Actions가 수집→중복제거→상세저장→아래 대시보드 갱신→텔레그램 브리핑까지 수행한다 (git-scraping — 서버·DB·API 비용 없음).

**완전 규칙 기반**: 소스마다 공식 API/RSS 또는 정규식 파서를 쓴다(LLM 미사용, 고정비 $0). 대신 사이트가 개편되면 파서가 조용히 0건을 낼 수 있어, 같은 소스가 **연속 2회 이상 0건**이면 `data/source_health.json`에 기록하고 다이제스트에 "⚠️ 소스 점검 필요"로 경고한다 — 이게 규칙 기반의 유일한 약점(개편에 안 깨지는 AI 추출 대비)을 메우는 피드백 루프다.

<!-- AUTO:START -->

_자동 갱신: 2026-09-30 (KST)_

## 마감 임박 지원사업

| 마감 | 공고 | 기관 | 출처 |
|---|---|---|---|
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
| 2026-09-30 | [[동대문구 창업지원센터] 9월 메이커스페이스(레이저커터, 3D프린팅) 교육 일정](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179096) | 동대문구 창업지원센터 | K-Startup 사업공고 |
| 2026-09-30 | [2026년 09월 초기 창업기업 대상 벤처기업 인증 행정자문&전략 수립 기업모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179093) | 박준범행정사사무소 | K-Startup 사업공고 |
| 2026-09-30 | [출연연, 대학 연구소기업 Business Development 프로그램 참여 예비창업자 모집 (9월)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179085) | 연구개발특구진흥재단 | K-Startup 사업공고 |
| 2026-09-30 | [2026년 안양산업진흥원 제3차 입주기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179081) | 안양산업진흥원 | K-Startup 사업공고 |
| 2026-09-30 | [2026년 2차 CNU Startup to TIPS 기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179080) | 충남대학교기술지주(주) | K-Startup 사업공고 |
| 2026-09-30 | [[성동구 관내기업] 「모두의 창업⸥ 정부R&D사업 및 베트남 해외진출 컨설팅 지원기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179078) | 성동구청 | K-Startup 사업공고 |
| 2026-09-30 | [2026년 스마트상점 기술보급사업 참여 소상공인 모집공고(2차)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179106) | 소상공인시장진흥공단 | K-Startup 사업공고 |

## 스타트업 뉴스

| 날짜 | 제목 | 출처 |
|---|---|---|
| 2026-09-29 | [파로스아이바이오, 호주를 AI 신약개발 R&D 거점으로…공동연구·사업개발 확대](https://www.venturesquare.net/1116789/) | 벤처스퀘어 |
| 2026-09-29 | [엔젤로보틱스, 사람 움직임을 AI 학습 데이터로 바꾼다…피지컬 AI 연구로봇 ‘phai-x1’ 공개](https://www.venturesquare.net/1116796/) | 벤처스퀘어 |
| 2026-09-29 | [연 1조 투자시장 된 액셀러레이터…전화성 KAIA 회장, 3년의 성과와 다음 과제](https://www.venturesquare.net/1116815/) | 벤처스퀘어 |
| 2026-09-29 | [텐마인즈, 잠들면 베개가 코골이에 반응하고 조명도 꺼진다…‘AI 슬립봇’ 스마트싱스 연동](https://www.venturesquare.net/1116810/) | 벤처스퀘어 |
| 2026-09-29 | [[컬처슬로건 탐방기] 그렙 – 위대한 사람, 성장, 그리고 신뢰](https://www.venturesquare.net/1116830/) | 벤처스퀘어 |
| 2026-09-29 | [패스트파이브, AI 스타트업 10곳에 사무실 최대 6개월 지원…‘창업 베이스캠프’ 2기 모집](https://www.venturesquare.net/1116832/) | 벤처스퀘어 |
| 2026-09-29 | [버즈니·KEA, KES 2026 참가기업 500곳 AI 숏폼 제작 돕는다…‘비스킷AI’ 지원](https://www.venturesquare.net/1116833/) | 벤처스퀘어 |
| 2026-09-29 | [팔로알토 네트웍스, AI가 공격자처럼 상시 보안 테스트…GPT-5.6·클로드 미토스 투입](https://www.venturesquare.net/1116846/) | 벤처스퀘어 |
| 2026-09-29 | [AI스페라, IP만 넣으면 연결된 도메인 AI가 찾는다…네트워크 위협 분석 기술 특허](https://www.venturesquare.net/1116850/) | 벤처스퀘어 |
| 2026-09-29 | [시마AI, 2036억원 시리즈C 유치…휴머노이드·드론 겨냥 ‘1000 TOPS’ 피지컬 AI 칩 개발](https://www.venturesquare.net/1116862/) | 벤처스퀘어 |
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
