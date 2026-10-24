# 🗂️ Phân Loại Dữ Liệu & Kỹ Thuật Đặc Trưng (Feature Engineering)

> **Nguồn:** Giáo trình "Mô hình học máy" — Học viện Ngân hàng (model.pdf, Part 1)
> **Câu hỏi mở đầu mọi dự án:** không phải *"dùng mô hình gì?"* mà là *"dữ liệu của tôi thuộc loại nào?"*

---

## 1. 📊 Ba loại dữ liệu theo cấu trúc

### 1.1. Dữ liệu có cấu trúc (Structured Data)
- **Định nghĩa:** tổ chức theo lược đồ định sẵn — mỗi hàng = một quan sát, mỗi cột = một biến có kiểu xác định.
- **Đặc điểm:** schema rõ ràng; kiểu cố định (số, ngày, chuỗi); truy vấn SQL được; dễ tổng hợp/lọc.
- **Lưu trữ:** CSDL quan hệ (MySQL, PostgreSQL, Oracle), kho dữ liệu, bảng tính, CSV.
- **Ví dụ ngân hàng:** bảng giao dịch, hồ sơ nhân sự, báo cáo tài chính theo mẫu.

Ví dụ bảng dữ liệu tín dụng:

| Mã KH | Tuổi | Thu nhập (tr/tháng) | Số năm làm việc | Dư nợ (tr) | Vỡ nợ |
| :--- | :---: | :---: | :---: | :---: | :---: |
| KH001 | 34 | 18.5 | 8 | 220 | 0 |
| KH002 | 27 | 12.0 | 3 | 150 | 1 |
| KH003 | 45 | 31.2 | 20 | 480 | 0 |

→ Mỗi hàng là một quan sát; mỗi cột là một **đặc trưng (feature)**; cột cuối "Vỡ nợ" là **nhãn (label)** — thứ cần dự đoán.

### 1.2. Dữ liệu phi cấu trúc (Unstructured Data)
- **Định nghĩa:** không có lược đồ — không hàng, không cột, không kiểu cố định.
- **Ví dụ:** văn bản tự do (email khiếu nại, hợp đồng), hình ảnh, ghi âm tổng đài, video, PDF quét.
- **Vì sao khó:** không truy vấn bằng SQL; ý nghĩa nằm trong ngữ cảnh; khối lượng rất lớn.
- **Vì sao giá trị cao:** lý do thật khiến khách hàng rời bỏ ngân hàng nằm trong **email khiếu nại**, không nằm trong bảng giao dịch.
- **Cách xử lý hiện nay:** mô hình học sâu chuyển thành **vector nhúng (embedding)** → sau đó mọi công cụ dữ liệu có cấu trúc dùng lại được.
- 📈 **Tỷ trọng:** ~80–90% dữ liệu của tổ chức là phi cấu trúc (ước tính IDC/Gartner — đọc thận trọng, là ước tính ngành không phải phép đo chính xác).

### 1.3. Dữ liệu bán cấu trúc (Semi-structured)
- **Định nghĩa:** không có lược đồ bảng cứng nhưng có **thẻ đánh dấu / khoá–giá trị**.
- **Ví dụ:** JSON, XML, log hệ thống, email (trường Người gửi/Chủ đề/Ngày + thân tự do), API, cảm biến IoT.
- Là dạng **phổ biến nhất** khi lấy dữ liệu từ Internet/hệ thống bên thứ ba. Bước đầu tiên hầu hết dự án: **làm phẳng thành bảng**.
- Ranh giới ba loại không tuyệt đối: PDF vừa chứa bảng số liệu vừa chứa đoạn thuyết minh.

### 1.4. Bảng so sánh ba loại

| Tiêu chí | Có cấu trúc | Bán cấu trúc | Phi cấu trúc |
| :--- | :--- | :--- | :--- |
| Tổ chức | Bảng, hàng & cột | Thẻ, khoá–giá trị | Không lược đồ |
| Ví dụ | CSV, bảng SQL | JSON, XML, log | Ảnh, video, văn bản |
| Truy vấn | SQL | Phân tích cú pháp | Mô hình học sâu |
| Nơi lưu | Kho dữ liệu | Hồ dữ liệu, NoSQL | Hồ dữ liệu, CSDL vector |
| Tỷ trọng | Nhỏ | Trung bình | Rất lớn |
| Độ khó khai thác | Thấp | Trung bình | Cao |

> 💡 Càng sang phải càng giàu thông tin nhưng càng khó khai thác — **học máy hiện đại là công cụ thu hẹp khoảng cách đó**.

---

## 2. 🏷️ Hai loại dữ liệu theo mục đích học máy

| Tiêu chí | Dữ liệu CÓ nhãn (Labeled) | Dữ liệu KHÔNG nhãn (Unlabeled) |
| :--- | :--- | :--- |
| Cấu trúc | Features + Labels (đầu ra mong muốn) | Chỉ có Features |
| Thuộc bài toán | Học có giám sát (Supervised) | Học không giám sát (Unsupervised) |
| Ví dụ ngân hàng | Khách hàng với (tuổi, thu nhập, số dư) + nhãn tín dụng tốt/xấu | Giao dịch (amount, date, location) không dán nhãn gian lận |
| Ứng dụng | Dự đoán rủi ro tín dụng, phân loại khách hàng | Phân cụm khách hàng, phát hiện bất thường |
| Thách thức | Gắn nhãn tốn thời gian & chi phí | Khó đánh giá kết quả (không có đáp án so sánh) |

### Bài toán không giám sát điển hình
1. **Phân nhóm khách hàng** (Customer Segmentation): chia cụm hành vi tương đồng để cá nhân hóa tiếp thị.
2. **Phát hiện gian lận** (Anomaly Detection): tìm giao dịch đáng ngờ trong hàng triệu giao dịch, không có nhãn trước đó.
3. **Phân loại chủ đề tin tức** (Topic Modeling): mô hình tự tìm chủ đề tiềm ẩn.
4. **Nhân cụm sản phẩm** (Product Clustering): nhóm sản phẩm tương đồng để tối ưu kệ hàng/gợi ý mua.

---

## 3. 🔧 Từ dữ liệu thô đến đặc trưng (Feature Engineering)

Mô hình ML **không "đọc" dữ liệu thô** — chỉ làm việc với con số. Bước biến đổi gọi là **kỹ thuật đặc trưng**:

| Loại dữ liệu thô | Biến đổi thành |
| :--- | :--- |
| Biến phân loại (giới tính, tỉnh thành) | Biến mã hoá 0/1 |
| Ngày tháng | Thứ trong tuần, tháng, số ngày kể từ mốc |
| Văn bản | Đếm từ, hoặc vector nhúng (embedding) |
| Ảnh | Ma trận điểm ảnh, hoặc vector đặc trưng từ mạng nơ-ron |

> 💡 **Kinh nghiệm thực chiến:** chất lượng đặc trưng quan trọng hơn độ phức tạp mô hình — *mô hình đơn giản + đặc trưng tốt thường thắng mô hình phức tạp + đặc trưng kém*.

---

## 4. 🧹 Chất lượng dữ liệu — 3 hiểm họa

1. **Thiếu dữ liệu:** ô trống thường KHÔNG ngẫu nhiên (vd: người thu nhập cao hay bỏ trống câu hỏi thu nhập) → xoá bừa hàng thiếu làm **lệch mẫu**.
2. **Nhiễu và sai sót:** sai đơn vị, sai dấu thập phân, outlier → luôn **vẽ phân phối từng biến** trước khi làm gì khác.
3. **Thiên lệch mẫu (sample bias):** dữ liệu chỉ từ khách hàng ĐÃ duyệt vay không nói gì về người bị từ chối → mô hình tái tạo đúng định kiến cũ.

> ⛔ **Nguyên tắc bất di bất dịch:** *Rác vào thì rác ra (Garbage In, Garbage Out)* — không mô hình nào cứu được dữ liệu tồi.

---

## 5. 📝 Câu hỏi thảo luận (trong slide — luyện tư duy)

Một ngân hàng muốn dự đoán khách hàng nào sắp đóng tài khoản:
1. Liệt kê 5 nguồn dữ liệu ngân hàng; xếp mỗi nguồn vào: có cấu trúc / bán cấu trúc / phi cấu trúc.
2. Từ lịch sử giao dịch, đề xuất 4 đặc trưng có thể tạo ra.
3. Chỉ ra một biến nếu đưa vào sẽ gây **rò rỉ dữ liệu (data leakage)** và giải thích vì sao.

*(Gợi ý câu 3: biến "số ngày còn lại đến ngày khách đóng tài khoản" hoặc "phí đóng tài khoản đã thanh toán" — phản ánh trực tiếp nhãn tương lai, mô hình "gian lận" đạt độ chính xác giả tạo.)*
