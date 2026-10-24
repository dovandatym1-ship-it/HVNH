"""
Script sinh chính - Kho Mẫu Slide PPT

Script này dùng để tạo hàng loạt tất cả các mẫu PPT chỉ bằng một lệnh và tổ chức vào thư mục templates/.
Đóng vai trò là script xây dựng chính của dự án, có thể được kích hoạt bởi CI/CD hoặc thủ công.

Cách chạy:
  python scripts/generate_all.py                         # Sinh toàn bộ mẫu
  python scripts/generate_all.py --theme blue_technology # Chỉ sinh chủ đề công nghệ xanh dương
  python scripts/generate_all.py --type cover            # Chỉ sinh mẫu trang bìa
  python scripts/generate_all.py --output ./out          # Chỉ định thư mục xuất

Cài đặt phụ thuộc:
  pip install -r requirements.txt
"""

import sys
import os
import time
import argparse

# Đảm bảo thư mục gốc dự án nằm trong search path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

from pptx.dml.color import RGBColor

# Import chủ đề
from themes import ALL_THEMES

# Bộ sinh trang bìa
from python.generators_cover import (
    GeometricRotationCover,
    CircleRingCover,
    TrainMistCover,
    DiamondRevealCover,
    MinimalistGradientCover,
    SplitScreenCover,
    HollowMaskCover,
    LayeredDepthCover,
)

# Bộ sinh mục lục
from python.generators_directory.diamond_animated import DiamondAnimatedGenerator
from python.generators_directory.circular_ring import CircularRingGenerator
from python.generators_directory.hexagon import HexagonGenerator
from python.generators_directory.sidebar import SidebarGenerator
from python.generators_directory.card_grid import CardGridGenerator
from python.generators_directory.timeline_style import TimelineStyleGenerator

# Bộ sinh dòng thời gian
from python.generators_timeline.horizontal import HorizontalTimeline
from python.generators_timeline.vertical import VerticalTimeline
from python.generators_timeline.dual_wave import DualWaveTimeline
from python.generators_timeline.spiral import SpiralTimeline

# Bộ sinh biểu đồ
from python.generators_chart.bar_chart import BarChart
from python.generators_chart.pie_chart import PieChart
from python.generators_chart.line_chart import LineChart
from python.generators_chart.animated_chart import AnimatedBarChart

# Bộ sinh trang nội dung
from python.generators_content.text_image_layout import TextImageLayoutGenerator
from python.generators_content.three_column import ThreeColumnGenerator
from python.generators_content.four_grid import FourGridGenerator
from python.generators_content.full_image_overlay import FullImageOverlayGenerator
from python.generators_content.comparison import ComparisonGenerator

# Bộ sinh trang đội ngũ
from python.generators_team.team_grid import TeamGridGenerator
from python.generators_team.person_card import PersonCardGenerator
from python.generators_team.org_chart import OrgChartGenerator

# Bộ sinh trang kết thúc
from python.generators_ending.thank_you import ThankYouGenerator
from python.generators_ending.qr_code import QRCodeGenerator
from python.generators_ending.contact import ContactPageGenerator


# ============================================================
# Bảng đăng ký mẫu (Template Registry)
# ============================================================

# Bảng đăng ký mẫu: Định nghĩa tất cả các mẫu có thể sinh cùng thông tin meta
# Mỗi mục mẫu bao gồm:
#   - class: Lớp sinh slide
#   - name: Định danh tên file
#   - label: Nhãn tiếng Việt
#   - category: Phân loại (animated/static)
#   - type: Loại (cover/directory/timeline/team/chart/content/ending)
#   - title: Tiêu đề mặc định
#   - subtitle: Tiêu đề phụ mặc định (tùy chọn)
#   - use_items: Có cần thiết lập dữ liệu mục lục/danh sách không
#   - use_events: Có cần thiết lập dữ liệu sự kiện dòng thời gian không
#   - use_members: Có cần thiết lập dữ liệu thành viên đội ngũ không

# ------------------------------------------------------------------ #
# Dữ liệu mẫu cho biểu đồ và trang nội dung
#
# Lưu ý: Hợp đồng trường dữ liệu của mỗi bộ sinh là khác nhau, không thể dùng chung
# DEFAULT_* như mục lục/dòng thời gian. Khi thiếu dữ liệu mẫu, trang biểu đồ chỉ vẽ
# tiêu đề, trang nội dung thậm chí không sinh ra slide nào, vì vậy mỗi mục mẫu bắt buộc phải có sample.
# ------------------------------------------------------------------ #

# Biểu đồ cột / Biểu đồ cột hoạt họa: list[dict{label, value}]
DEFAULT_CHART_BAR_DATA = [
    {"label": "Q1", "value": 120},
    {"label": "Q2", "value": 168},
    {"label": "Q3", "value": 205},
    {"label": "Q4", "value": 182},
    {"label": "Q5", "value": 246},
    {"label": "Q6", "value": 298},
]

# Biểu đồ tròn: list[dict{label, value}]
DEFAULT_CHART_PIE_DATA = [
    {"label": "Miền Bắc", "value": 38},
    {"label": "Miền Nam", "value": 24},
    {"label": "Miền Trung", "value": 19},
    {"label": "Tây Nguyên", "value": 11},
    {"label": "Khác", "value": 8},
]

# Biểu đồ đường: series là list[dict{name, data:list[float]}], data là danh sách số thực
DEFAULT_CHART_LINE_SERIES = [
    {"name": "2025", "data": [120.0, 150.0, 135.0, 200.0, 180.0, 220.0]},
    {"name": "2026", "data": [150.0, 178.0, 165.0, 236.0, 214.0, 268.0]},
]
DEFAULT_CHART_LINE_LABELS = ["Tháng 1", "Tháng 3", "Tháng 5", "Tháng 7", "Tháng 9", "Tháng 11"]

# Bố cục văn bản kèm hình ảnh: list[dict{title, description}], mỗi mục một trang
DEFAULT_CONTENT_TEXT_IMAGE = [
    {"title": "Bối cảnh dự án", "description": "Quy mô kinh doanh liên tục mở rộng, phương thức sản xuất thủ công không còn đáp ứng kịp tốc độ bàn giao, cần một giải pháp tạo bản trình bày có thể tham số hóa và tái sử dụng."},
    {"title": "Giải pháp cốt lõi", "description": "Tách biệt nội dung và kiểu dáng thông qua hệ thống chủ đề và các họ bộ sinh, một nguồn dữ liệu có thể điều khiển kết xuất trên cả Python và TypeScript."},
]

# Bố cục 3 cột: list[dict{icon_text, title, description}], tối đa 3 mục
DEFAULT_CONTENT_THREE_COLUMN = [
    {"icon_text": "01", "title": "Cộng tác hiệu quả", "description": "Quy chuẩn chủ đề và bố cục thống nhất, cộng tác liên nhóm không cần liên tục căn chỉnh chi tiết thị giác."},
    {"icon_text": "02", "title": "Dẫn dắt bởi dữ liệu", "description": "Trang biểu đồ được sinh trực tiếp từ dữ liệu, khi số liệu thay đổi chỉ cần chạy lại là cập nhật đồng bộ."},
    {"icon_text": "03", "title": "Liên tục phát triển", "description": "Thêm bộ sinh mới chỉ cần đăng ký vào bảng danh mục, script hàng loạt và cấu trúc thư mục sẽ tự động thích ứng."},
]

# Bố cục 4 ô lưới: list[dict{number, title, description}], tối đa 4 mục
DEFAULT_CONTENT_FOUR_GRID = [
    {"number": "01", "title": "Phân tích thị trường", "description": "Tổng quan quy mô ngành, tốc độ tăng trưởng và bối cảnh cạnh tranh."},
    {"number": "02", "title": "Thiết kế sản phẩm", "description": "Định nghĩa tính năng cốt lõi, hành trình người dùng và nguyên mẫu tương tác."},
    {"number": "03", "title": "Giải pháp kỹ thuật", "description": "Phân tầng kiến trúc, lựa chọn công nghệ trọng yếu và chỉ số hiệu năng."},
    {"number": "04", "title": "Kế hoạch vận hành", "description": "Chiến lược kênh phân phối, lộ trình triển khai và đo lường hiệu quả."},
]

# Phủ toàn màn hình: list[dict{title, subtitle, description}], mỗi mục một trang
DEFAULT_CONTENT_FULL_IMAGE = [
    {"title": "Tuyên ngôn thương hiệu", "subtitle": "Brand Vision", "description": "Đảm bảo mỗi lần xuất hiện đều giữ trọn chất lượng và tính chuyên nghiệp."},
    {"title": "Triết lý sản phẩm", "subtitle": "Product Philosophy", "description": "Giao phó công việc lặp lại cho mã lệnh, dành trọn sự sáng tạo cho chính nội dung."},
]

# Mục lục dòng thời gian: list[dict{number, title, subtitle}], nếu thiếu subtitle thẻ chỉ hiển thị tiêu đề
DEFAULT_TIMELINE_DIR_ITEMS = [
    {"number": "01", "title": "Khởi động dự án", "subtitle": "Khảo sát nhu cầu & xác định phạm vi"},
    {"number": "02", "title": "Thiết kế giải pháp", "subtitle": "Lựa chọn kiến trúc & đánh giá nguyên mẫu"},
    {"number": "03", "title": "Phát triển triển khai", "subtitle": "Lập trình module & tích hợp hệ thống"},
    {"number": "04", "title": "Kiểm thử nghiệm thu", "subtitle": "Kiểm thử chức năng & kiểm thử tải"},
    {"number": "05", "title": "Vận hành bàn giao", "subtitle": "Phát hành từng phần & bàn giao tài liệu"},
]

# Bố cục so sánh đối chiếu: list[dict{left_title, left_items, right_title, right_items}], mỗi mục một trang
DEFAULT_CONTENT_COMPARISON = [
    {
        "left_title": "Phương pháp truyền thống",
        "left_items": ["Phụ thuộc dàn trang thủ công, tốn thời gian và dễ lỗi", "Nhiều bộ tài liệu khó đồng nhất phong cách", "Tái sử dụng phải sao chép rồi sửa đổi"],
        "right_title": "Giải pháp này",
        "right_items": ["Script sinh hàng loạt, bàn giao trong vài phút", "7 bộ chủ đề đảm bảo tính nhất quán thị giác", "Chỉ cần đổi tham số là tái tạo lại toàn bộ"],
    },
]


TEMPLATE_REGISTRY = [
    # ========== Bìa hoạt họa ==========
    {
        "class": GeometricRotationCover,
        "name": "geometric_rotation",
        "label": "Bìa xoay hình học",
        "category": "animated",
        "type": "cover",
        "title": "Bìa xoay hình học",
        "subtitle": "Geometric Rotation Cover",
    },
    {
        "class": CircleRingCover,
        "name": "circle_ring",
        "label": "Bìa chuyển cảnh vòng tròn",
        "category": "animated",
        "type": "cover",
        "title": "Bìa chuyển cảnh vòng tròn",
        "subtitle": "Circle Ring Cover",
    },
    {
        "class": TrainMistCover,
        "name": "train_mist",
        "label": "Bìa tàu xuyên sương mù",
        "category": "animated",
        "type": "cover",
        "title": "Bìa tàu xuyên sương mù",
        "subtitle": "Train Mist Cover",
    },
    {
        "class": DiamondRevealCover,
        "name": "diamond_reveal",
        "label": "Bìa mở màn hình thoi",
        "category": "animated",
        "type": "cover",
        "title": "Bìa mở màn hình thoi",
        "subtitle": "Diamond Reveal Cover",
    },

    # ========== Bìa tĩnh ==========
    {
        "class": MinimalistGradientCover,
        "name": "minimalist_gradient",
        "label": "Bìa chuyển sắc tối giản",
        "category": "static",
        "type": "cover",
        "title": "Bìa chuyển sắc tối giản",
        "subtitle": "Minimalist Gradient Cover",
    },
    {
        "class": SplitScreenCover,
        "name": "split_screen",
        "label": "Bìa chia đôi màn hình",
        "category": "static",
        "type": "cover",
        "title": "Bìa chia đôi màn hình",
        "subtitle": "Split Screen Cover",
    },
    {
        "class": HollowMaskCover,
        "name": "hollow_mask",
        "label": "Bìa mặt nạ chữ rỗng",
        "category": "static",
        "type": "cover",
        "title": "Bìa mặt nạ chữ rỗng",
        "subtitle": "Hollow Mask Cover",
    },
    {
        "class": LayeredDepthCover,
        "name": "layered_depth",
        "label": "Bìa chiều sâu đa tầng",
        "category": "static",
        "type": "cover",
        "title": "Bìa chiều sâu đa tầng",
        "subtitle": "Layered Depth Cover",
    },

    # ========== Mục lục hoạt họa ==========
    {
        "class": DiamondAnimatedGenerator,
        "name": "diamond_animated",
        "label": "Mục lục hoạt họa hình thoi",
        "category": "animated",
        "type": "directory",
        "title": "Nội dung chính",
        "use_items": True,
    },
    {
        "class": CircularRingGenerator,
        "name": "circular_ring",
        "label": "Mục lục vòng tròn",
        "category": "animated",
        "type": "directory",
        "title": "Điều hướng mục lục",
        "use_items": True,
    },
    {
        "class": HexagonGenerator,
        "name": "hexagon",
        "label": "Mục lục tổ ong",
        "category": "animated",
        "type": "directory",
        "title": "Mục lục tổ ong",
        "use_items": True,
    },

    # ========== Mục lục tĩnh ==========
    {
        "class": SidebarGenerator,
        "name": "sidebar",
        "label": "Mục lục thanh bên",
        "category": "static",
        "type": "directory",
        "title": "Mục lục",
        "use_items": True,
    },
    {
        "class": CardGridGenerator,
        "name": "card_grid",
        "label": "Mục lục lưới thẻ",
        "category": "static",
        "type": "directory",
        "title": "Nội dung chính",
        "use_items": True,
    },
    {
        "class": TimelineStyleGenerator,
        "name": "timeline_style",
        "label": "Mục lục dòng thời gian",
        "category": "static",
        "type": "directory",
        "title": "Lịch trình thực hiện",
        "sample": DEFAULT_TIMELINE_DIR_ITEMS,
    },

    # ========== Dòng thời gian ==========
    {
        "class": HorizontalTimeline,
        "name": "horizontal",
        "label": "Dòng thời gian ngang",
        "category": "static",
        "type": "timeline",
        "title": "Lịch sử phát triển doanh nghiệp",
        "use_events": True,
    },
    {
        "class": VerticalTimeline,
        "name": "vertical",
        "label": "Dòng thời gian dọc",
        "category": "static",
        "type": "timeline",
        "title": "Lộ trình phát triển",
        "use_events": True,
    },
    {
        "class": DualWaveTimeline,
        "name": "dual_wave",
        "label": "Dòng thời gian sóng đôi",
        "category": "animated",
        "type": "timeline",
        "title": "Lộ trình phát triển",
        "use_events": True,
    },
    {
        "class": SpiralTimeline,
        "name": "spiral",
        "label": "Dòng thời gian xoắn ốc",
        "category": "animated",
        "type": "timeline",
        "title": "Lộ trình phát triển",
        "use_events": True,
    },

    # ========== Biểu đồ ==========
    {
        "class": BarChart,
        "name": "bar_chart",
        "label": "Biểu đồ cột",
        "category": "static",
        "type": "chart",
        "title": "Phân tích dữ liệu",
        "sample": DEFAULT_CHART_BAR_DATA,
    },
    {
        "class": PieChart,
        "name": "pie_chart",
        "label": "Biểu đồ tròn",
        "category": "static",
        "type": "chart",
        "title": "Phân tích tỷ trọng",
        "sample": DEFAULT_CHART_PIE_DATA,
    },
    {
        "class": LineChart,
        "name": "line_chart",
        "label": "Biểu đồ đường",
        "category": "static",
        "type": "chart",
        "title": "Phân tích xu hướng",
        # set_data của LineChart cần 2 tham số vị trí: (series, x_labels)
        "sample": (DEFAULT_CHART_LINE_SERIES, DEFAULT_CHART_LINE_LABELS),
    },
    {
        "class": AnimatedBarChart,
        "name": "animated_bar_chart",
        "label": "Biểu đồ cột hoạt họa",
        "category": "animated",
        "type": "chart",
        "title": "Trình diễn dữ liệu",
        "sample": DEFAULT_CHART_BAR_DATA,
    },

    # ========== Trang nội dung ==========
    {
        "class": TextImageLayoutGenerator,
        "name": "text_image_layout",
        "label": "Bố cục văn bản kèm hình ảnh",
        "category": "static",
        "type": "content",
        "title": "Trình bày nội dung",
        "sample": DEFAULT_CONTENT_TEXT_IMAGE,
    },
    {
        "class": ThreeColumnGenerator,
        "name": "three_column",
        "label": "Bố cục 3 cột",
        "category": "static",
        "type": "content",
        "title": "Ba ưu thế vượt trội",
        "sample": DEFAULT_CONTENT_THREE_COLUMN,
    },
    {
        "class": FourGridGenerator,
        "name": "four_grid",
        "label": "Bố cục 4 ô lưới",
        "category": "static",
        "type": "content",
        "title": "Điểm cốt lõi",
        "sample": DEFAULT_CONTENT_FOUR_GRID,
    },
    {
        "class": FullImageOverlayGenerator,
        "name": "full_image_overlay",
        "label": "Phủ toàn màn hình",
        "category": "static",
        "type": "content",
        "title": "Trình chiếu toàn trang",
        "sample": DEFAULT_CONTENT_FULL_IMAGE,
    },
    {
        "class": ComparisonGenerator,
        "name": "comparison",
        "label": "Bố cục so sánh",
        "category": "static",
        "type": "content",
        "title": "So sánh phương án",
        "sample": DEFAULT_CONTENT_COMPARISON,
    },

    # ========== Giới thiệu đội ngũ ==========
    {
        "class": TeamGridGenerator,
        "name": "team_grid",
        "label": "Lưới đội ngũ",
        "category": "static",
        "type": "team",
        "title": "Đội ngũ nòng cốt",
        "use_members": True,
    },
    {
        "class": PersonCardGenerator,
        "name": "person_card",
        "label": "Thẻ giới thiệu cá nhân",
        "category": "static",
        "type": "team",
        "title": "Giới thiệu nhân sự",
    },
    {
        "class": OrgChartGenerator,
        "name": "org_chart",
        "label": "Sơ đồ cơ cấu tổ chức",
        "category": "static",
        "type": "team",
        "title": "Cơ cấu tổ chức",
    },

    # ========== Trang kết thúc ==========
    {
        "class": ThankYouGenerator,
        "name": "thank_you",
        "label": "Trang cảm ơn",
        "category": "static",
        "type": "ending",
        "title": "Xin cảm ơn",
    },
    {
        "class": QRCodeGenerator,
        "name": "qr_code",
        "label": "Trang mã QR",
        "category": "static",
        "type": "ending",
        "title": "Quét mã quan tâm",
    },
    {
        "class": ContactPageGenerator,
        "name": "contact",
        "label": "Trang liên hệ",
        "category": "static",
        "type": "ending",
        "title": "Liên hệ chúng tôi",
    },
]


# ============================================================
# Dữ liệu mặc định
# ============================================================

# Dữ liệu mục lục mặc định
DEFAULT_DIR_ITEMS = [
    {"number": "01", "title": "Tổng quan dự án", "description": "Bối cảnh & mục tiêu dự án"},
    {"number": "02", "title": "Phân tích thị trường", "description": "Xu hướng ngành & bối cảnh cạnh tranh"},
    {"number": "03", "title": "Thiết kế sản phẩm", "description": "Tính năng cốt lõi & trải nghiệm người dùng"},
    {"number": "04", "title": "Giải pháp kỹ thuật", "description": "Thiết kế kiến trúc & chọn lọc công nghệ"},
    {"number": "05", "title": "Kế hoạch vận hành", "description": "Chiến lược quảng bá & lộ trình thực thi"},
    {"number": "06", "title": "Kế hoạch tài chính", "description": "Lập ngân sách & dự báo doanh thu"},
]

# Dữ liệu sự kiện dòng thời gian mặc định
DEFAULT_TIMELINE_EVENTS = [
    {"label": "Thành lập công ty", "date": "2020", "detail": "Xây dựng đội ngũ sáng lập"},
    {"label": "Nghiên cứu sản phẩm", "date": "2021", "detail": "Ra mắt sản phẩm cốt lõi"},
    {"label": "Mở rộng thị trường", "date": "2022", "detail": "Phủ sóng thị trường toàn quốc"},
    {"label": "Gọi vốn Vòng A", "date": "2023", "detail": "Hoàn thành gọi vốn triệu USD"},
    {"label": "Vươn ra quốc tế", "date": "2024", "detail": "Khai phá thị trường nước ngoài"},
]

# Dữ liệu thành viên đội ngũ mặc định
DEFAULT_TEAM_MEMBERS = [
    {"name": "Trần Minh", "title": "CEO Giám đốc điều hành"},
    {"name": "Lê Hoa", "title": "CTO Giám đốc công nghệ"},
    {"name": "Vương Phương", "title": "CPO Giám đốc sản phẩm"},
    {"name": "Triệu Cường", "title": "CFO Giám đốc tài chính"},
    {"name": "Trần Tĩnh", "title": "COO Giám đốc vận hành"},
    {"name": "Lưu Vĩ", "title": "CMO Giám đốc tiếp thị"},
]


# ============================================================
# Logic sinh cốt lõi
# ============================================================

def ensure_output_dirs(base_dir):
    """Tạo tất cả các thư mục xuất cần thiết

    Args:
        base_dir: Thư mục gốc chứa các mẫu xuất ra
    """
    subdirs = [
        "animated/cover",
        "animated/directory",
        "animated/timeline",
        "animated/chart",
        "animated/transition",
        "static/cover",
        "static/directory",
        "static/timeline",
        "static/chart",
        "static/content",
        "static/ending",
        "static/team",
        "complete",
    ]
    for subdir in subdirs:
        os.makedirs(os.path.join(base_dir, subdir), exist_ok=True)


def generate_template(template_info, theme, base_dir):
    """Sinh một mẫu slide đơn lẻ

    Args:
        template_info: Mục trong bảng đăng ký mẫu
        theme: Đối tượng chủ đề
        base_dir: Thư mục gốc xuất ra

    Returns:
        dict: Từ điển kết quả chứa success, filepath, elapsed, error
    """
    start = time.time()
    result = {
        "success": False,
        "filepath": "",
        "elapsed": 0,
        "error": None,
    }

    try:
        # Khởi tạo thể hiện của bộ sinh
        gen = template_info["class"](theme=theme)

        # Thiết lập tiêu đề
        if hasattr(gen, "set_title"):
            gen.set_title(template_info["title"])

        # Trang bìa cần thiết lập tiêu đề phụ
        if "subtitle" in template_info:
            if hasattr(gen, "set_subtitle"):
                gen.set_subtitle(template_info["subtitle"])

        # Thiết lập dữ liệu
        if template_info.get("use_items"):
            if hasattr(gen, "set_items"):
                gen.set_items(DEFAULT_DIR_ITEMS)
            elif hasattr(gen, "set_data"):
                gen.set_data(DEFAULT_DIR_ITEMS)

        if template_info.get("use_events"):
            if hasattr(gen, "set_data"):
                gen.set_data(DEFAULT_TIMELINE_EVENTS)

        if template_info.get("use_members"):
            if hasattr(gen, "set_members"):
                gen.set_members(DEFAULT_TEAM_MEMBERS)

        # Thiết lập dữ liệu mẫu: ưu tiên set_items, sau đó đến set_data.
        # Khi sample là tuple tức là set_data cần nhiều tham số vị trí (như LineChart: series + x_labels).
        if "sample" in template_info:
            sample = template_info["sample"]
            if hasattr(gen, "set_items"):
                gen.set_items(sample)
            elif isinstance(sample, tuple):
                gen.set_data(*sample)
            else:
                gen.set_data(sample)

        # Sinh slide
        gen.generate()

        # Xây dựng đường dẫn xuất (kèm tên chủ đề để tránh ghi đè)
        category = template_info["category"]
        page_type = template_info["type"]
        theme_key = [k for k, v in ALL_THEMES.items() if type(theme) is v]
        theme_name = theme_key[0] if theme_key else "default"
        filename = f"{template_info['name']}_{theme_name}.pptx"
        filepath = os.path.join(base_dir, category, page_type, filename)
        result["filepath"] = filepath

        # Lưu file
        gen.save(filepath)

        result["success"] = True
    except Exception as e:
        result["error"] = str(e)

    result["elapsed"] = time.time() - start
    return result


def run_generation(themes_filter=None, types_filter=None, output_dir=None):
    """Thực thi sinh hàng loạt

    Args:
        themes_filter: Danh sách lọc chủ đề (danh sách theme_key), None nghĩa là toàn bộ
        types_filter: Danh sách lọc loại mẫu (cover/directory/timeline/chart/content/team/ending), None nghĩa là toàn bộ
        output_dir: Thư mục xuất, None sẽ sử dụng mặc định templates/

    Returns:
        dict: Kết quả thống kê quá trình sinh
    """
    # Xác định thư mục xuất
    if output_dir is None:
        base_dir = os.path.join(project_root, "templates")
    else:
        base_dir = output_dir

    ensure_output_dirs(base_dir)

    # Xác định danh sách chủ đề cần sinh
    if themes_filter:
        themes_to_gen = {k: v for k, v in ALL_THEMES.items() if k in themes_filter}
    else:
        themes_to_gen = ALL_THEMES

    # Xác định danh sách loại mẫu cần sinh
    if types_filter:
        templates_to_gen = [
            t for t in TEMPLATE_REGISTRY
            if t["type"] in types_filter
        ]
    else:
        templates_to_gen = TEMPLATE_REGISTRY

    # Thống kê
    stats = {
        "total": 0,
        "success": 0,
        "failed": 0,
        "skipped": 0,
        "total_time": 0.0,
        "results": [],
    }

    print(f"\n  Thư mục xuất: {base_dir}")
    print(f"  Số lượng chủ đề: {len(themes_to_gen)}")
    print(f"  Số loại mẫu: {len(templates_to_gen)}")
    print(f"  Dự kiến sinh: {len(themes_to_gen) * len(templates_to_gen)} tệp")

    # Duyệt qua các chủ đề
    for theme_key, theme_cls in themes_to_gen.items():
        theme = theme_cls()
        print(f"\n{'━' * 60}")
        print(f"  Chủ đề: {theme.name}")
        print(f"{'━' * 60}")

        for tmpl in templates_to_gen:
            stats["total"] += 1

            result = generate_template(tmpl, theme, base_dir)

            status = "[OK]" if result["success"] else "[FAIL]"
            label = tmpl["label"]
            elapsed = result["elapsed"]

            if result["success"]:
                stats["success"] += 1
                filename = os.path.basename(result["filepath"])
                print(f"  {status} {label:<30} {filename:<45} {elapsed:.2f}s")
            else:
                stats["failed"] += 1
                print(f"  {status} {label:<30} Lỗi: {result['error']}")

            stats["results"].append({
                "theme": theme.name,
                "label": label,
                "category": tmpl["category"],
                "type": tmpl["type"],
                "success": result["success"],
                "filepath": result["filepath"],
                "elapsed": result["elapsed"],
                "error": result["error"],
            })

            stats["total_time"] += result["elapsed"]

    return stats


def print_summary(stats):
    """In báo cáo tổng kết quá trình sinh

    Args:
        stats: Từ điển kết quả thống kê
    """
    print("\n" + "=" * 60)
    print("  Báo cáo tổng kết quá trình sinh")
    print("=" * 60)
    print(f"  Tổng số mẫu  : {stats['total']} mẫu")
    print(f"  Thành công   : {stats['success']} mẫu")
    print(f"  Thất bại     : {stats['failed']} mẫu")
    print(f"  Tổng thời gian: {stats['total_time']:.2f} giây")
    if stats['total'] > 0:
        avg_time = stats['total_time'] / stats['total']
        print(f"  Trung bình   : {avg_time:.2f} giây/mẫu")

    # Thống kê theo phân loại
    categories = {}
    for r in stats["results"]:
        cat = r["type"]
        if cat not in categories:
            categories[cat] = {"total": 0, "success": 0}
        categories[cat]["total"] += 1
        if r["success"]:
            categories[cat]["success"] += 1

    print("\n  Thống kê theo phân loại:")
    for cat, count in categories.items():
        print(f"    {cat:<14} {count['success']}/{count['total']} thành công")

    # Chi tiết thất bại
    failures = [r for r in stats["results"] if not r["success"]]
    if failures:
        print("\n  Chi tiết thất bại:")
        for f in failures:
            print(f"    [{f['theme']}] {f['label']}: {f['error']}")

    print("=" * 60)


# ============================================================
# Điểm vào dòng lệnh (CLI)
# ============================================================

def parse_args():
    """Phân tích các tham số dòng lệnh"""
    parser = argparse.ArgumentParser(
        description="Kho Mẫu Slide PPT - Script sinh chính",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ví dụ:
  python scripts/generate_all.py                         # Sinh tất cả các mẫu
  python scripts/generate_all.py --theme blue_technology # Chỉ sinh chủ đề công nghệ xanh dương
  python scripts/generate_all.py --type cover            # Chỉ sinh mẫu trang bìa
  python scripts/generate_all.py --output ./my_templates # Chỉ định thư mục xuất

Các chủ đề có sẵn:
  blue_technology  - Công nghệ xanh dương
  purple_gradient  - Tím chuyển sắc
  dark_gold        - Vàng kim sang trọng
  minimalist_bw    - Đen trắng tối giản
  ocean_blue       - Xanh đại dương
  green_nature     - Xanh thiên nhiên
  red_business     - Đỏ thương mại

Các loại mẫu có sẵn:
  cover       - Mẫu trang bìa
  directory   - Mẫu mục lục
  timeline    - Mẫu dòng thời gian
  chart       - Mẫu biểu đồ
  content     - Mẫu trang nội dung
  team        - Mẫu giới thiệu đội ngũ
  ending      - Mẫu trang kết thúc
        """,
    )
    parser.add_argument(
        "--theme", "-t",
        nargs="+",
        help="Chỉ định chủ đề (có thể nhiều chủ đề), ví dụ: --theme blue_technology purple_gradient",
    )
    parser.add_argument(
        "--type", "-T",
        nargs="+",
        help="Chỉ định loại mẫu (có thể nhiều loại), ví dụ: --type cover directory",
    )
    parser.add_argument(
        "--output", "-o",
        help="Chỉ định thư mục xuất (mặc định: templates/)",
    )
    parser.add_argument(
        "--list-themes",
        action="store_true",
        help="Liệt kê tất cả các chủ đề có sẵn",
    )
    parser.add_argument(
        "--list-templates",
        action="store_true",
        help="Liệt kê tất cả các mẫu đã đăng ký",
    )
    return parser.parse_args()


def list_themes():
    """Liệt kê tất cả các chủ đề có sẵn"""
    print("\nCác chủ đề có sẵn:")
    print(f"  {'Khóa (Key)':<22} {'Tên':<25} {'Màu chính'}")
    print(f"  {'─'*22} {'─'*25} {'─'*12}")
    for key, cls in ALL_THEMES.items():
        theme = cls()
        print(f"  {key:<22} {theme.name:<25} {theme.primary}")


def list_templates():
    """Liệt kê tất cả các mẫu đã đăng ký"""
    print("\nCác mẫu đã đăng ký:")
    print(f"  {'Nhãn':<30} {'Phân loại':<12} {'Loại':<12} {'Tên tệp'}")
    print(f"  {'─'*30} {'─'*12} {'─'*12} {'─'*35}")
    for tmpl in TEMPLATE_REGISTRY:
        filename = f"{tmpl['type']}_{tmpl['category']}_{tmpl['name']}.pptx"
        print(f"  {tmpl['label']:<30} {tmpl['category']:<12} {tmpl['type']:<12} {filename}")


def main():
    """Hàm chạy chính"""
    args = parse_args()

    # Liệt kê thông tin
    if args.list_themes:
        list_themes()
        return
    if args.list_templates:
        list_templates()
        return

    print("=" * 60)
    print("  Kho Mẫu Slide PPT - Script sinh chính")
    print("  generate_all.py")
    print("=" * 60)

    # Thực hiện sinh
    start_time = time.time()
    stats = run_generation(
        themes_filter=args.theme,
        types_filter=args.type,
        output_dir=args.output,
    )
    elapsed = time.time() - start_time

    # In tổng kết
    print_summary(stats)

    print(f"\n  Tổng thời gian thực thi: {elapsed:.2f} giây")

    # Trả về mã trạng thái
    sys.exit(0 if stats["failed"] == 0 else 1)


if __name__ == "__main__":
    main()
