"""Bộ lắp ráp bài thuyết trình Chủ đề công nghệ hoàn chỉnh

Tạo bài thuyết trình chủ đề công nghệ gồm 16 trang:
Trang bìa -> Mục lục -> Kiến trúc công nghệ -> Công nghệ cốt lõi (3 trang) -> Ngăn xếp công nghệ -> Chỉ số hiệu năng (2 trang) -> Định hướng tương lai -> Lời cảm ơn

Mặc định sử dụng chủ đề Vàng kim sang trọng, bìa phong cách xoay hình học (biến thể nền tối).
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


class TechnologyThemeAssembler(TemplateGenerator):
    """Bộ lắp ráp bài thuyết trình Chủ đề công nghệ (16 slide)"""

    DEFAULT_THEME = {
        "primary": "#1A1A2E",
        "secondary": "#16213E",
        "accent": "#D4AF37",
        "highlight": "#F5DEB3",
        "light": "#2C2C3E",
        "bg": "#0F0F1A",
        "text_primary": "#D4AF37",
        "text_secondary": "#A0A0B0",
        "text_light": "#FFFFFF",
    }

    def __init__(self, theme=None):
        super().__init__(theme=theme)
        self._title = "Chủ đề công nghệ"
        self._subtitle = "Technology Theme"
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
            - architecture: Kiến trúc công nghệ
            - core_tech: Danh sách công nghệ cốt lõi
            - tech_stack: Thông tin ngăn xếp công nghệ
            - performance: Chỉ số hiệu năng
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
        self.add_shape(
            MSO_SHAPE.RECTANGLE,
            Inches(0), Inches(0), Inches(10), Inches(1.0),
            fill_color=self._get_color("primary"),
        )
        # Đường viền đáy màu vàng kim
        self.add_shape(
            MSO_SHAPE.RECTANGLE,
            Inches(0), Inches(0.95), Inches(10), Pt(2),
            fill_color=self._get_color("accent"),
        )
        self.add_textbox(
            title,
            Inches(0.6), Inches(0.15), Inches(8.8), Inches(0.7),
            font_size=28, font_color=self._get_color("text_light"),
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
            font_size=48, font_color=self._get_color("accent"),
            bold=True, alignment=PP_ALIGN.CENTER,
        )
        self.add_textbox(
            "Khai phá không giới hạn - Đổi mới không ngừng",
            Inches(1), Inches(3.5), Inches(8), Inches(0.8),
            font_size=22, font_color=RGBColor(160, 160, 176),
            alignment=PP_ALIGN.CENTER,
        )
        line_w = Inches(2)
        self.add_shape(
            MSO_SHAPE.RECTANGLE,
            (Inches(10) - line_w) // 2, Inches(3.3),
            line_w, Pt(2),
            fill_color=self._get_color("accent"),
        )
        # Điểm trang trí
        for i in range(5):
            x = Inches(3.5) + Inches(i * 0.8)
            self.add_shape(
                MSO_SHAPE.OVAL,
                x, Inches(4.5), Inches(0.1), Inches(0.1),
                fill_color=self._get_color("accent"),
            )
            set_shape_transparency(self.slide.shapes[-1], 0.3 + i * 0.12)

    def _add_tech_card(self, left, top, width, height, title, items):
        self.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            left, top, width, height,
            fill_color=self._get_color("light"),
        )
        # Đường kẻ đỉnh màu vàng kim
        self.add_shape(
            MSO_SHAPE.RECTANGLE,
            left, top, width, Pt(2),
            fill_color=self._get_color("accent"),
        )
        self.add_textbox(
            title,
            left + Inches(0.2), top + Inches(0.15),
            width - Inches(0.4), Inches(0.35),
            font_size=14, font_color=self._get_color("accent"),
            bold=True, alignment=PP_ALIGN.LEFT,
        )
        y = top + Inches(0.6)
        for item in items[:5]:
            self.add_textbox(
                f"  {item}",
                left + Inches(0.2), y,
                width - Inches(0.4), Inches(0.25),
                font_size=10, font_color=self._get_color("text_secondary"),
                alignment=PP_ALIGN.LEFT,
            )
            y += Inches(0.28)

    # ------------------------------------------------------------------ #
    #  Phương thức tạo từng trang slide
    # ------------------------------------------------------------------ #

    def _gen_cover(self):
        """Trang bìa: Xoay hình học (Biến thể nền tối)"""
        self.create_slide()
        primary = self._get_color("primary")
        secondary = self._get_color("secondary")
        accent = self._get_color("accent")
        highlight = self._get_color("highlight")

        # Nền tối màu
        self.add_gradient_shape(
            MSO_SHAPE.RECTANGLE,
            Inches(0), Inches(0), Inches(10), Inches(7.5),
            [primary, secondary], angle=135,
        )

        # Hiệu ứng lưới nền
        for i in range(8):
            x = Inches(1.25 * i)
            self.add_shape(
                MSO_SHAPE.RECTANGLE,
                x, Inches(0), Pt(1), Inches(7.5),
                fill_color=accent,
            )
            set_shape_transparency(self.slide.shapes[-1], 0.92)
        for i in range(6):
            y = Inches(1.25 * i)
            self.add_shape(
                MSO_SHAPE.RECTANGLE,
                Inches(0), y, Inches(10), Pt(1),
                fill_color=accent,
            )
            set_shape_transparency(self.slide.shapes[-1], 0.92)

        # Họa tiết hình học trang trí (tông vàng kim)
        shapes_config = [
            (MSO_SHAPE.RECTANGLE, Inches(0.3), Inches(0.2), Inches(2.8), Inches(2.8), 15, accent),
            (MSO_SHAPE.DIAMOND, Inches(5.8), Inches(0.3), Inches(2.2), Inches(2.2), 0, highlight),
            (MSO_SHAPE.RECTANGLE, Inches(7.0), Inches(4.5), Inches(2.5), Inches(2.5), -20, accent),
            (MSO_SHAPE.DIAMOND, Inches(0.8), Inches(5.0), Inches(1.8), Inches(1.8), 30, highlight),
        ]
        for shape_type, left, top, w, h, rot, color in shapes_config:
            shape = self.add_shape(shape_type, left, top, w, h, fill_color=color)
            set_shape_transparency(shape, 0.65)
            if rot != 0:
                from lxml import etree
                xfrm = shape._element.find('.//{http://schemas.openxmlformats.org/drawingml/2006/main}xfrm')
                if xfrm is not None:
                    xfrm.set('rot', str(int(rot * 60000)))

        # Mặt nạ tối màu trung tâm
        mask_w = Inches(6.5)
        mask_h = Inches(3.0)
        self.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            (Inches(10) - mask_w) // 2, (Inches(7.5) - mask_h) // 2,
            mask_w, mask_h,
            fill_color=RGBColor(0, 0, 0),
        )
        set_shape_transparency(self.slide.shapes[-1], 0.35)
        self.slide.shapes[-1].line.fill.background()

        # Viền trang trí màu vàng kim
        self.add_shape(
            MSO_SHAPE.RECTANGLE,
            (Inches(10) - mask_w) // 2, (Inches(7.5) - mask_h) // 2,
            mask_w, Pt(1),
            fill_color=accent,
        )
        self.add_shape(
            MSO_SHAPE.RECTANGLE,
            (Inches(10) - mask_w) // 2, (Inches(7.5) + mask_h) // 2 - Pt(1),
            mask_w, Pt(1),
            fill_color=accent,
        )

        # Tiêu đề
        self.add_textbox(
            self._title,
            Inches(1.5), Inches(2.6), Inches(7.0), Inches(1.2),
            font_size=44, font_color=self._get_color("accent"),
            bold=True, alignment=PP_ALIGN.CENTER,
        )
        # Đường phân cách
        line_w = Inches(2.5)
        self.add_shape(
            MSO_SHAPE.RECTANGLE,
            (Inches(10) - line_w) // 2, Inches(3.85),
            line_w, Pt(1),
            fill_color=accent,
        )
        # Tiêu đề phụ
        self.add_textbox(
            self._subtitle,
            Inches(1.5), Inches(4.1), Inches(7.0), Inches(0.8),
            font_size=20, font_color=RGBColor(160, 160, 176),
            alignment=PP_ALIGN.CENTER,
        )

    def _gen_directory(self):
        self.create_slide()
        self._add_bg()
        self._add_page_title_bar("Mục lục")

        sections = [
            ("01", "Kiến trúc công nghệ"),
            ("02", "Công nghệ cốt lõi"),
            ("03", "Ngăn xếp công nghệ"),
            ("04", "Chỉ số hiệu năng"),
            ("05", "Định hướng tương lai"),
        ]
        card_w = Inches(2.6)
        card_h = Inches(1.6)
        gap = Inches(0.4)
        cols = 3
        start_x = (Inches(10) - (min(cols, len(sections)) * card_w + (min(cols, len(sections)) - 1) * gap)) // 2
        start_y = Inches(1.5)

        for i, (num, title) in enumerate(sections):
            row, col = divmod(i, cols)
            x = start_x + col * (card_w + gap)
            y = start_y + row * (card_h + gap)
            self.add_shape(
                MSO_SHAPE.ROUNDED_RECTANGLE,
                x, y, card_w, card_h,
                fill_color=self._get_color("light"),
            )
            self.add_shape(
                MSO_SHAPE.RECTANGLE,
                x, y, card_w, Pt(2),
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
                font_size=14, font_color=self._get_color("text_light"),
                bold=True, alignment=PP_ALIGN.CENTER,
            )

    def _gen_architecture(self):
        """Trang kiến trúc công nghệ"""
        self.create_slide()
        self._add_bg()
        self._add_page_title_bar("Kiến trúc công nghệ")

        # Các tầng kiến trúc
        layers = [
            ("Tầng ứng dụng", "Giao diện Web | Di động | Cổng API Gateway | Bảng quản trị", self._get_color("accent")),
            ("Tầng dịch vụ", "Cụm vi dịch vụ | Động cơ AI | Xử lý dữ liệu | Hàng đợi thông điệp", self._get_color("highlight")),
            ("Tầng dữ liệu", "Cơ sở dữ liệu quan hệ | Bộ nhớ đệm Cache | Lưu trữ đối tượng | Kho dữ liệu Data Warehouse", self._get_color("accent")),
            ("Tầng hạ tầng", "Kubernetes | Docker | CI/CD | Giám sát & Cảnh báo", self._get_color("highlight")),
        ]

        layer_w = Inches(8.5)
        layer_h = Inches(1.1)
        start_x = (Inches(10) - layer_w) // 2
        start_y = Inches(1.3)

        for i, (title, components, color) in enumerate(layers):
            y = start_y + i * (layer_h + Inches(0.2))
            # Nền từng tầng
            self.add_shape(
                MSO_SHAPE.ROUNDED_RECTANGLE,
                start_x, y, layer_w, layer_h,
                fill_color=self._get_color("light"),
            )
            # Nhãn bên trái
            label_w = Inches(1.5)
            self.add_shape(
                MSO_SHAPE.RECTANGLE,
                start_x, y, label_w, layer_h,
                fill_color=color,
            )
            set_shape_transparency(self.slide.shapes[-1], 0.2)
            self.add_textbox(
                title,
                start_x, y + Inches(0.1), label_w, Inches(0.4),
                font_size=14, font_color=RGBColor(255, 255, 255),
                bold=True, alignment=PP_ALIGN.CENTER,
            )
            # Thành phần
            self.add_textbox(
                components,
                start_x + label_w + Inches(0.3), y + Inches(0.3),
                layer_w - label_w - Inches(0.6), Inches(0.5),
                font_size=12, font_color=self._get_color("text_secondary"),
                alignment=PP_ALIGN.LEFT,
            )

        # Mũi tên liên kết
        for i in range(3):
            y = start_y + (i + 1) * (layer_h + Inches(0.2)) - Inches(0.15)
            self.add_textbox(
                "|",
                Inches(5), y, Inches(0.5), Inches(0.3),
                font_size=16, font_color=self._get_color("accent"),
                alignment=PP_ALIGN.CENTER,
            )

        # Ghi chú phía dưới
        self.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            Inches(0.5), Inches(6.3), Inches(9.0), Inches(0.8),
            fill_color=self._get_color("light"),
        )
        self.add_textbox(
            "Sẵn sàng cao | Mở rộng ngang | Kiến trúc vi dịch vụ | Cloud-Native | Chuẩn mực bảo mật",
            Inches(0.5), Inches(6.45), Inches(9.0), Inches(0.5),
            font_size=13, font_color=self._get_color("accent"),
            bold=True, alignment=PP_ALIGN.CENTER,
        )

    def _gen_core_tech(self, page_num=1):
        """Trang công nghệ cốt lõi"""
        self.create_slide()
        self._add_bg()
        self._add_page_title_bar(f"Công nghệ cốt lõi - Phần {page_num}")

        tech_data = {
            1: [
                {"title": "Động cơ tính toán phân tán", "items": ["Tính toán thời gian thực trên nền Spark/Flink", "Hỗ trợ xử lý dữ liệu quy mô PB", "Bảo đảm độ trễ mức mili-giây", "Tự động chịu lỗi và phục hồi"]},
                {"title": "Khung suy luận AI", "items": ["Động cơ suy luận mô hình độc quyền", "Hỗ trợ đầu vào đa phương thức", "Điều phối cụm máy chủ GPU", "Quản lý phiên bản mô hình"]},
            ],
            2: [
                {"title": "Hệ thống định tuyến thông minh", "items": ["Cân bằng tải động thông minh", "Điều phối lưu lượng thích ứng", "Tự động chuyển đổi khi sự cố", "Hỗ trợ kiến trúc Multi-Active"]},
                {"title": "Hệ thống an ninh phòng vệ", "items": ["Mô hình bảo mật Zero-Trust", "Mã hóa truyền dẫn đầu cuối", "Phát hiện mối đe dọa tức thời", "Nhật ký kiểm toán tuân thủ"]},
            ],
            3: [
                {"title": "Kiến trúc Data Lake", "items": ["Lưu trữ dữ liệu thống nhất", "Tự động phát hiện Schema", "Truy vết nguồn gốc dữ liệu", "Hợp nhất dữ liệu đa nguồn"]},
                {"title": "Nền tảng tính toán biên", "items": ["Quản lý nút tính toán biên", "Năng lực xử lý ngoại tuyến", "Hiệp đồng suy luận biên - mây", "Kết nối thiết bị tiêu chuẩn hóa"]},
            ],
        }

        items = tech_data.get(page_num, tech_data[1])
        card_w = Inches(4.2)
        card_h = Inches(4.5)
        gap = Inches(0.5)
        start_x = (Inches(10) - (2 * card_w + gap)) // 2

        for i, tech in enumerate(items):
            x = start_x + i * (card_w + gap)
            y = Inches(1.3)
            self._add_tech_card(x, y, card_w, card_h, tech["title"], tech["items"])

    def _gen_tech_stack(self):
        """Trang ngăn xếp công nghệ"""
        self.create_slide()
        self._add_bg()
        self._add_page_title_bar("Ngăn xếp công nghệ")

        stack_layers = [
            ("Frontend", ["React", "Vue.js", "TypeScript", "Flutter", "WebSocket"]),
            ("Backend", ["Go", "Python", "Java", "gRPC", "GraphQL"]),
            ("Dữ liệu", ["PostgreSQL", "Redis", "Kafka", "Elasticsearch", "ClickHouse"]),
            ("AI/ML", ["PyTorch", "TensorFlow", "HuggingFace", "ONNX", "CUDA"]),
            ("DevOps", ["K8s", "Docker", "Terraform", "ArgoCD", "Prometheus"]),
            ("Điện toán đám mây", ["AWS", "Alibaba Cloud", "GCP", "Azure", "Hạ tầng IDC nội bộ"]),
        ]

        card_w = Inches(2.8)
        card_h = Inches(2.2)
        gap_x = Inches(0.3)
        gap_y = Inches(0.25)
        cols = 3
        start_x = (Inches(10) - (cols * card_w + (cols - 1) * gap_x)) // 2

        for i, (layer_name, techs) in enumerate(stack_layers):
            row, col = divmod(i, cols)
            x = start_x + col * (card_w + gap_x)
            y = Inches(1.3) + row * (card_h + gap_y)
            self.add_shape(
                MSO_SHAPE.ROUNDED_RECTANGLE,
                x, y, card_w, card_h,
                fill_color=self._get_color("light"),
            )
            # Tên tầng
            self.add_shape(
                MSO_SHAPE.RECTANGLE,
                x, y, card_w, Inches(0.45),
                fill_color=self._get_color("accent"),
            )
            set_shape_transparency(self.slide.shapes[-1], 0.15)
            self.add_textbox(
                layer_name,
                x, y + Inches(0.05), card_w, Inches(0.35),
                font_size=13, font_color=RGBColor(255, 255, 255),
                bold=True, alignment=PP_ALIGN.CENTER,
            )
            # Nhãn công nghệ
            tag_y = y + Inches(0.6)
            tag_x = x + Inches(0.15)
            for j, tech in enumerate(techs):
                tag_w = Inches(1.1)
                tag_h = Inches(0.28)
                if tag_x + tag_w > x + card_w:
                    tag_x = x + Inches(0.15)
                    tag_y += Inches(0.35)
                self.add_shape(
                    MSO_SHAPE.ROUNDED_RECTANGLE,
                    tag_x, tag_y, tag_w, tag_h,
                    fill_color=self._get_color("primary"),
                )
                self.add_textbox(
                    tech,
                    tag_x, tag_y, tag_w, tag_h,
                    font_size=8, font_color=self._get_color("accent"),
                    bold=True, alignment=PP_ALIGN.CENTER,
                )
                tag_x += tag_w + Inches(0.1)

    def _gen_performance(self, page_num=1):
        """Trang chỉ số hiệu năng"""
        self.create_slide()
        self._add_bg()
        self._add_page_title_bar(f"Chỉ số hiệu năng - Phần {page_num}")

        contents = {
            1: ("Hiệu năng hệ thống", [
                {"metric": "Thời gian phản hồi API", "value": "<50ms", "pct": "P99"},
                {"metric": "Độ sẵn sàng hệ thống", "value": "99.99%", "pct": "SLA"},
                {"metric": "Xử lý đồng thời", "value": "100K+", "pct": "QPS"},
                {"metric": "Dung lượng dữ liệu", "value": "5PB/ngày", "pct": "Xử lý hàng ngày"},
            ]),
            2: ("Hiệu năng AI", [
                {"metric": "Suy luận mô hình", "value": "<10ms", "pct": "Độ trễ P99"},
                {"metric": "Hiệu suất huấn luyện", "value": "3x tăng tốc", "pct": "So với chuẩn"},
                {"metric": "Độ chính xác", "value": "98.5%", "pct": "F1-Score"},
                {"metric": "Kích thước mô hình", "value": "50MB", "pct": "Sau khi nén"},
            ]),
        }

        title, metrics = contents.get(page_num, contents[1])

        self.add_textbox(
            title,
            Inches(0.6), Inches(1.2), Inches(8.8), Inches(0.4),
            font_size=18, font_color=self._get_color("text_primary"),
            bold=True, alignment=PP_ALIGN.LEFT,
        )

        card_w = Inches(2.0)
        card_h = Inches(2.5)
        gap = Inches(0.3)
        start_x = (Inches(10) - (4 * card_w + 3 * gap)) // 2

        for i, m in enumerate(metrics):
            x = start_x + i * (card_w + gap)
            y = Inches(1.8)
            self.add_shape(
                MSO_SHAPE.ROUNDED_RECTANGLE,
                x, y, card_w, card_h,
                fill_color=self._get_color("light"),
            )
            # Đường đỉnh màu vàng kim
            self.add_shape(
                MSO_SHAPE.RECTANGLE,
                x, y, card_w, Pt(2),
                fill_color=self._get_color("accent"),
            )
            # Tên chỉ số
            self.add_textbox(
                m["metric"],
                x, y + Inches(0.3), card_w, Inches(0.3),
                font_size=12, font_color=self._get_color("text_secondary"),
                alignment=PP_ALIGN.CENTER,
            )
            # Giá trị số
            self.add_textbox(
                m["value"],
                x, y + Inches(0.8), card_w, Inches(0.6),
                font_size=28, font_color=self._get_color("accent"),
                bold=True, alignment=PP_ALIGN.CENTER,
            )
            # Nhãn
            self.add_textbox(
                m["pct"],
                x, y + Inches(1.6), card_w, Inches(0.3),
                font_size=10, font_color=self._get_color("text_secondary"),
                alignment=PP_ALIGN.CENTER,
            )

        # Thuyết minh
        details = {
            1: ["Triển khai đa khu vực toàn cầu, định tuyến gần nhất", "Tự động co giãn theo tải đáp ứng lưu lượng đỉnh", "Giám sát toàn diện chuỗi xử lý, cảnh báo mức giây"],
            2: ["Động cơ suy luận độc quyền, tối ưu hóa sâu", "Hỗ trợ lượng tử hóa và cắt tỉa mô hình", "Thử nghiệm A/B trực tuyến, lặp liên tục"],
        }
        detail_items = details.get(page_num, [])
        dy = Inches(4.8)
        for d in detail_items:
            self.add_textbox(
                f"  {d}",
                Inches(1.0), dy, Inches(8.0), Inches(0.3),
                font_size=12, font_color=self._get_color("text_secondary"),
                alignment=PP_ALIGN.LEFT,
            )
            dy += Inches(0.35)

    def _gen_future_plan(self):
        """Trang định hướng tương lai"""
        self.create_slide()
        self._add_bg()
        self._add_page_title_bar("Định hướng tương lai")

        roadmap = [
            {"time": "Kỳ 2/2025", "title": "Công nghệ chuyên sâu", "items": ["Phát triển năng lực mô hình lớn", "Nâng cấp tính toán thời gian thực", "Gia cố toàn diện an toàn thông tin"]},
            {"time": "Kỳ 1/2026", "title": "Nền tảng hóa", "items": ["Mở cổng nền tảng Open API", "Xây dựng hệ sinh thái nhà phát triển", "Đóng gói giải pháp ngành hoàn chỉnh"]},
            {"time": "Kỳ 2/2026", "title": "Toàn cầu hóa", "items": ["Mở rộng triển khai đa khu vực", "Hỗ trợ giao diện đa ngôn ngữ", "Chứng nhận tuân thủ quốc tế"]},
        ]

        card_w = Inches(2.6)
        card_h = Inches(4.0)
        gap = Inches(0.4)
        start_x = (Inches(10) - (3 * card_w + 2 * gap)) // 2

        for i, phase in enumerate(roadmap):
            x = start_x + i * (card_w + gap)
            y = Inches(1.3)
            self.add_shape(
                MSO_SHAPE.ROUNDED_RECTANGLE,
                x, y, card_w, card_h,
                fill_color=self._get_color("light"),
            )
            # Chuyển sắc vàng kim phía trên
            self.add_gradient_shape(
                MSO_SHAPE.RECTANGLE,
                x, y, card_w, Inches(1.0),
                [self._get_color("accent"), self._get_color("highlight")],
                angle=90,
            )
            set_shape_transparency(self.slide.shapes[-1], 0.2)
            self.add_textbox(
                phase["time"],
                x, y + Inches(0.1), card_w, Inches(0.35),
                font_size=14, font_color=RGBColor(255, 255, 255),
                bold=True, alignment=PP_ALIGN.CENTER,
            )
            self.add_textbox(
                phase["title"],
                x, y + Inches(0.5), card_w, Inches(0.35),
                font_size=12, font_color=self._get_color("text_light"),
                alignment=PP_ALIGN.CENTER,
            )
            # Danh sách
            iy = y + Inches(1.3)
            for item in phase["items"]:
                self.add_textbox(
                    f"  {item}",
                    x + Inches(0.2), iy, card_w - Inches(0.4), Inches(0.3),
                    font_size=12, font_color=self._get_color("text_secondary"),
                    alignment=PP_ALIGN.LEFT,
                )
                iy += Inches(0.5)

        # Tầm nhìn phía dưới
        self.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            Inches(0.5), Inches(5.8), Inches(9.0), Inches(1.2),
            fill_color=self._get_color("light"),
        )
        self.add_textbox(
            "Tầm nhìn công nghệ",
            Inches(0.8), Inches(5.9), Inches(8.4), Inches(0.35),
            font_size=14, font_color=self._get_color("accent"),
            bold=True, alignment=PP_ALIGN.LEFT,
        )
        self.add_textbox(
            "Lấy đổi mới công nghệ làm động lực tăng trưởng kinh doanh, kiến tạo nền tảng công nghệ dẫn đầu ngành, trao quyền cho các lĩnh vực chuyển đổi số toàn diện.",
            Inches(0.8), Inches(6.3), Inches(8.4), Inches(0.5),
            font_size=12, font_color=self._get_color("text_secondary"),
            alignment=PP_ALIGN.LEFT,
        )

    # ------------------------------------------------------------------ #
    #  Phương thức tạo chính
    # ------------------------------------------------------------------ #

    def generate(self):
        """Tạo trọn bộ 16 trang chủ đề công nghệ"""
        self._gen_cover()              # 1. Trang bìa
        self._gen_directory()          # 2. Mục lục
        self._add_section_title("Kiến trúc công nghệ", "Architecture")  # 3. Tiêu đề phân mục
        self._gen_architecture()       # 4. Kiến trúc công nghệ
        self._add_section_title("Công nghệ cốt lõi", "Core Technology")  # 5. Tiêu đề phân mục
        self._gen_core_tech(1)         # 6. Công nghệ cốt lõi 1
        self._gen_core_tech(2)         # 7. Công nghệ cốt lõi 2
        self._gen_core_tech(3)         # 8. Công nghệ cốt lõi 3
        self._add_section_title("Ngăn xếp công nghệ & Hiệu năng", "Tech Stack & Performance")  # 9. Tiêu đề phân mục
        self._gen_tech_stack()         # 10. Ngăn xếp công nghệ
        self._gen_performance(1)       # 11. Chỉ số hiệu năng 1
        self._gen_performance(2)       # 12. Chỉ số hiệu năng 2
        self._add_section_title("Định hướng tương lai", "Future Roadmap")  # 13. Tiêu đề phân mục
        self._gen_future_plan()        # 14. Định hướng tương lai
        self._add_section_title("Tổng kết", "Summary")  # 15. Tiêu đề phân mục
        self._add_thank_you()          # 16. Lời cảm ơn
        return self


if __name__ == "__main__":
    assembler = TechnologyThemeAssembler()
    assembler.set_title("Chủ đề công nghệ").set_subtitle("Kiến trúc công nghệ & Định hướng tương lai")
    assembler.generate()
    output_path = os.path.join(os.path.dirname(__file__), '..', '..', 'output_technology_theme.pptx')
    assembler.save(output_path)
    print(f"Đã tạo bài thuyết trình chủ đề công nghệ: {output_path}")
