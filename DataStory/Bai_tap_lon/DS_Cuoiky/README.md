# BÁO CÁO CUỐI KỲ - MÔN HỌC DATA STORYTELLING

**Tên dự án:** Không sợ "Lỗ hổng" phát sinh, chỉ sợ thiếu "Khả năng phục hồi"  
**Bối cảnh Dữ liệu:** Phân tích tiến độ thi công của 6.000 dự án thuộc "Công ty Cổ phần Tập đoàn Công nghiệp Việt" (Giai đoạn 2022-2025).  
**Insight Cốt lõi (Aha Moment):** Thủ phạm lớn nhất gây trễ hạn dự án không phải là thời tiết hay mặt bằng, mà là sự cộng hưởng giữa **"Thay đổi thiết kế"** và sự thiếu vắng **"Khả năng phục hồi tiến độ" (Schedule Resilience)** của hệ thống quản lý.

---

## 📁 Cấu trúc Thư mục `DS_Cuoiky`

Bộ hồ sơ dự án này đã được đóng gói hoàn chỉnh bao gồm các thành phần sau:

### 1. Dữ liệu Thô (Raw Data)
- `data.csv` & `data.xlsx`: Bộ dữ liệu gốc 6.000 dòng được giả lập chứa các lỗi thực tế (Dữ liệu bẩn) như: định dạng ngày tháng lộn xộn, giá trị tiền tệ lẫn chữ ("15B", "15000 Triệu"), lỗi đánh máy (Typo) ở tên công ty, và dữ liệu khuyết thiếu (Missing Values).

### 2. Dữ liệu Sạch (Cleaned Data)
- `cleaned_data.csv` & `cleaned_data.xlsx`: Tập dữ liệu đã được làm sạch 100% bằng Python (`pandas`). File này có thể được import thẳng vào Tableau, PowerBI, hoặc Canva để xây dựng Dashboard biểu diễn.

### 3. Notebook Phân tích (Data Analysis & EDA)
- `EDA_Project.ipynb`: File Jupyter Notebook trình bày toàn bộ luồng tư duy và Code. Được cấu trúc chuẩn theo mạch Data Story: 
  - **Data Quality Check:** Đánh giá dữ liệu thô.
  - **Data Cleaning:** Xử lý chuỗi, ép kiểu dữ liệu thời gian/tiền tệ.
  - **EDA & Storyboarding:** Vẽ biểu đồ Bar Chart để bác bỏ định kiến (Truy tìm thủ phạm) và vẽ biểu đồ Scatter Plot để chứng minh tương quan tỷ lệ thuận tuyệt đối (Điểm bùng nổ Aha!).

### 4. Kịch bản Thuyết trình (Presentation Script)
- `Kich_ban_Thuyet_trinh_Canva.md`: Kịch bản thiết kế và lời thoại chi tiết cho 10 slide Canva, tuân thủ chặt chẽ mô hình *Freytag's Pyramid* (Hook -> Context -> Conflict -> Aha Moment -> Resolution).

---

## 🛠 Các kỹ thuật Data Cleaning đã áp dụng
Để làm ra file `cleaned_data`, quá trình tiền xử lý đã sử dụng các kỹ thuật sau:
1. **Datetime Parsing:** Đồng nhất 3 định dạng thời gian lộn xộn về chuẩn Datetime (`YYYY-MM-DD`).
2. **Currency Parsing (Regex):** Loại bỏ các từ khóa (Billion, Tỷ, Triệu, B), thay thế dấu phẩy bằng dấu chấm, và quy đổi toàn bộ cột Giá trị hợp đồng về kiểu `Float` (Đơn vị: Tỷ VNĐ).
3. **Text Standardization:** Xóa khoảng trắng thừa (`strip`), chuẩn hóa chữ in hoa đầu dòng (`title`), và thay thế các từ khóa bị Typo (Denisoo -> Deniso).
4. **Data Imputation:** Lấp đầy các giá trị rỗng (NaN) ở cột Nguyên nhân chậm tiến độ và Thầu phụ bằng các hằng số phân loại rõ ràng ("Chưa xác định", "Đúng/Sớm hạn").
5. **Feature Engineering:** Tạo thêm cột `Trạng thái` (Trễ hạn / Đúng hạn) từ việc trích xuất số nguyên trong cột `Số ngày chậm`.

---
*Dự án được xây dựng và đóng gói hoàn thiện phục vụ bài nộp cuối kỳ.*
