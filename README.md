# All-about-Korea-Startup-Information

세종 청년창업 기관 공지 · 정부 지원사업 공고 · 스타트업 뉴스를 **매일 14:00 KST에 자동 수집**하는 저장소.
GitHub Actions가 수집→중복제거→상세저장→아래 대시보드 갱신→텔레그램 브리핑까지 수행한다 (git-scraping — 서버·DB·API 비용 없음).

**완전 규칙 기반**: 소스마다 공식 API/RSS 또는 정규식 파서를 쓴다(LLM 미사용, 고정비 $0). 대신 사이트가 개편되면 파서가 조용히 0건을 낼 수 있어, 같은 소스가 **연속 2회 이상 0건**이면 `data/source_health.json`에 기록하고 다이제스트에 "⚠️ 소스 점검 필요"로 경고한다 — 이게 규칙 기반의 유일한 약점(개편에 안 깨지는 AI 추출 대비)을 메우는 피드백 루프다.

<!-- AUTO:START -->

_자동 갱신: 2026-11-28 (KST)_

## 마감 임박 지원사업

| 마감 | 공고 | 기관 | 출처 |
|---|---|---|---|
| 2026-11-28 | [2027 지역 창업 솔버톤 대회](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179848) | 주식회사 유디임팩트 | K-Startup 사업공고 |
| 2026-11-29 | [취약분야 상시 컨설팅 11월 참가자 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179514) | 강동구 청년해냄센터 | K-Startup 사업공고 |
| 2026-11-29 | [모두의 창업 등 정부지원사업 완벽 대비! 「1:1 창업 멘토링」 참가자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179797) | 강남구여성능력개발센터 | K-Startup 사업공고 |
| 2026-11-29 | [2026년 한국외대 창업보육센터 입주기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179877) | 한국외국어대학교 연구산학협력단 | K-Startup 사업공고 |
| 2026-11-30 | [2026년 컴퍼니빌더형 기술·경영 컨설팅 지원사업 TechBiz Venture Clinic](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179024) | 주식회사 단국대학교 기술지주회사, 씨엔티테크, 충남산학융합원 | K-Startup 사업공고 |
| 2026-11-30 | [2026년 서대문구 청년창업기업 및 사회연대경제기업 수시 전문상담 경영컨설팅 신청 기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179184) | 서대문구청장 | K-Startup 사업공고 |
| 2026-11-30 | [2026년 창업-Bus 프로그램「강원브릿지 화요IR」 참여기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179386) | (재)강원창조경제혁신센터 | K-Startup 사업공고 |
| 2026-11-30 | [2026년 중소기업 수출 부대비용 지원사업](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179417) | 한국고용정보원 | K-Startup 사업공고 |
| 2026-11-30 | [해외진출 기업 대상 AI 통역 서비스 「아네스노트」미팅 통역 이용권 지원 (11월)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179617) | 주식회사 팀제로코드 | K-Startup 사업공고 |
| 2026-11-30 | [2026년 11월 초기 창업기업 대상 벤처기업 인증 행정자문&전략 수립 기업모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179655) | 박준범행정사사무소 | K-Startup 사업공고 |
| 2026-11-30 | [「벤처·이노비즈·메인비즈 스케일업 밋업」 참여기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179647) | (주)엠비즈플래닛 산하 혁신기술경영인증지원센터 | K-Startup 사업공고 |
| 2026-11-30 | [[은행연합회] 청년 소상공인 컨설팅 지원 사업](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179630) | 한국생산성본부 | K-Startup 사업공고 |
| 2026-11-30 | [2026 벤처확인 인증준비기업 맞춤형 무료 진단 지원사업](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179663) | (주)엠비즈플래닛 산하 혁신기술경영인증지원센터 | K-Startup 사업공고 |
| 2026-11-30 | [[우리금융그룹 지정기탁사업] 청년사업가 도약기반 지원사업 &apos;우리새희망가게&apos; 참여자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179659) | 드림메이커스 사회적협동조합 | K-Startup 사업공고 |
| 2026-11-30 | [[무료 세미나] 글로벌 진출 초기 챙겨야 할 GEO 전략](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179711) | 토스페이먼츠 | K-Startup 사업공고 |
| 2026-11-30 | [[부산대학교병원]「의료·헬스케어 스타트업 인큐베이터 사업」입주기업 모집공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179696) | 부산대학교병원장 | K-Startup 사업공고 |
| 2026-11-30 | [출연연, 대학 연구소기업 Business Development 프로그램 참여 예비창업자 모집 (11월)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179694) | 연구개발특구진흥재단 | K-Startup 사업공고 |
| 2026-11-30 | [2027년도 &apos;맞춤형 해외 저작권 바우처 지원&apos; 사업 수행기관 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179722) | 한국저작권보호원장 | K-Startup 사업공고 |
| 2026-11-30 | [2026년 한라대학교 창업보육센터 11월 신규입주기업 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179761) | 한라대학교 창업보육센터 | K-Startup 사업공고 |
| 2026-11-30 | [2026년 특허출원·등록 비용 바우처 지원사업 17차(하반기 10차)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179777) | (사)한국중소기업발전협회 | K-Startup 사업공고 |

## 스타트업 뉴스

| 날짜 | 제목 | 출처 |
|---|---|---|
| 2026-11-28 | [허슬러즈, ‘산리오캐릭터즈 드림 트래블’ 대규모 업데이트](https://www.venturesquare.net/1132291/) | 벤처스퀘어 |
| 2026-11-28 | [[김지현의 Scale-Up Note] 스타트업의 대들보는 CEO 하나뿐이어야 하는가](https://www.venturesquare.net/1132298/) | 벤처스퀘어 |
| 2026-11-28 | [비대면진료 제도화 앞두고 스타트업 우려 확산…중기부, 의료법 하위규정 해법 찾기 나서](https://www.venturesquare.net/1132330/) | 벤처스퀘어 |
| 2026-11-26 | [컬리, 온라인 미식 큐레이션을 오프라인으로…184개 브랜드와 ‘컬리푸드페스타 2026’ 개최](https://www.venturesquare.net/1132007/) | 벤처스퀘어 |
| 2026-11-26 | [나눔비타민, 복지 혜택의 지급에서 실제 이용까지…위치정보 기반 복지 서비스로 KISA 원장상 수상](https://www.venturesquare.net/1132010/) | 벤처스퀘어 |
| 2026-11-26 | [블루포인트, 핵융합 기술의 산업화 가능성 찾는다…‘퓨전 빌더스’ 첫 개최](https://www.venturesquare.net/1132013/) | 벤처스퀘어 |
| 2026-11-26 | [아이브이웍스, 6G·위성통신 핵심 반도체 소재 기술 고도화…글로벌 팁스 50억원 확보](https://www.venturesquare.net/1132028/) | 벤처스퀘어 |
| 2026-11-26 | [클라썸, 여러 AI 에이전트가 협업해 하나의 답변 제공…딥테크 팁스 선정](https://www.venturesquare.net/1132035/) | 벤처스퀘어 |
| 2026-11-26 | [토니모리, 육아휴직부터 업무분담 장려금까지…일·생활 균형을 기업 경쟁력으로](https://www.venturesquare.net/1132040/) | 벤처스퀘어 |
| 2026-11-26 | [뉴플로이, 외부 서버 없이 PC에서 문서 처리…온디바이스 AI 다국어 기능 확대](https://www.venturesquare.net/1132038/) | 벤처스퀘어 |
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
