"""Kiểm thử hợp đồng tiêm dữ liệu (Data Injection Contract Tests)

Chữ ký hàm set_data / set_items của 39 bộ sinh không hoàn toàn đồng nhất, đây là hiện trạng tương thích có chủ đích;
Kiểm thử này sử dụng bảng hợp đồng tường minh "Lớp -> Trình khởi tạo dữ liệu" để mô tả cách gọi hợp lệ của từng lớp.
Mọi thay đổi chữ ký của bất kỳ bộ sinh nào cũng sẽ thất bại tại đây, thay vì đợi đến khi sinh hàng loạt mới phát hiện khuôn mẫu rỗng.

Bảng hợp đồng đồng bộ với các hằng số sample trong scripts/generate_all.py:
Khi thêm mục mới trong bảng đăng ký, bắt buộc phải đăng ký hợp đồng dữ liệu tại đây.
"""

import os
import sys

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from python.generators_chart import (
    AnimatedBarChart,
    BarChart,
    LineChart,
    PieChart,
)
from python.generators_content import (
    ComparisonGenerator,
    FourGridGenerator,
    FullImageOverlayGenerator,
    TextImageLayoutGenerator,
    ThreeColumnGenerator,
)
from python.generators_directory import (
    CardGridGenerator,
    CircularRingGenerator,
    DiamondAnimatedGenerator,
    HexagonGenerator,
    SidebarGenerator,
    TimelineStyleGenerator,
)
from python.generators_team import (
    OrgChartGenerator,
    PersonCardGenerator,
    TeamGridGenerator,
)
from python.generators_timeline import (
    DualWaveTimeline,
    HorizontalTimeline,
    SpiralTimeline,
    VerticalTimeline,
)

BAR_DATA = [{"label": f"Q{i}", "value": 100 + i} for i in range(1, 5)]
PIE_DATA = [{"label": f"Khu vực {i}", "value": 10 + i} for i in range(1, 4)]
LINE_SERIES = [{"name": "2025", "data": [1.0, 2.0, 3.0]}]
X_LABELS = ["Tháng 1", "Tháng 2", "Tháng 3"]

DIR_ITEMS = [{"number": "01", "title": f"Chương {i}", "description": "Mô tả"} for i in range(1, 4)]
TIMELINE_ITEMS = [{"number": "01", "title": "Khởi động", "subtitle": "Khảo sát"}]
EVENTS = [{"label": "Thành lập", "date": "2020", "detail": "Khởi nghiệp"}]
MEMBERS = [{"name": "Nguyễn Văn A", "title": "CEO"}]

CONTENT_ITEMS = {
    ComparisonGenerator: [{
        "left_title": "Phương án A", "left_items": ["Nhanh"],
        "right_title": "Phương án B", "right_items": ["Ổn định"],
    }],
    FourGridGenerator: [{"number": "01", "title": "Điểm chính", "description": "Mô tả"}],
    FullImageOverlayGenerator: [{"title": "Tuyên ngôn", "subtitle": "Vision", "description": "Mô tả"}],
    TextImageLayoutGenerator: [{"title": "Tiêu đề", "description": "Mô tả"}],
    ThreeColumnGenerator: [{"icon_text": "01", "title": "Ưu điểm", "description": "Mô tả"}],
}


def _instantiate(cls):
    """Tiêm dữ liệu mẫu theo chữ ký thực tế của từng nhóm."""
    if cls in (BarChart, AnimatedBarChart):
        data = cls()
        data.set_data(BAR_DATA, y_label="Triệu VNĐ")
    elif cls is PieChart:
        data = cls()
        data.set_data(PIE_DATA)
    elif cls is LineChart:
        data = cls()
        data.set_data(LINE_SERIES, X_LABELS, y_label="Triệu VNĐ")
    elif cls in (CardGridGenerator, SidebarGenerator, TimelineStyleGenerator):
        data = cls()
        data.set_title("Mục lục")
        data.set_items(DIR_ITEMS if cls is not TimelineStyleGenerator else TIMELINE_ITEMS)
    elif cls in (CircularRingGenerator, DiamondAnimatedGenerator, HexagonGenerator):
        data = cls()
        data.set_title("Mục lục")
        data.set_items(DIR_ITEMS)
    elif cls in (HorizontalTimeline, VerticalTimeline, SpiralTimeline, DualWaveTimeline):
        data = cls()
        data.set_data(EVENTS)
    elif cls is TeamGridGenerator:
        data = cls()
        data.set_members(MEMBERS)
        data.set_title("Đội ngũ")
    elif cls is PersonCardGenerator:
        data = cls()
        data.set_data(name="Nguyễn Văn A", title="CEO", bio="Nhà sáng lập")
    elif cls is OrgChartGenerator:
        data = cls()
        data.set_title("Cơ cấu tổ chức")
        data.set_data([[{"name": "CEO", "title": "Tổng giám đốc"}]])
    elif cls in CONTENT_ITEMS:
        data = cls()
        data.set_title("Tiêu đề")
        data.set_items(CONTENT_ITEMS[cls])
    else:
        raise AssertionError(f"Thiếu định nghĩa dữ liệu cho {cls.__name__} trong bảng hợp đồng")
    return data


CONTRACT_CLASSES = [
    BarChart, AnimatedBarChart, PieChart, LineChart,
    ComparisonGenerator, FourGridGenerator, FullImageOverlayGenerator,
    TextImageLayoutGenerator, ThreeColumnGenerator,
    CardGridGenerator, CircularRingGenerator, DiamondAnimatedGenerator,
    HexagonGenerator, SidebarGenerator, TimelineStyleGenerator,
    OrgChartGenerator, PersonCardGenerator, TeamGridGenerator,
    HorizontalTimeline, VerticalTimeline, SpiralTimeline, DualWaveTimeline,
]


@pytest.mark.parametrize("cls", CONTRACT_CLASSES, ids=lambda c: c.__name__)
def test_contract_generate_produces_slide(cls):
    """Sau khi tiêm dữ liệu đúng hợp đồng, phải sinh ra ít nhất 1 trang và trang đầu có không dưới 4 hình khối.

    'Ít nhất 1 trang' ngăn chặn lỗi rỗng khi items bị rỗng;
    'Hình khối >= 4' ngăn chặn các trang rỗng chỉ chứa mỗi tiêu đề (theo tiêu chuẩn của verify_templates.py).
    """
    gen = _instantiate(cls)
    gen.generate()
    prs = gen.prs
    assert len(prs.slides) >= 1, f"{cls.__name__} sinh ra 0 trang sau khi tiêm dữ liệu"
    assert len(prs.slides[0].shapes) >= 4, f"{cls.__name__} số hình khối ở trang đầu không đủ (nghi ngờ mẫu rỗng)"


@pytest.mark.parametrize("cls", CONTRACT_CLASSES, ids=lambda c: c.__name__)
def test_contract_theme_is_optional(cls):
    """Tất cả các bộ sinh bắt buộc phải hỗ trợ theme=None (không truyền chủ đề)."""
    _instantiate(cls)


def test_theme_instantiation_contract():
    """ALL_THEMES lưu trữ các lớp chứ không phải các thể hiện — dùng nhầm ALL_THEMES['x'].primary sẽ sinh trang không chủ đề."""
    from themes import ALL_THEMES

    for key, cls in ALL_THEMES.items():
        assert isinstance(cls, type), f"ALL_THEMES[{key!r}] phải là lớp chủ đề"
        instance = cls()
        for attr in ("primary", "secondary", "accent", "background", "text", "muted", "dark_bg"):
            assert hasattr(instance, attr), f"Chủ đề {key!r} thiếu thuộc tính {attr}"
