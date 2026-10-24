#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master Builder: Báo cáo Bài tập lớn môn Quản lý Quy trình Nghiệp vụ (BPM)
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
HEX_CALLOUT_BG = "F1F5F9"

md_lines = []

def log_md(line=""):
    md_lines.append(line)

def set_cell_background(cell, hex_color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=60, bottom=60, left=100, right=100):
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
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(8)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(title)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(15)
    r.font.bold = True
    r.font.color.rgb = COLOR_NAVY_HVNH
    log_md(f"\n# {title}\n")

def add_h2(doc, title):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(title)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(13.5)
    r.font.bold = True
    r.font.color.rgb = COLOR_BLUE_SEC
    log_md(f"\n## {title}\n")

def add_h3(doc, title):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(title)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(13)
    r.font.bold = True
    r.font.color.rgb = COLOR_ACCENT_BLUE
    log_md(f"\n### {title}\n")

def add_body_p(doc, text, bold_prefix=None, indent=True, line_spacing=1.35, space_after=5):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.line_spacing = line_spacing
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.first_line_indent = Inches(0.4) if indent else Inches(0)
        
    full_text = ""
    if bold_prefix:
        r_b = p.add_run(bold_prefix)
        r_b.font.name = 'Times New Roman'
        r_b.font.size = Pt(12.5)
        r_b.font.bold = True
        r_b.font.color.rgb = COLOR_DARK_TEXT
        full_text += f"**{bold_prefix}** "
        
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12.5)
    r.font.color.rgb = COLOR_DARK_TEXT
    full_text += text
    log_md(full_text + "\n")

def add_bullet_p(doc, text, bold_prefix=None):
    p = doc.add_paragraph(style='List Bullet')
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.line_spacing = 1.3
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(3)
    
    full_text = "- "
    if bold_prefix:
        r_b = p.add_run(bold_prefix)
        r_b.font.name = 'Times New Roman'
        r_b.font.size = Pt(12)
        r_b.font.bold = True
        r_b.font.color.rgb = COLOR_DARK_TEXT
        full_text += f"**{bold_prefix}** "
        
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r.font.color.rgb = COLOR_DARK_TEXT
    full_text += text
    log_md(full_text)

def add_image_figure(doc, img_path, fig_num, caption):
    if not img_path.exists():
        print(f"LỖI: Không tìm thấy ảnh: {img_path}")
        return
        
    p_img = doc.add_paragraph()
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img.paragraph_format.space_before = Pt(6)
    p_img.paragraph_format.space_after = Pt(3)
    p_img.paragraph_format.keep_with_next = True
    
    run_img = p_img.add_run()
    run_img.add_picture(str(img_path), width=Inches(6.2))
    
    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap.paragraph_format.space_before = Pt(2)
    p_cap.paragraph_format.space_after = Pt(8)
    
    r_cap = p_cap.add_run(f"Hình {fig_num}. {caption}")
    r_cap.font.name = 'Times New Roman'
    r_cap.font.size = Pt(11)
    r_cap.font.italic = True
    r_cap.font.bold = True
    r_cap.font.color.rgb = COLOR_BLUE_SEC
    
    log_md(f"\n![Hình {fig_num}. {caption}]({img_path.name})\n*Hình {fig_num}. {caption}*\n")

def add_table_custom(doc, table_num, caption, headers, rows_data, col_widths=None):
    # Caption trên bảng
    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p_cap.paragraph_format.space_before = Pt(6)
    p_cap.paragraph_format.space_after = Pt(3)
    p_cap.paragraph_format.keep_with_next = True
    
    r_cap = p_cap.add_run(f"Bảng {table_num}. {caption}")
    r_cap.font.name = 'Times New Roman'
    r_cap.font.size = Pt(11)
    r_cap.font.bold = True
    r_cap.font.color.rgb = COLOR_NAVY_HVNH
    
    table = doc.add_table(rows=len(rows_data) + 1, cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(table)
    
    # Header row
    hdr_row = table.rows[0]
    make_tbl_header(hdr_row)
    make_cant_split(hdr_row)
    for col_idx, h_text in enumerate(headers):
        cell = hdr_row.cells[col_idx]
        set_cell_background(cell, HEX_HDR_BG)
        set_cell_margins(cell, top=70, bottom=70, left=90, right=90)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run(h_text)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(10)
        r.font.bold = True
        r.font.color.rgb = COLOR_NAVY_HVNH
        
    # Data rows
    for row_idx, r_data in enumerate(rows_data):
        row = table.rows[row_idx + 1]
        make_cant_split(row)
        bg_color = HEX_ZEBRA_BG if row_idx % 2 == 1 else "FFFFFF"
        for col_idx, val in enumerate(r_data):
            cell = row.cells[col_idx]
            if bg_color != "FFFFFF":
                set_cell_background(cell, bg_color)
            set_cell_margins(cell, top=50, bottom=50, left=80, right=80)
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.15
            
            # Căn giữa nếu là số thứ tự hoặc mã ngắn, căn đều nếu là nội dung
            if col_idx == 0 or len(str(val)) < 8:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            else:
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                
            r = p.add_run(str(val))
            r.font.name = 'Times New Roman'
            r.font.size = Pt(9.5)
            r.font.color.rgb = COLOR_DARK_TEXT
            
    # Set col widths
    if col_widths:
        for row in table.rows:
            for idx, width in enumerate(col_widths):
                row.cells[idx].width = width
                
    # Add space after table
    p_sp = doc.add_paragraph()
    p_sp.paragraph_format.space_before = Pt(0)
    p_sp.paragraph_format.space_after = Pt(4)
    
    # Log markdown
    md_header = "| " + " | ".join(headers) + " |"
    md_sep = "| " + " | ".join(["---"] * len(headers)) + " |"
    log_md(f"\n**Bảng {table_num}. {caption}**\n\n{md_header}\n{md_sep}")
    for r_data in rows_data:
        log_md("| " + " | ".join(str(v).replace("\n", "<br>") for v in r_data) + " |")
    log_md("\n")

print(">>> Helper functions loaded.")
