# All-about-Korea-Startup-Information

세종 청년창업 기관 공지 · 정부 지원사업 공고 · 스타트업 뉴스를 **매일 14:00 KST에 자동 수집**하는 저장소.
GitHub Actions가 수집→중복제거→상세저장→아래 대시보드 갱신→텔레그램 브리핑까지 수행한다 (git-scraping — 서버·DB·API 비용 없음).

**완전 규칙 기반**: 소스마다 공식 API/RSS 또는 정규식 파서를 쓴다(LLM 미사용, 고정비 $0). 대신 사이트가 개편되면 파서가 조용히 0건을 낼 수 있어, 같은 소스가 **연속 2회 이상 0건**이면 `data/source_health.json`에 기록하고 다이제스트에 "⚠️ 소스 점검 필요"로 경고한다 — 이게 규칙 기반의 유일한 약점(개편에 안 깨지는 AI 추출 대비)을 메우는 피드백 루프다.

<!-- AUTO:START -->

_자동 갱신: 2026-08-14 (KST)_

## 마감 임박 지원사업

| 마감 | 공고 | 기관 | 출처 |
|---|---|---|---|
| 2026-08-14 | [[2026-063호] 2026년 정보보호 기업육성(사업화) 지원사업 모집공고](https://sjtp.or.kr/bbs/board.php?bo_table=business01&wr_id=1989) | (재)세종테크노파크 | 세종테크노파크 사업공고 |
| 2026-08-14 | [[2026-064호] 세종 지역특화산업 기업 정보보호 신규 비즈니스 모델 전략 수립 지원기업 모집공고](https://sjtp.or.kr/bbs/board.php?bo_table=business01&wr_id=1990) | (재)세종테크노파크 | 세종테크노파크 사업공고 |
| 2026-08-14 | [연구개발특구진흥재단 X HS효성/효성 2026년 오픈이노베이션 배치프로그램 참가기업 모집공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178764) | 주식회사 베타랩 | K-Startup 사업공고 |
| 2026-08-14 | [「2026 청년창업 지역정착 지원사업」 신규참여자 3차 추가모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178747) | 경상북도경제진흥원 | K-Startup 사업공고 |
| 2026-08-14 | [2026년 『G-Bio Funding Lab』 경기 바이오스타트업 투자유치 역량강화 참가기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178744) | (재)경기도경제과학진흥원 | K-Startup 사업공고 |
| 2026-08-14 | [2026년 국토교통 중소벤처기업 투자유치설명회 참여기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178729) | 국토교통과학기술진흥원 | K-Startup 사업공고 |
| 2026-08-14 | [『춘천시 1인 창조기업 지원센터 입주기업 모집 』공고 (9월)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178720) | 공고 기업(기관)명 : 춘천시1인창조기업지원센터 | K-Startup 사업공고 |
| 2026-08-14 | [2026년 특허출원·등록 비용 바우처 지원사업 10차(하반기 3차)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178716) | (사)한국중소기업발전협회 | K-Startup 사업공고 |
| 2026-08-14 | [기술창업 성장패키지 지원 참여기업 모집공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178684) | (재)광주테크노파크 | K-Startup 사업공고 |
| 2026-08-14 | [2026년 제1회 테크플러스 스테이지 입주기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178683) | (재)광주테크노파크 | K-Startup 사업공고 |
| 2026-08-14 | [[투자 및 TIPS 추천] 한림대학교 Station C 연계 창업기업 투자·육성 지원 프로그램 참가 안내](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178682) | 한국바이오투자파트너스 | K-Startup 사업공고 |
| 2026-08-14 | [2026년 창업 준비 아카데미 [원석 발굴 창업캠프 1차] 참가자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178808) | 광운대학교 NCI창업패키지사업단 | K-Startup 사업공고 |
| 2026-08-14 | [2026년 서울지식재산센터 IP디딤돌 IP창업존 32기 교육생 모집(2026년 1차)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178793) | 재단법인 서울경제진흥원 | K-Startup 사업공고 |
| 2026-08-14 | [로보어드바이저(RA) 신규 알고리즘 발굴 사업](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178787) | 키움증권 | K-Startup 사업공고 |
| 2026-08-14 | [충북대학교 『글로벌(G)테크벤처센터』연구소기업 참여희망 기업 모집 안내](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178777) | 충북대학교 글로벌(G)테크벤처센터 | K-Startup 사업공고 |
| 2026-08-14 | [하반기「스타트업 점프업 스쿨」 기술창업교육 참여기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178761) | 성남산업진흥원 | K-Startup 사업공고 |
| 2026-08-14 | [(재)여성기업종합지원센터 제주센터 제2차 입주기업 모집 연장 공고(~8/14)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178832) | (재)여성기업종합지원센터 제주센 | K-Startup 사업공고 |
| 2026-08-16 | [[혁신창업캠프]청년 창업자를 위한 창업 인사이트 캠프](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178752) | 관악구청 | K-Startup 사업공고 |
| 2026-08-16 | [26년 8월 스타트업 언론 홍보 지원사업 참가사 모집 공고(1차)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178759) | 스타트업 데일리 | K-Startup 사업공고 |
| 2026-08-16 | [2026년 AWS X AI 실무 프로젝트 아카데미 교육생 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178842) | 인천대학교 창업지원단 | K-Startup 사업공고 |

## 스타트업 뉴스

| 날짜 | 제목 | 출처 |
|---|---|---|
| 2026-08-13 | [투자받고 더 막막한 6~18개월…KAIST, 바이오벤처 ‘성장 공백’ 메운다](https://www.venturesquare.net/1105997/) | 벤처스퀘어 |
| 2026-08-13 | [AI가 먼저 만들고 사람은 검수…스팩스페이스, 생산성 6.5배 성과로 ‘서비스 AI 리더상’ 수상](https://www.venturesquare.net/1106008/) | 벤처스퀘어 |
| 2026-08-13 | [전세·월세 다음은 ‘단기임대’…삼삼엠투가 읽은 주거의 변화](https://www.venturesquare.net/1106011/) | 벤처스퀘어 |
| 2026-08-13 | [상반기 877억원 새 기록…디케이앤디, 합성피혁 다음은 ‘로봇 스킨’](https://www.venturesquare.net/1106021/) | 벤처스퀘어 |
| 2026-08-13 | [“스타트업 성장의 병목은 어디에 있을까”…스케일업스쿼드 박승표 대표가 300개 프로젝트에서 찾은 답](https://www.venturesquare.net/1100238/) | 벤처스퀘어 |
| 2026-08-13 | [연기금·기업 자금 1조원 벤처펀드로…‘LP성장펀드’가 출범한다](https://www.venturesquare.net/1106039/) | 벤처스퀘어 |
| 2026-08-13 | [진주 스타트업 10곳, 투자자 앞에 선다…IR부터 후속 상담까지 잇는다](https://www.venturesquare.net/1106045/) | 벤처스퀘어 |
| 2026-08-13 | [투자 뒤 사업까지 함께 만든다…그랜드벤처스, 증자 마치고 2기 투자 나선다](https://www.venturesquare.net/1106048/) | 벤처스퀘어 |
| 2026-08-13 | [입점부터 도쿄 팝업·금융까지 묶는다…K뷰티 8곳의 일본 데뷔를 돕는다](https://www.venturesquare.net/1106051/) | 벤처스퀘어 |
| 2026-08-13 | [AI는 어떤 브랜드를 답으로 고를까…박세용 대표, ‘브랜드, AI의 언어로 말하라’ 출간](https://www.venturesquare.net/1106082/) | 벤처스퀘어 |
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
