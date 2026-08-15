# All-about-Korea-Startup-Information

세종 청년창업 기관 공지 · 정부 지원사업 공고 · 스타트업 뉴스를 **매일 14:00 KST에 자동 수집**하는 저장소.
GitHub Actions가 수집→중복제거→상세저장→아래 대시보드 갱신→텔레그램 브리핑까지 수행한다 (git-scraping — 서버·DB·API 비용 없음).

**완전 규칙 기반**: 소스마다 공식 API/RSS 또는 정규식 파서를 쓴다(LLM 미사용, 고정비 $0). 대신 사이트가 개편되면 파서가 조용히 0건을 낼 수 있어, 같은 소스가 **연속 2회 이상 0건**이면 `data/source_health.json`에 기록하고 다이제스트에 "⚠️ 소스 점검 필요"로 경고한다 — 이게 규칙 기반의 유일한 약점(개편에 안 깨지는 AI 추출 대비)을 메우는 피드백 루프다.

<!-- AUTO:START -->

_자동 갱신: 2026-08-15 (KST)_

## 마감 임박 지원사업

| 마감 | 공고 | 기관 | 출처 |
|---|---|---|---|
| 2026-08-16 | [[혁신창업캠프]청년 창업자를 위한 창업 인사이트 캠프](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178752) | 관악구청 | K-Startup 사업공고 |
| 2026-08-16 | [26년 8월 스타트업 언론 홍보 지원사업 참가사 모집 공고(1차)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178759) | 스타트업 데일리 | K-Startup 사업공고 |
| 2026-08-16 | [2026년 AWS X AI 실무 프로젝트 아카데미 교육생 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178842) | 인천대학교 창업지원단 | K-Startup 사업공고 |
| 2026-08-17 | [한계를 뛰어넘는 연구와 기술에 투자하다 hosted by ARIA × Antler Korea 밋업](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178730) | 앤틀러코리아 | K-Startup 사업공고 |
| 2026-08-17 | [2027 서울관광플라자 신규 입주 스타트업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178711) | 서울관광재단 | K-Startup 사업공고 |
| 2026-08-17 | [2026년 SaaS 전환지원센터xAWS SaaS 현대화 교육 2회차 참가자 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178782) | 정보통신산업진흥원, SaaS 전환지원센터 | K-Startup 사업공고 |
| 2026-08-17 | [2026년 창업혁신공간(동부권) 하남시 스타트업 발굴 및 육성 지원사업 &apos;이루다+&apos; 참여기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178757) | 경기도경제과학진흥원 | K-Startup 사업공고 |
| 2026-08-17 | [[네스토리움] AI시대, 예비·초기창업기업 생존전략 세미나](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178822) | 네스토리움 주식회사 | K-Startup 사업공고 |
| 2026-08-17 | [「2026년 대구콘텐츠기업지원센터 기업 경영 상담 프로그램(2차)」 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178876) | (재)대구디지털혁신진흥원 | K-Startup 사업공고 |
| 2026-08-17 | [2026 주력산업분야 창업기업 스케일업 사업화지원](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178874) | 선문대학교 창업보육센터 | K-Startup 사업공고 |
| 2026-08-17 | [2026 서울창업허브 공덕 8월 허브아워 - 투자, 보증, 공공데이터](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178866) | (재)서울경제진흥원 | K-Startup 사업공고 |
| 2026-08-17 | [2026년 서울창업허브 창동-조이시티 오픈이노베이션 참가기업 추가모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178855) | 서울창업허브 창동 | K-Startup 사업공고 |
| 2026-08-18 | [2026년 웰컴 투 팁스 1차 참가기업 모집 (충청권)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178845) | (주)로우파트너스 | K-Startup 사업공고 |
| 2026-08-18 | [2026년 성남시 폴란드 방산 시장개척단 참가기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178812) | 성남산업진흥원 | K-Startup 사업공고 |
| 2026-08-18 | [중앙대-금천구 창업 협력공간(창업교육스튜디오) 입주자 모집 공고(2차)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178807) | 중앙대학교 산학협력단 | K-Startup 사업공고 |
| 2026-08-18 | [중앙대-금천구 창업 협력공간(혁신지원거점센터) 입주자 모집 공고(7차)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178805) | 중앙대학교 산학협력단 | K-Startup 사업공고 |
| 2026-08-18 | [[강동구 청년해냄센터] 투자유치 마스터 스쿨 참가자 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178797) | 감동구 청년해냄센터 | K-Startup 사업공고 |
| 2026-08-18 | [[용인시산업진흥원] 2026년 용인 오픈이노베이션 교류회 3회차(바이오·헬스케어)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178790) | 알파브라더스 | K-Startup 사업공고 |
| 2026-08-18 | [2026년 CKL기업지원센터 입주기업 하반기 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178818) | 한국콘텐츠진흥원 | K-Startup 사업공고 |
| 2026-08-18 | [[서귀포시] 2026년 서귀포시 스타트업타운 공석에 따른 입주기업 2기 하반기 모집 (~8/18)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178750) | 넥스트챌린지 | K-Startup 사업공고 |

## 스타트업 뉴스

| 날짜 | 제목 | 출처 |
|---|---|---|
| 2026-08-14 | [[김지현의 Scale-Up Note] 스케일업은 매출구조를 이해하는 데서 시작한다](https://www.venturesquare.net/1106183/) | 벤처스퀘어 |
| 2026-08-14 | [중기부 글로벌 팁스 선정 레티널, AI 글래스 광학 모듈 두께 53% 줄인다](https://www.venturesquare.net/1106191/) | 벤처스퀘어 |
| 2026-08-14 | [거래량 위축에 수익성이 더 크게 흔들렸다…두나무, 상반기 영업이익 79.7% 감소](https://www.venturesquare.net/1106194/) | 벤처스퀘어 |
| 2026-08-14 | [거래액 21조원·매출 14% 성장했지만…야놀자, 상반기 영업손실 152억원 기록했다](https://www.venturesquare.net/1106201/) | 벤처스퀘어 |
| 2026-08-14 | [OEM·ODM 수주와 뽀로로 치약 수출이 이끌었다…케이엠제약, 상반기 매출 13.4% 늘었다](https://www.venturesquare.net/1106213/) | 벤처스퀘어 |
| 2026-08-14 | [고독성 의약품을 밀폐된 채 검사한다…엔클로니, 유럽 제약사에 장비 공급](https://www.venturesquare.net/1106221/) | 벤처스퀘어 |
| 2026-08-14 | [학생이 영어 지문 어디에서 막히는지 읽는다…비주얼캠프 ‘리드클래스’ 금상 수상](https://www.venturesquare.net/1106224/) | 벤처스퀘어 |
| 2026-08-14 | [인공 적혈구 임상에 쓸 기준 세포를 만든다…아트블러드, 스케일업 팁스 선정](https://www.venturesquare.net/1106236/) | 벤처스퀘어 |
| 2026-08-14 | [채용 회복에 AX 매출을 더했다…원티드랩, 2분기 영업이익 17억원으로 돌아섰다](https://www.venturesquare.net/1106243/) | 벤처스퀘어 |
| 2026-08-14 | [AI 모델을 가볍게 만든 노타, 에이전트 운영 비용까지 줄인다](https://www.venturesquare.net/1106250/) | 벤처스퀘어 |
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
