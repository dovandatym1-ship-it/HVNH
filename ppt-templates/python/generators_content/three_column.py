"""Bố cục ba cột - Ba cột đều nhau, gồm biểu tượng + tiêu đề + mô tả"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from pptx.enum.shapes import MSO_SHAPE
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from python.base import TemplateGenerator
from python.utils import hex_to_rgb, create_grid_positions


class ThreeColumnGenerator(TemplateGenerator):
    """Bộ tạo bố cục ba cột"""

    def __init__(self, theme=None):
        super().__init__(theme=theme)
        self.items = []
        self.title = "Bố cục ba cột"
        self.accent_colors = [
            hex_to_rgb("#1976D2"),
            hex_to_rgb("#388E3C"),
            hex_to_rgb("#F57C00"),
        ]
        self.bg_colors = [
            hex_to_rgb("#E3F2FD"),
            hex_to_rgb("#E8F5E9"),
            hex_to_rgb("#FFF3E0"),
        ]

    def set_title(self, title):
        self.title = title

    def set_items(self, items):
        """Thiết lập nội dung ba cột
        items: danh sách các dict với các khóa 'icon_text', 'title', 'description'
        Tối đa 3 mục.
        """
        self.items = items[:3]

    def generate(self):
        self.create_slide()
        self._add_background()
        self._add_title()
        self._add_subtitle_line()
        self._add_columns()
        return self

    def _add_background(self):
        self.add_shape(
            MSO_SHAPE.RECTANGLE,
            Inches(0), Inches(0),
            Inches(10), Inches(7.5),
            fill_color=hex_to_rgb("#FAFAFA"),
        )

    def _add_title(self):
        self.add_textbox(
            self.title,
            Inches(0.5), Inches(0.4), Inches(9), Inches(0.6),
            font_size=30, font_color=hex_to_rgb("#212121"),
            bold=True, alignment=PP_ALIGN.CENTER,
        )

    def _add_subtitle_line(self):
        # Đường trang trí dưới tiêu đề
        self.add_shape(
            MSO_SHAPE.RECTANGLE,
            Inches(4.3), Inches(1.1),
            Inches(1.4), Inches(0.04),
            fill_color=hex_to_rgb("#1976D2"),
        )

    def _add_columns(self):
        count = len(self.items)
        if count == 0:
            return

        col_w = Inches(2.6)
        col_h = Inches(4.8)
        gap = Inches(0.5)
        total_w = count * col_w + (count - 1) * gap
        start_x = (Inches(10) - total_w) // 2
        start_y = Inches(1.6)

        for i, item in enumerate(self.items):
            x = start_x + i * (col_w + gap)
            color = self.accent_colors[i % len(self.accent_colors)]
            bg_color = self.bg_colors[i % len(self.bg_colors)]

            # Thẻ cột
            card = self.add_shape(
                MSO_SHAPE.ROUNDED_RECTANGLE,
                x, start_y, col_w, col_h,
                fill_color=hex_to_rgb("#FFFFFF"),
                outline_color=hex_to_rgb("#E0E0E0"),
                outline_width=Pt(1),
            )

            # Dải màu trên cùng
            self.add_shape(
                MSO_SHAPE.RECTANGLE,
                x, start_y,
                col_w, Inches(0.06),
                fill_color=color,
            )

            # Vòng tròn biểu tượng
            icon_size = Inches(0.9)
            icon_x = x + (col_w - icon_size) // 2
            icon_y = start_y + Inches(0.5)
            self.add_shape(
                MSO_SHAPE.OVAL,
                icon_x, icon_y, icon_size, icon_size,
                fill_color=bg_color,
            )

            # Văn bản biểu tượng
            self.add_textbox(
                item.get("icon_text", str(i + 1)),
                icon_x, icon_y + Inches(0.15),
                icon_size, Inches(0.6),
                font_size=22, font_color=color,
                bold=True, alignment=PP_ALIGN.CENTER,
            )

            # Tiêu đề cột
            self.add_textbox(
                item.get("title", ""),
                x + Inches(0.15), start_y + Inches(1.7),
                col_w - Inches(0.3), Inches(0.4),
                font_size=16, font_color=hex_to_rgb("#212121"),
                bold=True, alignment=PP_ALIGN.CENTER,
            )

            # Đường phân cách
            self.add_shape(
                MSO_SHAPE.RECTANGLE,
                x + (col_w - Inches(0.8)) // 2, start_y + Inches(2.2),
                Inches(0.8), Inches(0.03),
                fill_color=color,
            )

            # Mô tả chi tiết
            self.add_textbox(
                item.get("description", ""),
                x + Inches(0.2), start_y + Inches(2.4),
                col_w - Inches(0.4), Inches(2.2),
                font_size=11, font_color=hex_to_rgb("#616161"),
                alignment=PP_ALIGN.CENTER,
            )


if __name__ == "__main__":
    gen = ThreeColumnGenerator()
    gen.set_title("Năng lực cốt lõi")
    gen.set_items([
        {
            "icon_text": "01",
            "title": "Định hướng dữ liệu",
            "description": "Ứng dụng phân tích dữ liệu lớn và học máy,\ncung cấp cho doanh nghiệp hiểu biết dữ liệu chuẩn xác,\nhỗ trợ tối ưu hóa quyết định và tăng trưởng kinh doanh.",
        },
        {
            "icon_text": "02",
            "title": "Đổi mới công nghệ",
            "description": "Liên tục đầu tư nghiên cứu và phát triển công nghệ tiên phong,\nduy trì vị thế dẫn đầu vượt trội,\nmang đến cho khách hàng các giải pháp tối ưu nhất.",
        },
        {
            "icon_text": "03",
            "title": "Dịch vụ tận tâm",
            "description": "Triết lý dịch vụ lấy khách hàng làm trọng tâm,\ncung cấp hỗ trợ kỹ thuật và tư vấn toàn diện,\nđảm bảo dự án được bàn giao thành công mỹ mãn.",
        },
    ])
    gen.generate()
    output_path = os.path.join(os.path.dirname(__file__), '..', '..', 'output_three_column.pptx')
    gen.save(output_path)
    print(f"Đã lưu tại: {output_path}")
