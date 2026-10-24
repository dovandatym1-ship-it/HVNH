"""
Dựng báo cáo Word (.docx) chuẩn "hvnh-assignment" cho đồ án cuối kỳ:
"Tác động của Trí tuệ nhân tạo (AI) đến Việc làm năm 2030"

Sử dụng thư viện recipes của skill academic-docx-writer
(profile hvnh-assignment — Bài tập lớn/Tiểu luận môn học HVNH).
"""
import json
import sys
from pathlib import Path

import docx
from docx.shared import Cm, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

RECIPES_DIR = "/Users/dovandat/.gemini/config/skills/academic-docx-writer/references"
sys.path.insert(0, RECIPES_DIR)
from word_docx_recipes import (  # noqa: E402
    configure_academic_document, add_assignment_cover_page, apply_assignment_headers_footers,
    add_instructor_review_page, add_cam_doan_page, add_toc_field, add_abbreviation_table,
    add_exhibits_list, add_chapter_heading, add_section_heading, add_subsection_heading,
    add_body_paragraph, add_chapter_conclusion, add_numeric_citation, add_numbered_item,
    add_bullet_item, add_callout_box, add_figure_with_caption, style_academic_table,
    chapter_label, hvnh_book, hvnh_journal_article, validate_document,
    COLOR_NAVY_HVNH, COLOR_BLUE_SEC, COLOR_DARK_TEXT, CURRENT_PROFILE,
)

BASE_DIR = Path(__file__).resolve().parent
FIG_DIR = BASE_DIR / "figures"
with open(BASE_DIR / "pipeline_summary.json", encoding="utf-8") as f:
    S = json.load(f)

TEN_DE_TAI = "Tác động của Trí tuệ nhân tạo (AI) đến Việc làm năm 2030"
MON_HOC = "Phân tích Kinh doanh"
SINH_VIEN = "Đỗ Văn Đạt"
GVHD = "(Sinh viên bổ sung tên giảng viên hướng dẫn)"

doc = docx.Document()
configure_academic_document(doc, profile="hvnh-assignment")

# ===========================================================================
# SECTION 0 — FRONT MATTER
# ===========================================================================
add_assignment_cover_page(doc, ten_de_tai=TEN_DE_TAI, mon_hoc=MON_HOC,
                           giang_vien_hd=GVHD, sinh_vien_th=SINH_VIEN,
                           dia_diem_nam="HÀ NỘI – 2026")
add_instructor_review_page(doc)
add_cam_doan_page(doc, ho_ten=SINH_VIEN, ten_de_tai=TEN_DE_TAI)
add_toc_field(doc)

exhibits = [(f"2.{i+1}", cap, "") for i, cap in enumerate([
    "Phân bố số lượng nghề nghiệp theo Nhóm rủi ro tự động hoá 2030",
    "Phân bố Xác suất tự động hoá công việc vào năm 2030",
    "Mức lương trung bình theo Nhóm rủi ro tự động hoá",
    "Cơ cấu Nhóm rủi ro theo Trình độ học vấn",
    "Chỉ số Phơi nhiễm AI so với Xác suất tự động hoá 2030",
    "Ma trận tương quan giữa các biến định lượng chính",
    "Số năm kinh nghiệm và Xác suất tự động hoá 2030",
    "Xác suất tự động hoá trung bình theo Nghề nghiệp (20 nghề)",
    "Hệ số tăng trưởng công nghệ theo Nhóm rủi ro",
    "Điểm trung bình 10 nhóm kỹ năng theo Nhóm rủi ro",
    "Chỉ số Lợi thế con người theo Nhóm rủi ro",
])] + [(f"3.{i+1}", cap, "") for i, cap in enumerate([
    "Phương pháp Elbow và chỉ số Silhouette theo số cụm k",
    "Trực quan hoá 4 cụm hồ sơ kỹ năng qua PCA",
    "So sánh hiệu suất 3 mô hình phân loại Nhóm rủi ro tự động hoá",
    "Ma trận nhầm lẫn của 3 mô hình phân loại",
    "Mức độ quan trọng của biến (đã gộp Job_Title)",
    "Dự báo so với Thực tế — mô hình hồi quy tốt nhất",
])]
add_exhibits_list(doc, "DANH MỤC HÌNH VẼ", exhibits, label_prefix="Hình")

abbrevs = [
    ("AI", "Artificial Intelligence — Trí tuệ nhân tạo"),
    ("AUC", "Area Under the ROC Curve — Diện tích dưới đường cong ROC"),
    ("EDA", "Exploratory Data Analysis — Phân tích khám phá dữ liệu"),
    ("F1", "F1-Score — Điểm điều hoà giữa Precision và Recall"),
    ("IQR", "Interquartile Range — Khoảng tứ phân vị"),
    ("KNN/K-Means", "Thuật toán phân cụm K-Means"),
    ("MAE", "Mean Absolute Error — Sai số tuyệt đối trung bình"),
    ("PCA", "Principal Component Analysis — Phân tích thành phần chính"),
    ("R²", "Hệ số xác định (Coefficient of Determination)"),
    ("RMSE", "Root Mean Squared Error — Căn bậc hai sai số bình phương trung bình"),
    ("ROC", "Receiver Operating Characteristic"),
    ("XGBoost", "Extreme Gradient Boosting"),
]
add_abbreviation_table(doc, abbrevs)

# ===========================================================================
# SECTION 1 — BODY MATTER
# ===========================================================================
apply_assignment_headers_footers(doc, header_title=TEN_DE_TAI, start_value=1)

# ---------------------------------------------------------------------------
# MỞ ĐẦU
# ---------------------------------------------------------------------------
add_chapter_heading(doc, "MỞ ĐẦU", is_first_chapter=True)

add_section_heading(doc, "1. Lý do chọn đề tài")
add_body_paragraph(doc,
    "Trí tuệ nhân tạo (AI) đang mở rộng phạm vi ứng dụng từ các tác vụ lặp lại, thủ tục sang cả "
    "những công việc đòi hỏi phán đoán và tương tác phức tạp. Các tổ chức nghiên cứu quốc tế đưa "
    "ra những ước lượng khác nhau về tỷ lệ việc làm có nguy cơ bị tự động hoá trong 5-10 năm tới, "
    "và phần lớn đồng thuận rằng mức độ rủi ro không đồng đều giữa các nhóm nghề nghiệp. Đề tài "
    "lựa chọn phân tích một bộ dữ liệu mô phỏng gắn với chủ đề này nhằm rèn luyện quy trình phân "
    "tích kinh doanh trọn vẹn — từ tiền xử lý dữ liệu, phân tích khám phá, đến mô hình hoá dự báo "
    "— trên một bài toán có ý nghĩa thời sự.")

add_section_heading(doc, "2. Mục đích và phạm vi nghiên cứu")
add_body_paragraph(doc,
    "Mục đích của bài tập là vận dụng quy trình phân tích kinh doanh (tiền xử lý, EDA, phân cụm, "
    "phân loại, hồi quy) trên bộ dữ liệu mô phỏng "
    f"gồm {S['raw_shape'][0]} quan sát, {S['raw_shape'][1]} biến, mô tả đặc điểm của "
    f"{S['n_job_titles']} nghề nghiệp gắn với các chỉ số phơi nhiễm AI, xác suất và nhóm rủi ro "
    "tự động hoá năm 2030.")
add_body_paragraph(doc,
    "Phạm vi nghiên cứu giới hạn trong nội dung của bộ dữ liệu đã cho — một bộ dữ liệu tổng hợp "
    "(synthetic) phục vụ mục đích luyện tập kỹ thuật phân tích, không phải dữ liệu khảo sát thực "
    "địa. Do đó, các kết luận rút ra chỉ có giá trị nội tại đối với tập dữ liệu này; phần liên hệ "
    "với thực tiễn thị trường lao động được đối chiếu thận trọng với các nghiên cứu học thuật đã "
    "công bố (Chương 1) chứ không suy rộng trực tiếp từ kết quả thực nghiệm.")
add_body_paragraph(doc,
    "Phong cách trình bày quy trình phân tích (đọc dữ liệu, hiển thị các dòng đầu, tiền xử lý rồi "
    "mới đến EDA và mô hình hoá) có tham khảo cấu trúc notebook mẫu trên nền tảng Kaggle: "
    "Predicting Uber Ride Cancellations "
    "(https://www.kaggle.com/code/denvermagtibay/predicting-uber-ride-cancellations).")

add_section_heading(doc, "3. Kết cấu đề tài")
add_body_paragraph(doc, "Ngoài phần Mở đầu và Kết luận, nội dung báo cáo gồm 3 chương:", indent=True)
add_numbered_item(doc, "Chương 1.", "Cơ sở lý thuyết và tổng quan vấn đề",
                   "hệ thống hoá khái niệm AI/tự động hoá và các nghiên cứu quốc tế về tác động "
                   "của AI đến việc làm.")
add_numbered_item(doc, "Chương 2.", "Dữ liệu và phương pháp nghiên cứu",
                   "mô tả bộ dữ liệu, quy trình tiền xử lý, kết quả EDA và phương pháp mô hình hoá.")
add_numbered_item(doc, "Chương 3.", "Kết quả thực nghiệm và thảo luận",
                   "trình bày kết quả phân cụm, phân loại, hồi quy; thảo luận phát hiện chính và "
                   "hàm ý quản trị nhân sự.")

# ---------------------------------------------------------------------------
# CHƯƠNG 1
# ---------------------------------------------------------------------------
add_chapter_heading(doc, "CHƯƠNG 1. CƠ SỞ LÝ THUYẾT VÀ TỔNG QUAN VẤN ĐỀ")

add_section_heading(doc, "1.1. Trí tuệ nhân tạo và tự động hoá công việc")
add_body_paragraph(doc,
    "Trong kinh tế lao động, tự động hoá (automation) được hiểu là quá trình máy móc/phần mềm "
    "đảm nhiệm các tác vụ trước đây do con người thực hiện. AI hiện đại — đặc biệt các mô hình "
    "học máy và học sâu — mở rộng khả năng tự động hoá sang cả các tác vụ nhận thức (cognitive "
    "tasks) vốn được xem là khó thay thế trước đây, bên cạnh các tác vụ thủ tục (routine tasks) "
    "đã bị tự động hoá từ trước.")

add_section_heading(doc, "1.2. Cách tiếp cận theo tác vụ (Task-Based Approach)")
p = add_body_paragraph(doc,
    "Autor, Levy và Murnane phát triển khung phân tích trong đó rủi ro tự động hoá của một công "
    "việc phụ thuộc vào tỷ trọng các tác vụ thủ tục (routine) so với tác vụ phi thủ tục "
    "(non-routine) mà công việc đó đòi hỏi, chứ không phụ thuộc vào đặc điểm của cá nhân đảm "
    "nhiệm công việc ", indent=True, keep_with_next=False)
add_numeric_citation(p, [1])
add_body_paragraph(doc,
    "Hàm ý cốt lõi của khung phân tích này là: rủi ro tự động hoá được xác định ở cấp độ NGHỀ "
    "NGHIỆP (bản chất tác vụ), không phải ở cấp độ NGƯỜI LAO ĐỘNG cụ thể — hai người có kỹ năng, "
    "kinh nghiệm giống nhau nhưng làm hai nghề khác nhau có thể đối mặt mức rủi ro rất khác nhau. "
    "Đây chính là giả thuyết được kiểm định bằng thực nghiệm ở Chương 3 của báo cáo.")

add_section_heading(doc, "1.3. Các nghiên cứu thực nghiệm về rủi ro tự động hoá")
p = add_body_paragraph(doc,
    "Frey và Osborne ước lượng xác suất tự động hoá của 702 nghề nghiệp tại Hoa Kỳ dựa trên mức "
    "độ đòi hỏi về sáng tạo, đàm phán, và nhận thức xã hội, kết luận khoảng 47% việc làm có nguy "
    "cơ tự động hoá cao trong 1-2 thập kỷ tới ", indent=True)
add_numeric_citation(p, [2])
p = add_body_paragraph(doc,
    "Acemoglu và Restrepo mở rộng khung phân tích bằng mô hình \"displacement vs. reinstatement "
    "effect\", chỉ ra rằng tự động hoá vừa thay thế lao động ở một số tác vụ, vừa tạo ra tác vụ "
    "mới đòi hỏi lao động con người — tác động ròng phụ thuộc vào tốc độ tương đối của hai hiệu "
    "ứng này ", indent=True)
add_numeric_citation(p, [3])
p = add_body_paragraph(doc,
    "Ở cấp độ tổ chức quốc tế, McKinsey Global Institute ước lượng đến 375 triệu lao động toàn "
    "cầu có thể cần chuyển đổi nghề nghiệp do tự động hoá vào năm 2030 ", indent=True)
add_numeric_citation(p, [4])
p = add_body_paragraph(doc,
    "trong khi Diễn đàn Kinh tế Thế giới (WEF) công bố định kỳ Báo cáo Tương lai Việc làm "
    "(Future of Jobs Report), theo dõi biến động cơ cấu việc làm do AI và tự động hoá qua các "
    "vòng khảo sát doanh nghiệp toàn cầu ", indent=True)
add_numeric_citation(p, [5])
add_body_paragraph(doc,
    "Điểm chung của các nghiên cứu này là: (i) rủi ro tự động hoá phân bố KHÔNG ĐỒNG ĐỀU giữa "
    "các nhóm nghề, (ii) nghề có tỷ trọng tác vụ thủ tục/lặp lại cao (vận tải, bán lẻ, dịch vụ "
    "khách hàng cơ bản, xây dựng) có xu hướng rủi ro cao hơn nghề đòi hỏi phán đoán chuyên môn "
    "sâu, sáng tạo hoặc chăm sóc con người (y tế, giáo dục, nghiên cứu khoa học).")

add_callout_box(doc,
    "Khung phân tích áp dụng cho đề tài",
    "Dựa trên cách tiếp cận theo tác vụ (mục 1.2), Chương 2-3 của báo cáo sẽ kiểm định thực "
    "nghiệm giả thuyết: biến định danh NGHỀ NGHIỆP (Job_Title) giải thích rủi ro tự động hoá "
    "tốt hơn các biến ĐẶC ĐIỂM CÁ NHÂN (kỹ năng, kinh nghiệm, học vấn, lương) trên bộ dữ liệu "
    "thực nghiệm của bài tập.")

add_chapter_conclusion(doc, 1,
    "Chương 1 hệ thống hoá khung lý thuyết tiếp cận theo tác vụ (task-based approach) và các "
    "nghiên cứu thực nghiệm quốc tế về tác động của AI đến việc làm, làm cơ sở đối chiếu cho kết "
    "quả thực nghiệm ở Chương 3. Điểm mấu chốt được kế thừa là: rủi ro tự động hoá gắn với bản "
    "chất tác vụ của nghề nghiệp hơn là đặc điểm cá nhân người lao động — giả thuyết này sẽ được "
    "kiểm định trực tiếp trên dữ liệu thực nghiệm của bài tập ở Chương 3.")

# ---------------------------------------------------------------------------
# CHƯƠNG 2
# ---------------------------------------------------------------------------
add_chapter_heading(doc, "CHƯƠNG 2. DỮ LIỆU VÀ PHƯƠNG PHÁP NGHIÊN CỨU")

add_section_heading(doc, "2.1. Mô tả dữ liệu")
add_body_paragraph(doc,
    f"Bộ dữ liệu {S['raw_shape'][0]:,} quan sát x {S['raw_shape'][1]} biến mô tả đặc điểm của "
    f"{S['n_job_titles']} nghề nghiệp phổ biến, gồm 3 nhóm biến: (i) đặc điểm nhân khẩu học/nghề "
    "nghiệp (Job_Title, Average_Salary, Years_Experience, Education_Level); (ii) chỉ số công "
    "nghệ (AI_Exposure_Index, Tech_Growth_Factor); (iii) 10 điểm kỹ năng chuẩn hoá (Skill_1 đến "
    "Skill_10) và biến mục tiêu (Automation_Probability_2030, Risk_Category).")

tbl_desc_rows = [
    ("Job_Title", "Định danh", "Tên 20 nghề nghiệp khảo sát"),
    ("Average_Salary", "Định lượng", "Lương trung bình (USD/năm)"),
    ("Years_Experience", "Định lượng", "Số năm kinh nghiệm"),
    ("Education_Level", "Định tính thứ bậc", "High School / Bachelor's / Master's / PhD"),
    ("AI_Exposure_Index", "Định lượng [0,1]", "Chỉ số mức độ phơi nhiễm với công nghệ AI"),
    ("Tech_Growth_Factor", "Định lượng", "Hệ số tăng trưởng công nghệ của ngành nghề"),
    ("Automation_Probability_2030", "Định lượng [0,1]", "Xác suất tự động hoá dự kiến năm 2030 (biến mục tiêu)"),
    ("Risk_Category", "Định tính (Low/Medium/High)", "Nhóm rủi ro tự động hoá (biến mục tiêu)"),
    ("Skill_1 … Skill_10", "Định lượng [0,1] (x10)", "Điểm chuẩn hoá của 10 nhóm kỹ năng nghề nghiệp"),
]
t = doc.add_table(rows=len(tbl_desc_rows) + 1, cols=3)
t.rows[0].cells[0].paragraphs[0].add_run("Biến")
t.rows[0].cells[1].paragraphs[0].add_run("Loại biến")
t.rows[0].cells[2].paragraphs[0].add_run("Diễn giải")
for i, (a, b, c) in enumerate(tbl_desc_rows, start=1):
    t.rows[i].cells[0].paragraphs[0].add_run(a)
    t.rows[i].cells[1].paragraphs[0].add_run(b)
    t.rows[i].cells[2].paragraphs[0].add_run(c)
style_academic_table(doc, t, chapter_label(2, 1), "Mô tả các biến trong bộ dữ liệu")

add_section_heading(doc, "2.2. Quy trình tiền xử lý dữ liệu")
add_body_paragraph(doc,
    "Quy trình tiền xử lý gồm 6 bước: (1) kiểm tra dữ liệu thiếu; (2) loại dòng trùng lặp; "
    "(3) kiểm tra miền giá trị hợp lệ [0,1] của các chỉ số chuẩn hoá; (4) phát hiện ngoại lai "
    "bằng quy tắc IQR trên biến lương; (5) kiểm tra rò rỉ dữ liệu (data leakage) giữa "
    "Risk_Category và Automation_Probability_2030; (6) tạo 7 biến đặc trưng mới phục vụ mô hình "
    "hoá.")

tbl_prep_rows = [
    ("Dữ liệu thiếu", f"{S['n_missing_cells_total']} ô — không phát hiện dữ liệu thiếu"),
    ("Dữ liệu trùng lặp", f"{S['n_duplicates_removed']} dòng bị loại"),
    ("Vi phạm miền giá trị [0,1]", f"{S['n_invalid_range_rows_removed']} dòng bị loại"),
    ("Ngoại lai IQR (Average_Salary)",
     f"Q1={S['salary_iqr']['Q1']:,.0f}, Q3={S['salary_iqr']['Q3']:,.0f}, "
     f"cận trên={S['salary_iqr']['upper_bound']:,.0f} — {S['salary_iqr']['n_outliers']} hồ sơ ngoại lai (giữ nguyên)"),
    ("Rò rỉ dữ liệu (leakage)",
     "Risk_Category = hàm ngưỡng cố định của Automation_Probability_2030 "
     "(Low 0,05-0,30; Medium 0,31-0,70; High 0,71-0,95) → loại biến này khỏi tập đặc trưng phân loại"),
    ("Biến mới tạo thêm", f"{S['n_engineered_features']} biến (Skill_Diversity_Score, Skill_Std, "
     "High_Value_Skill_Count, Experience_Group, Salary_per_YearExp, Human_Edge_Score, Education_Level_Encoded)"),
    ("Kích thước dữ liệu sạch", f"{S['clean_shape'][0]:,} dòng x {S['clean_shape'][1]} cột"),
]
t2 = doc.add_table(rows=len(tbl_prep_rows) + 1, cols=2)
t2.rows[0].cells[0].paragraphs[0].add_run("Bước / Kiểm tra")
t2.rows[0].cells[1].paragraphs[0].add_run("Kết quả")
for i, (a, b) in enumerate(tbl_prep_rows, start=1):
    t2.rows[i].cells[0].paragraphs[0].add_run(a)
    t2.rows[i].cells[1].paragraphs[0].add_run(b)
style_academic_table(doc, t2, chapter_label(2, 2), "Tóm tắt kết quả tiền xử lý dữ liệu")

add_section_heading(doc, "2.3. Phân tích khám phá dữ liệu (EDA)")
add_body_paragraph(doc,
    "Mục này trình bày 11 biểu đồ khám phá dữ liệu, đi từ phân bố các biến đơn lẻ đến mối quan hệ "
    "hai biến, nhằm xác định biến nào thực sự mang thông tin phân biệt nhóm rủi ro tự động hoá.")

eda_figs = [
    ("01_risk_category_distribution.png", "Phân bố số lượng nghề nghiệp theo Nhóm rủi ro tự động hoá 2030",
     "Nhóm Medium chiếm đa số (50,7%); hai nhóm Low và High gần cân bằng (~24,6-24,7%)."),
    ("02_automation_probability_distribution.png", "Phân bố Xác suất tự động hoá công việc vào năm 2030",
     "Phân bố có 3 cụm mật độ tách biệt, gợi ý một yếu tố phân loại tiềm ẩn chi phối biến mục tiêu."),
    ("03_salary_by_risk_category.png", "Mức lương trung bình theo Nhóm rủi ro tự động hoá",
     "Trung vị và độ trải của lương gần như giống nhau ở cả 3 nhóm — lương không phân biệt được nhóm rủi ro."),
    ("04_education_vs_risk.png", "Cơ cấu Nhóm rủi ro theo Trình độ học vấn (%)",
     "Cơ cấu rủi ro gần như đồng nhất giữa 4 nhóm học vấn — học vấn cũng không phải yếu tố phân biệt."),
    ("05_ai_exposure_vs_automation.png", "Chỉ số Phơi nhiễm AI so với Xác suất tự động hoá 2030",
     "Không quan sát được xu hướng tuyến tính — AI_Exposure_Index không tương quan với biến mục tiêu."),
    ("06_correlation_heatmap.png", "Ma trận tương quan giữa các biến định lượng chính",
     "Toàn bộ hệ số tương quan với Automation_Probability_2030 đều xấp xỉ 0 (|r| < 0,05)."),
    ("07_experience_vs_automation.png", "Số năm kinh nghiệm và Xác suất tự động hoá 2030",
     "Đường hồi quy gần như phẳng — kinh nghiệm làm việc không giải thích được rủi ro tự động hoá."),
    ("08_jobtitle_automation_ranked.png", "Xác suất tự động hoá trung bình theo Nghề nghiệp (20 nghề)",
     f"20 nghề tách thành 3 tầng rõ rệt; kiểm định eta² cho thấy Job_Title giải thích "
     f"{S['job_title_eta_squared']*100:.1f}% phương sai của biến mục tiêu — bằng chứng then chốt của báo cáo."),
    ("09_tech_growth_by_risk.png", "Hệ số tăng trưởng công nghệ (Tech_Growth_Factor) theo Nhóm rủi ro",
     "Phân bố Tech_Growth_Factor tương tự nhau giữa 3 nhóm rủi ro."),
    ("10_skills_heatmap_by_risk.png", "Điểm trung bình 10 nhóm kỹ năng theo Nhóm rủi ro",
     "Điểm kỹ năng trung bình dao động rất hẹp quanh 0,49-0,51 ở mọi ô — không có nhóm kỹ năng nào nổi bật theo rủi ro."),
    ("11_human_edge_score_by_risk.png", "Chỉ số Lợi thế con người (Human_Edge_Score) theo Nhóm rủi ro",
     "Chỉ số tổng hợp tự xây dựng cũng không phân biệt được 3 nhóm rủi ro, nhất quán với các biến thành phần."),
]
for i, (fname, cap, note) in enumerate(eda_figs, start=1):
    add_figure_with_caption(doc, str(FIG_DIR / fname), chapter_label(2, i), cap)
    add_body_paragraph(doc, f"Nhận xét: {note}")

add_section_heading(doc, "2.4. Phương pháp mô hình hoá")
add_subsection_heading(doc, "2.4.1. Phân cụm K-Means")
add_body_paragraph(doc,
    "Áp dụng K-Means trên 12 biến (10 điểm kỹ năng + AI_Exposure_Index + Tech_Growth_Factor) sau "
    "chuẩn hoá StandardScaler, thử nghiệm k từ 2 đến 8, chọn k theo phương pháp Elbow kết hợp chỉ "
    "số Silhouette, trực quan hoá bằng PCA 2 thành phần.")
add_subsection_heading(doc, "2.4.2. Mô hình phân loại Risk_Category")
add_body_paragraph(doc,
    "So sánh 3 mô hình: Logistic Regression, Random Forest, XGBoost Classifier trên tập đặc "
    "trưng gồm các biến cá nhân/kỹ năng VÀ biến Job_Title (mã hoá one-hot, drop_first=True) — "
    "loại trừ Automation_Probability_2030 để tránh rò rỉ dữ liệu (mục 2.2). Dữ liệu chia "
    "train/test theo tỷ lệ 75/25, phân tầng (stratify) theo Risk_Category. Đánh giá bằng "
    "Accuracy, Precision/Recall/F1-macro và ROC-AUC (One-vs-Rest).")
add_subsection_heading(doc, "2.4.3. Mô hình hồi quy Automation_Probability_2030")
add_body_paragraph(doc,
    "Sử dụng cùng tập đặc trưng của mục 2.4.2 để hồi quy trực tiếp biến liên tục "
    "Automation_Probability_2030 bằng 3 mô hình: Linear Regression, Random Forest Regressor, "
    "XGBoost Regressor — như một kênh kiểm chứng độc lập cho kết quả phân loại, đánh giá bằng "
    "R², MAE, RMSE.")

add_chapter_conclusion(doc, 2,
    f"Chương 2 mô tả bộ dữ liệu {S['clean_shape'][0]:,} quan sát sau tiền xử lý và trình bày 11 "
    "biểu đồ EDA. Phát hiện xuyên suốt Chương 2 là: các biến đặc điểm cá nhân/kỹ năng (lương, "
    "kinh nghiệm, học vấn, chỉ số phơi nhiễm AI, điểm kỹ năng) đều KHÔNG cho thấy mối liên hệ rõ "
    "ràng với nhóm rủi ro tự động hoá, trong khi biến định danh Job_Title bộc lộ cấu trúc 3 tầng "
    "rất rõ rệt (Hình 2.8). Phát hiện này định hướng trực tiếp chiến lược mô hình hoá ở mục 2.4 "
    "và sẽ được kiểm định định lượng ở Chương 3.")

# ---------------------------------------------------------------------------
# CHƯƠNG 3
# ---------------------------------------------------------------------------
add_chapter_heading(doc, "CHƯƠNG 3. KẾT QUẢ THỰC NGHIỆM VÀ THẢO LUẬN")

add_section_heading(doc, "3.1. Kết quả phân cụm hồ sơ kỹ năng")
add_figure_with_caption(doc, str(FIG_DIR / "12_kmeans_elbow_silhouette.png"), chapter_label(3, 1),
                         "Phương pháp Elbow và chỉ số Silhouette theo số cụm k")
add_body_paragraph(doc,
    f"{S['clustering_caveat']}")
add_figure_with_caption(doc, str(FIG_DIR / "13_kmeans_clusters_pca.png"), chapter_label(3, 2),
                         "Trực quan hoá 4 cụm hồ sơ kỹ năng qua PCA (2 thành phần)")

cluster_rows = S["cluster_profile"]
t3 = doc.add_table(rows=len(cluster_rows) + 1, cols=6)
headers = ["Cụm", "Số lượng", "Xác suất tự động hoá trung bình", "Chỉ số phơi nhiễm AI trung bình",
           "Lương trung bình (USD)", "Số năm kinh nghiệm trung bình"]
for j, h in enumerate(headers):
    t3.rows[0].cells[j].paragraphs[0].add_run(h)
for i, row in enumerate(cluster_rows, start=1):
    vals = [str(row["Cluster"]), str(row["So_luong"]), f"{row['XacSuat_TuDongHoa_TB']:.3f}",
            f"{row['AI_Exposure_TB']:.3f}", f"{row['Luong_TB']:,.0f}", f"{row['KinhNghiem_TB']:.2f}"]
    for j, v in enumerate(vals):
        t3.rows[i].cells[j].paragraphs[0].add_run(v)
style_academic_table(doc, t3, chapter_label(3, 1), "Hồ sơ đặc trưng của 4 cụm phân khúc kỹ năng")
add_body_paragraph(doc,
    "Nhận xét: chỉ số Xác suất tự động hoá trung bình gần như bằng nhau giữa 4 cụm (dao động "
    "0,49-0,52) — xác nhận định lượng cho kết luận ở Hình 3.1: phân cụm trên hồ sơ kỹ năng KHÔNG "
    "tách được nhóm rủi ro cao/thấp. Tên gọi 4 cụm (Phụ lục — pipeline_summary.json) chỉ mang "
    "tính mô tả xếp hạng theo AI_Exposure_TB, không phản ánh cấu trúc phân cụm mạnh.")

add_section_heading(doc, "3.2. Kết quả mô hình phân loại Risk_Category")
cm = S["classification_model_metrics"]
t4 = doc.add_table(rows=len(cm) + 1, cols=6)
headers4 = ["Mô hình", "Accuracy", "Precision (macro)", "Recall (macro)", "F1 (macro)", "ROC-AUC (OvR)"]
for j, h in enumerate(headers4):
    t4.rows[0].cells[j].paragraphs[0].add_run(h)
for i, (name, m) in enumerate(cm.items(), start=1):
    vals = [name, f"{m['Accuracy']:.4f}", f"{m['Precision_macro']:.4f}", f"{m['Recall_macro']:.4f}",
            f"{m['F1_macro']:.4f}", f"{m['ROC_AUC_ovr']:.4f}"]
    for j, v in enumerate(vals):
        t4.rows[i].cells[j].paragraphs[0].add_run(v)
style_academic_table(doc, t4, chapter_label(3, 2), "So sánh hiệu suất 3 mô hình phân loại Nhóm rủi ro")
add_figure_with_caption(doc, str(FIG_DIR / "14_ml_model_comparison.png"), chapter_label(3, 3),
                         "So sánh hiệu suất 3 mô hình phân loại Nhóm rủi ro tự động hoá")
add_figure_with_caption(doc, str(FIG_DIR / "15_confusion_matrices.png"), chapter_label(3, 4),
                         "Ma trận nhầm lẫn của 3 mô hình phân loại")
add_body_paragraph(doc,
    f"Nhận xét: khi đưa Job_Title vào tập đặc trưng, F1-macro đạt "
    f"{max(m['F1_macro'] for m in cm.values()):.3f} và ROC-AUC đạt "
    f"{max(m['ROC_AUC_ovr'] for m in cm.values()):.3f} — vượt trội hoàn toàn so với thử nghiệm "
    "chỉ dùng đặc trưng cá nhân (F1-macro ~0,22-0,34, AUC ~0,50, xem Phụ lục pipeline_summary.json). "
    "Ma trận nhầm lẫn (Hình 3.4) cho thấy nhầm lẫn hầu như chỉ xảy ra giữa Medium và High — hợp lý "
    "vì đây là hai khoảng ngưỡng liền kề của biến gốc; không có nhầm lẫn giữa Low và High.")
add_figure_with_caption(doc, str(FIG_DIR / "16_feature_importance.png"), chapter_label(3, 5),
                         "Mức độ quan trọng của biến — XGBoost Classifier (đã gộp Job_Title)")
add_body_paragraph(doc,
    f"Nhận xét: nhóm biến giả Job_Title (gộp 19 biến) chiếm tới "
    f"{S['job_title_total_importance']*100:.1f}% tổng mức độ quan trọng của mô hình XGBoost — xác "
    "nhận định lượng cho giả thuyết task-based approach nêu ở mục 1.2: nghề nghiệp quyết định "
    "rủi ro tự động hoá, không phải đặc điểm cá nhân.")

add_section_heading(doc, "3.3. Kết quả mô hình hồi quy Automation_Probability_2030")
rm = S["regression_model_metrics"]
t5 = doc.add_table(rows=len(rm) + 1, cols=4)
headers5 = ["Mô hình", "R²", "MAE", "RMSE"]
for j, h in enumerate(headers5):
    t5.rows[0].cells[j].paragraphs[0].add_run(h)
for i, (name, m) in enumerate(rm.items(), start=1):
    vals = [name, f"{m['R2']:.4f}", f"{m['MAE']:.4f}", f"{m['RMSE']:.4f}"]
    for j, v in enumerate(vals):
        t5.rows[i].cells[j].paragraphs[0].add_run(v)
style_academic_table(doc, t5, chapter_label(3, 3), "So sánh hiệu suất 3 mô hình hồi quy")
add_figure_with_caption(doc, str(FIG_DIR / "17_regression_pred_vs_actual.png"), chapter_label(3, 6),
                         f"Dự báo so với Thực tế — {S['best_regression_model']} "
                         f"(R²={rm[S['best_regression_model']]['R2']:.3f})")
add_body_paragraph(doc,
    f"Nhận xét: mô hình hồi quy tốt nhất ({S['best_regression_model']}) đạt "
    f"R²={rm[S['best_regression_model']]['R2']:.3f}, MAE="
    f"{rm[S['best_regression_model']]['MAE']:.3f} — nhất quán với kết quả phân loại ở mục 3.2, "
    "củng cố thêm bằng một kênh đánh giá độc lập (hồi quy trên biến liên tục thay vì phân loại "
    "trên biến rời rạc).")

add_section_heading(doc, "3.4. Hàm ý quản trị nhân sự")
add_bullet_item(doc, "Thiết kế đào tạo lại theo nhóm nghề:",
                 "vì rủi ro gắn với bản chất công việc hơn hồ sơ cá nhân, chương trình reskilling "
                 "nên ưu tiên theo NHÓM NGHỀ NGHIỆP (occupation-level) thay vì chỉ đánh giá năng "
                 "lực cá nhân từng người lao động.")
add_bullet_item(doc, "Ưu tiên nhóm nghề tầng cao:",
                 "các nghề có tỷ trọng tác vụ lặp lại/thủ tục cao (ví dụ nhóm Retail Worker, "
                 "Security Guard, Construction Worker, Customer Support, Truck Driver trong dữ "
                 "liệu) cần được đưa vào lộ trình chuyển đổi nghề nghiệp sớm hơn.")
add_bullet_item(doc, "Không dùng hồ sơ kỹ năng đơn lẻ để xếp hạng rủi ro:",
                 "kết quả phân cụm (mục 3.1) cho thấy hồ sơ kỹ năng cá nhân không đủ để phân "
                 "biệt mức độ rủi ro — cần kết hợp thông tin nghề nghiệp/ngành nghề khi xây dựng "
                 "công cụ đánh giá rủi ro nội bộ doanh nghiệp.")

add_section_heading(doc, "3.5. Hạn chế của nghiên cứu")
add_body_paragraph(doc,
    "Thứ nhất, dữ liệu sử dụng là bộ dữ liệu MÔ PHỎNG (synthetic) phục vụ mục đích luyện tập kỹ "
    "thuật phân tích — bản thân Automation_Probability_2030 được gán theo quy tắc gắn với "
    "Job_Title, nên phát hiện \"nghề nghiệp quyết định, đặc điểm cá nhân không quyết định\" chỉ "
    "có giá trị NỘI TẠI đối với tập dữ liệu này, không thể suy rộng trực tiếp thành quy luật của "
    "thị trường lao động thực tế.")
add_body_paragraph(doc,
    "Thứ hai, dữ liệu không có chiều thời gian (chỉ một lát cắt tĩnh năm 2030), không có biến "
    "ngành/vùng địa lý cụ thể, nên không thể phân tích động thái thay đổi rủi ro theo thời gian "
    "hay khác biệt vùng miền như các nghiên cứu WEF/McKinsey thực hiện trên dữ liệu khảo sát "
    "thực tế.")
add_body_paragraph(doc,
    "Thứ ba, kết quả mô hình hoá xuất sắc (F1-macro, AUC gần tuyệt đối khi có Job_Title) phản ánh "
    "cơ chế SINH DỮ LIỆU có kiểm soát của bộ dữ liệu, không nên diễn giải như bằng chứng cho thấy "
    "rủi ro tự động hoá trong thực tế có thể dự báo chính xác đến mức độ tương tự — đây là điểm "
    "cần lưu ý để tránh khẳng định vượt quá mức độ mà thiết kế nghiên cứu cho phép (Epistemic "
    "Precision).")

add_chapter_conclusion(doc, 3,
    "Chương 3 kiểm định thực nghiệm giả thuyết nêu ở Chương 1: đưa Job_Title vào mô hình nâng "
    f"hiệu suất phân loại từ mức xấp xỉ ngẫu nhiên lên F1-macro ~"
    f"{max(m['F1_macro'] for m in cm.values()):.2f}, xác nhận rủi ro tự động hoá trong bộ dữ "
    "liệu được quyết định ở cấp độ nghề nghiệp. Phân cụm không giám sát trên hồ sơ kỹ năng không "
    "phát hiện được cấu trúc phân nhóm có ý nghĩa, cho thấy giá trị vượt trội của việc đưa thông "
    "tin nghề nghiệp vào mô hình có giám sát. Kết quả được diễn giải thận trọng trong phạm vi "
    "giới hạn của một bộ dữ liệu mô phỏng (mục 3.5).")

# ---------------------------------------------------------------------------
# KẾT LUẬN
# ---------------------------------------------------------------------------
add_chapter_heading(doc, "KẾT LUẬN")
add_body_paragraph(doc,
    "Báo cáo đã thực hiện trọn vẹn quy trình phân tích kinh doanh trên bộ dữ liệu mô phỏng về tác "
    "động của AI đến việc làm năm 2030: tiền xử lý dữ liệu (phát hiện và xử lý rủi ro rò rỉ dữ "
    "liệu giữa Risk_Category và Automation_Probability_2030), phân tích khám phá dữ liệu (11 "
    "biểu đồ), phân cụm K-Means, và hai kênh mô hình hoá dự báo độc lập (phân loại và hồi quy).")
add_body_paragraph(doc,
    "Phát hiện xuyên suốt là: các đặc trưng cá nhân của người lao động (kỹ năng, kinh nghiệm, học "
    "vấn, lương, chỉ số phơi nhiễm AI cá nhân) không mang thông tin dự báo rủi ro tự động hoá "
    "trong bộ dữ liệu này, trong khi biến định danh nghề nghiệp (Job_Title) giải thích khoảng "
    f"{S['job_title_eta_squared']*100:.0f}% phương sai của biến mục tiêu và khi đưa vào mô hình "
    f"giúp F1-macro đạt tới {max(m['F1_macro'] for m in cm.values()):.2f}. Phát hiện này nhất "
    "quán về mặt định tính với khung lý thuyết tiếp cận theo tác vụ (Autor, Levy & Murnane, 2003) "
    "và các nghiên cứu thực nghiệm của Frey & Osborne (2017): rủi ro tự động hoá gắn với bản "
    "chất công việc hơn là đặc điểm của người đảm nhiệm công việc đó.")
add_body_paragraph(doc,
    "Trong phạm vi một bộ dữ liệu mô phỏng phục vụ mục đích luyện tập, kết luận trên cần được "
    "hiểu như một minh hoạ phương pháp luận — kiểm định một giả thuyết học thuật đã có trên một "
    "tình huống dữ liệu cụ thể — hơn là một khẳng định tổng quát về thị trường lao động thực tế. "
    "Hướng phát triển tiếp theo có thể bổ sung chiều thời gian, dữ liệu ngành/vùng địa lý thực tế "
    "và đối chiếu trực tiếp với các bộ chỉ số công khai (O*NET Task Ratings, WEF Future of Jobs "
    "Survey) để tăng giá trị ứng dụng thực tiễn của phân tích.")

# ---------------------------------------------------------------------------
# TÀI LIỆU THAM KHẢO (chỉ gồm nguồn có thể kiểm chứng, tránh trích dẫn suy diễn)
# ---------------------------------------------------------------------------
doc.add_page_break()
p_h = doc.add_paragraph("TÀI LIỆU THAM KHẢO", style='Heading 1')
p_h.paragraph_format.space_before = Pt(16)
p_h.paragraph_format.first_line_indent = Cm(0)

_ref_n = {"n": 0}
def _ref_entry(segments):
    _ref_n["n"] += 1
    p = doc.add_paragraph()
    p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.left_indent = Cm(1.0)
    p.paragraph_format.first_line_indent = Cm(-1.0)
    p.paragraph_format.line_spacing = CURRENT_PROFILE["line_spacing"]
    p.paragraph_format.space_after = Pt(6)
    r_num = p.add_run(f"{_ref_n['n']}. ")
    r_num.font.name = 'Times New Roman'; r_num.font.size = Pt(13)
    for txt, italic in segments:
        r = p.add_run(txt)
        r.italic = italic
        r.font.name = 'Times New Roman'; r.font.size = Pt(13)
        r.font.color.rgb = COLOR_DARK_TEXT
    return p

references = [
    hvnh_journal_article("Autor, D. H., Levy, F., & Murnane, R. J.", 2003,
        "The Skill Content of Recent Technological Change: An Empirical Exploration",
        "The Quarterly Journal of Economics", 118, 4, "1279–1333", english=True),
    hvnh_journal_article("Frey, C. B., & Osborne, M. A.", 2017,
        "The Future of Employment: How Susceptible Are Jobs to Computerisation?",
        "Technological Forecasting and Social Change", 114, "-", "254–280", english=True),
    hvnh_journal_article("Acemoglu, D., & Restrepo, P.", 2019,
        "Automation and New Tasks: How Technology Displaces and Reinstates Labor",
        "Journal of Economic Perspectives", 33, 2, "3–30", english=True),
    hvnh_book("McKinsey Global Institute", 2017,
        "Jobs Lost, Jobs Gained: Workforce Transitions in a Time of Automation",
        "McKinsey & Company", "Washington, D.C."),
    hvnh_book("World Economic Forum", 2023,
        "Future of Jobs Report 2023", "World Economic Forum", "Geneva"),
    [("Magtibay, D. (2024), ", False), ("Predicting Uber Ride Cancellations", True),
     (", Kaggle Notebook — tham khảo phong cách trình bày quy trình notebook "
      "(đọc dữ liệu → EDA → tiền xử lý → mô hình hoá). Truy cập tại: "
      "https://www.kaggle.com/code/denvermagtibay/predicting-uber-ride-cancellations.", False)],
]
for seg in references:
    _ref_entry(seg)

# ===========================================================================
# VALIDATE & SAVE
# ===========================================================================
ok = validate_document(doc, min_heading1=5)
out_path = BASE_DIR / "Bao_Cao_Cuoi_Ky_TacDongAI_ViecLam2030.docx"
doc.save(out_path)
print(f"\nĐã lưu báo cáo: {out_path.name} ({'OK' if ok else 'CÓ CẢNH BÁO — xem log ở trên'})")
