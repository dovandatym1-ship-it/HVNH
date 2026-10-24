"""Lớp phủ toàn ảnh - Ảnh nền toàn slide + lớp phủ văn bản bán trong suốt"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from pptx.enum.shapes import MSO_SHAPE
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from python.base import TemplateGenerator
from python.utils import hex_to_rgb, set_shape_transparency


class FullImageOverlayGenerator(TemplateGenerator):
    """Bộ tạo lớp phủ toàn ảnh"""

    def __init__(self, theme=None):
        super().__init__(theme=theme)
        self.items = []
        self.title = "Lớp phủ toàn ảnh"
        self.overlay_color = hex_to_rgb("#000000")
        self.overlay_transparency = 0.55

    def set_title(self, title):
        self.title = title

    def set_items(self, items):
        """Thiết lập nội dung lớp phủ
        items: danh sách các dict với các khóa 'title', 'subtitle', 'description'
        Mỗi mục tương ứng với một trang slide.
        """
        self.items = items

    def generate(self):
        for i, item in enumerate(self.items):
            self.create_slide()
            self._add_full_background(i)
            self._add_overlay()
            self._add_text_content(i, item)
            self._add_bottom_bar()
        return self

    def _add_full_background(self, index):
        """Nền toàn slide (dùng màu đơn sắc + chuyển sắc mô phỏng ảnh nền)"""
        # Màu nền chuyển sắc cơ sở
        bg_colors = [
            [hex_to_rgb("#1A237E"), hex_to_rgb("#283593")],
            [hex_to_rgb("#004D40"), hex_to_rgb("#00695C")],
            [hex_to_rgb("#BF360C"), hex_to_rgb("#D84315")],
            [hex_to_rgb("#4A148C"), hex_to_rgb("#6A1B9A")],
        ]
        colors = bg_colors[index % len(bg_colors)]
        bg = self.add_gradient_shape(
            MSO_SHAPE.RECTANGLE,
            Inches(0), Inches(0),
            Inches(10), Inches(7.5),
            colors=colors,
        )

        # Khối hình học trang trí trên nền
        self.add_shape(
            MSO_SHAPE.OVAL,
            Inches(7), Inches(-1),
            Inches(4), Inches(4),
            fill_color=RGBColor(
                min(colors[0][0] + 20, 255),
                min(colors[0][1] + 20, 255),
                min(colors[0][2] + 20, 255),
            ),
        )
        self.add_shape(
            MSO_SHAPE.OVAL,
            Inches(-1), Inches(5),
            Inches(3), Inches(3),
            fill_color=RGBColor(
                min(colors[1][0] + 15, 255),
                min(colors[1][1] + 15, 255),
                min(colors[1][2] + 15, 255),
            ),
        )

    def _add_overlay(self):
        """Lớp phủ bán trong suốt"""
        overlay = self.add_shape(
            MSO_SHAPE.RECTANGLE,
            Inches(0), Inches(0),
            Inches(10), Inches(7.5),
            fill_color=self.overlay_color,
        )
        set_shape_transparency(overlay, self.overlay_transparency)

    def _add_text_content(self, index, item):
        """Thêm nội dung văn bản"""
        # Số trang lớn
        self.add_textbox(
            f"{index + 1:02d}",
            Inches(0.8), Inches(0.8),
            Inches(2), Inches(1),
            font_size=60, font_color=RGBColor(255, 255, 255),
            bold=True, alignment=PP_ALIGN.LEFT,
        )

        # Tiêu đề
        self.add_textbox(
            item.get("title", ""),
            Inches(0.8), Inches(2.2),
            Inches(8), Inches(1),
            font_size=36, font_color=RGBColor(255, 255, 255),
            bold=True, alignment=PP_ALIGN.LEFT,
        )

        # Đường phân cách
        self.add_shape(
            MSO_SHAPE.RECTANGLE,
            Inches(0.8), Inches(3.3),
            Inches(2), Inches(0.04),
            fill_color=hex_to_rgb("#FF6F00"),
        )

        # Tiêu đề phụ
        if item.get("subtitle"):
            self.add_textbox(
                item["subtitle"],
                Inches(0.8), Inches(3.6),
                Inches(8), Inches(0.5),
                font_size=20, font_color=RGBColor(255, 255, 255),
                alignment=PP_ALIGN.LEFT,
            )

        # Mô tả
        if item.get("description"):
            self.add_textbox(
                item["description"],
                Inches(0.8), Inches(4.3),
                Inches(7), Inches(2.5),
                font_size=14, font_color=RGBColor(220, 220, 220),
                alignment=PP_ALIGN.LEFT,
            )

        # Dấu ngoặc kép trang trí phong cách trích dẫn
        self.add_textbox(
            '"',
            Inches(0.5), Inches(2.0),
            Inches(0.5), Inches(0.6),
            font_size=48, font_color=hex_to_rgb("#FF6F00"),
            bold=True, alignment=PP_ALIGN.LEFT,
        )

    def _add_bottom_bar(self):
        """Thanh thông tin phía dưới"""
        bar = self.add_shape(
            MSO_SHAPE.RECTANGLE,
            Inches(0), Inches(6.8),
            Inches(10), Inches(0.7),
            fill_color=hex_to_rgb("#000000"),
        )
        set_shape_transparency(bar, 0.3)

        self.add_textbox(
            "CONFIDENTIAL  |  Tài liệu nội bộ",
            Inches(0.8), Inches(6.9),
            Inches(8), Inches(0.4),
            font_size=10, font_color=RGBColor(200, 200, 200),
            alignment=PP_ALIGN.LEFT,
        )


if __name__ == "__main__":
    gen = FullImageOverlayGenerator()
    gen.set_title("Lớp phủ toàn ảnh")
    gen.set_items([
        {
            "title": "Dẫn đầu chuyển đổi số",
            "subtitle": "Đổi mới nghiệp vụ bằng công nghệ tiên phong",
            "description": "Trong kỷ nguyên kinh tế số, chúng tôi cam kết trao quyền cho doanh nghiệp thông qua công nghệ hiện đại, hiện thực hóa nâng cấp số hóa toàn diện quy trình vận hành. Từ thu thập dữ liệu đến phân tích thông minh, từ tự động hóa quy trình đến tối ưu hóa quyết định, cung cấp giải pháp chuyển đổi số toàn diện từ đầu đến cuối.",
        },
        {
            "title": "Chiến lược vươn tầm toàn cầu",
            "subtitle": "Vững bước nội địa, hướng tới thế giới",
            "description": "Mạng lưới dịch vụ của chúng tôi hiện diện tại hơn 20 quốc gia và vùng lãnh thổ, phục vụ trên 500 khách hàng doanh nghiệp. Bằng vận hành bản địa hóa kết hợp hiệp đồng toàn cầu, chúng tôi mang đến giải pháp tùy chỉnh tối ưu cho từng thị trường.",
        },
        {
            "title": "Cam kết phát triển bền vững",
            "subtitle": "Công nghệ vị nhân sinh, kiến tạo tương lai xanh",
            "description": "Chúng tôi tin rằng công nghệ cần phụng sự sự phát triển bền vững của xã hội. Bằng cách tối ưu hóa hiệu quả năng lượng, giảm phát thải carbon và thúc đẩy kinh tế tuần hoàn, chúng tôi chung tay kiến tạo một tương lai xanh bền vững.",
        },
    ])
    gen.generate()
    output_path = os.path.join(os.path.dirname(__file__), '..', '..', 'output_full_image_overlay.pptx')
    gen.save(output_path)
    print(f"Đã lưu tại: {output_path}")
