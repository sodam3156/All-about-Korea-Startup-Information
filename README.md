# All-about-Korea-Startup-Information

세종 청년창업 기관 공지 · 정부 지원사업 공고 · 스타트업 뉴스를 **매일 14:00 KST에 자동 수집**하는 저장소.
GitHub Actions가 수집→중복제거→상세저장→아래 대시보드 갱신→텔레그램 브리핑까지 수행한다 (git-scraping — 서버·DB·API 비용 없음).

**완전 규칙 기반**: 소스마다 공식 API/RSS 또는 정규식 파서를 쓴다(LLM 미사용, 고정비 $0). 대신 사이트가 개편되면 파서가 조용히 0건을 낼 수 있어, 같은 소스가 **연속 2회 이상 0건**이면 `data/source_health.json`에 기록하고 다이제스트에 "⚠️ 소스 점검 필요"로 경고한다 — 이게 규칙 기반의 유일한 약점(개편에 안 깨지는 AI 추출 대비)을 메우는 피드백 루프다.

<!-- AUTO:START -->

_자동 갱신: 2026-08-28 (KST)_

## 마감 임박 지원사업

| 마감 | 공고 | 기관 | 출처 |
|---|---|---|---|
| 2026-08-28 | [[2026-047호] 2026년 디지털 콘텐츠 산업 규제개혁 어드바이저 참여기업 모집 공고](https://sjtp.or.kr/bbs/board.php?bo_table=business01&wr_id=1972) | 정보통신산업진흥원 | 세종테크노파크 사업공고 |
| 2026-08-28 | [2026년 2차 28청춘창업소 신규 입주기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178686) | 고양산업진흥원 | K-Startup 사업공고 |
| 2026-08-28 | [2026 하반기 MARU 배치 스타트업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178676) | 재단법인 아산나눔재단 | K-Startup 사업공고 |
| 2026-08-28 | [2026 경제계 주도 대국민 창업·육성 프로젝트 「더하기 창업」 참가팀 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178788) | 머스트액셀러레이터 | K-Startup 사업공고 |
| 2026-08-28 | [2026년 이천시 청년창업지원센터 입주기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178768) | 청강문화산업대학교 산학협력단 | K-Startup 사업공고 |
| 2026-08-28 | [2026 대전 팁스타운 제2차 팁스 링크 일본 파트너 초청 상담회](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178892) | 창업진흥원 | K-Startup 사업공고 |
| 2026-08-28 | [『2026년 서울바이오허브- (일본 제약기업) 마루호 오픈이노베이션 프로그램』참여기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178849) | 서울바이오허브 | K-Startup 사업공고 |
| 2026-08-28 | [일본 오사카(간사이) 지역 진출 지원사업 Plug in: Osaka #12 참가 스타트업 모집(~8/28 17:59까지)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178920) | (재)부산창조경제혁신센터 | K-Startup 사업공고 |
| 2026-08-28 | [초도물량 양산 패키지 수혜기업 모집(~8/28)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178919) | 경북대학교 스타트업지원센터장 | K-Startup 사업공고 |
| 2026-08-28 | [제품 런칭 패키지 수혜기업 모집(~8/28)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178918) | 경북대학교 스타트업지원센터장 | K-Startup 사업공고 |
| 2026-08-28 | [2026년 대전 스타트업 원스톱 지원센터 아카데미 2회차](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178860) | 대전창조경제혁신센터 | K-Startup 사업공고 |
| 2026-08-28 | [2026 AI 기반 소셜임팩트 기업 활성화 지원사업](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178944) | ㈜포켓컴퍼니 | K-Startup 사업공고 |
| 2026-08-28 | [2026년 한국지역난방공사 창업·벤처기업 지원사업 참여기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179004) | 한국청년기업가정신재단 | K-Startup 사업공고 |
| 2026-08-30 | [2026년 2nd S.Stage 개최 안내](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178721) | 서울창조경제혁신센터 | K-Startup 사업공고 |
| 2026-08-30 | [2026 창업오디션, 고양IR데이 참가기업 추가모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178810) | 고양시장 | K-Startup 사업공고 |
| 2026-08-30 | [2026년 판로확대 지원 참여 소상공인 모집(셀러허브)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178871) | 중소상공인희망재단 | K-Startup 사업공고 |
| 2026-08-30 | [[제2서울핀테크랩] 서울 핀테크 위크 2026 제2서울핀테크랩 데모데이 with 네이버클라우드 참가기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178858) | 제2서울핀테크랩 | K-Startup 사업공고 |
| 2026-08-31 | [2026 벤처확인 인증준비기업 맞춤형 무료 진단 지원사업](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178745) | (주)엠비즈플래닛 산하 혁신기술경영인증지원센터 | K-Startup 사업공고 |
| 2026-08-31 | [[국토교통부 x 물류산업진흥재단] 2026 물류상생 Meet-up 행사 기술기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178731) | 물류산업진흥재단 | K-Startup 사업공고 |
| 2026-08-31 | [2026 대덕특구 딥테크 혁신성장 플랫폼(전략기술 발굴 및 매칭) (8/1 ~ 8/31)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178719) | 연구개발특구진흥재단 | K-Startup 사업공고 |

## 스타트업 뉴스

| 날짜 | 제목 | 출처 |
|---|---|---|
| 2026-08-26 | [조선소 벽 타는 피지컬 AI…디든로보틱스, 포브스 아시아 유망기업 선정](https://www.venturesquare.net/1108879/) | 벤처스퀘어 |
| 2026-08-27 | [미국 테크와 동남아 성장기업 잇는다…SBVA, 비전펀드 출신 2인 영입](https://www.venturesquare.net/1108892/) | 벤처스퀘어 |
| 2026-08-27 | [지역의 자원을 서로 잇는다…경남 로컬기업 23곳 남해서 협업 모색](https://www.venturesquare.net/1108900/) | 벤처스퀘어 |
| 2026-08-27 | [AI가 통역해도 영어는 더 중요해진다…스픽·암참이 짚은 글로벌 인재 전략](https://www.venturesquare.net/1108907/) | 벤처스퀘어 |
| 2026-08-27 | [애니 보다가 미드로 갈아탄다…리얼클래스, 장르 칸막이 없앤 올인원 출시](https://www.venturesquare.net/1108917/) | 벤처스퀘어 |
| 2026-08-27 | [찍어둔 흉부 X-ray로 골다공증 위험 찾는다…프로메디우스·대웅제약 전국 유통](https://www.venturesquare.net/1108931/) | 벤처스퀘어 |
| 2026-08-27 | [한국서 18배 성장한 스노우플레이크…이제 AI가 ‘일하는 기업’ 만든다](https://www.venturesquare.net/1108964/) | 벤처스퀘어 |
| 2026-08-27 | [분석은 하루→10분, 데이터 사용자는 6.5배…‘데이터 드라이버 어워드 2026’ 수상 기업은 달랐다](https://www.venturesquare.net/1108973/) | 벤처스퀘어 |
| 2026-08-27 | [금융 AI, ‘무엇을 할 수 있나’에서 ‘어떻게 쓸까’로…AWS 파이낸셜 서비스 포럼 서울 2026](https://www.venturesquare.net/1108985/) | 벤처스퀘어 |
| 2026-08-27 | [“금융 AI, PoC 넘어 AI 네이티브로”…AWS가 본 금융 AX의 다음 단계](https://www.venturesquare.net/1108997/) | 벤처스퀘어 |
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
