"""Bộ tạo slide lưới đội ngũ

Sắp xếp thẻ thành viên đội ngũ theo dạng lưới (2x3 hoặc 3x2), mỗi thẻ chứa khung tròn đại diện, họ tên và chức vụ,
thẻ có viền mỏng và hiệu ứng đổ bóng, phía trên cùng có tiêu đề phân mục.
"""

from pptx.enum.shapes import MSO_SHAPE
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from python.base import TemplateGenerator
from python.utils import hex_to_rgb, add_shadow, set_shape_transparency
from python.animation import apply_animations_to_slide


class TeamGridGenerator(TemplateGenerator):
    """Lưới đội ngũ"""

    DEFAULT_PRIMARY = "#1A237E"
    DEFAULT_SECONDARY = "#283593"
    DEFAULT_ACCENT = "#3F51B5"
    DEFAULT_LIGHT = "#C5CAE9"
    DEFAULT_BG = "#F5F7FA"
    DEFAULT_CARD_BG = "#FFFFFF"
    DEFAULT_BORDER = "#E0E0E0"
    DEFAULT_TEXT_DARK = "#212121"
    DEFAULT_TEXT_MID = "#555555"

    # Màu giữ chỗ cho ảnh đại diện (xoay vòng)
    AVATAR_COLORS = [
        "#3F51B5", "#5C6BC0", "#7986CB",
        "#1E88E5", "#42A5F5", "#64B5F6",
        "#00897B", "#26A69A", "#4DB6AC",
        "#7B1FA2", "#AB47BC", "#CE93D8",
    ]

    def __init__(self, theme=None, **kwargs):
        super().__init__(theme=theme, **kwargs)
        self._title = "Đội ngũ nòng cốt"
        self._members = []
        self._cols = 3  # mặc định 3 cột
        self._rows = 2  # mặc định 2 hàng

    def set_members(self, members):
        """Thiết lập danh sách thành viên đội ngũ
        members: list of dict gồm các khóa 'name', 'title', tùy chọn 'avatar_color'
        """
        self._members = members
        total = len(members)
        if total <= 3:
            self._cols = 3
            self._rows = 1
        elif total <= 6:
            self._cols = 3
            self._rows = 2
        elif total <= 9:
            self._cols = 3
            self._rows = 3
        else:
            self._cols = 4
            self._rows = (total + 3) // 4
        return self

    def set_title(self, title):
        self._title = title
        return self

    def _get_color(self, attr, default_hex):
        if self.theme and hasattr(self.theme, attr):
            return getattr(self.theme, attr)
        return hex_to_rgb(default_hex)

    def generate(self):
        """Tạo slide lưới đội ngũ"""
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

        # --- Thanh chuyển sắc nhấn trên cùng ---
        top_bar = self.add_gradient_shape(
            MSO_SHAPE.RECTANGLE,
            0, 0, slide_w, Inches(0.06),
            [primary, accent],
        )
        animations.append((top_bar.shape_id, "fade_in", 0, 400))

        # --- Tiêu đề phân mục ---
        title_box = self.add_textbox(
            self._title,
            Inches(0.5), Inches(0.4), Inches(9.0), Inches(0.7),
            font_size=30, font_color=hex_to_rgb(self.DEFAULT_TEXT_DARK),
            bold=True, alignment=PP_ALIGN.CENTER,
        )
        animations.append((title_box.shape_id, "fade_in", 100, 500))

        # --- Đường trang trí dưới tiêu đề ---
        deco_line = self.add_gradient_shape(
            MSO_SHAPE.RECTANGLE,
            Inches(3.8), Inches(1.15), Inches(2.4), Inches(0.04),
            [primary, accent],
        )
        animations.append((deco_line.shape_id, "fade_in", 200, 400))

        # --- Lưới các thẻ thành viên ---
        cols = self._cols
        rows = self._rows
        card_w = Inches(2.6)
        card_h = Inches(3.4)
        gap_x = Inches(0.4)
        gap_y = Inches(0.4)

        total_w = cols * card_w + (cols - 1) * gap_x
        total_h = rows * card_h + (rows - 1) * gap_y
        start_x = (slide_w - total_w) // 2
        start_y = Inches(1.5) + (Inches(5.8) - total_h) // 2

        for idx, member in enumerate(self._members):
            row, col = divmod(idx, cols)
            cx = start_x + col * (card_w + gap_x)
            cy = start_y + row * (card_h + gap_y)

            delay_base = 300 + idx * 120

            # Nền thẻ (hình chữ nhật bo góc)
            card = self.add_shape(
                MSO_SHAPE.ROUNDED_RECTANGLE,
                cx, cy, card_w, card_h,
                fill_color=hex_to_rgb(self.DEFAULT_CARD_BG),
                outline_color=hex_to_rgb(self.DEFAULT_BORDER),
                outline_width=Pt(0.75),
            )
            add_shadow(card, blur=Pt(4), offset=Pt(2),
                       color=(0, 0, 0), opacity=0.12)
            animations.append((card.shape_id, "fade_in", delay_base, 500))

            # Khung tròn ảnh đại diện
            avatar_size = Inches(1.2)
            avatar_left = cx + (card_w - avatar_size) // 2
            avatar_top = cy + Inches(0.3)

            color_idx = idx % len(self.AVATAR_COLORS)
            avatar_color = member.get("avatar_color", self.AVATAR_COLORS[color_idx])

            avatar = self.add_shape(
                MSO_SHAPE.OVAL,
                avatar_left, avatar_top, avatar_size, avatar_size,
                fill_color=hex_to_rgb(avatar_color),
            )
            set_shape_transparency(avatar, 0.1)
            animations.append((avatar.shape_id, "fade_in", delay_base + 100, 500))

            # Bóng người trong ảnh đại diện
            person_head = self.add_shape(
                MSO_SHAPE.OVAL,
                avatar_left + Inches(0.35), avatar_top + Inches(0.2),
                Inches(0.5), Inches(0.5),
                fill_color=RGBColor(255, 255, 255),
            )
            set_shape_transparency(person_head, 0.4)

            person_shoulders = self.add_shape(
                MSO_SHAPE.OVAL,
                avatar_left + Inches(0.15), avatar_top + Inches(0.7),
                Inches(0.9), Inches(0.5),
                fill_color=RGBColor(255, 255, 255),
            )
            set_shape_transparency(person_shoulders, 0.35)

            # Họ và tên
            name_top = cy + Inches(1.65)
            self.add_textbox(
                member.get("name", "Họ và tên"),
                cx + Inches(0.1), name_top, card_w - Inches(0.2), Inches(0.45),
                font_size=16, font_color=hex_to_rgb(self.DEFAULT_TEXT_DARK),
                bold=True, alignment=PP_ALIGN.CENTER,
            )

            # Chức vụ
            title_top = cy + Inches(2.15)
            self.add_textbox(
                member.get("title", "Chức vụ"),
                cx + Inches(0.1), title_top, card_w - Inches(0.2), Inches(0.4),
                font_size=12, font_color=accent,
                bold=False, alignment=PP_ALIGN.CENTER,
            )

            # Đường nhấn trang trí nhỏ dưới chức danh
            line_w = Inches(0.8)
            line_left = cx + (card_w - line_w) // 2
            self.add_shape(
                MSO_SHAPE.RECTANGLE,
                line_left, title_top + Inches(0.4), line_w, Inches(0.025),
                fill_color=light,
            )

        # --- Áp dụng hiệu ứng hoạt họa ---
        apply_animations_to_slide(self.slide, animations)

        return self


if __name__ == "__main__":
    gen = TeamGridGenerator()
    gen.set_title("Đội ngũ nòng cốt")
    gen.set_members([
        {"name": "Nguyễn Văn A", "title": "CEO"},
        {"name": "Trần Thị B", "title": "CTO"},
        {"name": "Lê Văn C", "title": "CPO"},
        {"name": "Phạm Minh D", "title": "CFO"},
        {"name": "Hoàng Anh E", "title": "COO"},
        {"name": "Vũ Hải F", "title": "CMO"},
    ])
    output = gen.generate().save("team_grid.pptx")
    print(f"Đã lưu: {output}")
