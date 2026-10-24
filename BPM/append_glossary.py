import docx
from docx.shared import Inches, Pt, RGBColor
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

doc = docx.Document("Kich_ban_thuyet_trinh_LPBank_day_du.docx")

C_PRIMARY = RGBColor(0, 51, 102)     # Deep Navy
C_SECONDARY = RGBColor(194, 65, 12)  # Amber / Dark Orange
C_TEXT = RGBColor(30, 41, 59)        # Slate Dark
C_MUTED = RGBColor(100, 116, 139)    # Gray
C_CUE = RGBColor(13, 148, 136)       # Teal
C_ALERT = RGBColor(185, 28, 28)      # Crimson Red

def set_run_font(run, font_name="Times New Roman", size_pt=11.5, bold=False, italic=False, color=C_TEXT):
    run.font.name = font_name
    run.font.size = Pt(size_pt)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = color

def add_heading_1(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(16)
    p.paragraph_format.space_after = Pt(6)
    r = p.add_run(text)
    set_run_font(r, size_pt=14, bold=True, color=C_PRIMARY)
    return p

def add_heading_2(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(4)
    r = p.add_run(text)
    set_run_font(r, size_pt=12.5, bold=True, color=C_SECONDARY)
    return p

def add_term(term, full_name, meaning, example):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(3)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.15
    
    r_t = p.add_run(f"• {term}")
    set_run_font(r_t, size_pt=11.5, bold=True, color=C_PRIMARY)
    
    r_f = p.add_run(f" ({full_name}): ")
    set_run_font(r_f, size_pt=11, bold=True, italic=True, color=C_SECONDARY)
    
    r_m = p.add_run(meaning)
    set_run_font(r_m, size_pt=11, color=C_TEXT)
    
    if example:
        p_ex = doc.add_paragraph()
        p_ex.paragraph_format.space_before = Pt(0)
        p_ex.paragraph_format.space_after = Pt(5)
        r_e1 = p_ex.add_run("   👉 Ví dụ dễ hiểu: ")
        set_run_font(r_e1, size_pt=10.5, bold=True, color=C_CUE)
        r_e2 = p_ex.add_run(example)
        set_run_font(r_e2, size_pt=10.5, italic=True, color=C_TEXT)

add_heading_1("BẢNG GIẢI NGHĨA TOÀN BỘ CÁC TỪ VIẾT TẮT & THUẬT NGỮ CHUYÊN NGÀNH")
p_in = doc.add_paragraph()
r_in = p_in.add_run(
    "Dưới đây là cẩm nang giải nghĩa cực kỳ đơn giản, ngắn gọn và dễ hiểu cho toàn bộ các từ viết tắt xuất hiện trong Slide và Kịch bản thuyết trình, chia theo 5 nhóm nghiệp vụ để người đọc dễ tra cứu."
)
set_run_font(r_in, size_pt=10.5, italic=True, color=C_MUTED)

# Nhóm 1
add_heading_2("1. Nhóm Chức danh & Bộ phận Ngân hàng")
add_term("RM", "Relationship Manager", "Chuyên viên Quản lý Khách hàng (hay Cán bộ tín dụng tại Chi nhánh). Là người trực tiếp gặp gỡ khách hàng, nhận hồ sơ vay và đề xuất giải ngân.", "Anh RM tại phòng giao dịch LPBank nhận sổ đỏ và đơn xin vay của khách để scan lên máy tính.")
add_term("CSU", "Credit Support Unit", "Trung tâm / Bộ phận Hỗ trợ Tín dụng (thường đặt tại Hội sở hoặc trung tâm vùng). Là bộ phận độc lập có nhiệm vụ kiểm tra lại toàn bộ tính pháp lý của hồ sơ, kiểm tra điều kiện giải ngân trước khi cho phép xuất tiền.", "Sau khi chi nhánh duyệt, hồ sơ được đẩy lên CSU Hội sở để các chuyên viên CSU rà soát lại lần cuối.")
add_term("Maker–Checker", "Nguyên tắc 4 mắt (Người lập - Người duyệt)", "Nguyên tắc bắt buộc trong ngân hàng: Một người tạo lệnh (Maker) thì bắt buộc phải có một người khác có thẩm quyền kiểm tra và duyệt lệnh (Checker), không bao giờ để một người tự tung tự tác giải ngân.", "RM lập tờ trình giải ngân (Maker) -> Kiểm soát viên chi nhánh kiểm tra và ký duyệt (Checker).")
add_term("Process Owner", "Chủ sở hữu quy trình", "Một người (hoặc phòng ban) đứng ra chịu trách nhiệm toàn bộ từ đầu đến cuối cho một quy trình, chịu phạt/thưởng theo kết quả của quy trình đó.", "Nếu hồ sơ giải ngân bị trễ, khách hàng kêu ca, Process Owner sẽ là người đứng ra giải trình và tìm cách sửa chữa chứ không được đổ lỗi quanh co giữa RM và CSU.")

# Nhóm 2
add_heading_2("2. Nhóm Phần mềm & Công nghệ Ngân hàng")
add_term("Core Banking T24", "Hệ thống Ngân hàng lõi Temenos T24", "Là 'trái tim' của ngân hàng, phần mềm quản lý toàn bộ tiền, tài khoản, số dư, tính lãi và hạch toán sổ sách.", "Mọi thao tác trừ tiền tài khoản này, cộng tiền tài khoản kia đều phải chạy vào Core T24 để lưu sổ.")
add_term("LOS", "Loan Origination System", "Hệ thống Khởi tạo và Quản lý khoản vay. Nơi RM nhập thông tin khách hàng, chấm điểm tín dụng và theo dõi hồ sơ từ lúc tiếp nhận đến khi phê duyệt.", "Khi khách đến hỏi vay, RM mở LOS lên tạo mã khách hàng và nhập mức thu nhập của họ vào.")
add_term("Smart BPM", "Phần mềm Quản lý Quy trình Nghiệp vụ số của LPBank", "Phần mềm điều phối công việc, giao việc tự động giữa các phòng ban theo luồng quy định.", "BPM giống như người chỉ huy giao thông: Hồ sơ xong ở RM thì tự động chuyển sang màn hình của Kiểm soát viên.")
add_term("ECM", "Enterprise Content Management", "Hệ thống Quản trị Nội dung Doanh nghiệp (Kho lưu trữ chứng từ điện tử).", "Hợp đồng tín dụng, giấy tờ nhà đất sau khi ký được scan và cất vào kho số ECM để sau này dễ tìm kiếm.")
add_term("GenDoc", "Document Generation", "Hệ thống tự động sinh biểu mẫu, hợp đồng giấy tờ từ dữ liệu có sẵn.", "Thay vì RM phải gõ Word từng tờ hợp đồng, GenDoc tự lấy tên, CMND, số tiền vay từ hệ thống điền thẳng vào mẫu in.")
add_term("Pre-check / Rule Engine", "Kiểm tra trước tự động bằng Bộ quy tắc", "Hệ thống phần mềm tự động rà soát hồ sơ theo các điều kiện đặt sẵn trước khi chuyển cho con người xem.", "Hệ thống tự quét: Nếu thiếu chữ ký số hoặc ngày duyệt vay quá 30 ngày, máy tự báo lỗi ngay lập tức mà không cần chờ người xem.")
add_term("Idempotency / Idempotency Key", "Cơ chế khóa chống tạo trùng giao dịch", "Cơ chế đảm bảo một lệnh dù có bị bấm nhiều lần (do lag mạng, timeout) thì hệ thống cũng chỉ thực hiện trừ tiền đúng MỘT lần duy nhất.", "Bấm giải ngân 1 tỷ đồng nhưng mạng chập chờn, máy tự bấm gửi lại 3 lần. Nhờ có khóa Idempotency, tiền chỉ chuyển đi 1 lần chứ không bị chuyển thành 3 tỷ.")
add_term("Event Log", "Nhật ký sự kiện hệ thống", "Dữ liệu máy tính ghi lại chính xác: Ai làm, làm bước nào, vào lúc mấy giờ mấy phút mấy giây.", "Hệ thống ghi: '10:05 RM gửi hồ sơ -> 10:45 Kiểm soát viên mở xem'. Dựa vào đây để biết ai làm nhanh, ai làm chậm.")
add_term("Audit Trail", "Dấu vết kiểm toán", "Lịch sử không thể xóa về mọi chỉnh sửa dữ liệu, phục vụ cho thanh tra, kiểm toán tra soát lại khi có sự cố.", "Kiểm toán xem lại ai đã sửa số tiền vay từ 500 triệu lên 600 triệu vào ngày nào.")

# Nhóm 3
add_heading_2("3. Nhóm Phương pháp luận BPM & Chuẩn APQC")
add_term("BPM", "Business Process Management", "Quản trị Quy trình Nghiệp vụ: Phương pháp khoa học giúp thiết kế, vận hành, đo lường và tối ưu hóa các dòng công việc trong doanh nghiệp.", "Biến các bước làm việc lộn xộn thành một dây chuyền làm việc trơn tru, bài bản.")
add_term("APQC", "American Productivity & Quality Center", "Trung tâm Năng suất & Chất lượng Hoa Kỳ - Tổ chức phi lợi nhuận uy tín toàn cầu lập ra các khung chuẩn về quy trình doanh nghiệp.", "Là tổ chức đưa ra 'bảng cửu chương' về quy trình cho các ngân hàng trên thế giới tham khảo.")
add_term("PCF", "Process Classification Framework", "Khung Phân loại Quy trình của APQC: Danh sách chuẩn hóa tên gọi và mã số của tất cả các hoạt động trong một ngân hàng.", "APQC quy định việc giải ngân tiền vay có mã chuẩn là 13961.")
add_term("As-Is", "Hiện trạng (Như nó đang là)", "Mô tả quy trình thực tế đang chạy ở ngân hàng hiện tại (kèm theo các lỗi và điểm nghẽn của nó).", "Sơ đồ As-Is chỉ ra hồ sơ hiện nay phải qua 6 bước và bị trả đi trả lại nhiều lần.")
add_term("To-Be", "Tương lai (Như nó nên là)", "Mô hình quy trình mới được đề xuất cải tiến để chạy nhanh hơn, ít lỗi hơn.", "Sơ đồ To-Be đề xuất 8 chặng, đưa máy móc vào kiểm tra tự động từ đầu.")
add_term("VA / BVA / NVA", "Phân tích Giá trị theo Lean", "- VA (Value-Added): Việc khách hàng cần và sẵn sàng trả tiền (như nhận được tiền vay).\n- BVA (Business Value-Added): Việc khách không quan tâm nhưng bắt buộc ngân hàng phải làm để kiểm soát rủi ro và tuân thủ luật (như kiểm tra Maker-Checker, công chứng sổ đỏ).\n- NVA (Non-Value-Added): Lãng phí vô ích cần vứt bỏ (như ngồi chờ đợi, gõ đi gõ lại một thông tin, in giấy thừa).", "Cắt bỏ việc gõ lại hồ sơ (NVA), nhưng tuyệt đối phải giữ việc kiểm soát 4 mắt (BVA).")
add_term("RACI", "Ma trận Trách nhiệm", "Bảng phân định rõ trong một bước: Ai làm (R), Ai chịu trách nhiệm cao nhất (A), Ai cần hỏi ý kiến (C), và Ai cần báo kết quả (I).", "Tránh tình trạng 'cha chung không ai khóc', khi có lỗi thì đổ thừa cho nhau.")
add_term("Process Landscape", "Cảnh quan / Bức tranh tổng thể Quy trình", "Sơ đồ một trang giấy thể hiện toàn bộ các quy trình của mảng nghiệp vụ, chia làm 3 nhóm: Quản lý, Cốt lõi và Hỗ trợ.", "Nhìn vào sơ đồ để biết quy trình giải ngân nằm ở vị trí nào trong chuỗi giá trị của ngân hàng.")

# Nhóm 4
add_heading_2("4. Nhóm Chỉ số Đo lường Hiệu suất (KPI) & Tài chính")
add_term("CIR", "Cost-to-Income Ratio", "Tỷ lệ Chi phí trên Thu nhập. Đo xem để kiếm được 100 đồng thu nhập thì ngân hàng phải tốn bao nhiêu đồng chi phí hoạt động. Chỉ số này càng thấp càng chứng tỏ ngân hàng quản lý chi phí tốt.", "CIR của LPBank là 29,15%, nghĩa là kiếm 100 đồng chỉ mất khoảng 29 đồng chi phí vận hành.")
add_term("BSC", "Balanced Scorecard", "Bảng điểm cân bằng: Khung quản trị đánh giá doanh nghiệp qua 4 góc nhìn: Tài chính, Khách hàng, Quy trình nội bộ, và Con người (Học tập & Phát triển).", "Không chỉ chăm chăm nhìn vào mỗi tiền lãi (Tài chính), mà phải xem khách hàng có hài lòng không và quy trình có chuẩn không.")
add_term("Cycle Time E2E", "End-to-End Cycle Time", "Thời gian chu kỳ toàn trình: Tổng thời gian tính từ giây đầu tiên khách nộp hồ sơ giải ngân đến giây cuối cùng khi tiền vào tài khoản.", "Mục tiêu đề xuất giảm 20% Cycle Time: Trước đây mất 10 tiếng thì sau cải tiến chỉ còn 8 tiếng.")
add_term("FTR", "First-Time-Right", "Tỷ lệ làm đúng ngay từ lần đầu: Tỷ lệ hồ sơ được duyệt và chuyển tiền luôn mà không bị trả lại để bổ sung, sửa chữa.", "FTR tăng 15%: Cứ 100 bộ hồ sơ thì có thêm 15 bộ được chạy thông suốt không phải làm lại.")
add_term("SLA", "Service Level Agreement", "Cam kết chất lượng dịch vụ (thường là cam kết về thời gian).", "Quy định cam kết: Hồ sơ giải ngân chuẩn phải được xử lý xong trong vòng 4 giờ làm việc.")
add_term("Rework Rate", "Tỷ lệ làm lại", "Tỷ lệ hồ sơ bị cán bộ kiểm soát trả về do sai sót thông tin, thiếu giấy tờ.", "Rework rate cao nghĩa là nhân viên làm ẩu hoặc quy định không rõ ràng làm tốn công sửa đi sửa lại.")
add_term("Error Rate", "Tỷ lệ lỗi giao dịch", "Tỷ lệ giao dịch phát sinh sự cố kỹ thuật hoặc lỗi hạch toán trên tổng số giao dịch.", "Mục tiêu là Error rate tiến dần về 0 để không gây rủi ro thất thoát tiền.")
add_term("Median / P90", "Trung vị và Phân vị 90", "- Median (Trung vị): Mốc thời gian của hồ sơ nằm ở chính giữa danh sách. Dùng Median chính xác hơn số trung bình vì không bị ảnh hưởng bởi 1–2 hồ sơ cá biệt bị kẹt cả tháng.\n- P90: Mốc thời gian mà 90% hồ sơ hoàn thành nhanh hơn mốc đó.", "Median = 4 giờ (nghĩa là một nửa số hồ sơ xong dưới 4 giờ). P90 = 7 giờ (nghĩa là 90% hồ sơ xong dưới 7 giờ).")
add_term("Quality Gate", "Cổng kiểm soát chất lượng", "Các mốc chốt chặn kiểm tra trong lộ trình dự án: Đạt đủ tiêu chuẩn thì mới cho làm giai đoạn tiếp theo, không đạt thì phải dừng lại sửa.", "Chỉ khi giai đoạn Pilot ở 3 chi nhánh chạy mượt, không lỗi hạch toán thì mới được qua Gate để mở rộng toàn quốc.")

doc.save("Kich_ban_thuyet_trinh_LPBank_day_du.docx")
print("Glossary successfully appended to Kich_ban_thuyet_trinh_LPBank_day_du.docx")
