# Bộ Câu hỏi Phản biện & Đáp án Học thuật Bảo vệ Bài tập lớn CNM
**Học phần:** Công nghệ Mới nổi và Đổi mới (CNM - MIS01) • HVNH  
**Đề tài:** Hệ sinh thái Điểm thưởng Khách hàng thân thiết Techcombank bằng Blockchain ERC-20  
**Hội đồng chấm thi:** TS. Đinh Trọng Hiếu • TS. Đỗ Văn Thuật  

---

## 👨‍🏫 NHÓM CÂU HỎI KỸ THUẬT CHUYÊN SÂU (TS. ĐỖ VĂN THUẬT)

### ❓ Câu hỏi 1: Tại sao nhóm lại lựa chọn tiêu chuẩn ERC-20 (Fungible Token) mà không dùng ERC-721 (NFT) cho hệ thống điểm thưởng này?
* **Đáp án học thuật:**
  - Tiêu chuẩn **ERC-20** đại diện cho các tài sản có thể thay thế lẫn nhau (Fungible), trong đó 1 điểm TCB-PTS của khách hàng A có giá trị và thuộc tính hoàn toàn đồng nhất với 1 điểm TCB-PTS của khách hàng B. Điều này phản ánh chính xác bản chất toán học của "điểm tích lũy chi tiêu" (tính toán cộng dồn, chia nhỏ, gộp số dư khi thanh toán).
  - Ngược lại, tiêu chuẩn **ERC-721** dùng cho các tài sản độc bản (Non-Fungible Token - NFT) với mỗi token sở hữu một `tokenId` riêng biệt. Nếu dùng ERC-721 cho từng điểm thưởng, chi phí lưu trữ trạng thái (State Storage) trên EVM và lượng Gas tiêu thụ sẽ bùng nổ, gây nghẽn mạng nghiêm trọng.
  - *Mở rộng nâng cao:* Nhóm đề xuất có thể ứng dụng ERC-721 ở giai đoạn mở rộng cho các Voucher đặc biệt phiên bản giới hạn (VIP Membership Card hoặc vé xem hòa nhạc độc quyền).

### ❓ Câu hỏi 2: Chi phí Gas trên Ethereum Mainnet rất đắt đỏ và biến động. Khi áp dụng vào thực tế tại Techcombank với hàng triệu giao dịch mỗi ngày thì bài toán phí Gas được giải quyết ra sao?
* **Đáp án học thuật:**
  - Nhóm không bao giờ đề xuất triển khai trực tiếp hệ thống này trên Ethereum Layer-1 (vốn có chi phí hàng chục USD/giao dịch).
  - Giải pháp kiến trúc của nhóm là triển khai trên **Mạng lưới liên minh riêng (Consortium Blockchain)** hoặc **Ethereum Layer-2 Rollups** (như Arbitrum Orbit, Polygon CDK hoặc Optimism OP Stack). Trên Layer-2, hàng nghìn giao dịch được nén lại thông qua Calldata rồi mới gửi bằng chứng về L1, giúp chi phí thực thi mỗi giao dịch giảm xuống dưới **0.0005 USD (< 15 VNĐ)**.
  - Ngoài ra, mã nguồn của nhóm đã thiết kế hàm `batchRewardPoints()`, gom hàng nghìn giao dịch chi tiêu thẻ cuối ngày để xử lý trong 1 lệnh duy nhất, giúp tối ưu thêm 46% đến 68% lượng Gas tiêu thụ. Toàn bộ phí này do Ngân hàng tài trợ (Gas Subsidy/Account Abstraction ERC-4337), khách hàng hoàn toàn không phải trả phí Gas.

### ❓ Câu hỏi 3: Hợp đồng thông minh của nhóm phòng chống các cuộc tấn công bảo mật phổ biến như thế nào, đặc biệt là lỗi Tràn số (Overflow) và Tấn công Tái nhập (Reentrancy)?
* **Đáp án học thuật:**
  - **Về lỗi tràn số (Arithmetic Overflow/Underflow):** Nhóm biên dịch hợp đồng bằng trình biên dịch Solidity phiên bản `0.8.20`. Từ phiên bản `0.8.0` trở đi, Solidity đã tích hợp sẵn cơ chế kiểm tra toán học nghiêm ngặt mặc định ở cấp độ mã máy; nếu có phép tính vượt ngưỡng (ví dụ trừ số dư âm), EVM sẽ tự động kích hoạt lệnh `revert` và hủy bỏ giao dịch.
  - **Về lỗi tấn công tái nhập (Reentrancy):** Hợp đồng tuân thủ tuyệt đối nguyên tắc thiết kế **Checks-Effects-Interactions (CEI)**. Cụ thể trong hàm `redeemVoucher`, việc kiểm tra số dư (Checks) và lệnh đốt token `_burn()` (Effects - thay đổi trạng thái số dư nội tại) luôn được thực hiện TRƯỚC KHI phát sinh bất kỳ sự kiện hoặc tương tác nào với bên ngoài (Interactions), triệt tiêu hoàn toàn khả năng hacker gọi đệ quy rút cạn quỹ điểm. Đồng thời toàn bộ hợp đồng kế thừa mã nguồn đã qua kiểm toán (Audited) của OpenZeppelin Contracts v5.0.

### ❓ Câu hỏi 4: Khi khách hàng làm mất điện thoại hoặc mất Private Key của ví số, họ có bị mất toàn bộ điểm thưởng tích lũy không?
* **Đáp án học thuật:**
  - Trong mô hình tài chính ngân hàng truyền thống kết hợp Web3, Techcombank áp dụng kiến trúc **Ví phi tập trung có ủy thác quản lý (Semi-Custodial / Smart Contract Wallet chuẩn ERC-4337)**.
  - Khách hàng không cần phải tự ghi nhớ chuỗi 12 từ khóa hạt giống (Seed Phrase) phức tạp. Thay vào đó, việc tạo lập và khôi phục ví được thực hiện thông qua công nghệ **Social Recovery** và tính toán đa bên **MPC (Multi-Party Computation)** liên kết với số điện thoại, CCCD gắn chip và sinh trắc học khuôn mặt theo Quyết định 2345/QĐ-NHNN.
  - Khi khách hàng đổi thiết bị mới, họ chỉ cần thực hiện eKYC sinh trắc học trên ứng dụng Techcombank Mobile, hệ thống quản trị sẽ cấp lại quyền truy cập vào ví điểm thưởng mà số dư token trên Blockchain không hề bị ảnh hưởng.

---

## 👨‍🏫 NHÓM CÂU HỎI ĐỔI MỚI, KINH TẾ & PHÁP LÝ (TS. ĐINH TRỌNG HIẾU)

### ❓ Câu hỏi 5: Về bản chất kinh tế học của Đổi mới sáng tạo (Joseph Schumpeter), đề tài này thuộc loại hình đổi mới nào trong sổ tay Oslo Manual?
* **Đáp án học thuật:**
  - Căn cứ theo **Oslo Manual (OECD)** được TS. Đinh Trọng Hiếu giảng dạy tại Buổi 1 & 2, đề tài này tích hợp đồng thời hai loại hình đổi mới:
    1. **Đổi mới quy trình (Process Innovation):** Thay thế toàn bộ quy trình đối soát bù trừ thủ công chu kỳ 30 ngày (As-Is) bằng quy trình tự động hóa bù trừ theo thời gian thực Zero-Reconciliation (To-Be) thông qua Smart Contract, cắt giảm 85% chi phí vận hành.
    2. **Đổi mới mô hình kinh doanh & dịch vụ (Business Model / Product Innovation):** Chuyển dịch từ chương trình tích điểm đóng khép kín của riêng ngân hàng sang một "Hệ sinh thái mở đa đối tác" (Open Partner Coalition), biến điểm thưởng thành tài sản số thanh khoản cao có thể dùng chung giữa ngân hàng, hãng hàng không và bán lẻ.

### ❓ Câu hỏi 6: Theo quy định của Ngân hàng Nhà nước Việt Nam, tiền mã hóa không phải là phương tiện thanh toán hợp pháp. Việc Techcombank phát hành token TCB-PTS có vi phạm pháp luật không?
* **Đáp án học thuật:**
  - Nhóm khẳng định: **Hệ thống hoàn toàn tuân thủ pháp luật Việt Nam hiện hành.**
  - **Cơ sở pháp lý:** Theo Điều 10 Luật Các tổ chức tín dụng năm 2024 và các quy định liên quan của NHNN, token TCB-PTS được thiết kế tuyệt đối ở dạng **Điểm thưởng tiện ích nội bộ (Non-Monetary Loyalty Utility Token)**:
    1. TCB-PTS chỉ có giá trị quy đổi sang voucher hàng hóa/dịch vụ của đối tác liên minh đã ký kết hợp đồng thương mại với Techcombank.
    2. Token hoàn toàn KHÔNG ĐƯỢC PHÉP quy đổi trực tiếp ra tiền mặt (VND) hoặc giao dịch mua bán trên các sàn giao dịch tự do.
    3. Token không thực hiện chức năng phương tiện thanh toán thay thế tiền tệ quốc gia, mà bản chất kế toán chỉ là chứng từ ghi nhận nghĩa vụ khuyến mại chăm sóc khách hàng của ngân hàng.

### ❓ Câu hỏi 7: Phân tích tài chính cho thấy dự án hoàn vốn trong 11.5 tháng. Những giả định then chốt nào quyết định sự thành bại của con số ROI này?
* **Đáp án học thuật:**
  - Mô hình tài chính của nhóm dựa trên 3 giả định kinh tế thực tế từ Techcombank:
    1. **Cắt giảm chi phí nhân sự:** Techcombank hiện duy trì tổ chuyên trách 12 chuyên viên đối soát dữ liệu với chi phí trung bình 200 triệu đồng/năm/người. Khi tự động hóa 85% quy trình, ngân hàng tiết kiệm trực tiếp 2.04 tỷ đồng/năm.
    2. **Tăng trưởng tỷ lệ kích hoạt thẻ tín dụng:** Nhờ điểm thưởng có thể đổi cà phê Highlands hoặc dặm bay Vietnam Airlines tức thì, tỷ lệ chủ thẻ mới kích hoạt sử dụng tăng từ 58% lên 74% (+16%), tạo ra nguồn thu phí giao dịch quẹt thẻ (Interchange Fee) tăng thêm khoảng 4.5 tỷ đồng/năm.
    3. **Chi phí đầu tư ban đầu (CAPEX):** Ước tính khoảng 3.2 tỷ đồng bao gồm chi phí kiểm toán an ninh Smart Contract, tích hợp API Core Banking và triển khai hạ tầng Consortium node.
  - Phân tích độ nhạy (Sensitivity Analysis) cho thấy ngay cả khi tỷ lệ tăng trưởng thẻ chỉ đạt một nửa kỳ vọng (+8%), dự án vẫn đạt điểm hòa vốn sau 16 tháng.

### ❓ Câu hỏi 8: Nếu một đối tác bán lẻ trong liên minh (ví dụ Highlands Coffee) bị lỗi hệ thống mạng thì giao dịch đổi voucher có làm tắc nghẽn toàn bộ hệ thống của ngân hàng không?
* **Đáp án học thuật:**
  - Hoàn toàn không. Kiến trúc To-Be của nhóm áp dụng mô hình **Kiến trúc hướng sự kiện (Event-Driven Architecture) với Apache Kafka** làm vùng đệm trung chuyển tại Tầng 2.
  - Khi khách hàng đổi voucher, Smart Contract trên chuỗi khối hoàn tất việc đốt token và phát hành Event `VoucherRedeemed` độc lập. Node của Highlands Coffee nếu bị mất mạng tạm thời thì thông điệp sự kiện vẫn được xếp hàng an toàn trong Message Queue của Kafka. Khi hệ thống của đối tác phục hồi, dữ liệu bù trừ sẽ tự động đồng bộ tiếp mà không hề gây ảnh hưởng đến hoạt động quẹt thẻ và Core Banking của Techcombank.
