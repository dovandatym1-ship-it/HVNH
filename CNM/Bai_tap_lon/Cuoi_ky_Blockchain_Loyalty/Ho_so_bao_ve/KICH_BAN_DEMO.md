# Kịch bản Trình diễn Thực nghiệm Demo PoC (Thời lượng: 3 – 5 Phút)
**Đề tài:** Ứng dụng Blockchain và Smart Contract ERC-20 trong Hệ sinh thái Loyalty Techcombank  
**Bảo vệ học phần:** Công nghệ Mới nổi và Đổi mới (CNM - MIS01) • HVNH  

---

## 🕒 Khung Thời Gian Trình Diễn Chi Tiết

```
[0:00 - 0:30]               [0:30 - 1:30]               [1:30 - 2:30]               [2:30 - 3:30]
Giới thiệu Bối cảnh  ➔   Thao tác Ngân hàng  ➔   Khách hàng Đổi quà   ➔   Minh chứng Đối soát
   & Công cụ PoC         (rewardPoints & Batch)     (redeem & Burn Token)       (Zero-Reconciliation)
```

---

### PHẦN 1: MỞ ĐẦU VÀ GIỚI THIỆU CÔNG CỤ (30 Giây)
* **Hành động của người trình bày:** Chiếu Slide số 15, sau đó chuyển cửa sổ sang trình duyệt Web đang mở sẵn tệp `index.html` của PoC.
* **Lời thoại mẫu:**
  > *"Kính thưa quý thầy cô, để chứng minh tính khả thi kỹ thuật của giải pháp, nhóm đã đóng gói một sản phẩm PoC hoàn chỉnh mô phỏng tương tác giữa 3 chủ thể: Ngân hàng Techcombank, Khách hàng chủ thẻ và Đối tác liên minh bán lẻ. Toàn bộ logic nghiệp vụ được điều khiển bởi Hợp đồng thông minh `TechcombankLoyaltyToken.sol` tuân thủ tiêu chuẩn ERC-20 của OpenZeppelin. Sau đây em xin bắt đầu trình diễn 3 kịch bản cốt lõi."*

---

### PHẦN 2: THAO TÁC CỔNG QUẢN TRỊ TECHCOMBANK (60 Giây)
* **Hành động 1 (Thưởng điểm đơn lẻ):**
  - Giữ nguyên tại **Tab 1: Cổng Quản trị Techcombank**.
  - Chỉ vào ô *"Giá trị quẹt thẻ"*: Nhập `1.500.000 VNĐ`. Hệ thống tự quy đổi ra `150 TCB-PTS`.
  - Bấm nút **"🚀 Phát thưởng Điểm số lên Blockchain"**.
* **Lời thoại mẫu:**
  > *"Giả sử chủ thẻ Visa Platinum vừa chi tiêu 1,5 triệu đồng tại nhà hàng. Core Banking phát tín hiệu và ví quản trị của Techcombank gọi hàm `rewardPoints()`. Giao dịch được xác thực ngay trong 0.85 giây với mã băm TxHash hiển thị trên màn hình. Số điểm 150 token được chuyển thẳng vào ví số của khách."*
* **Hành động 2 (Thưởng điểm theo lô - Batch Settlement):**
  - Chỉ vào khung bên phải, bấm nút **"⚡ Thực thi Batch Settlement (3 Giao dịch)"**.
* **Lời thoại mẫu:**
  > *"Vào cuối ngày, để tối ưu hóa chi phí mạng, Techcombank kích hoạt hàm `batchRewardPoints()`. Ba giao dịch chi tiêu thẻ được gộp vào duy nhất một khối, giúp tiết kiệm tới 68% chi phí Gas so với việc gọi hàm đơn lẻ."*

---

### PHẦN 3: TRẢI NGHIỆM KHÁCH HÀNG MOBILE VÀ ĐỐT TOKEN (60 Giây)
* **Hành động:**
  - Nhấp chuột chuyển sang **Tab 2: Khách hàng Mobile Banking**.
  - Chỉ vào thẻ ví màu đỏ: Số dư điểm vừa tăng lên tương ứng.
  - Cuộn xuống danh mục Voucher, bấm nút **"Đổi Voucher Ngay"** tại thẻ *Highlands Coffee 50.000đ (Chi phí: 200 TCB-PTS)*.
  - Hộp thông báo màu xanh bật lên kèm mã voucher `HL-COFFEE-50K-xxxx` và mã xác thực TxHash.
* **Lời thoại mẫu:**
  > *"Bây giờ em đóng vai trò khách hàng mở Techcombank Mobile. Em thấy số dư của mình và quyết định đổi một ly cà phê Highlands trị giá 50.000 đồng với giá 200 điểm. Khi em bấm 'Đổi quà', Smart Contract gọi hàm `redeemVoucher()` và thực hiện lệnh `_burn()` 200 điểm khỏi ví em vĩnh viễn. Token bị tiêu hủy để ngăn chặn việc lạm phát và sinh ra một mã E-Voucher kèm mã băm mật mã keccak256."*

---

### PHẦN 4: MINH CHỨNG SỔ CÁI VÀ ĐỐI SOÁT ZERO-RECONCILIATION (60 Giây)
* **Hành động:**
  - Nhấp chuột chuyển sang **Tab 3: Đối tác & Đối soát Zero-Reconciliation**.
  - Chỉ vào dòng giao dịch vừa phát sinh trong bảng Sổ cái: Loại hành động `REDEEM_BURN (Highlands Coffee)`, Số lượng `-200`, Trạng thái `ZERO_REC_CONFIRMED`.
  - Bấm nút **"📥 Tải Báo cáo Đối soát CSV"**. Tệp CSV lập tức tải về máy.
* **Lời thoại mẫu:**
  > *"Đây chính là giá trị cốt lõi giải quyết bài toán của đề tài: Giao thức Zero-Reconciliation. Thay vì kế toán Techcombank và Highlands Coffee phải đối soát file Excel sau 30 ngày, thì ngay tại thời điểm khách hàng đổi voucher, sự kiện trên chuỗi khối đã lập tức ghi nhận khoản bù trừ doanh thu. Sổ cái phân tán này là bằng chứng kế toán bất biến giữa hai bên. Khi cần kiểm toán, chỉ cần nhấp một nút tải tệp CSV về, hoàn toàn không có độ trễ và không thể xảy ra sai lệch số liệu."*

---

### PHẦN 5: DỰ PHÒNG KHI GIẢNG VIÊN HỎI VỀ CODE SOLIDITY (REMIX IDE)
* **Tình huống:** TS. Đỗ Văn Thuật yêu cầu xem mã nguồn hợp đồng thật trên Remix.
* **Cách xử lý:**
  1. Mở sẵn tab trình duyệt truy cập `remix.ethereum.org`.
  2. Mở file `TechcombankLoyaltyToken.sol`.
  3. Bấm mở rộng Deployed Contract: Chỉ rõ hàm `rewardPoints` có modifier `onlyOwner`, hàm `redeemVoucher` có lệnh `_burn(msg.sender, rawCost)`, và hàm `validateAndUseVoucher` đổi cờ `item.isUsed = true`.
  4. Khẳng định: Toàn bộ code đã kế thừa thư viện chuẩn của OpenZeppelin Contracts v5.0 nên hoàn toàn miễn nhiễm với các lỗi bảo mật tràn số (Overflow) và tấn công tái nhập (Reentrancy).
