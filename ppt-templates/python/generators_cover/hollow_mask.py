"""Bộ sinh trang bìa mặt nạ chữ rỗng - Hiệu ứng hình học khoét rỗng, tạo chiều sâu ấn tượng"""

from pptx.enum.shapes import MSO_SHAPE
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from python.base import TemplateGenerator
from python.utils import hex_to_rgb, set_shape_transparency


class HollowMaskCover(TemplateGenerator):
    """Bìa mặt nạ chữ rỗng"""

    def __init__(self, theme=None):
        super().__init__(theme)
        self._title = ""
        self._subtitle = ""
        self._title_font_size = 42
        self._subtitle_font_size = 18
        self._title_color = RGBColor(255, 255, 255)
        self._subtitle_color = RGBColor(200, 200, 200)
        self._mask_color = None
        self._overlay_opacity = 0.55

    def set_title(self, title, font_size=None, color=None):
        """Thiết lập tiêu đề chính"""
        self._title = title
        if font_size is not None:
            self._title_font_size = font_size
        if color is not None:
            self._title_color = color
        return self

    def set_subtitle(self, subtitle, font_size=None, color=None):
        """Thiết lập tiêu đề phụ"""
        self._subtitle = subtitle
        if font_size is not None:
            self._subtitle_font_size = font_size
        if color is not None:
            self._subtitle_color = color
        return self

    def _get_theme_colors(self):
        """Lấy cấu hình màu chủ đề"""
        if self.theme:
            primary = hex_to_rgb(self.theme.primary)
            secondary = hex_to_rgb(self.theme.secondary)
            accent = hex_to_rgb(self.theme.accent)
        else:
            primary = RGBColor(15, 15, 35)
            secondary = RGBColor(26, 26, 62)
            accent = RGBColor(0, 210, 255)
        return primary, secondary, accent

    def generate(self):
        """Sinh slide trang bìa mặt nạ chữ rỗng"""
        self.create_slide()
        slide_w = self.prs.slide_width
        slide_h = self.prs.slide_height
        primary, secondary, accent = self._get_theme_colors()

        if self._mask_color is None:
            self._mask_color = primary

        # --- Nền gradient lớp dưới ---
        self.add_gradient_shape(
            MSO_SHAPE.RECTANGLE,
            Inches(0), Inches(0), slide_w, slide_h,
            [primary, secondary], angle=135
        )

        # --- Vòng tròn lớn (góc trên bên phải) ---
        circle_size = Inches(6.0)
        self.add_shape(
            MSO_SHAPE.OVAL,
            slide_w - circle_size + Inches(0.3),
            Inches(-2.0),
            circle_size, circle_size,
            fill_color=accent
        )
        set_shape_transparency(self.slide.shapes[-1], 0.88)

        # --- Vòng tròn cỡ vừa (góc dưới bên trái) ---
        circle_mid = Inches(4.0)
        self.add_shape(
            MSO_SHAPE.OVAL,
            Inches(-1.5),
            slide_h - circle_mid + Inches(0.5),
            circle_mid, circle_mid,
            fill_color=accent
        )
        set_shape_transparency(self.slide.shapes[-1], 0.92)

        # --- Lớp mặt nạ hình chữ nhật bán trong suốt (Nền chữ) ---
        mask_w = Inches(5.5)
        mask_h = Inches(2.8)
        mask_x = (slide_w - mask_w) // 2
        mask_y = (slide_h - mask_h) // 2

        mask_shape = self.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            mask_x, mask_y, mask_w, mask_h,
            fill_color=RGBColor(0, 0, 0)
        )
        set_shape_transparency(mask_shape, 0.45)
        mask_shape.line.fill.background()

        # --- Hình thoi nhỏ trang trí ---
        diamond_size = Inches(0.7)
        self.add_shape(
            MSO_SHAPE.DIAMOND,
            mask_x - Inches(0.9),
            mask_y + mask_h // 2 - diamond_size // 2,
            diamond_size, diamond_size,
            fill_color=accent
        )
        set_shape_transparency(self.slide.shapes[-1], 0.3)

        # --- Tiêu đề ---
        if self._title:
            self.add_textbox(
                self._title,
                mask_x + Inches(0.5), mask_y + Inches(0.4),
                mask_w - Inches(1.0), Inches(1.2),
                font_size=self._title_font_size,
                font_color=self._title_color,
                bold=True,
                alignment=PP_ALIGN.CENTER
            )

        # --- Đường phân cách mảnh ---
        line_w = Inches(2.0)
        self.add_shape(
            MSO_SHAPE.RECTANGLE,
            (slide_w - line_w) // 2,
            mask_y + mask_h // 2 + Inches(0.1),
            line_w, Pt(2),
            fill_color=accent
        )

        # --- Tiêu đề phụ ---
        if self._subtitle:
            self.add_textbox(
                self._subtitle,
                mask_x + Inches(0.5), mask_y + mask_h // 2 + Inches(0.4),
                mask_w - Inches(1.0), Inches(0.8),
                font_size=self._subtitle_font_size,
                font_color=self._subtitle_color,
                bold=False,
                alignment=PP_ALIGN.CENTER
            )

        return self


if __name__ == "__main__":
    cover = HollowMaskCover()
    cover.set_title("Bìa mặt nạ chữ rỗng", font_size=44)
    cover.set_subtitle("Hollow Mask Cover", font_size=20)
    cover.save("output/hollow_mask_cover.pptx")
    print("Đã sinh bìa mặt nạ chữ rỗng: output/hollow_mask_cover.pptx")
