# Quy Chuẩn Định Dạng Bài Tập Lớn / Tiểu Luận Học Viên (Assignment / Coursework Standard)

> **Mẫu thực tế tham chiếu:** `DoVanDat_CSDLNC.docx` (Khoa Sau đại học - Học viện Ngân hàng / Môn Cơ sở dữ liệu nâng cao).  
> **Template tệp tin mẫu sạch:** `templates/DoVanDat_CSDLNC_template.docx`.  
> **Profile áp dụng trong code:** `hvnh-assignment` (hoặc `hvnh-tieuluan`).

---

## 1. Mục Đích & Phạm Vi Sử Dụng

Quy chuẩn này dành riêng cho:
- **Bài tập lớn (BTL) / Bài tập chuyên đề học phần**.
- **Tiểu luận môn học** bậc Cao học (Thạc sĩ) và Đại học chất lượng cao tại Học viện Ngân hàng.
- **Báo cáo thực hành môn học / Lab assignment**.

Khác với **Luận văn Thạc sĩ tốt nghiệp** (profile `hvnh-thesis` vốn có yêu cầu đóng bìa cứng nhũ vàng, trang phụ bìa mẫu 10, số trang giữa đỉnh), quy chuẩn **Bài tập lớn / Tiểu luận môn học** (`hvnh-assignment`) được tinh gọn, mang tính ứng dụng cao, hỗ trợ bìa khung viền hoa văn chuẩn, phần nhận xét giảng viên, header tên đề tài và footer đánh số trang dưới đáy.

---

## 2. Bảng Thông Số Định Dạng Cốt Lõi (`hvnh-assignment`)

| Hạng mục | Thông số chuẩn (`DoVanDat_CSDLNC.docx`) | Chi tiết kỹ thuật OpenXML / Word |
| :--- | :--- | :--- |
| **Khổ giấy** | **Letter / A4** (Mặc định A4 $210 \times 297\text{ mm}$ hoặc Letter) | `w:pgSz w:w="12240" w:h="15840"` |
| **Lề trang (Margins)** | **Trái: 3.0 cm**, **Phải: 2.54 cm** (1 in), **Trên: 2.54 cm**, **Dưới: 2.54 cm** | `w:pgMar w:left="1701" w:right="1440" w:top="1440" w:bottom="1440"` (chừa gáy 3cm bấm kim/đóng tập) |
| **Font chữ** | **Times New Roman** xuyên suốt | Bảng mã Unicode, cỡ chữ 13pt cho thân bài |
| **Giãn dòng (Line spacing)** | **1.5 lines** (bắt buộc) | `line_spacing = 1.5` (`w:spacing w:line="360"`) |
| **Giãn đoạn (Paragraph spacing)** | After **6 pt**, Before **0 pt** | Thân bài không bị dính sát nhau |
| **Căn lề thân bài (Body Text)** | **Justified (Căn đều 2 bên)** | Thụt đầu dòng dòng đầu tiên: **1.0 cm – 1.27 cm** (first line indent) |
| **Phân cách Section** | **2 Sections riêng biệt**: Section 0 (Front matter) & Section 1 (Body) | Giúp ngắt số trang La Mã và số trang Ả Rập |
| **Đánh số trang Section 0** | Số La Mã thường (`i`, `ii`, ...), căn giữa chân trang (Footer), trang bìa ẩn số | `w:pgNumType w:fmt="lowerRoman" w:start="1"`, `different_first_page = True` |
| **Đánh số trang Section 1** | Căn giữa chân trang (Footer), format: **`Trang {PAGE}`**, bắt đầu lại từ 1 | `w:pgNumType w:start="1"`, `w:instrText` = `PAGE` |
| **Header (Tiêu đề đầu trang)** | Xuất hiện từ Section 1: Căn phải, chữ nghiêng 10pt kèm đường kẻ mờ phân cách | Text: `Tên đề tài bài tập / tiểu luận`, `w:pBdr/w:bottom` |

---

## 3. Cấu Trúc Toàn Văn Chuẩn Bài Tập Lớn (Document Flow)

```
SECTION 0: FRONT MATTER (Trang bìa & phần thủ tục, đánh số trang La Mã i, ii...)
├── 1. Trang Bìa (Cover Page)
│   ├── Khung viền hoa văn mỹ thuật bao quanh trang (Page Border: thinThickThinMediumGap)
│   ├── Tên cơ quan chủ quản: HỌC VIỆN NGÂN HÀNG - KHOA SAU ĐẠI HỌC (16pt, In hoa, Đậm)
│   ├── BÀI TIỂU LUẬN / BÀI TẬP LỚN (18pt, In hoa, Đậm)
│   ├── MÔN HỌC: CƠ SỞ DỮ LIỆU NÂNG CAO (18pt, In hoa, Đậm)
│   ├── ĐỀ TÀI: [TÊN ĐỀ TÀI BÀI TẬP] (16pt, In hoa, Đậm)
│   ├── Bảng thông tin tác giả (Table không viền hoặc viền ẩn): GVHD, Sinh viên, Mã SV, Lớp
│   └── Địa danh & Năm: HÀ NỘI – 2026 (13pt, Đậm, Căn giữa)
├── 2. Nhận Xét Của Giảng Viên Hướng Dẫn (Page break)
│   ├── Tiêu đề: NHẬN XÉT CỦA GIẢNG VIÊN HƯỚNG DẪN (14pt, Đậm, Giữa)
│   ├── Dòng kẻ chấm (Dotted lines) để giảng viên ghi nhận xét và điểm số
│   └── Ký tên: Hà Nội, ngày … tháng … năm 2026 / Giảng viên hướng dẫn
├── 3. Lời Cam Đoan (Honor Pledge) (Page break)
├── 4. Lời Cảm Ơn (Acknowledgements) (Page break)
├── 5. Mục Lục (Table of Contents - Dynamic TOC \o "1-3") (Page break)
├── 6. Danh Mục Hình Vẽ Và Bảng Biểu (List of Exhibits) (Page break)
└── 7. Danh Mục Chữ Viết Tắt (Bảng 2 cột: Viết tắt & Diễn giải) (Page break)

SECTION 1: BODY MATTER (Nội dung học thuật, Header tiêu đề đề tài, Footer 'Trang {PAGE}')
├── 8. MỞ ĐẦU (1. Lý do chọn đề tài, 2. Mục đích & phạm vi, 3. Kết cấu đề tài)
├── 9. CHƯƠNG 1. CƠ SỞ LÝ THUYẾT VÀ TỔNG QUAN VẤN ĐỀ
├── 10. CHƯƠNG 2. NỘI DUNG NGHIÊN CỨU / PHÂN TÍCH THỰC TRẠNG / THIẾT KẾ HỆ THỐNG
├── 11. CHƯƠNG 3. VÍ DỤ THỰC TẾ, CÀI ĐẶT THỬ NGHIỆM HOẶC ĐỀ XUẤT GIẢI PHÁP
├── 12. KẾT LUẬN (Tổng kết kết quả đạt được & hướng phát triển)
└── 13. TÀI LIỆU THAM KHẢO (Đánh số [1], [2], chuẩn IEEE/Numeric, có thể tách VN/Anh)
```

---

## 4. Hệ Thống Kiểu Dáng Headings & Các Thành Phần Nội Dung

| Thành Phần | Cỡ chữ | Kiểu dáng / Màu sắc | Spacing (Before/After) | Canh lề |
| :--- | :---: | :--- | :---: | :--- |
| **Heading 1 (Chương)** | `15.0 pt` | **Bold**, ALL CAPS, Màu Navy (`#1F3864`) | Before $14\text{ pt}$, After $8\text{ pt}$ | Trái (`Left`), `keep_with_next` |
| **Heading 2 (Mục 1.1)** | `13.5 pt` | **Bold**, Slate Blue (`#2E5496`) | Before $10\text{ pt}$, After $6\text{ pt}$ | Trái (`Left`), `keep_with_next` |
| **Heading 3 (Mục 1.1.1)** | `13.0 pt` | **Bold**, Italic, Accent Blue (`#2E5496`) | Before $8\text{ pt}$, After $5\text{ pt}$ | Trái (`Left`), `keep_with_next` |
| **Thân bài (Normal)** | `13.0 pt` | Regular, Times New Roman, `#000000` | After $6\text{ pt}$, Line spacing $1.5$ | Căn đều (`Justified`), thụt $1.0\text{ cm}$ |
| **Tiêu đề Bảng (Table Caption)** | `12.0 pt` | **Italic / Bold**, Căn giữa | Before $6\text{ pt}$, After $4\text{ pt}$ | Đặt **PHÍA TRÊN** bảng |
| **Tiêu đề Hình (Figure Caption)** | `12.0 pt` | **Italic / Bold**, Căn giữa | Before $4\text{ pt}$, After $8\text{ pt}$ | Đặt **PHÍA DƯỚI** hình ảnh |

---

## 5. Quy Chuẩn Bảng Biểu (Academic Table Grid)

Trong `DoVanDat_CSDLNC.docx`, bảng biểu học thuật tuân theo thiết kế gọn gàng, rõ nét:
- **Header dòng đầu (Hàng tiêu đề):** Tô màu xanh lam nhạt (`#D9E2F3`), chữ đậm 12pt, căn giữa hoặc căn trái tùy cột dữ liệu.
- **Viền bảng (Borders):** Viền mảnh xám đồng nhất (`#888888`, size 2), phân tách ô rõ ràng.
- **Đệm ô (Padding):** Top/Bottom: $60\text{ dxa}$ ($3\text{ pt}$), Left/Right: $110\text{ dxa}$ ($5.5\text{ pt}$).
- **Thuộc tính sang trang:** Luôn áp dụng `<w:tblHeader/>` cho hàng 1 và `<w:cantSplit/>` cho mọi dòng.

---

## 6. Cách Sử Dụng Template Chuẩn Bằng Python Hoặc Node.js

### Cách 1: Nạp trực tiếp Template DOCX bằng `python-docx`
Bạn có thể mở tệp mẫu đã nhân bản để giữ 100% khung viền bìa, header/footer, styles có sẵn:

```python
import docx

# Mở template chuẩn bài tập lớn
doc = docx.Document("templates/DoVanDat_CSDLNC_template.docx")

# Hoặc khởi tạo document mới bằng hàm cấu hình profile
from word_docx_recipes import configure_academic_document, apply_assignment_headers_footers
configure_academic_document(doc, profile="hvnh-assignment")
```

### Cách 2: Dùng module `word_docx_recipes.py` với profile `hvnh-assignment`
Skill hỗ trợ trực tiếp profile `hvnh-assignment`:
```python
from word_docx_recipes import (
    configure_academic_document,
    add_assignment_cover_page,
    apply_assignment_headers_footers,
    add_chapter_heading,
    add_section_heading,
    add_body_paragraph
)
```
