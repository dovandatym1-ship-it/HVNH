#!/usr/bin/env python3
"""Sinh 6 bộ bài thuyết trình hoàn chỉnh trong thư mục templates/complete/.

generate_all.py chỉ phụ trách các mẫu đơn trang (32 loại × 7 chủ đề = 224 mẫu),
bài thuyết trình hoàn chỉnh do script này sinh riêng: mỗi kịch bản một bộ, không nhân theo chủ đề, vì vậy 224 + 6 = 230.

Script này cố định chủ đề, tiêu đề chính và tiêu đề phụ để 6 bộ bài thuyết trình có thể tái tạo 100%.

Cách chạy:
    python scripts/generate_decks.py
    python scripts/generate_decks.py --output ./out
"""

import argparse
import os
import sys
import time

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

from themes import ALL_THEMES

from python.generators_complete import (
    AnnualReportAssembler,
    BusinessPlanAssembler,
    CareerPlanningAssembler,
    EducationCourseAssembler,
    ProductLaunchAssembler,
    TechnologyThemeAssembler,
)

# (Tên tệp xuất, Bộ dựng, Tiêu đề chính, Khóa chủ đề)
DECKS = [
    ("annual_report", AnnualReportAssembler, "Annual Report Demo", "red_business"),
    ("business_plan", BusinessPlanAssembler, "Business Plan Demo", "blue_technology"),
    ("career_planning", CareerPlanningAssembler, "Career Planning Demo", "purple_gradient"),
    ("education_course", EducationCourseAssembler, "Education Course Demo", "green_nature"),
    ("product_launch", ProductLaunchAssembler, "Product Launch Demo", "ocean_blue"),
    ("technology_theme", TechnologyThemeAssembler, "Technology Theme Demo", "dark_gold"),
]

# 6 bộ bài thuyết trình dùng chung tiêu đề phụ
DEFAULT_SUBTITLE = "PPT Template Library"


def build(output_dir: str) -> int:
    os.makedirs(output_dir, exist_ok=True)

    success = 0
    for name, assembler_cls, title, theme_key in DECKS:
        start = time.time()
        filepath = os.path.join(output_dir, f"{name}.pptx")
        try:
            deck = assembler_cls(theme=ALL_THEMES[theme_key]())
            deck.set_title(title)
            deck.set_subtitle(DEFAULT_SUBTITLE)
            deck.generate()
            deck.save(filepath)
            success += 1
            print(f"  [OK] {title:<26} {os.path.basename(filepath):<28} {time.time() - start:.2f}s")
        except Exception as exc:  # Lỗi đơn lẻ không làm gián đoạn các bài thuyết trình khác
            print(f"  [FAIL] {title:<26} Lỗi: {exc}")

    print(f"\n  Hoàn thành {success}/{len(DECKS)} bộ, thư mục xuất: {output_dir}")
    return 0 if success == len(DECKS) else 1


def main() -> int:
    parser = argparse.ArgumentParser(description="Sinh 6 bộ bài thuyết trình hoàn chỉnh")
    parser.add_argument(
        "--output",
        default=os.path.join(project_root, "templates", "complete"),
        help="Thư mục xuất (mặc định templates/complete)",
    )
    args = parser.parse_args()

    print(f"\n  Đang sinh {len(DECKS)} bộ bài thuyết trình hoàn chỉnh...")
    return build(args.output)


if __name__ == "__main__":
    raise SystemExit(main())
