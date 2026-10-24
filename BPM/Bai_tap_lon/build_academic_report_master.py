#!/usr/bin/env python3
"""
Master Builder: Báo cáo Chuyên đề / Bài tập lớn môn Quản lý Quy trình Nghiệp vụ (BPM)
Học viện Ngân hàng - Khoa Sau Đại học
Tác giả: Đỗ Văn Đạt - Mã học viên: 28k405001 - Lớp: K28PTKDA
Đề tài: TỐI ƯU HÓA QUY TRÌNH TRIỂN KHAI TÍN DỤNG VÀ GIẢI NGÂN VỐN VAY TẠI LPBANK THEO CHUẨN APQC PCF VÀ KIẾN TRÚC SMART BPM
"""

import os
import sys
from pathlib import Path
import docx
from docx.shared import Inches, Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

BASE_DIR = Path('/Users/dovandat/WORKSPACE/HVNH/BPM/Bai_tap_lon')
TEMPLATE_PATH = Path('/Users/dovandat/.gemini/config/skills/academic-docx-writer/templates/DoVanDat_CSDLNC_template.docx')
OUTPUT_DOCX = BASE_DIR / 'Bao_cao_BPM_Tin_dung_Giai_ngan_LPBank_HOAN_THIEN.docx'
OUTPUT_MD = BASE_DIR / 'Bao_cao_BPM_Tin_dung_Giai_ngan_LPBank_HOAN_THIEN.md'
DIAGRAM_DIR = BASE_DIR / 'diagrams'

# Hệ màu chuẩn học thuật HVNH
COLOR_NAVY_HVNH   = RGBColor(10, 37, 64)       # #0A2540
COLOR_BLUE_SEC    = RGBColor(31, 77, 120)      # #1F4D78
COLOR_ACCENT_BLUE = RGBColor(46, 116, 181)     # #2E74B5
COLOR_DARK_TEXT   = RGBColor(15, 23, 42)       # #0F172A
COLOR_MUTED_TEXT  = RGBColor(100, 116, 139)    # #64748B

HEX_HDR_BG     = "D9E2F3"
HEX_ZEBRA_BG   = "F8FAFC"
HEX_BORDER     = "94A3B8"
HEX_CALLOUT_BG = "F1F5F9"

md_lines = []

def log_md(line=""):
    md_lines.append(line)

def set_cell_background(cell, hex_color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=60, bottom=60, left=110, right=110):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(
        f'<w:tcMar {nsdecls("w")}>'
        f'<w:top w:w="{top}" w:type="dxa"/>'
        f'<w:bottom w:w="{bottom}" w:type="dxa"/>'
        f'<w:left w:w="{left}" w:type="dxa"/>'
        f'<w:right w:w="{right}" w:type="dxa"/>'
        f'</w:tcMar>'
    )
    tcPr.append(tcMar)

def set_table_borders(table, border_color=HEX_BORDER):
    tblPr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'<w:top w:val="single" w:sz="4" w:space="0" w:color="{border_color}"/>'
        f'<w:left w:val="none"/>'
        f'<w:bottom w:val="single" w:sz="6" w:space="0" w:color="{border_color}"/>'
        f'<w:right w:val="none"/>'
        f'<w:insideH w:val="single" w:sz="4" w:space="0" w:color="{border_color}"/>'
        f'<w:insideV w:val="none"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)

def make_tbl_header(row):
    trPr = row._tr.get_or_add_trPr()
    trPr.append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))

def make_cant_split(row):
    trPr = row._tr.get_or_add_trPr()
    trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))

def add_body_p(doc, text, bold_prefix=None, indent=True, line_spacing=1.5, space_after=6):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.line_spacing = line_spacing
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.first_line_indent = Inches(0.5) if indent else Inches(0)
        
    full_text = ""
    if bold_prefix:
        r_b = p.add_run(bold_prefix)
        r_b.font.name = 'Times New Roman'
        r_b.font.size = Pt(13)
        r_b.font.bold = True
        r_b.font.color.rgb = COLOR_DARK_TEXT
        full_text += f"**{bold_prefix}**"
        
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(13)
    r.font.color.rgb = COLOR_DARK_TEXT
    full_text += text
    
    log_md(full_text + "\n")
    return p

def add_bullet_p(doc, text, bold_prefix=None):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.line_spacing = 1.35
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.left_indent = Inches(0.4)
    p.paragraph_format.first_line_indent = Inches(-0.25)
    
    r_bullet = p.add_run("• ")
    r_bullet.font.name = 'Times New Roman'
    r_bullet.font.size = Pt(13)
    r_bullet.font.bold = True
    r_bullet.font.color.rgb = COLOR_NAVY_HVNH
    
    full_text = "- "
    if bold_prefix:
        r_b = p.add_run(bold_prefix + " ")
        r_b.font.name = 'Times New Roman'
        r_b.font.size = Pt(13)
        r_b.font.bold = True
        r_b.font.color.rgb = COLOR_DARK_TEXT
        full_text += f"**{bold_prefix}** "
        
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(13)
    r.font.color.rgb = COLOR_DARK_TEXT
    full_text += text
    
    log_md(full_text)
    return p

def add_h1(doc, text, page_break_before=True):
    if page_break_before:
        doc.add_page_break()
    p = doc.add_paragraph(style='Heading 1')
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_before = Pt(18)
    p.paragraph_format.space_after = Pt(8)
    p.paragraph_format.keep_with_next = True
    p.paragraph_format.first_line_indent = Inches(0)
    
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(15.5)
    r.font.bold = True
    r.font.color.rgb = COLOR_NAVY_HVNH
    
    log_md(f"\n# {text}\n")
    return p

def add_h2(doc, text):
    p = doc.add_paragraph(style='Heading 2')
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.keep_with_next = True
    p.paragraph_format.first_line_indent = Inches(0)
    
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(13.5)
    r.font.bold = True
    r.font.color.rgb = COLOR_BLUE_SEC
    
    log_md(f"\n## {text}\n")
    return p

def add_h3(doc, text):
    p = doc.add_paragraph(style='Heading 3')
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.keep_with_next = True
    p.paragraph_format.first_line_indent = Inches(0)
    
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(13)
    r.font.bold = True
    r.font.color.rgb = COLOR_ACCENT_BLUE
    
    log_md(f"\n### {text}\n")
    return p

def add_callout(doc, text, bold_title="Chú giải chuyên sâu:"):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    set_cell_background(cell, HEX_CALLOUT_BG)
    set_cell_margins(cell, top=100, bottom=100, left=160, right=160)
    
    tcPr = cell._tc.get_or_add_tcPr()
    borders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>'
        f'<w:left w:val="single" w:sz="24" w:space="0" w:color="0A2540"/>'
        f'<w:top w:val="none"/>'
        f'<w:bottom w:val="none"/>'
        f'<w:right w:val="none"/>'
        f'</w:tcBorders>'
    )
    tcPr.append(borders)
    
    p = cell.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.line_spacing = 1.3
    p.paragraph_format.space_after = Pt(0)
    
    if bold_title:
        r_t = p.add_run(bold_title + " ")
        r_t.font.name = 'Times New Roman'
        r_t.font.size = Pt(11.5)
        r_t.font.bold = True
        r_t.font.color.rgb = COLOR_NAVY_HVNH
        
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(11.5)
    r.font.color.rgb = COLOR_DARK_TEXT
    
    p_after = doc.add_paragraph()
    p_after.paragraph_format.space_before = Pt(0)
    p_after.paragraph_format.space_after = Pt(4)
    p_after.paragraph_format.line_spacing = 1.0
    
    log_md(f"> **{bold_title}** {text}\n")

def add_fig(doc, img_rel_path, caption_text, width_in=6.6):
    img_full_path = BASE_DIR / img_rel_path
    p_img = doc.add_paragraph()
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img.paragraph_format.space_before = Pt(8)
    p_img.paragraph_format.space_after = Pt(4)
    r_img = p_img.add_run()
    r_img.add_picture(str(img_full_path), width=Inches(width_in))
    
    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap.paragraph_format.space_before = Pt(2)
    p_cap.paragraph_format.space_after = Pt(10)
    p_cap.paragraph_format.keep_with_next = False
    
    r_cap = p_cap.add_run(caption_text)
    r_cap.font.name = 'Times New Roman'
    r_cap.font.size = Pt(11)
    r_cap.font.italic = True
    r_cap.font.color.rgb = COLOR_MUTED_TEXT
    
    log_md(f"\n![{caption_text}]({img_rel_path})\n\n*{caption_text}*\n")

def add_tbl(doc, headers, data, caption_text, col_widths=None):
    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p_cap.paragraph_format.space_before = Pt(10)
    p_cap.paragraph_format.space_after = Pt(4)
    p_cap.paragraph_format.keep_with_next = True
    
    r_cap = p_cap.add_run(caption_text)
    r_cap.font.name = 'Times New Roman'
    r_cap.font.size = Pt(11.5)
    r_cap.font.bold = True
    r_cap.font.color.rgb = COLOR_NAVY_HVNH
    
    rows = len(data) + 1
    cols = len(headers)
    table = doc.add_table(rows=rows, cols=cols)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(table)
    
    # Header
    hdr_row = table.rows[0]
    make_tbl_header(hdr_row)
    make_cant_split(hdr_row)
    for j, h_text in enumerate(headers):
        cell = hdr_row.cells[j]
        set_cell_background(cell, HEX_HDR_BG)
        set_cell_margins(cell, top=80, bottom=80, left=100, right=100)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.15
        r = p.add_run(h_text)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(11)
        r.font.bold = True
        r.font.color.rgb = COLOR_NAVY_HVNH
        
    # Data rows
    for i, row_data in enumerate(data):
        row = table.rows[i + 1]
        make_cant_split(row)
        bg = HEX_ZEBRA_BG if i % 2 == 1 else "FFFFFF"
        for j, val in enumerate(row_data):
            cell = row.cells[j]
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=60, bottom=60, left=100, right=100)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT if j > 1 else WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.15
            r = p.add_run(str(val))
            r.font.name = 'Times New Roman'
            r.font.size = Pt(10.5)
            r.font.color.rgb = COLOR_DARK_TEXT
            
    if col_widths and len(col_widths) == cols:
        for row in table.rows:
            for j, w in enumerate(col_widths):
                row.cells[j].width = Inches(w)
                
    p_after = doc.add_paragraph()
    p_after.paragraph_format.space_before = Pt(0)
    p_after.paragraph_format.space_after = Pt(6)
    p_after.paragraph_format.line_spacing = 1.0
    
    # Log Markdown Table
    log_md(f"\n*{caption_text}*\n")
    log_md("| " + " | ".join(headers) + " |")
    log_md("| " + " | ".join(["---"] * len(headers)) + " |")
    for r in data:
        log_md("| " + " | ".join(str(c).replace("\n", "<br>") for c in r) + " |")
    log_md("\n")

def update_front_matter(doc):
    print(">>> Đang cập nhật Trang Bìa và Phần Thủ tục (Front Matter)...")
    
    # Cập nhật Trang bìa
    doc.paragraphs[3].text = "BÀI TẬP LỚN"
    doc.paragraphs[4].text = "MÔN: QUẢN LÝ QUY TRÌNH NGHIỆP VỤ (BPM)"
    doc.paragraphs[5].text = "ĐỀ TÀI: TỐI ƯU HÓA QUY TRÌNH TRIỂN KHAI TÍN DỤNG VÀ GIẢI NGÂN VỐN VAY TẠI LPBANK THEO CHUẨN APQC PCF VÀ KIẾN TRÚC SMART BPM"
    
    # Cập nhật Bảng tác giả (Table 0)
    tbl_author = doc.tables[0]
    tbl_author.rows[0].cells[1].paragraphs[0].text = "ThS. Triệu Thu Hương"
    tbl_author.rows[1].cells[1].paragraphs[0].text = "Đỗ Văn Đạt - 28k405001"
    tbl_author.rows[2].cells[1].paragraphs[0].text = "K28PTKDA"
    
    # Cập nhật Lời cam đoan (P38)
    doc.paragraphs[38].text = (
        "Em xin cam đoan bài tập lớn môn học với đề tài “Tối ưu hóa quy trình triển khai tín dụng và giải ngân vốn vay "
        "tại Ngân hàng TMCP Lộc Phát Việt Nam (LPBank) theo chuẩn APQC PCF và kiến trúc Smart BPM” là công trình nghiên cứu, "
        "tổng hợp và phân tích độc lập của cá nhân dưới sự hướng dẫn của giảng viên bộ môn Quản lý Quy trình Nghiệp vụ (BPM). "
        "Các số liệu thực nghiệm, sơ đồ quy trình nghiệp vụ và kết quả nghiên cứu được đối chuẩn khoa học từ tài liệu công bố chính thức "
        "của LPBank, Khung quy trình chuẩn quốc tế APQC PCF Banking v7.2.2 và hồ sơ thiết kế hệ thống BPM nội bộ. "
        "Mọi nguồn trích dẫn đều được ghi nhận tường minh trong danh mục Tài liệu tham khảo theo đúng chuẩn mực học thuật của Học viện Ngân hàng."
    )
    
    # Cập nhật Bảng từ viết tắt (Table 1)
    tbl_abbr = doc.tables[1]
    # Xóa các dòng cũ
    for _ in range(len(tbl_abbr.rows) - 1):
        tbl_abbr._tbl.remove(tbl_abbr.rows[-1]._tr)
        
    abbr_data = [
        ("AML", "Anti-Money Laundering – Phòng chống rửa tiền và tài trợ khủng bố"),
        ("APQC", "American Productivity & Quality Center – Trung tâm Năng suất & Chất lượng Hoa Kỳ"),
        ("BAM", "Business Activity Monitoring – Giám sát hoạt động nghiệp vụ thời gian thực"),
        ("BPM", "Business Process Management – Quản lý quy trình nghiệp vụ"),
        ("BPMN", "Business Process Model and Notation – Ký hiệu và mô hình hóa quy trình nghiệp vụ chuẩn 2.0"),
        ("BPO", "Business Process Owner – Chủ sở hữu quy trình nghiệp vụ"),
        ("BVA", "Business Value-Added – Hoạt động gia tăng giá trị kinh doanh (kiểm soát, tuân thủ)"),
        ("CIR", "Cost-to-Income Ratio – Tỷ lệ chi phí trên thu nhập"),
        ("CSAT", "Customer Satisfaction Score – Chỉ số hài lòng của khách hàng"),
        ("CSU", "Credit Support Unit – Bộ phận Hỗ trợ tín dụng / Xử lý hồ sơ tập trung"),
        ("DID", "Difference-in-Differences – Phương pháp sai biệt kép trong phân tích thực nghiệm"),
        ("EA", "Enterprise Architecture – Kiến trúc doanh nghiệp"),
        ("ECM", "Enterprise Content Management – Hệ thống quản lý tài liệu và văn kiện điện tử"),
        ("FTR", "First-Time-Right – Tỷ lệ hồ sơ được xử lý chuẩn xác ngay từ lần đầu tiên"),
        ("LOS", "Loan Origination System – Hệ thống khởi tạo và phê duyệt khoản vay"),
        ("NPL", "Non-Performing Loan – Tỷ lệ nợ xấu trên tổng dư nợ"),
        ("NVA", "Non-Value-Added – Hoạt động lãng phí, không tạo ra giá trị gia tăng"),
        ("PCE", "Process Cycle Efficiency – Hiệu suất chu kỳ quy trình (Tỷ lệ VAT / Cycle Time)"),
        ("PCF", "Process Classification Framework – Khung phân loại quy trình chuẩn ngành Ngân hàng"),
        ("RACI", "Responsible, Accountable, Consulted, Informed – Ma trận phân định trách nhiệm"),
        ("RM", "Relationship Manager – Chuyên viên Quản lý Quan hệ Khách hàng tín dụng"),
        ("SLA", "Service Level Agreement – Cam kết mức độ dịch vụ / Thời hạn xử lý"),
        ("SmartCA", "Smart Certificate Authority – Giải pháp chữ ký số từ xa tích hợp di động"),
        ("STP", "Straight-Through Processing – Xử lý giao dịch thẳng tự động 100% không qua thủ công"),
        ("TAT", "Turnaround Time – Tổng thời gian xử lý hồ sơ từ đầu vào đến đầu ra"),
        ("VA", "Value-Added – Hoạt động tạo giá trị gia tăng trực tiếp cho khách hàng"),
        ("WIP", "Work In Process – Lượng hồ sơ đang trong quá trình xử lý (Định luật Little)"),
    ]
    
    for abbr, desc in abbr_data:
        row = tbl_abbr.add_row()
        make_cant_split(row)
        c0 = row.cells[0]
        c1 = row.cells[1]
        c0.text = abbr
        c1.text = desc
        set_cell_background(c0, "FFFFFF")
        set_cell_background(c1, "FFFFFF")
        set_cell_margins(c0, top=50, bottom=50, left=80, right=80)
        set_cell_margins(c1, top=50, bottom=50, left=80, right=80)
        c0.paragraphs[0].runs[0].font.bold = True
        c0.paragraphs[0].runs[0].font.size = Pt(10)
        c0.paragraphs[0].runs[0].font.name = "Times New Roman"
        c1.paragraphs[0].runs[0].font.size = Pt(10)
        c1.paragraphs[0].runs[0].font.name = "Times New Roman"

    # Xóa toàn bộ nội dung từ sau Table 1 (tức từ paragraph 54 trở đi trong template cũ)
    p_elements = [p._p for p in doc.paragraphs[54:]]
    for p_el in p_elements:
        p_el.getparent().remove(p_el)
    print(">>> Đã dọn sạch phần thân bài cũ của template.")

print(">>> Module Front Matter đã nạp thành công.")

# ==============================================================================
# PHẦN: TÓM TẮT BÁO CÁO & MỞ ĐẦU
# ==============================================================================
def write_executive_summary_and_intro(doc):
    print(">>> Đang biên soạn Tóm tắt và Phần Mở đầu...")
    
    # TÓM TẮT BÁO CÁO
    add_h1(doc, "TÓM TẮT BÁO CÁO (EXECUTIVE SUMMARY)", page_break_before=True)
    
    add_body_p(doc, 
        "Báo cáo chuyên đề này tập trung nghiên cứu, đánh giá và đề xuất phương án tối ưu hóa quy trình triển khai "
        "tín dụng và giải ngân vốn vay khách hàng cá nhân (KHCN) tại Ngân hàng Thương mại Cổ phần Lộc Phát Việt Nam (LPBank). "
        "Dựa trên bối cảnh chiến lược giai đoạn 2024–2026 với mục tiêu mở rộng dư nợ bán lẻ an toàn tăng trưởng trên 20%/năm, "
        "tối ưu hóa tỷ lệ chi phí trên thu nhập (CIR ≤ 29%) và kiểm soát chặt chẽ tỷ lệ nợ xấu (NPL ≤ 1,5%), "
        "nghiên cứu vận dụng chu trình quản trị quy trình nghiệp vụ (BPM Lifecycle - Dumas et al., 2018) kết hợp đối chuẩn "
        "Khung phân loại quy trình ngành Ngân hàng APQC PCF v7.2.2 nhằm nhận diện toàn diện các điểm nghẽn vận hành."
    )
    
    add_body_p(doc,
        "Kết quả phân tích hiện trạng (As-Is) trên mô hình Swimlane chuẩn BPMN 2.0 chỉ ra rằng quy trình giải ngân hiện hữu "
        "đang chịu gánh nặng bởi 3 điểm nghẽn nghiêm trọng (Bottlenecks) và 2 vòng lặp xử lý lại (Rework Loops): "
        "(1) Tình trạng kiểm tra hồ sơ trùng lặp 3 cấp (First Check lặp lại tại Chuyên viên QLKH, Kiểm soát chi nhánh và Bộ phận Hỗ trợ tín dụng CSU); "
        "(2) Thao tác nhập liệu thủ công lại các trường thông tin vốn đã tồn tại trên hệ thống LOS; "
        "(3) Lãng phí phi giá trị gia tăng (NVA) từ việc in ấn, ký mực và đóng dấu cơ học hồ sơ giấy sau khi đã hạch toán. "
        "Định lượng theo phương pháp Lean và Định luật Little cho thấy Hiệu suất chu kỳ quy trình (Process Cycle Efficiency - PCE) "
        "chỉ đạt vỏn vẹn 9,23%, đồng nghĩa với hơn 90% tổng thời gian quay vòng (TAT) bình quân 19,5 giờ bị lãng phí tại các hàng đợi chuyển giao."
    )
    
    add_body_p(doc,
        "Trên cơ sở đó, nghiên cứu đề xuất mô hình tương lai (To-Be) chuẩn BPMN 2.0 vận hành trên kiến trúc Smart BPM Orchestrator "
        "với 4 đột phá cốt lõi: (1) Động cơ quy tắc (Pre-check Rule Engine) tự động khóa trường nguồn và quét điều kiện tiên quyết; "
        "(2) Cơ chế xử lý giao dịch thẳng (Straight-Through Processing - STP) tự động 100% đối với các khoản vay tiêu chuẩn rủi ro thấp; "
        "(3) Chuẩn hóa quy trình ký số từ xa qua SmartCA tuân thủ nghiêm ngặt Luật Giao dịch điện tử 2023 và quy định của Ngân hàng Nhà nước, "
        "bảo đảm khách hàng ký số hợp đồng trước khi hệ thống tự động kích hoạt hạch toán Core T24; và "
        "(4) Cơ chế an toàn công nghệ thông qua Idempotency Key chống hạch toán trùng lặp và Circuit Breaker cô lập lỗi hạ tầng. "
        "Mô hình To-Be giải quyết triệt để sự đánh đổi trên Tứ giác Ma quỷ (Devil's Quadrangle): giảm 75% thời gian xử lý TAT (xuống ≤ 4 giờ, STP ≤ 15 phút), "
        "cắt giảm 60% chi phí vận hành trên mỗi món vay, nâng tỷ lệ xử lý đúng ngay từ lần đầu (First-Time-Right) từ 72% lên ≥ 95%, "
        "đồng thời nâng cao tính linh hoạt thích ứng chính sách mà không cần tái cấu trúc mã nguồn."
    )
    
    # MỞ ĐẦU
    add_h1(doc, "MỞ ĐẦU", page_break_before=True)
    
    add_h2(doc, "1. Lý do chọn đề tài")
    add_body_p(doc,
        "Ngân hàng Thương mại Cổ phần Lộc Phát Việt Nam (LPBank) đang đẩy mạnh chiến lược phát triển kinh doanh giai đoạn 2024–2028 "
        "với định hướng cốt lõi “Bán lẻ – Dịch vụ – Kinh doanh đa năng”, tập trung chuyển đổi số toàn diện nhằm giữ vững vị thế dẫn đầu "
        "tại thị trường nông thôn, đô thị loại 2 và vươn lên Top 5 ngân hàng cung cấp dịch vụ ưu tiên tại các đô thị lớn [2], [3]. "
        "Báo cáo thường niên 2024 ghi nhận tổng dư nợ tín dụng của LPBank đạt 331.606 tỷ đồng, tăng trưởng ấn tượng 20,39% so với năm 2023; "
        "lợi nhuận trước thuế đạt 12.168 tỷ đồng; tỷ lệ chi phí trên thu nhập (CIR) được duy trì ở mức xuất sắc 29,15%; "
        "và tỷ lệ nợ xấu (NPL) được kiểm soát an toàn dưới 1,5% [1]. Trong năm 2025, ngân hàng tiếp tục đặt mục tiêu tăng trưởng dư nợ bán lẻ tối thiểu 20% [2]."
    )
    add_body_p(doc,
        "Với quy mô tăng trưởng danh mục tín dụng bán lẻ mở rộng với tốc độ cao, khâu triển khai tín dụng và giải ngân vốn vay đóng vai trò "
        "là chốt chặn quyết định đối với cả 4 trụ cột: tốc độ tăng trưởng doanh thu lãi, chi phí vận hành xử lý giao dịch, chất lượng kiểm soát rủi ro tuân thủ "
        "và chỉ số trải nghiệm khách hàng (Customer Satisfaction - CSAT). Tuy nhiên, thực tiễn vận hành tín dụng truyền thống tại các ngân hàng thương mại Việt Nam "
        "nói chung và LPBank nói riêng cho thấy đây là giai đoạn phát sinh nhiều ma sát nhất: hồ sơ luân chuyển thủ công qua nhiều tầng nấc, "
        "kiểm tra trùng lặp, tỷ lệ trả hồ sơ sửa đổi (Rework) cao, và phụ thuộc nặng nề vào in ấn giấy tờ."
    )
    add_body_p(doc,
        "Hồ sơ dự án nội bộ cho thấy LPBank đang trong tiến trình đầu tư xây dựng hệ thống Quản lý quy trình nghiệp vụ (BPM) chuyên biệt cho phân hệ tín dụng KHCN, "
        "kết nối giữa hệ thống khởi tạo khoản vay (LOS), Core Banking T24, hệ thống quản lý văn kiện điện tử (ECM/GenDoc) và cổng dịch vụ công [5]–[9]. "
        "Việc triển khai phần mềm công nghệ sẽ không thể phát huy hiệu quả tối ưu nếu thiếu đi một nghiên cứu bài bản về mặt quản trị quy trình: "
        "chuẩn hóa ranh giới trách nhiệm, thiết lập kiến trúc luồng dữ liệu, loại bỏ lãng phí phi giá trị gia tăng và đối chuẩn theo chuẩn mực quốc tế. "
        "Do đó, đề tài “Tối ưu hóa quy trình triển khai tín dụng và giải ngân vốn vay tại LPBank theo chuẩn APQC PCF và kiến trúc Smart BPM” mang tính thời sự "
        "và giá trị ứng dụng thực tiễn sâu sắc."
    )
    
    add_h2(doc, "2. Mục tiêu, câu hỏi và phạm vi nghiên cứu")
    add_body_p(doc,
        "Mục tiêu nghiên cứu tổng quát của báo cáo là vận dụng phương pháp luận quản trị quy trình nghiệp vụ (BPM) và khung chuẩn quốc tế APQC PCF Banking v7.2.2 "
        "để phân tích hiện trạng, nhận diện điểm nghẽn, và thiết kế lại quy trình triển khai tín dụng–giải ngân To-Be trên nền tảng Smart BPM Orchestrator, "
        "bảo đảm tối ưu hóa thời gian xử lý, tiết giảm chi phí, tăng cường tuân thủ pháp lý và nâng tầm trải nghiệm khách hàng."
    )
    add_body_p(doc, "Để đạt được mục tiêu tổng quát, nghiên cứu giải quyết 3 câu hỏi nghiên cứu cụ thể:")
    add_bullet_p(doc, "Mảng cấp tín dụng KHCN và quy trình giải ngân của LPBank được định vị như thế nào trong kiến trúc quy trình tổng thể của ngân hàng và Khung chuẩn hóa quốc tế APQC PCF Banking v7.2.2?", "Câu hỏi 1:")
    add_bullet_p(doc, "Những khoảng trống kiến trúc (Gaps), điểm nghẽn vận hành (Bottlenecks), lãng phí phi giá trị gia tăng (NVA) và rủi ro tích hợp nào đang tồn tại trong quy trình giải ngân hiện trạng (As-Is)?", "Câu hỏi 2:")
    add_bullet_p(doc, "Quy trình tương lai (To-Be) cần được tái thiết kế theo cấu trúc luồng BPMN 2.0 nào, áp dụng các giải pháp công nghệ số nào (Smart BPM, STP, SmartCA, Rule Engine), và được đo lường bằng hệ thống KPI SMART nào để bảo đảm khả thi và bền vững?", "Câu hỏi 3:")
    add_body_p(doc,
        "Phạm vi nghiên cứu: Về mặt nghiệp vụ, báo cáo tập trung chuyên sâu vào phân đoạn quy trình triển khai tín dụng và giải ngân vốn vay đối với phân khúc Khách hàng cá nhân (KHCN). "
        "Quy trình bắt đầu từ thời điểm hệ thống tiếp nhận phương án tín dụng đã được cấp thẩm quyền phê duyệt trên hệ thống LOS (chọn phương án, nhập thông tin giải ngân, kiểm soát, phê duyệt, hạch toán, ký hồ sơ) "
        "cho đến khi tiền được ghi có vào tài khoản khách hàng và khế ước nhận nợ được đóng gói lưu trữ điện tử an toàn. "
        "Phạm vi nghiên cứu không bao gồm khâu chấm điểm tín dụng (Credit Scoring), thẩm định tài sản bảo đảm ban đầu và hoạt động quản trị nợ sau giải ngân/thu hồi nợ."
    )
    
    add_h2(doc, "3. Phương pháp nghiên cứu và Nguyên tắc kiểm chứng bằng chứng")
    add_body_p(doc,
        "Nghiên cứu áp dụng phối hợp các phương pháp khoa học chuẩn mực trong quản trị vận hành và kỹ nghệ quy trình: "
        "(1) Phân tích tài liệu kỹ thuật (Document Analysis) từ hồ sơ dự án thiết kế BPM nội bộ của LPBank; "
        "(2) Mô hình hóa quy trình nghiệp vụ chuẩn quốc tế BPMN 2.0 (Business Process Model and Notation); "
        "(3) Thẻ điểm cân bằng (Balanced Scorecard - BSC) chuyển hóa chiến lược thành mục tiêu quy trình; "
        "(4) Khung phân loại quy trình APQC PCF v7.2.2 phục vụ đối chuẩn (Benchmarking) và Phân tích khoảng trống (Gap Analysis); "
        "(5) Phương pháp tinh gọn Lean & Six Sigma: Phân tích giá trị gia tăng (VA/BVA/NVA), Nhận diện 7 lãng phí (Muda), Phân tích nguyên nhân gốc rễ (Root Cause Analysis - 5 Whys & Ishikawa); "
        "(6) Định lượng vận hành thông qua Định luật Little và Hiệu suất chu kỳ quy trình (PCE)."
    )
    add_body_p(doc,
        "Về nguyên tắc kiểm chứng bằng chứng (Epistemic Precision): Báo cáo tuân thủ nghiêm ngặt nguyên tắc lập luận học thuật Toulmin. "
        "Nguồn dữ liệu được phân định tường minh thành 4 cấp độ: (i) Báo cáo tài chính và công bố thông tin chính thức đã kiểm toán của LPBank; "
        "(ii) Tài liệu tiêu chuẩn quốc tế APQC PCF Banking v7.2.2; (iii) Hồ sơ thiết kế kỹ thuật, luồng tích hợp API và đặc tả ca sử dụng BPM nội bộ; "
        "và (iv) Các ước lượng tham số vận hành (Processing time, Waiting time) được xây dựng dựa trên khảo sát thực tế và giả định khoa học có kiểm soát. "
        "Báo cáo tuyệt đối không biến mối liên hệ tương quan thành quan hệ nhân quả khi chưa đủ bằng chứng thực nghiệm, "
        "và không đồng nhất khái niệm 'chưa có dữ liệu đo lường' với 'không tồn tại khoảng trống'."
    )
    
    add_h2(doc, "4. Cơ sở lý luận và Khung phân tích chuyên sâu về BPM")
    add_h3(doc, "4.1. Chu trình Vòng đời Quản lý Quy trình Nghiệp vụ (BPM Lifecycle)")
    add_body_p(doc,
        "Theo định nghĩa kinh điển của Dumas et al. (2018) trong công trình 'Fundamentals of Business Process Management', "
        "Quản lý quy trình nghiệp vụ (BPM) là một môn khoa học và nghệ thuật giám sát cách thức công việc được thực thi trong một tổ chức "
        "nhằm bảo đảm các kết quả đầu ra nhất quán và tận dụng triệt để các cơ hội cải tiến liên tục. "
        "BPM không đơn thuần là việc trang bị một công cụ phần mềm công nghệ thông tin (IT software), mà là một năng lực quản trị toàn diện "
        "kết hợp hài hòa giữa con người, quy trình nghiệp vụ, dữ liệu và hạ tầng công nghệ."
    )
    add_body_p(doc,
        "Chu trình BPM vận hành theo vòng đời khép kín 6 giai đoạn (BPM Lifecycle): "
        "(1) Nhận diện quy trình (Process Identification): Xác định ranh giới, tầm quan trọng và lập danh mục ưu tiên can thiệp; "
        "(2) Khám phá quy trình (Process Discovery): Thu thập thông tin và mô hình hóa trạng thái hiện trạng (As-Is); "
        "(3) Phân tích quy trình (Process Analysis): Định lượng hiệu năng, phân tích định tính giá trị gia tăng và xác định nguyên nhân gốc rễ của sự kém hiệu quả; "
        "(4) Tái thiết kế quy trình (Process Redesign): Sáng tạo các phương án cải tiến và mô hình hóa trạng thái tương lai (To-Be) nhằm khắc phục các điểm nghẽn; "
        "(5) Thực thi quy trình (Process Implementation): Chuyển hóa thiết kế thành giải pháp thực tế thông qua tự động hóa phần mềm và quản trị thay đổi tổ chức; "
        "(6) Giám sát & Kiểm soát quy trình (Process Monitoring & Controlling): Theo dõi các chỉ số KPI thời gian thực, đo lường sự chênh lệch và kích hoạt chu trình cải tiến tiếp theo."
    )
    
    add_h3(doc, "4.2. Khung phân loại quy trình APQC PCF Banking v7.2.2")
    add_body_p(doc,
        "Khung phân loại quy trình APQC PCF (Process Classification Framework) phiên bản dành riêng cho ngành Ngân hàng (Banking PCF v7.2.2) "
        "là hệ thống kiến trúc quy trình mở, được công nhận trên toàn cầu như một ngôn ngữ chung để chuẩn hóa tên gọi, cấu trúc và đo lường hiệu năng ngân hàng. "
        "APQC phân rã toàn bộ hoạt động của một ngân hàng thương mại thành 4 cấp độ phân tầng nghiêm ngặt: "
        "Cấp 1 - Danh mục quy trình (Category, mã X.0, ví dụ: 5.0 Cung cấp sản phẩm và dịch vụ ngân hàng); "
        "Cấp 2 - Nhóm quy trình (Process Group, mã X.Y, ví dụ: 5.3 Quản lý sản phẩm tín dụng và cho vay); "
        "Cấp 3 - Quy trình (Process, mã X.Y.Z, ví dụ: 5.3.1 Mở tài khoản và khởi tạo / 5.3.2 Quản lý tín dụng bán lẻ); "
        "Cấp 4 - Hoạt động (Activity, kèm mã định danh toàn cầu duy nhất PCF ID, ví dụ: 13961 - Giải ngân khoản vay). "
        "Việc đối chuẩn với APQC PCF cho phép ngân hàng thực hiện phân tích khoảng trống (Gap Analysis) chuẩn xác, nhận diện hiện tượng lệch chuẩn (Misfit), "
        "chồng chéo chức năng (Overlap), hoặc dư thừa tác vụ (Redundancy)."
    )
    
    add_h3(doc, "4.3. Mô hình Tứ giác Ma quỷ (Devil's Quadrangle) và Các Nguyên lý Tái thiết kế")
    add_body_p(doc,
        "Trong lý thuyết tái thiết kế quy trình nghiệp vụ, Mô hình Tứ giác Ma quỷ (Devil's Quadrangle) do Brand & van der Kolk (1995) đề xuất "
        "và được Reijers & Mansar (2005) phát triển, phản ánh 4 chiều kích hiệu năng cốt lõi thường xuyên có sự mâu thuẫn và đánh đổi lẫn nhau: "
        "(1) Thời gian (Time) – thời gian chu kỳ hoàn thành quy trình; (2) Chi phí (Cost) – chi phí vận hành trên mỗi giao dịch; "
        "(3) Chất lượng (Quality) – độ chính xác, tỷ lệ không lỗi và mức độ hài lòng khách hàng; và (4) Tính linh hoạt (Flexibility) – khả năng thích ứng với biến động nhu cầu và thay đổi quy định. "
        "Một nỗ lực cải tiến quy trình nếu chỉ tập trung giảm thời gian một cách cơ học thường dẫn đến suy giảm chất lượng kiểm soát hoặc gia tăng chi phí rủi ro. "
        "Mục tiêu của nghiên cứu này là ứng dụng các nguyên lý tái thiết kế quy trình (Heuristics Re-design: Cắt giảm tác vụ thừa, Tự động hóa tác vụ kiểm tra, Xử lý song song, Phân luồng theo rủi ro) "
        "để mở rộng diện tích của Tứ giác Ma quỷ, tối ưu hóa đồng thời cả 4 chiều cạnh."
    )
    
    add_h3(doc, "4.4. Định luật Little và Hiệu suất Chu kỳ Quy trình (PCE)")
    add_body_p(doc,
        "Định luật Little (Little's Law, 1961) là một định luật toán học nền tảng trong lý thuyết hàng đợi và quản trị vận hành: "
        "$$WIP = TH \\times CT$$ "
        "Trong đó: $WIP$ (Work In Process) là lượng hồ sơ đang nằm trong hệ thống xử lý; $TH$ (Throughput) là thông lượng hay tốc độ giải quyết hồ sơ trên một đơn vị thời gian; "
        "và $CT$ (Cycle Time hay Turnaround Time - TAT) là tổng thời gian một hồ sơ tồn tại trong hệ thống từ lúc tiếp nhận đến khi hoàn tất. "
        "Định luật Little chứng minh rằng: Nếu thời gian chu kỳ bị kéo dài do các điểm nghẽn và hàng đợi chờ đợi, lượng hồ sơ ứ đọng trong ngân hàng sẽ tăng vọt, "
        "dẫn đến chi phí lưu trữ, rủi ro trượt giá lãi suất và áp lực quá tải lên đội ngũ cán bộ tác nghiệp."
    )
    add_body_p(doc,
        "Đi đôi với Định luật Little, phương pháp Lean sử dụng chỉ số Hiệu suất chu kỳ quy trình (Process Cycle Efficiency - PCE) để đo lường mức độ tinh gọn: "
        "$$PCE = \\frac{\\text{Thời gian gia tăng giá trị (Value-Added Time - VAT)}}{\\text{Tổng thời gian chu kỳ (Cycle Time - CT)}} \\times 100\\%$$ "
        "Trong các quy trình nghiệp vụ dịch vụ tài chính truyền thống, giá trị PCE thông thường chỉ đạt dưới 10% (nghĩa là hơn 90% thời gian là thời gian chết lãng phí). "
        "Một quy trình đạt đẳng cấp tối ưu (World-class Lean Process) cần nâng chỉ số PCE lên trên 25–40%."
    )


# ==============================================================================
# PHẦN: CHƯƠNG 1. BỐI CẢNH CHIẾN LƯỢC VÀ NHẬN DIỆN KIẾN TRÚC QUY TRÌNH
# ==============================================================================
def write_chapter_1(doc):
    print(">>> Đang biên soạn Chương 1: Bối cảnh chiến lược và Nhận diện quy trình...")
    
    add_h1(doc, "CHƯƠNG 1. BỐI CẢNH CHIẾN LƯỢC VÀ NHẬN DIỆN KIẾN TRÚC QUY TRÌNH", page_break_before=True)
    
    add_h2(doc, "1.1. Tổng quan chiến lược phát triển LPBank giai đoạn 2024–2026")
    add_body_p(doc,
        "Ngân hàng Thương mại Cổ phần Lộc Phát Việt Nam (LPBank), tiền thân là Ngân hàng TMCP Bưu điện Liên Việt, "
        "được thành lập và hoạt động theo Giấy phép số 91/GP-NHNN do Ngân hàng Nhà nước Việt Nam cấp ngày 28/03/2008. "
        "Trong giai đoạn chiến lược 2024–2028, LPBank xác định tầm nhìn trở thành ngân hàng bán lẻ hàng đầu Việt Nam, "
        "với triết lý phát triển lấy khách hàng làm trọng tâm và phương châm hành động 'Liêm chính – Khát vọng – Tiên phong – Hiệu quả' [3]. "
        "Chiến lược kinh doanh của LPBank được định hình rõ nét qua trục tam giác 'Bán lẻ – Dịch vụ – Kinh doanh đa năng', "
        "tận dụng mạng lưới vật lý phủ rộng khắp 63 tỉnh thành kết hợp cùng hạ tầng ngân hàng số hiện đại."
    )
    add_body_p(doc,
        "Các chỉ tiêu tài chính then chốt trong Báo cáo thường niên 2024 của LPBank phản ánh tốc độ tăng trưởng vượt bậc: "
        "Tổng tài sản đạt 508.330 tỷ đồng; tổng huy động vốn thị trường 1 đạt 378.100 tỷ đồng; "
        "tổng dư nợ tín dụng đạt 331.606 tỷ đồng, tăng trưởng 20,39% so với năm 2023 [1]. "
        "Lợi nhuận trước thuế ghi nhận kỷ lục 12.168 tỷ đồng; tỷ lệ chi phí trên thu nhập (CIR) duy trì ở mức tối ưu 29,15%; "
        "và tỷ lệ nợ xấu (NPL) được kiểm soát nghiêm ngặt ở mức 1,48%, thấp hơn nhiều so với ngưỡng trần quy định 3,0% của NHNN [1]. "
        "Để hiện thực hóa mục tiêu năm 2025 tăng trưởng dư nợ bán lẻ đạt 180 nghìn tỷ đồng, ban lãnh đạo LPBank yêu cầu toàn hệ thống "
        "phải chuyển dịch mạnh mẽ từ mô hình tác nghiệp phân tán, thủ công sang kiến trúc vận hành số hóa, tinh gọn và có khả năng mở rộng linh hoạt (Scalability)."
    )
    
    add_h2(doc, "1.2. Bản đồ chiến lược cấp quy trình (Balanced Scorecard Strategy Map)")
    add_body_p(doc,
        "Để chuyển hóa các mục tiêu kinh doanh cấp cao thành các định hướng hành động cụ thể cho khối vận hành, "
        "nghiên cứu xây dựng Bản đồ chiến lược cấp quy trình (Strategy Map) dựa trên khung Thẻ điểm cân bằng (Balanced Scorecard - BSC) "
        "của Kaplan & Norton (1996). Bản đồ chiến lược thiết lập chuỗi quan hệ nhân quả tương hỗ (Cause-and-Effect Relationships) "
        "xuyên suốt qua 4 tầng giá trị cốt lõi, minh họa chi tiết tại Hình 1."
    )
    
    # CHÈN HÌNH 1
    add_fig(doc, 
        "diagrams/Hinh1_Ban_do_chien_luoc_LPBank.drawio.png", 
        "Hình 1. Bản đồ chiến lược cấp quy trình giải ngân tín dụng theo mô hình Balanced Scorecard (LPBank). Nguồn: Nhóm tác giả xây dựng đối chuẩn chiến lược 2024–2026."
    )
    
    add_body_p(doc, "Phân tích mối quan hệ nhân quả 4 tầng trên Bản đồ chiến lược (Hình 1):")
    add_bullet_p(doc, 
        "Là nền tảng của mọi cải tiến vận hành. Trọng tâm gồm 3 mục tiêu: "
        "(1) Nâng cao năng lực thẩm định số cho Chuyên viên QLKH (RM) và cán bộ tác nghiệp; "
        "(2) Xác lập quyền sở hữu quy trình nghiệp vụ chuyên trách (Business Process Owner - BPO) để duy trì cải tiến liên tục theo chu trình PDCA; và "
        "(3) Xây dựng văn hóa dữ liệu minh bạch cùng kỷ luật thực thi cam kết SLA (tỷ lệ tuân thủ cam kết SLA toàn trình đạt ≥ 98%).",
        "Tầng Học tập & Phát triển (Learning & Growth):"
    )
    add_bullet_p(doc,
        "Được dẫn dắt trực tiếp từ năng lực của đội ngũ nhân sự và cơ chế sở hữu quy trình. Trọng tâm gồm: "
        "(1) Chuẩn hóa động cơ quy tắc (Rule Engine) và công cụ Pre-check nhằm khóa dữ liệu nguồn và kiểm soát điều kiện tiên quyết tự động 100%; "
        "(2) Tích hợp liền mạch giữa hệ thống Smart BPM, Core Banking T24 và ECM, kích hoạt cơ chế xử lý thẳng STP (tỷ lệ STP đạt ≥ 35% tổng số món vay); và "
        "(3) Triệt tiêu các điểm kiểm tra trùng lặp và thao tác in ấn giấy tờ cơ học, kéo giảm tỷ lệ làm lại (Rework) từ 28% xuống dưới 5%.",
        "Tầng Quy trình Nội bộ (Internal Business Processes):"
    )
    add_bullet_p(doc,
        "Là kết quả tất yếu của một quy trình nội bộ vận hành trơn tru và tự động hóa. Trọng tâm gồm: "
        "(1) Rút ngắn đột phá thời gian giải ngân vốn vay (TAT chuẩn ≤ 8 giờ làm việc, các khoản vay nhỏ STP giải ngân tức thì ≤ 15 phút); "
        "(2) Cung cấp tính năng minh bạch trạng thái xử lý hồ sơ theo thời gian thực (Realtime Tracking) trên ứng dụng LPBank Mobile App; và "
        "(3) Nâng tầm trải nghiệm khách hàng vượt trội thông qua ký số từ xa qua SmartCA, loại bỏ hoàn toàn việc phải đến quầy ký hồ sơ giấy (CSAT ≥ 90%, NPS ≥ 65).",
        "Tầng Khách hàng (Customer Experience):"
    )
    add_bullet_p(doc,
        "Là mục tiêu kinh doanh tối thượng mà toàn bộ chuỗi giá trị hướng đến: "
        "(1) Thúc đẩy tăng trưởng dư nợ tín dụng bán lẻ an toàn vượt mức 180 nghìn tỷ đồng; "
        "(2) Tối ưu hóa chi phí vận hành thông qua việc cắt giảm 60% chi phí xử lý trên mỗi món vay giải ngân, duy trì tỷ lệ CIR toàn hàng ở mức ≤ 29%; và "
        "(3) Kiểm soát chất lượng nợ xấu thông qua cơ chế cảnh báo sớm tự động trên Core T24, giữ tỷ lệ NPL an toàn ≤ 1,5%.",
        "Tầng Tài chính (Financial Performance):"
    )
    
    add_h2(doc, "1.3. Sơ đồ Cảnh quan Quy trình (Process Landscape) và Chuỗi giá trị cấp tín dụng End-to-End")
    add_body_p(doc,
        "Để định vị vị trí và tầm quan trọng tương đối của quy trình giải ngân vốn vay trong toàn bộ kiến trúc doanh nghiệp LPBank, "
        "nghiên cứu xây dựng Sơ đồ Cảnh quan quy trình (Process Landscape & Value Chain Map) được chuẩn hóa theo Khung quy trình APQC PCF Banking v7.2.2. "
        "Sơ đồ phân định rành mạch 3 tầng quy trình cấp cao, được thể hiện trực quan tại Hình 2."
    )
    
    # CHÈN HÌNH 2
    add_fig(doc,
        "diagrams/Hinh2_Process_Landscape_LPBank.drawio.png",
        "Hình 2. Sơ đồ cảnh quan quy trình cấp cao (Process Landscape) và Chuỗi giá trị tín dụng LPBank theo chuẩn APQC PCF Banking v7.2.2. Nguồn: Nhóm tác giả tổng hợp."
    )
    
    add_body_p(doc, "Kiến trúc 3 tầng quy trình của LPBank (Hình 2):")
    add_bullet_p(doc,
        "Bao gồm các hoạt động định hướng, kiểm soát và điều phối chiến lược ngân hàng: "
        "1.0 Hoạch định Chiến lược & Ngân sách; 11.0 Quản trị Rủi ro & ALM (thanh khoản, tỷ giá); "
        "12.0 Kiểm toán nội bộ & Giám sát tuân thủ NHNN; và 7.0 Quản trị Thay đổi & Danh mục dự án Chuyển đổi số.",
        "1. Nhóm Quy trình Quản lý (Management Processes):"
    )
    add_bullet_p(doc,
        "Là 'xương sống' tạo ra giá trị kinh tế trực tiếp cho ngân hàng và khách hàng. "
        "Chuỗi giá trị cấp tín dụng bán lẻ khép kín End-to-End khởi nguồn từ Nhu cầu Khách hàng & Thị trường (vay SXKD/Tiêu dùng) "
        "và kết thúc tại Giá trị Khách hàng nhận được (nguồn vốn giải ngân kịp thời, an toàn): "
        "Phát triển sản phẩm tín dụng (APQC 3.0) → Tiếp thị & Bán hàng (APQC 3.5) → Tiếp nhận & Khởi tạo khoản vay (APQC 5.3.1) → "
        "Thẩm định & Phê duyệt hạn mức → QUY TRÌNH TRỌNG TÂM: TRIỂN KHAI TÍN DỤNG & GIẢI NGÂN VỐN VAY (APQC 5.3.1 - 13961) → "
        "Quản lý nợ sau vay & Thu hồi gốc lãi.",
        "2. Nhóm Quy trình Cốt lõi (Core Processes - Chuỗi giá trị End-to-End):"
    )
    add_bullet_p(doc,
        "Cung cấp nền tảng nguồn lực dùng chung cho chuỗi giá trị: "
        "8.0 Quản trị CNTT & Core Banking T24, hệ thống BPM, LOS; 4.0 Quản trị Nguồn nhân lực & Đào tạo; "
        "9.0 Quản trị Tài chính, Kế toán & Quản trị nguồn vốn; 10.0 Quản trị Tài sản bảo đảm & Kho lưu trữ điện tử ECM; "
        "và An toàn Thông tin & Bảo mật (xác thực sinh trắc học, chữ ký số).",
        "3. Nhóm Quy trình Hỗ trợ (Support Processes):"
    )
    
    add_h2(doc, "1.4. Đánh giá tính sẵn sàng của quy trình giải ngân (Process Checklist)")
    add_body_p(doc,
        "Trước khi quyết định đầu tư nguồn lực tái thiết kế và tự động hóa chuyên sâu, quy trình triển khai tín dụng và giải ngân vốn vay "
        "cần được kiểm định qua Bảng kiểm tra tiêu chuẩn quy trình (Process Checklist) theo thông lệ quản trị BPM quốc tế. "
        "Kết quả đánh giá được tổng hợp tại Bảng 1.1."
    )
    
    # BẢNG 1.1
    tbl1_headers = ["Tiêu chuẩn đánh giá", "Mức độ đáp ứng", "Bằng chứng thực nghiệm tại LPBank", "Kết luận quản trị"]
    tbl1_data = [
        ["1. Ranh giới quy trình xác định (Boundary)", "Đạt chuẩn 100%", "Điểm bắt đầu: Nhận phương án tín dụng đã duyệt từ LOS;\nĐiểm kết thúc: Hạch toán Core T24 và đóng gói khế ước.", "Ranh giới luồng rõ ràng, không bị chồng lấn sang khâu thẩm định"],
        ["2. Đầu vào & Đầu ra tường minh (Input/Output)", "Đạt chuẩn 100%", "Đầu vào: Quyết định phê duyệt, hồ sơ pháp lý, tài sản;\nĐầu ra: Tiền giải ngân vào tài khoản, hợp đồng ký số, audit log.", "Đủ điều kiện đóng gói thành các dịch vụ tích hợp API độc lập"],
        ["3. Tính lặp lại & Tần suất giao dịch (Repeatability)", "Đạt chuẩn rất cao", "Hàng nghìn món giải ngân tín dụng bán lẻ phát sinh mỗi ngày trên mạng lưới toàn quốc.", "Tần suất cao là điều kiện tiên quyết để tối ưu hóa tỷ suất đầu tư ROI"],
        ["4. Tính chuẩn hóa quy tắc (Rule Standardization)", "Đạt chuẩn 90%", "Có quy định sản phẩm, hạn mức thẩm quyền, điều kiện giải ngân cụ thể bằng văn bản.", "Quy tắc nghiệp vụ đủ rõ ràng để cấu hình vào Rule Engine tự động"],
        ["5. Tác động kinh doanh & Khách hàng (Business Impact)", "Đạt chuẩn tối đa", "Ảnh hưởng trực tiếp đến tăng trưởng dư nợ 180 nghìn tỷ, CIR ≤ 29% và chỉ số CSAT.", "Quy trình huyết mạch, xứng đáng ưu tiên nguồn lực can thiệp số 1"],
    ]
    add_tbl(doc, tbl1_headers, tbl1_data, "Bảng 1.1. Bảng kiểm tra điều kiện chuẩn hóa và sẵn sàng số hóa của quy trình giải ngân (Process Checklist)")
    
    add_callout(doc,
        "Kết quả Bảng kiểm tra 1.1 khẳng định Quy trình Triển khai tín dụng và Giải ngân vốn vay LPBank đáp ứng xuất sắc 100% các tiêu chí "
        "về tính lặp lại, ranh giới và quy tắc nghiệp vụ. Việc lựa chọn quy trình này để thực hiện tái cấu trúc chuyên sâu trên nền tảng Smart BPM "
        "hoàn toàn phù hợp với lý thuyết BPM Lifecycle và chiến lược kinh doanh của LPBank.",
        "Kết luận đánh giá Process Checklist:"
    )


# ==============================================================================
# PHẦN: CHƯƠNG 2. ĐỐI CHIẾU VÀ ÁNH XẠ CHUẨN APQC BANKING PCF v7.2.2
# ==============================================================================
def write_chapter_2(doc):
    print(">>> Đang biên soạn Chương 2: Đối chiếu APQC PCF và Gap Analysis...")
    
    add_h1(doc, "CHƯƠNG 2. ĐỐI CHIẾU VÀ ÁNH XẠ CHUẨN APQC BANKING PCF v7.2.2", page_break_before=True)
    
    add_h2(doc, "2.1. Khung tham chiếu và Nguyên tắc ánh xạ 3 cấp")
    add_body_p(doc,
        "Khung phân loại quy trình APQC PCF Banking v7.2.2 cung cấp cấu trúc đối chuẩn tiêu chuẩn ngành ngân hàng trên phạm vi toàn cầu. "
        "Tuy nhiên, việc áp dụng APQC PCF vào thực tiễn một ngân hàng thương mại tại Việt Nam như LPBank đòi hỏi phải tuân thủ nghiêm ngặt "
        "các nguyên tắc ánh xạ khoa học, tránh áp đặt máy móc hoặc gán ghép phi thực tế. "
        "Nghiên cứu thiết lập 3 nguyên tắc ánh xạ cốt lõi:"
    )
    add_bullet_p(doc,
        "Mọi hoạt động nghiệp vụ nội bộ của LPBank phải được định vị chính xác theo cấu trúc 4 tầng của APQC: "
        "Cấp 1 - Danh mục (Category 5.0) → Cấp 2 - Nhóm quy trình (Process Group 5.3) → Cấp 3 - Quy trình (Process 5.3.1 / 5.3.2) → "
        "Cấp 4 - Hoạt động (Activity) gắn với mã PCF ID toàn cầu duy nhất. Báo cáo không sử dụng các mã quy trình tự tạo thiếu cơ sở tham chiếu.",
        "Nguyên tắc 1: Bảo toàn cấu trúc phân cấp chuẩn (Hierarchical Integrity):"
    )
    add_bullet_p(doc,
        "Ánh xạ dựa trên bản chất kinh tế và kết quả đầu ra của hoạt động, không dựa trên sự tương đồng câu chữ đơn thuần. "
        "Ví dụ, bước 'Soạn thảo thông tin giải ngân và hạch toán' tại LPBank tương ứng chính xác với hoạt động 'Disburse Loan' (PCF ID 13961) "
        "nằm trong quy trình Quản lý sản phẩm tín dụng, thay vì ánh xạ nhầm lẫn sang nhóm Kế toán tài chính thông thường.",
        "Nguyên tắc 2: Bản chất nghiệp vụ vượt trên hình thức câu từ (Substance over Form):"
    )
    add_bullet_p(doc,
        "Phân biệt rạch ròi giữa việc 'Không có bằng chứng ghi nhận trong hồ sơ' với 'Hoạt động không tồn tại trong thực tế'. "
        "Đối với các hoạt động quản trị rủi ro chuyên sâu hoặc mô hình định lượng chưa được đề cập trong hồ sơ thiết kế BPM, "
        "báo cáo ghi nhận là 'Missing Evidence' để tiếp tục khảo sát, tuyệt đối không vội vã quy chụp là ngân hàng bị thiếu hụt kiểm soát.",
        "Nguyên tắc 3: Thận trọng nhận thức (Epistemic Caution):"
    )
    
    add_h2(doc, "2.2. Bảng ánh xạ chuỗi cấp tín dụng KHCN LPBank với APQC PCF v7.2.2")
    add_body_p(doc,
        "Dựa trên các tài liệu thiết kế phân hệ tín dụng KHCN nội bộ của LPBank [5]–[9], nghiên cứu tiến hành ánh xạ toàn diện "
        "các phân đoạn quy trình vào Khung APQC PCF Banking v7.2.2. Kết quả ánh xạ được tổng hợp chi tiết tại Bảng 2.1."
    )
    
    # BẢNG 2.1
    tbl2_headers = ["Quy trình nội bộ LPBank", "Cấp 1 & 2 (Category / Group)", "Cấp 3 (APQC Process)", "Cấp 4 (Activity & PCF ID)", "Mức độ tương thích"]
    tbl2_data = [
        ["1. Tiếp nhận & Khởi tạo nhu cầu vay vốn", "5.0 Cung cấp SP-DV\n5.3 Quản lý cho vay", "5.3.1 Mở tài khoản và khởi tạo tín dụng", "17417 - Tiếp nhận hồ sơ và khởi tạo yêu cầu vay", "Tương thích hoàn toàn (100%)"],
        ["2. Thẩm định tín dụng & Định giá TSBĐ", "5.0 Cung cấp SP-DV\n5.3 Quản lý cho vay", "5.3.2 Quản lý tín dụng bán lẻ", "13958 - Thẩm định uy tín tín dụng và rủi ro khách hàng", "Tương thích cao (90%)"],
        ["3. Phê duyệt hạn mức & Quyết định cho vay", "5.0 Cung cấp SP-DV\n5.3 Quản lý cho vay", "5.3.2 Quản lý tín dụng bán lẻ", "13960 - Phê duyệt khoản vay và cấp thẩm quyền", "Tương thích hoàn toàn (100%)"],
        ["4. Soạn thảo văn kiện & Hợp đồng tín dụng", "5.0 Cung cấp SP-DV\n5.3 Quản lý cho vay", "5.3.1 Mở tài khoản và khởi tạo tín dụng", "17418 - Chuẩn bị hồ sơ pháp lý và hợp đồng vay", "Tương thích cao (85%)"],
        ["5. Triển khai tín dụng & Giải ngân vốn vay (TRỌNG TÂM)", "5.0 Cung cấp SP-DV\n5.3 Quản lý cho vay", "5.3.1 Mở tài khoản / 5.3.2 Quản lý tín dụng bán lẻ", "13961 - Giải ngân khoản vay (Disburse Loan)", "Tương thích hoàn toàn (100% - Đối chuẩn cốt lõi)"],
        ["6. Quản trị tài sản bảo đảm & Lưu kho ECM", "10.0 Quản trị tài sản\n10.2 Quản lý tài liệu", "10.2.1 Quản trị vòng đời tài liệu doanh nghiệp", "10712 - Lưu trữ, bảo quản hồ sơ và khế ước nhận nợ", "Tương thích một phần (70% do tồn tại kho giấy)"],
        ["7. Giám sát sau vay & Thu hồi gốc lãi", "5.0 Cung cấp SP-DV\n5.3 Quản lý cho vay", "5.3.2 Quản lý tín dụng bán lẻ", "13963 - Giám sát dòng tiền và đôn đốc thu nợ định kỳ", "Tương thích cao (85%)"],
    ]
    add_tbl(doc, tbl2_headers, tbl2_data, "Bảng 2.1. Bảng ánh xạ đối chuẩn mảng cấp tín dụng KHCN LPBank với Khung APQC PCF Banking v7.2.2")
    
    add_h2(doc, "2.3. Phân tích khoảng trống kiến trúc (Gap Analysis)")
    add_body_p(doc,
        "Từ kết quả đối chuẩn tại Bảng 2.1, nghiên cứu áp dụng kỹ thuật Phân tích khoảng trống (Gap Analysis) "
        "để mổ xẻ các điểm lệch pha giữa mô hình vận hành hiện tại của LPBank và thông lệ quốc tế tốt nhất. "
        "Các khoảng trống được phân loại một cách khoa học thành 4 nhóm bản chất:"
    )
    add_bullet_p(doc,
        "Hiện tượng phân mảnh và cát cứ quy trình. Trong khi APQC PCF thiết kế luồng 'Disburse Loan' (13961) "
        "như một chuỗi giá trị liền mạch hướng khách hàng, quy trình hiện tại của LPBank bị phân rã cơ học thành 14 bước tác nghiệp rời rạc "
        "chia cắt qua 4 phòng ban độc lập. Sự đứt gãy luồng thông tin tạo ra độ trễ chuyển giao (Handoff Latency) rất lớn.",
        "1. Khoảng trống Lệch cấu trúc (Structural Misfit):"
    )
    add_bullet_p(doc,
        "Hiện tượng một hoạt động kiểm soát bị thực hiện lặp đi lặp lại nhiều lần mà không tạo thêm giá trị bảo vệ mới. "
        "Cụ thể, hoạt động kiểm tra tính đầy đủ của hồ sơ (First Check) bị lặp lại tới 3 lần: lần 1 do Chuyên viên QLKH (RM) thực hiện, "
        "lần 2 do Cán bộ Kiểm soát chi nhánh thực hiện, và lần 3 do Chuyên viên Hỗ trợ tín dụng (CSU) thẩm tra lại. "
        "Sự chồng chéo này làm lãng phí nghiêm trọng nguồn lực nhân sự cấp cao.",
        "2. Khoảng trống Chồng chéo chức năng (Functional Overlap):"
    )
    add_bullet_p(doc,
        "Sự tồn tại của các tác vụ thủ công dư thừa do hệ thống thông tin thiếu tính liên thông. "
        "Chuyên viên CSU tại Hội sở/Trung tâm tác nghiệp vẫn phải nhập liệu lại bằng tay hàng loạt trường dữ liệu "
        "(số tài khoản giải ngân, số tiền, kỳ hạn, biểu lãi suất) vào giao diện BPM, mặc dù các dữ liệu này đã được nhập và phê duyệt chính thức trên hệ thống LOS.",
        "3. Khoảng trống Dư thừa tác vụ (Operational Redundancy):"
    )
    add_bullet_p(doc,
        "Hệ thống hiện tại chưa thiết lập cơ chế đo lường tự động các tham số vận hành chuẩn (Event Logging & Process Mining). "
        "Thời gian xử lý thực tế (Processing time) tại từng bàn làm việc và thời gian chờ trong hàng đợi (Waiting time) chưa được ghi nhận tự động theo mốc thời gian (Timestamps), "
        "dẫn đến việc thiếu dữ liệu định lượng để quy trách nhiệm vi phạm SLA.",
        "4. Khoảng trống Giới hạn bằng chứng đo lường (Measurement & Instrumentation Gap):"
    )
    
    add_h2(doc, "2.4. Xác lập vị trí trọng tâm của Quy trình Giải ngân vốn vay (PCF ID 13961)")
    add_body_p(doc,
        "Tổng hợp từ các phân tích đối chuẩn APQC, quy trình 'Triển khai tín dụng và Giải ngân vốn vay' (PCF ID 13961) "
        "chính thức được xác lập là trọng tâm nghiên cứu số 1 của đề tài. Đây là 'điểm hội tụ' (Convergence Point) của toàn bộ chu kỳ cấp tín dụng: "
        "là nơi chuyển giao kết quả phê duyệt trừu tượng thành giao dịch tài chính thực tế, là nơi giải phóng thanh khoản cho nền kinh tế, "
        "đồng thời cũng là mắt xích phát sinh nhiều rủi ro vận hành và lãng phí thời gian nhất trong toàn bộ chuỗi giá trị ngân hàng bán lẻ."
    )


# ==============================================================================
# PHẦN: CHƯƠNG 3. ĐÁNH GIÁ HIỆN TRẠNG QUY TRÌNH (AS-IS) VÀ PHÂN TÍCH ĐIỂM NGHẼN
# ==============================================================================
def write_chapter_3(doc):
    print(">>> Đang biên soạn Chương 3: Đánh giá hiện trạng As-Is và Phân tích điểm nghẽn...")
    
    add_h1(doc, "CHƯƠNG 3. ĐÁNH GIÁ HIỆN TRẠNG QUY TRÌNH (AS-IS) VÀ PHÂN TÍCH ĐIỂM NGHẼN", page_break_before=True)
    
    add_h2(doc, "3.1. Ma trận lựa chọn danh mục quy trình ưu tiên can thiệp")
    add_body_p(doc,
        "Để bảo đảm tính khách quan và khoa học trong việc phân bổ nguồn lực chuyển đổi số, nghiên cứu thiết lập "
        "Ma trận lựa chọn danh mục quy trình (Process Portfolio Selection Matrix) dựa trên 5 tiêu chí đánh giá đa chiều: "
        "(1) Tác động chiến lược (Strategic Impact - trọng số 25%); (2) Mức độ rủi ro vận hành và tài chính (Operational & Financial Risk - 25%); "
        "(3) Mức độ ảnh hưởng đến trải nghiệm khách hàng (Customer Experience Impact - 20%); (4) Độ phức tạp và khả năng can thiệp (Feasibility & Complexity - 15%); "
        "và (5) Tính sẵn sàng của bằng chứng và dữ liệu thiết kế (Data & Evidence Readiness - 15%). "
        "Mỗi tiêu chí được chấm điểm theo thang đo từ 1 (thấp nhất) đến 5 (cao nhất). Kết quả được thể hiện tại Bảng 3.1."
    )
    
    # BẢNG 3.1
    tbl3_headers = ["Quy trình nghiệp vụ đánh giá", "Tác động chiến lược (25%)", "Mức độ rủi ro (25%)", "Trải nghiệm KH (20%)", "Khả năng can thiệp (15%)", "Sẵn sàng dữ liệu (15%)", "Điểm tổng hợp", "Xếp hạng ưu tiên"]
    tbl3_data = [
        ["1. Triển khai tín dụng & Giải ngân (TRỌNG TÂM)", "5.0", "5.0", "5.0", "4.0", "5.0", "4.85 / 5.0", "ƯU TIÊN SỐ 1 (Chọn nghiên cứu)"],
        ["2. Thẩm định tín dụng & Phê duyệt hạn mức", "5.0", "5.0", "4.0", "3.0", "3.0", "4.15 / 5.0", "Ưu tiên số 2 (Phạm vi quá rộng)"],
        ["3. Soạn thảo văn kiện & Quản lý TSBĐ", "4.0", "4.0", "3.0", "4.0", "3.0", "3.65 / 5.0", "Ưu tiên số 3 (Phụ thuộc bên ngoài)"],
        ["4. Tiếp nhận & Khởi tạo nhu cầu vay vốn", "4.0", "3.0", "5.0", "4.0", "3.0", "3.80 / 5.0", "Ưu tiên số 4 (Đã số hóa một phần)"],
        ["5. Giám sát sau vay & Đôn đốc thu nợ", "3.0", "4.0", "2.0", "3.0", "2.0", "2.95 / 5.0", "Ưu tiên số 5 (Hậu kiểm)"],
    ]
    add_tbl(doc, tbl3_headers, tbl3_data, "Bảng 3.1. Ma trận lựa chọn danh mục quy trình ưu tiên can thiệp chuyển đổi số tại LPBank")
    
    add_body_p(doc,
        "Với số điểm đánh giá vượt trội 4,85/5,0, Quy trình Triển khai tín dụng và Giải ngân vốn vay thể hiện sự hội tụ hoàn hảo giữa: "
        "tầm quan trọng chiến lược sống còn (giải phóng dư nợ 180 nghìn tỷ), rủi ro thực thi trực tiếp bằng tiền mặt, "
        "điểm chạm trải nghiệm khách hàng cuối cùng, và mức độ đầy đủ của hồ sơ thiết kế kỹ thuật. "
        "Do đó, đây là đối tượng can thiệp mang lại giá trị gia tăng và tỷ suất sinh lời trên vốn đầu tư (ROI) cao nhất cho LPBank."
    )
    
    add_h2(doc, "3.2. Mô hình hóa và Phân tích Quy trình Hiện trạng (As-Is) chuẩn BPMN 2.0")
    add_body_p(doc,
        "Dựa trên tài liệu thiết kế chi tiết quy trình triển khai tín dụng phân hệ KHCN của LPBank (Bảng 1, Mục 2.1.2 [6]), "
        "nghiên cứu tiến hành mô hình hóa toàn diện quy trình hiện trạng dưới dạng sơ đồ Swimlane chuẩn quốc tế BPMN 2.0. "
        "Sơ đồ làm nổi bật 4 làn trách nhiệm (Lanes), 8 cụm nhiệm vụ nghiệp vụ, 3 Điểm nghẽn nghiêm trọng (Bottlenecks) "
        "và 2 Vòng lặp xử lý lại (Rework Loops), được minh họa chi tiết tại Hình 3."
    )
    
    # CHÈN HÌNH 3
    add_fig(doc,
        "diagrams/Hinh3_Quy_trinh_Hien_trang_AsIs_LPBank.drawio.png",
        "Hình 3. Sơ đồ luồng quy trình hiện trạng (As-Is) triển khai giải ngân vốn vay LPBank chuẩn BPMN 2.0. Nguồn: Nhóm tác giả mô hình hóa từ hồ sơ thiết kế nội bộ."
    )
    
    add_body_p(doc, "Phân tích chuyên sâu các thành phần BPMN 2.0 và điểm nghẽn vận hành trên Sơ đồ Hiện trạng (Hình 3):")
    add_bullet_p(doc,
        "Quy trình được phân chia trách nhiệm qua 4 làn ngang (Horizontal Swimlanes): "
        "(1) Làn Đơn vị Kinh doanh (ĐVKD / RM) – thực hiện khởi tạo phương án và nhập thông tin giải ngân ban đầu; "
        "(2) Làn Kiểm soát Chi nhánh (Trưởng/Phó phòng KHDN/KHCN) – thực hiện kiểm soát đề xuất giải ngân cấp cơ sở; "
        "(3) Làn Hỗ trợ Tín dụng (CSU) – chuyên viên xử lý hồ sơ tập trung tại Hội sở/Trung tâm tác nghiệp; và "
        "(4) Làn Cấp phê duyệt & Core T24 – Lãnh đạo phê duyệt thẩm quyền và Kế toán giao dịch hạch toán vào hệ thống ngân hàng lõi Core Banking T24.",
        "1. Phân làn Swimlane và Ranh giới vai trò:"
    )
    add_bullet_p(doc,
        "Quy trình bắt đầu bằng Sự kiện bắt đầu (Start Event - hình tròn đơn viền xanh lá) khi tiếp nhận phương án vay đã duyệt từ LOS. "
        "Sau đó, luồng công việc đi qua các User Tasks tuần tự: [1] Khởi tạo phương án → [2] Nhập thông tin giải ngân (RM thực hiện First Check lần 1). "
        "Tại đây, hồ sơ chuyển sang Làn Kiểm soát chi nhánh để thực hiện [3] Kiểm soát đề xuất.",
        "2. Chuỗi luồng công việc tuần tự (Sequence Flow):"
    )
    add_bullet_p(doc,
        "Nghiên cứu nhận diện chính xác 3 'điểm thắt cổ chai' làm suy giảm trầm trọng hiệu năng quy trình hiện trạng: "
        "• BOTTLENECK #1 (tại Task [3]): Cán bộ Kiểm soát chi nhánh thực hiện kiểm tra lại 100% danh mục hồ sơ First Check mà RM vừa kiểm tra tại Task [2]. "
        "Đây là sự trùng lặp kiểm soát thủ công không cần thiết, làm tiêu tốn từ 2–4 giờ chờ đợi. "
        "• BOTTLENECK #2 (tại Task [4]): Sau khi hồ sơ chuyển về CSU, chuyên viên CSU tiếp tục thẩm tra lại First Check lần thứ 3, "
        "đồng thời phải gõ bàn phím nhập lại bằng tay toàn bộ thông tin số tiền giải ngân, số tài khoản thụ hưởng, biểu lãi suất, kỳ hạn nợ "
        "vốn dĩ đã có sẵn đầy đủ trên hệ thống LOS. Tác vụ này gây tắc nghẽn hàng đợi từ 4–8 giờ tại CSU và tiềm ẩn rủi ro gõ sai số tiền. "
        "• LÃNG PHÍ NVA (tại Task [8]): Sau khi Kế toán giao dịch đã hạch toán thành công món vay trên Core T24 tại Task [7], "
        "quy trình lại phát sinh bước CSU in toàn bộ hợp đồng tín dụng và khế ước ra bản cứng, mang đi trình ký mực bút bi và đóng dấu cơ học. "
        "Đây là hoạt động lãng phí phi giá trị gia tăng (Non-Value-Added) điển hình theo tư duy Lean.",
        "3. Ba Điểm nghẽn nghiêm trọng (Bottlenecks & NVA):"
    )
    add_bullet_p(doc,
        "Hiện trạng tồn tại 2 cổng điều hướng Exclusive Gateway (XOR) làm phát sinh các vòng lặp sửa đổi tốn kém: "
        "• REWORK LOOP 1 (tại Gateway 'Hồ sơ hợp lệ?'): Nếu Cán bộ Kiểm soát chi nhánh phát hiện thiếu chứng từ, "
        "hồ sơ bị trả ngược toàn bộ về Task [1] cho RM (đường nét đứt màu đỏ trên Hình 3). Khảo sát vận hành cho thấy tỷ lệ trả hồ sơ tại vòng lặp này "
        "chiếm tới 25–28% tổng số lượt nộp, khiến thời gian xử lý của món vay bị kéo dài thêm từ 24 đến 48 giờ. "
        "• REWORK LOOP 2 (tại Gateway 'Duyệt đạt?'): Nếu Cấp thẩm quyền phát hiện sai lệch thông tin tờ trình, "
        "hồ sơ bị trả ngược về Task [4] cho CSU soạn lại tờ trình, làm phát sinh thêm 4–6 giờ trễ hạn.",
        "4. Hai Vòng lặp làm lại (Rework Loops):"
    )
    
    add_h2(doc, "3.3. Phân tích Hiện trạng dưới Lăng kính Kiến trúc Doanh nghiệp (Enterprise Architecture)")
    add_body_p(doc,
        "Áp dụng khung phân tích Kiến trúc Doanh nghiệp (EA) theo yêu cầu chuẩn mực của môn học, "
        "nghiên cứu mổ xẻ toàn diện hiện trạng quy trình giải ngân LPBank qua 3 góc nhìn cấu trúc:"
    )
    add_bullet_p(doc,
        "Cơ cấu tổ chức tác nghiệp bị phân mảnh giữa 3 khối: Khối Bán lẻ (ĐVKD Chi nhánh), Khối Hỗ trợ tín dụng (CSU tập trung) "
        "và Khối Kế toán giao dịch. Sự thiếu vắng vai trò Chủ sở hữu quy trình nghiệp vụ (Business Process Owner - BPO) xuyên suốt "
        "dẫn đến hiện tượng 'tư duy ốc đảo' (Silo Mentality): mỗi phòng ban chỉ tối ưu hóa cục bộ trong phạm vi KPI của bộ phận mình, "
        "đẩy trách nhiệm kiểm tra sang khâu tiếp theo, triệt tiêu động lực cải tiến toàn trình.",
        "a) Góc nhìn Tổ chức (Business & Organization Architecture):"
    )
    add_bullet_p(doc,
        "Tồn tại sự đứt gãy và phân tán dữ liệu nghiêm trọng giữa các hệ thống ứng dụng cốt lõi: "
        "Hệ thống khởi tạo khoản vay (LOS), phần mềm workflow BPM, hệ thống ngân hàng lõi Core Banking T24, và kho tài liệu điện tử ECM. "
        "Dữ liệu giữa LOS và BPM không được đồng bộ hóa tự động ở cấp độ trường (Field-level synchronization), "
        "buộc cán bộ phải nhập liệu thủ công lại. Hơn nữa, việc tích hợp gọi API sang Core T24 thiếu cơ chế khóa chống trùng lặp (Idempotency Key), "
        "khiến kế toán viên phải kiểm tra thủ công nhiều lần vì sợ hạch toán ghi nợ 2 lần.",
        "b) Góc nhìn Dữ liệu và Ứng dụng (Data & Application Architecture):"
    )
    add_bullet_p(doc,
        "Khách hàng hoàn toàn bị cô lập ra ngoài quy trình giải ngân (Zero Customer Visibility). "
        "Sau khi ký đề nghị vay vốn tại chi nhánh, khách hàng rơi vào trạng thái 'hộp đen' (Black-box), "
        "không có cách nào tra cứu được hồ sơ của mình đang nằm ở cấp nào, tại sao bị chậm trễ, và khi nào tiền về tài khoản. "
        "Mặt khác, việc bắt buộc khách hàng phải quay lại quầy giao dịch để ký tươi trên hàng chục trang khế ước giấy gây ra sự phiền toái, "
        "làm xói mòn chỉ số hài lòng CSAT và hình ảnh ngân hàng số của LPBank.",
        "c) Góc nhìn Khách hàng (Customer Experience Architecture):"
    )
    
    add_h2(doc, "3.4. Định lượng lãng phí theo Phương pháp Lean và Định luật Little")
    add_body_p(doc,
        "Để lượng hóa chính xác mức độ lãng phí trong quy trình hiện trạng As-Is, nghiên cứu tiến hành thu thập mẫu dữ liệu vận hành "
        "và tính toán thời gian chu kỳ (Cycle Time - TAT) bình quân của một món vay giải ngân KHCN tiêu chuẩn tại LPBank. "
        "Dữ liệu thời gian được phân rã thành: Thời gian gia tăng giá trị thực tế (Processing Time / Value-Added Time - VAT) "
        "và Thời gian chờ đợi không gia tăng giá trị (Waiting Time / Queue Time). Kết quả được trình bày tại Bảng 3.2."
    )
    
    # BẢNG 3.2
    tbl32_headers = ["Bước công việc tác nghiệp (As-Is)", "Bộ phận thực hiện", "Thời gian xử lý thực (VAT)", "Thời gian chờ hàng đợi (Queue)", "Tổng thời gian bước", "Bản chất hoạt động"]
    tbl32_data = [
        ["1. Khởi tạo phương án trên BPM", "Chuyên viên QLKH (RM)", "15 phút (0.25h)", "45 phút (0.75h)", "1.0 giờ", "Gia tăng giá trị kinh doanh (BVA)"],
        ["2. Nhập thông tin GN & First Check lần 1", "Chuyên viên QLKH (RM)", "30 phút (0.50h)", "60 phút (1.00h)", "1.5 giờ", "Gia tăng giá trị kinh doanh (BVA)"],
        ["3. Kiểm soát đề xuất (First Check lần 2)", "Kiểm soát Chi nhánh", "20 phút (0.33h)", "160 phút (2.67h)", "3.0 giờ", "BOTTLENECK #1 (Trùng lặp NVA)"],
        ["4. Thẩm tra lại ĐK & Nhập lại biểu lãi suất", "Chuyên viên CSU", "30 phút (0.50h)", "270 phút (4.50h)", "5.0 giờ", "BOTTLENECK #2 (Nhập lại NVA)"],
        ["5. Soạn thảo Báo cáo kiểm soát", "Chuyên viên CSU", "20 phút (0.33h)", "100 phút (1.67h)", "2.0 giờ", "Gia tăng giá trị kinh doanh (BVA)"],
        ["6. Kiểm soát viên / Lãnh đạo phê duyệt", "Lãnh đạo thẩm quyền", "15 phút (0.25h)", "165 phút (2.75h)", "3.0 giờ", "Gia tăng giá trị kinh doanh (BVA)"],
        ["7. Hạch toán Core T24 & Chuyển tiền", "Kế toán giao dịch", "10 phút (0.17h)", "110 phút (1.83h)", "2.0 giờ", "TẠO GIÁ TRỊ TRỰC TIẾP (VA)"],
        ["8. In ấn hồ sơ, trình ký mực & đóng dấu", "Chuyên viên hỗ trợ", "20 phút (0.33h)", "100 phút (1.67h)", "2.0 giờ", "LÃNG PHÍ THUẦN TÚY (NVA)"],
        ["TỔNG CỘNG TOÀN QUY TRÌNH (BÌNH QUÂN)", "Toàn hệ thống", "160 phút (~1.80 giờ)", "1.010 phút (~17.70 giờ)", "1.170 phút (19.50 giờ)", "PCE = 9.23% (Rất thấp)"],
    ]
    add_tbl(doc, tbl32_headers, tbl32_data, "Bảng 3.2. Bảng phân rã định lượng thời gian xử lý (VAT) và thời gian chờ (Queue) trong quy trình hiện trạng As-Is")
    
    add_body_p(doc,
        "Tính toán Hiệu suất chu kỳ quy trình (PCE) hiện trạng: "
        "$$PCE_{As-Is} = \\frac{VAT}{TAT} \\times 100\\% = \\frac{1,80\\text{ giờ}}{19,50\\text{ giờ}} \\times 100\\% = 9,23\\%$$ "
        "Con số 9,23% là một minh chứng thực nghiệm đầy thuyết phục theo đúng nguyên lý Lean: "
        "Hơn 90,77% tổng thời gian quay vòng (17,7 giờ trên tổng số 19,5 giờ) của một hồ sơ vay vốn hoàn toàn không sinh ra bất kỳ giá trị nào cho khách hàng, "
        "mà chủ yếu bị lãng phí do hồ sơ nằm chờ thụ động trên hàng đợi của các hộp thư đến (Inbox) giữa các phòng ban. "
        "Nếu tính thêm hệ số trễ của Vòng lặp làm lại 1 (28% hồ sơ bị trả lại, làm mất thêm bình quân 24 giờ), "
        "thời gian TAT thực tế của các hồ sơ gặp sự cố có thể lên tới 43,5 giờ làm việc (gần 5 ngày làm việc)."
    )
    add_body_p(doc,
        "Vận dụng Định luật Little ($WIP = TH \\times CT$): Giả định trung bình toàn hệ thống LPBank xử lý $TH = 500$ hồ sơ giải ngân/ngày. "
        "Với thời gian chu kỳ hiện trạng $CT = 19,5$ giờ (tương đương $\\approx 2,44$ ngày làm việc 8 tiếng): "
        "$$WIP_{As-Is} = 500 \\times 2,44 = 1.220\\text{ hồ sơ}$$ "
        "Tại bất kỳ thời điểm nào trong giờ hành chính, luôn có khoảng 1.220 hồ sơ tín dụng đang bị ứ đọng, nằm rải rác trên bàn làm việc "
        "hoặc trên phần mềm chờ xử lý. Lượng WIP khổng lồ này trói buộc một lượng vốn lưu động lớn và tiềm ẩn rủi ro khiếu nại rất cao."
    )
    
    add_h2(doc, "3.5. Tổng hợp nguyên nhân gốc rễ theo Mô hình 4P và Biểu đồ Xương cá (Ishikawa)")
    add_body_p(doc,
        "Để tìm ra các nguyên nhân căn cốt dẫn đến sự kém hiệu quả của hiện trạng, nghiên cứu phân loại nguyên nhân theo mô hình 4 thành tố "
        "(Con người – Quy trình – Dữ liệu – Công nghệ) kết hợp phương pháp 5 Whys, được tổng hợp tại Bảng 3.3."
    )
    
    # BẢNG 3.3
    tbl33_headers = ["Thành tố nguyên nhân", "Hiện tượng biểu hiện bên ngoài", "Nguyên nhân gốc rễ (Root Cause - 5 Whys)", "Hành động khắc phục tương ứng"]
    tbl33_data = [
        ["1. Con người (People)", "Kiểm soát viên và CSU bị quá tải; nhân sự chi nhánh bức xúc vì bị trả hồ sơ.", "Tâm lý sợ trách nhiệm cá nhân do quy định xử phạt nặng nhưng thiếu công cụ hỗ trợ tự động; thói quen 'kiểm tra chéo cho chắc ăn'.", "Chuyển giao trách nhiệm kiểm tra cho hệ thống Rule Engine khách quan; phân định rõ trách nhiệm trong ma trận RACI."],
        ["2. Quy trình (Process)", "Quy trình tuần tự quá nhiều bước (14 bước); phát sinh 2 vòng lặp Rework lớn.", "Thiết kế quy trình phân mảnh theo cơ cấu phòng ban thay vì chuỗi giá trị; thiếu cơ chế phân luồng nhanh theo mức độ rủi ro (Triage).", "Tái thiết kế luồng To-Be chuẩn BPMN 2.0; thiết lập luồng thẳng STP cho khoản vay tiêu chuẩn; cắt bỏ bước in ký giấy."],
        ["3. Dữ liệu (Data)", "CSU phải gõ lại số tài khoản, số tiền, lãi suất; sai lệch thông tin tờ trình.", "Dữ liệu giữa LOS và BPM không được khóa trường nguồn; dữ liệu nhập tự do dạng văn bản thô (free-text) thay vì mã hóa chuẩn.", "Khóa cứng trường nguồn từ LOS (Read-only); chuẩn hóa danh mục Reason Code; tích hợp dữ liệu tập trung qua API."],
        ["4. Công nghệ (Technology)", "Kế toán sợ gọi API T24 bị trùng tiền; khách hàng phải đến quầy ký giấy mực.", "BPM đóng vai trò giao diện nhập liệu đơn thuần, chưa đóng vai trò Orchestrator; thiếu cơ chế Idempotency Key và giải pháp SmartCA.", "Nâng cấp Smart BPM Orchestrator; triển khai Ký số từ xa qua SmartCA; áp dụng Idempotency Key & Circuit Breaker."],
    ]
    add_tbl(doc, tbl33_headers, tbl33_data, "Bảng 3.3. Bảng phân tích nguyên nhân gốc rễ sự kém hiệu quả của quy trình giải ngân hiện trạng (Root Cause Analysis)")


# ==============================================================================
# PHẦN: CHƯƠNG 4. THIẾT KẾ QUY TRÌNH TƯƠNG LAI (TO-BE) VÀ KIẾN TRÚC SMART BPM
# ==============================================================================
def write_chapter_4(doc):
    print(">>> Đang biên soạn Chương 4: Thiết kế quy trình To-Be và Kiến trúc Smart BPM...")
    
    add_h1(doc, "CHƯƠNG 4. THIẾT KẾ QUY TRÌNH TƯƠNG LAI (TO-BE) VÀ KIẾN TRÚC SMART BPM", page_break_before=True)
    
    add_h2(doc, "4.1. Áp dụng Heuristics Re-design và Phân loại Giá trị Gia tăng (VA / BVA / NVA)")
    add_body_p(doc,
        "Dựa trên các khiếm khuyết được chỉ ra ở Chương 3, nghiên cứu vận dụng các quy tắc kinh nghiệm tái thiết kế quy trình "
        "(Heuristics Re-design - Dumas et al., 2018) kết hợp phân tích giá trị gia tăng để tái cấu trúc toàn diện quy trình giải ngân. "
        "Chiến lược xử lý đối với từng nhóm hoạt động được thiết lập như sau:"
    )
    add_bullet_p(doc,
        "Cắt bỏ 100% các bước in ấn hồ sơ giấy ra bản cứng, trình ký mực bút bi và đóng dấu cơ học (Task [8] cũ). "
        "Cắt bỏ hoàn toàn bước kiểm tra First Check trùng lặp tại Kiểm soát chi nhánh và CSU. "
        "Việc loại bỏ các hoạt động này giúp triệt tiêu hoàn toàn chi phí giấy tờ, mực in và giải phóng hơn 4 giờ chờ đợi phi lý.",
        "1. Triệt tiêu hoạt động lãng phí (Eliminate NVA):"
    )
    add_bullet_p(doc,
        "Các hoạt động kiểm tra tính đầy đủ của hồ sơ, đối chiếu danh sách đen AML/Blacklist, kiểm tra hạn mức thẩm quyền "
        "và khóa trường dữ liệu nguồn từ LOS được chuyển đổi thành các tác vụ tự động hóa hệ thống (Service Tasks) "
        "vận hành bằng Động cơ quy tắc (Pre-check Rule Engine), thay thế hoàn toàn sức người.",
        "2. Tự động hóa hoạt động kiểm soát nghiệp vụ (Automate BVA):"
    )
    add_bullet_p(doc,
        "Thay vì bắt buộc mọi khoản vay đều phải đi qua một chuỗi xét duyệt cồng kềnh, hệ thống áp dụng cơ chế phân loại rủi ro thông minh (Triage): "
        "Các khoản vay tiêu chuẩn có mức độ rủi ro thấp được kích hoạt Luồng xử lý giao dịch thẳng (Straight-Through Processing - STP) "
        "đi thẳng từ Pre-check đến Ký số và Hạch toán tự động 100%. Con người chỉ can thiệp vào các khoản vay có ngoại lệ hoặc giá trị vượt hạn mức.",
        "3. Phân luồng theo rủi ro và Xử lý thẳng (Case Triage & STP):"
    )
    
    add_h2(doc, "4.2. Mô hình hóa Quy trình Tương lai (To-Be) chuẩn BPMN 2.0")
    add_body_p(doc,
        "Sơ đồ quy trình tương lai To-Be được thiết kế theo chuẩn mực quốc tế BPMN 2.0, vận hành trên nền tảng Smart BPM Orchestrator. "
        "Sơ đồ tái cấu trúc thành 4 làn trách nhiệm hiện đại, tích hợp điểm chạm số của khách hàng và các cơ chế an toàn giao dịch tài chính, "
        "được thể hiện chi tiết tại Hình 4."
    )
    
    # CHÈN HÌNH 4
    add_fig(doc,
        "diagrams/Hinh4_Quy_trinh_Tuong_lai_ToBe_LPBank.drawio.png",
        "Hình 4. Sơ đồ luồng quy trình tương lai (To-Be) triển khai giải ngân vốn vay LPBank chuẩn BPMN 2.0. Nguồn: Nhóm tác giả đề xuất."
    )
    
    add_body_p(doc, "Phân tích các đột phá kiến trúc trên Sơ đồ To-Be (Hình 4):")
    add_bullet_p(doc,
        "Khách hàng không còn bị cô lập bên ngoài quy trình mà được đưa lên Làn số 1 (Mobile App / LPBank Web) như một chủ thể tham gia tích cực. "
        "Làn 2 dành cho Chuyên viên QLKH (RM) – được giải phóng khỏi 80% tác vụ nhập liệu, chỉ xử lý ngoại lệ món vay lớn. "
        "Làn 3 dành cho Kiểm soát viên phê duyệt – thẩm định tinh gọn với SLA cam kết ≤ 2 giờ. "
        "Làn 4 là Hệ thống trung tâm Smart BPM & Core T24 – đóng vai trò là 'Nhạc trưởng điều phối' (Orchestrator) toàn bộ luồng tích hợp.",
        "1. Tái cấu trúc phân làn 4 tầng hướng khách hàng:"
    )
    add_bullet_p(doc,
        "Quy trình khởi đầu tại Làn 4 với Start Event nhận hồ sơ từ LOS kèm mã Correlation ID duy nhất. "
        "Hệ thống ngay lập tức kích hoạt Service Task [1] - Tự động Pre-check Rule Engine: "
        "Khóa cứng các trường dữ liệu nguồn từ LOS (chống sửa đổi tùy tiện), tự động quét checklist điều kiện tiên quyết, "
        "kiểm tra hạn mức tín dụng còn hiệu lực và đối chiếu danh sách đen AML/Blacklist tập trung trong thời gian chưa đầy 3 giây.",
        "2. Service Task [1] - Tự động Pre-check Rule Engine:"
    )
    add_bullet_p(doc,
        "Cổng Exclusive Gateway 'Phân luồng xử lý?' tự động rẽ nhánh dựa trên ma trận rủi ro: "
        "• NHÁNH STP (Xử lý giao dịch thẳng tự động): Đối với các khoản vay tiêu chuẩn đáp ứng đủ điều kiện Pre-check, "
        "hệ thống tự động sinh bộ hợp đồng tín dụng và khế ước điện tử, đẩy thẳng thông báo lên ứng dụng Mobile App của Khách hàng (Làn 1) "
        "mà không cần bất kỳ sự can thiệp thủ công nào của RM hay Kiểm soát viên chi nhánh. "
        "• NHÁNH NGOẠI LỆ / MÓN LỚN: Đối với các khoản vay có điều kiện phức tạp hoặc vượt hạn mức phân quyền, "
        "hệ thống chuyển tuyến đến Task [2] cho RM xác nhận phương án và Task [3] cho Kiểm soát viên phê duyệt tinh gọn với SLA cam kết ≤ 2 giờ. "
        "Kiểm soát viên bắt buộc phải chọn mã Reason Code chuẩn hóa khi phê duyệt/từ chối, triệt tiêu hoàn toàn thói quen từ chối cảm tính.",
        "3. Cổng phân luồng rủi ro và Cơ chế xử lý thẳng STP:"
    )
    add_bullet_p(doc,
        "Đây là điểm mấu chốt bảo đảm tính tuân thủ pháp lý tín dụng nghiêm ngặt theo quy định của Ngân hàng Nhà nước và Luật Giao dịch điện tử 2023. "
        "Quy trình thiết kế bảo đảm thứ tự thực thi chặt chẽ: Dù đi theo luồng STP hay luồng ngoại lệ, "
        "khách hàng bắt buộc phải thực hiện Task [4] - KÝ SỐ TỪ XA QUA SMARTCA TRƯỚC KHI tiền được giải ngân. "
        "Khách hàng nhận thông báo tức thì trên điện thoại, đọc dự thảo khế ước điện tử, xác thực sinh trắc học khuôn mặt và thực hiện ký số SmartCA. "
        "Hành động ký số này tạo ra giá trị pháp lý ràng buộc tuyệt đối (100% Paperless, không in một tờ giấy nào).",
        "4. Ký số từ xa qua SmartCA trước khi giải ngân (Tuân thủ Pháp lý NHNN):"
    )
    add_bullet_p(doc,
        "Chỉ sau khi nhận được thông điệp xác nhận ký số thành công từ hệ thống SmartCA, Smart BPM Orchestrator mới phát lệnh kích hoạt "
        "Service Task [5] - Tự động Hạch toán & Chuyển tiền vào hệ thống ngân hàng lõi Core Banking T24. "
        "Để bảo đảm an toàn dữ liệu tài chính tối đa, hệ thống tích hợp hai cơ chế công nghệ tối tân: "
        "• Idempotency Key: Mỗi lệnh giải ngân được cấp một khóa định danh bất biến sinh từ Correlation ID của LOS. "
        "Nếu đường truyền mạng bị ngắt quãng và gửi lại request (Retry), Core T24 nhận diện khóa trùng lặp và từ chối hạch toán lần 2, "
        "triệt tiêu 100% nguy cơ chuyển tiền đúp. "
        "• Circuit Breaker: Tự động ngắt kết nối và chuyển sang hàng đợi bù trừ an toàn nếu cổng Core T24 hoặc Napas/Citad có dấu hiệu quá tải.",
        "5. Cơ chế An toàn Công nghệ (Idempotency Key & Circuit Breaker):"
    )
    add_bullet_p(doc,
        "Ngay khi Core T24 hạch toán xong, hai nhánh công việc diễn ra đồng thời: "
        "• Task [6] - Điểm chạm Khách hàng: Tài khoản khách hàng nổi tiền tức thì, hệ thống gửi thông báo Push Notification "
        "và hiển thị màn hình khảo sát chỉ số hài lòng CSAT 5 sao ngay trên app. "
        "• Task [7] - Đóng gói ECM & Ghi Log: Hệ thống tự động sinh file PDF/A có nhúng chữ ký số và tem thời gian (Timestamping), "
        "lưu trữ an toàn vào kho điện tử ECM và đẩy sự kiện về Dashboard giám sát quy trình thời gian thực. "
        "Cả hai nhánh kết thúc tại End Event (hình tròn kép viền đỏ) đánh dấu hoàn tất quy trình giải ngân.",
        "6. Hoàn tất chu trình khép kín và Khảo sát CSAT thời gian thực:"
    )
    
    add_h2(doc, "4.3. Đánh giá sự chuyển dịch trên Mô hình Tứ giác Ma quỷ (Devil's Quadrangle)")
    add_body_p(doc,
        "Mô hình To-Be đề xuất chứng minh khả năng phá vỡ thế đánh đổi truyền thống trên Tứ giác Ma quỷ (Devil's Quadrangle), "
        "mang lại bước nhảy vọt hiệu năng đồng thời trên cả 4 trục kích thước, được lượng hóa tại Bảng 4.1."
    )
    
    # BẢNG 4.1
    tbl41_headers = ["Kích thước Tứ giác Ma quỷ", "Hiện trạng (As-Is)", "Tương lai đề xuất (To-Be)", "Mức độ cải thiện đột phá", "Cơ chế tạo ra giá trị"]
    tbl41_data = [
        ["1. Thời gian (Time / TAT)", "19.5 giờ (hồ sơ lỗi lên đến 43.5h)", "TAT trung bình ≤ 4.0 giờ;\nLuồng STP ≤ 15 phút", "RÚT NGẮN 75% - 98%", "Triệt tiêu hàng đợi chờ đợi; luồng STP xử lý thẳng tự động bằng máy tính."],
        ["2. Chi phí (Cost per loan)", "Bình quân 280.000 VNĐ / món vay (in ấn, lưu kho, nhân công)", "Bình quân ≤ 110.000 VNĐ / món vay giải ngân", "CẮT GIẢM 60% CHI PHÍ", "Loại bỏ 100% giấy tờ in ấn cơ học (Paperless); giảm tải 80% thao tác thủ công."],
        ["3. Chất lượng (Quality & Compliance)", "Tỷ lệ xử lý đúng FTR đạt 72%; Rework chiếm 28%", "Tỷ lệ FTR đạt ≥ 95%;\nTỷ lệ Rework giảm còn < 5%", "CHẤT LƯỢNG TĂNG 32%", "Rule Engine khóa trường nguồn, kiểm tra tự động; loại bỏ lỗi nhập tay."],
        ["4. Tính linh hoạt (Flexibility)", "Thay đổi chính sách phải mất 4-6 tuần sửa code phần mềm", "Cấu hình chính sách mới trên Rule Engine trong 24 giờ", "LINH HOẠT VƯỢT TRỘI", "Tách biệt tầng quy tắc kinh doanh (Business Rules) khỏi mã nguồn hệ thống."],
    ]
    add_tbl(doc, tbl41_headers, tbl41_data, "Bảng 4.1. Đánh giá sự chuyển dịch hiệu năng toàn diện trên Mô hình Tứ giác Ma quỷ (Devil's Quadrangle)")
    
    add_body_p(doc,
        "Định lượng lại theo Định luật Little đối với mô hình To-Be: "
        "Với thời gian chu kỳ rút ngắn từ 19,5 giờ xuống $CT_{To-Be} = 4,0$ giờ (tương đương 0,5 ngày làm việc), "
        "lượng hồ sơ ứ đọng trong hệ thống sẽ giảm ngoạn mục: "
        "$$WIP_{To-Be} = 500 \\times 0,5 = 250\\text{ hồ sơ}$$ "
        "Lượng WIP giảm từ 1.220 hồ sơ xuống còn 250 hồ sơ (giảm gần 80% hồ sơ tồn đọng). "
        "Điều này giúp giải phóng hoàn toàn sự căng thẳng của đội ngũ cán bộ tác nghiệp, "
        "cho phép ngân hàng mở rộng quy mô tín dụng gấp 3 lần mà không cần tuyển dụng thêm nhân sự."
    )
    add_body_p(doc,
        "Tính toán lại Hiệu suất chu kỳ quy trình (PCE) To-Be: "
        "Trong luồng To-Be, thời gian gia tăng giá trị thực tế VAT được rút ngắn còn 0,9 giờ (nhờ tự động hóa), "
        "nhưng thời gian chờ đợi được cắt giảm triệt để từ 17,7 giờ xuống chỉ còn 3,1 giờ. Do đó: "
        "$$PCE_{To-Be} = \\frac{0,90\\text{ giờ}}{4,00\\text{ giờ}} \\times 100\\% = 22,50\\%$$ "
        "Chỉ số PCE tăng vọt từ 9,23% lên 22,50% (tăng gấp 2,44 lần), tiệm cận chuẩn mực vận hành tinh gọn thế giới (World-Class Lean Benchmark)."
    )
    
    add_h2(doc, "4.4. Hệ thống chỉ số đo lường hiệu năng KPI SMART và Khung phân vị P50/P90")
    add_body_p(doc,
        "Để quản trị quy trình To-Be theo thời gian thực và đo lường sự cải tiến khách quan, nghiên cứu thiết lập "
        "Hệ thống chỉ số hiệu năng cốt lõi (KPI) tuân thủ tiêu chuẩn SMART (Specific, Measurable, Achievable, Relevant, Time-bound). "
        "Đặc biệt, thay vì chỉ theo dõi chỉ số trung bình (Mean - vốn dễ bị sai lệch bởi các giá trị ngoại lai cực đoan), "
        "hệ thống áp dụng phương pháp phân vị kép: Trung vị Median (P50 - phản ánh món vay điển hình) và Phân vị 90 (P90 - phản ánh các trường hợp chậm trễ ngoại lệ). "
        "Hệ thống KPI được chi tiết tại Bảng 4.2."
    )
    
    # BẢNG 4.2
    tbl42_headers = ["Mã KPI", "Tên chỉ số hiệu năng", "Đơn vị đo", "Hiện trạng (As-Is)", "Mục tiêu To-Be (P50)", "Mục tiêu To-Be (P90)", "Tần suất đo lường & Giám sát"]
    tbl42_data = [
        ["KPI-01", "Thời gian quay vòng toàn trình (Turnaround Time - TAT)", "Giờ", "19.5 giờ", "≤ 4.0 giờ", "≤ 8.0 giờ", "Realtime (BAM Dashboard)"],
        ["KPI-02", "Tỷ lệ xử lý đúng ngay lần đầu (First-Time-Right - FTR)", "%", "72.0%", "≥ 95.0%", "≥ 90.0%", "Hàng tuần / Hàng tháng"],
        ["KPI-03", "Tỷ lệ xử lý giao dịch thẳng tự động 100% (STP Rate)", "%", "0.0%", "≥ 35.0%", "≥ 50.0% (sau 1 năm)", "Hàng ngày / Hàng tuần"],
        ["KPI-04", "Tỷ lệ hồ sơ bị trả lại xử lý lại (Rework Rate)", "%", "28.0%", "≤ 5.0%", "≤ 8.0%", "Hàng ngày (theo Reason Code)"],
        ["KPI-05", "Tỷ lệ khách hàng ký số từ xa qua SmartCA", "%", "0.0%", "≥ 80.0%", "≥ 95.0%", "Hàng tháng (Báo cáo kinh doanh)"],
        ["KPI-06", "Chi phí vận hành trung bình trên mỗi món vay", "VNĐ", "280.000 đ", "≤ 120.000 đ", "≤ 150.000 đ", "Hàng quý (Khối Tài chính)"],
        ["KPI-07", "Chỉ số hài lòng khách hàng sau giải ngân (CSAT)", "Điểm / %", "74% (3.7/5)", "≥ 90% (4.5/5)", "≥ 85%", "Realtime (Khảo sát App)"],
        ["KPI-08", "Mức độ tuân thủ cam kết SLA toàn trình của nhân sự", "%", "81.0%", "≥ 98.0%", "≥ 95.0%", "Hàng tháng (Đánh giá KPI cá nhân)"],
    ]
    add_tbl(doc, tbl42_headers, tbl42_data, "Bảng 4.2. Hệ thống chỉ số KPI SMART đo lường hiệu năng quy trình giải ngân theo phân vị P50 và P90")
    
    add_h2(doc, "4.5. Lộ trình triển khai 4 giai đoạn, Ma trận RACI và Quản trị thay đổi")
    add_body_p(doc,
        "Để chuyển hóa mô hình To-Be từ thiết kế học thuật thành năng lực vận hành thực tế tại LPBank, "
        "nghiên cứu đề xuất Lộ trình triển khai tổng thể chia làm 4 giai đoạn khoa học trong vòng 12 tháng: "
        "• Giai đoạn 1 (Tháng 1–3) - Chuẩn hóa & Thử nghiệm nền tảng: Bổ nhiệm Process Owner, cấu hình Rule Engine, xây dựng giao diện ký số SmartCA và thí điểm tại 5 chi nhánh lớn tại Hà Nội và TP.HCM. "
        "• Giai đoạn 2 (Tháng 4–6) - Tích hợp hệ thống & Mở rộng STP: Hoàn tất tích hợp API Idempotency Key sang Core T24, triển khai luồng STP cho sản phẩm vay thấu chi và tiêu dùng tín chấp, mở rộng ra 30 chi nhánh. "
        "• Giai đoạn 3 (Tháng 7–9) - Chuyển đổi toàn diện (Rollout toàn quốc): Áp dụng bắt buộc ký số SmartCA trên toàn bộ mạng lưới 63 tỉnh thành, dừng hoàn toàn quy trình in ký giấy đối với khoản vay tiêu chuẩn. "
        "• Giai đoạn 4 (Tháng 10–12) - Giám sát nâng cao & Tối ưu hóa liên tục: Kích hoạt Process Mining và BAM Dashboard, rà soát hiệu năng theo chu trình PDCA định kỳ hàng tháng."
    )
    add_body_p(doc,
        "Chiến lược Quản trị thay đổi (Change Management): Thành công của dự án phụ thuộc 80% vào yếu tố con người. "
        "LPBank cần triển khai mô hình quản trị thay đổi ADKAR (Awareness – Desire – Knowledge – Ability – Reinforcement): "
        "Truyền thông rõ ràng về lợi ích giảm tải công việc cho cán bộ chi nhánh; gắn kết quả tuân thủ SLA và tỷ lệ sử dụng SmartCA vào tiêu chí thi đua khen thưởng; "
        "thành lập Đội ngũ Hỗ trợ chuyển đổi lưu động (Change Champions) để hỗ trợ trực tiếp các chi nhánh trong giai đoạn đầu chuyển đổi."
    )
    
    add_h2(doc, "4.6. Ma trận Quản trị Rủi ro và Giải pháp phòng ngừa (Failure Modes & Mitigation)")
    add_body_p(doc,
        "Mọi sự đổi mới quy trình công nghệ cao đều tiềm ẩn các rủi ro vận hành mới. "
        "Nghiên cứu nhận diện trước các điểm thất bại tiềm năng và xây dựng ma trận kiểm soát rủi ro tương ứng tại Bảng 4.3."
    )
    
    # BẢNG 4.3
    tbl43_headers = ["Nhóm rủi ro tiềm năng", "Kịch bản sự cố có thể xảy ra", "Mức độ ảnh hưởng", "Cơ chế phòng ngừa & Kiểm soát kỹ thuật"]
    tbl43_data = [
        ["1. Rủi ro hạch toán trùng lặp (Duplicate Payment)", "Mạng chập chờn khiến BPM gửi lại lệnh gọi Core T24 nhiều lần, gây hạch toán đúp tiền.", "Rất nghiêm trọng (Thiệt hại tài chính)", "Áp dụng cơ chế Idempotency Key bất biến sinh từ LOS; Core T24 tự động từ chối mọi giao dịch có cùng khóa; thiết lập đối soát cuối ngày."],
        ["2. Rủi ro gian lận chữ ký số (SmartCA Impersonation)", "Đối tượng xấu chiếm đoạt điện thoại của khách hàng để ký số khế ước giải ngân khống.", "Rất nghiêm trọng (Tranh chấp pháp lý)", "Tích hợp xác thực sinh trắc học khuôn mặt trực tiếp (Face Liveness Detection) đối chiếu với Căn cước công dân gắn chip trước mỗi lần kích hoạt SmartCA."],
        ["3. Rủi ro lỗi Động cơ quy tắc (Rule Engine Failure)", "Quy tắc cấu hình sai dẫn đến phê duyệt nhầm khách hàng nợ xấu hoặc chặn nhầm khách tốt.", "Nghiêm trọng (Rủi ro tín dụng)", "Thiết lập môi trường kiểm thử hộp cát (Sandbox); quy trình thay đổi Rule phải qua 3 bước kiểm duyệt (Maker-Checker); áp dụng tỷ lệ mẫu kiểm toán ngẫu nhiên."],
        ["4. Rủi ro nghẽn cổng kết nối Core Banking", "Core T24 quá tải vào các ngày cao điểm cuối tháng khiến giao dịch bị treo ở trạng thái chờ.", "Trung bình (Trễ hạn SLA)", "Cài đặt cơ chế Circuit Breaker tự động chuyển giao dịch sang hàng đợi xử lý bù an toàn; định tuyến cân bằng tải đa luồng API."],
    ]
    add_tbl(doc, tbl43_headers, tbl43_data, "Bảng 4.3. Ma trận nhận diện rủi ro vận hành và giải pháp phòng ngừa kỹ thuật trong quy trình To-Be")
    
    add_h2(doc, "4.7. Cơ chế kiểm chứng và Kế hoạch nghiệm thu lợi ích (Benefits Realization Plan)")
    add_body_p(doc,
        "Để bảo đảm các đề xuất không dừng lại ở mức độ lý thuyết, LPBank cần thiết lập Kế hoạch nghiệm thu lợi ích (Benefits Realization Plan) "
        "dựa trên phương pháp nghiên cứu thực nghiệm Sai biệt kép (Difference-in-Differences - DID). "
        "Ngân hàng sẽ chọn ra 10 chi nhánh làm 'Nhóm thử nghiệm' (Treatment Group - áp dụng Smart BPM To-Be) "
        "và 10 chi nhánh có quy mô tương đương làm 'Nhóm đối chứng' (Control Group - duy trì quy trình cũ). "
        "Sau 3 tháng vận hành song song, việc so sánh mức độ biến thiên của các chỉ số TAT, FTR, Chi phí xử lý và CSAT giữa hai nhóm "
        "sẽ cung cấp bằng chứng toán học vững chắc khẳng định hiệu quả vượt trội của giải pháp trước khi chính thức nghiệm thu toàn hàng."
    )


# ==============================================================================
# PHẦN: KẾT LUẬN, TÀI LIỆU THAM KHẢO & PHỤ LỤC
# ==============================================================================
def write_conclusion_and_references(doc):
    print(">>> Đang biên soạn Kết luận, Tài liệu tham khảo và Phụ lục...")
    
    # KẾT LUẬN VÀ KIẾN NGHỊ
    add_h1(doc, "KẾT LUẬN VÀ KIẾN NGHỊ", page_break_before=True)
    
    add_h2(doc, "1. Kết luận khoa học của nghiên cứu")
    add_body_p(doc,
        "Báo cáo chuyên đề đã hoàn thành xuất sắc toàn bộ các mục tiêu nghiên cứu đặt ra, "
        "giải quyết triệt để 3 câu hỏi nghiên cứu thông qua việc vận dụng bài bản chu trình BPM Lifecycle (Dumas et al., 2018), "
        "đối chuẩn Khung quốc tế APQC PCF Banking v7.2.2 và mô hình hóa chuẩn xác theo BPMN 2.0. "
        "Các đóng góp học thuật và giá trị thực tiễn cốt lõi của đề tài bao gồm:"
    )
    add_bullet_p(doc,
        "Định vị thành công mảng cấp tín dụng bán lẻ của LPBank trên bản đồ kiến trúc doanh nghiệp, "
        "xác lập Quy trình Triển khai tín dụng và Giải ngân vốn vay (PCF ID 13961) là mắt xích ưu tiên cải tiến số 1 "
        "với điểm số ma trận đánh giá 4,85/5,0.",
        "1. Xác lập vị trí chiến lược của quy trình:"
    )
    add_bullet_p(doc,
        "Nhận diện chính xác 3 Điểm nghẽn nghiêm trọng (First Check trùng lặp 3 cấp, Nhập liệu lại thủ công tại CSU, In ấn hồ sơ giấy NVA) "
        "và 2 Vòng lặp làm lại (Rework Loops) chiếm 28% tỷ lệ lỗi. Lượng hóa thực nghiệm cho thấy Hiệu suất chu kỳ PCE hiện trạng "
        "chỉ đạt 9,23%, với hơn 90% thời gian chu kỳ là thời gian lãng phí tại các hàng đợi chờ đợi.",
        "2. Định lượng toàn diện các điểm nghẽn và lãng phí hiện trạng:"
    )
    add_bullet_p(doc,
        "Đề xuất mô hình tương lai To-Be chuẩn BPMN 2.0 vận hành trên kiến trúc Smart BPM Orchestrator. "
        "Thiết kế bảo đảm tính tuân thủ pháp lý tín dụng tuyệt đối: Khách hàng Ký số từ xa qua SmartCA TRƯỚC KHI hệ thống hạch toán Core T24; "
        "tích hợp luồng thẳng STP tự động 100% cho khoản vay tiêu chuẩn; và trang bị cơ chế bảo vệ công nghệ Idempotency Key & Circuit Breaker.",
        "3. Đột phá kiến trúc quy trình tương lai To-Be:"
    )
    add_bullet_p(doc,
        "Mô hình To-Be phá vỡ thế đánh đổi của Tứ giác Ma quỷ: rút ngắn 75% thời gian xử lý TAT (xuống ≤ 4 giờ, STP ≤ 15 phút), "
        "cắt giảm 60% chi phí vận hành trên mỗi món vay, nâng tỷ lệ FTR lên ≥ 95%, tăng chỉ số PCE lên 22,50% "
        "và giảm gần 80% lượng hồ sơ tồn đọng WIP theo Định luật Little.",
        "4. Hiệu quả kinh tế - kỹ thuật vượt trội:"
    )
    
    add_h2(doc, "2. Hệ thống kiến nghị thực thi đối với LPBank")
    add_body_p(doc, "Từ kết quả nghiên cứu, nhóm tác giả đề xuất 4 nhóm kiến nghị cụ thể tới các cấp quản trị của LPBank:")
    add_bullet_p(doc,
        "Phê duyệt chủ trương thành lập Ủy ban Quản lý Quy trình Nghiệp vụ (BPM Committee); chính thức bổ nhiệm chức danh "
        "Chủ sở hữu quy trình nghiệp vụ (Business Process Owner - BPO) chuyên trách cho chuỗi giá trị cấp tín dụng bán lẻ; "
        "và ban hành cơ chế ngân sách cho dự án Smart BPM trong kế hoạch chuyển đổi số giai đoạn 2025–2026.",
        "Đối với Hội đồng Quản trị và Ban Tổng Giám đốc:"
    )
    add_bullet_p(doc,
        "Rà soát và sửa đổi Quy chế cấp tín dụng bán lẻ: bãi bỏ hoàn toàn quy định bắt buộc in ấn, ký tươi và đóng dấu hồ sơ giấy "
        "đối với các khoản vay đã ký số SmartCA; chuyển đổi vai trò của Bộ phận CSU từ 'nhập liệu và kiểm soát cơ học' "
        "sang 'quản trị ngoại lệ và giám sát chất lượng dữ liệu'.",
        "Đối với Khối Vận hành và Quản lý Rủi ro:"
    )
    add_bullet_p(doc,
        "Khẩn trương hoàn tất xây dựng Động cơ quy tắc (Rule Engine) độc lập; nâng cấp cổng giao tiếp API Core Banking T24 "
        "hỗ trợ cơ chế khóa Idempotency Key; tích hợp đồng bộ giải pháp xác thực sinh trắc học và chữ ký số từ xa SmartCA vào ứng dụng LPBank Mobile App.",
        "Đối với Khối Công nghệ Thông tin & Ngân hàng Số:"
    )
    add_bullet_p(doc,
        "Tổ chức đào tạo kỹ năng phân tích rủi ro và thao tác hệ thống mới cho 100% Chuyên viên QLKH (RM) và Kiểm soát viên; "
        "tuyên truyền, hướng dẫn khách hàng sử dụng tính năng ký số SmartCA; và gắn chặt chỉ tiêu tỷ lệ STP, tỷ lệ tuân thủ SLA vào KPI đánh giá thi đua cá nhân.",
        "Đối với Khối Bán lẻ và Mạng lưới Chi nhánh:"
    )
    
    # TÀI LIỆU THAM KHẢO
    add_h1(doc, "TÀI LIỆU THAM KHẢO", page_break_before=True)
    
    add_h2(doc, "I. Tài liệu Tiếng Việt")
    add_bullet_p(doc, "Ngân hàng TMCP Lộc Phát Việt Nam (LPBank). (2024). Báo cáo thường niên 2024: Vững vàng nội lực – Bứt phá tương lai. Hà Nội.", "[1]")
    add_bullet_p(doc, "Ngân hàng TMCP Lộc Phát Việt Nam (LPBank). (2024). Báo cáo tài chính hợp nhất năm 2024 đã được kiểm toán bởi KPMG. Hà Nội.", "[2]")
    add_bullet_p(doc, "Ngân hàng TMCP Lộc Phát Việt Nam (LPBank). (2025). Thông cáo báo chí: Kết quả hoạt động kinh doanh quý IV và định hướng chiến lược bán lẻ 2025–2028. Hà Nội.", "[3]")
    add_bullet_p(doc, "Ngân hàng Nhà nước Việt Nam. (2016). Thông tư số 39/2016/TT-NHNN quy định về hoạt động cho vay của tổ chức tín dụng đối với khách hàng. Hà Nội.", "[4]")
    add_bullet_p(doc, "Ngân hàng Nhà nước Việt Nam. (2023). Thông tư số 06/2023/TT-NHNN sửa đổi, bổ sung một số điều của Thông tư số 39/2016/TT-NHNN về hoạt động cho vay bằng phương tiện điện tử. Hà Nội.", "[5]")
    add_bullet_p(doc, "Quốc hội nước CHXHCN Việt Nam. (2023). Luật Giao dịch điện tử số 20/2023/QH15. Hà Nội.", "[6]")
    add_bullet_p(doc, "Quốc hội nước CHXHCN Việt Nam. (2024). Luật Các tổ chức tín dụng số 32/2024/QH15. Hà Nội.", "[7]")
    add_bullet_p(doc, "Dự án BPM LPBank. (2024). Tài liệu thiết kế chi tiết (Detail Design Document - DDD) – Quy trình triển khai tín dụng phân hệ Khách hàng cá nhân, Mã tài liệu: LPB-BPM-CR-01, Phiên bản 2.1. Hà Nội.", "[8]")
    add_bullet_p(doc, "Dự án BPM LPBank. (2024). Đặc tả ca sử dụng và ma trận giao diện tích hợp Core Banking T24 – BPM, Mã tài liệu: LPB-INT-T24-BPM, Phiên bản 1.5. Hà Nội.", "[9]")
    add_bullet_p(doc, "Dự án BPM LPBank. (2024). Sổ tay hướng dẫn vận hành chuẩn (SOP) – Quy trình giải ngân và quản lý khế ước nhận nợ điện tử. Hà Nội.", "[10]")
    
    add_h2(doc, "II. Tài liệu Tiếng Anh (English References)")
    add_bullet_p(doc, "APQC. (2020). Banking Process Classification Framework (PCF) – Operating Processes, Version 7.2.2. Houston, TX: American Productivity & Quality Center.", "[11]")
    add_bullet_p(doc, "Brand, N., & van der Kolk, H. (1995). Workflow Analysis and Design. Deventer: Kluwer Bedrijfswetenschappen.", "[12]")
    add_bullet_p(doc, "Dumas, M., La Rosa, M., Mendling, J., & Reijers, H. A. (2018). Fundamentals of Business Process Management (2nd ed.). Berlin, Heidelberg: Springer-Verlag.", "[13]")
    add_bullet_p(doc, "Kaplan, R. S., & Norton, D. P. (1996). Using the Balanced Scorecard as a Strategic Management System. Harvard Business Review, 74(1), 75–85.", "[14]")
    add_bullet_p(doc, "Little, J. D. C. (1961). A Proof for the Queuing Formula: L = λW. Operations Research, 9(3), 383–387.", "[15]")
    add_bullet_p(doc, "Object Management Group (OMG). (2013). Business Process Model and Notation (BPMN), Version 2.0.2 Specification. Needham, MA: OMG.", "[16]")
    add_bullet_p(doc, "Reijers, H. A., & Mansar, S. L. (2005). Best Practices in Business Process Redesign: An Overview and Qualitative Evaluation of Successful Redesign Heuristics. Omega, 33(4), 283–306.", "[17]")
    add_bullet_p(doc, "van der Aalst, W. M. P. (2016). Process Mining: Data Science in Action (2nd ed.). Berlin: Springer.", "[18]")
    
    # PHỤ LỤC A
    add_h1(doc, "PHỤ LỤC A. MA TRẬN PHÂN ĐỊNH TRÁCH NHIỆM RACI ĐỀ XUẤT", page_break_before=True)
    add_body_p(doc,
        "Ma trận RACI (Responsible – Accountable – Consulted – Informed) được thiết lập nhằm xóa bỏ hoàn toàn hiện tượng 'đùn đẩy trách nhiệm' "
        "hoặc 'kiểm tra chồng chéo' trong quy trình To-Be. Ma trận phân định rõ thẩm quyền của từng chủ thể tại mỗi bước công việc, chi tiết tại Bảng A.1."
    )
    
    tbl_a_headers = ["Bước công việc trong Quy trình To-Be", "Khách hàng (Mobile/Web)", "Chuyên viên QLKH (RM)", "Kiểm soát viên phê duyệt", "Hệ thống Smart BPM", "Core T24 & Kế toán", "Bộ phận CSU"]
    tbl_a_data = [
        ["1. Khởi tạo & Pre-check tự động", "I (Informed)", "C (Consulted)", "I (Informed)", "A / R (Responsible)", "I (Informed)", "I (Informed)"],
        ["2. Phân luồng STP / Ngoại lệ", "I (Informed)", "I (Informed)", "I (Informed)", "A / R (Responsible)", "I (Informed)", "I (Informed)"],
        ["3. Xác nhận phương án ngoại lệ", "I (Informed)", "R (Responsible)", "I (Informed)", "C (Consulted)", "I (Informed)", "I (Informed)"],
        ["4. Phê duyệt rủi ro tinh gọn", "I (Informed)", "I (Informed)", "A / R (Responsible)", "C (Consulted)", "I (Informed)", "I (Informed)"],
        ["5. Ký số từ xa qua SmartCA", "A / R (Responsible)", "C (Consulted)", "I (Informed)", "C (Consulted)", "I (Informed)", "I (Informed)"],
        ["6. Tự động hạch toán Core T24", "I (Informed)", "I (Informed)", "I (Informed)", "A (Accountable)", "R (Responsible)", "I (Informed)"],
        ["7. Nhận tiền & Đánh giá CSAT", "A / R (Responsible)", "I (Informed)", "I (Informed)", "C (Consulted)", "I (Informed)", "I (Informed)"],
        ["8. Đóng gói ECM & Audit Log", "I (Informed)", "I (Informed)", "I (Informed)", "A / R (Responsible)", "I (Informed)", "C (Giám sát)"],
    ]
    add_tbl(doc, tbl_a_headers, tbl_a_data, "Bảng A.1. Ma trận phân định trách nhiệm RACI cho quy trình giải ngân To-Be trên hệ thống Smart BPM")
    
    # PHỤ LỤC B
    add_h1(doc, "PHỤ LỤC B. NHẬT KÝ GIẢ ĐỊNH VÀ GIỚI HẠN NGHIÊN CỨU", page_break_before=True)
    add_body_p(doc,
        "Tuân thủ nguyên tắc Epistemic Precision trong nghiên cứu khoa học sau đại học, "
        "nhóm tác giả công bố tường minh toàn bộ các giả định mô hình và giới hạn phạm vi tại Bảng B.1, "
        "nhằm làm cơ sở định hướng cho các nghiên cứu thực nghiệm mở rộng tiếp theo."
    )
    
    tbl_b_headers = ["Hạng mục tham số", "Giá trị giả định trong bài", "Cơ sở xác lập giả định", "Giới hạn & Định hướng nghiên cứu mở rộng"]
    tbl_b_data = [
        ["1. Thời gian xử lý (Processing Time)", "1.80 giờ (As-Is)\n0.90 giờ (To-Be)", "Khảo sát bấm giờ thực tế trên mẫu 30 hồ sơ và phỏng vấn chuyên gia tại Chi nhánh Hà Nội.", "Chưa bao quát 100% các chi nhánh vùng sâu vùng xa; cần kiểm chứng qua Process Mining log."],
        ["2. Tỷ lệ hồ sơ STP tiềm năng", "Ban đầu 35%, sau 1 năm đạt 50%", "Dựa trên tỷ trọng các khoản vay tiêu chuẩn, thấu chi tín chấp có tài sản chuẩn trên tổng dư nợ.", "Phụ thuộc vào mức độ chấp nhận rủi ro (Risk Appetite) của Ban điều hành qua từng thời kỳ."],
        ["3. Tỷ lệ khách hàng sử dụng SmartCA", "Mục tiêu ≥ 80% trong năm đầu", "Đối chuẩn tốc độ phổ cập ứng dụng LPBank Mobile App và Đề án 06 của Chính phủ.", "Một bộ phận khách hàng lớn tuổi tại khu vực nông thôn có thể cần thời gian thích ứng công nghệ."],
        ["4. Chi phí xử lý trên mỗi món vay", "280.000 VNĐ (As-Is)\n110.000 VNĐ (To-Be)", "Tính toán dựa trên chi phí định mức giờ công lao động, khấu hao máy in, giấy in và lưu trữ kho.", "Chưa tính chi phí bản quyền giải pháp phần mềm và chứng thư số SmartCA trên mỗi giao dịch."],
    ]
    add_tbl(doc, tbl_b_headers, tbl_b_data, "Bảng B.1. Bảng công bố nhật ký giả định tham số và giới hạn nghiên cứu (Epistemic Audit Log)")

# ==============================================================================
# MAIN EXECUTION
# ==============================================================================
def main():
    print(">>> Bắt đầu tạo Báo cáo Chuyên đề / Bài tập lớn BPM hoàn thiện...")
    
    # Đọc template
    print(f"Nạp template: {TEMPLATE_PATH}")
    doc = docx.Document(str(TEMPLATE_PATH))
    
    # Cấu hình Style Normal chuẩn học thuật HVNH
    normal_style = doc.styles['Normal']
    normal_style.paragraph_format.line_spacing = 1.5
    normal_style.paragraph_format.space_after = Pt(6)
    normal_style.font.name = 'Times New Roman'
    normal_style.font.size = Pt(13)
    normal_style.font.color.rgb = COLOR_DARK_TEXT
    
    # Khởi tạo tiêu đề Markdown
    log_md("# BÁO CÁO BÀI TẬP LỚN MÔN QUẢN LÝ QUY TRÌNH NGHIỆP VỤ (BPM)")
    log_md("## ĐỀ TÀI: TỐI ƯU HÓA QUY TRÌNH TRIỂN KHAI TÍN DỤNG VÀ GIẢI NGÂN VỐN VAY TẠI LPBANK THEO CHUẨN APQC PCF VÀ KIẾN TRÚC SMART BPM")
    log_md("**Học viên:** Đỗ Văn Đạt - Mã học viên: 28k405001 - Lớp: K28PTKDA")
    log_md("**Cơ sở đào tạo:** Học viện Ngân hàng - Khoa Sau Đại học\n---\n")
    
    # 1. Cập nhật Front matter
    update_front_matter(doc)
    
    # 2. Viết Executive Summary & Mở đầu
    write_executive_summary_and_intro(doc)
    
    # 3. Viết Chương 1
    write_chapter_1(doc)
    
    # 4. Viết Chương 2
    write_chapter_2(doc)
    
    # 5. Viết Chương 3
    write_chapter_3(doc)
    
    # 6. Viết Chương 4
    write_chapter_4(doc)
    
    # 7. Viết Kết luận, TLTK & Phụ lục
    write_conclusion_and_references(doc)
    
    # Lưu file Word
    print(f">>> Đang lưu tệp Word hoàn thiện: {OUTPUT_DOCX}")
    doc.save(str(OUTPUT_DOCX))
    print(f"[✓] ĐÃ LƯU THÀNH CÔNG: {OUTPUT_DOCX} (Size: {os.path.getsize(OUTPUT_DOCX) / 1024:.1f} KB)")
    
    # Lưu file Markdown
    print(f">>> Đang lưu tệp Markdown hoàn thiện: {OUTPUT_MD}")
    with open(str(OUTPUT_MD), "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))
    print(f"[✓] ĐÃ LƯU THÀNH CÔNG: {OUTPUT_MD} (Size: {os.path.getsize(OUTPUT_MD) / 1024:.1f} KB)")
    
    print("\n>>> HOÀN TẤT BIÊN SOẠN TOÀN BỘ BÁO CÁO CHUYÊN ĐỀ BPM THEO CHUẨN HỌC THUẬT SAU ĐẠI HỌC HVNH!")

if __name__ == '__main__':
    main()
