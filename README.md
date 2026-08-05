# All-about-Korea-Startup-Information

세종 청년창업 기관 공지 · 정부 지원사업 공고 · 스타트업 뉴스를 **매일 07:00 KST에 자동 수집**하는 저장소.
GitHub Actions가 수집→중복제거→상세정리(LLM)→아래 대시보드 갱신→텔레그램 브리핑까지 수행한다 (git-scraping — 서버·DB 없음).

<!-- AUTO:START -->

_자동 갱신: 2026-08-05 (KST)_

## 마감 임박 지원사업

| 마감 | 공고 | 기관 | 출처 |
|---|---|---|---|
| - | 수집된 공고 없음 | - | - |

## 스타트업 뉴스

| 날짜 | 제목 | 출처 |
|---|---|---|
| 2026-08-04 | [코스포 10년, 스타트업의 발자취 담는다…다음 10년 향한 캠페인 본격화](https://www.venturesquare.net/1103559/) | 벤처스퀘어 |
| 2026-08-04 | [K-자율주행, 중동 첫 대형 수출…에이투지, UAE에 110억 원 공급 계약](https://www.venturesquare.net/1103567/) | 벤처스퀘어 |
| 2026-08-04 | [토스 최연소 PO가 다시 창업했다…AI 광고 스타트업 ‘애딧앤아크’ 시드 투자 유치](https://www.venturesquare.net/1103574/) | 벤처스퀘어 |
| 2026-08-04 | [건물 데이터에서 설비 데이터까지…알스퀘어 RA, 영업 플랫폼으로 진화](https://www.venturesquare.net/1103577/) | 벤처스퀘어 |
| 2026-08-04 | [조선소 용접 로봇에도 피지컬 AI…마키나락스, HD한국조선해양과 이상탐지 실증](https://www.venturesquare.net/1103588/) | 벤처스퀘어 |
| 2026-08-04 | [맥스서밋 2026 성료…AI 시대 마케팅의 마지막 경쟁력은 ‘축적된 자산’](https://www.venturesquare.net/1103478/) | 벤처스퀘어 |
| 2026-08-05 | [잠드는 순간 산리오와 여행 시작…허슬러즈, 게임형 수면 앱 한·일 동시 출시](https://www.venturesquare.net/1103625/) | 벤처스퀘어 |
| 2026-08-05 | [AI 통번역 입은 올리브영…플리토, 외국인 쇼핑 경험 바꾼다](https://www.venturesquare.net/1103633/) | 벤처스퀘어 |
| 2026-08-05 | [AI 마케팅·펨테크에 베팅…씨엔티테크, 시그마인·이사벨라 시드 투자](https://www.venturesquare.net/1103636/) | 벤처스퀘어 |
| 2026-08-05 | [딜, ARR 15억달러 돌파…AI 보안 기업 인수로 글로벌 HR 플랫폼 경쟁력 강화](https://www.venturesquare.net/1103648/) | 벤처스퀘어 |
<!-- AUTO:END -->

## 데이터 구조

| 파일 | 내용 |
|---|---|
| `data/items.jsonl` | 수집된 전체 목록. 1줄 = 공고 1건: `{id, source, category(지원사업\|공지\|뉴스\|행사), title, url, org, posted, deadline, detail, scraped_at}` |
| `data/details/{id}.md` | 지원사업·공지의 상세 본문 (지원대상·내용·기간·방법·문의처·첨부 URL) — **지원서 작성 재료** |
| `data/status.jsonl` | 공고별 진행 상태. append-only, **id별 마지막 줄이 유효**: `{id, status(검토\|지원예정\|초안\|제출\|선정\|탈락), memo, updated_at}` |

## 에이전트(헤르메스) 연동

공개 저장소라 인증 없이 raw URL로 읽는다:

```
목록:   https://raw.githubusercontent.com/sodam3156/All-about-Korea-Startup-Information/main/data/items.jsonl
상세:   https://raw.githubusercontent.com/sodam3156/All-about-Korea-Startup-Information/main/data/details/{id}.md
상태:   https://raw.githubusercontent.com/sodam3156/All-about-Korea-Startup-Information/main/data/status.jsonl
```

**"이 공고 지원서 써줘" 흐름**: items.jsonl에서 공고 선택 → `detail` 경로의 md를 읽어 초안 작성 → status.jsonl에 `{"id":"...","status":"초안","memo":"...","updated_at":"..."}` 한 줄 append 후 push (또는 GitHub Contents API PUT). 사람이 GitHub 웹에서 직접 편집해도 된다.

상태를 기록해두면 다음 날 브리핑이 **마감 D-7 이내 진행 중 공고를 자동 리마인드**한다.

## 설정 (저장소 Settings → Secrets and variables → Actions)

| Secret | 용도 | 없으면 |
|---|---|---|
| `ANTHROPIC_API_KEY` | 게시판 추출·상세 정리·브리핑 요약 (claude-haiku-4-5) | 해당 단계 스킵 (JSON/RSS 소스만 수집) |
| `DATA_GO_KR_KEY` | [공공데이터포털](https://www.data.go.kr) "K-Startup 조회서비스" 활용신청 후 발급되는 서비스키 | K-Startup 소스 스킵 |
| `TELEGRAM_BOT_TOKEN` / `TELEGRAM_CHAT_ID` | 일일 브리핑 발송 (@BotFather로 봇 생성) | 브리핑을 Actions 로그에만 출력 |

## 소스 추가

`scrape.py`의 `SOURCES`에 한 줄 추가하면 끝. 게시판(HTML)은 `type: "board"`로 넣으면 사이트별 파서 없이 LLM이 스키마로 추출한다.

로컬 실행: `pip install -r requirements.txt && python scrape.py` / 자체 점검: `python test_scrape.py`
