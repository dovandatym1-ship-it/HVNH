# TÀI LIỆU ĐẶC TẢ YÊU CẦU PHẦN MỀM (SRS) & MA TRẬN TRUY VẾT
## Dự án: Xây dựng Hệ thống Quản trị Nhân sự Nội bộ (ABC-HRM)
### Mã tài liệu: BTL-QLDA-B2 | Giai đoạn: Lập kế hoạch (Planning)
### Tiêu chuẩn áp dụng: IEEE 830-1998 / ISO/IEC/IEEE 29148 | Học phần: QLDA CNTT Nâng cao (HVNH)

---

## 1. GIỚI THIỆU CHUNG VÀ PHẠM VI ÁP DỤNG

Tài liệu Đặc tả Yêu cầu Phần mềm (Software Requirements Specification - SRS) này định nghĩa chi tiết toàn bộ các yêu cầu chức năng (Functional Requirements - FR) và yêu cầu phi chức năng (Non-Functional Requirements - NFR) của hệ thống **ABC-HRM**, phục vụ làm căn cứ kỹ thuật cho quá trình thiết kế, lập trình, kiểm thử và nghiệm thu sản phẩm bàn giao.

---

## 2. ĐẶC TẢ CHI TIẾT 12 YÊU CẦU CHỨC NĂNG (FUNCTIONAL REQUIREMENTS)

### Module 1: Quản lý Hồ sơ Nhân sự & Hợp đồng Số
* **FR-01: Quản lý Hồ sơ Nhân viên (Employee Profile CRUD)**
  - *Mô tả:* Hệ thống cho phép chuyên viên HR tạo mới, tra cứu, cập nhật và khóa hồ sơ nhân viên. Mỗi nhân viên được cấp một mã số duy nhất (`staff_code`) định dạng `ABC-XXXX`.
  - *Dữ liệu lưu trữ:* Họ tên, ngày sinh, giới tính, số CCCD, ngày cấp, nơi cấp, mã số thuế cá nhân, số sổ BHXH, địa chỉ thường trú, số điện thoại, email công ty, phòng ban, chức vụ, tài khoản ngân hàng chi trả lương, danh sách người phụ thuộc đăng ký giảm trừ gia cảnh.
  - *Quy tắc nghiệp vụ:* Số CCCD, email công ty và mã số thuế phải là duy nhất trên toàn hệ thống. Nhân viên chỉ được xem và chỉnh sửa một số thông tin cá nhân cơ bản (số điện thoại, địa chỉ), không được tự sửa chức danh và mức lương.
* **FR-02: Quản lý Hợp đồng Lao động & Cảnh báo Tự động (Contract Management)**
  - *Mô tả:* Hệ thống quản lý toàn bộ hợp đồng lao động điện tử của nhân viên.
  - *Quy tắc nghiệp vụ:* Phân loại hợp đồng theo 3 loại chuẩn: Thử việc (02 tháng), Xác định thời hạn (12–36 tháng), Không xác định thời hạn. Cho phép đính kèm bản scan hợp đồng có chữ ký (định dạng PDF $\le 10$MB).
  - *Tính năng tự động:* Hàng ngày vào lúc 08h00 sáng, hệ thống tự động quét và gửi email thông báo tới Trưởng phòng HR danh sách các hợp đồng lao động sẽ hết hạn trong vòng 30 ngày tới kèm đường dẫn khởi tạo phụ lục hợp đồng hoặc quyết định thanh lý.

---

### Module 2: Chấm công & Quản lý Nghỉ phép
* **FR-03: Tích hợp Thiết bị Chấm công Vân tay (Biometric Device Integration)**
  - *Mô tả:* Hệ thống cung cấp dịch vụ Adapter (Background Service) kết nối liên tục với máy quét vân tay ZKTeco qua giao thức TCP/IP Socket hoặc Webhook.
  - *Quy tắc nghiệp vụ:* Khi nhân viên quét vân tay thành công tại cửa văn phòng, log chấm công (`device_id`, `staff_code`, `timestamp`, `verify_type`) phải được đẩy về hệ thống trong vòng không quá 05 giây. Trường hợp mất kết nối mạng nội bộ, thiết bị tự lưu trữ cục bộ và đồng bộ tự động khi kết nối internet được khôi phục.
* **FR-04: Quản lý Đơn từ & Duyệt Nghỉ phép Trực tuyến (Leave & OT Request Workflow)**
  - *Mô tả:* Cho phép nhân viên tạo các loại đơn điện tử: Đơn xin nghỉ phép năm, Đơn xin nghỉ ốm/chế độ thai sản, Đơn xin làm ngoài giờ (OT), Đơn giải trình quên quét vân tay.
  - *Quy trình phê duyệt:* Đơn được chuyển tự động tới Quản lý trực tiếp (Manager) qua thông báo nội bộ và email. Manager xem xét phê duyệt trong vòng 24 giờ $\rightarrow$ Đơn chuyển lên Trưởng phòng HR phê duyệt vòng cuối $\rightarrow$ Tự động trừ quỹ phép năm của nhân viên.
* **FR-05: Tự động Tổng hợp Bảng Chấm công Tháng (Timesheet Aggregation)**
  - *Mô tả:* Hệ thống đối soát tự động giữa dữ liệu quét vân tay vào/ra thực tế với lịch làm việc chuẩn và các đơn từ hợp lệ đã duyệt.
  - *Đầu ra:* Tự động xuất Bảng công tháng tổng hợp gồm: Số ngày công tiêu chuẩn (22 công), số ngày công thực tế, số phút đi muộn/về sớm, số giờ làm thêm (OT ngày thường, OT cuối tuần, OT lễ tết), và số ngày nghỉ phép (có lương/không lương). Cho phép HR xuất file Excel để kiểm tra chéo.

---

### Module 3: Động cơ Tính lương & Phúc lợi
* **FR-06: Động cơ Tính lương Gross-to-Net Linh hoạt (Payroll Engine)**
  - *Mô tả:* Tự động tính toán chi tiết bảng lương từng nhân viên vào ngày chốt lương hàng tháng căn cứ vào dữ liệu từ Bảng công tổng hợp (FR-05) và mức lương thỏa thuận trong Hợp đồng lao động (FR-02).
  - *Công thức cốt lõi:*
    $$\text{Lương Cơ bản Thực tế} = \frac{\text{Lương thỏa thuận}}{\text{Số ngày công chuẩn}} \times \text{Số ngày công thực tế}$$
    $$\text{Lương OT} = \sum (\text{Số giờ OT} \times \text{Đơn giá giờ chuẩn} \times \text{Hệ số OT } [150\%, 200\%, 300\%])$$
    $$\text{Tổng Thu nhập Chịu thuế} = \text{Lương Thực tế} + \text{Lương OT} + \text{Phụ cấp trách nhiệm} + \text{Thưởng hiệu suất}$$
* **FR-07: Tính toán Tự động Khấu trừ BHXH và Thuế TNCN (Statutory Deductions)**
  - *Mô tả:* Áp dụng tự động các quy định pháp luật lao động hiện hành tại Việt Nam mà không cần tính toán thủ công:
    - *Bảo hiểm bắt buộc trừ vào lương:* BHXH (8%), BHYT (1,5%), BHTN (1%) trên mức lương đóng bảo hiểm (áp dụng chặn mức trần đóng BHXH = 20 lần mức lương cơ sở).
    - *Thuế TNCN:* Tính giảm trừ bản thân (11 triệu VNĐ/tháng) và giảm trừ người phụ thuộc (4,4 triệu VNĐ/người/tháng $\times$ số người phụ thuộc hợp lệ). Áp biểu thuế lũy tiến từng phần 7 bậc (5%, 10%, 15%, 20%, 25%, 30%, 35%) theo Luật Thuế TNCN.
* **FR-08: Xuất Phiếu lương Điện tử Bảo mật & Gửi Email Tự động (Payslip Generation)**
  - *Mô tả:* Sau khi Bảng lương được Kế toán trưởng và Ban Giám đốc ký duyệt trên phần mềm, hệ thống tự động sinh phiếu lương cá nhân (Payslip) dưới dạng tệp tin PDF.
  - *Bảo mật:* File PDF được bảo vệ bằng mật khẩu mở file (mặc định là 6 chữ số cuối của số CCCD nhân viên). Hệ thống gửi phiếu lương tự động vào hòm thư cá nhân của 100 nhân viên trong vòng 15 phút.

---

### Module 4: Quản lý Tuyển dụng & Tiếp nhận Nhân sự
* **FR-09: Quản lý Tin Tuyển dụng và Phễu Ứng viên (Recruitment Pipeline)**
  - *Mô tả:* Cho phép Trưởng các bộ phận tạo yêu cầu tuyển dụng (Job Requisition); phòng HR phê duyệt và đăng tuyển vị trí công việc.
  - *Quản lý ứng viên:* Lưu trữ hồ sơ ứng viên (CV, thông tin liên lạc), theo dõi trạng thái qua phễu tuyển dụng: Ứng tuyển $\rightarrow$ Phỏng vấn $\rightarrow$ Đạt yêu cầu $\rightarrow$ Gửi Offer Letter $\rightarrow$ Đã tiếp nhận. Tự động chuyển đổi ứng viên trúng tuyển thành nhân viên mới trong hệ thống.
* **FR-10: Quy trình Hội nhập Nhân sự Mới (Onboarding Checklist Workflow)**
  - *Mô tả:* Tự động kích hoạt quy trình Onboarding chuẩn hóa khi nhân viên mới bắt đầu ngày làm việc đầu tiên:
    - Giao việc tự động cho phòng IT: Cấp tài khoản email, cài đặt máy tính, cấp thẻ vào/ra.
    - Giao việc cho phòng Hành chính: Bố trí chỗ ngồi, phát văn phòng phẩm.
    - Giao việc cho phòng HR: Ký hợp đồng thử việc, hướng dẫn quy chế nội bộ.

---

### Module 5: Quản trị Hiệu suất & Đánh giá KPI
* **FR-11: Thiết lập & Đánh giá Mục tiêu KPI (Performance Evaluation)**
  - *Mô tả:* Cho phép thiết lập bảng tiêu chí KPI theo từng chức danh công việc với trọng số điểm tương ứng (tổng trọng số = 100%).
  - *Đánh giá định kỳ:* Định kỳ cuối mỗi Quý, hệ thống mở cổng đánh giá: Nhân viên tự chấm điểm $\rightarrow$ Quản lý trực tiếp chấm điểm $\rightarrow$ Tổng hợp điểm số và xếp loại theo 4 hạng: A (Xuất sắc, $\ge 90$ điểm), B (Tốt, 80–89 điểm), C (Đạt, 70–79 điểm), D (Cần cải thiện, $< 70$ điểm). Kết quả tự động chuyển sang làm căn cứ xét thưởng kỳ lương.

---

### Module 6: Dashboard Báo cáo Quản trị & Phân quyền Hệ thống
* **FR-12: Dashboard Nhân sự & Phân quyền Truy cập (Executive Dashboard & RBAC)**
  - *Mô tả:* Cung cấp Dashboard trực quan hóa dữ liệu nhân sự phục vụ Ban Giám đốc và HR Manager: Biểu đồ biến động nhân sự, tỷ lệ nghỉ việc, cơ cấu nhân sự theo trình độ/độ tuổi, thống kê chi phí quỹ lương và chi phí làm thêm giờ.
  - *Phân quyền người dùng (Role-Based Access Control - RBAC):* Hệ thống thiết lập 5 nhóm quyền nghiêm ngặt:
    1. **System Admin:** Quản trị cấu hình hệ thống, sao lưu CSDL, quản lý tài khoản người dùng.
    2. **HR Manager:** Toàn quyền trên các phân hệ nhân sự, xem toàn bộ lương, duyệt đơn cấp cao.
    3. **HR Staff:** Nhập liệu hồ sơ, theo dõi bảng công, tính dự thảo bảng lương.
    4. **Manager (Trưởng bộ phận):** Xem thông tin nhân viên trong bộ phận, duyệt đơn xin nghỉ phép/OT, đánh giá KPI nhân viên cấp dưới.
    5. **Employee (Nhân viên thông thường):** Chỉ xem hồ sơ cá nhân, xem bảng công cá nhân, nộp đơn trực tuyến, xem phiếu lương và tự đánh giá KPI.

---

## 3. ĐẶC TẢ CHI TIẾT 6 YÊU CẦU PHI CHỨC NĂNG (NON-FUNCTIONAL REQUIREMENTS)

| Mã NFR | Nhóm thuộc tính | Đặc tả chi tiết | Tiêu chuẩn đo lường / Kiểm chứng |
|:---:|---|---|---|
| **NFR-01** | **Hiệu năng (Performance)** | • Thời gian tải trang giao diện trung bình $\le 1,5$ giây trên kết nối mạng nội bộ; không vượt quá 2,5 giây khi truy cập ngoài internet.<br/>• Thời gian xử lý chốt công và tính toán bảng lương cho 100 nhân viên không vượt quá **30 giây**.<br/>• Hỗ trợ tối thiểu 50 người dùng tương tác đồng thời mà không bị suy giảm hiệu năng. | Kiểm thử tải bằng Apache JMeter với kịch bản 50 concurrent users truy cập đồng thời trong 15 phút. |
| **NFR-02** | **Bảo mật (Security)** | • 100% mật khẩu được băm một chiều bằng thuật toán an toàn **Bcrypt** (Salt rounds $\ge 10$).<br/>• Các trường dữ liệu nhạy cảm (mức lương, số tài khoản ngân hàng, số CCCD) phải được mã hóa ở mức cơ sở dữ liệu bằng thuật toán đối xứng **AES-256**.<br/>• Áp dụng xác thực hai yếu tố (**2FA**) qua OTP ứng dụng đối với tài khoản quản trị Admin và HR Manager.<br/>• Đáp ứng tiêu chuẩn an toàn ứng dụng web theo **OWASP Top 10** (chống hoàn toàn SQL Injection, XSS, CSRF). | Rà quét lỗ hổng bảo mật bằng công cụ OWASP ZAP; báo cáo không còn lỗ hổng mức Critical hoặc High. |
| **NFR-03** | **Độ khả dụng (Availability & Disaster Recovery)** | • Hệ thống cam kết thời gian hoạt động liên tục (Uptime) $\ge \mathbf{99,5\%}$ trong giờ hành chính (08h00 – 18h00 từ Thứ Hai đến Thứ Bảy).<br/>• Thực hiện sao lưu CSDL tự động hàng ngày (Daily Backup) vào lúc 02h00 sáng, lưu trữ luân phiên tại 2 vị trí độc lập.<br/>• Mục tiêu điểm phục hồi dữ liệu (**RPO**) $\le 24$ giờ; Mục tiêu thời gian phục hồi hệ thống (**RTO**) $\le 4$ giờ khi xảy ra thảm họa phần cứng. | Diễn tập khôi phục dữ liệu từ bản sao lưu; đo thời gian khôi phục thực tế trên môi trường Staging. |
| **NFR-04** | **Khả năng Mở rộng (Scalability)** | • Kiến trúc phần mềm phân tầng rõ rệt (Tách rời Frontend SPA và Backend REST API theo mô hình Microservices-ready).<br/>• Cơ sở dữ liệu và cấu trúc API cho phép mở rộng quy mô quản lý từ 100 nhân sự hiện tại lên đến **500 nhân sự** trong 3 năm tới mà không cần viết lại kiến trúc lõi của hệ thống. | Kiểm tra thiết kế kiến trúc và chỉ mục (Index) CSDL PostgreSQL. |
| **NFR-05** | **Khả năng Tương thích (Compatibility & Usability)** | • Giao diện tương thích hoàn hảo trên các trình duyệt web phổ biến: Google Chrome, Microsoft Edge, Mozilla Firefox, Apple Safari.<br/>• Thiết kế giao diện đáp ứng linh hoạt (**Responsive Web Design**) cho các thiết bị di động (màn hình từ 375px đến 1920px).<br/>• Đạt tiêu chuẩn trải nghiệm người dùng: Một nhân viên mới có thể hoàn tất việc nộp đơn xin nghỉ phép trong vòng 03 thao tác nhấp chuột. | Kiểm thử hiển thị chéo trình duyệt (Cross-browser testing) và đánh giá độ tiện dụng người dùng. |
| **NFR-06** | **Tuân thủ Pháp lý (Compliance)** | • Mọi thuật toán tính lương, bảo hiểm và thuế phải tuân thủ nghiêm ngặt theo **Bộ luật Lao động số 45/2019/QH14**, **Luật Bảo hiểm Xã hội số 58/2014/QH13**, **Nghị định 145/2020/NĐ-CP** và **Luật Thuế Thu nhập Cá nhân hiện hành**. | Kế toán trưởng và Văn phòng Luật sư tư vấn rà soát công thức tính toán và ký xác nhận tuân thủ. |

---

## 4. MA TRẬN TRUY VẾT NGUỒN GỐC YÊU CẦU (REQUIREMENTS TRACEABILITY MATRIX - RTM)

Ma trận RTM dưới đây bảo đảm tính liên kết hai chiều chặt chẽ giữa: Nhu cầu kinh doanh ban đầu (Business Need) $\longleftrightarrow$ Yêu cầu hệ thống (FR/NFR) $\longleftrightarrow$ Gói công việc phân rã (WBS) $\longleftrightarrow$ Kịch bản kiểm thử nghiệm thu (Test Case ID):

| Mã Nhu cầu (Business Need) | Mã Yêu cầu (SRS ID) | Tên chức năng / Thuộc tính | Gói công việc WBS | Kịch bản Kiểm thử Nghiệm thu (Test Case ID) |
|---|---|---|---|---|
| **PB-01** (Thủ công đơn từ) | **FR-01** | Quản lý Hồ sơ nhân sự | 1.4.1 (Module Profile) | TC-HR-001, TC-HR-002 |
| **PB-01** (Thủ công đơn từ) | **FR-04** | Quản lý Đơn từ & Duyệt phép trực tuyến | 1.4.2 (Module Chấm công) | TC-ATT-003, TC-ATT-004 |
| **PB-01** (Thủ công chấm công) | **FR-03** | Tích hợp máy quét vân tay | 1.4.2 (Module Chấm công) | TC-ATT-001, TC-ATT-002 |
| **PB-01** (Mất 15h/tuần đối soát) | **FR-05** | Tổng hợp Bảng công tháng | 1.4.2 (Module Chấm công) | TC-ATT-005, TC-ATT-006 |
| **PB-02** (Tính lương mất 3 ngày) | **FR-06** | Động cơ tính lương Gross-Net | 1.4.3 (Module Tính lương) | TC-PAY-001, TC-PAY-002 |
| **PB-03** (Sai lệch lương 5,2%) | **FR-07** | Tự động tính BHXH & Thuế TNCN | 1.4.3 (Module Tính lương) | TC-PAY-003, TC-PAY-004 |
| **PB-03** (Bảo mật phiếu lương) | **FR-08** | Xuất phiếu lương PDF gửi email | 1.4.3 (Module Tính lương) | TC-PAY-005, TC-PAY-006 |
| **PB-05** (Turnover cao 18%) | **FR-09** | Quản lý Tuyển dụng ứng viên | 1.4.4 (Module Tuyển dụng) | TC-REC-001, TC-REC-002 |
| **PB-05** (Thiếu onboarding) | **FR-10** | Quy trình Onboarding nhân sự mới | 1.4.4 (Module Tuyển dụng) | TC-REC-003, TC-REC-004 |
| **PB-05** (Thiếu đánh giá KPI) | **FR-11** | Quản trị mục tiêu và đánh giá KPI | 1.4.5 (Module KPI) | TC-KPI-001, TC-KPI-002 |
| **PB-06** (Thiếu báo cáo quản trị) | **FR-12** | Executive Dashboard & Phân quyền RBAC | 1.4.6 (Module Dashboard) | TC-SYS-001, TC-SYS-002 |
| **NFR-SEC** (Bảo mật dữ liệu) | **NFR-02** | Mã hóa AES-256, Bcrypt, 2FA Admin | 1.3.1 (Kiến trúc) & 1.4 | TC-SEC-001 đến TC-SEC-004 |
| **NFR-PERF** (Thời gian xử lý) | **NFR-01** | Tính lương 100 người $< 30$ giây | 1.5.3 (System Test) | TC-PERF-001, TC-PERF-002 |
| **NFR-COMP** (Pháp lý lao động) | **NFR-06** | Tuân thủ Luật Lao động 2019 | 1.5.4 (UAT) | TC-COMP-001, TC-COMP-002 |

---

## 5. KẾT LUẬN VÀ PHÊ DUYỆT TÀI LIỆU SRS

Tài liệu này xác lập ranh giới kỹ thuật chi tiết của phần mềm **ABC-HRM**. Mọi sự điều chỉnh chức năng sau thời điểm phê duyệt bắt buộc phải tuân theo Quy trình Kiểm soát Thay đổi Tích hợp (Integrated Change Control) qua Hội đồng CCB.

| Đại diện Bên Phân tích (Lead BA) | Đại diện Nhóm Kỹ thuật (Tech Lead) | Đại diện Đơn vị Chấp thuận (HR Head) |
|:---:|:---:|:---:|
| *(Đã ký)* | *(Đã ký)* | *(Đã ký)* |
| **[Họ và tên Học viên 2]** | **[Họ và tên Học viên 3]** | **Trần Thị B** |
