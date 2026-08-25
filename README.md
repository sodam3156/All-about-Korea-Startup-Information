# All-about-Korea-Startup-Information

세종 청년창업 기관 공지 · 정부 지원사업 공고 · 스타트업 뉴스를 **매일 14:00 KST에 자동 수집**하는 저장소.
GitHub Actions가 수집→중복제거→상세저장→아래 대시보드 갱신→텔레그램 브리핑까지 수행한다 (git-scraping — 서버·DB·API 비용 없음).

**완전 규칙 기반**: 소스마다 공식 API/RSS 또는 정규식 파서를 쓴다(LLM 미사용, 고정비 $0). 대신 사이트가 개편되면 파서가 조용히 0건을 낼 수 있어, 같은 소스가 **연속 2회 이상 0건**이면 `data/source_health.json`에 기록하고 다이제스트에 "⚠️ 소스 점검 필요"로 경고한다 — 이게 규칙 기반의 유일한 약점(개편에 안 깨지는 AI 추출 대비)을 메우는 피드백 루프다.

<!-- AUTO:START -->

_자동 갱신: 2026-08-25 (KST)_

## 마감 임박 지원사업

| 마감 | 공고 | 기관 | 출처 |
|---|---|---|---|
| 2026-08-25 | [[숭실대학교 캠퍼스타운] 2026 석·박사급 실험실 창업스쿨(유형1) 참여자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178673) | 숭실대학교 캠퍼스타운사업단 | K-Startup 사업공고 |
| 2026-08-25 | [2026년 대전 스타트업스쿨 스타트업 리딩클래스 (3회차 ㅣ ESG와 기후테크를 활용한 스타트업 투자유치 전략)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178820) | 대전창조경제혁신센터 | K-Startup 사업공고 |
| 2026-08-25 | [2026년 민간 산림복지 창업·성장 패키지 FOR:SEED [예비창업패키지] 2차 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178806) | 한국산림복지진흥원  | K-Startup 사업공고 |
| 2026-08-25 | [Request for Proposals (RFP) for the 2026 Startup for All Global (New York) Program](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178847) | KISED | K-Startup 사업공고 |
| 2026-08-25 | [2026년 2기 서울 AI 허브 멤버십 기업 모집 안내](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178879) | 서울 AI 허브 | K-Startup 사업공고 |
| 2026-08-25 | [제3회 「S.Challenge IR」 AXˑDX 분야 창업기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178861) | 서울지방중소벤처기업청, 서울창조경제혁신센터 | K-Startup 사업공고 |
| 2026-08-25 | [[모집] 2026년 청년 산림창업가 시너지캠프 참가자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178853) | 한국임업진흥원 | K-Startup 사업공고 |
| 2026-08-25 | [[무료 웨비나] 해외 VC가 바라보는 시장, 창업가 그리고 글로벌 성장](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178929) | TBC | K-Startup 사업공고 |
| 2026-08-25 | [크라우드펀딩 플랫폼 등록 희망 여성창업자를 위한 2026 여성창업자 사업화지원금 경진대회](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178926) | 고양여성인력개발센터 | K-Startup 사업공고 |
| 2026-08-25 | [2026년 위치정보 보호조치 교육](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178901) | (주)아이전스 | K-Startup 사업공고 |
| 2026-08-25 | [[비전웍스벤처스] GTM 오디세이 차이나 오픈특강 참가자 모집 (~08/25)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178958) | 비전웍스벤처스 | K-Startup 사업공고 |
| 2026-08-25 | [(~8/25) 2026 SIW 서구 스타트업 스케일업 위크 참가자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178950) | 대전광역시 서구청 | K-Startup 사업공고 |
| 2026-08-25 | [경기창업혁신공간 서부권 「스담스담」(오픈 네트워킹) 2회차](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178940) | 경기도경제과학진흥원 | K-Startup 사업공고 |
| 2026-08-26 | [2026년 서울시 소셜벤처 임팩트 측정 사업설명회(2차) 참가신청 모집(~8.26.)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178702) | 서울소셜벤처허브 | K-Startup 사업공고 |
| 2026-08-26 | [2026 신용보증기금 「혁신아이콘」제16기 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178687) | 신용보증기금 | K-Startup 사업공고 |
| 2026-08-26 | [「민관협력 오픈이노베이션 지원」2026년 '성과기업 후속 지원' 창업기업 모집공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178821) | 중소벤처기업부 | K-Startup 사업공고 |
| 2026-08-26 | [[동대문구 창업지원센터] 8월 메이커스페이스(레이저커터, 3D프린팅) 교육 일정](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178774) | 동대문구 창업지원센터 | K-Startup 사업공고 |
| 2026-08-26 | [[서초창업스테이션] 8월 전문 분야 컨설팅 - 스타트업 정책자금 및 자금조달 전략 & 투자유치를 위한 IR·사업계획 고도화](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178825) | 서초창업스테이션 | K-Startup 사업공고 |
| 2026-08-26 | [2026년 웰컴 투 팁스 2차 참가기업 모집 (대경권)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178893) | (주)로우파트너스 | K-Startup 사업공고 |
| 2026-08-26 | [Startup OI Tokyo #Physical AI](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178899) | 재단법인 은행권청년창업재단 | K-Startup 사업공고 |

## 스타트업 뉴스

| 날짜 | 제목 | 출처 |
|---|---|---|
| 2026-08-24 | [식물성 콜라겐은 시작일 뿐…하경수 로가 대표가 설계한 ‘바이오파운드라’](https://www.venturesquare.net/1108077/) | 벤처스퀘어 |
| 2026-08-24 | [먹는 청귤, 바르는 청귤로…귤메달·구달 성수서 이색 협업 열려](https://www.venturesquare.net/1108097/) | 벤처스퀘어 |
| 2026-08-24 | [AI 모델만 지켜선 부족하다…GS네오텍, ‘운영 보안’ 해법 제시](https://www.venturesquare.net/1108101/) | 벤처스퀘어 |
| 2026-08-24 | [소상공인 위기, ‘경영진단’부터…중기부·학계 미래 전략 머리 맞댔다](https://www.venturesquare.net/1108112/) | 벤처스퀘어 |
| 2026-08-24 | [군집드론이 인천항 노린다면…쿠도커뮤니케이션, 58억 원 방어체계 가동](https://www.venturesquare.net/1108121/) | 벤처스퀘어 |
| 2026-08-24 | [상법 개정에 주주행동주의까지…디엘지·삼성화재, 임원 책임 해법 찾는다](https://www.venturesquare.net/1108124/) | 벤처스퀘어 |
| 2026-08-24 | [부산서 설계하고 태국서 만들고 인도서 개발…일에이엔 ‘아시아 IT 벨트’](https://www.venturesquare.net/1108135/) | 벤처스퀘어 |
| 2026-08-24 | [중고차 문 여는 순간까지 관리…오토핸즈, 세스코 전용 향 도입](https://www.venturesquare.net/1108143/) | 벤처스퀘어 |
| 2026-08-24 | [66세 시니어와 10대 개발 인턴이 한 회사에…PTKOREA가 바꾼 채용 문법](https://www.venturesquare.net/1108152/) | 벤처스퀘어 |
| 2026-08-24 | [K팝 굿즈 사러 해외 지갑 열렸다…딜리버드코리아 역직구 390억](https://www.venturesquare.net/1108159/) | 벤처스퀘어 |
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
