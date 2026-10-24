# THIẾT KẾ CƠ SỞ DỮ LIỆU (DATABASE DESIGN) VÀ TỪ ĐIỂN DỮ LIỆU (DATA DICTIONARY)
## Dự án: Xây dựng Hệ thống Quản trị Nhân sự Nội bộ (ABC-HRM)
### Mã tài liệu: BTL-QLDA-TECH-02 | Giai đoạn: Hồ sơ Kỹ thuật (Technical Specs)
### Hệ quản trị CSDL: PostgreSQL 15 | Chuẩn hóa: 3NF | Học phần: QLDA CNTT Nâng cao (HVNH)

---

## 1. KHUNG TIẾP CẬN BẢN CHẤT: LÀM GÌ? TẠI SAO LÀM? LÀM THẾ NÀO?

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                   MÔ HÌNH THIẾT KẾ CƠ SỞ DỮ LIỆU QUAN HỆ CHUẨN HÓA 3NF                           │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. TẠI SAO LÀM? (WHY)                                                                           │
│    • Dữ liệu nhân sự và bảng lương là tài sản thông tin cốt lõi của doanh nghiệp. Nếu thiết kế   │
│      CSDL bị trùng lặp, thiếu ràng buộc toàn vẹn hoặc không chuẩn hóa, hệ thống sẽ gặp các dị    │
│      thường cập nhật (Update Anomalies), sai sót số tiền lương hoặc mất tính toàn vẹn lịch sử.   │
│    • Thiết kế chuẩn hóa 3NF (Third Normal Form) kết hợp mã hóa cột bảo đảm CSDL vừa an toàn,     │
│      vừa đạt tốc độ truy vấn cao nhất khi tính lương đồng thời cho toàn bộ nhân sự.             │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 2. LÀM GÌ? (WHAT)                                                                                │
│    • Xây dựng Sơ đồ Thực thể Quan hệ (ERD) hoàn chỉnh gồm 10 bảng dữ liệu cốt lõi.               │
│    • Thiết lập Từ điển Dữ liệu (Data Dictionary) chi tiết hóa từng trường thông tin, kiểu dữ     │
│      liệu, khóa chính (PK), khóa ngoại (FK) và quy tắc ràng buộc (Constraints).                 │
│    • Xác lập Chiến lược Đánh Chỉ mục (Indexing) tối ưu hóa truy vấn bảng công và bảng lương.    │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 3. LÀM THẾ NÀO? (HOW)                                                                           │
│    • Sử dụng hệ quản trị CSDL quan hệ PostgreSQL 15 với hỗ trợ chuẩn ACID đầy đủ.               │
│    • Áp dụng kỹ thuật mã hóa mức cột (Column-level Encryption) với thuật toán AES-256-GCM        │
│      cho các trường thông tin nhạy cảm (mức lương, số CCCD, tài khoản ngân hàng).               │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. SƠ ĐỒ THỰC THỂ QUAN HỆ (ENTITY-RELATIONSHIP DIAGRAM - ERD)

```
┌─────────────────┐       1:N       ┌─────────────────────┐       1:N       ┌─────────────────────┐
│      ROLES      ├────────────────►│        USERS        ├────────────────►│   USER_ACTIVITIES   │
│  (Phân quyền)   │                 │ (Tài khoản truy cập)│                 │ (Nhật ký truy cập)  │
└─────────────────┘                 └──────────┬──────────┘                 └─────────────────────┘
                                               │ 1:1
                                               ▼
┌─────────────────┐       1:N       ┌─────────────────────┐       1:N       ┌─────────────────────┐
│   DEPARTMENTS   ├────────────────►│      EMPLOYEES      ├────────────────►│      CONTRACTS      │
│   (Phòng ban)   │                 │  (Hồ sơ nhân viên)  │                 │ (Hợp đồng lao động) │
└─────────────────┘                 └────┬──────┬──────┬──┘                 └─────────────────────┘
                                         │      │      │
                      ┌──────────────────┘      │      └──────────────────┐
                  1:N │                     1:N │                     1:N │
                      ▼                         ▼                         ▼
           ┌─────────────────────┐   ┌─────────────────────┐   ┌─────────────────────┐
           │   ATTENDANCE_LOGS   │   │   LEAVE_REQUESTS    │   │   PAYROLL_RECORDS   │
           │ (Log quét vân tay)  │   │  (Đơn phép / OT)    │   │  (Bảng lương tháng) │
           └─────────────────────┘   └─────────────────────┘   └──────────┬──────────┘
                                                                          │ 1:N
                                                                          ▼
                                                               ┌─────────────────────┐
                                                               │     DEPENDENTS      │
                                                               │  (Người phụ thuộc)  │
                                                               └─────────────────────┘
```

---

## 3. TỪ ĐIỂN DỮ LIỆU CHI TIẾT (DATA DICTIONARY - 10 BẢNG CỐT LÕI)

### 3.1. Bảng `roles` (Nhóm Quyền Người Dùng)
Lưu trữ định nghĩa 5 vai trò truy cập trong hệ thống (RBAC).

| Tên Cột | Kiểu Dữ Liệu | Ràng Buộc | Ý Nghĩa / Mô Tả | Dữ Liệu Mẫu |
|---|---|:---:|---|---|
| `id` | `VARCHAR(36)` | PK, Not Null | Mã định danh duy nhất (UUID) | `'r-001'` |
| `role_name` | `VARCHAR(50)` | Not Null, Unique | Tên vai trò quản trị | `'HR_MANAGER'` |
| `description`| `VARCHAR(255)`| Nullable | Mô tả quyền hạn của vai trò | `'Toàn quyền quản trị nhân sự'` |
| `permissions`| `JSONB` | Not Null | Danh sách mã quyền chi tiết | `'["employee:all", "payroll:all"]'` |

---

### 3.2. Bảng `users` (Tài Khoản Đăng Nhập Hệ Thống)

| Tên Cột | Kiểu Dữ Liệu | Ràng Buộc | Ý Nghĩa / Mô Tả | Dữ Liệu Mẫu |
|---|---|:---:|---|---|
| `id` | `VARCHAR(36)` | PK, Not Null | Mã định danh người dùng (UUID) | `'u-001'` |
| `email` | `VARCHAR(100)`| Not Null, Unique | Email công ty đăng nhập | `'nguyenvana@abc.com.vn'` |
| `password_hash`| `VARCHAR(255)`| Not Null | Mật khẩu băm một chiều Bcrypt | `'$2b$12$e8...'` |
| `role_id` | `VARCHAR(36)` | FK $\rightarrow$ `roles.id` | Khóa ngoại trỏ tới vai trò | `'r-001'` |
| `is_2fa_enabled`| `BOOLEAN` | Default False | Trạng thái kích hoạt xác thực 2 bước| `true` |
| `two_factor_secret`| `VARCHAR(100)`| Nullable | Khóa bí mật TOTP tạo mã OTP | `'JBSWY3DPEHPK3PXP'` |
| `status` | `VARCHAR(20)` | Default 'ACTIVE' | Trạng thái tài khoản | `'ACTIVE'`, `'LOCKED'` |

---

### 3.3. Bảng `employees` (Hồ Sơ Nhân Sự Chi Tiết)
Lưu trữ thông tin định danh và hành chính của 100 cán bộ nhân viên công ty.

| Tên Cột | Kiểu Dữ Liệu | Ràng Buộc | Ý Nghĩa / Mô Tả | Dữ Liệu Mẫu |
|---|---|:---:|---|---|
| `id` | `VARCHAR(36)` | PK, Not Null | Khóa chính duy nhất (UUID) | `'emp-101'` |
| `staff_code` | `VARCHAR(20)` | Not Null, Unique | Mã nhân viên chuẩn hóa định dạng | `'ABC-0015'` |
| `full_name` | `VARCHAR(100)`| Not Null | Họ và tên đầy đủ | `'Trần Thị Thu Thảo'` |
| `date_of_birth`| `DATE` | Not Null | Ngày tháng năm sinh | `'1994-08-15'` |
| `gender` | `VARCHAR(10)` | Not Null | Giới tính | `'FEMALE'`, `'MALE'` |
| `id_card_encrypted`| `TEXT` | Not Null | **Số CCCD mã hóa AES-256** | `'enc:U2FsdGVkX1...'` |
| `tax_code` | `VARCHAR(20)` | Nullable, Unique | Mã số thuế cá nhân | `'8492019482'` |
| `social_insurance_no`| `VARCHAR(20)`| Nullable | Số sổ bảo hiểm xã hội | `'0119283746'` |
| `department_id`| `VARCHAR(36)` | FK $\rightarrow$ `departments.id` | Thuộc phòng ban nào | `'dept-hr'` |
| `position` | `VARCHAR(100)`| Not Null | Chức danh công việc | `'Chuyên viên Tuyển dụng'` |
| `base_salary_encrypted`| `TEXT` | Not Null | **Mức lương cơ bản thỏa thuận (AES-256)**| `'enc:k9d8s7df...'` (18 tr) |
| `bank_account_encrypted`| `TEXT` | Not Null | **Số TK ngân hàng chi trả lương (AES-256)**| `'enc:092384...'` |
| `join_date` | `DATE` | Not Null | Ngày bắt đầu làm việc tại công ty | `'2023-03-01'` |
| `status` | `VARCHAR(20)` | Default 'ACTIVE' | Tình trạng lao động | `'ACTIVE'`, `'PROBATION'`, `'LEFT'` |

---

### 3.4. Bảng `contracts` (Hợp Đồng Lao Động)

| Tên Cột | Kiểu Dữ Liệu | Ràng Buộc | Ý Nghĩa / Mô Tả | Dữ Liệu Mẫu |
|---|---|:---:|---|---|
| `id` | `VARCHAR(36)` | PK, Not Null | Khóa chính hợp đồng | `'ct-005'` |
| `employee_id` | `VARCHAR(36)` | FK $\rightarrow$ `employees.id` | Nhân viên ký hợp đồng | `'emp-101'` |
| `contract_number`| `VARCHAR(50)` | Not Null, Unique | Số hiệu hợp đồng lao động | `'015/2024/HĐLĐ-ABC'` |
| `contract_type`| `VARCHAR(30)` | Not Null | Loại hợp đồng | `'THU_VIEC'`, `'XAC_DINH_TH_1Y'` |
| `start_date` | `DATE` | Not Null | Ngày có hiệu lực | `'2024-03-01'` |
| `end_date` | `DATE` | Nullable | Ngày hết hạn hợp đồng | `'2025-02-28'` |
| `attachment_path`| `VARCHAR(255)`| Nullable | Đường dẫn lưu trữ file PDF scan | `'/uploads/contracts/015.pdf'` |
| `status` | `VARCHAR(20)` | Default 'ACTIVE' | Trạng thái hiệu lực | `'ACTIVE'`, `'EXPIRED'`, `'TERMINATED'` |

---

### 3.5. Bảng `attendance_logs` (Nhật Ký Quét Vân Tay Thực Tế)

| Tên Cột | Kiểu Dữ Liệu | Ràng Buộc | Ý Nghĩa / Mô Tả | Dữ Liệu Mẫu |
|---|---|:---:|---|---|
| `id` | `BIGSERIAL` | PK, Not Null | Khóa chính tăng tự động | `1004829` |
| `device_id` | `VARCHAR(50)` | Not Null | Mã định danh thiết bị ZKTeco | `'ZK-OFFICE-T1'` |
| `staff_code` | `VARCHAR(20)` | FK $\rightarrow$ `employees.staff_code` | Mã nhân viên quét vân tay | `'ABC-0015'` |
| `punch_time` | `TIMESTAMP` | Not Null | Thời điểm quét thực tế | `'2026-03-10 08:14:22'` |
| `verify_type`| `VARCHAR(20)` | Default 'FINGERPRINT' | Phương thức xác thực | `'FINGERPRINT'`, `'FACE_ID'` |
| `created_at` | `TIMESTAMP` | Default NOW() | Thời điểm hệ thống nhận bản ghi | `'2026-03-10 08:14:24'` |

---

### 3.6. Bảng `leave_requests` (Đơn Nghỉ Phép & Làm Ngoài Giờ OT)

| Tên Cột | Kiểu Dữ Liệu | Ràng Buộc | Ý Nghĩa / Mô Tả | Dữ Liệu Mẫu |
|---|---|:---:|---|---|
| `id` | `VARCHAR(36)` | PK, Not Null | Khóa chính đơn từ | `'req-209'` |
| `employee_id` | `VARCHAR(36)` | FK $\rightarrow$ `employees.id` | Người làm đơn | `'emp-101'` |
| `request_type`| `VARCHAR(30)` | Not Null | Loại đơn | `'PHEP_NAM'`, `'PHEP_OM'`, `'OT'` |
| `start_time` | `TIMESTAMP` | Not Null | Thời gian bắt đầu nghỉ/OT | `'2026-03-15 08:00:00'` |
| `end_time` | `TIMESTAMP` | Not Null | Thời gian kết thúc nghỉ/OT | `'2026-03-15 17:30:00'` |
| `duration_days`| `DECIMAL(4,2)`| Not Null | Tổng số ngày/giờ tính công | `1.00` |
| `reason` | `TEXT` | Not Null | Lý do làm đơn | `'Giải quyết việc gia đình'` |
| `manager_status`| `VARCHAR(20)`| Default 'PENDING' | Trạng thái duyệt của Manager | `'APPROVED'`, `'REJECTED'` |
| `hr_status` | `VARCHAR(20)` | Default 'PENDING' | Trạng thái duyệt của HR | `'APPROVED'`, `'REJECTED'` |

---

### 3.7. Bảng `payroll_records` (Bảng Lương Tháng Tổng Hợp)

| Tên Cột | Kiểu Dữ Liệu | Ràng Buộc | Ý Nghĩa / Mô Tả | Dữ Liệu Mẫu |
|---|---|:---:|---|---|
| `id` | `VARCHAR(36)` | PK, Not Null | Khóa chính bản ghi lương | `'pr-2026-03-015'` |
| `employee_id` | `VARCHAR(36)` | FK $\rightarrow$ `employees.id` | Nhân viên hưởng lương | `'emp-101'` |
| `month` | `INT` | Not Null | Tháng tính lương (1–12) | `3` |
| `year` | `INT` | Not Null | Năm tính lương | `2026` |
| `standard_days`| `DECIMAL(4,1)`| Not Null | Số ngày công chuẩn của tháng | `22.0` |
| `actual_days` | `DECIMAL(4,1)`| Not Null | Số ngày công đi làm thực tế | `21.5` |
| `paid_leave_days`| `DECIMAL(4,1)`| Default 0.0 | Số ngày phép hưởng nguyên lương | `0.5` |
| `ot_hours` | `DECIMAL(5,1)`| Default 0.0 | Tổng số giờ làm ngoài giờ OT | `12.0` |
| `gross_salary`| `DECIMAL(14,2)`| Not Null | **Tổng thu nhập Gross tính thuế** | `22.450.000.00` |
| `bhxh_deduction`| `DECIMAL(14,2)`| Not Null | Tiền BHXH trừ lương (8%) | `1.440.000.00` |
| `bhyt_deduction`| `DECIMAL(14,2)`| Not Null | Tiền BHYT trừ lương (1.5%) | `270.000.00` |
| `bhtn_deduction`| `DECIMAL(14,2)`| Not Null | Tiền BHTN trừ lương (1%) | `180.000.00` |
| `personal_tax`| `DECIMAL(14,2)`| Not Null | **Thuế Thu nhập Cá nhân (TNCN)** | `865.000.00` |
| `net_salary` | `DECIMAL(14,2)`| Not Null | **LƯƠNG THỰC NHẬN (NET)** | `19.695.000.00` |
| `payslip_pdf_path`| `VARCHAR(255)`| Nullable | File PDF phiếu lương có mật khẩu | `'/payslips/2026_03_015.pdf'` |
| `is_paid` | `BOOLEAN` | Default False | Trạng thái ngân hàng đã giải ngân | `true` |

---

### 3.8. Bảng `dependents` (Người Phụ Thuộc Giảm Trừ Thuế)

| Tên Cột | Kiểu Dữ Liệu | Ràng Buộc | Ý Nghĩa / Mô Tả | Dữ Liệu Mẫu |
|---|---|:---:|---|---|
| `id` | `VARCHAR(36)` | PK, Not Null | Khóa chính người phụ thuộc | `'dp-01'` |
| `employee_id` | `VARCHAR(36)` | FK $\rightarrow$ `employees.id` | Nhân viên nuôi dưỡng | `'emp-101'` |
| `full_name` | `VARCHAR(100)`| Not Null | Tên người phụ thuộc | `'Trần Gia Huy'` |
| `relationship` | `VARCHAR(50)` | Not Null | Mối quan hệ | `'CON_RUOT'`, `'BO_ME'` |
| `start_month` | `VARCHAR(7)` | Not Null | Bắt đầu áp dụng giảm trừ (YYYY-MM) | `'2025-06'` |
| `end_month` | `VARCHAR(7)` | Nullable | Kết thúc giảm trừ nếu có | `NULL` |

---

## 4. CHIẾN LƯỢC ĐÁNH CHỈ MỤC TỐI ƯU HÓA TRUY VẤN (INDEXING STRATEGY)

Để đáp ứng yêu cầu phi chức năng NFR-01 (Tính lương 100 người $< 30$ giây và tìm kiếm nhân sự $< 1,5$ giây), các chỉ mục chuyên dụng sau được thiết lập:

```sql
-- 1. Tối ưu hóa tra cứu mã nhân viên và email
CREATE UNIQUE INDEX idx_employees_staff_code ON employees (staff_code);
CREATE UNIQUE INDEX idx_users_email ON users (email);

-- 2. Tối ưu hóa truy vấn đối soát chấm công theo khoảng thời gian của từng nhân viên
CREATE INDEX idx_attendance_staff_time ON attendance_logs (staff_code, punch_time);

-- 3. Tối ưu hóa truy vấn bảng lương theo kỳ lương (Tháng / Năm)
CREATE UNIQUE INDEX idx_payroll_emp_month_year ON payroll_records (employee_id, month, year);

-- 4. Tối ưu hóa quét cảnh báo hợp đồng sắp hết hạn (Cronjob hàng ngày)
CREATE INDEX idx_contracts_end_date ON contracts (end_date) WHERE status = 'ACTIVE';
```

Thiết kế CSDL chuẩn hóa 3NF trên đây đảm bảo hệ thống ABC-HRM hoạt động toàn vẹn, bảo mật cao và vận hành với hiệu năng tối ưu nhất.
