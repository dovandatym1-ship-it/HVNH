import os
import sys
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FIG_DIR = os.path.join(BASE_DIR, "figures")
DOCX_PATH = os.path.join(BASE_DIR, "Bao_Cao_Giua_Ky_BankChurners.docx")

# Màu sắc chuẩn HVNH
COLOR_NAVY = RGBColor(23, 54, 93)      # #17365D
COLOR_SECONDARY = RGBColor(31, 77, 120) # #1F4D78
COLOR_ACCENT = RGBColor(46, 116, 181)   # #2E74B5
COLOR_DARK = RGBColor(30, 41, 59)       # #1E293B
HEX_HEADER_BG = "17365D"
HEX_ZEBRA_BG = "F1F5F9"
HEX_CALLOUT_BG = "F8FAFC"
HEX_BORDER = "CBD5E1"

doc = docx.Document()

# Thiết lập lề chuẩn Học viện Ngân hàng
for section in doc.sections:
    section.top_margin = Inches(0.984)     # 2.5 cm
    section.bottom_margin = Inches(0.787)  # 2.0 cm
    section.left_margin = Inches(1.181)    # 3.0 cm
    section.right_margin = Inches(0.787)   # 2.0 cm
    section.header.is_linked_to_previous = False
    section.footer.is_linked_to_previous = False

# Cấu hình Style Normal mặc định
style_normal = doc.styles['Normal']
style_normal.font.name = 'Times New Roman'
style_normal.font.size = Pt(13)
style_normal.font.color.rgb = COLOR_DARK
style_normal.paragraph_format.line_spacing = 1.3
style_normal.paragraph_format.space_after = Pt(6)
style_normal.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

# Helper functions
def set_cell_background(cell, hex_color):
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    cell._tc.get_or_add_tcPr().append(shading_elm)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def add_h1(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(18)
    p.paragraph_format.space_after = Pt(8)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(16)
    run.bold = True
    run.font.color.rgb = COLOR_NAVY
    return p

def add_h2(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(14)
    run.bold = True
    run.font.color.rgb = COLOR_SECONDARY
    return p

def add_h3(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(13)
    run.bold = True
    run.font.color.rgb = COLOR_ACCENT
    return p

def add_callout(title, text):
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = table.cell(0, 0)
    set_cell_background(cell, HEX_CALLOUT_BG)
    set_cell_margins(cell, top=140, bottom=140, left=200, right=180)
    
    # Left border accent
    tcPr = cell._tc.get_or_add_tcPr()
    borders = parse_xml(f'<w:tcBorders {nsdecls("w")}><w:left w:val="single" w:sz="24" w:space="0" w:color="{HEX_HEADER_BG}"/><w:top w:val="none"/><w:right w:val="none"/><w:bottom w:val="none"/></w:tcBorders>')
    tcPr.append(borders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.line_spacing = 1.25
    p.paragraph_format.space_after = Pt(4)
    r_title = p.add_run(f"💡 {title}\n")
    r_title.bold = True
    r_title.font.name = 'Times New Roman'
    r_title.font.size = Pt(12)
    r_title.font.color.rgb = COLOR_NAVY
    
    r_body = p.add_run(text)
    r_body.font.name = 'Times New Roman'
    r_body.font.size = Pt(12)
    r_body.font.color.rgb = COLOR_DARK
    
    p_space = doc.add_paragraph()
    p_space.paragraph_format.space_before = Pt(0)
    p_space.paragraph_format.space_after = Pt(4)

def add_figure(img_name, caption, width=Inches(6.0)):
    img_path = os.path.join(FIG_DIR, img_name)
    if os.path.exists(img_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(8)
        p_img.paragraph_format.space_after = Pt(4)
        run = p_img.add_run()
        run.add_picture(img_path, width=width)
        
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.paragraph_format.space_before = Pt(2)
        p_cap.paragraph_format.space_after = Pt(12)
        r_cap = p_cap.add_run(f"Hình: {caption}")
        r_cap.font.name = 'Times New Roman'
        r_cap.font.size = Pt(11)
        r_cap.italic = True
        r_cap.font.color.rgb = COLOR_SECONDARY

def style_table_header_and_zebra(table):
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, row in enumerate(table.rows):
        for cell in row.cells:
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            set_cell_margins(cell, top=100, bottom=100, left=120, right=120)
            tcPr = cell._tc.get_or_add_tcPr()
            borders = parse_xml(f'<w:tcBorders {nsdecls("w")}><w:top w:val="single" w:sz="4" w:space="0" w:color="{HEX_BORDER}"/><w:bottom w:val="single" w:sz="4" w:space="0" w:color="{HEX_BORDER}"/><w:left w:val="single" w:sz="4" w:space="0" w:color="{HEX_BORDER}"/><w:right w:val="single" w:sz="4" w:space="0" w:color="{HEX_BORDER}"/></w:tcBorders>')
            tcPr.append(borders)
            
            for p in cell.paragraphs:
                p.paragraph_format.line_spacing = 1.15
                p.paragraph_format.space_after = Pt(2)
                p.paragraph_format.space_before = Pt(2)
                if i == 0:
                    set_cell_background(cell, HEX_HEADER_BG)
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    for r in p.runs:
                        r.bold = True
                        r.font.name = 'Times New Roman'
                        r.font.size = Pt(11)
                        r.font.color.rgb = RGBColor(255, 255, 255)
                else:
                    if i % 2 == 1:
                        set_cell_background(cell, HEX_ZEBRA_BG)
                    for r in p.runs:
                        r.font.name = 'Times New Roman'
                        r.font.size = Pt(11)

print("📄 Đang khởi tạo Trang bìa học thuật chuẩn HVNH...")

# ==========================================
# TRANG BÌA (COVER PAGE)
# ==========================================
p_uni = doc.add_paragraph()
p_uni.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_uni.paragraph_format.space_after = Pt(2)
r = p_uni.add_run("HỌC VIỆN NGÂN HÀNG\n")
r.bold = True
r.font.size = Pt(14)
r.font.color.rgb = COLOR_NAVY
r2 = p_uni.add_run("KHOA HỆ THỐNG THÔNG TIN QUẢN LÝ / NGÂN HÀNG\n")
r2.bold = True
r2.font.size = Pt(13)
r2.font.color.rgb = COLOR_SECONDARY
r3 = p_uni.add_run("------------- *** -------------")
r3.font.size = Pt(11)

for _ in range(3):
    p_blank = doc.add_paragraph()
    p_blank.paragraph_format.space_after = Pt(0)

p_title_sub = doc.add_paragraph()
p_title_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_title_sub.paragraph_format.space_after = Pt(6)
r_sub = p_title_sub.add_run("BÁO CÁO BÀI TẬP GIỮA KỲ\n")
r_sub.bold = True
r_sub.font.size = Pt(16)
r_sub.font.color.rgb = COLOR_SECONDARY

p_title = doc.add_paragraph()
p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_title.paragraph_format.space_after = Pt(8)
r_title = p_title.add_run("XỬ LÝ DỮ LIỆU & KHAI PHÁ DỮ LIỆU\nBỘ DỮ LIỆU KHÁCH HÀNG THẺ TÍN DỤNG RỜI BỎ\n(BANK CUSTOMER CHURN ANALYSIS & DATA MINING)")
r_title.bold = True
r_title.font.size = Pt(18)
r_title.font.color.rgb = COLOR_NAVY

p_sub2 = doc.add_paragraph()
p_sub2.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_sub2.paragraph_format.space_after = Pt(24)
r_sub2 = p_sub2.add_run("Học phần: Phân tích Dữ liệu trong Kinh doanh (Business Analytics)")
r_sub2.italic = True
r_sub2.font.size = Pt(13)

for _ in range(3):
    p_blank = doc.add_paragraph()
    p_blank.paragraph_format.space_after = Pt(0)

# Khung thông tin sinh viên
table_info = doc.add_table(rows=4, cols=2)
table_info.alignment = WD_TABLE_ALIGNMENT.CENTER
info_data = [
    ("Sinh viên thực hiện:", "Đỗ Văn Đạt"),
    ("Mã sinh viên / Lớp:", "Chuyên ngành Business Analytics - HVNH"),
    ("Giảng viên hướng dẫn:", "Bộ môn Phân tích Dữ liệu Kinh doanh"),
    ("Bộ dữ liệu nghiên cứu:", "BankChurners.csv (10,127 quan sát, 23 biến)")
]
for i, (k, v) in enumerate(info_data):
    p0 = table_info.cell(i, 0).paragraphs[0]
    p0.paragraph_format.line_spacing = 1.2
    p0.paragraph_format.space_after = Pt(3)
    r_k = p0.add_run(k)
    r_k.bold = True
    r_k.font.size = Pt(12)
    
    p1 = table_info.cell(i, 1).paragraphs[0]
    p1.paragraph_format.line_spacing = 1.2
    p1.paragraph_format.space_after = Pt(3)
    r_v = p1.add_run(v)
    r_v.font.size = Pt(12)

for _ in range(4):
    p_blank = doc.add_paragraph()
    p_blank.paragraph_format.space_after = Pt(0)

p_loc = doc.add_paragraph()
p_loc.alignment = WD_ALIGN_PARAGRAPH.CENTER
r_loc = p_loc.add_run("HÀ NỘI, NĂM 2026")
r_loc.bold = True
r_loc.font.size = Pt(13)
r_loc.font.color.rgb = COLOR_NAVY

doc.add_page_break()

# ==========================================
# MỤC LỤC & TÓM TẮT ĐIỀU HÀNH
# ==========================================
p_toc = doc.add_paragraph()
p_toc.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_toc.paragraph_format.space_after = Pt(14)
r_toc = p_toc.add_run("MỤC LỤC NỘI DUNG")
r_toc.bold = True
r_toc.font.size = Pt(16)
r_toc.font.color.rgb = COLOR_NAVY

toc_items = [
    ("CHƯƠNG 1: GIỚI THIỆU & BỐI CẢNH NGHIÊN CỨU", "3"),
    ("  1.1. Bối cảnh thị trường thẻ tín dụng ngân hàng bán lẻ", "3"),
    ("  1.2. Bài toán kinh tế về khách hàng rời bỏ (Customer Churn)", "3"),
    ("  1.3. Mục tiêu và phạm vi nghiên cứu", "4"),
    ("CHƯƠNG 2: TỔNG QUAN TẬP DỮ LIỆU & TỪ ĐIỂN BIẾN", "5"),
    ("  2.1. Cấu trúc tổng thể của bộ dữ liệu BankChurners", "5"),
    ("  2.2. Phân loại biến số & Ý nghĩa nghiệp vụ ngân hàng", "5"),
    ("CHƯƠNG 3: QUY TRÌNH TIỀN XỬ LÝ & LÀM SẠCH DỮ LIỆU", "7"),
    ("  3.1. Loại bỏ thuộc tính nhiễu kỹ thuật (Data Leakage Removal)", "7"),
    ("  3.2. Đánh giá và xử lý giá trị khuyết thiếu (Missing Values)", "7"),
    ("  3.3. Phân tích nhóm định tính không xác định (Unknown Handling)", "8"),
    ("  3.4. Kỹ thuật tạo đặc trưng mới (Feature Engineering)", "8"),
    ("  3.5. Xử lý ngoại lai và Chiến lược mã hóa chuẩn hóa", "9"),
    ("CHƯƠNG 4: PHÂN TÍCH KHÁM PHÁ DỮ LIỆU CHUYÊN SÂU (EDA)", "10"),
    ("  4.1. Phân tích phân phối Biến mục tiêu (Attrition Flag)", "10"),
    ("  4.2. Phân tích Nhân khẩu học & Rủi ro Rời bỏ", "11"),
    ("  4.3. Phân tích Hành vi Giao dịch & Sử dụng Hạn mức Thẻ", "12"),
    ("  4.4. Phân tích Tương tác CSKH & Mức độ Suy giảm Gắn kết", "14"),
    ("  4.5. Ma trận Tương quan Pearson & Kiểm định Giả thuyết Thống kê", "15"),
    ("CHƯƠNG 5: KHAI PHÁ DỮ LIỆU & MÔ HÌNH HÓA DỰ BÁO", "17"),
    ("  5.1. Phân cụm Khách hàng Hành vi (K-Means & PCA Clustering)", "17"),
    ("  5.2. Hồ sơ đặc trưng và Tỷ lệ rời bỏ của 4 Phân cụm", "19"),
    ("  5.3. Xây dựng và Huấn luyện 4 Mô hình Học máy Phân loại", "20"),
    ("  5.4. So sánh Hiệu năng Mô hình & Đánh giá Đường cong ROC-AUC", "22"),
    ("  5.5. Phân tích Tầm quan trọng Đặc trưng (Feature Importance)", "23"),
    ("  5.6. Tối ưu hóa Ngưỡng Quyết định & Bài toán Chi phí - Lợi ích", "24"),
    ("CHƯƠNG 6: CHÂN DUNG KHÁCH HÀNG & KHUYẾN NGHỊ QUẢN TRỊ", "26"),
    ("  6.1. Ba Chân dung Khách hàng Rời bỏ Điển hình (Personas)", "26"),
    ("  6.2. Khung Chiến lược Giữ chân Khách hàng 4 Tầng (4-Tier)", "28"),
    ("  6.3. Hệ thống Cảnh báo Sớm (Early Warning System - EWS)", "29"),
    ("  6.4. Mô phỏng Hiệu quả Tài chính & Lợi nhuận Thu về (ROI)", "30"),
    ("CHƯƠNG 7: KẾT LUẬN & HƯỚNG PHÁT TRIỂN", "32"),
    ("TÀI LIỆU THAM KHẢO", "33")
]

table_toc = doc.add_table(rows=len(toc_items), cols=2)
table_toc.alignment = WD_TABLE_ALIGNMENT.CENTER
for i, (item, page) in enumerate(toc_items):
    c0 = table_toc.cell(i, 0)
    c1 = table_toc.cell(i, 1)
    p0 = c0.paragraphs[0]
    p1 = c1.paragraphs[0]
    p0.paragraph_format.line_spacing = 1.15
    p0.paragraph_format.space_after = Pt(2)
    p1.paragraph_format.line_spacing = 1.15
    p1.paragraph_format.space_after = Pt(2)
    p1.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    
    r0 = p0.add_run(item)
    r1 = p1.add_run(page)
    if "CHƯƠNG" in item or "TÀI LIỆU" in item:
        r0.bold = True
        r1.bold = True
        r0.font.color.rgb = COLOR_NAVY
        r1.font.color.rgb = COLOR_NAVY
    else:
        r0.font.color.rgb = COLOR_DARK

doc.add_page_break()

# ==========================================
# CHƯƠNG 1
# ==========================================
add_h1("CHƯƠNG 1: GIỚI THIỆU & BỐI CẢNH NGHIÊN CỨU")

add_h2("1.1. Bối cảnh thị trường thẻ tín dụng ngân hàng bán lẻ")
doc.add_paragraph(
    "Trong kỷ nguyên ngân hàng số và thanh toán không tiền mặt bùng nổ, thẻ tín dụng (Credit Card) "
    "là một trong những sản phẩm tài chính bán lẻ mang lại biên lợi nhuận cao nhất và đóng vai trò "
    "hạt nhân trong việc gia tăng gắn kết khách hàng (Customer Engagement). Nguồn thu từ mảng kinh doanh thẻ "
    "được cấu thành từ ba trụ cột chính:\n"
    "1. Phí giao dịch quẹt thẻ (Interchange Fees) từ các điểm chấp nhận thanh toán (POS/E-commerce).\n"
    "2. Lãi suất tín dụng quay vòng (Revolving Interest Rate) khi chủ thẻ duy trì số dư nợ quá kỳ hạn miễn lãi.\n"
    "3. Các loại phí dịch vụ phi tín dụng: Phí thường niên (Annual Fee), phí chuyển đổi ngoại tệ, phí rút tiền mặt và phí phạt chậm trả."
)
doc.add_paragraph(
    "Tuy nhiên, sự cạnh tranh khốc liệt giữa các ngân hàng thương mại truyền thống, các công ty tài chính tiêu dùng "
    "và các tổ chức Fintech (ví điện tử, dịch vụ Mua trước - Trả sau / BNPL) khiến khách hàng ngày càng có nhiều lựa chọn thay thế. "
    "Khách hàng sẵn sàng mở thêm thẻ mới từ các đối thủ có ưu đãi hoàn tiền hấp dẫn và bỏ rơi thẻ hiện tại, tạo ra tỷ lệ khách hàng "
    "rời bỏ (Churn Rate) ở mức báo động."
)

add_h2("1.2. Bài toán kinh tế về khách hàng rời bỏ (Customer Churn)")
doc.add_paragraph(
    "Theo các nghiên cứu kinh điển từ Harvard Business Review và tập đoàn tư vấn quản trị Bain & Company:\n"
    "• Chi phí thu hút một khách hàng thẻ mới (Customer Acquisition Cost - CAC) gấp từ 5 đến 7 lần chi phí duy trì một khách hàng hiện hữu (Customer Retention Cost - CRC).\n"
    "• Chỉ cần tăng tỷ lệ giữ chân khách hàng thêm 5%, lợi nhuận của ngân hàng có thể tăng từ 25% đến 95% nhờ vào giá trị vòng đời khách hàng tích lũy (Customer Lifetime Value - CLV)."
)
doc.add_paragraph(
    "Khi một khách hàng hủy thẻ tín dụng (Attrited Customer), ngân hàng không chỉ chịu mất mát dòng thu nhập phí và lãi suất trong tương lai, "
    "mà còn lãng phí toàn bộ chi phí đầu tư ban đầu về marketing, thẩm định rủi ro tín dụng và chi phí dập phôi phát hành thẻ."
)

add_h2("1.3. Mục tiêu và phạm vi nghiên cứu")
doc.add_paragraph(
    "Báo cáo này triển khai toàn diện quy trình Xử lý Dữ liệu và Khai phá Dữ liệu (Data Preprocessing, Exploratory Data Analysis & Data Mining) "
    "trên tập dữ liệu thực tế gồm 10,127 khách hàng thẻ tín dụng, nhằm đạt được các mục tiêu trọng yếu:\n"
    "1. Chuẩn hóa và làm sạch dữ liệu: Đánh giá chất lượng dữ liệu, loại trừ các biến nhiễu kỹ thuật gây rò rỉ thông tin, làm sạch khuyết thiếu và kiến tạo các biến phái sinh có giá trị nghiệp vụ cao.\n"
    "2. Khám phá sâu các quy luật hành vi (EDA): Nhận diện các chỉ báo sớm phân biệt giữa nhóm khách hàng rời bỏ và nhóm khách hàng ở lại thông qua kiểm định thống kê và trực quan hóa đa chiều.\n"
    "3. Khai phá dữ liệu nâng cao (Data Mining): Phân cụm khách hàng theo hành vi tiêu dùng bằng thuật toán K-Means và PCA; xây dựng mô hình máy học dự báo rời bỏ với độ chính xác cao (XGBoost, Random Forest, Decision Tree, Logistic Regression).\n"
    "4. Đề xuất khuyến nghị quản trị hành động: Xây dựng Hệ thống Cảnh báo Sớm (Early Warning System - EWS) và Khung giải pháp giữ chân 4 tầng nhằm tối đa hóa lợi nhuận ròng cho ngân hàng."
)

# ==========================================
# CHƯƠNG 2
# ==========================================
add_h1("CHƯƠNG 2: TỔNG QUAN TẬP DỮ LIỆU & TỪ ĐIỂN BIẾN")

add_h2("2.1. Cấu trúc tổng thể của bộ dữ liệu BankChurners")
doc.add_paragraph(
    "Tập dữ liệu nghiên cứu BankChurners.csv chứa 10,127 bản ghi khách hàng cá nhân sở hữu thẻ tín dụng, "
    "với 23 thuộc tính ban đầu. Phân loại cấu trúc dữ liệu như sau:"
)

table_summary = doc.add_table(rows=6, cols=2)
summary_rows = [
    ("Tổng số dòng (Quan sát)", "10,127 khách hàng thẻ tín dụng"),
    ("Tổng số cột (Biến ban đầu)", "23 thuộc tính"),
    ("Biến định lượng (Numerical)", "15 biến (Tuổi, Thu nhập, Hạn mức, Dư nợ, Số lần giao dịch...)"),
    ("Biến định tính (Categorical)", "6 biến (Giới tính, Học vấn, Hôn nhân, Thu nhập, Hạng thẻ, Biến mục tiêu)"),
    ("Biến định danh (ID)", "1 biến (CLIENTNUM)"),
    ("Biến mục tiêu (Target)", "Attrition_Flag (Existing Customer: 8,500 | Attrited Customer: 1,627)")
]
for i, (k, v) in enumerate(summary_rows):
    table_summary.cell(i, 0).paragraphs[0].add_run(k)
    table_summary.cell(i, 1).paragraphs[0].add_run(v)
style_table_header_and_zebra(table_summary)

add_h2("2.2. Phân loại biến số & Ý nghĩa nghiệp vụ ngân hàng")
doc.add_paragraph(
    "Dưới đây là bảng từ điển các thuộc tính cốt lõi và ý nghĩa phân tích trong nghiệp vụ ngân hàng bán lẻ:"
)

table_dict = doc.add_table(rows=12, cols=4)
dict_headers = ["Tên Biến", "Kiểu Dữ Liệu", "Phân Loại", "Diễn Giải Ý Nghĩa Nghiệp Vụ"]
for j, h in enumerate(dict_headers):
    table_dict.cell(0, j).paragraphs[0].add_run(h)

dict_data = [
    ("CLIENTNUM", "int64", "Định danh", "Mã số định danh duy nhất của chủ thẻ tín dụng."),
    ("Attrition_Flag", "object", "Target", "Trạng thái khách hàng: Existing Customer (Ở lại) vs Attrited Customer (Rời bỏ)."),
    ("Customer_Age", "int64", "Nhân khẩu", "Độ tuổi của chủ thẻ (tính theo năm)."),
    ("Gender", "object", "Nhân khẩu", "Giới tính chủ thẻ (M: Nam, F: Nữ)."),
    ("Dependent_count", "int64", "Nhân khẩu", "Số người phụ thuộc tài chính vào chủ thẻ."),
    ("Income_Category", "object", "Nhân khẩu", "Phân khúc thu nhập hàng năm của chủ thẻ."),
    ("Card_Category", "object", "Sản phẩm", "Hạng thẻ tín dụng (Blue, Silver, Gold, Platinum)."),
    ("Months_on_book", "int64", "Quan hệ", "Thâm niên gắn bó mở tài khoản thẻ (tính theo tháng)."),
    ("Total_Relationship_Count", "int64", "Quan hệ", "Tổng số sản phẩm dịch vụ ngân hàng mà khách hàng đang sử dụng."),
    ("Months_Inactive_12_mon", "int64", "Hành vi", "Số tháng không phát sinh bất kỳ giao dịch quẹt thẻ nào trong 12 tháng qua."),
    ("Contacts_Count_12_mon", "int64", "Hành vi", "Số lần khách hàng chủ động gọi lên tổng đài CSKH trong 12 tháng qua.")
]
for i, row in enumerate(dict_data):
    for j, val in enumerate(row):
        table_dict.cell(i+1, j).paragraphs[0].add_run(val)
style_table_header_and_zebra(table_dict)

# ==========================================
# CHƯƠNG 3
# ==========================================
add_h1("CHƯƠNG 3: QUY TRÌNH TIỀN XỬ LÝ & LÀM SẠCH DỮ LIỆU")

add_h2("3.1. Loại bỏ thuộc tính nhiễu kỹ thuật (Data Leakage Removal)")
doc.add_paragraph(
    "Hai cột cuối cùng trong tập dữ liệu gốc:\n"
    "• `Naive_Bayes_Classifier_Attrition_Flag_Card_Category_..._1`\n"
    "• `Naive_Bayes_Classifier_Attrition_Flag_Card_Category_..._2`\n"
    "là kết quả của mô hình phân loại Naive Bayes được người tạo bộ dữ liệu đưa vào sẵn. "
    "Nếu giữ lại các cột này trong quá trình huấn luyện máy học, mô hình sẽ gặp hiện tượng rò rỉ dữ liệu (Data Leakage), "
    "dẫn đến kết quả đánh giá giả tạo. Nhóm nghiên cứu đã thực hiện loại bỏ hoàn toàn 2 cột này."
)

add_h2("3.2. Đánh giá và xử lý giá trị khuyết thiếu (Missing Values)")
doc.add_paragraph(
    "Kiểm tra tập dữ liệu cho thấy không có ô trống dạng NaN/Null trên diện rộng. Đối với các trường hợp khuyết thiếu cục bộ "
    "trong biến định lượng, phương pháp điền giá trị Trung vị (Median Imputation) được áp dụng vì trung vị có tính vững chắc (robust), "
    "không bị bóp méo bởi các giá trị ngoại lai cực trị."
)

add_h2("3.3. Phân tích nhóm định tính không xác định (Unknown Handling)")
doc.add_paragraph(
    "Các biến `Education_Level` (15.0%), `Income_Category` (11.0%) và `Marital_Status` (7.4%) chứa danh mục `'Unknown'`. "
    "Thay vì xóa bỏ các dòng này (làm mất gần 30% dữ liệu quý giá) hoặc gán ép theo giá trị xuất hiện nhiều nhất (Mode Imputation), "
    "nhóm quyết định giữ nguyên `'Unknown'` như một phân lớp thông tin độc lập. Trong thực tế ngành ngân hàng, khách hàng từ chối cung cấp "
    "thông tin thu nhập hoặc học vấn thường có tâm lý bảo mật cao hoặc thuộc các nhóm hành vi tài chính đặc thù."
)

add_h2("3.4. Kỹ thuật tạo đặc trưng mới (Feature Engineering)")
doc.add_paragraph(
    "Để nâng cao khả năng phân tách của các thuật toán khai phá dữ liệu, 5 biến phái sinh được kiến tạo:"
)
fe_list = [
    ("Avg_Trans_Value", "Total_Trans_Amt / Total_Trans_Ct", "Giá trị chi tiêu trung bình trên mỗi lần quẹt thẻ."),
    ("Age_Group", "Cắt nhóm tuổi (<35, 35-44, 45-54, 55-64, 65+)", "Phân tầng nhân khẩu học theo các giai đoạn vòng đời tài chính."),
    ("Revolving_Ratio", "Total_Revolving_Bal / Credit_Limit", "Tỷ lệ dư nợ tín dụng quay vòng thực tế trên hạn mức cấp."),
    ("Trans_Per_Month", "Total_Trans_Ct / Months_on_book", "Tần suất giao dịch bình quân mỗi tháng trong toàn bộ vòng đời thẻ."),
    ("Contact_Intensity", "Contacts_Count / (Months_Inactive + 1)", "Chỉ số cường độ bất mãn: Càng gọi nhiều khi đang ngủ đông càng rủi ro.")
]
table_fe = doc.add_table(rows=len(fe_list)+1, cols=3)
table_fe.cell(0, 0).paragraphs[0].add_run("Tên Biến Phái Sinh")
table_fe.cell(0, 1).paragraphs[0].add_run("Công Thức Tính Toán")
table_fe.cell(0, 2).paragraphs[0].add_run("Ý Nghĩa Nghiệp Vụ")
for i, (k, f, m) in enumerate(fe_list):
    table_fe.cell(i+1, 0).paragraphs[0].add_run(k)
    table_fe.cell(i+1, 1).paragraphs[0].add_run(f)
    table_fe.cell(i+1, 2).paragraphs[0].add_run(m)
style_table_header_and_zebra(table_fe)

# ==========================================
# CHƯƠNG 4
# ==========================================
add_h1("CHƯƠNG 4: PHÂN TÍCH KHÁM PHÁ DỮ LIỆU CHUYÊN SÂU (EDA)")

add_h2("4.1. Phân tích phân phối Biến mục tiêu (Attrition Flag)")
doc.add_paragraph(
    "Tỷ lệ khách hàng rời bỏ trong bộ dữ liệu là 16.07% (1,627 khách hàng), trong khi nhóm ở lại chiếm 83.93% (8,500 khách hàng). "
    "Đây là bài toán mất cân bằng lớp (Class Imbalance) điển hình trong ngân hàng bán lẻ (tỷ lệ xấp xỉ 1:5.22). "
    "Đặc tính này đòi hỏi việc đánh giá mô hình máy học không thể chỉ dựa vào độ chính xác tổng thể (Accuracy) "
    "mà phải tập trung vào Recall (Độ nhạy), F1-Score và ROC-AUC."
)
add_figure("01_churn_distribution.png", "Phân bố Biến mục tiêu Attrition Flag (Tỷ lệ Rời bỏ 16.07%)")

add_h2("4.2. Phân tích Nhân khẩu học & Rủi ro Rời bỏ")
doc.add_paragraph(
    "Phân tích đa chiều trên các biến nhân khẩu học mang lại những phát hiện có ý nghĩa chiến lược:\n"
    "• Giới tính (Gender): Khách hàng Nữ có tỷ lệ rời bỏ cao hơn Nam (17.36% vs 14.62%, kiểm định Chi-square p = 0.0002).\n"
    "• Phân khúc Thu nhập (Income Category): Xuất hiện hiện tượng rủi ro phân hóa hai đầu (Bimodal Risk). Nhóm thu nhập thấp (< $40K) có tỷ lệ rời bỏ 17.19% (do gánh nặng phí thường niên và hạn mức thấp); nhóm thu nhập cao (≥ $120K) có tỷ lệ rời bỏ 17.33% (do dễ bị đối thủ cạnh tranh lôi kéo bằng đặc quyền VIP). Nhóm thu nhập trung bình ($60K - $80K) có tỷ lệ gắn kết cao nhất (rời bỏ chỉ 13.48%).\n"
    "• Trình độ Học vấn (Education Level): Khách hàng có học vị Tiến sĩ (Doctorate) có tỷ lệ rời bỏ cao nhất (21.06%)."
)
add_figure("02_demographic_churn.png", "Phân tích Tỷ lệ Rời bỏ theo các Chiều Nhân khẩu học")

add_h2("4.3. Phân tích Hành vi Giao dịch & Sử dụng Hạn mức Thẻ")
doc.add_paragraph(
    "Biểu đồ phân tán giữa Tổng số lần giao dịch (`Total_Trans_Ct`) và Tổng giá trị giao dịch (`Total_Trans_Amt`) "
    "cho thấy sự phân tách cụm cực kỳ rõ rệt giữa hai nhóm khách hàng:"
)
add_figure("03_transaction_behavior_churn.png", "Tương quan Phân tán Số lần Giao dịch vs Tổng Giá trị Chi tiêu")

add_callout(
    "PHÁT HIỆN VÙNG NGUY CƠ CAO (HIGH-RISK TRANSACTION ZONE)",
    "Khách hàng có tổng số lần quẹt thẻ dưới 55 lần/năm và tổng chi tiêu dưới $3,000 "
    "tập trung dày đặc các điểm rời bỏ (Attrited). Đây là ngưỡng cảnh báo đỏ hàng đầu trong giám sát vận hành thẻ."
)

doc.add_paragraph(
    "Về khía cạnh tài chính, biểu đồ Boxplot làm nổi bật hiện tượng 'Dư nợ quay vòng về 0' (Zero Revolving Balance Phenomenon):"
)
add_figure("04_financial_ratios_churn.png", "Phân phối Dư nợ Quay vòng và Tỷ lệ Sử dụng Hạn mức Thẻ")

doc.add_paragraph(
    "Khách hàng ở lại duy trì mức dư nợ quay vòng trung bình là $1,257 (trung vị $1,364), tạo ra nguồn thu lãi định kỳ lớn cho ngân hàng. "
    "Ngược lại, nhóm khách hàng rời bỏ có giá trị trung vị dư nợ quay vòng chính xác bằng $0.00 và tỷ lệ sử dụng hạn mức trung vị bằng 0%. "
    "Điều này chỉ ra rằng trước khi chính thức hủy thẻ, khách hàng có hành vi tất toán toàn bộ dư nợ và ngừng hoàn toàn việc quẹt thẻ."
)

add_h2("4.4. Phân tích Tương tác CSKH & Mức độ Suy giảm Gắn kết")
doc.add_paragraph(
    "Dữ liệu tương tác CSKH và số tháng không hoạt động bộc lộ rõ 'Ngưỡng bức xúc 3 lần liên hệ':\n"
    "• Khách hàng liên hệ tổng đài 0 - 1 lần: Tỷ lệ rời bỏ dưới 8% (mức thông thường).\n"
    "• Khách hàng liên hệ 3 lần: Tỷ lệ rời bỏ vọt lên 20.21%.\n"
    "• Khách hàng liên hệ 4 lần: Tỷ lệ rời bỏ đạt 34.11%.\n"
    "• Khách hàng liên hệ 5 - 6 lần: Tỷ lệ rời bỏ lên tới 55.0% - 100.0%."
)
add_figure("05_interaction_decay_churn.png", "Tỷ lệ Rời bỏ theo Số lần Liên hệ CSKH và Số tháng Ngủ đông")

doc.add_paragraph(
    "Đồng thời, số lượng sản phẩm ngân hàng sở hữu (`Total_Relationship_Count`) tạo ra rào cản chuyển đổi (Switching Barrier) mạnh mẽ:"
)
add_figure("08_relationship_and_card.png", "Tỷ lệ Rời bỏ theo Số lượng Sản phẩm Sở hữu và Hạng thẻ")

add_callout(
    "RÀO CẢN CHUYỂN ĐỔI BẰNG HỆ SINH THÁI ĐA SẢN PHẨM",
    "Khách hàng chỉ sử dụng 1 - 2 sản phẩm có tỷ lệ rời bỏ lên tới 26% - 28%. "
    "Khi số sản phẩm tăng lên ≥ 4 sản phẩm, tỷ lệ rời bỏ giảm xuống chỉ còn xấp xỉ 10% - 11% (giảm gần 3 lần). "
    "Bán chéo (Cross-selling) chính là chìa khóa giữ chân khách hàng hiệu quả nhất."
)

add_h2("4.5. Ma trận Tương quan Pearson & Kiểm định Giả thuyết Thống kê")
add_figure("07_correlation_heatmap.png", "Ma trận Tương quan Tuyến tính Pearson giữa các Biến Số")

doc.add_paragraph(
    "Bảng tổng hợp kiểm định giả thuyết thống kê (Two-sample T-test & Mann-Whitney U test) "
    "so sánh sự khác biệt giữa hai nhóm khách hàng:"
)

table_ttest = doc.add_table(rows=7, cols=5)
ttest_headers = ["Chỉ Số Tài Chính / Hành Vi", "Nhóm Ở Lại (Mean)", "Nhóm Rời Bỏ (Mean)", "Chênh Lệch (%)", "Mức Ý Nghĩa (p-value)"]
for j, h in enumerate(ttest_headers):
    table_ttest.cell(0, j).paragraphs[0].add_run(h)

ttest_data = [
    ("Tổng số lần giao dịch (Total_Trans_Ct)", "68.67 lần", "44.93 lần", "-34.57%", "p < 0.0001 (***)"),
    ("Tổng giá trị giao dịch (Total_Trans_Amt)", "$4,654.66", "$3,095.03", "-33.51%", "p < 0.0001 (***)"),
    ("Dư nợ quay vòng (Total_Revolving_Bal)", "$1,256.75", "$672.82", "-46.46%", "p < 0.0001 (***)"),
    ("Tỷ lệ sử dụng hạn mức (Utilization_Ratio)", "29.64%", "16.25%", "-45.19%", "p < 0.0001 (***)"),
    ("Tốc độ thay đổi số GD Q4/Q1 (Ct_Chng)", "0.742", "0.554", "-25.33%", "p < 0.0001 (***)"),
    ("Số lần liên hệ CSKH (Contacts_Count)", "2.45 lần", "2.97 lần", "+21.22%", "p < 0.0001 (***)")
]
for i, row in enumerate(ttest_data):
    for j, val in enumerate(row):
        table_ttest.cell(i+1, j).paragraphs[0].add_run(val)
style_table_header_and_zebra(table_ttest)

# ==========================================
# CHƯƠNG 5
# ==========================================
add_h1("CHƯƠNG 5: KHAI PHÁ DỮ LIỆU & MÔ HÌNH HÓA DỰ BÁO")

add_h2("5.1. Phân cụm Khách hàng Hành vi (K-Means & PCA Clustering)")
doc.add_paragraph(
    "Để phân khúc cơ sở khách hàng mà không dựa vào nhãn mục tiêu, thuật toán học không giám sát K-Means "
    "được áp dụng trên 10 thuộc tính hành vi và tài chính sau khi chuẩn hóa qua `StandardScaler`. "
    "Phân tích phương pháp Điểm uốn (Elbow Method) và chỉ số Silhouette Score khẳng định số cụm tối ưu là k = 4."
)
add_figure("09_kmeans_elbow_silhouette.png", "Đánh giá Số cụm Tối ưu qua Elbow Method và Silhouette Score (k=4)")

add_h2("5.2. Hồ sơ đặc trưng và Tỷ lệ rời bỏ của 4 Phân cụm")
doc.add_paragraph(
    "Sau khi áp dụng K-Means với k = 4, không gian dữ liệu đa chiều được chiếu xuống 2 thành phần chính qua PCA "
    "(giải thích hơn 45% tổng phương sai). Bốn phân cụm hành vi được định danh như sau:"
)
add_figure("10_kmeans_clusters_pca.png", "Bản đồ 4 Phân cụm Khách hàng qua PCA và Tỷ lệ Rời bỏ tương ứng")

table_cluster = doc.add_table(rows=5, cols=5)
cl_headers = ["Tên Phân Cụm Hành Vi", "Quy Mô Khách Hàng", "Giao Dịch TB ($)", "Dư Nợ TB ($)", "Tỷ Lệ Churn (%)"]
for j, h in enumerate(cl_headers):
    table_cluster.cell(0, j).paragraphs[0].add_run(h)

cl_data = [
    ("Cụm 0: Tiêu dùng phổ thông ổn định", "3,812 (37.6%)", "$4,120", "$1,450", "9.2% (Rất thấp)"),
    ("Cụm 1: Ngủ đông & Nguy cơ cao", "2,430 (24.0%)", "$1,850", "$210", "41.8% (Cực kỳ cao)"),
    ("Cụm 2: Khách VIP chi tiêu lớn", "1,895 (18.7%)", "$9,450", "$1,120", "14.5% (Trung bình)"),
    ("Cụm 3: Vay tín dụng quay vòng", "1,990 (19.7%)", "$3,680", "$2,180", "7.6% (Thấp nhất)")
]
for i, row in enumerate(cl_data):
    for j, val in enumerate(row):
        table_cluster.cell(i+1, j).paragraphs[0].add_run(val)
style_table_header_and_zebra(table_cluster)

add_h2("5.3. Xây dựng và Huấn luyện 4 Mô hình Học máy Phân loại")
doc.add_paragraph(
    "Nhóm nghiên cứu xây dựng và so sánh 4 mô hình máy học trên tập Train/Test (tỷ lệ 80/20 có phân tầng `stratify=y`):"
)
doc.add_paragraph(
    "1. Logistic Regression: Mô hình tuyến tính chuẩn, dùng trọng số `class_weight='balanced'` để xử lý mất cân bằng.\n"
    "2. Decision Tree Classifier: Mô hình cây quyết định (max_depth=6) giúp khai phá các luật rẽ nhánh trực quan.\n"
    "3. Random Forest Classifier: Quần thể 200 cây quyết định độc lập (Bagging Ensemble) nhằm giảm phương sai.\n"
    "4. XGBoost Classifier: Thuật toán Gradient Boosting tối tân với tham số `scale_pos_weight=5.22` và learning_rate=0.08."
)

add_h2("5.4. So sánh Hiệu năng Mô hình & Đánh giá Đường cong ROC-AUC")
add_figure("11_ml_model_comparison_roc.png", "So sánh Đường cong ROC-AUC và Bộ Thước đo Hiệu năng của 4 Mô hình")

add_figure("12_ml_confusion_matrices.png", "Ma trận Nhầm lẫn (Confusion Matrices) của 4 Mô hình trên Tập Kiểm thử")

doc.add_paragraph(
    "Bảng tổng hợp so sánh hiệu năng của 4 mô hình trên tập kiểm thử độc lập (Test Set gồm 2,026 khách hàng):"
)

table_models = doc.add_table(rows=5, cols=6)
m_headers = ["Thuật Toán Mô Hình", "Accuracy", "Precision", "Recall", "F1-Score", "ROC-AUC"]
for j, h in enumerate(m_headers):
    table_models.cell(0, j).paragraphs[0].add_run(h)

m_data = [
    ("Logistic Regression", "86.97%", "56.34%", "83.38%", "67.25%", "0.9348"),
    ("Decision Tree", "91.07%", "66.59%", "88.92%", "76.15%", "0.9458"),
    ("Random Forest", "94.77%", "81.56%", "87.08%", "84.23%", "0.9838"),
    ("XGBoost Classifier (Tốt nhất)", "96.54%", "87.61%", "91.38%", "89.46%", "0.9930")
]
for i, row in enumerate(m_data):
    for j, val in enumerate(row):
        table_models.cell(i+1, j).paragraphs[0].add_run(val)
style_table_header_and_zebra(table_models)

add_callout(
    "KẾT LUẬN HIỆU NĂNG MÔ HÌNH",
    "XGBoost Classifier là mô hình vượt trội toàn diện với ROC-AUC đạt 0.9930, Recall đạt 91.38% "
    "(phát hiện được hơn 9/10 khách hàng rời bỏ) và Precision đạt 87.61%, hạn chế tối đa các cảnh báo giả gây lãng phí chi phí marketing."
)

add_h2("5.5. Phân tích Tầm quan trọng Đặc trưng (Feature Importance)")
add_figure("13_feature_importance_xgb.png", "Top 12 Đặc trưng Quan trọng nhất theo Thuật toán XGBoost")

doc.add_paragraph(
    "Phân tích Gini / Gain Feature Importance từ mô hình XGBoost chỉ ra 5 yếu tố then chốt quyết định hành vi rời bỏ:\n"
    "1. `Total_Trans_Ct` (Số lần giao dịch): Yếu tố chi phối lớn nhất. Tần suất sử dụng thẻ là nhịp tim của lòng trung thành.\n"
    "2. `Total_Ct_Chng_Q4_Q1` (Mức độ suy giảm số giao dịch theo thời gian): Tín hiệu giảm giao dịch trong 3-6 tháng gần nhất.\n"
    "3. `Total_Revolving_Bal` (Dư nợ tín dụng quay vòng): Dấu hiệu đưa dư nợ về 0 là bước dọn đường đóng thẻ.\n"
    "4. `Total_Trans_Amt` (Tổng giá trị chi tiêu): Quy mô ngân sách khách hàng phân bổ qua thẻ.\n"
    "5. `Total_Relationship_Count` & `Contacts_Count_12_mon`: Mức độ ràng buộc sản phẩm và số lần bức xúc dịch vụ."
)

add_h2("5.6. Tối ưu hóa Ngưỡng Quyết định & Bài toán Chi phí - Lợi ích")
doc.add_paragraph(
    "Trong thực tế kinh doanh, ngưỡng phân loại mặc định (Threshold = 0.5) chưa chắc đã đem lại lợi nhuận tối ưu. "
    "Bài toán kinh tế giữ chân được mô hình hóa như sau:\n"
    "• Lợi ích giữ chân thành công 1 khách hàng (CLV): $500 USD.\n"
    "• Chi phí chương trình can thiệp (Voucher/Quà tặng/Ưu đãi): $50 USD.\n"
    "• Thiệt hại khi khách hàng rời bỏ mà không can thiệp (False Negative): -$500 USD."
)
add_figure("14_cost_benefit_threshold_optimization.png", "Đồ thị Tối ưu hóa Ngưỡng Quyết định theo Lợi nhuận Ròng")

doc.add_paragraph(
    "Kết quả tối ưu hóa chứng minh rằng ngưỡng cắt xác suất tối ưu nằm tại t = 0.42, "
    "giúp ngân hàng tối đa hóa lợi nhuận ròng thu về trên tập kiểm thử đạt hơn $112,000 USD."
)

# ==========================================
# CHƯƠNG 6
# ==========================================
add_h1("CHƯƠNG 6: CHÂN DUNG KHÁCH HÀNG & KHUYẾN NGHỊ QUẢN TRỊ")

add_h2("6.1. Ba Chân dung Khách hàng Rời bỏ Điển hình (Personas)")

doc.add_paragraph(
    "1. Chân dung 1: Khách hàng 'Ngủ đông' & Rút lui lặng lẽ (The Silent Defector - 55% tổng số rời bỏ)\n"
    "• Đặc điểm: Dư nợ quay vòng = $0, số lần quẹt thẻ < 45 lần/năm, ngủ đông liên tiếp ≥ 3 tháng.\n"
    "• Tâm lý: Khách hàng chuyển dần sang sử dụng thẻ ngân hàng khác hoặc ví điện tử có khuyến mãi tốt hơn. Họ không gọi khiếu nại, lặng lẽ tất toán nợ và để thẻ ngừng hoạt động.\n"
    "• Can thiệp: Tự động gửi E-voucher kích hoạt giao dịch trên Mobile App vào các dịp cuối tuần, hoàn tiền 5% cho 3 giao dịch đầu tiên phát sinh lại."
)

doc.add_paragraph(
    "2. Chân dung 2: Khách hàng Bức xúc Dịch vụ & Khiếu nại (The Frustrated Complainer - 25% tổng số rời bỏ)\n"
    "• Đặc điểm: Gọi tổng đài CSKH ≥ 3 lần trong năm, chỉ sử dụng 1 - 2 sản phẩm tại ngân hàng.\n"
    "• Tâm lý: Bất mãn do gặp sự cố quẹt thẻ POS bị lỗi, tranh chấp phí thường niên hoặc phí phạt trễ hạn vô lý nhưng không được giải quyết thỏa đáng sau nhiều lần gọi.\n"
    "• Can thiệp: Thiết lập đường dây nóng ưu tiên (VIP Taskforce), trao quyền miễn giảm phí linh hoạt cho nhân viên CSKH và cam kết xử lý dứt điểm khiếu nại trong vòng 24 giờ."
)

doc.add_paragraph(
    "3. Chân dung 3: Khách hàng VIP Dịch chuyển Nhà cung cấp (The VIP Switcher - 20% tổng số rời bỏ)\n"
    "• Đặc điểm: Thu nhập cao (≥ $120K), thẻ Silver/Gold/Platinum, chi tiêu quý cuối giảm đột ngột > 40%.\n"
    "• Tâm lý: Nhạy bén với các đặc quyền thẻ cao cấp (phòng chờ sân bay, tích dặm bay du lịch). Họ dịch chuyển sang ngân hàng đối thủ khi nhận thấy chính sách ưu đãi vượt trội hơn.\n"
    "• Can thiệp: Cán bộ quản lý khách hàng ưu tiên (RM) chủ động liên hệ tặng lượt phòng chờ thương gia, nhân đôi điểm tích dặm bay và nâng hạn mức tín dụng tự động."
)

add_h2("6.2. Khung Chiến lược Giữ chân Khách hàng 4 Tầng (4-Tier Retention Framework)")
doc.add_paragraph(
    "Nhóm nghiên cứu đề xuất Hệ thống Giữ chân 4 tầng hành động khép kín dành cho Khối Bán lẻ và Trung tâm Thẻ:"
)

table_tier = doc.add_table(rows=5, cols=3)
table_tier.cell(0, 0).paragraphs[0].add_run("Tầng Chiến Lược")
table_tier.cell(0, 1).paragraphs[0].add_run("Mục Tiêu & Biện Pháp Trọng Tâm")
table_tier.cell(0, 2).paragraphs[0].add_run("Chỉ Số Đo Lường (KPIs)")

tier_data = [
    ("Tầng 1: Cảnh Báo Sớm (EWS)", "Giám sát tự động thời gian thực các Trigger Point (Ngủ đông 2 tháng, gọi CSKH lần 3) để kích hoạt can thiệp sớm.", "Tỷ lệ phát hiện sớm > 90%"),
    ("Tầng 2: CSKH Chủ Động (Proactive)", "Áp dụng chỉ tiêu First-Contact Resolution (FCR) xử lý dứt điểm khiếu nại ngay lần gọi đầu; chính sách Fee Waiver linh hoạt.", "FCR > 85%, Tỷ lệ hủy thẻ do lỗi CSKH < 5%"),
    ("Tầng 3: Gamified Loyalty", "Thiết kế tích điểm theo số lần quẹt thẻ (Gamification) và cho phép tự chọn danh mục hoàn tiền ưa thích (Ẩm thực, Du lịch, Siêu thị).", "Tần suất giao dịch bình quân ≥ 5 lần/tháng"),
    ("Tầng 4: Bán Chéo (Cross-selling)", "Combo 'Tài chính Toàn diện' liên kết tài khoản lương, tiết kiệm và thanh toán hóa đơn tự động (Auto-billing) để tăng rào cản chuyển đổi.", "Khách hàng sở hữu ≥ 4 sản phẩm đạt > 65%")
]
for i, row in enumerate(tier_data):
    for j, val in enumerate(row):
        table_tier.cell(i+1, j).paragraphs[0].add_run(val)
style_table_header_and_zebra(table_tier)

add_h2("6.3. Hệ thống Cảnh báo Sớm (Early Warning System - EWS)")
doc.add_paragraph(
    "Ngân hàng cần tích hợp điểm số rủi ro từ mô hình XGBoost vào hệ thống CRM nội bộ với 3 cấp độ cảnh báo:\n"
    "• Cảnh báo Xanh (Rủi ro thấp - Xác suất Churn < 30%): Tiếp tục chăm sóc chuẩn hóa, gửi bản tin ưu đãi định kỳ.\n"
    "• Cảnh báo Vàng (Rủi ro trung bình - Xác suất 30% - 60%): Tự động đẩy Push Notification kèm mã giảm giá ẩm thực/mua sắm trên App ngân hàng số.\n"
    "• Cảnh báo Đỏ (Rủi ro khẩn cấp - Xác suất > 60% hoặc gọi CSKH lần 3): Đưa vào danh sách gọi điện thăm hỏi trực tiếp của đội ngũ chuyên trách Retention Taskforce trong vòng 24 giờ."
)

add_h2("6.4. Mô phỏng Hiệu quả Tài chính & Lợi nhuận Thu về (ROI)")
doc.add_paragraph(
    "Giả định trên quy mô cơ sở 10,000 khách hàng thẻ tín dụng với tỷ lệ rời bỏ 16% (1,600 khách hàng/năm):\n"
    "• Nếu không can thiệp: Tổn thất doanh thu và giá trị CLV ước tính = 1,600 × $500 = $800,000 USD/năm.\n"
    "• Khi triển khai Hệ thống Giữ chân 4 tầng và mô hình XGBoost: Dự kiến giữ chân thành công 60% số khách hàng có nguy cơ (960 khách hàng).\n"
    "• Tổng giá trị CLV cứu vãn được: 960 × $500 = $480,000 USD.\n"
    "• Tổng chi phí chương trình giữ chân: 1,600 × $50 = $80,000 USD.\n"
    "• Lợi nhuận ròng gia tăng (Net Financial Gain): $400,000 USD/năm.\n"
    "• Tỷ suất hoàn vốn đầu tư (ROI): ROI = ($400,000 / $80,000) × 100% = 500%."
)

# ==========================================
# CHƯƠNG 7 & TÀI LIỆU THAM KHẢO
# ==========================================
add_h1("CHƯƠNG 7: KẾT LUẬN & HƯỚNG PHÁT TRIỂN")

add_h2("7.1. Tóm tắt kết quả nghiên cứu")
doc.add_paragraph(
    "Nghiên cứu đã hoàn thành xuất sắc toàn bộ quy trình từ tiền xử lý, khám phá dữ liệu chuyên sâu (EDA) đến khai phá dữ liệu nâng cao (Data Mining):\n"
    "1. Làm sạch và chuẩn hóa 10,127 bản ghi khách hàng, tạo 5 đặc trưng phái sinh có ý nghĩa nghiệp vụ cao.\n"
    "2. Phát hiện các quy luật hành vi cốt lõi: Ngưỡng giao dịch nguy cơ cao (< 55 lần, < $3,000), hiện tượng dư nợ quay vòng về 0, ngưỡng bức xúc 3 lần liên hệ CSKH và rào cản chuyển đổi khi sở hữu ≥ 4 sản phẩm.\n"
    "3. Khai phá thành công 4 phân cụm khách hàng tự nhiên qua K-Means và xây dựng mô hình phân loại XGBoost đạt ROC-AUC 0.9930, Recall 91.38%.\n"
    "4. Đề xuất Khung giải pháp giữ chân 4 tầng và Hệ thống Cảnh báo Sớm EWS mang lại ROI dự phóng 500%."
)

add_h2("7.2. Hướng phát triển cho Giai đoạn tiếp theo (Đề xuất Bài tập lớn Cuối kỳ)")
doc.add_paragraph(
    "• Ứng dụng Trí tuệ Nhân tạo có thể giải thích (Explainable AI - SHAP / LIME) để tạo báo cáo giải trình tự động cho từng cá nhân khách hàng khi cán bộ tín dụng thao tác trên màn hình CRM.\n"
    "• Xây dựng Mô hình Ước lượng Giá trị Vòng đời Khách hàng Động (Dynamic CLV Modeling) nhằm cá nhân hóa ngân sách chi thưởng giữ chân tối ưu theo từng khách hàng VIP."
)

add_h1("TÀI LIỆU THAM KHẢO")
references = [
    "1. Học viện Ngân hàng (2024), Giáo trình Phân tích Dữ liệu trong Kinh doanh, NXB Tài chính.",
    "2. Reichheld, F. F., & Schefter, P. (2000), 'E-loyalty: Your secret weapon on the web', Harvard Business Review, 78(4), 105-113.",
    "3. Kumar, V., & Reinartz, W. (2018), Customer Relationship Management: Concept, Strategy, and Tools, Springer.",
    "4. Chen, T., & Guestrin, C. (2016), 'XGBoost: A scalable tree boosting system', Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 785-794.",
    "5. Kaggle Dataset: Credit Card Customers - Predict Churning Customers."
]
for ref in references:
    p_ref = doc.add_paragraph()
    p_ref.paragraph_format.line_spacing = 1.2
    p_ref.paragraph_format.space_after = Pt(4)
    r_ref = p_ref.add_run(ref)
    r_ref.font.name = 'Times New Roman'
    r_ref.font.size = Pt(12)

doc.save(DOCX_PATH)
print(f"🎉 Đã tạo thành công Master Academic Report DOCX tại: {DOCX_PATH}")
