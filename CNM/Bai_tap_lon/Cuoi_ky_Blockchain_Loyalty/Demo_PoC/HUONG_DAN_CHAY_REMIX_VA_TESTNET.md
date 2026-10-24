# Hướng dẫn Vận hành Demo PoC: Hệ sinh thái Loyalty Techcombank (ERC-20)
**Học viện Ngân hàng (Banking Academy of Vietnam - HVNH)**  
**Học phần:** Công nghệ Mới nổi và Đổi mới (CNM - MIS01)  
**Giảng viên hướng dẫn:** TS. Đinh Trọng Hiếu • TS. Đỗ Văn Thuật  

---

## 🎯 Tổng quan Hai Phương án Trình diễn (Demo Options)

Nhóm phát triển đã đóng gói PoC với **hai phương án trình diễn độc lập**, đảm bảo 100% không bao giờ gặp lỗi khi bảo vệ trước Hội đồng:

1. **Phương án 1 (Khuyên dùng khi Thuyết trình): Web DApp Tương tác (`index.html`)**
   - Chạy trực tiếp trên bất kỳ trình duyệt nào (Chrome, Safari, Edge, Cốc Cốc) bằng cách mở tệp `index.html`.
   - Có sẵn chế độ mô phỏng mạng EVM nội tại (In-Memory Simulation) mượt mà, không phụ thuộc vào kết nối mạng trường học hay ví điện tử.
   - Hỗ trợ kết nối ví MetaMask thực tế nếu người dùng có sẵn ví.

2. **Phương án 2 (Kỹ thuật Chuyên sâu): Chạy Smart Contract trên Remix IDE**
   - Dành cho phần chất vấn kỹ thuật chuyên sâu của **TS. Đỗ Văn Thuật** về mã nguồn Solidity, phân bổ Gas, kiểm tra Transaction Logs và Event `_burn()`.

---

## 🚀 HƯỚNG DẪN CHI TIẾT PHƯƠNG ÁN 1: WEB DAPP TƯƠNG TÁC

### Bước 1: Khởi chạy Giao diện
- Chỉ cần nhấp đúp vào tệp tin:
  `Bai_tap_lon/Cuoi_ky_Blockchain_Loyalty/Demo_PoC/index.html`
- Hoặc mở terminal chạy một máy chủ mini:
  ```bash
  cd Bai_tap_lon/Cuoi_ky_Blockchain_Loyalty/Demo_PoC
  python3 -m http.server 8080
  # Mở trình duyệt tại: http://localhost:8080
  ```

### Bước 2: Kịch bản Thao tác 3 Phút
1. **Phần Ngân hàng (Tab 1):**
   - Nhập số tiền quẹt thẻ của khách: `2.000.000 VNĐ`. Hệ thống tự tính ra `200 TCB-PTS`.
   - Bấm nút **"Phát thưởng Điểm số lên Blockchain"**.
   - Màn hình hiện thông báo giao dịch thành công kèm mã băm `TxHash`.
2. **Phần Khách hàng (Tab 2):**
   - Chuyển sang Tab 2, chỉ cho hội đồng thấy số dư điểm ví khách đã tăng từ `1,250` lên `1,450 TCB-PTS`.
   - Nhấp nút **"Đổi Voucher Ngay"** tại ô Highlands Coffee 50k (Chi phí 200 điểm).
   - Hệ thống tự trừ điểm xuống còn `1,250`, đốt token và hiển thị mã E-Voucher.
3. **Phần Đối tác & Đối soát (Tab 3):**
   - Chuyển sang Tab 3, chỉ vào Sổ cái: Giao dịch thưởng và giao dịch đổi voucher đã được ghi nhận vĩnh viễn trên sổ cái kèm trạng thái `AUTO_SETTLED`.
   - Nhấp nút **"Tải Báo cáo Đối soát CSV"** để minh chứng khả năng thay thế file đối soát thủ công cuối tháng.

---

## ⛓️ HƯỚNG DẪN CHI TIẾT PHƯƠNG ÁN 2: CHẠY REMIX ETHEREUM IDE

### Bước 1: Mở Remix IDE
1. Mở trình duyệt web truy cập: [https://remix.ethereum.org](https://remix.ethereum.org)
2. Tại thư mục `contracts/`, tạo một tệp tin mới đặt tên là: `TechcombankLoyaltyToken.sol`.
3. Sao chép toàn bộ nội dung từ tệp `Demo_PoC/TechcombankLoyaltyToken.sol` dán vào Remix.

### Bước 2: Biên dịch Hợp đồng (Compile)
1. Ở thanh menu bên trái, chọn biểu tượng **Solidity Compiler** (hoặc bấm tổ hợp phím `Ctrl + S`).
2. Chọn phiên bản Compiler: `0.8.20` hoặc `0.8.24`.
3. Bấm nút **Compile TechcombankLoyaltyToken.sol**. Khi hiện dấu tích xanh lá cây `✔` là đã biên dịch thành công 100%.

### Bước 3: Triển khai (Deploy trên Remix VM)
1. Chuyển sang tab **Deploy & Run Transactions** (biểu tượng Ethereum có mũi tên).
2. Tại mục **ENVIRONMENT**, chọn: `Remix VM (Shanghai)` hoặc `Remix VM (Cancun)`.
3. Tại ô tham số của nút `Deploy` màu cam, điền địa chỉ ví quản trị viên (copy địa chỉ ví đầu tiên trong danh mục `ACCOUNT` của Remix, ví dụ: `0x5B38Da6a701c568545dCfcB03FcB875f56beddC4`).
4. Bấm nút **Deploy**. Dưới cửa sổ Console xuất hiện dòng log màu xanh:
   `[vm] from: 0x5B3... to: TechcombankLoyaltyToken.(constructor) status: true`.

### Bước 4: Thao tác các hàm Nghiệp vụ
Dưới mục **Deployed Contracts**, bấm mở rộng hợp đồng:

* **Kiểm tra số dư ban đầu của Ngân hàng:**
  - Nhập địa chỉ ngân hàng vào hàm màu xanh `balanceOf` -> Bấm nút: Hiển thị `10000000000000000000000000` (tương ứng 10 triệu điểm thưởng định dạng 18 số thập phân).
  - Hoặc bấm `getDisplayBalance` -> Hiển thị số nguyên gọn gàng: `10000000`.

* **Ngân hàng thưởng 500 điểm cho khách hàng:**
  - Chọn một địa chỉ ví khách hàng (ví dụ tài khoản thứ 2 trên Remix: `0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2`).
  - Điền vào hàm màu cam `rewardPoints`:
    + `customer`: `0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2`
    + `points`: `500`
    + `transactionRef`: `"POS-VINCOM-HN-001"`
  - Bấm nút `rewardPoints`. Giao dịch xác thực ngay lập tức.
  - Bấm `getDisplayBalance(0xAb8...)` -> Kết quả trả về đúng `500` điểm.

* **Khách hàng đổi 200 điểm lấy Voucher:**
  - Tại ô `ACCOUNT` trên đỉnh Remix, chuyển danh tính sang ví của khách hàng (`0xAb8...`).
  - Điền vào hàm `redeemVoucher`:
    + `costInPoints`: `200`
    + `partnerName`: `"Highlands Coffee"`
    + `voucherCode`: `"HL-50K-ONLINE"`
  - Bấm nút `redeemVoucher`.
  - Kiểm tra lại `getDisplayBalance(0xAb8...)` -> Số dư tự động tụt xuống còn `300`.
  - Mở chi tiết giao dịch trong Console, chỉ cho giảng viên thấy dòng Event `VoucherRedeemed` và lượng điểm đã bị `_burn()` biến mất khỏi lưu thông.

---

## 🛡️ Bảng Tổng hợp Tiêu chuẩn An toàn Kỹ thuật
- **Chuẩn Token:** Ethereum ERC-20 (EIP-20) có tương thích hoàn toàn các ví Web3 (MetaMask, TrustWallet, Rabby).
- **Phân quyền truy cập (Access Control):** Thừa kế mẫu bảo mật `Ownable` từ OpenZeppelin Contracts v5.0, chỉ tài khoản quản trị ngân hàng mới có quyền gọi hàm `rewardPoints` và `setPartnerStatus`.
- **Cơ chế chống lạm phát:** Điểm đổi quà bắt buộc phải `_burn()`, ngăn chặn rủi ro đối tác hoặc nhân viên nội bộ tái sử dụng điểm bất hợp pháp.
