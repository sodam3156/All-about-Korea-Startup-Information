# All-about-Korea-Startup-Information

세종 청년창업 기관 공지 · 정부 지원사업 공고 · 스타트업 뉴스를 **매일 14:00 KST에 자동 수집**하는 저장소.
GitHub Actions가 수집→중복제거→상세저장→아래 대시보드 갱신→텔레그램 브리핑까지 수행한다 (git-scraping — 서버·DB·API 비용 없음).

**완전 규칙 기반**: 소스마다 공식 API/RSS 또는 정규식 파서를 쓴다(LLM 미사용, 고정비 $0). 대신 사이트가 개편되면 파서가 조용히 0건을 낼 수 있어, 같은 소스가 **연속 2회 이상 0건**이면 `data/source_health.json`에 기록하고 다이제스트에 "⚠️ 소스 점검 필요"로 경고한다 — 이게 규칙 기반의 유일한 약점(개편에 안 깨지는 AI 추출 대비)을 메우는 피드백 루프다.

<!-- AUTO:START -->

_자동 갱신: 2026-08-12 (KST)_

## 마감 임박 지원사업

| 마감 | 공고 | 기관 | 출처 |
|---|---|---|---|
| 2026-08-12 | [2026 산업단지 오픈이노베이션프로그램 KICXUP 챌린지 & 로컬 스타트업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178746) | 한국산업단지공단 | K-Startup 사업공고 |
| 2026-08-12 | [청년 창업의 꿈, 『성동청년 창업이룸센터』 입주자 모집 공고【9차】](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178724) | 서울특별시 성동구청장 | K-Startup 사업공고 |
| 2026-08-12 | [2026년 여성CEO 비즈니스 아카데미 경상권역 시즌 1](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178671) | 한국여성경제인협회 | K-Startup 사업공고 |
| 2026-08-12 | [2026년도 방산 특화 창업중심대학 창업기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178662) | 중소벤처기업부 장관 | K-Startup 사업공고 |
| 2026-08-12 | [2026년 창업진흥원 대전 팁스타운 일본 파트너 초청 상담회 참가기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178839) | 창업진흥원장 | K-Startup 사업공고 |
| 2026-08-12 | [?[무료] 정책자금·TIPS 심사를 좌우하는 재무제표 결산 포인트?](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178840) | 하임벤처투자 | K-Startup 사업공고 |
| 2026-08-13 | [2026년 8월 동네창업학교 교육생 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178742) | 충남신용보증재단 | K-Startup 사업공고 |
| 2026-08-13 | [앤틀러코리아 ANTLER FORGE 소개 웨비나 | 팀 당 6억원 규모 투자](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178725) | 앤틀러코리아 | K-Startup 사업공고 |
| 2026-08-13 | [[대전관광공사] 2026 대전세종 관광기업 네트워킹 데이 3회차 참여기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178703) | 대전관광공사 | K-Startup 사업공고 |
| 2026-08-13 | [2026 시흥시 스타트업 통합 IR DAY](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178680) | (주)엔슬파트너스 | K-Startup 사업공고 |
| 2026-08-13 | [[2026년 G-Space 창업기업 홍보 콘텐츠 제작 지원사업] 창업기업 모집연장공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178667) | (재)경남창조경제혁신센터 대표이사 | K-Startup 사업공고 |
| 2026-08-13 | [(재)여성기업종합지원센터 인천센터 2026년 제1차 입주기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178665) | (재)여성기업종합지원센터 인천센터 | K-Startup 사업공고 |
| 2026-08-13 | [여성 1인 창조기업 지원센터 신규 입주기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178643) | (사)한국여성벤처협회 여성특화 1인 창조기업지원 센터장 | K-Startup 사업공고 |
| 2026-08-13 | [2026년 재도전성공패키지 충청·강원권 커뮤니티 데이](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178814) | 주식회사 알파브라더스 | K-Startup 사업공고 |
| 2026-08-14 | [[2026-063호] 2026년 정보보호 기업육성(사업화) 지원사업 모집공고](https://sjtp.or.kr/bbs/board.php?bo_table=business01&wr_id=1989) | (재)세종테크노파크 | 세종테크노파크 사업공고 |
| 2026-08-14 | [[2026-064호] 세종 지역특화산업 기업 정보보호 신규 비즈니스 모델 전략 수립 지원기업 모집공고](https://sjtp.or.kr/bbs/board.php?bo_table=business01&wr_id=1990) | (재)세종테크노파크 | 세종테크노파크 사업공고 |
| 2026-08-14 | [연구개발특구진흥재단 X HS효성/효성 2026년 오픈이노베이션 배치프로그램 참가기업 모집공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178764) | 주식회사 베타랩 | K-Startup 사업공고 |
| 2026-08-14 | [「2026 청년창업 지역정착 지원사업」 신규참여자 3차 추가모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178747) | 경상북도경제진흥원 | K-Startup 사업공고 |
| 2026-08-14 | [2026년 『G-Bio Funding Lab』 경기 바이오스타트업 투자유치 역량강화 참가기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178744) | (재)경기도경제과학진흥원 | K-Startup 사업공고 |
| 2026-08-14 | [2026년 국토교통 중소벤처기업 투자유치설명회 참여기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178729) | 국토교통과학기술진흥원 | K-Startup 사업공고 |

## 스타트업 뉴스

| 날짜 | 제목 | 출처 |
|---|---|---|
| 2026-08-11 | [설계에서 검증까지 AI가 맡는다…지멘스 EDA의 ‘AI-Native Design’](https://www.venturesquare.net/1105293/) | 벤처스퀘어 |
| 2026-08-11 | [K-브랜드 틱톡샵, 입점부터 크리에이터 매칭까지…바이버스 공식 파트너 선정](https://www.venturesquare.net/1105306/) | 벤처스퀘어 |
| 2026-08-11 | [매출 23% 늘고 영업손실 31% 줄었다…루닛, 상반기 458억원](https://www.venturesquare.net/1105309/) | 벤처스퀘어 |
| 2026-08-11 | [엑셀은 버겁고 SI는 비싸다…바틀, 맞춤 ERP 990만원 정찰제 제시](https://www.venturesquare.net/1105316/) | 벤처스퀘어 |
| 2026-08-11 | [세포주 분석·NGS, 싱가포르 한곳에서…머크, 아태 바이오안전성 시험 강화](https://www.venturesquare.net/1105328/) | 벤처스퀘어 |
| 2026-08-11 | [제주 당일배송 데이터로 수요·경로 예측…잇뉴, 시드투자 1억원 유치](https://www.venturesquare.net/1105335/) | 벤처스퀘어 |
| 2026-08-11 | [전국 매장서 쌓은 DX 경험, LA로…디토닉 북미 리테일 첫발](https://www.venturesquare.net/1105338/) | 벤처스퀘어 |
| 2026-08-11 | [가려움증·피부투과 기술, 일본서 PoC 기회…서울바이오허브 2개사 모집](https://www.venturesquare.net/1105345/) | 벤처스퀘어 |
| 2026-08-11 | [차단기·정산기 없는 소형 주차장…케이지페이먼츠, AI 활용지원 선정](https://www.venturesquare.net/1105355/) | 벤처스퀘어 |
| 2026-08-11 | [700만명이 2억9000만번 탔다…지쿠, 창립 9년 이동 데이터 공개](https://www.venturesquare.net/1105362/) | 벤처스퀘어 |
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
