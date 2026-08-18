# All-about-Korea-Startup-Information

세종 청년창업 기관 공지 · 정부 지원사업 공고 · 스타트업 뉴스를 **매일 14:00 KST에 자동 수집**하는 저장소.
GitHub Actions가 수집→중복제거→상세저장→아래 대시보드 갱신→텔레그램 브리핑까지 수행한다 (git-scraping — 서버·DB·API 비용 없음).

**완전 규칙 기반**: 소스마다 공식 API/RSS 또는 정규식 파서를 쓴다(LLM 미사용, 고정비 $0). 대신 사이트가 개편되면 파서가 조용히 0건을 낼 수 있어, 같은 소스가 **연속 2회 이상 0건**이면 `data/source_health.json`에 기록하고 다이제스트에 "⚠️ 소스 점검 필요"로 경고한다 — 이게 규칙 기반의 유일한 약점(개편에 안 깨지는 AI 추출 대비)을 메우는 피드백 루프다.

<!-- AUTO:START -->

_자동 갱신: 2026-08-18 (KST)_

## 마감 임박 지원사업

| 마감 | 공고 | 기관 | 출처 |
|---|---|---|---|
| 2026-08-18 | [2026년 웰컴 투 팁스 1차 참가기업 모집 (충청권)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178845) | (주)로우파트너스 | K-Startup 사업공고 |
| 2026-08-18 | [2026년 성남시 폴란드 방산 시장개척단 참가기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178812) | 성남산업진흥원 | K-Startup 사업공고 |
| 2026-08-18 | [중앙대-금천구 창업 협력공간(창업교육스튜디오) 입주자 모집 공고(2차)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178807) | 중앙대학교 산학협력단 | K-Startup 사업공고 |
| 2026-08-18 | [중앙대-금천구 창업 협력공간(혁신지원거점센터) 입주자 모집 공고(7차)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178805) | 중앙대학교 산학협력단 | K-Startup 사업공고 |
| 2026-08-18 | [[강동구 청년해냄센터] 투자유치 마스터 스쿨 참가자 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178797) | 감동구 청년해냄센터 | K-Startup 사업공고 |
| 2026-08-18 | [[용인시산업진흥원] 2026년 용인 오픈이노베이션 교류회 3회차(바이오·헬스케어)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178790) | 알파브라더스 | K-Startup 사업공고 |
| 2026-08-18 | [2026년 CKL기업지원센터 입주기업 하반기 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178818) | 한국콘텐츠진흥원 | K-Startup 사업공고 |
| 2026-08-18 | [[서귀포시] 2026년 서귀포시 스타트업타운 공석에 따른 입주기업 2기 하반기 모집 (~8/18)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178750) | 넥스트챌린지 | K-Startup 사업공고 |
| 2026-08-18 | [[모집기간연장] 제11회 소상공인 쇼케이스데이 참가기업 모집 (소상공인 투지유치 연계 & 판로확대 지원)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178869) | 재단법인 중소상공인희망재단  | K-Startup 사업공고 |
| 2026-08-18 | [[경과원X메가존] AWS AI-DLC 기반 원데이 워크숍](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178865) | 경기도경제과학진흥원 | K-Startup 사업공고 |
| 2026-08-18 | [2026 관광기업 베트남 오픈 이노베이션 참가기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178862) | 한국관광공사  | K-Startup 사업공고 |
| 2026-08-18 | [2026년 경기스타트업플랫폼 온라인 밋업위크(3차) 참가기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178809) | 경기도경제과학진흥원 | K-Startup 사업공고 |
| 2026-08-19 | [[글로벌] 2026 BIOHEALTH GLOBAL BRIDGE : JOHNS HOPKINS / HIKMA 프로그램 참가기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178743) | 서울창조경제혁신센터 | K-Startup 사업공고 |
| 2026-08-19 | [2026년 여성CEO 비즈니스 아카데미 서울권역 시즌 2](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178741) | 한국여성경제인협회 | K-Startup 사업공고 |
| 2026-08-19 | [2026년 제3차 창업지원센터 입주기업 모집공고(~8/19, 수 16시까지)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178708) | 용인시산업진흥원 | K-Startup 사업공고 |
| 2026-08-19 | [[서초창업스테이션] 서리풀 소상공인 창업 클리닉(8월) - 소상공인 1:1 컨설팅](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178690) | 서초창업스테이션 | K-Startup 사업공고 |
| 2026-08-19 | [경기 서부권 기술사업화 세미나](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178670) | 가톨릭대학교 | K-Startup 사업공고 |
| 2026-08-19 | [구로구 청년창업지원센터 일반 창업교육(반기: 1회차): 정부지원사업 효율적인 활용 방법](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178769) | 구로구 청년창업지원센터 | K-Startup 사업공고 |
| 2026-08-19 | [Se7en on the table 전문가 멘토링 프로그램 참가기업 모집 (~08.19)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178837) | 서강대학교 판교캠퍼스사업단 | K-Startup 사업공고 |
| 2026-08-19 | [「2026년 로봇 기반 공간컴퓨팅 창업지원사업」예비창업자(팀) 모집 추가공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178833) | (재)대구테크노파크 | K-Startup 사업공고 |

## 스타트업 뉴스

| 날짜 | 제목 | 출처 |
|---|---|---|
| 2026-08-17 | [싸이월드 170억 건 데이터 복원한다는데…김호광 전 대표 “서버부터 확인해야”](https://www.venturesquare.net/1106460/) | 벤처스퀘어 |
| 2026-08-17 | [밤 10시 주문·냉장고 안 배송이 거래를 키웠다…미트박스글로벌, 상반기 매출 797억원](https://www.venturesquare.net/1106498/) | 벤처스퀘어 |
| 2026-08-17 | [드론을 띄우지 않고 출고 품질을 검사한다…위플로, 미국서 DRQC 시연](https://www.venturesquare.net/1106507/) | 벤처스퀘어 |
| 2026-08-17 | [부츠·매닝스·올리브영 30년 경험을 화장품으로…달글로우인서울, 파리서 첫 시장 검증](https://www.venturesquare.net/1106511/) | 벤처스퀘어 |
| 2026-08-17 | [핀버로 “대출 아닌 매출로 자금 조달”… 퍼스트밸류 송봉호 대표가 증명한 금융 해법](https://www.venturesquare.net/1106483/) | 벤처스퀘어 |
| 2026-08-17 | [딥파인, 100억원 시리즈B 유치…현장별 AI 구축을 반복 매출 플랫폼으로 전환한다](https://www.venturesquare.net/1106541/) | 벤처스퀘어 |
| 2026-08-17 | [소재부터 직접 개발한 몰든, 누적 매출 90억원…더벤처스 ‘오블리뷰’에 시드 투자](https://www.venturesquare.net/1106544/) | 벤처스퀘어 |
| 2026-08-17 | [AI 에이전트가 매출 42%…와이즈넛, 상반기 적자 절반 줄였다](https://www.venturesquare.net/1106556/) | 벤처스퀘어 |
| 2026-08-17 | [3,300시간 무인 주행, 거래소 심사대로…라이드플럭스 코스닥 예심 청구](https://www.venturesquare.net/1106563/) | 벤처스퀘어 |
| 2026-08-18 | [위조상품에서 AI 사칭까지…마크비전 대형 고객 3배 늘었다](https://www.venturesquare.net/1106570/) | 벤처스퀘어 |
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
