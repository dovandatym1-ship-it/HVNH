"""Bộ sinh trang bìa chuyển sắc tối giản - Nền chuyển sắc toàn trang, thiết kế hiện đại tinh tế"""

from pptx.enum.shapes import MSO_SHAPE
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from python.base import TemplateGenerator
from python.utils import hex_to_rgb


class MinimalistGradientCover(TemplateGenerator):
    """Bìa chuyển sắc tối giản"""

    def __init__(self, theme=None):
        super().__init__(theme)
        self._title = ""
        self._subtitle = ""
        self._title_font_size = 44
        self._subtitle_font_size = 18
        self._title_color = RGBColor(255, 255, 255)
        self._subtitle_color = RGBColor(255, 255, 255)
        self._gradient_colors = None
        self._accent_color = None

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
            primary = RGBColor(26, 26, 46)
            secondary = RGBColor(22, 33, 62)
            accent = RGBColor(233, 69, 96)
        return primary, secondary, accent

    def generate(self):
        """Sinh slide trang bìa chuyển sắc tối giản"""
        self.create_slide()
        slide_w = self.prs.slide_width
        slide_h = self.prs.slide_height
        primary, secondary, accent = self._get_theme_colors()

        if self._gradient_colors is None:
            self._gradient_colors = [primary, secondary]

        # --- Nền gradient toàn màn hình ---
        bg = self.add_gradient_shape(
            MSO_SHAPE.RECTANGLE,
            Inches(0), Inches(0), slide_w, slide_h,
            self._gradient_colors, angle=45
        )

        # --- Vòng tròn trang trí nhẹ nhàng (Góc trên bên phải) ---
        circle_size = Inches(4.5)
        self.add_shape(
            MSO_SHAPE.OVAL,
            slide_w - circle_size + Inches(0.5),
            Inches(-1.5),
            circle_size, circle_size,
            fill_color=accent if self._accent_color is None else self._accent_color
        )
        # Thiết lập độ trong suốt
        from python.utils import set_shape_transparency
        set_shape_transparency(self.slide.shapes[-1], 0.88)

        # --- Đường kẻ ngang trang trí ---
        line_y = slide_h // 2 + Inches(1.2)
        line_w = Inches(3)
        self.add_shape(
            MSO_SHAPE.RECTANGLE,
            (slide_w - line_w) // 2,
            line_y,
            line_w, Pt(2),
            fill_color=self._title_color
        )

        # --- Tiêu đề chính (Căn giữa) ---
        title_y = slide_h // 2 - Inches(1.0)
        if self._title:
            self.add_textbox(
                self._title,
                Inches(1), title_y, slide_w - Inches(2), Inches(1.2),
                font_size=self._title_font_size,
                font_color=self._title_color,
                bold=True,
                alignment=PP_ALIGN.CENTER
            )

        # --- Tiêu đề phụ (Căn giữa, nằm dưới đường kẻ) ---
        if self._subtitle:
            self.add_textbox(
                self._subtitle,
                Inches(1), line_y + Inches(0.3),
                slide_w - Inches(2), Inches(0.8),
                font_size=self._subtitle_font_size,
                font_color=self._subtitle_color,
                bold=False,
                alignment=PP_ALIGN.CENTER
            )

        return self


if __name__ == "__main__":
    cover = MinimalistGradientCover()
    cover.set_title("Bìa chuyển sắc tối giản", font_size=48)
    cover.set_subtitle("Minimalist Gradient Cover", font_size=20)
    cover.save("output/minimalist_gradient_cover.pptx")
    print("Đã sinh bìa chuyển sắc tối giản: output/minimalist_gradient_cover.pptx")
