# All-about-Korea-Startup-Information

세종 청년창업 기관 공지 · 정부 지원사업 공고 · 스타트업 뉴스를 **매일 14:00 KST에 자동 수집**하는 저장소.
GitHub Actions가 수집→중복제거→상세저장→아래 대시보드 갱신→텔레그램 브리핑까지 수행한다 (git-scraping — 서버·DB·API 비용 없음).

**완전 규칙 기반**: 소스마다 공식 API/RSS 또는 정규식 파서를 쓴다(LLM 미사용, 고정비 $0). 대신 사이트가 개편되면 파서가 조용히 0건을 낼 수 있어, 같은 소스가 **연속 2회 이상 0건**이면 `data/source_health.json`에 기록하고 다이제스트에 "⚠️ 소스 점검 필요"로 경고한다 — 이게 규칙 기반의 유일한 약점(개편에 안 깨지는 AI 추출 대비)을 메우는 피드백 루프다.

<!-- AUTO:START -->

_자동 갱신: 2026-10-16 (KST)_

## 마감 임박 지원사업

| 마감 | 공고 | 기관 | 출처 |
|---|---|---|---|
| 2026-10-16 | [2026년 전시회 부스 지원 참여 소상공인 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179217) | 중소상공인희망재단 | K-Startup 사업공고 |
| 2026-10-16 | [ETRI 기술활용 신사업 모델 공모전](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179280) | 에트리홀딩스 | K-Startup 사업공고 |
| 2026-10-16 | [2026년 특허출원·등록 비용 바우처 지원사업 14차(하반기 7차)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179356) | (사)한국중소기업발전협회 | K-Startup 사업공고 |
| 2026-10-16 | [2026 경기도 ESG 인식확산 교육 (5~7회차) 참여자 모집 안내](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179325) | ESGi 이에스지아이 | K-Startup 사업공고 |
| 2026-10-16 | [[창업] 창업가를 위한 IR 피칭 기초 부스팅](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179414) | 마포청년창업취업지원센터 나루 | K-Startup 사업공고 |
| 2026-10-16 | [트레일 신산업 로컬창업지원 참여기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179396) | (주)크립톤 전북지사 | K-Startup 사업공고 |
| 2026-10-16 | [2026년 한신대학교 창업보육센터 신규 창업기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179377) | 한신대학교 창업보육센터 | K-Startup 사업공고 |
| 2026-10-16 | [TechGALA 2026 한국 스타트업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179438) | (주)플린토파트너스 | K-Startup 사업공고 |
| 2026-10-16 | [2026년 서울 라이프스타일 거점(일본) 진출사업 참여기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179454) | 서울경제진흥원 | K-Startup 사업공고 |
| 2026-10-16 | [2026 오세아니아 전략시장 진출 사업 참여기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179453) | 서울경제진흥원 | K-Startup 사업공고 |
| 2026-10-16 | [[제주창조경제혁신센터]「상시매칭 오픈이노베이션 플랫폼」&apos;에코프로 계열사&apos;&apos;수요과제 매칭 스타트업 모집 (~10/16)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179487) | 제주창조경제혁신센터 | K-Startup 사업공고 |
| 2026-10-16 | [성남 기후테크 UpSkill 아카데미 Vol.3 - 투자유치를 위한 IR 전략](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179490) | 도시혁신그룹 무브먼트 주식회사 | K-Startup 사업공고 |
| 2026-10-18 | [2026 강동구 창업가 네트워킹 데이 참가 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179388) | 강동구 청년해냄센터 | K-Startup 사업공고 |
| 2026-10-18 | [「2026 전북특구 이노폴리스 캠퍼스(액셀러레이팅 지원) 사업」배치프로그램 4기 참여기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179367) | 연구개발특구진흥재단 | K-Startup 사업공고 |
| 2026-10-18 | [2026 D-Global 딥테크 스케일업 세미나 참가 기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179494) | 조슈아파트너스(주) | K-Startup 사업공고 |
| 2026-10-19 | [2026년 대한민국 물산업 혁신 창업대전(Startup Water 2026) 참가자(팀) 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178976) | 기후에너지환경부 | K-Startup 사업공고 |
| 2026-10-19 | [UNIST 연구자-예비창업자 팀빌딩 프로그램](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179358) | 울산과학기술원(UNIST) | K-Startup 사업공고 |
| 2026-10-19 | [영도 창업오피스 크립톤 1:1 멘토링 입주기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179424) | 크립톤 부산센터 | K-Startup 사업공고 |
| 2026-10-19 | [2026년「강남 취‧창업허브센터」8차 입주 기업 신규 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179435) | 서울특별시 강남구청 | K-Startup 사업공고 |
| 2026-10-19 | [2026 Invest Seoul Partners Night](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179515) | 서울투자진흥재단 | K-Startup 사업공고 |

## 스타트업 뉴스

| 날짜 | 제목 | 출처 |
|---|---|---|
| 2026-10-15 | [부스터스 이퀄베리, 아마존 할인 행사 매출 5배 성장…NAD+ 세럼·크림이 실적 견인](https://www.venturesquare.net/1120284/) | 벤처스퀘어 |
| 2026-10-15 | [휴로틱스, 250억원 시리즈A 투자 유치…대웅·네이버·롯데 합류로 웨어러블 로봇 사업 확대](https://www.venturesquare.net/1120296/) | 벤처스퀘어 |
| 2026-10-15 | [경기창조경제혁신센터, 9개 기관과 ‘경기 스타트업 플렉스’ 개최…모빌리티원 중기부 장관상](https://www.venturesquare.net/1120321/) | 벤처스퀘어 |
| 2026-10-15 | [시높시스, 딥엑스 등 경기 팹리스 4개사와 협력…AI·반도체 스타트업 성장 지원](https://www.venturesquare.net/1120320/) | 벤처스퀘어 |
| 2026-10-15 | [디셈버앤컴퍼니 핀트, KB증권과 AI 투자 이벤트…직접투자·자동운용 결합](https://www.venturesquare.net/1120331/) | 벤처스퀘어 |
| 2026-10-15 | [번개장터, 찜한 상품에만 48시간 할인…‘비밀가격제안’ 도입 후 평균 7.4시간 만에 거래](https://www.venturesquare.net/1120330/) | 벤처스퀘어 |
| 2026-10-15 | [AI스페라, 일본 보안 전시회서 AI 위협 노출 관리 플랫폼 ‘AITEM’ 공개](https://www.venturesquare.net/1120263/) | 벤처스퀘어 |
| 2026-10-15 | [“기술이 남긴 문제, 기술로 해결한다”…블루포인트, 12개 스타트업이 펼친 ‘기술낙관주의’](https://www.venturesquare.net/1120338/) | 벤처스퀘어 |
| 2026-10-15 | [망고슬래브 AI 점자 프린터 ‘네모닉닷’, 美 타임 ‘2026 최고의 발명품’ 선정](https://www.venturesquare.net/1120356/) | 벤처스퀘어 |
| 2026-10-15 | [[VS 현장] “투자자도, 고객도 한자리에서”…인천 SuRF 2026, 스타트업 성장 기회 잇다](https://www.venturesquare.net/1118746/) | 벤처스퀘어 |
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
