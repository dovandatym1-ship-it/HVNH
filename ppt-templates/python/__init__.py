"""Bộ sinh mẫu PPT (phía Python) —— API công khai thống nhất

Cách dùng khuyến nghị:

    from python import BarChart, ALL_THEMES

    theme = ALL_THEMES["blue_technology"]()
    chart = BarChart(theme=theme)
    chart.set_title("Doanh thu theo quý").set_data([{"label": "Q1", "value": 120}])
    chart.generate()
    chart.save("out.pptx")

Module này không làm thay đổi bất kỳ đường dẫn submodule có sẵn nào (``python.base``, ``python.generators_cover``,...
vẫn có thể import trực tiếp), chỉ đóng vai trò xuất tổng hợp tại đây để thuận tiện sử dụng từ bên ngoài.
"""

from python.base import TemplateGenerator

from python.utils import (
    hex_to_rgb,
    create_circle_positions,
    create_grid_positions,
    add_shadow,
    set_shape_transparency,
    format_text,
)

from python.animation import (
    apply_animations_to_slide,
    add_slide_morph_transition,
)

from themes import BaseTheme, ALL_THEMES

# ---------------- Trang bìa (8) ----------------
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

# ---------------- Mục lục (6) ----------------
from python.generators_directory import (
    DiamondAnimatedGenerator,
    CircularRingGenerator,
    HexagonGenerator,
    SidebarGenerator,
    CardGridGenerator,
    TimelineStyleGenerator,
)

# ---------------- Trang nội dung (5) ----------------
from python.generators_content import (
    TextImageLayoutGenerator,
    ThreeColumnGenerator,
    FourGridGenerator,
    FullImageOverlayGenerator,
    ComparisonGenerator,
)

# ---------------- Biểu đồ (4) ----------------
from python.generators_chart import (
    BarChart,
    PieChart,
    LineChart,
    AnimatedBarChart,
)

# ---------------- Dòng thời gian (4) ----------------
from python.generators_timeline import (
    DualWaveTimeline,
    HorizontalTimeline,
    VerticalTimeline,
    SpiralTimeline,
)

# ---------------- Đội ngũ (3) ----------------
from python.generators_team import (
    PersonCardGenerator,
    TeamGridGenerator,
    OrgChartGenerator,
)

# ---------------- Kết thúc (3) ----------------
from python.generators_ending import (
    ThankYouGenerator,
    QRCodeGenerator,
    ContactPageGenerator,
)

# ---------------- Bộ dựng bài thuyết trình hoàn chỉnh (6) ----------------
from python.generators_complete import (
    BusinessPlanAssembler,
    CareerPlanningAssembler,
    ProductLaunchAssembler,
    AnnualReportAssembler,
    EducationCourseAssembler,
    TechnologyThemeAssembler,
)

__version__ = "1.1.0"

__all__ = [
    # Cơ sở
    "TemplateGenerator",
    "BaseTheme",
    "ALL_THEMES",
    "hex_to_rgb",
    "create_circle_positions",
    "create_grid_positions",
    "add_shadow",
    "set_shape_transparency",
    "format_text",
    "apply_animations_to_slide",
    "add_slide_morph_transition",
    # Trang bìa
    "GeometricRotationCover",
    "CircleRingCover",
    "TrainMistCover",
    "DiamondRevealCover",
    "MinimalistGradientCover",
    "SplitScreenCover",
    "HollowMaskCover",
    "LayeredDepthCover",
    # Mục lục
    "DiamondAnimatedGenerator",
    "CircularRingGenerator",
    "HexagonGenerator",
    "SidebarGenerator",
    "CardGridGenerator",
    "TimelineStyleGenerator",
    # Trang nội dung
    "TextImageLayoutGenerator",
    "ThreeColumnGenerator",
    "FourGridGenerator",
    "FullImageOverlayGenerator",
    "ComparisonGenerator",
    # Biểu đồ
    "BarChart",
    "PieChart",
    "LineChart",
    "AnimatedBarChart",
    # Dòng thời gian
    "DualWaveTimeline",
    "HorizontalTimeline",
    "VerticalTimeline",
    "SpiralTimeline",
    # Đội ngũ
    "PersonCardGenerator",
    "TeamGridGenerator",
    "OrgChartGenerator",
    # Kết thúc
    "ThankYouGenerator",
    "QRCodeGenerator",
    "ContactPageGenerator",
    # Bài thuyết trình hoàn chỉnh
    "BusinessPlanAssembler",
    "CareerPlanningAssembler",
    "ProductLaunchAssembler",
    "AnnualReportAssembler",
    "EducationCourseAssembler",
    "TechnologyThemeAssembler",
    "__version__",
]
