# KẾ HOẠCH KIỂM THỬ (TEST PLAN) VÀ BIÊN BẢN NGHIỆM THU CHẤP NHẬN (UAT SIGNOFF)
## Dự án: Xây dựng Hệ thống Quản trị Nhân sự Nội bộ (ABC-HRM)
### Mã tài liệu: BTL-QLDA-TECH-03 | Giai đoạn: Hồ sơ Kỹ thuật (Technical Specs)
### Tiêu chuẩn áp dụng: IEEE 829 Standard for Software Test Documentation | Học phần: QLDA CNTT Nâng cao (HVNH)

---

## 1. KHUNG TIẾP CẬN BẢN CHẤT: LÀM GÌ? TẠI SAO LÀM? LÀM THẾ NÀO?

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                   MÔ HÌNH ĐẢM BẢO CHẤT LƯỢNG VÀ KIỂM THỬ CHẤP NHẬN HỆ THỐNG                      │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. TẠI SAO LÀM? (WHY)                                                                           │
│    • Hệ thống ABC-HRM trực tiếp chi trả quyền lợi tài chính (tiền lương, thưởng, bảo hiểm) cho   │
│      100 cán bộ nhân viên. Một sai sót nhỏ trong công thức tính toán có thể làm sai lệch hàng chục│
│      triệu đồng, dẫn tới khiếu kiện lao động và đánh mất lòng tin vào ban lãnh đạo.             │
│    • Kiểm thử đa tầng và Kiểm thử Chấp nhận Người dùng (UAT) là rào chắn chất lượng cuối cùng   │
│      bảo đảm phần mềm vận hành không tì vết trước khi đưa vào khai thác chính thức.             │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 2. LÀM GÌ? (WHAT)                                                                                │
│    • Thiết lập Chiến lược Kiểm thử 4 cấp độ: Kiểm thử Đơn vị (Unit Test), Kiểm thử Tích hợp      │
│      (Integration Test), Kiểm thử Tải/Hiệu năng (Load Test) và Kiểm thử Chấp nhận (UAT).        │
│    • Xây dựng Bộ 50 Kịch bản Kiểm thử Nghiệm thu (UAT Test Cases) bao phủ trọn vẹn 6 phân hệ.    │
│    • Thực hiện UAT thực tế với Khối HR, Kế toán và ký Biên bản Nghiệm thu Chấp thuận (Sign-off). │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 3. LÀM THẾ NÀO? (HOW)                                                                           │
│    • Áp dụng mô hình chữ V (V-Model): Đối chiếu trực tiếp từng Test Case với các yêu cầu FR/NFR. │
│    • Sử dụng công cụ tự động hóa: Jest (Unit Test), Supertest (API), Apache JMeter (Load Test).  │
│    • Tiêu chí nghiệm thu nghiêm ngặt: 100% Test Case đạt, 0 lỗi Critical, 0 lỗi Major.          │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. CHIẾN LƯỢC KIỂM THỬ 4 CẤP ĐỘ (TESTING LEVELS)

```
       Yêu cầu Nghiệp vụ (Business Needs) ◄────────────────► Kiểm thử Chấp nhận (UAT)
                      ▲                                              │
                      │                                              ▼
          Đặc tả Yêu cầu SRS (FR & NFR) ◄──────────────────► Kiểm thử Hệ thống & Tải (System Test)
                      ▲                                              │
                      │                                              ▼
          Thiết kế Kiến trúc (Architecture) ◄──────────────► Kiểm thử Tích hợp (Integration Test)
                      ▲                                              │
                      │                                              ▼
          Thiết kế Chi tiết (Component Design) ◄───────────► Kiểm thử Đơn vị (Unit Test)
```

1. **Kiểm thử Đơn vị (Unit Testing):**
   - Công cụ: Thư viện **Jest** (Backend) và **Vitest + React Testing Library** (Frontend).
   - Mục tiêu: Kiểm tra độc lập từng hàm tính toán logic thuế TNCN, tính lương OT, kiểm tra định dạng CCCD/Email.
   - Tiêu chuẩn bao phủ mã nguồn: Đạt **$\ge 80\%$** toàn dự án; riêng Module Tính lương đạt **$\ge 85\%$**.
2. **Kiểm thử Tích hợp (Integration Testing):**
   - Công cụ: **Supertest** giả lập gọi API RESTful.
   - Mục tiêu: Kiểm tra luồng dữ liệu liên thông: Quét vân tay $\rightarrow$ Cập nhật Bảng công $\rightarrow$ Động cơ Tính lương lấy dữ liệu công để tính Net.
3. **Kiểm thử Hiệu năng & Tải (Load & Performance Testing):**
   - Công cụ: **Apache JMeter 5.6**.
   - Kịch bản thử nghiệm: Giả lập 50 người dùng đồng thời (Concurrent Users) truy cập xem phiếu lương và nộp đơn nghỉ phép trong 15 phút.
   - Tiêu chuẩn nghiệm thu: Thời gian phản hồi trung bình $< 1,5$ giây; tỷ lệ lỗi HTTP 5xx bằng $0,0\%$.
4. **Kiểm thử Chấp nhận Người dùng (User Acceptance Testing - UAT):**
   - Do trực tiếp Trưởng phòng HR (Bà Trần Thị B), 3 chuyên viên HR và Kế toán tiền lương thao tác trên môi trường Staging.
   - Bao gồm 50 kịch bản thử nghiệm nghiệp vụ; đánh giá tính tiện dụng và độ chính xác của giao diện người dùng.

---

## 3. BẢNG TRÍCH LƯỢC CÁC KỊCH BẢN KIỂM THỬ UAT TIÊU BIỂU (UAT TEST CASES)

Bộ kịch bản UAT bao gồm 50 kịch bản bao phủ trọn vẹn 12 Yêu cầu Chức năng (FR-01 đến FR-12). Bảng dưới đây trích lược các kịch bản kiểm thử trọng yếu:

| Mã Test Case | Phân hệ Chức năng | Tên Kịch bản Kiểm thử | Điều kiện Tiền đề | Các Bước Thực hiện Thử nghiệm | Kết quả Kỳ vọng (Expected Result) | Kết quả Thực tế | Trạng thái (Status) |
|:---:|---|---|---|---|---|:---:|:---:|
| **TC-HR-001** | Hồ sơ Nhân sự | Tạo mới hồ sơ nhân viên hợp lệ | Đăng nhập tài khoản HR Manager | 1. Vào menu "Hồ sơ" $\rightarrow$ Bấm "Thêm mới"<br/>2. Nhập đầy đủ họ tên, CCCD, ngày sinh, lương<br/>3. Bấm "Lưu hồ sơ" | Hệ thống tạo thành công mã `ABC-0101`, lưu CSDL và mã hóa cột lương AES-256. | Đúng kỳ vọng, sinh mã tự động | ✅ **PASS** |
| **TC-HR-002** | Hồ sơ & Hợp đồng | Cảnh báo tự động hợp đồng hết hạn 30 ngày (CR-001) | Có 1 HĐ lao động hết hạn vào ngày 25/04/2026 | 1. Đặt ngày hệ thống là 26/03/2026<br/>2. Kích hoạt Cronjob quét hợp đồng<br/>3. Kiểm tra hòm thư HR Manager | Nhận được email cảnh báo danh sách nhân viên sắp hết hạn kèm nút bấm "Tạo phụ lục". | Nhận email sau 2 phút | ✅ **PASS** |
| **TC-ATT-001**| Chấm công | Quét vân tay thực tế trên máy ZKTeco | Máy chấm công kết nối mạng nội bộ | 1. Nhân viên quét vân tay trên máy<br/>2. Mở màn hình "Bảng công hôm nay" trên Web | Log chấm công hiển thị trên Web trong vòng không quá 05 giây với đúng mã nhân viên. | Hiển thị sau 2,8 giây | ✅ **PASS** |
| **TC-ATT-004**| Quản lý Đơn từ | Nộp và duyệt đơn xin nghỉ phép 2 cấp | Nhân viên còn 10 ngày phép năm | 1. Nhân viên tạo đơn xin nghỉ 1 ngày phép<br/>2. Manager bấm "Duyệt đơn"<br/>3. HR Manager bấm "Phê duyệt cuối" | Trạng thái đơn chuyển "Đã duyệt"; Quỹ phép năm của nhân viên tự động giảm còn 9 ngày. | Trừ quỹ phép chính xác | ✅ **PASS** |
| **TC-PAY-001**| Tính lương | Tính tự động bảng lương cho nhân viên đủ công | Đã chốt bảng công tháng 22 công chuẩn | 1. Vào phân hệ "Tính lương"<br/>2. Chọn kỳ lương Tháng 03/2026<br/>3. Bấm "Chạy tính lương tự động" | Tính đúng 100% lương cơ bản, lương OT, các khoản trừ bảo hiểm (10,5%) và thuế TNCN. | Khớp bảng tính tay kế toán | ✅ **PASS** |
| **TC-PAY-003**| Tính lương | Tính thuế TNCN có người phụ thuộc sinh giữa năm | Nhân viên có 1 con đăng ký giảm trừ từ tháng 06/2025 | 1. Chạy bảng lương Tháng 03/2026<br/>2. Kiểm tra cột Giảm trừ người phụ thuộc | Giảm trừ đúng 4.400.000 VNĐ vào thu nhập tính thuế trước khi áp biểu thuế lũy tiến 7 bậc. | Tính đúng giảm trừ 4,4 tr | ✅ **PASS** |
| **TC-PAY-005**| Phiếu lương | Xuất phiếu lương PDF có mật khẩu mã hóa | Bảng lương đã được phê duyệt | 1. Bấm nút "Xuất & Gửi phiếu lương"<br/>2. Tải file PDF từ email nhân viên<br/>3. Nhập mật khẩu là 6 số cuối CCCD | File PDF chỉ mở được khi nhập đúng 6 số cuối CCCD; bố cục phiếu lương chuẩn đẹp. | Mở file bảo mật thành công | ✅ **PASS** |
| **TC-REC-001**| Tuyển dụng | Chuyển ứng viên trúng tuyển thành nhân viên | Ứng viên ở trạng thái "Đã nhận Offer" | 1. Bấm nút "Tiếp nhận nhân sự mới"<br/>2. Xác nhận ngày bắt đầu đi làm | Ứng viên tự động được chuyển sang bảng `employees`, tạo tài khoản và kích hoạt Onboarding. | Chuyển dữ liệu tự động | ✅ **PASS** |
| **TC-KPI-001**| Quản trị KPI | Đánh giá KPI quý và tự động xếp loại | Đã hoàn thành nhập điểm 360 độ | 1. Trưởng phòng chấm điểm 88 điểm<br/>2. Bấm "Khóa đánh giá kỳ" | Điểm tổng hợp đạt 88/100 $\rightarrow$ Hệ thống tự động xếp loại hạng **B (Tốt)**. | Xếp hạng B chính xác | ✅ **PASS** |
| **TC-SYS-001**| Bảo mật & RBAC | Kiểm tra phân quyền truy cập chéo | Đăng nhập tài khoản nhân viên thông thường | 1. Nhân viên gõ đường dẫn URL `/payroll/admin`<br/>2. Cố tình truy cập bảng lương người khác | Hệ thống chặn truy cập, trả về lỗi HTTP 403 Forbidden; ghi log cảnh báo an ninh. | Bị chặn truy cập 100% | ✅ **PASS** |

---

## 4. BẢNG TỔNG KẾT KẾT QUẢ KIỂM THỬ UAT (TEST EXECUTION SUMMARY)

* **Tổng số kịch bản kiểm thử (Total Test Cases):** **50 kịch bản**.
* **Số kịch bản Đạt (Passed):** **50 kịch bản (100%)**.
* **Số kịch bản Không Đạt (Failed):** **0 kịch bản (0%)**.
* **Tổng số lỗi phát hiện trong đợt UAT:** 03 lỗi (đã ghi nhận trong Issue Log và được khắc phục triệt để):
  - *Lỗi mức Critical (Nghiêm trọng):* 0 lỗi.
  - *Lỗi mức Major (Nặng):* 0 lỗi.
  - *Lỗi mức Minor (Giao diện, hiển thị):* 03 lỗi (Đã sửa xong và kiểm thử hồi quy Pass 100%).

---

## 5. BIÊN BẢN NGHIỆM THU CHẤP THUẬN KỸ THUẬT (UAT SIGNOFF CERTIFICATE)

Căn cứ vào kết quả kiểm thử thực tế trên môi trường Staging từ ngày **25/10/2025 đến ngày 03/11/2025**, Hội đồng Nghiệm thu Kỹ thuật thống nhất xác nhận:
1. Hệ thống ABC-HRM đáp ứng đầy đủ và chính xác toàn bộ 12 Yêu cầu Chức năng (FR) và 6 Yêu cầu Phi chức năng (NFR) theo đúng bản đặc tả SRS đã cam kết.
2. Động cơ tính lương và các quy tắc giảm trừ thuế TNCN, bảo hiểm xã hội đã được đối chiếu kiểm tra thực chứng với số liệu kế toán thực tế, bảo đảm độ chính xác đạt $100\%$.
3. Hệ thống đủ điều kiện chất lượng kỹ thuật để triển khai đưa lên môi trường máy chủ sản xuất (Production) phục vụ cắt chuyển vận hành Go-Live toàn công ty.

*Hà Nội, ngày 03 tháng 11 năm 2025*

| ĐẠI DIỆN ĐẢM BẢO CHẤT LƯỢNG (QA LEAD) | ĐẠI DIỆN NHÓM PHÁT TRIỂN (TECH LEAD) |
|:---:|:---:|
| *(Ký và ghi rõ họ tên)* | *(Ký và ghi rõ họ tên)* |
| <br/><br/><br/>**[Họ và tên Học viên 5]**<br/>Kỹ sư Trưởng Đảm bảo Chất lượng | <br/><br/><br/>**[Họ và tên Học viên 3]**<br/>Kỹ sư Phần mềm Cao cấp |
| **ĐẠI DIỆN PHÂN TÍCH NGHIỆP VỤ (LEAD BA)** | **ĐẠI DIỆN ĐƠN VỊ NGHIỆM THU (HR HEAD)** |
| *(Ký và ghi rõ họ tên)* | *(Ký và ghi rõ họ tên)* |
| <br/><br/><br/>**[Họ và tên Học viên 2]**<br/>Chuyên viên Phân tích Nghiệp vụ | <br/><br/><br/>**Trần Thị B**<br/>Trưởng phòng Quản trị Nhân sự |
