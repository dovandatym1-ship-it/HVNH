"""Bộ tạo slide cảm ơn

Chữ "Xin cảm ơn" cỡ lớn căn giữa, họa tiết hình học tinh tế, thông tin liên hệ phía dưới, tạo nên phần kết thúc trang nhã và thanh lịch.
"""

from pptx.enum.shapes import MSO_SHAPE
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from python.base import TemplateGenerator
from python.utils import hex_to_rgb, set_shape_transparency
from python.animation import apply_animations_to_slide


class ThankYouGenerator(TemplateGenerator):
    """Trang cảm ơn"""

    DEFAULT_PRIMARY = "#1A237E"
    DEFAULT_SECONDARY = "#283593"
    DEFAULT_ACCENT = "#3F51B5"
    DEFAULT_LIGHT = "#C5CAE9"
    DEFAULT_BG = "#F5F7FA"
    DEFAULT_TEXT_DARK = "#212121"
    DEFAULT_TEXT_MID = "#555555"

    def __init__(self, theme=None, **kwargs):
        super().__init__(theme=theme, **kwargs)
        self._title = "Xin cảm ơn"
        self._subtitle = "Thank You"
        self._contact_line = "Liên hệ với chúng tôi: contact@example.com"
        self._slogan = "Rất hân hạnh được hợp tác cùng Quý đối tác"

    def set_data(self, title=None, subtitle=None, contact_line=None, slogan=None):
        """Thiết lập dữ liệu trang cảm ơn"""
        if title is not None:
            self._title = title
        if subtitle is not None:
            self._subtitle = subtitle
        if contact_line is not None:
            self._contact_line = contact_line
        if slogan is not None:
            self._slogan = slogan
        return self

    def _get_color(self, attr, default_hex):
        if self.theme and hasattr(self.theme, attr):
            return getattr(self.theme, attr)
        return hex_to_rgb(default_hex)

    def generate(self):
        """Tạo trang cảm ơn"""
        self.create_slide()

        primary = self._get_color("primary", self.DEFAULT_PRIMARY)
        secondary = self._get_color("secondary", self.DEFAULT_SECONDARY)
        accent = self._get_color("accent", self.DEFAULT_ACCENT)
        light = self._get_color("light", self.DEFAULT_LIGHT)

        slide_w = Inches(10)
        slide_h = Inches(7.5)
        center_x = slide_w // 2
        center_y = slide_h // 2

        animations = []

        # --- Nền chuyển sắc ---
        bg = self.add_gradient_shape(
            MSO_SHAPE.RECTANGLE,
            0, 0, slide_w, slide_h,
            [primary, secondary],
            angle=135,
        )
        animations.append((bg.shape_id, "fade_in", 0, 600))

        # --- Họa tiết hình học trang trí ---
        # Khung hình thoi mờ lớn (khu vực trên bên trái)
        deco1 = self.add_shape(
            MSO_SHAPE.DIAMOND,
            Inches(0.5), Inches(0.5), Inches(2.0), Inches(2.0),
        )
        deco1.fill.background()
        deco1.line.color.rgb = light
        deco1.line.width = Pt(1.5)
        set_shape_transparency(deco1, 0.6)
        animations.append((deco1.shape_id, "fade_in", 100, 600))

        # Hình thoi nhỏ gần góc trên bên trái
        deco2 = self.add_shape(
            MSO_SHAPE.DIAMOND,
            Inches(1.5), Inches(1.0), Inches(0.6), Inches(0.6),
            fill_color=accent,
        )
        set_shape_transparency(deco2, 0.5)
        animations.append((deco2.shape_id, "fade_in", 150, 500))

        # Khung tròn trang trí (khu vực trên bên phải)
        deco3 = self.add_shape(
            MSO_SHAPE.OVAL,
            Inches(7.8), Inches(0.3), Inches(1.8), Inches(1.8),
        )
        deco3.fill.background()
        deco3.line.color.rgb = light
        deco3.line.width = Pt(1.2)
        set_shape_transparency(deco3, 0.55)
        animations.append((deco3.shape_id, "fade_in", 200, 600))

        # Hình thoi nhỏ (khu vực dưới bên phải)
        deco4 = self.add_shape(
            MSO_SHAPE.DIAMOND,
            Inches(8.5), Inches(5.8), Inches(1.2), Inches(1.2),
            fill_color=light,
        )
        set_shape_transparency(deco4, 0.5)
        animations.append((deco4.shape_id, "fade_in", 250, 600))

        # Hình thoi nhỏ góc dưới bên trái
        deco5 = self.add_shape(
            MSO_SHAPE.DIAMOND,
            Inches(0.8), Inches(6.0), Inches(0.5), Inches(0.5),
            fill_color=accent,
        )
        set_shape_transparency(deco5, 0.55)
        animations.append((deco5.shape_id, "fade_in", 280, 500))

        # Đường kẻ trang trí ngang mảnh
        deco_line = self.add_shape(
            MSO_SHAPE.RECTANGLE,
            Inches(2.5), center_y - Inches(0.05), Inches(5.0), Inches(0.03),
            fill_color=light,
        )
        set_shape_transparency(deco_line, 0.3)
        animations.append((deco_line.shape_id, "fade_in", 300, 500))

        # --- Tiêu đề chính: Xin cảm ơn ---
        title_box = self.add_textbox(
            self._title,
            Inches(1.0), center_y - Inches(1.5), Inches(8.0), Inches(1.5),
            font_size=64,
            font_color=RGBColor(0xFF, 0xFF, 0xFF),
            bold=True,
            alignment=PP_ALIGN.CENTER,
        )
        animations.append((title_box.shape_id, "fade_in", 400, 800))

        # --- Tiêu đề phụ: Thank You ---
        subtitle_box = self.add_textbox(
            self._subtitle,
            Inches(1.0), center_y + Inches(0.2), Inches(8.0), Inches(0.8),
            font_size=28,
            font_color=light,
            bold=False,
            alignment=PP_ALIGN.CENTER,
        )
        animations.append((subtitle_box.shape_id, "fade_in", 500, 700))

        # --- Thông điệp / Slogan ---
        slogan_box = self.add_textbox(
            self._slogan,
            Inches(1.5), center_y + Inches(1.2), Inches(7.0), Inches(0.6),
            font_size=16,
            font_color=RGBColor(0xC5, 0xCA, 0xE9),
            bold=False,
            alignment=PP_ALIGN.CENTER,
        )
        animations.append((slogan_box.shape_id, "fade_in", 600, 600))

        # --- Dòng thông tin liên hệ ---
        contact_box = self.add_textbox(
            self._contact_line,
            Inches(1.5), Inches(6.2), Inches(7.0), Inches(0.5),
            font_size=13,
            font_color=RGBColor(0x90, 0xA4, 0xAE),
            bold=False,
            alignment=PP_ALIGN.CENTER,
        )
        animations.append((contact_box.shape_id, "fade_in", 700, 500))

        # --- Thanh chuyển sắc trang trí phía dưới ---
        bottom_bar = self.add_gradient_shape(
            MSO_SHAPE.RECTANGLE,
            Inches(2.5), Inches(6.8), Inches(5.0), Inches(0.04),
            [accent, light],
        )
        animations.append((bottom_bar.shape_id, "fade_in", 750, 400))

        # --- Áp dụng hiệu ứng hoạt họa ---
        apply_animations_to_slide(self.slide, animations)

        return self


if __name__ == "__main__":
    gen = ThankYouGenerator()
    gen.set_data(
        title="Xin cảm ơn",
        subtitle="Thank You",
        contact_line="Liên hệ với chúng tôi: contact@example.com",
        slogan="Rất hân hạnh được hợp tác cùng Quý đối tác",
    )
    output = gen.generate().save("thank_you.pptx")
    print(f"Đã lưu: {output}")
