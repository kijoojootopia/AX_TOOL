"""관세청 HS부호 엑셀(공공데이터포털) → data/hsk.json

사용법:  python scripts/build_hsk.py 관세청_HS부호_20260101.xlsx
매년 1월 새 파일을 받아 다시 실행하세요.
"""
import json, re, sys
from pathlib import Path
import openpyxl

src = Path(sys.argv[1] if len(sys.argv) > 1 else "관세청_HS부호_20260101.xlsx")
out = Path(__file__).resolve().parent.parent / "data" / "hsk.json"

ws = openpyxl.load_workbook(src, read_only=True).worksheets[0]
rows = list(ws.iter_rows(values_only=True))
head = {h: i for i, h in enumerate(rows[0]) if h}
clean = lambda s: re.sub(r"\s+", " ", str(s or "")).strip()

leaf, parent = [], {}
valid_until = ""
for r in rows[1:]:
    code = clean(r[head["HS부호"]])
    ko, en = clean(r[head["한글품목명"]]), clean(r[head["영문품목명"]])
    cat = clean(r[head["성질통합분류코드명"]]).strip("()")
    end = r[head["적용종료일자"]]
    valid_until = max(valid_until, end.strftime("%Y-%m-%d") if end else "")
    if len(code) == 10:
        leaf.append((code, ko, en, cat))
    else:  # 7~9자리 = 중간 분류(상위 품명)
        parent[code] = (ko, en)

cats = sorted({c for *_, c in leaf if c})
cat_idx = {c: i for i, c in enumerate(cats)}

def with_parent(code, ko, en):
    # 가장 긴 상위 분류 이름을 앞에 붙여 '기타' 같은 품명에 맥락을 줌
    for n in (9, 8, 7):
        p = parent.get(code[:n])
        if p:
            return f"{p[0]} › {ko}", f"{p[1]} › {en}"
    return ko, en

data = []
for code, ko, en, cat in leaf:
    ko2, en2 = with_parent(code, ko, en)
    data.append([code, ko2, en2, cat_idx.get(cat, -1)])

out.parent.mkdir(exist_ok=True)
out.write_text(json.dumps({
    "source": "관세청 HS부호 (공공데이터포털)",
    "file": src.name,
    "valid_until": valid_until,
    "count": len(data),
    "cats": cats,
    "rows": data,
}, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
print(f"{len(data)} codes → {out} ({out.stat().st_size/1024:.0f} KB), valid until {valid_until}")
