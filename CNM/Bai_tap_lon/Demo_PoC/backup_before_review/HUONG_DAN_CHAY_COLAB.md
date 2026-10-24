# 📖 HƯỚNG DẪN CHẠY DEMO AI FRAUD DETECTION TRÊN GOOGLE COLAB
**Đề tài:** Ứng dụng AI & Xử lý Hướng sự kiện trong Phát hiện Gian lận Giao dịch Thời gian thực tại MB Bank  
**Học phần:** Công nghệ Mới nổi và Đổi mới (MIS01 - HVNH)  
**Giảng viên hướng dẫn:** **TS. Đinh Trọng Hiếu**

---

## 🎯 3 BƯỚC ĐƠN GIẢN ĐỂ KHỞI CHẠY TRÊN GOOGLE COLAB

### BƯỚC 1: Tải file Notebook lên Google Colab
1. Truy cập vào trang web: [https://colab.research.google.com/](https://colab.research.google.com/)
2. Đăng nhập tài khoản Google (Gmail cá nhân hoặc email HVNH).
3. Tại cửa sổ pop-up mở ra, chọn thẻ **"Upload" (Tải lên)** ➔ Bấm **"Choose File"** (hoặc kéo thả file):
   - Chọn file: `MB_Bank_Fraud_Detection_GoogleColab.ipynb` (nằm trong thư mục `HVNH/CNM/Bai_tap_lon/Demo_PoC/`).

---

### BƯỚC 2: Chạy toàn bộ chương trình (Run All)
1. Trên thanh menu trên cùng của Colab, chọn:  
   👉 **Runtime (Thời gian chạy) ➔ Run all (Chạy tất cả)**  
   *(Hoặc nhấn tổ hợp phím `Ctrl + F9` trên Windows, `Cmd + F9` trên Mac).*
2. Chờ khoảng 1 - 2 phút để Colab tự động:
   - Cài đặt các thư viện (`xgboost`, `streamlit`, `plotly`...).
   - Huấn luyện mô hình AI với 25,000 giao dịch ngân hàng giả lập (đạt ROC-AUC ~0.98).
   - Khởi động máy chủ Web Streamlit ở cổng 8501.

---

### BƯỚC 3: Mở đường link Dashboard tương tác
Tại ô code cuối cùng (**BƯỚC 4: Khởi chạy Streamlit & Lấy đường link**), bạn sẽ thấy kết quả hiển thị gồm 2 thông tin:

1. **Dãy số Mật khẩu (IP Address):**  
   Ví dụ: `34.125.89.214` ➔ **Hãy copy dãy số này.**
2. **Đường link truy cập công khai (localtunnel):**  
   Ví dụ: `your url is: https://spicy-dogs-sing.loca.lt` ➔ **Click vào link này.**
3. Trang web bảo mật của localtunnel hiện ra:
   - Dán dãy IP vừa copy vào ô: **"Endpoint IP"**.
   - Bấm nút: **"Click to Submit"**.
4. 🎉 **Giao diện Dashboard MB Bank Fraud SOC sẽ hiển thị ngay lập tức!** Bạn có thể gửi đường link này cho giảng viên hoặc các thành viên trong nhóm mở trực tiếp trên điện thoại/laptop để kiểm tra.

---

## 📸 KỊCH BẢN CHỤP ẢNH MINH CHỨNG CHO BÁO CÁO & SLIDE

Khi giao diện web hiện lên, nhóm hãy thực hiện 3 kịch bản sau để chụp ảnh đưa vào **Chương 4 (Báo cáo)** và **Slide thuyết trình**:

### Kịch bản 1: Giao dịch Hợp lệ (Cấp độ 1 - Xanh lá)
* **Thông số nhập:**
  - Số tiền: `1,500,000 VND`
  - Khung giờ: `14:00` (Ban ngày)
  - Thiết bị: `Thiết bị chính chủ quen thuộc`
  - Địa điểm: `Bình thường (Cùng tỉnh/thành)`
* **Kết quả:** Điểm rủi ro `< 15` ➔ Hệ thống báo **🟢 CẤP ĐỘ 1: GIAO DỊCH AN TOÀN** ➔ Tự động phê duyệt trong `28ms`.

### Kịch bản 2: Giao dịch Đáng ngờ (Cấp độ 2 - Màu Vàng - Tuân thủ QĐ 2345)
* **Thông số nhập:**
  - Số tiền: `25,000,000 VND`
  - Khung giờ: `23:00`
  - Thiết bị: `Thiết bị chính chủ`
  - Tần suất: `4 lần trong 10 phút qua`
* **Kết quả:** Điểm rủi ro `~55 - 65` ➔ Hệ thống báo **🟡 CẤP ĐỘ 2: CẢNH BÁO TRUNG BÌNH** ➔ Kích hoạt **Xác thực Sinh trắc học FaceID eKYC theo Quyết định 2345/QĐ-NHNN**.

### Kịch bản 3: Tấn công Chiếm quyền Tài khoản (Cấp độ 3 - Màu Đỏ)
* **Thông số nhập:**
  - Số tiền: `85,000,000 VND`
  - Khung giờ: `02:30` sáng
  - Thiết bị: `Thiết bị mới lạ vừa đổi`
  - Địa điểm: `Bất thường (Nhảy cóc >500km trong 15p)`
  - Lần nhập sai OTP: `2 lần`
  - Người thụ hưởng: `Tài khoản mới phát sinh lần đầu`
* **Kết quả:** Điểm rủi ro `~90 - 98` ➔ Hệ thống báo **🔴 CẤP ĐỘ 3: NGUY CƠ GIAN LẬN CAO** ➔ **Tức thì chặn giao dịch, tạm khóa tài khoản và bắn cảnh báo khẩn cấp về màn hình SOC MB Bank.**

---

## 🛠️ NẾU MUỐN CHẠY TRỰC TIẾP TRÊN MÁY TÍNH CỤC BỘ (OFFLINE)

Nếu máy bạn đã cài Python 3.10+, bạn cũng có thể chạy ngay trên máy tính mà không cần Colab:
```bash
cd /Users/dovandat/WORKSPACE/HVNH/CNM/Bai_tap_lon/Demo_PoC
pip install -r requirements.txt
python train_model.py
streamlit run app.py
```
Trình duyệt sẽ tự động mở trang web tại địa chỉ: `http://localhost:8501`.
