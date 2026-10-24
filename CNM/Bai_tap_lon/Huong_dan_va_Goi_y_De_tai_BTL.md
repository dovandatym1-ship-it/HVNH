# Hướng dẫn Chi tiết & Gợi ý Đề tài Bài tập lớn Học phần CNM
**Học viện Ngân hàng (Banking Academy of Vietnam - HVNH)**  
**Chương trình Thạc sĩ Hệ thống Thông tin Quản lý (MIS01)**  
**Học phần:** Công nghệ mới nổi và Đổi mới

---

## 🎯 Mục tiêu & Định hướng Thực hiện Bài tập lớn

Bài tập lớn (BTL) là bài kiểm tra toàn diện, chiếm trọng số cao trong kết quả học phần. Giảng viên yêu cầu học viên:
1. **Tiếp cận từ bài toán nghiệp vụ thực tế:** Không làm bài tập chung chung lý thuyết. Nhóm phải chọn một tổ chức cụ thể (ví dụ: Ngân hàng VietinBank, BIDV, Vietcombank, Techcombank, MB Bank, VNPT, MoMo, VNPay...) và chỉ rõ bài toán đau đầu (pain point) họ đang gặp phải.
2. **Mô hình hóa chuẩn nghiệp vụ:** Phải có sơ đồ quy trình hiện tại (**As-Is Process**) và quy trình đề xuất sau khi ứng dụng công nghệ (**To-Be Process**) theo chuẩn **BPMN 2.0**.
3. **Phân tích khả thi 3 góc độ:** Kỹ thuật (Feasibility), Kinh tế (Cost-Benefit / ROI), Tổ chức & Pháp lý (Tuân thủ quy định NHNN, văn hóa doanh nghiệp).
4. **Sản phẩm Demo / Proof-of-Concept (PoC):** Bắt buộc phải có sản phẩm thực nghiệm minh chứng tính khả thi (Smart Contract trên Remix IDE, cụm Docker Containers Microservices, mô hình AI phát hiện gian lận bằng Python/Streamlit,...).

---

## 💡 Top 5 Đề tài Chiến lược Sát Thực tế Ngân hàng & FinTech

### 🌟 Đề tài 1: Ứng dụng Blockchain & Smart Contracts trong Thư tín dụng điện tử (e-L/C) và Tài trợ chuỗi cung ứng (Supply Chain Finance)
* **Tổ chức mục tiêu:** Ngân hàng TMCP Đầu tư và Phát triển Việt Nam (BIDV) hoặc VietinBank.
* **Bài toán thực tế (As-Is):**
  - Quy trình L/C truyền thống dựa trên chứng từ giấy tờ dày đặc (Vận đơn B/L, Hóa đơn thương mại, Chứng nhận xuất xứ C/O).
  - Thời gian xử lý kéo dài từ 5 – 10 ngày làm việc; chi phí chuyển phát thư tín bảo đảm quốc tế tốn kém.
  - Nguy cơ gian lận chứng từ giả mạo, sửa chữa số liệu, rủi ro tài trợ trùng lặp (double financing) một lô hàng tại nhiều ngân hàng.
* **Giải pháp đề xuất (To-Be):**
  - Xây dựng mạng lưới Blockchain liên ngân hàng và đối tác vận tải / hải quan (Consortium Blockchain trên Hyperledger Fabric hoặc Ethereum L2).
  - Tự động hóa giải ngân thông qua **Smart Contract**: Khi Hãng tàu ký xác nhận giao hàng (e-B/L) và Hải quan kiểm duyệt trên chuỗi, Smart Contract tự động kích hoạt chuyển tiền thanh toán cho bên bán trong vòng 15 phút.
* **Sản phẩm Demo / PoC gợi ý:**
  - Viết hợp đồng thông minh `TradeFinanceLC.sol` trên Remix IDE (ngôn ngữ Solidity).
  - Các hàm chính: `createLC()`, `submitShippingDocuments()`, `verifyByCustoms()`, `releasePayment()`.
  - Giao diện minh họa trạng thái vòng đời L/C bằng Web3 hoặc Streamlit.

---

### 🌟 Đề tài 2: Hệ sinh thái Khách hàng thân thiết (Loyalty Points) Đa đối tác dựa trên Token ERC-20
* **Tổ chức mục tiêu:** Khối Ngân hàng Bán lẻ Techcombank hoặc MB Bank.
* **Bài toán thực tế (As-Is):**
  - Điểm thưởng tích lũy khi chi tiêu thẻ tín dụng bị phân mảnh, khó quy đổi qua các hệ sinh thái đối tác khác (hàng không, chuỗi cà phê, siêu thị).
  - Tỷ lệ khách hàng lãng quên và bỏ phí điểm thưởng rất cao (> 40%).
  - Chi phí vận hành, đối soát và bù trừ doanh thu giữa ngân hàng và đối tác liên kết tốn nhiều nhân lực và dễ sai sót.
* **Giải pháp đề xuất (To-Be):**
  - Tiêu chuẩn hóa điểm thưởng thành **Utility Token (chuẩn ERC-20)** lưu trữ trên sổ cái Blockchain.
  - Cho phép người dùng chuyển đổi, trao đổi hoặc ghép điểm thưởng giữa các dịch vụ trong hệ sinh thái mở một cách minh bạch.
  - Sổ cái bất biến giúp đối soát tự động theo thời gian thực (Zero-Reconciliation Cost).
* **Sản phẩm Demo / PoC gợi ý:**
  - Viết Smart Contract `BankLoyaltyToken.sol` kế thừa chuẩn OpenZeppelin ERC20.
  - Chức năng: `rewardCustomer(address, amount)`, `burnTokenForVoucher(address, voucherId)`.
  - Kết nối ví điện tử MetaMask chạy trên mạng thử nghiệm Ethereum Sepolia Testnet.

---

### 🌟 Đề tài 3: Di chuyển Hệ thống Ngân hàng số lên Hạ tầng Điện toán Đám mây lai (Hybrid Cloud) với Microservices & Kubernetes
* **Tổ chức mục tiêu:** Ngân hàng số Timo, TNEX, hoặc Mobile Banking của Vietcombank.
* **Bài toán thực tế (As-Is):**
  - Hạ tầng On-premise vật lý truyền thống thiếu tính co giãn; thường xuyên xảy ra tình trạng nghẽn nghẽ mạng vào các dịp cao điểm (ngày nhận lương 25 hàng tháng, Tết, sự kiện Flash Sale).
  - Quy trình nâng cấp ứng dụng phức tạp (Monolith), mỗi lần cập nhật bản vá lỗi phải dừng toàn bộ hệ thống (downtime).
  - Thời gian đưa tính năng mới ra thị trường (Time-to-Market) kéo dài nhiều tháng.
* **Giải pháp đề xuất (To-Be):**
  - Áp dụng kiến trúc **Hybrid Cloud**: Dữ liệu tài khoản cốt lõi và sổ cái ngân hàng (Core Banking) lưu giữ tuyệt đối tại Private Datacenter On-premise để tuân thủ Thông tư 09/2020/TT-NHNN; toàn bộ dịch vụ giao dịch số ngoại vi (Chuyển tiền nhanh Napas, Thanh toán hóa đơn, Thông báo đẩy) chuyển thành **Microservices** chạy trên Public Cloud nội địa (VNPT Cloud/Viettel Cloud) hoặc AWS.
  - Tự động co giãn (Auto-scaling) theo số lượng yêu cầu bằng **Kubernetes (K8s)** và triển khai không gián đoạn dịch vụ với **CI/CD Blue-Green Deployment**.
* **Sản phẩm Demo / PoC gợi ý:**
  - Xây dựng 3 Microservices nhỏ bằng Python (FastAPI/Flask) hoặc Node.js: `Auth-Service`, `Payment-Service`, `Notification-Service`.
  - Đóng gói từng service bằng Docker (`Dockerfile`).
  - Viết tệp `docker-compose.yml` điều phối các container cùng API Gateway (Nginx/Traefik).
  - Giả lập tải bằng công cụ Apache Bench / Locust chứng minh khả năng xử lý đồng thời.

---

### 🌟 Đề tài 4: Hệ thống Phát hiện Giao dịch Gian lận Tài chính Thời gian thực (Real-Time Fraud Detection) ứng dụng AI & Event-Driven Architecture trên Cloud
* **Tổ chức mục tiêu:** Trung tâm Giám sát Vận hành & Phòng chống Gian lận của NHTM hoặc Ví điện tử MoMo/ZaloPay.
* **Bài toán thực tế (As-Is):**
  - Tấn công mạng, lừa đảo chiếm quyền kiểm soát tài khoản (Account Takeover), thao túng chuyển tiền qua mạng xã hội gia tăng mạnh.
  - Các bộ lọc quy tắc cố định (Rule-based: chuyển > 20 triệu thì báo động) có tỷ lệ cảnh báo giả rất cao gây phiền hà khách hàng, trong khi kẻ gian dễ dàng lách luật bằng cách chia nhỏ giao dịch.
* **Giải pháp đề xuất (To-Be):**
  - Xây dựng luồng xử lý sự kiện theo thời gian thực (Event Stream với Apache Kafka / AWS Kinesis).
  - Triển khai mô hình học máy (Machine Learning: Isolation Forest, XGBoost, Autoencoder) đánh giá rủi ro (Risk Scoring) của từng giao dịch trong thời gian < 100ms dựa trên vị trí địa lý bất thường, tốc độ gõ phím, thiết bị đăng nhập, và lịch sử chi tiêu.
  - Tự động kích hoạt lớp xác thực nâng cao (FIDO2, eKYC sinh trắc học khuôn mặt) khi điểm rủi ro vượt ngưỡng an toàn.
* **Sản phẩm Demo / PoC gợi ý:**
  - Huấn luyện mô hình phát hiện giao dịch bất thường (Credit Card Fraud Detection Dataset).
  - Xây dựng API dự báo bằng FastAPI và giao diện bảng điều khiển giám sát Dashboard bằng Streamlit hiển thị các giao dịch bị chặn thời gian thực.

---

### 🌟 Đề tài 5: Hệ thống Định danh Phi tập trung (Decentralized Identity - DID) và Hồ sơ Tín dụng số trong Ngân hàng Mở (Open Banking)
* **Tổ chức mục tiêu:** Liên minh Ngân hàng mở và các công ty FinTech tài chính tiêu dùng.
* **Bài toán thực tế (As-Is):**
  - Khách hàng muốn vay vốn phải làm thủ tục chứng minh thu nhập và nộp hồ sơ KYC lặp đi lặp lại tại từng ngân hàng.
  - Dữ liệu cá nhân bị phân tán, rủi ro lộ lọt thông tin cao, thiếu một cơ chế chia sẻ tín nhiệm số bảo mật.
* **Giải pháp đề xuất (To-Be):**
  - Ứng dụng công nghệ W3C DID (Decentralized Identifiers) và Verifiable Credentials (VC).
  - Ngân hàng phát hành Chứng chỉ Tín nhiệm số (Credit Credential) có chữ ký số mã hóa cho người dùng lưu trong ví di động (Identity Wallet).
  - Khách hàng có thể xuất trình chứng chỉ này cho bất kỳ tổ chức FinTech nào mà không cần tiết lộ chi tiết số tài khoản hay số dư ngân hàng (Zero-Knowledge Proofs).
* **Sản phẩm Demo / PoC gợi ý:**
  - Tạo cặp khóa mật mã và sinh định danh DID chuẩn W3C bằng thư viện Python hoặc Javascript.
  - Minh họa quy trình: Ngân hàng ký số -> Khách hàng lưu chứng chỉ -> Tổ chức đối tác xác thực chữ ký số công khai trên chuỗi.

---

## 📋 Khung Cấu trúc Báo cáo Bài tập lớn Chuẩn Mực (HVNH)

Báo cáo nộp chính thức nên có độ dài từ **25 đến 40 trang** (định dạng Word chuẩn HVNH: Times New Roman 13pt, dãn dòng 1.5, lề trên/dưới/trái/phải chuẩn 2/2/3/2 cm).

```markdown
TRANG BÌA (Theo mẫu chuẩn Học viện Ngân hàng)
LỜI CẢM ƠN & LỜI CAM ĐOAN
MỤC LỤC, DANH MỤC TỪ VIẾT TẮT, DANH MỤC BẢNG BIỂU, HÌNH VẼ

CHƯƠNG 1: GIỚI THIỆU TỔNG QUAN VỀ CÔNG NGHỆ VÀ BỐI CẢNH ỨNG DỤNG
  1.1. Tổng quan về công nghệ mới nổi được lựa chọn (Bản chất, nguyên lý, xu hướng)
  1.2. Giới thiệu tổ chức/ngân hàng mục tiêu
  1.3. Tổng quan các công trình nghiên cứu và ứng dụng thực tiễn tương tự (Trong nước & Quốc tế)
  1.4. Bài học kinh nghiệm từ các dự án thành công và thất bại

CHƯƠNG 2: PHÂN TÍCH BÀI TOÁN NGHIỆP VỤ VÀ HIỆN TRẠNG (AS-IS)
  2.1. Mô tả chi tiết bài toán khó khăn/điểm nghẽn mà tổ chức đang gặp phải
  2.2. Phân tích nguyên nhân gốc rễ (Root Cause Analysis / 5 Whys / Fishbone)
  2.3. Mô hình hóa quy trình nghiệp vụ hiện tại (As-Is BPMN 2.0 Process Map)
  2.4. Phân tích các yêu cầu của giải pháp (Yêu cầu chức năng & phi chức năng)
  2.5. Xác định mục tiêu dự án theo tiêu chí SMART

CHƯƠNG 3: THIẾT KẾ GIẢI PHÁP ĐỔI MỚI VÀ QUY TRÌNH MỤC TIÊU (TO-BE)
  3.1. Đề xuất giải pháp công nghệ mới nổi
  3.2. Mô hình hóa quy trình nghiệp vụ sau đổi mới (To-Be BPMN 2.0 Process Map)
  3.3. So sánh đánh giá cải tiến quy trình: As-Is vs To-Be (Thời gian, chi phí, rủi ro)
  3.4. Thiết kế kiến trúc hệ thống tổng thể (System Architecture / C4 Model)
  3.5. Đánh giá tính khả thi 3 khía cạnh: Kỹ thuật (Technical), Kinh tế (Economic / ROI), Tổ chức & Pháp lý (Organizational & Regulatory)
  3.6. Các chỉ số đo lường hiệu quả cốt lõi (KPIs)

CHƯƠNG 4: THỰC NGHIỆM CÀI ĐẶT, TRIỂN KHAI DEMO / PROTOTYPE
  4.1. Kiến trúc môi trường thực nghiệm và công cụ triển khai
  4.2. Cài đặt và cấu hình hệ thống
  4.3. Kịch bản thực nghiệm và kết quả vận hành Demo / Proof-of-Concept
  4.4. Phân tích các khó khăn kỹ thuật phát sinh và bài học thực nghiệm

CHƯƠNG 5: ĐÁNH GIÁ, KẾT LUẬN VÀ KIẾN NGHỊ
  5.1. Đánh giá mức độ hoàn thành mục tiêu đề ra
  5.2. Các hạn chế còn tồn tại của giải pháp
  5.3. Lộ trình triển khai diện rộng trong thực tế (Roadmap 12 - 24 tháng)
  5.4. Kiến nghị với Ban Lãnh đạo Ngân hàng và Cơ quan Quản lý (Ngân hàng Nhà nước)

TÀI LIỆU THAM KHẢO (Chuẩn APA / Harvard)
PHỤ LỤC (Mã nguồn, Đặc tả cấu hình, Biên bản họp nhóm)
```

---

## ✅ Bảng Kiểm Tự Rà Soát (Checklist) Cho Học Viên

| Tiêu chí | Điểm tự rà soát | Tình trạng |
| :--- | :--- | :---: |
| **Công nghệ & Bối cảnh** | Đã chọn tổ chức cụ thể tại Việt Nam chưa? Đã nêu rõ tên ngân hàng/doanh nghiệp? | [ ] |
| **Quy trình As-Is** | Đã vẽ biểu đồ BPMN 2.0 cho quy trình hiện tại với đầy đủ Swimlanes chưa? | [ ] |
| **Quy trình To-Be** | Đã chỉ rõ công nghệ mới can thiệp vào bước nào để giải quyết điểm nghẽn chưa? | [ ] |
| **Phân tích 3 mặt** | Đã có mục phân tích Khả thi Kỹ thuật, Khả thi Kinh tế (CBA) và Khả thi Tổ chức? | [ ] |
| **Demo / Prototype** | Đã chạy thử nghiệm mã nguồn thành công và chụp ảnh chụp màn hình / video demo chưa? | [ ] |
| **Slide thuyết trình** | Đã chuẩn bị slide thuyết trình theo cấu trúc 15-20 slide cô đọng, giàu hình ảnh minh họa? | [ ] |
| **Phối hợp nhóm** | Báo cáo đã có bảng phân công công việc và tỷ lệ đóng góp của từng thành viên chưa? | [ ] |
