# All-about-Korea-Startup-Information

세종 청년창업 기관 공지 · 정부 지원사업 공고 · 스타트업 뉴스를 **매일 14:00 KST에 자동 수집**하는 저장소.
GitHub Actions가 수집→중복제거→상세저장→아래 대시보드 갱신→텔레그램 브리핑까지 수행한다 (git-scraping — 서버·DB·API 비용 없음).

**완전 규칙 기반**: 소스마다 공식 API/RSS 또는 정규식 파서를 쓴다(LLM 미사용, 고정비 $0). 대신 사이트가 개편되면 파서가 조용히 0건을 낼 수 있어, 같은 소스가 **연속 2회 이상 0건**이면 `data/source_health.json`에 기록하고 다이제스트에 "⚠️ 소스 점검 필요"로 경고한다 — 이게 규칙 기반의 유일한 약점(개편에 안 깨지는 AI 추출 대비)을 메우는 피드백 루프다.

<!-- AUTO:START -->

_자동 갱신: 2026-11-26 (KST)_

## 마감 임박 지원사업

| 마감 | 공고 | 기관 | 출처 |
|---|---|---|---|
| 2026-11-26 | [2026년도 키친인큐베이터 개별·공유주방 25기 및 제조주방 13기 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179653) | (재)서울경제진흥원 | K-Startup 사업공고 |
| 2026-11-26 | [(인천 대학 청년 창업펀드 2호) UniVest Scale-up 참여기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179742) | (재)인천테크노파크 | K-Startup 사업공고 |
| 2026-11-26 | [한국공항공사 창업보육센터 입주기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179731) | 한국공항공사 | K-Startup 사업공고 |
| 2026-11-26 | [2026 재도전˙혁신캠퍼스 성과공유회](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179730) | 대전창조경제혁신센터 | K-Startup 사업공고 |
| 2026-11-26 | [2026 여성벤처 글로벌 컨퍼런스](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179743) | (사)한국여성벤처협회 | K-Startup 사업공고 |
| 2026-11-26 | [2026 여성벤처활성화사업 「여성벤처&스타트업 혁신성장 포럼」참여자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179775) | (사)한국여성벤처협회 | K-Startup 사업공고 |
| 2026-11-26 | [[성동구사회적경제지원센터·KT&G상상플래닛 ] 스타트업(소셜벤처) 현장 사례 공유 <&apos;외로움은 사업이 될 수 있을까?&apos;>](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179792) | KT&G 상상플래닛 운영 | K-Startup 사업공고 |
| 2026-11-26 | [[창업행사] KOBIA와 함께하는 마포 청년 창업 재도전(모두의 창업 Re:Boot)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179802) | 마포청년창업취업지원센터 나루 | K-Startup 사업공고 |
| 2026-11-26 | [「Next OI 기술 커넥트(Pre-meetup)」 참여 스타트업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179832) | (재)대구창조경제혁신센터 | K-Startup 사업공고 |
| 2026-11-26 | [2026 강원권 LIPS 민간운영사 연합 INVESTOR DAY 12월](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179822) | (재)강원창조경제혁신센터 | K-Startup 사업공고 |
| 2026-11-26 | [2026년 여성창업기업 네트워킹 DAY 참여자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179870) | 달구벌여성인력개발센터 | K-Startup 사업공고 |
| 2026-11-26 | [[보도자료 = 기획] 창업기업을 위한 언론 홍보 실전 전략ㆍAI 활용 보도자료 작성 교육](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179882) | 한양대학교 ERICA 산학협력단 | K-Startup 사업공고 |
| 2026-11-27 | [[창업보육센터]K-Tech 창업성장아카데미 교육프로그램 수강생 모집(~11월)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179208) | 한국기술교육대학교 산학협력단 | K-Startup 사업공고 |
| 2026-11-27 | [[무료 AI 역량강화 교육] 생성형 AI 기반 무역 금융 리스크 최적화 과정(선착순 모집)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179631) | (주)글로벌창업연구소 | K-Startup 사업공고 |
| 2026-11-27 | [한국기술교육대학교 오픈이노베이션 프로그램 참여기업 모집 통합 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179662) | 한국기술교육대학교 앵커사업단 | K-Startup 사업공고 |
| 2026-11-27 | [김해시중장년기술창업센터 2026년 하반기 신규 입주(자)기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179714) | (재)김해의생명산업진흥원 | K-Startup 사업공고 |
| 2026-11-27 | [2026년 경기창업혁신공간 북동부권(구리) 신규 입주기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179701) | (재)경기도경제과학진흥원 | K-Startup 사업공고 |
| 2026-11-27 | [예비, 초기 창업자가 반드시 알아야 할 스타트업 마케팅 방법론 - 제11차 DDM 벤처스타트업 아카데미](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179835) | DDM 청년창업센터 유니콘 | K-Startup 사업공고 |
| 2026-11-27 | [[창업] 창업가를 위한 해외 진출 첫 걸음](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179868) | 마포청년창업취업지원센터 나루 | K-Startup 사업공고 |
| 2026-11-27 | [제42회 국제의료기기·병원설비전시회(KIMES 2027) 참가기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179820) | 한국과학기술연구원 서울바이오허브사업단 | K-Startup 사업공고 |

## 스타트업 뉴스

| 날짜 | 제목 | 출처 |
|---|---|---|
| 2026-11-25 | [[VS 현장] “세상을 바꾸는 비즈니스는 질문에서 시작된다”…현대차 정몽구 재단이 키우는 임팩트 기업가](https://www.venturesquare.net/1131471/) | 벤처스퀘어 |
| 2026-11-26 | [엑스엘에이트, AI 통번역의 전문성 높인다…‘이벤트캣’ 헬스케어 행사 6곳 연속 공급](https://www.venturesquare.net/1131650/) | 벤처스퀘어 |
| 2026-11-26 | [인핸스, 기업 업무 자동화 기술 국방으로 확장…국방정보본부 AI 민간자문기업 위촉](https://www.venturesquare.net/1131652/) | 벤처스퀘어 |
| 2026-11-26 | [액션파워 다글로, 회의 기록을 조직의 업무 자산으로…‘다글로챗’ 출시](https://www.venturesquare.net/1131659/) | 벤처스퀘어 |
| 2026-11-26 | [엘리스스쿨, 충남교육청에 생성형 AI 공급…교원 행정업무부터 학생 자기주도학습까지](https://www.venturesquare.net/1131666/) | 벤처스퀘어 |
| 2026-11-26 | [와디즈, 펀딩의 경쟁력은 메이커와 서포터의 소통…커뮤니티 운영 정책 개편](https://www.venturesquare.net/1131675/) | 벤처스퀘어 |
| 2026-11-26 | [젠엑시스, 투자유치만큼 중요한 창업가의 회복력…기보벤처캠프서 새로운 액셀러레이팅 시도](https://www.venturesquare.net/1131687/) | 벤처스퀘어 |
| 2026-11-26 | [라이클, 자전거 브랜드 탐색부터 가까운 매장 연결까지…온·오프라인 커머스 접점 강화](https://www.venturesquare.net/1131701/) | 벤처스퀘어 |
| 2026-11-26 | [옴디아, 아프리카 스마트폰 시장 40% 급감…저가폰 수요 위축 속 삼성 점유율 23%로 상승](https://www.venturesquare.net/1131704/) | 벤처스퀘어 |
| 2026-11-26 | [사운드리퍼블리카, AI 음악 ‘머무르’ 신곡 독점 유통…음원 권리 보호에서 글로벌 배급으로](https://www.venturesquare.net/1131710/) | 벤처스퀘어 |
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
