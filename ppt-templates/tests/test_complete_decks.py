"""Kiểm thử hợp đồng bài thuyết trình hoàn chỉnh (templates/complete/)

6 bộ bài thuyết trình hoàn chỉnh do scripts/generate_decks.py sinh ra, số trang được bố cục cố định trong generate(),
vì vậy số trang là một giá trị tất định. Các assertion ở đây đồng bộ với bảng "Bài thuyết trình hoàn chỉnh" trong README:
Khi sửa đổi bố cục số trang của bất kỳ bộ nào, bắt buộc phải cập nhật đồng thời README và tệp này.
"""

import os
import sys

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from python.generators_complete import (
    AnnualReportAssembler,
    BusinessPlanAssembler,
    CareerPlanningAssembler,
    EducationCourseAssembler,
    ProductLaunchAssembler,
    TechnologyThemeAssembler,
)

# Tên tệp -> (Bộ dựng, Số trang tất định)
EXPECTED_DECKS = {
    "business_plan": (BusinessPlanAssembler, 18),
    "career_planning": (CareerPlanningAssembler, 16),
    "product_launch": (ProductLaunchAssembler, 20),
    "annual_report": (AnnualReportAssembler, 22),
    "education_course": (EducationCourseAssembler, 18),
    "technology_theme": (TechnologyThemeAssembler, 16),
}


@pytest.mark.parametrize("name", sorted(EXPECTED_DECKS), ids=str)
def test_deck_page_count(name):
    """Số trang là giá trị cố định: trình tự slide trong generate() được lập trình sẵn, không có nhánh rẽ động."""
    cls, expected_pages = EXPECTED_DECKS[name]
    deck = cls()
    deck.set_title("Kiểm thử hợp đồng").set_subtitle("Contract Test")
    deck.generate()
    assert len(deck.prs.slides) == expected_pages, (
        f"{name} có số trang là {len(deck.prs.slides)} (kỳ vọng {expected_pages}). "
        "Nếu đây là thay đổi có chủ đích, vui lòng cập nhật bảng README và tệp kiểm thử này."
    )


@pytest.mark.parametrize("name", sorted(EXPECTED_DECKS), ids=str)
def test_deck_default_theme_does_not_crash(name):
    """Khi không truyền theme thì sử dụng bảng màu mặc định tích hợp, không được văng lỗi AttributeError."""
    cls, _ = EXPECTED_DECKS[name]
    deck = cls()
    deck.set_title("Kiểm thử không chủ đề").set_subtitle("No Theme")
    deck.generate()  # Không được văng exception
    assert len(deck.prs.slides) > 0
