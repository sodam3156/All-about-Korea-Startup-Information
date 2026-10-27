# All-about-Korea-Startup-Information

세종 청년창업 기관 공지 · 정부 지원사업 공고 · 스타트업 뉴스를 **매일 14:00 KST에 자동 수집**하는 저장소.
GitHub Actions가 수집→중복제거→상세저장→아래 대시보드 갱신→텔레그램 브리핑까지 수행한다 (git-scraping — 서버·DB·API 비용 없음).

**완전 규칙 기반**: 소스마다 공식 API/RSS 또는 정규식 파서를 쓴다(LLM 미사용, 고정비 $0). 대신 사이트가 개편되면 파서가 조용히 0건을 낼 수 있어, 같은 소스가 **연속 2회 이상 0건**이면 `data/source_health.json`에 기록하고 다이제스트에 "⚠️ 소스 점검 필요"로 경고한다 — 이게 규칙 기반의 유일한 약점(개편에 안 깨지는 AI 추출 대비)을 메우는 피드백 루프다.

<!-- AUTO:START -->

_자동 갱신: 2026-10-27 (KST)_

## 마감 임박 지원사업

| 마감 | 공고 | 기관 | 출처 |
|---|---|---|---|
| 2026-10-27 | [[무료 AI 역량강화 교육]생성형 AI 기반 글로벌 무역·물류 데이터 분석 및 공급망 최적화 과정 (대전)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179171) | (주)글로벌창업연구소 | K-Startup 사업공고 |
| 2026-10-27 | [2026 정주영 창업경진대회: 무한(INFINITE)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179245) | 아산나눔재단 | K-Startup 사업공고 |
| 2026-10-27 | [[동대문구 창업지원센터] 10월 메이커스페이스(레이저커터, 3D프린팅) 교육 일정](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179420) | 동대문구 창업지원센터 | K-Startup 사업공고 |
| 2026-10-27 | [2027년도 관광기업지원센터(서울) 신규 입주기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179465) | 한국관광공사 | K-Startup 사업공고 |
| 2026-10-27 | [Applications Now Open: 2026 OASIS-6 Global Startup Challenge 「2026 외국인 창업대전(OASIS-6)」 참가자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179459) | 글로벌창업이민센터(한국능률협회컨설팅) | K-Startup 사업공고 |
| 2026-10-27 | [[무료|150석 한정] 딥테크 창업가 컨퍼런스 d.day : founders summit 참가자 모집 10/29](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179527) | 재단법인 은행권청년창업재단 | K-Startup 사업공고 |
| 2026-10-27 | [2026 관광기업 동반성장 기술역량 강화교육](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179574) | 한국관광공사 | K-Startup 사업공고 |
| 2026-10-27 | [2026 문화예술 창업교육의 모든 것.zip 2기 참여자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179506) | 성북구 청년공간 길이음 | K-Startup 사업공고 |
| 2026-10-27 | [[강원ICT융합연구원] 강원 미래산업 AX혁신과 지산학연 신사업 발굴 포럼](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179592) | 강원ICT융합연구원 | K-Startup 사업공고 |
| 2026-10-27 | [제 7차 충남 오픈이노베이션 포럼](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179585) | 한국기술교육대학교 산학협력단 | K-Startup 사업공고 |
| 2026-10-28 | [동국대학교 BMC창업보육센터(고양)신규 입주기업 모집공고(2026년 6차)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179360) | 동국대학교 BMC창업보육센터 | K-Startup 사업공고 |
| 2026-10-28 | [2026 ICT 혁신성과 교류회 : ICT INNOVATION BRIDGE](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179373) | 차세대융합기술연구원 | K-Startup 사업공고 |
| 2026-10-28 | [[한국도로공사] 2026년 상생형 창업, 벤처기업 지원사업](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179431) | 한국도로공사 사장 | K-Startup 사업공고 |
| 2026-10-28 | [2026년 서울창업센터 동작 입주기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179421) | 서울경제진흥원 (서울창업센터 동작) | K-Startup 사업공고 |
| 2026-10-28 | [창업 초보를 위한 창업 A-Z 교육](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179461) | 하우그로우 원격평생교육원 | K-Startup 사업공고 |
| 2026-10-28 | [TECH IP-UP: IP 창출캠프 참가팀 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179484) | 단국대학교 기술지주회 | K-Startup 사업공고 |
| 2026-10-28 | [[2026 K-Bio Insight Forum] 현장에서 만나는 바이오·제약 산업의 성장과 혁신](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179511) | 서울창조경제혁신센 | K-Startup 사업공고 |
| 2026-10-28 | [2026년 웰컴 투 팁스 7차 참가기업 모집 (제주권)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179535) | (주)로우파트너스 | K-Startup 사업공고 |
| 2026-10-28 | [2026 초격차 클리마 데이 (Clima Day) 행사 개최 안내](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179581) | 한국에너지기술평가원 | K-Startup 사업공고 |
| 2026-10-28 | [COMEUP 2026 사전 오프라인 행사 '스타트업 커리어 TALK'](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179569) | (사)코리아스타트업포럼 | K-Startup 사업공고 |

## 스타트업 뉴스

| 날짜 | 제목 | 출처 |
|---|---|---|
| 2026-10-26 | [스페이스뱅크, 로보월드 2026서 이기종 로봇 통합 플랫폼 공개…소프트웨어 배포까지 확장](https://www.venturesquare.net/1123179/) | 벤처스퀘어 |
| 2026-10-26 | [패커티브 운영사 프로보티브, 딥테크 팁스 선정…패키징 제조 업무 AI 자동화 개발](https://www.venturesquare.net/1123182/) | 벤처스퀘어 |
| 2026-10-26 | [[컬처슬로건 탐방기] 스토어링크, AI 시대에 필요한 건 속도](https://www.venturesquare.net/1123206/) | 벤처스퀘어 |
| 2026-10-26 | [중기부, 중소기업 수출 334억 달러 역대 최고…K-뷰티 성장에 브랜드 육성 정책 더한다](https://www.venturesquare.net/1123185/) | 벤처스퀘어 |
| 2026-10-26 | [[VS 기획] 대기업 온투업 진출에 ‘저수지 속 고래’ 우려…투자재원·이해상충 쟁점](https://www.venturesquare.net/1122839/) | 벤처스퀘어 |
| 2026-10-26 | [베스핀글로벌, 삼성증권 AI 데이터 플랫폼 구축 성과로 오라클 APAC 파트너 어워드 수상](https://www.venturesquare.net/1123222/) | 벤처스퀘어 |
| 2026-10-26 | [뉴지엄랩, 환자별 질환·복용 약물 반영하는 임상영양 AI 출시…GLP-1 치료 영양관리부터 적용](https://www.venturesquare.net/1123221/) | 벤처스퀘어 |
| 2026-10-26 | [릴리스AI, ‘리드레이’로 서비스명 변경…130만 사용자 기반 글로벌 AI 읽기 시장 공략](https://www.venturesquare.net/1123228/) | 벤처스퀘어 |
| 2026-10-26 | [종근당건강 아임비타, SNS 채널 개편 4개월 만에 참여 지표 3배 증가…식품 부문 대상 수상](https://www.venturesquare.net/1123244/) | 벤처스퀘어 |
| 2026-10-26 | [인포시즈, 8B AI 모델로 GPT-5보다 높은 수치 추론 정확도…연구 논문 EMNLP 2026 발표](https://www.venturesquare.net/1123245/) | 벤처스퀘어 |
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
