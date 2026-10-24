# Chuẩn Trình Bày Luận Văn Thạc Sĩ Học Viện Ngân Hàng (HVNH Thesis Standard)

> **Nguồn:** "Quy định về trình bày luận văn" — Khoa Sau đại học, Học viện Ngân hàng
> (tải trực tiếp từ hvnh.edu.vn). Tài liệu này là **chuẩn gốc chi phối luận văn thạc sĩ HVNH**,
> có mức ưu tiên CAO HƠN Nghị định 30/2020/NĐ-CP cho loại tài liệu này.
>
> ⚠️ ND 30/2020/NĐ-CP là chuẩn **văn bản hành chính nhà nước**, KHÔNG phải chuẩn luận văn.
> Chỉ dùng ND 30 khi soạn báo cáo hành chính / công văn, không áp máy móc vào luận văn.

---

## 1. Thông Số Định Dạng Bắt Buộc (Luận văn Thạc sĩ)

| Hạng mục | Quy định gốc | Ghi chú kỹ thuật |
| :--- | :--- | :--- |
| Khổ giấy | A4 ($210 \times 297$ mm) | |
| Font | Times New Roman cỡ **13 hoặc 14** | Mật độ chữ bình thường, không nén/kéo dãn ký tự |
| Giãn dòng | **1.5 lines** (bắt buộc) | Không dùng 1.35 hay 1.3 cho luận văn TS |
| Lề trái | **3.5 cm** | Đóng gáy |
| Lề phải | **2.0 cm** | |
| Lề trên | **3.5 cm** | |
| Lề dưới | **3.0 cm** | |
| Số trang | Đánh ở **GIỮA, PHÍA TRÊN** đầu mỗi trang; **bắt đầu đếm từ trang MỞ ĐẦU** (= 1); các trang trước đó (bìa, cam đoan, mục lục...) không hiển thị số | Cần section break + `pgNumType w:start="1"` |

### Bảng đối chiếu với profile khác trong skill

| Profile | Lề (T/D/TR/P) | Giãn dòng | Trích dẫn | Dùng cho |
| :--- | :--- | :--- | :--- | :--- |
| `hvnh-thesis` | 3.5 / 3.0 / 3.5 / 2.0 cm | 1.5 | Số `[15, tr.314]` | **Luận văn Thạc sĩ HVNH** (chuẩn này) |
| `hvnh-khoaluan` | như trên | 1.3–1.5 (mặc định 1.5) | theo hướng dẫn Khoa | Khóa luận / Chuyên đề tốt nghiệp |
| `nd30-report` | 2.5 / 2.0 / 3.0 / 2.0 cm | ≥ dòng đơn, ≤ 1.5 | tùy | Báo cáo hành chính / công văn (ND 30) |

---

## 2. Trình Tự Trình Bày Toàn Văn

```
Bìa ngoài → Phụ bìa → Bìa trong → Cam đoan → Mục lục → Danh mục chữ viết tắt
→ Danh mục bảng biểu → [Danh mục hình vẽ] → MỞ ĐẦU (bắt đầu đánh số trang)
→ Chương 1 … Chương N → Kết luận → Danh mục công trình KH của tác giả đã công bố
→ Tài liệu tham khảo → Phụ lục
```

Quy tắc đi kèm:
- **Cuối mỗi chương phải có phần Tóm tắt chương (kết luận chương)** — không nhất thiết sang trang riêng.
- Tên đề tài, tên chương, tên mục lớn: viết **IN HOA**, không viết tắt.
- Cuối tên chương/mục **không có dấu chấm**.
- Không để 1 từ đơn lẻ trong 1 dòng.
- Xuống dòng lùi đều (1 tab ≈ 1.27 cm); riêng các mục không cần lùi.
- **Mục lục đánh đến 3 số** (ví dụ 2.1.3).
- Luận án đóng bìa cứng in chữ nhũ đủ dấu tiếng Việt (mẫu 09); trang phụ bìa theo mẫu 10.

---

## 3. Tiểu Mục (Mục Con)

- Đánh số thành nhóm chữ số, **nhiều nhất 4 chữ số**: `3.1.2.1` = tiểu mục 1, nhóm tiểu mục 2, mục 1, chương 3.
- **Cấm tiểu mục mồ côi:** tại mỗi nhóm phải có ÍT NHẤT HAI tiểu mục — không được tồn tại `2.1.1` mà không có `2.1.2`.

## 4. Bảng Biểu, Hình Vẽ, Phương Trình

- Đánh số **gắn với số chương**: `Hình 3.4` = hình thứ 4 của Chương 3; tương tự `Bảng 2.1`.
- Đầu đề bảng ghi **phía trên** bảng; đầu đề hình ghi **phía dưới** hình.
- Mọi bảng/hình lấy từ nguồn khác phải trích nguồn đầy đủ ("Nguồn: ...") và nguồn phải có mặt trong danh mục TLTK.
- Bảng ngắn đặt liền kề lần đề cập đầu tiên; bảng dài có thể để trang riêng nhưng vẫn phải ngay sau lần đề cập.
- Phương trình: đánh số trong ngoặc đơn, **căn lề phải** — `(5.1)`; nhóm phương trình `(5.1.1), (5.1.2)...`.
- Ký hiệu xuất hiện lần đầu phải được giải thích kèm đơn vị tính ngay tại phương trình.

## 5. Viết Tắt

- Chỉ viết tắt từ/cụm từ dùng nhiều lần; không viết tắt mệnh đề hoặc cụm ít xuất hiện.
- Lần đầu xuất hiện: ghi đầy đủ kèm chữ viết tắt trong ngoặc đơn.
- Có nhiều chữ viết tắt → lập bảng DANH MỤC CHỮ VIẾT TẮT xếp A→Z đặt ở đầu luận văn.

## 6. Trích Dẫn & Tài Liệu Tham Khảo

### 6.1. Trích dẫn trong văn bản — THEO SỐ THỨ TỰ
- Trích dẫn đánh dấu bằng **số thứ tự của tài liệu trong danh mục TLTK, đặt trong ngoặc vuông**: `[15]`.
- Cần số trang thì thêm: `[15, tr.314-315]`.
- Nhiều nguồn: mỗi số một ngoặc vuông, thứ tự tăng dần: `[19], [25], [41], [42]`.

### 6.2. Trích dẫn dài
- Ngắn hơn **2 câu hoặc 4 dòng**: dùng ngoặc kép ngay trong đoạn.
- Dài hơn: tách thành **đoạn riêng**, lề trái **lùi vào thêm 2 cm**, không dùng ngoặc kép.

### 6.3. Xếp danh mục TLTK
- **Tách riêng theo từng ngôn ngữ** (Tiếng Việt / Tiếng Anh / Pháp...); tài liệu nước ngoài giữ nguyên văn, không phiên âm.
- Xếp ABC: tác giả nước ngoài theo **họ**; tác giả Việt Nam theo **tên** (giữ trật tự tên thông thường, không đảo họ lên trước); không có tác giả → xếp theo tên cơ quan (Tổng cục Thống kê → vần T).
- Sách / luận án / báo cáo: `Tác giả (Năm), Tên sách (in nghiêng), Nhà xuất bản, Nơi xuất bản.`
- Bài báo tạp chí: `Tác giả (Năm), "Tên bài" (ngoặc kép, không nghiêng), Tên tạp chí (in nghiêng), Tập(Số), tr.trang.`
- Nếu entry dài quá một dòng: **dòng thứ hai lùi vào 1 cm** (hanging indent 1 cm).

## 7. Kiểm Tra Tuân Thủ (Checklist Gate)

Trước khi nộp, kiểm tra từng mục:
1. Lề đúng 3.5/3.0/3.5/2.0 cm — mở Page Setup đối chiếu.
2. Giãn dòng toàn thân bài = 1.5.
3. Số trang giữa-phía-trên, trang Mở đầu mang số 1, các trang trước đó trắng số.
4. Mọi caption gắn số chương (`Hình 3.4`, `Bảng 2.1`), bảng trên/dưới đúng vị trí, có Nguồn.
5. Không có tiểu mục mồ côi; tối đa 4 cấp.
6. Mỗi chương có Tóm tắt chương.
7. Trích dẫn dạng `[n]` khớp 100% với danh mục TLTK đánh số; TLTK tách ngôn ngữ, hanging indent 1 cm.
8. Trích dài > 4 dòng đã lùi 2 cm, bỏ ngoặc kép.
9. Mục lục đến 3 cấp; danh mục viết tắt xếp A→Z.
10. Cuối tên chương/mục không dấu chấm; tiêu đề lớn IN HOA.
