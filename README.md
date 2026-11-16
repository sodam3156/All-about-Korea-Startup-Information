# All-about-Korea-Startup-Information

세종 청년창업 기관 공지 · 정부 지원사업 공고 · 스타트업 뉴스를 **매일 14:00 KST에 자동 수집**하는 저장소.
GitHub Actions가 수집→중복제거→상세저장→아래 대시보드 갱신→텔레그램 브리핑까지 수행한다 (git-scraping — 서버·DB·API 비용 없음).

**완전 규칙 기반**: 소스마다 공식 API/RSS 또는 정규식 파서를 쓴다(LLM 미사용, 고정비 $0). 대신 사이트가 개편되면 파서가 조용히 0건을 낼 수 있어, 같은 소스가 **연속 2회 이상 0건**이면 `data/source_health.json`에 기록하고 다이제스트에 "⚠️ 소스 점검 필요"로 경고한다 — 이게 규칙 기반의 유일한 약점(개편에 안 깨지는 AI 추출 대비)을 메우는 피드백 루프다.

<!-- AUTO:START -->

_자동 갱신: 2026-11-16 (KST)_

## 마감 임박 지원사업

| 마감 | 공고 | 기관 | 출처 |
|---|---|---|---|
| 2026-11-16 | [AI 올라운더(기획,개발,마케팅) 창업가육성과정 8기 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179353) | 디지플래닛 | K-Startup 사업공고 |
| 2026-11-16 | [2026년 제4차 관악S밸리 창업 공간 신규 입주기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179582) | 재단법인 관악중소벤처진흥원 | K-Startup 사업공고 |
| 2026-11-16 | [ENSL TECH LAB 13th 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179530) | (주)엔슬파트너스 | K-Startup 사업공고 |
| 2026-11-16 | [[청년 취창업 특강] 나만의 일을 만들어가는 방법](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179611) | 관악구청 | K-Startup 사업공고 |
| 2026-11-16 | [[한국국제협력단]「 KOICA IMPACT TOGETHER 2026 」 행사](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179642) | 한국국제협력단 | K-Startup 사업공고 |
| 2026-11-16 | [[무료] 제 9회 2026 최신 기술 컨퍼런스:Practical Physical Process 과학을 현실로, 혁신을 확장으로 (11/17~18)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179692) | 써모 피셔 사이언티픽 코리아 | K-Startup 사업공고 |
| 2026-11-16 | [제8차 충남 오픈이노베이션 포럼](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179736) | 한국기술교육대학교 앵커사업단 | K-Startup 사업공고 |
| 2026-11-16 | [["Beyond Silicon 2026" 화합물반도체 미래를 여는 길] 개최](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179728) | 한국나노기술원 | K-Startup 사업공고 |
| 2026-11-16 | [사례에서 배우는 지역 창업 추진 전략 수립 교육](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179726) | 상지대학교 벤처창업본부  | K-Startup 사업공고 |
| 2026-11-16 | [소공인 역량강화 아카데미 5기 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179759) | 서울시 강동가죽제조지원센터 | K-Startup 사업공고 |
| 2026-11-16 | [2026년 인문·기술 융합 네트워크 ‘Thinking Day’ 2차 참가자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179770) | 단국C-앵커사업단 | K-Startup 사업공고 |
| 2026-11-17 | [2026 글로벌 진출 - 글로벌 진출과 협력 네트워크 확장 전략](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179555) | 서울창업허브 창동 | K-Startup 사업공고 |
| 2026-11-17 | [2026년 K-바이오랩허브 멤버십 기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179654) | 인천창조경제혁신센터 | K-Startup 사업공고 |
| 2026-11-17 | [[서울과학기술대학교]3D프린터 장비교육](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179757) | 서울과학기술대학교 | K-Startup 사업공고 |
| 2026-11-17 | [2026년 11월 전북 IR피칭 & 오피스아워 by KRYPTON 신청 접수](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179749) | (주)크립톤 전북지사 | K-Startup 사업공고 |
| 2026-11-17 | [[KIIN 포럼] 반도체 공정을 혁신하는 스타트업들 (11/18, 수)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179716) | 한국임팩트투자네트워크 | K-Startup 사업공고 |
| 2026-11-17 | [STARTUP STARRY NIGHT in Seoul 1:1 밋업(투자, O.I.) 참여기업 모집(11월 허브아워)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179765) | (재)서울경제진흥원 | K-Startup 사업공고 |
| 2026-11-17 | [[알파브라더스] 「2026 충청 스타트업 벤처포럼」 2회차-오픈이노베이션 교류회 참가 안내의 건](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179764) | 알파브라더스 | K-Startup 사업공고 |
| 2026-11-17 | [스타트업을 위한 B2B 영업 전략 특강](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179769) | 한국기술교육대학교 앵커사업단 | K-Startup 사업공고 |
| 2026-11-18 | [2026 논산시 사회적경제 창업 아카데미 참여자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179591) | 논산시 사회적경제통합지원센터 | K-Startup 사업공고 |

## 스타트업 뉴스

| 날짜 | 제목 | 출처 |
|---|---|---|
| 2026-11-16 | [슈퍼브에이아이, 디지털 혁신 유공 부총리 표창…산업용 비전 AI 기술력 인정](https://www.venturesquare.net/1128841/) | 벤처스퀘어 |
| 2026-11-16 | [ZEP, 20여 개국 참여한 ‘AI BEYOND 2026’ 개최…온라인서 AI 기술·비즈니스 교류](https://www.venturesquare.net/1128848/) | 벤처스퀘어 |
| 2026-11-16 | [한세실업·한세모빌리티, 장애 예술인 12명 채용…문화예술 직무 개발 성과 인정](https://www.venturesquare.net/1128851/) | 벤처스퀘어 |
| 2026-11-16 | [비글루, 클링 AI와 숏드라마 공모전 개최…수상 넘어 시리즈 제작·수익화 지원](https://www.venturesquare.net/1128864/) | 벤처스퀘어 |
| 2026-11-16 | [아이디어스, 블랙프라이데이 ‘아주큰 세일’ 개최…핸드메이드 작품 최대 89% 할인](https://www.venturesquare.net/1128865/) | 벤처스퀘어 |
| 2026-11-16 | [동국대·씨엔티테크, 스타트업 CEO·투자심사역 과정 14기 모집…1월 7일 개강](https://www.venturesquare.net/1128877/) | 벤처스퀘어 |
| 2026-11-16 | [어니스트AI, 금융권 AI 솔루션 공급 확대에 대규모 채용…현장 구축·신용전략 인력 강화](https://www.venturesquare.net/1128880/) | 벤처스퀘어 |
| 2026-11-16 | [딜라이트룸 알라미, K팝 신곡을 아침 알람으로…월 300만 회 사용한다](https://www.venturesquare.net/1128892/) | 벤처스퀘어 |
| 2026-11-16 | [크래프톤, 글로벌 개발자 1000명 모인 ‘KDC WEEK 2026’ 개최…실패 경험까지 공유](https://www.venturesquare.net/1128898/) | 벤처스퀘어 |
| 2026-11-16 | [엘리스그룹, 대한민국 인터넷대상 대통령상 수상…AI 인프라부터 산업용 에이전트까지 기술력 인정](https://www.venturesquare.net/1128901/) | 벤처스퀘어 |
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
