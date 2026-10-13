# All-about-Korea-Startup-Information

세종 청년창업 기관 공지 · 정부 지원사업 공고 · 스타트업 뉴스를 **매일 14:00 KST에 자동 수집**하는 저장소.
GitHub Actions가 수집→중복제거→상세저장→아래 대시보드 갱신→텔레그램 브리핑까지 수행한다 (git-scraping — 서버·DB·API 비용 없음).

**완전 규칙 기반**: 소스마다 공식 API/RSS 또는 정규식 파서를 쓴다(LLM 미사용, 고정비 $0). 대신 사이트가 개편되면 파서가 조용히 0건을 낼 수 있어, 같은 소스가 **연속 2회 이상 0건**이면 `data/source_health.json`에 기록하고 다이제스트에 "⚠️ 소스 점검 필요"로 경고한다 — 이게 규칙 기반의 유일한 약점(개편에 안 깨지는 AI 추출 대비)을 메우는 피드백 루프다.

<!-- AUTO:START -->

_자동 갱신: 2026-10-13 (KST)_

## 마감 임박 지원사업

| 마감 | 공고 | 기관 | 출처 |
|---|---|---|---|
| 2026-10-13 | [[무료 AI 역량강화 교육] 생성형 AI 기반 무역 금융 리스크 최적화 과정 (대전)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=178891) | (주)글로벌창업연구소 | K-Startup 사업공고 |
| 2026-10-13 | [2026 경기 스타트업 서밋(G-SUMMIT 2026) 사전등록 오픈](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179009) | (재)경기도경제과학진흥원 | K-Startup 사업공고 |
| 2026-10-13 | [2026년 과학기술분야 R&D 대체인력 활용 지원사업 4차 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179121) | 한국여성과학기술인육성재단 | K-Startup 사업공고 |
| 2026-10-13 | [「청년창업기업·사회적경제기업·예비창업자(소상공인) 대상」 2025년 제1기 서울콜라보레이션 청년 성공창업스쿨 교육생 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179218) | 서대문구청장 | K-Startup 사업공고 |
| 2026-10-13 | [구로구 청년창업지원센터_입주기업 모집·선발](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179285) | 구로구 청년창업지원센터 | K-Startup 사업공고 |
| 2026-10-13 | [[무료 세미나] ChatGPT·Gemini 시대, 우리 브랜드 AI 검색 노출 전략](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179306) | 토스페이먼츠 | K-Startup 사업공고 |
| 2026-10-13 | [용인시산업진흥원 2026년 제4차 창업지원센터 입주기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179284) | 용인시산업진흥원 | K-Startup 사업공고 |
| 2026-10-13 | [2026년 제5차 대전창업허브 및 대전소셜벤처캠퍼스 입주기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179350) | (재)대전창조경제혁신센터 | K-Startup 사업공고 |
| 2026-10-13 | [2026년 여성CEO 비즈니스 아카데미 충청권역 시즌 2](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179331) | 한국여성경제인협회 | K-Startup 사업공고 |
| 2026-10-13 | [2026년 10월 동네창업학교 교육생 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179403) | 충남신용보증재단 | K-Startup 사업공고 |
| 2026-10-13 | [[용인시산업진흥원] 「2026년 용인 오픈이노베이션 교류회」 5회차(반도체/피지컬AI)](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179385) | 알파브라더스 | K-Startup 사업공고 |
| 2026-10-13 | [2026년 10월 전북 IR피칭 & 오피스아워 by KRYPTON 신청 접수](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179378) | (주)크립톤 전북지사 | K-Startup 사업공고 |
| 2026-10-13 | [2026년 스타트업 법률지원사업 대전광역시 법률상담회 참여 기업 모집 안내](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179439) | 창업진흥원 원스톱지원실 | K-Startup 사업공고 |
| 2026-10-13 | [2026 광명시 기업박람회(GM TECH EXPO 2026) 참여기업 추가모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179433) | 광명시청 | K-Startup 사업공고 |
| 2026-10-13 | [2026년 대전 웰컴 스테이 지원사업 참여기업 모집 연장 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179449) | (재)대전창조경제혁신센터 | K-Startup 사업공고 |
| 2026-10-14 | [2026 디캠프 배치 9기 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179094) | 재단법인 은행권청년창업재단 | K-Startup 사업공고 |
| 2026-10-14 | [2026 글로벌 스타트업 서밋 (일본2차) 세미나&밋업 참여기업 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179221) | 인천창조경제혁신센터 대표이사 | K-Startup 사업공고 |
| 2026-10-14 | [[3D-FAB] 2026년 3D프린팅 네트워킹데이(창업 선배와의 만남) 참가자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179355) | 3D프린팅혁신성장센터 | K-Startup 사업공고 |
| 2026-10-14 | [해운대 청년채움공간(청년창업지원시설) 위탁운영기관 모집 공고](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179412) | 부산광역시 해운대구청장 | K-Startup 사업공고 |
| 2026-10-14 | [2026년 경기 스타트업 아카데미 딥테크 교육 참여자 모집](https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn=179404) | 경기도·경기도경제과학진흥원 | K-Startup 사업공고 |

## 스타트업 뉴스

| 날짜 | 제목 | 출처 |
|---|---|---|
| 2026-10-12 | [충남콘텐츠진흥원, 천안 스타트업 7곳 중국서 1560만달러 수출 상담·협력 성과…MOU 12건 체결](https://www.venturesquare.net/1119176/) | 벤처스퀘어 |
| 2026-10-12 | [리브애니웨어, 외국인 단기임대 거래액 10배 증가…전체 거래액의 29% 차지](https://www.venturesquare.net/1119187/) | 벤처스퀘어 |
| 2026-10-12 | [아델, 사노피에 1조4000억원 기술이전 이어 코스닥 도전…최대 543억원 공모](https://www.venturesquare.net/1119199/) | 벤처스퀘어 |
| 2026-10-12 | [소프트프릭, AI 민감정보 노출 진단·에이전트 접근 통제 기술 특허 2건 등록](https://www.venturesquare.net/1119206/) | 벤처스퀘어 |
| 2026-10-12 | [[VS기획] 프롭테크 87.5%가 AI 도입·개발 중…데이터·인력 부족에 가로막힌 현실](https://www.venturesquare.net/1118483/) | 벤처스퀘어 |
| 2026-10-12 | [스텔업, AI 한국어 교육 플랫폼 ‘한글링’ 베트남 현지 실무교육에 활용…한국기업 취업 지원](https://www.venturesquare.net/1119237/) | 벤처스퀘어 |
| 2026-10-12 | [멘탯, AI 학습용 도서 3만4000종 검색 서비스 출시…80억 토큰 데이터 거래 지원](https://www.venturesquare.net/1119236/) | 벤처스퀘어 |
| 2026-10-13 | [[컬처슬로건 탐방기] BHSN – 몰입이 가치를 만든다](https://www.venturesquare.net/1119264/) | 벤처스퀘어 |
| 2026-10-13 | [와이즈넛, 개발자 없이 대화로 AI 에이전트 제작…‘AI Festa 2026’서 현장 시연](https://www.venturesquare.net/1119285/) | 벤처스퀘어 |
| 2026-10-13 | [슬로크 다나야드, 파리 팝업 넘어 유럽 유통까지…K브랜드 시장 진출 지원](https://www.venturesquare.net/1119284/) | 벤처스퀘어 |
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
