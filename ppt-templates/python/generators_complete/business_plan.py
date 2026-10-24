"""Bộ lắp ráp bài thuyết trình Kế hoạch kinh doanh hoàn chỉnh

Tạo bài thuyết trình kế hoạch kinh doanh gồm 18 trang:
Trang bìa -> Mục lục -> Phân tích thị trường (3 trang) -> Giới thiệu đội ngũ -> Sản phẩm & Dịch vụ (2 trang) -> Mô hình kinh doanh -> Phân tích cạnh tranh -> Dự báo tài chính (3 trang) -> Kế hoạch gọi vốn -> Lộ trình phát triển -> Lời cảm ơn

Mặc định sử dụng chủ đề Công nghệ xanh dương, bìa phong cách xoay hình học.
"""

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from pptx.enum.shapes import MSO_SHAPE
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from python.base import TemplateGenerator
from python.utils import hex_to_rgb, set_shape_transparency, create_grid_positions


class BusinessPlanAssembler(TemplateGenerator):
    """Bộ lắp ráp bài thuyết trình Kế hoạch kinh doanh (18 slide)"""

    # Màu mặc định chủ đề Công nghệ xanh dương
    DEFAULT_THEME = {
        "primary": "#1A237E",
        "secondary": "#283593",
        "accent": "#3F51B5",
        "highlight": "#7986CB",
        "light": "#C5CAE9",
        "bg": "#F5F7FA",
        "text_primary": "#1A237E",
        "text_secondary": "#455A64",
        "text_light": "#FFFFFF",
    }

    def __init__(self, theme=None):
        super().__init__(theme=theme)
        self._title = "Kế hoạch kinh doanh"
        self._subtitle = "Business Plan"
        self._data = {}
        self._theme = theme or self.DEFAULT_THEME

    def set_title(self, title):
        self._title = title
        return self

    def set_subtitle(self, subtitle):
        self._subtitle = subtitle
        return self

    def set_data(self, data):
        """Thiết lập dữ liệu bài thuyết trình

        data: dict, có thể chứa các khóa:
            - company: Tên công ty
            - market_analysis: Danh sách nội dung phân tích thị trường
            - team_members: Danh sách thành viên đội ngũ
            - products: Danh sách sản phẩm & dịch vụ
            - business_model: Mô tả mô hình kinh doanh
            - competitors: Danh sách đối thủ cạnh tranh
            - financials: Dữ liệu dự báo tài chính
            - funding: Kế hoạch gọi vốn
            - roadmap: Lộ trình phát triển
        """
        self._data = data
        return self

    def _get_color(self, key):
        if isinstance(self._theme, dict):
            return hex_to_rgb(self._theme.get(key, self._theme["primary"]))
        return hex_to_rgb(getattr(self._theme, key, self._theme.primary))

    # ------------------------------------------------------------------ #
    #  Phương thức hỗ trợ trang chung
    # ------------------------------------------------------------------ #

    def _add_bg(self, color_key="bg"):
        """Thêm nền màu đơn sắc"""
        self.add_shape(
            MSO_SHAPE.RECTANGLE,
            Inches(0), Inches(0), Inches(10), Inches(7.5),
            fill_color=self._get_color(color_key),
        )

    def _add_page_title_bar(self, title):
        """Thanh tiêu đề trên cùng trang"""
        bar_color = self._get_color("primary")
        self.add_shape(
            MSO_SHAPE.RECTANGLE,
            Inches(0), Inches(0), Inches(10), Inches(1.0),
            fill_color=bar_color,
        )
        self.add_textbox(
            title,
            Inches(0.6), Inches(0.15), Inches(8.8), Inches(0.7),
            font_size=28, font_color=self._get_color("text_light"),
            bold=True, alignment=PP_ALIGN.LEFT,
        )

    def _add_section_title(self, title, subtitle=""):
        """Trang phân mục (Tiêu đề lớn căn giữa + tiêu đề phụ)"""
        self.create_slide()
        self._add_bg()
        accent = self._get_color("accent")
        self.add_shape(
            MSO_SHAPE.RECTANGLE,
            Inches(0), Inches(2.8), Inches(10), Inches(2.0),
            fill_color=accent,
        )
        set_shape_transparency(self.slide.shapes[-1], 0.10)
        self.add_textbox(
            title,
            Inches(1), Inches(3.0), Inches(8), Inches(1.0),
            font_size=36, font_color=self._get_color("text_primary"),
            bold=True, alignment=PP_ALIGN.CENTER,
        )
        if subtitle:
            self.add_textbox(
                subtitle,
                Inches(1), Inches(4.0), Inches(8), Inches(0.6),
                font_size=18, font_color=self._get_color("text_secondary"),
                alignment=PP_ALIGN.CENTER,
            )

    def _add_content_card(self, left, top, width, height, title, items, icon_num=""):
        """Thẻ nội dung"""
        card_color = RGBColor(255, 255, 255)
        card = self.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            left, top, width, height,
            fill_color=card_color,
        )
        set_shape_transparency(card, 0.05)
        # Dải màu trên cùng
        self.add_shape(
            MSO_SHAPE.RECTANGLE,
            left, top, width, Inches(0.06),
            fill_color=self._get_color("accent"),
        )
        # Vòng tròn số thứ tự
        if icon_num:
            circle_size = Inches(0.45)
            self.add_shape(
                MSO_SHAPE.OVAL,
                left + Inches(0.2), top + Inches(0.2),
                circle_size, circle_size,
                fill_color=self._get_color("accent"),
            )
            self.add_textbox(
                icon_num,
                left + Inches(0.2), top + Inches(0.2),
                circle_size, circle_size,
                font_size=14, font_color=self._get_color("text_light"),
                bold=True, alignment=PP_ALIGN.CENTER,
            )
        # Tiêu đề
        title_x = left + Inches(0.75) if icon_num else left + Inches(0.2)
        self.add_textbox(
            title,
            title_x, top + Inches(0.2),
            width - Inches(1.0), Inches(0.4),
            font_size=14, font_color=self._get_color("text_primary"),
            bold=True, alignment=PP_ALIGN.LEFT,
        )
        # Các mục danh sách
        item_top = top + Inches(0.7)
        for item in items[:4]:
            self.add_textbox(
                f"  {item}",
                left + Inches(0.25), item_top,
                width - Inches(0.5), Inches(0.3),
                font_size=10, font_color=self._get_color("text_secondary"),
                alignment=PP_ALIGN.LEFT,
            )
            item_top += Inches(0.28)

    def _add_thank_you(self):
        """Trang cảm ơn"""
        self.create_slide()
        self.add_gradient_shape(
            MSO_SHAPE.RECTANGLE,
            Inches(0), Inches(0), Inches(10), Inches(7.5),
            [self._get_color("primary"), self._get_color("secondary")],
            angle=135,
        )
        self.add_textbox(
            "Thank You",
            Inches(1), Inches(2.5), Inches(8), Inches(1.2),
            font_size=48, font_color=RGBColor(255, 255, 255),
            bold=True, alignment=PP_ALIGN.CENTER,
        )
        self.add_textbox(
            "Trân trọng cảm ơn sự theo dõi của Quý vị",
            Inches(1), Inches(3.8), Inches(8), Inches(0.8),
            font_size=24, font_color=RGBColor(197, 202, 233),
            alignment=PP_ALIGN.CENTER,
        )
        # Đường trang trí
        line_w = Inches(2)
        self.add_shape(
            MSO_SHAPE.RECTANGLE,
            (Inches(10) - line_w) // 2, Inches(3.55),
            line_w, Pt(2),
            fill_color=RGBColor(197, 202, 233),
        )

    # ------------------------------------------------------------------ #
    #  Phương thức tạo từng trang slide
    # ------------------------------------------------------------------ #

    def _gen_cover(self):
        """Trang bìa: Phong cách xoay hình học"""
        self.create_slide()
        primary = self._get_color("primary")
        secondary = self._get_color("secondary")
        accent = self._get_color("accent")
        highlight = self._get_color("highlight")
        light = self._get_color("light")

        # Nền chuyển sắc
        self.add_gradient_shape(
            MSO_SHAPE.RECTANGLE,
            Inches(0), Inches(0), Inches(10), Inches(7.5),
            [primary, secondary], angle=45,
        )

        # Họa tiết hình học trang trí
        shapes_config = [
            (MSO_SHAPE.RECTANGLE, Inches(0.5), Inches(0.3), Inches(3.0), Inches(3.0), 15, accent),
            (MSO_SHAPE.DIAMOND, Inches(5.5), Inches(0.1), Inches(2.5), Inches(2.5), 0, highlight),
            (MSO_SHAPE.RECTANGLE, Inches(6.5), Inches(4.0), Inches(2.8), Inches(2.8), -20, light),
            (MSO_SHAPE.DIAMOND, Inches(1.0), Inches(4.5), Inches(2.2), Inches(2.2), 30, accent),
            (MSO_SHAPE.RECTANGLE, Inches(3.5), Inches(5.0), Inches(2.5), Inches(2.5), 45, highlight),
        ]
        for shape_type, left, top, w, h, rot, color in shapes_config:
            shape = self.add_shape(shape_type, left, top, w, h, fill_color=color)
            set_shape_transparency(shape, 0.60)
            if rot != 0:
                from lxml import etree
                xfrm = shape._element.find('.//{http://schemas.openxmlformats.org/drawingml/2006/main}xfrm')
                if xfrm is not None:
                    xfrm.set('rot', str(int(rot * 60000)))

        # Tiêu đề
        self.add_textbox(
            self._title,
            Inches(1.5), Inches(2.6), Inches(7.0), Inches(1.2),
            font_size=42, font_color=RGBColor(255, 255, 255),
            bold=True, alignment=PP_ALIGN.CENTER,
        )
        # Đường phân cách
        line_w = Inches(2.5)
        self.add_shape(
            MSO_SHAPE.RECTANGLE,
            (Inches(10) - line_w) // 2, Inches(3.85),
            line_w, Pt(2),
            fill_color=RGBColor(197, 202, 233),
        )
        # Tiêu đề phụ
        self.add_textbox(
            self._subtitle,
            Inches(1.5), Inches(4.1), Inches(7.0), Inches(0.8),
            font_size=20, font_color=RGBColor(197, 202, 233),
            alignment=PP_ALIGN.CENTER,
        )

    def _gen_directory(self):
        """Trang mục lục"""
        self.create_slide()
        self._add_bg()
        self._add_page_title_bar("Mục lục")

        sections = [
            ("01", "Phân tích thị trường"),
            ("02", "Giới thiệu đội ngũ"),
            ("03", "Sản phẩm & Dịch vụ"),
            ("04", "Mô hình kinh doanh"),
            ("05", "Phân tích cạnh tranh"),
            ("06", "Dự báo tài chính"),
            ("07", "Kế hoạch gọi vốn"),
            ("08", "Lộ trình phát triển"),
        ]
        card_w = Inches(2.0)
        card_h = Inches(1.4)
        gap = Inches(0.35)
        cols = 4
        start_x = (Inches(10) - (cols * card_w + (cols - 1) * gap)) // 2
        start_y = Inches(1.6)

        for i, (num, title) in enumerate(sections):
            row, col = divmod(i, cols)
            x = start_x + col * (card_w + gap)
            y = start_y + row * (card_h + gap)
            self._add_content_card(x, y, card_w, card_h, title, [], icon_num=num)

    def _gen_market_analysis(self, page_num=1):
        """Trang phân tích thị trường"""
        self.create_slide()
        self._add_bg()
        self._add_page_title_bar(f"Phân tích thị trường - Phần {page_num}")

        contents = {
            1: ("Tổng quan ngành", ["Quy mô thị trường toàn cầu tăng trưởng bền vững", "Tốc độ tăng trưởng kép (CAGR) trên 15%", "Chuyển đổi số được đẩy mạnh toàn diện", "Chính sách vĩ mô hỗ trợ thuận lợi"]),
            2: ("Thị trường mục tiêu", ["Các đô thị loại 1 và trung tâm kinh tế", "Phân khúc khách hàng trọng tâm từ 25-45 tuổi", "Trọng tâm doanh nghiệp B2B vừa và lớn", "Khách hàng cá nhân cao cấp B2C"]),
            3: ("Nhu cầu khách hàng", ["Nhu cầu nâng cao hiệu suất lao động cấp thiết", "Xu hướng cá nhân hóa và may đo giải pháp", "Hệ sinh thái giải pháp tích hợp tất cả trong một", "Tiêu chuẩn bảo mật dữ liệu và quyền riêng tư"]),
        }
        title, items = contents.get(page_num, ("Phân tích thị trường", []))
        self._add_content_card(Inches(0.8), Inches(1.5), Inches(8.4), Inches(3.5), title, items)

        # Điểm sáng dữ liệu
        highlights = [
            ("100 tỷ+", "Quy mô thị trường"),
            ("15%", "Tăng trưởng năm"),
            ("50 triệu", "Khách hàng mục tiêu"),
        ]
        box_w = Inches(2.5)
        start_x = (Inches(10) - (3 * box_w + 2 * Inches(0.5))) // 2
        for i, (value, label) in enumerate(highlights):
            x = start_x + i * (box_w + Inches(0.5))
            self.add_shape(
                MSO_SHAPE.ROUNDED_RECTANGLE,
                x, Inches(5.3), box_w, Inches(1.5),
                fill_color=RGBColor(255, 255, 255),
            )
            self.add_textbox(
                value,
                x, Inches(5.4), box_w, Inches(0.8),
                font_size=28, font_color=self._get_color("accent"),
                bold=True, alignment=PP_ALIGN.CENTER,
            )
            self.add_textbox(
                label,
                x, Inches(6.1), box_w, Inches(0.5),
                font_size=12, font_color=self._get_color("text_secondary"),
                alignment=PP_ALIGN.CENTER,
            )

    def _gen_team(self):
        """Trang giới thiệu đội ngũ"""
        self.create_slide()
        self._add_bg()
        self._add_page_title_bar("Giới thiệu đội ngũ")

        team = self._data.get("team_members", [
            {"name": "Nguyễn Văn A", "role": "CEO", "desc": "10 năm kinh nghiệm điều hành"},
            {"name": "Trần Thị B", "role": "CTO", "desc": "Chuyên gia kiến trúc hệ thống"},
            {"name": "Lê Văn C", "role": "CMO", "desc": "Chuyên gia tiếp thị & thương hiệu"},
            {"name": "Phạm Minh D", "role": "CFO", "desc": "Quản trị tài chính & đầu tư"},
        ])

        card_w = Inches(2.0)
        card_h = Inches(3.2)
        gap = Inches(0.3)
        start_x = (Inches(10) - (len(team[:4]) * card_w + (len(team[:4]) - 1) * gap)) // 2

        for i, member in enumerate(team[:4]):
            x = start_x + i * (card_w + gap)
            y = Inches(1.5)
            # Nền thẻ
            self.add_shape(
                MSO_SHAPE.ROUNDED_RECTANGLE,
                x, y, card_w, card_h,
                fill_color=RGBColor(255, 255, 255),
            )
            # Vòng tròn giữ chỗ ảnh đại diện
            circle_size = Inches(1.0)
            self.add_shape(
                MSO_SHAPE.OVAL,
                x + (card_w - circle_size) // 2, y + Inches(0.3),
                circle_size, circle_size,
                fill_color=self._get_color("light"),
            )
            self.add_textbox(
                member["name"][0],
                x + (card_w - circle_size) // 2, y + Inches(0.45),
                circle_size, circle_size,
                font_size=28, font_color=self._get_color("primary"),
                bold=True, alignment=PP_ALIGN.CENTER,
            )
            # Họ và tên
            self.add_textbox(
                member["name"],
                x, y + Inches(1.5), card_w, Inches(0.4),
                font_size=16, font_color=self._get_color("text_primary"),
                bold=True, alignment=PP_ALIGN.CENTER,
            )
            # Chức danh
            self.add_textbox(
                member["role"],
                x, y + Inches(1.9), card_w, Inches(0.35),
                font_size=12, font_color=self._get_color("accent"),
                bold=True, alignment=PP_ALIGN.CENTER,
            )
            # Mô tả
            self.add_textbox(
                member.get("desc", ""),
                x, y + Inches(2.3), card_w, Inches(0.5),
                font_size=10, font_color=self._get_color("text_secondary"),
                alignment=PP_ALIGN.CENTER,
            )

    def _gen_product(self, page_num=1):
        """Trang sản phẩm & dịch vụ"""
        self.create_slide()
        self._add_bg()
        self._add_page_title_bar(f"Sản phẩm & Dịch vụ - Phần {page_num}")

        products = {
            1: ("Sản phẩm cốt lõi", [
                {"title": "Nền tảng phân tích thông minh", "desc": "Phân tích dữ liệu bằng AI"},
                {"title": "Giải pháp đám mây", "desc": "Kiến trúc co giãn linh hoạt"},
                {"title": "Bộ ứng dụng di động", "desc": "Bao phủ đa kịch bản người dùng"},
            ]),
            2: ("Hệ thống dịch vụ", [
                {"title": "Tư vấn kỹ thuật", "desc": "Giải pháp công nghệ chuyên biệt"},
                {"title": "Hỗ trợ vận hành", "desc": "Bảo đảm liên tục 24/7"},
                {"title": "Đào tạo chuyển giao", "desc": "Chuyển giao tri thức & nâng cao năng lực"},
            ]),
        }
        section_title, items = products.get(page_num, ("Sản phẩm & Dịch vụ", []))

        card_w = Inches(2.6)
        card_h = Inches(3.5)
        gap = Inches(0.4)
        start_x = (Inches(10) - (3 * card_w + 2 * gap)) // 2

        for i, item in enumerate(items):
            x = start_x + i * (card_w + gap)
            y = Inches(1.5)
            # Thẻ
            self.add_shape(
                MSO_SHAPE.ROUNDED_RECTANGLE,
                x, y, card_w, card_h,
                fill_color=RGBColor(255, 255, 255),
            )
            # Khối màu trên cùng
            self.add_shape(
                MSO_SHAPE.RECTANGLE,
                x, y, card_w, Inches(0.8),
                fill_color=self._get_color("accent"),
            )
            set_shape_transparency(self.slide.shapes[-1], 0.15)
            # Vòng tròn biểu tượng
            icon_size = Inches(0.7)
            self.add_shape(
                MSO_SHAPE.OVAL,
                x + (card_w - icon_size) // 2, y + Inches(0.05),
                icon_size, icon_size,
                fill_color=RGBColor(255, 255, 255),
            )
            set_shape_transparency(self.slide.shapes[-1], 0.3)
            self.add_textbox(
                str(i + 1),
                x + (card_w - icon_size) // 2, y + Inches(0.12),
                icon_size, icon_size,
                font_size=20, font_color=self._get_color("primary"),
                bold=True, alignment=PP_ALIGN.CENTER,
            )
            # Tiêu đề
            self.add_textbox(
                item["title"],
                x, y + Inches(1.1), card_w, Inches(0.5),
                font_size=16, font_color=self._get_color("text_primary"),
                bold=True, alignment=PP_ALIGN.CENTER,
            )
            # Mô tả
            self.add_textbox(
                item["desc"],
                x + Inches(0.2), y + Inches(1.7), card_w - Inches(0.4), Inches(1.2),
                font_size=11, font_color=self._get_color("text_secondary"),
                alignment=PP_ALIGN.CENTER,
            )

        self.add_textbox(
            section_title,
            Inches(0.6), Inches(5.8), Inches(8.8), Inches(0.5),
            font_size=14, font_color=self._get_color("text_secondary"),
            alignment=PP_ALIGN.CENTER,
        )

    def _gen_business_model(self):
        """Trang mô hình kinh doanh"""
        self.create_slide()
        self._add_bg()
        self._add_page_title_bar("Mô hình kinh doanh")

        models = [
            ("Thuê bao SaaS", "Thu phí theo tháng/năm\nGói cước linh hoạt"),
            ("Dịch vụ giá trị gia tăng", "Tính năng nâng cao chuyên sâu\nPhát triển theo yêu cầu riêng"),
            ("Dịch vụ dữ liệu", "Hiểu biết chuyên sâu ngành\nPhân tích dữ liệu lớn"),
            ("Hợp tác hệ sinh thái", "Chia sẻ doanh thu đối tác\nLiên kết quảng bá sản phẩm"),
        ]

        card_w = Inches(2.0)
        card_h = Inches(2.8)
        gap = Inches(0.3)
        start_x = (Inches(10) - (4 * card_w + 3 * gap)) // 2

        for i, (title, desc) in enumerate(models):
            x = start_x + i * (card_w + gap)
            y = Inches(1.6)
            # Thẻ
            self.add_shape(
                MSO_SHAPE.ROUNDED_RECTANGLE,
                x, y, card_w, card_h,
                fill_color=RGBColor(255, 255, 255),
            )
            # Vòng tròn trên cùng
            circle_size = Inches(0.9)
            self.add_shape(
                MSO_SHAPE.OVAL,
                x + (card_w - circle_size) // 2, y + Inches(0.3),
                circle_size, circle_size,
                fill_color=self._get_color("accent"),
            )
            self.add_textbox(
                f"0{i+1}",
                x + (card_w - circle_size) // 2, y + Inches(0.45),
                circle_size, circle_size,
                font_size=22, font_color=RGBColor(255, 255, 255),
                bold=True, alignment=PP_ALIGN.CENTER,
            )
            # Tiêu đề
            self.add_textbox(
                title,
                x, y + Inches(1.4), card_w, Inches(0.4),
                font_size=14, font_color=self._get_color("text_primary"),
                bold=True, alignment=PP_ALIGN.CENTER,
            )
            # Mô tả
            self.add_textbox(
                desc,
                x + Inches(0.15), y + Inches(1.8), card_w - Inches(0.3), Inches(0.8),
                font_size=10, font_color=self._get_color("text_secondary"),
                alignment=PP_ALIGN.CENTER,
            )

    def _gen_competition(self):
        """Trang phân tích cạnh tranh"""
        self.create_slide()
        self._add_bg()
        self._add_page_title_bar("Phân tích cạnh tranh")

        # Tiêu đề bảng đối chiếu
        cols = ["Tiêu chí", "Chúng tôi", "Đối thủ A", "Đối thủ B"]
        col_w = [Inches(1.8), Inches(2.4), Inches(2.4), Inches(2.4)]
        start_x = Inches(0.5)
        header_y = Inches(1.5)

        for i, (col_title, w) in enumerate(zip(cols, col_w)):
            x = start_x + sum(c.inches for c in [Inches(0)] + col_w[:i])
            # Hiệu chỉnh tính toán vị trí
            x_pos = start_x
            for j in range(i):
                x_pos += col_w[j]
            self.add_shape(
                MSO_SHAPE.RECTANGLE,
                x_pos, header_y, w, Inches(0.5),
                fill_color=self._get_color("primary") if i == 0 else self._get_color("accent"),
            )
            set_shape_transparency(self.slide.shapes[-1], 0.1 if i == 0 else 0.0)
            self.add_textbox(
                col_title,
                x_pos, header_y, w, Inches(0.5),
                font_size=13, font_color=RGBColor(255, 255, 255),
                bold=True, alignment=PP_ALIGN.CENTER,
            )

        rows = [
            ("Năng lực công nghệ", "Dẫn đầu", "Trung bình", "Trung bình"),
            ("Thị phần", "Tăng nhanh", "Ổn định", "Suy giảm"),
            ("Trải nghiệm người dùng", "Xuất sắc", "Tốt", "Bình thường"),
            ("Chiến lược giá", "Linh hoạt", "Khá cao", "Giá rẻ"),
            ("Năng lực đổi mới", "Mạnh", "Trung bình", "Yếu"),
        ]

        for r, (dim, ours, a, b) in enumerate(rows):
            y = header_y + Inches(0.5 + r * 0.55)
            row_bg = RGBColor(245, 247, 250) if r % 2 == 0 else RGBColor(255, 255, 255)
            values = [dim, ours, a, b]
            for i, (val, w) in enumerate(zip(values, col_w)):
                x_pos = start_x
                for j in range(i):
                    x_pos += col_w[j]
                self.add_shape(
                    MSO_SHAPE.RECTANGLE,
                    x_pos, y, w, Inches(0.5),
                    fill_color=row_bg,
                )
                fc = self._get_color("text_primary") if i == 0 else self._get_color("text_secondary")
                self.add_textbox(
                    val,
                    x_pos, y, w, Inches(0.5),
                    font_size=11, font_color=fc,
                    bold=(i == 0), alignment=PP_ALIGN.CENTER,
                )

    def _gen_financial(self, page_num=1):
        """Trang dự báo tài chính"""
        self.create_slide()
        self._add_bg()
        self._add_page_title_bar(f"Dự báo tài chính - Phần {page_num}")

        contents = {
            1: ("Dự báo doanh thu", [
                {"year": "2025", "revenue": "5 tỷ", "growth": "-"},
                {"year": "2026", "revenue": "20 tỷ", "growth": "300%"},
                {"year": "2027", "revenue": "80 tỷ", "growth": "300%"},
            ]),
            2: ("Cơ cấu chi phí", [
                {"item": "Đầu tư R&D", "ratio": "40%", "amount": "8 tỷ"},
                {"item": "Tiếp thị thị trường", "ratio": "25%", "amount": "5 tỷ"},
                {"item": "Chi phí vận hành", "ratio": "20%", "amount": "4 tỷ"},
            ]),
            3: ("Dự báo lợi nhuận", [
                {"year": "2025", "profit": "-3 tỷ", "rate": "-60%"},
                {"year": "2026", "profit": "2 tỷ", "rate": "10%"},
                {"year": "2027", "profit": "30 tỷ", "rate": "37.5%"},
            ]),
        }

        title, items = contents.get(page_num, ("Dữ liệu tài chính", []))
        # Tiêu đề
        self.add_textbox(
            title,
            Inches(0.6), Inches(1.3), Inches(8.8), Inches(0.5),
            font_size=18, font_color=self._get_color("text_primary"),
            bold=True, alignment=PP_ALIGN.LEFT,
        )

        # Thẻ dữ liệu
        card_w = Inches(2.6)
        card_h = Inches(3.8)
        gap = Inches(0.4)
        start_x = (Inches(10) - (len(items) * card_w + (len(items) - 1) * gap)) // 2

        for i, item in enumerate(items):
            x = start_x + i * (card_w + gap)
            y = Inches(2.0)
            self.add_shape(
                MSO_SHAPE.ROUNDED_RECTANGLE,
                x, y, card_w, card_h,
                fill_color=RGBColor(255, 255, 255),
            )
            # Dải màu trên cùng
            self.add_shape(
                MSO_SHAPE.RECTANGLE,
                x, y, card_w, Inches(0.08),
                fill_color=self._get_color("accent"),
            )
            # Nội dung
            values = list(item.values())
            for j, val in enumerate(values):
                fc = self._get_color("text_primary") if j == 0 else self._get_color("text_secondary")
                fs = 14 if j == 0 else 22 if j == 1 else 12
                bld = j <= 1
                self.add_textbox(
                    val,
                    x + Inches(0.2), y + Inches(0.4 + j * 1.0),
                    card_w - Inches(0.4), Inches(0.6),
                    font_size=fs, font_color=fc,
                    bold=bld, alignment=PP_ALIGN.CENTER,
                )

    def _gen_funding(self):
        """Trang kế hoạch gọi vốn"""
        self.create_slide()
        self._add_bg()
        self._add_page_title_bar("Kế hoạch gọi vốn")

        rounds = [
            {"round": "Vòng Thiên thần", "amount": "5 tỷ VNĐ", "use": "Phát triển sản phẩm", "time": "Quý 1/2025"},
            {"round": "Vòng Pre-A", "amount": "20 tỷ VNĐ", "use": "Mở rộng thị trường", "time": "Quý 4/2025"},
            {"round": "Vòng Series A", "amount": "80 tỷ VNĐ", "use": "Mở rộng quy mô", "time": "Quý 3/2026"},
        ]

        card_w = Inches(2.6)
        card_h = Inches(3.5)
        gap = Inches(0.4)
        start_x = (Inches(10) - (3 * card_w + 2 * gap)) // 2

        for i, rd in enumerate(rounds):
            x = start_x + i * (card_w + gap)
            y = Inches(1.6)
            self.add_shape(
                MSO_SHAPE.ROUNDED_RECTANGLE,
                x, y, card_w, card_h,
                fill_color=RGBColor(255, 255, 255),
            )
            # Vòng tròn số tiền
            circle_size = Inches(1.2)
            self.add_shape(
                MSO_SHAPE.OVAL,
                x + (card_w - circle_size) // 2, y + Inches(0.3),
                circle_size, circle_size,
                fill_color=self._get_color("accent"),
            )
            self.add_textbox(
                rd["amount"],
                x + (card_w - circle_size) // 2, y + Inches(0.55),
                circle_size, circle_size,
                font_size=14, font_color=RGBColor(255, 255, 255),
                bold=True, alignment=PP_ALIGN.CENTER,
            )
            # Vòng gọi vốn
            self.add_textbox(
                rd["round"],
                x, y + Inches(1.65), card_w, Inches(0.4),
                font_size=16, font_color=self._get_color("text_primary"),
                bold=True, alignment=PP_ALIGN.CENTER,
            )
            # Mục đích sử dụng
            self.add_textbox(
                f"Mục đích: {rd['use']}",
                x, y + Inches(2.1), card_w, Inches(0.35),
                font_size=11, font_color=self._get_color("text_secondary"),
                alignment=PP_ALIGN.CENTER,
            )
            # Thời gian
            self.add_textbox(
                f"Thời gian: {rd['time']}",
                x, y + Inches(2.5), card_w, Inches(0.35),
                font_size=11, font_color=self._get_color("text_secondary"),
                alignment=PP_ALIGN.CENTER,
            )

    def _gen_roadmap(self):
        """Trang lộ trình phát triển"""
        self.create_slide()
        self._add_bg()
        self._add_page_title_bar("Lộ trình phát triển")

        phases = [
            ("Quý 1/2025", "Khởi động dự án", "Hoàn thiện đội ngũ nòng cốt\nBắt đầu phát triển sản phẩm"),
            ("Quý 3/2025", "Ra mắt sản phẩm", "Phát hành bản MVP\nThu hút tệp người dùng thử nghiệm"),
            ("Quý 1/2026", "Mở rộng thị trường", "Quảng bá trên diện rộng\nThiết lập kênh phân phối"),
            ("Quý 3/2026", "Dẫn đầu thị trường", "Vào top 3 thị phần trong ngành\nKhởi động gọi vốn Series B"),
        ]

        # Trục đường thời gian
        line_y = Inches(3.5)
        self.add_shape(
            MSO_SHAPE.RECTANGLE,
            Inches(0.8), line_y, Inches(8.4), Pt(3),
            fill_color=self._get_color("accent"),
        )

        node_w = Inches(2.0)
        total_w = len(phases) * node_w + (len(phases) - 1) * Inches(0.3)
        start_x = (Inches(10) - total_w) // 2

        for i, (time, title, desc) in enumerate(phases):
            x = start_x + i * (node_w + Inches(0.3))
            # Vòng tròn điểm mốc
            circle_size = Inches(0.5)
            cx = x + node_w // 2 - circle_size // 2
            self.add_shape(
                MSO_SHAPE.OVAL,
                cx, line_y - circle_size // 2,
                circle_size, circle_size,
                fill_color=self._get_color("accent"),
            )
            self.add_textbox(
                str(i + 1),
                cx, line_y - Inches(0.15),
                circle_size, circle_size,
                font_size=14, font_color=RGBColor(255, 255, 255),
                bold=True, alignment=PP_ALIGN.CENTER,
            )

            # Thẻ phía trên (chỉ số chẵn)
            if i % 2 == 0:
                card_y = line_y - Inches(2.2)
                self.add_shape(
                    MSO_SHAPE.ROUNDED_RECTANGLE,
                    x, card_y, node_w, Inches(1.8),
                    fill_color=RGBColor(255, 255, 255),
                )
                self.add_textbox(
                    time,
                    x, card_y + Inches(0.1), node_w, Inches(0.3),
                    font_size=11, font_color=self._get_color("accent"),
                    bold=True, alignment=PP_ALIGN.CENTER,
                )
                self.add_textbox(
                    title,
                    x, card_y + Inches(0.4), node_w, Inches(0.35),
                    font_size=13, font_color=self._get_color("text_primary"),
                    bold=True, alignment=PP_ALIGN.CENTER,
                )
                self.add_textbox(
                    desc,
                    x + Inches(0.1), card_y + Inches(0.8), node_w - Inches(0.2), Inches(0.8),
                    font_size=9, font_color=self._get_color("text_secondary"),
                    alignment=PP_ALIGN.CENTER,
                )
            else:
                # Thẻ phía dưới (chỉ số lẻ)
                card_y = line_y + Inches(0.6)
                self.add_shape(
                    MSO_SHAPE.ROUNDED_RECTANGLE,
                    x, card_y, node_w, Inches(1.8),
                    fill_color=RGBColor(255, 255, 255),
                )
                self.add_textbox(
                    time,
                    x, card_y + Inches(0.1), node_w, Inches(0.3),
                    font_size=11, font_color=self._get_color("accent"),
                    bold=True, alignment=PP_ALIGN.CENTER,
                )
                self.add_textbox(
                    title,
                    x, card_y + Inches(0.4), node_w, Inches(0.35),
                    font_size=13, font_color=self._get_color("text_primary"),
                    bold=True, alignment=PP_ALIGN.CENTER,
                )
                self.add_textbox(
                    desc,
                    x + Inches(0.1), card_y + Inches(0.8), node_w - Inches(0.2), Inches(0.8),
                    font_size=9, font_color=self._get_color("text_secondary"),
                    alignment=PP_ALIGN.CENTER,
                )

    # ------------------------------------------------------------------ #
    #  Phương thức tạo chính
    # ------------------------------------------------------------------ #

    def generate(self):
        """Tạo trọn bộ 18 trang kế hoạch kinh doanh"""
        self._gen_cover()              # 1. Trang bìa
        self._gen_directory()          # 2. Mục lục
        self._add_section_title("Phân tích thị trường", "Market Analysis")  # 3. Tiêu đề phân mục
        self._gen_market_analysis(1)   # 4. Phân tích thị trường 1
        self._gen_market_analysis(2)   # 5. Phân tích thị trường 2
        self._gen_market_analysis(3)   # 6. Phân tích thị trường 3
        self._gen_team()               # 7. Giới thiệu đội ngũ
        self._gen_product(1)           # 8. Sản phẩm & dịch vụ 1
        self._gen_product(2)           # 9. Sản phẩm & dịch vụ 2
        self._gen_business_model()     # 10. Mô hình kinh doanh
        self._gen_competition()        # 11. Phân tích cạnh tranh
        self._add_section_title("Dự báo tài chính", "Financial Forecast")  # 12. Tiêu đề phân mục
        self._gen_financial(1)         # 13. Dự báo tài chính 1
        self._gen_financial(2)         # 14. Dự báo tài chính 2
        self._gen_financial(3)         # 15. Dự báo tài chính 3
        self._gen_funding()            # 16. Kế hoạch gọi vốn
        self._gen_roadmap()            # 17. Lộ trình phát triển
        self._add_thank_you()          # 18. Lời cảm ơn
        return self


if __name__ == "__main__":
    assembler = BusinessPlanAssembler()
    assembler.set_title("Kế hoạch kinh doanh").set_subtitle("Công ty Cổ phần Công nghệ Example - Năm 2025")
    assembler.generate()
    output_path = os.path.join(os.path.dirname(__file__), '..', '..', 'output_business_plan.pptx')
    assembler.save(output_path)
    print(f"Đã tạo kế hoạch kinh doanh: {output_path}")
