# All-about-Korea-Startup-Information

세종 청년창업 기관 공지 · 정부 지원사업 공고 · 스타트업 뉴스를 **매일 14:00 KST에 자동 수집**하는 저장소.
GitHub Actions가 수집→중복제거→상세저장→아래 대시보드 갱신→텔레그램 브리핑까지 수행한다 (git-scraping — 서버·DB·API 비용 없음).

**완전 규칙 기반**: 소스마다 공식 API/RSS 또는 정규식 파서를 쓴다(LLM 미사용, 고정비 $0). 대신 사이트가 개편되면 파서가 조용히 0건을 낼 수 있어, 같은 소스가 **연속 2회 이상 0건**이면 `data/source_health.json`에 기록하고 다이제스트에 "⚠️ 소스 점검 필요"로 경고한다 — 이게 규칙 기반의 유일한 약점(개편에 안 깨지는 AI 추출 대비)을 메우는 피드백 루프다.

<!-- AUTO:START -->

_자동 갱신: 2026-09-01 (KST)_

## 마감 임박 지원사업

| 마감 | 공고 | 기관 | 출처 |
|---|---|---|---|
| 2026-09-01 | [공공기술 기반 오픈이노베이션 밋업(with SK에코플랜트) 참여기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178880) | 씨엔티테크 | K-Startup 사업공고 |
| 2026-09-01 | [[창업] 창업가를 위한 온라인 판매 실전](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178935) | 마포청년창업취업지원센터 나루 | K-Startup 사업공고 |
| 2026-09-01 | [2026 대구·경북 스타트업 페스티벌 연계 제10회 대구 스타트업 오픈이노베이션 밋업데이(Meet-up) 참여 스타트업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178934) | 재단법인 대구창조경제혁신센터 대표이사,  경북대학교 창업지원단장 | K-Startup 사업공고 |
| 2026-09-01 | [2026 경기 고양 MICE 연계 창업리그 참가자 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178972) | (재)고양국제박람회재단 | K-Startup 사업공고 |
| 2026-09-01 | [[2026 시흥시 청년 창업가 육성 프로그램] 준비된 성장, 투자의 모든 것](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178960) | 주식회사뉴키즈인베스트먼트 | K-Startup 사업공고 |
| 2026-09-01 | [경기「스담스담」(오픈 네트워킹) 8회차](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179031) | 경기도경제과학진흥원 | K-Startup 사업공고 |
| 2026-09-01 | [2026년 양주시 「청년창업 토크콘서트」참여자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179022) | 양주시청년센터 | K-Startup 사업공고 |
| 2026-09-02 | [[LH한국토지주택공사] 판교 제2테크노밸리 기업성장센터(F2블록) 산업시설 입주기업 추가 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178785) | 한국토지주택공사 경기남부지역본부 | K-Startup 사업공고 |
| 2026-09-02 | [『BOUNCE 2026』 &apos;스타트업 오픈이노베이션 페스타&apos; 참여 스타트업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178883) | 부산창조경제혁신센터 | K-Startup 사업공고 |
| 2026-09-02 | [디캠프 9월 오피스아워 #벤처투자·#사업협력 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178938) | 재단법인 은행권청년창업재단 | K-Startup 사업공고 |
| 2026-09-02 | [구로구 청년창업지원센터 일반 창업교육(하반기: 2회차): 스타트업 재무 (feat. 합법적인 절세방안)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178973) | 구로구 청년창업지원센터 | K-Startup 사업공고 |
| 2026-09-02 | [2026년도 &apos;빅웨이브(BiiG WAVE)&apos; IR 사업 2회차 바이오 특화 IR 참여기업 모집공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178966) | 인천창조경제혁신센터 | K-Startup 사업공고 |
| 2026-09-02 | [[차세대융합기술연구원] 2026 제조 스타트업 멘토링 Meet-up Day](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178962) | 차세대융합기술연구원 | K-Startup 사업공고 |
| 2026-09-02 | [2026 관악S밸리 성장 지원 세미나 3회](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178961) | (재)관악중소벤처진흥원 | K-Startup 사업공고 |
| 2026-09-02 | [2026 제조 스타트업 멘토링 데이](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178991) | 볼트앤너트 | K-Startup 사업공고 |
| 2026-09-02 | [「2026년 제3회 부기테크 투자쇼」상담회 참가기업 모집공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179025) | 부산기술창업투자원 | K-Startup 사업공고 |
| 2026-09-02 | [2026 4대 과학기술원 창업리그 통합 결선, GRAVITY (9/3 목)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179041) | (주)스파크랩 | K-Startup 사업공고 |
| 2026-09-03 | [2026년 창업진흥원 정책 아이디어 공모전](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178709) | 창업진흥원 | K-Startup 사업공고 |
| 2026-09-03 | [[한국투자액셀러레이터] 바른동행 3차 모집｜선발 시 최대 5억원 투자](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178844) | 한국투자액셀러레이터 | K-Startup 사업공고 |
| 2026-09-03 | [2026년 지역 혁신 Start-up Demo Day](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178900) | 차세대융합기술연구원 | K-Startup 사업공고 |

## 스타트업 뉴스

| 날짜 | 제목 | 출처 |
|---|---|---|
| 2026-08-31 | [12번의 샘플 폐기 끝에 찾은 답…펫라이즈 김도형 대표, 배변봉투로 세계 시장 두드린다](https://www.venturesquare.net/1099122/) | 벤처스퀘어 |
| 2026-08-31 | [스테이블코인부터 RWA까지…글로벌 금융·웹3 리더 서울에 모인다](https://www.venturesquare.net/1109874/) | 벤처스퀘어 |
| 2026-08-31 | [비수도권 스타트업 20개사, 베트남 시장 두드렸다…PoC 등 MOU 66건](https://www.venturesquare.net/1109886/) | 벤처스퀘어 |
| 2026-08-31 | [이공계 넘어 ‘모든 대학생의 AI’로…튜링, 70억원 시리즈B 유치](https://www.venturesquare.net/1109893/) | 벤처스퀘어 |
| 2026-08-31 | [제조현장에 AI 스타트업 기술 연결…대기업 8개사와 ‘실증 가능성’ 찾는다](https://www.venturesquare.net/1109899/) | 벤처스퀘어 |
| 2026-08-31 | [51만건 세무 데이터, 대국민 AI로…삼쩜삼 ‘모두의 AI’ 합류](https://www.venturesquare.net/1109902/) | 벤처스퀘어 |
| 2026-09-01 | [페라리·람보르기니, 최대 7일 타보고 산다…차봇 ‘슈퍼 클래스’ 론칭](https://www.venturesquare.net/1109917/) | 벤처스퀘어 |
| 2026-09-01 | [‘미투데이·밴드’ 만든 박수만, AI 소셜로 다시 도전…벗뷰리풀 프리A 유치](https://www.venturesquare.net/1109923/) | 벤처스퀘어 |
| 2026-09-01 | [원하는 굴절률·유전율·열전도 ‘설계’한다…킴테크닉스, 씨엔티테크 투자 유치](https://www.venturesquare.net/1109930/) | 벤처스퀘어 |
| 2026-09-01 | [공공기관 인권경영 66.3% ‘제도 도입’에 그쳐…“실제 작동 여부 따져야”](https://www.venturesquare.net/1109937/) | 벤처스퀘어 |
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
