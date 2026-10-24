"""
Ví dụ phối màu tùy chỉnh - Kho Mẫu Slide PPT

Ví dụ này minh họa cách tạo chủ đề màu tùy chỉnh và áp dụng vào các bộ sinh slide.
Cách chạy: python examples/custom_colors.py
"""

import sys
import os

# Đảm bảo thư mục gốc dự án nằm trong search path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from pptx.dml.color import RGBColor
from themes import BaseTheme, ALL_THEMES
from python.generators_cover import GeometricRotationCover, CircleRingCover, TrainMistCover
from python.generators_directory.diamond_animated import DiamondAnimatedGenerator


# ============================================================
# Cách 1: Kế thừa BaseTheme để tạo lớp chủ đề tùy chỉnh hoàn chỉnh
# ============================================================

class TechOrangeTheme(BaseTheme):
    """Chủ đề Cam công nghệ - Phù hợp với bài thuyết trình năng động, sáng tạo"""
    name = "Cam công nghệ"
    primary = RGBColor(255, 107, 53)    # #FF6B35
    secondary = RGBColor(255, 166, 43)  # #FFA62B
    accent = RGBColor(43, 87, 154)      # #2B579A
    background = RGBColor(250, 250, 250) # #FAFAFA
    text = RGBColor(40, 40, 40)         # #282828
    muted = RGBColor(140, 140, 140)     # #8C8C8C
    dark_bg = RGBColor(30, 30, 30)      # #1E1E1E


class ForestGreenTheme(BaseTheme):
    """Chủ đề Xanh rừng sâu - Phù hợp với môi trường, tự nhiên"""
    name = "Xanh rừng sâu"
    primary = RGBColor(34, 139, 87)     # #228B57
    secondary = RGBColor(107, 181, 132) # #6BB584
    accent = RGBColor(218, 165, 105)    # #DAA569
    background = RGBColor(248, 253, 248) # #F8FDF8
    text = RGBColor(33, 60, 42)         # #213C2A
    muted = RGBColor(120, 150, 130)     # #789682
    dark_bg = RGBColor(15, 30, 20)      # #0F1E14


# ============================================================
# Cách 2: Tạo chủ đề động tạm thời (không cần định nghĩa lớp mới)
# ============================================================

def create_dynamic_theme(name, primary_hex, secondary_hex, accent_hex=None):
    """Tạo nhanh đối tượng chủ đề tạm thời

    Bằng cách thiết lập động các thuộc tính lớp, tạo chủ đề mà không cần kế thừa BaseTheme tường minh.
    Phù hợp cho nhu cầu dùng thử một lần hoặc kiểm thử hàng loạt các bảng màu khác nhau.

    Args:
        name: Tên chủ đề
        primary_hex: Mã hex màu chính (ví dụ "#FF5733")
        secondary_hex: Mã hex màu phụ
        accent_hex: Mã hex màu nhấn (tùy chọn)

    Returns:
        Đối tượng thể hiện của BaseTheme
    """
    DynamicTheme = type(
        f"DynamicTheme_{name}",
        (BaseTheme,),
        {
            "name": name,
            "primary": _hex_to_rgb(primary_hex),
            "secondary": _hex_to_rgb(secondary_hex),
            "accent": _hex_to_rgb(accent_hex or primary_hex),
            "background": RGBColor(255, 255, 255),
            "text": RGBColor(33, 33, 33),
            "muted": RGBColor(158, 158, 158),
            "dark_bg": RGBColor(26, 26, 46),
        },
    )
    return DynamicTheme()


def _hex_to_rgb(hex_color):
    """Chuyển chuỗi màu hex thành RGBColor"""
    hex_color = hex_color.lstrip("#")
    return RGBColor(
        int(hex_color[0:2], 16),
        int(hex_color[2:4], 16),
        int(hex_color[4:6], 16),
    )


# ============================================================
# Phần chạy thử nghiệm
# ============================================================

def demo_existing_themes():
    """Hiển thị toàn bộ các chủ đề có sẵn"""
    print("\n--- Danh sách chủ đề có sẵn ---")
    for key, theme_cls in ALL_THEMES.items():
        theme = theme_cls()
        print(f"  {key}: {theme.name}  (Màu chính: {theme.primary})")


def demo_custom_class_theme():
    """Dùng lớp chủ đề tùy chỉnh để sinh trang bìa"""
    print("\n--- Dùng lớp chủ đề tùy chỉnh: Cam công nghệ ---")
    theme = TechOrangeTheme()

    cover = GeometricRotationCover(theme=theme)
    cover.set_title("Hội nghị Đổi mới Công nghệ")
    cover.set_subtitle("Innovation Tech Summit 2026")
    cover.generate()

    output = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "output_custom_orange.pptx")
    )
    cover.save(output)
    print(f"  Đã lưu: {output}")
    return output


def demo_dynamic_theme():
    """Dùng chủ đề động để sinh trang bìa"""
    print("\n--- Dùng chủ đề khởi tạo động ---")

    # Tạo một chủ đề Hồng san hô
    coral_theme = create_dynamic_theme(
        name="Hồng san hô",
        primary_hex="#FF6B6B",
        secondary_hex="#FFA07A",
        accent_hex="#FFD93D",
    )
    print(f"  Tên chủ đề: {coral_theme.name}")

    cover = CircleRingCover(theme=coral_theme)
    cover.set_title("Hồng san hô mơ mộng")
    cover.set_subtitle("Coral Pink Theme")
    cover.generate()

    output = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "output_custom_coral.pptx")
    )
    cover.save(output)
    print(f"  Đã lưu: {output}")
    return output


def demo_theme_comparison():
    """Cùng một mẫu sinh với các chủ đề khác nhau để so sánh kết quả"""
    print("\n--- So sánh chủ đề: Cùng một trang mục lục với các chủ đề khác nhau ---")

    items = [
        {"number": "01", "title": "Tổng quan dự án", "subtitle": "Overview"},
        {"number": "02", "title": "Phân tích thị trường", "subtitle": "Market"},
        {"number": "03", "title": "Thiết kế sản phẩm", "subtitle": "Design"},
        {"number": "04", "title": "Kế hoạch vận hành", "subtitle": "Operation"},
        {"number": "05", "title": "Dự báo tài chính", "subtitle": "Finance"},
        {"number": "06", "title": "Quản trị rủi ro", "subtitle": "Risk"},
    ]

    # Chọn một số chủ đề tiêu biểu để so sánh
    comparison_themes = [
        ("blue_technology", ALL_THEMES["blue_technology"]()),
        ("purple_gradient", ALL_THEMES["purple_gradient"]()),
        ("forest_green", ForestGreenTheme()),
    ]

    outputs = []
    for theme_key, theme in comparison_themes:
        gen = DiamondAnimatedGenerator(theme=theme)
        gen.set_title(f"{theme.name} - Mục lục")
        gen.set_items(items)
        gen.generate()

        output = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", f"output_theme_{theme_key}.pptx")
        )
        gen.save(output)
        outputs.append(output)
        print(f"  [{theme.name}] Đã lưu: {output}")

    return outputs


def main():
    """Hàm chính"""
    print("=" * 55)
    print("  Kho Mẫu Slide PPT - Ví dụ phối màu tùy chỉnh")
    print("=" * 55)

    # 1. Trình diễn chủ đề có sẵn
    demo_existing_themes()

    # 2. Chủ đề lớp tùy chỉnh
    demo_custom_class_theme()

    # 3. Chủ đề động
    demo_dynamic_theme()

    # 4. So sánh chủ đề
    demo_theme_comparison()

    print("\n" + "=" * 55)
    print("  Hoàn thành toàn bộ!")
    print("")
    print("  Hai cách tùy chỉnh chủ đề màu sắc:")
    print("  Cách 1: Kế thừa lớp BaseTheme, định nghĩa các thuộc tính lớp (Khuyên dùng, tái sử dụng cao)")
    print("  Cách 2: Sử dụng hàm create_dynamic_theme() (Phù hợp dùng một lần)")
    print("")
    print("  Gợi ý: Đối tượng chủ đề chỉ cần chứa các thuộc tính:")
    print("  primary, secondary, accent, background, text, muted, dark_bg.")
    print("=" * 55)


if __name__ == "__main__":
    main()
