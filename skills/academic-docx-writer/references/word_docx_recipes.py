"""
Academic Postgraduate Writer — Complete Python-docx Recipes for Postgraduate Academic Reports
v3 — Profile-based standards engine:
  * hvnh-thesis    : Luận văn Thạc sĩ HVNH (Quy định về trình bày luận văn — Khoa Sau đại học HVNH)
                     Lề 3.5/3.0/3.5/2.0 cm • Giãn dòng 1.5 • Số trang giữa-phía-trên đếm từ MỞ ĐẦU
                     Trích dẫn số [15, tr.314] • Caption gắn số chương (Hình 3.4)
  * hvnh-khoaluan  : Khóa luận / Chuyên đề tốt nghiệp (giãn dòng 1.3–1.5, mặc định 1.5)
  * nd30-report    : Báo cáo hành chính theo ND 30/2020/NĐ-CP (legacy profile của v1)
Xem chi tiết chuẩn gốc: references/hvnh_thesis_standard.md

v3 bổ sung so với v2: cảnh báo rõ ràng khi thiếu ảnh (add_figure_with_caption), và
validate_document() để tự kiểm tra lề/giãn dòng/số trang/heading trước khi giao file
— xem SKILL.md §4 "Quy Trình Sử Dụng Đề Xuất".

Giới hạn đã biết: python-docx không thể kiểm tra xem font Times New Roman có thực sự
được cài trên máy mở file hay không — validate_document() chỉ kiểm tra font NAME được
ghi trong style, không kiểm tra font có render đúng khi mở bằng Word/LibreOffice.
"""
import os
import docx
from docx.shared import Inches, Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.enum.section import WD_SECTION
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls, qn

# ==============================================================================
# HỆ MÀU CHUẨN HỌC VIỆN NGÂN HÀNG & BÁO CÁO TÀI CHÍNH KHOA HỌC
# ==============================================================================
COLOR_NAVY_HVNH   = RGBColor(10, 37, 64)       # #0A2540: Xanh Navy đậm HVNH
COLOR_BLUE_SEC    = RGBColor(31, 77, 120)      # #1F4D78: Xanh Slate tiêu đề cấp 2
COLOR_ACCENT_BLUE = RGBColor(46, 116, 181)     # #2E74B5: Xanh tiêu đề cấp 3
COLOR_ORANGE_HVNH = RGBColor(234, 88, 12)      # #EA580C: Cam năng lượng BAV
COLOR_DARK_TEXT   = RGBColor(15, 23, 42)       # #0F172A: Màu chữ Slate 900
COLOR_MUTED_TEXT  = RGBColor(100, 116, 139)    # #64748B: Màu chữ chú thích Slate 500

HEX_NAVY_BG    = "0A2540"
HEX_BLUE_HDR   = "17365D"
HEX_ZEBRA_BG   = "F8FAFC"
HEX_CALLOUT_BG = "F1F5F9"
HEX_BORDER     = "CBD5E1"
HEX_ORANGE     = "EA580C"

# ==============================================================================
# PROFILE ĐỊNH DẠNG — chọn đúng chuẩn trước khi soạn thảo
# ==============================================================================
PROFILES = {
    "hvnh-thesis": {
        "name": "Luận văn Thạc sĩ HVNH (Quy định Khoa Sau đại học)",
        "margins_cm": {"top": 3.5, "bottom": 3.0, "left": 3.5, "right": 2.0},
        "line_spacing": 1.5,
        "page_number_pos": "top-center",
        "citation_style": "numeric-bracketed",
        "caption_numbering": "chapter-based",
    },
    "hvnh-khoaluan": {
        "name": "Khóa luận / Chuyên đề tốt nghiệp HVNH",
        "margins_cm": {"top": 3.5, "bottom": 3.0, "left": 3.5, "right": 2.0},
        "line_spacing": 1.5,
        "page_number_pos": "top-center",
        "citation_style": "numeric-bracketed",
        "caption_numbering": "chapter-based",
    },
    "hvnh-assignment": {
        "name": "Bài tập lớn / Tiểu luận môn học HVNH (DoVanDat_CSDLNC template)",
        "margins_cm": {"top": 2.54, "bottom": 2.54, "left": 3.0, "right": 2.54},
        "line_spacing": 1.5,
        "page_number_pos": "footer",
        "citation_style": "numeric-bracketed",
        "caption_numbering": "chapter-based",
    },
    "nd30-report": {
        "name": "Báo cáo hành chính ND 30/2020/NĐ-CP (legacy v1)",
        "margins_cm": {"top": 2.5, "bottom": 2.0, "left": 3.0, "right": 2.0},
        "line_spacing": 1.35,
        "page_number_pos": "footer",
        "citation_style": "author-date",
        "caption_numbering": "flat",
    },
}
CURRENT_PROFILE = PROFILES["hvnh-thesis"]

def get_profile(name):
    """Lấy cấu hình profile theo tên; ném lỗi rõ ràng nếu sai tên."""
    if name not in PROFILES:
        raise ValueError(
            f"Profile '{name}' không tồn tại. Các profile khả dụng: {list(PROFILES)}"
        )
    return PROFILES[name]

# ==============================================================================
# CẤU HÌNH TÀI LIỆU THEO PROFILE
# ==============================================================================
def configure_academic_document(doc, profile="hvnh-thesis"):
    """
    Cấu hình khổ giấy A4 + lề + giãn dòng theo profile đã chọn và khởi tạo hệ thống
    Built-in Heading Styles cho Word Navigation Pane.
    Mặc định 'hvnh-thesis': Trái 3.5cm, Phải 2.0cm, Trên 3.5cm, Dưới 3.0cm, giãn dòng 1.5.
    """
    global CURRENT_PROFILE
    CURRENT_PROFILE = get_profile(profile)

    sec = doc.sections[0]
    m = CURRENT_PROFILE["margins_cm"]
    sec.top_margin = Cm(m["top"])
    sec.bottom_margin = Cm(m["bottom"])
    sec.left_margin = Cm(m["left"])
    sec.right_margin = Cm(m["right"])
    sec.page_width = Cm(21.0)      # 210 mm (A4)
    sec.page_height = Cm(29.7)     # 297 mm (A4)

    ls = CURRENT_PROFILE["line_spacing"]

    # Style Normal (Body Text)
    s_norm = doc.styles['Normal']
    s_norm.font.name = 'Times New Roman'
    s_norm.font.size = Pt(13)
    s_norm.font.color.rgb = COLOR_DARK_TEXT
    s_norm.paragraph_format.line_spacing = ls
    s_norm.paragraph_format.space_after = Pt(6)
    s_norm.paragraph_format.space_before = Pt(0)
    s_norm.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    # Built-in Heading 1 (Word Navigation Pane Level 0)
    s_h1 = doc.styles['Heading 1']
    s_h1.font.name = 'Times New Roman'
    s_h1.font.size = Pt(15.0)
    s_h1.font.bold = True
    s_h1.font.color.rgb = COLOR_NAVY_HVNH
    s_h1.paragraph_format.space_before = Pt(16)
    s_h1.paragraph_format.space_after = Pt(8)
    s_h1.paragraph_format.keep_with_next = True
    s_h1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
    s_h1.paragraph_format.first_line_indent = Cm(0)

    # Built-in Heading 2 (Word Navigation Pane Level 1)
    s_h2 = doc.styles['Heading 2']
    s_h2.font.name = 'Times New Roman'
    s_h2.font.size = Pt(13.5)
    s_h2.font.bold = True
    s_h2.font.color.rgb = COLOR_BLUE_SEC
    s_h2.paragraph_format.space_before = Pt(14)
    s_h2.paragraph_format.space_after = Pt(6)
    s_h2.paragraph_format.keep_with_next = True
    s_h2.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
    s_h2.paragraph_format.first_line_indent = Cm(0)

    # Built-in Heading 3 (Word Navigation Pane Level 2)
    s_h3 = doc.styles['Heading 3']
    s_h3.font.name = 'Times New Roman'
    s_h3.font.size = Pt(13.0)
    s_h3.font.bold = True
    s_h3.font.color.rgb = COLOR_ACCENT_BLUE
    s_h3.paragraph_format.space_before = Pt(10)
    s_h3.paragraph_format.space_after = Pt(4)
    s_h3.paragraph_format.keep_with_next = True
    s_h3.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
    s_h3.paragraph_format.first_line_indent = Cm(0)

# ==============================================================================
# SỐ TRANG GIỮA-PHÍA-TRÊN, ĐẾM TỪ MỞ ĐẦU (chuẩn luận văn HVNH)
# ==============================================================================
def _set_page_number_start(section, start=1):
    """Ghi <w:pgNumType w:start='N'/> vào sectPr theo đúng vị trí schema (trước <w:cols>)."""
    sectPr = section._sectPr
    for el in sectPr.findall(qn('w:pgNumType')):
        sectPr.remove(el)
    pg = parse_xml('<w:pgNumType %s w:start="%d"/>' % (nsdecls('w'), start))
    cols = sectPr.find(qn('w:cols'))
    if cols is not None:
        cols.addprevious(pg)
    else:
        sectPr.append(pg)

def apply_page_numbers_top_center(doc, start_value=1):
    """
    Gọi NGAY TRƯỚC khi thêm tiêu đề 'MỞ ĐẦU'.
    Tạo section mới (ngắt trang): mọi section trước đó (bìa, cam đoan, mục lục...)
    không hiển thị số trang; từ section này trở đi, số trang nằm ở GIỮA PHÍA TRÊN
    và bắt đầu lại từ start_value (=1 theo quy định).
    Trả về section thân bài để tiện kiểm chứng.
    """
    body_sec = doc.add_section(WD_SECTION.NEW_PAGE)
    body_sec.header.is_linked_to_previous = False
    hdr_p = body_sec.header.paragraphs[0]
    hdr_p.paragraph_format.first_line_indent = Cm(0)
    hdr_p.paragraph_format.space_after = Pt(6)
    hdr_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    add_xml_page_field(hdr_p, "PAGE", default_val=str(start_value))
    _set_page_number_start(body_sec, start=start_value)
    return body_sec

def apply_assignment_headers_footers(doc, header_title="", start_value=1):
    """
    Thiết lập Header & Footer chuẩn Bài tập lớn / Tiểu luận môn học HVNH (DoVanDat_CSDLNC template):
    - Tạo section mới (thân bài).
    - Header: căn phải, chữ nghiêng 10pt (tên đề tài/tiểu luận) kèm đường kẻ mảnh phân cách dưới.
    - Footer: căn giữa, định dạng 'Trang {PAGE}', bắt đầu lại từ start_value (1).
    - Section trước (front matter): giữ số trang La Mã i, ii... và bìa không hiển thị số trang.
    """
    body_sec = doc.add_section(WD_SECTION.NEW_PAGE)
    body_sec.header.is_linked_to_previous = False
    body_sec.footer.is_linked_to_previous = False

    # Cấu hình Header thân bài
    if header_title:
        hdr_p = body_sec.header.paragraphs[0]
        hdr_p.paragraph_format.first_line_indent = Cm(0)
        hdr_p.paragraph_format.space_after = Pt(4)
        hdr_p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        # Thêm border bottom mờ cho header paragraph
        pPr = hdr_p._p.get_or_add_pPr()
        pBdr = parse_xml(f'<w:pBdr {nsdecls("w")}><w:bottom w:val="single" w:sz="4" w:space="2" w:color="BBBBBB"/></w:pBdr>')
        pPr.append(pBdr)
        r_hdr = hdr_p.add_run(header_title)
        r_hdr.font.name = 'Times New Roman'
        r_hdr.font.size = Pt(10)
        r_hdr.font.italic = True
        r_hdr.font.color.rgb = COLOR_MUTED_TEXT

    # Cấu hình Footer thân bài: 'Trang {PAGE}'
    ftr_p = body_sec.footer.paragraphs[0]
    ftr_p.paragraph_format.first_line_indent = Cm(0)
    ftr_p.paragraph_format.space_after = Pt(0)
    ftr_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_lbl = ftr_p.add_run("Trang ")
    r_lbl.font.name = 'Times New Roman'
    r_lbl.font.size = Pt(11)
    r_lbl.font.color.rgb = COLOR_MUTED_TEXT
    add_xml_page_field(ftr_p, "PAGE", default_val=str(start_value))
    _set_page_number_start(body_sec, start=start_value)
    return body_sec

# ==============================================================================
# TIỆN ÍCH XML CƠ SỞ
# ==============================================================================
def set_cell_background(cell, hex_color):
    """Thiết lập màu nền ô bảng (Shading)"""
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    cell._tc.get_or_add_tcPr().append(shading_elm)

def set_cell_margins(cell, top=90, bottom=90, left=110, right=110):
    """Thiết lập khoảng đệm trong ô bảng (dxa: 20 dxa = 1 pt)"""
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def add_xml_page_field(p, field_name="PAGE", default_val="1"):
    """Thêm mã trường đếm trang động OpenXML (PAGE / NUMPAGES) kèm fallback cached value"""
    run = p.add_run()
    fldChar1 = parse_xml(r'<w:fldChar %s w:fldCharType="begin"/>' % nsdecls('w'))
    instrText = parse_xml(r'<w:instrText %s xml:space="preserve"> %s </w:instrText>' % (nsdecls('w'), field_name))
    fldChar2 = parse_xml(r'<w:fldChar %s w:fldCharType="separate"/>' % nsdecls('w'))
    cached = parse_xml(r'<w:t %s>%s</w:t>' % (nsdecls('w'), default_val))
    fldChar3 = parse_xml(r'<w:fldChar %s w:fldCharType="end"/>' % nsdecls('w'))
    run._r.append(fldChar1)
    run._r.append(instrText)
    run._r.append(fldChar2)
    run._r.append(cached)
    run._r.append(fldChar3)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(10)
    run.font.color.rgb = COLOR_MUTED_TEXT

# ==============================================================================
# HEADING & NỘI DUNG THÂN BÀI
# ==============================================================================
def add_chapter_heading(doc, text, is_first_chapter=False):
    """Thêm Heading 1 kèm ngắt trang trước mỗi chương (Page break per chapter).
    Lưu ý chuẩn HVNH: tên chương IN HOA, không kết thúc bằng dấu chấm."""
    if not is_first_chapter:
        doc.add_page_break()
    p = doc.add_paragraph(text, style='Heading 1')
    p.paragraph_format.space_before = Pt(16)
    p.paragraph_format.space_after = Pt(8)
    p.paragraph_format.keep_with_next = True
    p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.first_line_indent = Cm(0)
    return p

def add_section_heading(doc, text):
    """Thêm Heading 2 (Mục cấp 1)"""
    p = doc.add_paragraph(text, style='Heading 2')
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.keep_with_next = True
    p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.first_line_indent = Cm(0)
    return p

def add_subsection_heading(doc, text):
    """Thêm Heading 3 (Mục cấp 2). Chuẩn HVNH: tối đa 4 cấp số (3.1.2.1);
    cấm tiểu mục mồ côi — phải có ít nhất 2 tiểu mục trong cùng nhóm."""
    p = doc.add_paragraph(text, style='Heading 3')
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.keep_with_next = True
    p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.first_line_indent = Cm(0)
    return p

def add_body_paragraph(doc, text, indent=True, keep_with_next=False):
    """Thêm đoạn văn nội dung căn đều (Justified) thụt đầu dòng 1.27cm"""
    p = doc.add_paragraph()
    p.paragraph_format.line_spacing = CURRENT_PROFILE["line_spacing"]
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.keep_with_next = keep_with_next
    if indent:
        p.paragraph_format.first_line_indent = Inches(0.5)  # 1.27 cm chuẩn
    else:
        p.paragraph_format.first_line_indent = Cm(0)
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(13)
    run.font.color.rgb = COLOR_DARK_TEXT
    return p

def add_block_quote(doc, text, italic=False):
    """Trích dẫn dài hơn 2 câu hoặc 4 dòng (chuẩn HVNH §2.5):
    tách thành đoạn riêng, lề trái lùi vào thêm 2cm, KHÔNG dùng ngoặc kép."""
    p = doc.add_paragraph()
    p.paragraph_format.line_spacing = CURRENT_PROFILE["line_spacing"]
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.left_indent = Cm(2)
    p.paragraph_format.first_line_indent = Cm(0)
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(13)
    run.font.italic = italic
    run.font.color.rgb = COLOR_DARK_TEXT
    return p

def add_chapter_conclusion(doc, chapter_no, summary_text):
    """Tóm tắt chương (kết luận chương) — bắt buộc ở cuối mỗi chương theo quy định.
    Không nhất thiết sang trang riêng."""
    p_h = doc.add_paragraph(f"TÓM TẮT CHƯƠNG {chapter_no}", style='Heading 2')
    p_h.paragraph_format.space_before = Pt(14)
    p_h.paragraph_format.keep_with_next = True
    return add_body_paragraph(doc, summary_text)

def add_numeric_citation(paragraph, refs, pages=None, before_text=None):
    """Trích dẫn số chuẩn HVNH trong ngoặc vuông, gắn vào paragraph hiện có.
    refs=[15]              -> [15]
    refs=[15], pages='314' -> [15, tr.314]
    refs=[19,25]           -> [19], [25]  (tăng dần, mỗi nguồn một ngoặc)
    """
    if not refs:
        print("[WARN] add_numeric_citation: refs rỗng — không có trích dẫn nào được chèn.")
        return paragraph
    refs = sorted(refs)
    if len(refs) == 1:
        marker = f"[{refs[0]}, tr.{pages}]" if pages else f"[{refs[0]}]"
    else:
        marker = ", ".join(f"[{r}]" for r in refs)
    if before_text:
        r_pre = paragraph.add_run(before_text)
        r_pre.font.name = 'Times New Roman'
        r_pre.font.size = Pt(13)
        r_pre.font.color.rgb = COLOR_DARK_TEXT
    r = paragraph.add_run(marker)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(13)
    r.font.color.rgb = COLOR_DARK_TEXT
    return paragraph

def add_numbered_item(doc, number_str, lead_text, body_text):
    """Thêm mục đánh số với hanging indent 0.3 inch"""
    p = doc.add_paragraph()
    p.paragraph_format.line_spacing = min(CURRENT_PROFILE["line_spacing"], 1.32)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.left_indent = Inches(0.3)
    p.paragraph_format.first_line_indent = Inches(-0.3)

    r_num = p.add_run(number_str + " ")
    r_num.bold = True
    r_num.font.name = 'Times New Roman'
    r_num.font.size = Pt(13)
    r_num.font.color.rgb = COLOR_NAVY_HVNH

    r_lead = p.add_run(lead_text + " ")
    r_lead.bold = True
    r_lead.font.name = 'Times New Roman'
    r_lead.font.size = Pt(13)
    r_lead.font.color.rgb = COLOR_NAVY_HVNH

    r_body = p.add_run(body_text)
    r_body.font.name = 'Times New Roman'
    r_body.font.size = Pt(13)
    r_body.font.color.rgb = COLOR_DARK_TEXT
    return p

def add_bullet_item(doc, lead_text, body_text):
    """Thêm gạch đầu dòng căn Trái (Left) chống dãn chữ"""
    p = doc.add_paragraph()
    p.paragraph_format.line_spacing = min(CURRENT_PROFILE["line_spacing"], 1.3)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.left_indent = Inches(0.3)
    p.paragraph_format.first_line_indent = Inches(-0.2)

    r_bullet = p.add_run("• ")
    r_bullet.bold = True
    r_bullet.font.name = 'Times New Roman'
    r_bullet.font.size = Pt(13)
    r_bullet.font.color.rgb = COLOR_NAVY_HVNH

    if lead_text:
        r_lead = p.add_run(lead_text + " ")
        r_lead.bold = True
        r_lead.font.name = 'Times New Roman'
        r_lead.font.size = Pt(13)
        r_lead.font.color.rgb = COLOR_NAVY_HVNH

    r_body = p.add_run(body_text)
    r_body.font.name = 'Times New Roman'
    r_body.font.size = Pt(13)
    r_body.font.color.rgb = COLOR_DARK_TEXT
    return p

def add_callout_box(doc, title, text, is_warning=False):
    """Tạo hộp Callout với viền trái màu nổi bật, nền xám nhạt và căn Trái chống dãn chữ"""
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = table.cell(0, 0)
    set_cell_background(cell, HEX_CALLOUT_BG)
    set_cell_margins(cell, top=120, bottom=120, left=160, right=140)

    border_color = HEX_ORANGE if is_warning else HEX_BLUE_HDR
    icon = "🚨" if is_warning else "💡"

    tcPr = cell._tc.get_or_add_tcPr()
    borders = parse_xml(f'<w:tcBorders {nsdecls("w")}><w:left w:val="single" w:sz="28" w:space="0" w:color="{border_color}"/><w:top w:val="none"/><w:right w:val="none"/><w:bottom w:val="none"/></w:tcBorders>')
    tcPr.append(borders)

    p_title = cell.paragraphs[0]
    p_title.paragraph_format.line_spacing = 1.2
    p_title.paragraph_format.space_before = Pt(0)
    p_title.paragraph_format.space_after = Pt(4)
    p_title.paragraph_format.first_line_indent = Cm(0)
    p_title.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT

    r_title = p_title.add_run(f"{icon} {title}")
    r_title.bold = True
    r_title.font.name = 'Times New Roman'
    r_title.font.size = Pt(12)
    r_title.font.color.rgb = COLOR_ORANGE_HVNH if is_warning else COLOR_NAVY_HVNH

    p_body = cell.add_paragraph()
    p_body.paragraph_format.line_spacing = 1.25
    p_body.paragraph_format.space_before = Pt(0)
    p_body.paragraph_format.space_after = Pt(0)
    p_body.paragraph_format.first_line_indent = Cm(0)
    p_body.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT

    r_body = p_body.add_run(text)
    r_body.font.name = 'Times New Roman'
    r_body.font.size = Pt(12)
    r_body.font.color.rgb = COLOR_DARK_TEXT

    p_sp = doc.add_paragraph()
    p_sp.paragraph_format.space_after = Pt(4)
    p_sp.paragraph_format.space_before = Pt(0)

# ==============================================================================
# CAPTION GẮN SỐ CHƯƠNG (Hình 3.4 / Bảng 2.1) — chuẩn luận văn HVNH
# ==============================================================================
def chapter_label(chapter_no, index_in_chapter):
    """Sinh nhãn đánh số gắn chương: ('3', 4) -> '3.4'. Dùng cho cả hình, bảng, phương trình."""
    return f"{chapter_no}.{index_in_chapter}"

def add_figure_with_caption(doc, img_path, fig_num, caption, source_text="(Nguồn: Kết quả phân tích từ tập dữ liệu thực nghiệm)", width=None):
    """Chèn hình ảnh kèm caption PHÍA DƯỚI hình + nguồn trích dẫn.
    fig_num nhận chuỗi gắn chương '3.4' (chuẩn luận văn HVNH) hoặc số nguyên (tương thích v1).
    Nếu img_path không tồn tại, hàm KHÔNG dừng chương trình — chỉ in cảnh báo rõ ràng và
    vẫn chèn caption (để không làm gãy số thứ tự Hình/Bảng đã lập kế hoạch từ trước)."""
    if width is None:
        width = Inches(5.9) if CURRENT_PROFILE is PROFILES["nd30-report"] else Cm(14.6)
    if os.path.exists(img_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(10)
        p_img.paragraph_format.space_after = Pt(4)
        p_img.paragraph_format.first_line_indent = Cm(0)
        p_img.paragraph_format.keep_with_next = True
        run = p_img.add_run()
        run.add_picture(img_path, width=width)
    else:
        print(f"[WARN] add_figure_with_caption: không tìm thấy ảnh tại '{img_path}' — Hình {fig_num} chỉ có caption, thiếu hình minh họa. Nhớ chèn ảnh trước khi nộp.")

    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap.paragraph_format.space_before = Pt(2)
    p_cap.paragraph_format.space_after = Pt(12)
    p_cap.paragraph_format.first_line_indent = Cm(0)

    r_num = p_cap.add_run(f"Hình {fig_num}: ")
    r_num.bold = True
    r_num.font.name = 'Times New Roman'
    r_num.font.size = Pt(11.5)
    r_num.font.color.rgb = COLOR_NAVY_HVNH

    r_cap = p_cap.add_run(caption + "\n")
    r_cap.font.name = 'Times New Roman'
    r_cap.font.size = Pt(11.5)
    r_cap.italic = True
    r_cap.font.color.rgb = COLOR_DARK_TEXT

    if source_text:
        r_src = p_cap.add_run(source_text)
        r_src.font.name = 'Times New Roman'
        r_src.font.size = Pt(10)
        r_src.italic = True
        r_src.font.color.rgb = COLOR_MUTED_TEXT

def _apply_table_body_style(table, zebra=True):
    """Định dạng thân bảng học thuật: tblHeader (lặp header qua trang), cantSplit,
    viền, padding, zebra striping, font ô bảng."""
    header_tr = table.rows[0]._tr.get_or_add_trPr()
    header_tr.append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))

    for i, row in enumerate(table.rows):
        trPr = row._tr.get_or_add_trPr()
        trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))

        for cell in row.cells:
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            set_cell_margins(cell, top=90, bottom=90, left=110, right=110)
            tcPr = cell._tc.get_or_add_tcPr()
            borders = parse_xml(f'<w:tcBorders {nsdecls("w")}><w:top w:val="single" w:sz="4" w:space="0" w:color="{HEX_BORDER}"/><w:bottom w:val="single" w:sz="4" w:space="0" w:color="{HEX_BORDER}"/><w:left w:val="single" w:sz="4" w:space="0" w:color="{HEX_BORDER}"/><w:right w:val="single" w:sz="4" w:space="0" w:color="{HEX_BORDER}"/></w:tcBorders>')
            tcPr.append(borders)

            for p in cell.paragraphs:
                p.paragraph_format.line_spacing = 1.15
                p.paragraph_format.space_after = Pt(2)
                p.paragraph_format.space_before = Pt(2)
                p.paragraph_format.first_line_indent = Cm(0)
                if i == 0:
                    set_cell_background(cell, HEX_BLUE_HDR)
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    for r in p.runs:
                        r.bold = True
                        r.font.name = 'Times New Roman'
                        r.font.size = Pt(10.5)
                        r.font.color.rgb = RGBColor(255, 255, 255)
                else:
                    if zebra and i % 2 == 1:
                        set_cell_background(cell, HEX_ZEBRA_BG)
                    for r in p.runs:
                        r.font.name = 'Times New Roman'
                        r.font.size = Pt(10.5)
                        r.font.color.rgb = COLOR_DARK_TEXT

def style_academic_table(doc, table, table_num, table_title, zebra=True):
    """Định dạng bảng học thuật kèm đầu đề PHÍA TRÊN bảng.
    table_num nhận chuỗi gắn chương '2.1' (chuẩn HVNH) hoặc số nguyên (tương thích v1)."""
    p_ttl = doc.add_paragraph()
    p_ttl.paragraph_format.space_before = Pt(10)
    p_ttl.paragraph_format.space_after = Pt(4)
    p_ttl.paragraph_format.keep_with_next = True
    p_ttl.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p_ttl.paragraph_format.first_line_indent = Cm(0)

    r_tnum = p_ttl.add_run(f"Bảng {table_num}: ")
    r_tnum.bold = True
    r_tnum.font.name = 'Times New Roman'
    r_tnum.font.size = Pt(11.5)
    r_tnum.font.color.rgb = COLOR_NAVY_HVNH

    r_tname = p_ttl.add_run(table_title)
    r_tname.bold = True
    r_tname.font.name = 'Times New Roman'
    r_tname.font.size = Pt(11.5)
    r_tname.font.color.rgb = COLOR_DARK_TEXT

    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    _apply_table_body_style(table, zebra=zebra)

    p_sp = doc.add_paragraph()
    p_sp.paragraph_format.space_after = Pt(6)
    p_sp.paragraph_format.space_before = Pt(0)

# ==============================================================================
# TRANG ĐẦU: PHỤ BÌA, CAM ĐOAN, MỤC LỤC, DANH MỤC
# ==============================================================================
def add_title_page(doc, ten_de_tai, tac_gia, chuyen_nganh="", ma_so="",
                   nguoi_huong_dan=(), loai_luan_van="LUẬN VĂN THẠC SĨ KINH TẾ",
                   co_quan_chu_quan=("NGÂN HÀNG NHÀ NƯỚC VIỆT NAM", "BỘ GIÁO DỤC VÀ ĐÀO TẠO"),
                   noi_thang_ban="Hà Nội - năm 2026"):
    """Trang phụ bìa theo Mẫu 10 — Quy định trình bày luận văn HVNH.
    Tên đề tài IN HOA, không viết tắt. Bìa ngoài (đóng gáy in chữ nhũ) in ấn riêng theo Mẫu 09."""
    def _center(text, size=13, bold=False, space_after=0, color=COLOR_DARK_TEXT):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(space_after)
        p.paragraph_format.first_line_indent = Cm(0)
        r = p.add_run(text.upper() if size >= 16 else text)
        r.bold = bold
        r.font.name = 'Times New Roman'
        r.font.size = Pt(size)
        r.font.color.rgb = color
        return p

    for i, cq in enumerate(co_quan_chu_quan):
        _center(cq, size=13, bold=True, space_after=0 if i < len(co_quan_chu_quan) - 1 else 6)
    _center("HỌC VIỆN NGÂN HÀNG", size=14, bold=True, space_after=72)
    _center(tac_gia, size=14, bold=True, space_after=48)
    _center(ten_de_tai, size=17, bold=True, space_after=36)
    if chuyen_nganh:
        _center(f"Chuyên ngành: {chuyen_nganh}", size=13, space_after=2)
    if ma_so:
        _center(f"Mã số: {ma_so}", size=13, space_after=24)
    _center(loai_luan_van, size=14, bold=True, space_after=36)
    if nguoi_huong_dan:
        _center("Người hướng dẫn khoa học:", size=13, bold=True, space_after=2)
        for i, gv in enumerate(nguoi_huong_dan):
            _center(f"{i + 1}. {gv}", size=13, space_after=2)
    _center("", space_after=60)
    _center(noi_thang_ban, size=13, bold=True)
    doc.add_page_break()

def add_assignment_cover_page(doc, ten_de_tai, mon_hoc, giang_vien_hd, sinh_vien_th, ma_sv="", lop="", dia_diem_nam="HÀ NỘI – 2026"):
    """
    Tạo trang bìa chuẩn Bài tập lớn / Tiểu luận môn học HVNH (theo mẫu DoVanDat_CSDLNC.docx):
    - Khung viền hoa văn trang bìa (display='firstPage')
    - Cơ quan: HỌC VIỆN NGÂN HÀNG - KHOA SAU ĐẠI HỌC
    - Tiêu đề: BÀI TIỂU LUẬN / BÀI TẬP LỚN - MÔN HỌC
    - ĐỀ TÀI: [TÊN ĐỀ TÀI IN HOA]
    - Bảng thông tin: GVHD, Sinh viên, Mã SV, Lớp (căn lề gọn gàng)
    - Địa danh - Năm
    """
    sec = doc.sections[0]
    sec.different_first_page_header_footer = True

    # Thêm Page Borders cho trang đầu tiên của Section 0
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
    _set_page_number_start(sec, start=1)

    # Đoạn văn phần trên bìa
    p1 = doc.add_paragraph()
    p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p1.paragraph_format.space_before = Pt(0)
    p1.paragraph_format.space_after = Pt(2)
    p1.paragraph_format.first_line_indent = Cm(0)
    r1 = p1.add_run("HỌC VIỆN NGÂN HÀNG")
    r1.bold = True
    r1.font.name = 'Times New Roman'
    r1.font.size = Pt(16)

    p2 = doc.add_paragraph()
    p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p2.paragraph_format.space_before = Pt(0)
    p2.paragraph_format.space_after = Pt(36)
    p2.paragraph_format.first_line_indent = Cm(0)
    r2 = p2.add_run("KHOA SAU ĐẠI HỌC")
    r2.bold = True
    r2.font.name = 'Times New Roman'
    r2.font.size = Pt(16)

    p3 = doc.add_paragraph()
    p3.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p3.paragraph_format.space_before = Pt(0)
    p3.paragraph_format.space_after = Pt(6)
    p3.paragraph_format.first_line_indent = Cm(0)
    r3 = p3.add_run("BÀI TIỂU LUẬN")
    r3.bold = True
    r3.font.name = 'Times New Roman'
    r3.font.size = Pt(18)

    p4 = doc.add_paragraph()
    p4.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p4.paragraph_format.space_before = Pt(0)
    p4.paragraph_format.space_after = Pt(30)
    p4.paragraph_format.first_line_indent = Cm(0)
    r4 = p4.add_run(f"MÔN: {mon_hoc.upper()}")
    r4.bold = True
    r4.font.name = 'Times New Roman'
    r4.font.size = Pt(18)

    p5 = doc.add_paragraph()
    p5.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p5.paragraph_format.space_before = Pt(0)
    p5.paragraph_format.space_after = Pt(40)
    p5.paragraph_format.first_line_indent = Cm(0)
    r5_label = p5.add_run("ĐỀ TÀI: ")
    r5_label.bold = True
    r5_label.font.name = 'Times New Roman'
    r5_label.font.size = Pt(16)
    r5_title = p5.add_run(ten_de_tai.upper())
    r5_title.bold = True
    r5_title.font.name = 'Times New Roman'
    r5_title.font.size = Pt(16)

    # Bảng thông tin tác giả (GVHD, SV, Lớp...)
    meta_rows = [
        ("Giảng viên hướng dẫn", giang_vien_hd),
        ("Sinh viên thực hiện", f"{sinh_vien_th}{f' - {ma_sv}' if ma_sv else ''}"),
        ("Lớp", lop)
    ]
    meta_rows = [row for row in meta_rows if row[1]]

    tbl = doc.add_table(rows=len(meta_rows), cols=2)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, (label, val) in enumerate(meta_rows):
        c0, c1 = tbl.rows[i].cells[0], tbl.rows[i].cells[1]
        c0.width = Inches(2.2)
        c1.width = Inches(3.8)
        p_c0 = c0.paragraphs[0]
        p_c0.paragraph_format.space_after = Pt(4)
        p_c0.paragraph_format.first_line_indent = Cm(0)
        r_l = p_c0.add_run(label + ":")
        r_l.bold = True
        r_l.font.name = 'Times New Roman'
        r_l.font.size = Pt(13)

        p_c1 = c1.paragraphs[0]
        p_c1.paragraph_format.space_after = Pt(4)
        p_c1.paragraph_format.first_line_indent = Cm(0)
        r_v = p_c1.add_run(val)
        r_v.font.name = 'Times New Roman'
        r_v.font.size = Pt(13)

    p_sp = doc.add_paragraph()
    p_sp.paragraph_format.space_after = Pt(60)

    p_bot = doc.add_paragraph()
    p_bot.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_bot.paragraph_format.space_after = Pt(0)
    p_bot.paragraph_format.first_line_indent = Cm(0)
    r_bot = p_bot.add_run(dia_diem_nam)
    r_bot.bold = True
    r_bot.font.name = 'Times New Roman'
    r_bot.font.size = Pt(13)
    doc.add_page_break()

def add_instructor_review_page(doc, dia_diem_nam="Hà Nội, ngày … tháng … năm 2026"):
    """
    Trang NHẬN XÉT CỦA GIẢNG VIÊN HƯỚNG DẪN chuẩn Bài tập lớn HVNH.
    Gồm tiêu đề, 10 dòng chấm và vị trí ký tên.
    """
    p_h = doc.add_paragraph("NHẬN XÉT CỦA GIẢNG VIÊN HƯỚNG DẪN")
    p_h.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_h.paragraph_format.space_before = Pt(12)
    p_h.paragraph_format.space_after = Pt(18)
    p_h.paragraph_format.first_line_indent = Cm(0)
    for r in p_h.runs:
        r.bold = True
        r.font.name = 'Times New Roman'
        r.font.size = Pt(14)
        r.font.color.rgb = COLOR_NAVY_HVNH

    # Các dòng chấm ghi nhận xét
    for _ in range(10):
        p_dot = doc.add_paragraph()
        p_dot.paragraph_format.space_before = Pt(8)
        p_dot.paragraph_format.space_after = Pt(8)
        p_dot.paragraph_format.first_line_indent = Cm(0)
        pPr = p_dot._p.get_or_add_pPr()
        pBdr = parse_xml(f'<w:pBdr {nsdecls("w")}><w:bottom w:val="dotted" w:sz="4" w:space="4" w:color="AAAAAA"/></w:pBdr>')
        pPr.append(pBdr)

    p_loc = doc.add_paragraph()
    p_loc.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p_loc.paragraph_format.space_before = Pt(20)
    p_loc.paragraph_format.space_after = Pt(4)
    p_loc.paragraph_format.first_line_indent = Cm(0)
    r_loc = p_loc.add_run(dia_diem_nam)
    r_loc.font.name = 'Times New Roman'
    r_loc.font.size = Pt(13)
    r_loc.italic = True

    p_sign = doc.add_paragraph()
    p_sign.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p_sign.paragraph_format.space_after = Pt(0)
    p_sign.paragraph_format.first_line_indent = Cm(0)
    r_sign = p_sign.add_run("Giảng viên hướng dẫn")
    r_sign.bold = True
    r_sign.font.name = 'Times New Roman'
    r_sign.font.size = Pt(13)
    doc.add_page_break()

def add_cam_doan_page(doc, ho_ten, ten_de_tai, dia_diem="Hà Nội"):
    """Trang CAM ĐOAN danh dự — bắt buộc theo quy định chung của HVNH."""
    p_h = doc.add_paragraph("CAM ĐOAN")
    p_h.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_h.paragraph_format.space_before = Pt(24)
    p_h.paragraph_format.space_after = Pt(18)
    p_h.paragraph_format.first_line_indent = Cm(0)
    for r in p_h.runs:
        r.bold = True
        r.font.name = 'Times New Roman'
        r.font.size = Pt(15)
        r.font.color.rgb = COLOR_NAVY_HVNH

    body = (
        f"Tôi cam đoan rằng công trình nghiên cứu \"{ten_de_tai}\" là sản phẩm do bản thân tôi "
        "trực tiếp thực hiện dưới sự hướng dẫn khoa học. Các số liệu và kết quả nêu trong luận văn "
        "là trung thực và chưa từng được công bố dưới bất kỳ hình thức nào. Nếu có sự vi phạm, "
        "tôi xin hoàn toàn chịu trách nhiệm trước Hội đồng khoa học và Học viện Ngân hàng."
    )
    add_body_paragraph(doc, body, indent=True)

    p_sign = doc.add_paragraph()
    p_sign.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p_sign.paragraph_format.space_before = Pt(36)
    p_sig_loc = p_sign.add_run(f"{dia_diem}, ngày ...... tháng ...... năm ......")
    p_sig_loc.font.name = 'Times New Roman'
    p_sig_loc.font.size = Pt(13)
    p_sign2 = doc.add_paragraph()
    p_sign2.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p_sig_author = p_sign2.add_run("Tác giả luận văn\n\n\n")
    p_sig_author.font.name = 'Times New Roman'
    p_sig_author.font.size = Pt(13)
    r_name = p_sign2.add_run(ho_ten)
    r_name.bold = True
    r_name.font.name = 'Times New Roman'
    r_name.font.size = Pt(13)
    doc.add_page_break()

def add_toc_field(doc, heading_text="MỤC LỤC"):
    """Mục lục động đến 3 cấp số (TOC \\o '1-3') — chuẩn 'Mục lục đánh đến 3 số'.
    Word sẽ tự hỏi cập nhật khi mở file nhờ cờ updateFields; người dùng cũng có thể F9."""
    p_h = doc.add_paragraph(heading_text)
    p_h.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_h.paragraph_format.space_after = Pt(18)
    p_h.paragraph_format.first_line_indent = Cm(0)
    for r in p_h.runs:
        r.bold = True
        r.font.name = 'Times New Roman'
        r.font.size = Pt(15)
        r.font.color.rgb = COLOR_NAVY_HVNH

    p = doc.add_paragraph()
    p.paragraph_format.line_spacing = CURRENT_PROFILE["line_spacing"]
    run = p.add_run()
    begin = parse_xml(r'<w:fldChar %s w:fldCharType="begin"/>' % nsdecls('w'))
    instr = parse_xml(r'<w:instrText %s xml:space="preserve"> TOC \o "1-3" \h \z \u </w:instrText>' % nsdecls('w'))
    sep = parse_xml(r'<w:fldChar %s w:fldCharType="separate"/>' % nsdecls('w'))
    cached = parse_xml(r'<w:t %s>(Mở file trong Word và chọn Update Field / F9 để hiển thị mục lục)</w:t>' % nsdecls('w'))
    end = parse_xml(r'<w:fldChar %s w:fldCharType="end"/>' % nsdecls('w'))
    for el in (begin, instr, sep, cached, end):
        run._r.append(el)

    settings_el = doc.settings.element
    if not settings_el.findall(qn('w:updateFields')):
        settings_el.append(parse_xml('<w:updateFields %s w:val="true"/>' % nsdecls('w')))
    doc.add_page_break()

def add_abbreviation_table(doc, abbrev_items):
    """DANH MỤC CHỮ VIẾT TẮT xếp A→Z (quy định §2.4). abbrev_items: [(viết_tắt, nghĩa), ...]."""
    p_h = doc.add_paragraph("DANH MỤC CHỮ VIẾT TẮT")
    p_h.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_h.paragraph_format.space_after = Pt(12)
    p_h.paragraph_format.first_line_indent = Cm(0)
    for r in p_h.runs:
        r.bold = True
        r.font.name = 'Times New Roman'
        r.font.size = Pt(15)
        r.font.color.rgb = COLOR_NAVY_HVNH

    items = sorted(abbrev_items, key=lambda kv: kv[0].upper())
    t = doc.add_table(rows=len(items) + 1, cols=2)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.rows[0].cells[0].paragraphs[0].add_run("Chữ viết tắt").bold = True
    t.rows[0].cells[1].paragraphs[0].add_run("Viết đầy đủ / Ý nghĩa").bold = True
    for i, (abbr, full) in enumerate(items, start=1):
        t.rows[i].cells[0].paragraphs[0].add_run(abbr)
        t.rows[i].cells[1].paragraphs[0].add_run(full)
    _apply_table_body_style(t, zebra=False)
    doc.add_page_break()

def add_exhibits_list(doc, heading_text, entries, label_prefix=None):
    """DANH MỤC BẢNG BIỂU / HÌNH VẼ dạng tĩnh. entries: [('2.1', 'Tiêu đề bảng/hình', trang), ...]."""
    p_h = doc.add_paragraph(heading_text)
    p_h.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_h.paragraph_format.space_after = Pt(12)
    p_h.paragraph_format.first_line_indent = Cm(0)
    for r in p_h.runs:
        r.bold = True
        r.font.name = 'Times New Roman'
        r.font.size = Pt(15)
        r.font.color.rgb = COLOR_NAVY_HVNH

    for label, caption, page in entries:
        p = doc.add_paragraph()
        p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.left_indent = Cm(1.5)
        p.paragraph_format.first_line_indent = Cm(-1.5)
        p.paragraph_format.line_spacing = CURRENT_PROFILE["line_spacing"]
        p.paragraph_format.space_after = Pt(4)
        prefix = label_prefix or ("Bảng" if "BẢNG" in heading_text.upper() else "Hình")
        r_lbl = p.add_run(f"{prefix} {label}: ")
        r_lbl.bold = True
        r_lbl.font.name = 'Times New Roman'
        r_lbl.font.size = Pt(13)
        r_lbl.font.color.rgb = COLOR_NAVY_HVNH
        r_txt = p.add_run(caption)
        r_txt.font.name = 'Times New Roman'
        r_txt.font.size = Pt(13)
        r_txt.font.color.rgb = COLOR_DARK_TEXT
        if page:
            r_pg = p.add_run(f"  .......... {page}")
            r_pg.font.name = 'Times New Roman'
            r_pg.font.size = Pt(13)
    doc.add_page_break()

# ==============================================================================
# TÀI LIỆU THAM KHẢO CHUẨN HVNH (đánh số, tách ngôn ngữ, hanging indent 1cm)
# ==============================================================================
def hvnh_book(author, year, title, publisher, place):
    """Segment entry cho sách/luận án/báo cáo: Tác giả (Năm), Tên sách (nghiêng), NXB, Nơi XB."""
    return [
        (f"{author} ({year}), ", False),
        (title, True),
        (f", {publisher}, {place}.", False),
    ]

def hvnh_journal_article(author, year, article_title, journal, volume, issue, pages, english=False):
    """Segment entry cho bài báo tạp chí: Tác giả (Năm), \"Tên bài\" (ngoặc kép),
    Tên tạp chí (nghiêng), Tập(Số), tr./pp.trang."""
    page_prefix = "pp." if english else "tr."
    return [
        (f"{author} ({year}), ", False),
        (f"“{article_title}”", False),
        (", ", False),
        (journal, True),
        (f", {volume}({issue}), {page_prefix}{pages}.", False),
    ]

def add_reference_section_hvnh(doc, vietnamese_entries, foreign_entries):
    """Phần TÀI LIỆU THAM KHẢO chuẩn HVNH:
    - Đánh số liên tục xuyên hai nhóm ngôn ngữ (số này được dùng cho trích dẫn [n] trong thân bài)
    - Tách Tiếng Việt / Tiếng Anh; VN xếp ABC theo TÊN, nước ngoài theo HỌ (caller đã sort trước)
    - Entry dài hơn một dòng: dòng thứ hai lùi vào 1cm (hanging indent 1cm)
    vietnamese_entries / foreign_entries: danh sách segment trả về bởi hvnh_book / hvnh_journal_article
    """
    if not vietnamese_entries and not foreign_entries:
        print("[WARN] add_reference_section_hvnh: cả hai danh sách Tiếng Việt và Tiếng Anh đều rỗng — mục TÀI LIỆU THAM KHẢO sẽ trống.")

    doc.add_page_break()
    p_h = doc.add_paragraph("TÀI LIỆU THAM KHẢO", style='Heading 1')
    p_h.paragraph_format.space_before = Pt(16)
    p_h.paragraph_format.first_line_indent = Cm(0)

    counter = {"n": 0}

    def _subhead(text):
        p_s = doc.add_paragraph(text)
        p_s.paragraph_format.space_before = Pt(12)
        p_s.paragraph_format.space_after = Pt(6)
        p_s.paragraph_format.first_line_indent = Cm(0)
        p_s.runs[0].bold = True
        p_s.runs[0].font.name = 'Times New Roman'
        p_s.runs[0].font.size = Pt(13.5)
        p_s.runs[0].font.color.rgb = COLOR_BLUE_SEC

    def _entry(segments):
        counter["n"] += 1
        p = doc.add_paragraph()
        p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.left_indent = Cm(1.0)
        p.paragraph_format.first_line_indent = Cm(-1.0)
        p.paragraph_format.line_spacing = CURRENT_PROFILE["line_spacing"]
        p.paragraph_format.space_after = Pt(6)
        r_num = p.add_run(f"{counter['n']}. ")
        r_num.font.name = 'Times New Roman'
        r_num.font.size = Pt(13)
        r_num.font.color.rgb = COLOR_DARK_TEXT
        for txt, italic in segments:
            r = p.add_run(txt)
            r.italic = italic
            r.font.name = 'Times New Roman'
            r.font.size = Pt(13)
            r.font.color.rgb = COLOR_DARK_TEXT
        return p

    _subhead("Tiếng Việt")
    for seg in vietnamese_entries:
        _entry(seg)
    if foreign_entries:
        _subhead("Tiếng Anh")
        for seg in foreign_entries:
            _entry(seg)

def add_published_works_section(doc, works):
    """DANH MỤC CÔNG TRÌNH KHOA HỌC CỦA TÁC GIẢ ĐÃ CÔNG BỐ — đứng trước TLTK theo trình tự."""
    doc.add_page_break()
    p_h = doc.add_paragraph("DANH MỤC CÔNG TRÌNH KHOA HỌC CỦA TÁC GIẢ ĐÃ CÔNG BỐ", style='Heading 1')
    p_h.paragraph_format.first_line_indent = Cm(0)
    for i, w in enumerate(works, start=1):
        p = doc.add_paragraph()
        p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.left_indent = Cm(1.0)
        p.paragraph_format.first_line_indent = Cm(-1.0)
        p.paragraph_format.space_after = Pt(4)
        r_n = p.add_run(f"{i}. ")
        r_n.font.name = 'Times New Roman'
        r_n.font.size = Pt(13)
        r_w = p.add_run(w)
        r_w.font.name = 'Times New Roman'
        r_w.font.size = Pt(13)

# ==============================================================================
# TỰ KIỂM TRA TÀI LIỆU TRƯỚC KHI GIAO (QA Gate)
# ==============================================================================
def validate_document(doc, profile_name=None, min_heading1=1):
    """
    Tự dò lại tài liệu vừa dựng và in checklist Đạt/Không đạt trước khi xuất file .docx,
    đối chiếu với §7 Checklist Gate của hvnh_thesis_standard.md:
      - Lề (trên/dưới/trái/phải) khớp profile đang dùng, sai lệch cho phép ±0.05cm.
      - Giãn dòng của style Normal khớp profile (1.5 cho hvnh-thesis/hvnh-khoaluan).
      - Nếu profile dùng số trang giữa-phía-trên: đã gọi apply_page_numbers_top_center()
        (kiểm tra gián tiếp qua số lượng section — tối thiểu 2: phần đầu + thân bài).
      - Có ít nhất min_heading1 Heading 1 và không có Heading 1 nào bị để trống.
    Trả về True nếu không phát hiện vấn đề, False nếu có — luôn in báo cáo ra console.

    Giới hạn: KHÔNG kiểm tra được font Times New Roman có thực sự cài trên máy render
    hay không (chỉ kiểm tra tên font ghi trong style); KHÔNG kiểm tra tiểu mục mồ côi,
    caption gắn chương hay khớp trích dẫn [n] với TLTK — các mục đó vẫn cần rà tay theo
    checklist đầy đủ trong hvnh_thesis_standard.md §7.
    """
    issues = []
    profile = CURRENT_PROFILE if profile_name is None else get_profile(profile_name)

    sec = doc.sections[-1]
    m = profile["margins_cm"]
    actual = {
        "top": round(sec.top_margin.cm, 2),
        "bottom": round(sec.bottom_margin.cm, 2),
        "left": round(sec.left_margin.cm, 2),
        "right": round(sec.right_margin.cm, 2),
    }
    for k in ("top", "bottom", "left", "right"):
        if abs(actual[k] - m[k]) > 0.05:
            issues.append(f"Lề {k} = {actual[k]}cm, khác chuẩn profile '{profile['name']}' ({m[k]}cm).")

    s_norm = doc.styles['Normal']
    actual_ls = s_norm.paragraph_format.line_spacing
    if actual_ls is None:
        issues.append("Style Normal chưa có giá trị line_spacing — chưa gọi configure_academic_document().")
    elif abs(actual_ls - profile["line_spacing"]) > 0.01:
        issues.append(f"Giãn dòng Normal = {actual_ls}, khác chuẩn profile ({profile['line_spacing']}).")

    if profile["page_number_pos"] == "top-center" and len(doc.sections) < 2:
        issues.append("Chưa gọi apply_page_numbers_top_center() — tài liệu chỉ có 1 section, số trang giữa-phía-trên chưa được thiết lập.")

    h1_texts = [p.text.strip() for p in doc.paragraphs if p.style.name == 'Heading 1']
    if len(h1_texts) < min_heading1:
        issues.append(f"Chỉ có {len(h1_texts)} Heading 1, ít hơn kỳ vọng tối thiểu ({min_heading1}).")
    empty_h1 = sum(1 for t in h1_texts if not t)
    if empty_h1:
        issues.append(f"Có {empty_h1} Heading 1 rỗng (không có tiêu đề).")

    print("=== VALIDATE DOCUMENT: BÁO CÁO KIỂM TRA ===")
    print(f"Profile đối chiếu: {profile['name']}")
    print(f"Số Heading 1 (chương/mục lớn): {len(h1_texts)}")
    if not issues:
        print("✅ ĐẠT — không phát hiện sai lệch so với profile.")
    else:
        print(f"⚠️ PHÁT HIỆN {len(issues)} VẤN ĐỀ:")
        for iss in issues:
            print(f"  - {iss}")
    print("Lưu ý: hãy đối chiếu thêm checklist đầy đủ ở hvnh_thesis_standard.md §7 (tiểu mục mồ côi, caption gắn chương, khớp trích dẫn TLTK...) — các mục này chưa được kiểm tự động.")
    return len(issues) == 0
