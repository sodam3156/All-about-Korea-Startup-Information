# All-about-Korea-Startup-Information

세종 청년창업 기관 공지 · 정부 지원사업 공고 · 스타트업 뉴스를 **매일 14:00 KST에 자동 수집**하는 저장소.
GitHub Actions가 수집→중복제거→상세저장→아래 대시보드 갱신→텔레그램 브리핑까지 수행한다 (git-scraping — 서버·DB·API 비용 없음).

**완전 규칙 기반**: 소스마다 공식 API/RSS 또는 정규식 파서를 쓴다(LLM 미사용, 고정비 $0). 대신 사이트가 개편되면 파서가 조용히 0건을 낼 수 있어, 같은 소스가 **연속 2회 이상 0건**이면 `data/source_health.json`에 기록하고 다이제스트에 "⚠️ 소스 점검 필요"로 경고한다 — 이게 규칙 기반의 유일한 약점(개편에 안 깨지는 AI 추출 대비)을 메우는 피드백 루프다.

<!-- AUTO:START -->

_자동 갱신: 2026-08-06 (KST)_

## 마감 임박 지원사업

| 마감 | 공고 | 기관 | 출처 |
|---|---|---|---|
| 2026-08-06 | [[서울과학기술대학교]3D프린터 장비교육](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178753) | 서울과학기술대학교 | K-Startup 사업공고 |
| 2026-08-07 | [[2026-061호] 2026년 세종테크노파크 본관동 입주기업 비즈니스 고도화 지원 프로그램 참여기업 모집 2차 공고](https://sjtp.or.kr/bbs/board.php?bo_table=business01&wr_id=1988) | 세종테크노파크 | 세종테크노파크 사업공고 |
| 2026-08-07 | [수원남문시장 「이어가게·열어가게」 창업아카데미 참여자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178723) | 수원도시재단 | K-Startup 사업공고 |
| 2026-08-07 | [고려대기술지주(주) 판교인큐베이팅센터 입주기업 모집공고(기간연장)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178700) | 고려대학교기술지주 주식회사  | K-Startup 사업공고 |
| 2026-08-07 | [라이콘 창업 경진대회 참여팀 모집(로컬 창업 아이디어톤)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178699) | 유원대학교 충남 앵커사업단 | K-Startup 사업공고 |
| 2026-08-07 | [2026 Blender와 AI로 완성하는 3D콘텐츠 제작교육](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178685) | 차세대융합기술연구원 | K-Startup 사업공고 |
| 2026-08-07 | [[한양대학교] 2026년 제23기 한양스타트업아카데미 교육생 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178677) | 한양대학교 창업지원단 | K-Startup 사업공고 |
| 2026-08-07 | [2026년 대구콘텐츠코리아랩 캐릭터 글로벌 진입 프로젝트 참가자 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178674) | (재)대구디지털혁신진흥원 | K-Startup 사업공고 |
| 2026-08-07 | [「제3회 DDM Union 청년 창업 아이디어 챌린지」참가자 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178664) | 서울특별시 동대문구청 | K-Startup 사업공고 |
| 2026-08-07 | [「2026 한국전자전(KES)」관악S밸리관 참가기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178659) | 관악중소벤처진흥원 | K-Startup 사업공고 |
| 2026-08-07 | [제조 AI 기술 사업화 지원 수혜기업 모집(~8/7)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178655) | 경북대학교 스타트업지원센터장 | K-Startup 사업공고 |
| 2026-08-07 | [제품 양산 패키지 수혜기업 모집(~8/7)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178654) | 경북대학교 스타트업지원센터장 | K-Startup 사업공고 |
| 2026-08-07 | [제3회 W-Venture 창업 경진대회(연장)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178653) | (사)부울경여성벤처협회 | K-Startup 사업공고 |
| 2026-08-07 | [2026년 대구 스타트업 오픈이노베이션 자율제안형(상향식) 실증 프로그램 지원기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178649) | (재)대구창조경제혁신센터 대표이사 | K-Startup 사업공고 |
| 2026-08-07 | [KAIST 딥테크 유망랩 라운드테이블](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178645) | (주)아이비유 | K-Startup 사업공고 |
| 2026-08-09 | [제5회 김해스타트업 창업캠프 참여기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178717) | 김해의생명산업진흥원 | K-Startup 사업공고 |
| 2026-08-09 | [2026년 재도전 커뮤니티 데이(수도권) 행사 사전등록 및 창업상담 참여자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178663) | 인천대학교 | K-Startup 사업공고 |
| 2026-08-10 | [[2026-060호]2026년 세종 지역특화 프로젝트 레전드50+2.0 기업진단 및 컨설팅 참여기업 모집](https://sjtp.or.kr/bbs/board.php?bo_table=business01&wr_id=1987) | (재)세종테크노파크 | 세종테크노파크 사업공고 |
| 2026-08-10 | [[코레일유통/본사] 제9차 청년창업 제휴사업자 모집공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178732) | 코레일유통(주) | K-Startup 사업공고 |
| 2026-08-10 | [2026년 제 5회 경남 스타트업 IR「A.C.E(에이스) 경진대회」오픈리그 참여기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178713) | 재단법인 경남창조경제혁신센터 | K-Startup 사업공고 |

## 스타트업 뉴스

| 날짜 | 제목 | 출처 |
|---|---|---|
| 2026-08-06 | [비즈니스온, B2B SaaS에 AI 심는다…AX 플랫폼 전환](https://www.venturesquare.net/1104025/) | 벤처스퀘어 |
| 2026-08-06 | [호텔에서 통했다… 티핑, 일본 현장 실증으로 해외시장 두드린다](https://www.venturesquare.net/1104036/) | 벤처스퀘어 |
| 2026-08-06 | [AI 주거플랫폼 트러스테이, 정보보호 국제표준 2종 동시 획득… 글로벌 공략 기반 강화](https://www.venturesquare.net/1104044/) | 벤처스퀘어 |
| 2026-08-06 | [AI 성과 만드는 법 한자리에… 스노우플레이크, 연례 컨퍼런스 ‘월드 투어 서울’ 개최](https://www.venturesquare.net/1104051/) | 벤처스퀘어 |
| 2026-08-06 | [“AI가 답할 때 우리 브랜드는 왜 없을까”…어센트AI 박세용 대표가 말하는 GEO](https://www.venturesquare.net/1103994/) | 벤처스퀘어 |
| 2026-08-06 | [AI 공격도 미리 침투해본다… AI스페라, 모의해킹 서비스 강화](https://www.venturesquare.net/1104062/) | 벤처스퀘어 |
| 2026-08-06 | [AI·로봇 스타트업, 투자자 만난다… 대전창업포럼 11일 개최](https://www.venturesquare.net/1104112/) | 벤처스퀘어 |
| 2026-08-06 | [99% 자율비행 성공률…니어스랩, 방산 드론으로 코스닥 출사](https://www.venturesquare.net/1104120/) | 벤처스퀘어 |
| 2026-08-06 | [성수가 스포티파이로 물든다…9월 ‘스포티파이 하우스 서울’ 개최](https://www.venturesquare.net/1104123/) | 벤처스퀘어 |
| 2026-08-06 | [공공 복지망도 ‘실시간 관제’…와탭랩스, 사보원 K-테스트베드 실증 완료](https://www.venturesquare.net/1104130/) | 벤처스퀘어 |
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
