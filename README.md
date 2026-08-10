# All-about-Korea-Startup-Information

세종 청년창업 기관 공지 · 정부 지원사업 공고 · 스타트업 뉴스를 **매일 14:00 KST에 자동 수집**하는 저장소.
GitHub Actions가 수집→중복제거→상세저장→아래 대시보드 갱신→텔레그램 브리핑까지 수행한다 (git-scraping — 서버·DB·API 비용 없음).

**완전 규칙 기반**: 소스마다 공식 API/RSS 또는 정규식 파서를 쓴다(LLM 미사용, 고정비 $0). 대신 사이트가 개편되면 파서가 조용히 0건을 낼 수 있어, 같은 소스가 **연속 2회 이상 0건**이면 `data/source_health.json`에 기록하고 다이제스트에 "⚠️ 소스 점검 필요"로 경고한다 — 이게 규칙 기반의 유일한 약점(개편에 안 깨지는 AI 추출 대비)을 메우는 피드백 루프다.

<!-- AUTO:START -->

_자동 갱신: 2026-08-10 (KST)_

## 마감 임박 지원사업

| 마감 | 공고 | 기관 | 출처 |
|---|---|---|---|
| 2026-08-10 | [[2026-060호]2026년 세종 지역특화 프로젝트 레전드50+2.0 기업진단 및 컨설팅 참여기업 모집](https://sjtp.or.kr/bbs/board.php?bo_table=business01&wr_id=1987) | (재)세종테크노파크 | 세종테크노파크 사업공고 |
| 2026-08-10 | [[코레일유통/본사] 제9차 청년창업 제휴사업자 모집공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178732) | 코레일유통(주) | K-Startup 사업공고 |
| 2026-08-10 | [2026년 제 5회 경남 스타트업 IR「A.C.E(에이스) 경진대회」오픈리그 참여기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178713) | 재단법인 경남창조경제혁신센터 | K-Startup 사업공고 |
| 2026-08-10 | [2026 지역창업 페스티벌 연계 제106회 대전창업포럼(AI•로봇) 참가 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178789) | (재)대전창조경제혁신센터 | K-Startup 사업공고 |
| 2026-08-10 | [2026 예술분야 예비창업 프로그램 참여자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178773) | 문화체육관광부·(재)예술경영지원센터 | K-Startup 사업공고 |
| 2026-08-11 | [2026년 제4차 대전창업허브 입주기업 모집공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178727) | (재)대전창조경제혁신센터 | K-Startup 사업공고 |
| 2026-08-11 | [디캠프 8월 오피스아워 #벤처투자·#사업협력](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178714) | 재단법인 은행권청년창업재단 | K-Startup 사업공고 |
| 2026-08-11 | [호서대학교(단계별 창업솔루션) 지역문제 해결 청년창업 리빙랩](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178696) | 주식회사 킹고스프링 | K-Startup 사업공고 |
| 2026-08-11 | [청년취업사관학교 AI 창업가 양성 과정 참가자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178669) | 주식회사뉴키즈인베스트먼트 | K-Startup 사업공고 |
| 2026-08-11 | [2026년 2차 서울 AI 허브 신규 입주기업 모집 안내](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178661) | 서울 AI 허브 | K-Startup 사업공고 |
| 2026-08-11 | [「제5회 대구콘텐츠페어」 대구콘텐츠기업지원센터(DIP) 공동관 참가기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178801) | (재)대구디지털혁신진흥원 | K-Startup 사업공고 |
| 2026-08-11 | [[한국수자원공사] CES 2027 K-water관 참여기관 모집 공고(2차)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178778) | K-water 기후테크혁신처장 | K-Startup 사업공고 |
| 2026-08-12 | [2026 산업단지 오픈이노베이션프로그램 KICXUP 챌린지 & 로컬 스타트업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178746) | 한국산업단지공단 | K-Startup 사업공고 |
| 2026-08-12 | [청년 창업의 꿈, 『성동청년 창업이룸센터』 입주자 모집 공고【9차】](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178724) | 서울특별시 성동구청장 | K-Startup 사업공고 |
| 2026-08-12 | [2026년 여성CEO 비즈니스 아카데미 경상권역 시즌 1](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178671) | 한국여성경제인협회 | K-Startup 사업공고 |
| 2026-08-12 | [2026년도 방산 특화 창업중심대학 창업기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178662) | 중소벤처기업부 장관 | K-Startup 사업공고 |
| 2026-08-12 | [2026년 창업진흥원 대전 팁스타운 일본 파트너 초청 상담회 참가기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178839) | 창업진흥원장 | K-Startup 사업공고 |
| 2026-08-13 | [2026년 8월 동네창업학교 교육생 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178742) | 충남신용보증재단 | K-Startup 사업공고 |
| 2026-08-13 | [앤틀러코리아 ANTLER FORGE 소개 웨비나 | 팀 당 6억원 규모 투자](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178725) | 앤틀러코리아 | K-Startup 사업공고 |
| 2026-08-13 | [[대전관광공사] 2026 대전세종 관광기업 네트워킹 데이 3회차 참여기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178703) | 대전관광공사 | K-Startup 사업공고 |

## 스타트업 뉴스

| 날짜 | 제목 | 출처 |
|---|---|---|
| 2026-08-09 | [“다윗은 어떻게 골리앗을 이겼을까”…벤처스퀘어, 실전 협상 ‘OPEN UP’ 연다](https://www.venturesquare.net/1104714/) | 벤처스퀘어 |
| 2026-08-09 | [추억의 챗봇’ 심심이는 어떻게 AI 기업이 됐나…최정회 대표의 24년 대화 실험](https://www.venturesquare.net/1097114/) | 벤처스퀘어 |
| 2026-08-09 | [[기고] 기후위기는 국가 시스템 리스크다…미래는 이미 도착했다](https://www.venturesquare.net/1104819/) | 벤처스퀘어 |
| 2026-08-10 | [투자자 앞에 설 AI·빅데이터 초기기업 찾는다…씨엔티테크 ‘로켓십 IR’](https://www.venturesquare.net/1104835/) | 벤처스퀘어 |
| 2026-08-10 | [엘리스그룹이 AI 풀스택을 선언한 이유](https://www.venturesquare.net/1104846/) | 벤처스퀘어 |
| 2026-08-10 | [외국인 인증은 API로, CAD는 웹으로…씨엔티테크가 고른 두 SaaS](https://www.venturesquare.net/1104838/) | 벤처스퀘어 |
| 2026-08-10 | [AI로 가짜뉴스·디지털 소외 해법 찾았다…메가존클라우드 청소년 포럼](https://www.venturesquare.net/1104857/) | 벤처스퀘어 |
| 2026-08-10 | [산업용 엣지 AI, 양산의 관건은 전력…마우저 설계 리소스 한곳에](https://www.venturesquare.net/1104866/) | 벤처스퀘어 |
| 2026-08-10 | [공공기관은 어떤 AI를 골랐나…와이즈넛, 에이전트·검색·챗봇 1위](https://www.venturesquare.net/1104873/) | 벤처스퀘어 |
| 2026-08-10 | [소비자 불편을 제품으로, 반응은 콘텐츠로…더벤처스가 오와이디에 투자한 이유](https://www.venturesquare.net/1104884/) | 벤처스퀘어 |
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
