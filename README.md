# All-about-Korea-Startup-Information

세종 청년창업 기관 공지 · 정부 지원사업 공고 · 스타트업 뉴스를 **매일 14:00 KST에 자동 수집**하는 저장소.
GitHub Actions가 수집→중복제거→상세저장→아래 대시보드 갱신→텔레그램 브리핑까지 수행한다 (git-scraping — 서버·DB·API 비용 없음).

**완전 규칙 기반**: 소스마다 공식 API/RSS 또는 정규식 파서를 쓴다(LLM 미사용, 고정비 $0). 대신 사이트가 개편되면 파서가 조용히 0건을 낼 수 있어, 같은 소스가 **연속 2회 이상 0건**이면 `data/source_health.json`에 기록하고 다이제스트에 "⚠️ 소스 점검 필요"로 경고한다 — 이게 규칙 기반의 유일한 약점(개편에 안 깨지는 AI 추출 대비)을 메우는 피드백 루프다.

<!-- AUTO:START -->

_자동 갱신: 2026-11-27 (KST)_

## 마감 임박 지원사업

| 마감 | 공고 | 기관 | 출처 |
|---|---|---|---|
| 2026-11-27 | [[창업보육센터]K-Tech 창업성장아카데미 교육프로그램 수강생 모집(~11월)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179208) | 한국기술교육대학교 산학협력단 | K-Startup 사업공고 |
| 2026-11-27 | [[무료 AI 역량강화 교육] 생성형 AI 기반 무역 금융 리스크 최적화 과정(선착순 모집)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179631) | (주)글로벌창업연구소 | K-Startup 사업공고 |
| 2026-11-27 | [한국기술교육대학교 오픈이노베이션 프로그램 참여기업 모집 통합 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179662) | 한국기술교육대학교 앵커사업단 | K-Startup 사업공고 |
| 2026-11-27 | [김해시중장년기술창업센터 2026년 하반기 신규 입주(자)기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179714) | (재)김해의생명산업진흥원 | K-Startup 사업공고 |
| 2026-11-27 | [2026년 경기창업혁신공간 북동부권(구리) 신규 입주기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179701) | (재)경기도경제과학진흥원 | K-Startup 사업공고 |
| 2026-11-27 | [예비, 초기 창업자가 반드시 알아야 할 스타트업 마케팅 방법론 - 제11차 DDM 벤처스타트업 아카데미](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179835) | DDM 청년창업센터 유니콘 | K-Startup 사업공고 |
| 2026-11-27 | [[창업] 창업가를 위한 해외 진출 첫 걸음](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179868) | 마포청년창업취업지원센터 나루 | K-Startup 사업공고 |
| 2026-11-27 | [제42회 국제의료기기·병원설비전시회(KIMES 2027) 참가기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179820) | 한국과학기술연구원 서울바이오허브사업단 | K-Startup 사업공고 |
| 2026-11-27 | [성남창업센터(킨스타워) 신규 입주기업 추가 모집공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179885) | 성남산업진흥원 | K-Startup 사업공고 |
| 2026-11-28 | [2027 지역 창업 솔버톤 대회](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179848) | 주식회사 유디임팩트 | K-Startup 사업공고 |
| 2026-11-29 | [취약분야 상시 컨설팅 11월 참가자 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179514) | 강동구 청년해냄센터 | K-Startup 사업공고 |
| 2026-11-29 | [모두의 창업 등 정부지원사업 완벽 대비! 「1:1 창업 멘토링」 참가자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179797) | 강남구여성능력개발센터 | K-Startup 사업공고 |
| 2026-11-30 | [2026년 컴퍼니빌더형 기술·경영 컨설팅 지원사업 TechBiz Venture Clinic](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179024) | 주식회사 단국대학교 기술지주회사, 씨엔티테크, 충남산학융합원 | K-Startup 사업공고 |
| 2026-11-30 | [2026년 서대문구 청년창업기업 및 사회연대경제기업 수시 전문상담 경영컨설팅 신청 기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179184) | 서대문구청장 | K-Startup 사업공고 |
| 2026-11-30 | [2026년 창업-Bus 프로그램「강원브릿지 화요IR」 참여기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179386) | (재)강원창조경제혁신센터 | K-Startup 사업공고 |
| 2026-11-30 | [2026년 중소기업 수출 부대비용 지원사업](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179417) | 한국고용정보원 | K-Startup 사업공고 |
| 2026-11-30 | [해외진출 기업 대상 AI 통역 서비스 「아네스노트」미팅 통역 이용권 지원 (11월)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179617) | 주식회사 팀제로코드 | K-Startup 사업공고 |
| 2026-11-30 | [2026년 11월 초기 창업기업 대상 벤처기업 인증 행정자문&전략 수립 기업모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179655) | 박준범행정사사무소 | K-Startup 사업공고 |
| 2026-11-30 | [「벤처·이노비즈·메인비즈 스케일업 밋업」 참여기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179647) | (주)엠비즈플래닛 산하 혁신기술경영인증지원센터 | K-Startup 사업공고 |
| 2026-11-30 | [[은행연합회] 청년 소상공인 컨설팅 지원 사업](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179630) | 한국생산성본부 | K-Startup 사업공고 |

## 스타트업 뉴스

| 날짜 | 제목 | 출처 |
|---|---|---|
| 2026-11-26 | [컬리, 온라인 미식 큐레이션을 오프라인으로…184개 브랜드와 ‘컬리푸드페스타 2026’ 개최](https://www.venturesquare.net/1132007/) | 벤처스퀘어 |
| 2026-11-26 | [나눔비타민, 복지 혜택의 지급에서 실제 이용까지…위치정보 기반 복지 서비스로 KISA 원장상 수상](https://www.venturesquare.net/1132010/) | 벤처스퀘어 |
| 2026-11-26 | [블루포인트, 핵융합 기술의 산업화 가능성 찾는다…‘퓨전 빌더스’ 첫 개최](https://www.venturesquare.net/1132013/) | 벤처스퀘어 |
| 2026-11-26 | [아이브이웍스, 6G·위성통신 핵심 반도체 소재 기술 고도화…글로벌 팁스 50억원 확보](https://www.venturesquare.net/1132028/) | 벤처스퀘어 |
| 2026-11-26 | [클라썸, 여러 AI 에이전트가 협업해 하나의 답변 제공…딥테크 팁스 선정](https://www.venturesquare.net/1132035/) | 벤처스퀘어 |
| 2026-11-26 | [토니모리, 육아휴직부터 업무분담 장려금까지…일·생활 균형을 기업 경쟁력으로](https://www.venturesquare.net/1132040/) | 벤처스퀘어 |
| 2026-11-26 | [뉴플로이, 외부 서버 없이 PC에서 문서 처리…온디바이스 AI 다국어 기능 확대](https://www.venturesquare.net/1132038/) | 벤처스퀘어 |
| 2026-11-26 | [크릿벤처스, K웹툰의 일본 IP 사업화에 베팅…국외창업기업 클링크 후속 투자 성공](https://www.venturesquare.net/1132052/) | 벤처스퀘어 |
| 2026-11-26 | [엔바이오셀, 주사형 바이오의약품을 먹는 약으로…셀트리온과 약물전달 기술 실증 추진](https://www.venturesquare.net/1132063/) | 벤처스퀘어 |
| 2026-11-26 | [루드다이나믹스, 약사가 퇴근하면 로봇이 약장을 살핀다…약국에서 찾은 피지컬 AI의 사업화 가능성](https://www.venturesquare.net/1132068/) | 벤처스퀘어 |
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
