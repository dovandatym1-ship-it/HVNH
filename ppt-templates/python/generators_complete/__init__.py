"""Bộ lắp ráp bản thuyết trình hoàn chỉnh

Kết hợp các bộ tạo slide đơn lẻ thành bài thuyết trình hoàn chỉnh từ 15-25 trang.
Mỗi bộ lắp ráp phụ trách một kịch bản thuyết trình cụ thể, bao gồm trang bìa, mục lục, các trang nội dung và trang kết thúc.
"""

from python.generators_complete.business_plan import BusinessPlanAssembler
from python.generators_complete.career_planning import CareerPlanningAssembler
from python.generators_complete.product_launch import ProductLaunchAssembler
from python.generators_complete.annual_report import AnnualReportAssembler
from python.generators_complete.education_course import EducationCourseAssembler
from python.generators_complete.technology_theme import TechnologyThemeAssembler

__all__ = [
    "BusinessPlanAssembler",
    "CareerPlanningAssembler",
    "ProductLaunchAssembler",
    "AnnualReportAssembler",
    "EducationCourseAssembler",
    "TechnologyThemeAssembler",
]
