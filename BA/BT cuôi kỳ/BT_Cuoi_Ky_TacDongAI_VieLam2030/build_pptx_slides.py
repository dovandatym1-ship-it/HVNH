"""
Dựng slide thuyết trình (.pptx) chuẩn EasySlides cho đồ án:
"Tác động của Trí tuệ nhân tạo (AI) đến Việc làm năm 2030"

18 slide, kiến trúc McKinsey Pyramid Principle (Answer First), Action Titles,
Speaker Notes 80-150 từ/slide, 16:9 Widescreen.
"""
import json
import sys
from pathlib import Path

RECIPES_DIR = "/Users/dovandat/.gemini/config/skills/academic-slide-writer/references"
sys.path.insert(0, RECIPES_DIR)

from pptx.util import Inches, Pt  # noqa: E402
from pptx.enum.text import PP_ALIGN  # noqa: E402
from presentation_pptx_recipes import (  # noqa: E402
    create_executive_deck, add_blank_slide, add_action_header, add_card_box,
    add_metric_card, add_chart_deep_dive_60_40, add_process_pipeline_4,
    add_persona_profile_cards, add_model_comparison_cards, add_strategic_tier_matrix,
    add_speaker_notes, validate_deck,
    C_HVNH_NAVY, C_HVNH_ORANGE, C_HVNH_GOLD, C_BLUE_CYAN, C_ACCENT_RED, C_ACCENT_GREEN,
    C_CANVAS_BG, C_CARD_BG, C_CARD_BORDER, C_TEXT_DARK, C_TEXT_MUTED, C_WHITE,
    FONT_PRIMARY, FONT_TITLE,
)

BASE_DIR = Path(__file__).resolve().parent
FIG_DIR = BASE_DIR / "figures"
with open(BASE_DIR / "pipeline_summary.json", encoding="utf-8") as f:
    S = json.load(f)

TOTAL_SLIDES = 18
TEN_DE_TAI = "Tác động của Trí tuệ nhân tạo (AI) đến Việc làm năm 2030"


def add_bullets_box(slide, left, top, width, height, bullets, font_size=14, title=None):
    """Textbox gạch đầu dòng đơn giản dùng cho các slide nội dung dạng văn bản."""
    tb = slide.shapes.add_textbox(left, top, width, height)
    tf = tb.text_frame
    tf.word_wrap = True
    first = True
    if title:
        p = tf.paragraphs[0]
        r = p.add_run()
        r.text = title
        r.font.name = FONT_TITLE
        r.font.size = Pt(font_size + 2)
        r.font.bold = True
        r.font.color.rgb = C_HVNH_NAVY
        first = False
    for b in bullets:
        p = tf.paragraphs[0] if first else tf.add_paragraph()
        first = False
        p.space_before = Pt(10)
        lead, _, rest = b.partition("::")
        if rest:
            r1 = p.add_run()
            r1.text = f"•  {lead.strip()}: "
            r1.font.bold = True
            r1.font.name = FONT_PRIMARY
            r1.font.size = Pt(font_size)
            r1.font.color.rgb = C_HVNH_ORANGE
            r2 = p.add_run()
            r2.text = rest.strip()
            r2.font.name = FONT_PRIMARY
            r2.font.size = Pt(font_size)
            r2.font.color.rgb = C_TEXT_DARK
        else:
            r = p.add_run()
            r.text = f"•  {b}"
            r.font.name = FONT_PRIMARY
            r.font.size = Pt(font_size)
            r.font.color.rgb = C_TEXT_DARK
    return tb


prs = create_executive_deck()

# ===========================================================================
# SLIDE 1 — COVER
# ===========================================================================
s1 = add_blank_slide(prs, bg_color=C_HVNH_NAVY)
band = s1.shapes.add_shape(1, Inches(0), Inches(3.15), prs.slide_width, Inches(0.05))
band.fill.solid(); band.fill.fore_color.rgb = C_HVNH_ORANGE; band.line.fill.background()

tb = s1.shapes.add_textbox(Inches(0.9), Inches(1.0), Inches(11.5), Inches(0.5))
p = tb.text_frame.paragraphs[0]
r = p.add_run(); r.text = "HỌC VIỆN NGÂN HÀNG  ·  HỌC PHẦN PHÂN TÍCH KINH DOANH"
r.font.name = FONT_PRIMARY; r.font.size = Pt(14); r.font.bold = True; r.font.color.rgb = C_HVNH_GOLD

tb2 = s1.shapes.add_textbox(Inches(0.9), Inches(1.7), Inches(11.5), Inches(1.4))
tf2 = tb2.text_frame; tf2.word_wrap = True
p2 = tf2.paragraphs[0]
r2 = p2.add_run(); r2.text = TEN_DE_TAI
r2.font.name = FONT_TITLE; r2.font.size = Pt(34); r2.font.bold = True; r2.font.color.rgb = C_WHITE

tb3 = s1.shapes.add_textbox(Inches(0.9), Inches(3.45), Inches(11.5), Inches(0.6))
p3 = tb3.text_frame.paragraphs[0]
r3 = p3.add_run(); r3.text = "Bài tập cuối kỳ — Phân tích dữ liệu và mô hình hoá dự báo"
r3.font.name = FONT_PRIMARY; r3.font.size = Pt(16); r3.font.italic = True; r3.font.color.rgb = C_CARD_BORDER

tb4 = s1.shapes.add_textbox(Inches(0.9), Inches(6.3), Inches(11.5), Inches(0.8))
tf4 = tb4.text_frame
p4 = tf4.paragraphs[0]
r4 = p4.add_run(); r4.text = "Sinh viên thực hiện: Đỗ Văn Đạt"
r4.font.name = FONT_PRIMARY; r4.font.size = Pt(13); r4.font.color.rgb = C_WHITE
p4b = tf4.add_paragraph()
r4b = p4b.add_run(); r4b.text = "Năm học 2025 – 2026"
r4b.font.name = FONT_PRIMARY; r4b.font.size = Pt(12); r4b.font.color.rgb = C_TEXT_MUTED
add_speaker_notes(s1,
    "Kính chào Hội đồng. Em xin trình bày đồ án cuối kỳ học phần Phân tích Kinh doanh với đề tài "
    "Tác động của Trí tuệ nhân tạo đến Việc làm năm 2030. Bài trình bày gồm ba phần chính: bối "
    "cảnh và cơ sở lý thuyết, phương pháp phân tích dữ liệu, và kết quả thực nghiệm cùng hàm ý "
    "quản trị nhân sự. Toàn bộ phân tích được thực hiện trên bộ dữ liệu mô phỏng 3.000 quan sát "
    "gắn với 20 nghề nghiệp, sử dụng quy trình tiền xử lý, phân tích khám phá dữ liệu, phân cụm "
    "và hai mô hình dự báo độc lập.")

# ===========================================================================
# SLIDE 2 — EXECUTIVE ABSTRACT
# ===========================================================================
s2 = add_blank_slide(prs)
add_action_header(s2, "TÓM TẮT ĐIỀU HÀNH",
                   "Nghề nghiệp Quyết định 85,7% Rủi ro Tự động hoá — Đặc điểm Cá nhân Gần như Vô nghĩa",
                   page_num=2, total_pages=TOTAL_SLIDES)
metrics2 = [
    (f"{S['job_title_eta_squared']*100:.1f}%", "Phương sai được giải thích bởi Job_Title (eta²)",
     ["So với ~0% của mọi biến cá nhân", "Kiểm định ANOVA trên 20 nghề"], C_HVNH_ORANGE),
    (f"{max(m['F1_macro'] for m in S['classification_model_metrics'].values()):.4f}",
     "F1-macro tốt nhất (phân loại Risk_Category)",
     ["Logistic Regression & XGBoost đồng hạng", "Tăng từ ~0,22-0,34 khi thiếu Job_Title"], C_HVNH_NAVY),
    (f"{max(m['ROC_AUC_ovr'] for m in S['classification_model_metrics'].values()):.4f}",
     "ROC-AUC (One-vs-Rest) tốt nhất", ["3 lớp: Low / Medium / High", "So với 0,50 = ngẫu nhiên"], C_BLUE_CYAN),
    (f"{S['regression_model_metrics'][S['best_regression_model']]['R2']:.3f}",
     "R² mô hình hồi quy tốt nhất (Linear Regression)",
     ["Kênh kiểm chứng độc lập", "MAE ≈ 0,078 (8 điểm % xác suất)"], C_ACCENT_GREEN),
]
card_w, card_h, gap, left0, top0 = Inches(2.85), Inches(4.6), Inches(0.2), Inches(0.8), Inches(1.8)
for i, (kpi, label, desc, color) in enumerate(metrics2):
    left = Inches(left0.inches + i * (card_w.inches + gap.inches))
    add_metric_card(s2, left, top0, card_w, card_h, kpi, label, desc, highlight_color=color)
add_speaker_notes(s2,
    "Phát hiện trung tâm của toàn bộ nghiên cứu là: biến định danh nghề nghiệp Job_Title giải "
    "thích tới 85,7% phương sai của xác suất tự động hoá, trong khi mọi biến đặc điểm cá nhân "
    "như kỹ năng, kinh nghiệm, học vấn và lương gần như không có giá trị dự báo. Khi đưa Job_Title "
    "vào mô hình, F1-macro của bài toán phân loại ba nhóm rủi ro đạt 0,9947 và ROC-AUC đạt 0,998, "
    "được xác nhận độc lập bởi mô hình hồi quy với R² đạt 0,86. Bốn con số này sẽ được giải thích "
    "chi tiết qua các slide tiếp theo, đi từ bối cảnh nghiên cứu đến bằng chứng thực nghiệm.")

# ===========================================================================
# SLIDE 3 — BỐI CẢNH & CÂU HỎI NGHIÊN CỨU
# ===========================================================================
s3 = add_blank_slide(prs)
add_action_header(s3, "BỐI CẢNH NGHIÊN CỨU",
                   "Rủi ro Tự động hoá Phân bố Không Đồng đều — Yếu tố Nào Thực sự Quyết định?",
                   page_num=3, total_pages=TOTAL_SLIDES)
add_bullets_box(s3, Inches(0.9), Inches(1.8), Inches(11.5), Inches(4.8), [
    "Bối cảnh :: AI mở rộng khả năng tự động hoá từ tác vụ thủ tục sang cả tác vụ nhận thức phức tạp.",
    "Vấn đề :: Các tổ chức quốc tế (Frey & Osborne, McKinsey, WEF) đồng thuận rằng rủi ro tự động hoá "
    "không đồng đều giữa các nhóm nghề, nhưng cơ chế quyết định vẫn cần làm rõ trên từng bộ dữ liệu cụ thể.",
    "Câu hỏi nghiên cứu :: Trên bộ dữ liệu mô phỏng của bài tập, yếu tố nào giải thích rủi ro tự động "
    "hoá tốt hơn — đặc điểm CÁ NHÂN người lao động (kỹ năng, kinh nghiệm, học vấn, lương) hay đặc "
    "điểm NGHỀ NGHIỆP (Job_Title)?",
    "Cách tiếp cận :: Kiểm định thực nghiệm bằng quy trình tiền xử lý → EDA → phân cụm → phân loại → "
    "hồi quy trên 3.000 quan sát, 20 nghề nghiệp.",
], font_size=15)
add_speaker_notes(s3,
    "Câu hỏi nghiên cứu trung tâm của đồ án là: trong bộ dữ liệu này, điều gì thực sự quyết định "
    "rủi ro tự động hoá của một công việc — đặc điểm cá nhân của người đang làm công việc đó, hay "
    "bản chất của chính nghề nghiệp? Đây không phải câu hỏi hiển nhiên, vì trực giác thông thường "
    "thường cho rằng người có kỹ năng cao, học vấn cao sẽ ít bị ảnh hưởng hơn bất kể họ làm nghề "
    "gì. Chúng ta sẽ kiểm định giả thuyết này bằng một quy trình phân tích dữ liệu đầy đủ, bắt đầu "
    "từ nền tảng lý thuyết ở slide tiếp theo.")

# ===========================================================================
# SLIDE 4 — CƠ SỞ LÝ THUYẾT
# ===========================================================================
s4 = add_blank_slide(prs)
add_action_header(s4, "CƠ SỞ LÝ THUYẾT",
                   "Task-Based Approach: Rủi ro Gắn với Bản chất Công việc, Không phải Người Lao động",
                   page_num=4, total_pages=TOTAL_SLIDES)
add_bullets_box(s4, Inches(0.9), Inches(1.8), Inches(11.5), Inches(4.8), [
    "Autor, Levy & Murnane (2003) :: rủi ro tự động hoá phụ thuộc tỷ trọng tác vụ thủ tục "
    "(routine) so với phi thủ tục trong công việc — quyết định ở cấp độ NGHỀ, không phải NGƯỜI.",
    "Frey & Osborne (2017) :: ước lượng ~47% việc làm Hoa Kỳ có nguy cơ tự động hoá cao, dựa trên "
    "mức đòi hỏi sáng tạo, đàm phán, nhận thức xã hội của từng nghề.",
    "Acemoglu & Restrepo (2019) :: mô hình displacement vs. reinstatement — tự động hoá vừa thay "
    "thế vừa tạo tác vụ mới, tác động ròng phụ thuộc ngành nghề cụ thể.",
    "McKinsey (2017) & WEF (2023) :: ước lượng hàng trăm triệu lao động toàn cầu cần chuyển đổi "
    "nghề nghiệp, với mức độ rủi ro khác biệt rõ rệt giữa các nhóm ngành.",
    "Giả thuyết kiểm định :: Job_Title sẽ giải thích rủi ro tự động hoá tốt hơn các đặc trưng cá "
    "nhân trên bộ dữ liệu thực nghiệm — kiểm định ở Slide 9 và 11-13.",
], font_size=13.5)
add_speaker_notes(s4,
    "Khung lý thuyết trung tâm mà nghiên cứu dựa vào là task-based approach của Autor, Levy và "
    "Murnane công bố năm 2003, cho rằng rủi ro tự động hoá gắn với tỷ trọng tác vụ thủ tục của "
    "công việc chứ không phải năng lực cá nhân người thực hiện. Các nghiên cứu thực nghiệm sau đó "
    "của Frey và Osborne, Acemoglu và Restrepo, cũng như báo cáo của McKinsey và Diễn đàn Kinh tế "
    "Thế giới đều củng cố quan điểm này ở quy mô quốc gia và toàn cầu. Từ khung lý thuyết này, "
    "nhóm xây dựng giả thuyết cụ thể để kiểm định trên dữ liệu của bài tập: biến Job_Title sẽ có "
    "sức giải thích vượt trội so với các biến đặc điểm cá nhân.")

# ===========================================================================
# SLIDE 5 — BỘ DỮ LIỆU
# ===========================================================================
s5 = add_blank_slide(prs)
add_action_header(s5, "DỮ LIỆU NGHIÊN CỨU",
                   "3.000 Hồ sơ x 20 Nghề nghiệp — Đầy đủ Chỉ số Kỹ năng, Lương, Học vấn và Công nghệ",
                   page_num=5, total_pages=TOTAL_SLIDES)
metrics5 = [
    ("3.000", "Quan sát (hồ sơ nghề nghiệp)", ["18 biến gốc", "Không thiếu, không trùng"], C_HVNH_NAVY),
    ("20", "Nghề nghiệp khảo sát", ["Từ Bác sĩ đến Bảo vệ", "132-175 quan sát/nghề"], C_HVNH_ORANGE),
    ("10", "Nhóm điểm kỹ năng (Skill_1..10)", ["Chuẩn hoá [0,1]", "+ AI_Exposure, Tech_Growth"], C_BLUE_CYAN),
    ("3", "Nhóm rủi ro mục tiêu", ["Low 24,6% · Medium 50,7%", "High 24,7%"], C_ACCENT_RED),
]
for i, (kpi, label, desc, color) in enumerate(metrics5):
    left = Inches(left0.inches + i * (card_w.inches + gap.inches))
    add_metric_card(s5, left, top0, card_w, card_h, kpi, label, desc, highlight_color=color)
add_speaker_notes(s5,
    "Bộ dữ liệu gồm 3.000 quan sát và 18 biến gốc, mô tả 20 nghề nghiệp phổ biến từ bác sĩ, giáo "
    "viên đến nhân viên bảo vệ, bán lẻ. Mỗi hồ sơ có đầy đủ thông tin lương, số năm kinh nghiệm, "
    "trình độ học vấn, hai chỉ số công nghệ là AI Exposure Index và Tech Growth Factor, mười điểm "
    "kỹ năng chuẩn hoá, và hai biến mục tiêu là xác suất tự động hoá liên tục và nhóm rủi ro rời "
    "rạc ba mức. Dữ liệu không có ô thiếu, không trùng lặp — đây là một bộ dữ liệu mô phỏng sạch, "
    "phù hợp để luyện tập kỹ thuật phân tích trước khi mở rộng sang dữ liệu thực tế.")

# ===========================================================================
# SLIDE 6 — QUY TRÌNH TIỀN XỬ LÝ
# ===========================================================================
s6 = add_blank_slide(prs)
add_action_header(s6, "TIỀN XỬ LÝ DỮ LIỆU",
                   "Tiền xử lý Phát hiện Rủi ro Rò rỉ Dữ liệu giữa Risk_Category và Automation_Probability",
                   page_num=6, total_pages=TOTAL_SLIDES)
steps6 = [
    ("01", "KIỂM TRA CHẤT LƯỢNG", ["0 ô thiếu dữ liệu", "0 dòng trùng lặp",
                                    "0 dòng ngoài miền giá trị [0,1]", "0 ngoại lai IQR (lương)"]),
    ("02", "PHÁT HIỆN RÒ RỈ", ["Risk_Category = f(ngưỡng cố định)", "của Automation_Probability_2030",
                                "→ loại biến mục tiêu liên tục khỏi tập đặc trưng phân loại"]),
    ("03", "FEATURE ENGINEERING", ["7 biến mới: Skill_Diversity_Score,", "Human_Edge_Score, High_Value_Skill...",
                                    "One-hot Job_Title: +19 biến giả"]),
    ("04", "DỮ LIỆU SẴN SÀNG", ["3.000 dòng x 25 cột (sạch)", "Train/test 75/25", "Stratify theo Risk_Category"]),
]
add_process_pipeline_4(s6, steps6)
add_speaker_notes(s6,
    "Quy trình tiền xử lý gồm bốn bước. Bước một kiểm tra chất lượng dữ liệu và không phát hiện "
    "vấn đề nào — dữ liệu sạch ngay từ đầu. Bước hai là phát hiện quan trọng nhất: nhóm rủi ro "
    "Risk_Category thực chất là hàm ngưỡng cố định của xác suất tự động hoá liên tục, nên nếu đưa "
    "cả hai biến này vào cùng một mô hình phân loại sẽ gây rò rỉ dữ liệu, khiến mô hình gian lận "
    "gián tiếp. Bước ba tạo thêm bảy biến đặc trưng mới và mã hoá một-nóng biến nghề nghiệp thành "
    "mười chín biến giả. Bước bốn hoàn tất, cho ra bộ dữ liệu sẵn sàng huấn luyện mô hình.")

# ===========================================================================
# SLIDE 7 — EDA 1: PHÂN BỐ RỦI RO
# ===========================================================================
s7 = add_blank_slide(prs)
add_action_header(s7, "PHÂN TÍCH KHÁM PHÁ DỮ LIỆU 1/3",
                   "Nhóm Medium Chiếm 50,7% — Phân bố Xác suất Ẩn chứa Ba Cụm Mật độ Tách biệt",
                   page_num=7, total_pages=TOTAL_SLIDES)
add_chart_deep_dive_60_40(s7, str(FIG_DIR / "02_automation_probability_distribution.png"),
    "Đọc biểu đồ", [
        ("Hình dạng", "Phân bố KHÔNG phải một đường cong chuẩn trơn mà có 3 vùng mật độ tách biệt."),
        ("Cơ cấu 3 nhóm", "Low 24,6% · Medium 50,7% · High 24,7% — chia theo ngưỡng cố định của xác suất."),
        ("Gợi ý ban đầu", "Cấu trúc 3 cụm gợi ý một biến phân loại tiềm ẩn (không phải nhiễu ngẫu nhiên) "
                            "đang chi phối biến mục tiêu — sẽ được xác định ở Slide 9."),
    ])
add_speaker_notes(s7,
    "Biểu đồ phân bố xác suất tự động hoá không có dạng đường cong chuẩn trơn thông thường mà thể "
    "hiện ba vùng mật độ tách biệt khá rõ. Ba nhóm rủi ro Low, Medium, High được chia theo ngưỡng "
    "cố định của xác suất này, trong đó nhóm Medium chiếm hơn một nửa mẫu quan sát. Hình dạng ba "
    "cụm mật độ này là một gợi ý quan trọng: rất có thể có một biến phân loại tiềm ẩn nào đó — "
    "không phải nhiễu ngẫu nhiên liên tục — đang quyết định giá trị của biến mục tiêu. Chúng ta sẽ "
    "xác định chính xác biến đó là gì ở các slide tiếp theo.")

# ===========================================================================
# SLIDE 8 — EDA 2: ĐẶC ĐIỂM CÁ NHÂN KHÔNG DỰ BÁO ĐƯỢC
# ===========================================================================
s8 = add_blank_slide(prs)
add_action_header(s8, "PHÂN TÍCH KHÁM PHÁ DỮ LIỆU 2/3",
                   "Lương, Học vấn, Kinh nghiệm, AI Exposure: Tương quan Xấp xỉ Bằng 0 với Rủi ro",
                   page_num=8, total_pages=TOTAL_SLIDES)
add_chart_deep_dive_60_40(s8, str(FIG_DIR / "06_correlation_heatmap.png"),
    "Đọc biểu đồ", [
        ("Ma trận tương quan", "Mọi hệ số tương quan giữa Automation_Probability_2030 và các biến cá nhân "
                                 "đều |r| < 0,05 — về mặt thống kê là KHÔNG có quan hệ tuyến tính."),
        ("Nhất quán qua nhiều góc nhìn", "Boxplot lương theo nhóm rủi ro, biểu đồ học vấn, biểu đồ kinh "
                                          "nghiệm (Slide phụ lục) đều cho kết luận tương tự."),
        ("Hệ quả", "Nếu chỉ dùng đặc điểm cá nhân, một mô hình dự báo sẽ hoạt động không tốt hơn "
                    "phỏng đoán ngẫu nhiên — sẽ được kiểm chứng định lượng ở Slide 11."),
    ])
add_speaker_notes(s8,
    "Sau khi kiểm tra từng biến một trong phần khám phá dữ liệu đầy đủ ở báo cáo văn bản, ma trận "
    "tương quan tổng hợp xác nhận: không một biến cá nhân nào — kể cả chỉ số phơi nhiễm AI vốn "
    "tưởng như liên quan trực tiếp đến chủ đề — có tương quan đáng kể với xác suất tự động hoá. "
    "Tất cả hệ số tương quan đều nhỏ hơn 0,05 về giá trị tuyệt đối, mức được xem là không có ý "
    "nghĩa thống kê thực tiễn trong hầu hết ngữ cảnh phân tích kinh doanh. Điều này có nghĩa nếu "
    "chỉ dựa vào hồ sơ cá nhân, chúng ta gần như không thể dự báo được rủi ro tự động hoá.")

# ===========================================================================
# SLIDE 9 — EDA 3: BẰNG CHỨNG THEN CHỐT
# ===========================================================================
s9 = add_blank_slide(prs)
add_action_header(s9, "PHÂN TÍCH KHÁM PHÁ DỮ LIỆU 3/3 — BẰNG CHỨNG THEN CHỐT",
                   "20 Nghề Tách 3 Tầng Rõ rệt — Job_Title Giải thích 85,7% Phương sai (Eta²)",
                   page_num=9, total_pages=TOTAL_SLIDES)
add_chart_deep_dive_60_40(s9, str(FIG_DIR / "08_jobtitle_automation_ranked.png"),
    "Ba tầng nghề nghiệp", [
        ("Tầng thấp (~0,18)", "AI Engineer, Research Scientist, Nurse, Teacher, Doctor — phán đoán "
                               "chuyên môn sâu, chăm sóc con người."),
        ("Tầng trung bình (~0,50)", "10 nghề chuyên môn/văn phòng còn lại (Data Scientist, Lawyer, "
                                     "Software Engineer, Chef...)."),
        ("Tầng cao (~0,83)", "Retail Worker, Security Guard, Construction Worker, Customer Support, "
                              "Truck Driver — tác vụ lặp lại/thủ tục cao."),
        ("Kiểm định eta²", "SSB/SST = 0,857 — Job_Title giải thích 85,7% phương sai, vượt trội mọi "
                            "biến cá nhân đã kiểm tra."),
    ])
add_speaker_notes(s9,
    "Đây là phát hiện quan trọng nhất của toàn bộ bài phân tích. Khi xếp hạng 20 nghề theo xác "
    "suất tự động hoá trung bình, dữ liệu tách thành ba tầng rất rõ rệt, gần như không có vùng "
    "chuyển tiếp mờ nhạt. Tầng thấp gồm những nghề đòi hỏi phán đoán chuyên môn sâu hoặc chăm sóc "
    "con người như bác sĩ, giáo viên, y tá, nhà nghiên cứu và kỹ sư AI. Tầng cao gồm những nghề có "
    "tỷ trọng tác vụ lặp lại, thủ tục cao như nhân viên bán lẻ, bảo vệ, xây dựng, hỗ trợ khách "
    "hàng và lái xe tải. Kiểm định eta bình phương định lượng phát hiện này: riêng biến nghề "
    "nghiệp giải thích tới tám mươi lăm phẩy bảy phần trăm phương sai của xác suất tự động hoá, "
    "một con số vượt trội hoàn toàn so với bất kỳ biến cá nhân nào đã kiểm tra trước đó.")

# ===========================================================================
# SLIDE 10 — PHÂN CỤM K-MEANS
# ===========================================================================
s10 = add_blank_slide(prs)
add_action_header(s10, "PHÂN CỤM KHÔNG GIÁM SÁT",
                   "Phân cụm Hồ sơ Kỹ năng Thất bại (Silhouette ≈ 0,06) — Xác nhận Kỹ năng Không Quyết định",
                   page_num=10, total_pages=TOTAL_SLIDES)
add_chart_deep_dive_60_40(s10, str(FIG_DIR / "13_kmeans_clusters_pca.png"),
    "Đọc biểu đồ", [
        ("Phương pháp", "K-Means trên 12 biến kỹ năng/công nghệ, k=4 chọn vì mục đích diễn giải nghiệp vụ."),
        ("Silhouette Score", "Chỉ 0,055-0,063 ở MỌI k (2-8) — gần 0, nghĩa là các cụm KHÔNG tách biệt."),
        ("Xác suất TĐH theo cụm", "4 cụm có xác suất tự động hoá trung bình gần như bằng nhau (0,49-0,52)."),
        ("Ý nghĩa", "Xác nhận thêm: hồ sơ kỹ năng cá nhân không mang thông tin phân biệt rủi ro — "
                     "khác biệt nằm ở nghề nghiệp (Slide 9), không ở kỹ năng."),
    ])
add_speaker_notes(s10,
    "Ở bước phân cụm không giám sát, nhóm thử tìm các hồ sơ kỹ năng tự nhiên bằng thuật toán "
    "K-Means trên mười hai biến liên quan đến kỹ năng và công nghệ. Kết quả chỉ số Silhouette chỉ "
    "dao động trong khoảng từ không phẩy không năm lăm đến không phẩy không sáu ba ở mọi giá trị k "
    "thử nghiệm từ hai đến tám — mức rất gần không, cho thấy các cụm không tách biệt rõ ràng. Bốn "
    "cụm được chọn cho mục đích diễn giải nghiệp vụ đều có xác suất tự động hoá trung bình gần như "
    "bằng nhau. Kết quả này càng củng cố kết luận: sự khác biệt về rủi ro không nằm ở hồ sơ kỹ "
    "năng cá nhân mà nằm ở chính nghề nghiệp, như đã thấy ở slide trước.")

# ===========================================================================
# SLIDE 11 — SO SÁNH MÔ HÌNH PHÂN LOẠI
# ===========================================================================
s11 = add_blank_slide(prs)
add_action_header(s11, "MÔ HÌNH PHÂN LOẠI RISK_CATEGORY",
                   "Logistic Regression & XGBoost Đồng hạng Nhất: F1-macro 0,9947 · AUC ≈ 0,998",
                   page_num=11, total_pages=TOTAL_SLIDES)
cm = S["classification_model_metrics"]
models11 = [
    (name, [("F1-macro", f"{m['F1_macro']:.4f}"), ("ROC-AUC", f"{m['ROC_AUC_ovr']:.4f}"),
            ("Accuracy", f"{m['Accuracy']:.4f}")])
    for name, m in cm.items()
]
add_model_comparison_cards(s11, models11, winner_index=0)
add_speaker_notes(s11,
    "Sau khi đưa biến Job_Title vào tập đặc trưng dưới dạng mã hoá một-nóng, ba mô hình phân loại "
    "được huấn luyện và so sánh: Logistic Regression, Random Forest và XGBoost Classifier. "
    "Logistic Regression và XGBoost đạt kết quả gần như tuyệt đối và đồng hạng nhất với F1-macro "
    "0,9947 và ROC-AUC lần lượt 0,9979 và 0,9964. Random Forest đạt kết quả thấp hơn một chút với "
    "F1-macro 0,9345, có thể do độ sâu cây bị giới hạn. Đây là bước ngoặt so với vòng thử nghiệm "
    "trước đó khi chưa có Job_Title, lúc đó F1-macro chỉ đạt khoảng không phẩy hai hai đến không "
    "phẩy ba tư, xấp xỉ mức dự đoán ngẫu nhiên.")

# ===========================================================================
# SLIDE 12 — FEATURE IMPORTANCE
# ===========================================================================
s12 = add_blank_slide(prs)
add_action_header(s12, "MỨC ĐỘ QUAN TRỌNG CỦA BIẾN",
                   f"{S['job_title_total_importance']*100:.1f}% Tầm quan trọng Mô hình Thuộc về Nhóm biến Job_Title",
                   page_num=12, total_pages=TOTAL_SLIDES)
add_chart_deep_dive_60_40(s12, str(FIG_DIR / "16_feature_importance.png"),
    "Đọc biểu đồ", [
        ("Phương pháp", "Feature importance của XGBoost Classifier, gộp 19 biến giả Job_Title thành 1 mục."),
        ("Kết quả", f"Nhóm Job_Title (gộp) chiếm {S['job_title_total_importance']*100:.1f}% tổng importance."),
        ("Phần còn lại", "Toàn bộ các biến cá nhân/kỹ năng khác cộng lại chỉ chiếm "
                          f"{(1-S['job_title_total_importance'])*100:.1f}% — gần như không đáng kể."),
        ("Kết luận", "Bằng chứng định lượng trực tiếp cho khung task-based approach (Slide 4): "
                      "mô hình học được chính xác quy luật ẩn trong dữ liệu."),
    ])
add_speaker_notes(s12,
    "Biểu đồ mức độ quan trọng của biến từ mô hình XGBoost, sau khi gộp mười chín biến giả của "
    "Job_Title thành một mục duy nhất để dễ diễn giải, cho thấy một bức tranh rất rõ ràng: nhóm "
    "biến nghề nghiệp chiếm tới chín mươi tám phẩy năm phần trăm tổng mức độ quan trọng của mô "
    "hình. Toàn bộ các biến còn lại — lương, kinh nghiệm, học vấn, mười điểm kỹ năng và các chỉ số "
    "tổng hợp — cộng lại chỉ chiếm chưa đến hai phần trăm. Đây là bằng chứng định lượng trực tiếp "
    "và thuyết phục nhất cho khung lý thuyết tiếp cận theo tác vụ đã trình bày ở phần cơ sở lý "
    "thuyết: mô hình học máy, một cách độc lập với giả thuyết ban đầu, đã tự khám phá ra đúng quy "
    "luật ẩn trong dữ liệu.")

# ===========================================================================
# SLIDE 13 — MÔ HÌNH HỒI QUY
# ===========================================================================
s13 = add_blank_slide(prs)
add_action_header(s13, "MÔ HÌNH HỒI QUY — KIỂM CHỨNG ĐỘC LẬP",
                   f"Hồi quy Độc lập Xác nhận: R² = {S['regression_model_metrics'][S['best_regression_model']]['R2']:.3f} khi Đưa Nghề nghiệp vào Mô hình",
                   page_num=13, total_pages=TOTAL_SLIDES)
add_chart_deep_dive_60_40(s13, str(FIG_DIR / "17_regression_pred_vs_actual.png"),
    "Đọc biểu đồ", [
        ("Phương pháp", "Hồi quy trực tiếp Automation_Probability_2030 (biến liên tục), cùng tập đặc trưng."),
        ("Kết quả tốt nhất", f"{S['best_regression_model']}: R²="
                              f"{S['regression_model_metrics'][S['best_regression_model']]['R2']:.3f}, "
                              f"MAE={S['regression_model_metrics'][S['best_regression_model']]['MAE']:.3f}."),
        ("Ý nghĩa MAE", "Sai số dự báo trung bình chỉ ~8 điểm phần trăm xác suất — mức hợp lý."),
        ("Vai trò của slide này", "Kênh đánh giá ĐỘC LẬP với bài toán phân loại — cùng kết luận, "
                                    "củng cố độ tin cậy của phát hiện chính."),
    ])
add_speaker_notes(s13,
    "Để kiểm chứng phát hiện chính bằng một góc nhìn độc lập, nhóm xây dựng thêm mô hình hồi quy "
    "dự báo trực tiếp giá trị liên tục của xác suất tự động hoá, thay vì phân loại rời rạc ba "
    "nhóm. Kết quả nhất quán hoàn toàn với bài toán phân loại: mô hình Linear Regression đạt hệ số "
    "xác định R bình phương bằng không phẩy tám sáu hai, với sai số tuyệt đối trung bình chỉ "
    "khoảng tám điểm phần trăm xác suất. Việc hai phương pháp đánh giá độc lập — phân loại và hồi "
    "quy — đều cho cùng một kết luận giúp tăng đáng kể độ tin cậy của phát hiện chính, thay vì chỉ "
    "dựa vào một góc nhìn phân tích duy nhất.")

# ===========================================================================
# SLIDE 14 — BA CHÂN DUNG NGHỀ NGHIỆP
# ===========================================================================
s14 = add_blank_slide(prs)
add_action_header(s14, "CHÂN DUNG BA TẦNG NGHỀ NGHIỆP",
                   "Từ Rủi ro Thấp (Bác sĩ, Giáo viên) đến Rủi ro Cao (Bán lẻ, Bảo vệ)",
                   page_num=14, total_pages=TOTAL_SLIDES)
personas14 = [
    ("Tầng Rủi ro THẤP", "~24,6% mẫu · XS TB ≈ 0,18",
     "AI Engineer, Research Scientist, Nurse, Teacher, Doctor — đòi hỏi phán đoán chuyên môn sâu "
     "hoặc chăm sóc/tương tác con người cường độ cao.",
     "Đầu tư phát triển chuyên sâu; không cần chuyển đổi nghề gấp; theo dõi định kỳ."),
    ("Tầng Rủi ro TRUNG BÌNH", "~50,7% mẫu · XS TB ≈ 0,50",
     "10 nghề chuyên môn/văn phòng: Data Scientist, Software Engineer, Lawyer, Chef, Marketing "
     "Manager... — pha trộn tác vụ thủ tục và phi thủ tục.",
     "Chủ động bổ sung kỹ năng số định kỳ để tránh dịch chuyển sang tầng cao."),
    ("Tầng Rủi ro CAO", "~24,7% mẫu · XS TB ≈ 0,83",
     "Retail Worker, Security Guard, Construction Worker, Customer Support, Truck Driver — tỷ "
     "trọng tác vụ lặp lại/thủ tục cao.",
     "Ưu tiên chương trình đào tạo lại (reskilling), xây dựng lộ trình chuyển đổi nghề sớm."),
]
add_persona_profile_cards(s14, personas14)
add_speaker_notes(s14,
    "Để chuyển kết quả phân tích thành thông tin dễ sử dụng cho quản trị nhân sự, nhóm tổng hợp ba "
    "tầng nghề nghiệp thành ba chân dung minh hoạ. Tầng rủi ro thấp gồm những nghề đòi hỏi chuyên "
    "môn sâu hoặc chăm sóc con người như bác sĩ, giáo viên, y tá. Tầng trung bình chiếm hơn một "
    "nửa mẫu, gồm các nghề chuyên môn văn phòng có tính chất pha trộn. Tầng rủi ro cao gồm những "
    "nghề có tỷ trọng tác vụ lặp lại cao như bán lẻ, bảo vệ, xây dựng, hỗ trợ khách hàng và lái xe "
    "tải. Mỗi tầng đi kèm một hướng hành động quản trị nhân sự cụ thể, sẽ được trình bày chi tiết "
    "hơn ở slide tiếp theo.")

# ===========================================================================
# SLIDE 15 — KHUNG HÀNH ĐỘNG
# ===========================================================================
s15 = add_blank_slide(prs)
add_action_header(s15, "HÀM Ý QUẢN TRỊ NHÂN SỰ",
                   "Khung Hành động 3 Tầng: Ưu tiên Đào tạo lại Theo Nhóm nghề, Không Theo Cá nhân",
                   page_num=15, total_pages=TOTAL_SLIDES)
tiers15 = [
    ("Tầng Rủi ro Thấp", "Đầu tư phát triển chuyên môn sâu và kỹ năng phán đoán/chăm sóc con người — "
     "nhóm nghề ít chịu áp lực tự động hoá trực tiếp trong ngắn-trung hạn.",
     "~24,6% mẫu · XS TB ≈ 0,18"),
    ("Tầng Rủi ro Trung bình", "Theo dõi định kỳ mức ứng dụng AI trong ngành, chủ động bổ sung kỹ "
     "năng số để không dịch chuyển sang tầng cao.", "~50,7% mẫu · XS TB ≈ 0,50"),
    ("Tầng Rủi ro Cao", "Ưu tiên chương trình đào tạo lại (reskilling) THEO NHÓM NGHỀ, xây dựng lộ "
     "trình chuyển đổi nghề nghiệp sớm thay vì chờ đến khi bị thay thế.", "~24,7% mẫu · XS TB ≈ 0,83"),
]
add_strategic_tier_matrix(s15, tiers15)
add_speaker_notes(s15,
    "Từ phát hiện thực nghiệm, hàm ý quản trị nhân sự quan trọng nhất là: chiến lược đào tạo lại "
    "nên được thiết kế theo NHÓM NGHỀ NGHIỆP thay vì chỉ dựa trên đánh giá năng lực cá nhân từng "
    "người lao động, vì dữ liệu cho thấy hai người có hồ sơ kỹ năng giống hệt nhau nhưng làm khác "
    "nghề có thể đối mặt mức rủi ro hoàn toàn khác nhau. Khung ba tầng đề xuất ở đây gắn mỗi nhóm "
    "rủi ro với một hành động cụ thể: tầng thấp tiếp tục đầu tư chuyên sâu, tầng trung bình chủ "
    "động bổ sung kỹ năng số, và tầng cao cần ưu tiên chương trình chuyển đổi nghề nghiệp sớm nhất "
    "trong ba nhóm.")

# ===========================================================================
# SLIDE 16 — HẠN CHẾ NGHIÊN CỨU
# ===========================================================================
s16 = add_blank_slide(prs)
add_action_header(s16, "HẠN CHẾ NGHIÊN CỨU",
                   "Giới hạn: Dữ liệu Mô phỏng — Kết luận Có giá trị Nội tại, Cần Đối chiếu Thực tế",
                   page_num=16, total_pages=TOTAL_SLIDES)
add_bullets_box(s16, Inches(0.9), Inches(1.8), Inches(11.5), Inches(4.8), [
    "Dữ liệu mô phỏng (synthetic) :: Automation_Probability_2030 được gán theo quy tắc gắn với "
    "Job_Title — phát hiện chỉ có giá trị NỘI TẠI với tập dữ liệu này, không suy rộng trực tiếp "
    "cho thị trường lao động thực tế.",
    "Thiếu chiều thời gian :: chỉ một lát cắt tĩnh năm 2030, không phân tích được động thái thay "
    "đổi rủi ro theo thời gian như các khảo sát WEF/McKinsey thực hiện định kỳ.",
    "Thiếu biến ngành/vùng địa lý :: không thể phân tích khác biệt theo khu vực kinh tế hay quốc gia.",
    "Hiệu suất mô hình gần tuyệt đối :: phản ánh cơ chế sinh dữ liệu có kiểm soát, KHÔNG nên diễn "
    "giải như bằng chứng cho khả năng dự báo tương tự trong dữ liệu thực tế.",
], font_size=15)
add_speaker_notes(s16,
    "Trước khi kết luận, cần nêu rõ ba giới hạn quan trọng của nghiên cứu để tránh diễn giải vượt "
    "quá mức độ bằng chứng cho phép. Thứ nhất, đây là bộ dữ liệu mô phỏng phục vụ mục đích luyện "
    "tập kỹ thuật, nên phát hiện chỉ có giá trị nội tại với chính tập dữ liệu này. Thứ hai, dữ "
    "liệu không có chiều thời gian hay biến ngành, vùng địa lý cụ thể. Thứ ba, và quan trọng nhất, "
    "hiệu suất mô hình gần như tuyệt đối phản ánh cách dữ liệu được sinh ra một cách có kiểm soát, "
    "không nên được xem là bằng chứng rằng rủi ro tự động hoá trong thực tế có thể dự báo chính "
    "xác đến mức độ tương tự.")

# ===========================================================================
# SLIDE 17 — KẾT LUẬN
# ===========================================================================
s17 = add_blank_slide(prs)
add_action_header(s17, "KẾT LUẬN",
                   "Nghề nghiệp — Không phải Kỹ năng Cá nhân — Là Biến số Quyết định Rủi ro",
                   page_num=17, total_pages=TOTAL_SLIDES)
add_bullets_box(s17, Inches(0.9), Inches(1.8), Inches(11.5), Inches(4.8), [
    "Phát hiện chính :: Job_Title giải thích 85,7% phương sai rủi ro tự động hoá; đưa vào mô hình "
    "nâng F1-macro từ mức ngẫu nhiên lên 0,9947 và R² hồi quy lên 0,862.",
    "Nhất quán lý thuyết :: kết quả phù hợp định tính với task-based approach (Autor et al., 2003) "
    "và Frey & Osborne (2017) — rủi ro gắn với bản chất tác vụ của nghề nghiệp.",
    "Hàm ý thực tiễn :: chiến lược đào tạo lại nên thiết kế theo nhóm nghề, không chỉ theo hồ sơ "
    "năng lực cá nhân.",
    "Giới hạn cần lưu ý :: kết luận rút ra từ dữ liệu mô phỏng, là minh hoạ phương pháp luận hơn "
    "là khẳng định tổng quát về thị trường lao động thực tế.",
    "Hướng phát triển :: bổ sung dữ liệu thời gian, ngành/vùng thực tế; đối chiếu O*NET Task "
    "Ratings và WEF Future of Jobs Survey.",
], font_size=14.5)
add_speaker_notes(s17,
    "Tóm lại, đồ án đã thực hiện trọn vẹn quy trình phân tích kinh doanh trên bộ dữ liệu mô phỏng "
    "về tác động của AI đến việc làm năm 2030, từ tiền xử lý, phân tích khám phá dữ liệu, phân "
    "cụm, đến hai mô hình dự báo độc lập. Phát hiện xuyên suốt là biến nghề nghiệp quyết định gần "
    "như hoàn toàn rủi ro tự động hoá trong khi đặc điểm cá nhân gần như không có vai trò — kết "
    "quả này nhất quán về mặt định tính với các lý thuyết và nghiên cứu quốc tế đã trình bày ở đầu "
    "bài. Trong phạm vi giới hạn của một bộ dữ liệu mô phỏng, đây là một minh hoạ phương pháp luận "
    "có giá trị, mở đường cho các phân tích sâu hơn trên dữ liệu thực tế trong tương lai. Em xin "
    "cảm ơn Hội đồng đã lắng nghe và sẵn sàng trả lời các câu hỏi.")

# ===========================================================================
# SLIDE 18 — Q&A
# ===========================================================================
s18 = add_blank_slide(prs, bg_color=C_HVNH_NAVY)
band18 = s18.shapes.add_shape(1, Inches(0), Inches(3.4), prs.slide_width, Inches(0.05))
band18.fill.solid(); band18.fill.fore_color.rgb = C_HVNH_ORANGE; band18.line.fill.background()
tbq = s18.shapes.add_textbox(Inches(0.9), Inches(2.5), Inches(11.5), Inches(0.9))
pq = tbq.text_frame.paragraphs[0]
rq = pq.add_run(); rq.text = "CẢM ƠN HỘI ĐỒNG — HỎI & ĐÁP"
rq.font.name = FONT_TITLE; rq.font.size = Pt(32); rq.font.bold = True; rq.font.color.rgb = C_WHITE
pq.alignment = PP_ALIGN.CENTER
tbq2 = s18.shapes.add_textbox(Inches(0.9), Inches(3.6), Inches(11.5), Inches(0.6))
pq2 = tbq2.text_frame.paragraphs[0]
pq2.alignment = PP_ALIGN.CENTER
rq2 = pq2.add_run()
rq2.text = "Đỗ Văn Đạt  ·  Phân tích Kinh doanh  ·  Học viện Ngân hàng"
rq2.font.name = FONT_PRIMARY; rq2.font.size = Pt(14); rq2.font.color.rgb = C_CARD_BORDER
add_speaker_notes(s18,
    "Cảm ơn Hội đồng đã theo dõi phần trình bày. Em xin phép nhắc lại ba câu hỏi phản biện có thể "
    "gặp: Một, vì sao không dùng trực tiếp Automation_Probability_2030 làm đặc trưng — vì đó chính "
    "là nguồn sinh ra Risk_Category nên sẽ gây rò rỉ dữ liệu. Hai, vì sao phân cụm không giám sát "
    "thất bại — vì các biến kỹ năng trong dữ liệu độc lập ngẫu nhiên với nghề nghiệp, không mang "
    "thông tin phân biệt. Ba, kết luận có áp dụng được cho thị trường lao động thực tế không — chỉ "
    "ở mức định tính, cần dữ liệu thực nghiệm để kiểm chứng định lượng. Em xin mời Hội đồng đặt câu hỏi.")

# ===========================================================================
# VALIDATE & SAVE
# ===========================================================================
ok = validate_deck(prs, expected_slides=TOTAL_SLIDES)
out_path = BASE_DIR / "Slide_Thuyet_Trinh_TacDongAI_ViecLam2030.pptx"
prs.save(out_path)
print(f"\nĐã lưu slide: {out_path.name} ({'OK' if ok else 'CÓ CẢNH BÁO — xem log ở trên'})")
