# All-about-Korea-Startup-Information

세종 청년창업 기관 공지 · 정부 지원사업 공고 · 스타트업 뉴스를 **매일 14:00 KST에 자동 수집**하는 저장소.
GitHub Actions가 수집→중복제거→상세저장→아래 대시보드 갱신→텔레그램 브리핑까지 수행한다 (git-scraping — 서버·DB·API 비용 없음).

**완전 규칙 기반**: 소스마다 공식 API/RSS 또는 정규식 파서를 쓴다(LLM 미사용, 고정비 $0). 대신 사이트가 개편되면 파서가 조용히 0건을 낼 수 있어, 같은 소스가 **연속 2회 이상 0건**이면 `data/source_health.json`에 기록하고 다이제스트에 "⚠️ 소스 점검 필요"로 경고한다 — 이게 규칙 기반의 유일한 약점(개편에 안 깨지는 AI 추출 대비)을 메우는 피드백 루프다.

<!-- AUTO:START -->

_자동 갱신: 2026-08-26 (KST)_

## 마감 임박 지원사업

| 마감 | 공고 | 기관 | 출처 |
|---|---|---|---|
| 2026-08-26 | [2026년 서울시 소셜벤처 임팩트 측정 사업설명회(2차) 참가신청 모집(~8.26.)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178702) | 서울소셜벤처허브 | K-Startup 사업공고 |
| 2026-08-26 | [2026 신용보증기금 「혁신아이콘」제16기 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178687) | 신용보증기금 | K-Startup 사업공고 |
| 2026-08-26 | [「민관협력 오픈이노베이션 지원」2026년 '성과기업 후속 지원' 창업기업 모집공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178821) | 중소벤처기업부 | K-Startup 사업공고 |
| 2026-08-26 | [[동대문구 창업지원센터] 8월 메이커스페이스(레이저커터, 3D프린팅) 교육 일정](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178774) | 동대문구 창업지원센터 | K-Startup 사업공고 |
| 2026-08-26 | [[서초창업스테이션] 8월 전문 분야 컨설팅 - 스타트업 정책자금 및 자금조달 전략 & 투자유치를 위한 IR·사업계획 고도화](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178825) | 서초창업스테이션 | K-Startup 사업공고 |
| 2026-08-26 | [2026년 웰컴 투 팁스 2차 참가기업 모집 (대경권)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178893) | (주)로우파트너스 | K-Startup 사업공고 |
| 2026-08-26 | [Startup OI Tokyo #Physical AI](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178899) | 재단법인 은행권청년창업재단 | K-Startup 사업공고 |
| 2026-08-26 | [도봉구 중소기업창업보육센터 신규 입주기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178898) | 도봉구청 | K-Startup 사업공고 |
| 2026-08-26 | [2026년 경기 스타트업 아카데미 「창업기초 및 투자유치 과정(하반기)」 교육생 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178886) | 경기도경제과학진흥원 | K-Startup 사업공고 |
| 2026-08-26 | [2026 창업경진대회(IMPACT ON 강북 : 아이디어와 투자로 만드는 강북의 창업 무대) 참가자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178884) | 강북청년창업마루 | K-Startup 사업공고 |
| 2026-08-26 | [[창업] 경험을 디자인하는 기획자 양성 과정](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178928) | 마포청년창업취업지원센터 나루 | K-Startup 사업공고 |
| 2026-08-26 | [2026 U-Global Connect x Fincnatieri 참여기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178923) | (재)울산창조경제혁신센터 | K-Startup 사업공고 |
| 2026-08-26 | [2026 대한민국 발명특허대전 출품 신청(~8.26)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178921) | 한국발명진흥회 | K-Startup 사업공고 |
| 2026-08-26 | [모두의 창업 설명회와 함께하는 &apos;200% 경쟁력 있는 사업계획서 작성법&apos; - DDM 제8차 벤처스타트업 아카데미](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178905) | DDM청년창업센터 유니콘 | K-Startup 사업공고 |
| 2026-08-26 | [2026년 경기 스타트업 아카데미 이오스튜디오(EO) 김태용 대표의 글로벌 마케팅 특강](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178903) | 경기도경제과학진흥원 | K-Startup 사업공고 |
| 2026-08-26 | [「제24차 세계한상대회 스타트업 경연대회-시애틀 진출 연계」 참여기업 모집 공고(AI 분야)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178954) | 재외동포청 | K-Startup 사업공고 |
| 2026-08-26 | [2026년 서울시 기후테크 온라인 기획전 실무교육](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178933) | 서울기후테크산업지원센터장 | K-Startup 사업공고 |
| 2026-08-26 | [서울디자인런 2026 - 사고 싶은 작은 것들: 창작의 가치를 상품으로 바꾸는 안목](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178978) | (주)오픈 | K-Startup 사업공고 |
| 2026-08-26 | [2026년 서울창업허브 창동 「창동 허브 네트워킹 데이」](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178964) | 서울창업허브 창동 | K-Startup 사업공고 |
| 2026-08-27 | [2026년 「차세대 반도체 패키징 산업전 시스템반도체 OSAT 전문교육(세미나)」 개최](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178736) | 한국나노기술원 | K-Startup 사업공고 |

## 스타트업 뉴스

| 날짜 | 제목 | 출처 |
|---|---|---|
| 2026-08-25 | [“주사 부담은 줄이고, 약효는 오래도록”…25년 연구 경험 담은 조재평 레제피온 대표의 약물전달 플랫폼](https://www.venturesquare.net/1108329/) | 벤처스퀘어 |
| 2026-08-25 | [아이돌 무대가 K브랜드의 일본 테스트베드로…콜로세움, 도쿄서 ICU콘](https://www.venturesquare.net/1108339/) | 벤처스퀘어 |
| 2026-08-25 | [의사가 설계하고 AI로 개인화하는 안티에이징 통합 솔루션…씨엔티테크, ‘필리데이’ 투자](https://www.venturesquare.net/1108346/) | 벤처스퀘어 |
| 2026-08-25 | [쌓인 제약 데이터를 ‘쓰는 상품’으로…비알피커넥트, 태블로 혁신 사례 공개](https://www.venturesquare.net/1108349/) | 벤처스퀘어 |
| 2026-08-25 | [드론의 ‘눈’과 통신을 한 플랫폼에…카네비모빌리티, 민군 모빌리티 기술 공개](https://www.venturesquare.net/1108357/) | 벤처스퀘어 |
| 2026-08-25 | [고객이 고객을 부른다…IPO 앞둔 에버스핀, 금융사 140곳 레퍼런스로 해외 확장](https://www.venturesquare.net/1108369/) | 벤처스퀘어 |
| 2026-08-25 | [GPU 활용률 2.8배 높인 기술…래블업, 코스닥 공모 돌입](https://www.venturesquare.net/1108377/) | 벤처스퀘어 |
| 2026-08-25 | [운동 목표에 맞춰 0.1㎖씩 제조…씨엔티테크, AI 음료 플랫폼 브링크 투자](https://www.venturesquare.net/1108385/) | 벤처스퀘어 |
| 2026-08-25 | [예비창업자 1만 명 찾는다…인천창경, ‘모두의 창업’ 설명회 성료](https://www.venturesquare.net/1108388/) | 벤처스퀘어 |
| 2026-08-25 | [지드래곤이 마련한 ‘영웅의 자리’…국가유공자 후손·교정공무원 BIGBANG 공연 초청](https://www.venturesquare.net/1108395/) | 벤처스퀘어 |
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
