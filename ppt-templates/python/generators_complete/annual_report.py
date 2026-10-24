"""Bộ lắp ráp bài thuyết trình Báo cáo thường niên hoàn chỉnh

Tạo bài thuyết trình báo cáo thường niên gồm 22 trang:
Trang bìa -> Mục lục -> Tổng quan công ty -> Kết quả nổi bật (3 trang) -> Phân tích dữ liệu (4 trang) -> Phát triển đội ngũ -> Trách nhiệm xã hội -> Định hướng tương lai -> Lời cảm ơn

Mặc định sử dụng chủ đề Đỏ thương mại (red_business), phong cách bìa tàu xuyên sương.
"""

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from pptx.enum.shapes import MSO_SHAPE
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from python.base import TemplateGenerator
from python.utils import hex_to_rgb, set_shape_transparency


class AnnualReportAssembler(TemplateGenerator):
    """Bộ lắp ráp bài thuyết trình Báo cáo thường niên (22 slide)"""

    DEFAULT_THEME = {
        "primary": "#B71C1C",
        "secondary": "#C62828",
        "accent": "#E53935",
        "highlight": "#EF9A9A",
        "light": "#FFEBEE",
        "bg": "#FAFAFA",
        "text_primary": "#B71C1C",
        "text_secondary": "#455A64",
        "text_light": "#FFFFFF",
    }

    def __init__(self, theme=None):
        super().__init__(theme=theme)
        self._title = "Báo cáo thường niên"
        self._subtitle = "Annual Report"
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
            - company: Thông tin công ty
            - overview: Tổng quan công ty
            - achievements: Kết quả nổi bật trong năm
            - data_analysis: Phân tích dữ liệu
            - team: Phát triển đội ngũ
            - csr: Trách nhiệm xã hội
            - outlook: Định hướng tương lai
        """
        self._data = data
        return self

    def _get_color(self, key):
        if isinstance(self._theme, dict):
            return hex_to_rgb(self._theme.get(key, self._theme["primary"]))
        return hex_to_rgb(getattr(self._theme, key, self._theme.primary))

    # ------------------------------------------------------------------ #
    #  Phương thức hỗ trợ chung
    # ------------------------------------------------------------------ #

    def _add_bg(self, color_key="bg"):
        self.add_shape(
            MSO_SHAPE.RECTANGLE,
            Inches(0), Inches(0), Inches(10), Inches(7.5),
            fill_color=self._get_color(color_key),
        )

    def _add_page_title_bar(self, title):
        self.add_shape(
            MSO_SHAPE.RECTANGLE,
            Inches(0), Inches(0), Inches(10), Inches(1.0),
            fill_color=self._get_color("primary"),
        )
        self.add_textbox(
            title,
            Inches(0.6), Inches(0.15), Inches(8.8), Inches(0.7),
            font_size=28, font_color=RGBColor(255, 255, 255),
            bold=True, alignment=PP_ALIGN.LEFT,
        )

    def _add_section_title(self, title, subtitle=""):
        """Trang phân mục"""
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

    def _add_thank_you(self):
        self.create_slide()
        self.add_gradient_shape(
            MSO_SHAPE.RECTANGLE,
            Inches(0), Inches(0), Inches(10), Inches(7.5),
            [self._get_color("primary"), self._get_color("secondary")],
            angle=135,
        )
        self.add_textbox(
            "Thank You",
            Inches(1), Inches(2.2), Inches(8), Inches(1.2),
            font_size=48, font_color=RGBColor(255, 255, 255),
            bold=True, alignment=PP_ALIGN.CENTER,
        )
        self.add_textbox(
            "Tri ân mọi sự đóng góp và cống hiến",
            Inches(1), Inches(3.5), Inches(8), Inches(0.8),
            font_size=22, font_color=RGBColor(239, 154, 154),
            alignment=PP_ALIGN.CENTER,
        )
        line_w = Inches(2)
        self.add_shape(
            MSO_SHAPE.RECTANGLE,
            (Inches(10) - line_w) // 2, Inches(3.3),
            line_w, Pt(2),
            fill_color=RGBColor(239, 154, 154),
        )
        self.add_textbox(
            "Đồng hành phát triển - Vững bước tương lai",
            Inches(1), Inches(4.2), Inches(8), Inches(0.5),
            font_size=16, font_color=RGBColor(239, 154, 154),
            alignment=PP_ALIGN.CENTER,
        )

    def _add_stat_card(self, left, top, width, height, value, label, color_key="accent"):
        self.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            left, top, width, height,
            fill_color=RGBColor(255, 255, 255),
        )
        self.add_textbox(
            value,
            left, top + Inches(0.2), width, Inches(0.6),
            font_size=28, font_color=self._get_color(color_key),
            bold=True, alignment=PP_ALIGN.CENTER,
        )
        self.add_textbox(
            label,
            left, top + Inches(0.85), width, Inches(0.35),
            font_size=12, font_color=self._get_color("text_secondary"),
            alignment=PP_ALIGN.CENTER,
        )

    # ------------------------------------------------------------------ #
    #  Phương thức tạo từng trang slide
    # ------------------------------------------------------------------ #

    def _gen_cover(self):
        """Trang bìa: Phong cách tàu xuyên sương"""
        self.create_slide()
        primary = self._get_color("primary")
        secondary = self._get_color("secondary")
        accent = self._get_color("accent")
        highlight = self._get_color("highlight")
        light = self._get_color("light")

        # Nền tối chuyển sắc
        self.add_gradient_shape(
            MSO_SHAPE.RECTANGLE,
            Inches(0), Inches(0), Inches(10), Inches(7.5),
            [primary, secondary], angle=160,
        )

        # Hiệu ứng sương mù - nhiều lớp hình chữ nhật bán trong suốt
        fog_layers = [
            (Inches(0), Inches(4.5), Inches(10), Inches(3.0), highlight, 0.85),
            (Inches(0), Inches(5.0), Inches(10), Inches(2.5), highlight, 0.88),
            (Inches(0), Inches(5.5), Inches(10), Inches(2.0), highlight, 0.92),
        ]
        for left, top, w, h, color, trans in fog_layers:
            shape = self.add_shape(
                MSO_SHAPE.RECTANGLE, left, top, w, h,
                fill_color=color,
            )
            set_shape_transparency(shape, trans)

        # Đường ray tàu hỏa
        for offset in [Inches(3.5), Inches(4.0), Inches(4.5)]:
            self.add_shape(
                MSO_SHAPE.RECTANGLE,
                Inches(0), offset, Inches(10), Pt(2),
                fill_color=RGBColor(255, 255, 255),
            )
            set_shape_transparency(self.slide.shapes[-1], 0.3)

        # Vạch tốc độ trang trí
        for i in range(5):
            line_w = Inches(1.5 - i * 0.2)
            self.add_shape(
                MSO_SHAPE.RECTANGLE,
                Inches(0.5 + i * 0.8), Inches(3.0 + i * 0.3),
                line_w, Pt(2),
                fill_color=RGBColor(255, 255, 255),
            )
            set_shape_transparency(self.slide.shapes[-1], 0.2 + i * 0.1)

        # Tiêu đề chính
        self.add_textbox(
            self._title,
            Inches(1.5), Inches(1.8), Inches(7.0), Inches(1.2),
            font_size=44, font_color=RGBColor(255, 255, 255),
            bold=True, alignment=PP_ALIGN.CENTER,
        )
        # Năm
        self.add_textbox(
            "2025",
            Inches(1.5), Inches(3.0), Inches(7.0), Inches(0.8),
            font_size=36, font_color=RGBColor(239, 154, 154),
            bold=True, alignment=PP_ALIGN.CENTER,
        )
        # Đường phân cách
        line_w = Inches(3)
        self.add_shape(
            MSO_SHAPE.RECTANGLE,
            (Inches(10) - line_w) // 2, Inches(3.85),
            line_w, Pt(2),
            fill_color=RGBColor(239, 154, 154),
        )
        # Tiêu đề phụ
        self.add_textbox(
            self._subtitle,
            Inches(1.5), Inches(4.1), Inches(7.0), Inches(0.8),
            font_size=20, font_color=RGBColor(239, 154, 154),
            alignment=PP_ALIGN.CENTER,
        )

    def _gen_directory(self):
        self.create_slide()
        self._add_bg()
        self._add_page_title_bar("Mục lục")

        sections = [
            ("01", "Tổng quan doanh nghiệp"),
            ("02", "Kết quả nổi bật"),
            ("03", "Phân tích dữ liệu"),
            ("04", "Phát triển đội ngũ"),
            ("05", "Trách nhiệm xã hội"),
            ("06", "Định hướng tương lai"),
        ]
        card_w = Inches(2.6)
        card_h = Inches(1.6)
        gap = Inches(0.4)
        cols = 3
        start_x = (Inches(10) - (cols * card_w + (cols - 1) * gap)) // 2
        start_y = Inches(1.5)

        for i, (num, title) in enumerate(sections):
            row, col = divmod(i, cols)
            x = start_x + col * (card_w + gap)
            y = start_y + row * (card_h + gap)
            self.add_shape(
                MSO_SHAPE.ROUNDED_RECTANGLE,
                x, y, card_w, card_h,
                fill_color=RGBColor(255, 255, 255),
            )
            self.add_shape(
                MSO_SHAPE.RECTANGLE,
                x, y, card_w, Inches(0.06),
                fill_color=self._get_color("accent"),
            )
            self.add_textbox(
                num,
                x, y + Inches(0.2), card_w, Inches(0.5),
                font_size=24, font_color=self._get_color("accent"),
                bold=True, alignment=PP_ALIGN.CENTER,
            )
            self.add_textbox(
                title,
                x, y + Inches(0.8), card_w, Inches(0.4),
                font_size=16, font_color=self._get_color("text_primary"),
                bold=True, alignment=PP_ALIGN.CENTER,
            )

    def _gen_overview(self):
        """Trang tổng quan doanh nghiệp"""
        self.create_slide()
        self._add_bg()
        self._add_page_title_bar("Tổng quan doanh nghiệp")

        overview_items = [
            ("Thành lập", "Năm 2018"),
            ("Quy mô nhân sự", "500+"),
            ("Phạm vi hoạt động", "Hơn 20 tỉnh thành"),
            ("Khách hàng phục vụ", "2000+ doanh nghiệp"),
        ]

        box_w = Inches(2.0)
        box_h = Inches(1.5)
        gap = Inches(0.3)
        start_x = (Inches(10) - (4 * box_w + 3 * gap)) // 2

        for i, (label, value) in enumerate(overview_items):
            x = start_x + i * (box_w + gap)
            y = Inches(1.5)
            self.add_shape(
                MSO_SHAPE.ROUNDED_RECTANGLE,
                x, y, box_w, box_h,
                fill_color=RGBColor(255, 255, 255),
            )
            self.add_textbox(
                value,
                x, y + Inches(0.3), box_w, Inches(0.5),
                font_size=24, font_color=self._get_color("accent"),
                bold=True, alignment=PP_ALIGN.CENTER,
            )
            self.add_textbox(
                label,
                x, y + Inches(0.9), box_w, Inches(0.3),
                font_size=12, font_color=self._get_color("text_secondary"),
                alignment=PP_ALIGN.CENTER,
            )

        # Giới thiệu công ty
        self.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            Inches(0.5), Inches(3.3), Inches(9.0), Inches(3.5),
            fill_color=RGBColor(255, 255, 255),
        )
        self.add_textbox(
            "Giới thiệu doanh nghiệp",
            Inches(0.8), Inches(3.5), Inches(8.4), Inches(0.4),
            font_size=16, font_color=self._get_color("text_primary"),
            bold=True, alignment=PP_ALIGN.LEFT,
        )
        desc = (
            "Chúng tôi là doanh nghiệp công nghệ tiên phong chuyên sâu về chuyển đổi số, cam kết ứng dụng trí tuệ nhân tạo, "
            "dữ liệu lớn và điện toán đám mây nhằm cung cấp giải pháp chuyển đổi số toàn diện cho đối tác. "
            "Sau hơn 7 năm phát triển, công ty đã đồng hành cùng hơn 2.000 khách hàng doanh nghiệp "
            "trong các lĩnh vực tài chính, sản xuất, bán lẻ và y tế."
        )
        self.add_textbox(
            desc,
            Inches(0.8), Inches(4.1), Inches(8.4), Inches(2.5),
            font_size=13, font_color=self._get_color("text_secondary"),
            alignment=PP_ALIGN.LEFT,
        )

    def _gen_achievement(self, page_num=1):
        """Trang kết quả nổi bật"""
        self.create_slide()
        self._add_bg()
        self._add_page_title_bar(f"Kết quả nổi bật - Phần {page_num}")

        contents = {
            1: ("Tăng trưởng doanh thu", [
                {"value": "250 tỷ", "label": "Doanh thu năm"},
                {"value": "35%", "label": "Tăng trưởng theo năm"},
                {"value": "85%", "label": "Tỷ lệ tái ký hợp đồng"},
            ]),
            2: ("Mở rộng thị trường", [
                {"value": "20+", "label": "Thành phố hiện diện"},
                {"value": "500+", "label": "Khách hàng doanh nghiệp mới"},
                {"value": "50+", "label": "Đối tác chiến lược"},
            ]),
            3: ("Đổi mới sản phẩm", [
                {"value": "12", "label": "Sản phẩm mới ra mắt"},
                {"value": "30+", "label": "Bằng sáng chế & bản quyền"},
                {"value": "99.9%", "label": "Độ sẵn sàng hệ thống"},
            ]),
        }

        title, items = contents.get(page_num, ("Kết quả nổi bật", []))

        # Tiêu đề lớn
        self.add_textbox(
            title,
            Inches(0.6), Inches(1.3), Inches(8.8), Inches(0.5),
            font_size=20, font_color=self._get_color("text_primary"),
            bold=True, alignment=PP_ALIGN.LEFT,
        )

        # Thẻ dữ liệu
        box_w = Inches(2.6)
        box_h = Inches(2.0)
        gap = Inches(0.4)
        start_x = (Inches(10) - (3 * box_w + 2 * gap)) // 2

        for i, item in enumerate(items):
            x = start_x + i * (box_w + gap)
            y = Inches(2.0)
            self._add_stat_card(x, y, box_w, box_h, item["value"], item["label"])

        # Thuyết minh chi tiết
        details = {
            1: ["Doanh thu nghiệp vụ nòng cốt chiếm 70%", "Mảng kinh doanh mới đóng góp tăng trưởng liên tục", "Biên lợi nhuận gộp duy trì trên 60%"],
            2: ["Phát triển cân bằng tại 3 miền Bắc, Trung, Nam", "Bắt đầu triển khai chiến lược thị trường quốc tế", "Mạng lưới đối tác phân phối không ngừng mở rộng"],
            3: ["Chi phí R&D chiếm 20% doanh thu", "Làm chủ hoàn toàn công nghệ lõi độc quyền", "Chỉ số hài lòng sản phẩm đạt 4.8/5.0"],
        }
        detail_items = details.get(page_num, [])
        dy = Inches(4.5)
        for d in detail_items:
            self.add_textbox(
                f"  {d}",
                Inches(1.0), dy, Inches(8.0), Inches(0.35),
                font_size=12, font_color=self._get_color("text_secondary"),
                alignment=PP_ALIGN.LEFT,
            )
            dy += Inches(0.4)

    def _gen_data_analysis(self, page_num=1):
        """Trang phân tích dữ liệu"""
        self.create_slide()
        self._add_bg()
        self._add_page_title_bar(f"Phân tích dữ liệu - Phần {page_num}")

        contents = {
            1: ("Xu hướng doanh thu", {
                "labels": ["Quý 1", "Quý 2", "Quý 3", "Quý 4"],
                "values": ["50 tỷ", "60 tỷ", "70 tỷ", "70 tỷ"],
                "total": "250 tỷ VNĐ",
            }),
            2: ("Cơ cấu khách hàng", {
                "labels": ["Tài chính", "Sản xuất", "Bán lẻ", "Y tế", "Khác"],
                "values": ["30%", "25%", "20%", "15%", "10%"],
                "total": "2000+ Khách hàng",
            }),
            3: ("Mức độ sử dụng sản phẩm", {
                "labels": ["Phân tích dữ liệu", "Tự động hóa", "Cộng tác", "API"],
                "values": ["85%", "70%", "60%", "45%"],
                "total": "DAU 500k+",
            }),
            4: ("Độ hài lòng", {
                "labels": ["Tính năng", "Hiệu năng", "Dịch vụ", "Chi phí"],
                "values": ["4.8", "4.7", "4.6", "4.5"],
                "total": "Tổng thể 4.65/5.0",
            }),
        }

        title, data = contents.get(page_num, ("Phân tích dữ liệu", {}))

        # Khối bên trái - Tiêu đề và tổng quan
        self.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            Inches(0.5), Inches(1.3), Inches(4.2), Inches(5.5),
            fill_color=RGBColor(255, 255, 255),
        )
        self.add_textbox(
            title,
            Inches(0.8), Inches(1.5), Inches(3.6), Inches(0.4),
            font_size=18, font_color=self._get_color("text_primary"),
            bold=True, alignment=PP_ALIGN.LEFT,
        )
        self.add_textbox(
            data.get("total", ""),
            Inches(0.8), Inches(2.1), Inches(3.6), Inches(0.6),
            font_size=28, font_color=self._get_color("accent"),
            bold=True, alignment=PP_ALIGN.LEFT,
        )
        # Khu vực biểu đồ mô phỏng
        chart_h = Inches(3.0)
        self.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            Inches(0.8), Inches(3.0), Inches(3.6), chart_h,
            fill_color=self._get_color("light"),
        )
        set_shape_transparency(self.slide.shapes[-1], 0.3)
        self.add_textbox(
            "Khu vực biểu đồ",
            Inches(0.8), Inches(4.2), Inches(3.6), Inches(0.4),
            font_size=12, font_color=self._get_color("text_secondary"),
            alignment=PP_ALIGN.CENTER,
        )

        # Khối bên phải - Chi tiết từng chỉ tiêu
        labels = data.get("labels", [])
        values = data.get("values", [])
        self.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            Inches(5.0), Inches(1.3), Inches(4.5), Inches(5.5),
            fill_color=RGBColor(255, 255, 255),
        )
        self.add_textbox(
            "Dữ liệu chi tiết",
            Inches(5.3), Inches(1.5), Inches(3.9), Inches(0.4),
            font_size=14, font_color=self._get_color("text_primary"),
            bold=True, alignment=PP_ALIGN.LEFT,
        )

        for i, (label, value) in enumerate(zip(labels, values)):
            y = Inches(2.2 + i * 1.1)
            self.add_textbox(
                label,
                Inches(5.3), y, Inches(2.0), Inches(0.3),
                font_size=12, font_color=self._get_color("text_secondary"),
                alignment=PP_ALIGN.LEFT,
            )
            # Nền thanh tiến độ
            bar_y = y + Inches(0.35)
            bar_w = Inches(3.5)
            bar_h = Inches(0.3)
            self.add_shape(
                MSO_SHAPE.ROUNDED_RECTANGLE,
                Inches(5.3), bar_y, bar_w, bar_h,
                fill_color=self._get_color("light"),
            )
            # Tiền cảnh thanh tiến độ
            progress = 0.3 + (4 - i) * 0.15
            self.add_shape(
                MSO_SHAPE.ROUNDED_RECTANGLE,
                Inches(5.3), bar_y, int(bar_w * progress), bar_h,
                fill_color=self._get_color("accent"),
            )
            # Giá trị
            self.add_textbox(
                value,
                Inches(5.3), bar_y + Inches(0.35), Inches(3.5), Inches(0.25),
                font_size=11, font_color=self._get_color("text_primary"),
                bold=True, alignment=PP_ALIGN.LEFT,
            )

    def _gen_team_building(self):
        """Trang phát triển đội ngũ"""
        self.create_slide()
        self._add_bg()
        self._add_page_title_bar("Phát triển đội ngũ")

        stats = [
            {"value": "500+", "label": "Quy mô nhân sự", "growth": "Tăng 25% theo năm"},
            {"value": "45%", "label": "Trình độ Thạc sĩ/Tiến sĩ", "growth": "Trọng tâm kỹ sư công nghệ"},
            {"value": "92%", "label": "Hài lòng nhân viên", "growth": "Mức dẫn đầu ngành"},
        ]

        box_w = Inches(2.6)
        box_h = Inches(2.0)
        gap = Inches(0.4)
        start_x = (Inches(10) - (3 * box_w + 2 * gap)) // 2

        for i, stat in enumerate(stats):
            x = start_x + i * (box_w + gap)
            y = Inches(1.3)
            self.add_shape(
                MSO_SHAPE.ROUNDED_RECTANGLE,
                x, y, box_w, box_h,
                fill_color=RGBColor(255, 255, 255),
            )
            self.add_textbox(
                stat["value"],
                x, y + Inches(0.2), box_w, Inches(0.5),
                font_size=28, font_color=self._get_color("accent"),
                bold=True, alignment=PP_ALIGN.CENTER,
            )
            self.add_textbox(
                stat["label"],
                x, y + Inches(0.75), box_w, Inches(0.3),
                font_size=14, font_color=self._get_color("text_primary"),
                bold=True, alignment=PP_ALIGN.CENTER,
            )
            self.add_textbox(
                stat["growth"],
                x, y + Inches(1.15), box_w, Inches(0.3),
                font_size=10, font_color=self._get_color("text_secondary"),
                alignment=PP_ALIGN.CENTER,
            )

        # Các sáng kiến xây dựng đội ngũ
        initiatives = [
            ("Đào tạo nhân tài", "Kế hoạch đào tạo bao phủ 100% nhân viên\nHơn 20 buổi tọa đàm cùng chuyên gia hàng đầu"),
            ("Văn hóa doanh nghiệp", "Hoạt động gắn kết đội ngũ định kỳ\nQuỹ phúc lợi và chăm sóc nhân viên"),
            ("Cơ chế đãi ngộ", "Chính sách cổ phần thưởng ESOP\nCơ chế thưởng hiệu quả công việc cạnh tranh"),
        ]

        card_w = Inches(2.6)
        card_h = Inches(2.5)
        gap = Inches(0.4)
        start_x = (Inches(10) - (3 * card_w + 2 * gap)) // 2
        start_y = Inches(3.8)

        for i, (title, desc) in enumerate(initiatives):
            x = start_x + i * (card_w + gap)
            self.add_shape(
                MSO_SHAPE.ROUNDED_RECTANGLE,
                x, start_y, card_w, card_h,
                fill_color=RGBColor(255, 255, 255),
            )
            self.add_shape(
                MSO_SHAPE.RECTANGLE,
                x, start_y, card_w, Inches(0.06),
                fill_color=self._get_color("accent"),
            )
            self.add_textbox(
                title,
                x, start_y + Inches(0.25), card_w, Inches(0.35),
                font_size=14, font_color=self._get_color("text_primary"),
                bold=True, alignment=PP_ALIGN.CENTER,
            )
            self.add_textbox(
                desc,
                x + Inches(0.3), start_y + Inches(0.8), card_w - Inches(0.6), Inches(1.5),
                font_size=11, font_color=self._get_color("text_secondary"),
                alignment=PP_ALIGN.CENTER,
            )

    def _gen_csr(self):
        """Trang trách nhiệm xã hội"""
        self.create_slide()
        self._add_bg()
        self._add_page_title_bar("Trách nhiệm xã hội")

        csr_items = [
            ("Bảo vệ môi trường", "Giảm 30% phát thải carbon\nVăn phòng xanh không rác thải nhựa\nƯu tiên nguồn năng lượng sạch"),
            ("Hoạt động thiện nguyện", "Ngân sách an sinh xã hội 2 tỷ đồng\nDự án học bổng thắp sáng ước mơ\nHỗ trợ chuyển đổi số vùng sâu vùng xa"),
            ("Gắn kết cộng đồng", "Hơn 500 lượt nhân viên tình nguyện\nNgày hội trải nghiệm công nghệ\nChia sẻ tri thức học thuật cho sinh viên"),
        ]

        card_w = Inches(2.6)
        card_h = Inches(4.0)
        gap = Inches(0.4)
        start_x = (Inches(10) - (3 * card_w + 2 * gap)) // 2

        for i, (title, desc) in enumerate(csr_items):
            x = start_x + i * (card_w + gap)
            y = Inches(1.3)
            self.add_shape(
                MSO_SHAPE.ROUNDED_RECTANGLE,
                x, y, card_w, card_h,
                fill_color=RGBColor(255, 255, 255),
            )
            # Biểu tượng
            icon_size = Inches(0.8)
            self.add_shape(
                MSO_SHAPE.OVAL,
                x + (card_w - icon_size) // 2, y + Inches(0.3),
                icon_size, icon_size,
                fill_color=self._get_color("accent"),
            )
            set_shape_transparency(self.slide.shapes[-1], 0.15)
            self.add_textbox(
                str(i + 1),
                x + (card_w - icon_size) // 2, y + Inches(0.38),
                icon_size, icon_size,
                font_size=24, font_color=RGBColor(255, 255, 255),
                bold=True, alignment=PP_ALIGN.CENTER,
            )
            self.add_textbox(
                title,
                x, y + Inches(1.3), card_w, Inches(0.4),
                font_size=16, font_color=self._get_color("text_primary"),
                bold=True, alignment=PP_ALIGN.CENTER,
            )
            self.add_textbox(
                desc,
                x + Inches(0.3), y + Inches(1.9), card_w - Inches(0.6), Inches(1.8),
                font_size=12, font_color=self._get_color("text_secondary"),
                alignment=PP_ALIGN.CENTER,
            )

    def _gen_outlook(self):
        """Trang định hướng tương lai"""
        self.create_slide()
        self._add_bg()
        self._add_page_title_bar("Định hướng tương lai")

        goals = [
            ("Mục tiêu năm 2026", "Doanh thu vượt mốc 500 tỷ VNĐ\nGấp đôi số lượng khách hàng\nKhởi động thị trường Đông Nam Á"),
            ("Trọng tâm chiến lược", "Phát triển chuyên sâu sản phẩm AI\nHoàn thiện giải pháp theo ngành\nXây dựng hệ sinh thái mở rộng lớn"),
            ("Nâng cấp tổ chức", "Quy mô đội ngũ đạt 800 nhân sự\nHoàn thiện cấu trúc đa quốc gia\nTối ưu hóa hiệu suất làm việc"),
        ]

        card_w = Inches(2.6)
        card_h = Inches(4.0)
        gap = Inches(0.4)
        start_x = (Inches(10) - (3 * card_w + 2 * gap)) // 2

        for i, (title, desc) in enumerate(goals):
            x = start_x + i * (card_w + gap)
            y = Inches(1.3)
            self.add_shape(
                MSO_SHAPE.ROUNDED_RECTANGLE,
                x, y, card_w, card_h,
                fill_color=RGBColor(255, 255, 255),
            )
            # Chuyển sắc phía trên
            self.add_gradient_shape(
                MSO_SHAPE.RECTANGLE,
                x, y, card_w, Inches(1.0),
                [self._get_color("primary"), self._get_color("accent")],
                angle=90,
            )
            self.add_textbox(
                title,
                x, y + Inches(0.2), card_w, Inches(0.5),
                font_size=16, font_color=RGBColor(255, 255, 255),
                bold=True, alignment=PP_ALIGN.CENTER,
            )
            self.add_textbox(
                desc,
                x + Inches(0.3), y + Inches(1.3), card_w - Inches(0.6), Inches(2.5),
                font_size=12, font_color=self._get_color("text_secondary"),
                alignment=PP_ALIGN.LEFT,
            )

    # ------------------------------------------------------------------ #
    #  Phương thức tạo chính
    # ------------------------------------------------------------------ #

    def generate(self):
        """Tạo trọn bộ 22 trang báo cáo thường niên"""
        self._gen_cover()              # 1. Trang bìa
        self._gen_directory()          # 2. Mục lục
        self._add_section_title("Tổng quan doanh nghiệp", "Company Overview")  # 3. Tiêu đề phân mục
        self._gen_overview()           # 4. Tổng quan doanh nghiệp
        self._add_section_title("Kết quả nổi bật", "Annual Achievements")  # 5. Tiêu đề phân mục
        self._gen_achievement(1)       # 6. Kết quả nổi bật - Tăng trưởng doanh thu
        self._gen_achievement(2)       # 7. Kết quả nổi bật - Mở rộng thị trường
        self._gen_achievement(3)       # 8. Kết quả nổi bật - Đổi mới sản phẩm
        self._add_section_title("Điểm sáng hoạt động", "Performance Highlights")  # 9. Tiêu đề phân mục
        self._add_section_title("Phân tích dữ liệu", "Data Analysis")  # 10. Tiêu đề phân mục
        self._gen_data_analysis(1)     # 11. Phân tích dữ liệu - Xu hướng doanh thu
        self._gen_data_analysis(2)     # 12. Phân tích dữ liệu - Cơ cấu khách hàng
        self._gen_data_analysis(3)     # 13. Phân tích dữ liệu - Mức độ sử dụng sản phẩm
        self._gen_data_analysis(4)     # 14. Phân tích dữ liệu - Độ hài lòng
        self._add_section_title("Đội ngũ & Văn hóa", "Team & Culture")  # 15. Tiêu đề phân mục
        self._gen_team_building()      # 16. Phát triển đội ngũ
        self._add_section_title("Trách nhiệm xã hội", "CSR")  # 17. Tiêu đề phân mục
        self._gen_csr()                # 18. Trách nhiệm xã hội
        self._add_section_title("Định hướng tương lai", "Future Outlook")  # 19. Tiêu đề phân mục
        self._gen_outlook()            # 20. Định hướng tương lai
        self._add_section_title("Tổng kết & Đánh giá", "Summary")  # 21. Tiêu đề phân mục
        self._add_thank_you()          # 22. Lời cảm ơn
        return self


if __name__ == "__main__":
    assembler = AnnualReportAssembler()
    assembler.set_title("Báo cáo thường niên").set_subtitle("Báo cáo kết quả hoạt động năm 2025")
    assembler.generate()
    output_path = os.path.join(os.path.dirname(__file__), '..', '..', 'output_annual_report.pptx')
    assembler.save(output_path)
    print(f"Đã tạo báo cáo thường niên: {output_path}")
