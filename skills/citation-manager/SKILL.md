---
name: citation-manager
description: "Quản lý danh mục Tài liệu tham khảo (TLTK) chuẩn HVNH bằng file YAML có cấu trúc: tự động đánh số [n] đúng thứ tự (tách khối Tiếng Việt/Tiếng Anh, xếp ABC theo tên/họ), xuất danh mục TLTK đúng format, và đối chiếu trích dẫn [n] trong bản thảo (.docx/.md/.txt) với danh mục để phát hiện trích dẫn thiếu nguồn hoặc nguồn mồ côi chưa được trích."
---

# Citation Manager

Công cụ quản lý **danh mục nguồn có cấu trúc** cho luận văn/báo cáo chuẩn HVNH, thay vì gõ tay số thứ tự `[n]` và tự xếp ABC — dễ sai khi danh mục có vài chục nguồn và chỉnh sửa nhiều lần trong quá trình viết.

Dùng **cùng với** `academic-docx-writer`: sau khi danh mục đã đánh số ổn định ở đây, dùng `hvnh_book()` / `hvnh_journal_article()` / `add_reference_section_hvnh()` trong `word_docx_recipes.py` của skill đó để chèn danh mục thật vào file `.docx` — `citation_manager.py` không tự sinh file `.docx`, chỉ quản lý dữ liệu nguồn và logic đánh số/đối chiếu.

Chuẩn trích dẫn tham chiếu đầy đủ tại [references/hvnh_thesis_standard.md](references/hvnh_thesis_standard.md) §6.

---

## 1. Quy trình sử dụng

1. Khai báo từng nguồn vào file YAML theo mẫu [references/sources_template.yaml](references/sources_template.yaml) — mỗi nguồn có `id` (định danh nội bộ tự đặt, không phải số `[n]`), `type` (`book`/`article`), `language` (`vi`/`en`), và các trường bắt buộc tương ứng.
2. Xem danh mục đã đánh số đúng chuẩn HVNH:
   ```bash
   python3 references/citation_manager.py list nguon_cua_toi.yaml
   ```
3. Trong lúc viết, chèn `[n]` vào bản thảo theo đúng số mà lệnh `list` vừa in ra.
4. Trước khi nộp, đối chiếu toàn bộ bản thảo với danh mục:
   ```bash
   python3 references/citation_manager.py check nguon_cua_toi.yaml ban_thao.docx
   ```
   Lệnh này báo hai loại vấn đề:
   * **Thiếu trong danh mục**: `[n]` xuất hiện trong bản thảo nhưng không có nguồn nào được đánh số `n`.
   * **Mồ côi trong danh mục**: nguồn có trong danh mục nhưng chưa từng được trích `[n]` trong bản thảo lần nào.
5. Khi danh mục đã khớp 100% (exit code 0), dùng `add_reference_section_hvnh()` bên `academic-docx-writer` để chèn danh mục thật vào file `.docx`.

## 2. Quy tắc đánh số (đúng chuẩn HVNH, không tự chế)

* Tách hai khối theo `language`: **Tiếng Việt xếp trước, Tiếng Anh xếp sau**.
* Trong mỗi khối, xếp ABC: **nguồn Tiếng Việt theo TÊN** (giữ trật tự tên thông thường, không đảo họ lên trước — ví dụ "Nguyễn Văn A" xếp theo "A"); **nguồn nước ngoài theo HỌ** (nên ghi `author` dạng `"Họ, Tên viết tắt"` ví dụ `"Chen, T."` để xếp đúng — nếu ghi không có dấu phẩy, chương trình lấy từ đầu tiên làm họ, có thể sai với tên nhiều từ).
* Đánh số **liên tục xuyên hai khối** — khối Tiếng Anh không reset về 1, mà tiếp tục từ số cuối của khối Tiếng Việt. Số này chính là số dùng cho trích dẫn `[n]` trong thân bài.

## 3. Giới hạn quan trọng — đọc trước khi dùng

* Việc đối chiếu chỉ dựa trên **số `[n]`** xuất hiện trong text — không kiểm tra được nội dung trích dẫn có đúng ngữ nghĩa với nguồn hay không (ví dụ trích `[3]` nhưng nội dung câu văn thực ra phù hợp với `[5]` hơn — công cụ không phát hiện được loại lỗi này).
* Xếp ABC theo HỌ cho nguồn nước ngoài phụ thuộc vào cách bạn ghi `author` — sai định dạng (không có dấu phẩy, tên ghép nhiều từ) có thể khiến thứ tự sai; luôn xem lại kết quả `list` trước khi tin tưởng.
* File YAML được validate nghiêm ngặt (thiếu trường bắt buộc, trùng `id` đều bị chặn với thông báo lỗi rõ ràng) — nhưng không kiểm tra được lỗi chính tả trong tên tác giả/tên sách.

Đã kiểm thử đầy đủ: đánh số + sắp xếp đúng thứ tự HVNH, đối chiếu bắt đúng cả trích dẫn thiếu nguồn lẫn nguồn mồ côi, báo lỗi rõ ràng khi YAML thiếu trường hoặc trùng `id`, và không crash khi file không tồn tại.

## 4. Hệ thống tài liệu tham khảo kèm theo

| Tài liệu / Module | Đường dẫn | Nội dung |
| :--- | :--- | :--- |
| **Chuẩn trích dẫn & TLTK HVNH** | [references/hvnh_thesis_standard.md](references/hvnh_thesis_standard.md) | Quy tắc gốc §6: trích dẫn số `[n]`, trích dẫn dài, xếp danh mục TLTK theo ngôn ngữ/ABC, hanging indent. |
| **Mẫu khai báo nguồn** | [references/sources_template.yaml](references/sources_template.yaml) | 4 nguồn mẫu (2 Việt, 2 Anh, cả book lẫn article) kèm chú thích từng trường. |
| **Công cụ quản lý** | [references/citation_manager.py](references/citation_manager.py) | `load_sources`, `sort_sources`, `assign_numbers`, `render_reference_list`, `extract_cited_numbers`, `cross_check`, CLI `list`/`check`. |
