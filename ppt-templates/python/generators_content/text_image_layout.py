"""Bố cục hình ảnh và văn bản - Bố cục ảnh trái chữ phải / ảnh phải chữ trái"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from pptx.enum.shapes import MSO_SHAPE
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from python.base import TemplateGenerator
from python.utils import hex_to_rgb


class TextImageLayoutGenerator(TemplateGenerator):
    """Bộ tạo bố cục hình ảnh và văn bản"""

    def __init__(self, theme=None):
        super().__init__(theme=theme)
        self.items = []
        self.title = "Bố cục hình ảnh và văn bản"
        self.accent_color = hex_to_rgb("#1976D2")

    def set_title(self, title):
        self.title = title

    def set_items(self, items):
        """Thiết lập các mục nội dung
        items: danh sách các dict với các khóa 'title', 'description', 'image' (tùy chọn)
        """
        self.items = items

    def generate(self):
        for i, item in enumerate(self.items):
            self.create_slide()
            self._add_background()
            self._add_title_bar(i + 1)
            if i % 2 == 0:
                self._add_left_image(i, item)
            else:
                self._add_right_image(i, item)
        return self

    def _add_background(self):
        self.add_shape(
            MSO_SHAPE.RECTANGLE,
            Inches(0), Inches(0),
            Inches(10), Inches(7.5),
            fill_color=hex_to_rgb("#FFFFFF"),
        )

    def _add_title_bar(self, page_num):
        # Thanh nhấn trên cùng
        self.add_shape(
            MSO_SHAPE.RECTANGLE,
            Inches(0), Inches(0),
            Inches(10), Inches(0.06),
            fill_color=self.accent_color,
        )
        # Số trang
        self.add_textbox(
            f"{page_num:02d}",
            Inches(0.5), Inches(0.3),
            Inches(1), Inches(0.5),
            font_size=36, font_color=hex_to_rgb("#E0E0E0"),
            bold=True, alignment=PP_ALIGN.LEFT,
        )

    def _add_left_image(self, index, item):
        """Bố cục ảnh bên trái, chữ bên phải"""
        # Khung giữ chỗ ảnh (bên trái)
        img_x, img_y = Inches(0.5), Inches(1.2)
        img_w, img_h = Inches(4.5), Inches(5.5)

        img_shape = self.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            img_x, img_y, img_w, img_h,
            fill_color=hex_to_rgb("#E3F2FD"),
            outline_color=hex_to_rgb("#BBDEFB"),
            outline_width=Pt(1),
        )

        # Biểu tượng ảnh giữ chỗ
        icon_size = Inches(1.0)
        self.add_shape(
            MSO_SHAPE.OVAL,
            img_x + (img_w - icon_size) // 2,
            img_y + (img_h - icon_size) // 2,
            icon_size, icon_size,
            fill_color=hex_to_rgb("#BBDEFB"),
        )
        self.add_textbox(
            "IMG",
            img_x + (img_w - icon_size) // 2,
            img_y + (img_h - icon_size) // 2 + Inches(0.2),
            icon_size, Inches(0.5),
            font_size=14, font_color=hex_to_rgb("#1976D2"),
            bold=True, alignment=PP_ALIGN.CENTER,
        )

        # Khu vực văn bản (bên phải)
        text_x = Inches(5.5)
        text_w = Inches(4.0)

        # Đường dọc nhấn
        self.add_shape(
            MSO_SHAPE.RECTANGLE,
            text_x - Inches(0.15), Inches(1.5),
            Inches(0.05), Inches(1.0),
            fill_color=self.accent_color,
        )

        # Tiêu đề
        self.add_textbox(
            item.get("title", ""),
            text_x, Inches(1.5), text_w, Inches(0.5),
            font_size=24, font_color=hex_to_rgb("#212121"),
            bold=True, alignment=PP_ALIGN.LEFT,
        )

        # Mô tả
        self.add_textbox(
            item.get("description", ""),
            text_x, Inches(2.2), text_w, Inches(3.5),
            font_size=14, font_color=hex_to_rgb("#616161"),
            alignment=PP_ALIGN.LEFT,
        )

        # Các chấm trang trí phía dưới
        for j in range(3):
            self.add_shape(
                MSO_SHAPE.OVAL,
                text_x + j * Inches(0.25), Inches(6.2),
                Inches(0.08), Inches(0.08),
                fill_color=self.accent_color,
            )

    def _add_right_image(self, index, item):
        """Bố cục ảnh bên phải, chữ bên trái"""
        # Khu vực văn bản (bên trái)
        text_x = Inches(0.5)
        text_w = Inches(4.0)

        # Đường dọc nhấn
        self.add_shape(
            MSO_SHAPE.RECTANGLE,
            text_x, Inches(1.5),
            Inches(0.05), Inches(1.0),
            fill_color=self.accent_color,
        )

        # Tiêu đề
        self.add_textbox(
            item.get("title", ""),
            text_x + Inches(0.2), Inches(1.5), text_w, Inches(0.5),
            font_size=24, font_color=hex_to_rgb("#212121"),
            bold=True, alignment=PP_ALIGN.LEFT,
        )

        # Mô tả
        self.add_textbox(
            item.get("description", ""),
            text_x + Inches(0.2), Inches(2.2), text_w, Inches(3.5),
            font_size=14, font_color=hex_to_rgb("#616161"),
            alignment=PP_ALIGN.LEFT,
        )

        # Khung giữ chỗ ảnh (bên phải)
        img_x, img_y = Inches(5.0), Inches(1.2)
        img_w, img_h = Inches(4.5), Inches(5.5)

        img_shape = self.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            img_x, img_y, img_w, img_h,
            fill_color=hex_to_rgb("#FFF3E0"),
            outline_color=hex_to_rgb("#FFE0B2"),
            outline_width=Pt(1),
        )

        # Biểu tượng ảnh giữ chỗ
        icon_size = Inches(1.0)
        self.add_shape(
            MSO_SHAPE.OVAL,
            img_x + (img_w - icon_size) // 2,
            img_y + (img_h - icon_size) // 2,
            icon_size, icon_size,
            fill_color=hex_to_rgb("#FFE0B2"),
        )
        self.add_textbox(
            "IMG",
            img_x + (img_w - icon_size) // 2,
            img_y + (img_h - icon_size) // 2 + Inches(0.2),
            icon_size, Inches(0.5),
            font_size=14, font_color=hex_to_rgb("#E65100"),
            bold=True, alignment=PP_ALIGN.CENTER,
        )

        # Các chấm trang trí phía dưới
        for j in range(3):
            self.add_shape(
                MSO_SHAPE.OVAL,
                text_x + Inches(0.2) + j * Inches(0.25), Inches(6.2),
                Inches(0.08), Inches(0.08),
                fill_color=self.accent_color,
            )


if __name__ == "__main__":
    gen = TextImageLayoutGenerator()
    gen.set_title("Giới thiệu sản phẩm")
    gen.set_items([
        {
            "title": "Nền tảng phân tích thông minh",
            "description": "Nền tảng phân tích dữ liệu trên nền trí tuệ nhân tạo, hỗ trợ giám sát dữ liệu thời gian thực,\ndự báo thông minh và tự động tạo báo cáo.\n\nTương thích nhiều nguồn dữ liệu, tùy biến bảng điều khiển trực quan,\nquản trị nhóm và phân quyền chuyên nghiệp.",
        },
        {
            "title": "Ứng dụng di động",
            "description": "Ứng dụng di động đa nền tảng, hỗ trợ tối ưu trên cả hệ điều hành iOS và Android.\n\nHỗ trợ chế độ ngoại tuyến, thông báo đẩy, đồng bộ dữ liệu tức thời,\nmang đến trải nghiệm mượt mà cùng giao diện thân thiện.",
        },
        {
            "title": "Dịch vụ đám mây",
            "description": "Kiến trúc đám mây độ sẵn sàng cao với cam kết SLA 99.99%.\n\nTự động co giãn theo tải, thanh toán linh hoạt theo nhu cầu thực tế,\nbảo mật chuẩn doanh nghiệp kết hợp mã hóa dữ liệu đa lớp.",
        },
    ])
    gen.generate()
    output_path = os.path.join(os.path.dirname(__file__), '..', '..', 'output_text_image_layout.pptx')
    gen.save(output_path)
    print(f"Đã lưu tại: {output_path}")
