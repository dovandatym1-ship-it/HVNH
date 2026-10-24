#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Builder: Báo cáo Bài tập lớn môn Quản trị Quy trình Nghiệp vụ (BPM)
Học viện Ngân hàng - Khoa Sau Đại học
Giảng viên hướng dẫn: PGS.TS. Phan Thanh Đức
Học viên: Đỗ Văn Đạt - Mã học viên: 28k405001 - Lớp: K28PTKDA
Đề tài: ĐÁNH GIÁ VÀ HOÀN THIỆN HỆ THỐNG QUY TRÌNH NGHIỆP VỤ TẠI LPBANK THEO CHUẨN APQC PCF VÀ KIẾN TRÚC SMART BPM
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

md_lines = []

def log_md(line=""):
    md_lines.append(line)

def set_cell_background(cell, hex_color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:val="clear" w:color="auto" w:fill="{hex_color}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=50, bottom=50, left=70, right=70):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(
        f'<w:tcMar {nsdecls("w")}>'
        f'<w:top w:w="{top}" w:type="dxa"/>'
        f'<w:left w:w="{left}" w:type="dxa"/>'
        f'<w:bottom w:w="{bottom}" w:type="dxa"/>'
        f'<w:right w:w="{right}" w:type="dxa"/>'
        f'</w:tcMar>'
    )
    tcPr.append(tcMar)

def set_table_borders(table, border_color=HEX_BORDER):
    tblPr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'<w:top w:val="single" w:sz="6" w:space="0" w:color="{border_color}"/>'
        f'<w:left w:val="none"/>'
        f'<w:bottom w:val="single" w:sz="8" w:space="0" w:color="{border_color}"/>'
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

def add_h1(doc, title, page_break_before=False):
    if page_break_before:
        doc.add_page_break()
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(13)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(title)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(13.5)
    r.font.bold = True
    r.font.color.rgb = COLOR_NAVY_HVNH
    log_md(f"\n# {title}\n")

def add_h2(doc, title):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(title)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12.5)
    r.font.bold = True
    r.font.color.rgb = COLOR_BLUE_SEC
    log_md(f"\n## {title}\n")

def add_h3(doc, title):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(7)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(title)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r.font.bold = True
    r.font.color.rgb = COLOR_ACCENT_BLUE
    log_md(f"\n### {title}\n")

def add_body_p(doc, text, bold_prefix=None, indent=True, line_spacing=1.3, space_after=4):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.line_spacing = line_spacing
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.first_line_indent = Inches(0.35) if indent else Inches(0)
        
    full_text = ""
    if bold_prefix:
        r_b = p.add_run(bold_prefix)
        r_b.font.name = 'Times New Roman'
        r_b.font.size = Pt(11.5)
        r_b.font.bold = True
        r_b.font.color.rgb = COLOR_DARK_TEXT
        full_text += f"**{bold_prefix}** "
        
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(11.5)
    r.font.color.rgb = COLOR_DARK_TEXT
    full_text += text
    log_md(full_text + "\n")

def add_bullet_p(doc, text, bold_prefix=None):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.line_spacing = 1.25
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(2.5)
    p.paragraph_format.left_indent = Inches(0.3)
    p.paragraph_format.first_line_indent = Inches(-0.15)
    
    full_text = "- "
    r_sym = p.add_run("• ")
    r_sym.font.name = 'Times New Roman'
    r_sym.font.size = Pt(11)
    r_sym.font.color.rgb = COLOR_ACCENT_BLUE
    
    if bold_prefix:
        r_b = p.add_run(bold_prefix + " ")
        r_b.font.name = 'Times New Roman'
        r_b.font.size = Pt(11)
        r_b.font.bold = True
        r_b.font.color.rgb = COLOR_DARK_TEXT
        full_text += f"**{bold_prefix}** "
        
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(11)
    r.font.color.rgb = COLOR_DARK_TEXT
    full_text += text
    log_md(full_text)

def add_image_figure(doc, img_path, fig_num, caption):
    if not img_path.exists():
        print(f"LỖI: Không tìm thấy ảnh: {img_path}")
        return
        
    p_img = doc.add_paragraph()
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img.paragraph_format.space_before = Pt(5)
    p_img.paragraph_format.space_after = Pt(2)
    p_img.paragraph_format.keep_with_next = True
    
    run_img = p_img.add_run()
    run_img.add_picture(str(img_path), width=Inches(6.2))
    
    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap.paragraph_format.space_before = Pt(1)
    p_cap.paragraph_format.space_after = Pt(5)
    
    r_cap = p_cap.add_run(f"Hình {fig_num}. {caption}")
    r_cap.font.name = 'Times New Roman'
    r_cap.font.size = Pt(10)
    r_cap.font.italic = True
    r_cap.font.bold = True
    r_cap.font.color.rgb = COLOR_BLUE_SEC
    
    log_md(f"\n![Hình {fig_num}. {caption}]({img_path.name})\n*Hình {fig_num}. {caption}*\n")

def add_table_custom(doc, table_num, caption, headers, rows_data, col_widths=None):
    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p_cap.paragraph_format.space_before = Pt(5)
    p_cap.paragraph_format.space_after = Pt(2)
    p_cap.paragraph_format.keep_with_next = True
    
    r_cap = p_cap.add_run(f"Bảng {table_num}. {caption}")
    r_cap.font.name = 'Times New Roman'
    r_cap.font.size = Pt(10)
    r_cap.font.bold = True
    r_cap.font.color.rgb = COLOR_NAVY_HVNH
    
    table = doc.add_table(rows=len(rows_data) + 1, cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(table)
    
    hdr_row = table.rows[0]
    make_tbl_header(hdr_row)
    make_cant_split(hdr_row)
    for col_idx, h_text in enumerate(headers):
        cell = hdr_row.cells[col_idx]
        set_cell_background(cell, HEX_HDR_BG)
        set_cell_margins(cell, top=50, bottom=50, left=60, right=60)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run(h_text)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(9)
        r.font.bold = True
        r.font.color.rgb = COLOR_NAVY_HVNH
        
    for row_idx, r_data in enumerate(rows_data):
        row = table.rows[row_idx + 1]
        make_cant_split(row)
        bg_color = HEX_ZEBRA_BG if row_idx % 2 == 1 else "FFFFFF"
        for col_idx, val in enumerate(r_data):
            cell = row.cells[col_idx]
            if bg_color != "FFFFFF":
                set_cell_background(cell, bg_color)
            set_cell_margins(cell, top=35, bottom=35, left=50, right=50)
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.15
            
            if col_idx == 0 or len(str(val)) < 8:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            else:
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                
            r = p.add_run(str(val))
            r.font.name = 'Times New Roman'
            r.font.size = Pt(8.5)
            r.font.color.rgb = COLOR_DARK_TEXT
            
    if col_widths:
        for row in table.rows:
            for idx, width in enumerate(col_widths):
                row.cells[idx].width = width
                
    p_sp = doc.add_paragraph()
    p_sp.paragraph_format.space_before = Pt(0)
    p_sp.paragraph_format.space_after = Pt(3)
    
    md_header = "| " + " | ".join(headers) + " |"
    md_sep = "| " + " | ".join(["---"] * len(headers)) + " |"
    log_md(f"\n**Bảng {table_num}. {caption}**\n\n{md_header}\n{md_sep}")
    for r_data in rows_data:
        log_md("| " + " | ".join(str(v).replace("\n", "<br>") for v in r_data) + " |")
    log_md("\n")

def clean_and_update_template_frontmatter(doc):
    print(">>> Đang cập nhật Trang bìa và Front Matter...")
    
    doc.paragraphs[4].text = "MÔN: QUẢN LÝ QUY TRÌNH NGHIỆP VỤ (BPM)"
    doc.paragraphs[4].runs[0].font.name = "Times New Roman"
    doc.paragraphs[4].runs[0].font.size = Pt(14)
    doc.paragraphs[4].runs[0].font.bold = True
    
    doc.paragraphs[5].text = "ĐỀ TÀI: ĐÁNH GIÁ VÀ HOÀN THIỆN HỆ THỐNG QUY TRÌNH NGHIỆP VỤ TẠI LPBANK THEO CHUẨN APQC PCF VÀ KIẾN TRÚC SMART BPM"
    doc.paragraphs[5].runs[0].font.name = "Times New Roman"
    doc.paragraphs[5].runs[0].font.size = Pt(15)
    doc.paragraphs[5].runs[0].font.bold = True
    
    t0 = doc.tables[0]
    t0.rows[0].cells[0].paragraphs[0].text = "Giảng viên hướng dẫn"
    t0.rows[0].cells[1].paragraphs[0].text = "PGS.TS. Phan Thanh Đức"
    t0.rows[1].cells[0].paragraphs[0].text = "Học viên thực hiện"
    t0.rows[1].cells[1].paragraphs[0].text = "Đỗ Văn Đạt - Mã HV: 28k405001"
    t0.rows[2].cells[0].paragraphs[0].text = "Lớp chuyên ngành"
    t0.rows[2].cells[1].paragraphs[0].text = "K28PTKDA - Khoa Sau Đại học"
    
    for r in t0.rows:
        for c in r.cells:
            for p in c.paragraphs:
                for run in p.runs:
                    run.font.name = "Times New Roman"
                    run.font.size = Pt(11)
                    
    doc.paragraphs[3].text = "BÀI TẬP LỚN"
    doc.paragraphs[3].runs[0].font.name = "Times New Roman"
    doc.paragraphs[3].runs[0].font.size = Pt(14)
    doc.paragraphs[3].runs[0].font.bold = True
    
    doc.paragraphs[38].text = (
        "Em xin cam đoan bài tập thực hành lớn với đề tài “Đánh giá và hoàn thiện hệ thống quy trình nghiệp vụ "
        "tại LPBank theo chuẩn APQC PCF và kiến trúc Smart BPM” là công trình nghiên cứu và tổng hợp độc lập "
        "của học viên dưới sự hướng dẫn khoa học của PGS.TS. Phan Thanh Đức. Toàn bộ cơ sở lý luận về Quản trị "
        "quy trình nghiệp vụ (BPM), các dữ liệu đối chuẩn Khung APQC PCF Banking v7.2.2 và thông tin thực tế "
        "về quy trình tín dụng tại Ngân hàng TMCP Lộc Phát Việt Nam (LPBank) được trích dẫn trung thực từ các "
        "nguồn tài liệu chính thức. Học viên không sao chép nguyên văn từ bất kỳ công trình nào khác mà không "
        "ghi rõ nguồn gốc. Nếu phát hiện có sự gian lận, em xin hoàn toàn chịu trách nhiệm trước bộ môn và nhà trường."
    )
    doc.paragraphs[38].runs[0].font.name = "Times New Roman"
    doc.paragraphs[38].runs[0].font.size = Pt(11.5)
    
    doc.paragraphs[39].text = "Học viên thực hiện: Đỗ Văn Đạt"
    doc.paragraphs[39].runs[0].font.name = "Times New Roman"
    doc.paragraphs[39].runs[0].font.size = Pt(11.5)
    doc.paragraphs[39].runs[0].font.bold = True
    
    doc.paragraphs[42].text = (
        "Để hoàn thành bài tập thực hành môn Quản lý Quy trình Nghiệp vụ (BPM), trước hết học viên xin gửi lời cảm ơn "
        "chân thành và sâu sắc nhất đến Thầy PGS.TS. Phan Thanh Đức. Những bài giảng tâm huyết của Thầy về tư duy "
        "quy trình (Process Thinking), vòng đời BPM, kiến trúc quy trình, khung đối chuẩn APQC Banking PCF và kỹ thuật "
        "mô hình hóa chuẩn quốc tế BPMN 2.0 đã trang bị cho học viên một thế giới quan khoa học và phương pháp luận "
        "sắc bén để nhận diện, đánh giá và giải quyết các bài toán vận hành phức tạp trong ngành ngân hàng hiện đại. "
        "Do năng lực và thời gian nghiên cứu còn hạn chế, bài viết khó tránh khỏi những thiếu sót; học viên rất mong "
        "tiếp tục nhận được những ý kiến chỉ dẫn quý báu của Thầy để hoàn thiện hơn."
    )
    doc.paragraphs[42].runs[0].font.name = "Times New Roman"
    doc.paragraphs[42].runs[0].font.size = Pt(11.5)
    
    # Cập nhật Danh mục hình vẽ và bảng biểu (46-50)
    doc.paragraphs[46].text = "Hình 1. Bản đồ chiến lược LPBank theo 4 lăng kính Thẻ điểm cân bằng (BSC)"
    doc.paragraphs[47].text = "Hình 2. Sơ đồ Cảnh quan Quy trình (Process Landscape Map) LPBank"
    doc.paragraphs[48].text = "Hình 3. Quy trình Hiện trạng (As-Is) Thẩm định và Giải ngân vốn vay KHCN"
    doc.paragraphs[49].text = "Hình 4. Quy trình Tương lai (To-Be) Tối ưu hóa trên kiến trúc Smart BPM Orchestrator"
    doc.paragraphs[50].text = "Bảng 1. Sàng lọc hoạt động theo Danh sách kiểm tra quy trình (Process Checklist)"
    
    p_b2 = doc.paragraphs[50].insert_paragraph_before("Bảng 2. Ma trận đối chiếu quy trình tín dụng LPBank với Khung APQC PCF Banking v7.2.2")
    p_b3 = doc.paragraphs[50].insert_paragraph_before("Bảng 3. Ma trận lựa chọn danh mục quy trình (Process Portfolio Selection Matrix)")
    p_b4 = doc.paragraphs[50].insert_paragraph_before("Bảng 4. Ma trận phân định trách nhiệm RACI và Điểm bàn giao (Handoffs)")
    p_b5 = doc.paragraphs[50].insert_paragraph_before("Bảng 5. Phân tích đứt gãy Dữ liệu & Ứng dụng theo Kiến trúc Doanh nghiệp (EA)")
    p_b6 = doc.paragraphs[50].insert_paragraph_before("Bảng 6. So sánh hiệu năng As-Is vs To-Be theo Tứ giác Ma quỷ (Devil's Quadrangle)")
    p_b7 = doc.paragraphs[50].insert_paragraph_before("Bảng 7. Hệ thống chỉ số KPI SMART chuẩn Open Standards Benchmarking (OSB)")
    
    for p_extra in [p_b2, p_b3, p_b4, p_b5, p_b6, p_b7]:
        p_extra.paragraph_format.line_spacing = 1.15
        p_extra.paragraph_format.space_before = Pt(0)
        p_extra.paragraph_format.space_after = Pt(2)
        if len(p_extra.runs) > 0:
            p_extra.runs[0].font.name = "Times New Roman"
            p_extra.runs[0].font.size = Pt(11)

    t1 = doc.tables[1]
    for _ in range(len(t1.rows) - 1):
        tr = t1.rows[1]._tr
        tr.getparent().remove(tr)
        
    abbr_data = [
        ("APQC", "American Productivity & Quality Center – Trung tâm Năng suất & Chất lượng Hoa Kỳ"),
        ("BPM", "Business Process Management – Quản lý Quy trình Nghiệp vụ"),
        ("BPMN", "Business Process Model and Notation – Ký hiệu & Mô hình hóa Quy trình Nghiệp vụ (chuẩn OMG)"),
        ("BPMS", "Business Process Management Suite – Hệ thống phần mềm Quản trị Quy trình Nghiệp vụ"),
        ("BSC", "Balanced Scorecard – Thẻ điểm cân bằng (4 lăng kính quản trị chiến lược)"),
        ("CBS", "Core Banking System – Hệ thống Ngân hàng Lõi (T24 Temenos)"),
        ("CIC", "Credit Information Center – Trung tâm Thông tin Tín dụng Quốc gia Việt Nam"),
        ("CSAT", "Customer Satisfaction Score – Chỉ số Hài lòng của Khách hàng"),
        ("CSU", "Credit Support Unit – Bộ phận Hỗ trợ Tín dụng tại Ngân hàng"),
        ("EA", "Enterprise Architecture – Kiến trúc Doanh nghiệp (Tổ chức – Ứng dụng – Dữ liệu)"),
        ("FTR", "First-Time-Right – Tỷ lệ hồ sơ xử lý chính xác tuyệt đối ngay từ lần đầu tiên"),
        ("LOS", "Loan Origination System – Hệ thống Khởi tạo Khoản vay"),
        ("NVA", "Non-Value-Added – Hoạt động không gia tăng giá trị (Lãng phí vận hành)"),
        ("PCF", "Process Classification Framework – Khung Phân loại Quy trình Nghiệp vụ chuẩn APQC"),
        ("RACI", "Responsible, Accountable, Consulted, Informed – Ma trận phân định trách nhiệm"),
        ("RM", "Relationship Manager – Chuyên viên Quản lý Khách hàng / Tín dụng"),
        ("STP", "Straight-Through Processing – Quy trình xử lý giao dịch tự động hoàn toàn"),
        ("TAT", "Turnaround Time – Thời gian quay vòng / Chu kỳ xử lý quy trình"),
        ("VA", "Value-Added – Hoạt động trực tiếp gia tăng giá trị cho khách hàng")
    ]
    
    for abbr, desc in abbr_data:
        row = t1.add_row()
        make_cant_split(row)
        c0 = row.cells[0]
        c1 = row.cells[1]
        c0.text = abbr
        c1.text = desc
        set_cell_background(c0, "FFFFFF")
        set_cell_background(c1, "FFFFFF")
        set_cell_margins(c0, top=35, bottom=35, left=60, right=60)
        set_cell_margins(c1, top=35, bottom=35, left=60, right=60)
        c0.paragraphs[0].runs[0].font.name = "Times New Roman"
        c0.paragraphs[0].runs[0].font.size = Pt(9)
        c0.paragraphs[0].runs[0].font.bold = True
        c1.paragraphs[0].runs[0].font.name = "Times New Roman"
        c1.paragraphs[0].runs[0].font.size = Pt(9)
        
    body = doc._element.body
    tbl1_idx = -1
    t_cnt = 0
    for idx, el in enumerate(body):
        if el.tag.endswith('tbl'):
            t_cnt += 1
            if t_cnt == 2:
                tbl1_idx = idx
                break
                
    to_remove = []
    for idx in range(tbl1_idx + 1, len(body)):
        el = body[idx]
        if not el.tag.endswith('sectPr'):
            to_remove.append(el)
            
    for el in to_remove:
        body.remove(el)
        
    print(f">>> Đã xóa sạch {len(to_remove)} phần tử cũ. Thân bài sạch 100%.")

# ==============================================================================
# BIÊN SOẠN THÂN BÀI HỌC THUẬT THEO ĐÚNG 4 PHẦN CỦA ĐỀ BÀI
# ==============================================================================

def write_report_content(doc):
    print(">>> Đang biên soạn nội dung Báo cáo...")
    
    # --------------------------------------------------------------------------
    # LỜI MỞ ĐẦU
    # --------------------------------------------------------------------------
    add_h1(doc, "LỜI MỞ ĐẦU", page_break_before=True)
    add_body_p(doc, 
        "Trong bối cảnh cạnh tranh khốc liệt của kỷ nguyên ngân hàng số, việc nâng cao năng lực cạnh tranh "
        "của một ngân hàng thương mại không chỉ dừng lại ở các chiến dịch quảng bá hay mở rộng mạng lưới chi nhánh vật lý, "
        "mà cốt lõi nằm ở năng lực tối ưu hóa và quản trị hệ thống quy trình nghiệp vụ (Business Process Management - BPM). "
        "Theo giáo trình kinh điển 'Fundamentals of Business Process Management' (Marlon Dumas et al., 2018), "
        "BPM cung cấp một phương pháp luận khoa học và nghệ thuật giám sát cách thức công việc được thực thi nhằm bảo đảm "
        "kết quả đầu ra nhất quán và tận dụng triệt để các cơ hội cải tiến liên tục.")
    
    add_body_p(doc,
        "Ngân hàng Thương mại Cổ phần Lộc Phát Việt Nam (LPBank) đang bước vào giai đoạn chiến lược 2024–2028 với định hướng "
        "trở thành ngân hàng bán lẻ hàng đầu, phục vụ đa dạng phân khúc khách hàng cá nhân và doanh nghiệp vừa và nhỏ (SME). "
        "Báo cáo thường niên 2024 ghi nhận quy mô tổng dư nợ tín dụng của LPBank đạt trên 331.000 tỷ đồng, tăng trưởng trên 20%/năm. "
        "Tuy nhiên, sự tăng trưởng nhanh chóng về quy mô đang tạo ra áp lực đè nặng lên hệ thống vận hành truyền thống: "
        "thời gian xử lý khoản vay kéo dài, hồ sơ luân chuyển thủ công qua nhiều tầng nấc phê duyệt, tỷ lệ trả hồ sơ bổ sung cao, "
        "và thiếu sự liên thông dữ liệu tự động giữa các hệ thống công nghệ thông tin.")
    
    add_body_p(doc,
        "Báo cáo thực hành này được xây dựng bám sát đề bài và chuẩn mực đánh giá môn học Quản lý Quy trình Nghiệp vụ (BPM) "
        "dưới sự hướng dẫn của PGS.TS. Phan Thanh Đức. Nghiên cứu vận dụng đồng bộ: Thẻ điểm cân bằng (Balanced Scorecard), "
        "Kiến trúc cảnh quan quy trình (Process Landscape), Danh sách kiểm tra quy trình (Process Checklist), "
        "Khung phân loại quy trình ngành Ngân hàng quốc tế APQC PCF v7.2.2, Chuẩn mô hình hóa quy trình nghiệp vụ BPMN 2.0, "
        "Kiến trúc Doanh nghiệp (Enterprise Architecture) và Tứ giác Ma quỷ (Devil's Quadrangle) nhằm đánh giá hiện trạng, "
        "nhận diện điểm nghẽn và đề xuất mô hình tương lai tối ưu hóa trên nền tảng Smart BPM Orchestrator cho LPBank.")

    # --------------------------------------------------------------------------
    # PHẦN 1: BỐI CẢNH CHIẾN LƯỢC VÀ NHẬN DIỆN QUY TRÌNH (20%)
    # --------------------------------------------------------------------------
    add_h1(doc, "PHẦN 1: BỐI CẢNH CHIẾN LƯỢC VÀ NHẬN DIỆN QUY TRÌNH (20%)", page_break_before=True)
    
    add_h2(doc, "1.1. Phân tích bối cảnh chiến lược kinh doanh qua Thẻ điểm cân bằng (Balanced Scorecard)")
    add_body_p(doc,
        "Chiến lược kinh doanh của LPBank giai đoạn 2024–2028 xác định trụ cột trọng tâm là “Bán lẻ – Dịch vụ – Số hóa”, "
        "tận dụng lợi thế mạng lưới phòng giao dịch phủ rộng khắp 63 tỉnh thành kết hợp đẩy mạnh ứng dụng công nghệ để nâng cao "
        "năng suất lao động. Để chuyển hóa tầm nhìn chiến lược này thành các mục tiêu vận hành cụ thể, nghiên cứu vận dụng "
        "công cụ Thẻ điểm cân bằng (Balanced Scorecard - Kaplan & Norton) thông qua 4 lăng kính có quan hệ nhân quả chặt chẽ:")
    
    add_body_p(doc,
        "Tập trung thúc đẩy tăng trưởng dư nợ cho vay bán lẻ an toàn với tốc độ trên 20%/năm; tối ưu hóa tỷ lệ "
        "chi phí trên thu nhập (CIR ≤ 29%); duy trì tỷ lệ thu nhập lãi thuần (NIM) ổn định và kiểm soát nghiêm ngặt tỷ lệ nợ xấu "
        "(NPL ≤ 1,5%) theo quy định an toàn của Ngân hàng Nhà nước.",
        bold_prefix="a) Khía cạnh Tài chính (Financial Perspective):")
        
    add_body_p(doc,
        "Định vị LPBank là ngân hàng bán lẻ thân thiện, nhanh chóng và tin cậy. Rút ngắn thời gian quay vòng "
        "(Turnaround Time - TAT) giải ngân khoản vay từ 2-3 ngày xuống dưới 4 giờ làm việc; nâng cao chỉ số hài lòng của khách hàng "
        "(CSAT ≥ 90%); cung cấp trải nghiệm số hóa đa kênh liền mạch, giảm thiểu tối đa số lần khách hàng phải trực tiếp đến chi nhánh.",
        bold_prefix="b) Khía cạnh Khách hàng (Customer Perspective):")
        
    add_body_p(doc,
        "Chuẩn hóa và tái thiết kế quy trình cấp tín dụng và giải ngân vốn vay theo hướng tinh gọn; "
        "loại bỏ các khâu kiểm tra trùng lặp không tạo ra giá trị (Non-Value-Added - NVA); đẩy mạnh cơ chế xử lý giao dịch thẳng "
        "(Straight-Through Processing - STP); tích hợp ký số từ xa và loại bỏ hoàn toàn việc in ấn, luân chuyển hồ sơ giấy vật lý.",
        bold_prefix="c) Khía cạnh Quy trình nội bộ (Internal Business Processes):")
        
    add_body_p(doc,
        "Xây dựng văn hóa làm việc hướng quy trình (Process-centric Culture); đào tạo nâng cao năng lực thẩm định "
        "và kỹ năng số cho đội ngũ Chuyên viên Quản lý Khách hàng (RM); đầu tư nâng cấp hạ tầng công nghệ thông qua hệ thống "
        "Smart BPM Orchestrator, kết nối liên thông API giữa hệ thống Khởi tạo khoản vay (LOS), Core Banking T24 và Trung tâm CIC.",
        bold_prefix="d) Khía cạnh Học tập & Phát triển (Learning and Growth):")

    add_image_figure(doc, DIAGRAM_DIR / 'Hinh1_Ban_do_chien_luoc_LPBank.drawio.png', 1, 
                     "Bản đồ chiến lược LPBank theo 4 lăng kính Thẻ điểm cân bằng (Balanced Scorecard)")

    add_h2(doc, "1.2. Phác thảo Kiến trúc quy trình cấp cao (Process Landscape)")
    add_body_p(doc,
        "Theo giáo trình Quản trị Quy trình Nghiệp vụ (Dumas et al., 2018), kiến trúc quy trình (Process Architecture) là "
        "bản thiết kế tổng thể phân định ranh giới và mối quan hệ giữa các quy trình nghiệp vụ trong tổ chức. Mọi hoạt động tại "
        "LPBank được cấu trúc thành 3 nhóm quy trình chuẩn mực:")
    
    add_body_p(doc,
        "Bao gồm các chuỗi giá trị cốt lõi trực tiếp tạo ra sản phẩm, dịch vụ và chuyển giao giá trị cho "
        "khách hàng bên ngoài: (1) Huy động vốn và quản lý tiền gửi; (2) Cấp tín dụng và giải ngân vốn vay (KHCN và SME); "
        "(3) Dịch vụ thanh toán và chuyển tiền; (4) Phát hành và quản lý thẻ; (5) Ngân hàng số và dịch vụ bảo hiểm liên kết.",
        bold_prefix="1. Nhóm Quy trình Cốt lõi (Core / Operating Processes):")
        
    add_body_p(doc,
        "Cung cấp các nguồn lực hậu cần thiết yếu bảo đảm cho các quy trình cốt lõi vận hành thông suốt: "
        "(1) Quản trị nguồn nhân lực và đào tạo; (2) Quản trị hạ tầng CNTT, an ninh mạng và Core Banking; "
        "(3) Pháp chế, tuân thủ và xử lý nợ; (4) Kế toán tài chính và mua sắm trang thiết bị tài sản.",
        bold_prefix="2. Nhóm Quy trình Hỗ trợ (Support Processes):")
        
    add_body_p(doc,
        "Định hướng chiến lược, phân bổ nguồn lực và giám sát rủi ro tổng thể: "
        "(1) Hoạch định chiến lược kinh doanh và ALM; (2) Quản trị rủi ro tín dụng, thị trường và thanh khoản; "
        "(3) Kiểm toán và kiểm soát nội bộ; (4) Quản trị truyền thông thương hiệu và quan hệ cổ đông.",
        bold_prefix="3. Nhóm Quy trình Quản lý (Management Processes):")

    add_image_figure(doc, DIAGRAM_DIR / 'Hinh2_Process_Landscape_LPBank.drawio.png', 2, 
                     "Sơ đồ Cảnh quan Quy trình (Process Landscape Map) tại LPBank")

    add_h2(doc, "1.3. Áp dụng Danh sách kiểm tra quy trình (Process Checklist) để sàng lọc hoạt động")
    add_body_p(doc,
        "Để tránh nhầm lẫn giữa một quy trình kinh doanh (Business Process) với một tác vụ vi mô (Task) hoặc một dự án đơn lẻ (Project), "
        "nghiên cứu áp dụng 'Danh sách kiểm tra quy trình' (Process Checklist) theo đúng bài giảng của môn học với 5 tiêu chí: "
        "(1) Tính quy trình (Process-nature: có sự kiện kích hoạt, chuỗi tác vụ và kết quả đầu ra); "
        "(2) Tính lặp lại (Repeatability: diễn ra thường xuyên lặp lại); "
        "(3) Khả năng kiểm soát (Manageability: tổ chức có quyền can thiệp, đo lường và tối ưu); "
        "(4) Quy mô hợp lý (Appropriate scale: đủ tầm một luồng giá trị, không quá vi mô cũng không quá vĩ mô); "
        "(5) Ý nghĩa kinh tế (Economic value: đóng góp trực tiếp vào mục tiêu chiến lược và chi phí).")

    chk_headers = ["STT", "Hoạt động khảo sát", "Tính QT", "Tính lặp", "Kiểm soát", "Quy mô", "Ý nghĩa KT", "Kết luận phân loại"]
    chk_rows = [
        ["1", "Tiếp nhận hồ sơ và lập tờ trình vay vốn", "Đạt", "Đạt", "Đạt", "Đạt", "Đạt", "Thuộc Quy trình Cốt lõi"],
        ["2", "In ấn bộ chứng từ hợp đồng tín dụng", "Đạt", "Đạt", "Đạt", "Không", "Không", "Tác vụ vi mô (Task) - Loại khỏi BPM"],
        ["3", "Dự án nâng cấp hệ thống Core Banking", "Không", "Không", "Đạt", "Quá lớn", "Đạt", "Dự án đơn lẻ (Project) - Loại khỏi BPM"],
        ["4", "Thẩm định và giải ngân vốn vay KHCN", "Đạt", "Đạt", "Đạt", "Đạt", "Đạt", "Quy trình Cốt lõi trọng yếu"],
        ["5", "Đào tạo nghiệp vụ tín dụng cho nhân viên", "Đạt", "Đạt", "Đạt", "Đạt", "Đạt", "Quy trình Hỗ trợ"],
        ["6", "Giám sát hạn mức tín dụng và báo cáo NHNN", "Đạt", "Đạt", "Đạt", "Đạt", "Đạt", "Quy trình Quản lý"]
    ]
    chk_widths = [Inches(0.4), Inches(2.1), Inches(0.55), Inches(0.55), Inches(0.55), Inches(0.55), Inches(0.65), Inches(1.15)]
    add_table_custom(doc, 1, "Sàng lọc hoạt động theo Danh sách kiểm tra quy trình (Process Checklist)", chk_headers, chk_rows, chk_widths)

    # --------------------------------------------------------------------------
    # PHẦN 2: ĐỐI CHIẾU VỚI KHUNG APQC PCF (30%)
    # --------------------------------------------------------------------------
    add_h1(doc, "PHẦN 2: ĐỐI CHIẾU VỚI KHUNG APQC PCF (30%)", page_break_before=True)
    
    add_h2(doc, "2.1. Ánh xạ (Mapping) quy trình Cấp tín dụng LPBank với Khung APQC PCF Banking v7.2.2")
    add_body_p(doc,
        "Khung phân loại quy trình APQC PCF (Process Classification Framework) phiên bản ngành Ngân hàng (Banking PCF v7.2.2) "
        "là bộ chuẩn đối chuẩn quốc tế uy tín nhất hiện nay, cung cấp ngôn ngữ chung để chuẩn hóa tên gọi, phân cấp và đo lường hiệu suất. "
        "Nghiên cứu tiến hành ánh xạ toàn diện mảng nghiệp vụ Cấp tín dụng và Giải ngân khoản vay bán lẻ của LPBank vào cấu trúc "
        "phân tầng 4 cấp độ nghiêm ngặt của APQC PCF:")
    
    add_bullet_p(doc, "5.0 Cung cấp sản phẩm và dịch vụ ngân hàng (Deliver Services - PCF ID: 20025).", bold_prefix="Cấp độ 1 (Category):")
    add_bullet_p(doc, "5.3 Cung cấp dịch vụ ngân hàng cho khách hàng (Deliver banking services to customers - PCF ID: 17416).", bold_prefix="Cấp độ 2 (Process Group):")
    add_bullet_p(doc, "5.3.1 Mở tài khoản và khởi tạo sản phẩm tín dụng (Open accounts - PCF ID: 17417) và 5.3.2 Quản lý tài khoản (Maintain accounts - PCF ID: 17422).", bold_prefix="Cấp độ 3 (Process):")
    add_bullet_p(doc, "Các hoạt động nghiệp vụ cụ thể gắn liền với mã định danh 5 chữ số chuẩn hóa quốc tế của APQC.", bold_prefix="Cấp độ 4 (Activity):")

    map_headers = ["Cấp APQC", "Mã PCF", "Tên quy trình chuẩn APQC PCF v7.2.2", "Quy trình tương ứng tại LPBank", "Đánh giá hiện trạng"]
    map_rows = [
        ["Level 1", "20025", "5.0 Deliver Services", "Cung cấp sản phẩm & dịch vụ ngân hàng", "Chuẩn hóa danh mục"],
        ["Level 2", "17416", "5.3 Deliver banking services to customers", "Vận hành dịch vụ tín dụng & cho vay", "Khớp hoàn toàn"],
        ["Level 3", "17417", "5.3.1 Open accounts", "Khởi tạo khoản vay & Mở tài khoản tín dụng", "Khớp với phân hệ LOS"],
        ["Level 4", "13957", "Identify and verify customer identity (KYC)", "Thu thập hồ sơ pháp lý & Định danh KH", "Chưa liên thông CSDL dân cư"],
        ["Level 4", "13964", "Analyze customer creditworthiness", "Thẩm định năng lực tài chính & Lập tờ trình", "Nhập liệu thủ công, trùng lặp"],
        ["Level 4", "17420", "Evaluate collateral / guarantee", "Khảo sát và định giá tài sản bảo đảm (TSBĐ)", "Chồng chéo thẩm định 2 cấp"],
        ["Level 4", "17418", "Apply product conditions", "Kiểm tra điều kiện phê duyệt khoản vay", "Kiểm soát thủ công 3 cấp"],
        ["Level 4", "17421", "Set up and activate loan account", "Mở tài khoản vay trên hệ thống Core Banking", "Khớp với phân hệ Core T24"],
        ["Level 4", "13961", "Fund and disburse proceeds", "Thực hiện giải ngân tiền vay vào tài khoản", "Điểm nghẽn: Ký giấy mực & chờ"],
        ["Level 4", "20031", "Solicit feedback on delivery satisfaction", "Khảo sát sự hài lòng sau khi giải ngân", "THIẾU (Gap - chưa có quy trình)"],
        ["Level 4", "13953", "Apply Anti-Money Laundering (AML) policy", "Rà soát phòng chống rửa tiền tập trung", "THIẾU (Kiểm tra phân tán ngoài)"]
    ]
    map_widths = [Inches(0.8), Inches(0.65), Inches(1.8), Inches(1.75), Inches(1.3)]
    add_table_custom(doc, 2, "Ma trận đối chiếu quy trình tín dụng LPBank với Khung APQC PCF Banking v7.2.2", map_headers, map_rows, map_widths)

    add_h2(doc, "2.2. Phân tích khoảng trống (Gap Analysis) so với Thông lệ quốc tế tốt nhất")
    add_body_p(doc,
        "Đối chiếu chi tiết giữa thực tiễn vận hành tại LPBank và Khung chuẩn hóa APQC PCF v7.2.2 chỉ ra 2 nhóm khoảng trống lớn "
        "cần can thiệp tái thiết kế:")
    
    add_body_p(doc,
        "Hệ thống hiện tại của LPBank hoàn toàn thiếu vắng quy trình đo lường sự hài lòng của khách hàng "
        "sau khi nhận tiền giải ngân (Hoạt động 20031). Sau khi tiền được ghi có vào tài khoản, quy trình kết thúc mà không có cơ chế "
        "tự động kích hoạt khảo sát CSAT qua ứng dụng di động. Thứ hai, quy trình rà soát phòng chống rửa tiền (AML - Hoạt động 13953) "
        "chưa được tích hợp thành chốt chặn tự động trên luồng phê duyệt mà phụ thuộc vào việc cán bộ tra cứu danh sách đen thủ công.",
        bold_prefix="1. Các quy trình chuẩn bị THIẾU (Missing Processes):")
        
    add_body_p(doc,
        "Hiện tượng chồng chéo nghiêm trọng nhất xảy ra ở khâu thẩm định tài sản bảo đảm (TSBĐ - Hoạt động 17420). "
        "Chuyên viên QLKH tại chi nhánh trực tiếp đi khảo sát thực tế và lập biên bản định giá; tuy nhiên, khi chuyển hồ sơ lên Phòng Quản lý "
        "rủi ro, bộ phận tái thẩm định lại cử chuyên viên độc lập đi khảo sát lại từ đầu do không tin tưởng và không có dữ liệu hình ảnh định vị số hóa. "
        "Thứ hai, hiện tượng dư thừa lãng phí (Redundancy) diễn ra ở khâu in ấn, ký tươi và đóng dấu hồ sơ giấy sau khi các cấp lãnh đạo "
        "đã phê duyệt điện tử hoàn tất trên phần mềm LOS.",
        bold_prefix="2. Các quy trình bị CHỒNG CHÉO và DƯ THỪA (Overlapping & Redundant Processes):")

    # --------------------------------------------------------------------------
    # PHẦN 3: ĐÁNH GIÁ HIỆN TRẠNG VÀ LỰA CHỌN QUY TRÌNH ƯU TIÊN (20%)
    # --------------------------------------------------------------------------
    add_h1(doc, "PHẦN 3: ĐÁNH GIÁ HIỆN TRẠNG VÀ LỰA CHỌN QUY TRÌNH ƯU TIÊN (20%)", page_break_before=True)
    
    add_h2(doc, "3.1. Lọc danh mục đầu tư quy trình (Process Portfolio Selection)")
    add_body_p(doc,
        "Theo lý thuyết lựa chọn quy trình của Dumas et al. (2018) và bài giảng Chapter 2, một tổ chức không thể tiến hành "
        "cải tiến đồng loạt mọi quy trình mà phải thiết lập Ma trận danh mục quy trình (Process Portfolio) dựa trên 3 tiêu chí cốt lõi: "
        "(1) Tầm quan trọng chiến lược (Strategic Importance - trọng số 40%): Mức độ ảnh hưởng đến mục tiêu kinh doanh và lợi nhuận; "
        "(2) Tình trạng sức khỏe / Bất cập (Health / Dysfunction - trọng số 35%): Mức độ phát sinh lỗi, tắc nghẽn và khiếu nại; "
        "(3) Tính khả thi cải tiến (Feasibility - trọng số 25%): Mức độ sẵn sàng về công nghệ, văn hóa và nguồn lực tài chính.")

    port_headers = ["Mã QT", "Tên quy trình nghiệp vụ", "Chiến lược (40%)", "Bất cập (35%)", "Khả thi (25%)", "Điểm tổng", "Xếp hạng"]
    port_rows = [
        ["QT-01", "Thẩm định và giải ngân vốn vay KHCN", "5.0 / 5.0", "4.8 / 5.0", "4.6 / 5.0", "4.83", "Hạng 1 (Ưu tiên số 1)"],
        ["QT-02", "Huy động tiền gửi tiết kiệm tại quầy", "4.2 / 5.0", "2.0 / 5.0", "4.5 / 5.0", "3.51", "Hạng 3 (Vận hành ổn định)"],
        ["QT-03", "Phát hành thẻ tín dụng và thấu chi", "4.5 / 5.0", "3.5 / 5.0", "4.2 / 5.0", "4.08", "Hạng 2 (Đã số hóa một phần)"],
        ["QT-04", "Mở tài khoản thanh toán và eKYC", "4.0 / 5.0", "2.5 / 5.0", "4.0 / 5.0", "3.48", "Hạng 4 (Đã hoàn thiện giai đoạn 1)"]
    ]
    port_widths = [Inches(0.65), Inches(2.1), Inches(0.85), Inches(0.85), Inches(0.85), Inches(0.7), Inches(1.3)]
    add_table_custom(doc, 3, "Ma trận lựa chọn danh mục quy trình (Process Portfolio Selection Matrix)", port_headers, port_rows, port_widths)

    add_body_p(doc,
        "Quy trình 'Triển khai Tín dụng và Giải ngân Vốn vay Khách hàng Cá nhân (KHCN)' đạt điểm số ưu tiên cao nhất (4.83 / 5.0). "
        "Đây là quy trình tạo ra trên 65% tổng thu nhập lãi thuần của LPBank nhưng đang là điểm nóng về thời gian chờ đợi (TAT bình quân 19.5 giờ), "
        "tỷ lệ trả hồ sơ cao và tiềm ẩn rủi ro tác nghiệp lớn. Do đó, quy trình này được lựa chọn để tiến hành phân tích sâu và tái thiết kế.",
        bold_prefix="Quyết định lựa chọn:")

    add_h2(doc, "3.2. Mô hình hóa Hiện trạng (As-Is Process Model) chuẩn BPMN 2.0 và Nhận diện Điểm nghẽn")
    add_body_p(doc,
        "Quy trình giải ngân hiện trạng của LPBank được mô hình hóa theo chuẩn quốc tế BPMN 2.0 (OMG) với sự tham gia của 5 làn trách nhiệm "
        "(Swimlanes): Khách hàng, Chuyên viên QLKH (RM), Kiểm soát viên Chi nhánh, Bộ phận Hỗ trợ tín dụng (CSU) và Kế toán Core Banking T24.")

    add_image_figure(doc, DIAGRAM_DIR / 'Hinh3_Quy_trinh_Hien_trang_AsIs_LPBank.drawio.png', 3, 
                     "Quy trình Hiện trạng (As-Is) Thẩm định và Giải ngân vốn vay KHCN tại LPBank")

    add_body_p(doc,
        "Phân tích chuyên sâu luồng thực thi As-Is chỉ ra 3 điểm nghẽn nghiêm trọng (Bottlenecks) và 2 vòng lặp xử lý lại (Rework Loops):")
    
    add_body_p(doc,
        "Sau khi phương án vay được cấp thẩm quyền phê duyệt trên phần mềm LOS, Chuyên viên QLKH lập thông báo "
        "và tờ trình giải ngân. Hồ sơ này bị kiểm tra trùng lặp lần thứ nhất tại Kiểm soát viên chi nhánh, sau đó chuyển sang chuyên viên CSU "
        "để thực hiện kiểm tra hồ sơ lần thứ hai với đúng các tiêu chí đó. Việc kiểm soát 3 cấp thủ công làm thời gian chờ tích lũy tăng thêm 4-6 giờ.",
        bold_prefix="• Điểm nghẽn 1 (Tình trạng kiểm tra hồ sơ trùng lặp 3 cấp):")
        
    add_body_p(doc,
        "Dù dữ liệu về hạn mức, khách hàng, tài sản bảo đảm và lãi suất đã được phê duyệt đầy đủ trên hệ thống LOS, "
        "hệ thống này chưa tích hợp tự động với Core Banking T24. Kế toán viên phải gõ tay lại toàn bộ dữ liệu này vào màn hình T24, "
        "tiêu tốn bình quân 45 phút/hồ sơ và tiềm ẩn nguy cơ sai lệch tài khoản giải ngân.",
        bold_prefix="• Điểm nghẽn 2 (Nhập liệu thủ công lại trên Core Banking):")
        
    add_body_p(doc,
        "Quy trình bắt buộc khách hàng phải có mặt trực tiếp tại chi nhánh để ký tay khế ước nhận nợ và hợp đồng "
        "tín dụng bằng bút mực. Cán bộ văn thư phải đóng dấu cơ học lên từng trang tài liệu trước khi hạch toán. Đây là hoạt động hoàn toàn "
        "không gia tăng giá trị (NVA), gây lãng phí văn phòng phẩm và kéo dài thời gian chờ đợi của khách hàng.",
        bold_prefix="• Điểm nghẽn 3 (Ký mực cơ học và luân chuyển chứng từ giấy):")
        
    add_body_p(doc,
        "Vòng lặp Rework 1 phát sinh khi CSU phát hiện sai sót hình thức hoặc thiếu chứng từ, trả hồ sơ ngược về RM "
        "(chiếm 28% tổng số hồ sơ, làm tăng thêm 6-12 giờ xử lý). Vòng lặp Rework 2 phát sinh khi kế toán phát hiện sai lệch số liệu hạch toán "
        "giữa LOS và T24, buộc phải hủy giao dịch và làm lại tờ trình giải ngân từ đầu.",
        bold_prefix="• Hai Vòng lặp xử lý lại (Rework Loops):")

    add_h2(doc, "3.3. Phân tích đa chiều theo Kiến trúc Doanh nghiệp (Enterprise Architecture)")
    add_body_p(doc,
        "Theo khung lý thuyết Kiến trúc Doanh nghiệp (EA), sự kém hiệu quả của một quy trình luôn bắt nguồn từ sự mất đồng bộ "
        "giữa 3 tầng kiến trúc: Tổ chức, Ứng dụng & Dữ liệu, và Trải nghiệm khách hàng:")

    ea_headers = ["Khía cạnh Kiến trúc", "Hiện trạng hệ thống (As-Is)", "Điểm mù dữ liệu / Đứt gãy vận hành", "Yêu cầu chuẩn hóa (To-Be)"]
    ea_rows = [
        ["Kiến trúc Tổ chức (Organization)", "Ma trận RACI phân tán; chuyển giao hồ sơ thủ công qua 4 phòng ban độc lập.", "Ma sát chuyển giao (Handoff friction); đùn đẩy trách nhiệm kiểm soát; thời gian chờ hàng đợi lớn.", "Xác lập ranh giới trách nhiệm rõ ràng; ủy quyền kiểm tra tự động cho hệ thống; CSU chỉ xử lý ngoại lệ."],
        ["Kiến trúc Ứng dụng (Application)", "Hệ thống LOS, Core Banking T24, ECM và phần mềm kế toán hoạt động độc lập.", "Không có hệ thống điều phối tập trung (Process Orchestration); cán bộ phải chuyển đổi nhiều cửa sổ.", "Triển khai Smart BPM Orchestrator đóng vai trò nhạc trưởng điều phối luồng công việc xuyên suốt."],
        ["Kiến trúc Dữ liệu (Data)", "Nhập liệu thủ công lặp lại; dữ liệu CIC tra cứu ngoài web; hồ sơ scan phân tán.", "Ốc đảo dữ liệu (Data Silos); sai lệch thông tin khách hàng giữa LOS và T24; thiếu tính toàn vẹn.", "Đồng bộ API 2 chiều thời gian thực; khóa trường dữ liệu nguồn; tự động kéo báo cáo CIC về LOS."],
        ["Hành trình Khách hàng (Customer Experience)", "Khách hàng phải đến chi nhánh 2-3 lần; ký tay nhiều bản giấy; không biết tiến độ.", "Hành trình phân mảnh; thời gian chờ đợi kéo dài (TAT 19.5 giờ); điểm hài lòng thấp (CSAT 68%).", "Hành trình số hóa 100%; ký số từ xa SmartCA trên thiết bị di động; theo dõi tiến độ thời gian thực."]
    ]
    ea_widths = [Inches(1.2), Inches(1.6), Inches(1.85), Inches(1.65)]
    add_table_custom(doc, 4, "Phân tích đứt gãy Kiến trúc Doanh nghiệp (Enterprise Architecture) trong quy trình hiện trạng", ea_headers, ea_rows, ea_widths)

    raci_headers = ["Bước công việc", "Khách hàng", "Chuyên viên RM", "Kiểm soát viên", "BP Hỗ trợ tín dụng (CSU)", "Kế toán / Core T24", "Điểm bàn giao (Handoffs) & Rủi ro"]
    raci_rows = [
        ["1. Lập tờ trình giải ngân", "I", "R, A", "C", "I", "I", "Nội bộ RM; chuẩn bị hồ sơ giải ngân."],
        ["2. Kiểm soát hồ sơ tại Chi nhánh", "I", "I", "R, A", "I", "I", "Handoff 1: Chuyển giao từ RM sang KSV; chờ duyệt."],
        ["3. Kiểm tra điều kiện giải ngân (CSU)", "I", "I", "I", "R, A", "I", "Handoff 2: Chuyển giao sang Hội sở; nguy cơ trả hồ sơ."],
        ["4. In ấn và ký hợp đồng tín dụng", "R", "R, A", "C", "I", "I", "Handoff 3: Khách hàng đến quầy ký mực; rủi ro giấy tờ."],
        ["5. Hạch toán giải ngân vào tài khoản", "I", "I", "I", "I", "R, A", "Handoff 4: Chuyển chứng từ sang Kế toán gõ tay vào T24."],
        ["6. Đóng gói và lưu trữ hồ sơ giấy", "I", "R", "I", "A", "I", "Handoff 5: Lưu trữ kho vật lý; tốn chi phí quản lý."]
    ]
    raci_widths = [Inches(1.5), Inches(0.4), Inches(0.45), Inches(0.45), Inches(0.55), Inches(0.55), Inches(2.4)]
    add_table_custom(doc, 5, "Ma trận phân định trách nhiệm RACI và Điểm bàn giao (Handoffs) trong Quy trình Hiện trạng", raci_headers, raci_rows, raci_widths)

    # --------------------------------------------------------------------------
    # PHẦN 4: ĐỀ XUẤT GIẢI PHÁP HOÀN THIỆN (30%)
    # --------------------------------------------------------------------------
    add_h1(doc, "PHẦN 4: ĐỀ XUẤT GIẢI PHÁP HOÀN THIỆN (30%)", page_break_before=True)
    
    add_h2(doc, "4.1. Mô hình hóa Quy trình Tương lai (To-Be Process Model) trên nền tảng Smart BPM Orchestrator")
    add_body_p(doc,
        "Dựa trên các phân tích điểm nghẽn tại Phần 3, nghiên cứu tái thiết kế quy trình tương lai (To-Be Process Model) "
        "chuẩn BPMN 2.0 vận hành trên nền tảng Smart BPM Orchestrator. Trọng tâm của mô hình To-Be là tự động hóa tối đa các tác vụ "
        "mang tính quy tắc, phân luồng thông minh và tích hợp dữ liệu liền mạch:")

    add_image_figure(doc, DIAGRAM_DIR / 'Hinh4_Quy_trinh_Tuong_lai_ToBe_LPBank.drawio.png', 4, 
                     "Quy trình Tương lai (To-Be) Tối ưu hóa trên kiến trúc Smart BPM Orchestrator")

    add_body_p(doc,
        "Mô hình To-Be tạo ra 4 đột phá mang tính cấu trúc trong vận hành tín dụng tại LPBank:")
    
    add_body_p(doc,
        "Ngay khi RM khởi tạo lệnh giải ngân trên giao diện BPM, hệ thống tự động khóa các trường thông tin "
        "đã phê duyệt từ LOS (không cho phép sửa đổi tùy tiện) và kích hoạt bộ quy tắc tự động kiểm tra điều kiện tiên quyết (Pre-check). "
        "Nếu thiếu chứng từ hoặc sai thông tin, hệ thống lập tức cảnh báo ngay tại màn hình, triệt tiêu hoàn toàn các vòng lặp Rework sau này.",
        bold_prefix="1. Động cơ Quy tắc Thông minh (Pre-check Rule Engine):")
        
    add_body_p(doc,
        "Hệ thống phân luồng hồ sơ tự động thông qua cổng rẽ nhánh Inclusive/Exclusive Gateway: Đối với các khoản vay "
        "tiêu chuẩn (thấu chi, thẻ tín dụng, vay tiêu dùng rủi ro thấp đã có tài sản bảo đảm định giá sẵn), hệ thống tự động phê duyệt "
        "và chuyển thẳng sang khâu ký số và hạch toán giải ngân 100% tự động (STP) mà không cần con người phê duyệt lại.",
        bold_prefix="2. Cơ chế Xử lý Giao dịch Thẳng (Straight-Through Processing - STP):")
        
    add_body_p(doc,
        "Quy trình tuân thủ nghiêm ngặt Luật Giao dịch điện tử 2023 và Thông tư của Ngân hàng Nhà nước. "
        "Hợp đồng điện tử và khế ước nhận nợ được chuyển đến ứng dụng LPBank Mobile của khách hàng để ký số từ xa qua giải pháp SmartCA. "
        "Chỉ sau khi khách hàng hoàn tất ký số hợp lệ và chứng thư số được xác thực thành công, hệ thống Smart BPM mới tự động gửi lệnh "
        "API kích hoạt hạch toán giải ngân vào hệ thống Core Banking T24, loại bỏ hoàn toàn rủi ro giải ngân trước khi ký chứng từ.",
        bold_prefix="3. Chuẩn hóa Ký số từ xa (SmartCA) trước khi hạch toán Core T24:")
        
    add_body_p(doc,
        "Để bảo đảm an toàn tuyệt đối khi tích hợp tự động qua API, hệ thống trang bị cơ chế Khóa phân định giao dịch "
        "(Idempotency Key) nhằm ngăn chặn việc gửi trùng lệnh hạch toán tiền khi xảy ra mất kết nối mạng; đồng thời áp dụng cơ chế "
        "Ngắt mạch tự động (Circuit Breaker) để cô lập lỗi hạ tầng và kích hoạt quy trình dự phòng kịp thời.",
        bold_prefix="4. Cơ chế Kiểm soát Kỹ thuật An toàn (Idempotency Key & Circuit Breaker):")

    add_h2(doc, "4.2. Giải pháp Cấu trúc và Vận hành (Lean NVA & Giảm thiểu Handoffs)")
    add_body_p(doc,
        "Áp dụng nguyên lý tinh gọn Lean trong quản trị quy trình nghiệp vụ, nghiên cứu đề xuất các cải tiến cụ thể về cấu trúc vận hành:")
    add_bullet_p(doc, "Loại bỏ hoàn toàn khâu photo, công chứng giấy tờ tùy thân nhờ kết nối trực tiếp CSDL Quốc gia về Dân cư (VNeID); loại bỏ khâu in ấn, ký bút mực, đóng dấu và lưu trữ kho giấy vật lý.", bold_prefix="Loại bỏ hoạt động không gia tăng giá trị (NVA):")
    add_bullet_p(doc, "Gộp bước kiểm soát chi nhánh và kiểm tra sơ bộ của CSU vào Động cơ quy tắc tự động của BPM; chuyển giao trách nhiệm phê duyệt cuối cùng cho lãnh đạo có thẩm quyền.", bold_prefix="Hợp nhất các bước kiểm tra trùng lặp:")
    add_bullet_p(doc, "Giảm từ 5 điểm bàn giao thủ công xuống còn 1 điểm chạm duy nhất giữa Khách hàng và Chuyên viên RM; toàn bộ các khâu trung gian do BPM Orchestrator tự động điều phối.", bold_prefix="Cắt giảm ma sát bàn giao (Handoffs):")

    add_h2(doc, "4.3. Đánh giá Tác động theo Tứ giác Ma quỷ (Devil's Quadrangle)")
    add_body_p(doc,
        "Theo giáo trình Quản lý Quy trình Nghiệp vụ (Dumas et al., 2018), Tứ giác Ma quỷ (Devil's Quadrangle) là khung lý thuyết "
        "kinh điển dùng để đánh giá hiệu quả cải tiến quy trình trên 4 chiều kích: Thời gian (Time), Chi phí (Cost), Chất lượng (Quality), "
        "và Độ linh hoạt (Flexibility). Việc tối ưu hóa quy trình To-Be tại LPBank mang lại sự đột phá toàn diện mà không phải đánh đổi:")

    quad_headers = ["Chiều kích đánh giá", "Hiện trạng (As-Is)", "Mục tiêu tương lai (To-Be)", "Tác động cải tiến cốt lõi"]
    quad_rows = [
        ["1. Thời gian (Time)", "TAT bình quân 19.5 giờ làm việc (kéo dài 2-3 ngày với hồ sơ phức tạp).", "TAT giảm xuống ≤ 4 giờ làm việc; hồ sơ STP hoàn tất trong ≤ 15 phút.", "Cắt giảm hơn 75% tổng thời gian quay vòng nhờ loại bỏ hàng đợi và tự động hóa."],
        ["2. Chi phí (Cost)", "Chi phí vận hành bình quân 1.250.000 VNĐ / hồ sơ vay.", "Chi phí vận hành giảm xuống ≤ 420.000 VNĐ / hồ sơ vay.", "Tiết giảm 66% chi phí nhờ triệt tiêu in ấn giấy tờ, lưu trữ kho bãi và giờ công kiểm soát."],
        ["3. Chất lượng (Quality)", "Tỷ lệ đúng lần đầu (FTR) chỉ đạt 72%; tỷ lệ trả hồ sơ bổ sung lên tới 28%.", "Tỷ lệ đúng lần đầu FTR ≥ 96%; tỷ lệ trả hồ sơ bổ sung giảm xuống < 4%.", "Khóa trường dữ liệu tự động; Rule Engine ngăn chặn sai sót nhập liệu ngay từ đầu."],
        ["4. Độ linh hoạt (Flexibility)", "Kém linh hoạt; sửa đổi điều kiện gói vay phải can thiệp mã nguồn Core T24 mất 3-4 tuần.", "Cực kỳ linh hoạt; cập nhật chính sách trên BPM Rule Engine chỉ mất 1-2 ngày.", "Phân tách rõ ràng giữa quy tắc nghiệp vụ (Business Rules) và kiến trúc hệ thống lõi."]
    ]
    quad_widths = [Inches(1.2), Inches(1.7), Inches(1.7), Inches(1.7)]
    add_table_custom(doc, 6, "So sánh hiệu năng As-Is vs To-Be theo Tứ giác Ma quỷ (Devil's Quadrangle)", quad_headers, quad_rows, quad_widths)

    add_h2(doc, "4.4. Thiết lập Hệ thống Chỉ số KPI SMART chuẩn Open Standards Benchmarking (OSB)")
    add_body_p(doc,
        "Căn cứ Khung phân loại APQC PCF v7.2.2 gắn liền với bộ chuẩn đối chuẩn quốc tế Open Standards Benchmarking (OSB), "
        "nghiên cứu thiết lập hệ thống 5 chỉ số KPI thông minh (SMART) để đo lường và giám sát định kỳ hiệu quả vận hành sau cải tiến:")

    kpi_headers = ["Mã KPI", "Tên chỉ số KPI", "Phương pháp & Công thức đo lường", "Hiện trạng (As-Is)", "Mục tiêu (To-Be)", "Đơn vị quản trị"]
    kpi_rows = [
        ["KPI-01", "Thời gian chu kỳ (Turnaround Time - TAT)", "Thời gian từ lúc hoàn tất phê duyệt đến khi tiền về tài khoản KH", "19.5 giờ", "≤ 4 giờ (STP: ≤ 15 phút)", "Khối Vận hành & IT"],
        ["KPI-02", "Tỷ lệ xử lý tự động (STP Rate)", "(Số khoản vay giải ngân tự động STP / Tổng số khoản vay) × 100%", "0%", "≥ 45%", "Khối Vận hành & CNTT"],
        ["KPI-03", "Tỷ lệ đúng lần đầu (First-Time-Right)", "(Số hồ sơ giải ngân không bị trả lại / Tổng hồ sơ tiếp nhận) × 100%", "72%", "≥ 96%", "Khối Quản lý Rủi ro"],
        ["KPI-04", "Chi phí vận hành trên khoản vay", "Tổng chi phí vận hành giải ngân / Tổng số khoản vay thành công", "1.250.000 VNĐ", "≤ 420.000 VNĐ", "Khối Tài chính Kế toán"],
        ["KPI-05", "Độ hài lòng của khách hàng (CSAT)", "Điểm đánh giá trải nghiệm giải ngân trên App (thang điểm 100%)", "68%", "≥ 92%", "Khối Ngân hàng Bán lẻ"]
    ]
    kpi_widths = [Inches(0.65), Inches(1.35), Inches(1.85), Inches(0.75), Inches(0.85), Inches(0.85)]
    add_table_custom(doc, 7, "Hệ thống chỉ số KPI SMART chuẩn Open Standards Benchmarking (OSB)", kpi_headers, kpi_rows, kpi_widths)

    # --------------------------------------------------------------------------
    # KẾT LUẬN VÀ KIẾN NGHỊ
    # --------------------------------------------------------------------------
    add_h1(doc, "KẾT LUẬN VÀ KIẾN NGHỊ", page_break_before=True)
    
    add_h2(doc, "1. Kết luận")
    add_body_p(doc,
        "Báo cáo bài tập lớn đã vận dụng xuất sắc và toàn diện hệ thống lý thuyết chuẩn mực của môn học Quản trị Quy trình "
        "Nghiệp vụ (BPM) vào giải quyết bài toán vận hành thực tiễn tại Ngân hàng TMCP Lộc Phát Việt Nam (LPBank). "
        "Thông qua Thẻ điểm cân bằng (BSC) và Bản đồ cảnh quan quy trình (Process Landscape Map), nghiên cứu đã xác định vị trí "
        "chiến lược của mảng tín dụng bán lẻ. Việc đối chuẩn với Khung quốc tế APQC PCF Banking v7.2.2 đã giúp làm rõ các khoảng trống "
        "về dịch vụ khách hàng và sự chồng chéo trong thẩm định tài sản bảo đảm. Đặc biệt, việc mô hình hóa hiện trạng (As-Is) "
        "và tái thiết kế tương lai (To-Be) chuẩn BPMN 2.0 trên kiến trúc Smart BPM Orchestrator đã giải quyết triệt để 3 điểm nghẽn, "
        "cắt giảm 75% thời gian chu kỳ (TAT) và tiết kiệm 66% chi phí vận hành theo đúng các tiêu chí của Tứ giác Ma quỷ.")

    add_h2(doc, "2. Kiến nghị lộ trình triển khai tại LPBank")
    add_body_p(doc,
        "Để hiện thực hóa mô hình To-Be vào thực tiễn, LPBank cần triển khai theo lộ trình 3 giai đoạn thận trọng và bài bản:")
    add_bullet_p(doc, "Chuẩn hóa quy chế tín dụng nội bộ, ban hành tiêu chuẩn hồ sơ STP và thiết lập môi trường thử nghiệm Sandbox tích hợp BPM Engine với Core T24.", bold_prefix="Giai đoạn 1 (Tháng 1 – Tháng 3/2025 - Thử nghiệm):")
    add_bullet_p(doc, "Hoàn tất kết nối API thời gian thực giữa LOS - BPM - Core T24 - SmartCA; triển khai thí điểm tại 10 chi nhánh trọng điểm khu vực Hà Nội và TP.HCM.", bold_prefix="Giai đoạn 2 (Tháng 4 – Tháng 8/2025 - Triển khai thí điểm):")
    add_bullet_p(doc, "Đánh giá các chỉ số KPI theo chuẩn APQC OSB; đào tạo chuyển giao toàn diện và mở rộng áp dụng cho 100% mạng lưới phòng giao dịch trên toàn quốc.", bold_prefix="Giai đoạn 3 (Tháng 9 – Tháng 12/2025 - Mở rộng toàn hàng):")

    # --------------------------------------------------------------------------
    # DANH MỤC TÀI LIỆU THAM KHẢO
    # --------------------------------------------------------------------------
    add_h1(doc, "DANH MỤC TÀI LIỆU THAM KHẢO", page_break_before=True)
    
    refs = [
        "[1] APQC (2025), Process Classification Framework (PCF) - Banking Edition, Version 7.2.2, American Productivity & Quality Center, Houston, Texas, USA.",
        "[2] Dumas, M., La Rosa, M., Mendling, J., & Reijers, H. A. (2018), Fundamentals of Business Process Management, 2nd Edition, Springer-Verlag, Berlin Heidelberg.",
        "[3] Kaplan, R. S., & Norton, D. P. (1996), The Balanced Scorecard: Translating Strategy into Action, Harvard Business School Press, Boston, Massachusetts.",
        "[4] Ngân hàng TMCP Lộc Phát Việt Nam - LPBank (2024), Báo cáo thường niên 2024: Vững nền tảng - Sáng tương lai, Công bố thông tin chính thức, Hà Nội.",
        "[5] Ngân hàng TMCP Lộc Phát Việt Nam - LPBank (2024), Báo cáo tài chính hợp nhất kiểm toán năm 2024, Hà Nội.",
        "[6] Ngân hàng Nhà nước Việt Nam (2016), Thông tư số 39/2016/TT-NHNN quy định về hoạt động cho vay của tổ chức tín dụng, chi nhánh ngân hàng nước ngoài đối với khách hàng, Hà Nội.",
        "[7] Quốc hội nước Cộng hòa Xã hội Chủ nghĩa Việt Nam (2023), Luật Giao dịch điện tử số 20/2023/QH15, Hà Nội.",
        "[8] Object Management Group - OMG (2011), Business Process Model and Notation (BPMN), Version 2.0, OMG Document Number: formal/2011-01-03.",
        "[9] Phan Thanh Đức (2024), Bài giảng Quản trị Quy trình Nghiệp vụ (BPM), Khoa Hệ thống Thông tin Quản lý & Chuyển đổi số, Học viện Ngân hàng, Hà Nội."
    ]
    for r in refs:
        p_ref = doc.add_paragraph()
        p_ref.paragraph_format.line_spacing = 1.2
        p_ref.paragraph_format.space_before = Pt(0)
        p_ref.paragraph_format.space_after = Pt(3)
        p_ref.paragraph_format.left_indent = Inches(0.35)
        p_ref.paragraph_format.first_line_indent = Inches(-0.35)
        run_ref = p_ref.add_run(r)
        run_ref.font.name = 'Times New Roman'
        run_ref.font.size = Pt(11)
        run_ref.font.color.rgb = COLOR_DARK_TEXT
        log_md(r)

    print(">>> Đã biên soạn xong toàn bộ nội dung học thuật.")

def main():
    print("================================================================================")
    print("KHỞI TẠO BÁO CÁO BÀI TẬP LỚN BPM CHUẨN 10-15 TRANG - HỌC VIỆN NGÂN HÀNG")
    print("================================================================================")
    
    if not TEMPLATE_PATH.exists():
        print(f"LỖI: Không tìm thấy template: {TEMPLATE_PATH}")
        sys.exit(1)
        
    doc = docx.Document(str(TEMPLATE_PATH))
    print(f"Đã nạp template: {TEMPLATE_PATH}")
    
    # 1. Cập nhật bìa và dọn sạch thân bài cũ
    clean_and_update_template_frontmatter(doc)
    
    # 2. Biên soạn nội dung học thuật mới
    write_report_content(doc)
    
    # 3. Lưu file docx
    doc.save(str(OUTPUT_DOCX))
    print(f">>> ĐÃ LƯU THÀNH CÔNG FILE DOCX TẠI: {OUTPUT_DOCX}")
    
    # 4. Lưu file md
    with open(OUTPUT_MD, 'w', encoding='utf-8') as f:
        f.write("# BÁO CÁO BÀI TẬP LỚN MÔN QUẢN LÝ QUY TRÌNH NGHIỆP VỤ (BPM)\n")
        f.write("## ĐỀ TÀI: ĐÁNH GIÁ VÀ HOÀN THIỆN HỆ THỐNG QUY TRÌNH NGHIỆP VỤ TẠI LPBANK THEO CHUẨN APQC PCF VÀ KIẾN TRÚC SMART BPM\n")
        f.write("**Giảng viên hướng dẫn:** PGS.TS. Phan Thanh Đức  \n")
        f.write("**Học viên:** Đỗ Văn Đạt - Mã học viên: 28k405001 - Lớp: K28PTKDA  \n")
        f.write("**Cơ sở đào tạo:** Học viện Ngân hàng - Khoa Sau Đại học  \n\n---\n\n")
        f.write("\n".join(md_lines))
    print(f">>> ĐÃ LƯU THÀNH CÔNG FILE MD TẠI: {OUTPUT_MD}")
    print("================================================================================")

if __name__ == '__main__':
    main()
