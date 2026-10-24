#!/usr/bin/env python3
"""Kiểm tra tính nhất quán trong hợp đồng giữa Python và TypeScript.

Triển khai song ngữ là nguồn chi phí bảo trì chính của dự án này. Script này thực hiện kiểm tra 3 cấp độ trong CI:

1. Đối đẳng số lượng: Số lượng bộ sinh của mỗi họ ở cả hai phía phải như nhau
2. Ánh xạ tên lớp: Mỗi lớp Python đều có thể ánh xạ sang lớp TS theo quy tắc hoặc bảng ngoại lệ; thất bại nếu không ánh xạ được
3. Nhất quán màu chủ đề: 7 bộ chủ đề so khớp tên và 7 mã màu từng mục một, thất bại nếu có bất kỳ điểm nào không khớp

Khác biệt đã biết và được cố ý giữ lại (chỉ ghi chú, không đánh giá thất bại):
- Tỷ lệ khung hình: Lớp cơ sở Python là 10x7.5 inch (4:3), lớp cơ sở TS là 13.33x7.5 inch (16:9).
  Tọa độ hơn 230 mẫu phía Python thiết kế theo 4:3, việc đồng nhất kích thước cần chỉnh lại bố cục (xem FAQ trong README).

Cách dùng:
    python scripts/check_parity.py
Mã thoát 0 nghĩa là nhất quán, 1 nghĩa là có sự sai lệch.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

FAMILIES = [
    "chart",
    "complete",
    "content",
    "cover",
    "directory",
    "ending",
    "team",
    "timeline",
]

PY_CLASS_RE = re.compile(r"^class\s+(\w+)", re.MULTILINE)
TS_CLASS_RE = re.compile(r"^export\s+class\s+(\w+)", re.MULTILINE)

# Khác biệt tên lớp song ngữ không thể bao phủ bằng quy tắc (Tên Python -> Tên TS)
CLASS_NAME_EXCEPTIONS = {
    "AnimatedBarChart": "AnimatedChart",
}

# Quy tắc ánh xạ tên lớp: lặp bóc tách hậu tố cho đến khi không đổi (XxxGenerator -> Xxx, XxxCover -> Xxx,
# XxxTimeline -> Xxx, ContactPageGenerator -> ContactPage -> Contact), trùng tên giữ nguyên
SUFFIXES = ("Generator", "Assembler", "Cover", "Timeline", "Page")

# Quan hệ đối ứng khóa chủ đề giữa 2 phía (Tên thuộc tính Python -> Tên thuộc tính TS)
THEME_KEYS = ["primary", "secondary", "accent", "background", "text", "muted", "dark_bg"]
TS_KEY_OF = {k: ("darkBg" if k == "dark_bg" else k) for k in THEME_KEYS}

# Tên tệp chủ đề Python -> Tên biến xuất TS
THEME_FILES = {
    "blue_technology": "blueTechnology",
    "purple_gradient": "purpleGradient",
    "dark_gold": "darkGold",
    "minimalist_bw": "minimalistBW",
    "ocean_blue": "oceanBlue",
    "green_nature": "greenNature",
    "red_business": "redBusiness",
}

PY_THEME_RE = re.compile(r"^\s*(\w+)\s*=\s*RGBColor\((\d+),\s*(\d+),\s*(\d+)\)", re.MULTILINE)
PY_NAME_RE = re.compile(r'^\s*name\s*=\s*"([^"]+)"', re.MULTILINE)
TS_THEME_RE = re.compile(r"(\w+):\s*'([0-9A-Fa-f]{6})'", re.MULTILINE)
TS_NAME_RE = re.compile(r"name:\s*'([^']+)'", re.MULTILINE)


def python_classes(family: str) -> list[str]:
    pkg = ROOT / "python" / f"generators_{family}"
    if not pkg.is_dir():
        return []
    names: list[str] = []
    for path in sorted(pkg.glob("*.py")):
        if path.name == "__init__.py":
            continue
        names.extend(PY_CLASS_RE.findall(path.read_text(encoding="utf-8")))
    return sorted(names)


def typescript_classes(family: str) -> list[str]:
    path = ROOT / "js" / "src" / "generators" / f"{family}.ts"
    if not path.is_file():
        return []
    return sorted(TS_CLASS_RE.findall(path.read_text(encoding="utf-8")))


def py_to_ts_class(name: str) -> str:
    """Ánh xạ tên lớp Python sang tên lớp TS theo quy tắc, ngoại lệ tra bảng tường minh."""
    if name in CLASS_NAME_EXCEPTIONS:
        return CLASS_NAME_EXCEPTIONS[name]
    changed = True
    while changed:
        changed = False
        for suffix in SUFFIXES:
            if name.endswith(suffix):
                name = name[: -len(suffix)]
                changed = True
    return name


def parse_python_themes() -> dict[str, dict]:
    """Phân tích cú pháp name và giá trị RGBColor trong themes/*.py thành chuỗi hex."""
    themes = {}
    for stem, _ in THEME_FILES.items():
        path = ROOT / "themes" / f"{stem}.py"
        src = path.read_text(encoding="utf-8")
        entry: dict[str, str] = {}
        m = PY_NAME_RE.search(src)
        if m:
            entry["name"] = m.group(1)
        for key, r, g, b in PY_THEME_RE.findall(src):
            if key in THEME_KEYS:
                entry[key] = f"{int(r):02X}{int(g):02X}{int(b):02X}"
        themes[stem] = entry
    return themes


def parse_typescript_themes() -> dict[str, dict]:
    """Phân tích 7 đối tượng chủ đề trong js/src/themes/index.ts."""
    src = (ROOT / "js" / "src" / "themes" / "index.ts").read_text(encoding="utf-8")
    themes = {}
    for stem, var in THEME_FILES.items():
        m = re.search(rf"export const {var}: Theme = \{{(.*?)\}};", src, re.DOTALL)
        if not m:
            themes[stem] = {}
            continue
        body = m.group(1)
        entry: dict[str, str] = {}
        mn = TS_NAME_RE.search(body)
        if mn:
            entry["name"] = mn.group(1)
        for key, hexv in TS_THEME_RE.findall(body):
            py_key = [pk for pk, tk in TS_KEY_OF.items() if tk == key]
            if py_key:
                entry[py_key[0]] = hexv.upper()
        themes[stem] = entry
    return themes


def main() -> int:
    failed = False
    total_py = total_ts = 0

    print(f"{'Nhóm bộ sinh':<14}{'Python':>8}{'TS':>8}{'Trạng thái':>12}")
    print("-" * 44)

    # ---- 1+2. Số lượng và ánh xạ tên lớp ----
    for family in FAMILIES:
        py = python_classes(family)
        ts = typescript_classes(family)
        total_py += len(py)
        total_ts += len(ts)

        ts_set = set(ts)
        unmapped = [name for name in py if py_to_ts_class(name) not in ts_set]
        mapped_ts = {py_to_ts_class(p) for p in py}
        extra = [name for name in ts if name not in mapped_ts]

        if len(py) == len(ts) and not unmapped and not extra:
            status = "OK"
        else:
            status = "Không khớp"
            failed = True

        print(f"{family:<14}{len(py):>8}{len(ts):>8}{status:>12}")
        if unmapped:
            print(f"    Phía Python không ánh xạ được sang TS: {', '.join(unmapped)}")
        if extra:
            print(f"    Phía TS thiếu lớp Python tương ứng: {', '.join(extra)}")

    print("-" * 44)
    print(f"{'Tổng cộng':<14}{total_py:>8}{total_ts:>8}")

    # ---- 3. Tính nhất quán của chủ đề ----
    py_themes = parse_python_themes()
    ts_themes = parse_typescript_themes()
    print("\nTính nhất quán chủ đề (Python themes/*.py vs js/src/themes/index.ts)")
    for stem in THEME_FILES:
        p, t = py_themes.get(stem, {}), ts_themes.get(stem, {})
        diffs = [k for k in ["name"] + THEME_KEYS if p.get(k) != t.get(k)]
        if diffs:
            theme_bad = True
            failed = True
            print(f"  [LỖI] {stem}: Mục không khớp {', '.join(diffs)}")
            for k in diffs:
                print(f"         {k}: Python={p.get(k)}  TS={t.get(k)}")
        else:
            print(f"  [OK]   {stem}")

    # ---- Ghi chú khác biệt đã biết (không đánh giá lỗi) ----
    print("\nKhác biệt đã biết (chỉ ghi chú)")
    print("  [CẢNH BÁO] Tỷ lệ khung hình: Python 10x7.5 inch (4:3) vs TS 13.33x7.5 inch (16:9).")
    print("             Tọa độ mẫu phía Python thiết kế theo 4:3, việc đồng nhất cần căn chỉnh lại bố cục (xem FAQ trong README).")

    if failed:
        print("\n[LỖI] Hợp đồng song ngữ có điểm sai lệch, vui lòng hoàn thiện phía bị thiếu.", file=sys.stderr)
        return 1

    print(f"\n[OK] Hợp đồng song ngữ hoàn toàn nhất quán: {total_py} bộ sinh, 7 bộ chủ đề đã khớp từng mục.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
