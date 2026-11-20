# All-about-Korea-Startup-Information

세종 청년창업 기관 공지 · 정부 지원사업 공고 · 스타트업 뉴스를 **매일 14:00 KST에 자동 수집**하는 저장소.
GitHub Actions가 수집→중복제거→상세저장→아래 대시보드 갱신→텔레그램 브리핑까지 수행한다 (git-scraping — 서버·DB·API 비용 없음).

**완전 규칙 기반**: 소스마다 공식 API/RSS 또는 정규식 파서를 쓴다(LLM 미사용, 고정비 $0). 대신 사이트가 개편되면 파서가 조용히 0건을 낼 수 있어, 같은 소스가 **연속 2회 이상 0건**이면 `data/source_health.json`에 기록하고 다이제스트에 "⚠️ 소스 점검 필요"로 경고한다 — 이게 규칙 기반의 유일한 약점(개편에 안 깨지는 AI 추출 대비)을 메우는 피드백 루프다.

<!-- AUTO:START -->

_자동 갱신: 2026-11-20 (KST)_

## 마감 임박 지원사업

| 마감 | 공고 | 기관 | 출처 |
|---|---|---|---|
| 2026-11-20 | [선문대학교 맞춤형 창업멘토링 참가자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179614) | 조슈아파트너스(주) | K-Startup 사업공고 |
| 2026-11-20 | [2026년 초기창업패키지 SM엔터테인먼트 오픈이노베이션 밋업 CultureTech Challenge](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179661) | 씨엔티테크(주) | K-Startup 사업공고 |
| 2026-11-20 | [2027년도 초기창업·창업도약 패키지 사업 신규 주관기관 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179660) | 중소벤처기업부 장관 | K-Startup 사업공고 |
| 2026-11-20 | [2026 맞춤형 창업과정 교육생 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179688) | 김해시중장년기술창업센터장 | K-Startup 사업공고 |
| 2026-11-20 | [2026 제4차 노원사회적경제지원센터 입주기업 신규 공모](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179700) | 노원사회적경제지원센터 | K-Startup 사업공고 |
| 2026-11-20 | [2027년 청년 쿡 비즈니스·푸드테크 센터 스타트업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179687) | 서울특별시 | K-Startup 사업공고 |
| 2026-11-20 | [NEST G밸리 4기 입주기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179733) | 신용보증기금 스케일업금융센터 | K-Startup 사업공고 |
| 2026-11-20 | [임팩트 페스타 2026 참관객 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179745) | 서울소셜벤처허브 | K-Startup 사업공고 |
| 2026-11-20 | [[행사 안내] 2026 경기도 R&D 성과공유회](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179763) | 주식회사 내비온파트너스 | K-Startup 사업공고 |
| 2026-11-20 | [호서대학교 서울창업보육센터 신규입주모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179776) | 호서대학교 서울창업보육센터 | K-Startup 사업공고 |
| 2026-11-20 | [[창업 디자이너 양성과정] 마포 디자인 크리에이터 스쿨](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179795) | 마포청년창업취업지원센터 나루 | K-Startup 사업공고 |
| 2026-11-20 | [[충남] 2026 충남 앵커 산학프로젝트 멘토링 참여기업 모집(6개 대학 교수 1:1 기술 멘토링, 무료)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179805) | 단국대학교 천안캠퍼스 산학협력단 | K-Startup 사업공고 |
| 2026-11-20 | [성동안심상가(소셜벤처 허브센터) 입주기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179800) | 성동구청 | K-Startup 사업공고 |
| 2026-11-20 | [2026년 서부 경기문화창조허브 제4차 가상사무실 지원기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179817) | 경기콘텐츠진흥원 | K-Startup 사업공고 |
| 2026-11-20 | [BoomUP AI 넥스트 웨이브](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179812) | 주식회사 더이노베이터스 | K-Startup 사업공고 |
| 2026-11-20 | [2026년 4차 단국대학교(천안) 창업보육센터 '창조플러스존'입주기업 모집 (연장)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179810) | 단국대학교 생명공학창업보육센터장 | K-Startup 사업공고 |
| 2026-11-22 | [[인탑스 액셀러레이팅 6기 모집] 제품 디자인·설계·양산부터 IR까지! 하드웨어 스타트업 올인원 스케일업](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179558) | 인탑스 주식회사  | K-Startup 사업공고 |
| 2026-11-22 | [[1:1 무료 코칭데이] 하드웨어 스타트업 디자인·설계·금형·양산, 현직 엔지니어 상담](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179693) | 인탑스 주식회사  | K-Startup 사업공고 |
| 2026-11-22 | [한국외국어대학교 창업보육센터 입주기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179709) | 한국외국어대학교연구산학협력단 | K-Startup 사업공고 |
| 2026-11-22 | [2026년 대전 스타트업 원스톱 지원센터 아카데미 4회차](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179695) | 대전창조경제혁신센터 | K-Startup 사업공고 |

## 스타트업 뉴스

| 날짜 | 제목 | 출처 |
|---|---|---|
| 2026-11-20 | [제주창조경제혁신센터, 스타트업 145개사 발굴·109억원 투자 연계…창업도시 기반 확대](https://www.venturesquare.net/1130250/) | 벤처스퀘어 |
| 2026-11-20 | [암세포를 삼키는 면역세포에서 세포 원료 사업까지…케이더블유바이오 장희순 대표](https://www.venturesquare.net/1130248/) | 벤처스퀘어 |
| 2026-11-20 | [에이닷큐어, ‘모두의 챌린지 바이오’ 선정…음성 AI로 심부전 환자 상태 변화 추적한다](https://www.venturesquare.net/1130273/) | 벤처스퀘어 |
| 2026-11-20 | [센스톤, 미국 텍사스 수도 인프라 보안 프로젝트 참여…OT 접속 통제 기술 공급](https://www.venturesquare.net/1130275/) | 벤처스퀘어 |
| 2026-11-20 | [청년창업사관학교 총동문회, ‘K-유니콘 드림쇼 2026’서 선후배 창업가 연결…전국 동문 네트워크 강화](https://www.venturesquare.net/1130281/) | 벤처스퀘어 |
| 2026-11-20 | [모레, SC26서 자기 개선형 AI 추론 기술 ‘TIDE’ 공개…처리량 최대 1.66배 향상](https://www.venturesquare.net/1130289/) | 벤처스퀘어 |
| 2026-11-20 | [서울대 캠퍼스타운, 입주기업 8개사 현안에 AI 적용…학생 26개 팀 실무 솔루션 개발](https://www.venturesquare.net/1130295/) | 벤처스퀘어 |
| 2026-11-20 | [아파트멘터리, 올해 매출 48% 증가…마포 두 번째 직영 상담공간 개설](https://www.venturesquare.net/1130305/) | 벤처스퀘어 |
| 2026-11-20 | [한시간컴, AI 영상 제작 플랫폼 모픽으로 ‘방울방울 쥐방울’ 제작…애니메이션 부트캠프 대상](https://www.venturesquare.net/1130313/) | 벤처스퀘어 |
| 2026-11-20 | [젠엑시스, 기보벤처캠프 19기 10개사 투자유치 역량 강화…로아키친·마이일타·라제온 우수기업 선정](https://www.venturesquare.net/1130319/) | 벤처스퀘어 |
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
