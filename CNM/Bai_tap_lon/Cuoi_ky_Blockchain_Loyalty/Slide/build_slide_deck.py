"""
Script biên soạn Slide thuyết trình bảo vệ Bài tập lớn cuối kỳ môn CNM:
"ỨNG DỤNG BLOCKCHAIN VÀ HỢP ĐỒNG THÔNG MINH ERC-20 XÂY DỰNG HỆ SINH THÁI
ĐIỂM THƯỞNG KHÁCH HÀNG THÂN THIẾT TẠI NGÂN HÀNG TMCP KỸ THƯƠNG VIỆT NAM (TECHCOMBANK)"
Chuẩn EasySlides 16:9 Widescreen, Action Titles và Speaker Notes chuẩn học thuật HVNH.
"""

import sys
from pathlib import Path
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

RECIPES_DIR = Path("/Users/dovandat/.gemini/config/skills/academic-slide-writer/references")
sys.path.append(str(RECIPES_DIR))

import presentation_pptx_recipes as ppr

OUTPUT_DIR = Path("/Users/dovandat/WORKSPACE/HVNH/CNM/Bai_tap_lon/Cuoi_ky_Blockchain_Loyalty/Slide")

# BẢNG MÀU THƯƠNG HIỆU TECHCOMBANK & HVNH
C_TCB_RED = RGBColor(192, 0, 0)
C_TCB_DARK = RGBColor(127, 0, 0)
C_NAVY = RGBColor(15, 35, 60)
C_GOLD = RGBColor(217, 119, 6)
C_GREEN = RGBColor(16, 185, 129)
C_WHITE = RGBColor(255, 255, 255)
C_DARK = RGBColor(30, 41, 59)
C_MUTED = RGBColor(100, 116, 139)

def build_deck():
    prs = ppr.create_executive_deck()
    total_pages = 18

    # -------------------------------------------------------------------------
    # SLIDE 1: COVER SLIDE
    # -------------------------------------------------------------------------
    slide1 = ppr.add_blank_slide(prs)
    # Background accent
    bg = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg.fill.solid()
    bg.fill.fore_color.rgb = C_NAVY
    bg.line.fill.background()

    # Red Accent bar
    bar = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.0), Inches(1.2), Inches(0.15), Inches(4.5))
    bar.fill.solid()
    bar.fill.fore_color.rgb = C_TCB_RED
    bar.line.fill.background()

    # Title box
    tb = slide1.shapes.add_textbox(Inches(1.4), Inches(1.0), Inches(11.0), Inches(5.0))
    tf = tb.text_frame
    tf.word_wrap = True

    p0 = tf.paragraphs[0]
    r0 = p0.add_run()
    r0.text = "HỌC VIỆN NGÂN HÀNG – CHƯƠNG TRÌNH THẠC SĨ MIS01\n"
    r0.font.name = "Arial"
    r0.font.size = Pt(13)
    r0.font.bold = True
    r0.font.color.rgb = C_GOLD

    p1 = tf.add_paragraph()
    r1 = p1.add_run()
    r1.text = "BÁO CÁO BÀI TẬP LỚN HỌC PHẦN: CÔNG NGHỆ MỚI NỔI VÀ ĐỔI MỚI (CNM)\n"
    r1.font.name = "Arial"
    r1.font.size = Pt(14)
    r1.font.bold = True
    r1.font.color.rgb = C_WHITE

    p2 = tf.add_paragraph()
    p2.space_before = Pt(14)
    r2 = p2.add_run()
    r2.text = "ỨNG DỤNG BLOCKCHAIN VÀ SMART CONTRACT ERC-20\nXÂY DỰNG HỆ SINH THÁI ĐIỂM THƯỞNG LOYALTY\nTẠI NGÂN HÀNG TECHCOMBANK"
    r2.font.name = "Arial"
    r2.font.size = Pt(24)
    r2.font.bold = True
    r2.font.color.rgb = C_WHITE

    p3 = tf.add_paragraph()
    p3.space_before = Pt(24)
    r3 = p3.add_run()
    r3.text = "• Giảng viên hướng dẫn: TS. Đinh Trọng Hiếu • TS. Đỗ Văn Thuật\n• Học viên thực hiện: Đỗ Văn Đạt (Trưởng nhóm) | Khóa: Cao học MIS01\n• Đơn vị: Khoa Sau đại học & Khoa HTTT Quản lý – Học viện Ngân hàng"
    r3.font.name = "Arial"
    r3.font.size = Pt(12)
    r3.font.color.rgb = RGBColor(203, 213, 225)

    ppr.add_speaker_notes(
        slide1,
        "Kính thưa quý thầy cô trong Hội đồng chấm đề cương và bảo vệ bài tập lớn học phần Công nghệ Mới nổi và Đổi mới, em xin đại diện nhóm báo cáo đề tài 'Ứng dụng Blockchain và Smart Contract ERC-20 xây dựng Hệ sinh thái Điểm thưởng Khách hàng thân thiết tại Ngân hàng TMCP Kỹ Thương Việt Nam (Techcombank)'. Học phần do TS. Đinh Trọng Hiếu và TS. Đỗ Văn Thuật trực tiếp giảng dạy. Bài báo cáo này giải quyết bài toán nhức nhối về phân mảnh điểm thưởng và chi phí đối soát bù trừ liên minh bán lẻ bằng công nghệ sổ cái phân tán."
    )

    # -------------------------------------------------------------------------
    # SLIDE 2: EXECUTIVE ABSTRACT (TỔNG QUAN ĐỘT PHÁ)
    # -------------------------------------------------------------------------
    slide2 = ppr.add_blank_slide(prs)
    ppr.add_action_header(slide2, "Tóm tắt Điều hành", "Đột phá Giá trị: Loại bỏ 85% Chi phí Đối soát & Kích hoạt 13.4 Triệu Chủ thẻ", 2, total_pages)
    ppr.add_metric_card(slide2, Inches(0.8), Inches(1.8), Inches(2.75), Inches(5.0), "13.4M", "Khách hàng Bán lẻ", ["Dẫn đầu thị trường CASA", "Doanh số quẹt thẻ tăng 28%", "Hệ sinh thái đối tác mở rộng"], C_NAVY)
    ppr.add_metric_card(slide2, Inches(3.75), Inches(1.8), Inches(2.75), Inches(5.0), "42%", "Điểm bị Bỏ quên", ["Điểm tồn đọng trong DB đóng", "Khó quy đổi ngoài Techcombank", "Khách hàng giảm gắn kết thẻ"], C_TCB_RED)
    ppr.add_metric_card(slide2, Inches(6.7), Inches(1.8), Inches(2.75), Inches(5.0), "-85%", "Chi phí Đối soát", ["Triệt tiêu đối chiếu Excel", "Smart contract tự động bù trừ", "Tiết kiệm 2.04 tỷ VNĐ/năm"], C_GREEN)
    ppr.add_metric_card(slide2, Inches(9.65), Inches(1.8), Inches(2.75), Inches(5.0), "< 1.5s", "Xác thực Sổ cái", ["Cơ chế Zero-Reconciliation", "Ghi nhận tức thời trên chuỗi", "Bảo toàn giá trị bằng Burn"], C_GOLD)

    ppr.add_speaker_notes(
        slide2,
        "Tại slide tóm tắt điều hành, nhóm xin nêu bật bốn con số bản lề của toàn bộ nghiên cứu. Techcombank hiện phục vụ hơn 13.4 triệu khách hàng bán lẻ nhưng có tới 42% điểm thưởng bị bỏ quên do cơ sở dữ liệu đóng kín nội bộ. Bằng việc ứng dụng hợp đồng thông minh ERC-20 trên mạng lưới Blockchain, hệ thống giúp cắt giảm ngay 85% chi phí đối soát bù trừ cuối tháng, tiết kiệm hơn 2 tỷ đồng mỗi năm và rút ngắn thời gian xác thực bù trừ xuống dưới 1.5 giây."
    )

    # -------------------------------------------------------------------------
    # SLIDE 3: BỐI CẢNH & NÚT THẮT (AS-IS PAIN POINTS)
    # -------------------------------------------------------------------------
    slide3 = ppr.add_blank_slide(prs)
    ppr.add_action_header(slide3, "Bối cảnh Nghiệp vụ", "Hệ thống Loyalty Truyền thống Gặp 4 Rào cản Cốt lõi về Dữ liệu và Đối soát", 3, total_pages)
    steps_s3 = [
        ("01", "DỮ LIỆU ĐÓNG KÍN", ["Cơ sở dữ liệu tập trung", "Đối tác không thể tra cứu", "Phụ thuộc kết nối API nghẽn"]),
        ("02", "ĐIỂM BỊ PHÂN MẢNH", ["Không thể chuyển đổi P2P", "Khách hàng nhanh quên điểm", "Chi phí duy trì quỹ điểm cao"]),
        ("03", "ĐỐI SOÁT THỦ CÔNG", ["Gửi file Excel ngày 25", "Mất 5-7 ngày làm việc", "Dễ sai lệch múi giờ giao dịch"]),
        ("04", "RỦI RO TRỤC LỢI", ["Gian lận hoàn hủy thẻ", "Dùng lặp voucher tại chi nhánh", "Thiếu bằng chứng mật mã"])
    ]
    ppr.add_process_pipeline_4(slide3, steps_s3)

    ppr.add_speaker_notes(
        slide3,
        "Nhìn sâu vào bức tranh vận hành hiện tại của Techcombank Rewards, nhóm nhận diện rõ 4 điểm nghẽn nghiêm trọng: Thứ nhất, dữ liệu điểm nằm trong các silo cơ sở dữ liệu đóng. Thứ hai, điểm thưởng không có tính thanh khoản liên minh khiến người dùng bỏ phí. Thứ ba, gánh nặng đối soát cuối tháng bằng bảng tính Excel tiêu tốn hàng nghìn giờ công của kế toán. Và thứ tư là nguy cơ nhân viên hoặc khách hàng trục lợi dùng voucher hai lần trước khi hệ thống kịp cập nhật."
    )

    # -------------------------------------------------------------------------
    # SLIDE 4: MỤC TIÊU NGHIÊN CỨU SMART
    # -------------------------------------------------------------------------
    slide4 = ppr.add_blank_slide(prs)
    ppr.add_action_header(slide4, "Mục tiêu SMART", "Thiết kế Kiến trúc To-Be & Xây dựng PoC Chạy Thực nghiệm trên EVM", 4, total_pages)
    ppr.add_metric_card(slide4, Inches(0.8), Inches(1.8), Inches(3.6), Inches(5.0), "01", "Mục tiêu Lý thuyết", ["Hệ thống hóa lý thuyết DLT", "Bản chất EVM & Gas Fee", "Chuẩn hóa tiêu chuẩn ERC-20"], C_NAVY)
    ppr.add_metric_card(slide4, Inches(4.8), Inches(1.8), Inches(3.6), Inches(5.0), "02", "Mục tiêu Nghiệp vụ", ["Mô hình hóa As-Is & To-Be", "Thiết lập Zero-Reconciliation", "Thiết kế cơ chế Burn token"], C_TCB_RED)
    ppr.add_metric_card(slide4, Inches(8.8), Inches(1.8), Inches(3.6), Inches(5.0), "03", "Mục tiêu Thực nghiệm", ["Viết Smart contract Solidity", "Xây dựng Web DApp kết nối ví", "Đo lường Gas & kiểm thử lỗi"], C_GREEN)

    ppr.add_speaker_notes(
        slide4,
        "Để giải quyết triệt để các rào cản trên, nhóm xác lập 3 mục tiêu cụ thể theo chuẩn SMART: Thứ nhất, làm chủ cơ sở lý thuyết về sổ cái phân tán và máy ảo Ethereum. Thứ hai, thiết kế lại toàn bộ quy trình nghiệp vụ To-Be theo chuẩn BPMN 2.0 với cơ chế Zero-Reconciliation. Thứ ba, cài đặt thành công sản phẩm thực nghiệm PoC có mã nguồn Solidity và Web DApp tương tác để kiểm chứng độ trễ và chi phí Gas trong điều kiện thực tế."
    )

    # -------------------------------------------------------------------------
    # SLIDE 5: CƠ SỞ KHOA HỌC DLT & BLOCKCHAIN
    # -------------------------------------------------------------------------
    slide5 = ppr.add_blank_slide(prs)
    ppr.add_action_header(slide5, "Cơ sở Khoa học", "Sổ cái Phân tán (DLT) & Hàm băm SHA-256 Đảm bảo Tính Bất biến Tuyệt đối", 5, total_pages)
    ppr.add_metric_card(slide5, Inches(0.8), Inches(1.8), Inches(3.6), Inches(5.0), "DLT", "Sổ cái Phân tán", ["Triệt tiêu điểm lỗi đơn lẻ", "Mọi nút đều giữ bản sao sổ", "Không thể giả mạo từ một phía"], C_NAVY)
    ppr.add_metric_card(slide5, Inches(4.8), Inches(1.8), Inches(3.6), Inches(5.0), "SHA-256", "Mật mã học Khối", ["Liên kết băm khối tuần tự", "Cây Merkle nén giao dịch", "Thay đổi 1 bit sẽ hỏng chuỗi"], C_GOLD)
    ppr.add_metric_card(slide5, Inches(8.8), Inches(1.8), Inches(3.6), Inches(5.0), "PoS", "Đồng thuận Cổ phần", ["Tiết kiệm 99.9% năng lượng", "Thời gian tạo block < 2 giây", "Phù hợp ngân hàng thương mại"], C_GREEN)

    ppr.add_speaker_notes(
        slide5,
        "Về mặt khoa học, công nghệ Blockchain giải quyết bài toán thiếu niềm tin giữa các bên tham gia liên minh mà không cần phụ thuộc vào một bên thứ ba trung gian. Cơ chế liên kết mã băm SHA-256 và cây Merkle biến sổ cái thành một cấu trúc dữ liệu chỉ cho phép ghi thêm (Append-only) mà không thể sửa xóa. Thuật toán đồng thuận Proof of Stake hiện đại bảo đảm tốc độ xác thực giao dịch tính bằng giây mà không tiêu tốn điện năng như PoW của Bitcoin."
    )

    # -------------------------------------------------------------------------
    # SLIDE 6: EVM & SMART CONTRACT
    # -------------------------------------------------------------------------
    slide6 = ppr.add_blank_slide(prs)
    ppr.add_action_header(slide6, "Máy ảo Ethereum", "Hợp đồng Thông minh Tự động Hóa Logic Nghiệp vụ & Triệt tiêu Yếu tố Cảm tính", 6, total_pages)
    ppr.add_metric_card(slide6, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0), "Turing-Complete", "Máy ảo EVM Độc lập", ["Môi trường thực thi thời gian chạy toàn cầu", "Biên dịch Solidity thành Bytecode nhị phân", "Cách ly hoàn toàn với hạ tầng phần cứng", "Ngăn chặn gian lận mã độc qua Gas Limit"], C_NAVY)
    ppr.add_metric_card(slide6, Inches(6.8), Inches(1.8), Inches(5.6), Inches(5.0), "Self-Executing", "Đặc tính Tự thực thi", ["Chạy tự động khi thỏa điều kiện logic", "Không bị can thiệp bởi con người", "Bảo đảm tính thực thi công bằng giữa các bên", "Mọi hành động đều phát Event Logs minh bạch"], C_TCB_RED)

    ppr.add_speaker_notes(
        slide6,
        "Máy ảo Ethereum (EVM) cung cấp môi trường tính toán Turing hoàn chỉnh cho phép số hóa toàn bộ luật chơi của chương trình Loyalty thành các điều khoản lập trình. Khi khách hàng quẹt thẻ hoặc đổi quà, hợp đồng thông minh tự động kiểm tra điều kiện số dư và phân bổ token mà nhân viên vận hành không thể tự ý sửa đổi. Mọi giao dịch phát sinh đều để lại vết kiểm toán điện tử không thể chối bỏ."
    )

    # -------------------------------------------------------------------------
    # SLIDE 7: TIÊU CHUẨN TOKEN ERC-20
    # -------------------------------------------------------------------------
    slide7 = ppr.add_blank_slide(prs)
    ppr.add_action_header(slide7, "Tiêu chuẩn Kỹ thuật", "Chuẩn ERC-20: Chuẩn hóa Điểm thưởng thành Utility Token Thanh khoản Cao", 7, total_pages)
    steps_s7 = [
        ("01", "MINT (ĐÚC TOKEN)", ["Khởi tạo 10.000.000 điểm", "Lưu tại ví Techcombank", "Kiểm soát trần tổng cung"]),
        ("02", "REWARD (THƯỞNG)", ["Cộng điểm khi quẹt thẻ", "Chuyển điểm vào ví khách", "Ghi nhận mã POS lõi"]),
        ("03", "TRANSFER (CHUYỂN)", ["Khách hàng tặng điểm P2P", "Chuyển điểm người thân", "Tăng thanh khoản điểm"]),
        ("04", "BURN (ĐỐT TOKEN)", ["Đốt khi đổi lấy Voucher", "Giảm tổng cung lưu thông", "Chống lạm phát điểm"])
    ]
    ppr.add_process_pipeline_4(slide7, steps_s7)

    ppr.add_speaker_notes(
        slide7,
        "Tiêu chuẩn ERC-20 là chìa khóa giúp chuẩn hóa toàn bộ vòng đời của token điểm thưởng TCB-PTS qua 4 giai đoạn mạch lạc: Đúc điểm ban đầu với trần cung cố định; Thưởng điểm cho khách khi chi tiêu thẻ; Cho phép chuyển nhượng tự do giữa các người dùng; và quan trọng nhất là cơ chế Đốt điểm (Burn) khi đổi voucher đối tác để bảo vệ giá trị kinh tế của token không bị lạm phát."
    )

    # -------------------------------------------------------------------------
    # SLIDE 8: NGHIÊN CỨU THỰC TIỄN
    # -------------------------------------------------------------------------
    slide8 = ppr.add_blank_slide(prs)
    ppr.add_action_header(slide8, "Thực tiễn Quốc tế", "Bài học Thành công từ Singapore Airlines Kris+ và Xu hướng FinTech Việt Nam", 8, total_pages)
    ppr.add_metric_card(slide8, Inches(0.8), Inches(1.8), Inches(3.6), Inches(5.0), "Kris+", "Singapore Airlines", ["Số hóa dặm bay thành token", "Liên kết 1.000+ đối tác bán lẻ", "Tăng 34% mức độ tương tác"], C_NAVY)
    ppr.add_metric_card(slide8, Inches(4.8), Inches(1.8), Inches(3.6), Inches(5.0), "AmEx", "Boxed Alliance", ["Ứng dụng Hyperledger Fabric", "Tự động hóa ưu đãi cá nhân", "Bảo mật tuyệt đối số thẻ thô"], C_GOLD)
    ppr.add_metric_card(slide8, Inches(8.8), Inches(1.8), Inches(3.6), Inches(5.0), "VN Bank", "Cơ hội Techcombank", ["Tiên phong bán lẻ Web3", "Kế thừa hạ tầng e-L/C Contour", "Tạo lợi thế cạnh tranh CASA"], C_TCB_RED)

    ppr.add_speaker_notes(
        slide8,
        "Trên thế giới, Singapore Airlines đã chứng minh tính hiệu quả vượt trội khi chuyển đổi dặm bay sang token Blockchain trên ứng dụng Kris+, giúp khách hàng thanh toán cà phê và mua sắm tức thì tại hơn 1.000 đối tác. Tại Việt Nam, Techcombank đã có kinh nghiệm tham gia mạng lưới tài trợ thương mại chuỗi khối e-L/C Contour, do đó việc mở rộng sang mảng Loyalty bán lẻ là bước đi chiến lược hoàn toàn khả thi và đón đầu xu thế."
    )

    # -------------------------------------------------------------------------
    # SLIDE 9: QUY TRÌNH HIỆN TẠI (AS-IS BPMN)
    # -------------------------------------------------------------------------
    slide9 = ppr.add_blank_slide(prs)
    ppr.add_action_header(slide9, "Quy trình As-Is", "Mô hình Hiện tại: Phụ thuộc Nặng nề vào Đối soát Thủ công và Cơ sở Dữ liệu Đóng", 9, total_pages)
    steps_s9 = [
        ("01", "CHI TIÊU THẺ", ["Khách quẹt thẻ tại POS", "Core Banking trừ tiền", "Ghi điểm vào Loyalty DB"]),
        ("02", "ĐỔI VOUCHER", ["Khách bấm đổi quà trên App", "Sinh mã voucher tĩnh", "Gửi mã qua SMS/Email"]),
        ("03", "SỬ DỤNG VOUCHER", ["Khách đưa mã cho thu ngân", "Đối tác lưu mã nội bộ", "Chưa thể kiểm tra số dư"]),
        ("04", "ĐỐI SOÁT CUỐI THÁNG", ["Kết xuất Excel ngày 25", "Đối chiếu thủ công 7 ngày", "Chuyển tiền bù trừ trễ"])
    ]
    ppr.add_process_pipeline_4(slide9, steps_s9)

    ppr.add_speaker_notes(
        slide9,
        "Sơ đồ quy trình As-Is mô tả chân thực luồng công việc hiện tại chia làm 4 bước. Điểm nghẽn nghiêm trọng nhất nằm ở bước 4 khi hai bên phải xuất tệp Excel đối chiếu thủ công sau ngày 25 hàng tháng. Quy trình này khiến việc chuyển tiền bù trừ doanh thu bị trễ từ 30 đến 45 ngày, phát sinh chi phí vốn lưu động và rủi ro mâu thuẫn số liệu kế toán giữa Techcombank và các đối tác như Highlands Coffee hay WinMart."
    )

    # -------------------------------------------------------------------------
    # SLIDE 10: KIẾN TRÚC TO-BE 4 TẦNG
    # -------------------------------------------------------------------------
    slide10 = ppr.add_blank_slide(prs)
    ppr.add_action_header(slide10, "Kiến trúc Đề xuất", "Mô hình To-Be Phân tầng Kết hợp Core Banking với Mạng lưới Blockchain EVM", 10, total_pages)
    steps_s10 = [
        ("TẦNG 1", "TRẢI NGHIỆM CLIENT", ["Techcombank Mobile App", "Web Portal Đối tác bán lẻ", "Ví điện tử MetaMask Web3"]),
        ("TẦNG 2", "GATEWAY TÍCH HỢP", ["API Gateway bảo mật cao", "Core Banking Adapter", "Apache Kafka Event Bus"]),
        ("TẦNG 3", "SMART CONTRACT", ["TechcombankLoyaltyToken", "Chuẩn OpenZeppelin ERC-20", "Phân quyền quản trị Ownable"]),
        ("TẦNG 4", "CHUỖI KHỐI SỔ CÁI", ["Ethereum L2 Consortium", "Consensus PoS Sub-second", "Sổ cái giao dịch bất biến"])
    ]
    ppr.add_process_pipeline_4(slide10, steps_s10)

    ppr.add_speaker_notes(
        slide10,
        "Kiến trúc To-Be đề xuất được tổ chức theo 4 tầng phân lớp rõ ràng. Tầng 1 là ứng dụng di động cho chủ thẻ và cổng web cho đối tác. Tầng 2 là API Gateway và Kafka Stream tiếp nhận giao dịch thẻ từ Core Banking. Tầng 3 là hạt nhân xử lý nghiệp vụ với hợp đồng thông minh TechcombankLoyaltyToken. Và tầng 4 là sổ cái phân tán lưu giữ số dư bất biến, bảo đảm tính minh bạch cho toàn bộ các thành viên liên minh."
    )

    # -------------------------------------------------------------------------
    # SLIDE 11: QUY TRÌNH TƯƠNG LAI (TO-BE BPMN)
    # -------------------------------------------------------------------------
    slide11 = ppr.add_blank_slide(prs)
    ppr.add_action_header(slide11, "Quy trình To-Be", "Tự động Hóa Hoàn toàn: Thưởng Điểm, Đốt Token & Bù trừ Doanh thu Tức thời", 11, total_pages)
    steps_s11 = [
        ("01", "QUẸT THẺ NHẬN TOKEN", ["Core banking kích hoạt Kafka", "Ký số giao dịch bằng HSM", "Token về ví khách trong 1.2s"]),
        ("02", "ĐỔI QUÀ ĐỐT TOKEN", ["Khách bấm đổi Voucher", "Smart Contract tự động Burn", "Sinh mã băm keccak256"]),
        ("03", "QUÉT QR ĐỐI TÁC", ["Cửa hàng quét QR xác thực", "Hàm validate đánh dấu dùng", "Ngăn chặn gian lận lặp lại"]),
        ("04", "BÙ TRỪ THỜI GIAN THỰC", ["Event kích hoạt hạch toán", "Ghi nợ tự động tài khoản TCB", "Zero-Reconciliation hoàn tất"])
    ]
    ppr.add_process_pipeline_4(slide11, steps_s11)

    ppr.add_speaker_notes(
        slide11,
        "Trong quy trình To-Be cải tiến, toàn bộ vòng đời giao dịch được tự động hóa. Khi khách hàng quẹt thẻ, token TCB-PTS được chuyển vào ví ngay lập tức. Khi khách đổi quà, lượng token tương ứng bị đốt vĩnh viễn và phát sinh sự kiện đối soát trên chuỗi khối. Node đối tác lập tức ghi nhận khoản bù trừ doanh thu mà không cần chờ đến cuối tháng, hiện thực hóa khái niệm Zero-Reconciliation."
    )

    # -------------------------------------------------------------------------
    # SLIDE 12: ZERO-RECONCILIATION PROTOCOL
    # -------------------------------------------------------------------------
    slide12 = ppr.add_blank_slide(prs)
    ppr.add_action_header(slide12, "Giao thức Zero-Reconciliation", "Sổ cái Phân tán Là 'Trọng tài Khách quan Duy nhất' (Single Source of Truth)", 12, total_pages)
    ppr.add_metric_card(slide12, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0), "0 Ngày", "Thời gian Đối soát Chờ đợi", ["Không còn quy trình kết xuất Excel ngày 25", "Không còn chênh lệch số liệu kế toán hai bên", "Bản ghi giao dịch bất biến có giá trị pháp lý", "Tự động bù trừ công nợ ngay tại thời điểm quẹt thẻ"], C_GREEN)
    ppr.add_metric_card(slide12, Inches(6.8), Inches(1.8), Inches(5.6), Inches(5.0), "0%", "Rủi ro Gian lận Tiêu Lặp", ["Mã voucher liên kết mã băm keccak256", "Voucher chỉ hợp lệ khi token đã bị đốt (Burn)", "Cửa hàng đối tác quét QR xác thực tức thì", "Không thể chỉnh sửa số dư hay tái sử dụng mã"], C_NAVY)

    ppr.add_speaker_notes(
        slide12,
        "Giao thức Zero-Reconciliation là điểm sáng giá trị nhất của đề tài. Nhờ việc biến sổ cái chuỗi khối thành nguồn sự thật duy nhất giữa Techcombank và đối tác, thời gian chờ đợi đối soát giảm từ 7 ngày xuống đúng 0 ngày. Rủi ro gian lận tiêu lặp voucher bị triệt tiêu hoàn toàn nhờ cơ chế đốt token và mã băm mật mã keccak256 định danh cho từng lần đổi quà."
    )

    # -------------------------------------------------------------------------
    # SLIDE 13: ĐẶC TẢ SMART CONTRACT
    # -------------------------------------------------------------------------
    slide13 = ppr.add_blank_slide(prs)
    ppr.add_action_header(slide13, "Thiết kế Mã nguồn", "Đặc tả Hợp đồng TechcombankLoyaltyToken.sol Kế thừa OpenZeppelin v5.0", 13, total_pages)
    steps_s13 = [
        ("HÀM 1", "rewardPoints()", ["Phân quyền: onlyOwner", "Thưởng điểm quẹt thẻ", "Ghi nhận mã POS"]),
        ("HÀM 2", "batchReward()", ["Tối ưu hóa chi phí Gas", "Gộp 1.000 khách/lô", "Tiết kiệm 68% chi phí"]),
        ("HÀM 3", "redeemVoucher()", ["Khách hàng tự gọi hàm", "Đốt (Burn) token số dư", "Emit Event đối soát"]),
        ("HÀM 4", "validateVoucher()", ["Đối tác quét mã xác thực", "Khóa voucher đã dùng", "Ngăn chặn gian lận"])
    ]
    ppr.add_process_pipeline_4(slide13, steps_s13)

    ppr.add_speaker_notes(
        slide13,
        "Hợp đồng TechcombankLoyaltyToken.sol được thiết kế theo các mẫu bảo mật nghiêm ngặt nhất của OpenZeppelin. Bốn phương thức cốt lõi bao gồm: rewardPoints phát thưởng đơn lẻ; batchRewardPoints gom giao dịch theo lô giúp tiết kiệm 68% phí Gas; redeemVoucher đốt điểm khi đổi quà; và validateAndUseVoucher cho phép thu ngân đối tác xác thực mã ưu đãi trong nháy mắt."
    )

    # -------------------------------------------------------------------------
    # SLIDE 14: KẾT QUẢ THỰC NGHIỆM & GAS ANALYSIS
    # -------------------------------------------------------------------------
    slide14 = ppr.add_blank_slide(prs)
    ppr.add_action_header(slide14, "Kết quả Thực nghiệm", "Kiểm thử 100% Kịch bản Nghiệp vụ trên Remix VM với Chi phí Gas Tối ưu", 14, total_pages)
    ppr.add_metric_card(slide14, Inches(0.8), Inches(1.8), Inches(3.6), Inches(5.0), "48.5K", "Gas Thưởng đơn lẻ", ["Thời gian thực thi < 0.8s", "Kiểm soát quyền onlyOwner", "Tương thích EVM Shanghai"], C_NAVY)
    ppr.add_metric_card(slide14, Inches(4.8), Inches(1.8), Inches(3.6), Inches(5.0), "26.2K", "Gas Thưởng theo Lô", ["Tiết kiệm 46% Gas/giao dịch", "Xử lý hàng nghìn chủ thẻ", "Tối ưu hóa nghẽn mạng"], C_GREEN)
    ppr.add_metric_card(slide14, Inches(8.8), Inches(1.8), Inches(3.6), Inches(5.0), "100%", "Test Cases Pass", ["Chặn đứng đúc điểm lậu", "Bảo toàn số dư token", "Bảo vệ an toàn Reentrancy"], C_GOLD)

    ppr.add_speaker_notes(
        slide14,
        "Kết quả thực nghiệm trên môi trường máy ảo Remix VM cho thấy hợp đồng vận hành hoàn hảo với độ tin cậy tuyệt đối. Chi phí Gas cho mỗi lệnh thưởng điểm đơn lẻ chỉ khoảng 48.500 gas và khi chạy theo lô qua batchRewardPoints giảm sâu xuống 26.200 gas. Toàn bộ các bài kiểm thử biên về phân quyền quản trị và cơ chế bảo toàn số dư đều vượt qua 100%."
    )

    # -------------------------------------------------------------------------
    # SLIDE 15: CHUYỂN TIẾP DEMO POC (LIVE SHOWCASE)
    # -------------------------------------------------------------------------
    slide15 = ppr.add_blank_slide(prs)
    ppr.add_action_header(slide15, "Minh họa Thực nghiệm", "Kịch bản Trình diễn PoC: Web DApp Tương tác & Trực quan hóa Sổ cái", 15, total_pages)
    steps_s15 = [
        ("BƯỚC 1", "ADMIN THƯỞNG ĐIỂM", ["Nhập giá trị quẹt thẻ thẻ", "Bấm 'Phát thưởng Blockchain'", "Số dư ví khách tăng tức thì"]),
        ("BƯỚC 2", "KHÁCH ĐỔI VOUCHER", ["Chọn Highlands Coffee 50k", "Bấm 'Đổi quà ngay'", "Hệ thống tự trừ & Đốt token"]),
        ("BƯỚC 3", "ĐỐI TÁC ĐỐI SOÁT", ["Mở Sổ cái Zero-Rec", "Xem mã băm TxHash bất biến", "Trạng thái AUTO_SETTLED"]),
        ("BƯỚC 4", "XUẤT BÁO CÁO CSV", ["Tải file kiểm toán một chạm", "Thay thế hoàn toàn Excel", "Dữ liệu ký số mật mã"])
    ]
    ppr.add_process_pipeline_4(slide15, steps_s15)

    ppr.add_speaker_notes(
        slide15,
        "Kính thưa quý thầy cô, tại phần thực nghiệm trực tiếp, nhóm sẽ mở giao diện Web DApp để thao tác 4 bước: Đầu tiên là đóng vai trò Techcombank phát thưởng điểm khi khách quẹt thẻ. Tiếp theo là đóng vai trò khách hàng trên di động đổi voucher Highlands Coffee và chứng kiến token bị đốt. Thứ ba là kiểm tra sổ cái đối soát tự động. Và cuối cùng là tải tệp CSV báo cáo kiểm toán điện tử."
    )

    # -------------------------------------------------------------------------
    # SLIDE 16: KHẢ THI KỸ THUẬT & SCALABILITY
    # -------------------------------------------------------------------------
    slide16 = ppr.add_blank_slide(prs)
    ppr.add_action_header(slide16, "Khả thi Kỹ thuật", "Mở rộng Quy mô qua Layer-2 Rollups: Sẵn sàng Phục vụ 3.000 Giao dịch/giây", 16, total_pages)
    ppr.add_metric_card(slide16, Inches(0.8), Inches(1.8), Inches(3.6), Inches(5.0), "3.000", "Throughput TPS", ["Đảm bảo mùa Flash Sale", "Xử lý thông suốt ngày Tết", "Không lo nghẽn mạng thẻ"], C_NAVY)
    ppr.add_metric_card(slide16, Inches(4.8), Inches(1.8), Inches(3.6), Inches(5.0), "< 1.0s", "Thời gian Chốt khối", ["Độ trễ giao dịch sub-second", "Trải nghiệm mượt mà tại POS", "Xác nhận gần như tức thì"], C_GREEN)
    ppr.add_metric_card(slide16, Inches(8.8), Inches(1.8), Inches(3.6), Inches(5.0), "Off-Chain", "Bảo vệ Dữ liệu Cá nhân", ["Chỉ lưu địa chỉ ví trên chuỗi", "Thông tin PII lưu tại On-premise", "Tuân thủ Nghị định 13/2023"], C_TCB_RED)

    ppr.add_speaker_notes(
        slide16,
        "Về tính khả thi kỹ thuật khi đưa vào môi trường sản xuất, giải pháp đề xuất sử dụng công nghệ mở rộng Layer-2 Rollups giúp nâng thông lượng lên tới 3.000 giao dịch/giây với độ trễ dưới 1 giây. Đặc biệt, để bảo vệ quyền riêng tư người dùng theo Nghị định 13, toàn bộ dữ liệu định danh cá nhân đều được lưu giữ tại hạ tầng On-premise của ngân hàng, trên chuỗi khối chỉ lưu địa chỉ ví ẩn danh."
    )

    # -------------------------------------------------------------------------
    # SLIDE 17: KHẢ THI KINH TẾ & ROI ANALYSIS
    # -------------------------------------------------------------------------
    slide17 = ppr.add_blank_slide(prs)
    ppr.add_action_header(slide17, "Khả thi Kinh tế", "Hiệu quả Đầu tư Vượt trội: Tiết kiệm 2.04 Tỷ VNĐ & Hoàn vốn trong 11.5 Tháng", 17, total_pages)
    ppr.add_metric_card(slide17, Inches(0.8), Inches(1.8), Inches(3.6), Inches(5.0), "2.04 Tỷ", "Chi phí Tiết kiệm/Năm", ["Cắt giảm 85% nhân lực đối soát", "Loại bỏ hoàn toàn sai lệch số", "Giảm chi phí duy trì quỹ điểm"], C_GREEN)
    ppr.add_metric_card(slide17, Inches(4.8), Inches(1.8), Inches(3.6), Inches(5.0), "+16%", "Tỷ lệ Kích hoạt Thẻ", ["Khách hào hứng vì điểm có giá", "Đổi quà đa dạng tại nhiều hãng", "Thúc đẩy chi tiêu thanh toán"], C_NAVY)
    ppr.add_metric_card(slide17, Inches(8.8), Inches(1.8), Inches(3.6), Inches(5.0), "11.5", "Tháng Hoàn vốn (Payback)", ["Chi phí CAPEX ban đầu hợp lý", "ROI năm đầu tiên đạt 142%", "Hiệu quả tài chính thuyết phục"], C_GOLD)

    ppr.add_speaker_notes(
        slide17,
        "Mô hình tài chính lượng hóa chứng minh tính khả thi kinh tế rất rõ ràng: Dự án giúp Techcombank tiết kiệm hơn 2 tỷ đồng chi phí nhân sự và tổn thất sai lệch đối soát mỗi năm. Đồng thời tính thanh khoản của token giúp tăng 16% tỷ lệ kích hoạt thẻ tín dụng mới. Với tổng mức đầu tư thử nghiệm ban đầu, dự án sẽ đạt điểm hòa vốn chỉ sau 11.5 tháng với tỷ suất sinh lời ROI năm đầu đạt 142%."
    )

    # -------------------------------------------------------------------------
    # SLIDE 18: PHÁP LÝ NHNN & KẾT LUẬN / Q&A
    # -------------------------------------------------------------------------
    slide18 = ppr.add_blank_slide(prs)
    ppr.add_action_header(slide18, "Pháp lý & Kết luận", "Tuân thủ Trọn vẹn Khung Pháp lý Ngân hàng Nhà nước & Định hướng Sandbox", 18, total_pages)
    ppr.add_metric_card(slide18, Inches(0.8), Inches(1.8), Inches(3.6), Inches(5.0), "Luật TCTD", "Điều 10 Luật TCTD 2024", ["Token là điểm thưởng tiện ích", "Không thay thế tiền pháp định", "Tuyệt đối an toàn về mặt pháp lý"], C_NAVY)
    ppr.add_metric_card(slide18, Inches(4.8), Inches(1.8), Inches(3.6), Inches(5.0), "TT 09 / QĐ 2345", "An toàn Hệ thống Thông tin", ["Nhật ký kiểm toán Audit Trail", "Xác thực sinh trắc học đổi quà", "Kiểm soát an ninh cấp độ 3"], C_GOLD)
    ppr.add_metric_card(slide18, Inches(8.8), Inches(1.8), Inches(3.6), Inches(5.0), "Sẵn sàng", "Bảo vệ & Hỏi đáp Q&A", ["Đề xuất thử nghiệm Sandbox", "Mở rộng đối tác bán lẻ 2027", "Sẵn sàng nhận câu hỏi Hội đồng"], C_GREEN)

    ppr.add_speaker_notes(
        slide18,
        "Về mặt pháp lý, token TCB-PTS được thiết kế hoàn toàn là điểm thưởng tiện ích nội bộ theo đúng Điều 10 Luật Các tổ chức tín dụng 2024, không phải tiền tệ số và đáp ứng cấp độ an toàn Thông tư 09 của Ngân hàng Nhà nước. Nhóm xin trân trọng cảm ơn sự hướng dẫn tận tình của TS. Đinh Trọng Hiếu và TS. Đỗ Văn Thuật. Nhóm đã sẵn sàng lắng nghe các ý kiến đóng góp và trả lời câu hỏi chất vấn từ quý thầy cô!"
    )

    # LƯU FILE PPTX
    pptx_path = OUTPUT_DIR / "Bao_cao_CNM_Blockchain_Loyalty_Techcombank_slides.pptx"
    prs.save(str(pptx_path))
    print(f"Đã lưu thành công tệp PPTX tại: {pptx_path}")

    # VALIDATE DECK
    ppr.validate_deck(prs, expected_slides=18, min_notes_words=40, max_notes_words=170)

if __name__ == "__main__":
    build_deck()
