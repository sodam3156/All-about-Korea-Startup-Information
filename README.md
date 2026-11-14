# All-about-Korea-Startup-Information

세종 청년창업 기관 공지 · 정부 지원사업 공고 · 스타트업 뉴스를 **매일 14:00 KST에 자동 수집**하는 저장소.
GitHub Actions가 수집→중복제거→상세저장→아래 대시보드 갱신→텔레그램 브리핑까지 수행한다 (git-scraping — 서버·DB·API 비용 없음).

**완전 규칙 기반**: 소스마다 공식 API/RSS 또는 정규식 파서를 쓴다(LLM 미사용, 고정비 $0). 대신 사이트가 개편되면 파서가 조용히 0건을 낼 수 있어, 같은 소스가 **연속 2회 이상 0건**이면 `data/source_health.json`에 기록하고 다이제스트에 "⚠️ 소스 점검 필요"로 경고한다 — 이게 규칙 기반의 유일한 약점(개편에 안 깨지는 AI 추출 대비)을 메우는 피드백 루프다.

<!-- AUTO:START -->

_자동 갱신: 2026-11-14 (KST)_

## 마감 임박 지원사업

| 마감 | 공고 | 기관 | 출처 |
|---|---|---|---|
| 2026-11-15 | [[국비지원] AI 기반 서비스 개발·사업화 1인 창업가 캠프 8기 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179430) | 넥스트러너스 주식회사 | K-Startup 사업공고 |
| 2026-11-15 | [KETI 파트너쉽 대덕특구 연구소기업](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179528) | 연구개발특구진흥재단 | K-Startup 사업공고 |
| 2026-11-15 | [[ZUZU X 삼성화재 집중검토] 헬스케어·모빌리티·AI·홈/라이프 Seed·Pre-A 투자 검토 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179658) | (주) 코드박스 Kodebox | K-Startup 사업공고 |
| 2026-11-15 | [26년 11월 스타트업 언론 홍보 지원사업 참가사 모집 공고(1차)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179644) | 스타트업 데일리 | K-Startup 사업공고 |
| 2026-11-15 | [2026년 특허출원·등록 비용 바우처 지원사업 16차(하반기 9차)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179641) | (사)한국중소기업발전협회 | K-Startup 사업공고 |
| 2026-11-15 | [[킹고스프링] KINGO SPRINGBOARD PROGRAM 9기](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179639) | 킹고스프링 | K-Startup 사업공고 |
| 2026-11-15 | [2026년 스타트업 법률지원사업 제주특별자치도 법률상담회 참여기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179762) | 창업진흥원 원스톱지원실 | K-Startup 사업공고 |
| 2026-11-15 | [[창업중심대학]2026 대학연합 지역관광 창업경진대회(K-TOURISM STARTUP CHALLENGE)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179781) | 한양대 창업지원단 | K-Startup 사업공고 |
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
| 2026-11-17 | [2026 글로벌 진출 - 글로벌 진출과 협력 네트워크 확장 전략](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179555) | 서울창업허브 창동 | K-Startup 사업공고 |
| 2026-11-17 | [2026년 K-바이오랩허브 멤버십 기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179654) | 인천창조경제혁신센터 | K-Startup 사업공고 |

## 스타트업 뉴스

| 날짜 | 제목 | 출처 |
|---|---|---|
| 2026-11-13 | [[우준호의 협상의 기술] 4,000억을 부르고 다닌 1년…희망 매각가를 낮추지 않은 이유](https://www.venturesquare.net/1128573/) | 벤처스퀘어 |
| 2026-11-14 | [[Deep Tech Insight] 보이지 않는 금융시장을 검증하는 기술…젠OTC는 수학적 모델을 어떻게 서비스로 만들었나](https://www.venturesquare.net/1128593/) | 벤처스퀘어 |
| 2026-11-14 | [[VS 기획] AI 안경은 일상을 바꾸는데, 시험장에선 부정행위 도구?…기술과 신뢰 사이의 딜레마](https://www.venturesquare.net/1128607/) | 벤처스퀘어 |
| 2026-11-12 | [셀바스AI·메디아나, 인텔 AI 협력망 합류…기업 업무 자동화부터 병원 물류까지 확장](https://www.venturesquare.net/1128264/) | 벤처스퀘어 |
| 2026-11-12 | [소울아트, CES 2027 최고혁신상 수상…착용 장비 없는 모션 트래커로 글로벌 시장 공략](https://www.venturesquare.net/1128267/) | 벤처스퀘어 |
| 2026-11-12 | [두나무 업비트, 전국 14개 대학서 디지털자산 교육…청년 3200명 만났다](https://www.venturesquare.net/1128280/) | 벤처스퀘어 |
| 2026-11-12 | [사람을 더 모으는 대신 더 잘 모셨다…컬리뷰티페스타 2026의 선택](https://www.venturesquare.net/1128301/) | 벤처스퀘어 |
| 2026-11-12 | [[VS 기획] ‘AI와 대화하는 직원, 복도 누비는 로봇’…사무실의 기준이 달라진다](https://www.venturesquare.net/1125736/) | 벤처스퀘어 |
| 2026-11-12 | [스팩스페이스, 사진·영상으로 움직이는 장면까지 3D 복원…‘위드비전’ 공개](https://www.venturesquare.net/1128291/) | 벤처스퀘어 |
| 2026-11-12 | [[부산에서 발굴한 초기 스타트업 ④] 김세윤 컴퍼지트솔루션즈 대표 “버려진 페트병이 자동차와 항공기의 소재가 된다면”](https://www.venturesquare.net/1126980/) | 벤처스퀘어 |
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
