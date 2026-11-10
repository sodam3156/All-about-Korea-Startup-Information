# All-about-Korea-Startup-Information

세종 청년창업 기관 공지 · 정부 지원사업 공고 · 스타트업 뉴스를 **매일 14:00 KST에 자동 수집**하는 저장소.
GitHub Actions가 수집→중복제거→상세저장→아래 대시보드 갱신→텔레그램 브리핑까지 수행한다 (git-scraping — 서버·DB·API 비용 없음).

**완전 규칙 기반**: 소스마다 공식 API/RSS 또는 정규식 파서를 쓴다(LLM 미사용, 고정비 $0). 대신 사이트가 개편되면 파서가 조용히 0건을 낼 수 있어, 같은 소스가 **연속 2회 이상 0건**이면 `data/source_health.json`에 기록하고 다이제스트에 "⚠️ 소스 점검 필요"로 경고한다 — 이게 규칙 기반의 유일한 약점(개편에 안 깨지는 AI 추출 대비)을 메우는 피드백 루프다.

<!-- AUTO:START -->

_자동 갱신: 2026-11-10 (KST)_

## 마감 임박 지원사업

| 마감 | 공고 | 기관 | 출처 |
|---|---|---|---|
| 2026-11-10 | [[무료 AI 역량강화 교육]생성형 AI 기반 무역 컴플라이언스 및 관세·ESG 리스크 최적화(부산)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179251) | (주)글로벌창업연구소 | K-Startup 사업공고 |
| 2026-11-10 | [2026년도 양자산업 QX 네트워킹 포럼 「Quantum Horizon」 참가 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179455) | 블루포인트파트너스 | K-Startup 사업공고 |
| 2026-11-10 | [(경남센터) 2026년 제9회 제대군인 창업 워크숍 개최 안내](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179520) | 국가보훈부 | K-Startup 사업공고 |
| 2026-11-10 | [[GBSA] 2026 판교스타트업 투자교류회 제 4차 투자교류회](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179554) | ㈜내비온파트너스 | K-Startup 사업공고 |
| 2026-11-10 | [2026 TEL VENTURE CAPITAL X 충남창조경제혁신센터 Nexus Connect 투자 밋업 데이](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179543) | (재)충남창조경제혁신센터 대표이사 | K-Startup 사업공고 |
| 2026-11-10 | [G밸리의료기기개발지원센터 글로벌역량강화 교육프로그램 참가자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179545) | 한국과학기술연구원 | K-Startup 사업공고 |
| 2026-11-10 | [상지대학교 창업보육센터 입주기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179612) | 상지대학교 산학협력단 창업보육센터 | K-Startup 사업공고 |
| 2026-11-10 | [[강동구 청년해냄센터] 전문분야 창업멘토링 11월 참가자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179629) | 강동구 청년해냄센터 | K-Startup 사업공고 |
| 2026-11-10 | [2026 서울게임콘텐츠센터 게임랩 신규 입주기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179636) | (재)서울경제진흥원 | K-Startup 사업공고 |
| 2026-11-11 | [구로구 청년창업지원센터 일반 창업교육(하반기: 6회차): 발표평가 자료 작성 및 발표 요령](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179590) | 구로구 청년창업지원센터 | K-Startup 사업공고 |
| 2026-11-11 | [[롯데벤처스] LOTTE OPEN INNOVATION DAY 참관객 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179580) | 롯데벤처스 | K-Startup 사업공고 |
| 2026-11-11 | [2026 의왕시 청년e-Room 창업아이디어 공모전 참가자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179565) | 의왕시청 | K-Startup 사업공고 |
| 2026-11-11 | [「2026년 강원연구개발특구육성(R&D)사업」 강원 특구 배치 프로그램 1기 참여기업 모집공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179596) | 재단법인 강원창조경제혁신센터 | K-Startup 사업공고 |
| 2026-11-11 | [예비 초기 스타트업을 위한 창업 교육 프로그램 러닝메이트 9기 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179621) | 재단법인 오렌지플래닛 창업재단 | K-Startup 사업공고 |
| 2026-11-11 | [[ZUZU X 마크앤컴퍼니 집중검토] 딥테크·소부장 Pre-Seed ~ Pre-A 투자 검토 모집 (찾아가는 GF)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179657) | (주) 코드박스 Kodebox | K-Startup 사업공고 |
| 2026-11-11 | [2026년 위치정보 보호조치 교육 (7차)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179679) | (주) 아이전스 | K-Startup 사업공고 |
| 2026-11-11 | [2026년 대전 테스트베드 연계사업 공모](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179677) | 한국수자원공사 | K-Startup 사업공고 |
| 2026-11-12 | [[숭실대학교 캠퍼스타운] 생성형 AI 활용 기초 및 업무 자동화 과정 참여자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179458) | 숭실대학교 캠퍼스타운사업단 | K-Startup 사업공고 |
| 2026-11-12 | [2026년 남구다운 청년 창업 지원사업 통합공고(수정)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179486) | (사)대구경북고용복지연구원 | K-Startup 사업공고 |
| 2026-11-12 | [[해수부] 2026년 해양수산 통합데모데이 참가자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179533) | 부산지역대학연합기술지주(주) | K-Startup 사업공고 |

## 스타트업 뉴스

| 날짜 | 제목 | 출처 |
|---|---|---|
| 2026-11-10 | [파네시아, 미국 법인 설립·MS 출신 전문가 영입…AI 데이터센터 시장 공략 강화](https://www.venturesquare.net/1127157/) | 벤처스퀘어 |
| 2026-11-10 | [딥엑스, 5W 생성형 AI 반도체 ‘DX-M2’ CES 2027 혁신상…삼성 2나노 공정으로 개발](https://www.venturesquare.net/1127174/) | 벤처스퀘어 |
| 2026-11-10 | [브리즘, 하버드 경영대학원서 두 번째 사례 수업…“맞춤 안경, 왜 더 비싸게 팔지 않나”](https://www.venturesquare.net/1127176/) | 벤처스퀘어 |
| 2026-11-10 | [경기창조경제혁신센터, 기술 스타트업 10개사와 대·중견기업 연결…사업화·투자 밋업 개최](https://www.venturesquare.net/1127185/) | 벤처스퀘어 |
| 2026-11-10 | [뉴튠, WIPO서 AI 창작물 분류 체계 제안…음악 저작권·라이선싱 기준 논의](https://www.venturesquare.net/1127184/) | 벤처스퀘어 |
| 2026-11-10 | [부산연합기술지주, 경성대·동명대·국립부경대 창업팀 15개 육성…대학 연합 실전교육 운영](https://www.venturesquare.net/1127193/) | 벤처스퀘어 |
| 2026-11-10 | [컬리, 3분기 매출 7,779억원 역대 최대…영업이익 100억원·7분기 연속 흑자](https://www.venturesquare.net/1127204/) | 벤처스퀘어 |
| 2026-11-10 | [엑시스, 30년 전 카메라를 인터넷에 연결했다…이제는 ‘보안 너머’를 본다](https://www.venturesquare.net/1127211/) | 벤처스퀘어 |
| 2026-11-10 | [한국무역협회, 서비스 수출실적 증명 통합 추진…6개 기관 AI 기반 공동 심사체계 구축](https://www.venturesquare.net/1127233/) | 벤처스퀘어 |
| 2026-11-10 | [딥인사이트, NVIDIA Inception 선정…로봇 학습용 3D 데이터 기술 고도화](https://www.venturesquare.net/1127232/) | 벤처스퀘어 |
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
