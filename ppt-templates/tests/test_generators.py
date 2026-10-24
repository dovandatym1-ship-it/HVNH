"""Kiểm thử đơn vị cho các bộ sinh biểu đồ và hệ thống chủ đề

Lưu ý: Chữ ký set_data của từng bộ sinh không hoàn toàn giống nhau, cần truyền dữ liệu theo từng lớp:
- BarChart / AnimatedBarChart : set_data(data, y_label)
- PieChart                   : set_data(data)
- LineChart                  : set_data(series, x_labels, y_label)
"""

import os
import sys

import pytest
from pptx import Presentation

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from python.generators_chart import (
    AnimatedBarChart,
    BarChart,
    LineChart,
    PieChart,
)
from themes import ALL_THEMES

BAR_DATA = [
    {"label": "Q1", "value": 120},
    {"label": "Q2", "value": 180},
    {"label": "Q3", "value": 95},
    {"label": "Q4", "value": 210},
]

PIE_DATA = [
    {"label": "Miền Bắc", "value": 42},
    {"label": "Miền Nam", "value": 28},
    {"label": "Miền Trung", "value": 30},
]

LINE_SERIES = [
    {"name": "2024", "data": [12.0, 18.0, 9.5, 21.0]},
    {"name": "2025", "data": [15.0, 22.0, 13.0, 25.5]},
]

X_LABELS = ["Q1", "Q2", "Q3", "Q4"]


def _theme(name="blue_technology"):
    """ALL_THEMES lưu trữ các lớp chủ đề, cần khởi tạo thể hiện trước khi dùng."""
    return ALL_THEMES[name]()


def _assert_valid_pptx(path, expected_slides=1):
    assert path.exists(), f"Không tìm thấy file đã sinh: {path}"
    assert path.stat().st_size > 0, "File PPTX sinh ra bị rỗng"
    reopened = Presentation(str(path))
    assert len(reopened.slides) == expected_slides
    return reopened


def test_bar_chart_roundtrip(tmp_path):
    chart = BarChart(theme=_theme())
    chart.set_title("Doanh thu theo quý", "Kiểm thử đơn vị")
    chart.set_data(BAR_DATA, y_label="Triệu VNĐ")
    chart.generate()
    out = tmp_path / "bar.pptx"
    chart.save(str(out))
    _assert_valid_pptx(out)


def test_animated_bar_chart_roundtrip(tmp_path):
    chart = AnimatedBarChart(theme=_theme())
    chart.set_title("Doanh thu theo quý (Hoạt họa)", "Kiểm thử đơn vị")
    chart.set_data(BAR_DATA, y_label="Triệu VNĐ")
    chart.generate()
    out = tmp_path / "animated.pptx"
    chart.save(str(out))
    _assert_valid_pptx(out)


def test_pie_chart_roundtrip(tmp_path):
    chart = PieChart(theme=_theme())
    chart.set_title("Tỷ trọng theo khu vực", "Kiểm thử đơn vị")
    chart.set_data(PIE_DATA)
    chart.generate()
    out = tmp_path / "pie.pptx"
    chart.save(str(out))
    _assert_valid_pptx(out)


def test_line_chart_roundtrip(tmp_path):
    chart = LineChart(theme=_theme())
    chart.set_title("Xu hướng theo năm", "Kiểm thử đơn vị")
    chart.set_data(LINE_SERIES, X_LABELS, y_label="Triệu VNĐ")
    chart.generate()
    out = tmp_path / "line.pptx"
    chart.save(str(out))
    _assert_valid_pptx(out)


@pytest.mark.parametrize("name", sorted(ALL_THEMES))
def test_theme_exposes_required_colors(name):
    theme = ALL_THEMES[name]()
    for attr in ("primary", "secondary", "accent", "background", "text", "muted"):
        assert getattr(theme, attr, None) is not None, f"{name} thiếu thuộc tính màu sắc {attr}"


@pytest.mark.parametrize("name", sorted(ALL_THEMES))
def test_theme_gradient_returns_color_pair(name):
    theme = ALL_THEMES[name]()
    for variant in ("primary", "accent", "dark"):
        gradient = theme.get_gradient(variant)
        assert isinstance(gradient, list) and len(gradient) >= 2


@pytest.mark.parametrize(
    "cls",
    [BarChart, PieChart, LineChart, AnimatedBarChart],
    ids=lambda c: c.__name__,
)
def test_generator_accepts_every_theme(cls):
    """Mỗi bộ sinh đều phải khởi tạo thành công với toàn bộ các chủ đề."""
    for name in ALL_THEMES:
        assert cls(theme=ALL_THEMES[name]()) is not None
