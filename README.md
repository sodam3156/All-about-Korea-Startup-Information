# All-about-Korea-Startup-Information

세종 청년창업 기관 공지 · 정부 지원사업 공고 · 스타트업 뉴스를 **매일 14:00 KST에 자동 수집**하는 저장소.
GitHub Actions가 수집→중복제거→상세저장→아래 대시보드 갱신→텔레그램 브리핑까지 수행한다 (git-scraping — 서버·DB·API 비용 없음).

**완전 규칙 기반**: 소스마다 공식 API/RSS 또는 정규식 파서를 쓴다(LLM 미사용, 고정비 $0). 대신 사이트가 개편되면 파서가 조용히 0건을 낼 수 있어, 같은 소스가 **연속 2회 이상 0건**이면 `data/source_health.json`에 기록하고 다이제스트에 "⚠️ 소스 점검 필요"로 경고한다 — 이게 규칙 기반의 유일한 약점(개편에 안 깨지는 AI 추출 대비)을 메우는 피드백 루프다.

<!-- AUTO:START -->

_자동 갱신: 2026-10-22 (KST)_

## 마감 임박 지원사업

| 마감 | 공고 | 기관 | 출처 |
|---|---|---|---|
| 2026-10-22 | [2026년 강북창업지원센터 10월 창업 교육 및 그룹상담 프로그램 참가자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179418) | 강북청년창업마루 | K-Startup 사업공고 |
| 2026-10-22 | [쇼미더임팩트 시즌6 참가자 모집 [IMPACT IR 경연대회]](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179375) | 충남사회적경제지원센터장 | K-Startup 사업공고 |
| 2026-10-22 | [[강동구 청년해냄센터] 2026 모의창업스쿨 2차 교육 참가자 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179460) | 강동구 청년해냄센터 | K-Startup 사업공고 |
| 2026-10-22 | [[온라인·무료] 코딩·사업자 없이 여는 내 강의·전자책 판매 사이트](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179443) | 스쿨모아 주식회사  | K-Startup 사업공고 |
| 2026-10-22 | [[중앙사회서비스원] 2026년 제3회 사회서비스 투자교류회](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179501) | 중앙사회서비스원 | K-Startup 사업공고 |
| 2026-10-22 | [마포비즈니스센터 4차 신규입주기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179489) | 마포비즈니스센터 | K-Startup 사업공고 |
| 2026-10-22 | [제3회 판다밋업 : Inside Japan 제약·바이오·의료기기 가치사슬 기반 일본 진출 전략](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179504) | 경기도 4차산업혁명센터 | K-Startup 사업공고 |
| 2026-10-22 | [2026 신한퓨처스랩 스타트업 성장 포럼 &apos;인사이트랩(Insight Lab)&apos; 참관 기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179502) | 신한퓨처스랩 | K-Startup 사업공고 |
| 2026-10-22 | [[ 모 집 ] GVC AI Platform Startup Enabling Program 및 스마트워크·쇼핑몰 창업지원 및 AI 전환 지원](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179540) | 글로벌벤처센터 | K-Startup 사업공고 |
| 2026-10-23 | [2026년 스마트 혁신가전 유공자 포상 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179307) | 한국전자정보통신산업진흥회 | K-Startup 사업공고 |
| 2026-10-23 | [2026년 제2차 대전센터 여성BI 입주기업 모집공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179338) | (재)여성기업종합지원센터 대전센터장 | K-Startup 사업공고 |
| 2026-10-23 | [2026년 하반기 남동구 청년창업지원센터 입주기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179411) | 남동구 청년창업지원센터 | K-Startup 사업공고 |
| 2026-10-23 | [2026년 위치정보 보호조치 교육 (6차)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179393) |  (주)아이전스 | K-Startup 사업공고 |
| 2026-10-23 | [[ 칠곡군 중장년 기술창업센터]제3차 Pre-인큐베이팅 창업교육 수강생 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179381) | 칠곡군중장년기술창업센터 | K-Startup 사업공고 |
| 2026-10-23 | [경기창업혁신공간 서부권 「스담스담」(오픈 네트워킹) 3회차](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179416) | 경기도경제과학진흥원 | K-Startup 사업공고 |
| 2026-10-23 | [[서초창업스테이션] 10월 1:1 전문 분야 컨설팅 - 지식재산권/특허 전략, 브랜딩 전략](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179434) | 서초창업스테이션 | K-Startup 사업공고 |
| 2026-10-23 | [2027년 K-water 해외시장개척단 참여기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179477) | K-water 기후테크혁신처장 | K-Startup 사업공고 |
| 2026-10-23 | [2026년 초기창업패키지 로켓십 IR 경진대회 참가기업 모집 (3회차: 기후·ESG)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179474) | 씨엔티테크(주) | K-Startup 사업공고 |
| 2026-10-23 | [2026 산업단지 오픈이노베이션프로그램 KICXUP 챌린지 & 로컬 스타트업 2차 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179496) | 한국산업단지공단 | K-Startup 사업공고 |
| 2026-10-23 | [2026년 나주형 청년 에너지 창업 사관학교(직·주·락·비) 사업 1차 수행기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179519) |  (재)전남테크노파크 | K-Startup 사업공고 |

## 스타트업 뉴스

| 날짜 | 제목 | 출처 |
|---|---|---|
| 2026-10-21 | [핀다, 대원저축은행 지분 60% 인수 승인…대출 중개 넘어 금융상품 직접 공급](https://www.venturesquare.net/1121776/) | 벤처스퀘어 |
| 2026-10-21 | [에이딘로보틱스, ROBEX 2026서 로봇 힘 제어 기술 시연…HD현대로보틱스와 협력 확대](https://www.venturesquare.net/1121791/) | 벤처스퀘어 |
| 2026-10-21 | [울산창조경제혁신센터, 기술 스타트업 3개사 영국 진출 지원…런던·버밍엄서 협력 기회 발굴](https://www.venturesquare.net/1121795/) | 벤처스퀘어 |
| 2026-10-21 | [중기부, 대구·경북 첫 통합 지역성장펀드 1300억원 결성…2000억원 벤처펀드 조성 추진](https://www.venturesquare.net/1121806/) | 벤처스퀘어 |
| 2026-10-21 | [네이션에이, 85억원 시리즈A 투자 유치…AI 영상 제작 플랫폼 통합·글로벌 확장 추진](https://www.venturesquare.net/1121809/) | 벤처스퀘어 |
| 2026-10-21 | [칼렛바이오, 친환경 포장 기술로 국무총리표창 수상…재활용 종이테이프 상용화 성과](https://www.venturesquare.net/1121819/) | 벤처스퀘어 |
| 2026-10-21 | [줌, 회의·채팅·고객 데이터 연결하는 ‘통합 컨텍스트 레이어’ 공개…AI 업무 자동화 확대](https://www.venturesquare.net/1121829/) | 벤처스퀘어 |
| 2026-10-21 | [오후두시랩 설수경 대표, 탄소 데이터를 소비자의 선택 기준으로 바꾸다](https://www.venturesquare.net/1121444/) | 벤처스퀘어 |
| 2026-10-22 | [노드큐어, 반려견 맞춤형 면역항암제 개발로 치료 선택지 확대](https://www.venturesquare.net/1121881/) | 벤처스퀘어 |
| 2026-10-22 | [넥썸, 반도체 냉각유체 관리에서 정밀 온도제어 장비까지](https://www.venturesquare.net/1121855/) | 벤처스퀘어 |
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
