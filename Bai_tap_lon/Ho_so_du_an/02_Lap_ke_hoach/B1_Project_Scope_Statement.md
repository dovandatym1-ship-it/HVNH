# TUYÊN BỐ PHẠM VI DỰ ÁN (PROJECT SCOPE STATEMENT)
## Dự án: Xây dựng Hệ thống Quản trị Nhân sự Nội bộ (ABC-HRM)
### Mã tài liệu: BTL-QLDA-B1 | Giai đoạn: Lập kế hoạch (Planning)
### Đơn vị thụ hưởng: Công ty Cổ phần ABC | Học phần: Quản lý Dự án CNTT Nâng cao (HVNH)

---

## 1. MỤC TIÊU VÀ PHẠM VI TỔNG THỂ

Tuyên bố Phạm vi Dự án (Project Scope Statement) đóng vai trò là tài liệu cơ sở xác lập ranh giới công việc của dự án **ABC-HRM**, phân định rõ ràng giữa những gì **thuộc phạm vi dự án (In-Scope)** và những gì **nằm ngoài phạm vi dự án (Exclusions)**. Đây là công cụ pháp lý và kỹ thuật quan trọng nhất để thiết lập Đường cơ sở Phạm vi (Scope Baseline), đồng thời bảo vệ dự án khỏi hiện tượng phình to phạm vi (Scope Creep) làm mất kiểm soát tiến độ và chi phí.

---

## 2. MÔ TẢ PHẠM VI SẢN PHẨM (PRODUCT SCOPE DESCRIPTION)

Sản phẩm của dự án là **Hệ thống Quản trị Nhân sự Nội bộ (ABC-HRM)** chạy trên nền tảng Web Application tập trung, phục vụ toàn bộ 100 cán bộ nhân viên của Công ty Cổ phần ABC, bao gồm 6 phân hệ chức năng:

### 2.1. Phân hệ 1: Quản lý Hồ sơ Nhân sự (Employee Profile Management)
* Quản lý hồ sơ nhân viên tập trung theo mã định danh duy nhất (Staff ID), bao gồm: thông tin cá nhân, sơ yếu lý lịch, quá trình đào tạo, lịch sử công tác, chức danh, cấp bậc và mức lương cơ sở.
* Quản lý vòng đời Hợp đồng lao động: Hợp đồng thử việc, hợp đồng xác định thời hạn (12–36 tháng), hợp đồng không xác định thời hạn; số hóa và lưu trữ tài liệu đính kèm (scan CCCD, văn bằng, chứng chỉ) với dung lượng tối đa 10MB/tài liệu.
* Tự động quét và cảnh báo trước 30 ngày các hợp đồng lao động sắp hết hạn để phòng HR tiến hành thủ tục gia hạn hoặc thanh lý.

### 2.2. Phân hệ 2: Chấm công & Quản lý Nghỉ phép (Attendance & Leave Management)
* Kết nối trực tiếp qua API/Webhook với thiết bị chấm công vân tay ZKTeco đặt tại văn phòng công ty; đồng bộ dữ liệu vào/ra (Check-in/Check-out) theo thời gian thực (độ trễ không quá 5 giây).
* Quản lý lịch làm việc linh hoạt: Giờ làm việc tiêu chuẩn (8h00 – 17h30, nghỉ trưa 1h30), ca làm thêm giờ (OT ngày thường 150%, ngày nghỉ 200%, ngày lễ 300%).
* Quản lý quỹ nghỉ phép hàng năm: Cấp phát tự động 12 ngày phép năm/nhân viên (tăng thêm 1 ngày sau mỗi 5 năm cống hiến theo Bộ luật Lao động); quy trình nộp đơn xin nghỉ phép, duyệt đơn trực tuyến 2 cấp (Quản lý trực tiếp $\rightarrow$ Trưởng phòng HR).
* Tự động tổng hợp Bảng công tháng chi tiết (số công chuẩn, số công thực tế, số giờ OT, số ngày nghỉ phép có lương/không lương).

### 2.3. Phân hệ 3: Tính lương & Phúc lợi (Payroll & Benefits Engine)
* Động cơ tính lương tự động dựa trên công thức cấu hình tham số:
  $$\text{Lương thực nhận (Net)} = \text{Lương cứng} + \text{Phụ cấp} + \text{Lương OT} + \text{Thưởng KPI} - \text{Các khoản trích BHXH/BHYT/BHTN} - \text{Thuế TNCN}$$
* Tự động tính toán các khoản trích theo lương theo quy định hiện hành của pháp luật Việt Nam:
  - Trừ vào lương nhân viên: BHXH (8%), BHYT (1,5%), BHTN (1%).
  - Chi phí doanh nghiệp đóng: BHXH (17,5%), BHYT (3%), BHTN (1%), Kinh phí Công đoàn (2%).
* Tự động tính thuế Thu nhập cá nhân (TNCN) theo biểu thuế lũy tiến từng phần 7 bậc sau khi đã khấu trừ giảm trừ gia cảnh cho bản thân (11 triệu/tháng) và người phụ thuộc (4,4 triệu/người/tháng).
* Tự động xuất phiếu lương điện tử (Payslip định dạng PDF có mật khẩu mã hóa) và gửi qua email nội bộ cho từng nhân viên.

### 2.4. Phân hệ 4: Tuyển dụng & Onboarding (Recruitment & Onboarding)
* Đăng tải và quản lý kế hoạch định biên tuyển dụng theo phòng ban.
* Quản lý phễu ứng viên (Candidate Pipeline): Ứng tuyển $\rightarrow$ Sơ loại hồ sơ $\rightarrow$ Phỏng vấn vòng 1 $\rightarrow$ Phỏng vấn vòng 2 $\rightarrow$ Gửi thư mời nhận việc (Offer Letter).
* Quy trình tiếp nhận nhân sự mới (Onboarding Checklist): Tự động tạo danh mục công việc cần chuẩn bị (cấp email, cấp thiết bị máy tính, bàn giao chỗ ngồi, ký cam kết bảo mật NDA).

### 2.5. Phân hệ 5: Quản trị Hiệu suất KPI (Performance & KPI Management)
* Thiết lập mục tiêu chiến lược của công ty phân rã về từng phòng ban và nhân viên theo phương pháp KPI/OKRs định kỳ (theo quý và năm).
* Cho phép nhân viên tự đánh giá (Self-assessment), Quản lý trực tiếp đánh giá, và phản hồi 360 độ từ đồng nghiệp.
* Tổng hợp điểm hiệu suất phân loại nhân sự theo 4 mức: Xuất sắc (A), Tốt (B), Đạt yêu cầu (C), Cần cải thiện (D) để phục vụ xét tăng lương và chi trả thưởng Tết.

### 2.6. Phân hệ 6: Báo cáo & Dashboard Quản trị (Analytics & Executive Dashboard)
* Cung cấp Dashboard biểu đồ tương tác thời gian thực dành cho Ban Giám đốc và HR Manager: Thống kê quy mô nhân sự (Headcount), cơ cấu thâm niên, cơ cấu độ tuổi, tỷ lệ thôi việc (Turnover rate), chi phí quỹ lương hàng tháng, và tỷ lệ chuyên cần.
* Cho phép kết xuất báo cáo đa định dạng (Excel, PDF) phục vụ công tác thanh tra lao động và quyết toán thuế cuối năm.

---

## 3. MÔ TẢ PHẠM VI DỰ ÁN (PROJECT SCOPE DESCRIPTION)

Để bàn giao được sản phẩm trên, nhóm dự án phải hoàn thành các gói công việc quản lý và kỹ thuật sau:
1. **Khảo sát hiện trạng & Lập tài liệu đặc tả yêu cầu (SRS):** Phỏng vấn 100% các bên liên quan, thu thập toàn bộ biểu mẫu Excel cũ và chuẩn hóa luồng nghiệp vụ.
2. **Thiết kế Hệ thống:** Xây dựng Kiến trúc 3 tầng (React / NestJS / PostgreSQL), thiết kế mô hình CSDL quan hệ (ERD), thiết kế giao diện UI/UX trên Figma (Wireframe & High-fidelity prototype).
3. **Phát triển Phần mềm:** Lập trình mã nguồn Backend API, Frontend UI, và Module Adapter kết nối thiết bị phần cứng ZKTeco theo chuẩn RESTful API.
4. **Kiểm thử Hệ thống:** Thực hiện kiểm thử đơn vị (Unit Test $\ge 80\%$ code coverage), kiểm thử tích hợp (Integration Test), kiểm thử tải (Load Test tính lương 100 nhân viên $< 30$ giây), và kiểm thử chấp nhận người dùng (UAT).
5. **Di chuyển Dữ liệu (Data Migration):** Viết script ETL để trích xuất, làm sạch và nạp 100% hồ sơ của 100 nhân viên từ các file Excel cũ vào PostgreSQL.
6. **Đào tạo & Chuyển giao:** Biên soạn tài liệu User Guide, Ops Manual; tổ chức 03 buổi đào tạo người dùng và hỗ trợ vận hành song hành 30 ngày sau go-live.
7. **Bảo hành:** Cam kết bảo hành, khắc phục lỗi kỹ thuật phát sinh trong 03 tháng kể từ ngày ký biên bản nghiệm thu chính thức.

---

## 4. DANH MỤC PHẠM VI LOẠI TRỪ (PROJECT EXCLUSIONS)

> [!CRITICAL]
> **Quy định Chống Lạm phát Phạm vi (Scope Creep Prevention):**
> Để đảm bảo dự án không bị vỡ ngân sách trần 850 triệu VNĐ và không bị chậm tiến độ go-live 30/04/2026, các hạng mục dưới đây **TUYỆT ĐỐI KHÔNG NẰM TRONG PHẠM VI DỰ ÁN**:

| Mã loại trừ | Hạng mục loại trừ | Lý do loại trừ và Ranh giới quản lý |
|:---:|---|---|
| **EX-01** | **Ứng dụng Di động Bản địa (Native iOS/Android App)** | Chi phí phát triển ứng dụng di động bản địa và duy trì trên App Store/Google Play vượt quá ngân sách cho phép. Thay vào đó, hệ thống chỉ hỗ trợ **Responsive Web**, cho phép nhân viên truy cập đầy đủ tính năng qua trình duyệt điện thoại. |
| **EX-02** | **Tích hợp hai chiều với Hệ thống Kế toán ERP lớn (SAP, MISA, Oracle)** | Việc tích hợp API phức tạp với hệ thống kế toán bên ngoài đòi hỏi chi phí bản quyền cổng kết nối rất lớn. Ranh giới kỹ thuật: Hệ thống ABC-HRM chỉ xuất bảng lương dạng file Excel chuẩn theo đúng mẫu của phòng Kế toán để kế toán viên import thủ công. |
| **EX-03** | **Phân hệ Quản lý Đào tạo Nội bộ (LMS / E-Learning)** | Khảo sát cho thấy nhu cầu đào tạo trực tuyến chưa cấp bách trong năm 2026; đưa phân hệ này vào sẽ làm kéo dài thời gian phát triển thêm ít nhất 20 ngày công. Hạng mục này được quy hoạch vào **Giai đoạn 2 (Phase 2)** sau khi hệ thống cốt lõi vận hành ổn định. |
| **EX-04** | **Hỗ trợ Đa ngôn ngữ (Multi-language Support)** | Công ty ABC là doanh nghiệp nội địa với 100% nhân sự người Việt Nam; hệ thống chỉ sử dụng **ngôn ngữ Tiếng Việt**, không phát triển cơ chế chuyển đổi ngôn ngữ (i18n) để tối ưu hóa thời gian lập trình. |
| **EX-05** | **Mua sắm Phần cứng Máy tính / Thay thế Máy chấm công mới** | Dự án chỉ phát triển phần mềm; tận dụng nguyên trạng các máy quét vân tay ZKTeco hiện có tại văn phòng công ty. Mọi chi phí sửa chữa hỏng hóc phần cứng thuộc ngân sách bảo trì hành chính của công ty. |

---

## 5. TIÊU CHÍ CHẤP NHẬN SẢN PHẨM BÀN GIAO (ACCEPTANCE CRITERIA)

Dự án chỉ được nghiệm thu khi đáp ứng đầy đủ các tiêu chuẩn định lượng sau:

| STT | Lĩnh vực | Tiêu chí chấp nhận định lượng | Phương pháp thẩm định |
|:---:|---|---|---|
| 1 | **Chức năng** | 100% trong số 12 Yêu cầu Chức năng (FR-01 đến FR-12) hoạt động chính xác theo đặc tả SRS đã được phê duyệt. | Chạy bộ kiểm thử chấp nhận UAT với 50 kịch bản thử nghiệm mẫu. |
| 2 | **Độ chính xác dữ liệu** | Sai số trong tính toán bảng lương cho 100 nhân sự bằng **0%**; đối chiếu bảng tính hệ thống với bảng tính tay kế toán khớp nhau tuyệt đối. | Kế toán trưởng và HR Manager ký xác nhận bảng lương thử nghiệm kỳ lương tháng 03/2026. |
| 3 | **Hiệu năng hệ thống** | Thời gian tải trang trung bình $< 2,0$ giây; thời gian tính toán và xuất bảng lương 100 nhân sự $< 30$ giây; hỗ trợ 50 người dùng truy cập đồng thời. | Kiểm thử tải tự động (Load Testing) bằng công cụ Apache JMeter. |
| 4 | **Bảo mật** | Mã hóa 100% mật khẩu người dùng (Bcrypt) và thông tin tiền lương nhạy cảm (AES-256); không có lỗi bảo mật thuộc danh mục OWASP Top 10 (SQL Injection, XSS, CSRF). | Báo cáo rà quét bảo mật và ký xác nhận của Trưởng phòng CNTT (IT Lead). |
| 5 | **Chuyển đổi dữ liệu** | 100% hồ sơ của 100 nhân viên hiện tại được nạp đầy đủ vào hệ thống mới mà không mất mát bất kỳ trường thông tin lịch sử nào. | Báo cáo đối soát dữ liệu (Reconciliation Report) ký bởi HR Manager. |
| 6 | **Mức độ ứng dụng** | Tỷ lệ nhân viên kích hoạt tài khoản và tự nộp đơn/chấm công đạt $\ge 90\%$ sau 30 ngày go-live. | Trích xuất báo cáo thống kê log truy cập từ Dashboard hệ thống. |

---

## 6. PHÊ DUYỆT TUYÊN BỐ PHẠM VI

Tuyên bố Phạm vi Dự án này là căn cứ tối thượng để thiết lập Cấu trúc Phân chia Công việc (WBS) và kiểm soát mọi phát sinh thay đổi.

| Quản lý Dự án (PM) | Trưởng phòng Nhân sự (HR Head) | Trưởng phòng CNTT (IT Lead) |
|:---:|:---:|:---:|
| *(Đã ký)* | *(Đã ký)* | *(Đã ký)* |
| **[Họ và tên Học viên 1]** | **Trần Thị B** | **Phạm Quốc D** |
