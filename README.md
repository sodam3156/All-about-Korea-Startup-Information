# All-about-Korea-Startup-Information

세종 청년창업 기관 공지 · 정부 지원사업 공고 · 스타트업 뉴스를 **매일 14:00 KST에 자동 수집**하는 저장소.
GitHub Actions가 수집→중복제거→상세저장→아래 대시보드 갱신→텔레그램 브리핑까지 수행한다 (git-scraping — 서버·DB·API 비용 없음).

**완전 규칙 기반**: 소스마다 공식 API/RSS 또는 정규식 파서를 쓴다(LLM 미사용, 고정비 $0). 대신 사이트가 개편되면 파서가 조용히 0건을 낼 수 있어, 같은 소스가 **연속 2회 이상 0건**이면 `data/source_health.json`에 기록하고 다이제스트에 "⚠️ 소스 점검 필요"로 경고한다 — 이게 규칙 기반의 유일한 약점(개편에 안 깨지는 AI 추출 대비)을 메우는 피드백 루프다.

<!-- AUTO:START -->

_자동 갱신: 2026-09-09 (KST)_

## 마감 임박 지원사업

| 마감 | 공고 | 기관 | 출처 |
|---|---|---|---|
| 2026-09-09 | [「민관협력 오픈이노베이션 지원」2026년 '규제자유특구 지원' 창업기업 모집공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178975) | 중소벤처기업부장관 | K-Startup 사업공고 |
| 2026-09-09 | [2026년 WoW!메이커스 IR클리닉 참여기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178992) | 수원대학교 WoW!메이커스 | K-Startup 사업공고 |
| 2026-09-09 | [[경과원 X 노션] &apos;노션으로 만드는 스타트업 AI OS&apos; 특강 참여자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179030) | 경기도경제과학진흥원 | K-Startup 사업공고 |
| 2026-09-09 | [중동상황대응 [수출위기극복 및 대체시장 개척] 심화컨설팅](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179017) | 서울경제진흥원 | K-Startup 사업공고 |
| 2026-09-09 | [2026년도 ｢서울 관광스타트업 육성 지원(상생협력) 사업｣ 공모](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179008) | 서울특별시장 | K-Startup 사업공고 |
| 2026-09-09 | [2026년 『고양시 투자 레벨업 프로그램 NEXT ROUND』 참가기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179003) | 고양산업진흥원 | K-Startup 사업공고 |
| 2026-09-09 | [2026년 충북 바이오 오픈이노베이션 사업 참여 스타트업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178998) | 오송첨단의료산업진흥재단 | K-Startup 사업공고 |
| 2026-09-09 | [[서울여자대학교 창업보육센터] 신규 입주기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179056) | 서울여자대학교 창업보육센터 | K-Startup 사업공고 |
| 2026-09-09 | [2026 서울 오픈이노베이션 인사이트 데이](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179028) | (주)마크앤컴퍼니 | K-Startup 사업공고 |
| 2026-09-09 | [관악 마케팅 지원 참여자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179076) | 관악구청 | K-Startup 사업공고 |
| 2026-09-09 | [스타트업 자금조달 WEEK (투자) 프로그램 참가기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179074) | 서강대학교 판교캠퍼스사업단 | K-Startup 사업공고 |
| 2026-09-09 | [2026 창업경진대회(IMPACT ON 강북 : 아이디어와 투자로 만드는 강북의 창업 무대) 관람객 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179165) | 강북청년창업마루 | K-Startup 사업공고 |
| 2026-09-09 | [서울디자인런 2026 - 창업은 언제 혼자를 벗어나야 할까?](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179137) | (주)오픈놀 | K-Startup 사업공고 |
| 2026-09-10 | [2026년 CAU Tech-Connecting Day [중앙대학교 기술세미나 및 기술상담회]](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178924) | 중앙대학교 창업보육센터(다빈치) | K-Startup 사업공고 |
| 2026-09-10 | [2026 인도네시아 자카르타 할랄 식품전시회 지역 수출컨소시엄](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178984) | 성남산업진흥원 | K-Startup 사업공고 |
| 2026-09-10 | [2026년 민간 산림복지 창업 아카데미[1차] 참가자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179045) | 한국산림복지진흥원 | K-Startup 사업공고 |
| 2026-09-10 | [2026년 대구 콘텐츠 스케일업 액셀러레이팅 프로그램 지원사업 참여기업 추가 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179039) | (재)대구디지털혁신진흥원 | K-Startup 사업공고 |
| 2026-09-10 | [26년 AI·스마트전자제품 금형지원 기업모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179061) | 한국전자정보통신산업진흥회 | K-Startup 사업공고 |
| 2026-09-10 | [홍콩 코스모프로프 미용 전시회(Cosmoprof Asia 2026) 서울 공동관 참여기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179071) | 서울경제진흥원 | K-Startup 사업공고 |
| 2026-09-10 | [2026년 서울창업센터 관악 관악S밸리 창업 페스티벌 &apos;창업 아이디어 경진대회&apos; 참가자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179130) | 서울창업센터 관 | K-Startup 사업공고 |

## 스타트업 뉴스

| 날짜 | 제목 | 출처 |
|---|---|---|
| 2026-09-08 | [9,000원 항공권·2만9000원 호텔 타임딜…트립닷컴, ‘9.9 메가세일’](https://www.venturesquare.net/1111873/) | 벤처스퀘어 |
| 2026-09-08 | [3D프린팅 인프라와 창업기업 잇는다…인천창경·재능대, 적층제조 생태계 협력](https://www.venturesquare.net/1111884/) | 벤처스퀘어 |
| 2026-09-08 | [양자점 센서에 초정밀 광학 더한다…SDT·그린광학, 국산 SWIR 카메라 공동개발](https://www.venturesquare.net/1111887/) | 벤처스퀘어 |
| 2026-09-08 | [CCTV가 위험 판단하고 보고서까지…모멘트큐브, 엔비디아 ‘엔업’ 선정](https://www.venturesquare.net/1111894/) | 벤처스퀘어 |
| 2026-09-08 | [복지·세정·예산 잇는 공공 AI…메타빌드, AX 공급 영역 확장](https://www.venturesquare.net/1111906/) | 벤처스퀘어 |
| 2026-09-08 | [‘옮긴 뒤’의 운영·비용까지…스마일샤크, AWS 마이그레이션 전략 공유](https://www.venturesquare.net/1111914/) | 벤처스퀘어 |
| 2026-09-08 | [시험지 없이 영어 성장 추적…리딩앤, 학습과정 분석 ‘LISA’ 첫 적용](https://www.venturesquare.net/1111917/) | 벤처스퀘어 |
| 2026-09-08 | [삼성전자가 택한 유럽 AI 주권…미스트랄, 30억 유로 시리즈 D 유치](https://www.venturesquare.net/1111928/) | 벤처스퀘어 |
| 2026-09-08 | [코스모로보틱스, 보행재활 로봇 기술로 국무총리 표창](https://www.venturesquare.net/1111931/) | 벤처스퀘어 |
| 2026-09-08 | [아이디어를 검증 가능한 사업으로…경남혁신센터, ‘GIFT BM PLUS’ 운영](https://www.venturesquare.net/1111942/) | 벤처스퀘어 |
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
