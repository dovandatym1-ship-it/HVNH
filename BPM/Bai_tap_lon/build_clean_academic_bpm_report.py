#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Academic Master Report Builder for HVNH Postgraduate Program
Báo cáo Bài tập nhóm: Quản lý Quy trình Nghiệp vụ (BPM)
Khoa Sau Đại học - Học viện Ngân hàng
Chuyển hóa trực tiếp từ Bao_cao_BPM_Tin_dung_Giai_ngan_LPBank_HOAN_THIEN.md
sang Bao_cao_BPM_Tin_dung_Giai_ngan_LPBank_HOAN_THIEN.docx theo chuẩn mực
Template Bài tập lớn HVNH (/academic-docx-writer - DoVanDat_CSDLNC_template)
và chuẩn văn phong học thuật sau đại học (/academic-postgrad-writer).
"""

import os
import re
import sys
from pathlib import Path
import docx
from docx.shared import Inches, Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.enum.section import WD_SECTION
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

BASE_DIR = Path('/Users/dovandat/WORKSPACE/HVNH/BPM/Bai_tap_lon')
INPUT_MD = BASE_DIR / 'Bao_cao_BPM_Tin_dung_Giai_ngan_LPBank_HOAN_THIEN.md'
OUTPUT_DOCX = BASE_DIR / 'Bao_cao_BPM_Tin_dung_Giai_ngan_LPBank_HOAN_THIEN.docx'
DIAGRAM_DIR = BASE_DIR / 'diagrams'

# Hệ màu chuẩn học thuật Học viện Ngân hàng
COLOR_NAVY_HVNH   = RGBColor(10, 37, 64)       # #0A2540 - Navy đậm HVNH
COLOR_BLUE_SEC    = RGBColor(31, 77, 120)      # #1F4D78 - Slate Blue
COLOR_ACCENT_BLUE = RGBColor(46, 116, 181)     # #2E74B5 - Cyan Blue
COLOR_DARK_TEXT   = RGBColor(15, 23, 42)       # #0F172A - Slate 900
COLOR_MUTED_TEXT  = RGBColor(100, 116, 139)    # #64748B - Muted Slate

HEX_HDR_BG     = "D9E2F3"                      # Nền header bảng (Xanh nhạt thanh nhã)
HEX_ZEBRA_BG   = "F8FAFC"                      # Nền dòng chẵn
HEX_BORDER     = "94A3B8"                      # Viền bảng mảnh
HEX_BORDER_THIN= "CBD5E1"

def set_run_font(run, font_name="Times New Roman", size_pt=13.0, bold=False, italic=False, color=None):
    run.font.name = font_name
    run.font.size = Pt(size_pt)
    run.bold = bold
    run.italic = italic
    if color:
        run.font.color.rgb = color
    rPr = run._r.get_or_add_rPr()
    rFonts = rPr.find(qn('w:rFonts'))
    if rFonts is None:
        rFonts = parse_xml(f'<w:rFonts {nsdecls("w")} w:ascii="{font_name}" w:hAnsi="{font_name}" w:cs="{font_name}" w:eastAsia="{font_name}"/>')
        rPr.append(rFonts)
    else:
        rFonts.set(qn('w:ascii'), font_name)
        rFonts.set(qn('w:hAnsi'), font_name)
        rFonts.set(qn('w:cs'), font_name)
        rFonts.set(qn('w:eastAsia'), font_name)

def set_cell_margins(cell, top=80, bottom=80, left=110, right=110):
    """Đặt lề trong của ô bảng (đơn vị twips: 20 twips = 1 pt)."""
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def set_cell_background(cell, hex_color):
    tcPr = cell._tc.get_or_add_tcPr()
    for shd in tcPr.findall(qn('w:shd')):
        tcPr.remove(shd)
    new_shd = parse_xml(f'<w:shd {nsdecls("w")} w:val="clear" w:color="auto" w:fill="{hex_color}"/>')
    tcPr.append(new_shd)

def set_table_borders(table, border_color=HEX_BORDER):
    tblPr = table._tbl.tblPr
    for b in tblPr.findall(qn('w:tblBorders')):
        tblPr.remove(b)
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'  <w:top w:val="single" w:sz="6" w:space="0" w:color="{border_color}"/>'
        f'  <w:bottom w:val="single" w:sz="6" w:space="0" w:color="{border_color}"/>'
        f'  <w:left w:val="single" w:sz="4" w:space="0" w:color="{border_color}"/>'
        f'  <w:right w:val="single" w:sz="4" w:space="0" w:color="{border_color}"/>'
        f'  <w:insideH w:val="single" w:sz="4" w:space="0" w:color="{border_color}"/>'
        f'  <w:insideV w:val="single" w:sz="4" w:space="0" w:color="{border_color}"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)

def make_table_openxml_compliant(table):
    """Thêm tblHeader và cantSplit cho toàn bộ bảng để sang trang không bị lỗi."""
    if len(table.rows) > 0:
        hdr_tr = table.rows[0]._tr.get_or_add_trPr()
        if hdr_tr.find(qn('w:tblHeader')) is None:
            hdr_tr.append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))
    for row in table.rows:
        trPr = row._tr.get_or_add_trPr()
        if trPr.find(qn('w:cantSplit')) is None:
            trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))

def add_xml_page_field(p, field_name="PAGE", default_val="1"):
    """Thêm trường đánh số trang OpenXML chuẩn."""
    fld = parse_xml(
        f'<w:fldSimple {nsdecls("w")} w:instr="{field_name}">'
        f'  <w:r><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/><w:sz w:val="20"/></w:rPr>'
        f'  <w:t>{default_val}</w:t></w:r>'
        f'</w:fldSimple>'
    )
    p._p.append(fld)

def _set_page_number_start(section, start=1):
    sectPr = section._sectPr
    for el in sectPr.findall(qn('w:pgNumType')):
        sectPr.remove(el)
    pg = parse_xml(f'<w:pgNumType {nsdecls("w")} w:start="{start}"/>')
    cols = sectPr.find(qn('w:cols'))
    if cols is not None:
        cols.addprevious(pg)
    else:
        sectPr.append(pg)

def add_assignment_cover_page(doc):
    """
    Tạo trang bìa chuẩn Bài tập lớn HVNH kế thừa DoVanDat_CSDLNC_template:
    - Viền hoa văn trang bìa mỹ thuật OpenXML (thinThickThinMediumGap)
    - Tiêu đề cơ quan đào tạo
    - BÀI TẬP NHÓM - MÔN HỌC
    - ĐỀ TÀI IN HOA
    - Bảng thông tin tác giả và giảng viên
    - HÀ NỘI – 2026
    """
    sec = doc.sections[0]
    sec.different_first_page_header_footer = True
    sec.page_width = Cm(21.0)
    sec.page_height = Cm(29.7)
    sec.top_margin = Cm(2.54)
    sec.bottom_margin = Cm(2.54)
    sec.left_margin = Cm(3.0)
    sec.right_margin = Cm(2.54)

    # Thêm viền hoa văn kép bao quanh trang bìa
    sectPr = sec._sectPr
    for el in sectPr.findall(qn('w:pgBorders')):
        sectPr.remove(el)
    borders_xml = parse_xml(
        f'<w:pgBorders {nsdecls("w")} w:display="firstPage" w:offsetFrom="page">'
        f'<w:top w:val="thinThickThinMediumGap" w:sz="24" w:space="24" w:color="auto"/>'
        f'<w:left w:val="thinThickThinMediumGap" w:sz="24" w:space="24" w:color="auto"/>'
        f'<w:bottom w:val="thinThickThinMediumGap" w:sz="24" w:space="24" w:color="auto"/>'
        f'<w:right w:val="thinThickThinMediumGap" w:sz="24" w:space="24" w:color="auto"/>'
        f'</w:pgBorders>'
    )
    sectPr.append(borders_xml)

    # Đặt footer cho Section 0 (La Mã thường i, ii... trang bìa ẩn số)
    sec.footer.is_linked_to_previous = False
    ftr_p = sec.footer.paragraphs[0]
    ftr_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    ftr_p.paragraph_format.first_line_indent = Cm(0)
    add_xml_page_field(ftr_p, "PAGE", default_val="i")
    pg_roman = parse_xml(f'<w:pgNumType {nsdecls("w")} w:fmt="lowerRoman" w:start="1"/>')
    sectPr.append(pg_roman)

    p1 = doc.add_paragraph()
    p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p1.paragraph_format.space_before = Pt(8)
    p1.paragraph_format.space_after = Pt(2)
    p1.paragraph_format.first_line_indent = Cm(0)
    r1 = p1.add_run("HỌC VIỆN NGÂN HÀNG")
    set_run_font(r1, size_pt=16.0, bold=True, color=COLOR_NAVY_HVNH)

    p2 = doc.add_paragraph()
    p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p2.paragraph_format.space_before = Pt(0)
    p2.paragraph_format.space_after = Pt(30)
    p2.paragraph_format.first_line_indent = Cm(0)
    r2 = p2.add_run("KHOA SAU ĐẠI HỌC")
    set_run_font(r2, size_pt=16.0, bold=True, color=COLOR_NAVY_HVNH)

    p3 = doc.add_paragraph()
    p3.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p3.paragraph_format.space_before = Pt(0)
    p3.paragraph_format.space_after = Pt(4)
    p3.paragraph_format.first_line_indent = Cm(0)
    r3 = p3.add_run("BÀI TẬP NHÓM")
    set_run_font(r3, size_pt=18.0, bold=True, color=COLOR_NAVY_HVNH)

    p4 = doc.add_paragraph()
    p4.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p4.paragraph_format.space_before = Pt(0)
    p4.paragraph_format.space_after = Pt(28)
    p4.paragraph_format.first_line_indent = Cm(0)
    r4 = p4.add_run("MÔN HỌC: QUẢN LÝ QUY TRÌNH NGHIỆP VỤ (BPM)")
    set_run_font(r4, size_pt=15.0, bold=True, color=COLOR_BLUE_SEC)

    p5 = doc.add_paragraph()
    p5.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p5.paragraph_format.space_before = Pt(0)
    p5.paragraph_format.space_after = Pt(36)
    p5.paragraph_format.first_line_indent = Cm(0)
    r5_label = p5.add_run("ĐỀ TÀI:\n")
    set_run_font(r5_label, size_pt=14.0, bold=True, color=COLOR_DARK_TEXT)
    r5_title = p5.add_run(
        "ĐÁNH GIÁ VÀ HOÀN THIỆN QUY TRÌNH TRIỂN KHAI TÍN DỤNG\n"
        "VÀ GIẢI NGÂN KHOẢN VAY KHÁCH HÀNG CÁ NHÂN TẠI LPBANK\n"
        "TRONG BỐI CẢNH ỨNG DỤNG BPM"
    )
    set_run_font(r5_title, size_pt=15.5, bold=True, color=COLOR_NAVY_HVNH)

    # Bảng thông tin tác giả
    table = doc.add_table(rows=4, cols=2)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(table, border_color="94A3B8")

    info_data = [
        ("Giảng viên hướng dẫn:", "PGS.TS. Phan Thanh Đức"),
        ("Lớp / Khóa đào tạo:", "Cao học K28 – Khoa Sau Đại học"),
        ("Học viên thực hiện:", "Nhóm học viên K28 (Trưởng nhóm: Đỗ Văn Đạt – Mã HV: 28k405001)"),
        ("Đơn vị nghiên cứu:", "Ngân hàng TMCP Lộc Phát Việt Nam (LPBank)")
    ]

    col_widths = [Cm(5.2), Cm(10.2)]
    for r_idx, (k, v) in enumerate(info_data):
        row = table.rows[r_idx]
        row.height = Pt(22)
        c0, c1 = row.cells[0], row.cells[1]
        c0.width, c1.width = col_widths[0], col_widths[1]
        set_cell_margins(c0, top=70, bottom=70, left=100, right=100)
        set_cell_margins(c1, top=70, bottom=70, left=100, right=100)
        if r_idx % 2 == 1:
            set_cell_background(c0, HEX_ZEBRA_BG)
            set_cell_background(c1, HEX_ZEBRA_BG)

        p_k = c0.paragraphs[0]
        p_k.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p_k.paragraph_format.space_after = Pt(0)
        r_k = p_k.add_run(k)
        set_run_font(r_k, size_pt=11.5, bold=True, color=COLOR_DARK_TEXT)

        p_v = c1.paragraphs[0]
        p_v.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p_v.paragraph_format.space_after = Pt(0)
        r_v = p_v.add_run(v)
        set_run_font(r_v, size_pt=11.5, bold=False, color=COLOR_DARK_TEXT)

    make_table_openxml_compliant(table)

    p_bot = doc.add_paragraph()
    p_bot.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_bot.paragraph_format.space_before = Pt(50)
    p_bot.paragraph_format.space_after = Pt(0)
    p_bot.paragraph_format.first_line_indent = Cm(0)
    r_bot = p_bot.add_run("Hà Nội, 2026")
    set_run_font(r_bot, size_pt=12.5, bold=True, color=COLOR_DARK_TEXT)

    doc.add_page_break()

def add_instructor_review_page(doc):
    """Trang NHẬN XÉT CỦA GIẢNG VIÊN HƯỚNG DẪN chuẩn Bài tập lớn HVNH."""
    p_h = doc.add_paragraph("NHẬN XÉT CỦA GIẢNG VIÊN HƯỚNG DẪN")
    p_h.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_h.paragraph_format.space_before = Pt(8)
    p_h.paragraph_format.space_after = Pt(14)
    p_h.paragraph_format.first_line_indent = Cm(0)
    r_h = p_h.runs[0]
    set_run_font(r_h, size_pt=14.0, bold=True, color=COLOR_NAVY_HVNH)

    p_info = doc.add_paragraph()
    p_info.paragraph_format.space_before = Pt(0)
    p_info.paragraph_format.space_after = Pt(4)
    p_info.paragraph_format.first_line_indent = Cm(0)
    r_info = p_info.add_run(
        "Họ và tên học viên: Đỗ Văn Đạt (Trưởng nhóm) và các thành viên nhóm K28\n"
        "Lớp chuyên ngành: Cao học K28 – Khoa Sau Đại học\n"
        "Đề tài: Đánh giá và hoàn thiện quy trình triển khai tín dụng và giải ngân khoản vay khách hàng cá nhân tại LPBank trong bối cảnh ứng dụng BPM"
    )
    set_run_font(r_info, size_pt=11.5, bold=False, italic=True, color=COLOR_DARK_TEXT)

    criteria = [
        "1. Về tinh thần, thái độ làm việc nhóm và tính độc lập trong nghiên cứu:",
        "2. Về cơ sở lý luận môn học và tính ứng dụng thực tiễn (BPM, APQC PCF, BPMN 2.0):",
        "3. Kết quả đạt được và khả năng ứng dụng hoàn thiện quy trình tại ngân hàng:",
        "4. Điểm đánh giá: Điểm số: ............... Điểm chữ: ......................................."
    ]

    for idx, c in enumerate(criteria):
        p_c = doc.add_paragraph()
        p_c.paragraph_format.space_before = Pt(6)
        p_c.paragraph_format.space_after = Pt(2)
        p_c.paragraph_format.first_line_indent = Cm(0)
        r_c = p_c.add_run(c)
        set_run_font(r_c, size_pt=12.0, bold=True, color=COLOR_BLUE_SEC)
        if idx < 3:
            for _ in range(2):
                p_dot = doc.add_paragraph()
                p_dot.paragraph_format.space_after = Pt(2)
                p_dot.paragraph_format.first_line_indent = Cm(0)
                r_dot = p_dot.add_run(". " * 45)
                set_run_font(r_dot, size_pt=10.0, color=COLOR_MUTED_TEXT)

    p_sig = doc.add_paragraph()
    p_sig.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p_sig.paragraph_format.space_before = Pt(20)
    p_sig.paragraph_format.space_after = Pt(0)
    p_sig.paragraph_format.first_line_indent = Cm(0)
    r_sig = p_sig.add_run(
        "Hà Nội, ngày … tháng … năm 2026\n"
        "GIẢNG VIÊN HƯỚNG DẪN\n\n\n\n"
        "PGS.TS. Phan Thanh Đức"
    )
    set_run_font(r_sig, size_pt=12.0, bold=True, color=COLOR_NAVY_HVNH)

    doc.add_page_break()

def apply_assignment_headers_footers(doc, header_title="", start_value=1):
    """
    Thiết lập Header & Footer chuẩn Bài tập lớn / Tiểu luận môn học HVNH:
    - Tạo Section mới (Section 1 - Thân bài).
    - Header: căn phải, chữ nghiêng 10pt (tên đề tài) kèm đường kẻ mờ phân cách dưới.
    - Footer: căn giữa, định dạng chuẩn 'Trang {PAGE}', bắt đầu lại từ start_value (1).
    """
    body_sec = doc.add_section(WD_SECTION.NEW_PAGE)
    body_sec.page_width = Cm(21.0)
    body_sec.page_height = Cm(29.7)
    body_sec.top_margin = Cm(2.54)
    body_sec.bottom_margin = Cm(2.54)
    body_sec.left_margin = Cm(3.0)
    body_sec.right_margin = Cm(2.54)
    body_sec.header.is_linked_to_previous = False
    body_sec.footer.is_linked_to_previous = False

    if header_title:
        hdr_p = body_sec.header.paragraphs[0]
        hdr_p.paragraph_format.first_line_indent = Cm(0)
        hdr_p.paragraph_format.space_after = Pt(4)
        hdr_p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        pPr = hdr_p._p.get_or_add_pPr()
        pBdr = parse_xml(f'<w:pBdr {nsdecls("w")}><w:bottom w:val="single" w:sz="4" w:space="2" w:color="CBD5E1"/></w:pBdr>')
        pPr.append(pBdr)
        r_hdr = hdr_p.add_run(header_title)
        set_run_font(r_hdr, size_pt=9.5, italic=True, color=COLOR_MUTED_TEXT)

    ftr_p = body_sec.footer.paragraphs[0]
    ftr_p.paragraph_format.first_line_indent = Cm(0)
    ftr_p.paragraph_format.space_after = Pt(0)
    ftr_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_lbl = ftr_p.add_run("Trang ")
    set_run_font(r_lbl, size_pt=10.5, color=COLOR_MUTED_TEXT)
    add_xml_page_field(ftr_p, "PAGE", default_val=str(start_value))
    _set_page_number_start(body_sec, start=start_value)
    return body_sec

def format_text_runs(paragraph, text, base_size=13.0, is_italic=False, default_color=COLOR_DARK_TEXT):
    """Phân tách và định dạng các đoạn in đậm **bold** và in nghiêng *italic* trong Markdown."""
    tokens = re.split(r'(\*\*.*?\*\*|\*.*?\*)', text)
    for tok in tokens:
        if not tok:
            continue
        if tok.startswith('**') and tok.endswith('**'):
            inner = tok[2:-2]
            run = paragraph.add_run(inner)
            set_run_font(run, size_pt=base_size, bold=True, italic=is_italic, color=default_color)
        elif tok.startswith('*') and tok.endswith('*'):
            inner = tok[1:-1]
            run = paragraph.add_run(inner)
            set_run_font(run, size_pt=base_size, bold=False, italic=True, color=default_color)
        else:
            run = paragraph.add_run(tok)
            set_run_font(run, size_pt=base_size, bold=False, italic=is_italic, color=default_color)

def parse_markdown_table(lines):
    """Chuyển đổi một khối bảng Markdown thành ma trận 2D."""
    rows = []
    for line in lines:
        line = line.strip()
        if not line or not line.startswith('|'):
            continue
        if re.match(r'^\|[\s\-:]+(\|[\s\-:]+)+\|$', line):
            continue
        cells = [c.strip() for c in line.split('|')[1:-1]]
        rows.append(cells)
    return rows

def render_table_to_docx(doc, rows_data):
    """Vẽ bảng dữ liệu vào Word chuẩn OpenXML."""
    if not rows_data or len(rows_data) == 0:
        return
    num_rows = len(rows_data)
    num_cols = len(rows_data[0])

    table = doc.add_table(rows=num_rows, cols=num_cols)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(table, border_color=HEX_BORDER)

    # Chiều rộng khả dụng: 21.0 - (3.0 + 2.54) = 15.46 cm
    total_w = 15.46
    col_w = total_w / num_cols

    for r_idx, row_cells in enumerate(rows_data):
        row = table.rows[r_idx]
        is_header = (r_idx == 0)

        for c_idx in range(min(num_cols, len(row_cells))):
            cell = row.cells[c_idx]
            cell.width = Cm(col_w)
            cell_text = row_cells[c_idx]

            set_cell_margins(cell, top=65, bottom=65, left=90, right=90)

            if is_header:
                set_cell_background(cell, HEX_HDR_BG)
            elif r_idx % 2 == 1:
                set_cell_background(cell, HEX_ZEBRA_BG)

            sub_lines = re.split(r'<br\s*/?>', cell_text)
            for s_idx, sub_line in enumerate(sub_lines):
                if s_idx == 0:
                    p = cell.paragraphs[0]
                else:
                    p = cell.add_paragraph()
                p.paragraph_format.space_before = Pt(1)
                p.paragraph_format.space_after = Pt(2)
                p.paragraph_format.line_spacing = 1.05

                if c_idx == 0 and len(cell_text) <= 5 and not is_header:
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                else:
                    p.alignment = WD_ALIGN_PARAGRAPH.LEFT

                format_text_runs(p, sub_line.strip(), base_size=10.5, default_color=COLOR_NAVY_HVNH if is_header else COLOR_DARK_TEXT)
                if is_header:
                    for r in p.runs:
                        r.bold = True

    make_table_openxml_compliant(table)

    p_sp = doc.add_paragraph()
    p_sp.paragraph_format.space_after = Pt(4)
    p_sp.paragraph_format.line_spacing = 1.0

def add_outline_level(paragraph, level):
    pPr = paragraph._p.get_or_add_pPr()
    outline = parse_xml(f'<w:outlineLvl {nsdecls("w")} w:val="{level}"/>')
    pPr.append(outline)

def compile_markdown_to_docx(md_path, docx_path):
    print("================================================================================")
    print("BIÊN DỊCH BÁO CÁO HỌC THUẬT BPM SAU ĐẠI HỌC THEO TEMPLATE DOVANDAT_CSDLNC")
    print("================================================================================")

    with open(md_path, 'r', encoding='utf-8') as f:
        md_text = f.read()

    lines = md_text.splitlines()
    doc = docx.Document()

    # 1. Thêm trang bìa có hoa văn trang trọng theo chuẩn DoVanDat_CSDLNC
    add_assignment_cover_page(doc)

    # 2. Thêm trang Nhận xét của giảng viên hướng dẫn
    add_instructor_review_page(doc)

    # 3. Phân tách nội dung
    content_start_idx = 0
    for idx, l in enumerate(lines):
        if l.strip().startswith('# **MỤC LỤC**'):
            content_start_idx = idx
            break

    content_lines = lines[content_start_idx:]

    line_idx = 0
    in_section_body = False

    while line_idx < len(content_lines):
        line = content_lines[line_idx].strip()

        if not line:
            line_idx += 1
            continue

        # Kiểm tra bước chuyển sang MỞ ĐẦU để kích hoạt Section Thân bài
        if line.startswith('# **MỞ ĐẦU**') and not in_section_body:
            apply_assignment_headers_footers(
                doc,
                header_title="BÀI TẬP NHÓM BPM: QUY TRÌNH TRIỂN KHAI TÍN DỤNG & GIẢI NGÂN LPBANK",
                start_value=1
            )
            in_section_body = True

        # Bảng biểu Markdown
        if line.startswith('|') and line.endswith('|'):
            table_lines = [line]
            line_idx += 1
            while line_idx < len(content_lines) and content_lines[line_idx].strip().startswith('|'):
                table_lines.append(content_lines[line_idx].strip())
                line_idx += 1
            table_data = parse_markdown_table(table_lines)
            render_table_to_docx(doc, table_data)
            continue

        # Hình ảnh Markdown
        img_match = re.match(r'^!\[(.*?)\]\((.*?)\)$', line)
        if img_match:
            img_rel_path = img_match.group(2)
            img_full_path = BASE_DIR / img_rel_path

            if img_full_path.exists():
                p_img = doc.add_paragraph()
                p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p_img.paragraph_format.space_before = Pt(8)
                p_img.paragraph_format.space_after = Pt(2)
                run_img = p_img.add_run()
                run_img.add_picture(str(img_full_path), width=Cm(15.2))
            else:
                print(f"CẢNH BÁO: Không tìm thấy ảnh: {img_full_path}")
            line_idx += 1
            continue

        # Tiêu đề Cấp 1 (# ...)
        if line.startswith('# '):
            raw_h1 = line[2:].strip().replace('**', '')
            p_h = doc.add_paragraph()
            p_h.style = 'Heading 1'
            p_h.alignment = WD_ALIGN_PARAGRAPH.LEFT
            p_h.paragraph_format.space_before = Pt(14)
            p_h.paragraph_format.space_after = Pt(6)
            p_h.paragraph_format.keep_with_next = True
            add_outline_level(p_h, 0)
            r_h = p_h.add_run(raw_h1)
            set_run_font(r_h, size_pt=14.5, bold=True, color=COLOR_NAVY_HVNH)
            line_idx += 1
            continue

        # Tiêu đề Cấp 2 (## ...)
        if line.startswith('## '):
            raw_h2 = line[3:].strip().replace('**', '')
            p_h = doc.add_paragraph()
            p_h.style = 'Heading 2'
            p_h.alignment = WD_ALIGN_PARAGRAPH.LEFT
            p_h.paragraph_format.space_before = Pt(11)
            p_h.paragraph_format.space_after = Pt(5)
            p_h.paragraph_format.keep_with_next = True
            add_outline_level(p_h, 1)
            r_h = p_h.add_run(raw_h2)
            set_run_font(r_h, size_pt=13.5, bold=True, color=COLOR_BLUE_SEC)
            line_idx += 1
            continue

        # Tiêu đề Cấp 3 (### ...)
        if line.startswith('### '):
            raw_h3 = line[4:].strip().replace('**', '')
            p_h = doc.add_paragraph()
            p_h.style = 'Heading 3'
            p_h.alignment = WD_ALIGN_PARAGRAPH.LEFT
            p_h.paragraph_format.space_before = Pt(9)
            p_h.paragraph_format.space_after = Pt(3)
            p_h.paragraph_format.keep_with_next = True
            add_outline_level(p_h, 2)
            r_h = p_h.add_run(raw_h3)
            set_run_font(r_h, size_pt=13.0, bold=True, color=COLOR_ACCENT_BLUE)
            line_idx += 1
            continue

        # Caption Bảng biểu / Hình ảnh
        if line.startswith('**Bảng ') or line.startswith('*Hình '):
            is_table_caption = line.startswith('**Bảng ')
            p_cap = doc.add_paragraph()
            p_cap.alignment = WD_ALIGN_PARAGRAPH.LEFT if is_table_caption else WD_ALIGN_PARAGRAPH.CENTER
            p_cap.paragraph_format.space_before = Pt(8)
            p_cap.paragraph_format.space_after = Pt(4)
            p_cap.paragraph_format.keep_with_next = True

            clean_cap = line.replace('**', '').replace('*', '').strip()
            format_text_runs(p_cap, clean_cap, base_size=11.5, is_italic=True, default_color=COLOR_NAVY_HVNH)
            for r in p_cap.runs:
                if is_table_caption:
                    r.bold = True
            line_idx += 1
            continue

        # Danh sách gạch đầu dòng
        if line.startswith('* ') or line.startswith('- '):
            list_text = line[2:].strip()
            p_li = doc.add_paragraph()
            p_li.paragraph_format.left_indent = Cm(0.8)
            p_li.paragraph_format.first_line_indent = Cm(-0.4)
            p_li.paragraph_format.space_before = Pt(1)
            p_li.paragraph_format.space_after = Pt(3)
            p_li.paragraph_format.line_spacing = 1.3
            p_li.alignment = WD_ALIGN_PARAGRAPH.LEFT

            bullet_run = p_li.add_run("•  ")
            set_run_font(bullet_run, size_pt=11.5, bold=True, color=COLOR_ACCENT_BLUE)
            format_text_runs(p_li, list_text, base_size=13.0)
            line_idx += 1
            continue

        # Danh sách số thứ tự
        numbered_match = re.match(r'^(\d+)\.\s+(.*)$', line)
        if numbered_match:
            num_idx = numbered_match.group(1)
            num_text = numbered_match.group(2)
            p_num = doc.add_paragraph()
            p_num.paragraph_format.left_indent = Cm(0.8)
            p_num.paragraph_format.first_line_indent = Cm(-0.4)
            p_num.paragraph_format.space_before = Pt(1)
            p_num.paragraph_format.space_after = Pt(3)
            p_num.paragraph_format.line_spacing = 1.3
            p_num.alignment = WD_ALIGN_PARAGRAPH.LEFT

            num_run = p_num.add_run(f"{num_idx}.  ")
            set_run_font(num_run, size_pt=13.0, bold=True, color=COLOR_BLUE_SEC)
            format_text_runs(p_num, num_text, base_size=13.0)
            line_idx += 1
            continue

        # Đoạn văn thông thường (Body Text)
        p_body = doc.add_paragraph()
        p_body.paragraph_format.space_before = Pt(0)
        p_body.paragraph_format.space_after = Pt(5)
        p_body.paragraph_format.line_spacing = 1.35

        # Căn đều (Justified) cho đoạn dài, căn trái (Left align) cho đoạn ngắn
        if len(line) > 100:
            p_body.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            p_body.paragraph_format.first_line_indent = Cm(1.0)
        else:
            p_body.alignment = WD_ALIGN_PARAGRAPH.LEFT
            p_body.paragraph_format.first_line_indent = Cm(0.0)

        format_text_runs(p_body, line, base_size=13.0)
        line_idx += 1

    doc.save(str(docx_path))
    print(f">>> ĐÃ LƯU THÀNH CÔNG BÁO CÁO DOCX TẠI: {docx_path}")

if __name__ == '__main__':
    compile_markdown_to_docx(INPUT_MD, OUTPUT_DOCX)
