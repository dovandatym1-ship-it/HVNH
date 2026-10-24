"""Bộ lắp ráp bài thuyết trình Bài giảng giáo dục hoàn chỉnh

Tạo bài thuyết trình bài giảng giáo dục gồm 18 trang:
Trang bìa -> Mục lục -> Giới thiệu môn học -> Mục tiêu giảng dạy -> Kiến thức trọng tâm (6 trang) -> Phân tích tình huống (2 trang) -> Bài tập trên lớp -> Tổng kết & Ôn tập -> Lời cảm ơn

Mặc định sử dụng chủ đề Xanh thiên nhiên, bìa chuyển sắc tối giản.
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


class EducationCourseAssembler(TemplateGenerator):
    """Bộ lắp ráp bài thuyết trình Bài giảng giáo dục (18 slide)"""

    DEFAULT_THEME = {
        "primary": "#1B5E20",
        "secondary": "#2E7D32",
        "accent": "#43A047",
        "highlight": "#81C784",
        "light": "#E8F5E9",
        "bg": "#FAFAFA",
        "text_primary": "#1B5E20",
        "text_secondary": "#455A64",
        "text_light": "#FFFFFF",
    }

    def __init__(self, theme=None):
        super().__init__(theme=theme)
        self._title = "Bài giảng giáo dục"
        self._subtitle = "Education Course"
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
            - course_intro: Giới thiệu môn học
            - objectives: Mục tiêu giảng dạy
            - knowledge_points: Danh sách kiến thức trọng tâm
            - cases: Phân tích tình huống
            - exercises: Bài tập trên lớp
            - summary: Tổng kết & Ôn tập
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
            "Trân trọng cảm ơn - Chúc các bạn học tập tốt",
            Inches(1), Inches(3.5), Inches(8), Inches(0.8),
            font_size=22, font_color=RGBColor(129, 199, 132),
            alignment=PP_ALIGN.CENTER,
        )
        line_w = Inches(2)
        self.add_shape(
            MSO_SHAPE.RECTANGLE,
            (Inches(10) - line_w) // 2, Inches(3.3),
            line_w, Pt(2),
            fill_color=RGBColor(129, 199, 132),
        )

    def _add_knowledge_card(self, left, top, width, height, num, title, points):
        """Thẻ kiến thức"""
        self.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            left, top, width, height,
            fill_color=RGBColor(255, 255, 255),
        )
        # Vòng tròn số thứ tự
        circle_size = Inches(0.5)
        self.add_shape(
            MSO_SHAPE.OVAL,
            left + Inches(0.2), top + Inches(0.2),
            circle_size, circle_size,
            fill_color=self._get_color("accent"),
        )
        self.add_textbox(
            str(num),
            left + Inches(0.2), top + Inches(0.25),
            circle_size, circle_size,
            font_size=16, font_color=RGBColor(255, 255, 255),
            bold=True, alignment=PP_ALIGN.CENTER,
        )
        # Tiêu đề
        self.add_textbox(
            title,
            left + Inches(0.8), top + Inches(0.2),
            width - Inches(1.0), Inches(0.35),
            font_size=14, font_color=self._get_color("text_primary"),
            bold=True, alignment=PP_ALIGN.LEFT,
        )
        # Các điểm chính
        y_pos = top + Inches(0.7)
        for point in points[:4]:
            self.add_textbox(
                f"  {point}",
                left + Inches(0.2), y_pos,
                width - Inches(0.4), Inches(0.25),
                font_size=10, font_color=self._get_color("text_secondary"),
                alignment=PP_ALIGN.LEFT,
            )
            y_pos += Inches(0.28)

    # ------------------------------------------------------------------ #
    #  Phương thức tạo từng trang slide
    # ------------------------------------------------------------------ #

    def _gen_cover(self):
        """Trang bìa: Chuyển sắc tối giản"""
        self.create_slide()
        primary = self._get_color("primary")
        secondary = self._get_color("secondary")
        accent = self._get_color("accent")
        highlight = self._get_color("highlight")

        # Nền chuyển sắc
        self.add_gradient_shape(
            MSO_SHAPE.RECTANGLE,
            Inches(0), Inches(0), Inches(10), Inches(7.5),
            [primary, secondary], angle=45,
        )

        # Vòng tròn trang trí
        circle_size = Inches(4.5)
        self.add_shape(
            MSO_SHAPE.OVAL,
            Inches(10) - circle_size + Inches(0.5),
            Inches(-1.5),
            circle_size, circle_size,
            fill_color=accent,
        )
        set_shape_transparency(self.slide.shapes[-1], 0.85)

        circle_size2 = Inches(3.0)
        self.add_shape(
            MSO_SHAPE.OVAL,
            Inches(-1.0),
            Inches(7.5) - circle_size2 + Inches(0.5),
            circle_size2, circle_size2,
            fill_color=highlight,
        )
        set_shape_transparency(self.slide.shapes[-1], 0.88)

        # Tiêu đề
        self.add_textbox(
            self._title,
            Inches(1.5), Inches(2.6), Inches(7.0), Inches(1.2),
            font_size=44, font_color=RGBColor(255, 255, 255),
            bold=True, alignment=PP_ALIGN.CENTER,
        )
        # Đường phân cách
        line_w = Inches(2.5)
        self.add_shape(
            MSO_SHAPE.RECTANGLE,
            (Inches(10) - line_w) // 2, Inches(3.85),
            line_w, Pt(2),
            fill_color=RGBColor(129, 199, 132),
        )
        # Tiêu đề phụ
        self.add_textbox(
            self._subtitle,
            Inches(1.5), Inches(4.1), Inches(7.0), Inches(0.8),
            font_size=20, font_color=RGBColor(129, 199, 132),
            alignment=PP_ALIGN.CENTER,
        )

    def _gen_directory(self):
        self.create_slide()
        self._add_bg()
        self._add_page_title_bar("Mục lục")

        sections = [
            ("01", "Giới thiệu môn học"),
            ("02", "Mục tiêu giảng dạy"),
            ("03", "Nội dung kiến thức"),
            ("04", "Phân tích tình huống"),
            ("05", "Bài tập trên lớp"),
            ("06", "Tổng kết & Ôn tập"),
        ]
        card_w = Inches(2.6)
        card_h = Inches(1.5)
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
                font_size=14, font_color=self._get_color("text_primary"),
                bold=True, alignment=PP_ALIGN.CENTER,
            )

    def _gen_course_intro(self):
        """Trang giới thiệu môn học"""
        self.create_slide()
        self._add_bg()
        self._add_page_title_bar("Giới thiệu môn học")

        # Bên trái
        self.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            Inches(0.5), Inches(1.3), Inches(5.5), Inches(5.5),
            fill_color=RGBColor(255, 255, 255),
        )
        self.add_textbox(
            "Tổng quan học phần",
            Inches(0.8), Inches(1.5), Inches(5.0), Inches(0.4),
            font_size=18, font_color=self._get_color("text_primary"),
            bold=True, alignment=PP_ALIGN.LEFT,
        )
        intro_lines = [
            "Học phần nhằm giúp học viên nắm vững hệ thống kiến thức và kỹ năng cốt lõi.",
            "Thông qua kết hợp chặt chẽ giữa lý thuyết nền tảng và bài tập thực hành,",
            "giúp học viên tự tin vận dụng linh hoạt vào thực tiễn công việc chuyên môn.",
            "",
            "Thời lượng: 4 buổi (Tổng 180 phút)",
            "Cấp độ: Nâng cao",
            "Đối tượng: Học viên đã nắm kiến thức cơ sở",
        ]
        y = Inches(2.1)
        for line in intro_lines:
            self.add_textbox(
                line,
                Inches(0.8), y, Inches(5.0), Inches(0.3),
                font_size=12, font_color=self._get_color("text_secondary"),
                alignment=PP_ALIGN.LEFT,
            )
            y += Inches(0.35)

        # Bên phải - Cấu trúc môn học
        self.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            Inches(6.3), Inches(1.3), Inches(3.2), Inches(5.5),
            fill_color=RGBColor(255, 255, 255),
        )
        self.add_textbox(
            "Cấu trúc học phần",
            Inches(6.5), Inches(1.5), Inches(2.8), Inches(0.4),
            font_size=16, font_color=self._get_color("text_primary"),
            bold=True, alignment=PP_ALIGN.LEFT,
        )
        structure = [
            ("Buổi 1", "Khái niệm và Nguyên lý nền tảng"),
            ("Buổi 2", "Phân tích các kiến thức trọng tâm"),
            ("Buổi 3", "Phân tích tình huống & Thảo luận"),
            ("Buổi 4", "Thực hành ứng dụng & Tổng kết"),
        ]
        y = Inches(2.2)
        for time, desc in structure:
            self.add_shape(
                MSO_SHAPE.ROUNDED_RECTANGLE,
                Inches(6.5), y, Inches(2.8), Inches(0.9),
                fill_color=self._get_color("light"),
            )
            self.add_textbox(
                time,
                Inches(6.6), y + Inches(0.1), Inches(2.6), Inches(0.3),
                font_size=11, font_color=self._get_color("accent"),
                bold=True, alignment=PP_ALIGN.LEFT,
            )
            self.add_textbox(
                desc,
                Inches(6.6), y + Inches(0.45), Inches(2.6), Inches(0.3),
                font_size=10, font_color=self._get_color("text_secondary"),
                alignment=PP_ALIGN.LEFT,
            )
            y += Inches(1.1)

    def _gen_objectives(self):
        """Trang mục tiêu giảng dạy"""
        self.create_slide()
        self._add_bg()
        self._add_page_title_bar("Mục tiêu giảng dạy")

        objectives = [
            ("Mục tiêu kiến thức", [
                "Thấu hiểu sâu sắc các khái niệm cốt lõi và nguyên lý",
                "Nắm vững mối liên hệ hữu cơ giữa các khối kiến thức",
                "Cập nhật các xu hướng phát triển mới nhất trong ngành",
            ]),
            ("Mục tiêu kỹ năng", [
                "Phát triển năng lực phân tích và giải quyết vấn đề độc lập",
                "Thành thạo ứng dụng công cụ và phương pháp chuyên môn",
                "Sẵn sàng tham gia triển khai các dự án thực tế",
            ]),
            ("Mục tiêu phẩm chất", [
                "Rèn luyện năng lực tư duy phản biện sắc bén",
                "Nâng cao kỹ năng cộng tác nhóm và giao tiếp hiệu quả",
                "Xây dựng tinh thần học tập suốt đời chủ động",
            ]),
        ]

        card_w = Inches(2.6)
        card_h = Inches(4.5)
        gap = Inches(0.4)
        start_x = (Inches(10) - (3 * card_w + 2 * gap)) // 2

        for i, (title, items) in enumerate(objectives):
            x = start_x + i * (card_w + gap)
            y = Inches(1.3)
            self.add_shape(
                MSO_SHAPE.ROUNDED_RECTANGLE,
                x, y, card_w, card_h,
                fill_color=RGBColor(255, 255, 255),
            )
            # Khối màu trên cùng
            self.add_shape(
                MSO_SHAPE.RECTANGLE,
                x, y, card_w, Inches(1.0),
                fill_color=self._get_color("accent"),
            )
            set_shape_transparency(self.slide.shapes[-1], 0.1)
            self.add_textbox(
                f"0{i+1}",
                x, y + Inches(0.1), card_w, Inches(0.4),
                font_size=20, font_color=RGBColor(255, 255, 255),
                bold=True, alignment=PP_ALIGN.CENTER,
            )
            self.add_textbox(
                title,
                x, y + Inches(0.5), card_w, Inches(0.35),
                font_size=13, font_color=RGBColor(255, 255, 255),
                alignment=PP_ALIGN.CENTER,
            )
            # Danh sách
            iy = y + Inches(1.3)
            for item in items:
                self.add_textbox(
                    f"  {item}",
                    x + Inches(0.2), iy, card_w - Inches(0.4), Inches(0.35),
                    font_size=11, font_color=self._get_color("text_secondary"),
                    alignment=PP_ALIGN.LEFT,
                )
                iy += Inches(0.45)

    def _gen_knowledge_point(self, page_num=1):
        """Trang kiến thức trọng tâm"""
        self.create_slide()
        self._add_bg()
        self._add_page_title_bar(f"Kiến thức trọng tâm - Phần {page_num}")

        knowledge_data = {
            1: ("Khái niệm cốt lõi", [
                {"title": "Định nghĩa cơ bản", "points": ["Xác định rõ phạm vi khái niệm", "Phân biệt các khái niệm tương đồng", "Thấu hiểu bối cảnh áp dụng"]},
                {"title": "Cơ sở lý thuyết", "points": ["Điểm lại lý thuyết kinh điển", "Sự phát triển thời hiện đại", "Các giả định then chốt"]},
            ]),
            2: ("Nguyên lý chủ chốt", [
                {"title": "Nguyên lý I", "points": ["Chuỗi logic cốt lõi", "Quy trình suy luận chặt chẽ", "Phương pháp tiếp cận trực quan"]},
                {"title": "Nguyên lý II", "points": ["Tình huống ứng dụng thực tế", "Phân tích điều kiện biên", "Các sai lầm phổ biến cần tránh"]},
            ]),
            3: ("Phương pháp luận", [
                {"title": "Khung phân tích", "points": ["Phương pháp tư duy hệ thống", "Chiến lược phân loại phân tầng", "Kỹ năng sắp xếp mức ưu tiên"]},
                {"title": "Khai thác công cụ", "points": ["Giới thiệu bộ công cụ phổ biến", "Hướng dẫn thao tác từng bước", "Kinh nghiệm thực tiễn tốt nhất"]},
            ]),
            4: ("Kỹ năng thực hành", [
                {"title": "Vấn đề thường gặp", "points": ["Top 10 sự cố tần suất cao", "Biểu mẫu giải pháp chuẩn", "Cẩm nang phòng ngừa rủi ro"]},
                {"title": "Tối ưu hiệu suất", "points": ["Mẹo thao tác nhanh", "Giải pháp tự động hóa", "Quy trình làm việc phối hợp"]},
            ]),
            5: ("Nội dung nâng cao", [
                {"title": "Phân tích chuyên sâu", "points": ["Phương pháp phân tích nâng cao", "Quyết định dựa trên dữ liệu", "Kỹ năng xây dựng mô hình"]},
                {"title": "Ứng dụng liên ngành", "points": ["Nghiên cứu điển hình đa ngành", "Giải pháp tùy biến linh hoạt", "Phương pháp dự báo xu hướng"]},
            ]),
            6: ("Xu hướng tiên phong", [
                {"title": "Xu hướng công nghệ", "points": ["Tiến bộ công nghệ mới nhất", "AI và tự động hóa quy trình", "Định hướng chuyển đổi ngành"]},
                {"title": "Bài học thực tiễn", "points": ["Kinh nghiệm từ doanh nghiệp dẫn đầu", "Tình huống đổi mới sáng tạo", "Tầm nhìn phát triển tương lai"]},
            ]),
        }

        section_title, items = knowledge_data.get(page_num, ("Kiến thức trọng tâm", []))

        for i, item in enumerate(items):
            x = Inches(0.5) if i == 0 else Inches(5.0)
            self._add_knowledge_card(
                x, Inches(1.3), Inches(4.5), Inches(5.5),
                (page_num - 1) * 2 + i + 1, item["title"], item["points"]
            )

    def _gen_case_study(self, page_num=1):
        """Trang phân tích tình huống"""
        self.create_slide()
        self._add_bg()
        self._add_page_title_bar(f"Phân tích tình huống - Phần {page_num}")

        cases = {
            1: {
                "title": "Tình huống 1: Chuyển đổi số doanh nghiệp",
                "background": "Doanh nghiệp sản xuất truyền thống đối mặt với hiệu suất thấp và dữ liệu phân mảnh",
                "approach": "Áp dụng chiến lược chuyển đổi số phân kỳ, chuẩn hóa quy trình cốt lõi trước",
                "result": "Năng suất tăng 35%, chi phí vận hành giảm 20%",
                "lessons": ["Sự cam kết của lãnh đạo là then chốt", "Chiến lược từ dễ đến khó", "Quản trị dữ liệu là nền móng"],
            },
            2: {
                "title": "Tình huống 2: Tăng trưởng sản phẩm công nghệ",
                "background": "Sản phẩm mới ra mắt có tốc độ tăng trưởng người dùng chậm, tỷ lệ giữ chân thấp",
                "approach": "Tối ưu hóa hành trình người dùng qua thử nghiệm A/B, cá nhân hóa trải nghiệm",
                "result": "Lượng người dùng hoạt động hàng tháng tăng 200%, tỷ lệ giữ chân ngày 2 tăng 15%",
                "lessons": ["Quyết định dựa trên dữ liệu", "Lặp nhanh để kiểm chứng", "Khép kín vòng phản hồi người dùng"],
            },
        }

        case = cases.get(page_num, cases[1])

        # Tiêu đề tình huống
        self.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            Inches(0.5), Inches(1.3), Inches(9.0), Inches(0.6),
            fill_color=self._get_color("accent"),
        )
        set_shape_transparency(self.slide.shapes[-1], 0.1)
        self.add_textbox(
            case["title"],
            Inches(0.8), Inches(1.35), Inches(8.4), Inches(0.5),
            font_size=16, font_color=RGBColor(255, 255, 255),
            bold=True, alignment=PP_ALIGN.LEFT,
        )

        sections = [
            ("Bối cảnh", case["background"]),
            ("Phương pháp", case["approach"]),
            ("Kết quả", case["result"]),
        ]

        y = Inches(2.1)
        for label, content in sections:
            self.add_shape(
                MSO_SHAPE.ROUNDED_RECTANGLE,
                Inches(0.5), y, Inches(9.0), Inches(1.0),
                fill_color=RGBColor(255, 255, 255),
            )
            # Nhãn
            self.add_shape(
                MSO_SHAPE.ROUNDED_RECTANGLE,
                Inches(0.7), y + Inches(0.2), Inches(0.8), Inches(0.35),
                fill_color=self._get_color("light"),
            )
            self.add_textbox(
                label,
                Inches(0.7), y + Inches(0.2), Inches(0.8), Inches(0.35),
                font_size=10, font_color=self._get_color("accent"),
                bold=True, alignment=PP_ALIGN.CENTER,
            )
            self.add_textbox(
                content,
                Inches(1.7), y + Inches(0.25), Inches(7.6), Inches(0.5),
                font_size=12, font_color=self._get_color("text_secondary"),
                alignment=PP_ALIGN.LEFT,
            )
            y += Inches(1.15)

        # Bài học kinh nghiệm
        self.add_textbox(
            "Bài học kinh nghiệm & Suy ngẫm",
            Inches(0.7), Inches(5.6), Inches(8.4), Inches(0.35),
            font_size=14, font_color=self._get_color("text_primary"),
            bold=True, alignment=PP_ALIGN.LEFT,
        )
        lesson_text = " | ".join(case["lessons"])
        self.add_textbox(
            lesson_text,
            Inches(0.7), Inches(6.0), Inches(8.4), Inches(0.5),
            font_size=11, font_color=self._get_color("text_secondary"),
            alignment=PP_ALIGN.LEFT,
        )

    def _gen_exercise(self):
        """Trang bài tập trên lớp"""
        self.create_slide()
        self._add_bg()
        self._add_page_title_bar("Bài tập trên lớp")

        exercises = [
            {"num": "1", "question": "Dựa trên nội dung bài học, hãy vẽ sơ đồ tư duy cho các khái niệm cốt lõi.",
             "hint": "Gợi ý: Bắt đầu từ khái niệm trung tâm, mở rộng ít nhất 3 nhánh con"},
            {"num": "2", "question": "Phân tích tình huống sau và vận dụng phương pháp đã học để đề xuất giải pháp.",
             "hint": "Gợi ý: Kết hợp các khung phân tích trong bài học"},
            {"num": "3", "question": "Thảo luận nhóm: Làm thế nào để áp dụng kiến thức bài học vào thực tế công việc?",
             "hint": "Gợi ý: Mỗi nhóm thảo luận 15 phút, đại diện trình bày 5 phút"},
        ]

        card_w = Inches(9.0)
        card_h = Inches(1.6)
        start_y = Inches(1.3)

        for i, ex in enumerate(exercises):
            y = start_y + i * (card_h + Inches(0.25))
            self.add_shape(
                MSO_SHAPE.ROUNDED_RECTANGLE,
                Inches(0.5), y, card_w, card_h,
                fill_color=RGBColor(255, 255, 255),
            )
            # Số thứ tự
            circle_size = Inches(0.5)
            self.add_shape(
                MSO_SHAPE.OVAL,
                Inches(0.7), y + Inches(0.3),
                circle_size, circle_size,
                fill_color=self._get_color("accent"),
            )
            self.add_textbox(
                ex["num"],
                Inches(0.7), y + Inches(0.35),
                circle_size, circle_size,
                font_size=16, font_color=RGBColor(255, 255, 255),
                bold=True, alignment=PP_ALIGN.CENTER,
            )
            # Đề bài
            self.add_textbox(
                ex["question"],
                Inches(1.4), y + Inches(0.3), Inches(7.8), Inches(0.5),
                font_size=14, font_color=self._get_color("text_primary"),
                bold=True, alignment=PP_ALIGN.LEFT,
            )
            # Gợi ý
            self.add_textbox(
                ex["hint"],
                Inches(1.4), y + Inches(0.9), Inches(7.8), Inches(0.4),
                font_size=11, font_color=self._get_color("text_secondary"),
                alignment=PP_ALIGN.LEFT,
            )

        # Lưu ý quan trọng
        self.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            Inches(0.5), Inches(6.5), Inches(9.0), Inches(0.7),
            fill_color=self._get_color("light"),
        )
        self.add_textbox(
            "Lưu ý: Học viên làm vào vở bài tập, sau đó trao đổi cùng bạn bên cạnh. Giảng viên sẽ nhận xét và giải đáp.",
            Inches(0.8), Inches(6.6), Inches(8.4), Inches(0.4),
            font_size=11, font_color=self._get_color("text_primary"),
            alignment=PP_ALIGN.LEFT,
        )

    def _gen_summary(self):
        """Trang tổng kết & ôn tập"""
        self.create_slide()
        self._add_bg()
        self._add_page_title_bar("Tổng kết & Ôn tập")

        summary_items = [
            ("Khái niệm cốt lõi", "Nắm vững định nghĩa cơ bản và nền tảng lý thuyết\nThấu hiểu mối liên hệ hữu cơ giữa các khái niệm"),
            ("Phương pháp & Công cụ", "Làm chủ các khung phân tích và phương pháp luận\nThành thạo kỹ năng sử dụng công cụ phổ biến"),
            ("Thực hành ứng dụng", "Hiểu sâu sắc hơn thông qua phân tích tình huống\nĐặt nền tảng vững chắc cho công việc thực tế"),
        ]

        card_w = Inches(2.6)
        card_h = Inches(3.5)
        gap = Inches(0.4)
        start_x = (Inches(10) - (3 * card_w + 2 * gap)) // 2

        for i, (title, desc) in enumerate(summary_items):
            x = start_x + i * (card_w + gap)
            y = Inches(1.3)
            self.add_shape(
                MSO_SHAPE.ROUNDED_RECTANGLE,
                x, y, card_w, card_h,
                fill_color=RGBColor(255, 255, 255),
            )
            # Vòng tròn biểu tượng
            icon_size = Inches(0.7)
            self.add_shape(
                MSO_SHAPE.OVAL,
                x + (card_w - icon_size) // 2, y + Inches(0.3),
                icon_size, icon_size,
                fill_color=self._get_color("accent"),
            )
            self.add_textbox(
                str(i + 1),
                x + (card_w - icon_size) // 2, y + Inches(0.38),
                icon_size, icon_size,
                font_size=20, font_color=RGBColor(255, 255, 255),
                bold=True, alignment=PP_ALIGN.CENTER,
            )
            self.add_textbox(
                title,
                x, y + Inches(1.2), card_w, Inches(0.4),
                font_size=16, font_color=self._get_color("text_primary"),
                bold=True, alignment=PP_ALIGN.CENTER,
            )
            self.add_textbox(
                desc,
                x + Inches(0.2), y + Inches(1.8), card_w - Inches(0.4), Inches(1.5),
                font_size=11, font_color=self._get_color("text_secondary"),
                alignment=PP_ALIGN.CENTER,
            )

        # Nhiệm vụ sau buổi học
        self.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            Inches(0.5), Inches(5.2), Inches(9.0), Inches(1.8),
            fill_color=RGBColor(255, 255, 255),
        )
        self.add_textbox(
            "Nhiệm vụ sau buổi học",
            Inches(0.8), Inches(5.3), Inches(8.4), Inches(0.4),
            font_size=16, font_color=self._get_color("text_primary"),
            bold=True, alignment=PP_ALIGN.LEFT,
        )
        tasks = [
            "1. Ôn tập toàn bộ kiến thức bài học và hệ thống lại ghi chép cá nhân",
            "2. Hoàn thành đầy đủ bài tập về nhà (Sách giáo trình trang 45-48)",
            "3. Chuẩn bị trước bài học tiếp theo: Ứng dụng nâng cao và thực chiến chuyên sâu",
        ]
        ty = Inches(5.8)
        for task in tasks:
            self.add_textbox(
                task,
                Inches(0.8), ty, Inches(8.4), Inches(0.3),
                font_size=12, font_color=self._get_color("text_secondary"),
                alignment=PP_ALIGN.LEFT,
            )
            ty += Inches(0.35)

    # ------------------------------------------------------------------ #
    #  Phương thức tạo chính
    # ------------------------------------------------------------------ #

    def generate(self):
        """Tạo trọn bộ 18 trang bài giảng giáo dục"""
        self._gen_cover()              # 1. Trang bìa
        self._gen_directory()          # 2. Mục lục
        self._add_section_title("Giới thiệu môn học", "Course Introduction")  # 3. Tiêu đề phân mục
        self._gen_course_intro()       # 4. Giới thiệu môn học
        self._gen_objectives()         # 5. Mục tiêu giảng dạy
        self._add_section_title("Nội dung kiến thức", "Knowledge Points")  # 6. Tiêu đề phân mục
        self._gen_knowledge_point(1)   # 7. Kiến thức trọng tâm 1
        self._gen_knowledge_point(2)   # 8. Kiến thức trọng tâm 2
        self._gen_knowledge_point(3)   # 9. Kiến thức trọng tâm 3
        self._gen_knowledge_point(4)   # 10. Kiến thức trọng tâm 4
        self._gen_knowledge_point(5)   # 11. Kiến thức trọng tâm 5
        self._gen_knowledge_point(6)   # 12. Kiến thức trọng tâm 6
        self._add_section_title("Tình huống & Luyện tập", "Cases & Practice")  # 13. Tiêu đề phân mục
        self._gen_case_study(1)        # 14. Phân tích tình huống 1
        self._gen_case_study(2)        # 15. Phân tích tình huống 2
        self._gen_exercise()           # 16. Bài tập trên lớp
        self._gen_summary()            # 17. Tổng kết & Ôn tập
        self._add_thank_you()          # 18. Lời cảm ơn
        return self


if __name__ == "__main__":
    assembler = EducationCourseAssembler()
    assembler.set_title("Bài giảng giáo dục").set_subtitle("Khóa học Thực chiến Chuyển đổi số")
    assembler.generate()
    output_path = os.path.join(os.path.dirname(__file__), '..', '..', 'output_education_course.pptx')
    assembler.save(output_path)
    print(f"Đã tạo bài giảng giáo dục: {output_path}")
