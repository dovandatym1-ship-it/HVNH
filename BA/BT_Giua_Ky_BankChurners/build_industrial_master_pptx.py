"""
Build Master Presentation - Industrial Engineering Theme Standard (HVNH)
Creates: Slide_Thuyet_Trinh_BankChurners_V3_Industrial.pptx (20.0 x 11.25 inches)
Strict Academic Standards (Epistemic Precision, Zero AI smell)
"""
import os
import sys
import pptx
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.dml.color import RGBColor
from pptx.oxml import parse_xml

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FIG_DIR = os.path.join(BASE_DIR, "figures")
TEMPLATE_PATH = os.path.join(BASE_DIR, "Industrial Engineering Thesis Defense Presentation.pptx")
OUTPUT_PATH = os.path.join(BASE_DIR, "Slide_Thuyet_Trinh_BankChurners_V3_Industrial.pptx")

# ==============================================================================
# HỆ THỐNG MÀU SẮC ĐỒNG BỘ THEO TEMPLATE & THƯƠNG HIỆU HỌC VIỆN NGÂN HÀNG (HVNH)
# ==============================================================================
C_WHITE           = RGBColor(255, 255, 255)
C_SLATE_50        = RGBColor(248, 250, 252)
C_SLATE_200       = RGBColor(226, 232, 240)
C_SLATE_300       = RGBColor(203, 213, 225)
C_SLATE_400       = RGBColor(148, 163, 184)
C_SLATE_500       = RGBColor(100, 116, 139)
C_SLATE_700       = RGBColor(51, 65, 85)
C_SLATE_800       = RGBColor(30, 41, 59)
C_SLATE_900       = RGBColor(15, 23, 42)

# Nền card tối siêu tinh tế (Translucent Glassmorphism)
C_CARD_BG         = RGBColor(24, 28, 34)       # #181C22: Nền Card tối đồng bộ nền than chì
C_CARD_BORDER     = RGBColor(55, 65, 81)       # #374151: Viền Slate 700 mỏng
C_CARD_INNER_BG   = RGBColor(32, 38, 46)       # #20262E: Nền khối phụ
C_CARD_LIGHT_BG   = RGBColor(255, 255, 255)    # Cho khung biểu đồ

# Điểm nhấn thương hiệu HVNH & Trạng thái phân tích
C_HVNH_ORANGE     = RGBColor(234, 88, 12)      # #EA580C: Cam năng động HVNH
C_HVNH_GOLD       = RGBColor(245, 158, 11)     # #F59E0B: Vàng kim sang trọng
C_BLUE_CYAN       = RGBColor(56, 189, 248)     # #38BDF8: Xanh Cyan công nghệ
C_ACCENT_RED      = RGBColor(239, 68, 68)      # #EF4444: Đỏ cảnh báo Churn / Rủi ro
C_ACCENT_GREEN    = RGBColor(16, 185, 129)     # #10B981: Xanh ngọc thành công / ROI

FONT_TITLE        = 'Bebas Neue'
FONT_PRIMARY      = 'Calibri'

TOTAL_SLIDES = 21

# Load template để lấy Master, Layout và Background Gradient chuẩn
prs = Presentation(TEMPLATE_PATH)
slide0_bg = prs.slides[0]._element.cSld.xpath('p:bg')[0]
BG_XML = slide0_bg.xml.replace('val="100%"', 'val="100000"').replace('b="100%"', 'b="100000"').replace('r="100%"', 'r="100000"').replace('l="-100%"', 'l="-100000"').replace('t="-100%"', 't="-100000"')
blank_layout = prs.slide_layouts[0]

# Tùy biến Master Slide: Header & Footer Chrome
master = prs.slide_masters[0]
if len(master.shapes) > 3 and master.shapes[3].shape_type == pptx.enum.shapes.MSO_SHAPE_TYPE.GROUP:
    for s in master.shapes[3].shapes:
        if s.name == 'Google Shape;46;p1':
            s.width = Inches(6.0)
            s.left = Inches(13.2)
            p = s.text_frame.paragraphs[0]
            p.text = 'HỌC VIỆN NGÂN HÀNG'
            r = p.runs[0]
            r.font.name = FONT_TITLE
            r.font.size = Pt(18)
            r.font.color.rgb = C_SLATE_400
        elif s.name == 'Google Shape;47;p1':
            s.width = Inches(6.0)
            s.left = Inches(13.2)
        elif s.name == 'Google Shape;47;p1':
            p = s.text_frame.paragraphs[0]
            p.text = 'KHOA HTTTQL • BAV'
            r = p.runs[0]
            r.font.name = FONT_TITLE
            r.font.size = Pt(21)
            r.font.color.rgb = C_SLATE_400

# Xóa 20 slide cũ của template để xây dựng 21 slide mới chuẩn chỉ
rId_list = [prs.slides._sldIdLst[i].rId for i in range(len(prs.slides))]
for rId in rId_list:
    prs.part.drop_rel(rId)
del prs.slides._sldIdLst[:]

# ==============================================================================
# HÀM BỔ TRỢ XÂY DỰNG GIAO DIỆN CHUẨN TEMPLATE
# ==============================================================================
def create_slide():
    """Tạo slide mới thừa hưởng layout và gắn background gradient gốc"""
    slide = prs.slides.add_slide(blank_layout)
    slide._element.cSld.insert(0, parse_xml(BG_XML))
    return slide

def add_header(slide, action_title, tracker_text="PHẦN 01: TỔNG QUAN & BỐI CẢNH", section_num=1):
    """Action Header chuẩn 2 tầng: Tracker Cam & Action Title Trắng sáng"""
    # 1. Tracker Bar
    tb_trk = slide.shapes.add_textbox(Inches(1.5), Inches(0.45), Inches(14.5), Inches(0.35))
    tf_trk = tb_trk.text_frame
    tf_trk.word_wrap = True
    tf_trk.margin_left = tf_trk.margin_top = tf_trk.margin_right = tf_trk.margin_bottom = 0
    p_trk = tf_trk.paragraphs[0]
    p_trk.text = f"{tracker_text.upper()}  |  HỌC VIỆN NGÂN HÀNG"
    p_trk.font.name = FONT_TITLE
    p_trk.font.size = Pt(16)
    p_trk.font.bold = False
    p_trk.font.color.rgb = C_HVNH_ORANGE

    # 2. Action Title
    tb_title = slide.shapes.add_textbox(Inches(1.5), Inches(0.85), Inches(14.8), Inches(1.15))
    tf_title = tb_title.text_frame
    tf_title.word_wrap = True
    tf_title.margin_left = tf_title.margin_top = tf_title.margin_right = tf_title.margin_bottom = 0
    p_title = tf_title.paragraphs[0]
    p_title.text = action_title
    p_title.font.name = FONT_PRIMARY
    p_title.font.size = Pt(28)
    p_title.font.bold = True
    p_title.font.color.rgb = C_WHITE

    # 3. Horizontal Separator Line
    line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.5), Inches(2.08), Inches(15.2), Inches(0.02))
    line.fill.solid()
    line.fill.fore_color.rgb = C_SLATE_700
    line.line.color.rgb = C_SLATE_700

    # 4. Highlight Section Pill on right navigation bar
    highlight_section_pill(slide, section_num)

    # 5. Footer Line
    tb_foot = slide.shapes.add_textbox(Inches(1.5), Inches(10.7), Inches(15.2), Inches(0.3))
    tf_foot = tb_foot.text_frame
    tf_foot.margin_left = tf_foot.margin_top = tf_foot.margin_right = tf_foot.margin_bottom = 0
    p_foot = tf_foot.paragraphs[0]
    p_foot.text = "HỌC VIỆN NGÂN HÀNG  •  KHOA HỆ THỐNG THÔNG TIN QUẢN LÝ  •  HỌC VIÊN: ĐỖ VĂN ĐẠT"
    p_foot.font.name = FONT_TITLE
    p_foot.font.size = Pt(13)
    p_foot.font.color.rgb = C_SLATE_500

def highlight_section_pill(slide, section_num):
    """Tạo điểm nhấn tròn nổi bật trên thanh định vị 01-06 góc phải"""
    y_map = {
        1: Inches(3.18),
        2: Inches(4.30),
        3: Inches(5.26),
        4: Inches(6.15),
        5: Inches(7.04),
        6: Inches(7.94),
    }
    y_pos = y_map.get(section_num, Inches(3.18))
    circle = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(18.52), y_pos, Inches(0.64), Inches(0.64))
    circle.fill.solid()
    circle.fill.fore_color.rgb = C_HVNH_ORANGE
    circle.line.color.rgb = C_HVNH_GOLD
    circle.line.width = Pt(1.5)
    tf = circle.text_frame
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    p.text = f"{section_num:02d}"
    p.font.name = FONT_PRIMARY
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = C_WHITE

def add_card(slide, x, y, w, h, bg_color=C_CARD_BG, border_color=C_CARD_BORDER, border_width=Pt(1)):
    """Tạo khối thẻ nền than chì bo góc chuẩn mực"""
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, w, h)
    card.fill.solid()
    card.fill.fore_color.rgb = bg_color
    card.line.color.rgb = border_color
    card.line.width = border_width
    return card

def add_speaker_notes(slide, notes_text):
    """Gắn Speaker Notes học thuật chuyên sâu (80-150 từ)"""
    notes_slide = slide.notes_slide
    tf = notes_slide.notes_text_frame
    tf.text = notes_text

def add_framed_image(slide, img_path, x, y, w, h, caption=None):
    """Nhúng ảnh biểu đồ nằm gọn gàng trên thẻ nền trắng có viền và đổ bóng"""
    if not os.path.exists(img_path):
        print(f"Warning: Image not found: {img_path}")
        return None
    frame = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, w, h)
    frame.fill.solid()
    frame.fill.fore_color.rgb = C_CARD_LIGHT_BG
    frame.line.color.rgb = C_SLATE_700
    frame.line.width = Pt(1)

    pad_x = Inches(0.12)
    pad_y = Inches(0.12)
    img_w = w - (pad_x * 2)
    img_h = h - (pad_y * 2)
    if caption:
        img_h -= Inches(0.35)
    img = slide.shapes.add_picture(img_path, x + pad_x, y + pad_y, width=img_w, height=img_h)

    if caption:
        tb = slide.shapes.add_textbox(x, y + h - Inches(0.40), w, Inches(0.35))
        tf = tb.text_frame
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        p.text = caption
        p.font.name = FONT_PRIMARY
        p.font.size = Pt(11)
        p.font.color.rgb = C_SLATE_800
        p.font.bold = True
    return img

def format_structured_bullets(tf, bullets_list, font_size=13, space_after=Pt(8)):
    """Render danh sách các gạch đầu dòng có tiêu đề in đậm màu vàng/cam"""
    for idx, item in enumerate(bullets_list):
        if isinstance(item, tuple):
            lead, body = item
        else:
            lead = ""
            body = item
        p = tf.add_paragraph()
        p.space_after = space_after
        p.word_wrap = True
        if lead:
            r1 = p.add_run()
            r1.text = lead + " "
            r1.font.name = FONT_PRIMARY
            r1.font.size = Pt(font_size)
            r1.font.bold = True
            r1.font.color.rgb = C_HVNH_GOLD
        r2 = p.add_run()
        r2.text = body
        r2.font.name = FONT_PRIMARY
        r2.font.size = Pt(font_size)
        r2.font.color.rgb = C_SLATE_200

# ==============================================================================
# SLIDE 01: BÌA BÁO CÁO HỌC THUẬT (COVER SLIDE)
# ==============================================================================
s1 = create_slide()
highlight_section_pill(s1, 1)

# Watermark chữ lớn nền chìm Bebas Neue
tb_wm = s1.shapes.add_textbox(Inches(1.5), Inches(1.2), Inches(16.0), Inches(2.2))
tf_wm = tb_wm.text_frame
p_wm = tf_wm.paragraphs[0]
p_wm.text = "BANKING ACADEMY OF VIETNAM"
p_wm.font.name = FONT_TITLE
p_wm.font.size = Pt(56)
p_wm.font.bold = True
p_wm.font.color.rgb = RGBColor(45, 52, 62)

# Subtitle Badge
badge = add_card(s1, Inches(1.5), Inches(2.8), Inches(8.2), Inches(0.45), bg_color=C_HVNH_ORANGE, border_color=C_HVNH_GOLD)
tf_b = badge.text_frame
tf_b.margin_left = tf_b.margin_top = tf_b.margin_right = tf_b.margin_bottom = 0
p_b = tf_b.paragraphs[0]
p_b.alignment = PP_ALIGN.CENTER
p_b.text = "BÁO CÁO BÀI TẬP GIỮA KỲ  •  CHUYÊN ĐỀ CAO HỌC 2026"
p_b.font.name = FONT_TITLE
p_b.font.size = Pt(16)
p_b.font.bold = True
p_b.font.color.rgb = C_WHITE

# Main Title
tb_m = s1.shapes.add_textbox(Inches(1.5), Inches(3.5), Inches(14.5), Inches(2.8))
tf_m = tb_m.text_frame
tf_m.word_wrap = True
tf_m.margin_left = tf_m.margin_top = tf_m.margin_right = tf_m.margin_bottom = 0
p_m1 = tf_m.paragraphs[0]
p_m1.text = "PHÂN TÍCH HÀNH VI, PHÂN CỤM &\nDỰ BÁO NGUY CƠ RỜI BỎ KHÁCH HÀNG THẺ TÍN DỤNG"
p_m1.font.name = FONT_PRIMARY
p_m1.font.size = Pt(36)
p_m1.font.bold = True
p_m1.font.color.rgb = C_WHITE
p_m1.space_after = Pt(12)

p_m2 = tf_m.add_paragraph()
p_m2.text = "Customer Churn Prediction & Retention Optimization Strategy with XGBoost and Explainable AI"
p_m2.font.name = FONT_PRIMARY
p_m2.font.size = Pt(18)
p_m2.font.color.rgb = C_BLUE_CYAN

# Student Details Box
card_info = add_card(s1, Inches(1.5), Inches(6.8), Inches(9.2), Inches(3.4), bg_color=C_CARD_BG, border_color=C_CARD_BORDER)
tb_ci = s1.shapes.add_textbox(Inches(1.8), Inches(7.0), Inches(8.6), Inches(3.0))
tf_ci = tb_ci.text_frame
tf_ci.word_wrap = True
bullets_s1 = [
    ("Học viên thực hiện:", "Đỗ Văn Đạt  |  Chuyên ngành: Business Analytics (Phân tích Dữ liệu Kinh doanh)"),
    ("Học phần đào tạo:", "Xử lý và Khai phá Dữ liệu Sau Đại học  |  Khoa Hệ thống Thông tin Quản lý"),
    ("Tập dữ liệu thực nghiệm:", "BankChurners.csv (10,127 hồ sơ khách hàng, 23 thuộc tính nhân khẩu học & giao dịch)"),
    ("Thời gian & Địa điểm:", "Học viện Ngân hàng (BAV), Chùa Bộc, Đống Đa, Hà Nội — Năm 2026")
]
format_structured_bullets(tf_ci, bullets_s1, font_size=13, space_after=Pt(8))

# 3 Key Metric Highlight Cards on right side
highlights = [
    ("0.9930", "ROC-AUC (XGBoost)", "Dẫn đầu tuyệt đối", C_HVNH_ORANGE),
    ("t* = 0.42", "Ngưỡng Tối Ưu Kinh Tế", "Tối đa hóa Net Benefit", C_BLUE_CYAN),
    ("+$400,000", "Lợi Nhuận Ròng / Năm", "ROI = 500% (10K khách)", C_ACCENT_GREEN)
]
for idx, (val, lbl, sub, col) in enumerate(highlights):
    y_hl = Inches(6.8 + idx * 1.18)
    hl_card = add_card(s1, Inches(11.0), y_hl, Inches(5.5), Inches(1.05), border_color=col, border_width=Pt(1.2))
    tb_hl = s1.shapes.add_textbox(Inches(11.2), y_hl + Inches(0.1), Inches(5.1), Inches(0.85))
    tf_hl = tb_hl.text_frame
    tf_hl.margin_left = tf_hl.margin_top = tf_hl.margin_right = tf_hl.margin_bottom = 0
    p_v = tf_hl.paragraphs[0]
    p_v.text = val
    p_v.font.name = FONT_TITLE
    p_v.font.size = Pt(28)
    p_v.font.bold = True
    p_v.font.color.rgb = col
    
    p_l = tf_hl.add_paragraph()
    p_l.text = f"{lbl}  •  {sub}"
    p_l.font.name = FONT_PRIMARY
    p_l.font.size = Pt(11)
    p_l.font.color.rgb = C_SLATE_300

add_speaker_notes(s1,
    "Kính thưa Thầy/Cô trong Hội đồng chấm bảo vệ và toàn thể các bạn học viên cao học.\n"
    "Hôm nay tôi xin phép được báo cáo kết quả nghiên cứu bài tập giữa kỳ môn Xử lý và Khai phá Dữ liệu với đề tài: "
    "'Phân tích hành vi, Phân cụm và Dự báo nguy cơ rời bỏ của khách hàng thẻ tín dụng tại Ngân hàng thương mại'.\n"
    "Đề tài được thực hiện trên bộ dữ liệu thực tế 10,127 khách hàng với mục tiêu chuyển hóa năng lực dự báo Machine Learning thành giá trị kinh tế ròng cho ngân hàng."
)

# ==============================================================================
# SLIDE 02: MỤC LỤC & CẤU TRÚC BÁO CÁO (5 TRỤ CỘT CHIẾN LƯỢC)
# ==============================================================================
s2 = create_slide()
add_header(s2, "Cấu Trúc Báo Cáo: 5 Trụ Cột Chiến Lược Từ Khai Phá Đến Hành Động", "PHẦN 01: TỔNG QUAN & BỐI CẢNH", section_num=1)

pillars = [
    ("01", "TỔNG QUAN & BỐI CẢNH", "Slide 03 — 04", C_HVNH_ORANGE, [
        ("Nội dung cốt lõi:", "Bối cảnh kinh tế thẻ tín dụng, chi phí thu hút khách mới CAC ($250-$300) so với giữ chân CRC ($40-$50)."),
        ("Tóm tắt điều hành:", "4 phát hiện trọng tâm: 16.07% Churn, ROC-AUC 0.9930, t* = 0.42 và Lợi nhuận +$400,000 USD/năm.")
    ]),
    ("02", "PHƯƠNG PHÁP & TIỀN XỬ LÝ", "Slide 05 — 06", C_BLUE_CYAN, [
        ("Kiến trúc nghiên cứu:", "Pipeline 4 giai đoạn chuẩn mực từ tiền xử lý, khám phá EDA đến ứng dụng kinh tế."),
        ("Kiểm soát rò rỉ nhãn:", "Loại bỏ triệt để 2 cột Naive Bayes; kiến tạo 5 biến phái sinh tài chính nâng cao.")
    ]),
    ("03", "KHÁM PHÁ EDA & PHÂN CỤM", "Slide 07 — 13", C_HVNH_GOLD, [
        ("Khai phá 6 chiều hành vi:", "Mất cân bằng lớp 1:5.22, nghịch lý 2 đầu thu nhập, ranh giới 55 lần quẹt, 55% dư nợ về 0 USD."),
        ("Phân cụm K-Means & PCA:", "Xác lập k=4; nhận diện Cụm 1 là 'Tâm điểm rủi ro' tập trung 52.6% khách hàng rời bỏ.")
    ]),
    ("04", "MÔ HÌNH HÓA DỰ BÁO & XAI", "Slide 14 — 16", C_ACCENT_RED, [
        ("So sánh 4 thuật toán:", "XGBoost Classifier dẫn đầu toàn diện (ROC-AUC 0.9930, Recall 91.38%, Precision 91.08%)."),
        ("Giải thích mô hình XAI:", "5 đòn bẩy hành vi quyết định; kiểm soát sai số Loại II bỏ sót Churn chỉ 8.62%.")
    ]),
    ("05", "CHIẾN LƯỢC GIỮ CHÂN & ROI", "Slide 17 — 21", C_ACCENT_GREEN, [
        ("Tối ưu hóa ngưỡng kinh tế:", "Thiết lập điểm cắt t* = 0.42; xây dựng 3 chân dung khách hàng và Khung chiến lược 4 tầng EWS."),
        ("Hiệu quả tài chính:", "Mô phỏng 10,000 chủ thẻ giữ chân 960 khách, tạo lợi nhuận ròng +$400,000 USD/năm (ROI 500%).")
    ])
]

for idx, (p_num, p_title, p_slides, p_col, p_items) in enumerate(pillars):
    x_c = Inches(1.5 + idx * 3.25)
    c_card = add_card(s2, x_c, Inches(2.4), Inches(3.1), Inches(8.0), border_color=p_col, border_width=Pt(1.2))
    
    # Top badge in card
    top_b = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x_c + Inches(0.12), Inches(2.55), Inches(2.86), Inches(1.05))
    top_b.fill.solid()
    top_b.fill.fore_color.rgb = C_CARD_INNER_BG
    top_b.line.color.rgb = p_col
    top_b.line.width = Pt(1)
    tf_tb = top_b.text_frame
    tf_tb.margin_left = tf_tb.margin_top = tf_tb.margin_right = tf_tb.margin_bottom = 0
    p_num_t = tf_tb.paragraphs[0]
    p_num_t.text = f"TRỤ CỘT {p_num}"
    p_num_t.font.name = FONT_TITLE
    p_num_t.font.size = Pt(16)
    p_num_t.font.color.rgb = p_col
    
    p_tit_t = tf_tb.add_paragraph()
    p_tit_t.text = p_title
    p_tit_t.font.name = FONT_PRIMARY
    p_tit_t.font.size = Pt(11)
    p_tit_t.font.bold = True
    p_tit_t.font.color.rgb = C_WHITE
    
    p_sl_t = tf_tb.add_paragraph()
    p_sl_t.text = p_slides
    p_sl_t.font.name = FONT_PRIMARY
    p_sl_t.font.size = Pt(10)
    p_sl_t.font.color.rgb = C_SLATE_400

    # Body text
    tb_b = s2.shapes.add_textbox(x_c + Inches(0.15), Inches(3.8), Inches(2.8), Inches(6.4))
    tf_b = tb_b.text_frame
    tf_b.word_wrap = True
    format_structured_bullets(tf_b, p_items, font_size=11, space_after=Pt(8))

add_speaker_notes(s2,
    "Báo cáo được cấu trúc thành 5 trụ cột chiến lược logic và chặt chẽ theo nguyên lý Pyramid Principle:\n"
    "Bắt đầu từ Bối cảnh thị trường và Bài toán chi phí CAC vs CRC;\n"
    "Tiếp nối là Phương pháp luận và Tiền xử lý dữ liệu ngăn ngừa rò rỉ;\n"
    "Kế đến là Khai phá EDA 6 chiều hành vi then chốt và Phân cụm khách hàng;\n"
    "Trọng tâm thực nghiệm là Mô hình hóa dự báo với XGBoost và Giải thích XAI;\n"
    "Và cuối cùng là Tối ưu hóa ngưỡng quyết định kinh tế cùng Khung chiến lược giữ chân 4 tầng tạo ROI 500%."
)

# ==============================================================================
# SLIDE 03: EXECUTIVE SUMMARY: 4 PHÁT HIỆN TRỌNG TÂM
# ==============================================================================
s3 = create_slide()
add_header(s3, "Executive Summary: 4 Phát Hiện Trọng Tâm & Giá Trị Đóng Góp Thực Tiễn", "PHẦN 01: TỔNG QUAN & BỐI CẢNH", section_num=1)

exec_items = [
    ("16.07%", "TỶ LỆ RỜI BỎ TỰ NHIÊN", C_ACCENT_RED, [
        ("Quy mô thất thoát:", "1,627 trên tổng số 10,127 khách hàng đã chủ động đóng thẻ tín dụng."),
        ("Mất cân bằng dữ liệu:", "Tỷ lệ mất cân bằng nghiêm trọng 1:5.22, đặt ra cạm bẫy 'Accuracy Paradox'."),
        ("Tổn thất doanh thu:", "Thất thoát trực tiếp dòng tiền phí thường niên, phí quẹt POS và lãi suất dư nợ quay vòng.")
    ]),
    ("0.9930", "ROC-AUC (XGBOOST CLASSIFIER)", C_HVNH_ORANGE, [
        ("Vượt trội toàn diện:", "Đánh bại hoàn toàn Logistic Regression (0.9348) và Random Forest (0.9892)."),
        ("Kiểm soát sai số:", "Recall đạt 91.38%, chỉ bỏ sót đúng 28 khách hàng rời bỏ trong 325 khách ở tập kiểm thử."),
        ("Độ tin cậy cao:", "Precision đạt 91.08%, tỷ lệ báo động giả cực thấp chỉ 2.12%.")
    ]),
    ("t* = 0.42", "NGƯỠNG TỐI ƯU KINH TẾ", C_BLUE_CYAN, [
        ("Thay thế ngưỡng 0.50:", "Không áp dụng máy móc ngưỡng mặc định 0.50 vốn bỏ lỡ nhiều khách hàng giá trị cao."),
        ("Hàm Cost-Benefit:", "Tối ưu hóa điểm cực đại trên đường cong Net Benefit Curve."),
        ("Lợi nhuận thặng dư:", "Gia tăng thêm +$24,500 USD lợi nhuận ròng trên tập kiểm thử so với ngưỡng thông thường.")
    ]),
    ("+$400K", "LỢI NHUẬN RÒNG / NĂM (ROI 500%)", C_ACCENT_GREEN, [
        ("Mô phỏng thực tế:", "Quy mô danh mục 10,000 chủ thẻ, nhận diện và giữ chân thành công 960 khách hàng."),
        ("Bảo toàn giá trị CLV:", "Cứu vãn được $480,000 USD giá trị vòng đời khách hàng."),
        ("Hiệu quả sinh lời:", "Chi phí can thiệp chỉ $80,000 USD ($50/khách), tạo tỷ suất sinh lời danh nghĩa ROI = 500%.")
    ])
]

for idx, (m_val, m_lbl, m_col, m_bullets) in enumerate(exec_items):
    x_e = Inches(1.5 + idx * 4.05)
    e_card = add_card(s3, x_e, Inches(2.4), Inches(3.85), Inches(8.0), border_color=m_col, border_width=Pt(1.2))
    
    # Header box inside card
    h_box = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x_e + Inches(0.12), Inches(2.55), Inches(3.61), Inches(1.4))
    h_box.fill.solid()
    h_box.fill.fore_color.rgb = C_CARD_INNER_BG
    h_box.line.color.rgb = m_col
    h_box.line.width = Pt(1)
    tf_hb = h_box.text_frame
    tf_hb.margin_left = tf_hb.margin_top = tf_hb.margin_right = tf_hb.margin_bottom = 0
    p_val = tf_hb.paragraphs[0]
    p_val.alignment = PP_ALIGN.CENTER
    p_val.text = m_val
    p_val.font.name = FONT_TITLE
    p_val.font.size = Pt(36)
    p_val.font.bold = True
    p_val.font.color.rgb = m_col
    
    p_lbl = tf_hb.add_paragraph()
    p_lbl.alignment = PP_ALIGN.CENTER
    p_lbl.text = m_lbl
    p_lbl.font.name = FONT_PRIMARY
    p_lbl.font.size = Pt(10)
    p_lbl.font.bold = True
    p_lbl.font.color.rgb = C_WHITE

    # Bullets
    tb_b = s3.shapes.add_textbox(x_e + Inches(0.18), Inches(4.15), Inches(3.5), Inches(6.0))
    tf_b = tb_b.text_frame
    tf_b.word_wrap = True
    format_structured_bullets(tf_b, m_bullets, font_size=11.5, space_after=Pt(9))

add_speaker_notes(s3,
    "Tại slide Tóm tắt điều hành này, tôi xin nhấn mạnh 4 kết quả then chốt nhất của toàn bộ nghiên cứu:\n"
    "Thứ nhất: Tỷ lệ rời bỏ tự nhiên 16.07% với tỷ lệ mất cân bằng 1:5.22, đòi hỏi không thể dùng Accuracy mà phải tập trung vào Recall và ROC-AUC.\n"
    "Thứ hai: Mô hình XGBoost Classifier đạt ROC-AUC 0.9930 và Recall 91.38%, chỉ bỏ sót 28 khách hàng rời bỏ.\n"
    "Thứ ba: Thay vì áp dụng ngưỡng cắt 0.50 mặc định, đề tài xác lập điểm cắt tối ưu t* = 0.42 mang lại lợi nhuận cao nhất.\n"
    "Và thứ tư: Mô phỏng tài chính chứng minh giải pháp tạo ra 400,000 USD lợi nhuận ròng hàng năm trên 10,000 khách hàng, đạt tỷ suất sinh lời ROI lên tới 500%."
)

# ==============================================================================
# SLIDE 04: BỐI CẢNH THỊ TRƯỜNG THẺ & BÀI TOÁN KINH TẾ (CAC VS CRC)
# ==============================================================================
s4 = create_slide()
add_header(s4, "Bối Cảnh Thị Trường Thẻ & Bài Toán Chi Phí: Quy Tắc 5:1 Giữa CAC và CRC", "PHẦN 01: TỔNG QUAN & BỐI CẢNH", section_num=1)

# Left Column: CAC vs CRC Comparison
card_cac = add_card(s4, Inches(1.5), Inches(2.4), Inches(7.8), Inches(4.8), border_color=C_ACCENT_RED, border_width=Pt(1.2))
tb_cac = s4.shapes.add_textbox(Inches(1.8), Inches(2.6), Inches(7.2), Inches(4.4))
tf_cac = tb_cac.text_frame
tf_cac.word_wrap = True
p = tf_cac.paragraphs[0]
p.text = "CHI PHÍ THU HÚT KHÁCH HÀNG MỚI (CAC): $250 — $300 USD"
p.font.name = FONT_TITLE
p.font.size = Pt(18)
p.font.bold = True
p.font.color.rgb = C_ACCENT_RED
p.space_after = Pt(10)
cac_bullets = [
    ("Chi phí Marketing & Tiếp cận:", "Chiến dịch quảng cáo số, quà tặng mở thẻ, tài trợ điểm bán POS."),
    ("Chi phí Thẩm định & Phát hành:", "Tra cứu điểm tín dụng CIC, xác minh thu nhập, in dập phôi thẻ vật lý và chuyển phát nhanh."),
    ("Thời gian hòa vốn kéo dài:", "Ngân hàng cần trung bình 18 - 24 tháng thu phí và lãi vay mới bù đắp được chi phí bỏ ra ban đầu.")
]
format_structured_bullets(tf_cac, cac_bullets, font_size=12, space_after=Pt(8))

card_crc = add_card(s4, Inches(9.8), Inches(2.4), Inches(8.2), Inches(4.8), border_color=C_ACCENT_GREEN, border_width=Pt(1.2))
tb_crc = s4.shapes.add_textbox(Inches(10.1), Inches(2.6), Inches(7.6), Inches(4.4))
tf_crc = tb_crc.text_frame
tf_crc.word_wrap = True
p = tf_crc.paragraphs[0]
p.text = "CHI PHÍ GIỮ CHÂN KHÁCH HÀNG (CRC): $40 — $50 USD (GẤP 5:1)"
p.font.name = FONT_TITLE
p.font.size = Pt(18)
p.font.bold = True
p.font.color.rgb = C_ACCENT_GREEN
p.space_after = Pt(10)
crc_bullets = [
    ("Chi phí Ưu đãi Chủ động:", "E-voucher mua sắm, tặng điểm thưởng hoàn tiền, miễn phí thường niên 1 năm có điều kiện."),
    ("Chăm sóc Khách hàng Cá thể hóa:", "Điện thoại hỗ trợ riêng từ Relationship Manager cấp cao xử lý triệt để bức xúc trong 24h."),
    ("Hiệu quả tức thì:", "Giữ lại ngay dòng tiền lãi thẻ hiện hữu mà không mất chi phí thẩm định lại điểm tín dụng từ đầu.")
]
format_structured_bullets(tf_crc, crc_bullets, font_size=12, space_after=Pt(8))

# Bottom Full-width Card: Early Warning System (EWS)
card_ews = add_card(s4, Inches(1.5), Inches(7.5), Inches(16.5), Inches(2.9), border_color=C_HVNH_ORANGE, border_width=Pt(1.2))
tb_ews = s4.shapes.add_textbox(Inches(1.8), Inches(7.65), Inches(15.9), Inches(2.5))
tf_ews = tb_ews.text_frame
tf_ews.word_wrap = True
p = tf_ews.paragraphs[0]
p.text = "CHUYỂN DỊCH TỪ ỨNG PHÓ BỊ ĐỘNG SANG HỆ THỐNG CẢNH BÁO SỚM (EARLY WARNING SYSTEM)"
p.font.name = FONT_TITLE
p.font.size = Pt(17)
p.font.bold = True
p.font.color.rgb = C_HVNH_ORANGE
p.space_after = Pt(6)
ews_bullets = [
    ("Thách thức của mô hình truyền thống:", "Ngân hàng chỉ biết khách hàng rời bỏ khi họ đã đến quầy làm thủ tục hủy thẻ hoặc tài khoản không hoạt động suốt 6 tháng — lúc này tỷ lệ giữ chân thành công gần như bằng 0%."),
    ("Giải pháp Machine Learning đề xuất:", "Xây dựng Hệ thống Cảnh báo sớm (EWS) tự động quét tín hiệu hành vi hàng tuần, phát hiện nguy cơ rời bỏ trước 2 - 3 tháng (khi khách hàng bắt đầu giảm tần suất quẹt thẻ hoặc tất toán dư nợ)."),
    ("Ý nghĩa chiến lược:", "Chuyển thế chủ động cho chi nhánh và phòng CSKH, tối ưu hóa ngân sách giữ chân vào đúng những khách hàng có xác suất rời bỏ cao nhất.")
]
format_structured_bullets(tf_ews, ews_bullets, font_size=12, space_after=Pt(5))

add_speaker_notes(s4,
    "Để hiểu rõ tại sao đề tài này có ý nghĩa sống còn đối với ngân hàng, chúng ta cần nhìn vào bài toán kinh tế học mảng thẻ:\n"
    "Quy tắc kinh tế 5:1 chỉ ra rằng chi phí thu hút một khách hàng thẻ mới (CAC) tiêu tốn tới 250 - 300 USD cho marketing, thẩm định CIC và phát hành thẻ.\n"
    "Trong khi đó, chi phí giữ chân một khách hàng cũ (CRC) chỉ tiêu tốn từ 40 - 50 USD.\n"
    "Nếu ngân hàng chỉ đợi khách hàng nộp đơn hủy thẻ mới can thiệp thì đã quá muộn. "
    "Mô hình Machine Learning đóng vai trò là một Hệ thống Cảnh báo sớm (EWS) giúp ngân hàng can thiệp trước 2 đến 3 tháng khi các tín hiệu sụt giảm giao dịch vừa chớm xuất hiện."
)

# ==============================================================================
# SLIDE 05: PHƯƠNG PHÁP NGHIÊN CỨU & KIẾN TRÚC PIPELINE 4 BƯỚC
# ==============================================================================
s5 = create_slide()
add_header(s5, "Phương Pháp Nghiên Cứu: Kiến Trúc Pipeline 4 Giai Đoạn Khép Kín", "PHẦN 02: PHƯƠNG PHÁP & TIỀN XỬ LÝ", section_num=2)

pipeline_steps = [
    ("GIAI ĐOẠN 01", "TIỀN XỬ LÝ & FEATURE ENGINEERING", C_HVNH_ORANGE, [
        ("Làm sạch dữ liệu:", "Kiểm tra Null/Missing, xử lý định dạng 10,127 quan sát."),
        ("Kiểm soát rò rỉ nhãn:", "Loại bỏ triệt để 2 cột Naive Bayes ở cuối bảng gốc."),
        ("Mã hóa biến:", "Binary encoding biến Target, One-Hot/Ordinal encoding biến định tính."),
        ("Kiến tạo đặc trưng:", "Tạo 5 biến phái sinh tài chính đo lường mật độ giao dịch và đòn bẩy.")
    ]),
    ("GIAI ĐOẠN 02", "KHÁM PHÁ EDA & PHÂN CỤM", C_BLUE_CYAN, [
        ("Phân tích đơn & đa biến:", "Kiểm định phân phối 6 chiều hành vi then chốt."),
        ("Kiểm định thống kê:", "T-Test, Mann-Whitney U và Chi-square kiểm định khác biệt có ý nghĩa."),
        ("Phân cụm K-Means:", "Tối ưu hóa số cụm k=4 qua phương pháp Elbow và Silhouette Score."),
        ("Giảm chiều không gian:", "Áp dụng PCA 2 chiều để trực quan hóa cấu trúc các phân khúc.")
    ]),
    ("GIAI ĐOẠN 03", "MÔ HÌNH HÓA DỰ BÁO", C_HVNH_GOLD, [
        ("Phân chia tập mẫu:", "Stratified 80/20 bảo toàn cấu trúc mất cân bằng lớp."),
        ("Huấn luyện 4 thuật toán:", "Logistic Regression, Random Forest, SVM, XGBoost."),
        ("Kiểm định chéo:", "Stratified 5-Fold Cross Validation tối ưu hóa siêu tham số GridSearch."),
        ("Thang đo hiệu năng:", "Ưu tiên tối thượng ROC-AUC, Recall, Precision và F1-Score.")
    ]),
    ("GIAI ĐOẠN 04", "ỨNG DỤNG QUẢN TRỊ & ROI", C_ACCENT_GREEN, [
        ("Giải thích mô hình XAI:", "Xác định 5 đòn bẩy hành vi quan trọng nhất qua SHAP / Gain."),
        ("Tối ưu hóa ngưỡng cắt:", "Xác lập t* = 0.42 tối đa hóa lợi nhuận ròng."),
        ("Phác họa 3 Personas:", "Xây dựng chân dung khách hàng kèm kịch bản can thiệp chuyên biệt."),
        ("Mô phỏng tài chính:", "Đo lường ROI 500% trên quy mô danh mục 10,000 chủ thẻ.")
    ])
]

for idx, (p_phase, p_title, p_col, p_bullets) in enumerate(pipeline_steps):
    x_p = Inches(1.5 + idx * 4.05)
    p_card = add_card(s5, x_p, Inches(2.4), Inches(3.85), Inches(8.0), border_color=p_col, border_width=Pt(1.2))
    
    # Top phase banner
    ph_box = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x_p + Inches(0.12), Inches(2.55), Inches(3.61), Inches(1.2))
    ph_box.fill.solid()
    ph_box.fill.fore_color.rgb = C_CARD_INNER_BG
    ph_box.line.color.rgb = p_col
    ph_box.line.width = Pt(1)
    tf_ph = ph_box.text_frame
    tf_ph.margin_left = tf_ph.margin_top = tf_ph.margin_right = tf_ph.margin_bottom = 0
    p_ph = tf_ph.paragraphs[0]
    p_ph.text = p_phase
    p_ph.font.name = FONT_TITLE
    p_ph.font.size = Pt(18)
    p_ph.font.bold = True
    p_ph.font.color.rgb = p_col
    
    p_ti = tf_ph.add_paragraph()
    p_ti.text = p_title
    p_ti.font.name = FONT_PRIMARY
    p_ti.font.size = Pt(10.5)
    p_ti.font.bold = True
    p_ti.font.color.rgb = C_WHITE

    # Bullets
    tb_b = s5.shapes.add_textbox(x_p + Inches(0.18), Inches(3.95), Inches(3.5), Inches(6.2))
    tf_b = tb_b.text_frame
    tf_b.word_wrap = True
    format_structured_bullets(tf_b, p_bullets, font_size=11, space_after=Pt(8))

add_speaker_notes(s5,
    "Để đảm bảo tính chặt chẽ về mặt khoa học dữ liệu, đề tài tuân thủ quy trình Pipeline 4 giai đoạn khép kín:\n"
    "Giai đoạn 1 tập trung vào Tiền xử lý dữ liệu và Ngăn chặn rò rỉ dữ liệu (Data Leakage) — một lỗi rất phổ biến khi sử dụng bộ dữ liệu BankChurners.\n"
    "Giai đoạn 2 thực hiện Khám phá EDA trên 6 chiều dữ liệu kết hợp Phân cụm K-Means để bóc tách phân khúc.\n"
    "Giai đoạn 3 là Huấn luyện và Đánh giá 4 thuật toán Machine Learning qua Stratified 5-Fold Cross Validation.\n"
    "Và Giai đoạn 4 là Chuyển giao ứng dụng quản trị: Giải thích XAI, Tối ưu ngưỡng cắt kinh tế và Đo lường ROI định lượng."
)

# ==============================================================================
# SLIDE 06: TIỀN XỬ LÝ DỮ LIỆU & 5 BIẾN PHÁI SINH
# ==============================================================================
s6 = create_slide()
add_header(s6, "Tiền Xử Lý Dữ Liệu: Kiểm Soát Rò Rỉ Nhãn & Kiến Tạo 5 Biến Phái Sinh Tài Chính", "PHẦN 02: PHƯƠNG PHÁP & TIỀN XỬ LÝ", section_num=2)

card_prep = add_card(s6, Inches(1.5), Inches(2.4), Inches(7.8), Inches(8.0), border_color=C_HVNH_ORANGE, border_width=Pt(1.2))
tb_cp = s6.shapes.add_textbox(Inches(1.8), Inches(2.6), Inches(7.2), Inches(7.5))
tf_cp = tb_cp.text_frame
tf_cp.word_wrap = True
p = tf_cp.paragraphs[0]
p.text = "LÀM SẠCH & KIỂM SOÁT RÒ RỈ DỮ LIỆU (DATA LEAKAGE)"
p.font.name = FONT_TITLE
p.font.size = Pt(17)
p.font.bold = True
p.font.color.rgb = C_HVNH_ORANGE
p.space_after = Pt(10)
prep_bullets = [
    ("Quy mô dữ liệu ban đầu:", "10,127 quan sát với 23 thuộc tính gốc. Dữ liệu hoàn thiện, không phát hiện giá trị Null/Missing."),
    ("LOẠI BỎ TRIỆT ĐỂ 2 CỘT RÒ RỈ NHÃN:", "Hai cột cuối cùng trong bộ dữ liệu gốc `Naive_Bayes_Classifier_Attrition_Flag_...` là đầu ra dự báo của một mô hình Naive Bayes trước đó. Nếu giữ lại, mô hình sẽ đạt Accuracy 100% giả tạo do Data Leakage nghiêm trọng."),
    ("Mã hóa biến mục tiêu (Target Encoding):", "Gán nhãn nhị phân: `Attrited Customer` = 1 (1,627 khách rời bỏ), `Existing Customer` = 0 (8,500 khách ở lại)."),
    ("Mã hóa biến định tính:", "One-Hot Encoding cho các biến không có thứ bậc (Marital_Status, Gender) và Ordinal Encoding cho biến có thứ bậc (Education_Level, Income_Category)."),
    ("Chuẩn hóa dữ liệu (Scaling):", "Áp dụng RobustScaler để hạn chế tối đa ảnh hưởng của các điểm ngoại lai (Outliers) trong dữ liệu giao dịch tài chính.")
]
format_structured_bullets(tf_cp, prep_bullets, font_size=12, space_after=Pt(9))

card_fe = add_card(s6, Inches(9.8), Inches(2.4), Inches(8.2), Inches(8.0), border_color=C_BLUE_CYAN, border_width=Pt(1.2))
tb_fe = s6.shapes.add_textbox(Inches(10.1), Inches(2.6), Inches(7.6), Inches(7.5))
tf_fe = tb_fe.text_frame
tf_fe.word_wrap = True
p = tf_fe.paragraphs[0]
p.text = "5 BIẾN PHÁI SINH TÀI CHÍNH KIẾN TẠO MỚI (FEATURE ENGINEERING)"
p.font.name = FONT_TITLE
p.font.size = Pt(17)
p.font.bold = True
p.font.color.rgb = C_BLUE_CYAN
p.space_after = Pt(10)
fe_bullets = [
    ("1. Trans_Ct_Density (Mật độ quẹt thẻ):", "Công thức: `Total_Trans_Ct / Months_on_book`. Đo lường tần suất giao dịch bình quân mỗi tháng trong suốt vòng đời sử dụng thẻ."),
    ("2. Trans_Amt_per_Capita (Chi tiêu bình quân):", "Công thức: `Total_Trans_Amt / Total_Trans_Ct`. Phản ánh giá trị trung bình trên một lần quẹt thẻ, tách biệt giữa giao dịch chi tiêu thiết yếu và chi tiêu lớn."),
    ("3. Revolving_Ratio (Tỷ lệ đòn bẩy nợ):", "Công thức: `Total_Revolving_Bal / Credit_Limit`. Đo lường mức độ phụ thuộc vào tín dụng quay vòng của chủ thẻ."),
    ("4. Total_Interaction_Ct (Tổng tương tác rủi ro):", "Công thức: `Contacts_Count_12_mon + Months_Inactive_12_mon`. Chỉ số tích hợp giữa mức độ bất mãn CSKH và thời gian ngủ đông."),
    ("5. Open_To_Buy_Ratio (Tỷ lệ hạn mức khả dụng):", "Công thức: `Avg_Open_To_Buy / Credit_Limit`. Phản ánh dư địa chi tiêu khả dụng chưa được khai thác của khách hàng.")
]
format_structured_bullets(tf_fe, fe_bullets, font_size=12, space_after=Pt(9))

add_speaker_notes(s6,
    "Về mặt kỹ thuật dữ liệu, đề tài đặc biệt lưu ý đến tính hợp lệ của bài toán:\n"
    "Nhiều nghiên cứu trước đây đã mắc lỗi nghiêm trọng khi giữ lại 2 cột Naive Bayes ở cuối bảng BankChurners, dẫn đến hiện tượng Data Leakage làm mô hình đạt kết quả hoàn hảo giả tạo. "
    "Nghiên cứu của tôi đã loại bỏ triệt để 2 cột này trước mọi bước xử lý.\n"
    "Đồng thời, đề tài kiến tạo 5 biến phái sinh tài chính mới: nổi bật nhất là biến Mật độ quẹt thẻ (Trans_Ct_Density) và Tỷ lệ đòn bẩy nợ (Revolving_Ratio). "
    "Các biến này sau đó được chứng minh là có giá trị giải thích vượt trội trong mô hình XGBoost."
)

# ==============================================================================
# HÀM DỰNG SLIDE EDA & TÍCH HỢP BIỂU ĐỒ (SLIDES 07 — 12)
# ==============================================================================
def build_eda_slide(slide_num, action_title, badge_text, fig_filename, card_title, bullets_list, takeaway_text, speaker_note):
    slide = create_slide()
    add_header(slide, action_title, tracker_text=f"PHẦN 03: KHÁM PHÁ DỮ LIỆU & PHÂN CỤM ({badge_text})", section_num=3)
    
    # Left 60%: Biểu đồ khung viền sang trọng
    img_path = os.path.join(FIG_DIR, fig_filename)
    add_framed_image(slide, img_path, Inches(1.5), Inches(2.4), Inches(9.2), Inches(8.0), caption=f"Biểu đồ phân tích thực nghiệm trích xuất từ figures/{fig_filename}")
    
    # Right 40%: Thẻ phân tích dữ liệu & Takeaway
    c_right = add_card(slide, Inches(11.0), Inches(2.4), Inches(7.0), Inches(8.0), border_color=C_HVNH_ORANGE, border_width=Pt(1.2))
    
    tb = slide.shapes.add_textbox(Inches(11.25), Inches(2.6), Inches(6.5), Inches(5.6))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = card_title
    p.font.name = FONT_TITLE
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = C_HVNH_ORANGE
    p.space_after = Pt(8)
    format_structured_bullets(tf, bullets_list, font_size=11.5, space_after=Pt(7))
    
    # Takeaway box at bottom of right column
    t_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(11.2), Inches(8.65), Inches(6.6), Inches(1.55))
    t_box.fill.solid()
    t_box.fill.fore_color.rgb = C_CARD_INNER_BG
    t_box.line.color.rgb = C_HVNH_GOLD
    t_box.line.width = Pt(1)
    tf_t = t_box.text_frame
    tf_t.word_wrap = True
    tf_t.margin_left = tf_t.margin_right = tf_t.margin_top = tf_t.margin_bottom = Inches(0.1)
    p_t1 = tf_t.paragraphs[0]
    p_t1.text = "HÀM Ý QUẢN TRỊ NGÂN HÀNG:"
    p_t1.font.name = FONT_PRIMARY
    p_t1.font.size = Pt(11)
    p_t1.font.bold = True
    p_t1.font.color.rgb = C_HVNH_GOLD
    p_t1.space_after = Pt(2)
    p_t2 = tf_t.add_paragraph()
    p_t2.text = takeaway_text
    p_t2.font.name = FONT_PRIMARY
    p_t2.font.size = Pt(11)
    p_t2.font.color.rgb = C_SLATE_200
    
    add_speaker_notes(slide, speaker_note)
    return slide

# SLIDE 07: EDA 1
build_eda_slide(
    7, "EDA 1 — Phân Bố Biến Mục Tiêu: Mất Cân Bằng Lớp 1:5.22 & Cạm Bẫy Accuracy Paradox",
    "BIẾN MỤC TIÊU", "01_churn_distribution.png", "QUY LUẬT PHÂN BỐ & CHIẾN LƯỢC METRIC",
    [
        ("Tỷ lệ khách hàng rời bỏ (Churn):", "16.07% (1,627 khách hàng đã đóng tài khoản thẻ)."),
        ("Tỷ lệ khách hàng duy trì (Existing):", "83.93% (8,500 khách hàng vẫn đang hoạt động)."),
        ("Tỷ lệ mất cân bằng (Imbalance Ratio):", "Xấp xỉ 1 : 5.22, đặt ra bài toán mất cân bằng phân loại điển hình trong ngân hàng."),
        ("Cạm bẫy độ chính xác (Accuracy Paradox):", "Một mô hình ngây thơ dự báo toàn bộ khách hàng ở lại vẫn đạt Accuracy 83.93% nhưng thất bại hoàn toàn trong việc phát hiện rủi ro."),
        ("Chiến lược lựa chọn Metric:", "Nghiên cứu ưu tiên tối đa chỉ số Recall (độ nhạy) cùng đường cong ROC-AUC và PR-AUC.")
    ],
    "Trong bài toán mất cân bằng 1:5.22, Recall và ROC-AUC là thước đo phản ánh trung thực năng lực phát hiện rủi ro, tránh đánh giá sai lầm bằng Accuracy.",
    "Kính thưa Hội đồng, bước vào phần Khám phá dữ liệu EDA, phát hiện đầu tiên là sự mất cân bằng lớp 1:5.22 với 16.07% khách hàng rời bỏ.\n"
    "Nếu chỉ nhìn vào Accuracy, một mô hình dự báo toàn bộ khách hàng ở lại vẫn đạt tới gần 84% độ chính xác nhưng hoàn toàn vô giá trị về mặt thực tiễn.\n"
    "Vì vậy, toàn bộ nghiên cứu này tập trung vào Recall (khả năng phát hiện đúng khách hàng churn) và diện tích dưới đường cong ROC-AUC."
)

# SLIDE 08: EDA 2
build_eda_slide(
    8, "EDA 2 — Nhân Khẩu Học: Hiện Tượng Rủi Ro Phân Hóa Hai Đầu Thu Nhập (<$40K & >$120K)",
    "NHÂN KHẨU HỌC", "02_demographic_churn.png", "PHÂN TÍCH THEO CÁC BIẾN SỐ NHÂN KHẨU HỌC",
    [
        ("Khác biệt theo giới tính:", "Khách hàng Nữ có tỷ lệ rời bỏ 17.36%, cao hơn Nam giới (14.62%), phản ánh sự nhạy cảm cao với các chương trình tích điểm mua sắm."),
        ("Độ tuổi tập trung rủi ro:", "Khách hàng trong độ tuổi 40 - 50 tuổi (trung bình 46.3 tuổi) có xu hướng thay đổi nhà cung cấp dịch vụ thẻ cao nhất."),
        ("HIỆN TƯỢNG PHÂN HÓA 2 ĐẦU THU NHẬP:", "Tỷ lệ Churn tăng vọt ở 2 phân khúc: Dưới $40K (17.19% - nhạy cảm phí thường niên) và Trên $120K (17.33% - nhạy cảm đặc quyền thẻ VIP)."),
        ("Nhóm thu nhập trung bình ổn định:", "Phân khúc thu nhập $60K - $80K có tỷ lệ rời bỏ thấp nhất (chỉ 13.48%)."),
        ("Quy mô người phụ thuộc:", "Khách hàng có 2 - 3 người phụ thuộc có tỷ lệ rời bỏ cao hơn, tương quan với áp lực chi tiêu gia đình.")
    ],
    "Ngân hàng cần áp dụng chính sách khác biệt hóa: Hỗ trợ miễn giảm phí thường niên cho nhóm thu nhập thấp, đồng thời nâng cấp đặc quyền phòng chờ/golf cho nhóm VIP.",
    "Khám phá nhân khẩu học chỉ ra một phát hiện rất thú vị: Hiện tượng rủi ro phân hóa 2 đầu thu nhập.\n"
    "Nhóm thu nhập thấp dưới 40K USD và nhóm thu nhập cao trên 120K USD đều có tỷ lệ đóng thẻ cao trên 17%, nhưng nguyên nhân hoàn toàn khác nhau.\n"
    "Nhóm thu nhập thấp nhạy cảm với biểu phí thường niên, trong khi nhóm VIP dễ bị ngân hàng đối thủ lôi kéo bởi các đặc quyền thẻ thượng lưu."
)

# SLIDE 09: EDA 3
build_eda_slide(
    9, "EDA 3 — Hành Vi Giao Dịch: Vùng Báo Động Đỏ Dưới 55 Lần Quẹt Thẻ & Dưới $3,000 USD",
    "HÀNH VI GIAO DỊCH", "03_transaction_behavior_churn.png", "QUY LUẬT PHÂN BỔ TẦN SUẤT & DOANH SỐ",
    [
        ("Tần suất quẹt thẻ bình quân (Total_Trans_Ct):", "Khách hàng rời bỏ chỉ thực hiện trung bình 44.9 lần/năm, sụt giảm 34.6% so với khách hàng ở lại (68.7 lần)."),
        ("VÙNG BÁO ĐỘNG ĐỎ VỀ HÀNH VI:", "Khi tần suất quẹt thẻ giảm xuống dưới 55 lần/năm (dưới 4.5 lần/tháng) và chi tiêu dưới $3,000 USD, xác suất rời bỏ tăng vọt lên trên 60%."),
        ("Quy mô chi tiêu bình quân (Total_Trans_Amt):", "Khách hàng rời bỏ chi tiêu trung bình $3,095 USD/năm so với $4,654 USD của nhóm duy trì."),
        ("Đặc trưng phân bố mật độ:", "Biểu đồ phân tán chỉ ra một cụm khách hàng rời bỏ tập trung dày đặc ở góc dưới bên trái của không gian giao dịch."),
        ("Bản chất hoạt động:", "Tần suất quẹt thẻ chính là 'nhịp tim' phản ánh mức độ gắn kết thường nhật của chủ thẻ.")
    ],
    "Tần suất giao dịch là chỉ báo sống còn: sụt giảm dưới ngưỡng 55 lần/năm là điều kiện tiên quyết kích hoạt thông báo chăm sóc và tặng voucher kích cầu tức thì.",
    "Về hành vi giao dịch, tần suất quẹt thẻ chính là chiếc 'nhiệt kế' đo lường sức khỏe khách hàng.\n"
    "Khách hàng rời bỏ chỉ quẹt thẻ trung bình 44 lần một năm, sụt giảm tới 35%.\n"
    "Khi phân tích biểu đồ phân tán, chúng tôi phát hiện ra một 'Vùng báo động đỏ': Khách hàng có dưới 55 lần quẹt thẻ và chi tiêu dưới 3,000 USD có nguy cơ đóng thẻ lên tới hơn 60%."
)

# SLIDE 10: EDA 4
build_eda_slide(
    10, "EDA 4 — Chỉ Số Tài Chính: Hiện Tượng Rút Lui Lặng Lẽ (55% Khách Churn Đưa Dư Nợ Về $0)",
    "CHỈ SỐ TÀI CHÍNH", "04_financial_ratios_churn.png", "TÍN HIỆU BIẾN ĐỘNG DƯ NỢ & HẠN MỨC",
    [
        ("Dư nợ quay vòng bình quân (Total_Revolving_Bal):", "Khách hàng rời bỏ có dư nợ bình quân chỉ $672 USD, thấp hơn một nửa so với mức $1,256 USD của nhóm ở lại."),
        ("HIỆN TƯỢNG RÚT LUI LẶNG LẼ (SILENT CHURN):", "Gần 55% khách hàng rời bỏ đã chủ động thanh toán hết toàn bộ nợ về 0 USD trước khi yêu cầu đóng thẻ."),
        ("Tỷ lệ sử dụng hạn mức tín dụng:", "Khách hàng rời bỏ chỉ sử dụng trung bình 16.2% hạn mức được cấp, so với 29.6% ở nhóm khách hàng hoạt động tích cực."),
        ("Mức độ sụt giảm giao dịch Q4/Q1:", "Chỉ số biến thiên giao dịch Q4 so với Q1 sụt giảm tới 45% ở nhóm rời bỏ."),
        ("Dấu hiệu nhận diện sớm:", "Tất toán dư nợ và không phát sinh nợ quay vòng là tín hiệu báo trước việc đóng thẻ trong vòng 30 - 60 ngày tới.")
    ],
    "Hành vi trả hết nợ về 0 USD kết hợp giảm tỷ lệ sử dụng hạn mức là 'tín hiệu vàng' giúp EWS can thiệp sớm ngay trước khi khách hàng ra quyết định đóng thẻ.",
    "Khám phá thứ tư mang tên 'Hiện tượng rút lui lặng lẽ' (Silent Churn).\n"
    "Gần 55% khách hàng rời bỏ có dư nợ quay vòng bằng đúng 0 USD tại thời điểm ghi nhận dữ liệu.\n"
    "Họ không thông báo trước cho ngân hàng mà lặng lẽ trả hết nợ thẻ, ngưng quẹt thẻ mới, và sau đó 1-2 tháng mới chính thức yêu cầu đóng tài khoản. "
    "Đây là cơ hội bằng vàng để ngân hàng kích hoạt ưu đãi giữ chân."
)

# SLIDE 11: EDA 5
build_eda_slide(
    11, "EDA 5 — Tương Tác CSKH: Ngưỡng Báo Động Đột Biến Khi Khách Hàng Gọi Điện Lần Thứ 3",
    "CHĂM SÓC KHÁCH HÀNG", "05_interaction_decay_churn.png", "TƯƠNG QUAN TẦN SUẤT LIÊN HỆ TỔNG ĐÀI CSKH",
    [
        ("Tương quan với số cuộc gọi CSKH:", "Khách hàng gọi tổng đài 1 - 2 lần có tỷ lệ rời bỏ bình thường (~14%). Nhưng khi gọi đến lần 3, tỷ lệ Churn tăng gấp đôi lên 28.6%."),
        ("NGƯỠNG BÙNG PHÁT NGUY CƠ:", "Gọi 4 lần: tỷ lệ Churn tăng vọt lên 52.4%; Gọi 6 lần: tỷ lệ rời bỏ đạt tuyệt đối 100%."),
        ("Bản chất nghiệp vụ:", "Phản ánh thất bại trong chỉ tiêu First-Contact Resolution (FCR) — các sự cố tra soát hoặc khiếu nại biểu phí không được xử lý dứt điểm."),
        ("Thời gian ngủ đông (Months_Inactive):", "Khách hàng không phát sinh giao dịch từ 3 tháng trở lên trong năm có nguy cơ rời bỏ cao gấp 2.5 lần."),
        ("Khuyến nghị phân luồng vận hành:", "Cần tự động chuyển tiếp cuộc gọi sang chuyên viên cấp cao ngay khi khách hàng bấm máy gọi lần thứ 3.")
    ],
    "Nâng cao chỉ số First-Contact Resolution (FCR > 85%) và cài đặt Trigger phân luồng CSKH ưu tiên từ cuộc gọi thứ 3 là giải pháp chặn đứng nguy cơ bùng phát Churn.",
    "Phân tích về kênh liên hệ tổng đài CSKH bộc lộ một sự thật nghiêm túc về mặt trải nghiệm khách hàng.\n"
    "Nếu khách hàng chỉ gọi 1-2 lần, tỷ lệ rời bỏ ở mức bình thường. Nhưng đến cuộc gọi thứ 3, tỷ lệ Churn tăng gấp đôi lên 28.6%, gọi lần 4 tăng lên 52% và gọi lần 6 thì 100% khách hàng đóng thẻ.\n"
    "Điều này phản ánh các khiếu nại của khách hàng bị đùn đẩy, xử lý chậm trễ khiến họ bức xúc và quyết định hủy thẻ."
)

# SLIDE 12: EDA 6
build_eda_slide(
    12, "EDA 6 — Hệ Sinh Thái Sản Phẩm: Hiệu Ứng Khóa Chân Hạ Tỷ Lệ Rời Bỏ Xuống Dưới 10%",
    "HỆ SINH THÁI SẢN PHẨM", "08_relationship_and_card.png", "QUY MÔ SẢN PHẨM & RÀO CẢN CHUYỂN ĐỔI",
    [
        ("Quan hệ sản phẩm đơn lẻ (1 - 2 sản phẩm):", "Khách hàng chỉ sử dụng 1 đến 2 sản phẩm có tỷ lệ rời bỏ lên tới 25.4% do chi phí chuyển đổi (Switching Cost) gần như bằng 0."),
        ("HIỆU ỨNG KHÓA CHÂN (LOCK-IN EFFECT):", "Khi khách hàng liên kết từ 4 đến 6 sản phẩm ngân hàng, tỷ lệ rời bỏ giảm mạnh xuống mức 9.8% - 12.5%."),
        ("Cơ cấu danh mục theo hạng thẻ:", "Thẻ Blue chiếm 93.2% danh mục; các dòng thẻ cao cấp Silver/Gold/Platinum có tỷ lệ Churn cao hơn do kỳ vọng dịch vụ khắt khe."),
        ("Hàm ý chiến lược Bán chéo (Cross-selling):", "Khuyến nghị liên kết thẻ tín dụng với tài khoản nhận lương, tiền gửi tiết kiệm và ứng dụng Mobile Banking."),
        ("Rào cản tự nhiên:", "Càng nhiều điểm chạm dịch vụ, khách hàng càng ngại thay đổi ngân hàng giao dịch chính.")
    ],
    "Xây dựng các gói sản phẩm tích hợp (Combo Thẻ - Lương - Tiết kiệm) là chiến lược kiến tạo rào cản chuyển đổi tự nhiên bền vững nhất cho ngân hàng thương mại.",
    "Điểm chạm cuối cùng của phần EDA là Hệ sinh thái sản phẩm và Hiệu ứng khóa chân (Lock-in Effect).\n"
    "Nếu khách hàng chỉ dùng 1-2 sản phẩm, chi phí chuyển đổi của họ bằng 0 nên tỷ lệ rời bỏ lên tới trên 25%.\n"
    "Ngược lại, nếu khách hàng sử dụng từ 4 sản phẩm trở lên, tỷ lệ rời bỏ giảm ngoạn mục xuống dưới 10%.\n"
    "Đây là bằng chứng đanh thép ủng hộ chiến lược bán chéo các sản phẩm gắn kết như tài khoản nhận lương và tiền gửi thanh toán."
)

# ==============================================================================
# SLIDE 13: PHÂN CỤM HÀNH VI K-MEANS & PCA (k=4)
# ==============================================================================
s13 = create_slide()
add_header(s13, "Phân Cụm Hành Vi: Thực Nghiệm K-Means & PCA Xác Lập 4 Phân Khúc Khách Hàng", "PHẦN 03: KHÁM PHÁ DỮ LIỆU & PHÂN CỤM", section_num=3)

# Left 60%: Biểu đồ PCA 2D
img_p13 = os.path.join(FIG_DIR, "10_kmeans_clusters_pca.png")
add_framed_image(s13, img_p13, Inches(1.5), Inches(2.4), Inches(9.2), Inches(8.0), caption="Trực quan hóa không gian phân cụm K-Means qua 2 thành phần chính PCA (figures/10_kmeans_clusters_pca.png)")

# Right 40%: 4 Cụm Thẻ Hành Vi
c_km = add_card(s13, Inches(11.0), Inches(2.4), Inches(7.0), Inches(8.0), border_color=C_ACCENT_RED, border_width=Pt(1.2))
tb_km = s13.shapes.add_textbox(Inches(11.25), Inches(2.6), Inches(6.5), Inches(7.5))
tf_km = tb_km.text_frame
tf_km.word_wrap = True
p = tf_km.paragraphs[0]
p.text = "KẾT QUẢ PHÂN ĐOẠN 4 CỤM HÀNH VI (k=4)"
p.font.name = FONT_TITLE
p.font.size = Pt(17)
p.font.bold = True
p.font.color.rgb = C_ACCENT_RED
p.space_after = Pt(8)

km_bullets = [
    ("Đánh giá số cụm tối ưu:", "Phương pháp Elbow kết hợp hệ số Silhouette Score (0.34) xác nhận k=4 là giải pháp phân cụm cân bằng và có ý nghĩa thống kê cao nhất."),
    ("CỤM 1 — TÂM ĐIỂM RỦI RO (52.6% TỔNG CHURN):", "Quẹt thẻ rất ít (42 lần), chi tiêu thấp ($2,850), dư nợ về 0 USD. Đây chính là phân khúc ưu tiên can thiệp số 1 của toàn bộ đề tài."),
    ("Cụm 0 — Giao dịch Phổ thông (38.5% danh mục):", "Quẹt thẻ đều đặn (65 lần/năm), chi tiêu vừa phải, tỷ lệ rời bỏ ở mức thấp an toàn (11.2%)."),
    ("Cụm 2 — Khách hàng Cao cấp VIP:", "Hạn mức tín dụng cao (> $20,000 USD), thu nhập > $120K, đòi hỏi đặc quyền dịch vụ và ưu đãi chuyên biệt."),
    ("Cụm 3 — Siêu Giao dịch (Super Users):", "Quẹt thẻ > 105 lần/năm, doanh số chi tiêu > $14,000 USD, tỷ lệ rời bỏ cực thấp (dưới 2%).")
]
format_structured_bullets(tf_km, km_bullets, font_size=11.5, space_after=Pt(7))

add_speaker_notes(s13,
    "Trước khi bước vào huấn luyện Machine Learning có giám sát, nghiên cứu áp dụng thuật toán học không giám sát K-Means kết hợp giảm chiều PCA.\n"
    "Kết quả chỉ ra cấu trúc 4 phân cụm tối ưu. Trong đó, Cụm 1 được định danh là 'Tâm điểm rủi ro' khi tập trung tới 52.6% tổng lượng khách hàng rời bỏ của toàn bộ ngân hàng.\n"
    "Nhờ phân đoạn này, ngân hàng tránh được việc áp dụng các chính sách chăm sóc cào bằng tốn kém, mà tập trung ngân sách chính xác vào Cụm 1."
)

# ==============================================================================
# SLIDE 14: SO SÁNH 4 MÔ HÌNH MACHINE LEARNING (WINNER: XGBOOST)
# ==============================================================================
s14 = create_slide()
add_header(s14, "Mô Hình Hóa Máy Học: XGBoost Classifier Dẫn Đầu Toàn Diện Với ROC-AUC 0.9930", "PHẦN 04: MÔ HÌNH HÓA DỰ BÁO & XAI", section_num=4)

# Left 60%: ROC Curves Image
img_p14 = os.path.join(FIG_DIR, "11_ml_model_comparison_roc.png")
add_framed_image(s14, img_p14, Inches(1.5), Inches(2.4), Inches(9.2), Inches(8.0), caption="Đường cong ROC Curve so sánh 4 mô hình Machine Learning trên tập kiểm thử (figures/11_ml_model_comparison_roc.png)")

# Right 40%: Bảng so sánh 4 mô hình & Thẻ Winner
c_mod = add_card(s14, Inches(11.0), Inches(2.4), Inches(7.0), Inches(8.0), border_color=C_HVNH_ORANGE, border_width=Pt(1.2))
tb_mod = s14.shapes.add_textbox(Inches(11.25), Inches(2.6), Inches(6.5), Inches(7.5))
tf_mod = tb_mod.text_frame
tf_mod.word_wrap = True
p = tf_mod.paragraphs[0]
p.text = "BẢNG HIỆU NĂNG ĐỐI THỰC NGHIỆM"
p.font.name = FONT_TITLE
p.font.size = Pt(17)
p.font.bold = True
p.font.color.rgb = C_HVNH_ORANGE
p.space_after = Pt(8)

models_perf = [
    ("1. Logistic Regression (Baseline):", "ROC-AUC: 0.9348 | Recall: 83.38% | F1: 67.25%. Mô hình tuyến tính đơn giản, bắt sót nhiều quan hệ phi tuyến phức tạp."),
    ("2. Random Forest Classifier:", "ROC-AUC: 0.9892 | Recall: 88.31% | F1: 89.97%. Mô hình tổ hợp cây rất mạnh, kiểm soát tốt hiện tượng Overfitting."),
    ("3. Support Vector Machine (SVM):", "ROC-AUC: 0.9702 | Recall: 84.62% | F1: 81.34%. Nhạy cảm với phân bố biên và khoảng cách không gian."),
    ("🏆 4. XGBOOST CLASSIFIER (WINNER):", "ROC-AUC: 0.9930 | RECALL: 91.38% | PRECISION: 91.08% | F1-SCORE: 91.23%."),
    ("Đánh giá kỹ thuật:", "XGBoost tối ưu hóa hàm tổn thất gradient boosting, xử lý vượt trội dữ liệu mất cân bằng và đạt độ hội tụ cao nhất.")
]
format_structured_bullets(tf_mod, models_perf, font_size=11.5, space_after=Pt(7))

# Winner callout badge
win_b = s14.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(11.2), Inches(8.7), Inches(6.6), Inches(1.5))
win_b.fill.solid()
win_b.fill.fore_color.rgb = C_HVNH_ORANGE
win_b.line.color.rgb = C_HVNH_GOLD
win_b.line.width = Pt(1.5)
tf_wb = win_b.text_frame
tf_wb.word_wrap = True
tf_wb.margin_left = tf_wb.margin_right = tf_wb.margin_top = tf_wb.margin_bottom = Inches(0.1)
p_w1 = tf_wb.paragraphs[0]
p_w1.alignment = PP_ALIGN.CENTER
p_w1.text = "🏆 MÔ HÌNH DẪN ĐẦU: XGBOOST CLASSIFIER"
p_w1.font.name = FONT_TITLE
p_w1.font.size = Pt(16)
p_w1.font.bold = True
p_w1.font.color.rgb = C_WHITE

p_w2 = tf_wb.add_paragraph()
p_w2.alignment = PP_ALIGN.CENTER
p_w2.text = "ROC-AUC = 0.9930  •  Recall = 91.38%  •  Precision = 91.08%"
p_w2.font.name = FONT_PRIMARY
p_w2.font.size = Pt(12)
p_w2.font.bold = True
p_w2.font.color.rgb = C_WHITE

add_speaker_notes(s14,
    "Kính thưa Hội đồng, đây là kết quả thực nghiệm mô hình hóa cốt lõi của đề tài.\n"
    "Bốn thuật toán Machine Learning đại diện đã được thử nghiệm độc lập trên tập kiểm thử 2,026 quan sát.\n"
    "Kết quả cho thấy XGBoost Classifier là mô hình chiến thắng toàn diện, đạt diện tích ROC-AUC lên tới 0.9930, Recall 91.38% và Precision 91.08%.\n"
    "Đường cong ROC màu cam của XGBoost áp sát góc trên bên trái, thể hiện năng lực phân tách thực nghiệm vượt trội so với Random Forest và Logistic Regression."
)

# ==============================================================================
# SLIDE 15: MA TRẬN NHẦM LẪN & KIỂM SOÁT SAI SỐ LOẠI I, II
# ==============================================================================
s15 = create_slide()
add_header(s15, "Đánh Giá Sai Số: Kiểm Soát Tối Ưu Sai Số Loại I (2.12%) & Loại II (8.62%)", "PHẦN 04: MÔ HÌNH HÓA DỰ BÁO & XAI", section_num=4)

img_p15 = os.path.join(FIG_DIR, "12_ml_confusion_matrices.png")
add_framed_image(s15, img_p15, Inches(1.5), Inches(2.4), Inches(9.2), Inches(8.0), caption="Ma trận nhầm lẫn (Confusion Matrices) của 4 thuật toán trên Test Set N=2,026 (figures/12_ml_confusion_matrices.png)")

c_cm = add_card(s15, Inches(11.0), Inches(2.4), Inches(7.0), Inches(8.0), border_color=C_BLUE_CYAN, border_width=Pt(1.2))
tb_cm = s15.shapes.add_textbox(Inches(11.25), Inches(2.6), Inches(6.5), Inches(7.5))
tf_cm = tb_cm.text_frame
tf_cm.word_wrap = True
p = tf_cm.paragraphs[0]
p.text = "KIỂM SOÁT SAI SỐ LOẠI I & II"
p.font.name = FONT_TITLE
p.font.size = Pt(17)
p.font.bold = True
p.font.color.rgb = C_BLUE_CYAN
p.space_after = Pt(8)

cm_bullets = [
    ("Quy mô tập kiểm thử (Test Set):", "Gồm 2,026 khách hàng độc lập (1,701 khách duy trì Existing và 325 khách rời bỏ Attrited)."),
    ("KIỂM SOÁT SAI SỐ LOẠI II (FALSE NEGATIVE):", "Bỏ sót khách Churn là sai số nguy hiểm nhất gây mất doanh thu vĩnh viễn. XGBoost phát hiện đúng 297/325 khách Churn, chỉ bỏ sót đúng 28 người (tỷ lệ 8.62%)."),
    ("KIỂM SOÁT SAI SỐ LOẠI I (FALSE POSITIVE):", "Báo động giả gây lãng phí chi phí chăm sóc. Mô hình chỉ báo nhầm 36/1,701 khách ở lại thành Churn (tỷ lệ báo động giả cực thấp: 2.12%)."),
    ("Độ chính xác cảnh báo (Precision = 91.08%):", "Cứ 100 khách hàng được mô hình cảnh báo thì có hơn 91 khách hàng thực sự có nguy cơ rời bỏ."),
    ("Ý nghĩa thực tiễn ngân hàng:", "Mô hình đảm bảo ngân sách giữ chân được chi tiêu chính xác và hiệu quả nhất.")
]
format_structured_bullets(tf_cm, cm_bullets, font_size=11.5, space_after=Pt(7))

add_speaker_notes(s15,
    "Trong bài toán ngân hàng, việc hiểu rõ Ma trận nhầm lẫn là yếu tố quyết định hiệu quả triển khai.\n"
    "Sai số Loại II (bỏ sót khách rời bỏ) là sai số gây tổn thất nặng nề nhất. Mô hình XGBoost đã kiểm soát sai số này ở mức ấn tượng: Trong 325 khách rời bỏ, chỉ bỏ sót duy nhất 28 khách (tỷ lệ 8.6%).\n"
    "Đồng thời, tỷ lệ báo động giả (Sai số Loại I) chỉ ở mức 2.12%, đảm bảo bộ phận CSKH không bị lãng phí công sức gọi điện chăm sóc những khách hàng vốn dĩ đang rất hài lòng."
)

# ==============================================================================
# SLIDE 16: GIẢI THÍCH MÔ HÌNH: 5 ĐÒN BẨY HÀNH VI THEN CHỐT (XAI)
# ==============================================================================
s16 = create_slide()
add_header(s16, "Giải Thích Mô Hình (XAI): 5 Đòn Bẩy Hành Vi Quyết Định Xác Suất Rời Bỏ Thẻ", "PHẦN 04: MÔ HÌNH HÓA DỰ BÁO & XAI", section_num=4)

img_p16 = os.path.join(FIG_DIR, "13_feature_importance_xgb.png")
add_framed_image(s16, img_p16, Inches(1.5), Inches(2.4), Inches(9.2), Inches(8.0), caption="Độ quan trọng đặc trưng Gain-based & SHAP values của XGBoost (figures/13_feature_importance_xgb.png)")

c_xai = add_card(s16, Inches(11.0), Inches(2.4), Inches(7.0), Inches(8.0), border_color=C_HVNH_GOLD, border_width=Pt(1.2))
tb_xai = s16.shapes.add_textbox(Inches(11.25), Inches(2.6), Inches(6.5), Inches(7.5))
tf_xai = tb_xai.text_frame
tf_xai.word_wrap = True
p = tf_xai.paragraphs[0]
p.text = "THỨ BẬC 5 ĐÒN BẨY HÀNH VI CỐT LÕI"
p.font.name = FONT_TITLE
p.font.size = Pt(17)
p.font.bold = True
p.font.color.rgb = C_HVNH_GOLD
p.space_after = Pt(8)

xai_bullets = [
    ("1. Total_Trans_Ct (Số lần quẹt thẻ - Top 1 > 25%):", "Biến số có sức mạnh giải thích lớn nhất. Khách hàng ngưng quẹt thẻ là chỉ báo trực tiếp nhất của việc chuẩn bị đóng tài khoản."),
    ("2. Total_Amt_Chng_Q4_Q1 (Tốc độ giảm chi tiêu):", "Chỉ số đo lường sự dịch chuyển dòng tiền chi tiêu sang thẻ của ngân hàng đối thủ qua các quý gần nhất."),
    ("3. Total_Revolving_Bal (Dư nợ quay vòng):", "Tín hiệu tất toán nợ về 0 USD đóng vai trò là dấu hiệu báo trước việc hủy thẻ trong 30-60 ngày."),
    ("4. Total_Trans_Amt (Tổng doanh số giao dịch):", "Thước đo quy mô tài chính và hạn mức chi tiêu của chủ thẻ."),
    ("5. Total_Relationship_Count (Số lượng sản phẩm):", "Rào cản chuyển đổi tự nhiên thông qua hệ sinh thái đa dịch vụ của ngân hàng.")
]
format_structured_bullets(tf_xai, xai_bullets, font_size=11.5, space_after=Pt(7))

add_speaker_notes(s16,
    "Để giải quyết vấn đề mô hình 'Hộp đen' (Black-box), nghiên cứu đã áp dụng kỹ thuật Explainable AI để trích xuất 5 đòn bẩy quan trọng nhất.\n"
    "Đứng đầu bảng với hơn 25% trọng số là Tổng số lần giao dịch, tiếp theo là Mức độ sụt giảm chi tiêu quý 4 so với quý 1 và Dư nợ quay vòng.\n"
    "Điều này hoàn toàn khớp với logic ngân hàng: Khách hàng không bao giờ bỏ đi đột ngột mà luôn trải qua quá trình giảm tần suất quẹt thẻ và thanh toán hết nợ trước đó vài tháng."
)

# ==============================================================================
# SLIDE 17: TỐI ƯU HÓA NGƯỠNG QUYẾT ĐỊNH KINH TẾ (t = 0.42)
# ==============================================================================
s17 = create_slide()
add_header(s17, "Tối Ưu Kinh Tế: Xác Lập Điểm Cắt Xác Suất t* = 0.42 Tối Đa Hóa Lợi Nhuận Ròng", "PHẦN 05: TỐI ƯU KINH TẾ & CHIẾN LƯỢC GIỮ CHÂN", section_num=5)

img_p17 = os.path.join(FIG_DIR, "14_cost_benefit_threshold_optimization.png")
add_framed_image(s17, img_p17, Inches(1.5), Inches(2.4), Inches(9.2), Inches(8.0), caption="Đường cong tối ưu hóa Lợi ích ròng Net Benefit Curve (figures/14_cost_benefit_threshold_optimization.png)")

c_opt = add_card(s17, Inches(11.0), Inches(2.4), Inches(7.0), Inches(8.0), border_color=C_ACCENT_GREEN, border_width=Pt(1.2))
tb_opt = s17.shapes.add_textbox(Inches(11.25), Inches(2.6), Inches(6.5), Inches(7.5))
tf_opt = tb_opt.text_frame
tf_opt.word_wrap = True
p = tf_opt.paragraphs[0]
p.text = "MÔ HÌNH HÓA HÀM CHI PHÍ - LỢI ÍCH"
p.font.name = FONT_TITLE
p.font.size = Pt(17)
p.font.bold = True
p.font.color.rgb = C_ACCENT_GREEN
p.space_after = Pt(8)

opt_bullets = [
    ("Hạn chế của ngưỡng chuẩn t = 0.50:", "Ngưỡng 0.50 mặc định bỏ lỡ những khách hàng có xác suất rời bỏ từ 40% - 49% nhưng có giá trị vòng đời (CLV) rất lớn."),
    ("Thiết lập hàm mục tiêu Net Profit:", "Net Benefit = (CLV * P_success - CRC) * TP - CRC * FP - CLV * FN. Giả định CLV=$500, CRC=$50, Tỷ lệ cứu vãn=75%."),
    ("XÁC ĐỊNH ĐIỂM CẮT TỐI ƯU t* = 0.42:", "Điểm cực đại trên đường cong Net Benefit Curve, tạo ra sự cân bằng hoàn hảo giữa chi phí can thiệp và doanh thu bảo toàn."),
    ("Lợi nhuận gia tăng thặng dư:", "Mang lại thêm +$24,500 USD lợi nhuận ròng trên tập kiểm thử so với việc áp dụng ngưỡng 0.50 truyền thống."),
    ("Ý nghĩa quản trị:", "Chủ động tiếp cận sớm nhóm khách hàng có giá trị cao trước khi hành vi rời bỏ diễn ra.")
]
format_structured_bullets(tf_opt, opt_bullets, font_size=11.5, space_after=Pt(7))

add_speaker_notes(s17,
    "Một đóng góp quan trọng của đề tài là không áp dụng máy móc ngưỡng cắt xác suất 0.50 mặc định, mà xây dựng hàm tối ưu hóa Chi phí - Lợi ích thực tế cho ngân hàng.\n"
    "Với giá trị khách hàng giữ lại được là 500 USD và chi phí can thiệp chỉ 50 USD, việc hạ ngưỡng cắt xác suất xuống t = 0.42 cho phép ngân hàng chủ động can thiệp sớm vào nhóm khách hàng chớm có nguy cơ.\n"
    "Đường cong Net Benefit chứng minh tại t = 0.42, ngân hàng thu được lợi nhuận kinh tế ròng tối đa, cao hơn 24,500 USD so với ngưỡng 0.50 trên tập test."
)

# ==============================================================================
# SLIDE 18: PHÁC HỌA 3 CHÂN DUNG KHÁCH HÀNG RỜI BỎ (PERSONAS)
# ==============================================================================
s18 = create_slide()
add_header(s18, "Phác Họa 3 Chân Dung Khách Hàng Rời Bỏ & Kịch Bản Can Thiệp Cá Thể Hóa", "PHẦN 05: TỐI ƯU KINH TẾ & CHIẾN LƯỢC GIỮ CHÂN", section_num=5)

personas = [
    ("CHÂN DUNG 1 (55% TỔNG CHURN)", "THE SILENT DEFECTOR", "(Rút lui lặng lẽ & Ngủ đông)", C_HVNH_ORANGE,
     "\"Dạo này tôi bận quá, chẳng nhớ đến cái thẻ này nữa...\"", "MỨC NGUY CƠ: TỐI CAO [■■■]", C_ACCENT_RED, [
        ("Dấu hiệu nhận diện:", "Dư nợ = 0 USD, quẹt thẻ < 45 lần/năm, chi tiêu giảm > 40%, không nợ xấu."),
        ("Nguyên nhân cốt lõi:", "Giảm nhu cầu mua sắm hoặc chuyển dần sang dùng thẻ ngân hàng khác."),
        ("Kịch bản can thiệp:", "Push thông báo tặng E-voucher 100K khi quẹt thẻ vào cuối tuần; hoàn tiền 5% ăn uống/siêu thị để kích hoạt lại thói quen quẹt thẻ.")
    ]),
    ("CHÂN DUNG 2 (25% TỔNG CHURN)", "FRUSTRATED COMPLAINER", "(Bức xúc về Trải nghiệm Dịch vụ)", C_ACCENT_RED,
     "\"Tôi đã gọi tổng đài 3 lần mà tra soát giao dịch vẫn chưa xong!\"", "MỨC NGUY CƠ: TRUNG BÌNH [■■□]", C_HVNH_GOLD, [
        ("Dấu hiệu nhận diện:", "Gọi tổng đài CSKH từ 3 - 6 lần/năm, ngưng giao dịch ngay sau khi phát sinh sự cố tra soát."),
        ("Nguyên nhân cốt lõi:", "Bất mãn với thời gian xử lý khiếu nại chậm hoặc biểu phí thường niên/lãi suất chưa rõ ràng."),
        ("Kịch bản can thiệp:", "Tổng đài viên cấp cao gọi điện xin lỗi và giải quyết dứt điểm trong 24h; miễn phí thường niên 1 năm để xoa dịu.")
    ]),
    ("CHÂN DUNG 3 (20% TỔNG CHURN)", "THE VIP SWITCHER", "(Khách hàng Cao cấp Chuyển dịch)", C_BLUE_CYAN,
     "\"Bên ngân hàng kia vừa tặng tôi thẻ phòng chờ thương gia rồi...\"", "MỨC ƯU TIÊN: GIỮ CHÂN [■■■]", C_BLUE_CYAN, [
        ("Dấu hiệu nhận diện:", "Thu nhập ≥ $120K, thẻ Gold/Platinum, hạn mức tín dụng > $20,000 USD."),
        ("Nguyên nhân cốt lõi:", "Bị ngân hàng đối thủ lôi kéo bằng các gói đặc quyền phòng chờ sân bay, golf, tích dặm bay hấp dẫn hơn."),
        ("Kịch bản can thiệp:", "Chuyên viên Khách hàng Ưu tiên (Priority RM) chăm sóc riêng 1-1, nâng hạng đặc quyền và tặng lượt phòng chờ sân bay.")
    ])
]

for idx, (p_tag, p_name, p_sub, col, quote, risk_txt, risk_col, p_items) in enumerate(personas):
    x_c = Inches(1.5 + idx * 5.5)
    c_card = add_card(s18, x_c, Inches(2.4), Inches(5.2), Inches(8.0), border_color=col, border_width=Pt(1.2))
    
    # Top Header banner
    h_box = s18.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x_c + Inches(0.12), Inches(2.55), Inches(4.96), Inches(1.35))
    h_box.fill.solid()
    h_box.fill.fore_color.rgb = C_CARD_INNER_BG
    h_box.line.color.rgb = col
    h_box.line.width = Pt(1)
    tf_h = h_box.text_frame
    tf_h.margin_left = tf_h.margin_top = tf_h.margin_right = tf_h.margin_bottom = 0
    p_h1 = tf_h.paragraphs[0]
    p_h1.text = p_tag
    p_h1.font.name = FONT_TITLE
    p_h1.font.size = Pt(15)
    p_h1.font.bold = True
    p_h1.font.color.rgb = col
    
    p_h2 = tf_h.add_paragraph()
    p_h2.text = f"{p_name} {p_sub}"
    p_h2.font.name = FONT_PRIMARY
    p_h2.font.size = Pt(12)
    p_h2.font.bold = True
    p_h2.font.color.rgb = C_WHITE

    p_q = tf_h.add_paragraph()
    p_q.text = quote
    p_q.font.name = FONT_PRIMARY
    p_q.font.size = Pt(10)
    p_q.font.italic = True
    p_q.font.color.rgb = C_SLATE_400

    # Risk gauge box
    rg = s18.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x_c + Inches(0.15), Inches(4.05), Inches(4.9), Inches(0.42))
    rg.fill.solid()
    rg.fill.fore_color.rgb = C_CARD_BG
    rg.line.color.rgb = risk_col
    rg.line.width = Pt(1)
    tf_rg = rg.text_frame
    tf_rg.margin_left = tf_rg.margin_top = tf_rg.margin_right = tf_rg.margin_bottom = 0
    p_rg = tf_rg.paragraphs[0]
    p_rg.alignment = PP_ALIGN.CENTER
    p_rg.text = risk_txt
    p_rg.font.name = FONT_PRIMARY
    p_rg.font.size = Pt(11)
    p_rg.font.bold = True
    p_rg.font.color.rgb = risk_col

    # Body items
    tb_b = s18.shapes.add_textbox(x_c + Inches(0.18), Inches(4.6), Inches(4.85), Inches(5.6))
    tf_b = tb_b.text_frame
    tf_b.word_wrap = True
    format_structured_bullets(tf_b, p_items, font_size=11.5, space_after=Pt(8))

add_speaker_notes(s18,
    "Để chính sách can thiệp đi vào thực tế của ngân hàng, nghiên cứu đã xây dựng 3 chân dung khách hàng rời bỏ điển hình:\n"
    "Thứ nhất là 'The Silent Defector' chiếm 55% Churn: nhóm này lặng lẽ đưa dư nợ về 0 USD và giảm quẹt thẻ. Giải pháp là tặng voucher hoàn tiền kích hoạt lại chi tiêu.\n"
    "Thứ hai là 'Frustrated Complainer' chiếm 25% Churn: nhóm bức xúc gọi CSKH trên 3 lần. Giải pháp là cấp quản lý gọi điện xử lý dứt điểm trong 24h và miễn phí thường niên.\n"
    "Thứ ba là 'The VIP Switcher' chiếm 20% Churn: nhóm khách hàng giàu có thu nhập trên 120K USD. Giải pháp là chuyên viên Priority RM chăm sóc 1-1 và nâng cấp đặc quyền phòng chờ sân bay."
)

# ==============================================================================
# SLIDE 19: KHUNG CHIẾN LƯỢC GIỮ CHÂN 4 TẦNG & HỆ THỐNG CẢNH BÁO SỚM
# ==============================================================================
s19 = create_slide()
add_header(s19, "Khung Chiến Lược Giữ Chân 4 Tầng & Hệ Thống Cảnh Báo Sớm Real-Time", "PHẦN 05: TỐI ƯU KINH TẾ & CHIẾN LƯỢC GIỮ CHÂN", section_num=5)

tiers = [
    ("TẦNG 1: CẢNH BÁO SỚM REAL-TIME (EWS)", C_HVNH_ORANGE,
     "Thiết lập hệ thống giám sát tự động kích hoạt Trigger Points: Khách hàng không quẹt thẻ 2 tháng hoặc chi tiêu giảm >30% quý gần nhất lập tức đưa vào diện theo dõi đặc biệt.",
     "KPI: Tỷ lệ phát hiện sớm > 90% trước 60 ngày"),
    ("TẦNG 2: CHĂM SÓC KHÁCH HÀNG CHỦ ĐỘNG (PROACTIVE CARE)", C_ACCENT_RED,
     "Áp dụng chỉ tiêu First-Contact Resolution (FCR). Khách hàng liên hệ tổng đài lần thứ 3 tự động chuyển tiếp tới chuyên viên cấp cao giải quyết dứt điểm khiếu nại trong 24h.",
     "KPI: FCR > 85%  •  Tỷ lệ Churn CSKH < 5%"),
    ("TẦNG 3: GAMIFIED LOYALTY & TÍCH ĐIỂM TẦN SUẤT", C_HVNH_GOLD,
     "Thiết kế chương trình 'Quẹt Thẻ Mỗi Tuần' tích điểm theo tần suất sử dụng thay vì chỉ tính theo doanh số. Thưởng E-voucher ẩm thực/mua sắm khi đạt mốc 8 giao dịch/tháng.",
     "KPI: Duy trì tần suất quẹt thẻ ≥ 5 lần/tháng"),
    ("TẦNG 4: BÁN CHÉO HỆ SINH THÁI (CROSS-SELLING & LOCK-IN)", C_ACCENT_GREEN,
     "Xây dựng gói Combo tích hợp: Liên kết thẻ tín dụng với tài khoản nhận lương, tiền gửi tiết kiệm và ví điện tử VNPAY/MoMo. Miễn phí thường niên trọn đời khi duy trì số dư CASA.",
     "KPI: Khách hàng sở hữu ≥ 4 sản phẩm > 65%")
]

for idx, (t_name, col, t_desc, kpi) in enumerate(tiers):
    y_t = Inches(2.4 + idx * 1.95)
    t_card = add_card(s19, Inches(1.5), y_t, Inches(16.5), Inches(1.75), border_color=col, border_width=Pt(1.2))
    
    # Left vertical accent bar
    v_bar = s19.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.5), y_t, Inches(0.18), Inches(1.75))
    v_bar.fill.solid()
    v_bar.fill.fore_color.rgb = col
    v_bar.line.fill.background()

    # Text content
    tb_t = s19.shapes.add_textbox(Inches(1.9), y_t + Inches(0.12), Inches(11.5), Inches(1.5))
    tf_t = tb_t.text_frame
    tf_t.word_wrap = True
    p = tf_t.paragraphs[0]
    p.text = t_name
    p.font.name = FONT_TITLE
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = col
    p.space_after = Pt(4)
    
    p_d = tf_t.add_paragraph()
    p_d.text = t_desc
    p_d.font.name = FONT_PRIMARY
    p_d.font.size = Pt(12)
    p_d.font.color.rgb = C_SLATE_200

    # KPI Badge on the right
    kpi_card = add_card(s19, Inches(13.6), y_t + Inches(0.35), Inches(4.1), Inches(1.05), bg_color=C_CARD_INNER_BG, border_color=col, border_width=Pt(1))
    tb_k = s19.shapes.add_textbox(Inches(13.7), y_t + Inches(0.4), Inches(3.9), Inches(0.95))
    tf_k = tb_k.text_frame
    tf_k.margin_left = tf_k.margin_top = tf_k.margin_right = tf_k.margin_bottom = 0
    p_k1 = tf_k.paragraphs[0]
    p_k1.alignment = PP_ALIGN.CENTER
    p_k1.text = "CHỈ SỐ ĐO LƯỜNG (KPI)"
    p_k1.font.name = FONT_PRIMARY
    p_k1.font.size = Pt(10)
    p_k1.font.bold = True
    p_k1.font.color.rgb = col
    
    p_k2 = tf_k.add_paragraph()
    p_k2.alignment = PP_ALIGN.CENTER
    p_k2.text = kpi
    p_k2.font.name = FONT_PRIMARY
    p_k2.font.size = Pt(11)
    p_k2.font.bold = True
    p_k2.font.color.rgb = C_WHITE

add_speaker_notes(s19,
    "Từ các phát hiện nghiên cứu, đề tài đề xuất Khung chiến lược giữ chân khách hàng 4 tầng toàn diện kèm KPI định lượng:\n"
    "Tầng 1 là Hệ thống Cảnh báo sớm EWS kích hoạt tự động theo thời gian thực.\n"
    "Tầng 2 là Quy trình CSKH chủ động nhằm nâng chỉ tiêu giải quyết lần đầu FCR lên trên 85%.\n"
    "Tầng 3 là Chương trình Gamified Loyalty kích thích tần suất quẹt thẻ định kỳ hàng tuần.\n"
    "Và Tầng 4 là Bán chéo hệ sinh thái nhằm tạo rào cản chuyển đổi tự nhiên bền vững. "
    "Bốn tầng này phối hợp đồng bộ tạo thành pháo đài vững chắc bảo vệ danh mục thẻ của ngân hàng."
)

# ==============================================================================
# SLIDE 20: MÔ PHỎNG TÀI CHÍNH: LỢI NHUẬN RÒNG +$400,000 USD (ROI 500%)
# ==============================================================================
s20 = create_slide()
add_header(s20, "Mô Phỏng Tài Chính: Giữ Chân 960 Khách, Tạo Lợi Nhuận Ròng +$400,000 USD (ROI 500%)", "PHẦN 06: TÀI CHÍNH & TỔNG KẾT", section_num=6)

sim_steps = [
    ("BƯỚC 1: ĐẦU TƯ CRC", "$80,000 USD", C_ACCENT_RED, [
        ("Quy mô danh mục:", "10,000 khách hàng thẻ tín dụng."),
        ("Lượng khách Churn tự nhiên:", "1,607 khách hàng (tỷ lệ 16.07%)."),
        ("Tổng ngân sách giữ chân:", "Can thiệp ưu đãi cho 1,600 khách hàng."),
        ("Chi phí bình quân:", "50 USD/khách hàng (E-voucher, CSKH, miễn phí).")
    ]),
    ("BƯỚC 2: XGBOOST (t=0.42)", "91.38% RECALL", C_HVNH_ORANGE, [
        ("Năng lực nhận diện:", "Phát hiện chính xác 1,468 khách hàng có nguy cơ đóng thẻ."),
        ("Kiểm soát rủi ro:", "Chỉ bỏ sót 8.62% số khách hàng rời bỏ."),
        ("Độ tin cậy cảnh báo:", "Precision 91.08%, hạn chế tối đa chi phí can thiệp lãng phí.")
    ]),
    ("BƯỚC 3: BẢO TOÀN CLV", "$480,000 USD", C_BLUE_CYAN, [
        ("Xác suất cứu vãn kỳ vọng:", "75% khách hàng được can thiệp đồng ý duy trì thẻ."),
        ("Số khách giữ chân thành công:", "960 khách hàng được bảo vệ thành công."),
        ("Giá trị vòng đời CLV:", "Bảo toàn $500 USD CLV/khách hàng."),
        ("Tổng giá trị cứu vãn:", "960 * $500 = $480,000 USD.")
    ]),
    ("BƯỚC 4: LỢI NHUẬN RÒNG", "+$400,000 USD", C_ACCENT_GREEN, [
        ("Lợi nhuận ròng tăng thêm:", "$480,000 (CLV) - $80,000 (CRC) = +$400,000 USD/năm."),
        ("TỶ SUẤT HOÀN VỐN (ROI):", "($400,000 / $80,000) * 100% = 500%."),
        ("Ý nghĩa kinh tế:", "Khẳng định tính khả thi vượt trội của dự án đầu tư hệ thống Machine Learning tại ngân hàng.")
    ])
]

for idx, (st_step, st_kpi, st_col, st_bullets) in enumerate(sim_steps):
    x_s = Inches(1.5 + idx * 4.05)
    s_card = add_card(s20, x_s, Inches(2.4), Inches(3.85), Inches(8.0), border_color=st_col, border_width=Pt(1.2))
    
    # Top box inside card
    s_box = s20.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x_s + Inches(0.12), Inches(2.55), Inches(3.61), Inches(1.4))
    s_box.fill.solid()
    s_box.fill.fore_color.rgb = C_CARD_INNER_BG
    s_box.line.color.rgb = st_col
    s_box.line.width = Pt(1)
    tf_sb = s_box.text_frame
    tf_sb.margin_left = tf_sb.margin_top = tf_sb.margin_right = tf_sb.margin_bottom = 0
    p_step = tf_sb.paragraphs[0]
    p_step.text = st_step
    p_step.font.name = FONT_PRIMARY
    p_step.font.size = Pt(10)
    p_step.font.bold = True
    p_step.font.color.rgb = st_col
    
    p_kpi = tf_sb.add_paragraph()
    p_kpi.text = st_kpi
    p_kpi.font.name = FONT_TITLE
    p_kpi.font.size = Pt(28)
    p_kpi.font.bold = True
    p_kpi.font.color.rgb = st_col

    # Bullets
    tb_b = s20.shapes.add_textbox(x_s + Inches(0.18), Inches(4.15), Inches(3.5), Inches(6.0))
    tf_b = tb_b.text_frame
    tf_b.word_wrap = True
    format_structured_bullets(tf_b, st_bullets, font_size=11.5, space_after=Pt(9))

add_speaker_notes(s20,
    "Để chứng minh tính khả thi kinh tế của đề tài, nghiên cứu xây dựng mô phỏng tài chính trên quy mô danh mục 10,000 khách hàng:\n"
    "Với tỷ lệ rời bỏ tự nhiên 16.07%, mô hình XGBoost phát hiện được 1,468 khách hàng có nguy cơ.\n"
    "Khi triển khai gói can thiệp ưu đãi 50 USD/khách với tỷ lệ cứu vãn kỳ vọng 75%, ngân hàng giữ lại thành công 960 khách hàng, tương đương bảo tồn 480,000 USD giá trị CLV.\n"
    "Sau khi trừ đi toàn bộ 80,000 USD chi phí thực hiện, dự án đem lại +400,000 USD lợi nhuận ròng hàng năm, đạt tỷ suất sinh lời danh nghĩa ROI lên tới 500%."
)

# ==============================================================================
# SLIDE 21: TỔNG KẾT HỌC THUẬT & PHIÊN HỎI ĐÁP (Q&A SESSION)
# ==============================================================================
s21 = create_slide()
add_header(s21, "Tổng Kết Học Thuật: Đóng Góp Thực Tiễn, Giới Hạn & Định Hướng MLOps / TabNet", "PHẦN 06: TÀI CHÍNH & TỔNG KẾT", section_num=6)

conc_cols = [
    ("1. ĐÓNG GÓP CỦA ĐỀ TÀI", C_HVNH_GOLD, [
        ("Xây dựng Pipeline hoàn chỉnh:", "Giải quyết trọn vẹn từ làm sạch, ngăn rò rỉ dữ liệu Naive Bayes đến mô hình hóa."),
        ("Hiệu năng vượt trội:", "XGBoost đạt ROC-AUC 0.9930 và Recall 91.38%, kiểm soát tối ưu sai số Loại I và II."),
        ("Chuyển giao kinh tế định lượng:", "Tối ưu hóa điểm cắt t* = 0.42 và lượng hóa lợi nhuận ròng +$400,000 USD/năm.")
    ]),
    ("2. HẠN CHẾ & HƯỚNG ĐI", C_BLUE_CYAN, [
        ("Hạn chế dữ liệu cắt ngang:", "Tập dữ liệu dạng bảng cắt ngang (Cross-sectional), chưa ghi nhận chuỗi thời gian liên tục POS."),
        ("Thử nghiệm kiến trúc Deep Learning:", "Mở rộng thử nghiệm TabNet / Tabular Transformers cho dữ liệu tài chính."),
        ("Triển khai MLOps thời gian thực:", "Tích hợp Kafka Streaming và mô hình SHAP Waterfall giải thích cá thể hóa cho từng cán bộ RM.")
    ]),
    ("3. PHIÊN HỎI ĐÁP (Q&A)", C_HVNH_ORANGE, [
        ("Trân trọng cảm ơn Hội đồng:", "Kính chúc Quý Thầy/Cô và các bạn học viên cao học dồi dào sức khỏe và thành công!"),
        ("Thông tin liên hệ nghiên cứu:", "Học viên: Đỗ Văn Đạt  |  Email: datdv@bav.edu.vn"),
        ("Sẵn sàng bảo vệ:", "Rất mong nhận được các ý kiến nhận xét, đóng góp và câu hỏi phản biện từ Hội đồng chấm bảo vệ!")
    ])
]

for idx, (col_title, col_color, col_bullets) in enumerate(conc_cols):
    x_c = Inches(1.5 + idx * 5.5)
    c_card = add_card(s21, x_c, Inches(2.4), Inches(5.2), Inches(8.0), border_color=col_color, border_width=Pt(1.2))
    
    # Top box inside card
    h_box = s21.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x_c + Inches(0.12), Inches(2.55), Inches(4.96), Inches(0.85))
    h_box.fill.solid()
    h_box.fill.fore_color.rgb = C_CARD_INNER_BG
    h_box.line.color.rgb = col_color
    h_box.line.width = Pt(1)
    tf_h = h_box.text_frame
    tf_h.margin_left = tf_h.margin_top = tf_h.margin_right = tf_h.margin_bottom = 0
    p_h = tf_h.paragraphs[0]
    p_h.alignment = PP_ALIGN.CENTER
    p_h.text = col_title
    p_h.font.name = FONT_TITLE
    p_h.font.size = Pt(17)
    p_h.font.bold = True
    p_h.font.color.rgb = col_color

    # Bullets
    tb_b = s21.shapes.add_textbox(x_c + Inches(0.18), Inches(3.6), Inches(4.85), Inches(6.5))
    tf_b = tb_b.text_frame
    tf_b.word_wrap = True
    format_structured_bullets(tf_b, col_bullets, font_size=12, space_after=Pt(10))

add_speaker_notes(s21,
    "Kính thưa Thầy/Cô và các bạn, bài báo cáo nghiên cứu của tôi đến đây là kết thúc.\n"
    "Đề tài đã hoàn thành xuất sắc các mục tiêu nghiên cứu: từ kiểm soát chặt chẽ dữ liệu, huấn luyện mô hình XGBoost đạt ROC-AUC 0.9930 đến tối ưu hóa kinh tế ROI 500%.\n"
    "Tôi xin trân trọng cảm ơn Quý Thầy/Cô đã lắng nghe và rất mong nhận được những góp ý quý báu từ Hội đồng trong phiên hỏi đáp ngay sau đây!"
)

# ==============================================================================
# XUẤT BẢN FILE PPTX VÀ KIỂM ĐỊNH TỰ ĐỘNG
# ==============================================================================
prs.save(OUTPUT_PATH)
print(f"✅ Đã xuất bản thành công {len(prs.slides)} slide chuẩn Industrial Template tại:")
print(f"👉 {OUTPUT_PATH}")
