# AX Tools

해외영업 반복 업무를 줄이는 웹 도구 모음. 저장소는 하나, **도구마다 폴더 하나 = 버셀 프로젝트 하나 = 링크 하나**.

| 도구 | 폴더 | 설명 |
|---|---|---|
| 수출 견적서 계산기 | [quotation-builder](quotation-builder/) | 인코텀즈별 단가 비교 · 협상가 마진 확인 · 영문 견적서 출력 · CSV/엑셀 품목 불러오기 · 환율 API · 관세청 HS Code 검색 |
| 바이어 관리 보드 | [buyer-pipeline](buyer-pipeline/) | 단계별 칸반 · 오늘 할 일(팔로업) 자동 정리 · 가중 파이프라인 · 현지 시각 · CSV 내보내기/불러오기 |

## 배포 (Vercel)
- 도구마다 버셀 프로젝트를 따로 만들고 **Root Directory = 도구 폴더**로 지정 → 각자 독립 링크
- 각 폴더는 그 안에서 완결: 필요한 데이터(`data/`)와 서버 함수(`api/`)도 폴더 안에 둡니다
- 견적서 계산기만 환경변수 `EXCHANGE_RATE_API_KEY` 필요 (`quotation-builder/api/rate.js`가 사용, 브라우저에 노출 안 됨)
  키가 없거나 실패하면 키 없는 공개 API(open.er-api.com → frankfurter)로 대신 조회

## HS Code 데이터
- 출처: 공공데이터포털 「관세청 HS부호」 (2026년, 적용 종료 2026-12-31)
- 변환: `python scripts/build_hsk.py 관세청_HS부호_YYYYMMDD.xlsx` → `quotation-builder/data/hsk.json`
- **2027-01-01 HS 개정** 시 새 파일을 받아 다시 변환하세요.

## 폴더 규칙
- 폴더 이름은 영문 소문자-하이픈 (`quotation-builder`, `mail-template`) — 버셀 프로젝트 이름·링크로도 그대로 씁니다
- 각 폴더: `index.html`(도구) + `PROMPT.md`(만들 때 쓴 프롬프트), 필요하면 `data/`·`api/`
- 폴더 밖 파일을 참조하지 않기 (`../` 금지) — 독립 배포가 깨집니다
