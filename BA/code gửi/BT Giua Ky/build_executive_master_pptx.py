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

C_CANVAS_BG   = RGBColor(248, 250, 252)    # #F8FAFC: Nền Canvas xám siêu nhạt cao cấp
C_CARD_BG     = RGBColor(255, 255, 255)    # #FFFFFF: Thẻ card trắng tinh khiết
C_CARD_BORDER = RGBColor(226, 232, 240)    # #E2E8F0: Viền thẻ mỏng tinh tế
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
    tb_trk = slide.shapes.add_textbox(Inches(0.8), Inches(0.35), Inches(11.733), Inches(0.3))
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
    tb_ttl = slide.shapes.add_textbox(Inches(0.8), Inches(0.65), Inches(11.733), Inches(0.65))
    tf_ttl = tb_ttl.text_frame
    tf_ttl.word_wrap = True
    tf_ttl.margin_left = tf_ttl.margin_right = tf_ttl.margin_top = tf_ttl.margin_bottom = 0
    p_ttl = tf_ttl.paragraphs[0]
    p_ttl.text = action_title
    p_ttl.font.name = FONT_TITLE
    p_ttl.font.size = Pt(19)
    p_ttl.font.bold = True
    p_ttl.font.color.rgb = C_HVNH_NAVY
    
    # Bottom accent line under title
    line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.35), Inches(2.2), Inches(0.04))
    line.fill.solid()
    line.fill.fore_color.rgb = C_HVNH_ORANGE
    line.line.fill.background()

def add_footer(slide, slide_num, total_slides=20):
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

def format_bullet_point(paragraph, lead_text, body_text, lead_color=C_HVNH_NAVY, body_color=C_TEXT_DARK, font_size=11.5):
    paragraph.space_before = Pt(3)
    paragraph.space_after = Pt(4)
    paragraph.line_spacing = 1.2
    
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

print("🎨 Đang thiết kế bộ Slide PowerPoint Executive Master Level chuẩn Học viện Ngân hàng...")

# ==============================================================================
# SLIDE 1: HERO TITLE SLIDE (ĐẲNG CẤP CAO HỌC / THẠC SĨ HVNH)
# ==============================================================================
s1 = prs.slides.add_slide(blank_layout)
set_bg(s1, C_HVNH_NAVY)

# Orange Accent Top Banner
top_bar = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(0.12))
top_bar.fill.solid()
top_bar.fill.fore_color.rgb = C_HVNH_ORANGE
top_bar.line.fill.background()

# University & Program Badge
tb_bav = s1.shapes.add_textbox(Inches(1.0), Inches(1.0), Inches(11.333), Inches(0.5))
tf_bav = tb_bav.text_frame
tf_bav.margin_left = tf_bav.margin_right = tf_bav.margin_top = tf_bav.margin_bottom = 0
p_bav = tf_bav.paragraphs[0]
r = p_bav.add_run()
r.text = "🏛️ HỌC VIỆN NGÂN HÀNG (BANKING ACADEMY OF VIETNAM)  •  KHOA HỆ THỐNG THÔNG TIN QUẢN LÝ"
r.font.name = FONT_PRIMARY
r.font.size = Pt(12)
r.font.bold = True
r.font.color.rgb = C_HVNH_GOLD

# Main Title & Subtitle
tb_ttl1 = s1.shapes.add_textbox(Inches(1.0), Inches(1.6), Inches(11.333), Inches(3.2))
tf_ttl1 = tb_ttl1.text_frame
tf_ttl1.word_wrap = True
tf_ttl1.margin_left = tf_ttl1.margin_right = tf_ttl1.margin_top = tf_ttl1.margin_bottom = 0

p1 = tf_ttl1.paragraphs[0]
p1.text = "BÁO CÁO BÀI TẬP GIỮA KỲ CHUYÊN ĐỀ CAO HỌC"
p1.font.name = FONT_PRIMARY
p1.font.size = Pt(14)
p1.font.bold = True
p1.font.color.rgb = RGBColor(186, 230, 253) # Light sky blue
p1.space_after = Pt(8)

p2 = tf_ttl1.add_paragraph()
p2.text = "XỬ LÝ DỮ LIỆU & KHAI PHÁ DỮ LIỆU"
p2.font.name = FONT_TITLE
p2.font.size = Pt(28)
p2.font.bold = True
p2.font.color.rgb = C_WHITE
p2.space_after = Pt(4)

p3 = tf_ttl1.add_paragraph()
p3.text = "PHÂN TÍCH HÀNH VI, PHÂN CỤM & DỰ BÁO NGUY CƠ RỜI BỎ\nCỦA KHÁCH HÀNG THẺ TÍN DỤNG (BANK CUSTOMER CHURN)"
p3.font.name = FONT_TITLE
p3.font.size = Pt(22)
p3.font.bold = True
p3.font.color.rgb = RGBColor(254, 215, 170) # Light Orange

# Horizontal divider
divider = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.0), Inches(4.9), Inches(11.333), Inches(0.02))
divider.fill.solid()
divider.fill.fore_color.rgb = RGBColor(51, 65, 85)
divider.line.fill.background()

# Metadata Cards at bottom (4 grid cards)
meta_items = [
    ("👤 HỌC VIÊN THỰC HIỆN", "ĐỖ VĂN ĐẠT", "Chuyên ngành Business Analytics"),
    ("📚 HỌC PHẦN NGHIÊN CỨU", "PHÂN TÍCH DỮ LIỆU KINH DOANH", "Business Analytics — HVNH"),
    ("📊 BỘ DỮ LIỆU THỰC NGHIỆM", "BANKCHURNERS.CSV", "10,127 quan sát • 23 thuộc tính"),
    ("📅 NIÊN KHÓA ĐÀO TẠO", "NĂM HỌC 2025 - 2026", "Hà Nội, Năm 2026")
]

for idx, (label, val1, val2) in enumerate(meta_items):
    c_left = Inches(1.0 + idx * 2.9)
    card = create_card(s1, c_left, Inches(5.2), Inches(2.7), Inches(1.6), bg_color=RGBColor(15, 31, 56), border_color=RGBColor(30, 58, 102))
    
    tb = s1.shapes.add_textbox(c_left + Inches(0.15), Inches(5.35), Inches(2.4), Inches(1.3))
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

add_speaker_note(s1, "Kính chào Quý Thầy/Cô Hội đồng và các bạn học viên. Em tên là Đỗ Văn Đạt. Hôm nay em xin phép được trình bày Báo cáo bài tập giữa kỳ: Xử lý dữ liệu và Khai phá dữ liệu trên bộ dữ liệu khách hàng thẻ tín dụng BankChurners.")

# ==============================================================================
# SLIDE 2: EXECUTIVE SUMMARY (TỔNG HỢP ĐIỀU HÀNH 4 TRỤ CỘT)
# ==============================================================================
s2 = prs.slides.add_slide(blank_layout)
set_bg(s2)
add_header(s2, "Executive Summary: Tổng Hợp 4 Phát Hiện & Đóng Góp Giá Trị Của Đề Tài", category_badge="TỔNG QUAN CHIẾN LƯỢC")
add_footer(s2, 2)

exec_cards = [
    ("1. BÀI TOÁN KINH TẾ CHURN", "16.07%", "Tỷ lệ rời bỏ nghiêm trọng", "• Mất 1,627/10,127 khách hàng mở thẻ.\n• Chi phí tìm khách mới (CAC) gấp 5-7 LẦN chi phí giữ chân khách cũ (CRC).\n• Tổn thất ước tính: $800,000 USD/năm.", C_ACCENT_RED),
    ("2. QUY LUẬT HÀNH VI CỐT LÕI", "< 55 GD", "Vùng nguy cơ báo động đỏ", "• Khách quẹt thẻ < 55 lần & < $3,000.\n• Dư nợ quay vòng Median = $0.00.\n• Gọi tổng đài lần 3: Churn vọt 20.2%.\n• Dùng ≥ 4 SP: Churn giảm còn 10.5%.", C_HVNH_ORANGE),
    ("3. MÔ HÌNH HỌC MÁY TÂN TIẾN", "0.9930", "ROC-AUC XGBoost vượt trội", "• XGBoost Classifier dẫn đầu toàn diện.\n• Recall 91.38% (bắt trúng >9/10 khách).\n• Precision 87.61% | Accuracy 96.54%.\n• Tối ưu ngưỡng kinh tế t = 0.42.", C_BLUE_CYAN),
    ("4. HIỆU QUẢ TÀI CHÍNH THỰC THI", "ROI 500%", "+$400,000 USD / Năm", "• Giữ chân 960 khách hàng có nguy cơ.\n• Cứu vãn $480,000 USD giá trị CLV.\n• Chi phí can thiệp ưu đãi: $80,000 USD.\n• Khung giữ chân 4 tầng & EWS.", C_ACCENT_GREEN)
]

for idx, (p_tag, p_big, p_sub, p_desc, p_col) in enumerate(exec_cards):
    c_left = Inches(0.8 + idx * 2.98)
    card = create_card(s2, c_left, Inches(1.55), Inches(2.78), Inches(5.2))
    
    # Top Accent Stripe
    stripe = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, c_left, Inches(1.55), Inches(2.78), Inches(0.1))
    stripe.fill.solid()
    stripe.fill.fore_color.rgb = p_col
    stripe.line.fill.background()
    
    tb = s2.shapes.add_textbox(c_left + Inches(0.18), Inches(1.75), Inches(2.42), Inches(4.8))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    
    p = tf.paragraphs[0]
    p.text = p_tag
    p.font.name = FONT_PRIMARY
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = p_col
    p.space_after = Pt(8)
    
    p = tf.add_paragraph()
    p.text = p_big
    p.font.name = FONT_TITLE
    p.font.size = Pt(26)
    p.font.bold = True
    p.font.color.rgb = C_HVNH_NAVY
    p.space_after = Pt(2)
    
    p = tf.add_paragraph()
    p.text = p_sub
    p.font.name = FONT_PRIMARY
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = p_col
    p.space_after = Pt(12)
    
    for line_txt in p_desc.split('\n'):
        if line_txt.strip():
            p = tf.add_paragraph()
            p.text = line_txt
            p.font.name = FONT_PRIMARY
            p.font.size = Pt(10.5)
            p.font.color.rgb = C_TEXT_DARK
            p.space_after = Pt(4)
            p.line_spacing = 1.15

add_speaker_note(s2, "Slide Tổng quan điều hành tóm lược toàn bộ 4 điểm cốt lõi của đề tài: Bài toán kinh tế Churn 16.07%, Quy luật hành vi 'Vùng nguy cơ cao', Mô hình máy học XGBoost đạt ROC-AUC 0.9930 và Hiệu quả tài chính ROI 500%.")

# ==============================================================================
# SLIDE 3: BỐI CẢNH & BÀI TOÁN KINH TẾ GIỮ CHÂN KHÁCH HÀNG
# ==============================================================================
s3 = prs.slides.add_slide(blank_layout)
set_bg(s3)
add_header(s3, "Bối Cảnh Thị Trường Thẻ & Bài Toán Kinh Tế Giữ Chân (CAC vs CRC)", category_badge="BỐI CẢNH KINH DOANH")
add_footer(s3, 3)

c_w = Inches(3.7)
c_h = Inches(5.2)

# Card 1: Trụ cột thu nhập thẻ
create_card(s3, Inches(0.8), Inches(1.55), c_w, c_h)
tb = s3.shapes.add_textbox(Inches(1.0), Inches(1.75), c_w - Inches(0.4), c_h - Inches(0.4))
tf = tb.text_frame
tf.word_wrap = True
tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0

p = tf.paragraphs[0]
p.text = "💳 3 Trụ Cột Lợi Nhuận Thẻ"
p.font.name = FONT_TITLE
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = C_HVNH_NAVY
p.space_after = Pt(12)

format_bullet_point(tf.add_paragraph(), "1. Phí Quẹt Thẻ (Interchange):", "Nguồn thu từ tỷ lệ chiết khấu giao dịch tại điểm chấp nhận thanh toán POS & E-commerce.")
format_bullet_point(tf.add_paragraph(), "2. Lãi Suất Quay Vòng (Revolving):", "Lãi suất biên cao nhất khi khách hàng duy trì số dư nợ quá thời hạn miễn lãi (45-55 ngày).")
format_bullet_point(tf.add_paragraph(), "3. Phí Dịch Vụ Định Kỳ:", "Phí thường niên, phí chậm thanh toán, phí chuyển đổi ngoại tệ và rút tiền mặt.")

# Card 2: Quy tắc 5:1
create_card(s3, Inches(4.82), Inches(1.55), c_w, c_h)
tb = s3.shapes.add_textbox(Inches(5.02), Inches(1.75), c_w - Inches(0.4), c_h - Inches(0.4))
tf = tb.text_frame
tf.word_wrap = True
tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0

p = tf.paragraphs[0]
p.text = "⚖️ Đòn Bẩy Chi Phí 5:1"
p.font.name = FONT_TITLE
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = C_BLUE_CYAN
p.space_after = Pt(12)

format_bullet_point(tf.add_paragraph(), "• Quy tắc 5:1 (CAC vs CRC):", "Chi phí thu hút một khách hàng thẻ mới (CAC) gấp từ 5 đến 7 LẦN chi phí giữ chân khách hàng cũ (CRC).")
format_bullet_point(tf.add_paragraph(), "• Tác động lợi nhuận:", "Tăng 5% tỷ lệ giữ chân khách hàng giúp thúc đẩy lợi nhuận ngân hàng tăng 25% - 95% (Bain & Company).")
format_bullet_point(tf.add_paragraph(), "• Mất mát kép khi Churn:", "Ngân hàng mất dòng thu lãi/phí tương lai và lãng phí chi phí marketing, thẩm định ban đầu.")

# Card 3: Thách thức thị trường
create_card(s3, Inches(8.84), Inches(1.55), c_w, c_h)
tb = s3.shapes.add_textbox(Inches(9.04), Inches(1.75), c_w - Inches(0.4), c_h - Inches(0.4))
tf = tb.text_frame
tf.word_wrap = True
tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0

p = tf.paragraphs[0]
p.text = "🚨 Thực Trạng Rời Bỏ (16.07%)"
p.font.name = FONT_TITLE
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = C_ACCENT_RED
p.space_after = Pt(12)

format_bullet_point(tf.add_paragraph(), "• Tỷ lệ Churn 16.07%:", "1,627 trên tổng số 10,127 khách hàng trong tập dữ liệu đã hủy/đóng tài khoản thẻ tín dụng.")
format_bullet_point(tf.add_paragraph(), "• Cạnh tranh gay gắt:", "Fintech (Ví điện tử, BNPL) và các ngân hàng đối thủ liên tục tung ưu đãi hoàn tiền hấp dẫn lôi kéo chủ thẻ.")
format_bullet_point(tf.add_paragraph(), "• Yêu cầu cấp thiết:", "Cần xây dựng hệ thống dự báo bằng AI để phát hiện sớm tín hiệu rủi ro trước khi khách đóng thẻ.")

add_speaker_note(s3, "Mảng thẻ tín dụng có biên lợi nhuận cao nhưng đang chịu áp lực lớn từ tỷ lệ rời bỏ 16.07%. Việc giữ chân khách hàng mang lại hiệu quả kinh tế vượt trội so với tìm kiếm khách hàng mới.")

# ==============================================================================
# SLIDE 4: PHƯƠNG PHÁP LUẬN & KIẾN TRÚC PIPELINE 4 BƯỚC
# ==============================================================================
s4 = prs.slides.add_slide(blank_layout)
set_bg(s4)
add_header(s4, "Kiến Trúc Pipeline Xử Lý Dữ Liệu & Khai Phá Máy Học Toàn Diện", category_badge="PHƯƠNG PHÁP LUẬN")
add_footer(s4, 4)

phases = [
    ("GIAI ĐOẠN 1", "TIỀN XỬ LÝ DỮ LIỆU", "• Loại bỏ 2 cột Naive Bayes thừa\n• Xử lý Missing bằng Median Imputation\n• Bảo toàn nhóm 'Unknown' độc lập\n• Feature Engineering 5 biến tài chính", C_HVNH_NAVY),
    ("GIAI ĐOẠN 2", "KHÁM PHÁ DỮ LIỆU (EDA)", "• Phân tích phân phối Attrition_Flag\n• Khảo sát nhân khẩu học & kiểm định χ²\n• Nhận diện Vùng rủi ro GD (<55 lần)\n• Phát hiện Dư nợ về 0 & Ngưỡng gọi CSKH", C_BLUE_CYAN),
    ("GIAI ĐOẠN 3", "KHAI PHÁ NÂNG CAO (ML)", "• Phân cụm 4 nhóm K-Means & PCA\n• Huấn luyện 4 thuật toán: LR, DT, RF, XGB\n• Đánh giá ROC-AUC, Recall & Precision\n• Tối ưu ngưỡng kinh tế (t = 0.42)", C_HVNH_ORANGE),
    ("GIAI ĐOẠN 4", "ỨNG DỤNG QUẢN TRỊ", "• Phác họa 3 Chân dung rủi ro (Personas)\n• Khung Chiến lược Giữ chân 4 Tầng\n• Hệ thống Cảnh báo Sớm (EWS)\n• Mô phỏng ROI tài chính đạt 500%", C_ACCENT_GREEN)
]

for idx, (p_tag, p_title, p_desc, p_col) in enumerate(phases):
    c_left = Inches(0.8 + idx * 2.98)
    create_card(s4, c_left, Inches(1.55), Inches(2.78), Inches(5.2))
    
    # Header box with solid color
    hdr_box = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, c_left, Inches(1.55), Inches(2.78), Inches(0.9))
    hdr_box.fill.solid()
    hdr_box.fill.fore_color.rgb = p_col
    hdr_box.line.fill.background()
    
    tb = s4.shapes.add_textbox(c_left + Inches(0.15), Inches(1.65), Inches(2.48), Inches(0.7))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    p = tf.paragraphs[0]
    p.text = p_tag
    p.font.name = FONT_PRIMARY
    p.font.size = Pt(9.5)
    p.font.bold = True
    p.font.color.rgb = RGBColor(254, 215, 170) if p_col == C_HVNH_NAVY else C_WHITE
    
    p = tf.add_paragraph()
    p.text = p_title
    p.font.name = FONT_PRIMARY
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = C_WHITE
    
    tb_b = s4.shapes.add_textbox(c_left + Inches(0.18), Inches(2.6), Inches(2.42), Inches(3.9))
    tf_b = tb_b.text_frame
    tf_b.word_wrap = True
    tf_b.margin_left = tf_b.margin_right = tf_b.margin_top = tf_b.margin_bottom = 0
    
    for line_txt in p_desc.split('\n'):
        if line_txt.strip():
            p = tf_b.add_paragraph()
            p.text = line_txt
            p.font.name = FONT_PRIMARY
            p.font.size = Pt(11)
            p.font.color.rgb = C_TEXT_DARK
            p.space_after = Pt(6)
            p.line_spacing = 1.2

add_speaker_note(s4, "Pipeline nghiên cứu được thiết kế theo 4 giai đoạn chuẩn mực khoa học dữ liệu, từ tiền xử lý, EDA thống kê, khai phá học máy đến xây dựng khung chiến lược kinh doanh.")

# ==============================================================================
# SLIDE 5: TIỀN XỬ LÝ DỮ LIỆU & FEATURE ENGINEERING
# ==============================================================================
s5 = prs.slides.add_slide(blank_layout)
set_bg(s5)
add_header(s5, "Tiền Xử Lý Dữ Liệu: Loại Bỏ Nhiễu & Kiến Tạo 5 Đặc Trưng Phái Sinh", category_badge="DATA ENGINEERING")
add_footer(s5, 5)

# Cột trái: Làm sạch
create_card(s5, Inches(0.8), Inches(1.55), Inches(5.7), Inches(5.2))
tb = s5.shapes.add_textbox(Inches(1.05), Inches(1.75), Inches(5.2), Inches(4.8))
tf = tb.text_frame
tf.word_wrap = True
tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0

p = tf.paragraphs[0]
p.text = "🧹 Chiến Lược Làm Sạch & Chuẩn Hóa"
p.font.name = FONT_TITLE
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = C_HVNH_NAVY
p.space_after = Pt(12)

format_bullet_point(tf.add_paragraph(), "1. Loại trừ Rò rỉ Dữ liệu (Data Leakage):", "Xóa bỏ 2 cột Naive Bayes phân loại sẵn ở cuối bảng để đảm bảo tính khách quan thực nghiệm.")
format_bullet_point(tf.add_paragraph(), "2. Xử lý Missing bằng Median Imputation:", "Điền giá trị Trung vị cho các ô trống trong biến số nhằm đảm bảo tính vững chắc (robust) trước các điểm ngoại lai.")
format_bullet_point(tf.add_paragraph(), "3. Bảo toàn Danh mục 'Unknown':", "Giữ nguyên nhóm 'Unknown' trong Học vấn (15.0%), Thu nhập (11.0%), Hôn nhân (7.4%) như một phân lớp thông tin hành vi độc lập thay vì xóa bỏ.")

# Cột phải: Feature Engineering
create_card(s5, Inches(6.8), Inches(1.55), Inches(5.733), Inches(5.2))
tb = s5.shapes.add_textbox(Inches(7.05), Inches(1.75), Inches(5.233), Inches(4.8))
tf = tb.text_frame
tf.word_wrap = True
tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0

p = tf.paragraphs[0]
p.text = "⚙️ Kỹ Thuật Tạo 5 Đặc Trưng Mới"
p.font.name = FONT_TITLE
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = C_HVNH_ORANGE
p.space_after = Pt(12)

format_bullet_point(tf.add_paragraph(), "• Avg_Trans_Value:", "= Total_Trans_Amt / Total_Trans_Ct (Giá trị chi tiêu trung bình trên mỗi lần quẹt thẻ).")
format_bullet_point(tf.add_paragraph(), "• Revolving_Ratio:", "= Total_Revolving_Bal / Credit_Limit (Tỷ lệ sử dụng dư nợ quay vòng trên hạn mức cấp).")
format_bullet_point(tf.add_paragraph(), "• Contact_Intensity:", "= Contacts_Count / (Months_Inactive + 1) (Chỉ số cường độ bất mãn khi đang ngủ đông).")
format_bullet_point(tf.add_paragraph(), "• Age_Group:", "Phân tầng lứa tuổi theo 5 nhóm vòng đời tài chính: <35, 35-44, 45-54, 55-64, 65+.")
format_bullet_point(tf.add_paragraph(), "• Churn_Binary:", "Mã hóa nhị phân 1 (Attrited Customer) vs 0 (Existing Customer).")

add_speaker_note(s5, "Khâu Feature Engineering giúp kiến tạo các chỉ số tài chính sâu sắc, phản ánh đúng bản chất hành vi quẹt thẻ và áp lực nợ của khách hàng.")

# ==============================================================================
# SLIDE 6: PHÂN BỐ BIẾN MỤC TIÊU & MẤT CÂN BẰNG LỚP
# ==============================================================================
s6 = prs.slides.add_slide(blank_layout)
set_bg(s6)
add_header(s6, "Phân Bố Biến Mục Tiêu: Thách Thức Mất Cân Bằng Lớp (Imbalance Ratio 1:5.22)", category_badge="EDA — BIẾN MỤC TIÊU")
add_footer(s6, 6)

create_card(s6, Inches(0.8), Inches(1.55), Inches(6.5), Inches(5.2))
s6.shapes.add_picture(os.path.join(FIG_DIR, "01_churn_distribution.png"), Inches(1.0), Inches(1.75), width=Inches(6.1))

create_card(s6, Inches(7.6), Inches(1.55), Inches(4.933), Inches(5.2))
tb = s6.shapes.add_textbox(Inches(7.85), Inches(1.75), Inches(4.433), Inches(4.8))
tf = tb.text_frame
tf.word_wrap = True
tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0

p = tf.paragraphs[0]
p.text = "📊 Thống Kê & Chiến Lược Đánh Giá"
p.font.name = FONT_TITLE
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = C_HVNH_NAVY
p.space_after = Pt(10)

format_bullet_point(tf.add_paragraph(), "• Cơ cấu Khách hàng:", "8,500 khách hàng Ở lại (83.93%) vs 1,627 khách hàng Rời bỏ (16.07%).")
format_bullet_point(tf.add_paragraph(), "• Tỷ lệ mất cân bằng:", "Xấp xỉ 1:5.22 (Cứ 6 khách hàng mở thẻ thì có 1 khách hàng rời bỏ).")
format_bullet_point(tf.add_paragraph(), "• Bẫy Accuracy (Độ chính xác giả):", "Nếu mô hình dự đoán toàn bộ khách hàng ở lại, Accuracy vẫn đạt 83.93% nhưng bỏ sót 100% khách rời bỏ.")
format_bullet_point(tf.add_paragraph(), "• Bộ chỉ số đánh giá tối ưu:", "Bắt buộc phải ưu tiên Recall (Độ nhạy), Precision, F1-Score và diện tích dưới đường cong ROC-AUC.")

add_speaker_note(s6, "Mất cân bằng lớp 16.07% đòi hỏi chúng ta không dùng Accuracy thuần túy mà phải tập trung tối ưu Recall và ROC-AUC để bắt trúng khách hàng rời bỏ.")

# ==============================================================================
# SLIDE 7: PHÂN TÍCH NHÂN KHẨU HỌC & RỦI RO PHÂN HÓA 2 ĐẦU
# ==============================================================================
s7 = prs.slides.add_slide(blank_layout)
set_bg(s7)
add_header(s7, "Phân Tích Nhân Khẩu Học: Khách Nữ & Hiện Tượng Rủi Ro Phân Hóa 2 Đầu Thu Nhập", category_badge="EDA — NHÂN KHẨU HỌC")
add_footer(s7, 7)

create_card(s7, Inches(0.8), Inches(1.55), Inches(6.8), Inches(5.2))
s7.shapes.add_picture(os.path.join(FIG_DIR, "02_demographic_churn.png"), Inches(0.95), Inches(1.68), width=Inches(6.5))

create_card(s7, Inches(7.9), Inches(1.55), Inches(4.633), Inches(5.2))
tb = s7.shapes.add_textbox(Inches(8.15), Inches(1.75), Inches(4.133), Inches(4.8))
tf = tb.text_frame
tf.word_wrap = True
tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0

p = tf.paragraphs[0]
p.text = "🔍 3 Phát Hiện Nhân Khẩu Cốt Lõi"
p.font.name = FONT_TITLE
p.font.size = Pt(15.5)
p.font.bold = True
p.font.color.rgb = C_HVNH_NAVY
p.space_after = Pt(10)

format_bullet_point(tf.add_paragraph(), "1. Chênh lệch Giới tính (Gender):", "Khách hàng Nữ có tỷ lệ rời bỏ 17.36% cao hơn Nam là 14.62% (kiểm định χ² có ý nghĩa thống kê p = 0.0002).")
format_bullet_point(tf.add_paragraph(), "2. Rủi ro 2 đầu Thu nhập (Bimodal):", "• Thu nhập < $40K: Churn 17.19% (áp lực phí).\n• Thu nhập ≥ $120K: Churn 17.33% (đối thủ lôi kéo).\n• Thu nhập $60K-$80K: Trung thành nhất (13.48%).")
format_bullet_point(tf.add_paragraph(), "3. Trình độ Học vấn (Doctorate):", "Học vị Tiến sĩ có tỷ lệ rời bỏ cao nhất toàn mẫu (21.06%).")

add_speaker_note(s7, "Phân tích nhân khẩu học chỉ ra hiện tượng phân hóa rủi ro ở 2 đầu thu nhập và khách hàng nữ có xu hướng rời bỏ cao hơn nam đáng kể.")

# ==============================================================================
# SLIDE 8: HÀNH VI GIAO DỊCH — VÙNG NGUY CƠ BÁO ĐỘNG ĐỎ
# ==============================================================================
s8 = prs.slides.add_slide(blank_layout)
set_bg(s8)
add_header(s8, "Hành Vi Giao Dịch: Nhận Diện 'Vùng Nguy Cơ Cao' (< 55 Giao Dịch & < $3,000)", category_badge="EDA — HÀNH VI QUẸT THẺ")
add_footer(s8, 8)

create_card(s8, Inches(0.8), Inches(1.55), Inches(6.8), Inches(5.2))
s8.shapes.add_picture(os.path.join(FIG_DIR, "03_transaction_behavior_churn.png"), Inches(0.95), Inches(1.75), width=Inches(6.5))

create_card(s8, Inches(7.9), Inches(1.55), Inches(4.633), Inches(5.2))
tb = s8.shapes.add_textbox(Inches(8.15), Inches(1.75), Inches(4.133), Inches(4.8))
tf = tb.text_frame
tf.word_wrap = True
tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0

p = tf.paragraphs[0]
p.text = "🚨 Điểm Báo Động Hành Vi"
p.font.name = FONT_TITLE
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = C_ACCENT_RED
p.space_after = Pt(10)

format_bullet_point(tf.add_paragraph(), "• Tổng số lần GD (Total_Trans_Ct):", "Khách ở lại 68.7 lần vs Khách churn 44.9 lần (-34.6%, p < 0.0001).")
format_bullet_point(tf.add_paragraph(), "• Tổng tiền GD (Total_Trans_Amt):", "Khách ở lại $4,655 vs Khách churn $3,095 (-33.5%, p < 0.0001).")
format_bullet_point(tf.add_paragraph(), "• VÙNG NGUY CƠ CAO (RED CLUSTER):", "Toàn bộ khách hàng quẹt thẻ dưới 55 lần/năm và chi tiêu dưới $3,000 tập trung dày đặc các điểm rời bỏ. Tần suất quẹt thẻ chính là 'nhịp tim' của lòng trung thành.")

add_speaker_note(s8, "Biểu đồ phân tán chỉ ra ranh giới cực kỳ sắc nét: Quẹt thẻ dưới 55 lần và chi tiêu dưới 3000 USD là vùng tập trung dày đặc khách hàng rời bỏ.")

# ==============================================================================
# SLIDE 9: CHỈ SỐ TÀI CHÍNH — HIỆN TƯỢNG DƯ NỢ VỀ 0
# ==============================================================================
s9 = prs.slides.add_slide(blank_layout)
set_bg(s9)
add_header(s9, "Chỉ Số Tài Chính: Hiện Tượng 'Dư Nợ Quay Vòng Về 0' Trước Khi Đóng Thẻ", category_badge="EDA — TÀI CHÍNH")
add_footer(s9, 9)

create_card(s9, Inches(0.8), Inches(1.55), Inches(6.8), Inches(5.2))
s9.shapes.add_picture(os.path.join(FIG_DIR, "04_financial_ratios_churn.png"), Inches(0.95), Inches(1.75), width=Inches(6.5))

create_card(s9, Inches(7.9), Inches(1.55), Inches(4.633), Inches(5.2))
tb = s9.shapes.add_textbox(Inches(8.15), Inches(1.75), Inches(4.133), Inches(4.8))
tf = tb.text_frame
tf.word_wrap = True
tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0

p = tf.paragraphs[0]
p.text = "📉 Tín Hiệu Dọn Đường Đóng Thẻ"
p.font.name = FONT_TITLE
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = C_HVNH_NAVY
p.space_after = Pt(10)

format_bullet_point(tf.add_paragraph(), "• Dư nợ quay vòng (Revolving Bal):", "• Khách ở lại: Mean $1,257 (Median $1,364)\n• Khách rời bỏ: Mean $673 (MEDIAN = $0.00!)")
format_bullet_point(tf.add_paragraph(), "• Tỷ lệ sử dụng hạn mức (Utilization):", "• Khách ở lại: 29.64% (Median 21.1%)\n• Khách rời bỏ: 16.25% (MEDIAN = 0.00%!)")
format_bullet_point(tf.add_paragraph(), "• Quy luật tâm lý tài chính:", "Khách hàng trước khi hủy thẻ luôn có hành vi tất toán sạch nợ để không phát sinh lãi phạt và hoàn toàn dừng quẹt thẻ.")

add_speaker_note(s9, "Hiện tượng dư nợ quay vòng về 0 là bằng chứng thực nghiệm rõ ràng nhất cho thấy khách hàng chuẩn bị dọn đường hủy thẻ.")

# ==============================================================================
# SLIDE 10: TƯƠNG TÁC CSKH & NGƯỠNG BÁO ĐỘNG 3 LẦN GỌI
# ==============================================================================
s10 = prs.slides.add_slide(blank_layout)
set_bg(s10)
add_header(s10, "Tương Tác CSKH & Mức Độ Ngủ Đông: 'Ngưỡng Báo Động 3 Lần Liên Hệ'", category_badge="EDA — DỊCH VỤ KHÁCH HÀNG")
add_footer(s10, 10)

create_card(s10, Inches(0.8), Inches(1.55), Inches(6.8), Inches(5.2))
s10.shapes.add_picture(os.path.join(FIG_DIR, "05_interaction_decay_churn.png"), Inches(0.95), Inches(1.75), width=Inches(6.5))

create_card(s10, Inches(7.9), Inches(1.55), Inches(4.633), Inches(5.2))
tb = s10.shapes.add_textbox(Inches(8.15), Inches(1.75), Inches(4.133), Inches(4.8))
tf = tb.text_frame
tf.word_wrap = True
tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0

p = tf.paragraphs[0]
p.text = "📞 Ngưỡng Bức Xúc 3 Lần Gọi"
p.font.name = FONT_TITLE
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = C_HVNH_ORANGE
p.space_after = Pt(10)

format_bullet_point(tf.add_paragraph(), "• Gọi CSKH 0 - 1 lần:", "Tỷ lệ rời bỏ dưới 8% (mức thông thường).")
format_bullet_point(tf.add_paragraph(), "• Gọi CSKH 3 lần:", "Tỷ lệ rời bỏ vọt lên 20.21% (Báo động vàng).")
format_bullet_point(tf.add_paragraph(), "• Gọi CSKH 4 lần:", "Tỷ lệ rời bỏ đạt 34.11% (Báo động đỏ).")
format_bullet_point(tf.add_paragraph(), "• Gọi CSKH 5 - 6 lần:", "Tỷ lệ rời bỏ lên tới 55% - 100% (Bất mãn cực độ).")
format_bullet_point(tf.add_paragraph(), "• Bài học vận hành:", "Cần áp dụng chỉ số First-Contact Resolution (FCR) xử lý dứt điểm khiếu nại trong 24 giờ.")

add_speaker_note(s10, "Dữ liệu chứng minh việc khách hàng gọi lên tổng đài đến lần thứ 3 là tín hiệu báo động đỏ cho thấy sự cố chưa được giải quyết thỏa đáng.")

# ==============================================================================
# SLIDE 11: RÀO CẢN CHUYỂN ĐỔI QUA HỆ SINH THÁI ĐA SẢN PHẨM
# ==============================================================================
s11 = prs.slides.add_slide(blank_layout)
set_bg(s11)
add_header(s11, "Hệ Sinh Thái Sản Phẩm: Rào Cản Chuyển Đổi Khi Khách Hàng Dùng ≥ 4 Sản Phẩm", category_badge="EDA — BÁN CHÉO")
add_footer(s11, 11)

create_card(s11, Inches(0.8), Inches(1.55), Inches(6.8), Inches(5.2))
s11.shapes.add_picture(os.path.join(FIG_DIR, "08_relationship_and_card.png"), Inches(0.95), Inches(1.75), width=Inches(6.5))

create_card(s11, Inches(7.9), Inches(1.55), Inches(4.633), Inches(5.2))
tb = s11.shapes.add_textbox(Inches(8.15), Inches(1.75), Inches(4.133), Inches(4.8))
tf = tb.text_frame
tf.word_wrap = True
tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0

p = tf.paragraphs[0]
p.text = "🔗 Sức Mạnh của Bán Chéo (Cross-selling)"
p.font.name = FONT_TITLE
p.font.size = Pt(15.5)
p.font.bold = True
p.font.color.rgb = C_ACCENT_GREEN
p.space_after = Pt(10)

format_bullet_point(tf.add_paragraph(), "• Dùng 1 - 2 sản phẩm:", "Tỷ lệ rời bỏ lên tới 26.15% - 27.81% (Gắn kết lỏng lẻo).")
format_bullet_point(tf.add_paragraph(), "• Dùng 3 sản phẩm:", "Tỷ lệ rời bỏ giảm xuống 17.77%.")
format_bullet_point(tf.add_paragraph(), "• Dùng ≥ 4 đến 6 sản phẩm:", "Tỷ lệ rời bỏ giảm mạnh chỉ còn 10.49% - 11.78% (Giảm gần 3 lần!).")
format_bullet_point(tf.add_paragraph(), "• Kết luận chiến lược:", "Càng tích hợp nhiều dịch vụ (tài khoản lương, tiết kiệm, vay thế chấp), chi phí chuyển đổi càng cao, giữ chân khách hàng tự nhiên.")

add_speaker_note(s11, "Sở hữu từ 4 sản phẩm trở lên giúp hạ tỷ lệ rời bỏ xuống chỉ còn 10%. Bán chéo chính là chìa khóa gia tăng rào cản chuyển đổi.")

# ==============================================================================
# SLIDE 12: KHAI PHÁ DỮ LIỆU — PHÂN CỤM K-MEANS & PCA (k=4)
# ==============================================================================
s12 = prs.slides.add_slide(blank_layout)
set_bg(s12)
add_header(s12, "Khai Phá Dữ Liệu: Phân Cụm 4 Nhóm Khách Hàng Hành Vi (K-Means & PCA)", category_badge="DATA MINING — CLUSTERING")
add_footer(s12, 12)

create_card(s12, Inches(0.8), Inches(1.55), Inches(6.8), Inches(5.2))
s12.shapes.add_picture(os.path.join(FIG_DIR, "10_kmeans_clusters_pca.png"), Inches(0.95), Inches(1.75), width=Inches(6.5))

create_card(s12, Inches(7.9), Inches(1.55), Inches(4.633), Inches(5.2))
tb = s12.shapes.add_textbox(Inches(8.15), Inches(1.75), Inches(4.133), Inches(4.8))
tf = tb.text_frame
tf.word_wrap = True
tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0

p = tf.paragraphs[0]
p.text = "👥 Hồ Sơ Đặc Trưng 4 Phân Cụm"
p.font.name = FONT_TITLE
p.font.size = Pt(15.5)
p.font.bold = True
p.font.color.rgb = C_HVNH_NAVY
p.space_after = Pt(8)

format_bullet_point(tf.add_paragraph(), "• Cụm 0 (37.6%): Tiêu dùng ổn định:", "Chi tiêu $4.1K, Dư nợ $1.4K, Churn = 9.2% (Thấp).")
format_bullet_point(tf.add_paragraph(), "• Cụm 1 (24.0%): Ngủ đông & Nguy cơ cao:", "Chi tiêu $1.8K, Dư nợ $210, Churn = 41.8%! (Cực cao, ưu tiên can thiệp số 1).", lead_color=C_ACCENT_RED)
format_bullet_point(tf.add_paragraph(), "• Cụm 2 (18.7%): VIP Chi tiêu lớn:", "Chi tiêu $9.5K, Hạn mức cao, Churn = 14.5% (Nhạy bén ưu đãi).")
format_bullet_point(tf.add_paragraph(), "• Cụm 3 (19.7%): Vay nợ quay vòng:", "Dư nợ $2.2K sinh lãi, Churn = 7.6% (Gắn kết nhất).")

add_speaker_note(s12, "Thuật toán K-Means kết hợp PCA đã tách biệt 4 phân cụm hành vi rõ rệt, định vị chính xác Cụm 1 là nhóm rủi ro Churn lên tới 41.8%.")

# ==============================================================================
# SLIDE 13: MÔ HÌNH HÓA MÁY HỌC — SO SÁNH 4 MÔ HÌNH
# ==============================================================================
s13 = prs.slides.add_slide(blank_layout)
set_bg(s13)
add_header(s13, "Mô Hình Hóa Dự Báo: XGBoost Vượt Trội Toàn Diện (ROC-AUC = 0.9930, Recall = 91.38%)", category_badge="MACHINE LEARNING")
add_footer(s13, 13)

create_card(s13, Inches(0.8), Inches(1.55), Inches(6.8), Inches(5.2))
s13.shapes.add_picture(os.path.join(FIG_DIR, "11_ml_model_comparison_roc.png"), Inches(0.95), Inches(1.75), width=Inches(6.5))

create_card(s13, Inches(7.9), Inches(1.55), Inches(4.633), Inches(5.2))
tb = s13.shapes.add_textbox(Inches(8.15), Inches(1.75), Inches(4.133), Inches(4.8))
tf = tb.text_frame
tf.word_wrap = True
tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0

p = tf.paragraphs[0]
p.text = "🏆 So Sánh Hiệu Năng 4 Thuật Toán"
p.font.name = FONT_TITLE
p.font.size = Pt(15.5)
p.font.bold = True
p.font.color.rgb = C_HVNH_NAVY
p.space_after = Pt(8)

format_bullet_point(tf.add_paragraph(), "• Logistic Regression (Baseline):", "ROC-AUC = 0.9348 | Recall = 83.38% | F1 = 67.25%")
format_bullet_point(tf.add_paragraph(), "• Decision Tree Classifier:", "ROC-AUC = 0.9458 | Recall = 88.92% | F1 = 76.15%")
format_bullet_point(tf.add_paragraph(), "• Random Forest Classifier:", "ROC-AUC = 0.9838 | Recall = 87.08% | F1 = 84.23%")
format_bullet_point(tf.add_paragraph(), "🌟 XGBOOST CLASSIFIER (TOP 1):", "• ROC-AUC: 0.9930 (Gần như tuyệt đối)\n• Recall: 91.38% (Bắt trúng >9/10 khách churn)\n• Precision: 87.61% | Accuracy: 96.54%", lead_color=C_ACCENT_GREEN)

add_speaker_note(s13, "XGBoost Classifier đạt hiệu năng vượt trội với ROC-AUC 0.9930 và Recall 91.38%, chứng minh khả năng phân tách phi tuyến xuất sắc.")

# ==============================================================================
# SLIDE 14: ĐÁNH GIÁ CHI TIẾT MA TRẬN NHẦM LẪN (CONFUSION MATRIX)
# ==============================================================================
s14 = prs.slides.add_slide(blank_layout)
set_bg(s14)
add_header(s14, "Đánh Giá Sai Số: Ma Trận Nhầm Lẫn & Khả Năng Kiểm Soát Báo Động Giả", category_badge="MODEL VALIDATION")
add_footer(s14, 14)

create_card(s14, Inches(0.8), Inches(1.55), Inches(6.8), Inches(5.2))
s14.shapes.add_picture(os.path.join(FIG_DIR, "12_ml_confusion_matrices.png"), Inches(0.95), Inches(1.75), width=Inches(6.5))

create_card(s14, Inches(7.9), Inches(1.55), Inches(4.633), Inches(5.2))
tb = s14.shapes.add_textbox(Inches(8.15), Inches(1.75), Inches(4.133), Inches(4.8))
tf = tb.text_frame
tf.word_wrap = True
tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0

p = tf.paragraphs[0]
p.text = "🎯 Kiểm Soát Sai Số Loại I & II"
p.font.name = FONT_TITLE
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = C_HVNH_NAVY
p.space_after = Pt(10)

format_bullet_point(tf.add_paragraph(), "• Sai số Loại II (False Negative):", "Chỉ bỏ sót 28/325 khách hàng rời bỏ trên tập kiểm thử độc lập (Tỷ lệ lỗi < 8.6%).")
format_bullet_point(tf.add_paragraph(), "• Sai số Loại I (False Positive):", "Chỉ có 42/1,701 khách hàng ở lại bị dự đoán nhầm (Tỷ lệ báo động giả < 2.5%).")
format_bullet_point(tf.add_paragraph(), "• Ý nghĩa kinh tế thực tế:", "Giúp ngân hàng can thiệp trúng đích khách hàng nguy cơ mà không lãng phí ngân sách ưu đãi cho khách hàng trung thành.")

add_speaker_note(s14, "Ma trận nhầm lẫn chứng minh XGBoost kiểm soát cả hai loại sai số cực tốt, tối ưu hóa chi phí vận hành cho ngân hàng.")

# ==============================================================================
# SLIDE 15: TOP ĐẶC TRƯNG QUYẾT ĐỊNH RỜI BỎ (FEATURE IMPORTANCE)
# ==============================================================================
s15 = prs.slides.add_slide(blank_layout)
set_bg(s15)
add_header(s15, "Giải Thích Mô Hình: 5 Đòn Bẩy Hành Vi Quyết Định Đến Nguy Cơ Rời Bỏ", category_badge="EXPLAINABLE AI")
add_footer(s15, 15)

create_card(s15, Inches(0.8), Inches(1.55), Inches(6.8), Inches(5.2))
s15.shapes.add_picture(os.path.join(FIG_DIR, "13_feature_importance_xgb.png"), Inches(0.95), Inches(1.75), width=Inches(6.5))

create_card(s15, Inches(7.9), Inches(1.55), Inches(4.633), Inches(5.2))
tb = s15.shapes.add_textbox(Inches(8.15), Inches(1.75), Inches(4.133), Inches(4.8))
tf = tb.text_frame
tf.word_wrap = True
tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0

p = tf.paragraphs[0]
p.text = "🔑 5 Đòn Bẩy Hành Vi Cốt Lõi"
p.font.name = FONT_TITLE
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = C_HVNH_NAVY
p.space_after = Pt(10)

format_bullet_point(tf.add_paragraph(), "1. Total_Trans_Ct (Số lần giao dịch):", "Đóng góp quan trọng nhất. Tần suất quẹt thẻ phản ánh nhịp tim gắn kết.")
format_bullet_point(tf.add_paragraph(), "2. Total_Ct_Chng_Q4_Q1:", "Mức độ sụt giảm số giao dịch trong quý cuối so với đầu năm.")
format_bullet_point(tf.add_paragraph(), "3. Total_Revolving_Bal:", "Dấu hiệu tất toán đưa dư nợ quay vòng về 0.")
format_bullet_point(tf.add_paragraph(), "4. Total_Trans_Amt:", "Quy mô ngân sách chi tiêu phân bổ qua thẻ.")
format_bullet_point(tf.add_paragraph(), "5. Relationship_Count & Contacts:", "Ràng buộc hệ sinh thái và mức độ bức xúc dịch vụ.")

add_speaker_note(s15, "Top 5 đặc trưng quan trọng nhất hoàn toàn tương thích với các quy luật nghiệp vụ đã phát hiện ở phần EDA.")

# ==============================================================================
# SLIDE 16: TỐI ƯU HÓA NGƯỠNG KINH TẾ (COST-BENEFIT OPTIMIZATION)
# ==============================================================================
s16 = prs.slides.add_slide(blank_layout)
set_bg(s16)
add_header(s16, "Tối Ưu Hóa Ngưỡng Quyết Định: Điểm Cân Bằng Lợi Nhuận Ròng Tại t = 0.42", category_badge="TỐI ƯU HÓA KINH TẾ")
add_footer(s16, 16)

create_card(s16, Inches(0.8), Inches(1.55), Inches(6.8), Inches(5.2))
s16.shapes.add_picture(os.path.join(FIG_DIR, "14_cost_benefit_threshold_optimization.png"), Inches(0.95), Inches(1.75), width=Inches(6.5))

create_card(s16, Inches(7.9), Inches(1.55), Inches(4.633), Inches(5.2))
tb = s16.shapes.add_textbox(Inches(8.15), Inches(1.75), Inches(4.133), Inches(4.8))
tf = tb.text_frame
tf.word_wrap = True
tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0

p = tf.paragraphs[0]
p.text = "💰 Mô Hình Hóa Chi Phí - Lợi Ích"
p.font.name = FONT_TITLE
p.font.size = Pt(15.5)
p.font.bold = True
p.font.color.rgb = C_HVNH_NAVY
p.space_after = Pt(8)

format_bullet_point(tf.add_paragraph(), "• Giả định bài toán kinh tế:", "• Giá trị CLV giữ chân: $500 / khách\n• Chi phí can thiệp ưu đãi: $50 / khách\n• Mất khách không can thiệp: -$500 / khách")
format_bullet_point(tf.add_paragraph(), "🎯 ĐIỂM CẮT TỐI ƯU (t = 0.42):", "• Thay vì dùng ngưỡng 0.50 mặc định, dịch chuyển ngưỡng sang t = 0.42 giúp tối đa hóa lợi nhuận ròng.\n• Recall đạt 94.0%, Precision đạt 86.2%.\n• Lợi nhuận ròng tối đa trên tập Test: > $112,000 USD.", lead_color=C_ACCENT_GREEN)

add_speaker_note(s16, "Ngưỡng cắt xác suất t = 0.42 mang lại lợi nhuận kinh tế tối đa cho ngân hàng theo mô hình chi phí - lợi ích.")

# ==============================================================================
# SLIDE 17: BA CHÂN DUNG KHÁCH HÀNG RỜI BỎ (CUSTOMER PERSONAS)
# ==============================================================================
s17 = prs.slides.add_slide(blank_layout)
set_bg(s17)
add_header(s17, "Phác Họa 3 Chân Dung Khách Hàng Rời Bỏ Điển Hình & Hành Động Can Thiệp", category_badge="CHÂN DUNG KHÁCH HÀNG")
add_footer(s17, 17)

personas = [
    ("CHÂN DUNG 1 (55% TỔNG CHURN)", "THE SILENT DEFECTOR\n(Ngủ đông & Rút lui lặng lẽ)", "• Dư nợ quay vòng = $0 USD\n• Quẹt thẻ < 45 lần/năm\n• Ngủ đông liên tiếp ≥ 3 tháng\n• Chi tiêu Q4 giảm > 50%\n\n💡 GIẢI PHÁP CAN THIỆP:\nTự động gửi E-voucher quẹt thẻ cuối tuần trên App, hoàn tiền 5% cho 3 giao dịch đầu tiên.", C_HVNH_NAVY),
    ("CHÂN DUNG 2 (25% TỔNG CHURN)", "FRUSTRATED COMPLAINER\n(Bức xúc Dịch vụ & Khiếu nại)", "• Gọi CSKH ≥ 3 - 6 lần/năm\n• Chỉ dùng 1 - 2 sản phẩm\n• Bất mãn về lỗi POS / phí phạt\n• Tỷ lệ Churn lên tới 35% - 100%\n\n💡 GIẢI PHÁP CAN THIỆP:\nĐội ngũ VIP Taskforce liên hệ hỗ trợ trong 24h, miễn giảm phí thường niên linh hoạt.", C_ACCENT_RED),
    ("CHÂN DUNG 3 (20% TỔNG CHURN)", "THE VIP SWITCHER\n(Khách VIP Chuyển dịch)", "• Thu nhập ≥ $120K, Thẻ Gold/Plat\n• Hạn mức tín dụng > $15K\n• Chi tiêu Q4 sụt giảm đột ngột\n• Bị đối thủ lôi kéo bằng đặc quyền\n\n💡 GIẢI PHÁP CAN THIỆP:\nCán bộ RM tặng lượt phòng chờ sân bay, nhân đôi điểm tích dặm bay du lịch.", C_BLUE_CYAN)
]

for idx, (p_tag, p_title, p_desc, p_col) in enumerate(personas):
    c_left = Inches(0.8 + idx * 3.98)
    create_card(s17, c_left, Inches(1.55), Inches(3.78), Inches(5.2))
    
    # Top card banner
    top_b = s17.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, c_left, Inches(1.55), Inches(3.78), Inches(0.1))
    top_b.fill.solid()
    top_b.fill.fore_color.rgb = p_col
    top_b.line.fill.background()
    
    tb = s17.shapes.add_textbox(c_left + Inches(0.18), Inches(1.75), Inches(3.42), Inches(4.8))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    
    p = tf.paragraphs[0]
    p.text = p_tag
    p.font.name = FONT_PRIMARY
    p.font.size = Pt(9.5)
    p.font.bold = True
    p.font.color.rgb = p_col
    p.space_after = Pt(4)
    
    p = tf.add_paragraph()
    p.text = p_title
    p.font.name = FONT_TITLE
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = C_HVNH_NAVY
    p.space_after = Pt(10)
    
    for line_txt in p_desc.split('\n'):
        if line_txt.strip():
            p = tf.add_paragraph()
            p.text = line_txt
            p.font.name = FONT_PRIMARY
            p.font.size = Pt(11)
            p.font.color.rgb = C_TEXT_DARK
            p.space_after = Pt(4)
            p.line_spacing = 1.15

add_speaker_note(s17, "Nhóm nghiên cứu xây dựng 3 chân dung khách hàng với hành vi và giải pháp can thiệp chuyên biệt, tăng tỷ lệ cứu vãn thành công.")

# ==============================================================================
# SLIDE 18: KHUNG CHIẾN LƯỢC GIỮ CHÂN 4 TẦNG & EWS
# ==============================================================================
s18 = prs.slides.add_slide(blank_layout)
set_bg(s18)
add_header(s18, "Khung Chiến Lược Giữ Chân Khách Hàng 4 Tầng & Hệ Thống Cảnh Báo Sớm (EWS)", category_badge="KHUYẾN NGHỊ QUẢN TRỊ")
add_footer(s18, 18)

tiers_data = [
    ("TẦNG 1: CẢNH BÁO SỚM (EWS)", "Giám sát tự động thời gian thực các Trigger Point:\n• Ngủ đông 2 tháng -> Đẩy Push Notification & E-voucher kích hoạt.\n• Gọi CSKH lần 3 -> Chuyển VIP Ticket xử lý khẩn cấp.", "KPI: Tỷ lệ phát hiện sớm > 90%", C_HVNH_NAVY),
    ("TẦNG 2: CSKH CHỦ ĐỘNG (PROACTIVE CARE)", "• Áp dụng chỉ tiêu First-Contact Resolution (FCR) giải quyết dứt điểm khiếu nại trong 24h.\n• Trao quyền Miễn giảm phí (Fee Waiver) linh hoạt cho nhân viên tổng đài.", "KPI: FCR > 85%, Churn CSKH < 5%", C_BLUE_CYAN),
    ("TẦNG 3: GAMIFIED LOYALTY & TÍCH ĐIỂM", "• Chiến dịch 'Quẹt Thẻ Mỗi Tuần' tích điểm theo tần suất quẹt thẻ thay vì chỉ tính theo số tiền.\n• Tự chọn danh mục hoàn tiền ưa thích (Ẩm thực, Mua sắm, Du lịch).", "KPI: Tần suất GD ≥ 5 lần/tháng", C_HVNH_ORANGE),
    ("TẦNG 4: BÁN CHÉO HỆ SINH THÁI (CROSS-SELLING)", "• Combo 'Tài chính Toàn diện' liên kết thẻ tín dụng với tài khoản lương và tiền gửi tiết kiệm.\n• Kích hoạt Auto-billing thanh toán hóa đơn điện nước để tăng rào cản chuyển đổi.", "KPI: Sở hữu ≥ 4 SP đạt > 65%", C_ACCENT_GREEN)
]

for idx, (t_title, t_desc, t_kpi, t_col) in enumerate(tiers_data):
    t_top = Inches(1.55 + idx * 1.3)
    create_card(s18, Inches(0.8), t_top, Inches(11.733), Inches(1.2))
    
    # Left vertical color stripe
    stripe = s18.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), t_top, Inches(0.12), Inches(1.2))
    stripe.fill.solid()
    stripe.fill.fore_color.rgb = t_col
    stripe.line.fill.background()
    
    tb = s18.shapes.add_textbox(Inches(1.05), t_top + Inches(0.1), Inches(8.2), Inches(1.0))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    
    p = tf.paragraphs[0]
    p.text = t_title
    p.font.name = FONT_TITLE
    p.font.size = Pt(13.5)
    p.font.bold = True
    p.font.color.rgb = t_col
    p.space_after = Pt(2)
    
    for line_txt in t_desc.split('\n'):
        if line_txt.strip():
            p = tf.add_paragraph()
            p.text = line_txt
            p.font.name = FONT_PRIMARY
            p.font.size = Pt(11)
            p.font.color.rgb = C_TEXT_DARK
            p.line_spacing = 1.15
            
    # Right KPI Box
    tb_kpi = s18.shapes.add_textbox(Inches(9.3), t_top + Inches(0.35), Inches(3.0), Inches(0.5))
    tf_kpi = tb_kpi.text_frame
    tf_kpi.word_wrap = True
    tf_kpi.margin_left = tf_kpi.margin_right = tf_kpi.margin_top = tf_kpi.margin_bottom = 0
    p_kpi = tf_kpi.paragraphs[0]
    p_kpi.alignment = PP_ALIGN.RIGHT
    p_kpi.text = t_kpi
    p_kpi.font.name = FONT_PRIMARY
    p_kpi.font.size = Pt(11)
    p_kpi.font.bold = True
    p_kpi.font.color.rgb = t_col

add_speaker_note(s18, "Khung chiến lược 4 tầng tạo nên hệ sinh thái giữ chân toàn diện, giải quyết từ cảnh báo sớm đến chăm sóc và gia tăng rào cản chuyển đổi.")

# ==============================================================================
# SLIDE 19: BÀI TOÁN KINH TẾ & TỶ SUẤT HOÀN VỐN ĐẦU TƯ (ROI = 500%)
# ==============================================================================
s19 = prs.slides.add_slide(blank_layout)
set_bg(s19)
add_header(s19, "Mô Phỏng Tài Chính: Lợi Nhuận Ròng Tăng +$400,000 USD/Năm (ROI = 500%)", category_badge="TÀI CHÍNH & ROI")
add_footer(s19, 19)

# Card trái: Giả định
create_card(s19, Inches(0.8), Inches(1.55), Inches(5.7), Inches(5.2))
tb = s19.shapes.add_textbox(Inches(1.05), Inches(1.75), Inches(5.2), Inches(4.8))
tf = tb.text_frame
tf.word_wrap = True
tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0

p = tf.paragraphs[0]
p.text = "📊 Giả Định Quy Mô 10,000 Khách Hàng"
p.font.name = FONT_TITLE
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = C_HVNH_NAVY
p.space_after = Pt(10)

format_bullet_point(tf.add_paragraph(), "• Quy mô cơ sở:", "10,000 chủ thẻ tín dụng đang hoạt động.")
format_bullet_point(tf.add_paragraph(), "• Tỷ lệ rời bỏ tự nhiên (16%):", "1,600 khách hàng rời bỏ mỗi năm.")
format_bullet_point(tf.add_paragraph(), "• Giá trị CLV trung bình:", "$500 USD / khách hàng.")
format_bullet_point(tf.add_paragraph(), "🚨 TỔN THẤT NẾU KHÔNG CAN THIỆP:", "1,600 khách × $500 = $800,000 USD / NĂM!", lead_color=C_ACCENT_RED)
format_bullet_point(tf.add_paragraph(), "🎯 Mục tiêu giữ chân với XGBoost:", "Cứu vãn thành công 60% số khách có nguy cơ = 960 KHÁCH HÀNG GIỮ LẠI.")

# Card phải: Tính ROI
create_card(s19, Inches(6.8), Inches(1.55), Inches(5.733), Inches(5.2))
tb = s19.shapes.add_textbox(Inches(7.05), Inches(1.75), Inches(5.233), Inches(4.8))
tf = tb.text_frame
tf.word_wrap = True
tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0

p = tf.paragraphs[0]
p.text = "💵 Tính Toán Lợi Nhuận & Tỷ Suất ROI"
p.font.name = FONT_TITLE
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = C_ACCENT_GREEN
p.space_after = Pt(10)

format_bullet_point(tf.add_paragraph(), "1. Giá trị CLV cứu vãn được:", "960 khách × $500 = $480,000 USD.")
format_bullet_point(tf.add_paragraph(), "2. Tổng chi phí can thiệp ưu đãi:", "1,600 khách × $50 = $80,000 USD.")
format_bullet_point(tf.add_paragraph(), "3. LỢI NHUẬN RÒNG GIA TĂNG:", "$480,000 - $80,000 = +$400,000 USD / NĂM!", lead_color=C_ACCENT_GREEN)
format_bullet_point(tf.add_paragraph(), "🚀 TỶ SUẤT HOÀN VỐN ĐẦU TƯ (ROI):", "ROI = ($400,000 / $80,000) × 100% = 500%!", lead_color=C_BLUE_CYAN)

add_speaker_note(s19, "Mô phỏng tài chính khẳng định đầu tư vào hệ thống giữ chân mang lại ROI lên đến 500%, bổ sung 400,000 USD lợi nhuận ròng hàng năm.")

# ==============================================================================
# SLIDE 20: KẾT LUẬN & HƯỚNG PHÁT TRIỂN / Q&A
# ==============================================================================
s20 = prs.slides.add_slide(blank_layout)
set_bg(s20, C_HVNH_NAVY)

# Top Orange Accent Stripe
top_bar = s20.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(0.12))
top_bar.fill.solid()
top_bar.fill.fore_color.rgb = C_HVNH_ORANGE
top_bar.line.fill.background()

tb20 = s20.shapes.add_textbox(Inches(1.0), Inches(1.5), Inches(11.333), Inches(4.5))
tf20 = tb20.text_frame
tf20.word_wrap = True

p = tf20.paragraphs[0]
p.text = "XIN TRÂN TRỌNG CẢM ƠN QUÝ THẦY/CÔ VÀ CÁC BẠN!"
p.font.name = FONT_TITLE
p.font.size = Pt(32)
p.font.bold = True
p.font.color.rgb = C_WHITE
p.alignment = PP_ALIGN.CENTER
p.space_after = Pt(14)

p = tf20.add_paragraph()
p.text = "HỌC VIỆN NGÂN HÀNG (BANKING ACADEMY OF VIETNAM) — KHOA HTTTQL"
p.font.name = FONT_PRIMARY
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = C_HVNH_GOLD
p.alignment = PP_ALIGN.CENTER
p.space_after = Pt(24)

p = tf20.add_paragraph()
p.text = "HỎI & ĐÁP (Q&A SESSION)"
p.font.name = FONT_TITLE
p.font.size = Pt(24)
p.font.bold = True
p.font.color.rgb = RGBColor(186, 230, 253)
p.alignment = PP_ALIGN.CENTER
p.space_after = Pt(12)

p = tf20.add_paragraph()
p.text = "Rất mong nhận được các ý kiến nhận xét và câu hỏi phản biện từ Hội đồng!"
p.font.name = FONT_PRIMARY
p.font.size = Pt(13)
p.font.color.rgb = RGBColor(226, 232, 240)
p.alignment = PP_ALIGN.CENTER

add_speaker_note(s20, "Em xin chân thành cảm ơn Quý Thầy/Cô và các bạn học viên đã chú ý theo dõi. Em xin sẵn sàng lắng nghe các câu hỏi phản biện từ Hội đồng.")

prs.save(PPTX_PATH)
print(f"🎉 Đã tạo thành công Master Slide PowerPoint Cao học tại: {PPTX_PATH}")
