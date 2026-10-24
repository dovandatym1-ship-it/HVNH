import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

doc = docx.Document()

# Margin setup
for s in doc.sections:
    s.top_margin = Inches(0.8)
    s.bottom_margin = Inches(0.8)
    s.left_margin = Inches(1.0)
    s.right_margin = Inches(0.8)

# Colors
C_PRIMARY = RGBColor(0, 51, 102)     # Deep Navy
C_SECONDARY = RGBColor(194, 65, 12)  # Amber / Dark Orange
C_TEXT = RGBColor(30, 41, 59)        # Slate Dark
C_MUTED = RGBColor(100, 116, 139)    # Gray
C_CUE = RGBColor(13, 148, 136)       # Teal
C_ALERT = RGBColor(185, 28, 28)      # Crimson Red
C_EXPLAIN = RGBColor(3, 105, 161)    # Blue for integrated explanations

def set_run_font(run, font_name="Times New Roman", size_pt=12, bold=False, italic=False, color=C_TEXT):
    run.font.name = font_name
    run.font.size = Pt(size_pt)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = color

def add_title(text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(4)
    r = p.add_run(text)
    set_run_font(r, size_pt=17, bold=True, color=C_PRIMARY)
    return p

def add_subtitle(text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(6)
    r = p.add_run(text)
    set_run_font(r, size_pt=12.5, bold=True, color=C_SECONDARY)
    return p

def add_meta_info(text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(12)
    r = p.add_run(text)
    set_run_font(r, size_pt=11, italic=True, color=C_MUTED)
    return p

def add_heading_1(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(5)
    r = p.add_run(text)
    set_run_font(r, size_pt=13.5, bold=True, color=C_PRIMARY)
    return p

def add_heading_2(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(9)
    p.paragraph_format.space_after = Pt(3)
    r = p.add_run(text)
    set_run_font(r, size_pt=12, bold=True, color=C_SECONDARY)
    return p

def add_speaker_tag(speaker, slide_title, duration):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(2)
    
    r1 = p.add_run(f"🎤 [{speaker}] ")
    set_run_font(r1, size_pt=11.5, bold=True, color=C_PRIMARY)
    
    r2 = p.add_run(f"• {slide_title}  ")
    set_run_font(r2, size_pt=11.5, bold=True, color=C_TEXT)
    
    r3 = p.add_run(f"(Thời lượng: ~{duration})")
    set_run_font(r3, size_pt=10.5, italic=True, color=C_MUTED)
    return p

def add_speech(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.15
    r = p.add_run(text)
    set_run_font(r, size_pt=11.5, color=C_TEXT)
    return p

def add_cue(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(1)
    p.paragraph_format.space_after = Pt(3)
    r = p.add_run(f"👉 [Hành động & Điểm nhấn]: {text}")
    set_run_font(r, size_pt=10, italic=True, color=C_CUE)
    return p

def add_handover(from_person, to_person, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(8)
    
    r1 = p.add_run(f"🤝 [LỜI NỐI CHUYỂN GIAO • {from_person} ➔ {to_person}]: ")
    set_run_font(r1, size_pt=10.5, bold=True, color=C_ALERT)
    
    r2 = p.add_run(f"\"{text}\"")
    set_run_font(r2, size_pt=11, bold=True, italic=True, color=C_TEXT)
    return p

def add_qa_item(num, question, trap_intent, answer_script, tip):
    add_heading_2(f"Câu hỏi {num}: \"{question}\"")
    
    p_trap = doc.add_paragraph()
    p_trap.paragraph_format.space_after = Pt(2)
    r_t1 = p_trap.add_run("🎯 Ý đồ của Thầy: ")
    set_run_font(r_t1, size_pt=10.5, bold=True, color=C_ALERT)
    r_t2 = p_trap.add_run(trap_intent)
    set_run_font(r_t2, size_pt=10.5, italic=True, color=C_MUTED)
    
    p_ans = doc.add_paragraph()
    p_ans.paragraph_format.space_after = Pt(3)
    p_ans.paragraph_format.line_spacing = 1.15
    r_a1 = p_ans.add_run("💬 Câu trả lời mẫu: ")
    set_run_font(r_a1, size_pt=11, bold=True, color=C_PRIMARY)
    r_a2 = p_ans.add_run(f"\"{answer_script}\"")
    set_run_font(r_a2, size_pt=11, color=C_TEXT)
    
    p_tip = doc.add_paragraph()
    p_tip.paragraph_format.space_after = Pt(6)
    r_tp1 = p_tip.add_run("💡 Mẹo ứng biến: ")
    set_run_font(r_tp1, size_pt=10, bold=True, color=C_CUE)
    r_tp2 = p_tip.add_run(tip)
    set_run_font(r_tp2, size_pt=10, italic=True, color=C_TEXT)

# --- START WRITING CONTENT ---

add_title("KỊCH BẢN THUYẾT TRÌNH BẢO VỆ ĐỀ TÀI BPM (BẢN LỒNG GHÉP GIẢI NGHĨA THUẬT NGỮ)")
add_subtitle("ĐÁNH GIÁ VÀ HOÀN THIỆN QUY TRÌNH TRIỂN KHAI TÍN DỤNG VÀ GIẢI NGÂN KHÁCH HÀNG CÁ NHÂN TẠI LPBANK")
add_meta_info("Học viện Ngân hàng • Môn Quản trị Quy trình Nghiệp vụ (BPM) • GVHD: TS. Phan Thanh Đức\nThời lượng chuẩn: 15–17 phút  |  Khung slide: 19 slide  |  Phân vai: 5 học viên")

# Guideline Box
p_g = doc.add_paragraph()
p_g.paragraph_format.space_before = Pt(3)
p_g.paragraph_format.space_after = Pt(8)
r_g1 = p_g.add_run("📌 ĐIỂM ĐẶC BIỆT CỦA BẢN KỊCH BẢN NÀY:\n")
set_run_font(r_g1, size_pt=10.5, bold=True, color=C_PRIMARY)
r_g2 = p_g.add_run(
    "Toàn bộ các từ viết tắt và thuật ngữ chuyên ngành (như CIR, BSC, Process Landscape, Checklist, APQC PCF, Idempotency, As-Is, To-Be, Maker–Checker, CSU, RM, Shift-Left, Cycle Time, FTR, SLA, RACI...) "
    "ĐÃ ĐƯỢC LỒNG GHÉP GIẢI THÍCH TRỰC TIẾP VÀO TỪNG CÂU NÓI bằng ngôn ngữ đời thường, gãy gọn.\n"
    "Người thuyết trình chỉ cần nói theo kịch bản là vừa giải thích được bản chất cho Thầy và cả lớp hiểu, vừa không bị vấp hay 'nói vẹt' thuật ngữ!"
)
set_run_font(r_g2, size_pt=10, italic=True, color=C_TEXT)

# Table of roles
add_heading_1("BẢNG PHÂN CÔNG DIỄN THUYẾT (5 THÀNH VIÊN)")
table = doc.add_table(rows=6, cols=5)
table.alignment = WD_TABLE_ALIGNMENT.CENTER
headers = ["Vai trò", "Họ và tên", "Mã học viên", "Phạm vi phụ trách", "Thời lượng"]
for i, h in enumerate(headers):
    cell = table.cell(0, i)
    cell.text = h
    cell.paragraphs[0].runs[0].font.bold = True
    cell.paragraphs[0].runs[0].font.name = "Times New Roman"
    cell.paragraphs[0].runs[0].font.size = Pt(10)
    cell.paragraphs[0].runs[0].font.color.rgb = RGBColor(255, 255, 255)
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="003366"/>')
    cell._tc.get_or_add_tcPr().append(shd)

roles_data = [
    ("Người 1", "Nguyễn Linh Chi", "28K406003", "Mở đầu & Phần 1: Bối cảnh, BSC, Landscape, Checklist (Slide 1–6)", "3.5 phút"),
    ("Người 2", "Tạ Ngọc Tuệ", "28K406011", "Phần 2: Đối chiếu chuẩn APQC Banking PCF & Gap Analysis (Slide 7–9)", "3.0 phút"),
    ("Người 3", "Đỗ Văn Đạt", "28K405001", "Phần 3: Chọn quy trình ưu tiên, Luồng As-Is, Đánh giá EA/Lean (Slide 10–12)", "3.0 phút"),
    ("Người 4", "Trương An Ninh", "28K405003", "Phần 4A: Đề xuất luồng To-Be 8 chặng & 5 Nhóm giải pháp cải tiến (Slide 13–14)", "3.0 phút"),
    ("Người 5", "Trần Ngọc Dũng", "28K406005", "Phần 4B & Kết luận: 5 KPI, Lộ trình, Nghiệm thu, 4 Ưu tiên & Disclaimer (Slide 15–19)", "3.5 phút"),
]

for row_idx, data in enumerate(roles_data, 1):
    for col_idx, text in enumerate(data):
        cell = table.cell(row_idx, col_idx)
        cell.text = text
        p_c = cell.paragraphs[0]
        p_c.runs[0].font.name = "Times New Roman"
        p_c.runs[0].font.size = Pt(9.5)
        p_c.runs[0].font.color.rgb = C_TEXT
        if row_idx % 2 == 1:
            shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="F1F5F9"/>')
            cell._tc.get_or_add_tcPr().append(shd)

# -------------------------------------------------------------
# PHẦN 1
# -------------------------------------------------------------
add_heading_1("PHẦN MỞ ĐẦU VÀ PHẦN 1: BỐI CẢNH CHIẾN LƯỢC & NHẬN DIỆN QUY TRÌNH (20%)")

add_speaker_tag("Người 1: Nguyễn Linh Chi", "Slide 1: Giới thiệu đề tài", "45 giây")
add_cue("Đứng thẳng, mỉm cười tự tin, hướng mắt về Thầy Phan Thanh Đức và toàn thể lớp.")
add_speech(
    "Kính thưa Thầy TS. Phan Thanh Đức và các anh chị học viên!\n"
    "Đại diện nhóm nghiên cứu, em xin trình bày đề tài: 'Đánh giá và hoàn thiện quy trình triển khai tín dụng và giải ngân Khách hàng cá nhân – tức mảng KHCN vay mua nhà, mua xe, tiêu dùng – tại Ngân hàng Lộc Phát Việt Nam LPBank'."
)
add_speech(
    "Trong hoạt động ngân hàng, phê duyệt khoản vay mới chỉ là một nửa chặng đường. "
    "Khoản vay đó có thực sự tạo ra giá trị hay không phụ thuộc hoàn toàn vào khâu giải ngân – nơi tiền thực tế được chuyển vào tài khoản khách hàng. "
    "Quy trình này đòi hỏi phải vừa giải ngân nhanh cho khách, nhưng vừa phải kiểm soát chặt chẽ rủi ro mất vốn và sai sót pháp lý. "
    "Hôm nay, nhóm em áp dụng môn học Quản trị Quy trình Nghiệp vụ – BPM – kết hợp với bộ khung chuẩn quốc tế APQC để cùng bóc tách hiện trạng và đề xuất giải pháp cải tiến thực chất cho LPBank."
)

add_speaker_tag("Người 1: Nguyễn Linh Chi", "Slide 2: Giới thiệu nhóm & Cấu trúc nghiên cứu", "30 giây")
add_cue("Đưa tay hướng nhẹ về màn hình Slide 2, giới thiệu nhanh đồng đội.")
add_speech(
    "Nhóm nghiên cứu gồm 5 thành viên như trên màn hình: Linh Chi, Ngọc Tuệ, Văn Đạt, An Ninh và Ngọc Dũng."
)
add_speech(
    "Bài trình bày gồm 4 phần trọng tâm:\n"
    "• Phần 1: Bối cảnh chiến lược và nhận diện quy trình bằng bức tranh tổng thể Process Landscape.\n"
    "• Phần 2: Đối chuẩn với khung phân loại quốc tế APQC Banking PCF 7.2.2 và phân tích khoảng trống Gap Analysis.\n"
    "• Phần 3: Đánh giá luồng hiện trạng As-Is – tức cách ngân hàng đang làm hiện tại – qua kiến trúc doanh nghiệp và lãng phí Lean.\n"
    "• Phần 4: Đề xuất luồng tương lai To-Be 8 chặng, giải pháp công nghệ và bộ 5 KPI đo lường hiệu suất."
)

add_speaker_tag("Người 1: Nguyễn Linh Chi", "Slide 3: Bối cảnh LPBank và Mục tiêu chiến lược", "50 giây")
add_cue("Chỉ tay vào 3 con số tài chính nổi bật trên Slide 3.")
add_speech(
    "Về bối cảnh: Giai đoạn 2024–2028, LPBank định hướng phát triển bán lẻ đa năng, lấy khách hàng làm trọng tâm."
)
add_speech(
    "Năm 2025, quy mô LPBank tăng trưởng rất ấn tượng: Tổng tài sản đạt trên 508 nghìn tỷ đồng, dư nợ tín dụng hơn 331 nghìn tỷ, "
    "và lợi nhuận trước thuế trên 12 nghìn tỷ. "
    "Đặc biệt, tỷ lệ chi phí trên thu nhập – viết tắt là CIR (Cost-to-Income Ratio) – được kiểm soát rất tốt ở mức 29,15%. "
    "Con số này có nghĩa là: Để kiếm được 100 đồng thu nhập, LPBank chỉ tốn hơn 29 đồng chi phí hoạt động, phản ánh khả năng quản trị chi phí xuất sắc của ngân hàng."
)
add_speech(
    "Khi quy mô tín dụng bán lẻ tăng trưởng bùng nổ, lượng hồ sơ giải ngân dồn về các chi nhánh ngày càng lớn. "
    "Tối ưu quy trình giải ngân là yêu cầu sống còn: Giúp khách hàng nhận tiền đúng hẹn, đồng thời giúp nhân viên nâng cao năng suất xử lý mà không làm phình to chi phí vận hành."
)

add_speaker_tag("Người 1: Nguyễn Linh Chi", "Slide 4: Mục tiêu chiến lược theo Balanced Scorecard (BSC)", "45 giây")
add_cue("Chỉ vào 4 ô vuông đại diện cho 4 lăng kính của Bảng điểm cân bằng.")
add_speech(
    "Để gắn kết bài toán giải ngân với chiến lược chung, nhóm sử dụng công cụ Bảng điểm cân bằng – Balanced Scorecard (BSC) – qua 4 lăng kính toàn diện:\n"
    "1. Lăng kính Tài chính: Tăng trưởng dư nợ an toàn và hạ thấp chi phí xử lý trên từng món vay.\n"
    "2. Lăng kính Khách hàng: Tiền đến tay kịp thời, cắt giảm thủ tục rườm rà và không bắt khách hàng nộp đi nộp lại hồ sơ.\n"
    "3. Lăng kính Quy trình nội bộ: Chuẩn hóa luồng công việc, đồng bộ dữ liệu giữa các phần mềm và phân định rõ trách nhiệm kiểm soát.\n"
    "4. Lăng kính Học tập & phát triển: Đào tạo nhân viên bài bản và chuẩn hóa bộ quy tắc nghiệp vụ."
)
add_speech(
    "Thông điệp của nhóm: Cải tiến quy trình không chỉ là làm nhanh, mà phải tạo ra hiệu quả đồng bộ trên cả 4 trụ cột của Bảng điểm cân bằng."
)

add_speaker_tag("Người 1: Nguyễn Linh Chi", "Slide 5: Kiến trúc quy trình Process Landscape", "40 giây")
add_cue("Chỉ vào dải màu giữa màn hình (nhóm Core Process).")
add_speech(
    "Trên bức tranh tổng thể Process Landscape – tức sơ đồ toàn cảnh các quy trình mảng KHCN – nhóm phân chia thành 3 tầng: "
    "Tầng Quản lý (Management), Tầng Cốt lõi (Core) và Tầng Hỗ trợ (Support)."
)
add_speech(
    "Trong chuỗi giá trị cốt lõi đi từ Tiếp nhận ➔ Thẩm định ➔ Phê duyệt ➔ Triển khai & Giải ngân ➔ Quản lý sau vay, "
    "thì khâu Giải ngân chính là chiếc cầu nối bản lề: biến phương án duyệt trên giấy thành dòng vốn thực tế chạy vào tài khoản. "
    "Vì tầm quan trọng sống còn này, nhóm chọn đây là phạm vi nghiên cứu sâu."
)

add_speaker_tag("Người 1: Nguyễn Linh Chi", "Slide 6: Process Checklist - Kiểm tra tính độc lập", "40 giây")
add_cue("Chỉ vào bảng 5 tiêu chí trên Slide 6.")
add_speech(
    "Trước khi phân tích sâu, nhóm dùng danh sách kiểm tra Process Checklist gồm 5 tiêu chí để xác thực giải ngân có phải một quy trình độc lập hay không:\n"
    "• Thứ nhất, Đầu vào – đầu ra rõ ràng: từ khoản vay đã duyệt đến khi tiền vào tài khoản và hạch toán thành công.\n"
    "• Thứ hai, Có chuỗi công việc lặp lại định kỳ.\n"
    "• Thứ ba, Có chủ thể rõ ràng: từ cán bộ tín dụng RM, Kiểm soát viên đến hệ thống Core T24.\n"
    "• Thứ tư, Hoàn toàn đo lường được qua hệ thống task và nhật ký sự kiện log.\n"
    "• Và thứ năm, Phạm vi tách bạch: chỉ tập trung sau phê duyệt, không lẫn sang thẩm định hay thu hồi nợ."
)
add_speech(
    "Kết luận: Hoạt động giải ngân hoàn toàn đủ điều kiện để quản trị như một quy trình độc lập, cần có Chủ sở hữu quy trình – Process Owner – và bộ chỉ số KPI riêng."
)

add_handover(
    "Nguyễn Linh Chi", "Tạ Ngọc Tuệ",
    "Sau khi đã xác định rõ ranh giới quy trình, câu hỏi đặt ra là: Nếu đối chiếu với chuẩn quốc tế, quy trình của LPBank đang nằm ở đâu và còn những khoảng trống nào? Sau đây xin mời bạn Tạ Ngọc Tuệ trình bày Phần 2: Đối chiếu khung chuẩn APQC."
)

# -------------------------------------------------------------
# PHẦN 2
# -------------------------------------------------------------
add_heading_1("PHẦN 2: ĐỐI CHIẾU VỚI BỘ KHUNG CHUẨN QUỐC TẾ APQC BANKING PCF (30%)")

add_speaker_tag("Người 2: Tạ Ngọc Tuệ", "Slide 7: Định vị theo APQC Banking PCF 7.2.2", "50 giây")
add_cue("Gật đầu cảm ơn Linh Chi, tự tin nhận mic, hướng mắt lên màn hình.")
add_speech(
    "Xin cảm ơn bạn Linh Chi! Kính thưa Thầy và các anh chị, để có thước đo khách quan, nhóm đối chuẩn với khung APQC Banking Process Classification Framework (PCF) – "
    "đây là Khung phân loại quy trình ngành ngân hàng chuẩn quốc tế do Trung tâm Năng suất & Chất lượng Hoa Kỳ ban hành, bản cập nhật mới nhất 7.2.2."
)
add_speech(
    "APQC cung cấp một ngôn ngữ chung toàn cầu qua 4 cấp độ phân cấp. "
    "Tại Level 4, hoạt động trọng tâm của chúng ta được định vị chính xác với mã chuẩn quốc tế PCF ID là 13961: 'Cấp vốn và giải ngân tiền vay' (Fund and disburse proceeds)."
)
add_speech(
    "Một nguyên tắc then chốt mà nhóm luôn quán triệt: APQC là khung phân loại chức năng (Classification) để biết mình có đủ việc hay không, "
    "chứ không phải sơ đồ luồng công việc tác nghiệp (Workflow). Vì vậy, nhóm dùng APQC để soi khoảng trống, chứ không sao chép máy móc APQC thành quy trình hàng ngày."
)

add_speaker_tag("Người 2: Tạ Ngọc Tuệ", "Slide 8: Mapping chi tiết giữa APQC và LPBank", "55 giây")
add_cue("Chỉ vào bảng đối chiếu 7 cụm nghiệp vụ trên Slide 8.")
add_speech(
    "Trên Slide 8, nhóm đã ánh xạ 7 cụm nghiệp vụ tại LPBank tương ứng các mã PCF ID chuẩn của APQC: từ tải hồ sơ (17400), theo dõi trạng thái (17405), kiểm soát điều kiện vay (17418), "
    "lãi suất (17419), tài sản bảo đảm (17420), thiết lập hạn mức trên T24 (17421), đến hạch toán giải ngân (13961)."
)
add_speech(
    "Về hạ tầng, LPBank đã trang bị hệ thống khởi tạo khoản vay LOS và phần mềm quản trị quy trình Smart BPM khá đầy đủ. "
    "Tuy nhiên, khoảng cách giữa 'có phần mềm' và 'vận hành trơn tru' nằm ở những điểm cần kiểm chứng thực tế:\n"
    "Ví dụ: Đã có màn hình theo dõi trạng thái, nhưng đã có tính năng cảnh báo tự động khi sắp trễ hạn cam kết SLA hay chưa? "
    "Đã có tích hợp với hệ thống ngân hàng lõi Core T24, nhưng khi xảy ra rớt mạng hoặc timeout, cơ chế xử lý lỗi và khóa chống tạo trùng giao dịch – thuật ngữ chuyên ngành gọi là Idempotency Key – đã được kiểm soát chặt chẽ hay chưa? "
    "Khóa Idempotency này cực kỳ quan trọng: nó đảm bảo khi mạng lag gửi lại lệnh, hệ thống cũng chỉ trừ tiền và giải ngân đúng MỘT lần duy nhất, tuyệt đối không bị giải ngân trùng hai lần."
)

add_speaker_tag("Người 2: Tạ Ngọc Tuệ", "Slide 9: Phân tích khoảng trống Gap Analysis", "45 giây")
add_cue("Nhấn mạnh bằng giọng dứt khoát vào 4 ô khoảng trống trên Slide 9.")
add_speech(
    "Từ việc đối chiếu đó, nhóm rút ra 4 bài toán khoảng trống trong phân tích Gap Analysis trên Slide 9:\n"
    "1. Khoảng trống Quản trị: Chưa thấy rõ vai trò của một Process Owner chịu trách nhiệm toàn trình từ đầu đến cuối, và thiếu bộ số liệu mốc chuẩn (baseline) để đo thời gian thực tế.\n"
    "2. Khoảng trống Tích hợp: Cần kiểm chứng cơ chế đối soát tự động giữa phần mềm BPM và ngân hàng lõi T24 để ngăn ngừa rủi ro hạch toán trùng.\n"
    "3. Nguy cơ Chồng chéo: Cần kiểm chứng việc cán bộ tín dụng và kiểm soát viên phải kiểm tra và gõ lại dữ liệu trùng lặp nhiều lần.\n"
    "4. Nguy cơ Phân loại sai: Hiện chưa có bằng chứng kết luận có bước nào bị phân loại sai so với APQC."
)
add_speech(
    "Quan điểm của nhóm là: 'Chưa có bằng chứng không đồng nghĩa với chức năng đó không tồn tại ở LPBank'. Nhóm đánh giá dựa trên sự thận trọng khoa học."
)

add_handover(
    "Tạ Ngọc Tuệ", "Đỗ Văn Đạt",
    "Để trả lời cho câu hỏi: Tại sao nhóm chọn Giải ngân làm ưu tiên cải tiến số 1, và luồng hiện trạng As-Is đang chạy ra sao? Sau đây xin mời bạn Đỗ Văn Đạt sẽ tiếp nối với Phần 3: Đánh giá hiện trạng."
)

# -------------------------------------------------------------
# PHẦN 3
# -------------------------------------------------------------
add_heading_1("PHẦN 3: LỰA CHỌN QUY TRÌNH ƯU TIÊN & ĐÁNH GIÁ HIỆN TRẠNG AS-IS (20%)")

add_speaker_tag("Người 3: Đỗ Văn Đạt", "Slide 10: Ma trận lựa chọn quy trình ưu tiên", "45 giây")
add_cue("Cầm mic tự tin, chỉ vào bảng chấm điểm 4 quy trình trên Slide 10.")
add_speech(
    "Xin cảm ơn bạn Tuệ! Kính thưa Thầy và các anh chị, để chọn ra quy trình cần tối ưu trước tiên, nhóm xây dựng ma trận đánh giá gồm 5 tiêu chí: "
    "Tác động chiến lược (25%), Mức độ ảnh hưởng khách hàng (20%), Rủi ro vận hành (25%), Điểm nghẽn tiềm ẩn (15%) và Dữ liệu sẵn có (15%)."
)
add_speech(
    "Kết quả: Quy trình Giải ngân đạt tới 4,85/5 điểm – đứng đầu bảng, vượt qua cả Thẩm định phê duyệt (4,35) hay Quản lý tài sản bảo đảm (4,10)."
)
add_speech(
    "Lý do rất rõ ràng: Thẩm định là bài toán chính sách tín dụng, còn Giải ngân là nút thắt tác nghiệp trực tiếp. "
    "Chậm giải ngân làm khách hàng bức xúc; sai sót giải ngân gây rủi ro mất tiền ngay lập tức. "
    "Và xin lưu ý: 4,85 là điểm số ưu tiên do nhóm nghiên cứu chấm để lựa chọn đề tài, không phải chỉ số nội bộ của ngân hàng."
)

add_speaker_tag("Người 3: Đỗ Văn Đạt", "Slide 11: Mô tả luồng hiện trạng As-Is", "50 giây")
add_cue("Dùng ngón tay quét từ bước 01 đến 06 trên sơ đồ ngang Slide 11.")
add_speech(
    "Trên Slide 11 là luồng hiện trạng As-Is – tức cách vận hành thực tế hiện nay – gồm 6 bước:\n"
    "• Bước 01: Khởi tạo hồ sơ trên BPM sau khi có thông báo phê duyệt khoản vay.\n"
    "• Bước 02: Cán bộ tín dụng – chuyên viên QHKH (gọi tắt là RM - Relationship Manager) thu thập chứng từ và lập tờ trình giải ngân.\n"
    "• Bước 03: Kiểm soát viên chi nhánh kiểm tra hồ sơ, nếu thiếu giấy tờ thì trả lại cho RM làm lại.\n"
    "• Bước 04: Chuyển tiếp lên Trung tâm Hỗ trợ Tín dụng (CSU - Credit Support Unit) tại Hội sở để rà soát điều kiện giải ngân và thông số tài sản.\n"
    "• Bước 05: Đẩy dữ liệu sang hệ thống ngân hàng lõi Core T24 để hạch toán ghi nợ và giải ngân chuyển tiền.\n"
    "• Bước 06: Lưu trữ điện tử trên hệ thống quản trị nội dung ECM và đóng hồ sơ."
)
add_speech(
    "Ba điểm nghẽn tác nghiệp lớn nhất ở đây là: Hiện tượng 'bóng bàn' – hồ sơ bị trả lại qua lại nhiều lần giữa Kiểm soát viên và RM; "
    "thời gian chờ bàn giao giữa Chi nhánh và CSU Hội sở; cùng nguy cơ lỗi tích hợp khi đẩy dữ liệu sang T24."
)

add_speaker_tag("Người 3: Đỗ Văn Đạt", "Slide 12: Đánh giá theo Kiến trúc Doanh nghiệp & Lean", "50 giây")
add_cue("Chỉ vào 3 trụ cột EA và phân tích lãng phí Lean ở cuối Slide 12.")
add_speech(
    "Nhóm đánh giá sâu hơn hiện trạng này qua 3 tầng Kiến trúc Doanh nghiệp (EA - Enterprise Architecture):\n"
    "• Tầng Tổ chức: Quy trình đi qua quá nhiều bàn tay từ RM chi nhánh đến CSU Hội sở, nhưng thiếu một Process Owner giám sát toàn trình khiến việc phối hợp dễ bị đứt đoạn.\n"
    "• Tầng Dữ liệu: Thông tin phân tán giữa phần mềm khởi tạo LOS, phần mềm quy trình BPM và ngân hàng lõi T24, gây lãng phí gõ lại dữ liệu nhiều lần.\n"
    "• Tầng Khách hàng: Trải nghiệm giảm sút nếu họ phải chờ đợi lâu và bị gọi lên bổ sung giấy tờ lặp đi lặp lại."
)
add_speech(
    "Đặc biệt, dưới góc nhìn Lean BPM về phân tích giá trị:\n"
    "Nhóm đề xuất cắt bỏ triệt để các lãng phí không tạo giá trị – gọi là NVA (Non-Value-Added) như việc chờ đợi và gõ lại hồ sơ;\n"
    "nhưng tuyệt đối PHẢI GIỮ LẠI các hoạt động tạo giá trị cho việc kiểm soát rủi ro và tuân thủ – gọi là BVA (Business Value-Added) – "
    "tiêu biểu là nguyên tắc kiểm soát 4 mắt Maker–Checker bắt buộc của ngành ngân hàng, nơi người lập và người duyệt phải luôn tách biệt."
)

add_handover(
    "Đỗ Văn Đạt", "Trương An Ninh",
    "Vậy làm thế nào để giải quyết triệt để các điểm nghẽn As-Is mà vẫn giữ vững an toàn hệ thống? Tiếp theo đây, xin mời bạn Trương An Ninh trình bày Phần 4 với Bản thiết kế quy trình To-Be 8 chặng và các giải pháp công nghệ."
)

# -------------------------------------------------------------
# PHẦN 4A
# -------------------------------------------------------------
add_heading_1("PHẦN 4A: QUY TRÌNH TO-BE ĐỀ XUẤT & CÁC NHÓM GIẢI PHÁP CẢI TIẾN (15%)")

add_speaker_tag("Người 4: Trương An Ninh", "Slide 13: Quy trình To-Be 8 chặng - Kiểm soát ngay từ đầu", "55 giây")
add_cue("Bắt đầu bằng giọng sôi nổi, tự tin, chỉ vào sơ đồ luồng 8 chặng trên Slide 13.")
add_speech(
    "Cảm ơn bạn Đạt! Kính thưa Thầy và các anh chị, để giải quyết bài toán trên, nhóm đề xuất luồng quy trình tương lai To-Be gồm 8 chặng chuẩn hóa."
)
add_speech(
    "Trọng tâm của quy trình mới nằm ở tư duy 'Shift-Left' – tức đưa việc kiểm soát lên ngay phía trước cửa ngõ:\n"
    "• Ở Chặng 01 và 02: Ngay khi nhận dữ liệu từ phần mềm LOS, hệ thống chạy tự động bộ quy tắc kiểm tra trước (Pre-check bằng Rule Engine). "
    "Hệ thống tự động kiểm tra tính hợp lệ của hồ sơ, thời hạn phê duyệt, hạn mức và tài sản bảo đảm. "
    "Nếu thiếu chứng từ, hệ thống cảnh báo ngay cho cán bộ tín dụng RM xử lý liền, chặn đứng lỗi từ cửa ngõ trước khi hồ sơ kịp gửi đi lòng vòng!\n"
    "• Chặng 03 & 04: RM xác nhận và thực hiện phê duyệt kiểm soát 4 mắt Maker–Checker chuẩn hóa.\n"
    "• Chặng 05 & 06: Tự động gọi API sang Core T24 để hạch toán giải ngân và chuyển tiền theo cơ chế khóa Idempotency chống tạo trùng giao dịch.\n"
    "• Chặng 07 & 08: Đối soát dữ liệu tự động, lưu trữ vào kho số ECM và ghi nhận nhật ký Event Log để đo lường KPI."
)
add_speech(
    "Điểm khác biệt cốt lõi: Thay vì phát hiện lỗi ở cuối quy trình rồi trả hồ sơ lại từ đầu, To-Be chặn đứng lỗi ngay từ cửa ngõ, giúp dòng chảy công việc thông suốt."
)

add_speaker_tag("Người 4: Trương An Ninh", "Slide 14: 5 Nhóm giải pháp hoàn thiện đồng bộ", "50 giây")
add_cue("Chỉ vào bảng 5 nhóm giải pháp trên Slide 14, nhấn mạnh sự kết hợp Quản trị + Công nghệ.")
add_speech(
    "Để hiện thực hóa To-Be, nhóm đề xuất 5 nhóm giải pháp đồng bộ trên Slide 14, kết hợp giữa Quản trị và Công nghệ:\n"
    "1. Cấu trúc & Trách nhiệm: Chỉ định Process Owner duy nhất cho quy trình giải ngân và ban hành ma trận phân định trách nhiệm RACI rõ ràng – quy định rõ Ai làm, Ai chịu trách nhiệm, Ai cần hỏi ý kiến, và Ai cần báo cáo.\n"
    "2. Kiểm soát đầu vào: Xây dựng bộ tiền kiểm Pre-check tự động và chuẩn hóa bảng mã lý do trả hồ sơ (Reason Code) – ví dụ mã ERR01 là thiếu CCCD, ERR02 là lệch số tiền – để biết chính xác nguyên nhân lỗi ở đâu.\n"
    "3. Chuẩn hóa Dữ liệu: Xây dựng Từ điển dữ liệu Data Dictionary và quy định hệ thống nguồn để dữ liệu tự động đồng bộ giữa LOS, BPM và T24.\n"
    "4. Tích hợp Giao dịch: Ứng dụng khóa Idempotency chống trùng lệnh, cơ chế tự động thử lại khi rớt mạng (Retry) và đối soát cuối ngày với T24.\n"
    "5. Giám sát & Tuân thủ: Kích hoạt ghi vết nhật ký Event Log, cảnh báo nguy cơ trễ hạn cam kết SLA và lưu trữ vết kiểm toán Audit Trail phục vụ thanh tra."
)
add_speech(
    "Nhóm xin nhấn mạnh: Tốc độ tăng lên là nhờ tự động hóa thông minh, chứ không hề cắt giảm hay nới lỏng bất kỳ bước kiểm soát rủi ro nào."
)

add_handover(
    "Trương An Ninh", "Trần Ngọc Dũng",
    "Vậy những cải tiến này sẽ được đo lường bằng những chỉ số cụ thể nào, và lộ trình triển khai ra sao để bảo đảm an toàn tuyệt đối? Xin mời bạn Trần Ngọc Dũng trình bày phần cuối của bài báo cáo."
)

# -------------------------------------------------------------
# PHẦN 4B & KẾT LUẬN
# -------------------------------------------------------------
add_heading_1("PHẦN 4B & KẾT LUẬN: ĐO LƯỜNG KPI, LỘ TRÌNH, NGHIỆM THU & THÔNG ĐIỆP (15%)")

add_speaker_tag("Người 5: Trần Ngọc Dũng", "Slide 15: 5 Chỉ số KPI quản trị hiệu suất", "55 giây")
add_cue("Cầm mic đĩnh đạc, chỉ vào bảng 5 chỉ số KPI trên Slide 15.")
add_speech(
    "Xin cảm ơn bạn Ninh! Thưa Thầy và các anh chị, phương châm của BPM là: 'Cái gì không đo lường được thì không thể cải tiến được'. "
    "Do đó, nhóm đề xuất 5 chỉ số KPI theo chuẩn đối chuẩn mở quốc tế APQC Open Standards Benchmarking:\n"
    "1. Thời gian xử lý toàn trình (Cycle Time End-to-End): Đo tổng thời gian từ lúc nộp hồ sơ đến khi tiền vào tài khoản, mục tiêu đề xuất giảm ít nhất 20% thời gian trung vị (Median – tức mốc thời gian của hồ sơ nằm chính giữa, không bị méo mó bởi 1-2 hồ sơ cá biệt).\n"
    "2. First-Time-Right (viết tắt là FTR): Tỷ lệ hồ sơ làm đúng ngay từ lần đầu mà không bị trả lại bổ sung, mục tiêu tăng tối thiểu 15 điểm phần trăm.\n"
    "3. Tỷ lệ hoàn thành đúng hạn cam kết SLA: Đạt trên 95% số hồ sơ sau giai đoạn thí điểm.\n"
    "4. Tỷ lệ hồ sơ phải làm lại sửa chữa (Rework Rate); và 5. Tỷ lệ giao dịch lỗi (Error Rate)."
)
add_speech(
    "Hai chỉ tiêu Rework Rate và Error Rate hiện chưa chốt con số cứng, vì nhóm đề xuất ngân hàng phải đo đạc số liệu mốc chuẩn – baseline – thực tế trong 4 tuần trước khi chính thức phê duyệt chỉ tiêu."
)

add_speaker_tag("Người 5: Trần Ngọc Dũng", "Slide 16: Lộ trình triển khai 4 giai đoạn", "45 giây")
add_cue("Chỉ vào dải 4 mốc thời gian trên Slide 16.")
add_speech(
    "Để triển khai một cách chắc chắn và an toàn, lộ trình được chia thành 4 giai đoạn rõ ràng:\n"
    "• Giai đoạn 0 (Baseline - 4 tuần): Thu thập số liệu thực tế trên hệ thống, chuẩn hóa ma trận RACI và chốt công thức tính KPI.\n"
    "• Giai đoạn 1 (Pilot - 6–8 tuần): Thí điểm quy trình mới To-Be tại 3 đến 5 chi nhánh đại diện để kiểm chứng tính năng Pre-check và đo lường FTR.\n"
    "• Giai đoạn 2 (Roll-out - 8–12 tuần): Chỉ khi giai đoạn Pilot vượt qua Cổng kiểm soát an toàn (gọi là Quality Gate 1), ngân hàng mới mở rộng triển khai trên toàn hệ thống.\n"
    "• Giai đoạn 3 (Sustain): Duy trì cải tiến liên tục bằng công cụ khai phá quy trình Process Mining và định kỳ rà soát quy tắc nghiệp vụ."
)

add_speaker_tag("Người 5: Trần Ngọc Dũng", "Slide 17: Bộ tiêu chí nghiệm thu chặt chẽ", "40 giây")
add_cue("Chỉ vào 3 khối nghiệm thu trên Slide 17.")
add_speech(
    "Dự án sẽ được nghiệm thu chặt chẽ qua 3 mặt:\n"
    "1. Nghiệm thu Kỹ thuật: Phân quyền thông suốt, tính năng Pre-check chạy chuẩn, chống trùng lệnh Idempotency và lưu đủ dấu vết kiểm toán Audit Trail.\n"
    "2. Nghiệm thu Nghiệp vụ: Nhật ký Event Log ghi nhận chuẩn xác mốc thời gian, mã Reason Code áp dụng chuẩn và các chỉ số KPI chứng minh được sự tiến bộ rõ rệt so với trước cải tiến.\n"
    "3. An toàn tuyệt đối: Không phát sinh lỗi hạch toán nghiêm trọng và bảo toàn nguyên tắc bảo mật dữ liệu khách hàng."
)
add_speech(
    "Biên bản nghiệm thu bắt buộc phải có sự đồng thuận ký duyệt của cả 4 bên: Process Owner, Khối Vận hành, Khối Quản trị rủi ro và Khối CNTT."
)

add_speaker_tag("Người 5: Trần Ngọc Dũng", "Slide 18: Kết luận & 4 Ưu tiên hành động", "40 giây")
add_cue("Nhìn thẳng vào Thầy và Hội đồng, giọng truyền cảm, dứt khoát.")
add_speech(
    "Kính thưa Thầy và các anh chị, từ toàn bộ quá trình nghiên cứu, nhóm đúc kết 4 ưu tiên hành động cho LPBank:\n"
    "Một là: Xác lập Process Owner chịu trách nhiệm toàn trình KPI.\n"
    "Hai là: Đưa Pre-check lên đầu luồng để giảm vòng lặp hồ sơ.\n"
    "Ba là: Tích hợp chuẩn hóa và đối soát tự động với Core T24.\n"
    "Và Bốn là: Quản trị dựa trên dữ liệu thực tế bằng chu trình Đo Baseline ➔ Thí điểm Pilot ➔ Đánh giá Before-After."
)
add_speech(
    "Thông điệp cốt lõi mà nhóm em muốn gửi gắm ngày hôm nay là: \"Thành công của quản trị quy trình kinh doanh BPM không nằm ở số lượng chức năng được số hóa trên phần mềm, mà nằm ở hiệu quả vận hành thực chất được chứng minh bằng dữ liệu, đồng thời luôn giữ vững tính an toàn và kiểm soát rủi ro của ngân hàng.\""
)

add_speaker_tag("Người 5: Trần Ngọc Dũng", "Slide 19: Tài liệu tham khảo & Lời cảm ơn", "30 giây")
add_cue("Cúi đầu nhẹ chào Thầy và cả lớp.")
add_speech(
    "Bài nghiên cứu của nhóm được xây dựng dựa trên đề bài môn học, chuẩn APQC Banking PCF 7.2.2 và các tài liệu mô tả quy trình của LPBank. Các chỉ số KPI và giải pháp là đề xuất học thuật của nhóm phục vụ môn học."
)
add_speech(
    "Đại diện nhóm, em xin trân trọng cảm ơn Thầy TS. Phan Thanh Đức đã tận tình giảng dạy và hướng dẫn, cảm ơn các anh chị học viên đã chú ý lắng nghe. Nhóm rất mong nhận được những câu hỏi chất vấn và góp ý từ Thầy và cả lớp ạ. Em xin trân trọng cảm ơn!"
)

# -------------------------------------------------------------
# PHẦN Q&A PHẢN BIỆN
# -------------------------------------------------------------
add_heading_1("BỘ CÂU HỎI PHẢN BIỆN CHẤT VẤN KINH ĐIỂN CỦA GIẢNG VIÊN & CÂU TRẢ LỜI MẪU")
p_qa_intro = doc.add_paragraph()
r_qi = p_qa_intro.add_run(
    "Dưới đây là 9 câu hỏi bẫy thường gặp nhất từ Giảng viên hướng dẫn (TS. Phan Thanh Đức) và Hội đồng bảo vệ môn BPM. "
    "Mỗi câu hỏi đều được phân tích rõ 'ý đồ bắt bẻ của Thầy', 'câu trả lời chuẩn mực lấy điểm tối đa' và 'mẹo ứng biến thực tế'."
)
set_run_font(r_qi, size_pt=10.5, italic=True, color=C_MUTED)

add_qa_item(
    1,
    "Tại sao nhóm lại chọn quy trình Giải ngân mà không chọn quy trình Thẩm định phê duyệt – vốn là khâu rủi ro tín dụng lớn nhất của ngân hàng?",
    "Thầy muốn kiểm tra xem nhóm có tư duy chiến lược BPM hay chỉ chọn bừa một quy trình dễ làm. Thầy muốn xem nhóm có hiểu sự khác biệt giữa 'Chính sách tín dụng' và 'Nút thắt vận hành' hay không.",
    "Kính thưa Thầy, nhóm em hoàn toàn đồng ý Thẩm định phê duyệt là khâu kiểm soát rủi ro tín dụng quan trọng nhất. "
    "Tuy nhiên, dưới góc độ Quản trị quy trình nghiệp vụ (BPM), thẩm định chủ yếu phụ thuộc vào mô hình chấm điểm (Credit Scoring) và khẩu vị rủi ro của ngân hàng. "
    "Trong khi đó, khâu Triển khai và Giải ngân là một nút thắt tác nghiệp (Operational Bottleneck) trực tiếp: Đây là nơi khoản vay đã được cấp thẩm quyền duyệt nhưng tiền chưa đến tay khách hàng; "
    "là nơi xảy ra nhiều ma sát nhất giữa Chi nhánh (cán bộ tín dụng RM) và Hội sở (bộ phận hỗ trợ CSU); và là khâu phát sinh lãng phí bàn giao (Handoffs) lớn nhất. "
    "Cải tiến giải ngân sẽ mang lại hiệu quả thấy ngay về trải nghiệm khách hàng và giảm chi phí xử lý món vay mà không làm xáo trộn chính sách tín dụng cốt lõi của ngân hàng ạ.",
    "Nhắc đến con số chấm điểm 4,85 trên Slide 10 để chứng minh nhóm đã cân nhắc bài bản 5 tiêu chí trước khi chọn."
)

add_qa_item(
    2,
    "Khung APQC là tiêu chuẩn của Mỹ, ngân hàng Việt Nam nói riêng và LPBank nói chung có bắt buộc phải làm theo APQC không? Nhóm dùng APQC để làm gì?",
    "Thầy thử xem nhóm có bị 'máy móc hóa lý thuyết' hay không. Nếu nhóm trả lời 'bắt buộc phải tuân thủ APQC' là rớt bẫy ngay lập tức!",
    "Kính thưa Thầy, APQC hoàn toàn không phải là một quy định mang tính bắt buộc tuân thủ pháp lý như các Thông tư của Ngân hàng Nhà nước hay Basel. "
    "APQC bản chất là một bộ khung phân loại chuẩn (Taxonomy & Benchmarking) giúp các tổ chức có một 'ngôn ngữ chung'. "
    "Nhóm sử dụng APQC PCF 7.2.2 vào bài tập này nhằm 3 mục đích:\n"
    "Thứ nhất, để đối chuẩn (Benchmarking) xem quy trình của LPBank đã có đủ các hoạt động cấu thành chuẩn quốc tế hay chưa;\n"
    "Thứ hai, dùng bảng phân loại của APQC để rà soát khoảng trống (Gap Analysis) và tránh việc đặt tên hay thiết kế chức năng trùng lặp;\n"
    "Và thứ ba, sử dụng bộ chỉ số Open Standards Benchmarking của APQC để xây dựng các KPI đo lường hiệu suất khách quan ạ.",
    "Khẳng định rõ: APQC là 'khung tham chiếu đối chuẩn', còn quy trình thực tế phải luôn 'may đo' theo khẩu vị rủi ro và quy định pháp lý của Việt Nam."
)

add_qa_item(
    3,
    "Các điểm nghẽn và số liệu trong bài (như trả hồ sơ nhiều lần, chờ đợi giữa RM và CSU) là số liệu thật nhóm đo tại LPBank hay tự suy đoán?",
    "Thầy kiểm tra tính trung thực khoa học (Epistemic Precision) và liêm chính học thuật của học viên cao học.",
    "Kính thưa Thầy, nhóm em xin báo cáo rất trung thực: Các điểm nghẽn về việc trả hồ sơ bổ sung hay độ trễ bàn giao là những nguy cơ tiềm ẩn được nhóm nhận diện "
    "dựa trên tài liệu mô tả luồng công việc As-Is và các cuộc phỏng vấn nghiệp vụ định tính với cán bộ ngân hàng. "
    "Do giới hạn tiếp cận dữ liệu bảo mật sản xuất của LPBank, nhóm chưa có bộ dữ liệu log chính thức để kết luận tỷ lệ trả hồ sơ chính xác là bao nhiêu phần trăm. "
    "Chính vì vậy, trong lộ trình triển khai ở Slide 16, nhóm đã thiết kế riêng Giai đoạn 0 (Baseline kéo dài 4 tuần) chỉ để đo đạc số liệu thực tế trước khi kết luận và chốt chỉ tiêu chính thức ạ.",
    "Tuyệt đối không 'chém gió' nhận vơ số liệu! Thầy Đức cực kỳ đánh giá cao học viên biết thừa nhận giới hạn dữ liệu và đề xuất phương pháp đo đạc khoa học."
)

add_qa_item(
    4,
    "Quy trình To-Be có 8 bước, nhiều hơn quy trình As-Is 6 bước. Tại sao số bước tăng lên mà nhóm lại dám khẳng định quy trình sẽ nhanh hơn?",
    "Bẫy kinh điển của giảng viên BPM: Đánh đồng 'số lượng bước' với 'thời gian xử lý'!",
    "Kính thưa Thầy, câu hỏi của Thầy rất sắc bén ạ! Nhìn bề ngoài, To-Be có 8 bước so với 6 bước của As-Is, nhưng bản chất vận hành hoàn toàn khác biệt:\n"
    "Trong quy trình cũ 6 bước, khi hồ sơ bị lỗi ở bước 3 hoặc bước 4, nó sẽ bị trả ngược về bước 2 để RM làm lại từ đầu. Vòng lặp 'bóng bàn' (Ping-pong loop) này có thể lặp lại 2–3 lần, "
    "khiến tổng số lần chạm tay thực tế lên tới mười mấy bước và phát sinh thời gian chờ đợi hàng ngày trời.\n"
    "Trong quy trình mới To-Be, các bước 01, 02, 05, 07 và 08 hoàn toàn là CÔNG NGHỆ TỰ ĐỘNG HÓA chạy bằng API và Rule Engine trong vài giây, con người không phải xử lý thủ công. "
    "Bước Pre-check chặn đứng lỗi ngay từ đầu giúp triệt tiêu hoàn toàn các vòng lặp làm lại. Do đó, dù số bước phân rã nhiều hơn để minh bạch trách nhiệm, nhưng tổng thời gian Cycle Time thực tế lại giảm ít nhất 20% ạ.",
    "Dùng từ khóa: 'Phân rã kiểm soát tự động' khác với 'Bước thủ công con người'. To-Be tăng tự động hóa để giảm thời gian chờ (Queue time)."
)

add_qa_item(
    5,
    "Tại sao trong phân tích VA/BVA/NVA, nhóm không bỏ luôn khâu kiểm soát Maker–Checker để duyệt và giải ngân siêu tốc trong 5 phút như các app Fintech?",
    "Thầy kiểm tra xem học viên có hiểu bản chất rủi ro ngân hàng hay bị cuốn theo trào lưu công nghệ viển vông.",
    "Kính thưa Thầy, các ứng dụng Fintech có thể giải ngân tức thì trong vài phút vì họ áp dụng cho các khoản vay tiêu dùng tín chấp giá trị nhỏ (vài triệu đến vài chục triệu đồng) với lãi suất cao bù đắp rủi ro. "
    "Còn đối tượng của LPBank ở đây là Tín dụng Khách hàng cá nhân có giá trị lớn (vay mua nhà, mua xe, kinh doanh hàng trăm triệu đến hàng tỷ đồng), "
    "thường có tài sản bảo đảm và hồ sơ chứng minh mục đích sử dụng vốn phức tạp theo quy định của NHNN. "
    "Theo nguyên lý Lean BPM, bước Maker–Checker thuộc nhóm Business Value-Added (BVA) – tức hoạt động bắt buộc phục vụ quản trị rủi ro và tuân thủ pháp luật. "
    "Mục tiêu của nhóm là loại bỏ lãng phí (NVA) do thủ tục giấy tờ rườm rà, chứ tuyệt đối không đánh đổi kiểm soát tuân thủ để lấy tốc độ ạ.",
    "Nhắc đến nguyên tắc bảo toàn kiểm soát rủi ro pháp lý của Ngân hàng Nhà nước để khẳng định lập trường vững vàng."
)

add_qa_item(
    6,
    "Cơ sở nào để nhóm đề xuất mục tiêu Cycle Time giảm 20% và First-Time-Right tăng 15 điểm phần trăm? Sao không phải là 50% hay 5%?",
    "Thầy kiểm tra tính khả thi và phương pháp luận đặt mục tiêu KPI theo tiêu chuẩn SMART.",
    "Kính thưa Thầy, mức giảm 20% Cycle Time và tăng 15 điểm % FTR được nhóm đề xuất dựa trên hai cơ sở:\n"
    "Thứ nhất là đối chuẩn theo thông lệ Open Standards Benchmarking của APQC đối với các dự án chuyển đổi số quy trình tín dụng ngân hàng bán lẻ khi triển khai Pre-check tự động;\n"
    "Thứ hai, nhóm tính toán dựa trên việc loại bỏ thời gian chết (Queue time) của khâu trả hồ sơ. Hiện nay, một lần trả hồ sơ bổ sung thường làm chậm tiến độ từ 1–2 ngày làm việc. "
    "Nếu tính năng Pre-check chặn được khoảng 60–70% các lỗi hình thức ban đầu, việc giảm 20% tổng thời gian và nâng FTR thêm 15% là ngưỡng mục tiêu vừa thách thức nhưng hoàn toàn khả thi.\n"
    "Tuy nhiên, như nhóm đã nhấn mạnh ở Slide 15, đây là mục tiêu đề xuất ban đầu; con số chính thức sẽ được tinh chỉnh sau khi có số liệu đo đạc Baseline 4 tuần ạ.",
    "Nhấn mạnh lại từ 'Ngưỡng đề xuất' và cam kết đo Baseline để chứng minh tư duy cẩn trọng của người làm quản trị."
)

add_qa_item(
    7,
    "Việc tối ưu quy trình giải ngân này đóng góp cụ thể gì cho việc cải thiện chỉ số CIR (29,15%) của LPBank?",
    "Thầy kiểm tra khả năng kết nối giữa 'Quy trình tác nghiệp' với 'Chỉ số tài chính vĩ mô'.",
    "Kính thưa Thầy, chỉ số CIR phản ánh tỷ lệ chi phí hoạt động trên tổng thu nhập. Việc tối ưu giải ngân tác động tích cực lên cả Tử số và Mẫu số của CIR:\n"
    "• Tác động lên Mẫu số (Thu nhập): Giải ngân nhanh hơn giúp tiền vay đến tay khách hàng sớm hơn, ngân hàng bắt đầu thu lãi sớm hơn và tăng trưởng dư nợ bán lẻ an toàn;\n"
    "• Tác động lên Tử số (Chi phí): Hiện nay, chi phí nhân sự cho việc kiểm tra thủ công, nhập lại dữ liệu và xử lý hồ sơ bị trả lại chiếm tỷ trọng lớn trong chi phí vận hành. "
    "Khi FTR tăng lên và các tác vụ được tự động hóa, năng suất lao động của mỗi RM và kiểm soát viên tăng lên, ngân hàng có thể xử lý quy mô hồ sơ gấp đôi mà không cần tăng tương ứng nhân sự, từ đó giảm chi phí trên mỗi món vay và tối ưu CIR ạ.",
    "Giải thích theo đúng công thức: CIR = Chi phí hoạt động / Tổng thu nhập (Cả tử số giảm và mẫu số tăng)."
)

add_qa_item(
    8,
    "Thuật ngữ 'Idempotency' (khóa chống trùng) trên slide 8 và 14 nghĩa là gì trong thực tế vận hành giữa BPM và T24?",
    "Thầy muốn kiểm tra xem nhóm có thực sự hiểu thuật ngữ công nghệ mình đưa lên slide hay chỉ sao chép lý thuyết.",
    "Kính thưa Thầy, 'Idempotency' là một nguyên lý thiết kế giao dịch cực kỳ quan trọng trong ngân hàng số:\n"
    "Khi hệ thống BPM gửi lệnh giải ngân sang Core Banking T24, nếu chẳng may xảy ra sự cố nghẽn mạng hoặc timeout, BPM sẽ không nhận được phản hồi là T24 đã trừ tiền thành công hay chưa. "
    "Nếu hệ thống tự động bấm 'thử lại' (retry) mà không có khóa Idempotency, Core Banking có thể sẽ hạch toán 2 lần, dẫn đến việc giải ngân tiền vay gấp đôi cho khách hàng – gây rủi ro tài chính cực kỳ nghiêm trọng!\n"
    "Cơ chế Idempotency gán một Mã định danh giao dịch duy nhất (Idempotency Key) cho mỗi lần duyệt vay. Nếu T24 nhận lại đúng mã đó, hệ thống sẽ chỉ trả về kết quả đã hạch toán trước đó chứ không bao giờ thực hiện hạch toán lần thứ hai ạ.",
    "Giải thích bằng ví dụ mất mạng/timeout thực tế – đây là câu trả lời chuẩn dân IT Ngân hàng, Thầy sẽ cực kỳ ấn tượng!"
)

add_qa_item(
    9,
    "Nếu ban lãnh đạo LPBank yêu cầu triển khai ngay lập tức quy trình To-Be này trên toàn quốc trong tháng tới, nhóm có đồng ý không? Vì sao?",
    "Câu hỏi bẫy về quản trị sự thay đổi (Change Management) và quản trị rủi ro triển khai.",
    "Kính thưa Thầy, nếu Ban lãnh đạo yêu cầu như vậy, nhóm em xin phép được can gián và bảo vệ quan điểm triển khai có lộ trình ạ!\n"
    "Bởi vì trong ngân hàng, triển khai quy trình mới liên quan trực tiếp đến dòng tiền và hệ thống Core Banking T24. Nếu nóng vội mở rộng toàn quốc ngay mà chưa qua kiểm chứng, "
    "khi phần mềm phát sinh lỗi hoặc nhân viên chi nhánh chưa thuần thục bảng mã Reason Code, hậu quả sẽ là ách tắc hàng ngàn món vay trên toàn quốc.\n"
    "Đó là lý do nhóm kiên định với lộ trình 4 giai đoạn ở Slide 16: Phải thí điểm (Pilot) tại 3–5 chi nhánh trong 6–8 tuần, đo lường FTR và kiểm soát lỗi đạt chuẩn Quality Gate 1 thì mới được phép mở rộng toàn hệ thống. "
    "Sự an toàn của ngân hàng phải luôn được đặt lên hàng đầu ạ!",
    "Khẳng định tinh thần cẩn trọng và chuẩn mực quản trị rủi ro ngân hàng."
)

# Save document
doc.save("Kich_ban_thuyet_trinh_LPBank_day_du.docx")
print("Successfully generated and saved Kich_ban_thuyet_trinh_LPBank_day_du.docx with integrated glossary!")
