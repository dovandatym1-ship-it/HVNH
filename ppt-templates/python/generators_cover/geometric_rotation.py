"""Bộ sinh trang bìa xoay hình học

Tạo bìa với bố cục xoay gồm nhiều hình khối xếp chồng (hình chữ nhật, hình thoi),
mỗi hình sử dụng màu chuyển sắc kết hợp độ trong suốt, tiêu đề chính ở giữa, tiêu đề phụ ở dưới.
"""

import math
from pptx.enum.shapes import MSO_SHAPE
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from python.base import TemplateGenerator
from python.utils import hex_to_rgb, set_shape_transparency
from python.animation import apply_animations_to_slide


class GeometricRotationCover(TemplateGenerator):
    """Bìa xoay hình học"""

    # Màu chủ đề mặc định
    DEFAULT_PRIMARY = "#1A237E"
    DEFAULT_SECONDARY = "#283593"
    DEFAULT_ACCENT = "#3F51B5"
    DEFAULT_HIGHLIGHT = "#7986CB"
    DEFAULT_LIGHT = "#C5CAE9"

    def __init__(self, theme=None, **kwargs):
        super().__init__(theme=theme, **kwargs)
        self._title = "Bìa xoay hình học"
        self._subtitle = "Geometric Rotation Cover"

    def set_title(self, title):
        self._title = title
        return self

    def set_subtitle(self, subtitle):
        self._subtitle = subtitle
        return self

    def _get_color(self, attr, default_hex):
        """Lấy màu từ chủ đề, nếu không có thì dùng màu mặc định"""
        if self.theme and hasattr(self.theme, attr):
            return getattr(self.theme, attr)
        return hex_to_rgb(default_hex)

    def generate(self):
        """Sinh slide trang bìa xoay hình học"""
        self.create_slide()

        primary = self._get_color("primary", self.DEFAULT_PRIMARY)
        secondary = self._get_color("secondary", self.DEFAULT_SECONDARY)
        accent = self._get_color("accent", self.DEFAULT_ACCENT)
        highlight = self._get_color("highlight", self.DEFAULT_HIGHLIGHT)
        light = self._get_color("light", self.DEFAULT_LIGHT)

        slide_width = Inches(10)
        slide_height = Inches(7.5)
        center_x = slide_width // 2
        center_y = slide_height // 2

        # --- Nền chuyển sắc ---
        bg_shape = self.add_gradient_shape(
            MSO_SHAPE.RECTANGLE,
            0, 0, slide_width, slide_height,
            [primary, secondary],
            angle=45,
        )
        bg_shape_id = bg_shape.shape_id

        # --- Định nghĩa hình khối hình học (Bố cục xoay) ---
        # Tham số hình khối: (loại, lệch X so với tâm, lệch Y so với tâm, rộng, cao, góc xoay, màu tô, độ trong suốt)
        shapes_config = [
            (MSO_SHAPE.RECTANGLE, -1.2, -0.8, 3.5, 3.5, 15, accent, 0.60),
            (MSO_SHAPE.DIAMOND, 0.0, -1.0, 3.0, 3.0, 0, highlight, 0.50),
            (MSO_SHAPE.RECTANGLE, 1.0, -0.6, 2.8, 2.8, -20, light, 0.45),
            (MSO_SHAPE.DIAMOND, -0.8, 0.6, 2.5, 2.5, 30, accent, 0.55),
            (MSO_SHAPE.RECTANGLE, 0.6, 0.8, 3.2, 3.2, 45, highlight, 0.40),
            (MSO_SHAPE.DIAMOND, 0.0, 0.0, 2.0, 2.0, 0, light, 0.35),
            (MSO_SHAPE.RECTANGLE, -1.8, 0.2, 2.2, 2.2, -35, accent, 0.65),
            (MSO_SHAPE.DIAMOND, 1.5, -0.2, 1.8, 1.8, 60, highlight, 0.50),
        ]

        animations = []

        for i, (shape_type, off_x, off_y, w, h, rotation, color, transparency) in enumerate(shapes_config):
            left = center_x - Inches(w / 2) + Inches(off_x)
            top = center_y - Inches(h / 2) + Inches(off_y)
            width = Inches(w)
            height = Inches(h)

            shape = self.add_shape(shape_type, left, top, width, height)
            # Tô màu gradient
            shape.fill.gradient()
            shape.fill.gradient_stops[0].color.rgb = color
            shape.fill.gradient_stops[0].position = 0.0
            shape.fill.gradient_stops[1].color.rgb = primary
            shape.fill.gradient_stops[1].position = 1.0
            shape.line.fill.background()

            # Xoay hình khối
            if rotation != 0:
                from lxml import etree
                xfrm = shape._element.find('.//{http://schemas.openxmlformats.org/drawingml/2006/main}xfrm')
                if xfrm is not None:
                    xfrm.set('rot', str(int(rotation * 60000)))

            # Thiết lập độ trong suốt
            set_shape_transparency(shape, transparency)

            # Hoạt ảnh: fade_in tuần tự
            delay = i * 200
            animations.append((shape.shape_id, "fade_in", delay, 600))

        # --- Tiêu đề chính ---
        title_box = self.add_textbox(
            self._title,
            Inches(1.5), Inches(2.8), Inches(7.0), Inches(1.2),
            font_size=40,
            font_color=RGBColor(0xFF, 0xFF, 0xFF),
            bold=True,
            alignment=PP_ALIGN.CENTER,
            font_name="Microsoft YaHei",
        )
        title_box_id = title_box.shape_id
        animations.append((title_box_id, "fade_in", len(shapes_config) * 200 + 100, 700))

        # --- Tiêu đề phụ ---
        subtitle_box = self.add_textbox(
            self._subtitle,
            Inches(1.5), Inches(4.0), Inches(7.0), Inches(0.8),
            font_size=22,
            font_color=RGBColor(0xC5, 0xCA, 0xE9),
            bold=False,
            alignment=PP_ALIGN.CENTER,
            font_name="Microsoft YaHei",
        )
        subtitle_box_id = subtitle_box.shape_id
        animations.append((subtitle_box_id, "fade_in", len(shapes_config) * 200 + 300, 700))

        # --- Áp dụng hoạt ảnh ---
        apply_animations_to_slide(self.slide, animations)

        return self


if __name__ == "__main__":
    generator = GeometricRotationCover()
    generator.set_title("Bản trình diễn bìa xoay hình học").set_subtitle("Thiết kế bố cục hình học động")
    output = generator.generate().save("geometric_rotation_cover.pptx")
    print(f"Đã lưu: {output}")
