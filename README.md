# AX Tools

해외영업 반복 업무를 줄이는 웹 도구 모음. 도구마다 폴더 하나, `index.html` 하나로 동작합니다.

| 도구 | 폴더 | 설명 |
|---|---|---|
| 수출 견적서 계산기 | [quotation-builder](quotation-builder/) | 인코텀즈별 단가 비교 · 협상가 마진 확인 · 영문 견적서 출력 · CSV/엑셀 품목 불러오기 · 무료 환율 API |

## 환율 자동 갱신
`.github/workflows/update-rate.yml`이 평일 09:10(KST)에 ExchangeRate-API로 USD/KRW를 받아 `data/usd-krw.json`에 커밋합니다.
API 키는 저장소 **Settings → Secrets and variables → Actions → `EXCHANGE_RATE_API_KEY`** 에만 저장합니다(페이지·코드에 노출 안 됨).
파일이 없거나 실패하면 페이지가 키 없는 공개 API로 대신 조회합니다.

## 폴더 규칙
- 폴더 이름은 영문 소문자-하이픈 (`quotation-builder`, `mail-template`) — 한글 폴더명은 URL이 깨져 보입니다
- 각 폴더: `index.html`(도구) + `PROMPT.md`(만들 때 쓴 프롬프트)
- 새 도구를 만들면 루트 `index.html` 목록과 이 표에 한 줄 추가
