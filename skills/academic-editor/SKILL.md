---
name: academic-editor
description: "Rà soát văn phong một bản thảo học thuật ĐÃ VIẾT SẴN (.docx / .md / .txt): phát hiện sáo ngữ / 'AI smell', khẳng định tuyệt đối hóa thiếu cơ sở (overclaim), và nguy cơ diễn đạt tương quan thành nhân quả. Xuất báo cáo từng điểm kèm ngữ cảnh, lý do và gợi ý sửa — dùng trước khi nộp luận văn/báo cáo/bài báo."
---

# Academic Editor

Công cụ **rà soát** một bản thảo học thuật đã có sẵn nội dung — khác với `academic-docx-writer` và `academic-slide-writer` (dùng để **dựng** tài liệu/slide mới từ đầu). Quy trình khuyến nghị: soạn bằng hai skill kia, rà lại bằng skill này trước khi nộp hoặc bảo vệ.

Dựa trên cùng bộ chuẩn Epistemic Precision với `academic-docx-writer`/`academic-slide-writer` — xem đầy đủ tại [references/academic_writing_mastery.md](references/academic_writing_mastery.md).

---

## 1. Ba nhóm lỗi được phát hiện

1. **Sáo ngữ / "AI smell"** — các cụm mở đầu/diễn đạt sáo rỗng theo bảng tra cứu §3.1 của `academic_writing_mastery.md` (ví dụ: "trong bối cảnh hiện nay", "có thể thấy rằng", "mang tính đột phá"...). Mỗi phát hiện kèm gợi ý diễn đạt lại cụ thể.
2. **Khẳng định tuyệt đối hóa (Overclaim)** — các cụm như "hoàn toàn đúng", "chắc chắn 100%", "vô song", "không thể bàn cãi"... vượt quá mức độ khẳng định mà bằng chứng thực nghiệm thông thường cho phép (xem thang đo Epistemic Modality §1.1).
3. **Nguy cơ diễn đạt Tương quan → Nhân quả** — câu vừa nêu "tương quan"/"có mối liên hệ" vừa dùng động từ nhân quả ("gây ra", "dẫn đến", "khiến", "tạo ra"...) trong cùng câu. Chỉ hợp lệ khi thiết kế nghiên cứu là RCT/IV/DID/RDD; nếu không, gợi ý đổi sang diễn đạt tương quan thuần túy.

## 2. Cách dùng

```bash
# In báo cáo ra console
python3 references/style_audit.py duong_dan/ban_thao.docx

# Xuất thêm báo cáo Markdown để lưu lại / gửi cho người hướng dẫn
python3 references/style_audit.py duong_dan/ban_thao.docx --out bao_cao_ra_soat.md
```

Hỗ trợ đọc trực tiếp `.docx` (qua `python-docx`), `.md` và `.txt` (đoạn văn phân tách bởi dòng trống). Có thể gọi từ Python:

```python
from style_audit import audit_file, print_report
findings, total_paragraphs = audit_file("ban_thao.docx")
print_report(findings, total_paragraphs)
```

## 3. Giới hạn quan trọng — đọc trước khi dùng

Đây là bộ lọc dựa trên từ khóa/regex, **không phải mô hình hiểu ngữ nghĩa**:
* Có thể **bỏ sót** sáo ngữ diễn đạt theo cách khác không có trong bảng tra cứu.
* Có thể **báo nhầm** (false positive) khi câu văn hợp lệ vô tình chứa cụm từ trong danh sách (ví dụ câu trích dẫn nguyên văn nguồn khác).
* Không đánh giá được chất lượng lập luận tổng thể, chỉ bắt các mẫu câu cụ thể.

**Luôn đọc lại từng điểm được báo trước khi sửa — không tự động thay thế hàng loạt.** Đã kiểm thử với văn bản có lỗi (bắt đúng cả 3 nhóm) và văn bản chuẩn mực (không có false positive) — xem để hiểu bộ lọc hoạt động thế nào trước khi tin tưởng hoàn toàn kết quả.

## 4. Hệ thống tài liệu tham khảo kèm theo

| Tài liệu / Module | Đường dẫn | Nội dung |
| :--- | :--- | :--- |
| **Cẩm nang viết học thuật** | [references/academic_writing_mastery.md](references/academic_writing_mastery.md) | Nguồn gốc đầy đủ của 3 bộ quy tắc trên: thang đo Epistemic Modality, phân biệt tương quan/nhân quả, bảng sáo ngữ đầy đủ. |
| **Công cụ rà soát** | [references/style_audit.py](references/style_audit.py) | `audit_file`, `audit_text`, `audit_paragraph`, `print_report`, `write_markdown_report`, CLI `main()`. |
