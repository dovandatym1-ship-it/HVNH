---
name: academic-docx-writer
description: "Biên soạn luận văn / báo cáo tổng hợp học thuật trình độ sau đại học dưới dạng Word (.docx) chuẩn OpenXML: văn phong chống sáo ngữ AI, lập luận logic chính xác (Epistemic Precision), và kỹ nghệ định dạng Microsoft Word chuẩn HVNH (lề 3.5/3/3.5/2cm, giãn dòng 1.5, số trang giữa-phía-trên, Word Native Headings, Navigation Pane, Tables, Caption gắn số chương, Dynamic Numbering)."
---

# Academic Postgraduate DOCX Writer

Kỹ năng chuyên sâu về **viết học thuật tiếng Việt trình độ sau đại học**, biên tập khoa học, kiểm soát tính chính xác khái niệm (*Epistemic Precision*), lập luận logic (*Toulmin & Swales Models*) và **tự động hóa định dạng tài liệu Microsoft Word (.docx) chuẩn OpenXML**.

> Đây là skill dành riêng cho **báo cáo / luận văn / khóa luận dạng văn bản Word**. Nếu cần dựng **slide thuyết trình bảo vệ**, dùng skill song sinh `academic-slide-writer`.

---

## 1. Tuyên Ngôn Triết Lý & Nguyên Tắc Tối Thượng

> **Precision > Clarity > Logic > Evidence > Concision > Formality**

1. **Không tạo văn bản "trang trọng giả tạo":** Tuyệt đối không thay thế từ ngữ đơn giản bằng từ Hán-Việt phức tạp nếu không làm tăng độ chính xác của khái niệm (*sử dụng* $\rightarrow$ không cần đổi thành *vận dụng*; *làm rõ* $\rightarrow$ không cần đổi thành *minh định*).
2. **Không sáo ngữ & Không "AI smell":** Loại bỏ triệt để các cụm từ sáo rỗng (*"trong bối cảnh hiện nay", "có thể thấy rằng", "đóng vai trò vô cùng quan trọng", "góp phần không nhỏ", "ngày càng trở nên cấp thiết", "mang tính đột phá"...*).
3. **Độ chính xác nhận thức (Epistemic Precision):**
   * **Tương quan $\neq$ Nhân quả:** Không chuyển từ *"có tương quan với"* thành *"gây ra / dẫn đến / tác động đến"* nếu thiết kế nghiên cứu không đủ để xác lập quan hệ nhân quả.
   * **Mức độ khẳng định phải tương xứng với bằng chứng:** Phân biệt rõ *cho thấy, chỉ ra, gợi ý, hàm ý, có thể lý giải, chưa đủ cơ sở để kết luận* vs *chứng minh, cho phép kết luận*.
4. **Cấu trúc Lập luận Toulmin chuẩn mực:**
   $$\text{Luận điểm (Claim)} \longleftarrow \text{Bằng chứng (Data)} + \text{Luận cứ (Warrant)} + \text{Cơ sở (Backing)} + \text{Mức độ (Qualifier)}$$

Chi tiết đầy đủ về Toulmin Model, Swales CARS Model, thang đo mức độ khẳng định, bộ lọc chống sáo ngữ và quy tắc trích dẫn theo loại tài liệu — xem [references/academic_writing_mastery.md](references/academic_writing_mastery.md).

---

## 2. Quy Chuẩn Định Dạng Microsoft Word (.docx) Bậc Sau Đại Học

### 2.1. Chọn Đúng Profile Chuẩn Trước Khi Soạn Thảo
> **Phạm vi chuẩn:** ND 30/2020/NĐ-CP chỉ áp cho **văn bản hành chính**. Luận văn Thạc sĩ HVNH
> tuân theo "Quy định về trình bày luận văn" — Khoa Sau đại học HVNH (`hvnh_thesis_standard.md`).

| Profile | Lề (T/D/TR/P) | Giãn dòng | Trích dẫn | Số trang | Dùng cho |
| :--- | :---: | :---: | :--- | :--- | :--- |
| **`hvnh-thesis`** ⭐ | 3.5 / 3.0 / 3.5 / 2.0 cm | **1.5** | Số `[15, tr.314]` | Giữa-phía-trên, đếm từ MỞ ĐẦU | **Luận văn Thạc sĩ HVNH** |
| **`hvnh-assignment`** 📘 | 3.0 / 2.54 / 2.54 / 2.54 cm | **1.5** | Số `[15]` | Chân trang `Trang {PAGE}`, bìa khung | **Bài tập lớn / Tiểu luận môn học HVNH** |
| `hvnh-khoaluan` | 3.5 / 3.0 / 3.5 / 2.0 cm | 1.3–1.5 | theo hướng dẫn Khoa | Giữa-phía-trên | Khóa luận / Chuyên đề TN |
| `nd30-report` | 2.5 / 2.0 / 3.0 / 2.0 cm | ≤ 1.5 | tùy chọn | Footer | Báo cáo hành chính ND 30 |

```python
from word_docx_recipes import configure_academic_document, apply_assignment_headers_footers, add_assignment_cover_page
# Dành cho Luận văn Thạc sĩ:
configure_academic_document(doc, profile="hvnh-thesis")
apply_page_numbers_top_center(doc, start_value=1)

# Dành cho Bài tập lớn / Tiểu luận môn học (chuẩn DoVanDat_CSDLNC.docx):
configure_academic_document(doc, profile="hvnh-assignment")
add_assignment_cover_page(doc, ten_de_tai="...", mon_hoc="...", giang_vien_hd="...", sinh_vien_th="...")
apply_assignment_headers_footers(doc, header_title="Tên đề tài bài tập", start_value=1)
```

* **Khổ giấy:** A4 ($210 \times 297\text{ mm}$).
* **Font chữ đồng nhất:** **Times New Roman**, bảng mã Unicode.

### 2.2. Quy Chuẩn Đoạn Văn (Body Text) & Heading Phân Cấp
| Thành Phần | Cỡ Chữ | Kiểu Dáng / Màu Sắc | Giãn Dòng & Đoạn | Canh Lề / Thụt Đầu Dòng |
| :--- | :---: | :--- | :--- | :--- |
| **Body Text** | `13.0 pt` | Regular, Slate 900 (`#0F172A`) | Line $1.35$ • After $6\text{ pt}$ | **Justified** • First-line indent $1.27\text{ cm}$ |
| **Heading 1 (Chương)** | `15.0 - 15.5 pt` | **Bold**, Navy (`#0A2540`), ALL CAPS | Before $16\text{ pt}$ • After $8\text{ pt}$ | **Left** • First-line indent $0\text{ cm}$ |
| **Heading 2 (Mục 1.1)** | `13.5 pt` | **Bold**, Slate Blue (`#1F4D78`) | Before $14\text{ pt}$ • After $6\text{ pt}$ | **Left** • First-line indent $0\text{ cm}$ |
| **Heading 3 (Mục 1.1.1)** | `13.0 pt` | **Bold**, Cyan Blue (`#2E74B5`) | Before $10\text{ pt}$ • After $4\text{ pt}$ | **Left** • First-line indent $0\text{ cm}$ |
| **Caption (Bảng/Hình)** | `11.5 pt` | **Bold / Italic**, Navy (`#0A2540`) | Before $10\text{ pt}$ • After $4\text{ pt}$ | **Center / Left** • No indent |

> [!CRITICAL]
> **Giãn dòng theo profile:** bảng trên ghi giá trị legacy 1.35 của `nd30-report`; với
> `hvnh-thesis` / `hvnh-khoaluan`, giãn dòng thân bài là **1.5** (bắt buộc theo quy định Khoa Sau đại học).
>
> **Quy Tắc Chống Giãn Chữ (Anti-Justification Stretch):**
> 1. Chỉ áp dụng `Justified` cho các đoạn văn phân tích dài (Body text nhiều dòng).
> 2. Các **Tiêu đề Callout, Tiêu đề Bảng, Danh sách gạch đầu dòng ngắn, và Công thức tính toán** BẮT BUỘC phải đặt căn **TRÁI (Left Align)** để tránh bị Word kéo dãn khoảng cách giữa các từ/ký tự (`×`, `=`, `$`).
> 3. Mỗi Chương (`CHƯƠNG 1` đến `CHƯƠNG 7` và `TÀI LIỆU THAM KHẢO`) phải luôn bắt đầu bằng một **Page Break** (`doc.add_page_break()`) để tránh ngắt trang dở dang.
>
> **Quy Tắc Cấu Trúc Luận Văn HVNH:** caption gắn số chương (`Hình 3.4`, `Bảng 2.1`);
> bảng caption TRÊN — hình caption DƯỚI; tiểu mục tối đa 4 cấp và cấm mồ côi (phải có ≥2 tiểu mục);
> cuối mỗi chương có Tóm tắt chương; trích dài >4 dòng lùi lề trái 2cm bỏ ngoặc kép;
> TLTK đánh số `[n]` tách Tiếng Việt/Tiếng Anh, hanging indent 1cm; mục lục động 3 cấp.

Chi tiết kỹ nghệ OpenXML đầy đủ (cấu trúc `w:sectPr`, field codes số trang, `w:tblHeader`/`w:cantSplit`, cell margins, zebra striping, quy tắc cấu trúc luận văn §2.7) — xem [references/word_docx_engineering.md](references/word_docx_engineering.md).

Toàn văn "Quy định về trình bày luận văn" gốc (Khoa Sau đại học HVNH) và checklist gate 10 điểm trước khi nộp — xem [references/hvnh_thesis_standard.md](references/hvnh_thesis_standard.md).

---

## 3. Hệ Thống Tài Liệu Tham Khảo & Code Library Kèm Theo

| Tài Liệu / Module | Đường Dẫn Tệp Tin | Nội Dung & Ý Nghĩa Kỹ Thuật |
| :--- | :--- | :--- |
| **Chuẩn Luận Văn HVNH (gốc)** | [references/hvnh_thesis_standard.md](references/hvnh_thesis_standard.md) | Quy định trình bày luận văn Khoa Sau đại học HVNH: lề, giãn dòng 1.5, số trang giữa-phía-trên đếm từ MỞ ĐẦU, tiểu mục ≤4 cấp cấm mồ côi, caption gắn chương, trích dẫn `[n]`, TLTK tách ngôn ngữ, checklist gate 10 điểm. **Ưu tiên cao nhất cho luận văn.** |
| **Chuẩn Bài Tập Lớn / Tiểu Luận** ⭐ | [references/hvnh_assignment_standard.md](references/hvnh_assignment_standard.md) | Quy chuẩn định dạng Bài tập lớn / Tiểu luận môn học chuẩn thực tế HVNH (DoVanDat_CSDLNC): lề Trái 3cm gáy / 2.54cm, bìa hoa văn khung viền, trang nhận xét GVHD, Header tên đề tài, Footer 'Trang {PAGE}'. |
| **Template Mẫu Bài Tập Lớn DOCX** | [templates/DoVanDat_CSDLNC_template.docx](templates/DoVanDat_CSDLNC_template.docx) | Tệp tin DOCX mẫu sạch chuẩn bài tập lớn môn học HVNH để clone trực tiếp khi tạo bài mới. |
| **Cẩm Nang Viết Học Thuật** | [references/academic_writing_mastery.md](references/academic_writing_mastery.md) | Epistemic Precision, Toulmin Model, Swales CARS Model, Bộ lọc chống sáo ngữ AI, Trích dẫn theo loại tài liệu (`[n]` HVNH / APA 7th). |
| **Kỹ Nghệ Định Dạng Word** | [references/word_docx_engineering.md](references/word_docx_engineering.md) | Cấu trúc OpenXML, Word Navigation Pane, Dynamic Page Numbers giữa-phía-trên, Bảng biểu `w:tblHeader` / `w:cantSplit`, Anti-Justification, Quy tắc cấu trúc luận văn §2.7. |
| **Thư Viện Code Python-docx** | [references/word_docx_recipes.py](references/word_docx_recipes.py) | Module v3 profile-based: `configure_academic_document(doc, profile)`, `apply_page_numbers_top_center`, `apply_assignment_headers_footers`, `add_assignment_cover_page`, `add_instructor_review_page`, `add_title_page`, `add_cam_doan_page`, `add_toc_field`, `add_abbreviation_table`, `add_exhibits_list`, caption gắn chương (`chapter_label`), `validate_document(doc)` (QA gate). |

## 4. Quy Trình Sử Dụng Đề Xuất

1. Xác định loại tài liệu (luận văn thạc sĩ / khóa luận / báo cáo chuyên đề) → chọn đúng `profile` ở mục 2.1.
2. Soạn nội dung theo chuẩn văn phong Epistemic Precision (mục 1, chi tiết ở `academic_writing_mastery.md`).
3. Dựng khung tài liệu bằng `word_docx_recipes.py`: gọi `configure_academic_document()` trước tiên, dựng bìa/cam đoan/mục lục, rồi `apply_page_numbers_top_center()` ngay trước MỞ ĐẦU.
4. Soạn từng chương với `add_chapter_heading`, `add_section_heading`, `add_body_paragraph`, `add_figure_with_caption`, `style_academic_table`... đảm bảo mỗi chương có Tóm tắt chương.
5. Dựng danh mục TLTK bằng `add_reference_section_hvnh` (tách Tiếng Việt/Tiếng Anh) và rà lại trích dẫn số `[n]` khớp 100%.
6. Gọi `validate_document(doc)` để tự động dò lề/giãn dòng/số trang/heading theo đúng profile — sửa ngay các vấn đề được báo trước khi qua bước rà tay.
7. Chạy checklist gate 10 điểm trong `hvnh_thesis_standard.md` §7 trước khi bàn giao (bao gồm các mục `validate_document()` không kiểm được: tiểu mục mồ côi, caption gắn chương, khớp trích dẫn TLTK).
