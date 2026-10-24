# KẾ HOẠCH TRIỂN KHAI BÀI TẬP LỚN — DỰ ÁN HRM NỘI BỘ

## Dự án: Phát triển Hệ thống Quản lý Nhân sự (HRM) nội bộ cho Công ty ABC (100 nhân sự)

> Tài liệu này là **bản kế hoạch tổng thể** để triển khai BTL môn QLDA CNTT NC, ánh xạ (mapping) từng yêu cầu trong đề bài sang các sản phẩm bàn giao (deliverables) cụ thể cho dự án HRM.

---

## I. TỔNG QUAN DỰ ÁN

| Hạng mục | Chi tiết |
|---|---|
| **Tên dự án** | ABC-HRM: Hệ thống Quản lý Nhân sự Nội bộ |
| **Khách hàng** | Công ty Cổ phần ABC — ngành dịch vụ/công nghệ, 100 nhân sự |
| **Vấn đề hiện tại** | Quản lý nhân sự bằng Excel + giấy → sai sót chấm công, chậm tính lương, khó truy xuất hồ sơ, không có dashboard nhân sự cho Ban Giám đốc |
| **Giải pháp** | Xây dựng ứng dụng web HRM nội bộ (SaaS on-premise hoặc Cloud) |
| **Phương pháp luận** | Hybrid (Waterfall cho tài liệu QLDA + Agile/Scrum cho phát triển phần mềm) |
| **Thời gian dự kiến** | 6 tháng (24 tuần), từ 01/11/2025 → 30/04/2026 |
| **Ngân sách sơ bộ** | 850.000.000 VNĐ (≈ 850 triệu) |
| **Nhóm thực hiện** | 5 thành viên (theo yêu cầu BTL) |

### Các Module chính của hệ thống HRM:
1. **Quản lý Hồ sơ Nhân sự** — CRUD thông tin cá nhân, hợp đồng, bảo hiểm
2. **Chấm công & Quản lý Nghỉ phép** — tích hợp thiết bị chấm công, duyệt đơn online
3. **Tính lương & Phúc lợi** — công thức lương, BHXH/BHYT/TNCN tự động
4. **Tuyển dụng & Onboarding** — quy trình tuyển dụng, checklist onboarding
5. **Đánh giá Hiệu suất (KPI)** — thiết lập KPI, đánh giá 360°, báo cáo hiệu suất
6. **Dashboard & Báo cáo** — biểu đồ thống kê cho HR Manager và Ban Giám đốc

---

## II. ÁNH XẠ YÊU CẦU BTL → SẢN PHẨM BÀN GIAO

### A. GIAI ĐOẠN KHỞI TẠO (INITIATING) — Tuần 1–3

| # | Yêu cầu BTL | Sản phẩm bàn giao | Ghi chú |
|---|---|---|---|
| A1 | Nghiên cứu Khởi đầu & Xác nhận Giá trị | **Business Case + Phân tích tài chính** | Tính NPV, ROI, Payback Period |
| A2 | Hiến chương Dự án (Project Charter) | **Project Charter** | Dùng template từ giảng viên, mục tiêu SMART |
| A3 | Stakeholder Register | **Nhật ký Bên liên quan** | Liệt kê ≥ 10 stakeholders |
| A4 | Power/Interest Grid | **Ma trận Quyền lực/Quan tâm** | 4 góc phần tư + chiến lược quản lý |

#### A1. Business Case — Phân tích Tài chính Sơ bộ

**Nhu cầu kinh doanh (Business Needs):**
- Công ty ABC có 100 nhân sự, HR team gồm 3 người đang quản lý bằng Excel → mất ~15h/tuần cho chấm công thủ công, ~2 ngày/tháng tính lương, sai sót trung bình 5%/tháng.
- Ban GĐ không có dữ liệu nhân sự real-time để ra quyết định.
- Tỷ lệ nghỉ việc năm trước: 18% — thiếu công cụ đánh giá & giữ chân nhân sự.

**Phân tích tài chính:**

| Chỉ số | Công thức & Giá trị |
|---|---|
| **Tổng đầu tư (Year 0)** | 850.000.000 VNĐ |
| **Lợi ích hàng năm** | Giảm 1 FTE HR (180 tr/năm) + Giảm sai sót lương (50 tr/năm) + Giảm turnover (120 tr/năm) = **350 tr/năm** |
| **Discount Rate** | 10% |
| **NPV (5 năm)** | -850 + 350/1.1 + 350/1.21 + 350/1.331 + 350/1.4641 + 350/1.6105 ≈ **+477 triệu VNĐ** |
| **ROI (5 năm)** | (1.750 - 850) / 850 × 100% ≈ **105,9%** |
| **Payback Period** | 850 / 350 ≈ **2,43 năm** (≈ 2 năm 5 tháng) |

→ **Kết luận:** Dự án có NPV dương, ROI > 100%, hoàn vốn dưới 3 năm → đáng đầu tư.

#### A2. Project Charter — Tóm tắt Nội dung Cốt lõi

| Mục | Nội dung |
|---|---|
| **Mục tiêu SMART** | Hoàn thành hệ thống HRM có ≥ 6 module, phục vụ 100 user, go-live trước 30/04/2026, ngân sách ≤ 850 tr |
| **Phạm vi sơ bộ** | 6 module chính (Hồ sơ, Chấm công, Lương, Tuyển dụng, KPI, Dashboard) |
| **Milestones** | Xong thiết kế: T1/2026, Xong phát triển: T3/2026, UAT: T4/2026, Go-live: 30/04/2026 |
| **Ngân sách** | 850 tr VNĐ (từ quỹ chuyển đổi số nội bộ) |
| **Rủi ro cao** | Tích hợp máy chấm công, di chuyển dữ liệu từ Excel, thay đổi yêu cầu từ HR |
| **Tiêu chí thành công** | ≥ 90% user active sau 1 tháng, sai sót lương < 0,5%, thời gian tính lương giảm 70% |
| **PM** | [Tên thành viên nhóm] — toàn quyền điều phối nguồn lực |
| **Sponsor** | Giám đốc Công ty ABC |

#### A3. Stakeholder Register

| # | Tên/Vai trò | Phòng ban | Quan tâm | Ảnh hưởng | Chiến lược |
|---|---|---|---|---|---|
| 1 | Giám đốc (Sponsor) | Ban GĐ | Cao | Cao | **Manage Closely** — Báo cáo hàng tuần, phê duyệt milestones |
| 2 | Trưởng phòng HR | Nhân sự | Cao | Cao | **Manage Closely** — Tham gia review requirements hàng Sprint |
| 3 | Nhân viên HR (3 người) | Nhân sự | Cao | Trung bình | **Keep Informed** — Demo mỗi Sprint, thu thập feedback |
| 4 | Trưởng phòng Kế toán | Tài chính | Trung bình | Cao | **Keep Satisfied** — Xác nhận tích hợp module lương ↔ kế toán |
| 5 | Kế toán trưởng | Tài chính | Trung bình | Trung bình | **Keep Informed** — Thông báo khi module lương hoàn thành |
| 6 | Toàn bộ nhân viên (100 người) | All | Trung bình | Thấp | **Keep Informed** — Email thông báo, hướng dẫn sử dụng |
| 7 | Trưởng phòng IT | CNTT | Cao | Trung bình | **Keep Informed** — Phối hợp hạ tầng, bảo mật |
| 8 | Nhân viên IT (2 người) | CNTT | Trung bình | Thấp | **Monitor** — Hỗ trợ triển khai, vận hành |
| 9 | Nhà cung cấp máy chấm công | Bên ngoài | Thấp | Trung bình | **Keep Satisfied** — Cung cấp API/SDK tích hợp |
| 10 | Luật sư/Tư vấn pháp lý | Bên ngoài | Thấp | Thấp | **Monitor** — Đảm bảo tuân thủ Luật lao động, BHXH |

#### A4. Power/Interest Grid

```
         Quyền lực (Power)
              CAO
     ┌────────────┬────────────┐
     │  KEEP      │  MANAGE    │
     │  SATISFIED │  CLOSELY   │
     │            │            │
     │  TP Kế toán│  GĐ (Spon) │
     │            │  TP HR      │
     ├────────────┼────────────┤
     │  MONITOR   │  KEEP      │
     │            │  INFORMED  │
     │            │            │
     │  Luật sư   │  NV HR     │
     │  NV IT     │  NV Cty    │
     │  NCC chấm  │  TP IT     │
     │  công      │  Kế toán   │
     └────────────┴────────────┘
      THẤP         CAO
              Quan tâm (Interest)
```

---

### B. GIAI ĐOẠN LẬP KẾ HOẠCH (PLANNING) — Tuần 3–8

| # | Yêu cầu BTL | Sản phẩm bàn giao |
|---|---|---|
| B1 | Scope Statement | **Tuyên bố Phạm vi Dự án** |
| B2 | Requirements Documentation | **Tài liệu Yêu cầu (FR + NFR)** |
| B3 | WBS (cấp 3–4) | **Cấu trúc Phân chia Công việc** |
| B4 | WBS Dictionary | **Từ điển WBS** |
| B5 | Network Diagram + PERT | **Sơ đồ Mạng + Ước tính 3 điểm** |
| B6 | Gantt Chart + CPM | **Biểu đồ Gantt + Đường găng** |
| B7 | Bottom-Up Cost + S-Curve | **Ước tính Chi phí + Đường cơ sở Chi phí** |
| B8 | RACI Matrix | **Ma trận Phân công Trách nhiệm** |
| B9 | Risk Register (≥ 10 rủi ro) | **Sổ đăng ký Rủi ro + Kế hoạch ứng phó** |

#### B1. Tuyên bố Phạm vi Dự án (Project Scope Statement)

**Phạm vi Sản phẩm (Product Scope):**
- Ứng dụng web responsive (React + Node.js/NestJS + PostgreSQL)
- 6 module: Hồ sơ NS, Chấm công, Lương, Tuyển dụng, KPI, Dashboard
- Phân quyền: Admin, HR Manager, HR Staff, Employee, Manager (cấp quản lý trực tiếp)
- Tích hợp API máy chấm công vân tay hiện có
- Export báo cáo PDF/Excel

**Phạm vi Dự án (Project Scope):**
- Phân tích yêu cầu, Thiết kế UI/UX, Thiết kế CSDL, Phát triển, Kiểm thử, Đào tạo, Triển khai, Bàn giao
- Bảo hành 3 tháng sau go-live

**Phạm vi Loại trừ (Exclusions):**
- ❌ KHÔNG tích hợp với hệ thống kế toán bên ngoài (SAP, MISA…)
- ❌ KHÔNG phát triển ứng dụng mobile native
- ❌ KHÔNG bao gồm module quản lý đào tạo (Training Management)
- ❌ KHÔNG hỗ trợ đa ngôn ngữ (chỉ Tiếng Việt)

**Tiêu chí Chấp nhận (Acceptance Criteria):**
- Tất cả 6 module hoạt động đúng chức năng theo SRS
- Tỷ lệ lỗi < 0,01% trong UAT (< 1 lỗi Critical/Major trên 10.000 test cases)
- Thời gian phản hồi trang < 2 giây
- 100% nhân viên HR có thể sử dụng sau đào tạo (đánh giá qua bài kiểm tra)

#### B2. Tài liệu Yêu cầu — Trích lược Chính

**Yêu cầu Chức năng (Functional Requirements):**

| ID | Module | Mô tả |
|---|---|---|
| FR-01 | Hồ sơ NS | CRUD thông tin nhân viên (họ tên, CMND/CCCD, hợp đồng, BHXH) |
| FR-02 | Hồ sơ NS | Upload và lưu trữ scan hợp đồng, bằng cấp (PDF/ảnh) |
| FR-03 | Chấm công | Nhận dữ liệu từ API máy chấm công vân tay theo thời gian thực |
| FR-04 | Chấm công | Nhân viên nộp đơn xin nghỉ phép online, quản lý trực tiếp duyệt |
| FR-05 | Chấm công | Tổng hợp bảng chấm công tháng tự động |
| FR-06 | Lương | Tính lương gross → net theo công thức cấu hình được |
| FR-07 | Lương | Tự động tính BHXH/BHYT/BHTN/TNCN theo quy định hiện hành |
| FR-08 | Lương | Xuất phiếu lương cá nhân (PDF), gửi email tự động |
| FR-09 | Tuyển dụng | Quản lý vị trí tuyển dụng, quy trình phỏng vấn, trạng thái ứng viên |
| FR-10 | KPI | Thiết lập KPI theo phòng ban/cá nhân, đánh giá theo kỳ |
| FR-11 | Dashboard | Biểu đồ tổng hợp: headcount, turnover rate, chi phí nhân sự, overtime |
| FR-12 | Hệ thống | Phân quyền RBAC (Role-Based Access Control) 5 vai trò |

**Yêu cầu Phi chức năng (Non-Functional Requirements):**

| ID | Loại | Mô tả |
|---|---|---|
| NFR-01 | Hiệu năng | Thời gian phản hồi trung bình < 2s, tính lương 100 nhân sự < 30s |
| NFR-02 | Bảo mật | Mã hóa dữ liệu nhạy cảm (AES-256), xác thực 2 lớp (2FA) cho Admin |
| NFR-03 | Khả dụng | Uptime ≥ 99,5% trong giờ làm việc (8h–18h, T2–T7) |
| NFR-04 | Khả mở rộng | Kiến trúc hỗ trợ scale lên 500 nhân sự mà không cần refactor |
| NFR-05 | Sao lưu | Backup tự động hàng ngày, khôi phục trong < 4 giờ (RPO: 24h, RTO: 4h) |
| NFR-06 | Tuân thủ | Tuân thủ Luật Lao động 2019, Luật BHXH 2014, Nghị định 145/2020/NĐ-CP |

#### B3. Cấu trúc Phân chia Công việc (WBS) — Cấp 4

```
1. HỆ THỐNG HRM ABC (Cấp 1 - Dự án)
│
├── 1.1 QUẢN LÝ DỰ ÁN (Cấp 2)
│   ├── 1.1.1 Khởi tạo
│   │   ├── 1.1.1.1 Nghiên cứu khả thi & Business Case
│   │   ├── 1.1.1.2 Xây dựng Project Charter
│   │   └── 1.1.1.3 Xác định Stakeholders
│   ├── 1.1.2 Lập kế hoạch
│   │   ├── 1.1.2.1 Lập Scope Statement & WBS
│   │   ├── 1.1.2.2 Lập lịch trình (Gantt + CPM)
│   │   ├── 1.1.2.3 Ước tính chi phí & ngân sách
│   │   ├── 1.1.2.4 Lập kế hoạch rủi ro
│   │   └── 1.1.2.5 Lập kế hoạch truyền thông
│   ├── 1.1.3 Giám sát & Kiểm soát
│   │   ├── 1.1.3.1 Theo dõi EVM (2 thời điểm)
│   │   ├── 1.1.3.2 Xử lý Change Requests
│   │   └── 1.1.3.3 Báo cáo tình trạng
│   └── 1.1.4 Đóng dự án
│       ├── 1.1.4.1 Lessons Learned
│       └── 1.1.4.2 Final Closure Report
│
├── 1.2 PHÂN TÍCH YÊU CẦU (Cấp 2)
│   ├── 1.2.1 Khảo sát hiện trạng
│   │   ├── 1.2.1.1 Phỏng vấn HR & Ban GĐ
│   │   └── 1.2.1.2 Thu thập biểu mẫu Excel hiện tại
│   ├── 1.2.2 Đặc tả yêu cầu (SRS)
│   │   ├── 1.2.2.1 Đặc tả FR (12 use cases)
│   │   └── 1.2.2.2 Đặc tả NFR (6 tiêu chí)
│   └── 1.2.3 Thiết kế Prototype UI
│       └── 1.2.3.1 Wireframe & Mockup 6 module
│
├── 1.3 THIẾT KẾ HỆ THỐNG (Cấp 2)
│   ├── 1.3.1 Thiết kế kiến trúc
│   │   ├── 1.3.1.1 Kiến trúc tổng thể (Architecture Diagram)
│   │   └── 1.3.1.2 Thiết kế API (RESTful endpoints)
│   ├── 1.3.2 Thiết kế CSDL
│   │   └── 1.3.2.1 ERD & Data Dictionary
│   └── 1.3.3 Thiết kế UI/UX
│       └── 1.3.3.1 Design System & High-fidelity Mockup
│
├── 1.4 PHÁT TRIỂN PHẦN MỀM (Cấp 2)
│   ├── 1.4.1 Module Hồ sơ Nhân sự
│   │   ├── 1.4.1.1 Backend API
│   │   └── 1.4.1.2 Frontend UI
│   ├── 1.4.2 Module Chấm công & Nghỉ phép
│   │   ├── 1.4.2.1 Backend API + Tích hợp máy chấm công
│   │   └── 1.4.2.2 Frontend UI
│   ├── 1.4.3 Module Tính lương & Phúc lợi
│   │   ├── 1.4.3.1 Backend API (engine tính lương)
│   │   └── 1.4.3.2 Frontend UI + Export phiếu lương
│   ├── 1.4.4 Module Tuyển dụng & Onboarding
│   │   ├── 1.4.4.1 Backend API
│   │   └── 1.4.4.2 Frontend UI
│   ├── 1.4.5 Module KPI & Đánh giá
│   │   ├── 1.4.5.1 Backend API
│   │   └── 1.4.5.2 Frontend UI
│   └── 1.4.6 Module Dashboard & Báo cáo
│       ├── 1.4.6.1 Backend API (aggregate queries)
│       └── 1.4.6.2 Frontend UI (charts & export)
│
├── 1.5 KIỂM THỬ (Cấp 2)
│   ├── 1.5.1 Kiểm thử Đơn vị (Unit Test)
│   ├── 1.5.2 Kiểm thử Tích hợp (Integration Test)
│   ├── 1.5.3 Kiểm thử Hệ thống (System Test)
│   └── 1.5.4 Kiểm thử Chấp nhận (UAT)
│
├── 1.6 TRIỂN KHAI & ĐÀO TẠO (Cấp 2)
│   ├── 1.6.1 Cài đặt môi trường Production
│   ├── 1.6.2 Di chuyển dữ liệu (Data Migration từ Excel)
│   ├── 1.6.3 Đào tạo người dùng
│   │   ├── 1.6.3.1 Đào tạo HR team (2 buổi)
│   │   └── 1.6.3.2 Hướng dẫn nhân viên (video + tài liệu)
│   └── 1.6.4 Go-live & Hỗ trợ song hành
│
└── 1.7 BÀN GIAO & BẢO HÀNH (Cấp 2)
    ├── 1.7.1 Bàn giao mã nguồn & tài liệu
    ├── 1.7.2 Bảo hành 3 tháng
    └── 1.7.3 Chuyển giao vận hành cho IT nội bộ
```

#### B4. Từ điển WBS — Trích mẫu 3 Work Package

| WBS ID | Tên | Mô tả | Deliverable | Người chịu TN | Thời lượng | Tiêu chí chấp nhận |
|---|---|---|---|---|---|---|
| 1.4.3.1 | Backend API Engine tính lương | Phát triển module tính lương gross→net, tự động tính BHXH/BHYT/TNCN theo công thức cấu hình được | API endpoints `/payroll/*` đã code & unit test | Dev Backend Senior | 15 ngày | Pass 100% unit test, tính đúng lương cho 5 kịch bản mẫu |
| 1.4.2.1 | Backend API + Tích hợp chấm công | Phát triển API nhận dữ liệu từ máy chấm công vân tay, xử lý nghỉ phép | API `/attendance/*` + SDK integration | Dev Backend + IT | 12 ngày | Đồng bộ dữ liệu chấm công real-time, latency < 5s |
| 1.6.2 | Di chuyển dữ liệu từ Excel | Viết script ETL chuyển đổi dữ liệu nhân sự từ file Excel hiện tại sang PostgreSQL | Script migration + Báo cáo kiểm tra dữ liệu | Dev + HR | 5 ngày | 100% records migrated, 0 data loss, HR xác nhận đúng |

#### B5. Ước tính Thời lượng PERT — Các hoạt động chính

| Hoạt động | O (ngày) | M (ngày) | P (ngày) | E = (O+4M+P)/6 | σ = (P-O)/6 |
|---|---|---|---|---|---|
| Khảo sát & Phân tích yêu cầu | 8 | 12 | 20 | **12,7** | 2,0 |
| Thiết kế Kiến trúc + CSDL | 5 | 8 | 14 | **8,5** | 1,5 |
| Thiết kế UI/UX (Mockup) | 5 | 7 | 12 | **7,5** | 1,2 |
| Dev Module Hồ sơ NS | 8 | 10 | 15 | **10,5** | 1,2 |
| Dev Module Chấm công | 10 | 14 | 22 | **14,7** | 2,0 |
| Dev Module Tính lương | 12 | 18 | 28 | **18,7** | 2,7 |
| Dev Module Tuyển dụng | 6 | 8 | 12 | **8,3** | 1,0 |
| Dev Module KPI | 8 | 10 | 16 | **10,7** | 1,3 |
| Dev Dashboard & Báo cáo | 6 | 8 | 14 | **8,7** | 1,3 |
| Kiểm thử tích hợp + hệ thống | 8 | 12 | 18 | **12,3** | 1,7 |
| UAT | 5 | 7 | 10 | **7,2** | 0,8 |
| Triển khai + Data Migration | 3 | 5 | 10 | **5,5** | 1,2 |
| Đào tạo | 3 | 5 | 7 | **5,0** | 0,7 |

#### B6. Đường Găng (Critical Path) — Xác định

```
Đường Găng dự kiến:

  Khảo sát      Thiết kế       Dev Module      Dev Module       Kiểm thử
  & Phân tích → Kiến trúc+DB → Chấm công  →   Tính lương   →  Tích hợp  → UAT → Triển khai
  (12,7 ngày)   (8,5 ngày)    (14,7 ngày)     (18,7 ngày)     (12,3 ngày)  (7,2)  (5,5)

  Tổng đường găng ≈ 79,6 ngày làm việc ≈ 16 tuần

  → Các hoạt động KHÔNG trên đường găng (có Float):
    • Dev Hồ sơ NS (Float ≈ 8 ngày) — song song với Dev Chấm công
    • Dev Tuyển dụng (Float ≈ 18 ngày) — song song với Dev Lương
    • Dev KPI (Float ≈ 14 ngày) — song song với Dev Lương
    • Thiết kế UI/UX (Float ≈ 1 ngày) — song song với Thiết kế Kiến trúc

  ⚠️ Module Chấm công và Tính lương nằm trên đường găng vì chúng có
  mối quan hệ FS (Finish-to-Start) — phải hoàn thành chấm công mới có
  dữ liệu để tính lương. Bất kỳ chậm trễ nào ở 2 module này đều trực
  tiếp làm chậm ngày go-live của toàn dự án.
```

#### B7. Ước tính Chi phí Bottom-Up

| WBS | Hạng mục | Chi tiết | Thành tiền (VNĐ) |
|---|---|---|---|
| 1.1 | Quản lý dự án | PM 6 tháng × 25 tr/tháng | 150.000.000 |
| 1.2 | Phân tích yêu cầu | BA 2 tháng × 20 tr/tháng | 40.000.000 |
| 1.3 | Thiết kế | UI/UX Designer 1,5 tháng × 22 tr | 33.000.000 |
| 1.4 | Phát triển | 2 Dev × 4 tháng × 25 tr/tháng | 200.000.000 |
| | | 1 Senior Dev × 4 tháng × 35 tr | 140.000.000 |
| 1.5 | Kiểm thử | 1 QA × 2,5 tháng × 18 tr | 45.000.000 |
| 1.6 | Triển khai & Đào tạo | Nhân công + tài liệu | 22.000.000 |
| | Hạ tầng Cloud/Server | 6 tháng × 8 tr/tháng | 48.000.000 |
| | Giấy phép & Công cụ | (GitHub, Jira, Figma, CI/CD) | 20.000.000 |
| | Phần cứng (SDK chấm công) | License tích hợp API | 12.000.000 |
| | **Tổng ước tính** | | **710.000.000** |
| | **Dự trữ Dự phòng (15%)** | Cho rủi ro đã biết | **106.500.000** |
| | **Cost Baseline** | | **816.500.000** |
| | **Dự trữ Quản lý (~4%)** | Cho rủi ro chưa biết | **33.500.000** |
| | **TỔNG NGÂN SÁCH (BAC)** | | **850.000.000** |

#### B8. Ma trận RACI

| Gói công việc \ Vai trò | PM | BA | Sr Dev | Dev 1 | Dev 2 | QA |
|---|---|---|---|---|---|---|
| Business Case & Charter | A/R | C | I | I | I | I |
| Thu thập yêu cầu | A | R | C | I | I | I |
| Thiết kế Kiến trúc | A | C | R | C | C | I |
| Thiết kế UI/UX | A | C | C | R | I | I |
| Dev Module Hồ sơ NS | A | I | C | R | I | I |
| Dev Module Chấm công | A | I | R | C | I | I |
| Dev Module Tính lương | A | C | R | I | C | I |
| Dev Module Tuyển dụng | A | I | C | I | R | I |
| Dev Module KPI | A | I | C | R | I | I |
| Dev Dashboard | A | I | C | I | R | I |
| Kiểm thử (Unit/Integration) | A | I | C | C | C | R |
| UAT | A | R | I | I | I | C |
| Data Migration | A | C | R | C | I | I |
| Đào tạo người dùng | A | R | I | I | I | I |
| Triển khai Go-live | A | I | R | C | C | C |

*(R = Responsible, A = Accountable, C = Consulted, I = Informed)*

**Thách thức QLNNL đặc thù CNTT:**
- Senior Dev là nguồn lực then chốt (Key Resource) — nếu nghỉ việc → dự án bị ảnh hưởng nghiêm trọng → backup plan: Dev 1 knowledge transfer
- Động lực nội tại: Cho phép team tự chọn công nghệ, code review peer-to-peer, hackathon nội bộ cuối Sprint

#### B9. Sổ Đăng ký Rủi ro (Risk Register) — 12 rủi ro

| # | Rủi ro | Loại | P | I | Score | Chiến lược ứng phó |
|---|---|---|---|---|---|---|
| R1 | Senior Dev nghỉ việc giữa dự án | Nhân sự | 2 | 5 | **10** | **Giảm thiểu**: Knowledge sharing hàng tuần, pair programming |
| R2 | Luật BHXH/TNCN sửa đổi ảnh hưởng engine lương | Pháp lý | 3 | 4 | **12** | **Giảm thiểu**: Thiết kế engine cấu hình rule-based, không hard-code |
| R3 | API máy chấm công không tương thích / thiếu docs | Kỹ thuật | 3 | 4 | **12** | **Tránh né**: PoC tích hợp ngay Sprint 1; fallback → nhập thủ công |
| R4 | Scope Creep — HR yêu cầu thêm module Đào tạo | Phạm vi | 4 | 3 | **12** | **Chuyển giao**: Đưa vào Phase 2, kiểm soát qua CCB |
| R5 | Dữ liệu Excel không nhất quán (trùng mã NV) | Dữ liệu | 4 | 3 | **12** | **Giảm thiểu**: Kiểm tra & làm sạch sớm (Tuần 4), HR validate |
| R6 | Nhân viên phản đối hệ thống mới | Tổ chức | 3 | 3 | **9** | **Giảm thiểu**: Pilot group 10 người trước go-live toàn bộ |
| R7 | Hiệu năng chậm khi tính lương 100 NS đồng loạt | Kỹ thuật | 2 | 4 | **8** | **Giảm thiểu**: Load testing Sprint 4, tối ưu query, caching |
| R8 | Lộ dữ liệu nhân sự nhạy cảm (lương, CMND) | Bảo mật | 2 | 5 | **10** | **Giảm thiểu**: AES-256, 2FA Admin, OWASP checklist, pentest |
| R9 | Thiếu phản hồi từ HR khi UAT | Truyền thông | 3 | 3 | **9** | **Giảm thiểu**: SLA phản hồi 2 ngày, lịch review cố định |
| R10 | Server/Cloud sự cố khi go-live | Hạ tầng | 2 | 4 | **8** | **Chuyển giao**: Cloud SLA 99,9%, server backup |
| R11 | *(Cơ hội)* HR hào hứng → mở rộng chi nhánh | Cơ hội | 3 | 3 | **9** | **Khai thác**: Thiết kế multi-tenant ngay từ đầu |
| R12 | *(Cơ hội)* Team nâng cao năng lực tech stack mới | Cơ hội | 4 | 2 | **8** | **Tăng cường**: Tech sharing, blog nội bộ |

---

### C. GIAI ĐOẠN THỰC HIỆN & GIÁM SÁT/KIỂM SOÁT — Tuần 8–22

#### C1. Giả định 2 Yêu cầu Thay đổi (Change Requests)

**CR-001: Thêm "Cảnh báo hợp đồng sắp hết hạn tự động"**

| Mục | Nội dung |
|---|---|
| Ngày | 15/01/2026 (Sprint 3) |
| Người yêu cầu | Trưởng phòng HR |
| Mô tả | Hệ thống tự cảnh báo hợp đồng hết hạn trước 30 ngày + tạo draft gia hạn |
| Tác động | Phạm vi: +1 tính năng. Thời gian: +3 ngày. Chi phí: +5,5 tr |
| Quyết định CCB | ✅ **PHÊ DUYỆT** — Giá trị cao, tác động nhỏ. Cập nhật baseline |

**CR-002: Thêm module "Quản lý Đào tạo nội bộ"**

| Mục | Nội dung |
|---|---|
| Ngày | 10/02/2026 (Sprint 5) |
| Người yêu cầu | Giám đốc (Sponsor) |
| Mô tả | Quản lý khóa đào tạo, đăng ký, theo dõi tiến độ học |
| Tác động | +1 module mới. Thời gian: +20 ngày. Chi phí: +85 tr. Vượt ngân sách và deadline |
| Quyết định CCB | ❌ **TỪ CHỐI** — Đưa vào Phase 2 sau go-live |

**Change Log:**

| CR ID | Ngày | Mô tả | Trạng thái | Tác động PMB |
|---|---|---|---|---|
| CR-001 | 15/01/2026 | Cảnh báo HĐ hết hạn | Approved | +3 ngày, +5,5 tr |
| CR-002 | 10/02/2026 | Module Đào tạo | Rejected → Phase 2 | Không thay đổi |

#### C2. Quản lý Giá trị Thu được (EVM)

**BAC sau CR-001 = 822.000.000 VNĐ**

**Thời điểm 1: 15/10 (Tuần 14/24 — kế hoạch 58%)**

| Chỉ số | Giá trị | Ý nghĩa |
|---|---|---|
| **PV** | 476.760.000 | 58% × 822 tr |
| **EV** | 452.100.000 | 55% hoàn thành × 822 tr |
| **AC** | 470.000.000 | Chi thực tế |
| **CV** = EV − AC | **−17.900.000** | ⚠️ Vượt chi 17,9 tr |
| **SV** = EV − PV | **−24.660.000** | ⚠️ Chậm tiến độ ~3% |
| **CPI** = EV/AC | **0,962** | Mỗi 1đ chi ra → 0,962đ giá trị |
| **SPI** = EV/PV | **0,948** | Tiến độ 94,8% so kế hoạch |
| **EAC** = BAC/CPI | **854.470.000** | Dự báo tổng chi phí cuối |

→ **Nhận xét**: Chậm nhẹ do API máy chấm công (R3 hiện thực hóa). **Hành động**: Senior Dev tham gia trực tiếp module Chấm công.

**Thời điểm 2: 20/10 (Tuần 18/24 — kế hoạch 75%)**

| Chỉ số | Giá trị | Ý nghĩa |
|---|---|---|
| **PV** | 616.500.000 | 75% × 822 tr |
| **EV** | 608.280.000 | 74% hoàn thành × 822 tr |
| **AC** | 612.000.000 | Chi thực tế |
| **CV** = EV − AC | **−3.720.000** | Gần như on-budget |
| **SV** = EV − PV | **−8.220.000** | Chậm nhẹ ~1% |
| **CPI** = EV/AC | **0,994** | ≈ 1,0 → phục hồi |
| **SPI** = EV/PV | **0,987** | ≈ 1,0 → phục hồi |
| **EAC** = BAC/CPI | **826.960.000** | Trong ngân sách ✅ |

→ **Nhận xét**: Sau hành động điều chỉnh, CPI và SPI tiến gần 1,0. EAC ≈ 827 tr < BAC + Management Reserve → hoàn thành trong ngân sách.

#### C3. Báo cáo Tình trạng — Traffic Light

**Thời điểm 15/10:**

| Lĩnh vực | Trạng thái | Ghi chú |
|---|---|---|
| Phạm vi | 🟢 Xanh | Đúng phạm vi, CR-002 từ chối |
| Thời gian | 🟡 Vàng | SPI = 0,948 — chậm 3% |
| Chi phí | 🟡 Vàng | CPI = 0,962 — vượt nhẹ |

**Thời điểm 20/10:**

| Lĩnh vực | Trạng thái | Ghi chú |
|---|---|---|
| Phạm vi | 🟢 Xanh | Ổn định |
| Thời gian | 🟢 Xanh | SPI = 0,987 — phục hồi |
| Chi phí | 🟢 Xanh | CPI = 0,994 — on-budget |

**Issue Log:**

| # | Ngày | Mô tả | Mức độ | Người xử lý | Trạng thái |
|---|---|---|---|---|---|
| ISS-001 | 08/01/2026 | API chấm công thiếu docs endpoint đồng bộ lịch sử | Cao | Sr Dev + NCC | ✅ Đã giải quyết 18/01 |
| ISS-002 | 20/01/2026 | Dữ liệu Excel có 12 bản ghi trùng mã NV | Trung bình | BA + HR | ✅ Đã giải quyết 23/01 |
| ISS-003 | 15/02/2026 | Phiếu lương tính sai thuế TNCN cho NV có phụ thuộc | Cao | Sr Dev | 🔄 Đang xử lý |

---

### D. GIAI ĐOẠN KẾT THÚC (CLOSING) — Tuần 22–24

#### D1. Bài học Kinh nghiệm (Lessons Learned)

**Tri thức Hữu hình (Explicit Knowledge):**

| Lĩnh vực | Bài học | Hành động cho dự án sau |
|---|---|---|
| Ước tính | Module Tính lương bị thiếu 20% effort do độ phức tạp thuế TNCN | Buffer ≥ 25% cho module tài chính/pháp lý |
| Tích hợp | API chấm công thiếu docs → mất 5 ngày reverse-engineer | PoC tích hợp API bên ngoài trong Sprint 0 |
| Chất lượng | Code review bắt 15 lỗi logic tính lương trước UAT | PR bắt buộc ≥ 1 reviewer; module tài chính = 2 reviewer |
| Rủi ro | R5 xảy ra nhưng giảm thiểu nhờ kiểm tra sớm | Luôn validate dữ liệu nguồn trong Phase Phân tích |

**Tri thức Vô hình (Tacit Knowledge):**

| Bài học | Mô tả |
|---|---|
| Stakeholder | TP HR ban đầu ngại thay đổi → sau demo Sprint 2 trở thành supporter. **Insight**: Cho thấy sản phẩm sớm = giảm resistance |
| Động lực team | Dev 2 (junior) tăng 40% năng suất khi được giao ownership module Tuyển dụng. **Insight**: Autonomy > giám sát chặt |
| Giao tiếp | Daily standup 15 phút phát hiện blocker sớm hơn 2-3 ngày so với báo cáo tuần |

#### D2. Final Closure Report — Tóm tắt

| Mục | Kế hoạch | Kết quả thực tế | Đánh giá |
|---|---|---|---|
| Thời gian | 24 tuần (30/04/2026) | 24,5 tuần (04/05/2026) | 🟢 Chấp nhận (+2 ngày do CR-001) |
| Ngân sách | 850 tr VNĐ | 827 tr VNĐ | 🟢 Dưới 2,7% |
| Phạm vi | 6 module, 12 FR | 6 module, 13 FR (+CR-001) | 🟢 Đạt 100% + bonus |
| Chất lượng | Lỗi < 0,01% UAT | 0 Critical, 2 Minor (đã fix) | 🟢 Đạt |
| User Adoption | ≥ 90% active | 95% active | 🟢 Vượt mục tiêu |

**Chuyển giao:** ✅ Mã nguồn (Git) → IT | ✅ Ops Manual → IT | ✅ User Guide → HR | ✅ API docs (Swagger) → IT | ✅ Formal Acceptance ký bởi GĐ ngày 04/05/2026

**Giải tán nhóm:** PM → Phase 2 | Sr Dev → Tech Advisor 3 tháng bảo hành | Dev 1,2 + QA released | BA hỗ trợ training 2 tuần

**Thanh lý:** IP → thuộc ABC | GitHub/Jira → IT quản lý | Cloud subscription → IT tiếp quản

---

## III. CHECKLIST SẢN PHẨM BÀN GIAO BTL (20 deliverables)

| # | Tài liệu | Giai đoạn | Trạng thái |
|---|---|---|---|
| 1 | Business Case (NPV, ROI, Payback) | A | 📋 Cần soạn chi tiết |
| 2 | Project Charter | A | 📋 Dùng template |
| 3 | Stakeholder Register (10 bên) | A | ✅ Dữ liệu sẵn |
| 4 | Power/Interest Grid | A | ✅ Dữ liệu sẵn |
| 5 | Scope Statement + Exclusions | B | ✅ Dữ liệu sẵn |
| 6 | Requirements (12 FR + 6 NFR) | B | ✅ Dữ liệu sẵn |
| 7 | WBS cấp 4 | B | ✅ Dữ liệu sẵn |
| 8 | WBS Dictionary (mẫu 3 WP) | B | ✅ Dữ liệu sẵn |
| 9 | Network Diagram | B | 📋 Cần vẽ (Draw.io) |
| 10 | PERT Estimates (13 hoạt động) | B | ✅ Dữ liệu sẵn |
| 11 | Gantt Chart + Critical Path | B | 📋 Cần vẽ (MS Project) |
| 12 | Bottom-Up Cost + S-Curve | B | ✅ Dữ liệu sẵn |
| 13 | RACI Matrix | B | ✅ Dữ liệu sẵn |
| 14 | Risk Register (12 rủi ro) | B | ✅ Dữ liệu sẵn |
| 15 | Change Log (2 CRs) + CCB | C | ✅ Dữ liệu sẵn |
| 16 | EVM (2 thời điểm) | C | ✅ Dữ liệu sẵn |
| 17 | Status Report (Traffic Light) | C | ✅ Dữ liệu sẵn |
| 18 | Issue Log (3 issues) | C | ✅ Dữ liệu sẵn |
| 19 | Lessons Learned (Explicit+Tacit) | D | ✅ Dữ liệu sẵn |
| 20 | Final Closure Report | D | ✅ Dữ liệu sẵn |

---

## IV. PHÂN CÔNG NHÓM 5 THÀNH VIÊN

| TV | Vai trò BTL | Phụ trách chính |
|---|---|---|
| TV1 | PM / Team Lead | Charter, RACI, EVM, Status Reports, Closure Report |
| TV2 | BA / Scope Lead | Business Case, Scope Statement, Requirements, WBS, WBS Dictionary |
| TV3 | Schedule & Cost Lead | PERT, Network Diagram, Gantt, CPM, Bottom-Up Cost, S-Curve |
| TV4 | Risk & Change Lead | Stakeholder Register, Power/Interest Grid, Risk Register, Change Log, Issue Log |
| TV5 | Quality & Closing | Coding Standards, Test Plan, Lessons Learned, tài liệu kỹ thuật |

> Tất cả thành viên review chéo. Họp nhóm ≥ 1 lần/tuần (60 phút).
