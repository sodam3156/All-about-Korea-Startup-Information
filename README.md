# All-about-Korea-Startup-Information

세종 청년창업 기관 공지 · 정부 지원사업 공고 · 스타트업 뉴스를 **매일 14:00 KST에 자동 수집**하는 저장소.
GitHub Actions가 수집→중복제거→상세저장→아래 대시보드 갱신→텔레그램 브리핑까지 수행한다 (git-scraping — 서버·DB·API 비용 없음).

**완전 규칙 기반**: 소스마다 공식 API/RSS 또는 정규식 파서를 쓴다(LLM 미사용, 고정비 $0). 대신 사이트가 개편되면 파서가 조용히 0건을 낼 수 있어, 같은 소스가 **연속 2회 이상 0건**이면 `data/source_health.json`에 기록하고 다이제스트에 "⚠️ 소스 점검 필요"로 경고한다 — 이게 규칙 기반의 유일한 약점(개편에 안 깨지는 AI 추출 대비)을 메우는 피드백 루프다.

<!-- AUTO:START -->

_자동 갱신: 2026-10-14 (KST)_

## 마감 임박 지원사업

| 마감 | 공고 | 기관 | 출처 |
|---|---|---|---|
| 2026-10-14 | [2026 디캠프 배치 9기 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179094) | 재단법인 은행권청년창업재단 | K-Startup 사업공고 |
| 2026-10-14 | [2026 글로벌 스타트업 서밋 (일본2차) 세미나&밋업 참여기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179221) | 인천창조경제혁신센터 대표이사 | K-Startup 사업공고 |
| 2026-10-14 | [[3D-FAB] 2026년 3D프린팅 네트워킹데이(창업 선배와의 만남) 참가자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179355) | 3D프린팅혁신성장센터 | K-Startup 사업공고 |
| 2026-10-14 | [해운대 청년채움공간(청년창업지원시설) 위탁운영기관 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179412) | 부산광역시 해운대구청장 | K-Startup 사업공고 |
| 2026-10-14 | [2026년 경기 스타트업 아카데미 딥테크 교육 참여자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179404) | 경기도·경기도경제과학진흥원 | K-Startup 사업공고 |
| 2026-10-14 | [2026년 제2차 테크플러스 스테이지 입주기업 모집 연장 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179391) | (재)광주테크노파크 | K-Startup 사업공고 |
| 2026-10-14 | [2026년 경기 스타트업 아카데미 딥테크 세미나 참여자 모집 / Future AI Technology - AI 메모리 반도체의 발전과 미래](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179384) | 경기도·경기도경제과학진흥원 | K-Startup 사업공고 |
| 2026-10-14 | [2026년도 해양수산 투자박람회](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179415) | 한국벤처캐피탈협회 | K-Startup 사업공고 |
| 2026-10-14 | [[대전창조경제혁신센터] 모두의창업 대전지역 오디션 &apos;3라운드 진출 도전자 공개 오디션&apos; 관람객 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179481) | 대전창조경제혁신센터 | K-Startup 사업공고 |
| 2026-10-14 | [「2026 슈퍼:콘 엑셀러레이팅」 지원사업 참여기업 모집공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179485) | 대전정보문화산업진흥원 | K-Startup 사업공고 |
| 2026-10-15 | [2026년 하반기 화성시 벤처인증 비용 지원사업](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178737) | (재)화성산업진흥원 | K-Startup 사업공고 |
| 2026-10-15 | [26년 10월 스타트업 언론 홍보 지원사업 참가사 모집 공고(1차)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179361) | 스타트업 데일리 | K-Startup 사업공고 |
| 2026-10-15 | [[부산울산경남센터] 사회적협동조합 설립인가 및 경영공시 교육 안내 (10.14.(수), 10.15.(목) - 온라인병행)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179337) | 한국사회적기업진흥원 부산울산경남센터 | K-Startup 사업공고 |
| 2026-10-15 | [(Plug in: Tokyo) 일본 도쿄 Startup JAPAN expo 2026 참여 스타트업 모집(~10/15)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179326) | (재)부산창조경제혁신센터 | K-Startup 사업공고 |
| 2026-10-15 | [[강동구 청년해냄센터] 고덕비즈밸리 강동U1센터 청년창업공간 입주기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179402) | 강동구 청년해냄센터 | K-Startup 사업공고 |
| 2026-10-15 | [[숭실대학교 캠퍼스타운 x 스팩스페이스] 생성형 AI활용 사업계획서 마스터링 과정 참여자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179372) | 숭실대학교 캠퍼스타운사업단 | K-Startup 사업공고 |
| 2026-10-15 | [모두의 창업 등 정부지원사업 완벽 대비! 「1:1 맞춤형 창업 멘토링」 참가자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179422) | 강남구여성능력개발센터 | K-Startup 사업공고 |
| 2026-10-15 | [(창업도시조성프로젝트)울산 벤처빌더 플랫폼(Step1) 참여팀 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179469) | (재)울산창조경제혁신센터 | K-Startup 사업공고 |
| 2026-10-16 | [2026년 전시회 부스 지원 참여 소상공인 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179217) | 중소상공인희망재단 | K-Startup 사업공고 |
| 2026-10-16 | [ETRI 기술활용 신사업 모델 공모전](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179280) | 에트리홀딩스 | K-Startup 사업공고 |

## 스타트업 뉴스

| 날짜 | 제목 | 출처 |
|---|---|---|
| 2026-10-13 | [AI 투자 늘어도 성과는 6%…지멘스, ‘인텔리전스 센터 X’로 기업 AI 상용화 해법 제시](https://www.venturesquare.net/1119475/) | 벤처스퀘어 |
| 2026-10-13 | [더밀크, 오픈AI·GS·AWS 전문가 한자리에…2027년 기업이 내려야 할 AI 결정 7가지](https://www.venturesquare.net/1119466/) | 벤처스퀘어 |
| 2026-10-13 | [차즘, 장기렌트 중도해지 대신 계약 승계…차량·월 납입금 비교부터 안전거래까지](https://www.venturesquare.net/1119483/) | 벤처스퀘어 |
| 2026-10-13 | [디멧, 창문에서 전기 만드는 반투명 태양전지 개발…경기창조경제혁신센터 투자 유치](https://www.venturesquare.net/1119486/) | 벤처스퀘어 |
| 2026-10-13 | [초기투자액셀러레이터협회, 동남권 AC 네트워크 출범…누적 투자 3404억원 지역 생태계 연결](https://www.venturesquare.net/1119499/) | 벤처스퀘어 |
| 2026-10-13 | [여의시스템, 드론 방어·무인기 통제용 러기드 컴퓨터 공개…극한 환경서 AI 연산 지원](https://www.venturesquare.net/1119507/) | 벤처스퀘어 |
| 2026-10-13 | [부산창조경제혁신센터, 의료기기 기업 협업부터 청년 소통까지…‘휴앤커넥트’ 만족도 최고 5점](https://www.venturesquare.net/1119508/) | 벤처스퀘어 |
| 2026-10-13 | [동승, 신사업·M&A 전담 ‘동승글로벌’ 설립…VC 출신 박혁진 대표 영입](https://www.venturesquare.net/1119520/) | 벤처스퀘어 |
| 2026-10-13 | [엔닷라이트, 스케일업 팁스 선정…최대 30억원 지원받아 로봇 학습용 3D 데이터 검증 기술 개발](https://www.venturesquare.net/1119522/) | 벤처스퀘어 |
| 2026-10-13 | [마이리얼트립, 대전 빵축제 이어 구미 라면축제까지…지역 먹거리 여행 기획전 확대](https://www.venturesquare.net/1119536/) | 벤처스퀘어 |
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
