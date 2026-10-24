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

# Theme Colors
C_NAVY = RGBColor(10, 37, 64)       # #0A2540
C_BLUE = RGBColor(0, 112, 243)      # #0070F3
C_CYAN = RGBColor(2, 132, 199)      # #0284C7
C_RED = RGBColor(239, 68, 68)       # #EF4444
C_GREEN = RGBColor(16, 185, 129)    # #10B981
C_WHITE = RGBColor(255, 255, 255)
C_DARK = RGBColor(15, 23, 42)       # #0F172A
C_MUTED = RGBColor(100, 116, 139)   # #64748B
C_BG = RGBColor(248, 250, 252)      # #F8FAFC
C_BORDER = RGBColor(226, 232, 240)  # #E2E8F0

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)

blank_slide_layout = prs.slide_layouts[6]

def set_slide_background(slide, color=C_BG):
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = color

def add_header(slide, title_text, category_text="HỌC VIỆN NGÂN HÀNG | BÀI TẬP GIỮA KỲ"):
    # Category tag
    tb_cat = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.3))
    tf_cat = tb_cat.text_frame
    tf_cat.word_wrap = True
    p_cat = tf_cat.paragraphs[0]
    p_cat.text = category_text.upper()
    p_cat.font.size = Pt(11)
    p_cat.font.bold = True
    p_cat.font.color.rgb = C_BLUE
    
    # Slide Title
    tb_title = slide.shapes.add_textbox(Inches(0.8), Inches(0.7), Inches(11.7), Inches(0.6))
    tf_title = tb_title.text_frame
    tf_title.word_wrap = True
    p_title = tf_title.paragraphs[0]
    p_title.text = title_text
    p_title.font.size = Pt(22)
    p_title.font.bold = True
    p_title.font.color.rgb = C_NAVY

def add_footer(slide, slide_num, total_slides=19):
    tb_f = slide.shapes.add_textbox(Inches(0.8), Inches(7.0), Inches(11.7), Inches(0.3))
    tf_f = tb_f.text_frame
    p_f = tf_f.paragraphs[0]
    p_f.text = f"Phân tích Dữ liệu Kinh doanh (HVNH) — Sinh viên: Đỗ Văn Đạt  |  Slide {slide_num}/{total_slides}"
    p_f.font.size = Pt(10)
    p_f.font.color.rgb = C_MUTED

def add_card(slide, left, top, width, height, bg_color=C_WHITE, border_color=C_BORDER):
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = bg_color
    shape.line.color.rgb = border_color
    shape.line.width = Pt(1.5)
    return shape

def add_speaker_note(slide, note_text):
    notes_slide = slide.notes_slide
    text_frame = notes_slide.notes_text_frame
    text_frame.text = note_text

print("🎨 Đang sinh bộ Slide PowerPoint 16:9 cao cấp...")

# ==========================================
# SLIDE 1: TITLE SLIDE
# ==========================================
s1 = prs.slides.add_slide(blank_slide_layout)
set_slide_background(s1, C_NAVY)

# Main Title Box
tb1 = s1.shapes.add_textbox(Inches(1.0), Inches(1.2), Inches(11.333), Inches(4.5))
tf1 = tb1.text_frame
tf1.word_wrap = True

p1 = tf1.paragraphs[0]
p1.text = "HỌC VIỆN NGÂN HÀNG (BANKING ACADEMY)"
p1.font.size = Pt(14)
p1.font.bold = True
p1.font.color.rgb = C_CYAN
p1.space_after = Pt(14)

p2 = tf1.add_paragraph()
p2.text = "XỬ LÝ DỮ LIỆU & KHAI PHÁ DỮ LIỆU"
p2.font.size = Pt(28)
p2.font.bold = True
p2.font.color.rgb = C_WHITE

p3 = tf1.add_paragraph()
p3.text = "PHÂN TÍCH HÀNH VI, PHÂN CỤM & DỰ BÁO NGUY CƠ RỜI BỎ\nCỦA KHÁCH HÀNG THẺ TÍN DỤNG (BANK CHURN ANALYSIS)"
p3.font.size = Pt(22)
p3.font.bold = True
p3.font.color.rgb = RGBColor(254, 202, 202) # Light Coral
p3.space_after = Pt(24)

p4 = tf1.add_paragraph()
p4.text = "• Học phần: Phân tích Dữ liệu trong Kinh doanh (Business Analytics)\n• Sinh viên thực hiện: ĐỖ VĂN ĐẠT\n• Tập dữ liệu: BankChurners.csv (10,127 quan sát, 23 thuộc tính)\n• Năm học: 2025 - 2026"
p4.font.size = Pt(14)
p4.font.color.rgb = RGBColor(226, 232, 240)

add_speaker_note(s1, "Kính chào Thầy/Cô và các bạn. Hôm nay em xin phép được trình bày Báo cáo bài tập giữa kỳ đề tài: Xử lý dữ liệu và Khai phá dữ liệu trên bộ dữ liệu khách hàng thẻ tín dụng BankChurners.")

# ==========================================
# SLIDE 2: BỐI CẢNH & BÀI TOÁN KINH TẾ
# ==========================================
s2 = prs.slides.add_slide(blank_slide_layout)
set_slide_background(s2)
add_header(s2, "1. Bối cảnh Kinh doanh & Bài toán Kinh tế Giữ chân Khách hàng")
add_footer(s2, 2)

# 3 Cards ngang
c_w = Inches(3.64)
c_h = Inches(4.8)
top_pos = Inches(1.6)

# Card 1: Nguồn thu thẻ
add_card(s2, Inches(0.8), top_pos, c_w, c_h)
tb = s2.shapes.add_textbox(Inches(0.95), top_pos + Inches(0.2), c_w - Inches(0.3), c_h - Inches(0.4))
tf = tb.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
p.text = "💳 Trụ Cột Lợi Nhuận Thẻ"
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = C_NAVY
p.space_after = Pt(10)
p = tf.add_paragraph()
p.text = "1. Phí quẹt thẻ (Interchange Fees) từ các điểm POS & E-commerce.\n\n2. Lãi suất tín dụng quay vòng (Revolving Interest) sinh lời cao nhất.\n\n3. Phí dịch vụ: Phí thường niên, phí chuyển đổi ngoại tệ, phí chậm trả."
p.font.size = Pt(13)
p.font.color.rgb = C_DARK

# Card 2: Quy tắc 5:1
add_card(s2, Inches(4.84), top_pos, c_w, c_h)
tb = s2.shapes.add_textbox(Inches(4.99), top_pos + Inches(0.2), c_w - Inches(0.3), c_h - Inches(0.4))
tf = tb.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
p.text = "⚖️ Bài Toán Chi Phí (CAC vs CRC)"
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = C_BLUE
p.space_after = Pt(10)
p = tf.add_paragraph()
p.text = "• Chi phí tìm khách mới (CAC) gấp 5 - 7 LẦN chi phí giữ chân khách cũ (CRC).\n\n• Tăng 5% tỷ lệ giữ chân giúp gia tăng 25% - 95% lợi nhuận ngân hàng (Bain & Co).\n\n• Mất 1 khách thẻ = Mất toàn bộ doanh thu phí + lãi suất tương lai."
p.font.size = Pt(13)
p.font.color.rgb = C_DARK

# Card 3: Thực trạng Churn
add_card(s2, Inches(8.88), top_pos, c_w, c_h)
tb = s2.shapes.add_textbox(Inches(9.03), top_pos + Inches(0.2), c_w - Inches(0.3), c_h - Inches(0.4))
tf = tb.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
p.text = "🚨 Thực Trạng Tỷ Lệ Rời Bỏ"
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = C_RED
p.space_after = Pt(10)
p = tf.add_paragraph()
p.text = "• Tỷ lệ Churn trong dữ liệu: 16.07% (1,627 / 10,127 khách hàng).\n\n• Cứ 6 khách hàng mở thẻ thì có 1 khách hàng đóng thẻ.\n\n• Thách thức: Phát hiện sớm 'tín hiệu ngầm' trước khi khách hàng đóng tài khoản."
p.font.size = Pt(13)
p.font.color.rgb = C_DARK

add_speaker_note(s2, "Mảng thẻ tín dụng là 'con gà đẻ trứng vàng' của ngân hàng bán lẻ, nhưng bài toán giữ chân đang trở nên cấp bách khi chi phí tìm khách mới gấp 5-7 lần chi phí giữ chân.")

# ==========================================
# SLIDE 3: KIẾN TRÚC QUY TRÌNH NGHIÊN CỨU
# ==========================================
s3 = prs.slides.add_slide(blank_slide_layout)
set_slide_background(s3)
add_header(s3, "2. Kiến Trúc Pipeline Xử Lý & Khai Phá Dữ Liệu Toàn Diện")
add_footer(s3, 3)

phases = [
    ("GIAI ĐOẠN 1", "TIỀN XỬ LÝ DỮ LIỆU", "• Loại 2 cột Naive Bayes nhiễu\n• Xử lý Missing bằng Median\n• Giữ 'Unknown' thành phân lớp\n• Feature Engineering 5 biến mới", C_NAVY),
    ("GIAI ĐOẠN 2", "KHÁM PHÁ DỮ LIỆU (EDA)", "• Phân tích Nhân khẩu học\n• Nhận diện Vùng rủi ro GD\n• Hiện tượng Dư nợ về 0\n• Ngưỡng báo động 3 lần gọi CSKH", C_BLUE),
    ("GIAI ĐOẠN 3", "KHAI PHÁ NÂNG CAO (ML)", "• Phân cụm 4 nhóm K-Means & PCA\n• Train 4 mô hình (LR, DT, RF, XGB)\n• Đánh giá ROC-AUC > 0.99\n• Tối ưu ngưỡng kinh tế giữ chân", C_CYAN),
    ("GIAI ĐOẠN 4", "ỨNG DỤNG QUẢN TRỊ", "• Xây dựng 3 Chân dung rủi ro\n• Khung Chiến lược 4 Tầng\n• Hệ thống Cảnh báo Sớm (EWS)\n• Mô phỏng ROI tài chính 500%", C_GREEN)
]

card_w = Inches(2.7)
card_h = Inches(4.8)
for idx, (p_tag, p_title, p_desc, p_col) in enumerate(phases):
    c_left = Inches(0.8 + idx * 2.95)
    add_card(s3, c_left, Inches(1.6), card_w, card_h)
    
    tb = s3.shapes.add_textbox(c_left + Inches(0.15), Inches(1.8), card_w - Inches(0.3), card_h - Inches(0.4))
    tf = tb.text_frame
    tf.word_wrap = True
    
    p = tf.paragraphs[0]
    p.text = p_tag
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = p_col
    
    p = tf.add_paragraph()
    p.text = p_title
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = C_NAVY
    p.space_after = Pt(12)
    
    p = tf.add_paragraph()
    p.text = p_desc
    p.font.size = Pt(12)
    p.font.color.rgb = C_DARK

add_speaker_note(s3, "Đề tài được triển khai qua 4 giai đoạn chuẩn mực từ Tiền xử lý, EDA chuyên sâu, Khai phá máy học đến Ứng dụng giải pháp kinh doanh.")

# ==========================================
# SLIDE 4: TIỀN XỬ LÝ & FEATURE ENGINEERING
# ==========================================
s4 = prs.slides.add_slide(blank_slide_layout)
set_slide_background(s4)
add_header(s4, "3. Quy Trình Tiền Xử Lý Dữ Liệu & Kỹ Thuật Tạo Biến")
add_footer(s4, 4)

# Cột trái: Làm sạch
add_card(s4, Inches(0.8), Inches(1.6), Inches(5.6), Inches(4.8))
tb = s4.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(5.2), Inches(4.4))
tf = tb.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
p.text = "🧹 Chiến Lược Làm Sạch Dữ Liệu"
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = C_NAVY
p.space_after = Pt(10)
p = tf.add_paragraph()
p.text = "1. Loại bỏ rò rỉ dữ liệu (Data Leakage):\n   Xóa 2 cột Naive Bayes thừa ở cuối bảng.\n\n2. Xử lý giá trị khuyết thiếu (Missing Values):\n   Điền Median cho các biến số bị khuyết lẻ tẻ để đảm bảo tính vững chắc trước ngoại lai.\n\n3. Bảo toàn nhóm 'Unknown':\n   Giữ nguyên danh mục 'Unknown' trong Học vấn (15%), Thu nhập (11%), Hôn nhân (7.4%) như một phân lớp thông tin hành vi độc lập."
p.font.size = Pt(12)
p.font.color.rgb = C_DARK

# Cột phải: Feature Engineering
add_card(s4, Inches(6.8), Inches(1.6), Inches(5.7), Inches(4.8))
tb = s4.shapes.add_textbox(Inches(7.0), Inches(1.8), Inches(5.3), Inches(4.4))
tf = tb.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
p.text = "⚙️ Kỹ Thuật Tạo Biến (Feature Engineering)"
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = C_BLUE
p.space_after = Pt(10)
p = tf.add_paragraph()
p.text = "• Avg_Trans_Value = Total_Trans_Amt / Total_Trans_Ct\n  (Giá trị chi tiêu trung bình / lần quẹt thẻ)\n\n• Revolving_Ratio = Total_Revolving_Bal / Credit_Limit\n  (Tỷ lệ dư nợ quay vòng trên hạn mức cấp)\n\n• Contact_Intensity = Contacts / (Inactive_Months + 1)\n  (Chỉ số bức xúc dịch vụ trên thời gian ngủ đông)\n\n• Age_Group: Phân 5 nhóm tuổi (<35, 35-44, 45-54, 55-64, 65+)\n\n• Churn_Binary: Mã hóa 1 (Attrited) / 0 (Existing)"
p.font.size = Pt(12)
p.font.color.rgb = C_DARK

add_speaker_note(s4, "Chúng em đặc biệt chú trọng khâu Feature Engineering để bóc tách các chỉ số tài chính và hành vi then chốt phục vụ phân cụm và mô hình hóa.")

# ==========================================
# SLIDE 5: BIẾN MỤC TIÊU & MẤT CÂN BẰNG LỚP
# ==========================================
s5 = prs.slides.add_slide(blank_slide_layout)
set_slide_background(s5)
add_header(s5, "4. Phân Bố Biến Mục Tiêu: Thách Thức Mất Cân Bằng Lớp")
add_footer(s5, 5)

# Cột trái: Ảnh
add_card(s5, Inches(0.8), Inches(1.6), Inches(6.2), Inches(4.8))
s5.shapes.add_picture(os.path.join(FIG_DIR, "01_churn_distribution.png"), Inches(1.0), Inches(1.8), width=Inches(5.8))

# Cột phải: Phân tích
add_card(s5, Inches(7.3), Inches(1.6), Inches(5.2), Inches(4.8))
tb = s5.shapes.add_textbox(Inches(7.5), Inches(1.8), Inches(4.8), Inches(4.4))
tf = tb.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
p.text = "📊 Thống Kê & Ý Nghĩa Nghiệp Vụ"
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = C_NAVY
p.space_after = Pt(10)
p = tf.add_paragraph()
p.text = "• Khách hàng ở lại (Existing): 8,500 người (83.93%)\n• Khách hàng rời bỏ (Attrited): 1,627 người (16.07%)\n\n⚖️ Tỷ lệ mất cân bằng: ~ 1 : 5.22\n\n🚨 Tác động đến Mô hình hóa Học máy:\n- Độ chính xác thuần túy (Accuracy) không phản ánh đúng thực chất (nếu đoán toàn bộ ở lại, Accuracy vẫn đạt 84%).\n- Bắt buộc phải tối ưu hóa Recall (Độ nhạy), Precision, F1-Score và ROC-AUC.\n- Sử dụng scale_pos_weight = 5.22 và class_weight='balanced' trong quá trình huấn luyện."
p.font.size = Pt(12)
p.font.color.rgb = C_DARK

add_speaker_note(s5, "Biến mục tiêu có tỷ lệ 16.07% Churn, bài toán imbalanced classification đòi hỏi mô hình phải tập trung vào Recall để không bỏ sót khách hàng rời bỏ.")

# ==========================================
# SLIDE 6: PHÂN TÍCH NHÂN KHẨU HỌC
# ==========================================
s6 = prs.slides.add_slide(blank_slide_layout)
set_slide_background(s6)
add_header(s6, "5. Phân Tích Nhân Khẩu Học & Tỷ Lệ Rời Bỏ")
add_footer(s6, 6)

add_card(s6, Inches(0.8), Inches(1.6), Inches(6.6), Inches(4.8))
s6.shapes.add_picture(os.path.join(FIG_DIR, "02_demographic_churn.png"), Inches(0.9), Inches(1.7), width=Inches(6.4))

add_card(s6, Inches(7.7), Inches(1.6), Inches(4.8), Inches(4.8))
tb = s6.shapes.add_textbox(Inches(7.9), Inches(1.8), Inches(4.4), Inches(4.4))
tf = tb.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
p.text = "🔍 Phát Hiện Trọng Tâm"
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = C_NAVY
p.space_after = Pt(10)
p = tf.add_paragraph()
p.text = "1. Giới tính (Gender):\n   Nữ có tỷ lệ rời bỏ cao hơn Nam đáng kể (17.36% vs 14.62%, p = 0.0002).\n\n2. Phân hóa Thu nhập 2 đầu (Bimodal Risk):\n   - Thu nhập < $40K: Churn 17.19% (áp lực phí).\n   - Thu nhập ≥ $120K: Churn 17.33% (đối thủ lôi kéo).\n   - Thu nhập $60K-$80K: Trung thành nhất (13.48%).\n\n3. Trình độ Học vấn:\n   Trình độ Tiến sĩ (Doctorate) có tỷ lệ rời bỏ cao nhất (21.06%)."
p.font.size = Pt(12)
p.font.color.rgb = C_DARK

add_speaker_note(s6, "Phân tích nhân khẩu học cho thấy hiện tượng phân hóa rủi ro ở 2 đầu thu nhập và khách hàng nữ có xu hướng rời bỏ cao hơn nam.")

# ==========================================
# SLIDE 7: HÀNH VI GIAO DỊCH - VÙNG NGUY CƠ CAO
# ==========================================
s7 = prs.slides.add_slide(blank_slide_layout)
set_slide_background(s7)
add_header(s7, "6. Hành Vi Giao Dịch: Nhận Diện 'Vùng Nguy Cơ Cao'")
add_footer(s7, 7)

add_card(s7, Inches(0.8), Inches(1.6), Inches(6.6), Inches(4.8))
s7.shapes.add_picture(os.path.join(FIG_DIR, "03_transaction_behavior_churn.png"), Inches(0.9), Inches(1.8), width=Inches(6.4))

add_card(s7, Inches(7.7), Inches(1.6), Inches(4.8), Inches(4.8))
tb = s7.shapes.add_textbox(Inches(7.9), Inches(1.8), Inches(4.4), Inches(4.4))
tf = tb.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
p.text = "🚨 Điểm Báo Động Hành Vi"
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = C_RED
p.space_after = Pt(10)
p = tf.add_paragraph()
p.text = "• Tổng số lần GD (Total_Trans_Ct):\n  Khách ở lại: 68.7 lần vs Khách churn: 44.9 lần (-34.6%, p < 0.0001).\n\n• Tổng tiền GD (Total_Trans_Amt):\n  Khách ở lại: $4,655 vs Khách churn: $3,095 (-33.5%, p < 0.0001).\n\n💡 VÙNG NGUY CƠ CAO (RED CLUSTER):\nKhách hàng có < 55 lần quẹt thẻ/năm và tổng chi tiêu < $3,000 tập trung dày đặc các trường hợp hủy thẻ. Tần suất quẹt thẻ chính là 'nhịp tim' của lòng trung thành."
p.font.size = Pt(12)
p.font.color.rgb = C_DARK

add_speaker_note(s7, "Scatter plot chỉ ra ranh giới tách biệt rõ ràng: khách hàng quẹt thẻ dưới 55 lần và chi tiêu dưới 3000 USD là vùng nguy cơ cực kỳ cao.")

# ==========================================
# SLIDE 8: HIỆN TƯỢNG DƯ NỢ VỀ 0
# ==========================================
s8 = prs.slides.add_slide(blank_slide_layout)
set_slide_background(s8)
add_header(s8, "7. Chỉ Số Tài Chính: Hiện Tượng 'Dư Nợ Quay Vòng Về 0'")
add_footer(s8, 8)

add_card(s8, Inches(0.8), Inches(1.6), Inches(6.6), Inches(4.8))
s8.shapes.add_picture(os.path.join(FIG_DIR, "04_financial_ratios_churn.png"), Inches(0.9), Inches(1.8), width=Inches(6.4))

add_card(s8, Inches(7.7), Inches(1.6), Inches(4.8), Inches(4.8))
tb = s8.shapes.add_textbox(Inches(7.9), Inches(1.8), Inches(4.4), Inches(4.4))
tf = tb.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
p.text = "📉 Tín Hiệu Dọn Đường Đóng Thẻ"
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = C_NAVY
p.space_after = Pt(10)
p = tf.add_paragraph()
p.text = "• Dư nợ quay vòng (Total_Revolving_Bal):\n  - Khách ở lại: Mean $1,257 (Median $1,364)\n  - Khách rời bỏ: Mean $673 (MEDIAN = $0.00!)\n\n• Tỷ lệ sử dụng hạn mức (Utilization Ratio):\n  - Khách ở lại: 29.64% (Median 21.1%)\n  - Khách rời bỏ: 16.25% (MEDIAN = 0.00%!)\n\n📌 Kết luận nghiệp vụ:\nTrước khi chính thức hủy thẻ, khách hàng có hành vi tất toán toàn bộ số dư nợ về 0 để tránh phát sinh lãi phạt và hoàn toàn ngừng quẹt thẻ."
p.font.size = Pt(12)
p.font.color.rgb = C_DARK

add_speaker_note(s8, "Hiện tượng dư nợ quay vòng về 0 là chỉ báo trễ then chốt cho thấy khách hàng chuẩn bị dọn đường hủy thẻ.")

# ==========================================
# SLIDE 9: TƯƠNG TÁC CSKH & RÀO CẢN ĐA SẢN PHẨM
# ==========================================
s9 = prs.slides.add_slide(blank_slide_layout)
set_slide_background(s9)
add_header(s9, "8. Tương Tác CSKH & Rào Cản Chuyển Đổi Hệ Sinh Thái")
add_footer(s9, 9)

# Nửa trên: 2 ảnh nhỏ
add_card(s9, Inches(0.8), Inches(1.6), Inches(5.7), Inches(4.8))
s9.shapes.add_picture(os.path.join(FIG_DIR, "05_interaction_decay_churn.png"), Inches(0.9), Inches(1.8), width=Inches(5.5))

add_card(s9, Inches(6.8), Inches(1.6), Inches(5.7), Inches(4.8))
s9.shapes.add_picture(os.path.join(FIG_DIR, "08_relationship_and_card.png"), Inches(6.9), Inches(1.8), width=Inches(5.5))

add_speaker_note(s9, "Ngưỡng bức xúc 3 lần liên hệ tổng đài và việc sở hữu trên 4 sản phẩm giúp hạ tỷ lệ rời bỏ xuống chỉ còn 10%.")

# ==========================================
# SLIDE 10: KHAI PHÁ DỮ LIỆU - PHÂN CỤM K-MEANS & PCA
# ==========================================
s10 = prs.slides.add_slide(blank_slide_layout)
set_slide_background(s10)
add_header(s10, "9. Khai Phá Dữ Liệu: Phân Cụm Hành Vi (K-Means & PCA)")
add_footer(s10, 10)

add_card(s10, Inches(0.8), Inches(1.6), Inches(6.6), Inches(4.8))
s10.shapes.add_picture(os.path.join(FIG_DIR, "10_kmeans_clusters_pca.png"), Inches(0.9), Inches(1.8), width=Inches(6.4))

add_card(s10, Inches(7.7), Inches(1.6), Inches(4.8), Inches(4.8))
tb = s10.shapes.add_textbox(Inches(7.9), Inches(1.8), Inches(4.4), Inches(4.4))
tf = tb.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
p.text = "👥 4 Phân Cụm Khách Hàng (k=4)"
p.font.size = Pt(15)
p.font.bold = True
p.font.color.rgb = C_NAVY
p.space_after = Pt(8)
p = tf.add_paragraph()
p.text = "• Cụm 0 (37.6%): Tiêu dùng phổ thông ổn định\n  (Chi tiêu $4.1K, Dư nợ $1.4K, Churn = 9.2%)\n\n• Cụm 1 (24.0%): Ngủ đông & Nguy cơ cao\n  (Chi tiêu $1.8K, Dư nợ $210, CHURN = 41.8%!)\n\n• Cụm 2 (18.7%): VIP Chi tiêu lớn\n  (Chi tiêu $9.5K, Hạn mức cao, Churn = 14.5%)\n\n• Cụm 3 (19.7%): Vay tín dụng quay vòng\n  (Dư nợ $2.2K sinh lãi cao, Churn = 7.6%)"
p.font.size = Pt(11.5)
p.font.color.rgb = C_DARK

add_speaker_note(s10, "K-Means phân cụm khách hàng thành 4 nhóm rõ rệt, trong đó Cụm 1 có tỷ lệ Churn lên đến 41.8%.")

# ==========================================
# SLIDE 11: MÔ HÌNH HÓA MÁY HỌC - SO SÁNH 4 MÔ HÌNH
# ==========================================
s11 = prs.slides.add_slide(blank_slide_layout)
set_slide_background(s11)
add_header(s11, "10. Mô Hình Hóa Máy Học Dự Báo Rời Bỏ (Supervised ML)")
add_footer(s11, 11)

add_card(s11, Inches(0.8), Inches(1.6), Inches(6.6), Inches(4.8))
s11.shapes.add_picture(os.path.join(FIG_DIR, "11_ml_model_comparison_roc.png"), Inches(0.9), Inches(1.8), width=Inches(6.4))

add_card(s11, Inches(7.7), Inches(1.6), Inches(4.8), Inches(4.8))
tb = s11.shapes.add_textbox(Inches(7.9), Inches(1.8), Inches(4.4), Inches(4.4))
tf = tb.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
p.text = "🏆 Hiệu Năng Vượt Trội của XGBoost"
p.font.size = Pt(15)
p.font.bold = True
p.font.color.rgb = C_NAVY
p.space_after = Pt(8)
p = tf.add_paragraph()
p.text = "• Logistic Regression: ROC-AUC = 0.9348, Recall = 83.38%, F1 = 67.25%\n\n• Decision Tree: ROC-AUC = 0.9458, Recall = 88.92%, F1 = 76.15%\n\n• Random Forest: ROC-AUC = 0.9838, Recall = 87.08%, F1 = 84.23%\n\n🌟 XGBOOST CLASSIFIER (TOP 1):\n- ROC-AUC: 0.9930 (Gần như hoàn hảo)\n- Recall (Độ nhạy): 91.38% (Bắt trúng >9/10 khách churn)\n- Precision: 87.61% | Accuracy: 96.54%"
p.font.size = Pt(11.5)
p.font.color.rgb = C_DARK

add_speaker_note(s11, "XGBoost đạt ROC-AUC 0.9930 và Recall 91.38%, vượt trội so với các thuật toán truyền thống.")

# ==========================================
# SLIDE 12: MA TRẬN NHẦM LẪN
# ==========================================
s12 = prs.slides.add_slide(blank_slide_layout)
set_slide_background(s12)
add_header(s12, "11. Đánh Giá Chi Tiết Ma Trận Nhầm Lẫn (Confusion Matrix)")
add_footer(s12, 12)

add_card(s12, Inches(0.8), Inches(1.6), Inches(6.6), Inches(4.8))
s12.shapes.add_picture(os.path.join(FIG_DIR, "12_ml_confusion_matrices.png"), Inches(0.9), Inches(1.8), width=Inches(6.4))

add_card(s12, Inches(7.7), Inches(1.6), Inches(4.8), Inches(4.8))
tb = s12.shapes.add_textbox(Inches(7.9), Inches(1.8), Inches(4.4), Inches(4.4))
tf = tb.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
p.text = "🎯 Kiểm Soát Sai Số Loại I & II"
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = C_NAVY
p.space_after = Pt(10)
p = tf.add_paragraph()
p.text = "• Sai số Loại II (False Negative - Bỏ sót khách Churn):\n  XGBoost chỉ bỏ sót 28/325 khách hàng rời bỏ trên tập Test (tỷ lệ lỗi < 8.6%).\n\n• Sai số Loại I (False Positive - Cảnh báo giả):\n  Chỉ có 42/1,701 khách hàng ở lại bị dự đoán nhầm (tỷ lệ báo động giả < 2.5%).\n\n💡 Ý nghĩa thực tế: Giúp ngân hàng can thiệp đúng đối tượng rủi ro mà không lãng phí ngân sách ưu đãi cho khách hàng trung thành."
p.font.size = Pt(12)
p.font.color.rgb = C_DARK

add_speaker_note(s12, "Ma trận nhầm lẫn chứng minh XGBoost kiểm soát cả hai loại sai số cực tốt, giảm thiểu lãng phí chi phí marketing.")

# ==========================================
# SLIDE 13: FEATURE IMPORTANCE
# ==========================================
s13 = prs.slides.add_slide(blank_slide_layout)
set_slide_background(s13)
add_header(s13, "12. Top Nhân Tố Quyết Định Rời Bỏ (Feature Importance)")
add_footer(s13, 13)

add_card(s13, Inches(0.8), Inches(1.6), Inches(6.6), Inches(4.8))
s13.shapes.add_picture(os.path.join(FIG_DIR, "13_feature_importance_xgb.png"), Inches(0.9), Inches(1.8), width=Inches(6.4))

add_card(s13, Inches(7.7), Inches(1.6), Inches(4.8), Inches(4.8))
tb = s13.shapes.add_textbox(Inches(7.9), Inches(1.8), Inches(4.4), Inches(4.4))
tf = tb.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
p.text = "🔑 5 Đòn Bẩy Hành Vi Cốt Lõi"
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = C_NAVY
p.space_after = Pt(10)
p = tf.add_paragraph()
p.text = "1. Total_Trans_Ct (Số lần giao dịch): Chi phối lớn nhất.\n\n2. Total_Ct_Chng_Q4_Q1 (Tốc độ suy giảm giao dịch quý cuối).\n\n3. Total_Revolving_Bal (Hành vi trả hết nợ về 0).\n\n4. Total_Trans_Amt (Quy mô ngân sách chi tiêu qua thẻ).\n\n5. Total_Relationship_Count (Số lượng sản phẩm gắn kết)."
p.font.size = Pt(12)
p.font.color.rgb = C_DARK

add_speaker_note(s13, "5 nhân tố quan trọng nhất phản ánh đúng bản chất hành vi tiêu dùng và động thái suy giảm gắn kết trước khi hủy thẻ.")

# ==========================================
# SLIDE 14: TỐI ƯU HÓA NGƯỠNG KINH TẾ
# ==========================================
s14 = prs.slides.add_slide(blank_slide_layout)
set_slide_background(s14)
add_header(s14, "13. Tối Ưu Hóa Ngưỡng Quyết Định & Bài Toán Kinh Tế")
add_footer(s14, 14)

add_card(s14, Inches(0.8), Inches(1.6), Inches(6.6), Inches(4.8))
s14.shapes.add_picture(os.path.join(FIG_DIR, "14_cost_benefit_threshold_optimization.png"), Inches(0.9), Inches(1.8), width=Inches(6.4))

add_card(s14, Inches(7.7), Inches(1.6), Inches(4.8), Inches(4.8))
tb = s14.shapes.add_textbox(Inches(7.9), Inches(1.8), Inches(4.4), Inches(4.4))
tf = tb.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
p.text = "💰 Tối Đa Hóa Lợi Nhuận Ròng"
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = C_NAVY
p.space_after = Pt(10)
p = tf.add_paragraph()
p.text = "• Giả định bài toán kinh tế:\n  - Giá trị CLV giữ chân: $500 / khách\n  - Chi phí can thiệp / quà tặng: $50 / khách\n  - Mất khách không can thiệp: -$500 / khách\n\n🎯 KẾT QUẢ TỐI ƯU:\n- Ngưỡng cắt xác suất tối ưu: t = 0.42 (thay vì 0.50 mặc định).\n- Đạt điểm cân bằng hoàn hảo giữa Recall (94%) và Precision (86%).\n- Lợi nhuận ròng tối đa trên tập Test: > $112,000 USD."
p.font.size = Pt(12)
p.font.color.rgb = C_DARK

add_speaker_note(s14, "Ngưỡng cắt xác suất t=0.42 mang lại lợi nhuận kinh tế tối đa cho ngân hàng theo mô hình chi phí - lợi ích.")

# ==========================================
# SLIDE 15: BA CHÂN DUNG KHÁCH HÀNG RỜI BỎ
# ==========================================
s15 = prs.slides.add_slide(blank_slide_layout)
set_slide_background(s15)
add_header(s15, "14. Ba Chân Dung Khách Hàng Rời Bỏ Điển Hình (Personas)")
add_footer(s15, 15)

personas = [
    ("CHÂN DUNG 1 (55%)", "THE SILENT DEFECTOR\n(Ngủ đông & Rút lui lặng lẽ)", "• Dư nợ quay vòng = $0\n• Quẹt thẻ < 45 lần/năm\n• Ngủ đông liên tiếp ≥ 3 tháng\n• Chi tiêu Q4 giảm > 50%\n\n💡 Hành động: Gửi Voucher kích hoạt quẹt thẻ cuối tuần, hoàn tiền 5% cho 3 GD đầu.", C_NAVY),
    ("CHÂN DUNG 2 (25%)", "FRUSTRATED COMPLAINER\n(Bức xúc Dịch vụ & Khiếu nại)", "• Gọi CSKH ≥ 3 - 6 lần\n• Chỉ dùng 1 - 2 sản phẩm\n• Bất mãn về lỗi POS / phí phạt\n• Churn rate lên tới 35% - 100%\n\n💡 Hành động: VIP Taskforce gọi hỗ trợ 24h, miễn giảm phí thường niên linh hoạt.", C_RED),
    ("CHÂN DUNG 3 (20%)", "THE VIP SWITCHER\n(Khách VIP Chuyển dịch)", "• Thu nhập ≥ $120K, Thẻ Gold/Plat\n• Hạn mức tín dụng > $15K\n• Chi tiêu Q4 sụt giảm đột ngột\n• Bị đối thủ hút bằng ưu đãi VIP\n\n💡 Hành động: Cán bộ RM tặng lượt phòng chờ sân bay, x2 điểm dặm bay du lịch.", C_BLUE)
]

for idx, (p_tag, p_title, p_desc, p_col) in enumerate(personas):
    c_left = Inches(0.8 + idx * 3.95)
    add_card(s15, c_left, Inches(1.6), Inches(3.7), Inches(4.8))
    tb = s15.shapes.add_textbox(c_left + Inches(0.15), Inches(1.8), Inches(3.4), Inches(4.4))
    tf = tb.text_frame
    tf.word_wrap = True
    
    p = tf.paragraphs[0]
    p.text = p_tag
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = p_col
    
    p = tf.add_paragraph()
    p.text = p_title
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = C_NAVY
    p.space_after = Pt(10)
    
    p = tf.add_paragraph()
    p.text = p_desc
    p.font.size = Pt(11.5)
    p.font.color.rgb = C_DARK

add_speaker_note(s15, "Nhóm nghiên cứu phân tách 3 chân dung khách hàng với hành vi và giải pháp can thiệp chuyên biệt.")

# ==========================================
# SLIDE 16: KHUNG CHIẾN LƯỢC GIỮ CHÂN 4 TẦNG
# ==========================================
s16 = prs.slides.add_slide(blank_slide_layout)
set_slide_background(s16)
add_header(s16, "15. Khung Chiến Lược Giữ Chân Khách Hàng 4 Tầng (4-Tier)")
add_footer(s16, 16)

tiers = [
    ("TẦNG 1: CẢNH BÁO SỚM (EWS)", "Giám sát tự động thời gian thực các Trigger Point:\n• Ngủ đông 2 tháng -> Đẩy Push Noti & E-voucher\n• Gọi CSKH lần 3 -> Chuyển VIP Ticket xử lý khẩn cấp", C_NAVY),
    ("TẦNG 2: CSKH CHỦ ĐỘNG (PROACTIVE CARE)", "• Áp dụng KPI First-Contact Resolution (FCR) xử lý dứt điểm khiếu nại trong 24h.\n• Chính sách Miễn giảm phí (Fee Waiver) linh hoạt cho khách hàng tốt.", C_BLUE),
    ("TẦNG 3: GAMIFIED LOYALTY & TÍCH ĐIỂM", "• Chiến dịch 'Quẹt Thẻ Mỗi Tuần' tích điểm theo tần suất quẹt thẻ thay vì chỉ tính theo số tiền.\n• Tự chọn danh mục hoàn tiền ưa thích (Ẩm thực, Mua sắm, Du lịch).", C_CYAN),
    ("TẦNG 4: BÁN CHÉO HỆ SINH THÁI (CROSS-SELLING)", "• Combo 'Tài chính Toàn diện' liên kết thẻ tín dụng với tài khoản lương và tiết kiệm.\n• Kích hoạt Auto-billing thanh toán hóa đơn điện nước để tăng rào cản chuyển đổi.", C_GREEN)
]

for idx, (t_title, t_desc, t_col) in enumerate(tiers):
    t_top = Inches(1.6 + idx * 1.25)
    add_card(s16, Inches(0.8), t_top, Inches(11.7), Inches(1.15))
    tb = s16.shapes.add_textbox(Inches(1.0), t_top + Inches(0.1), Inches(11.3), Inches(0.95))
    tf = tb.text_frame
    tf.word_wrap = True
    
    p = tf.paragraphs[0]
    p.text = t_title
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = t_col
    
    p = tf.add_paragraph()
    p.text = t_desc
    p.font.size = Pt(11)
    p.font.color.rgb = C_DARK

add_speaker_note(s16, "Khung chiến lược 4 tầng bao gồm: Cảnh báo sớm, CSKH chủ động, Gamified loyalty và Bán chéo đa sản phẩm.")

# ==========================================
# SLIDE 17: BÀI TOÁN TÀI CHÍNH & ROI 500%
# ==========================================
s17 = prs.slides.add_slide(blank_slide_layout)
set_slide_background(s17)
add_header(s17, "16. Bài Toán Kinh Tế & Mô Phỏng Hiệu Quả Đầu Tư (ROI)")
add_footer(s17, 17)

add_card(s17, Inches(0.8), Inches(1.6), Inches(5.7), Inches(4.8))
tb = s17.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(5.3), Inches(4.4))
tf = tb.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
p.text = "📊 Giả Định Quy Mô 10,000 Khách Hàng"
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = C_NAVY
p.space_after = Pt(10)
p = tf.add_paragraph()
p.text = "• Tổng khách hàng thẻ: 10,000 người\n• Tỷ lệ Churn hàng năm: 16% (1,600 khách rời bỏ)\n• Giá trị CLV trung bình: $500 / khách hàng\n\n🚨 Tổn thất nếu KHÔNG can thiệp:\n1,600 × $500 = $800,000 USD / năm\n\n🎯 Mục tiêu giữ chân với Mô hình XGBoost:\nCứu vãn thành công 60% khách hàng nguy cơ = 960 KHÁCH HÀNG GIỮ LẠI ĐƯỢC."
p.font.size = Pt(12)
p.font.color.rgb = C_DARK

add_card(s17, Inches(6.8), Inches(1.6), Inches(5.7), Inches(4.8))
tb = s17.shapes.add_textbox(Inches(7.0), Inches(1.8), Inches(5.3), Inches(4.4))
tf = tb.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
p.text = "💵 Tính Toán Lợi Nhuận & Tỷ Suất ROI"
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = C_GREEN
p.space_after = Pt(10)
p = tf.add_paragraph()
p.text = "1. Giá trị CLV cứu vãn được:\n   960 khách × $500 = $480,000 USD\n\n2. Tổng chi phí can thiệp (Voucher/Call):\n   1,600 khách × $50 = $80,000 USD\n\n3. LỢI NHUẬN RÒNG GIA TĂNG:\n   $480,000 - $80,000 = $400,000 USD / NĂM!\n\n🚀 TỶ SUẤT HOÀN VỐN ĐẦU TƯ (ROI):\n   ROI = ($400,000 / $80,000) × 100% = 500%!"
p.font.size = Pt(12)
p.font.color.rgb = C_DARK

add_speaker_note(s17, "Mô phỏng tài chính chứng minh chiến lược giữ chân mang lại ROI lên đến 500%, tăng thêm 400,000 USD lợi nhuận ròng mỗi năm.")

# ==========================================
# SLIDE 18: KẾT LUẬN & ĐỀ XUẤT
# ==========================================
s18 = prs.slides.add_slide(blank_slide_layout)
set_slide_background(s18)
add_header(s18, "17. Kết Luận & Hướng Phát Triển Đề Tài")
add_footer(s18, 18)

add_card(s18, Inches(0.8), Inches(1.6), Inches(5.7), Inches(4.8))
tb = s18.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(5.3), Inches(4.4))
tf = tb.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
p.text = "🎯 Đóng Góp Chính của Đề Tài"
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = C_NAVY
p.space_after = Pt(10)
p = tf.add_paragraph()
p.text = "1. Tiền xử lý & làm sạch 10,127 bản ghi, tạo 5 đặc trưng phái sinh có giá trị cao.\n\n2. Khám phá các quy luật hành vi cốt lõi: Vùng nguy cơ GD < 55 lần, dư nợ về 0, ngưỡng gọi CSKH 3 lần, rào cản chuyển đổi ≥ 4 sản phẩm.\n\n3. Mô hình XGBoost đạt ROC-AUC 0.9930, Recall 91.38%, tối ưu ngưỡng kinh tế t = 0.42.\n\n4. Đề xuất Khung chiến lược 4 tầng & EWS với ROI 500%."
p.font.size = Pt(12)
p.font.color.rgb = C_DARK

add_card(s18, Inches(6.8), Inches(1.6), Inches(5.7), Inches(4.8))
tb = s18.shapes.add_textbox(Inches(7.0), Inches(1.8), Inches(5.3), Inches(4.4))
tf = tb.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
p.text = "🚀 Hướng Phát Triển Cuối Kỳ (BTL)"
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = C_BLUE
p.space_after = Pt(10)
p = tf.add_paragraph()
p.text = "• Ứng dụng Explainable AI (SHAP / LIME):\n  Giải thích nguyên nhân rủi ro cho từng khách hàng cụ thể trên màn hình CRM của cán bộ ngân hàng.\n\n• Mô hình Ước lượng CLV Động (Dynamic CLV):\n  Tối ưu hóa ngân sách chi thưởng cá nhân hóa theo từng khách hàng VIP.\n\n• Tích hợp API Real-time Scoring:\n  Chấm điểm rủi ro ngay khi phát sinh giao dịch quẹt thẻ hoặc khiếu nại."
p.font.size = Pt(12)
p.font.color.rgb = C_DARK

add_speaker_note(s18, "Tóm tắt kết quả nghiên cứu và hướng mở rộng ứng dụng Explainable AI và Dynamic CLV cho bài tập lớn cuối kỳ.")

# ==========================================
# SLIDE 19: THANK YOU & Q&A
# ==========================================
s19 = prs.slides.add_slide(blank_slide_layout)
set_slide_background(s19, C_NAVY)

tb19 = s19.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(11.333), Inches(3.5))
tf19 = tb19.text_frame
tf19.word_wrap = True

p = tf19.paragraphs[0]
p.text = "XIN TRÂN TRỌNG CẢM ƠN!"
p.font.size = Pt(36)
p.font.bold = True
p.font.color.rgb = C_WHITE
p.alignment = PP_ALIGN.CENTER
p.space_after = Pt(16)

p = tf19.add_paragraph()
p.text = "Kính chúc Thầy/Cô và các bạn nhiều sức khỏe & thành công!"
p.font.size = Pt(18)
p.font.color.rgb = RGBColor(226, 232, 240)
p.alignment = PP_ALIGN.CENTER
p.space_after = Pt(24)

p = tf19.add_paragraph()
p.text = "HỎI & ĐÁP (Q&A)"
p.font.size = Pt(22)
p.font.bold = True
p.font.color.rgb = C_CYAN
p.alignment = PP_ALIGN.CENTER

add_speaker_note(s19, "Em xin chân thành cảm ơn Thầy/Cô và các bạn đã chú ý lắng nghe. Em rất mong nhận được những ý kiến đóng góp và câu hỏi phản biện từ Thầy/Cô.")

prs.save(PPTX_PATH)
print(f"🎉 Đã tạo thành công Master Slide PowerPoint tại: {PPTX_PATH}")
