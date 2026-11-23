# All-about-Korea-Startup-Information

세종 청년창업 기관 공지 · 정부 지원사업 공고 · 스타트업 뉴스를 **매일 14:00 KST에 자동 수집**하는 저장소.
GitHub Actions가 수집→중복제거→상세저장→아래 대시보드 갱신→텔레그램 브리핑까지 수행한다 (git-scraping — 서버·DB·API 비용 없음).

**완전 규칙 기반**: 소스마다 공식 API/RSS 또는 정규식 파서를 쓴다(LLM 미사용, 고정비 $0). 대신 사이트가 개편되면 파서가 조용히 0건을 낼 수 있어, 같은 소스가 **연속 2회 이상 0건**이면 `data/source_health.json`에 기록하고 다이제스트에 "⚠️ 소스 점검 필요"로 경고한다 — 이게 규칙 기반의 유일한 약점(개편에 안 깨지는 AI 추출 대비)을 메우는 피드백 루프다.

<!-- AUTO:START -->

_자동 갱신: 2026-11-24 (KST)_

## 마감 임박 지원사업

| 마감 | 공고 | 기관 | 출처 |
|---|---|---|---|
| 2026-11-24 | [「2026년 대구스타트업 리더스포럼」제65차 IR피칭 참여기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179348) | (재) 대구창조경제혁신센터  대표이사 | K-Startup 사업공고 |
| 2026-11-24 | [[동대문구 창업지원센터] 11월 메이커스페이스(레이저커터, 3D프린팅) 교육 일정](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179707) | 동대문구 창업지원센터 | K-Startup 사업공고 |
| 2026-11-24 | [2026년 탄소배출권 실무교육 안내](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179699) | 서울기후테크산업지원센터장서 | K-Startup 사업공고 |
| 2026-11-24 | [2026-6회 호남 엔젤리더스포럼 in 전북](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179719) | 한국엔젤투자협회 호남권 엔젤투자허브 | K-Startup 사업공고 |
| 2026-11-24 | [[경과원 X 나이스디앤비] 스타트업 공공시장 진출 실전 특강 - 공공입찰부터 기업·기술평가까지 한번에!](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179793) | 경기도·경기도경제과학진흥원 | K-Startup 사업공고 |
| 2026-11-24 | [대전 팁스타운 26년 제3차 팁스아카데미 : 스타트업의 새로운 기회, 오픈이노베이션](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179836) | 창업진흥원 | K-Startup 사업공고 |
| 2026-11-25 | [창업 초보를 위한 창업 A-Z 교육](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179650) | 하우그로우 원격평생교육원 | K-Startup 사업공고 |
| 2026-11-25 | [용인시산업진흥원 2026년 제5차 창업지원센터 입주기업 모집공고(~11. 25. 수 16:00까지)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179740) | 용인시산업진흥원 | K-Startup 사업공고 |
| 2026-11-25 | [2027년 인천관광기업지원센터 입주기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179738) | 인천관광공사 | K-Startup 사업공고 |
| 2026-11-25 | [구로구 청년창업지원센터 일반 창업교육(하반기: 7회차): 사업계획서 작성 요령](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179790) | 구로구 청년창업지원센터 | K-Startup 사업공고 |
| 2026-11-25 | [제 2회 판다밋업 : AI 반도체 글로벌 파트너십 Innovation Bridge](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179807) | 경기도 4차산업혁명센터 | K-Startup 사업공고 |
| 2026-11-25 | [2026년 IP거래 네트워크(IP-LINK)(원자력·조선·해양수산) 참가기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179787) | 와이앤아처 주식회사 | K-Startup 사업공고 |
| 2026-11-25 | [2026-6회 호남권 엔젤투자 설명회 in 전북 상담부스 참여기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179823) | 한국엔젤투자협회 호남권 엔젤투자허브 | K-Startup 사업공고 |
| 2026-11-26 | [2026년도 키친인큐베이터 개별·공유주방 25기 및 제조주방 13기 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179653) | (재)서울경제진흥원 | K-Startup 사업공고 |
| 2026-11-26 | [(인천 대학 청년 창업펀드 2호) UniVest Scale-up 참여기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179742) | (재)인천테크노파크 | K-Startup 사업공고 |
| 2026-11-26 | [한국공항공사 창업보육센터 입주기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179731) | 한국공항공사 | K-Startup 사업공고 |
| 2026-11-26 | [2026 재도전˙혁신캠퍼스 성과공유회](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179730) | 대전창조경제혁신센터 | K-Startup 사업공고 |
| 2026-11-26 | [2026 여성벤처 글로벌 컨퍼런스](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179743) | (사)한국여성벤처협회 | K-Startup 사업공고 |
| 2026-11-26 | [2026 여성벤처활성화사업 「여성벤처&스타트업 혁신성장 포럼」참여자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179775) | (사)한국여성벤처협회 | K-Startup 사업공고 |
| 2026-11-26 | [[성동구사회적경제지원센터·KT&G상상플래닛 ] 스타트업(소셜벤처) 현장 사례 공유 <&apos;외로움은 사업이 될 수 있을까?&apos;>](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179792) | KT&G 상상플래닛 운영 | K-Startup 사업공고 |

## 스타트업 뉴스

| 날짜 | 제목 | 출처 |
|---|---|---|
| 2026-11-23 | [아스테로모프, AI가 제안한 ‘DNA 나노브릿지’ 세포 실험으로 검증…치료 기술 특허 출원](https://www.venturesquare.net/1130672/) | 벤처스퀘어 |
| 2026-11-23 | [딥브레인AI, 포브스코리아 ‘대한민국 AI 50’ 3년 연속 선정…AI 휴먼 상용화 성과 인정](https://www.venturesquare.net/1130678/) | 벤처스퀘어 |
| 2026-11-23 | [조지메이슨대 한국캠퍼스, 사회문제 담은 디지털아트 6개 작품 선정…대상에 ‘한여름 밤의 꿀’](https://www.venturesquare.net/1130688/) | 벤처스퀘어 |
| 2026-11-23 | [심심이, 24년간 4억5000만 명과 대화한 AI 챗봇…‘평생의 AI 친구’로 진화한다](https://www.venturesquare.net/1130687/) | 벤처스퀘어 |
| 2026-11-23 | [두나무, 전통시장에 AI·블록체인 접목…청년 아이디어 91건 중 4개 팀 선정](https://www.venturesquare.net/1130701/) | 벤처스퀘어 |
| 2026-11-23 | [모두싸인, 공공기관 300곳에 전자서명 공급…이영준 대표 중기부 장관 표창](https://www.venturesquare.net/1130704/) | 벤처스퀘어 |
| 2026-11-23 | [씨엔티테크, 기보벤처캠프 19기 데모데이 개최…잉크플록 등 우수기업 3개사 선정](https://www.venturesquare.net/1130712/) | 벤처스퀘어 |
| 2026-11-23 | [와이즈넛, 공공솔루션마켓서 AI 에이전트 운영 전략 공개…“성능보다 신뢰와 통제가 중요”](https://www.venturesquare.net/1130721/) | 벤처스퀘어 |
| 2026-11-23 | [스노우플레이크, AWS 마켓플레이스 계약 실적 1위…신설 특별상 수상](https://www.venturesquare.net/1130725/) | 벤처스퀘어 |
| 2026-11-23 | [AWS, 구글·깃허브 계정으로 클라우드 가입…AI 코딩 에이전트가 인프라 구축까지](https://www.venturesquare.net/1130726/) | 벤처스퀘어 |
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
