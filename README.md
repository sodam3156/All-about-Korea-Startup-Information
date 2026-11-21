# All-about-Korea-Startup-Information

세종 청년창업 기관 공지 · 정부 지원사업 공고 · 스타트업 뉴스를 **매일 14:00 KST에 자동 수집**하는 저장소.
GitHub Actions가 수집→중복제거→상세저장→아래 대시보드 갱신→텔레그램 브리핑까지 수행한다 (git-scraping — 서버·DB·API 비용 없음).

**완전 규칙 기반**: 소스마다 공식 API/RSS 또는 정규식 파서를 쓴다(LLM 미사용, 고정비 $0). 대신 사이트가 개편되면 파서가 조용히 0건을 낼 수 있어, 같은 소스가 **연속 2회 이상 0건**이면 `data/source_health.json`에 기록하고 다이제스트에 "⚠️ 소스 점검 필요"로 경고한다 — 이게 규칙 기반의 유일한 약점(개편에 안 깨지는 AI 추출 대비)을 메우는 피드백 루프다.

<!-- AUTO:START -->

_자동 갱신: 2026-11-21 (KST)_

## 마감 임박 지원사업

| 마감 | 공고 | 기관 | 출처 |
|---|---|---|---|
| 2026-11-22 | [[인탑스 액셀러레이팅 6기 모집] 제품 디자인·설계·양산부터 IR까지! 하드웨어 스타트업 올인원 스케일업](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179558) | 인탑스 주식회사  | K-Startup 사업공고 |
| 2026-11-22 | [[1:1 무료 코칭데이] 하드웨어 스타트업 디자인·설계·금형·양산, 현직 엔지니어 상담](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179693) | 인탑스 주식회사  | K-Startup 사업공고 |
| 2026-11-22 | [한국외국어대학교 창업보육센터 입주기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179709) | 한국외국어대학교연구산학협력단 | K-Startup 사업공고 |
| 2026-11-22 | [2026년 대전 스타트업 원스톱 지원센터 아카데미 4회차](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179695) | 대전창조경제혁신센터 | K-Startup 사업공고 |
| 2026-11-22 | [경기창업혁신공간 서부권 「스담스담」(오픈 네트워킹) 4회차](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179791) | 경기도경제과학진흥원 | K-Startup 사업공고 |
| 2026-11-23 | [경기대학교 2026년 예비창업패키지 KGU 창업준비 아카데미 모집 신청 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179673) | 경기대학교 창업지원단 | K-Startup 사업공고 |
| 2026-11-23 | [2027년도 초기창업·창업도약 패키지 사업 신규 주관기관 모집 수정공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179705) | 중소벤처기업부 장관 | K-Startup 사업공고 |
| 2026-11-23 | [제9회 원주권 스타트업 커뮤니티 데이 참가자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179727) | 상지대학교 벤처창업본부  | K-Startup 사업공고 |
| 2026-11-23 | [(부산센터) 2026년 제10회 제대군인 창업 워크숍 개최 안내](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179725) | 국가보훈부 | K-Startup 사업공고 |
| 2026-11-23 | [2026년 인공지능산업융합사업단「AI 창업동」 입주기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179710) | 인공지능산업융합사업단 | K-Startup 사업공고 |
| 2026-11-23 | [2027 Global Startup Center Workspace Call for Applications](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179744) | Korea Institute of Startup & Entrepreneurship Development | K-Startup 사업공고 |
| 2026-11-23 | [[창업] 실패하지 않는 내 매장 자리 찾기](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179751) | 마포청년창업취업지원센터 나루 | K-Startup 사업공고 |
| 2026-11-23 | [2027년 고양인쇄문화허브센터 입주기업 모집 공고 ( ~ 2026.11.23.(월)까지)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179729) | (재)경기대진테크노파크원장 | K-Startup 사업공고 |
| 2026-11-23 | [[강동구 청년해냄센터] 2027년 정부 지원 사업 대비 성공 창업 스쿨 참가자 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179766) | 강동구 청년해냄센터 | K-Startup 사업공고 |
| 2026-11-23 | [2026 전북콘텐츠코리아랩 AI 활용 콘텐츠(캐릭터) 아이디어 발굴 캠프](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179772) | (재)전북특별자치도 콘텐츠융합진흥원 | K-Startup 사업공고 |
| 2026-11-23 | [2026 서울게임콘텐츠센터 프라이빗 IR 참가기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179794) | 서울경제진흥원 | K-Startup 사업공고 |
| 2026-11-23 | [2026년 서울지식재산센터 IP창업클럽: 스타트업 IP:ON (~11/23까지, 선착순)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179784) | 서울경제진흥원 | K-Startup 사업공고 |
| 2026-11-23 | [2026년 기업공개(IPO) 상장지원 인사이트데이 참가자 모집(~11.23)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179778) | (재)부산기술창업투자원 | K-Startup 사업공고 |
| 2026-11-23 | [「올해의 K-스타트업 2026」 창업경진대회 왕중왕전 청중평가단 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179808) | 창업진흥원 | K-Startup 사업공고 |
| 2026-11-23 | [2026 펨테크 산업 육성사업 DEMO DAY](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179785) | 씨엔티테크 | K-Startup 사업공고 |

## 스타트업 뉴스

| 날짜 | 제목 | 출처 |
|---|---|---|
| 2026-11-20 | [디엘스킨, 미국 LA에 ‘K뷰티 하우스’ 개관…국내 화장품 브랜드의 현지 유통 진출 지원](https://www.venturesquare.net/1130477/) | 벤처스퀘어 |
| 2026-11-20 | [아테코, AI 메모리 통합 검사장비로 장영실상 수상…SOCAMM·LPCAMM 대응 기술 확보](https://www.venturesquare.net/1130479/) | 벤처스퀘어 |
| 2026-11-20 | [더인벤션랩·삼천리, 로봇 구동·무선충전 스타트업 2개사 투자협약…미래 모빌리티 협력 확대](https://www.venturesquare.net/1130487/) | 벤처스퀘어 |
| 2026-11-20 | [셀렉트스타, 대한출판문화협회와 AI 학습용 출판데이터 협력…저작권 보호·품질 검증 체계 구축](https://www.venturesquare.net/1130496/) | 벤처스퀘어 |
| 2026-11-20 | [부산창조경제혁신센터, 해양 스타트업 6개사와 전문기관 연결…기술 실증·사업화 협력 모색](https://www.venturesquare.net/1130494/) | 벤처스퀘어 |
| 2026-11-20 | [더네이쳐홀딩스, 국립수목원과 생태 교육 협력 확대…3년간 키즈 탐험대 1,700팀 참여](https://www.venturesquare.net/1130503/) | 벤처스퀘어 |
| 2026-11-20 | [엑스와이지, 로봇의 실패를 학습 데이터로 전환…’듀스’ 봉투 파지 성공률 90% 달성](https://www.venturesquare.net/1130515/) | 벤처스퀘어 |
| 2026-11-21 | [[최앤리의 스타트업 법률 가이드] Cross-border M&A 법률실사, 숨은 위험을 거래 조건에 반영하는 법](https://www.venturesquare.net/1129712/) | 벤처스퀘어 |
| 2026-11-21 | [네이버, 애플 학생 할인부터 로봇 AI 연구까지…쇼핑·여행·금융 서비스 확대](https://www.venturesquare.net/1130521/) | 벤처스퀘어 |
| 2026-11-21 | [[리포트+] 벤처기업 67.9% ‘업무 쏠림’ 경험…R&D 마감 앞에 근로시간 운영도 난제, 해법은?](https://www.venturesquare.net/1130551/) | 벤처스퀘어 |
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
