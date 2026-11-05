# AX Tools

해외영업 반복 업무를 줄이는 웹 도구 모음. 도구마다 폴더 하나, `index.html` 하나로 동작합니다.

| 도구 | 폴더 | 설명 |
|---|---|---|
| 수출 견적서 계산기 | [quotation-builder](quotation-builder/) | 인코텀즈별 단가 비교 · 협상가 마진 확인 · 영문 견적서 출력 · CSV/엑셀 품목 불러오기 · 환율 API · 관세청 HS Code 검색 |

## 배포 (Vercel)
- 정적 파일 + 서버 함수 `api/rate.js`(환율). 프레임워크 설정 없음(Other).
- 환경변수 `EXCHANGE_RATE_API_KEY` 를 Vercel 프로젝트 설정에 등록. 키는 브라우저에 노출되지 않습니다.
- 키가 없거나 실패하면 페이지가 키 없는 공개 API(open.er-api.com → frankfurter)로 대신 조회합니다.

## HS Code 데이터
- 출처: 공공데이터포털 「관세청 HS부호」 (2026년, 적용 종료 2026-12-31)
- 변환: `python scripts/build_hsk.py 관세청_HS부호_YYYYMMDD.xlsx` → `data/hsk.json`
- **2027-01-01 HS 개정** 시 새 파일을 받아 다시 변환하세요.

## 폴더 규칙
- 폴더 이름은 영문 소문자-하이픈 (`quotation-builder`, `mail-template`) — 한글 폴더명은 URL이 깨져 보입니다
- 각 폴더: `index.html`(도구) + `PROMPT.md`(만들 때 쓴 프롬프트)
- 새 도구를 만들면 루트 `index.html` 목록과 이 표에 한 줄 추가
