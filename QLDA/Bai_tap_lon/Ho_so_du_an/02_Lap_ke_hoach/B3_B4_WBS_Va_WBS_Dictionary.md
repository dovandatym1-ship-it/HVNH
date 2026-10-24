# CẤU TRÚC PHÂN CHIA CÔNG VIỆC (WBS) VÀ TỪ ĐIỂN WBS (WBS DICTIONARY)
## Dự án: Xây dựng Hệ thống Quản trị Nhân sự Nội bộ (ABC-HRM)
### Mã tài liệu: BTL-QLDA-B3-B4 | Giai đoạn: Lập kế hoạch (Planning)
### Tiêu chuẩn áp dụng: PMI PMBOK Guide / WBS Practice Standard | Học phần: QLDA CNTT Nâng cao (HVNH)

---

## 1. NGUYÊN TẮC THIẾT LẬP CẤU TRÚC PHÂN CHIA CÔNG VIỆC (WBS)

Cấu trúc Phân chia Công việc (Work Breakdown Structure - WBS) là sự phân rã có thứ bậc, **định hướng theo sản phẩm bàn giao (Deliverable-oriented)** của toàn bộ phạm vi công việc mà nhóm dự án phải thực thi để hoàn thành các mục tiêu dự án.

WBS của dự án **ABC-HRM** được thiết kế tuân thủ nghiêm ngặt các nguyên tắc chuẩn mực quốc tế của PMI:
1. **Quy tắc 100% (The 100% Rule):** Tổng hợp công việc của các phần tử con ở mỗi cấp bắt buộc phải bao quát đúng 100% công việc của phần tử cha, không thừa và không thiếu.
2. **Không trùng lặp phạm vi (Mutually Exclusive):** Mỗi phần tử WBS đại diện cho một phạm vi công việc độc lập, không bị chồng chéo trách nhiệm giữa các gói công việc.
3. **Phân rã đến Cấp độ 4 (Work Package Level):** Mọi nhánh công việc được phân rã sâu đến cấp Gói công việc (Work Package - WP), tại đó thời lượng, chi phí, tài nguyên và người chịu trách nhiệm có thể được ước tính và kiểm soát một cách đáng tin cậy (nguyên tắc 8/80: một gói công việc có thời lượng không ngắn hơn 8 giờ và không dài quá 80 giờ làm việc của một cá nhân/nhóm).

---

## 2. BIỂU ĐỒ PHÂN RÃ WBS CẤP ĐỘ 4 (HỆ THỐNG ABC-HRM)

```
1.0 HỆ THỐNG QUẢN TRỊ NHÂN SỰ NỘI BỘ (ABC-HRM) [Cấp 1 - Toàn bộ Dự án]
│
├── 1.1 QUẢN LÝ DỰ ÁN (PROJECT MANAGEMENT) [Cấp 2]
│   ├── 1.1.1 Khởi tạo Dự án [Cấp 3]
│   │   ├── 1.1.1.1 Lập Business Case & Đánh giá Tài chính 5 năm
│   │   ├── 1.1.1.2 Xây dựng & Phê duyệt Hiến chương Dự án (Project Charter)
│   │   └── 1.1.1.3 Nhận diện Bên liên quan & Lập Ma trận Quyền lực/Quan tâm
│   ├── 1.1.2 Lập Kế hoạch Dự án [Cấp 3]
│   │   ├── 1.1.2.1 Lập Tuyên bố Phạm vi (Scope Statement) & Danh mục Loại trừ
│   │   ├── 1.1.2.2 Lập Cấu trúc WBS & Từ điển WBS
│   │   ├── 1.1.2.3 Lập Lịch trình (PERT, Sơ đồ mạng PDM, Đường Găng CPM, Gantt)
│   │   ├── 1.1.2.4 Lập Dự toán Chi phí Bottom-Up & Đường cơ sở Chi phí (S-Curve)
│   │   ├── 1.1.2.5 Lập Kế hoạch Nguồn nhân lực & Ma trận RACI
│   │   ├── 1.1.2.6 Lập Kế hoạch Quản lý Rủi ro & Bảng ứng phó 12 rủi ro
│   │   └── 1.1.2.7 Lập Kế hoạch Truyền thông & Báo cáo
│   ├── 1.1.3 Giám sát & Kiểm soát Dự án [Cấp 3]
│   │   ├── 1.1.3.1 Báo cáo Hiệu suất EVM tại 2 mốc (15/10 và 20/10)
│   │   ├── 1.1.3.2 Vận hành Hội đồng CCB & Xử lý 2 Yêu cầu Thay đổi (CR)
│   │   ├── 1.1.3.3 Báo cáo Tình trạng Đèn giao thông (Traffic Light Status Report)
│   │   └── 1.1.3.4 Theo dõi & Đóng Sổ theo dõi Vấn đề (Issue Log)
│   └── 1.1.4 Đóng Dự án [Cấp 3]
│       ├── 1.1.4.1 Họp Tổng kết Retrospective & Đóng gói Bài học Kinh nghiệm
│       ├── 1.1.4.2 Lập Báo cáo Đóng Dự án (Final Closure Report)
│       └── 1.1.4.3 Ký Biên bản Nghiệm thu Chính thức & Giải tán Đội ngũ
│
├── 1.2 KHẢO SÁT & PHÂN TÍCH NGHIỆP VỤ [Cấp 2]
│   ├── 1.2.1 Khảo sát Hiện trạng & Thu thập Dữ liệu [Cấp 3]
│   │   ├── 1.2.1.1 Phỏng vấn chuyên sâu Khối HR, Kế toán và Ban Giám đốc
│   │   ├── 1.2.1.2 Thu thập & Phân tích các biểu mẫu bảng tính Excel hiện hành
│   │   └── 1.2.1.3 Khảo sát thông số kỹ thuật máy quét vân tay ZKTeco
│   ├── 1.2.2 Xây dựng Tài liệu Đặc tả Yêu cầu (SRS) [Cấp 3]
│   │   ├── 1.2.2.1 Đặc tả 12 Yêu cầu Chức năng (FR-01 đến FR-12)
│   │   ├── 1.2.2.2 Đặc tả 6 Yêu cầu Phi chức năng (NFR-01 đến NFR-06)
│   │   └── 1.2.2.3 Lập Ma trận Truy vết Nguồn gốc Yêu cầu (RTM)
│   └── 1.2.3 Thiết kế Nguyên mẫu Giao diện (UI Prototyping) [Cấp 3]
│       ├── 1.2.3.1 Xây dựng Sơ đồ Luồng Người dùng (User Flow Diagrams)
│       └── 1.2.3.2 Thiết kế Wireframe khung sườn 6 phân hệ
│
├── 1.3 THIẾT KẾ KỸ THUẬT HỆ THỐNG [Cấp 2]
│   ├── 1.3.1 Thiết kế Kiến trúc Hệ thống [Cấp 3]
│   │   ├── 1.3.1.1 Xây dựng Mô hình Kiến trúc Phân tầng (3-tier Architecture)
│   │   ├── 1.3.1.2 Thiết kế Kiến trúc Bảo mật (JWT, RBAC, AES-256, Bcrypt, 2FA)
│   │   └── 1.3.1.3 Thiết kế Chuẩn giao tiếp RESTful API & Webhook Service
│   ├── 1.3.2 Thiết kế Cơ sở Dữ liệu [Cấp 3]
│   │   ├── 1.3.2.1 Xây dựng Mô hình Thực thể Quan hệ (ERD) chuẩn hóa 3NF
│   │   ├── 1.3.2.2 Lập Từ điển Dữ liệu (Data Dictionary) cho 9 bảng cốt lõi
│   │   └── 1.3.2.3 Thiết kế Chỉ mục (Index) và Chiến lược Partitioning
│   └── 1.3.3 Thiết kế Trải nghiệm Giao diện Chi tiết (UI/UX) [Cấp 3]
│       ├── 1.3.3.1 Xây dựng Design System & Bảng Mã màu / Typography
│       └── 1.3.3.2 Thiết kế Giao diện Độ phân giải cao (High-Fidelity Mockup) trên Figma
│
├── 1.4 PHÁT TRIỂN PHẦN MỀM (SOFTWARE DEVELOPMENT) [Cấp 2]
│   ├── 1.4.1 Phân hệ Quản lý Hồ sơ Nhân sự [Cấp 3]
│   │   ├── 1.4.1.1 Lập trình Backend API Quản lý Hồ sơ (CRUD)
│   │   ├── 1.4.1.2 Lập trình Backend API Hợp đồng số & Quét cảnh báo hết hạn
│   │   ├── 1.4.1.3 Lập trình Frontend UI Quản lý Hồ sơ & Hợp đồng
│   │   └── 1.4.1.4 Viết Unit Test Phân hệ Hồ sơ (Coverage $\ge 80\%$)
│   ├── 1.4.2 Phân hệ Chấm công & Quản lý Nghỉ phép [Cấp 3]
│   │   ├── 1.4.2.1 Phát triển Dịch vụ Adapter tích hợp SDK máy chấm công ZKTeco
│   │   ├── 1.4.2.2 Lập trình Backend API Quản lý Đơn từ & Duyệt Nghỉ phép/OT
│   │   ├── 1.4.2.3 Lập trình Thuật toán Tự động Tổng hợp Bảng công tháng
│   │   ├── 1.4.2.4 Lập trình Frontend UI Chấm công & Nộp đơn trực tuyến
│   │   └── 1.4.2.5 Viết Unit Test Phân hệ Chấm công (Coverage $\ge 80\%$)
│   ├── 1.4.3 Phân hệ Tính lương & Phúc lợi [Cấp 3]
│   │   ├── 1.4.3.1 Phát triển Động cơ Tính lương Gross-to-Net (Payroll Engine)
│   │   ├── 1.4.3.2 Phát triển Module Tính Khấu trừ BHXH & Thuế TNCN lũy tiến
│   │   ├── 1.4.3.3 Lập trình Chức năng Sinh Phiếu lương PDF bảo mật mật khẩu
│   │   ├── 1.4.3.4 Lập trình Dịch vụ Tự động gửi Email Phiếu lương hàng loạt
│   │   ├── 1.4.3.5 Lập trình Frontend UI Bảng tính lương & Phê duyệt chi trả
│   │   └── 1.4.3.6 Viết Unit Test Phân hệ Tính lương (Coverage $\ge 85\%$)
│   ├── 1.4.4 Phân hệ Tuyển dụng & Onboarding [Cấp 3]
│   │   ├── 1.4.4.1 Lập trình Backend API Quản lý Tin tuyển dụng & Phễu ứng viên
│   │   ├── 1.4.4.2 Lập trình Luồng Workflow Checklist Tiếp nhận Nhân sự mới
│   │   ├── 1.4.4.3 Lập trình Frontend UI Tuyển dụng & Onboarding
│   │   └── 1.4.4.4 Viết Unit Test Phân hệ Tuyển dụng (Coverage $\ge 80\%$)
│   ├── 1.4.5 Phân hệ Quản trị Hiệu suất KPI [Cấp 3]
│   │   ├── 1.4.5.1 Lập trình Backend API Thiết lập Mục tiêu & Đánh giá 360 độ
│   │   ├── 1.4.5.2 Lập trình Thuật toán Phân loại Xếp hạng A/B/C/D
│   │   ├── 1.4.5.3 Lập trình Frontend UI Đánh giá Hiệu suất cá nhân & phòng ban
│   │   └── 1.4.5.4 Viết Unit Test Phân hệ KPI (Coverage $\ge 80\%$)
│   └── 1.4.6 Phân hệ Báo cáo & Dashboard Quản trị [Cấp 3]
│       ├── 1.4.6.1 Lập trình Backend API Tổng hợp Số liệu Thống kê & Phân quyền RBAC
│       ├── 1.4.6.2 Lập trình Frontend UI Executive Dashboard & Biểu đồ phân tích
│       ├── 1.4.6.3 Lập trình Chức năng Kết xuất Báo cáo Định dạng Excel / PDF
│       └── 1.4.6.4 Viết Unit Test Phân hệ Dashboard (Coverage $\ge 80\%$)
│
├── 1.5 KIỂM THỬ CHẤT LƯỢNG (TESTING & QA) [Cấp 2]
│   ├── 1.5.1 Kiểm thử Đơn vị & Tích hợp (Unit & Integration Test) [Cấp 3]
│   │   ├── 1.5.1.1 Chạy & Đánh giá toàn bộ kiểm thử tích hợp giữa các phân hệ
│   │   └── 1.5.1.2 Kiểm tra tính toàn vẹn luồng dữ liệu (Data Flow Testing)
│   ├── 1.5.2 Kiểm thử Tải & Hiệu năng (Load & Performance Test) [Cấp 3]
│   │   ├── 1.5.2.1 Thực hiện Stress Test tính lương đồng thời 100 nhân sự
│   │   └── 1.5.2.2 Đo lường & Tối ưu hóa thời gian phản hồi giao diện ($< 2$s)
│   ├── 1.5.3 Kiểm thử An toàn Bảo mật (Security Pentest) [Cấp 3]
│   │   ├── 1.5.3.1 Rà quét lỗ hổng theo danh mục OWASP Top 10
│   │   └── 1.5.3.2 Kiểm tra cơ chế mã hóa AES-256 và bảo vệ mật khẩu
│   └── 1.5.4 Kiểm thử Nghiệm thu Người dùng Cuối (UAT) [Cấp 3]
│       ├── 1.5.4.1 Chuẩn bị Bộ dữ liệu Thử nghiệm và Kịch bản Nghiệm thu (50 Test Cases)
│       ├── 1.5.4.2 Tổ chức Đợt UAT với Phòng HR và Khối Kế toán
│       └── 1.5.4.3 Ký Biên bản Nghiệm thu UAT Chính thức (Sign-off)
│
├── 1.6 TRIỂN KHAI & CHUYỂN ĐỔI VẬN HÀNH [Cấp 2]
│   ├── 1.6.1 Thiết lập Môi trường Sản xuất (Production Setup) [Cấp 3]
│   │   ├── 1.6.1.1 Cấu hình Máy chủ Cloud VPS, Docker Compose, Nginx Reverse Proxy
│   │   ├── 1.6.1.2 Cài đặt Chứng chỉ Bảo mật SSL/TLS và Cấu hình Tường lửa (Firewall)
│   │   └── 1.6.1.3 Thiết lập Đường ống Tự động hóa CI/CD (GitHub Actions)
│   ├── 1.6.2 Di chuyển Dữ liệu Lịch sử (Data Migration) [Cấp 3]
│   │   ├── 1.6.2.1 Viết Script ETL trích xuất và làm sạch dữ liệu từ Excel cũ
│   │   ├── 1.6.2.2 Thực hiện Nạp dữ liệu vào PostgreSQL và Kiểm tra Đối soát
│   │   └── 1.6.2.3 Trưởng phòng HR ký Biên bản Xác nhận Dữ liệu Chuyển đổi
│   ├── 1.6.3 Đào tạo Người dùng Cuối (End-User Training) [Cấp 3]
│   │   ├── 1.6.3.1 Tổ chức 02 Buổi Đào tạo Chuyên sâu cho Khối HR & Kế toán
│   │   ├── 1.6.3.2 Tổ chức 01 Buổi Đào tạo Toàn diện & Phát hành Video hướng dẫn
│   │   └── 1.6.3.3 Đánh giá Kết quả Đào tạo (100% HR đạt yêu cầu thao tác)
│   └── 1.6.4 Cắt chuyển Vận hành Chính thức (Go-Live) [Cấp 3]
│       ├── 1.6.4.1 Kích hoạt Hệ thống Chính thức trên Production (30/04/2026)
│       └── 1.6.4.2 Vận hành Song hành (Parallel Run) & Hỗ trợ Sự cố Tuần đầu
│
└── 1.7 BÀN GIAO & KẾT THÚC DỰ ÁN [Cấp 2]
    ├── 1.7.1 Chuyển giao Sản phẩm Bàn giao [Cấp 3]
    │   ├── 1.7.1.1 Bàn giao Kho Lưu trữ Mã nguồn Git & Tài liệu Kỹ thuật
    │   ├── 1.7.1.2 Bàn giao Tài liệu Quản trị Vận hành (Ops Manual) & User Guide
    │   └── 1.7.1.3 Bàn giao Quyền Quản trị Hệ thống cho Trưởng phòng CNTT
    ├── 1.7.2 Dịch vụ Hỗ trợ Bảo hành [Cấp 3]
    │   ├── 1.7.2.1 Thiết lập Kênh Tiếp nhận Sự cố Bảo hành (SLA 4 giờ)
    │   └── 1.7.2.2 Thực hiện Bảo hành Kỹ thuật Miễn phí 03 tháng
    └── 1.7.3 Hoàn tất Pháp lý & Thanh lý Dự án [Cấp 3]
        ├── 1.7.3.1 Ký Biên bản Bàn giao & Nghiệm thu Tổng thể Dự án
        └── 1.7.3.2 Quyết toán Tài chính và Thanh lý Hợp đồng Dự án
```

---

## 3. TỪ ĐIỂN WBS (WBS DICTIONARY) CHO CÁC GÓI CÔNG VIỆC TRỌNG YẾU

Bảng Từ điển WBS dưới đây định nghĩa chi tiết trách nhiệm, nội dung kỹ thuật, tiêu chí nghiệm thu và nguồn lực của **các gói công việc nòng cốt (Work Packages)** thuộc Cấp 4:

| Mã WBS | Tên Gói Công việc | Mô tả Nội dung Kỹ thuật | Sản phẩm Bàn giao (Deliverable) | Vai trò Chịu TN (RACI) | Thời lượng Ước tính | Dự toán Chi phí (VNĐ) | Tiêu chí Chấp nhận Nghiệm thu |
|:---:|---|---|---|:---:|:---:|:---:|---|
| **1.1.1.2** | Phê duyệt Hiến chương Dự án | Soạn thảo mục tiêu SMART, ngân sách, phân quyền PM, lấy chữ ký phê duyệt của Sponsor. | Bản Project Charter có đủ chữ ký lãnh đạo. | **PM** *(Accountable)* | 5 ngày công | 6.250.000 | Sponsor phê duyệt không điều chỉnh; mục tiêu rõ ràng. |
| **1.2.2.1** | Đặc tả Yêu cầu Chức năng (FR) | Phỏng vấn, viết chi tiết 12 yêu cầu chức năng từ quản lý hồ sơ, chấm công, tính lương tới báo cáo. | Văn bản đặc tả FR trong tài liệu SRS chuẩn IEEE 830. | **BA** *(Responsible)* | 8 ngày công | 8.000.000 | Trưởng phòng HR và IT Lead ký xác nhận đầy đủ 12 FR. |
| **1.3.1.1** | Thiết kế Kiến trúc Hệ thống | Xây dựng sơ đồ kiến trúc 3 tầng (React / NestJS / PostgreSQL), luồng dữ liệu, API Gateway, bảo mật. | Bản vẽ Kiến trúc Kỹ thuật & Báo cáo thuyết minh. | **Senior Dev** *(Responsible)* | 6 ngày công | 10.500.000 | IT Lead thẩm định đạt chuẩn khả năng chịu tải và bảo mật. |
| **1.3.2.1** | Thiết kế CSDL Quan hệ (ERD) | Thiết kế lược đồ quan hệ 9 bảng dữ liệu, chuẩn hóa 3NF, ràng buộc khóa ngoại, định nghĩa chỉ mục Index. | Sơ đồ ERD & Tài liệu Từ điển CSDL chi tiết. | **Senior Dev** *(Responsible)* | 4 ngày công | 7.000.000 | 100% bảng đạt chuẩn 3NF, không có dư thừa dữ liệu bất hợp lý. |
| **1.4.2.1** | Phát triển Adapter SDK Chấm công | Viết dịch vụ nền (Background Service) kết nối socket với máy chấm công ZKTeco, nhận log đẩy về CSDL. | Module mã nguồn Adapter + Tài liệu hướng dẫn kết nối. | **Senior Dev** *(Responsible)* | 12 ngày công | 21.000.000 | Quét vân tay thực tế trên máy, log hiển thị trên web trong $< 5$ giây. |
| **1.4.3.1** | Phát triển Động cơ Tính lương | Lập trình engine tính lương Gross-to-Net, tích hợp bảng công, phụ cấp, thưởng, cấu hình công thức động. | Module mã nguồn Payroll Engine + Bộ Unit Test. | **Senior Dev** *(Responsible)* | 15 ngày công | 26.250.000 | Pass 100% test cases mẫu tính lương; sai số bằng 0%. |
| **1.4.3.2** | Module Khấu trừ Bảo hiểm & Thuế | Lập trình thuật toán tự động tính trần đóng BHXH/BHYT/BHTN và thuế TNCN lũy tiến 7 bậc. | Module mã nguồn Statutory Deductions logic. | **Dev 1** *(Responsible)* | 8 ngày công | 10.000.000 | Khớp tuyệt đối với bảng đối chiếu thuế của Kế toán trưởng. |
| **1.4.3.3** | Chức năng Xuất Phiếu lương PDF | Lập trình chức năng sinh file PDF phiếu lương tự động, đặt mật khẩu bảo vệ bằng 6 số cuối CCCD. | Dịch vụ sinh PDF & mã nguồn đính kèm mật khẩu. | **Dev 2** *(Responsible)* | 5 ngày công | 6.250.000 | File PDF mở được đúng mật khẩu; bố cục phiếu lương chuẩn hóa. |
| **1.5.2.1** | Stress Test Tính lương 100 Nhân sự | Giả lập dữ liệu bảng công của 100 nhân sự và kích hoạt lệnh tính lương đồng thời bằng JMeter. | Báo cáo Kết quả Kiểm thử Hiệu năng (Performance Report). | **QA** *(Responsible)* | 3 ngày công | 2.700.000 | Thời gian hoàn tất tính toán $< 30$ giây, CPU máy chủ $< 70\%$. |
| **1.5.4.2** | Tổ chức Đợt Kiểm thử UAT | Điều phối nhân viên phòng HR và Kế toán thao tác trên toàn bộ 50 kịch bản thử nghiệm nghiệp vụ. | Biên bản ghi nhận kết quả UAT & Danh sách lỗi (Defect Log). | **PM & BA** *(Responsible)* | 5 ngày công | 6.000.000 | 100% kịch bản UAT pass; không còn lỗi mức Critical/Major. |
| **1.6.2.1** | Viết Script ETL Di chuyển Dữ liệu | Viết mã nguồn Python/SQL làm sạch, chuẩn hóa và nạp toàn bộ hồ sơ từ 15 file Excel vào PostgreSQL. | Script ETL hoàn chỉnh & Báo cáo chuyển đổi dữ liệu. | **Senior Dev** *(Responsible)* | 5 ngày công | 8.750.000 | 100% hồ sơ 100 nhân viên nạp thành công, 0% bản ghi mất mát. |
| **1.6.3.1** | Đào tạo Chuyên sâu Khối HR | Biên soạn slide, tài liệu hướng dẫn và tổ chức 2 buổi đào tạo trực tiếp cho 3 chuyên viên HR. | Danh sách điểm danh & Bài kiểm tra đánh giá sau đào tạo. | **BA** *(Responsible)* | 2 ngày công | 2.000.000 | 100% nhân viên HR vượt qua bài kiểm tra thực hành $> 85$ điểm. |

---

## 4. KẾT LUẬN VỀ CẤU TRÚC WBS

Cấu trúc WBS 4 cấp độ và Từ điển WBS trên đây đã phân rã toàn diện mục tiêu của dự án **ABC-HRM** thành các gói công việc định lượng rõ ràng. Đây là cơ sở cốt tử để:
1. Xác định trình tự hoạt động và thiết lập Mô hình mạng lịch trình (PERT/CPM).
2. Tính toán tổng mức đầu tư theo phương pháp Từ dưới lên (Bottom-Up Cost Estimating).
3. Phân định rạch ròi trách nhiệm của 5 thành viên trong Ma trận RACI.
