"""Bộ tạo slide thông tin liên hệ

Bố cục thông tin liên hệ: email, số điện thoại, website, địa chỉ, mỗi mục có biểu tượng/nhãn, bố cục dạng thẻ sạch sẽ và thanh lịch.
"""

from pptx.enum.shapes import MSO_SHAPE
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from python.base import TemplateGenerator
from python.utils import hex_to_rgb, add_shadow, set_shape_transparency
from python.animation import apply_animations_to_slide


class ContactPageGenerator(TemplateGenerator):
    """Trang thông tin liên hệ"""

    DEFAULT_PRIMARY = "#1A237E"
    DEFAULT_SECONDARY = "#283593"
    DEFAULT_ACCENT = "#3F51B5"
    DEFAULT_LIGHT = "#C5CAE9"
    DEFAULT_BG = "#F5F7FA"
    DEFAULT_CARD_BG = "#FFFFFF"
    DEFAULT_TEXT_DARK = "#212121"
    DEFAULT_TEXT_MID = "#555555"
    DEFAULT_TEXT_LIGHT = "#9E9E9E"
    DEFAULT_BORDER = "#E0E0E0"

    # Các mục liên hệ mặc định
    DEFAULT_ITEMS = [
        {"icon": "EMAIL", "label": "Email liên hệ", "value": "contact@example.com"},
        {"icon": "TEL", "label": "Điện thoại", "value": "+84 24 1234 5678"},
        {"icon": "WEB", "label": "Website", "value": "www.example.com"},
        {"icon": "ADDR", "label": "Địa chỉ văn phòng", "value": "Tòa nhà Example, Số 123 Đường Cầu Giấy, Hà Nội"},
    ]

    def __init__(self, theme=None, **kwargs):
        super().__init__(theme=theme, **kwargs)
        self._title = "Thông tin liên hệ"
        self._items = list(self.DEFAULT_ITEMS)
        self._company_name = "Công ty TNHH Example"

    def set_data(self, title=None, items=None, company_name=None):
        """Thiết lập dữ liệu thông tin liên hệ
        items: danh sách dict gồm các khóa 'icon', 'label', 'value'
        """
        if title is not None:
            self._title = title
        if items is not None:
            self._items = items
        if company_name is not None:
            self._company_name = company_name
        return self

    def _get_color(self, attr, default_hex):
        if self.theme and hasattr(self.theme, attr):
            return getattr(self.theme, attr)
        return hex_to_rgb(default_hex)

    def generate(self):
        """Tạo trang thông tin liên hệ"""
        self.create_slide()

        primary = self._get_color("primary", self.DEFAULT_PRIMARY)
        accent = self._get_color("accent", self.DEFAULT_ACCENT)
        light = self._get_color("light", self.DEFAULT_LIGHT)

        slide_w = Inches(10)
        slide_h = Inches(7.5)

        animations = []

        # --- Nền ---
        self.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, slide_w, slide_h,
                       fill_color=hex_to_rgb(self.DEFAULT_BG))

        # --- Dải màu nhấn trên cùng ---
        top_bar = self.add_gradient_shape(
            MSO_SHAPE.RECTANGLE,
            0, 0, slide_w, Inches(0.06),
            [primary, accent],
        )
        animations.append((top_bar.shape_id, "fade_in", 0, 400))

        # --- Tiêu đề ---
        title_box = self.add_textbox(
            self._title,
            Inches(0.5), Inches(0.4), Inches(9.0), Inches(0.7),
            font_size=30, font_color=hex_to_rgb(self.DEFAULT_TEXT_DARK),
            bold=True, alignment=PP_ALIGN.CENTER,
        )
        animations.append((title_box.shape_id, "fade_in", 100, 500))

        # --- Gạch chân tiêu đề ---
        deco = self.add_gradient_shape(
            MSO_SHAPE.RECTANGLE,
            Inches(3.8), Inches(1.15), Inches(2.4), Inches(0.04),
            [primary, accent],
        )
        animations.append((deco.shape_id, "fade_in", 200, 400))

        # --- Tên công ty ---
        company_box = self.add_textbox(
            self._company_name,
            Inches(1.0), Inches(1.45), Inches(8.0), Inches(0.5),
            font_size=16,
            font_color=accent,
            bold=False,
            alignment=PP_ALIGN.CENTER,
        )
        animations.append((company_box.shape_id, "fade_in", 250, 500))

        # --- Bố cục thẻ liên hệ ---
        n_items = len(self._items)
        if n_items <= 4:
            cols = 2
            rows = 2
        else:
            cols = 3
            rows = (n_items + 2) // 3

        card_w = Inches(3.6)
        card_h = Inches(2.0)
        gap_x = Inches(0.5)
        gap_y = Inches(0.4)

        total_w = cols * card_w + (cols - 1) * gap_x
        total_h = rows * card_h + (rows - 1) * gap_y
        start_x = (slide_w - total_w) // 2
        start_y = Inches(2.2) + (Inches(5.0) - total_h) // 2

        for idx, item in enumerate(self._items):
            row, col = divmod(idx, cols)
            cx = start_x + col * (card_w + gap_x)
            cy = start_y + row * (card_h + gap_y)

            delay_base = 300 + idx * 120

            # Nền thẻ
            card = self.add_shape(
                MSO_SHAPE.ROUNDED_RECTANGLE,
                cx, cy, card_w, card_h,
                fill_color=hex_to_rgb(self.DEFAULT_CARD_BG),
                outline_color=hex_to_rgb(self.DEFAULT_BORDER),
                outline_width=Pt(0.75),
            )
            add_shadow(card, blur=Pt(3), offset=Pt(2),
                       color=(0, 0, 0), opacity=0.1)
            animations.append((card.shape_id, "fade_in", delay_base, 500))

            # Biểu tượng hình tròn bên trái thẻ
            icon_size = Inches(0.65)
            icon_left = cx + Inches(0.25)
            icon_top = cy + (card_h - icon_size) // 2

            icon_bg = self.add_shape(
                MSO_SHAPE.OVAL,
                icon_left, icon_top, icon_size, icon_size,
                fill_color=primary,
            )
            animations.append((icon_bg.shape_id, "fade_in", delay_base + 80, 400))

            # Văn bản biểu tượng
            icon_text_box = self.add_textbox(
                item.get("icon", ""),
                icon_left, icon_top + Inches(0.08),
                icon_size, icon_size - Inches(0.08),
                font_size=11,
                font_color=RGBColor(0xFF, 0xFF, 0xFF),
                bold=True,
                alignment=PP_ALIGN.CENTER,
            )

            # Nhãn
            text_left = cx + Inches(1.1)
            text_width = card_w - Inches(1.3)

            label_box = self.add_textbox(
                item.get("label", "Nhãn"),
                text_left, cy + Inches(0.3),
                text_width, Inches(0.4),
                font_size=13,
                font_color=hex_to_rgb(self.DEFAULT_TEXT_LIGHT),
                bold=False,
                alignment=PP_ALIGN.LEFT,
            )

            # Giá trị
            value_box = self.add_textbox(
                item.get("value", "Chưa cập nhật"),
                text_left, cy + Inches(0.75),
                text_width, Inches(0.8),
                font_size=16,
                font_color=hex_to_rgb(self.DEFAULT_TEXT_DARK),
                bold=True,
                alignment=PP_ALIGN.LEFT,
            )

        # --- Họa tiết trang trí các góc ---
        deco_d1 = self.add_shape(
            MSO_SHAPE.DIAMOND,
            Inches(0.3), Inches(6.8), Inches(0.3), Inches(0.3),
            fill_color=light,
        )
        set_shape_transparency(deco_d1, 0.4)
        animations.append((deco_d1.shape_id, "fade_in", 800, 400))

        deco_d2 = self.add_shape(
            MSO_SHAPE.DIAMOND,
            Inches(9.4), Inches(6.5), Inches(0.4), Inches(0.4),
            fill_color=accent,
        )
        set_shape_transparency(deco_d2, 0.45)
        animations.append((deco_d2.shape_id, "fade_in", 820, 400))

        # --- Thanh chuyển sắc phía dưới ---
        bottom_bar = self.add_gradient_shape(
            MSO_SHAPE.RECTANGLE,
            Inches(0.8), Inches(7.1), Inches(8.4), Inches(0.04),
            [light, accent],
        )
        animations.append((bottom_bar.shape_id, "fade_in", 850, 400))

        # --- Áp dụng hiệu ứng hoạt họa ---
        apply_animations_to_slide(self.slide, animations)

        return self


if __name__ == "__main__":
    gen = ContactPageGenerator()
    gen.set_data(
        title="Thông tin liên hệ",
        company_name="Công ty Cổ phần Công nghệ Example",
        items=[
            {"icon": "EMAIL", "label": "Email liên hệ", "value": "contact@example.com"},
            {"icon": "TEL", "label": "Điện thoại", "value": "+84 24 1234 5678"},
            {"icon": "WEB", "label": "Website", "value": "www.example.com"},
            {"icon": "ADDR", "label": "Địa chỉ văn phòng", "value": "Tòa nhà Example, Số 123 Đường Cầu Giấy, Hà Nội"},
        ],
    )
    output = gen.generate().save("contact.pptx")
    print(f"Đã lưu: {output}")
