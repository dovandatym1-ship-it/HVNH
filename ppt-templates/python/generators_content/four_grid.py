"""Bố cục lưới 4 ô - Thẻ nội dung dạng lưới 2x2"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from pptx.enum.shapes import MSO_SHAPE
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from python.base import TemplateGenerator
from python.utils import hex_to_rgb, create_grid_positions, add_shadow


class FourGridGenerator(TemplateGenerator):
    """Bộ tạo bố cục lưới 4 ô"""

    def __init__(self, theme=None):
        super().__init__(theme=theme)
        self.items = []
        self.title = "Bố cục lưới 4 ô"
        self.colors = [
            hex_to_rgb("#2196F3"),
            hex_to_rgb("#4CAF50"),
            hex_to_rgb("#FF9800"),
            hex_to_rgb("#E91E63"),
        ]
        self.bg_colors = [
            hex_to_rgb("#E3F2FD"),
            hex_to_rgb("#E8F5E9"),
            hex_to_rgb("#FFF3E0"),
            hex_to_rgb("#FCE4EC"),
        ]

    def set_title(self, title):
        self.title = title

    def set_items(self, items):
        """Thiết lập nội dung lưới 4 ô
        items: danh sách các dict gồm các khóa 'number', 'title', 'description'
        Tối đa 4 mục.
        """
        self.items = items[:4]

    def generate(self):
        self.create_slide()
        self._add_background()
        self._add_title()
        self._add_grid()
        return self

    def _add_background(self):
        self.add_shape(
            MSO_SHAPE.RECTANGLE,
            Inches(0), Inches(0),
            Inches(10), Inches(7.5),
            fill_color=hex_to_rgb("#F5F5F5"),
        )

    def _add_title(self):
        self.add_textbox(
            self.title,
            Inches(0.5), Inches(0.3), Inches(9), Inches(0.6),
            font_size=28, font_color=hex_to_rgb("#333333"),
            bold=True, alignment=PP_ALIGN.CENTER,
        )

    def _add_grid(self):
        count = len(self.items)
        if count == 0:
            return

        card_w = Inches(4.0)
        card_h = Inches(2.6)
        gap = Inches(0.4)
        cols = 2

        positions = create_grid_positions(
            2, cols,
            start_x=(Inches(10) - (cols * card_w + (cols - 1) * gap)) // 2,
            start_y=Inches(1.2) + (Inches(6.0) - (2 * card_h + gap)) // 2,
            cell_width=card_w,
            cell_height=card_h,
            gap=gap,
        )

        for i, item in enumerate(self.items):
            if i >= len(positions):
                break
            x, y = positions[i]
            color = self.colors[i % len(self.colors)]
            bg_color = self.bg_colors[i % len(self.bg_colors)]

            # Nền thẻ
            card = self.add_shape(
                MSO_SHAPE.ROUNDED_RECTANGLE,
                x, y, card_w, card_h,
                fill_color=hex_to_rgb("#FFFFFF"),
            )
            add_shadow(card, blur=Pt(6), offset=Pt(2), opacity=0.12)

            # Thanh nhấn bên trái
            self.add_shape(
                MSO_SHAPE.RECTANGLE,
                x, y + Inches(0.15),
                Inches(0.06), card_h - Inches(0.3),
                fill_color=color,
            )

            # Vòng tròn số thứ tự
            circle_size = Inches(0.6)
            self.add_shape(
                MSO_SHAPE.OVAL,
                x + Inches(0.3), y + Inches(0.3),
                circle_size, circle_size,
                fill_color=bg_color,
            )
            self.add_textbox(
                item.get("number", str(i + 1)),
                x + Inches(0.3), y + Inches(0.35),
                circle_size, circle_size,
                font_size=18, font_color=color,
                bold=True, alignment=PP_ALIGN.CENTER,
            )

            # Tiêu đề
            self.add_textbox(
                item.get("title", ""),
                x + Inches(1.1), y + Inches(0.3),
                card_w - Inches(1.4), Inches(0.4),
                font_size=16, font_color=hex_to_rgb("#212121"),
                bold=True, alignment=PP_ALIGN.LEFT,
            )

            # Mô tả chi tiết
            self.add_textbox(
                item.get("description", ""),
                x + Inches(0.3), y + Inches(1.1),
                card_w - Inches(0.6), Inches(1.3),
                font_size=11, font_color=hex_to_rgb("#616161"),
                alignment=PP_ALIGN.LEFT,
            )

            # Họa tiết trang trí góc dưới bên phải
            self.add_shape(
                MSO_SHAPE.OVAL,
                x + card_w - Inches(0.8), y + card_h - Inches(0.8),
                Inches(0.6), Inches(0.6),
                fill_color=bg_color,
            )

    def _add_bottom_bar(self):
        # Thanh nhấn đáy tùy chọn
        self.add_shape(
            MSO_SHAPE.RECTANGLE,
            Inches(0), Inches(7.3),
            Inches(10), Inches(0.2),
            fill_color=hex_to_rgb("#1976D2"),
        )


if __name__ == "__main__":
    gen = FourGridGenerator()
    gen.set_title("Chỉ số trọng yếu")
    gen.set_items([
        {
            "number": "01",
            "title": "Tăng trưởng người dùng",
            "description": "Người dùng hoạt động hàng tháng (MAU) vượt mốc 1 triệu, tăng trưởng 45% so với cùng kỳ. Nhờ tiếp thị chuẩn xác và lan tỏa tự nhiên, chi phí thu hút người dùng giảm 30%.",
        },
        {
            "number": "02",
            "title": "Mục tiêu doanh thu",
            "description": "Doanh thu theo quý đạt 50 tỷ đồng, biên lợi nhuận nâng lên mức 25%. Các mảng kinh doanh mới đóng góp 35% tổng doanh thu.",
        },
        {
            "number": "03",
            "title": "Phát triển sản phẩm",
            "description": "Hoàn thành 3 đợt cập nhật phiên bản lớn, bổ sung hơn 20 mô-đun tính năng. Điểm số hài lòng của người dùng đạt mức 4.8/5.",
        },
        {
            "number": "04",
            "title": "Xây dựng đội ngũ",
            "description": "Đội ngũ nhân sự nòng cốt mở rộng lên 50 thành viên, nhân sự công nghệ chiếm 60%. Xây dựng lộ trình đào tạo và thăng tiến toàn diện.",
        },
    ])
    gen.generate()
    output_path = os.path.join(os.path.dirname(__file__), '..', '..', 'output_four_grid.pptx')
    gen.save(output_path)
    print(f"Đã lưu tại: {output_path}")
