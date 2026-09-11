# All-about-Korea-Startup-Information

세종 청년창업 기관 공지 · 정부 지원사업 공고 · 스타트업 뉴스를 **매일 14:00 KST에 자동 수집**하는 저장소.
GitHub Actions가 수집→중복제거→상세저장→아래 대시보드 갱신→텔레그램 브리핑까지 수행한다 (git-scraping — 서버·DB·API 비용 없음).

**완전 규칙 기반**: 소스마다 공식 API/RSS 또는 정규식 파서를 쓴다(LLM 미사용, 고정비 $0). 대신 사이트가 개편되면 파서가 조용히 0건을 낼 수 있어, 같은 소스가 **연속 2회 이상 0건**이면 `data/source_health.json`에 기록하고 다이제스트에 "⚠️ 소스 점검 필요"로 경고한다 — 이게 규칙 기반의 유일한 약점(개편에 안 깨지는 AI 추출 대비)을 메우는 피드백 루프다.

<!-- AUTO:START -->

_자동 갱신: 2026-09-11 (KST)_

## 마감 임박 지원사업

| 마감 | 공고 | 기관 | 출처 |
|---|---|---|---|
| 2026-09-11 | [2026년 경기도일자리재단 1인 창조기업 지원센터 하반기 신규 기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178792) | 경기도일자리재단 | K-Startup 사업공고 |
| 2026-09-11 | [2026 북부 경기문화창조허브 스타트업 입주사 23기 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178872) | 경기콘텐츠진흥원 | K-Startup 사업공고 |
| 2026-09-11 | [2026년 서울창업허브M+ 글로벌 오픈 이노베이션](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178915) | 서울경제진흥원 | K-Startup 사업공고 |
| 2026-09-11 | [2026 예비오션스타 기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178977) | 해양수산부장관 | K-Startup 사업공고 |
| 2026-09-11 | [달서구 중장년 기술창업센터](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178996) | 달서구 중장년 기술창업센터 | K-Startup 사업공고 |
| 2026-09-11 | [2026년 초기창업패키지 네이버클라우드 오픈이노베이션 밋업 참가기업 모집공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178994) | 씨엔티테크(주) | K-Startup 사업공고 |
| 2026-09-11 | [2026년 수원대학교 WoW!메이커스 특허 출원 지원 참여기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179032) | 수원대학교 WoW!메이커스 | K-Startup 사업공고 |
| 2026-09-11 | [[부산대학교병원]「2026년 의료·헬스케어 스타트업 인큐베이터 사업」오픈이노베이션 지원사업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179027) | 부산대학교병원 | K-Startup 사업공고 |
| 2026-09-11 | [2026 오픈소스 로봇 손(Amazing Hand)으로 배우는 Physical AI 실습 교육](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179010) | 차세대융합기술연구원 | K-Startup 사업공고 |
| 2026-09-11 | [&apos;26-2차 KHNP AI(아이)누리 입주기업 공모](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179005) | 한국수력원자력(주) | K-Startup 사업공고 |
| 2026-09-11 | [「상생형 창업벤처기업 지원사업」한전KDN 에너지 ICT 창업벤처기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179066) | 한국전기산업진흥회 에너지밸리기업개발원 | K-Startup 사업공고 |
| 2026-09-11 | [2026년 제3차 관악S밸리 창업 공간 신규 입주기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179113) | 재단법인 관악중소벤처진흥원 | K-Startup 사업공고 |
| 2026-09-11 | [2026년 한국공항공사 상생형 창업·벤처 기업지원 프로그램 참여기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179110) | 한국공항공사 | K-Startup 사업공고 |
| 2026-09-11 | [2026년 세종특별자치시 나성동 AI융합창업보육센터 3차 입주기업(인큐베이팅룸) 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179102) | (재)세종창조경제혁신센터 | K-Startup 사업공고 |
| 2026-09-11 | [고려대기술지주(주) 판교인큐베이팅센터 입주기업 모집공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179100) | 고려대학교기술지주 주식회사  | K-Startup 사업공고 |
| 2026-09-11 | [2026년 한양대학교 ERICA 산학협력단지 입주기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179087) | 한양대학교  ERICA 캠퍼스혁신파크사업단 | K-Startup 사업공고 |
| 2026-09-11 | [인천스타트업파크 부스트 스타트업 TechCrunch Disrupt 2026 참가기업 모집공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179075) | (재)인천테크노파크 | K-Startup 사업공고 |
| 2026-09-11 | [「2026년 스타트업 법률지원사업 대구광역시 법률상담회」 참여기업 모집 안내](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179197) | 창업진흥원 원스톱지원실 | K-Startup 사업공고 |
| 2026-09-12 | [<소셜벤처 프렙스쿨 14기> 사회연대경제기업 창업 육성 프로그램 참여기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179091) | 유원대학교 충남 앵커사업단 | K-Startup 사업공고 |
| 2026-09-12 | [모두의창업 지원서 작성법 특강 "모두의창업 지원서 작성포인트! 사례로 알려드립니다"](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179162) | 단국대학교 창업교육센터 | K-Startup 사업공고 |

## 스타트업 뉴스

| 날짜 | 제목 | 출처 |
|---|---|---|
| 2026-09-10 | [블록체인 서버에서 금융 인프라로…람다256, 노드 운영 신입 뽑는다](https://www.venturesquare.net/1112381/) | 벤처스퀘어 |
| 2026-09-10 | [사진 찍는 순간 표정 짓는 ‘페이커’…클레온, 게임스컴서 디지털 휴먼 공개](https://www.venturesquare.net/1112384/) | 벤처스퀘어 |
| 2026-09-10 | [지난 상담에서 거절한 고객까지 AI로 재현…크디랩, 맞춤 롤플레이 공개](https://www.venturesquare.net/1112395/) | 벤처스퀘어 |
| 2026-09-10 | [자연어로 화면 설계부터 코드까지…토마토시스템, AI 개발 에이전트 시연](https://www.venturesquare.net/1112410/) | 벤처스퀘어 |
| 2026-09-10 | [화장품 용기 품질·양산성 잡는다…우진플라임, K-뷰티 설비 수요 공략](https://www.venturesquare.net/1112413/) | 벤처스퀘어 |
| 2026-09-10 | [여러 폐기물 업체 관리를 한 플랫폼으로…리코, 물류센터용 ‘업박스’ 선보인다](https://www.venturesquare.net/1112426/) | 벤처스퀘어 |
| 2026-09-10 | [정책자금부터 후속 투자까지…유니콘랩 대구, 보육기업 7개사 성장 진단](https://www.venturesquare.net/1112429/) | 벤처스퀘어 |
| 2026-09-10 | [문서 자동화 넘어 공장 판단까지…포티투마루, 디스플레이 AX 해법 제시](https://www.venturesquare.net/1112436/) | 벤처스퀘어 |
| 2026-09-10 | [초기 설치비 없이 히트펌프 쓴다…모닥불에너지, 10년 구독 금융 마련](https://www.venturesquare.net/1112444/) | 벤처스퀘어 |
| 2026-09-10 | [팬덤의 레시피를 PB 상품으로…풀릭스, 크리에이터 제조 실전 공유](https://www.venturesquare.net/1112455/) | 벤처스퀘어 |
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
