# All-about-Korea-Startup-Information

세종 청년창업 기관 공지 · 정부 지원사업 공고 · 스타트업 뉴스를 **매일 14:00 KST에 자동 수집**하는 저장소.
GitHub Actions가 수집→중복제거→상세저장→아래 대시보드 갱신→텔레그램 브리핑까지 수행한다 (git-scraping — 서버·DB·API 비용 없음).

**완전 규칙 기반**: 소스마다 공식 API/RSS 또는 정규식 파서를 쓴다(LLM 미사용, 고정비 $0). 대신 사이트가 개편되면 파서가 조용히 0건을 낼 수 있어, 같은 소스가 **연속 2회 이상 0건**이면 `data/source_health.json`에 기록하고 다이제스트에 "⚠️ 소스 점검 필요"로 경고한다 — 이게 규칙 기반의 유일한 약점(개편에 안 깨지는 AI 추출 대비)을 메우는 피드백 루프다.

<!-- AUTO:START -->

_자동 갱신: 2026-10-21 (KST)_

## 마감 임박 지원사업

| 마감 | 공고 | 기관 | 출처 |
|---|---|---|---|
| 2026-10-21 | [파주청년창업지원센터 하반기 청년 창업아카데미 참여기업/팀 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179318) | 파주시, (재)경기테크노파크 | K-Startup 사업공고 |
| 2026-10-21 | [[서초창업스테이션] 서리풀 소상공인 창업 클리닉(10월) - 소상공인 1:1 컨설팅](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179370) | 서초창업스테이션 | K-Startup 사업공고 |
| 2026-10-21 | [2026년 제3차 I-PLEX광주 입주기업 모집공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179442) | (재)광주테크노파크 | K-Startup 사업공고 |
| 2026-10-21 | [구로구 청년창업지원센터 일반 창업교육(하반기: 5회차): 투자를 위한 비즈니스 모델 수립 전략](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179457) | 구로구 청년창업지원센터 | K-Startup 사업공고 |
| 2026-10-21 | [바이오/헬스케어 기업들을 위한 「2026 혁신신약살롱 마곡」 참여 안내](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179492) | (재)서울경제진흥원 | K-Startup 사업공고 |
| 2026-10-21 | [2026 충남창업마루나비 하반기 입주기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179524) | 충남창조경제혁신센터 | K-Startup 사업공고 |
| 2026-10-21 | [충북테크노파크 차세대에너지 스타트업 DEMO DAY](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179537) | 주식회사 내비온파트너스 | K-Startup 사업공고 |
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

## 스타트업 뉴스

| 날짜 | 제목 | 출처 |
|---|---|---|
| 2026-10-20 | [샌디플로어, 중기부 팁스 선정…AI 기반 게임 개발·배포 자동화 기술 개발](https://www.venturesquare.net/1121539/) | 벤처스퀘어 |
| 2026-10-20 | [NC AI, ‘바르코 3D·사운드’ 첫 달 구독료 50% 할인…AI 콘텐츠 제작 지원](https://www.venturesquare.net/1121533/) | 벤처스퀘어 |
| 2026-10-20 | [핀다, 보험 퍼미션 기업 더열심히와 협력…금융 플랫폼 기반 보험 고객 발굴 확대](https://www.venturesquare.net/1121547/) | 벤처스퀘어 |
| 2026-10-20 | [에코마케팅, 틱톡 ‘프리미어 에이전시’ 선정…AI 기반 글로벌 광고·커머스 사업 강화](https://www.venturesquare.net/1121554/) | 벤처스퀘어 |
| 2026-10-20 | [노이즈앤피치, ‘창창프로젝트’ 크리에이터 컨설팅 완료…AI 데이터 분석으로 성장 전략 제시](https://www.venturesquare.net/1121557/) | 벤처스퀘어 |
| 2026-10-20 | [그립컴퍼니, 카카오톡 라이브 방송 알림 ‘방송톡’ 출시…크리에이터 매출·시청자 유입 지원](https://www.venturesquare.net/1121568/) | 벤처스퀘어 |
| 2026-10-20 | [메디웨이브, 카카오톡 기반 병원 서류 발급·환자 관리 솔루션 ‘메디챗’ 100개 병·의원 도입](https://www.venturesquare.net/1121576/) | 벤처스퀘어 |
| 2026-10-20 | [“AI가 일하기 시작했다, 기업은 무엇이 달라졌나”…씽킹AI 서밋 2026, AI 에이전트의 실전 성적표](https://www.venturesquare.net/1121590/) | 벤처스퀘어 |
| 2026-10-20 | [릴리스AI 오현수 대표, 130만 명이 선택한 AI를 다시 만든 이유…글로벌 겨냥 ‘리드레이’ 26일 출시](https://www.venturesquare.net/1121220/) | 벤처스퀘어 |
| 2026-10-20 | [직방, 스마트홈 AI 브랜드 ‘소마’ 출범…자녀 귀가 알리는 도어록 ‘소마 케어 P1’ 출시](https://www.venturesquare.net/1121611/) | 벤처스퀘어 |
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
