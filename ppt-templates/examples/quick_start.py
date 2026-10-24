"""
Ví dụ bắt đầu nhanh - Kho Mẫu Slide PPT

Ví dụ này minh họa cách tạo nhanh một bản trình bày đơn giản gồm trang bìa, trang nội dung và trang kết thúc.
Cách chạy: python examples/quick_start.py
"""

import sys
import os

# Đảm bảo thư mục gốc của dự án nằm trong sys.path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from pptx.enum.shapes import MSO_SHAPE
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

from python.base import TemplateGenerator
from python.generators_cover import GeometricRotationCover, DiamondRevealCover
from themes import ALL_THEMES


def create_simple_content_page(theme, title, content_items):
    """Tạo một trang nội dung súc tích

    Args:
        theme: Đối tượng chủ đề
        title: Tiêu đề trang
        content_items: Danh sách nội dung, mỗi mục là một chuỗi

    Returns:
        TemplateGenerator: Thể hiện generator (dùng để gọi chuỗi save)
    """
    gen = TemplateGenerator(theme=theme)
    gen.create_slide()

    slide_w = Inches(10)
    slide_h = Inches(7.5)

    # Lấy màu chủ đề (ưu tiên chủ đề, nếu không dùng màu mặc định)
    primary = getattr(theme, "primary", RGBColor(0, 102, 204))
    text_color = getattr(theme, "text", RGBColor(33, 33, 33))
    muted = getattr(theme, "muted", RGBColor(158, 158, 158))

    # Màu nền (lấy màu nền chủ đề, mặc định màu trắng)
    bg_color = getattr(theme, "background", RGBColor(255, 255, 255))

    # Vẽ nền
    gen.add_shape(
        MSO_SHAPE.RECTANGLE, 0, 0, slide_w, slide_h,
        fill_color=bg_color,
    )

    # Thanh trang trí phía trên
    gen.add_gradient_shape(
        MSO_SHAPE.RECTANGLE,
        0, 0, slide_w, Inches(0.06),
        [primary, getattr(theme, "secondary", primary)],
    )

    # Tiêu đề
    gen.add_textbox(
        title,
        Inches(0.8), Inches(0.5), Inches(8.4), Inches(0.8),
        font_size=28,
        font_color=text_color,
        bold=True,
        alignment=PP_ALIGN.LEFT,
    )

    # Đường phân cách trang trí
    gen.add_shape(
        MSO_SHAPE.RECTANGLE,
        Inches(0.8), Inches(1.35), Inches(1.2), Inches(0.04),
        fill_color=primary,
    )

    # Các mục nội dung
    y_start = Inches(1.8)
    for i, item in enumerate(content_items):
        y_pos = y_start + Inches(i * 0.65)

        # Chấm tròn đánh số
        dot_size = Inches(0.35)
        gen.add_shape(
            MSO_SHAPE.OVAL,
            Inches(1.0), y_pos, dot_size, dot_size,
            fill_color=primary,
        )
        # Số thứ tự
        gen.add_textbox(
            str(i + 1),
            Inches(1.0), y_pos + Inches(0.02),
            dot_size, dot_size,
            font_size=14,
            font_color=RGBColor(255, 255, 255),
            bold=True,
            alignment=PP_ALIGN.CENTER,
        )

        # Nội dung chữ
        gen.add_textbox(
            item,
            Inches(1.6), y_pos + Inches(0.03),
            Inches(7.5), Inches(0.35),
            font_size=16,
            font_color=text_color,
        )

    return gen


def create_simple_ending(theme, title="Xin chân thành cảm ơn", subtitle="Thank You"):
    """Tạo một trang kết thúc tinh gọn

    Args:
        theme: Đối tượng chủ đề
        title: Tiêu đề chính
        subtitle: Tiêu đề phụ

    Returns:
        TemplateGenerator: Thể hiện generator
    """
    gen = TemplateGenerator(theme=theme)
    gen.create_slide()

    slide_w = Inches(10)
    slide_h = Inches(7.5)

    primary = getattr(theme, "primary", RGBColor(0, 102, 204))
    secondary = getattr(theme, "secondary", primary)
    dark_bg = getattr(theme, "dark_bg", RGBColor(26, 26, 46))

    # Nền chuyển sắc màu tối
    gen.add_gradient_shape(
        MSO_SHAPE.RECTANGLE,
        0, 0, slide_w, slide_h,
        [dark_bg, primary],
    )

    # Vòng tròn trang trí
    gen.add_shape(
        MSO_SHAPE.OVAL,
        Inches(3.5), Inches(2.0), Inches(3.0), Inches(3.0),
        fill_color=secondary,
    )
    # Thêm độ trong suốt cho vòng tròn
    from python.utils import set_shape_transparency
    circle = gen.slide.shapes[-1]
    set_shape_transparency(circle, 0.85)

    # Tiêu đề chính
    gen.add_textbox(
        title,
        Inches(1.5), Inches(2.5), Inches(7.0), Inches(1.2),
        font_size=42,
        font_color=RGBColor(255, 255, 255),
        bold=True,
        alignment=PP_ALIGN.CENTER,
    )

    # Tiêu đề phụ
    gen.add_textbox(
        subtitle,
        Inches(1.5), Inches(3.8), Inches(7.0), Inches(0.6),
        font_size=20,
        font_color=getattr(theme, "muted", RGBColor(180, 180, 180)),
        alignment=PP_ALIGN.CENTER,
    )

    return gen


def main():
    """Hàm chính: Sinh một bản trình bày đơn giản hoàn chỉnh"""
    print("=" * 50)
    print("  Kho Mẫu Slide PPT - Ví dụ bắt đầu nhanh")
    print("=" * 50)

    # ---- Bước 1: Chọn chủ đề ----
    # Các chủ đề sẵn có: blue_technology, purple_gradient, dark_gold,
    #                    minimalist_bw, ocean_blue, green_nature, red_business
    theme_name = "blue_technology"
    theme = ALL_THEMES[theme_name]()
    print(f"\n[1/4] Đã chọn chủ đề: {theme.name}")

    # ---- Bước 2: Sinh trang bìa ----
    print("[2/4] Đang sinh trang bìa...")
    cover = GeometricRotationCover(theme=theme)
    cover.set_title("Trình diễn mẫu PPT")
    cover.set_subtitle("Bắt đầu nhanh · Quick Start")
    cover.generate()
    cover_path = os.path.join(os.path.dirname(__file__), "..", "output_quick_cover.pptx")
    cover_path = os.path.abspath(cover_path)
    cover.save(cover_path)
    print(f"       Trang bìa đã lưu: {cover_path}")

    # ---- Bước 3: Sinh trang nội dung ----
    print("[3/4] Đang sinh trang nội dung...")
    content = create_simple_content_page(
        theme,
        "Tổng quan dự án",
        [
            "Bối cảnh & Mục tiêu dự án: Định hướng rõ ràng, tập trung vào giá trị cốt lõi",
            "Thiết kế kiến trúc kỹ thuật: Tính module hóa, dễ mở rộng, tính sẵn sàng cao",
            "Kế hoạch triển khai: Triển khai theo giai đoạn, đảm bảo tiến độ bàn giao",
            "Phân công đội ngũ: Phối hợp liên phòng ban, phân định trách nhiệm rõ ràng",
            "Kiểm soát rủi ro: Nhận diện rủi ro sớm, thiết lập phương án đối phó",
            "Kết quả kỳ vọng: Mục tiêu định lượng cụ thể, tối ưu hóa hiệu quả đầu tư",
        ],
    )
    content_path = os.path.join(os.path.dirname(__file__), "..", "output_quick_content.pptx")
    content_path = os.path.abspath(content_path)
    content.save(content_path)
    print(f"       Trang nội dung đã lưu: {content_path}")

    # ---- Bước 4: Sinh trang kết thúc ----
    print("[4/4] Đang sinh trang kết thúc...")
    ending = create_simple_ending(theme, "Xin chân thành cảm ơn", "Thank You for Watching")
    ending_path = os.path.join(os.path.dirname(__file__), "..", "output_quick_ending.pptx")
    ending_path = os.path.abspath(ending_path)
    ending.save(ending_path)
    print(f"       Trang kết thúc đã lưu: {ending_path}")

    # ---- Tổng kết ----
    print("\n" + "=" * 50)
    print("  Hoàn thành! Đã sinh 3 tệp mẫu:")
    print(f"  1. {os.path.basename(cover_path)}")
    print(f"  2. {os.path.basename(content_path)}")
    print(f"  3. {os.path.basename(ending_path)}")
    print("")
    print("  Gợi ý: Bạn có thể ghép các trang này thành một bài thuyết trình,")
    print("  hoặc sử dụng từng trang riêng lẻ làm mẫu thiết kế.")
    print("=" * 50)


if __name__ == "__main__":
    main()
