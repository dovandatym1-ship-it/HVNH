"""Bộ lắp ráp bài thuyết trình Định hướng sự nghiệp hoàn chỉnh

Tạo bài thuyết trình định hướng sự nghiệp gồm 16 trang:
Trang bìa -> Mục lục -> Thấu hiểu bản thân (2 trang) -> Khám phá nghề nghiệp (2 trang) -> Thiết lập mục tiêu -> Nâng cao năng lực (2 trang) -> Kinh nghiệm thực tiễn -> Thành tựu nổi bật -> Định hướng tương lai -> Lời cảm ơn

Mặc định sử dụng chủ đề Tím chuyển sắc, bìa phong cách vòng tròn.
"""

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from pptx.enum.shapes import MSO_SHAPE
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from python.base import TemplateGenerator
from python.utils import hex_to_rgb, set_shape_transparency, create_circle_positions


class CareerPlanningAssembler(TemplateGenerator):
    """Bộ lắp ráp bài thuyết trình Định hướng sự nghiệp (16 slide)"""

    DEFAULT_THEME = {
        "primary": "#4A148C",
        "secondary": "#6A1B9A",
        "accent": "#9C27B0",
        "highlight": "#CE93D8",
        "light": "#F3E5F5",
        "bg": "#FAFAFA",
        "text_primary": "#4A148C",
        "text_secondary": "#5D4037",
        "text_light": "#FFFFFF",
    }

    def __init__(self, theme=None):
        super().__init__(theme=theme)
        self._title = "Kế hoạch định hướng sự nghiệp"
        self._subtitle = "Career Planning"
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
            - self_analysis: Nội dung thấu hiểu bản thân
            - career_exploration: Nội dung khám phá nghề nghiệp
            - goals: Thiết lập mục tiêu
            - skills: Kế hoạch nâng cao năng lực
            - experiences: Kinh nghiệm thực tiễn
            - achievements: Thành tựu nổi bật
            - future_plan: Định hướng tương lai
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
        bar_color = self._get_color("primary")
        self.add_shape(
            MSO_SHAPE.RECTANGLE,
            Inches(0), Inches(0), Inches(10), Inches(1.0),
            fill_color=bar_color,
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
            Inches(1), Inches(2.5), Inches(8), Inches(1.2),
            font_size=48, font_color=RGBColor(255, 255, 255),
            bold=True, alignment=PP_ALIGN.CENTER,
        )
        self.add_textbox(
            "Trân trọng cảm ơn",
            Inches(1), Inches(3.8), Inches(8), Inches(0.8),
            font_size=24, font_color=RGBColor(206, 147, 216),
            alignment=PP_ALIGN.CENTER,
        )
        line_w = Inches(2)
        self.add_shape(
            MSO_SHAPE.RECTANGLE,
            (Inches(10) - line_w) // 2, Inches(3.55),
            line_w, Pt(2),
            fill_color=RGBColor(206, 147, 216),
        )

    # ------------------------------------------------------------------ #
    #  Phương thức tạo từng trang slide
    # ------------------------------------------------------------------ #

    def _gen_cover(self):
        """Trang bìa: Phong cách vòng tròn"""
        self.create_slide()
        primary = self._get_color("primary")
        secondary = self._get_color("secondary")
        accent = self._get_color("accent")
        highlight = self._get_color("highlight")

        # Nền chuyển sắc
        self.add_gradient_shape(
            MSO_SHAPE.RECTANGLE,
            Inches(0), Inches(0), Inches(10), Inches(7.5),
            [primary, secondary], angle=135,
        )

        # Vòng tròn lớn trung tâm
        ring_size = Inches(3.5)
        cx = Inches(5) - ring_size // 2
        cy = Inches(3.75) - ring_size // 2
        self.add_shape(
            MSO_SHAPE.OVAL,
            cx, cy, ring_size, ring_size,
            fill_color=accent,
        )
        set_shape_transparency(self.slide.shapes[-1], 0.7)
        # Vòng tròn bên trong
        inner_size = Inches(2.5)
        self.add_shape(
            MSO_SHAPE.OVAL,
            Inches(5) - inner_size // 2, Inches(3.75) - inner_size // 2,
            inner_size, inner_size,
            fill_color=primary,
        )

        # Các chấm tròn trang trí viền ngoài
        positions = create_circle_positions(Inches(5), Inches(3.75), Inches(3.2), 8, start_angle=0)
        for px, py in positions:
            self.add_shape(
                MSO_SHAPE.OVAL,
                px - Inches(0.15), py - Inches(0.15),
                Inches(0.3), Inches(0.3),
                fill_color=highlight,
            )
            set_shape_transparency(self.slide.shapes[-1], 0.4)

        # Tiêu đề
        self.add_textbox(
            self._title,
            Inches(1.5), Inches(2.6), Inches(7.0), Inches(1.2),
            font_size=40, font_color=RGBColor(255, 255, 255),
            bold=True, alignment=PP_ALIGN.CENTER,
        )
        # Đường phân cách
        line_w = Inches(2)
        self.add_shape(
            MSO_SHAPE.RECTANGLE,
            (Inches(10) - line_w) // 2, Inches(3.85),
            line_w, Pt(2),
            fill_color=RGBColor(206, 147, 216),
        )
        # Tiêu đề phụ
        self.add_textbox(
            self._subtitle,
            Inches(1.5), Inches(4.1), Inches(7.0), Inches(0.8),
            font_size=20, font_color=RGBColor(206, 147, 216),
            alignment=PP_ALIGN.CENTER,
        )

    def _gen_directory(self):
        self.create_slide()
        self._add_bg()
        self._add_page_title_bar("Mục lục")

        sections = [
            ("01", "Thấu hiểu bản thân"),
            ("02", "Khám phá nghề nghiệp"),
            ("03", "Thiết lập mục tiêu"),
            ("04", "Nâng cao năng lực"),
            ("05", "Kinh nghiệm thực tiễn"),
            ("06", "Thành tựu nổi bật"),
            ("07", "Định hướng tương lai"),
        ]
        card_w = Inches(2.2)
        card_h = Inches(1.5)
        gap = Inches(0.35)
        cols = 4
        start_x = (Inches(10) - (cols * card_w + (cols - 1) * gap)) // 2
        start_y = Inches(1.6)

        for i, (num, title) in enumerate(sections):
            row, col = divmod(i, cols)
            x = start_x + col * (card_w + gap)
            y = start_y + row * (card_h + gap)
            self._add_content_card(x, y, card_w, card_h, title, num)

    def _add_content_card(self, left, top, width, height, title, num=""):
        self.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            left, top, width, height,
            fill_color=RGBColor(255, 255, 255),
        )
        self.add_shape(
            MSO_SHAPE.RECTANGLE,
            left, top, width, Inches(0.06),
            fill_color=self._get_color("accent"),
        )
        if num:
            circle_size = Inches(0.45)
            self.add_shape(
                MSO_SHAPE.OVAL,
                left + Inches(0.2), top + Inches(0.2),
                circle_size, circle_size,
                fill_color=self._get_color("accent"),
            )
            self.add_textbox(
                num,
                left + Inches(0.2), top + Inches(0.2),
                circle_size, circle_size,
                font_size=14, font_color=RGBColor(255, 255, 255),
                bold=True, alignment=PP_ALIGN.CENTER,
            )
        title_x = left + Inches(0.75) if num else left + Inches(0.2)
        self.add_textbox(
            title,
            title_x, top + Inches(0.2),
            width - Inches(1.0), Inches(0.4),
            font_size=14, font_color=self._get_color("text_primary"),
            bold=True, alignment=PP_ALIGN.LEFT,
        )

    def _gen_self_analysis(self, page_num=1):
        """Trang thấu hiểu bản thân"""
        self.create_slide()
        self._add_bg()
        self._add_page_title_bar(f"Thấu hiểu bản thân - Phần {page_num}")

        contents = {
            1: ("Đặc điểm tính cách", [
                "Nhóm tính cách MBTI: INTJ / ENTJ",
                "Tư duy logic và khả năng lập kế hoạch xuất sắc",
                "Định hướng mục tiêu, tính kỷ luật và thực thi cao",
                "Chú trọng hiệu quả công việc và kết quả thực tế",
            ]),
            2: ("Sở thích & Giá trị cốt lõi", [
                "Đam mê công nghệ tiên phong và đổi mới sáng tạo",
                "Không ngừng học hỏi và phát triển bản thân",
                "Coi trọng tinh thần đồng đội và tầm ảnh hưởng tích cực",
                "Khao khát tạo ra giá trị hữu ích cho cộng đồng",
            ]),
        }
        title, items = contents.get(page_num, ("Thấu hiểu bản thân", []))

        # Thẻ lớn bên trái
        self.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            Inches(0.5), Inches(1.5), Inches(5.0), Inches(5.0),
            fill_color=RGBColor(255, 255, 255),
        )
        self.add_textbox(
            title,
            Inches(0.8), Inches(1.7), Inches(4.4), Inches(0.5),
            font_size=20, font_color=self._get_color("text_primary"),
            bold=True, alignment=PP_ALIGN.LEFT,
        )
        y_pos = Inches(2.4)
        for item in items:
            self.add_textbox(
                f"  {item}",
                Inches(0.8), y_pos, Inches(4.4), Inches(0.35),
                font_size=13, font_color=self._get_color("text_secondary"),
                alignment=PP_ALIGN.LEFT,
            )
            y_pos += Inches(0.45)

        # Khung giữ chỗ biểu đồ radar bên phải
        self.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            Inches(5.8), Inches(1.5), Inches(3.7), Inches(5.0),
            fill_color=RGBColor(255, 255, 255),
        )
        self.add_textbox(
            "Biểu đồ radar năng lực",
            Inches(5.8), Inches(1.7), Inches(3.7), Inches(0.4),
            font_size=14, font_color=self._get_color("accent"),
            bold=True, alignment=PP_ALIGN.CENTER,
        )
        # Các vòng tròn mô phỏng biểu đồ radar
        radar_size = Inches(2.5)
        self.add_shape(
            MSO_SHAPE.OVAL,
            Inches(5.8) + (Inches(3.7) - radar_size) // 2,
            Inches(2.3) + (Inches(4.0) - radar_size) // 2,
            radar_size, radar_size,
            fill_color=self._get_color("light"),
        )
        set_shape_transparency(self.slide.shapes[-1], 0.5)
        labels = ["Lãnh đạo", "Giao tiếp", "Kỹ thuật", "Đổi mới", "Thực thi"]
        positions = create_circle_positions(
            Inches(7.65), Inches(4.3), Inches(1.2), 5, start_angle=-90
        )
        for (px, py), label in zip(positions, labels):
            self.add_textbox(
                label,
                px - Inches(0.5), py - Inches(0.12),
                Inches(1.0), Inches(0.25),
                font_size=9, font_color=self._get_color("text_secondary"),
                bold=True, alignment=PP_ALIGN.CENTER,
            )

    def _gen_career_exploration(self, page_num=1):
        """Trang khám phá nghề nghiệp"""
        self.create_slide()
        self._add_bg()
        self._add_page_title_bar(f"Khám phá nghề nghiệp - Phần {page_num}")

        contents = {
            1: ("Phân tích ngành", [
                {"title": "Công nghệ Internet", "desc": "Tăng trưởng liên tục\nNhu cầu nhân tài lớn"},
                {"title": "Trí tuệ nhân tạo", "desc": "Lĩnh vực đột phá\nTriển vọng rộng mở"},
                {"title": "Năng lượng mới", "desc": "Chính sách hỗ trợ\nPhát triển bền vững"},
            ]),
            2: ("Nghiên cứu vị trí", [
                {"title": "Giám đốc Sản phẩm", "desc": "Thấu hiểu người dùng\nQuản lý yêu cầu"},
                {"title": "Giám đốc Kỹ thuật", "desc": "Kiến trúc hệ thống\nQuản trị đội ngũ"},
                {"title": "Đối tác khởi nghiệp", "desc": "Tư duy kinh doanh\nTối ưu nguồn lực"},
            ]),
        }
        section_title, items = contents.get(page_num, ("Khám phá nghề nghiệp", []))

        card_w = Inches(2.6)
        card_h = Inches(3.5)
        gap = Inches(0.4)
        start_x = (Inches(10) - (3 * card_w + 2 * gap)) // 2

        for i, item in enumerate(items):
            x = start_x + i * (card_w + gap)
            y = Inches(1.5)
            self.add_shape(
                MSO_SHAPE.ROUNDED_RECTANGLE,
                x, y, card_w, card_h,
                fill_color=RGBColor(255, 255, 255),
            )
            # Khu vực biểu tượng
            icon_size = Inches(0.8)
            self.add_shape(
                MSO_SHAPE.OVAL,
                x + (card_w - icon_size) // 2, y + Inches(0.4),
                icon_size, icon_size,
                fill_color=self._get_color("accent"),
            )
            set_shape_transparency(self.slide.shapes[-1], 0.2)
            self.add_textbox(
                f"0{i+1}",
                x + (card_w - icon_size) // 2, y + Inches(0.5),
                icon_size, icon_size,
                font_size=20, font_color=RGBColor(255, 255, 255),
                bold=True, alignment=PP_ALIGN.CENTER,
            )
            # Tiêu đề
            self.add_textbox(
                item["title"],
                x, y + Inches(1.4), card_w, Inches(0.4),
                font_size=16, font_color=self._get_color("text_primary"),
                bold=True, alignment=PP_ALIGN.CENTER,
            )
            # Mô tả
            self.add_textbox(
                item["desc"],
                x + Inches(0.2), y + Inches(1.9), card_w - Inches(0.4), Inches(1.0),
                font_size=11, font_color=self._get_color("text_secondary"),
                alignment=PP_ALIGN.CENTER,
            )

    def _gen_goal_setting(self):
        """Trang thiết lập mục tiêu"""
        self.create_slide()
        self._add_bg()
        self._add_page_title_bar("Thiết lập mục tiêu")

        goals = [
            ("Mục tiêu ngắn hạn\n(1 năm)", "Đạt chứng chỉ chuyên môn\nTích lũy kinh nghiệm dự án\nMở rộng kết nối trong ngành"),
            ("Mục tiêu trung hạn\n(3 năm)", "Trở thành chuyên gia đầu ngành\nDẫn dắt đội ngũ 5-10 người\nThu nhập nâng tầm vượt bậc"),
            ("Mục tiêu dài hạn\n(5-10 năm)", "Lãnh đạo uy tín trong ngành\nKhởi nghiệp hoặc đồng sáng lập\nĐạt tự do tài chính vững chắc"),
        ]

        card_w = Inches(2.6)
        card_h = Inches(4.5)
        gap = Inches(0.4)
        start_x = (Inches(10) - (3 * card_w + 2 * gap)) // 2

        for i, (title, desc) in enumerate(goals):
            x = start_x + i * (card_w + gap)
            y = Inches(1.5)
            self.add_shape(
                MSO_SHAPE.ROUNDED_RECTANGLE,
                x, y, card_w, card_h,
                fill_color=RGBColor(255, 255, 255),
            )
            # Khối màu trên cùng
            self.add_shape(
                MSO_SHAPE.RECTANGLE,
                x, y, card_w, Inches(1.2),
                fill_color=self._get_color("accent"),
            )
            set_shape_transparency(self.slide.shapes[-1], 0.1)
            # Số thứ tự
            self.add_textbox(
                f"0{i+1}",
                x, y + Inches(0.1), card_w, Inches(0.5),
                font_size=28, font_color=RGBColor(255, 255, 255),
                bold=True, alignment=PP_ALIGN.CENTER,
            )
            # Tiêu đề mục tiêu
            self.add_textbox(
                title,
                x, y + Inches(0.55), card_w, Inches(0.6),
                font_size=12, font_color=RGBColor(255, 255, 255),
                alignment=PP_ALIGN.CENTER,
            )
            # Mô tả
            self.add_textbox(
                desc,
                x + Inches(0.3), y + Inches(1.5), card_w - Inches(0.6), Inches(2.5),
                font_size=12, font_color=self._get_color("text_secondary"),
                alignment=PP_ALIGN.LEFT,
            )

    def _gen_skill_improvement(self, page_num=1):
        """Trang nâng cao năng lực"""
        self.create_slide()
        self._add_bg()
        self._add_page_title_bar(f"Nâng cao năng lực - Phần {page_num}")

        contents = {
            1: ("Nâng cao kỹ năng cứng", [
                {"skill": "Phân tích dữ liệu", "level": "Python / SQL / Công cụ BI"},
                {"skill": "Quản lý dự án", "level": "Chứng chỉ PMP / Phương pháp Agile"},
                {"skill": "Năng lực công nghệ", "level": "AI / Điện toán đám mây / Thiết kế kiến trúc"},
            ]),
            2: ("Nâng cao kỹ năng mềm", [
                {"skill": "Năng lực lãnh đạo", "level": "Quản lý và tạo động lực đội ngũ"},
                {"skill": "Giao tiếp diễn đạt", "level": "Thuyết trình / Soạn thảo / Đàm phán"},
                {"skill": "Tư duy đổi mới", "level": "Tư duy thiết kế / Phương pháp khởi nghiệp"},
            ]),
        }
        section_title, items = contents.get(page_num, ("Nâng cao năng lực", []))

        for i, item in enumerate(items):
            y = Inches(1.5) + i * Inches(1.8)
            # Thẻ dạng thanh ngang
            self.add_shape(
                MSO_SHAPE.ROUNDED_RECTANGLE,
                Inches(0.5), y, Inches(9.0), Inches(1.5),
                fill_color=RGBColor(255, 255, 255),
            )
            # Khối màu bên trái
            self.add_shape(
                MSO_SHAPE.RECTANGLE,
                Inches(0.5), y, Inches(0.08), Inches(1.5),
                fill_color=self._get_color("accent"),
            )
            # Tên kỹ năng
            self.add_textbox(
                item["skill"],
                Inches(0.9), y + Inches(0.2), Inches(2.5), Inches(0.4),
                font_size=16, font_color=self._get_color("text_primary"),
                bold=True, alignment=PP_ALIGN.LEFT,
            )
            # Chi tiết
            self.add_textbox(
                item["level"],
                Inches(0.9), y + Inches(0.7), Inches(3.0), Inches(0.5),
                font_size=12, font_color=self._get_color("text_secondary"),
                alignment=PP_ALIGN.LEFT,
            )
            # Nền thanh tiến độ
            bar_x = Inches(5.0)
            bar_w = Inches(4.2)
            bar_h = Inches(0.3)
            bar_y = y + Inches(0.6)
            self.add_shape(
                MSO_SHAPE.ROUNDED_RECTANGLE,
                bar_x, bar_y, bar_w, bar_h,
                fill_color=self._get_color("light"),
            )
            # Tiền cảnh thanh tiến độ
            progress = 0.5 + i * 0.15
            self.add_shape(
                MSO_SHAPE.ROUNDED_RECTANGLE,
                bar_x, bar_y, int(bar_w * progress), bar_h,
                fill_color=self._get_color("accent"),
            )

    def _gen_practice(self):
        """Trang kinh nghiệm thực tiễn"""
        self.create_slide()
        self._add_bg()
        self._add_page_title_bar("Kinh nghiệm thực tiễn")

        experiences = [
            ("06/2023 - 06/2024", "Công ty TNHH Công nghệ Example", "Thực tập sinh Quản lý Sản phẩm", "Phụ trách mô-đun tăng trưởng người dùng\nTham gia 3 đợt lặp tính năng cốt lõi"),
            ("09/2022 - 05/2023", "Dự án Khởi nghiệp Sinh viên", "Trưởng dự án", "Dẫn dắt nhóm 5 thành viên hoàn thành MVP\nĐoạt giải Nhất cuộc thi Khởi nghiệp cấp trường"),
            ("09/2021 - 06/2022", "Hội Sinh viên", "Phó Chủ tịch", "Tổ chức 10+ sự kiện quy mô lớn\nQuản lý và điều phối nhóm 30 nhân sự"),
        ]

        card_w = Inches(9.0)
        card_h = Inches(1.5)
        start_y = Inches(1.5)

        for i, (time, company, role, desc) in enumerate(experiences):
            y = start_y + i * (card_h + Inches(0.25))
            self.add_shape(
                MSO_SHAPE.ROUNDED_RECTANGLE,
                Inches(0.5), y, card_w, card_h,
                fill_color=RGBColor(255, 255, 255),
            )
            # Dải màu bên trái
            self.add_shape(
                MSO_SHAPE.RECTANGLE,
                Inches(0.5), y, Inches(0.06), card_h,
                fill_color=self._get_color("accent"),
            )
            # Thời gian
            self.add_textbox(
                time,
                Inches(0.8), y + Inches(0.2), Inches(2.5), Inches(0.3),
                font_size=11, font_color=self._get_color("accent"),
                bold=True, alignment=PP_ALIGN.LEFT,
            )
            # Đơn vị công tác
            self.add_textbox(
                company,
                Inches(0.8), y + Inches(0.5), Inches(2.5), Inches(0.3),
                font_size=14, font_color=self._get_color("text_primary"),
                bold=True, alignment=PP_ALIGN.LEFT,
            )
            # Chức vụ
            self.add_textbox(
                role,
                Inches(0.8), y + Inches(0.9), Inches(2.5), Inches(0.3),
                font_size=12, font_color=self._get_color("text_secondary"),
                alignment=PP_ALIGN.LEFT,
            )
            # Mô tả
            self.add_textbox(
                desc,
                Inches(4.0), y + Inches(0.3), Inches(5.2), Inches(1.0),
                font_size=12, font_color=self._get_color("text_secondary"),
                alignment=PP_ALIGN.LEFT,
            )

    def _gen_achievements(self):
        """Trang thành tựu nổi bật"""
        self.create_slide()
        self._add_bg()
        self._add_page_title_bar("Thành tựu nổi bật")

        achievements = [
            ("5+", "Chứng chỉ chuyên môn"),
            ("3", "Dự án khởi nghiệp"),
            ("10+", "Giải thưởng & Danh hiệu"),
            ("50+", "Mạng lưới kết nối"),
        ]

        box_w = Inches(2.0)
        box_h = Inches(2.2)
        gap = Inches(0.35)
        start_x = (Inches(10) - (4 * box_w + 3 * gap)) // 2

        for i, (value, label) in enumerate(achievements):
            x = start_x + i * (box_w + gap)
            y = Inches(1.8)
            self.add_shape(
                MSO_SHAPE.ROUNDED_RECTANGLE,
                x, y, box_w, box_h,
                fill_color=RGBColor(255, 255, 255),
            )
            # Vòng tròn trên cùng
            circle_size = Inches(0.8)
            self.add_shape(
                MSO_SHAPE.OVAL,
                x + (box_w - circle_size) // 2, y + Inches(0.3),
                circle_size, circle_size,
                fill_color=self._get_color("accent"),
            )
            self.add_textbox(
                str(i + 1),
                x + (box_w - circle_size) // 2, y + Inches(0.4),
                circle_size, circle_size,
                font_size=20, font_color=RGBColor(255, 255, 255),
                bold=True, alignment=PP_ALIGN.CENTER,
            )
            # Giá trị
            self.add_textbox(
                value,
                x, y + Inches(1.2), box_w, Inches(0.5),
                font_size=28, font_color=self._get_color("accent"),
                bold=True, alignment=PP_ALIGN.CENTER,
            )
            # Nhãn
            self.add_textbox(
                label,
                x, y + Inches(1.7), box_w, Inches(0.35),
                font_size=12, font_color=self._get_color("text_secondary"),
                alignment=PP_ALIGN.CENTER,
            )

        # Danh sách chi tiết
        details = [
            "Chứng chỉ Chuyên gia Quản lý Dự án PMP",
            "Giải Nhất Cuộc thi Đổi mới Sáng tạo & Khởi nghiệp",
            "Chứng chỉ Cao cấp Phân tích Dữ liệu Python",
            "Cán bộ Đoàn Hội xuất sắc / Học bổng Khuyến khích Tài năng",
        ]
        detail_y = Inches(4.4)
        for detail in details:
            self.add_textbox(
                f"  {detail}",
                Inches(1.0), detail_y, Inches(8.0), Inches(0.35),
                font_size=12, font_color=self._get_color("text_secondary"),
                alignment=PP_ALIGN.LEFT,
            )
            detail_y += Inches(0.4)

    def _gen_future_plan(self):
        """Trang định hướng tương lai"""
        self.create_slide()
        self._add_bg()
        self._add_page_title_bar("Định hướng tương lai")

        phases = [
            ("Ngắn hạn", "Trong 1 năm", "Đào sâu chuyên môn\nThi chứng chỉ nghề nghiệp\nTích lũy kinh nghiệm dự án"),
            ("Trung hạn", "Trong 3 năm", "Chuyển dịch sang quản lý\nTạo tầm ảnh hưởng ngành\nTích lũy nguồn lực chiến lược"),
            ("Dài hạn", "Trên 5 năm", "Khởi nghiệp / Cấp quản lý cao\nLãnh đạo uy tín trong ngành\nĐóng góp cho xã hội"),
        ]

        card_w = Inches(2.6)
        card_h = Inches(4.0)
        gap = Inches(0.4)
        start_x = (Inches(10) - (3 * card_w + 2 * gap)) // 2

        for i, (phase, period, desc) in enumerate(phases):
            x = start_x + i * (card_w + gap)
            y = Inches(1.5)
            self.add_shape(
                MSO_SHAPE.ROUNDED_RECTANGLE,
                x, y, card_w, card_h,
                fill_color=RGBColor(255, 255, 255),
            )
            # Phía trên
            self.add_shape(
                MSO_SHAPE.RECTANGLE,
                x, y, card_w, Inches(1.0),
                fill_color=self._get_color("accent"),
            )
            set_shape_transparency(self.slide.shapes[-1], 0.1)
            self.add_textbox(
                phase,
                x, y + Inches(0.1), card_w, Inches(0.4),
                font_size=20, font_color=RGBColor(255, 255, 255),
                bold=True, alignment=PP_ALIGN.CENTER,
            )
            self.add_textbox(
                period,
                x, y + Inches(0.5), card_w, Inches(0.35),
                font_size=12, font_color=RGBColor(206, 147, 216),
                alignment=PP_ALIGN.CENTER,
            )
            # Mô tả
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
        """Tạo trọn bộ 16 trang định hướng sự nghiệp"""
        self._gen_cover()           # 1. Trang bìa
        self._gen_directory()       # 2. Mục lục
        self._add_section_title("Thấu hiểu bản thân", "Self-Awareness")  # 3. Tiêu đề phân mục
        self._gen_self_analysis(1)  # 4. Thấu hiểu bản thân 1
        self._gen_self_analysis(2)  # 5. Thấu hiểu bản thân 2
        self._add_section_title("Khám phá nghề nghiệp", "Career Exploration")  # 6. Tiêu đề phân mục
        self._gen_career_exploration(1)  # 7. Khám phá nghề nghiệp 1
        self._gen_career_exploration(2)  # 8. Khám phá nghề nghiệp 2
        self._gen_goal_setting()    # 9. Thiết lập mục tiêu
        self._gen_skill_improvement(1)  # 10. Nâng cao năng lực 1
        self._gen_skill_improvement(2)  # 11. Nâng cao năng lực 2
        self._add_section_title("Thực tiễn & Thành tựu", "Practice & Achievements")  # 12. Tiêu đề phân mục
        self._gen_practice()        # 13. Kinh nghiệm thực tiễn
        self._gen_achievements()    # 14. Thành tựu nổi bật
        self._gen_future_plan()     # 15. Định hướng tương lai
        self._add_thank_you()       # 16. Lời cảm ơn
        return self


if __name__ == "__main__":
    assembler = CareerPlanningAssembler()
    assembler.set_title("Kế hoạch định hướng sự nghiệp").set_subtitle("Lộ trình phát triển sự nghiệp cá nhân")
    assembler.generate()
    output_path = os.path.join(os.path.dirname(__file__), '..', '..', 'output_career_planning.pptx')
    assembler.save(output_path)
    print(f"Đã tạo kế hoạch định hướng sự nghiệp: {output_path}")
