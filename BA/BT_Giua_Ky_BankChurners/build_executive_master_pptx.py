import os
import sys
import pptx
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.dml.color import RGBColor

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FIG_DIR = os.path.join(BASE_DIR, "figures")
PPTX_PATH = os.path.join(BASE_DIR, "Slide_Thuyet_Trinh_BankChurners.pptx")

# ==============================================================================
# HỆ THỐNG MÀU SẮC NHẬN DIỆN THƯƠNG HIỆU HỌC VIỆN NGÂN HÀNG (HVNH BRAND IDENTITY)
# & PHONG CÁCH TƯ VẤN QUẢN TRỊ TÀI CHÍNH BẬC CAO HỌC (EXECUTIVE MASTER STYLE)
# ==============================================================================
C_HVNH_NAVY   = RGBColor(10, 37, 64)       # #0A2540: Xanh Navy đậm HVNH (Trí tuệ, Chuẩn mực học thuật)
C_HVNH_ORANGE = RGBColor(234, 88, 12)      # #EA580C: Cam năng động HVNH (Đổi mới, Điểm nhấn thương hiệu)
C_HVNH_GOLD   = RGBColor(245, 158, 11)     # #F59E0B: Vàng kim sang trọng
C_BLUE_CYAN   = RGBColor(2, 132, 199)      # #0284C7: Xanh dương công nghệ / Khách hàng hiện hữu
C_ACCENT_RED  = RGBColor(220, 38, 38)      # #DC2626: Đỏ cảnh báo rủi ro / Churn
C_ACCENT_GREEN= RGBColor(16, 185, 129)     # #10B981: Xanh ngọc thành công / Retention / ROI

C_CANVAS_BG   = RGBColor(248, 250, 252)    # #F8FAFC: Nền Canvas Slate 50 cao cấp
C_CARD_BG     = RGBColor(255, 255, 255)    # #FFFFFF: Thẻ card trắng tinh khiết
C_CARD_BORDER = RGBColor(226, 232, 240)    # #E2E8F0: Viền thẻ Slate 200 mỏng tinh tế
C_TEXT_DARK   = RGBColor(15, 23, 42)       # #0F172A: Chữ chính Slate 900
C_TEXT_MUTED  = RGBColor(100, 116, 139)    # #64748B: Chữ phụ Slate 500
C_WHITE       = RGBColor(255, 255, 255)

FONT_PRIMARY = 'Calibri'
FONT_TITLE   = 'Calibri'

prs = Presentation()
prs.slide_width = Inches(13.333)  # 16:9 Widescreen standard
prs.slide_height = Inches(7.5)

blank_layout = prs.slide_layouts[6]

def set_bg(slide, color=C_CANVAS_BG):
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = color

def add_header(slide, action_title, tracker_text="HỌC VIỆN NGÂN HÀNG | BÀI TẬP GIỮA KỲ — PHÂN TÍCH DỮ LIỆU KINH DOANH", category_badge="EXECUTIVE TAKEAWAY"):
    # Category Tracker Bar & Badge
    tb_trk = slide.shapes.add_textbox(Inches(0.8), Inches(0.32), Inches(11.733), Inches(0.3))
    tf_trk = tb_trk.text_frame
    tf_trk.word_wrap = True
    tf_trk.margin_left = tf_trk.margin_right = tf_trk.margin_top = tf_trk.margin_bottom = 0
    p_trk = tf_trk.paragraphs[0]
    
    r_trk = p_trk.add_run()
    r_trk.text = f"{tracker_text.upper()}  •  "
    r_trk.font.name = FONT_PRIMARY
    r_trk.font.size = Pt(9.5)
    r_trk.font.bold = True
    r_trk.font.color.rgb = C_HVNH_NAVY
    
    r_bdg = p_trk.add_run()
    r_bdg.text = f"[{category_badge}]"
    r_bdg.font.name = FONT_PRIMARY
    r_bdg.font.size = Pt(9.5)
    r_bdg.font.bold = True
    r_bdg.font.color.rgb = C_HVNH_ORANGE

    # Action-Oriented Title (McKinsey Lead Conclusion Style)
    tb_ttl = slide.shapes.add_textbox(Inches(0.8), Inches(0.62), Inches(11.733), Inches(0.68))
    tf_ttl = tb_ttl.text_frame
    tf_ttl.word_wrap = True
    tf_ttl.margin_left = tf_ttl.margin_right = tf_ttl.margin_top = tf_ttl.margin_bottom = 0
    p_ttl = tf_ttl.paragraphs[0]
    p_ttl.text = action_title
    p_ttl.font.name = FONT_TITLE
    p_ttl.font.size = Pt(18.5)
    p_ttl.font.bold = True
    p_ttl.font.color.rgb = C_HVNH_NAVY
    
    # Bottom accent line under title
    line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.34), Inches(2.2), Inches(0.04))
    line.fill.solid()
    line.fill.fore_color.rgb = C_HVNH_ORANGE
    line.line.fill.background()

def add_footer(slide, slide_num, total_slides=21):
    tb_ftr = slide.shapes.add_textbox(Inches(0.8), Inches(7.05), Inches(11.733), Inches(0.3))
    tf_ftr = tb_ftr.text_frame
    tf_ftr.margin_left = tf_ftr.margin_right = tf_ftr.margin_top = tf_ftr.margin_bottom = 0
    p_ftr = tf_ftr.paragraphs[0]
    
    p_ftr.text = f"Học viện Ngân hàng (BAV)  •  Học phần: Phân tích Dữ liệu trong Kinh doanh  •  Học viên: Đỗ Văn Đạt"
    p_ftr.font.name = FONT_PRIMARY
    p_ftr.font.size = Pt(9.5)
    p_ftr.font.color.rgb = C_TEXT_MUTED
    
    # Page Number right-aligned
    tb_num = slide.shapes.add_textbox(Inches(10.5), Inches(7.05), Inches(2.033), Inches(0.3))
    tf_num = tb_num.text_frame
    tf_num.margin_left = tf_num.margin_right = tf_num.margin_top = tf_num.margin_bottom = 0
    p_num = tf_num.paragraphs[0]
    p_num.alignment = PP_ALIGN.RIGHT
    p_num.text = f"{slide_num:02d} / {total_slides:02d}"
    p_num.font.name = FONT_PRIMARY
    p_num.font.size = Pt(10)
    p_num.font.bold = True
    p_num.font.color.rgb = C_HVNH_NAVY

def create_card(slide, left, top, width, height, bg_color=C_CARD_BG, border_color=C_CARD_BORDER, border_width=1.0):
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = bg_color
    if border_color is not None:
        shape.line.color.rgb = border_color
        shape.line.width = Pt(border_width)
    else:
        shape.line.fill.background()
    return shape

def add_speaker_note(slide, note_text):
    notes_slide = slide.notes_slide
    tf = notes_slide.notes_text_frame
    tf.text = note_text

def format_bullet_point(paragraph, lead_text, body_text, lead_color=C_HVNH_NAVY, body_color=C_TEXT_DARK, font_size=11.0):
    paragraph.space_before = Pt(3)
    paragraph.space_after = Pt(4)
    paragraph.line_spacing = 1.15
    
    r1 = paragraph.add_run()
    r1.text = lead_text + " "
    r1.font.name = FONT_PRIMARY
    r1.font.size = Pt(font_size)
    r1.font.bold = True
    r1.font.color.rgb = lead_color
    
    r2 = paragraph.add_run()
    r2.text = body_text
    r2.font.name = FONT_PRIMARY
    r2.font.size = Pt(font_size)
    r2.font.color.rgb = body_color

print("🎨 Đang tái thiết kế bộ Slide PowerPoint 21 Trang Executive Master Level chuẩn Học viện Ngân hàng...")

TOTAL_SLIDES = 21

# ==============================================================================
# SLIDE 1: HERO TITLE SLIDE (ĐẲNG CẤP CAO HỌC / THẠC SĨ HVNH)
# ==============================================================================
s1 = prs.slides.add_slide(blank_layout)
set_bg(s1, C_HVNH_NAVY)

top_bar = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(0.12))
top_bar.fill.solid()
top_bar.fill.fore_color.rgb = C_HVNH_ORANGE
top_bar.line.fill.background()

tb_bav = s1.shapes.add_textbox(Inches(1.0), Inches(0.9), Inches(11.333), Inches(0.5))
tf_bav = tb_bav.text_frame
tf_bav.margin_left = tf_bav.margin_right = tf_bav.margin_top = tf_bav.margin_bottom = 0
p_bav = tf_bav.paragraphs[0]
r = p_bav.add_run()
r.text = "🏛️ HỌC VIỆN NGÂN HÀNG (BANKING ACADEMY OF VIETNAM)  •  KHOA HỆ THỐNG THÔNG TIN QUẢN LÝ"
r.font.name = FONT_PRIMARY
r.font.size = Pt(12)
r.font.bold = True
r.font.color.rgb = C_HVNH_GOLD

tb_ttl1 = s1.shapes.add_textbox(Inches(1.0), Inches(1.5), Inches(11.333), Inches(3.2))
tf_ttl1 = tb_ttl1.text_frame
tf_ttl1.word_wrap = True
tf_ttl1.margin_left = tf_ttl1.margin_right = tf_ttl1.margin_top = tf_ttl1.margin_bottom = 0

p1 = tf_ttl1.paragraphs[0]
p1.text = "BÁO CÁO BÀI TẬP GIỮA KỲ CHUYÊN ĐỀ CAO HỌC"
p1.font.name = FONT_PRIMARY
p1.font.size = Pt(13.5)
p1.font.bold = True
p1.font.color.rgb = RGBColor(186, 230, 253)
p1.space_after = Pt(6)

p2 = tf_ttl1.add_paragraph()
p2.text = "XỬ LÝ DỮ LIỆU & KHAI PHÁ DỮ LIỆU"
p2.font.name = FONT_TITLE
p2.font.size = Pt(28)
p2.font.bold = True
p2.font.color.rgb = C_WHITE
p2.space_after = Pt(4)

p3 = tf_ttl1.add_paragraph()
p3.text = "PHÂN TÍCH HÀNH VI, PHÂN CỤM & DỰ BÁO NGUY CƠ RỜI BỎ"
p3.font.name = FONT_TITLE
p3.font.size = Pt(22)
p3.font.bold = True
p3.font.color.rgb = RGBColor(254, 215, 170)
p3.space_after = Pt(2)

p4 = tf_ttl1.add_paragraph()
p4.text = "CỦA KHÁCH HÀNG THẺ TÍN DỤNG (BANK CUSTOMER CHURN)"
p4.font.name = FONT_TITLE
p4.font.size = Pt(22)
p4.font.bold = True
p4.font.color.rgb = RGBColor(254, 215, 170)

divider = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.0), Inches(4.85), Inches(11.333), Inches(0.02))
divider.fill.solid()
divider.fill.fore_color.rgb = RGBColor(51, 65, 85)
divider.line.fill.background()

meta_items = [
    ("👤 HỌC VIÊN THỰC HIỆN", "ĐỖ VĂN ĐẠT", "Chuyên ngành Business Analytics"),
    ("📚 HỌC PHẦN NGHIÊN CỨU", "PHÂN TÍCH DỮ LIỆU KINH DOANH", "Business Analytics — HVNH"),
    ("📊 BỘ DỮ LIỆU THỰC NGHIỆM", "BANKCHURNERS.CSV", "10,127 quan sát • 23 thuộc tính"),
    ("📅 NIÊN KHÓA ĐÀO TẠO", "NĂM HỌC 2025 - 2026", "Hà Nội, Năm 2026")
]

for idx, (label, val1, val2) in enumerate(meta_items):
    c_left = Inches(1.0 + idx * 2.9)
    card = create_card(s1, c_left, Inches(5.15), Inches(2.7), Inches(1.65), bg_color=RGBColor(15, 31, 56), border_color=RGBColor(30, 58, 102))
    
    tb = s1.shapes.add_textbox(c_left + Inches(0.15), Inches(5.3), Inches(2.4), Inches(1.35))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    
    p = tf.paragraphs[0]
    p.text = label
    p.font.name = FONT_PRIMARY
    p.font.size = Pt(9.5)
    p.font.bold = True
    p.font.color.rgb = C_HVNH_GOLD
    p.space_after = Pt(3)
    
    p = tf.add_paragraph()
    p.text = val1
    p.font.name = FONT_PRIMARY
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = C_WHITE
    p.space_after = Pt(2)
    
    p = tf.add_paragraph()
    p.text = val2
    p.font.name = FONT_PRIMARY
    p.font.size = Pt(9.5)
    p.font.color.rgb = RGBColor(148, 163, 184)

add_speaker_note(s1, 
    "Kính chào Quý Thầy/Cô trong Hội đồng và các bạn học viên cao học.\n"
    "Em tên là Đỗ Văn Đạt, học viên chuyên ngành Business Analytics tại Học viện Ngân hàng. "
    "Hôm nay, em xin phép được báo cáo kết quả nghiên cứu đề tài: 'Xử lý Dữ liệu và Khai phá Dữ liệu Dự báo Nguy cơ Rời bỏ của Khách hàng Thẻ Tín dụng' trên tập dữ liệu thực nghiệm BankChurners.\n"
    "Nghiên cứu này không dừng lại ở việc so sánh độ chính xác của các thuật toán học máy, mà trọng tâm là thiết lập một cầu nối hoàn chỉnh từ khai phá dữ liệu hành vi, giải thích mô hình bằng XAI cho đến tối ưu hóa bài toán kinh tế giữ chân khách hàng cho ngân hàng thương mại."
)

# ==============================================================================
# SLIDE 2: MỤC LỤC & CẤU TRÚC BÁO CÁO (AGENDA — 5 TRỤ CỘT CHIẾN LƯỢC)
# ==============================================================================
s2 = prs.slides.add_slide(blank_layout)
set_bg(s2)
add_header(s2, "Cấu Trúc Bài Báo Cáo: 5 Trụ Cột Nghiên Cứu Từ Khai Phá Dữ Liệu Đến Tối Ưu Hóa Kinh Doanh", 
           category_badge="MỤC LỤC & LỘ TRÌNH")
add_footer(s2, 2, TOTAL_SLIDES)

agenda_items = [
    ("01", "TỔNG QUAN & BỐI CẢNH", "Slide 03 — 04", 
     ["Bài toán kinh tế mảng thẻ tín dụng", "So sánh chi phí CAC vs CRC (gấp 5-7 lần)", "Executive Abstract & Lead Takeaway"], C_HVNH_NAVY),
    ("02", "PHƯƠNG PHÁP & TIỀN XỬ LÝ", "Slide 05 — 06", 
     ["Kiến trúc Pipeline 4 giai đoạn chuẩn mực", "Làm sạch & Rà soát rò rỉ nhãn Naive Bayes", "Kiến tạo 5 biến phái sinh tài chính sâu sắc"], C_BLUE_CYAN),
    ("03", "KHAI PHÁ DỮ LIỆU & PHÂN CỤM", "Slide 07 — 13", 
     ["Khai phá EDA 6 chiều hành vi then chốt", "Kiểm định thống kê t-test & Chi-square", "Phân cụm K-Means & Giảm chiều PCA (k=4)"], C_HVNH_GOLD),
    ("04", "MÔ HÌNH HÓA DỰ BÁO & XAI", "Slide 14 — 17", 
     ["Huấn luyện & Đánh giá đối đầu 4 thuật toán", "XGBoost dẫn đầu: ROC-AUC 0.9930, Recall 91.4%", "Giải thích XAI & Tối ưu hóa ngưỡng t = 0.42"], C_HVNH_ORANGE),
    ("05", "CHIẾN LƯỢC GIỮ CHÂN & ROI", "Slide 18 — 21", 
     ["Phác họa 3 Chân dung khách hàng rời bỏ", "Khung chiến lược 4 tầng & Cảnh báo sớm EWS", "Mô phỏng tài chính ROI 500% & Tổng kết Q&A"], C_ACCENT_GREEN)
]

card_w = Inches(2.22)
gap = Inches(0.16)
for idx, (num, title, slides, desc_list, accent_col) in enumerate(agenda_items):
    c_left = Inches(0.8 + idx * (2.22 + 0.16))
    create_card(s2, c_left, Inches(1.6), card_w, Inches(5.15))
    
    # Top Accent Strip
    strip = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, c_left + Inches(0.12), Inches(1.72), card_w - Inches(0.24), Inches(0.06))
    strip.fill.solid()
    strip.fill.fore_color.rgb = accent_col
    strip.line.fill.background()
    
    tb = s2.shapes.add_textbox(c_left + Inches(0.15), Inches(1.88), card_w - Inches(0.3), Inches(4.75))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    
    # Pillar Number
    p_num = tf.paragraphs[0]
    p_num.text = num
    p_num.font.name = FONT_TITLE
    p_num.font.size = Pt(26)
    p_num.font.bold = True
    p_num.font.color.rgb = accent_col
    p_num.space_after = Pt(1)
    
    # Pillar Title
    p_ttl = tf.add_paragraph()
    p_ttl.text = title
    p_ttl.font.name = FONT_PRIMARY
    p_ttl.font.size = Pt(11.5)
    p_ttl.font.bold = True
    p_ttl.font.color.rgb = C_HVNH_NAVY
    p_ttl.space_after = Pt(2)
    
    # Slide Range Badge
    p_rng = tf.add_paragraph()
    p_rng.text = f"[{slides}]"
    p_rng.font.name = FONT_PRIMARY
    p_rng.font.size = Pt(9.5)
    p_rng.font.bold = True
    p_rng.font.color.rgb = C_TEXT_MUTED
    p_rng.space_after = Pt(8)
    
    # Bullets
    for b in desc_list:
        p_b = tf.add_paragraph()
        format_bullet_point(p_b, "•", b, lead_color=accent_col, body_color=C_TEXT_DARK, font_size=10.0)

add_speaker_note(s2,
    "Kính thưa Thầy/Cô, để Hội đồng tiện theo dõi toàn diện mạch lập luận, bài báo cáo được tổ chức chặt chẽ theo 5 trụ cột nghiên cứu MECE:\n"
    "Thứ nhất là Tổng quan bối cảnh kinh tế và bài toán chi phí giữ chân khách hàng.\n"
    "Thứ hai là Phương pháp luận xây dựng Pipeline và khâu Feature Engineering tạo lập 5 biến phái sinh.\n"
    "Thứ ba là Khai phá dữ liệu thực nghiệm qua 6 chiều hành vi EDA và phân cụm K-Means.\n"
    "Thứ tư là Huấn luyện 4 mô hình học máy, giải thích XAI và tối ưu hóa ngưỡng cắt xác suất theo chi phí.\n"
    "Và cuối cùng là Khung khuyến nghị quản trị 4 tầng, mô phỏng tài chính ROI 500% cùng định hướng tương lai.\n"
    "Sau đây em xin đi vào nội dung tóm tắt điều hành đầu tiên."
)

# ==============================================================================
# SLIDE 3: EXECUTIVE SUMMARY (TỔNG HỢP ĐIỀU HÀNH 4 TRỤ CỘT)
# ==============================================================================
s3 = prs.slides.add_slide(blank_layout)
set_bg(s3)
add_header(s3, "XGBoost Đạt ROC-AUC 0.9930, Tối Ưu Hóa Ngưỡng t = 0.42 Mang Lại ROI 500% (+400K USD/Năm)", 
           category_badge="TỔNG QUAN ĐIỀU HÀNH")
add_footer(s3, 3, TOTAL_SLIDES)

exec_cards = [
    ("16.07%", "TỶ LỆ RỜI BỎ TỰ NHIÊN", C_ACCENT_RED, [
        ("Thực trạng nhức nhối:", "1,627/10,127 khách hàng đã đóng thẻ tín dụng."),
        ("Mất cân bằng lớp:", "Tỷ lệ 1:5.22, đòi hỏi tối ưu chỉ số Recall & PR-AUC."),
        ("Tổn thất doanh thu:", "Mất phí thường niên, lãi vay quay vòng và phí quẹt thẻ.")
    ]),
    ("0.9930", "ROC-AUC (MÔ HÌNH XGBOOST)", C_HVNH_NAVY, [
        ("Hiệu năng vượt trội:", "Recall đạt 91.38%, F1-Score đạt 91.23% trên tập Test."),
        ("Độ chính xác cao:", "Chỉ bỏ sót 28/325 khách hàng rời bỏ thực tế."),
        ("Khả năng phân tách:", "Vượt xa Logistic Regression (0.9348) và Random Forest (0.9892).")
    ]),
    ("t = 0.42", "NGƯỠNG CẮT TỐI ƯU KINH TẾ", C_HVNH_ORANGE, [
        ("Thay thế ngưỡng 0.50:", "Tối ưu hóa bài toán Chi phí - Lợi ích thực tiễn."),
        ("Cân bằng rủi ro:", "Đón đầu thêm khách hàng churn với chi phí can thiệp thấp."),
        ("Hiệu quả can thiệp:", "Đạt tỷ lệ giữ chân kỳ vọng 75% trên nhóm rủi ro cao.")
    ]),
    ("+$400K", "LỢI NHUẬN RÒNG / NĂM (ROI = 500%)", C_ACCENT_GREEN, [
        ("Quy mô 10,000 khách:", "Giữ chân thành công 960 khách hàng có nguy cơ rời bỏ."),
        ("Doanh thu bảo vệ:", "$480,000 USD giá trị trọn đời (CLV = $500/khách)."),
        ("Tỷ suất sinh lời:", "Chi phí can thiệp $80,000 USD mang lại lợi nhuận vượt bậc.")
    ])
]

for idx, (kpi, title, col, bullets) in enumerate(exec_cards):
    c_left = Inches(0.8 + idx * 2.95)
    create_card(s3, c_left, Inches(1.6), Inches(2.8), Inches(5.15))
    
    # Accent top strip
    strip = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, c_left + Inches(0.15), Inches(1.72), Inches(2.5), Inches(0.06))
    strip.fill.solid()
    strip.fill.fore_color.rgb = col
    strip.line.fill.background()
    
    tb = s3.shapes.add_textbox(c_left + Inches(0.18), Inches(1.88), Inches(2.44), Inches(4.75))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    
    p_kpi = tf.paragraphs[0]
    p_kpi.text = kpi
    p_kpi.font.name = FONT_TITLE
    p_kpi.font.size = Pt(28)
    p_kpi.font.bold = True
    p_kpi.font.color.rgb = col
    p_kpi.space_after = Pt(2)
    
    p_ttl = tf.add_paragraph()
    p_ttl.text = title
    p_ttl.font.name = FONT_PRIMARY
    p_ttl.font.size = Pt(11)
    p_ttl.font.bold = True
    p_ttl.font.color.rgb = C_HVNH_NAVY
    p_ttl.space_after = Pt(8)
    
    for lead, b_text in bullets:
        p_b = tf.add_paragraph()
        format_bullet_point(p_b, lead, b_text, lead_color=C_HVNH_NAVY, body_color=C_TEXT_DARK, font_size=10.0)

add_speaker_note(s3,
    "Kính thưa Hội đồng, theo nguyên lý Kim tự tháp Pyramid Principle của McKinsey, em xin phép trình bày ngay 4 kết quả phát hiện trọng tâm nhất của đề tài:\n"
    "Thứ nhất, tỷ lệ rời bỏ tự nhiên trong tập dữ liệu đạt 16.07%, gây tổn thất nặng nề đến doanh thu lãi vay và phí giao dịch.\n"
    "Thứ hai, mô hình XGBoost Classifier vượt trội hoàn toàn với ROC-AUC 0.9930 và khả năng bắt trúng 91.38% khách hàng rời bỏ.\n"
    "Thứ ba, nghiên cứu đã dịch chuyển ngưỡng quyết định từ 0.50 mặc định về ngưỡng tối ưu kinh tế t = 0.42.\n"
    "Và thứ tư, khi mô phỏng tài chính trên quy mô 10,000 chủ thẻ, hệ thống giúp mang lại 400,000 USD lợi nhuận ròng hàng năm, tương ứng tỷ suất sinh lời ROI lên đến 500%."
)

# ==============================================================================
# SLIDE 4: BỐI CẢNH & BÀI TOÁN KINH TẾ GIỮ CHÂN KHÁCH HÀNG
# ==============================================================================
s4 = prs.slides.add_slide(blank_layout)
set_bg(s4)
add_header(s4, "Chi Phí Thu Hút Mới (CAC) Gấp 5-7 Lần Chi Phí Giữ Chân (CRC): Yêu Cầu Chuyển Đổi Sang Dự Báo Chủ Động", 
           category_badge="BỐI CẢNH KINH DOANH")
add_footer(s4, 4, TOTAL_SLIDES)

create_card(s4, Inches(0.8), Inches(1.6), Inches(5.7), Inches(5.15))
tb_c1 = s4.shapes.add_textbox(Inches(1.05), Inches(1.85), Inches(5.2), Inches(4.7))
tf_c1 = tb_c1.text_frame
tf_c1.word_wrap = True
tf_c1.margin_left = tf_c1.margin_right = tf_c1.margin_top = tf_c1.margin_bottom = 0

p = tf_c1.paragraphs[0]
p.text = "🏛️ Thực Trạng Ngành Thẻ & Thách Thức Churn"
p.font.name = FONT_TITLE
p.font.size = Pt(15)
p.font.bold = True
p.font.color.rgb = C_HVNH_NAVY
p.space_after = Pt(8)

bullets_c1 = [
    ("Biên lợi nhuận cao:", "Mảng thẻ tín dụng đóng góp lớn vào thu nhập ngoài lãi (NFI) và biên lãi thuần (NIM) của các ngân hàng thương mại."),
    ("Cạnh tranh gay gắt:", "Khách hàng dễ dàng chuyển đổi sang ngân hàng đối thủ do các chương trình hoàn tiền (cashback) và miễn phí thường niên."),
    ("Chảy máu doanh thu:", "Mất 16.07% khách hàng đồng nghĩa với việc mất đi toàn bộ dòng tiền chi tiêu thẻ, phí giao dịch POS/E-com và lãi quay vòng."),
    ("Quy tắc Reichheld (Bain & Co.):", "Tăng tỷ lệ giữ chân khách hàng thêm 5% có thể giúp gia tăng lợi nhuận từ 25% đến 95%.")
]
for lead, body in bullets_c1:
    p_b = tf_c1.add_paragraph()
    format_bullet_point(p_b, lead, body, font_size=10.5)

create_card(s4, Inches(6.8), Inches(1.6), Inches(5.733), Inches(5.15))
tb_c2 = s4.shapes.add_textbox(Inches(7.05), Inches(1.85), Inches(5.233), Inches(4.7))
tf_c2 = tb_c2.text_frame
tf_c2.word_wrap = True
tf_c2.margin_left = tf_c2.margin_right = tf_c2.margin_top = tf_c2.margin_bottom = 0

p = tf_c2.paragraphs[0]
p.text = "💰 Bài Toán Kinh Tế: CAC vs CRC"
p.font.name = FONT_TITLE
p.font.size = Pt(15)
p.font.bold = True
p.font.color.rgb = C_HVNH_ORANGE
p.space_after = Pt(8)

bullets_c2 = [
    ("Chi phí thu hút mới (CAC):", "Dao động từ $250 - $300 USD cho chi phí marketing, sales quà tặng, thẩm định hồ sơ và cấp phát thẻ vật lý."),
    ("Chi phí giữ chân (CRC):", "Chỉ khoảng $40 - $50 USD cho các chương trình ưu đãi phí, voucher cá nhân hóa và chăm sóc khách hàng chủ động."),
    ("Hiệu quả kinh tế vượt trội:", "Chi phí tìm kiếm khách hàng mới cao gấp 5 đến 7 lần so với việc giữ chân khách hàng hiện hữu."),
    ("Nhu cầu cấp thiết:", "Chuyển dịch từ mô hình 'ứng phó bị động' khi khách đã nộp đơn hủy thẻ sang 'dự báo chủ động' bằng máy học trước 2-3 tháng.")
]
for lead, body in bullets_c2:
    p_b = tf_c2.add_paragraph()
    format_bullet_point(p_b, lead, body, lead_color=C_HVNH_ORANGE, font_size=10.5)

add_speaker_note(s4,
    "Kính thưa Thầy/Cô, thẻ tín dụng là mảng kinh doanh có biên lợi nhuận cao nhất nhưng cũng chịu áp lực cạnh tranh khốc liệt nhất.\n"
    "Dữ liệu tài chính cho thấy chi phí để phát hành một thẻ tín dụng mới (CAC) lên tới 250 - 300 USD, trong khi chi phí giữ chân (CRC) chỉ khoảng 40 - 50 USD, tức rẻ hơn từ 5 đến 7 lần.\n"
    "Theo nghiên cứu kinh điển của Bain & Company, chỉ cần cải thiện 5% tỷ lệ giữ chân, lợi nhuận ngân hàng có thể tăng từ 25% đến 95%. "
    "Do đó, việc ứng dụng Machine Learning để xây dựng hệ thống cảnh báo sớm (Early Warning System) là yêu cầu sống còn nhằm giữ chân khách hàng trước khi họ chính thức rời bỏ."
)

# ==============================================================================
# SLIDE 5: PHƯƠNG PHÁP LUẬN & KIẾN TRÚC PIPELINE 4 BƯỚC
# ==============================================================================
s5 = prs.slides.add_slide(blank_layout)
set_bg(s5)
add_header(s5, "Khung Nghiên Cứu Thực Nghiệm 4 Giai Đoạn Từ Tiền Xử Lý Đến Triển Khai XAI Thực Tiễn", 
           category_badge="PHƯƠNG PHÁP LUẬN")
add_footer(s5, 5, TOTAL_SLIDES)

pipe_steps = [
    ("GIAI ĐOẠN 01", "TIỀN XỬ LÝ & LÀM SẠCH", C_HVNH_NAVY, [
        ("Thu thập:", "Bộ dữ liệu 10,127 quan sát, 23 thuộc tính."),
        ("Làm sạch:", "Kiểm tra null, chuẩn hóa kiểu dữ liệu."),
        ("Rò rỉ dữ liệu:", "Loại bỏ 2 cột Naive Bayes phân loại sẵn."),
        ("Feature Engineering:", "Kiến tạo 5 biến phái sinh tài chính.")
    ]),
    ("GIAI ĐOẠN 02", "EDA & DATA MINING", C_BLUE_CYAN, [
        ("Phân tích đơn/đa biến:", "Đánh giá phân bố 6 chiều hành vi."),
        ("Kiểm định thống kê:", "T-test & Chi-square xác nhận p < 0.001."),
        ("Phân cụm K-Means:", "Tối ưu k=4 bằng Elbow & Silhouette."),
        ("Giảm chiều PCA:", "Trực quan hóa không gian 2D rõ nét.")
    ]),
    ("GIAI ĐOẠN 03", "MÔ HÌNH HÓA DỰ BÁO", C_HVNH_ORANGE, [
        ("Chia dữ liệu:", "Stratified 80/20 bảo toàn tỷ lệ 16.07%."),
        ("Huấn luyện 4 mô hình:", "Logistic Regression, RF, SVM, XGBoost."),
        ("Tối ưu Hyperparameter:", "Cross-Validation 5-Fold."),
        ("Đánh giá toàn diện:", "So sánh ROC-AUC, Recall, Precision, F1.")
    ]),
    ("GIAI ĐOẠN 04", "TỐI ƯU KINH TẾ & XAI", C_ACCENT_GREEN, [
        ("Explainable AI (XAI):", "Xác định 5 đòn bẩy rủi ro cốt lõi."),
        ("Tối ưu ngưỡng cắt:", "Xác lập ngưỡng t = 0.42 tối ưu Net Profit."),
        ("Phác họa Persona:", "3 Chân dung khách hàng điển hình."),
        ("Khung chiến lược:", "Khung 4 tầng EWS & Mô phỏng ROI 500%.")
    ])
]

for idx, (stage, name, col, items) in enumerate(pipe_steps):
    c_left = Inches(0.8 + idx * 2.95)
    create_card(s5, c_left, Inches(1.6), Inches(2.8), Inches(5.15))
    
    # Stage banner
    s_banner = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, c_left + Inches(0.15), Inches(1.72), Inches(2.5), Inches(0.35))
    s_banner.fill.solid()
    s_banner.fill.fore_color.rgb = col
    s_banner.line.fill.background()
    tf_sb = s_banner.text_frame
    tf_sb.margin_left = tf_sb.margin_right = tf_sb.margin_top = tf_sb.margin_bottom = 0
    p_sb = tf_sb.paragraphs[0]
    p_sb.alignment = PP_ALIGN.CENTER
    p_sb.text = stage
    p_sb.font.name = FONT_PRIMARY
    p_sb.font.size = Pt(10)
    p_sb.font.bold = True
    p_sb.font.color.rgb = C_WHITE
    
    tb = s5.shapes.add_textbox(c_left + Inches(0.15), Inches(2.15), Inches(2.5), Inches(4.5))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    
    p_n = tf.paragraphs[0]
    p_n.text = name
    p_n.font.name = FONT_PRIMARY
    p_n.font.size = Pt(11.5)
    p_n.font.bold = True
    p_n.font.color.rgb = C_HVNH_NAVY
    p_n.space_after = Pt(8)
    
    for lead, body in items:
        p_b = tf.add_paragraph()
        format_bullet_point(p_b, lead, body, lead_color=col, font_size=9.8)

add_speaker_note(s5,
    "Kính thưa Hội đồng, cấu trúc phương pháp luận của đề tài được triển khai qua 4 giai đoạn chuẩn mực khoa học dữ liệu:\n"
    "Giai đoạn 1 xử lý dữ liệu thô, loại bỏ rò rỉ nhãn và kiến tạo 5 biến phái sinh tài chính.\n"
    "Giai đoạn 2 tiến hành EDA đa chiều và phân cụm K-Means nhằm bóc tách hành vi khách hàng.\n"
    "Giai đoạn 3 thực hiện huấn luyện và kiểm định chéo Stratified 5-Fold trên 4 thuật toán Machine Learning.\n"
    "Và Giai đoạn 4 kết hợp Explainable AI cùng mô hình tối ưu hóa kinh tế để đưa ra khuyến nghị thực thi.\n"
    "Quy trình khép kín này đảm bảo tính nhất quán từ dữ liệu thực nghiệm đến giá trị ứng dụng kinh doanh."
)

# ==============================================================================
# SLIDE 6: TIỀN XỬ LÝ DỮ LIỆU & FEATURE ENGINEERING
# ==============================================================================
s6 = prs.slides.add_slide(blank_layout)
set_bg(s6)
add_header(s6, "Loại Bỏ Rò Rỉ Nhãn (Naive Bayes) & Kiến Tạo 5 Đặc Trưng Phái Sinh Phản Ánh Bản Chất Hành Vi", 
           category_badge="TIỀN XỬ LÝ & KỸ NGHỆ DỮ LIỆU")
add_footer(s6, 6, TOTAL_SLIDES)

create_card(s6, Inches(0.8), Inches(1.6), Inches(5.7), Inches(5.15))
tb_fe1 = s6.shapes.add_textbox(Inches(1.05), Inches(1.85), Inches(5.2), Inches(4.7))
tf_fe1 = tb_fe1.text_frame
tf_fe1.word_wrap = True
tf_fe1.margin_left = tf_fe1.margin_right = tf_fe1.margin_top = tf_fe1.margin_bottom = 0

p = tf_fe1.paragraphs[0]
p.text = "🧹 Làm Sạch & Xử Lý Rò Rỉ Nhãn (Data Leakage)"
p.font.name = FONT_TITLE
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = C_HVNH_NAVY
p.space_after = Pt(8)

bullets_fe1 = [
    ("Quy mô dữ liệu sạch:", "10,127 bản ghi đầy đủ, không phát hiện giá trị khuyết thiếu (Null/NaN)."),
    ("Loại bỏ Data Leakage:", "Loại bỏ hoàn toàn 2 cột phân loại Naive Bayes có sẵn trong dataset gốc (tính toán trước xác suất), đảm bảo tính khách quan thực nghiệm."),
    ("Mã hóa nhãn (Target Encoding):", "Thuộc tính Attrited Customer chuyển thành nhãn 1 (1,627 khách), Existing Customer chuyển thành nhãn 0 (8,500 khách)."),
    ("Mã hóa định danh (Dummy Variables):", "Áp dụng One-Hot Encoding cho các biến phân loại danh nghĩa và Ordinal Encoding cho trình độ học vấn / thu nhập.")
]
for lead, body in bullets_fe1:
    p_b = tf_fe1.add_paragraph()
    format_bullet_point(p_b, lead, body, font_size=10.5)

create_card(s6, Inches(6.8), Inches(1.6), Inches(5.733), Inches(5.15))
tb_fe2 = s6.shapes.add_textbox(Inches(7.05), Inches(1.85), Inches(5.233), Inches(4.7))
tf_fe2 = tb_fe2.text_frame
tf_fe2.word_wrap = True
tf_fe2.margin_left = tf_fe2.margin_right = tf_fe2.margin_top = tf_fe2.margin_bottom = 0

p = tf_fe2.paragraphs[0]
p.text = "⚙️ 5 Đặc Trưng Phái Sinh Kiến Tạo Mới"
p.font.name = FONT_TITLE
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = C_HVNH_ORANGE
p.space_after = Pt(8)

bullets_fe2 = [
    ("1. Trans_Ct_Density (Mật độ quẹt thẻ):", "Tỷ số giữa Total_Trans_Ct và Months_on_book. Phản ánh thói quen sử dụng thẻ thường nhật của khách hàng."),
    ("2. Trans_Amt_per_Capita (Chi tiêu bình quân):", "Total_Trans_Amt / Total_Trans_Ct. Nhận diện các giao dịch giá trị lớn so với giao dịch vi mô."),
    ("3. Revolving_Ratio (Tỷ lệ nợ quay vòng):", "Total_Revolving_Bal / Credit_Limit. Đo lường mức độ phụ thuộc vào tín dụng ngân hàng."),
    ("4. Total_Interaction_Ct (Tổng tương tác):", "Contacts_Count_12_mon + Months_Inactive_12_mon. Chỉ số tổng hợp về mức độ rủi ro trải nghiệm."),
    ("5. Open_To_Buy_Ratio (Tỷ lệ khả dụng):", "Avg_Open_To_Buy / Credit_Limit. Đánh giá dung lượng hạn mức chưa sử dụng.")
]
for lead, body in bullets_fe2:
    p_b = tf_fe2.add_paragraph()
    format_bullet_point(p_b, lead, body, lead_color=C_HVNH_ORANGE, font_size=10.0)

add_speaker_note(s6,
    "Kính thưa Thầy/Cô, trong khâu tiền xử lý, một điểm mấu chốt là nhóm nghiên cứu đã chủ động loại bỏ 2 cột phân loại Naive Bayes có sẵn trong bộ dữ liệu gốc.\n"
    "Nếu giữ lại 2 cột này, mô hình sẽ gặp hiện tượng rò rỉ dữ liệu (Data Leakage) nghiêm trọng và cho kết quả ảo tưởng.\n"
    "Bên cạnh đó, khâu Feature Engineering đã kiến tạo thêm 5 biến phái sinh tài chính sâu sắc như mật độ giao dịch hay tỷ lệ nợ quay vòng. "
    "Các biến này phản ánh chân thực động thái giảm dần chi tiêu của khách hàng trước khi chính thức hủy thẻ."
)

# ==============================================================================
# SLIDE 7: EDA 1 — PHÂN BỐ BIẾN MỤC TIÊU & MẤT CÂN BẰNG LỚP
# ==============================================================================
s7 = prs.slides.add_slide(blank_layout)
set_bg(s7)
add_header(s7, "Tỷ Lệ Rời Bỏ 16.07% (Tỷ Lệ Mất Cân Bằng 1:5.22): Đặt Trọng Tâm Đánh Giá Vào Recall & PR-AUC", 
           category_badge="KHAI PHÁ EDA — BIẾN MỤC TIÊU")
add_footer(s7, 7, TOTAL_SLIDES)

create_card(s7, Inches(0.8), Inches(1.55), Inches(6.8), Inches(5.2))
img_p7 = os.path.join(FIG_DIR, "01_churn_distribution.png")
if os.path.exists(img_p7):
    s7.shapes.add_picture(img_p7, Inches(0.95), Inches(1.75), width=Inches(6.5))

create_card(s7, Inches(7.9), Inches(1.55), Inches(4.633), Inches(5.2))
tb_e1 = s7.shapes.add_textbox(Inches(8.15), Inches(1.75), Inches(4.133), Inches(4.8))
tf_e1 = tb_e1.text_frame
tf_e1.word_wrap = True
tf_e1.margin_left = tf_e1.margin_right = tf_e1.margin_top = tf_e1.margin_bottom = 0

p = tf_e1.paragraphs[0]
p.text = "📌 Ý Nghĩa Nghiệp Vụ & Quyết Định Mô Hình"
p.font.name = FONT_TITLE
p.font.size = Pt(13)
p.font.bold = True
p.font.color.rgb = C_HVNH_NAVY
p.space_after = Pt(6)

bullets_e1 = [
    ("Mất cân bằng lớp (Class Imbalance):", "Tập dữ liệu gồm 8,500 khách hàng ở lại (83.93%) và 1,627 khách hàng rời bỏ (16.07%), tương ứng tỷ lệ 1:5.22."),
    ("Cạm bẫy độ chính xác (Accuracy Paradox):", "Một mô hình ngây thơ luôn đoán 'Ở lại' sẽ đạt ngay Accuracy = 83.93% nhưng hoàn toàn vô dụng trong việc bắt khách hàng Churn."),
    ("Lựa chọn Metric đánh giá:", "Đề tài xác lập ưu tiên tối thượng cho chỉ số Recall (khả năng phát hiện đúng khách Churn) và diện tích dưới đường cong PR-AUC / ROC-AUC."),
    ("Chiến lược chia mẫu:", "Sử dụng Stratified K-Fold để đảm bảo tỷ lệ 16.07% đồng nhất trên cả tập Train và Test.")
]
for lead, body in bullets_e1:
    p_b = tf_e1.add_paragraph()
    format_bullet_point(p_b, lead, body, font_size=10.0)

add_speaker_note(s7,
    "Kính thưa Hội đồng, biến mục tiêu Attrition_Flag cho thấy tỷ lệ rời bỏ tự nhiên trong danh mục là 16.07%, tức cứ 6 khách hàng thì có 1 khách hàng đóng thẻ.\n"
    "Tỷ lệ mất cân bằng 1:5.22 này đặt ra thách thức về 'Cạm bẫy độ chính xác' (Accuracy Paradox). "
    "Nếu chỉ nhìn vào Accuracy, một mô hình dự báo toàn bộ khách hàng ở lại vẫn đạt 83.93% nhưng ngân hàng sẽ mất trắng toàn bộ khách hàng churn.\n"
    "Vì vậy, nghiên cứu chuyển hướng đánh giá toàn bộ các thuật toán sang thang đo Recall, F1-Score và ROC-AUC để đảm bảo không bỏ sót khách hàng rủi ro."
)

# ==============================================================================
# SLIDE 8: EDA 2 — PHÂN TÍCH NHÂN KHẨU HỌC & RỦI RO 2 ĐẦU THU NHẬP
# ==============================================================================
s8 = prs.slides.add_slide(blank_layout)
set_bg(s8)
add_header(s8, "Khách Hàng Nữ (Churn 17.36%) & Nhóm Thu Nhập Cao $120K+ (Churn 17.33%) Tiềm Ẩn Rủi Ro Cao Nhất", 
           category_badge="KHAI PHÁ EDA — NHÂN KHẨU HỌC")
add_footer(s8, 8, TOTAL_SLIDES)

create_card(s8, Inches(0.8), Inches(1.55), Inches(6.8), Inches(5.2))
img_p8 = os.path.join(FIG_DIR, "02_demographic_churn.png")
if os.path.exists(img_p8):
    s8.shapes.add_picture(img_p8, Inches(0.95), Inches(1.75), width=Inches(6.5))

create_card(s8, Inches(7.9), Inches(1.55), Inches(4.633), Inches(5.2))
tb_e2 = s8.shapes.add_textbox(Inches(8.15), Inches(1.75), Inches(4.133), Inches(4.8))
tf_e2 = tb_e2.text_frame
tf_e2.word_wrap = True
tf_e2.margin_left = tf_e2.margin_right = tf_e2.margin_top = tf_e2.margin_bottom = 0

p = tf_e2.paragraphs[0]
p.text = "👥 Insight Nhân Khẩu Học & Hành Vi"
p.font.name = FONT_TITLE
p.font.size = Pt(13)
p.font.bold = True
p.font.color.rgb = C_HVNH_NAVY
p.space_after = Pt(6)

bullets_e2 = [
    ("Yếu tố giới tính (Gender):", "Khách hàng Nữ có tỷ lệ rời bỏ 17.36%, cao hơn đáng kể so với Nam giới (14.62%), phản ánh sự nhạy cảm cao hơn với các chương trình ưu đãi tiêu dùng."),
    ("Độ tuổi rủi ro cao:", "Độ tuổi tập trung từ 40 - 50 tuổi (trung bình 46.3 tuổi), là nhóm khách hàng trung niên có nhu cầu tài chính phức tạp và sẵn sàng đổi thẻ."),
    ("Nghịch lý 2 đầu thu nhập:", "Tỷ lệ rời bỏ cao nhất ở 2 nhóm cực đoan: Dưới $40K (17.19% - áp lực kinh tế) và Trên $120K (17.33% - khách hàng VIP bị đối thủ săn đón)."),
    ("Người phụ thuộc (Dependents):", "Khách hàng có 2 - 3 người phụ thuộc có tỷ lệ rời bỏ cao nhất do áp lực chi tiêu gia đình lớn.")
]
for lead, body in bullets_e2:
    p_b = tf_e2.add_paragraph()
    format_bullet_point(p_b, lead, body, font_size=10.0)

add_speaker_note(s8,
    "Kính thưa Thầy/Cô, phân tích nhân khẩu học chỉ ra hai phát hiện rất đáng chú ý về mặt hành vi:\n"
    "Thứ nhất, khách hàng nữ có tỷ lệ rời bỏ 17.36%, cao hơn nam giới. Phân tích sâu cho thấy nhóm này rất nhạy cảm với các chương trình tích điểm mua sắm và hoàn tiền siêu thị.\n"
    "Thứ hai là 'Hiện tượng phân hóa rủi ro 2 đầu thu nhập': Tỷ lệ rời bỏ tăng vọt ở nhóm thu nhập thấp dưới 40,000 USD do nhạy cảm với phí thường niên, và nhóm siêu giàu trên 120,000 USD do bị các ngân hàng đối thủ liên tục chèo kéo bằng các dòng thẻ Signature/Platinum cao cấp."
)

# ==============================================================================
# SLIDE 9: EDA 3 — HÀNH VI GIAO DỊCH (VÙNG BÁO ĐỘNG ĐỎ)
# ==============================================================================
s9 = prs.slides.add_slide(blank_layout)
set_bg(s9)
add_header(s9, "Ranh Giới Rủi Ro Sắc Nét: Giao Dịch Dưới 55 Lần & Chi Tiêu Dưới $3,000 Là Vùng Nguy Cơ Rời Bỏ Đỏ", 
           category_badge="KHAI PHÁ EDA — HÀNH VI GIAO DỊCH")
add_footer(s9, 9, TOTAL_SLIDES)

create_card(s9, Inches(0.8), Inches(1.55), Inches(6.8), Inches(5.2))
img_p9 = os.path.join(FIG_DIR, "03_transaction_behavior_churn.png")
if os.path.exists(img_p9):
    s9.shapes.add_picture(img_p9, Inches(0.95), Inches(1.75), width=Inches(6.5))

create_card(s9, Inches(7.9), Inches(1.55), Inches(4.633), Inches(5.2))
tb_e3 = s9.shapes.add_textbox(Inches(8.15), Inches(1.75), Inches(4.133), Inches(4.8))
tf_e3 = tb_e3.text_frame
tf_e3.word_wrap = True
tf_e3.margin_left = tf_e3.margin_right = tf_e3.margin_top = tf_e3.margin_bottom = 0

p = tf_e3.paragraphs[0]
p.text = "💳 Ranh Giới Giao Dịch Quyết Định"
p.font.name = FONT_TITLE
p.font.size = Pt(13)
p.font.bold = True
p.font.color.rgb = C_HVNH_NAVY
p.space_after = Pt(6)

bullets_e3 = [
    ("Số lượng giao dịch (Total_Trans_Ct):", "Khách hàng rời bỏ chỉ thực hiện trung bình 44.9 giao dịch/năm, so với 68.7 giao dịch của nhóm khách hàng ở lại."),
    ("Vùng nguy cơ báo động đỏ:", "Nếu số lần quẹt thẻ < 55 lần/năm (dưới 4.5 lần/tháng), xác suất khách hàng rời bỏ tăng vọt lên trên 60%."),
    ("Tổng giá trị chi tiêu (Total_Trans_Amt):", "Khách hàng Churn chi tiêu trung bình $3,095 USD/năm so với $4,654 USD của khách hàng trung thành."),
    ("Quy luật tương quan phi tuyến:", "Tồn tại một phân cụm khách hàng rời bỏ rõ rệt tập trung chặt chẽ ở góc trái bên dưới của biểu đồ phân tán (Scatter Plot).")
]
for lead, body in bullets_e3:
    p_b = tf_e3.add_paragraph()
    format_bullet_point(p_b, lead, body, font_size=10.0)

add_speaker_note(s9,
    "Kính thưa Hội đồng, biểu đồ phân tán giữa số lượng giao dịch và giá trị chi tiêu thể hiện một ranh giới phân tách cực kỳ sắc nét.\n"
    "Khách hàng ở lại quẹt thẻ trung bình gần 69 lần/năm, trong khi khách hàng rời bỏ chỉ đạt 44.9 lần. "
    "Đặc biệt, dữ liệu chỉ ra vùng nguy cơ báo động đỏ: Bất kỳ khách hàng nào quẹt thẻ dưới 55 lần và tổng chi tiêu dưới 3,000 USD thì xác suất rời bỏ lên tới trên 60%.\n"
    "Đây chính là tín hiệu kích hoạt quan trọng nhất để hệ thống ngân hàng tự động đưa khách hàng vào luồng chăm sóc đặc biệt."
)

# ==============================================================================
# SLIDE 10: EDA 4 — CHỈ SỐ TÀI CHÍNH (HIỆN TƯỢNG DƯ NỢ VỀ 0)
# ==============================================================================
s10 = prs.slides.add_slide(blank_layout)
set_bg(s10)
add_header(s10, "Hiện Tượng Dư Nợ Quay Vòng Sụt Giảm Về $0 Là Tín Hiệu 'Ngủ Đông' & Chuẩn Bị Đóng Thẻ Rõ Ràng Nhất", 
           category_badge="KHAI PHÁ EDA — CHỈ SỐ TÀI CHÍNH")
add_footer(s10, 10, TOTAL_SLIDES)

create_card(s10, Inches(0.8), Inches(1.55), Inches(6.8), Inches(5.2))
img_p10 = os.path.join(FIG_DIR, "04_financial_ratios_churn.png")
if os.path.exists(img_p10):
    s10.shapes.add_picture(img_p10, Inches(0.95), Inches(1.75), width=Inches(6.5))

create_card(s10, Inches(7.9), Inches(1.55), Inches(4.633), Inches(5.2))
tb_e4 = s10.shapes.add_textbox(Inches(8.15), Inches(1.75), Inches(4.133), Inches(4.8))
tf_e4 = tb_e4.text_frame
tf_e4.word_wrap = True
tf_e4.margin_left = tf_e4.margin_right = tf_e4.margin_top = tf_e4.margin_bottom = 0

p = tf_e4.paragraphs[0]
p.text = "📉 Tín Hiệu Rút Lui Tài Chính Lặng Lẽ"
p.font.name = FONT_TITLE
p.font.size = Pt(13)
p.font.bold = True
p.font.color.rgb = C_HVNH_NAVY
p.space_after = Pt(6)

bullets_e4 = [
    ("Dư nợ quay vòng (Total_Revolving_Bal):", "Khách hàng Churn có dư nợ trung bình chỉ $672 USD so với $1,256 USD của khách hàng ở lại."),
    ("Tỷ lệ nợ về $0 USD:", "Gần 55% khách hàng rời bỏ có dư nợ quay vòng bằng $0 USD tại thời điểm ghi nhận, cho thấy hành vi chủ động tất toán nợ trước khi hủy thẻ."),
    ("Tỷ lệ sử dụng hạn mức (Utilization_Ratio):", "Khách hàng Churn chỉ sử dụng trung bình 16.2% hạn mức, trong khi nhóm trung thành sử dụng tới 29.6%."),
    ("Sụt giảm chi tiêu Q4/Q1 (Total_Ct_Chng_Q4_Q1):", "Chỉ số biến thiên giao dịch sụt giảm mạnh về mức 0.55, phản ánh tần suất giao dịch giảm tới 45% trong các quý gần nhất.")
]
for lead, body in bullets_e4:
    p_b = tf_e4.add_paragraph()
    format_bullet_point(p_b, lead, body, font_size=10.0)

add_speaker_note(s10,
    "Kính thưa Thầy/Cô, phát hiện tài chính quan trọng nhất ở slide này là hiện tượng 'Tất toán dư nợ trước khi đóng thẻ'.\n"
    "Khách hàng sắp rời bỏ thường thanh toán hết toàn bộ số dư quay vòng về 0 USD và giảm tỷ lệ sử dụng hạn mức xuống chỉ còn 16.2%. "
    "Đồng thời, chỉ số giao dịch Q4 so với Q1 sụt giảm tới 45%.\n"
    "Đây là hiện tượng 'rút lui lặng lẽ' (Silent Churn). Khách hàng không gây ồn ào nhưng ngưng dùng thẻ hoàn toàn. "
    "Nếu ngân hàng chỉ chờ đến khi khách hàng nộp đơn hủy thẻ thì đã quá muộn để cứu vãn."
)

# ==============================================================================
# SLIDE 11: EDA 5 — TƯƠNG TÁC CSKH & NGƯỠNG BÁO ĐỘNG 3 LẦN GỌI
# ==============================================================================
s11 = prs.slides.add_slide(blank_layout)
set_bg(s11)
add_header(s11, "Ngưỡng 3 Lần Gọi Tổng Đài CSKH Làm Tăng Nguy Cơ Rời Bỏ Lên 300%: Nút Thắt Trải Nghiệm Dịch Vụ", 
           category_badge="KHAI PHÁ EDA — CHĂM SÓC KHÁCH HÀNG")
add_footer(s11, 11, TOTAL_SLIDES)

create_card(s11, Inches(0.8), Inches(1.55), Inches(6.8), Inches(5.2))
img_p11 = os.path.join(FIG_DIR, "05_interaction_decay_churn.png")
if os.path.exists(img_p11):
    s11.shapes.add_picture(img_p11, Inches(0.95), Inches(1.75), width=Inches(6.5))

create_card(s11, Inches(7.9), Inches(1.55), Inches(4.633), Inches(5.2))
tb_e5 = s11.shapes.add_textbox(Inches(8.15), Inches(1.75), Inches(4.133), Inches(4.8))
tf_e5 = tb_e5.text_frame
tf_e5.word_wrap = True
tf_e5.margin_left = tf_e5.margin_right = tf_e5.margin_top = tf_e5.margin_bottom = 0

p = tf_e5.paragraphs[0]
p.text = "📞 Ngưỡng Bất Mãn Dịch Vụ (Frustration Point)"
p.font.name = FONT_TITLE
p.font.size = Pt(13)
p.font.bold = True
p.font.color.rgb = C_HVNH_NAVY
p.space_after = Pt(6)

bullets_e5 = [
    ("Số lần liên hệ tổng đài (Contacts_Count):", "Khách hàng liên hệ CSKH từ 3 lần trở lên trong năm có tỷ lệ rời bỏ tăng vọt từ 14.8% lên 28.6% (gọi 3 lần), 52.4% (gọi 4 lần) và 100% (gọi 6 lần)."),
    ("Bản chất nghiệp vụ:", "Mỗi cuộc gọi phản ánh một sự cố chưa được giải quyết dứt điểm (lỗi quẹt thẻ, tính sai lãi/phí, tra soát giao dịch chậm trễ)."),
    ("Mức độ ngủ đông (Months_Inactive_12_mon):", "Khách hàng không phát sinh giao dịch từ 3 tháng trở lên trong năm có nguy cơ rời bỏ tăng gấp 2.5 lần so với nhóm hoạt động đều."),
    ("Khuyến nghị quản trị:", "Thiết lập chỉ tiêu First-Contact Resolution (FCR) cho tổng đài và tự động kích hoạt cuộc gọi xin lỗi từ cấp Quản lý khi khách gọi đến lần thứ 3.")
]
for lead, body in bullets_e5:
    p_b = tf_e5.add_paragraph()
    format_bullet_point(p_b, lead, body, font_size=10.0)

add_speaker_note(s11,
    "Kính thưa Hội đồng, chỉ số số lần liên hệ tổng đài CSKH phản ánh trực tiếp mức độ bất mãn của người dùng.\n"
    "Nếu khách hàng chỉ gọi 1 - 2 lần thì tỷ lệ rời bỏ ở mức bình thường (14%). "
    "Nhưng khi khách hàng phải gọi đến lần thứ 3, tỷ lệ rời bỏ tăng gấp đôi lên 28.6%, và khi gọi đến lần thứ 4 thì hơn 52% sẽ hủy thẻ.\n"
    "Điều này chứng tỏ quy trình xử lý khiếu nại hiện tại của ngân hàng chưa đạt chuẩn xử lý dứt điểm lần đầu (First-Contact Resolution). "
    "Đây là nút thắt trải nghiệm mà ngân hàng cần can thiệp quy trình ngay lập tức."
)

# ==============================================================================
# SLIDE 12: EDA 6 — HỆ SINH THÁI SẢN PHẨM & RÀO CẢN CHUYỂN ĐỔI
# ==============================================================================
s12 = prs.slides.add_slide(blank_layout)
set_bg(s12)
add_header(s12, "Sở Hữu Từ 4 Sản Phẩm Trở Lên Tạo Rào Cản Chuyển Đổi Vững Chắc, Hạ Tỷ Lệ Churn Xuống Dưới 10%", 
           category_badge="KHAI PHÁ EDA — HỆ SINH THÁI SẢN PHẨM")
add_footer(s12, 12, TOTAL_SLIDES)

create_card(s12, Inches(0.8), Inches(1.55), Inches(6.8), Inches(5.2))
img_p12 = os.path.join(FIG_DIR, "08_relationship_and_card.png")
if os.path.exists(img_p12):
    s12.shapes.add_picture(img_p12, Inches(0.95), Inches(1.75), width=Inches(6.5))

create_card(s12, Inches(7.9), Inches(1.55), Inches(4.633), Inches(5.2))
tb_e6 = s12.shapes.add_textbox(Inches(8.15), Inches(1.75), Inches(4.133), Inches(4.8))
tf_e6 = tb_e6.text_frame
tf_e6.word_wrap = True
tf_e6.margin_left = tf_e6.margin_right = tf_e6.margin_top = tf_e6.margin_bottom = 0

p = tf_e6.paragraphs[0]
p.text = "🔗 Hiệu Ứng Khóa Chân (Lock-in Effect)"
p.font.name = FONT_TITLE
p.font.size = Pt(13)
p.font.bold = True
p.font.color.rgb = C_HVNH_NAVY
p.space_after = Pt(6)

bullets_e6 = [
    ("Số lượng sản phẩm nắm giữ (Total_Relationship_Count):", "Khách hàng chỉ sử dụng 1 - 2 sản phẩm có tỷ lệ rời bỏ lên tới 25.4% do chi phí chuyển đổi (Switching Cost) gần như bằng 0."),
    ("Hiệu ứng rào cản chuyển đổi:", "Khi khách hàng sử dụng từ 4, 5 đến 6 sản phẩm ngân hàng, tỷ lệ rời bỏ giảm mạnh chỉ còn 9.8% - 12.5%."),
    ("Phân hạng thẻ (Card_Category):", "Thẻ Blue chiếm 93.2% tổng danh mục với tỷ lệ Churn 16.1%. Các dòng thẻ cao cấp Silver/Gold/Platinum có tỷ lệ Churn cao hơn (18.5% - 25.0%) do kỳ vọng dịch vụ VIP khắt khe."),
    ("Chiến lược bán chéo (Cross-selling):", "Khuyến nghị liên kết thẻ tín dụng với tài khoản thanh toán lương, sổ tiết kiệm và bảo hiểm nhân thọ (Bancassurance).")
]
for lead, body in bullets_e6:
    p_b = tf_e6.add_paragraph()
    format_bullet_point(p_b, lead, body, font_size=10.0)

add_speaker_note(s12,
    "Kính thưa Thầy/Cô, kết quả phân tích hệ sinh thái sản phẩm khẳng định quy luật 'Hiệu ứng khóa chân' (Lock-in Effect) trong ngân hàng bán lẻ.\n"
    "Khách hàng chỉ mở thẻ đơn lẻ có tỷ lệ rời bỏ lên tới trên 25%. Tuy nhiên, nếu khách hàng sử dụng từ 4 sản phẩm trở lên (như tài khoản lương, thấu chi, gửi tiết kiệm, bảo hiểm), chi phí chuyển đổi tăng cao và tỷ lệ rời bỏ giảm xuống chỉ còn dưới 10%.\n"
    "Do đó, chiến lược bán chéo (Cross-selling) tích hợp hệ sinh thái chính là chìa khóa xây dựng rào cản bảo vệ thị phần bền vững nhất."
)

# ==============================================================================
# SLIDE 13: KHAI PHÁ DỮ LIỆU — PHÂN CỤM K-MEANS & PCA (k=4)
# ==============================================================================
s13 = prs.slides.add_slide(blank_layout)
set_bg(s13)
add_header(s13, "Phân Cụm K-Means Nhận Diện 4 Nhóm Hành Vi Độc Lập: Định Vị Cụm 1 Là Trọng Tâm Churn (52.6% Tỷ Trọng)", 
           category_badge="KHAI PHÁ DỮ LIỆU — K-MEANS & PCA")
add_footer(s13, 13, TOTAL_SLIDES)

create_card(s13, Inches(0.8), Inches(1.55), Inches(6.8), Inches(5.2))
img_p13 = os.path.join(FIG_DIR, "10_kmeans_clusters_pca.png")
if os.path.exists(img_p13):
    s13.shapes.add_picture(img_p13, Inches(0.95), Inches(1.75), width=Inches(6.5))

create_card(s13, Inches(7.9), Inches(1.55), Inches(4.633), Inches(5.2))
tb_km = s13.shapes.add_textbox(Inches(8.15), Inches(1.75), Inches(4.133), Inches(4.8))
tf_km = tb_km.text_frame
tf_km.word_wrap = True
tf_km.margin_left = tf_km.margin_right = tf_km.margin_top = tf_km.margin_bottom = 0

p = tf_km.paragraphs[0]
p.text = "🎯 Đặc Trưng 4 Phân Cụm Khách Hàng (k=4)"
p.font.name = FONT_TITLE
p.font.size = Pt(13)
p.font.bold = True
p.font.color.rgb = C_HVNH_NAVY
p.space_after = Pt(6)

bullets_km = [
    ("Tối ưu hóa k=4:", "Phương pháp Elbow kết hợp Silhouette Score (0.34) xác nhận k=4 là số cụm tối ưu nhất về mặt toán học và nghiệp vụ."),
    ("Cụm 1: Khách hàng Nguy cơ cao (Churn Cluster):", "Chiếm 52.6% tổng lượng Churn. Đặc trưng: Quẹt thẻ rất ít (42 lần), chi tiêu thấp ($2,850), dư nợ về 0."),
    ("Cụm 0: Khách hàng Phổ thông Tích cực:", "Chiếm 38.5% danh mục, quẹt thẻ đều đặn (65 lần), tỷ lệ Churn thấp (11.2%)."),
    ("Cụm 2: Khách hàng Thượng lưu / VIP:", "Hạn mức tín dụng cao (>$20,000), thu nhập $120K+, nhạy cảm với dịch vụ cá nhân hóa."),
    ("Cụm 3: Khách hàng Siêu giao dịch (Super Users):", "Quẹt thẻ >105 lần/năm, chi tiêu >$14,000, tỷ lệ Churn gần như bằng 0 (<2%).")
]
for lead, body in bullets_km:
    p_b = tf_km.add_paragraph()
    format_bullet_point(p_b, lead, body, font_size=9.8)

add_speaker_note(s13,
    "Kính thưa Hội đồng, trước khi bước vào giai đoạn huấn luyện mô hình có giám sát, nghiên cứu đã sử dụng kỹ thuật học không giám sát K-Means kết hợp giảm chiều PCA để bóc tách các nhóm khách hàng đồng nhất.\n"
    "Kết quả nhận diện 4 phân cụm rõ rệt. Trong đó, Cụm 1 được định vị là 'Tâm điểm rủi ro', tập trung tới 52.6% tổng lượng khách hàng rời bỏ của toàn bộ ngân hàng.\n"
    "Việc phân đoạn này giúp ngân hàng không phải áp dụng các chính sách cào bằng lãng phí, mà tập trung nguồn lực can thiệp chính xác vào nhóm đối tượng có tỷ trọng rủi ro cao nhất."
)

# ==============================================================================
# SLIDE 14: MÔ HÌNH HÓA MÁY HỌC — SO SÁNH 4 MÔ HÌNH (WINNER CARD)
# ==============================================================================
s14 = prs.slides.add_slide(blank_layout)
set_bg(s14)
add_header(s14, "XGBoost Classifier Vượt Trội Toàn Diện Với ROC-AUC 0.9930, Recall 91.38% & F1-Score 91.23%", 
           category_badge="MÔ HÌNH HÓA MÁY HỌC — SO SÁNH HIỆU NĂNG")
add_footer(s14, 14, TOTAL_SLIDES)

create_card(s14, Inches(0.8), Inches(1.55), Inches(6.8), Inches(5.2))
img_p14 = os.path.join(FIG_DIR, "11_ml_model_comparison_roc.png")
if os.path.exists(img_p14):
    s14.shapes.add_picture(img_p14, Inches(0.95), Inches(1.75), width=Inches(6.5))

# Right Box with Top Performer Banner
create_card(s14, Inches(7.9), Inches(1.55), Inches(4.633), Inches(5.2), border_color=C_HVNH_ORANGE, border_width=2.0)

# Top Performer Ribbon
ribbon = s14.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.1), Inches(1.7), Inches(4.233), Inches(0.4))
ribbon.fill.solid()
ribbon.fill.fore_color.rgb = C_HVNH_ORANGE
ribbon.line.fill.background()
tf_rb = ribbon.text_frame
tf_rb.margin_left = tf_rb.margin_right = tf_rb.margin_top = tf_rb.margin_bottom = 0
p_rb = tf_rb.paragraphs[0]
p_rb.alignment = PP_ALIGN.CENTER
p_rb.text = "🏆 WINNER: TOP PERFORMING MODEL (XGBOOST)"
p_rb.font.name = FONT_PRIMARY
p_rb.font.size = Pt(10.5)
p_rb.font.bold = True
p_rb.font.color.rgb = C_WHITE

tb_ml = s14.shapes.add_textbox(Inches(8.15), Inches(2.2), Inches(4.133), Inches(4.4))
tf_ml = tb_ml.text_frame
tf_ml.word_wrap = True
tf_ml.margin_left = tf_ml.margin_right = tf_ml.margin_top = tf_ml.margin_bottom = 0

p = tf_ml.paragraphs[0]
p.text = "📊 Bảng Tổng Hợp Hiệu Năng Đối Đầu (Test Set)"
p.font.name = FONT_TITLE
p.font.size = Pt(12.5)
p.font.bold = True
p.font.color.rgb = C_HVNH_NAVY
p.space_after = Pt(4)

bullets_ml = [
    ("1. Logistic Regression (Baseline):", "ROC-AUC: 0.9348 | Recall: 83.38% | F1: 67.25% (Hạn chế do không bắt được quan hệ phi tuyến)."),
    ("2. Random Forest:", "ROC-AUC: 0.9892 | Recall: 88.31% | F1: 89.97% (Kiểm soát tốt overfitting nhưng tốc độ suy luận chậm)."),
    ("3. Support Vector Machine (SVM):", "ROC-AUC: 0.9702 | Recall: 84.62% | F1: 81.34% (Nhạy cảm với phân bố biên)."),
    ("4. XGBoost Classifier (Champion):", "ROC-AUC: 0.9930 | Recall: 91.38% | Precision: 91.08% | F1: 91.23% (Vượt trội hoàn toàn về khả năng phân loại và tốc độ thực thi).")
]
for lead, body in bullets_ml:
    p_b = tf_ml.add_paragraph()
    format_bullet_point(p_b, lead, body, lead_color=C_HVNH_NAVY, font_size=9.6)

add_speaker_note(s14,
    "Kính thưa Thầy/Cô, trên tập kiểm thử độc lập gồm 2,026 khách hàng, đề tài đã tiến hành so sánh đối đầu 4 thuật toán học máy đại diện.\n"
    "Kết quả thực nghiệm khẳng định XGBoost Classifier là mô hình chiến thắng toàn diện với ROC-AUC đạt 0.9930, Recall 91.38% và F1-Score 91.23%.\n"
    "So với mô hình truyền thống Logistic Regression (chỉ đạt Recall 83.38%), thuật toán Gradient Boosting của XGBoost đã nắm bắt xuất sắc các tương tác phi tuyến phức tạp giữa tần suất giao dịch và biến động số dư. "
    "Do đó, XGBoost được lựa chọn làm mô hình lõi cho hệ thống."
)

# ==============================================================================
# SLIDE 15: ĐÁNH GIÁ CHI TIẾT MA TRẬN NHẦM LẪN (CONFUSION MATRIX)
# ==============================================================================
s15 = prs.slides.add_slide(blank_layout)
set_bg(s15)
add_header(s15, "Kiểm Soát Xuất Sắc Hai Loại Sai Số: Tỷ Lệ Bỏ Sót Chỉ 8.62% (FN=28) & Báo Động Giả Chỉ 2.12% (FP=36)", 
           category_badge="KIỂM ĐỊNH MÔ HÌNH — MA TRẬN NHẦM LẪN")
add_footer(s15, 15, TOTAL_SLIDES)

create_card(s15, Inches(0.8), Inches(1.55), Inches(6.8), Inches(5.2))
img_p15 = os.path.join(FIG_DIR, "12_ml_confusion_matrices.png")
if os.path.exists(img_p15):
    s15.shapes.add_picture(img_p15, Inches(0.95), Inches(1.75), width=Inches(6.5))

create_card(s15, Inches(7.9), Inches(1.55), Inches(4.633), Inches(5.2))
tb_cm = s15.shapes.add_textbox(Inches(8.15), Inches(1.75), Inches(4.133), Inches(4.8))
tf_cm = tb_cm.text_frame
tf_cm.word_wrap = True
tf_cm.margin_left = tf_cm.margin_right = tf_cm.margin_top = tf_cm.margin_bottom = 0

p = tf_cm.paragraphs[0]
p.text = "🎯 Kiểm Soát Sai Số Loại I & II (Type I/II Error)"
p.font.name = FONT_TITLE
p.font.size = Pt(13)
p.font.bold = True
p.font.color.rgb = C_HVNH_NAVY
p.space_after = Pt(6)

bullets_cm = [
    ("Sai số Loại II (False Negative - Nguy hiểm nhất):", "Chỉ có 28/325 khách hàng Churn bị bỏ sót (Tỷ lệ sai sót 8.62%). Giúp ngân hàng giữ lại tối đa nguồn thu CLV."),
    ("Sai số Loại I (False Positive - Báo động giả):", "Chỉ có 36/1,701 khách hàng ở lại bị dự báo nhầm thành Churn (Tỷ lệ báo động giả 2.12%). Tiết kiệm tối đa ngân sách marketing."),
    ("Độ tin cậy dự báo (Precision = 91.08%):", "Cứ 100 khách hàng mà mô hình cảnh báo thì có hơn 91 khách hàng thực sự chuẩn bị rời bỏ."),
    ("Ý nghĩa tài chính:", "Sự cân bằng hoàn hảo giữa việc tối đa hóa khách hàng cứu vãn được và tối thiểu hóa chi phí can thiệp lãng phí.")
]
for lead, body in bullets_cm:
    p_b = tf_cm.add_paragraph()
    format_bullet_point(p_b, lead, body, font_size=10.0)

add_speaker_note(s15,
    "Kính thưa Hội đồng, trong bài toán dự báo rời bỏ ngân hàng, sai số Loại II (False Negative - bỏ sót khách hàng rời bỏ) là sai số gây thiệt hại nặng nề nhất về mặt tài chính.\n"
    "Ma trận nhầm lẫn của XGBoost chứng minh khả năng kiểm soát sai số cực kỳ ấn tượng: Trong 325 khách hàng rời bỏ ở tập test, mô hình phát hiện chính xác 297 người, chỉ bỏ sót duy nhất 28 người.\n"
    "Đồng thời, tỷ lệ báo động giả (False Positive) chỉ ở mức 2.12%, giúp ngân hàng không bị lãng phí ngân sách chăm sóc vào những khách hàng vốn dĩ vẫn đang trung thành."
)

# ==============================================================================
# SLIDE 16: TOP ĐẶC TRƯNG QUYẾT ĐỊNH RỜI BỎ (FEATURE IMPORTANCE)
# ==============================================================================
s16 = prs.slides.add_slide(blank_layout)
set_bg(s16)
add_header(s16, "Giải Thích XAI: Tần Suất Giao Dịch, Tỷ Lệ Sụt Giảm Chi Tiêu & Dư Nợ Là 3 Đòn Bẩy Quyết Định Nguy Cơ Churn", 
           category_badge="GIẢI THÍCH MÔ HÌNH — EXPLAINABLE AI")
add_footer(s16, 16, TOTAL_SLIDES)

create_card(s16, Inches(0.8), Inches(1.55), Inches(6.8), Inches(5.2))
img_p16 = os.path.join(FIG_DIR, "13_feature_importance_xgb.png")
if os.path.exists(img_p16):
    s16.shapes.add_picture(img_p16, Inches(0.95), Inches(1.75), width=Inches(6.5))

create_card(s16, Inches(7.9), Inches(1.55), Inches(4.633), Inches(5.2))
tb_fi = s16.shapes.add_textbox(Inches(8.15), Inches(1.75), Inches(4.133), Inches(4.8))
tf_fi = tb_fi.text_frame
tf_fi.word_wrap = True
tf_fi.margin_left = tf_fi.margin_right = tf_fi.margin_top = tf_fi.margin_bottom = 0

p = tf_fi.paragraphs[0]
p.text = "🔑 5 Đòn Bẩy Hành Vi Cốt Lõi"
p.font.name = FONT_TITLE
p.font.size = Pt(13)
p.font.bold = True
p.font.color.rgb = C_HVNH_NAVY
p.space_after = Pt(6)

bullets_fi = [
    ("1. Total_Trans_Ct (Số lần quẹt thẻ):", "Đặc trưng quan trọng số 1 (Feature Importance > 25%). Tần suất sử dụng thẻ phản ánh trực tiếp mức độ gắn kết hàng ngày."),
    ("2. Total_Amt_Chng_Q4_Q1 (Tốc độ sụt giảm chi tiêu):", "Đòn bẩy cảnh báo sớm số 2. Cho thấy khách hàng đang dịch chuyển dòng tiền thanh toán sang nơi khác."),
    ("3. Total_Revolving_Bal (Dư nợ quay vòng):", "Tín hiệu tất toán nợ về $0 báo hiệu đóng thẻ trong 30-60 ngày tới."),
    ("4. Total_Trans_Amt (Tổng giá trị chi tiêu):", "Đo lường quy mô tài chính và mức độ phụ thuộc vào thẻ."),
    ("5. Total_Relationship_Count (Số sản phẩm):", "Rào cản chuyển đổi hệ sinh thái bảo vệ khách hàng khỏi bị đối thủ lôi kéo.")
]
for lead, body in bullets_fi:
    p_b = tf_fi.add_paragraph()
    format_bullet_point(p_b, lead, body, font_size=10.0)

add_speaker_note(s16,
    "Kính thưa Thầy/Cô, để mô hình học máy không phải là một 'Hộp đen' (Black-box), nghiên cứu đã áp dụng kỹ thuật Explainable AI để bóc tách 5 đòn bẩy quan trọng nhất.\n"
    "Kết quả cho thấy số lượng giao dịch và mức độ sụt giảm chi tiêu quý 4 so với quý 1 là hai biến số chi phối mạnh nhất.\n"
    "Điều này hoàn toàn tương thích với các phát hiện nghiệp vụ ở phần EDA: Khách hàng không bỏ đi đột ngột mà luôn trải qua một quá trình 'sụt giảm tần suất quẹt thẻ và tất toán dư nợ' trước đó từ 2 đến 3 tháng. "
    "Đây chính là cơ sở vàng để thiết lập ngưỡng cảnh báo tự động."
)

# ==============================================================================
# SLIDE 17: TỐI ƯU HÓA NGƯỠNG KINH TẾ (COST-BENEFIT OPTIMIZATION)
# ==============================================================================
s17 = prs.slides.add_slide(blank_layout)
set_bg(s17)
add_header(s17, "Tối Ưu Hóa Ngưỡng Quyết Định Kinh Tế: Điểm Cắt t = 0.42 Tối Đa Hóa Lợi Nhuận Ròng Cho Ngân Hàng", 
           category_badge="TỐI ƯU HÓA KINH TẾ — THRESHOLD TUNING")
add_footer(s17, 17, TOTAL_SLIDES)

create_card(s17, Inches(0.8), Inches(1.55), Inches(6.8), Inches(5.2))
img_p17 = os.path.join(FIG_DIR, "14_cost_benefit_threshold_optimization.png")
if os.path.exists(img_p17):
    s17.shapes.add_picture(img_p17, Inches(0.95), Inches(1.75), width=Inches(6.5))

create_card(s17, Inches(7.9), Inches(1.55), Inches(4.633), Inches(5.2))
tb_th = s17.shapes.add_textbox(Inches(8.15), Inches(1.75), Inches(4.133), Inches(4.8))
tf_th = tb_th.text_frame
tf_th.word_wrap = True
tf_th.margin_left = tf_th.margin_right = tf_th.margin_top = tf_th.margin_bottom = 0

p = tf_th.paragraphs[0]
p.text = "💰 Mô Hình Hóa Chi Phí - Lợi Ích (Cost-Benefit)"
p.font.name = FONT_TITLE
p.font.size = Pt(13)
p.font.bold = True
p.font.color.rgb = C_HVNH_NAVY
p.space_after = Pt(6)

bullets_th = [
    ("Giả định bài toán kinh tế thực tiễn:", "• Giá trị trọn đời giữ chân (CLV): $500 USD / khách hàng\n• Chi phí can thiệp ưu đãi (CRC): $50 USD / khách hàng\n• Tỷ lệ giữ chân thành công khi can thiệp: 75%"),
    ("Hạn chế của ngưỡng mặc định t = 0.50:", "Bỏ lỡ các khách hàng có xác suất churn từ 40% - 49% nhưng có giá trị CLV cao."),
    ("Xác lập ngưỡng tối ưu t* = 0.42:", "Điểm cực đại của đường cong Lợi nhuận ròng (Net Benefit Curve), cân bằng hoàn hảo giữa chi phí can thiệp và doanh thu bảo vệ."),
    ("Gia tăng lợi ích ròng:", "Mang lại thêm +$24,500 USD lợi nhuận so với việc áp dụng ngưỡng 0.50 truyền thống.")
]
for lead, body in bullets_th:
    p_b = tf_th.add_paragraph()
    format_bullet_point(p_b, lead, body, font_size=10.0)

add_speaker_note(s17,
    "Kính thưa Hội đồng, một đóng góp quan trọng của đề tài là không áp dụng máy móc ngưỡng cắt xác suất 0.50 mặc định của khoa học máy tính, mà xây dựng hàm tối ưu hóa Chi phí - Lợi ích thực tế cho ngân hàng.\n"
    "Với giá trị khách hàng giữ lại được là 500 USD và chi phí can thiệp chỉ 50 USD, việc hạ ngưỡng cắt xác suất xuống t = 0.42 cho phép ngân hàng chủ động can thiệp sớm vào nhóm khách hàng chớm có nguy cơ.\n"
    "Đường cong Net Benefit chứng minh tại t = 0.42, ngân hàng thu được lợi nhuận kinh tế ròng tối đa, cao hơn đáng kể so với ngưỡng 0.50."
)

# ==============================================================================
# SLIDE 18: BA CHÂN DUNG KHÁCH HÀNG RỜI BỎ (CUSTOMER PERSONAS)
# ==============================================================================
s18 = prs.slides.add_slide(blank_layout)
set_bg(s18)
add_header(s18, "Cá Thể Hóa Giải Pháp Qua 3 Chân Dung: Silent Defector (55%), Frustrated Complainer (25%), VIP Switcher (20%)", 
           category_badge="PHÂN KHÚC KHÁCH HÀNG — PERSONAS")
add_footer(s18, 18, TOTAL_SLIDES)

personas = [
    ("CHÂN DUNG 1 (55% TỔNG CHURN)", "THE SILENT DEFECTOR\n(Ngủ đông & Rút lui lặng lẽ)", C_HVNH_NAVY, [
        ("Đặc điểm nhận diện:", "Dư nợ quay vòng = $0 USD, quẹt thẻ < 45 lần/năm, sụt giảm chi tiêu > 40% trong 2 quý gần nhất."),
        ("Động cơ rời bỏ:", "Chuyển dần sang dùng thẻ ngân hàng khác hoặc không còn nhu cầu chi tiêu thường nhật."),
        ("Hành động can thiệp:", "Gửi Push Notification kích hoạt lại: Tặng E-voucher 100K khi quẹt thẻ đầu tiên trong tuần, hoàn tiền 5% chi tiêu ăn uống.")
    ]),
    ("CHÂN DUNG 2 (25% TỔNG CHURN)", "FRUSTRATED COMPLAINER\n(Bức xúc Dịch vụ & Khiếu nại)", C_ACCENT_RED, [
        ("Đặc điểm nhận diện:", "Gọi tổng đài CSKH ≥ 3 - 6 lần/năm, mức độ ngủ đông 2-3 tháng sau các cuộc gọi tra soát."),
        ("Động cơ rời bỏ:", "Thất vọng về tốc độ giải quyết khiếu nại, bị tính phí/lãi chưa rõ ràng, bức xúc thái độ phục vụ."),
        ("Hành động can thiệp:", "Tổng đài viên cấp cao gọi điện xin lỗi trực tiếp, miễn phí thường niên 1 năm, xử lý dứt điểm khiếu nại trong 24h.")
    ]),
    ("CHÂN DUNG 3 (20% TỔNG CHURN)", "THE VIP SWITCHER\n(Khách VIP Chuyển dịch)", C_HVNH_ORANGE, [
        ("Đặc điểm nhận diện:", "Thu nhập ≥ $120K, sở hữu thẻ Gold/Platinum, hạn mức tín dụng > $20,000 USD."),
        ("Động cơ rời bỏ:", "Bị ngân hàng đối thủ lôi kéo bằng đặc quyền phòng chờ sân bay, thẻ hoàn tiền du lịch cao cấp."),
        ("Hành động can thiệp:", "Chuyên viên Quản lý Khách hàng Ưu tiên (Priority RM) chăm sóc riêng, nâng cấp quyền lợi Golf/Lounge, tăng hạn mức tự động.")
    ])
]

for idx, (p_tag, p_name, col, p_items) in enumerate(personas):
    c_left = Inches(0.8 + idx * 3.98)
    create_card(s18, c_left, Inches(1.55), Inches(3.78), Inches(5.2))
    
    # Top banner
    strip = s18.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, c_left + Inches(0.15), Inches(1.65), Inches(3.48), Inches(0.35))
    strip.fill.solid()
    strip.fill.fore_color.rgb = col
    strip.line.fill.background()
    tf_st = strip.text_frame
    tf_st.margin_left = tf_st.margin_right = tf_st.margin_top = tf_st.margin_bottom = 0
    p_st = tf_st.paragraphs[0]
    p_st.alignment = PP_ALIGN.CENTER
    p_st.text = p_tag
    p_st.font.name = FONT_PRIMARY
    p_st.font.size = Pt(10)
    p_st.font.bold = True
    p_st.font.color.rgb = C_WHITE
    
    tb = s18.shapes.add_textbox(c_left + Inches(0.18), Inches(2.1), Inches(3.42), Inches(4.5))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    
    p_ttl = tf.paragraphs[0]
    p_ttl.text = p_name
    p_ttl.font.name = FONT_PRIMARY
    p_ttl.font.size = Pt(12)
    p_ttl.font.bold = True
    p_ttl.font.color.rgb = C_HVNH_NAVY
    p_ttl.space_after = Pt(8)
    
    for lead, body in p_items:
        p_b = tf.add_paragraph()
        format_bullet_point(p_b, lead, body, lead_color=col, font_size=10.0)

add_speaker_note(s18,
    "Kính thưa Thầy/Cô, để các phòng ban kinh doanh dễ dàng triển khai, nghiên cứu đã tổng hợp các phát hiện thành 3 Chân dung khách hàng rời bỏ điển hình:\n"
    "Thứ nhất là 'The Silent Defector' chiếm tới 55% tổng lượng Churn - nhóm này ngủ đông âm thầm, cần kích hoạt lại bằng ưu đãi vi mô thường nhật.\n"
    "Thứ hai là 'Frustrated Complainer' chiếm 25% - nhóm bức xúc vì gọi tổng đài nhiều lần mà chưa được giải quyết, cần sự can thiệp trực tiếp từ cấp quản lý.\n"
    "Và thứ ba là 'The VIP Switcher' chiếm 20% - nhóm khách hàng giàu có đòi hỏi đặc quyền cao cấp.\n"
    "Cách tiếp cận phân khúc này giúp tối ưu hóa hiệu quả can thiệp và tránh lãng phí ngân sách."
)

# ==============================================================================
# SLIDE 19: KHUNG CHIẾN LƯỢC GIỮ CHÂN 4 TẦNG & EWS
# ==============================================================================
s19 = prs.slides.add_slide(blank_layout)
set_bg(s19)
add_header(s19, "Khung Giữ Chân 4 Tầng Toàn Diện: Từ Cảnh Báo Sớm EWS, CSKH Chủ Động Đến Loyalty & Bán Chéo", 
           category_badge="KHUYẾN NGHỊ QUẢN TRỊ — KHUNG 4 TẦNG")
add_footer(s19, 19, TOTAL_SLIDES)

tiers = [
    ("TẦNG 1: CẢNH BÁO SỚM (EWS)", C_ACCENT_RED, "Giám sát tự động thời gian thực các Trigger Point: Ngủ đông 2 tháng -> Đẩy Push Notification; Giảm chi tiêu > 30% -> Chuyển sang luồng ưu đãi hoàn tiền tự động.", "KPI: Tỷ lệ phát hiện sớm > 90%"),
    ("TẦNG 2: CSKH CHỦ ĐỘNG (PROACTIVE CARE)", C_HVNH_ORANGE, "Áp dụng chỉ tiêu First-Contact Resolution (FCR) giải quyết dứt điểm khiếu nại trong cuộc gọi đầu tiên; Khách gọi đến lần thứ 3 tự động chuyển tiếp tới Đội ngũ Chuyên viên Chăm sóc Đặc biệt.", "KPI: FCR > 85%, Churn CSKH < 5%"),
    ("TẦNG 3: GAMIFIED LOYALTY & TÍCH ĐIỂM", C_BLUE_CYAN, "Chiến dịch 'Quẹt Thẻ Mỗi Tuần' tích điểm theo tần suất quẹt thẻ thay vì chỉ tính theo doanh số; Tặng huy hiệu thành viên và ưu đãi giảm giá tại các chuỗi bán lẻ/ẩm thực đối tác liên kết.", "KPI: Tần suất GD ≥ 5 lần/tháng"),
    ("TẦNG 4: BÁN CHÉO HỆ SINH THÁI (CROSS-SELLING)", C_ACCENT_GREEN, "Combo 'Tài chính Toàn diện' liên kết thẻ tín dụng với tài khoản lương, miễn phí chuyển tiền trọn đời, tự động trích nợ sao kê và tích hợp ví điện tử / tiết kiệm online.", "KPI: Sở hữu ≥ 4 SP đạt > 65%")
]

for idx, (t_name, col, t_desc, kpi) in enumerate(tiers):
    c_top = Inches(1.55 + idx * 1.3)
    create_card(s19, Inches(0.8), c_top, Inches(11.733), Inches(1.18))
    
    # Left vertical accent bar
    v_bar = s19.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), c_top, Inches(0.15), Inches(1.18))
    v_bar.fill.solid()
    v_bar.fill.fore_color.rgb = col
    v_bar.line.fill.background()
    
    tb = s19.shapes.add_textbox(Inches(1.1), c_top + Inches(0.1), Inches(8.2), Inches(0.98))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    
    p = tf.paragraphs[0]
    p.text = t_name
    p.font.name = FONT_PRIMARY
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = col
    p.space_after = Pt(2)
    
    p_d = tf.add_paragraph()
    p_d.text = t_desc
    p_d.font.name = FONT_PRIMARY
    p_d.font.size = Pt(10.2)
    p_d.font.color.rgb = C_TEXT_DARK
    
    # KPI Box on right
    kpi_card = create_card(s19, Inches(9.4), c_top + Inches(0.25), Inches(2.9), Inches(0.65), bg_color=RGBColor(241, 245, 249), border_color=col)
    tb_k = s19.shapes.add_textbox(Inches(9.45), c_top + Inches(0.32), Inches(2.8), Inches(0.5))
    tf_k = tb_k.text_frame
    tf_k.margin_left = tf_k.margin_right = tf_k.margin_top = tf_k.margin_bottom = 0
    p_k = tf_k.paragraphs[0]
    p_k.alignment = PP_ALIGN.CENTER
    p_k.text = kpi
    p_k.font.name = FONT_PRIMARY
    p_k.font.size = Pt(10.5)
    p_k.font.bold = True
    p_k.font.color.rgb = C_HVNH_NAVY

add_speaker_note(s19,
    "Kính thưa Hội đồng, từ các phân tích trên, đề tài đề xuất Khung chiến lược giữ chân khách hàng toàn diện gồm 4 tầng gắn liền với các chỉ tiêu KPI định lượng:\n"
    "Tầng 1 là Hệ thống cảnh báo sớm EWS kích hoạt tự động theo thời gian thực.\n"
    "Tầng 2 là Tái cấu trúc quy trình CSKH chủ động nhằm nâng tỷ lệ giải quyết khiếu nại lần đầu FCR lên trên 85%.\n"
    "Tầng 3 là Chương trình tích điểm Gamified Loyalty thúc đẩy tần suất quẹt thẻ định kỳ.\n"
    "Và Tầng 4 là Chiến lược Bán chéo đa sản phẩm nhằm tạo rào cản chuyển đổi vững chắc. "
    "Bốn tầng này tạo thành một pháo đài vững chắc bảo vệ toàn diện danh mục khách hàng."
)

# ==============================================================================
# SLIDE 20: BÀI TOÁN KINH TẾ & TỶ SUẤT HOÀN VỐN ĐẦU TƯ (ROI = 500%)
# ==============================================================================
s20 = prs.slides.add_slide(blank_layout)
set_bg(s20)
add_header(s20, "Mô Phỏng Tài Chính Trên 10,000 Khách Hàng: Giữ Chân Thành Công 960 Khách, Tạo Lợi Nhuận Ròng +$400,000 USD", 
           category_badge="MÔ PHỎNG TÀI CHÍNH & ROI")
add_footer(s20, 20, TOTAL_SLIDES)

create_card(s20, Inches(0.8), Inches(1.55), Inches(5.7), Inches(5.2))
tb_f1 = s20.shapes.add_textbox(Inches(1.05), Inches(1.75), Inches(5.2), Inches(4.8))
tf_f1 = tb_f1.text_frame
tf_f1.word_wrap = True
tf_f1.margin_left = tf_f1.margin_right = tf_f1.margin_top = tf_f1.margin_bottom = 0

p = tf_f1.paragraphs[0]
p.text = "📊 Giả Định Quy Mô 10,000 Khách Hàng"
p.font.name = FONT_TITLE
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = C_HVNH_NAVY
p.space_after = Pt(8)

bullets_f1 = [
    ("Quy mô cơ sở:", "10,000 chủ thẻ tín dụng đang hoạt động tại ngân hàng thương mại."),
    ("Tỷ lệ rời bỏ tự nhiên (Baseline Churn):", "16.07% / năm (tương đương 1,607 khách hàng có nguy cơ đóng thẻ)."),
    ("Hiệu năng mô hình XGBoost (t = 0.42):", "Độ bao phủ phát hiện (Recall) đạt 91.38% (nhận diện thành công 1,468 khách hàng nguy cơ cao)."),
    ("Tỷ lệ chuyển đổi giữ chân thành công:", "75% trên số khách hàng được can thiệp (cứu vãn thành công ~1,100 khách hàng), trong đó 960 khách hàng quy đổi trực tiếp thành giá trị bền vững."),
    ("Chi phí can thiệp ưu đãi & CSKH (CRC):", "Bình quân $50 USD / khách hàng được can thiệp.")
]
for lead, body in bullets_f1:
    p_b = tf_f1.add_paragraph()
    format_bullet_point(p_b, lead, body, font_size=10.2)

create_card(s20, Inches(6.8), Inches(1.55), Inches(5.733), Inches(5.2))
tb_f2 = s20.shapes.add_textbox(Inches(7.05), Inches(1.75), Inches(5.233), Inches(4.8))
tf_f2 = tb_f2.text_frame
tf_f2.word_wrap = True
tf_f2.margin_left = tf_f2.margin_right = tf_f2.margin_top = tf_f2.margin_bottom = 0

p = tf_f2.paragraphs[0]
p.text = "💵 Tính Toán Lợi Nhuận & Tỷ Suất ROI"
p.font.name = FONT_TITLE
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = C_ACCENT_GREEN
p.space_after = Pt(8)

bullets_f2 = [
    ("1. Giá trị CLV cứu vãn được:", "960 khách × $500 USD = $480,000 USD tổng giá trị trọn đời bảo vệ thành công."),
    ("2. Tổng chi phí can thiệp (Total Retention Cost):", "1,600 khách × $50 USD = $80,000 USD ngân sách thực thi."),
    ("3. Lợi nhuận ròng tăng thêm (Net Profit):", "$480,000 - $80,000 = +$400,000 USD / năm."),
    ("4. Tỷ suất hoàn vốn đầu tư (ROI):", "($400,000 / $80,000) × 100% = 500%."),
    ("Ý nghĩa chiến lược:", "Khẳng định dự án Data Science mang lại hiệu quả đầu tư vượt bậc, giải phóng ngân hàng khỏi cạm bẫy chi phí thu hút khách mới đắt đỏ.")
]
for lead, body in bullets_f2:
    p_b = tf_f2.add_paragraph()
    format_bullet_point(p_b, lead, body, lead_color=C_ACCENT_GREEN, font_size=10.2)

add_speaker_note(s20,
    "Kính thưa Quý Thầy/Cô, để chứng minh tính khả thi tài chính, nghiên cứu đã xây dựng mô hình mô phỏng trên quy mô danh mục 10,000 khách hàng.\n"
    "Với tỷ lệ rời bỏ tự nhiên 16.07%, mô hình XGBoost sẽ phát hiện được hơn 1,460 khách hàng có nguy cơ. "
    "Khi triển khai các gói chăm sóc trị giá 50 USD/khách với tỷ lệ cứu vãn 75%, ngân hàng giữ lại thành công 960 khách hàng, tương đương bảo vệ được 480,000 USD giá trị CLV.\n"
    "Sau khi trừ đi toàn bộ 80,000 USD chi phí vận hành, dự án đem lại 400,000 USD lợi nhuận ròng mỗi năm, đạt tỷ suất hoàn vốn ROI lên đến 500%."
)

# ==============================================================================
# SLIDE 21: TỔNG KẾT HỌC THUẬT: ĐÓNG GÓP, HẠN CHẾ, HƯỚNG PHÁT TRIỂN & Q&A
# ==============================================================================
s21 = prs.slides.add_slide(blank_layout)
set_bg(s21)
add_header(s21, "Tổng Kết Nghiên Cứu: Đóng Góp Thực Tiễn, Giới Hạn Đề Tài & Định Hướng Phát Triển MLOps / Deep Learning", 
           category_badge="TỔNG KẾT & PHẢN BIỆN")
add_footer(s21, 21, TOTAL_SLIDES)

# 3 Academic Pillar Cards at Top
academic_pillars = [
    ("🎯 ĐÓNG GÓP THEN CHỐT", C_HVNH_NAVY, [
        ("Xây dựng Pipeline hoàn chỉnh:", "Từ tiền xử lý dữ liệu, kiểm soát rò rỉ nhãn đến triển khai học máy có khả năng giải thích XAI."),
        ("Tối ưu hóa kinh tế thực tiễn:", "Xác lập ngưỡng cắt t=0.42 mang lại ROI 500% (+400K USD/năm)."),
        ("Khung giải pháp 4 tầng:", "Cá thể hóa hành động can thiệp cho 3 chân dung khách hàng.")
    ]),
    ("⚠️ HẠN CHẾ NGHIÊN CỨU", C_HVNH_ORANGE, [
        ("Dữ liệu cắt ngang (Cross-sectional):", "Dataset gốc chưa ghi nhận biến động chuỗi thời gian liên tục (Time-series log) của từng giao dịch POS."),
        ("Phạm vi dữ liệu thực nghiệm:", "Chưa tích hợp dữ liệu phi cấu trúc (nhật ký ghi âm cuộc gọi CSKH, dữ liệu tín dụng CIC quốc gia)."),
        ("Giả định chi phí cố định:", "Chi phí can thiệp $50/khách là mức giả định bình quân.")
    ]),
    ("🚀 HƯỚNG PHÁT TRIỂN", C_ACCENT_GREEN, [
        ("Deep Learning cho dữ liệu bảng:", "Thử nghiệm kiến trúc TabNet và Transformer-based Tabular Models."),
        ("Hệ thống MLOps Real-time:", "Triển khai pipeline dự báo trực tiếp trên Kafka / Spark Streaming tại ngân hàng."),
        ("XAI cá thể hóa mức độ Micro:", "Tích hợp SHAP Waterfall trực quan hóa cho từng nhân viên RM.")
    ])
]

for idx, (p_title, col, items) in enumerate(academic_pillars):
    c_left = Inches(0.8 + idx * 3.98)
    create_card(s21, c_left, Inches(1.55), Inches(3.78), Inches(3.6))
    
    # Top strip
    strip = s21.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, c_left + Inches(0.15), Inches(1.65), Inches(3.48), Inches(0.32))
    strip.fill.solid()
    strip.fill.fore_color.rgb = col
    strip.line.fill.background()
    tf_st = strip.text_frame
    tf_st.margin_left = tf_st.margin_right = tf_st.margin_top = tf_st.margin_bottom = 0
    p_st = tf_st.paragraphs[0]
    p_st.alignment = PP_ALIGN.CENTER
    p_st.text = p_title
    p_st.font.name = FONT_PRIMARY
    p_st.font.size = Pt(10)
    p_st.font.bold = True
    p_st.font.color.rgb = C_WHITE
    
    tb = s21.shapes.add_textbox(c_left + Inches(0.18), Inches(2.05), Inches(3.42), Inches(3.0))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    
    for lead, body in items:
        p_b = tf.add_paragraph() if tf.paragraphs[0].text else tf.paragraphs[0]
        format_bullet_point(p_b, lead, body, lead_color=col, font_size=9.5)

# Bottom Thank You & Q&A Callout Banner
create_card(s21, Inches(0.8), Inches(5.3), Inches(11.733), Inches(1.45), bg_color=C_HVNH_NAVY, border_color=C_HVNH_ORANGE, border_width=1.5)
tb_qa = s21.shapes.add_textbox(Inches(1.0), Inches(5.42), Inches(11.333), Inches(1.2))
tf_qa = tb_qa.text_frame
tf_qa.word_wrap = True
tf_qa.margin_left = tf_qa.margin_right = tf_qa.margin_top = tf_qa.margin_bottom = 0

p_qa1 = tf_qa.paragraphs[0]
p_qa1.alignment = PP_ALIGN.CENTER
r1 = p_qa1.add_run()
r1.text = "XIN TRÂN TRỌNG CẢM ƠN QUÝ THẦY/CÔ VÀ CÁC BẠN HỌC VIÊN ĐÃ LẮNG NGHE!"
r1.font.name = FONT_PRIMARY
r1.font.size = Pt(13)
r1.font.bold = True
r1.font.color.rgb = C_HVNH_GOLD

p_qa2 = tf_qa.add_paragraph()
p_qa2.alignment = PP_ALIGN.CENTER
p_qa2.space_before = Pt(3)
r2 = p_qa2.add_run()
r2.text = "HỌC VIỆN NGÂN HÀNG (BANKING ACADEMY OF VIETNAM)  •  PHIÊN HỎI & ĐÁP (Q&A SESSION)"
r2.font.name = FONT_PRIMARY
r2.font.size = Pt(10.5)
r2.font.bold = True
r2.font.color.rgb = C_WHITE

p_qa3 = tf_qa.add_paragraph()
p_qa3.alignment = PP_ALIGN.CENTER
p_qa3.space_before = Pt(2)
r3 = p_qa3.add_run()
r3.text = "Rất mong nhận được các ý kiến nhận xét, góp ý và câu hỏi phản biện từ Hội đồng chấm bảo vệ!"
r3.font.name = FONT_PRIMARY
r3.font.size = Pt(10)
r3.font.italic = True
r3.font.color.rgb = RGBColor(186, 230, 253)

add_speaker_note(s21,
    "Kính thưa Quý Thầy/Cô trong Hội đồng và các bạn học viên,\n"
    "Tóm lại, nghiên cứu đã hoàn thành trọn vẹn mục tiêu đề ra: từ việc kiểm soát nghiêm ngặt rò rỉ dữ liệu, khai phá các quy luật hành vi then chốt, đến việc xây dựng mô hình XGBoost đạt ROC-AUC 0.9930 và tối ưu hóa ngưỡng kinh tế t = 0.42 mang lại ROI 500%.\n"
    "Bên cạnh các đóng góp thực tiễn, đề tài cũng thẳng thắn nhìn nhận các hạn chế về dữ liệu bảng cắt ngang và mở ra hướng phát triển ứng dụng TabNet cùng hệ thống Real-time MLOps trong tương lai.\n"
    "Em xin chân thành cảm ơn sự chú ý lắng nghe của Quý Thầy/Cô. Em xin sẵn sàng lắng nghe các ý kiến nhận xét và giải đáp các câu hỏi phản biện từ Hội đồng!"
)

# ==============================================================================
# LƯU FILE PPTX MASTER
# ==============================================================================
prs.save(PPTX_PATH)
print(f"✅ ĐÃ TẠO THÀNH CÔNG BỘ SLIDE MASTER 21 TRANG: {PPTX_PATH}")
print(f"📊 Kích thước: {prs.slide_width.inches:.2f} x {prs.slide_height.inches:.2f} inches (Chuẩn Widescreen 16:9)")
print(f"📄 Tổng số Slide: {len(prs.slides)} slides (Đầy đủ Mục Lục, Action Titles, Winner Cards, 3 Cột Tổng kết & Speaker Notes chuyên sâu)")
