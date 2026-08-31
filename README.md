# All-about-Korea-Startup-Information

세종 청년창업 기관 공지 · 정부 지원사업 공고 · 스타트업 뉴스를 **매일 14:00 KST에 자동 수집**하는 저장소.
GitHub Actions가 수집→중복제거→상세저장→아래 대시보드 갱신→텔레그램 브리핑까지 수행한다 (git-scraping — 서버·DB·API 비용 없음).

**완전 규칙 기반**: 소스마다 공식 API/RSS 또는 정규식 파서를 쓴다(LLM 미사용, 고정비 $0). 대신 사이트가 개편되면 파서가 조용히 0건을 낼 수 있어, 같은 소스가 **연속 2회 이상 0건**이면 `data/source_health.json`에 기록하고 다이제스트에 "⚠️ 소스 점검 필요"로 경고한다 — 이게 규칙 기반의 유일한 약점(개편에 안 깨지는 AI 추출 대비)을 메우는 피드백 루프다.

<!-- AUTO:START -->

_자동 갱신: 2026-08-31 (KST)_

## 마감 임박 지원사업

| 마감 | 공고 | 기관 | 출처 |
|---|---|---|---|
| 2026-08-31 | [2026 벤처확인 인증준비기업 맞춤형 무료 진단 지원사업](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178745) | (주)엠비즈플래닛 산하 혁신기술경영인증지원센터 | K-Startup 사업공고 |
| 2026-08-31 | [[국토교통부 x 물류산업진흥재단] 2026 물류상생 Meet-up 행사 기술기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178731) | 물류산업진흥재단 | K-Startup 사업공고 |
| 2026-08-31 | [2026 대덕특구 딥테크 혁신성장 플랫폼(전략기술 발굴 및 매칭) (8/1 ~ 8/31)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178719) | 연구개발특구진흥재단 | K-Startup 사업공고 |
| 2026-08-31 | [[KEA] IoT제품 개발 지원 및 빅데이터 분석 과제기획 수요기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178718) | 한국전자정보통신산업진흥회 | K-Startup 사업공고 |
| 2026-08-31 | [(기간연장)[창업점검] 2026년 체육인 직업안정사업(창업열매) 참여자 추가 모집_(~8.31마감시)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178693) | 국민체육진흥공단 | K-Startup 사업공고 |
| 2026-08-31 | [[무료 AI 역량강화 교육] 생성형 AI기반, 글로벌 마케팅 자동화 및 현지화 에이전트 구축과](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178672) | (주)글로벌창업연구소 | K-Startup 사업공고 |
| 2026-08-31 | [2026 Nexus Connect 오픈이노베이션 밋업 데이](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178795) | (재)충남창조경제혁신센터 | K-Startup 사업공고 |
| 2026-08-31 | [충북대학교 『글로벌(G)테크벤처센터(BI) 』 입주기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178781) | 충북대학교 글로벌(G)테크벤처센터 | K-Startup 사업공고 |
| 2026-08-31 | [2026 협성대학교 창업보육센터 하반기 신규 입주기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178771) | 협성대학교 창업보육센터 | K-Startup 사업공고 |
| 2026-08-31 | [해외진출 기업 대상 AI 통역 서비스 「아네스노트」 이용권 지원](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178765) | 주식회사 팀제로코드 | K-Startup 사업공고 |
| 2026-08-31 | [2026년 스타 IR 데모데이 참여기업 모집공고(4차)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178740) | 스타에셋파트너스 주식회사 | K-Startup 사업공고 |
| 2026-08-31 | [제3회 K-ROBOTICS Startup CUP 참가팀 모집(~8/31 마감)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178841) | KAIST | K-Startup 사업공고 |
| 2026-08-31 | [「민관협력 오픈이노베이션 지원」 '공공데이터 활용 지원' 창업기업 제안 협업 과제(Bottom-Up) 모집공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178875) | 중소벤처기업부장관 | K-Startup 사업공고 |
| 2026-08-31 | [「민관협력 오픈이노베이션 지원」'공공데이터 활용 지원' 공공기관 제안 협업 과제(Top-Down) 모집공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178873) | 중소벤처기업 | K-Startup 사업공고 |
| 2026-08-31 | [2026년 여성CEO 비즈니스 아카데미 호남권역 시즌 2](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178894) | 한국여성경제인협회 | K-Startup 사업공고 |
| 2026-08-31 | [2026년 특허출원·등록 비용 바우처 지원사업 11차(하반기 4차)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178870) | (사)한국중소기업발전협회 | K-Startup 사업공고 |
| 2026-08-31 | [2026년 8월 KICXUP 서울 입주기업 모집공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178867) | 한국산업단지공단,씨엔티테크 | K-Startup 사업공고 |
| 2026-08-31 | [이재용 회계사와 함께하는 ‘스타트업 재무 특강’ 참여자 모집 (『신한 스퀘어브릿지 대전』 X SIW BRIDGE TALK)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178932) | 신한금융희망재단 | K-Startup 사업공고 |
| 2026-08-31 | [26년 8월 스타트업 언론 홍보 지원사업 참가사 모집 공고(2차)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178912) | 스타트업 데일리 | K-Startup 사업공고 |
| 2026-08-31 | [2026년 한국광해광업공단 상생형 창업‧벤처기업 지원사업 참여기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178946) | 한국광해광업공단 | K-Startup 사업공고 |

## 스타트업 뉴스

| 날짜 | 제목 | 출처 |
|---|---|---|
| 2026-08-31 | [틱톡 아이섀도 1위에서 타겟 611개 매장으로…카자, 미국 소비자 일상 동선 공략](https://www.venturesquare.net/1109632/) | 벤처스퀘어 |
| 2026-08-31 | [남성 가임력·영양 상태 확인, 약국에서 산다…윈티 전국 유통 확대](https://www.venturesquare.net/1109636/) | 벤처스퀘어 |
| 2026-08-31 | [10번 찾은 단골 72%가 3040…컬리N마트, 거래액 1년 새 10배](https://www.venturesquare.net/1109647/) | 벤처스퀘어 |
| 2026-08-31 | [발행주식 0.7% 없앤다…예선테크, 자사주 4만8989주 소각](https://www.venturesquare.net/1109654/) | 벤처스퀘어 |
| 2026-08-31 | [캐나다서 검증하고 북미로…TBDC·KOC, 5개 도시 스타트업 로드쇼](https://www.venturesquare.net/1109662/) | 벤처스퀘어 |
| 2026-08-31 | [스쿨존 지키는 CCTV·에어백 펜스…‘아이가드’ 부산시장상](https://www.venturesquare.net/1109670/) | 벤처스퀘어 |
| 2026-08-31 | [클라우드 없이 집 안에서 판단…코아시아세미, LG전자 주도 AI 홈 칩 2종 개발](https://www.venturesquare.net/1109678/) | 벤처스퀘어 |
| 2026-08-31 | [AI 에이전트에 금융 인프라 연다…바이낸스, 권한 통제형 ‘에이전트 OS’ 공개](https://www.venturesquare.net/1109685/) | 벤처스퀘어 |
| 2026-08-31 | [PC 파일 읽고 이사 일정 챙긴다…이스트소프트, AI 비서 ‘알비서’ 하반기 출시](https://www.venturesquare.net/1109688/) | 벤처스퀘어 |
| 2026-08-31 | [인터넷 없이 5시간, 물리올림피아드 이론 28.6점…아스테로모프 AI 현장 평가](https://www.venturesquare.net/1109697/) | 벤처스퀘어 |
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
