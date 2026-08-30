# All-about-Korea-Startup-Information

세종 청년창업 기관 공지 · 정부 지원사업 공고 · 스타트업 뉴스를 **매일 14:00 KST에 자동 수집**하는 저장소.
GitHub Actions가 수집→중복제거→상세저장→아래 대시보드 갱신→텔레그램 브리핑까지 수행한다 (git-scraping — 서버·DB·API 비용 없음).

**완전 규칙 기반**: 소스마다 공식 API/RSS 또는 정규식 파서를 쓴다(LLM 미사용, 고정비 $0). 대신 사이트가 개편되면 파서가 조용히 0건을 낼 수 있어, 같은 소스가 **연속 2회 이상 0건**이면 `data/source_health.json`에 기록하고 다이제스트에 "⚠️ 소스 점검 필요"로 경고한다 — 이게 규칙 기반의 유일한 약점(개편에 안 깨지는 AI 추출 대비)을 메우는 피드백 루프다.

<!-- AUTO:START -->

_자동 갱신: 2026-08-30 (KST)_

## 마감 임박 지원사업

| 마감 | 공고 | 기관 | 출처 |
|---|---|---|---|
| 2026-08-30 | [2026년 2nd S.Stage 개최 안내](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178721) | 서울창조경제혁신센터 | K-Startup 사업공고 |
| 2026-08-30 | [2026 창업오디션, 고양IR데이 참가기업 추가모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178810) | 고양시장 | K-Startup 사업공고 |
| 2026-08-30 | [2026년 판로확대 지원 참여 소상공인 모집(셀러허브)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178871) | 중소상공인희망재단 | K-Startup 사업공고 |
| 2026-08-30 | [[제2서울핀테크랩] 서울 핀테크 위크 2026 제2서울핀테크랩 데모데이 with 네이버클라우드 참가기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178858) | 제2서울핀테크랩 | K-Startup 사업공고 |
| 2026-08-31 | [2026 벤처확인 인증준비기업 맞춤형 무료 진단 지원사업](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178745) | (주)엠비즈플래닛 산하 혁신기술경영인증지원센터 | K-Startup 사업공고 |
| 2026-08-31 | [[국토교통부 x 물류산업진흥재단] 2026 물류상생 Meet-up 행사 기술기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178731) | 물류산업진흥재단 | K-Startup 사업공고 |
| 2026-08-31 | [2026 대덕특구 딥테크 혁신성장 플랫폼(전략기술 발굴 및 매칭) (8/1 ~ 8/31)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178719) | 연구개발특구진흥재단 | K-Startup 사업공고 |
| 2026-08-31 | [[KEA] IoT제품 개발 지원 및 빅데이터 분석 과제기획 수요기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178718) | 한국전자정보통신산업진흥회 | K-Startup 사업공고 |
| 2026-08-31 | [(기간연장)[창업점검] 2026년 체육인 직업안정사업(창업열매) 참여자 추가 모집_(~8.31마감시)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178693) | 국민체육진흥공단 | K-Startup 사업공고 |
| 2026-08-31 | [[무료 AI 역량강화 교육] 생성형 AI기반, 글로벌 마케팅 자동화 및 현지화 에이전트 구축과](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178672) | (주)글로벌창업연구소 | K-Startup 사업공고 |
| 2026-08-31 | [2026 Nexus Connect 오픈이노베이션 밋업 데이](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178795) | (재)충남창조경제혁신센터 | K-Startup 사업공고 |
| 2026-08-31 | [충북대학교 『글로벌(G)테크벤처센터(BI) 』 입주기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178781) | 충북대학교 글로벌(G)테크벤처센터 | K-Startup 사업공고 |
| 2026-08-31 | [2026 협성대학교 창업보육센터 하반기 신규 입주기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178771) | 협성대학교 창업보육센터 | K-Startup 사업공고 |
| 2026-08-31 | [해외진출 기업 대상 AI 통역 서비스 「아네스노트」 이용권 지원](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178765) | 주식회사 팀제로코드 | K-Startup 사업공고 |
| 2026-08-31 | [2026년 스타 IR 데모데이 참여기업 모집공고(4차)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178740) | 스타에셋파트너스 주식회사 | K-Startup 사업공고 |
| 2026-08-31 | [제3회 K-ROBOTICS Startup CUP 참가팀 모집(~8/31 마감)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178841) | KAIST | K-Startup 사업공고 |
| 2026-08-31 | [「민관협력 오픈이노베이션 지원」 '공공데이터 활용 지원' 창업기업 제안 협업 과제(Bottom-Up) 모집공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178875) | 중소벤처기업부장관 | K-Startup 사업공고 |
| 2026-08-31 | [「민관협력 오픈이노베이션 지원」'공공데이터 활용 지원' 공공기관 제안 협업 과제(Top-Down) 모집공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178873) | 중소벤처기업 | K-Startup 사업공고 |
| 2026-08-31 | [2026년 여성CEO 비즈니스 아카데미 호남권역 시즌 2](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178894) | 한국여성경제인협회 | K-Startup 사업공고 |
| 2026-08-31 | [2026년 특허출원·등록 비용 바우처 지원사업 11차(하반기 4차)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178870) | (사)한국중소기업발전협회 | K-Startup 사업공고 |

## 스타트업 뉴스

| 날짜 | 제목 | 출처 |
|---|---|---|
| 2026-08-29 | [좋은 제안은 왜 결정으로 이어지지 않을까…OPEN UP, 강자를 움직이는 협상 해부](https://www.venturesquare.net/1109504/) | 벤처스퀘어 |
| 2026-08-29 | [“외국인 정착의 든든한 둥지 될 것”…AI 정착 케어 플랫폼 ‘네스티아’ 미노 마토 루 대표](https://www.venturesquare.net/1109487/) | 벤처스퀘어 |
| 2026-08-30 | [‘기후변호사’에서 중기부 장관 후보자로…스타트업 업계가 이소영에 거는 기대](https://www.venturesquare.net/1109519/) | 벤처스퀘어 |
| 2026-08-29 | [‘휴대폰 대리점서 스타트업으로’, 김용래 포피플 대표가 조직을 다시 짠 방법](https://www.venturesquare.net/1086448/) | 벤처스퀘어 |
| 2026-08-27 | [닭갈비집 줄자로 재고 3D로 바꾼다…춘천기계공고 학생들 ‘가상 리모델링’](https://www.venturesquare.net/1109182/) | 벤처스퀘어 |
| 2026-08-27 | [간판 바꾸고 매출도 움직였다…코카-콜라, 신흥시장 협업으로 에피 최고상 2연패](https://www.venturesquare.net/1109186/) | 벤처스퀘어 |
| 2026-08-27 | [AI가 고르고 스테이블코인이 결제…두나무·비자, 미래 결제 모델 찾는다](https://www.venturesquare.net/1109193/) | 벤처스퀘어 |
| 2026-08-27 | [장애 원인 찾는 데 4시간→30분…오케스트로, ‘고객 AX’ 앞서 내부부터 바꿨다](https://www.venturesquare.net/1109200/) | 벤처스퀘어 |
| 2026-08-28 | [“이 도면, 법규에 맞나” AI가 계약서까지 대조…서치독, 팁스 선정](https://www.venturesquare.net/1109223/) | 벤처스퀘어 |
| 2026-08-28 | [투자한 기술, 약 100명이 직접 써봤다…한국투자액셀러레이터의 ‘피지컬 AI 밸류업’](https://www.venturesquare.net/1109230/) | 벤처스퀘어 |
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
