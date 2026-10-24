"""Bộ tạo sơ đồ cơ cấu tổ chức

Cấu trúc hình cây phân cấp: cấp cao nhất (CEO/Người đứng đầu) kết nối xuống cấp trung, cấp trung kết nối xuống cấp cơ sở,
giữa các nút được liên kết bằng đường kẻ, mỗi nút là một hình chữ nhật bo góc chứa tên và chức vụ.
"""

from pptx.enum.shapes import MSO_SHAPE
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from python.base import TemplateGenerator
from python.utils import hex_to_rgb, set_shape_transparency
from python.animation import apply_animations_to_slide


class OrgChartGenerator(TemplateGenerator):
    """Sơ đồ cơ cấu tổ chức"""

    DEFAULT_PRIMARY = "#1A237E"
    DEFAULT_SECONDARY = "#283593"
    DEFAULT_ACCENT = "#3F51B5"
    DEFAULT_LIGHT = "#C5CAE9"
    DEFAULT_BG = "#F5F7FA"
    DEFAULT_CARD_BG = "#FFFFFF"
    DEFAULT_TEXT_DARK = "#212121"
    DEFAULT_TEXT_WHITE = "#FFFFFF"
    DEFAULT_LINE_COLOR = "#90A4AE"

    def __init__(self, theme=None, **kwargs):
        super().__init__(theme=theme, **kwargs)
        self._title = "Sơ đồ tổ chức"
        # Dữ liệu phân cấp: danh sách các tầng
        # tầng 0: nút cao nhất, tầng 1: cấp trung, tầng 2: cấp dưới
        self._layers = [
            [{"name": "Nguyễn Văn A", "title": "Tổng Giám đốc (CEO)"}],
            [
                {"name": "Trần Thị B", "title": "Giám đốc Kỹ thuật"},
                {"name": "Lê Văn C", "title": "Giám đốc Sản phẩm"},
                {"name": "Phạm Minh D", "title": "Giám đốc Vận hành"},
            ],
            [
                {"name": "Hoàng Anh E", "title": "Trưởng nhóm Frontend"},
                {"name": "Vũ Hải F", "title": "Trưởng nhóm Backend"},
                {"name": "Đặng Quốc G", "title": "Quản lý Sản phẩm"},
                {"name": "Bùi Mai H", "title": "Quản lý Marketing"},
            ],
        ]

    def set_title(self, title):
        self._title = title
        return self

    def set_data(self, layers):
        """Thiết lập dữ liệu phân cấp
        layers: danh sách các danh sách dict, mỗi dict gồm 'name' và 'title'.
        Ví dụ: [[{"name":"CEO","title":"CEO"}], [{"name":"A","title":"CTO"}, ...], ...]
        """
        self._layers = layers
        return self

    def _get_color(self, attr, default_hex):
        if self.theme and hasattr(self.theme, attr):
            return getattr(self.theme, attr)
        return hex_to_rgb(default_hex)

    def _draw_node(self, cx, cy, name, title, w, h, fill_color, text_color,
                   delay, animations):
        """Vẽ một nút tổ chức và ghi nhận hiệu ứng hoạt họa"""
        left = cx - w // 2
        top = cy - h // 2

        node = self.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            left, top, w, h,
            fill_color=fill_color,
        )
        animations.append((node.shape_id, "fade_in", delay, 500))

        # Văn bản tên
        name_box = self.add_textbox(
            name,
            left + Inches(0.05), top + Inches(0.05),
            w - Inches(0.1), Inches(0.4),
            font_size=13, font_color=text_color,
            bold=True, alignment=PP_ALIGN.CENTER,
        )

        # Văn bản chức danh
        title_box = self.add_textbox(
            title,
            left + Inches(0.05), top + Inches(0.4),
            w - Inches(0.1), Inches(0.35),
            font_size=10, font_color=text_color,
            bold=False, alignment=PP_ALIGN.CENTER,
        )

        return node

    def _draw_connector(self, x1, y1, x2, y2, line_color, delay, animations):
        """Vẽ đường liên kết (dùng hình chữ nhật mỏng để mô phỏng)"""
        # Vẽ đường dọc + ngang bằng hình chữ nhật mỏng
        mid_y = y1 + (y2 - y1) // 2

        # Dọc từ nút cha tới điểm giữa
        v_line = self.add_shape(
            MSO_SHAPE.RECTANGLE,
            x1 - Pt(1), min(y1, mid_y), Pt(2), abs(mid_y - y1),
            fill_color=line_color,
        )
        animations.append((v_line.shape_id, "fade_in", delay, 300))

        # Ngang ở giữa
        h_left = min(x1, x2)
        h_right = max(x1, x2)
        h_line = self.add_shape(
            MSO_SHAPE.RECTANGLE,
            h_left, mid_y - Pt(1), h_right - h_left, Pt(2),
            fill_color=line_color,
        )
        animations.append((h_line.shape_id, "fade_in", delay + 100, 300))

        # Dọc từ điểm giữa tới nút con
        v2_line = self.add_shape(
            MSO_SHAPE.RECTANGLE,
            x2 - Pt(1), min(mid_y, y2), Pt(2), abs(y2 - mid_y),
            fill_color=line_color,
        )
        animations.append((v2_line.shape_id, "fade_in", delay + 200, 300))

    def generate(self):
        """Tạo slide sơ đồ tổ chức"""
        self.create_slide()

        primary = self._get_color("primary", self.DEFAULT_PRIMARY)
        accent = self._get_color("accent", self.DEFAULT_ACCENT)
        light = self._get_color("light", self.DEFAULT_LIGHT)

        slide_w = Inches(10)
        slide_h = Inches(7.5)

        animations = []
        line_color = hex_to_rgb(self.DEFAULT_LINE_COLOR)

        # --- Nền ---
        self.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, slide_w, slide_h,
                       fill_color=hex_to_rgb(self.DEFAULT_BG))

        # --- Thanh nhấn phía trên ---
        top_bar = self.add_gradient_shape(
            MSO_SHAPE.RECTANGLE,
            0, 0, slide_w, Inches(0.06),
            [primary, accent],
        )
        animations.append((top_bar.shape_id, "fade_in", 0, 400))

        # --- Tiêu đề ---
        title_box = self.add_textbox(
            self._title,
            Inches(0.5), Inches(0.35), Inches(9.0), Inches(0.65),
            font_size=30, font_color=hex_to_rgb(self.DEFAULT_TEXT_DARK),
            bold=True, alignment=PP_ALIGN.CENTER,
        )
        animations.append((title_box.shape_id, "fade_in", 100, 500))

        # --- Gạch chân trang trí tiêu đề ---
        deco = self.add_gradient_shape(
            MSO_SHAPE.RECTANGLE,
            Inches(3.8), Inches(1.08), Inches(2.4), Inches(0.04),
            [primary, accent],
        )
        animations.append((deco.shape_id, "fade_in", 200, 400))

        # --- Tham số bố cục ---
        num_layers = len(self._layers)
        # Khoảng cách dọc theo số lượng tầng
        layer_gap = Inches(1.6) if num_layers <= 3 else Inches(1.3)
        top_y = Inches(1.5)

        node_w = Inches(1.8)
        node_h = Inches(0.8)

        # Tính toán vị trí cho từng nút trên từng tầng
        layer_positions = []  # danh sách danh sách (cx, cy) theo từng tầng

        for layer_idx, layer in enumerate(self._layers):
            n = len(layer)
            cy = top_y + layer_idx * layer_gap
            total_w = n * node_w + (n - 1) * Inches(0.4)
            start_x = (slide_w - total_w) // 2
            positions = []
            for i in range(n):
                cx = start_x + i * (node_w + Inches(0.4)) + node_w // 2
                positions.append((cx, cy))
            layer_positions.append(positions)

        # --- Vẽ đường liên kết trước (nằm phía sau nút) ---
        for layer_idx in range(1, num_layers):
            parent_positions = layer_positions[layer_idx - 1]
            child_positions = layer_positions[layer_idx]
            n_parents = len(parent_positions)
            n_children = len(child_positions)

            # Phân bổ các nút con theo nút cha
            for c_idx, (child_cx, child_cy) in enumerate(child_positions):
                p_idx = int(c_idx * n_parents / n_children)
                parent_cx, parent_cy = parent_positions[p_idx]
                parent_bottom = parent_cy + node_h // 2
                child_top = child_cy - node_h // 2
                delay = 300 + layer_idx * 200 + c_idx * 50
                self._draw_connector(
                    parent_cx, parent_bottom,
                    child_cx, child_top,
                    line_color, delay, animations,
                )

        # --- Vẽ các nút (nằm đè lên đường liên kết) ---
        for layer_idx, layer in enumerate(self._layers):
            positions = layer_positions[layer_idx]
            for i, member in enumerate(layer):
                cx, cy = positions[i]

                if layer_idx == 0:
                    # Nút cao nhất: màu chính
                    fill = primary
                    text_col = hex_to_rgb(self.DEFAULT_TEXT_WHITE)
                    w = Inches(2.2)
                    h = Inches(0.9)
                elif layer_idx == 1:
                    # Cấp trung: màu nhấn
                    fill = accent
                    text_col = hex_to_rgb(self.DEFAULT_TEXT_WHITE)
                    w = Inches(1.9)
                    h = Inches(0.85)
                else:
                    # Cấp dưới: thẻ nền sáng với chữ tối
                    fill = hex_to_rgb(self.DEFAULT_CARD_BG)
                    text_col = hex_to_rgb(self.DEFAULT_TEXT_DARK)
                    w = Inches(1.7)
                    h = Inches(0.8)

                delay = 300 + layer_idx * 200 + i * 80
                self._draw_node(
                    cx, cy,
                    member.get("name", ""),
                    member.get("title", ""),
                    w, h, fill, text_col,
                    delay, animations,
                )

        # --- Họa tiết góc trang trí ---
        deco_d1 = self.add_shape(
            MSO_SHAPE.DIAMOND,
            Inches(0.3), Inches(6.8), Inches(0.3), Inches(0.3),
            fill_color=light,
        )
        set_shape_transparency(deco_d1, 0.4)
        animations.append((deco_d1.shape_id, "fade_in", 600, 400))

        deco_d2 = self.add_shape(
            MSO_SHAPE.DIAMOND,
            Inches(9.5), Inches(0.2), Inches(0.25), Inches(0.25),
            fill_color=accent,
        )
        set_shape_transparency(deco_d2, 0.45)
        animations.append((deco_d2.shape_id, "fade_in", 650, 400))

        # --- Áp dụng hiệu ứng hoạt họa ---
        apply_animations_to_slide(self.slide, animations)

        return self


if __name__ == "__main__":
    gen = OrgChartGenerator()
    gen.set_title("Sơ đồ tổ chức")
    gen.set_data([
        [{"name": "Nguyễn Văn A", "title": "Tổng Giám đốc (CEO)"}],
        [
            {"name": "Trần Thị B", "title": "Giám đốc Kỹ thuật"},
            {"name": "Lê Văn C", "title": "Giám đốc Sản phẩm"},
            {"name": "Phạm Minh D", "title": "Giám đốc Vận hành"},
        ],
        [
            {"name": "Hoàng Anh E", "title": "Trưởng nhóm Frontend"},
            {"name": "Vũ Hải F", "title": "Trưởng nhóm Backend"},
            {"name": "Đặng Quốc G", "title": "Quản lý Sản phẩm"},
            {"name": "Bùi Mai H", "title": "Quản lý Marketing"},
        ],
    ])
    output = gen.generate().save("org_chart.pptx")
    print(f"Đã lưu: {output}")
