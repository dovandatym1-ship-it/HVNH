"""Bộ lắp ráp bài thuyết trình Ra mắt sản phẩm hoàn chỉnh

Tạo bài thuyết trình ra mắt sản phẩm gồm 20 trang:
Trang bìa -> Mục lục -> Phân tích bài toán -> Giải pháp đột phá -> Tính năng sản phẩm (4 trang) -> Trình diễn sản phẩm -> Khách hàng tiêu biểu (2 trang) -> Bảng giá dịch vụ -> So sánh đối thủ -> Kế hoạch ra mắt -> Lời cảm ơn

Mặc định sử dụng chủ đề Xanh đại dương, bìa phong cách hé lộ hình thoi.
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


class ProductLaunchAssembler(TemplateGenerator):
    """Bộ lắp ráp bài thuyết trình Ra mắt sản phẩm (20 slide)"""

    DEFAULT_THEME = {
        "primary": "#0D47A1",
        "secondary": "#1565C0",
        "accent": "#2196F3",
        "highlight": "#64B5F6",
        "light": "#BBDEFB",
        "bg": "#F0F7FF",
        "text_primary": "#0D47A1",
        "text_secondary": "#455A64",
        "text_light": "#FFFFFF",
    }

    def __init__(self, theme=None):
        super().__init__(theme=theme)
        self._title = "Lễ ra mắt sản phẩm"
        self._subtitle = "Product Launch"
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
            - pain_points: Danh sách bài toán thực tế
            - solution: Giải pháp đột phá
            - features: Danh sách tính năng sản phẩm
            - demo_url: Liên kết trải nghiệm thử nghiệm
            - cases: Khách hàng tiêu biểu
            - pricing: Bảng giá dịch vụ
            - competitors: Thông tin so sánh đối thủ
            - launch_plan: Kế hoạch ra mắt
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
            "Sản phẩm hoàn toàn mới, sắp chính thức ra mắt",
            Inches(1), Inches(3.5), Inches(8), Inches(0.6),
            font_size=22, font_color=RGBColor(187, 222, 251),
            alignment=PP_ALIGN.CENTER,
        )
        line_w = Inches(2)
        self.add_shape(
            MSO_SHAPE.RECTANGLE,
            (Inches(10) - line_w) // 2, Inches(3.25),
            line_w, Pt(2),
            fill_color=RGBColor(187, 222, 251),
        )
        self.add_textbox(
            "Kính mời đón chờ",
            Inches(1), Inches(4.2), Inches(8), Inches(0.5),
            font_size=16, font_color=RGBColor(100, 181, 246),
            alignment=PP_ALIGN.CENTER,
        )

    def _add_feature_card(self, left, top, width, height, icon_num, title, desc):
        self.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            left, top, width, height,
            fill_color=RGBColor(255, 255, 255),
        )
        # Biểu tượng
        icon_size = Inches(0.7)
        self.add_shape(
            MSO_SHAPE.OVAL,
            left + Inches(0.2), top + Inches(0.2),
            icon_size, icon_size,
            fill_color=self._get_color("accent"),
        )
        self.add_textbox(
            str(icon_num),
            left + Inches(0.2), top + Inches(0.28),
            icon_size, icon_size,
            font_size=18, font_color=RGBColor(255, 255, 255),
            bold=True, alignment=PP_ALIGN.CENTER,
        )
        self.add_textbox(
            title,
            left + Inches(1.0), top + Inches(0.2),
            width - Inches(1.2), Inches(0.35),
            font_size=14, font_color=self._get_color("text_primary"),
            bold=True, alignment=PP_ALIGN.LEFT,
        )
        self.add_textbox(
            desc,
            left + Inches(1.0), top + Inches(0.6),
            width - Inches(1.2), height - Inches(0.8),
            font_size=11, font_color=self._get_color("text_secondary"),
            alignment=PP_ALIGN.LEFT,
        )

    # ------------------------------------------------------------------ #
    #  Phương thức tạo từng trang slide
    # ------------------------------------------------------------------ #

    def _gen_cover(self):
        """Trang bìa: Phong cách hé lộ hình thoi"""
        self.create_slide()
        primary = self._get_color("primary")
        secondary = self._get_color("secondary")
        accent = self._get_color("accent")
        highlight = self._get_color("highlight")
        light = self._get_color("light")

        # Nền
        self.add_gradient_shape(
            MSO_SHAPE.RECTANGLE,
            Inches(0), Inches(0), Inches(10), Inches(7.5),
            [primary, secondary], angle=120,
        )

        # Họa tiết hình thoi trang trí
        diamonds = [
            (Inches(0.5), Inches(0.3), Inches(2.5), Inches(2.5), 15, accent),
            (Inches(6.5), Inches(0.5), Inches(2.0), Inches(2.0), 0, highlight),
            (Inches(7.0), Inches(4.5), Inches(2.8), Inches(2.8), -10, light),
            (Inches(0.8), Inches(5.0), Inches(1.8), Inches(1.8), 30, accent),
            (Inches(4.0), Inches(5.5), Inches(1.5), Inches(1.5), 45, highlight),
        ]
        for left, top, w, h, rot, color in diamonds:
            shape = self.add_shape(
                MSO_SHAPE.DIAMOND, left, top, w, h,
                fill_color=color,
            )
            set_shape_transparency(shape, 0.55)
            if rot != 0:
                from lxml import etree
                xfrm = shape._element.find('.//{http://schemas.openxmlformats.org/drawingml/2006/main}xfrm')
                if xfrm is not None:
                    xfrm.set('rot', str(int(rot * 60000)))

        # Mặt nạ chữ nhật trung tâm
        mask_w = Inches(6.0)
        mask_h = Inches(2.8)
        self.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            (Inches(10) - mask_w) // 2, (Inches(7.5) - mask_h) // 2,
            mask_w, mask_h,
            fill_color=RGBColor(0, 0, 0),
        )
        set_shape_transparency(self.slide.shapes[-1], 0.4)
        self.slide.shapes[-1].line.fill.background()

        # Tiêu đề
        self.add_textbox(
            self._title,
            Inches(2), Inches(2.5), Inches(6), Inches(1.2),
            font_size=44, font_color=RGBColor(255, 255, 255),
            bold=True, alignment=PP_ALIGN.CENTER,
        )
        # Đường phân cách
        line_w = Inches(2.5)
        self.add_shape(
            MSO_SHAPE.RECTANGLE,
            (Inches(10) - line_w) // 2, Inches(3.75),
            line_w, Pt(2),
            fill_color=RGBColor(187, 222, 251),
        )
        # Tiêu đề phụ
        self.add_textbox(
            self._subtitle,
            Inches(2), Inches(4.0), Inches(6), Inches(0.8),
            font_size=20, font_color=RGBColor(187, 222, 251),
            alignment=PP_ALIGN.CENTER,
        )

    def _gen_directory(self):
        self.create_slide()
        self._add_bg()
        self._add_page_title_bar("Mục lục")

        sections = [
            ("01", "Phân tích bài toán"),
            ("02", "Giải pháp đột phá"),
            ("03", "Tính năng sản phẩm"),
            ("04", "Trình diễn sản phẩm"),
            ("05", "Khách hàng tiêu biểu"),
            ("06", "Bảng giá dịch vụ"),
            ("07", "So sánh đối thủ"),
            ("08", "Kế hoạch ra mắt"),
        ]
        card_w = Inches(2.0)
        card_h = Inches(1.35)
        gap = Inches(0.3)
        cols = 4
        start_x = (Inches(10) - (cols * card_w + (cols - 1) * gap)) // 2
        start_y = Inches(1.5)

        for i, (num, title) in enumerate(sections):
            row, col = divmod(i, cols)
            x = start_x + col * (card_w + gap)
            y = start_y + row * (card_h + gap)
            # Thẻ
            self.add_shape(
                MSO_SHAPE.ROUNDED_RECTANGLE,
                x, y, card_w, card_h,
                fill_color=RGBColor(255, 255, 255),
            )
            self.add_shape(
                MSO_SHAPE.RECTANGLE,
                x, y, card_w, Inches(0.05),
                fill_color=self._get_color("accent"),
            )
            self.add_textbox(
                num,
                x, y + Inches(0.2), card_w, Inches(0.4),
                font_size=22, font_color=self._get_color("accent"),
                bold=True, alignment=PP_ALIGN.CENTER,
            )
            self.add_textbox(
                title,
                x, y + Inches(0.7), card_w, Inches(0.35),
                font_size=13, font_color=self._get_color("text_primary"),
                bold=True, alignment=PP_ALIGN.CENTER,
            )

    def _gen_pain_points(self):
        """Trang phân tích bài toán"""
        self.create_slide()
        self._add_bg()
        self._add_page_title_bar("Phân tích bài toán")

        pain_points = [
            ("Hiệu suất thấp", "Quy trình làm việc truyền thống rườm rà\nThao tác thủ công lặp lại tốn thời gian"),
            ("Chi phí đắt đỏ", "Chi phí nhân sự liên tục gia tăng\nChi phí vận hành IT duy trì ở mức cao"),
            ("Dữ liệu phân mảnh", "Dữ liệu các phòng ban không liên thông\nRa quyết định thiếu góc nhìn toàn cục"),
            ("Trải nghiệm kém", "Giao diện phức tạp khó sử dụng\nChi phí học tập làm quen quá cao"),
        ]

        card_w = Inches(4.2)
        card_h = Inches(2.4)
        gap_x = Inches(0.4)
        gap_y = Inches(0.3)
        start_x = (Inches(10) - (2 * card_w + gap_x)) // 2
        start_y = Inches(1.5)

        for i, (title, desc) in enumerate(pain_points):
            row, col = divmod(i, 2)
            x = start_x + col * (card_w + gap_x)
            y = start_y + row * (card_h + gap_y)
            self.add_shape(
                MSO_SHAPE.ROUNDED_RECTANGLE,
                x, y, card_w, card_h,
                fill_color=RGBColor(255, 255, 255),
            )
            # Dải màu đỏ bên trái
            self.add_shape(
                MSO_SHAPE.RECTANGLE,
                x, y, Inches(0.06), card_h,
                fill_color=RGBColor(244, 67, 54),
            )
            # Biểu tượng cảnh báo
            icon_size = Inches(0.6)
            self.add_shape(
                MSO_SHAPE.OVAL,
                x + Inches(0.3), y + Inches(0.3),
                icon_size, icon_size,
                fill_color=RGBColor(244, 67, 54),
            )
            set_shape_transparency(self.slide.shapes[-1], 0.15)
            self.add_textbox(
                "!",
                x + Inches(0.3), y + Inches(0.35),
                icon_size, icon_size,
                font_size=20, font_color=RGBColor(255, 255, 255),
                bold=True, alignment=PP_ALIGN.CENTER,
            )
            # Tiêu đề
            self.add_textbox(
                title,
                x + Inches(1.0), y + Inches(0.3),
                card_w - Inches(1.2), Inches(0.35),
                font_size=16, font_color=RGBColor(244, 67, 54),
                bold=True, alignment=PP_ALIGN.LEFT,
            )
            # Mô tả
            self.add_textbox(
                desc,
                x + Inches(0.3), y + Inches(1.1),
                card_w - Inches(0.6), Inches(1.0),
                font_size=12, font_color=self._get_color("text_secondary"),
                alignment=PP_ALIGN.LEFT,
            )

    def _gen_solution(self):
        """Trang giải pháp đột phá"""
        self.create_slide()
        self._add_bg()
        self._add_page_title_bar("Giải pháp đột phá")

        solutions = [
            ("Động cơ AI thông minh", "Phân tích và ra quyết định\ndựa trên học sâu"),
            ("Nền tảng hợp nhất", "Xóa bỏ rào cản dữ liệu\nCổng quản trị tập trung"),
            ("Thiết kế tối giản", "Làm quen nhanh chóng\nTrải nghiệm trực quan"),
        ]

        card_w = Inches(2.6)
        card_h = Inches(4.2)
        gap = Inches(0.4)
        start_x = (Inches(10) - (3 * card_w + 2 * gap)) // 2

        for i, (title, desc) in enumerate(solutions):
            x = start_x + i * (card_w + gap)
            y = Inches(1.4)
            self.add_shape(
                MSO_SHAPE.ROUNDED_RECTANGLE,
                x, y, card_w, card_h,
                fill_color=RGBColor(255, 255, 255),
            )
            # Đỉnh chuyển sắc
            self.add_gradient_shape(
                MSO_SHAPE.RECTANGLE,
                x, y, card_w, Inches(1.2),
                [self._get_color("primary"), self._get_color("accent")],
                angle=90,
            )
            # Số thứ tự
            self.add_textbox(
                f"0{i+1}",
                x, y + Inches(0.15), card_w, Inches(0.5),
                font_size=28, font_color=RGBColor(255, 255, 255),
                bold=True, alignment=PP_ALIGN.CENTER,
            )
            # Tiêu đề
            self.add_textbox(
                title,
                x, y + Inches(1.5), card_w, Inches(0.5),
                font_size=16, font_color=self._get_color("text_primary"),
                bold=True, alignment=PP_ALIGN.CENTER,
            )
            # Mô tả
            self.add_textbox(
                desc,
                x + Inches(0.3), y + Inches(2.2), card_w - Inches(0.6), Inches(1.5),
                font_size=12, font_color=self._get_color("text_secondary"),
                alignment=PP_ALIGN.CENTER,
            )

    def _gen_product_feature(self, page_num=1):
        """Trang tính năng sản phẩm"""
        self.create_slide()
        self._add_bg()
        self._add_page_title_bar(f"Tính năng sản phẩm - Phần {page_num}")

        features = {
            1: [
                {"icon": "1", "title": "Phân tích dữ liệu thông minh", "desc": "Tạo báo cáo trực quan trong 1 chạm\nAI tự động phát hiện hiểu biết sâu\nHỗ trợ bảng điều khiển tùy biến"},
                {"icon": "2", "title": "Luồng công việc tự động", "desc": "Kéo thả thiết kế quy trình dễ dàng\nHỗ trợ 500+ quy tắc tự động hóa\nĐồng bộ dữ liệu liên hệ thống"},
            ],
            2: [
                {"icon": "3", "title": "Trung tâm cộng tác nhóm", "desc": "Cộng tác thời gian thực nhiều người\nQuy trình bình luận & phê duyệt chuẩn\nPhân công và theo dõi tiến độ"},
                {"icon": "4", "title": "Bảo mật & Tuân thủ", "desc": "Mã hóa dữ liệu cấp doanh nghiệp\nPhân quyền chi tiết nhiều cấp\nBảo đảm tuân thủ chuẩn quốc tế"},
            ],
            3: [
                {"icon": "5", "title": "Nền tảng API mở", "desc": "Giao diện lập trình RESTful API\nThông báo sự kiện qua Webhook\nTài liệu thân thiện lập trình viên"},
                {"icon": "6", "title": "Trải nghiệm trên di động", "desc": "Ứng dụng gốc iOS/Android mượt mà\nĐồng bộ dữ liệu ngoại tuyến tức thời\nThông báo đẩy theo thời gian thực"},
            ],
            4: [
                {"icon": "7", "title": "Gợi ý thông minh", "desc": "Cá nhân hóa nội dung khuyến nghị\nDự đoán hành vi người dùng\nHỗ trợ kiểm thử A/B Testing"},
                {"icon": "8", "title": "Hỗ trợ đa ngôn ngữ", "desc": "Hỗ trợ hơn 12 ngôn ngữ phổ biến\nTùy biến bản địa hóa tối ưu\nTương thích văn hóa người dùng"},
            ],
        }

        items = features.get(page_num, features[1])
        card_w = Inches(4.2)
        card_h = Inches(3.5)
        gap = Inches(0.5)
        start_x = (Inches(10) - (2 * card_w + gap)) // 2

        for i, item in enumerate(items):
            x = start_x + i * (card_w + gap)
            y = Inches(1.5)
            self._add_feature_card(x, y, card_w, card_h,
                                   item["icon"], item["title"], item["desc"])

    def _gen_demo(self):
        """Trang trình diễn sản phẩm"""
        self.create_slide()
        self._add_bg()
        self._add_page_title_bar("Trình diễn sản phẩm")

        # Khung mô phỏng màn hình
        screen_w = Inches(8.0)
        screen_h = Inches(4.5)
        screen_x = (Inches(10) - screen_w) // 2
        screen_y = Inches(1.5)

        # Viền màn hình
        self.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            screen_x - Inches(0.1), screen_y - Inches(0.1),
            screen_w + Inches(0.2), screen_h + Inches(0.2),
            fill_color=RGBColor(33, 33, 33),
        )
        # Khu vực nội dung màn hình
        self.add_shape(
            MSO_SHAPE.RECTANGLE,
            screen_x, screen_y, screen_w, screen_h,
            fill_color=RGBColor(240, 247, 255),
        )
        # Thanh công cụ trên cùng
        self.add_shape(
            MSO_SHAPE.RECTANGLE,
            screen_x, screen_y, screen_w, Inches(0.4),
            fill_color=self._get_color("primary"),
        )
        # Chấm tròn trang trí
        for j, color in enumerate([RGBColor(255, 95, 87), RGBColor(255, 189, 46), RGBColor(39, 201, 63)]):
            self.add_shape(
                MSO_SHAPE.OVAL,
                screen_x + Inches(0.2 + j * 0.3), screen_y + Inches(0.08),
                Inches(0.2), Inches(0.2),
                fill_color=color,
            )

        # Khu vực nội dung mô phỏng
        sidebar_w = Inches(1.5)
        self.add_shape(
            MSO_SHAPE.RECTANGLE,
            screen_x, screen_y + Inches(0.4), sidebar_w, screen_h - Inches(0.4),
            fill_color=self._get_color("primary"),
        )
        set_shape_transparency(self.slide.shapes[-1], 0.15)

        # Tiêu đề khu vực nội dung chính
        self.add_textbox(
            "Giao diện trình diễn sản phẩm",
            screen_x + sidebar_w + Inches(0.3), screen_y + Inches(0.6),
            Inches(5.0), Inches(0.4),
            font_size=16, font_color=self._get_color("text_primary"),
            bold=True, alignment=PP_ALIGN.LEFT,
        )
        # Khu vực biểu đồ mô phỏng
        self.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            screen_x + sidebar_w + Inches(0.3), screen_y + Inches(1.2),
            Inches(3.5), Inches(2.0),
            fill_color=RGBColor(255, 255, 255),
        )
        self.add_textbox(
            "Khu vực trực quan hóa dữ liệu",
            screen_x + sidebar_w + Inches(0.3), screen_y + Inches(1.8),
            Inches(3.5), Inches(0.5),
            font_size=12, font_color=self._get_color("text_secondary"),
            alignment=PP_ALIGN.CENTER,
        )

        # Bảng điều khiển bên phải
        self.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            screen_x + sidebar_w + Inches(4.2), screen_y + Inches(0.6),
            Inches(2.0), Inches(3.3),
            fill_color=RGBColor(255, 255, 255),
        )

        # Ghi chú phía dưới
        self.add_textbox(
            "Xử lý dữ liệu thời gian thực | Phân tích thông minh | Xuất báo cáo 1 chạm",
            Inches(1), Inches(6.3), Inches(8), Inches(0.4),
            font_size=13, font_color=self._get_color("text_secondary"),
            alignment=PP_ALIGN.CENTER,
        )

    def _gen_user_case(self, page_num=1):
        """Trang khách hàng tiêu biểu"""
        self.create_slide()
        self._add_bg()
        self._add_page_title_bar(f"Khách hàng tiêu biểu - Phần {page_num}")

        cases = {
            1: [
                {"company": "Tập đoàn Sản xuất Quy mô lớn", "industry": "Sản xuất",
                 "result": "Hiệu suất tăng 40%", "desc": "Ứng dụng luồng công việc tự động, rút ngắn thời gian lập lịch sản xuất từ 3 ngày xuống 4 giờ"},
                {"company": "Công ty Công nghệ Internet", "industry": "Internet",
                 "result": "Chi phí giảm 30%", "desc": "Hợp nhất nền tảng dữ liệu, xóa bỏ trùng lặp xử lý, tiết kiệm đáng kể chi phí nhân lực"},
            ],
            2: [
                {"company": "Tổ chức Tài chính Ngân hàng", "industry": "Tài chính",
                 "result": "Ra quyết định nhanh hơn 50%", "desc": "AI phân tích dữ liệu tức thời hỗ trợ ban điều hành đưa ra quyết định đầu tư chính xác"},
                {"company": "Tập đoàn Bán lẻ Chuỗi", "industry": "Bán lẻ",
                 "result": "Doanh thu tăng 25%", "desc": "Chân dung khách hàng chuẩn xác kết hợp gợi ý cá nhân hóa, nâng cao tỷ lệ chuyển đổi"},
            ],
        }

        items = cases.get(page_num, cases[1])
        card_w = Inches(8.5)
        card_h = Inches(2.2)
        start_y = Inches(1.5)

        for i, case in enumerate(items):
            y = start_y + i * (card_h + Inches(0.4))
            self.add_shape(
                MSO_SHAPE.ROUNDED_RECTANGLE,
                Inches(0.75), y, card_w, card_h,
                fill_color=RGBColor(255, 255, 255),
            )
            # Khối màu bên trái
            self.add_shape(
                MSO_SHAPE.RECTANGLE,
                Inches(0.75), y, Inches(0.06), card_h,
                fill_color=self._get_color("accent"),
            )
            # Tên công ty
            self.add_textbox(
                case["company"],
                Inches(1.1), y + Inches(0.3), Inches(3.5), Inches(0.4),
                font_size=16, font_color=self._get_color("text_primary"),
                bold=True, alignment=PP_ALIGN.LEFT,
            )
            # Nhãn ngành nghề
            self.add_shape(
                MSO_SHAPE.ROUNDED_RECTANGLE,
                Inches(1.1), y + Inches(0.8), Inches(1.2), Inches(0.3),
                fill_color=self._get_color("light"),
            )
            self.add_textbox(
                case["industry"],
                Inches(1.1), y + Inches(0.8), Inches(1.2), Inches(0.3),
                font_size=9, font_color=self._get_color("accent"),
                bold=True, alignment=PP_ALIGN.CENTER,
            )
            # Mô tả
            self.add_textbox(
                case["desc"],
                Inches(1.1), y + Inches(1.3), Inches(4.5), Inches(0.6),
                font_size=12, font_color=self._get_color("text_secondary"),
                alignment=PP_ALIGN.LEFT,
            )
            # Điểm sáng kết quả
            self.add_shape(
                MSO_SHAPE.ROUNDED_RECTANGLE,
                Inches(6.5), y + Inches(0.4), Inches(2.5), Inches(1.4),
                fill_color=self._get_color("accent"),
            )
            set_shape_transparency(self.slide.shapes[-1], 0.1)
            self.add_textbox(
                case["result"],
                Inches(6.5), y + Inches(0.7), Inches(2.5), Inches(0.6),
                font_size=20, font_color=RGBColor(255, 255, 255),
                bold=True, alignment=PP_ALIGN.CENTER,
            )

    def _gen_pricing(self):
        """Trang bảng giá dịch vụ"""
        self.create_slide()
        self._add_bg()
        self._add_page_title_bar("Bảng giá dịch vụ")

        plans = [
            {"name": "Bản Cơ bản", "price": "Miễn phí", "period": "",
             "features": ["5 người dùng", "10GB lưu trữ", "Phân tích cơ bản", "Hỗ trợ qua Email"],
             "highlight": False},
            {"name": "Bản Chuyên nghiệp", "price": "999.000", "period": "đ/tháng",
             "features": ["50 người dùng", "100GB lưu trữ", "Phân tích nâng cao", "Hỗ trợ ưu tiên"],
             "highlight": True},
            {"name": "Bản Doanh nghiệp", "price": "Liên hệ", "period": "",
             "features": ["Không giới hạn", "Lưu trữ vô hạn", "Tính năng riêng", "Chuyên viên tận nơi"],
             "highlight": False},
        ]

        card_w = Inches(2.6)
        card_h = Inches(4.5)
        gap = Inches(0.4)
        start_x = (Inches(10) - (3 * card_w + 2 * gap)) // 2

        for i, plan in enumerate(plans):
            x = start_x + i * (card_w + gap)
            y = Inches(1.3)
            # Thẻ
            self.add_shape(
                MSO_SHAPE.ROUNDED_RECTANGLE,
                x, y, card_w, card_h,
                fill_color=RGBColor(255, 255, 255),
            )
            if plan["highlight"]:
                # Viền làm nổi bật
                self.slide.shapes[-1].line.color.rgb = self._get_color("accent")
                self.slide.shapes[-1].line.width = Pt(2)
                # Nhãn đề xuất
                self.add_shape(
                    MSO_SHAPE.RECTANGLE,
                    x + Inches(0.8), y - Inches(0.2),
                    Inches(1.0), Inches(0.35),
                    fill_color=self._get_color("accent"),
                )
                self.add_textbox(
                    "Phổ biến",
                    x + Inches(0.8), y - Inches(0.2),
                    Inches(1.0), Inches(0.35),
                    font_size=10, font_color=RGBColor(255, 255, 255),
                    bold=True, alignment=PP_ALIGN.CENTER,
                )
            else:
                self.slide.shapes[-1].line.fill.background()

            # Tên gói
            self.add_textbox(
                plan["name"],
                x, y + Inches(0.3), card_w, Inches(0.4),
                font_size=18, font_color=self._get_color("text_primary"),
                bold=True, alignment=PP_ALIGN.CENTER,
            )
            # Mức giá
            self.add_textbox(
                plan["price"],
                x, y + Inches(0.9), card_w, Inches(0.6),
                font_size=32, font_color=self._get_color("accent") if plan["highlight"] else self._get_color("text_primary"),
                bold=True, alignment=PP_ALIGN.CENTER,
            )
            if plan["period"]:
                self.add_textbox(
                    plan["period"],
                    x, y + Inches(1.4), card_w, Inches(0.3),
                    font_size=11, font_color=self._get_color("text_secondary"),
                    alignment=PP_ALIGN.CENTER,
                )
            # Đường phân cách
            self.add_shape(
                MSO_SHAPE.RECTANGLE,
                x + Inches(0.3), y + Inches(1.8),
                card_w - Inches(0.6), Pt(1),
                fill_color=self._get_color("light"),
            )
            # Danh sách tính năng
            fy = y + Inches(2.0)
            for feat in plan["features"]:
                self.add_textbox(
                    f"  {feat}",
                    x + Inches(0.3), fy,
                    card_w - Inches(0.6), Inches(0.3),
                    font_size=11, font_color=self._get_color("text_secondary"),
                    alignment=PP_ALIGN.LEFT,
                )
                fy += Inches(0.35)

    def _gen_competitor(self):
        """Trang so sánh đối thủ"""
        self.create_slide()
        self._add_bg()
        self._add_page_title_bar("So sánh đối thủ")

        headers = ["Tính năng", "Chúng tôi", "Đối thủ A", "Đối thủ B"]
        col_w = [Inches(2.0), Inches(2.3), Inches(2.3), Inches(2.3)]
        start_x = Inches(0.6)
        header_y = Inches(1.4)

        for i, (h, w) in enumerate(zip(headers, col_w)):
            x = start_x
            for j in range(i):
                x += col_w[j]
            self.add_shape(
                MSO_SHAPE.RECTANGLE,
                x, header_y, w, Inches(0.5),
                fill_color=self._get_color("primary") if i == 0 else self._get_color("accent"),
            )
            self.add_textbox(
                h, x, header_y, w, Inches(0.5),
                font_size=13, font_color=RGBColor(255, 255, 255),
                bold=True, alignment=PP_ALIGN.CENTER,
            )

        rows = [
            ("Phân tích AI", "Tích hợp sẵn động cơ AI", "Thu phụ phí đắt đỏ", "Không có"),
            ("Cộng tác nhóm", "Cộng tác thời gian thực", "Cộng tác cơ bản", "Không có"),
            ("Nền tảng API mở", "Mở hoàn toàn", "Mở một phần", "Không hỗ trợ"),
            ("Bảo mật dữ liệu", "Mã hóa cấp doanh nghiệp", "Mã hóa cơ bản", "Mã hóa tiêu chuẩn"),
            ("Mức giá", "Tối ưu và cạnh tranh", "Khá đắt", "Thấp nhưng ít tính năng"),
        ]

        for r, row in enumerate(rows):
            y = header_y + Inches(0.5 + r * 0.55)
            bg = RGBColor(240, 247, 255) if r % 2 == 0 else RGBColor(255, 255, 255)
            for i, (val, w) in enumerate(zip(row, col_w)):
                x = start_x
                for j in range(i):
                    x += col_w[j]
                self.add_shape(MSO_SHAPE.RECTANGLE, x, y, w, Inches(0.5), fill_color=bg)
                fc = self._get_color("text_primary") if i == 0 else self._get_color("text_secondary")
                self.add_textbox(
                    val, x, y, w, Inches(0.5),
                    font_size=11, font_color=fc,
                    bold=(i == 0), alignment=PP_ALIGN.CENTER,
                )

    def _gen_launch_plan(self):
        """Trang kế hoạch ra mắt"""
        self.create_slide()
        self._add_bg()
        self._add_page_title_bar("Kế hoạch ra mắt")

        phases = [
            ("Giai đoạn 1", "Quý 3/2025", "Thử nghiệm nội bộ", "Phát triển tính năng lõi\nMời người dùng thử nghiệm\nSửa lỗi và tinh chỉnh hiệu năng"),
            ("Giai đoạn 2", "Quý 4/2025", "Thử nghiệm công khai", "Mở đăng ký cộng đồng\nHoàn thiện tính năng\nThu thập phản hồi đóng góp"),
            ("Giai đoạn 3", "Quý 1/2026", "Phát hành chính thức", "Chiến dịch truyền thông lớn\nKết nối đối tác phân phối\nVận hành quy mô mở rộng"),
        ]

        # Trục thời gian
        line_y = Inches(3.5)
        self.add_shape(
            MSO_SHAPE.RECTANGLE,
            Inches(0.8), line_y, Inches(8.4), Pt(3),
            fill_color=self._get_color("accent"),
        )

        node_w = Inches(2.5)
        total_w = len(phases) * node_w + (len(phases) - 1) * Inches(0.4)
        start_x = (Inches(10) - total_w) // 2

        for i, (phase, time, title, desc) in enumerate(phases):
            x = start_x + i * (node_w + Inches(0.4))
            # Điểm mốc
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

            # Thẻ
            card_y = line_y - Inches(2.2) if i % 2 == 0 else line_y + Inches(0.6)
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
                x + Inches(0.15), card_y + Inches(0.8), node_w - Inches(0.3), Inches(0.8),
                font_size=9, font_color=self._get_color("text_secondary"),
                alignment=PP_ALIGN.CENTER,
            )

    # ------------------------------------------------------------------ #
    #  Phương thức tạo chính
    # ------------------------------------------------------------------ #

    def generate(self):
        """Tạo trọn bộ 20 trang ra mắt sản phẩm"""
        self._gen_cover()           # 1. Trang bìa
        self._gen_directory()       # 2. Mục lục
        self._add_section_title("Phân tích bài toán", "Pain Points")  # 3. Tiêu đề phân mục
        self._gen_pain_points()     # 4. Phân tích bài toán
        self._gen_solution()        # 5. Giải pháp đột phá
        self._add_section_title("Tính năng sản phẩm", "Product Features")  # 6. Tiêu đề phân mục
        self._gen_product_feature(1)  # 7. Tính năng sản phẩm 1
        self._gen_product_feature(2)  # 8. Tính năng sản phẩm 2
        self._gen_product_feature(3)  # 9. Tính năng sản phẩm 3
        self._gen_product_feature(4)  # 10. Tính năng sản phẩm 4
        self._add_section_title("Trình diễn & Điển hình", "Demo & Cases")  # 11. Tiêu đề phân mục
        self._gen_demo()            # 12. Trình diễn sản phẩm
        self._gen_user_case(1)      # 13. Khách hàng tiêu biểu 1
        self._gen_user_case(2)      # 14. Khách hàng tiêu biểu 2
        self._add_section_title("Hợp tác thương mại", "Business")  # 15. Tiêu đề phân mục
        self._gen_pricing()         # 16. Bảng giá dịch vụ
        self._gen_competitor()      # 17. So sánh đối thủ
        self._add_section_title("Kế hoạch ra mắt", "Launch Plan")  # 18. Tiêu đề phân mục
        self._gen_launch_plan()     # 19. Kế hoạch ra mắt
        self._add_thank_you()       # 20. Lời cảm ơn
        return self


if __name__ == "__main__":
    assembler = ProductLaunchAssembler()
    assembler.set_title("Lễ ra mắt sản phẩm").set_subtitle("Sản phẩm đột phá - Vươn tầm công nghệ")
    assembler.generate()
    output_path = os.path.join(os.path.dirname(__file__), '..', '..', 'output_product_launch.pptx')
    assembler.save(output_path)
    print(f"Đã tạo bài thuyết trình ra mắt sản phẩm: {output_path}")
