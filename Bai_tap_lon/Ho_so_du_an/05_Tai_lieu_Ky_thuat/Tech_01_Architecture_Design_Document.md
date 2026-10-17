# TÀI LIỆU THIẾT KẾ KIẾN TRÚC HỆ THỐNG (SYSTEM ARCHITECTURE DESIGN)
## Dự án: Xây dựng Hệ thống Quản trị Nhân sự Nội bộ (ABC-HRM)
### Mã tài liệu: BTL-QLDA-TECH-01 | Giai đoạn: Hồ sơ Kỹ thuật (Technical Specs)
### Tiêu chuẩn áp dụng: ISO/IEC/IEEE 42010 Architecture Description | Học phần: QLDA CNTT Nâng cao (HVNH)

---

## 1. KHUNG TIẾP CẬN BẢN CHẤT: LÀM GÌ? TẠI SAO LÀM? LÀM THẾ NÀO?

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                   MÔ HÌNH THIẾT KẾ KIẾN TRÚC HỆ THỐNG PHẦN MỀM ABC-HRM                           │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. TẠI SAO LÀM? (WHY)                                                                           │
│    • Một hệ thống phần mềm quản lý nhân sự và tiền lương chứa đựng nhiều dữ liệu cực kỳ nhạy     │
│      cảm (mức thu nhập, thông tin định danh cá nhân) và có các tác vụ xử lý thời gian thực       │
│      (nhận log chấm công từ máy quét vân tay).                                                   │
│    • Nếu không có bản thiết kế kiến trúc chuẩn mực, hệ thống sẽ dễ bị tổn thương trước các cuộc │
│      tấn công an ninh mạng, khó bảo trì, nghẽn cổ chai khi tính lương hàng loạt và không thể mở  │
│      rộng khi doanh nghiệp tăng quy mô nhân sự lên 500 người.                                    │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 2. LÀM GÌ? (WHAT)                                                                                │
│    • Xây dựng Mô hình Kiến trúc Phân tầng 3 lớp (3-tier Architecture: Presentation, Application, │
│      Data Layer) tách biệt hoàn toàn giữa Frontend SPA và Backend RESTful API.                   │
│    • Thiết kế Cơ chế Tích hợp Phần cứng (Hardware Adapter) kết nối thiết bị vân tay ZKTeco.     │
│    • Thiết lập Kiến trúc An ninh Bảo mật Đa tầng (JWT, RBAC 5 vai trò, AES-256, 2FA, Bcrypt).    │
│    • Thiết kế Hạ tầng Triển khai Sản xuất (Docker Compose, Nginx Reverse Proxy, SSL, CI/CD).     │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 3. LÀM THẾ NÀO? (HOW)                                                                           │
│    • Lựa chọn Tech-stack hiện đại, ổn định: React 18, Node.js (NestJS Framework), PostgreSQL 15, │
│      Redis Caching, Docker container hóa toàn bộ ứng dụng.                                       │
│    • Tuân thủ nghiêm ngặt nguyên tắc SOLID, Clean Architecture và bộ tiêu chuẩn an toàn OWASP.   │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. LỰA CHỌN CÔNG NGHỆ VÀ LUẬN GIẢI KHOA HỌC (TECHNOLOGY STACK)

| Tầng Kiến trúc | Công nghệ Lựa chọn | Phiên bản | Luận giải Khoa học & Ưu thế Kỹ thuật |
|---|---|:---:|---|
| **Frontend (Client)** | **React.js + Vite + TailwindCSS** | React 18.x | Ứng dụng Single Page Application (SPA) cho tốc độ tải cực nhanh; Virtual DOM giúp hiển thị bảng công 100 nhân sự mượt mà không bị giật lag; TailwindCSS tạo giao diện hiện đại chuẩn Enterprise. |
| **Backend (Application)** | **Node.js (NestJS Framework)** | NestJS 10.x | Framework hướng đối tượng (OOP) xây dựng trên nền tảng TypeScript, cấu trúc Modular chặt chẽ theo mẫu kiến trúc Clean Architecture; cơ chế Dependency Injection giúp dễ dàng viết Unit Test độc lập. |
| **Cơ sở Dữ liệu (Database)** | **PostgreSQL** | PostgreSQL 15.x | Hệ quản trị CSDL quan hệ mã nguồn mở mạnh mẽ nhất hiện nay; hỗ trợ chuẩn ACID tuyệt đối, bảo đảm an toàn cho các giao dịch tài chính tính lương; hỗ trợ chỉ mục Index B-Tree và JSONB linh hoạt. |
| **Bộ nhớ Đệm (Caching)** | **Redis** | Redis 7.x | Lưu trữ In-Memory phục vụ lưu phiên đăng nhập (Session token), phân quyền người dùng và lưu tạm thời (Buffer) hàng nghìn bản ghi log chấm công trước khi ghi xuống đĩa cứng. |
| **Tích hợp Phần cứng** | **Node.js Socket Service** | TCP/IP Socket | Dịch vụ nền (Background Worker) duy trì kết nối Socket ổn định với máy quét vân tay ZKTeco, tự động nhận diện gói tin đẩy và đồng bộ dữ liệu vào hệ thống trong $< 5$ giây. |
| **Đóng gói & Hạ tầng** | **Docker & Docker Compose** | Docker 24.x | Container hóa toàn bộ môi trường; loại bỏ hoàn toàn lỗi "chạy được trên máy dev nhưng lỗi trên máy chủ"; triển khai tự động qua GitHub Actions CI/CD. |

---

## 3. BIỂU ĐỒ KIẾN TRÚC TỔNG THỂ HỆ THỐNG (SYSTEM ARCHITECTURE DIAGRAM)

```
                            [ NGƯỜI DÙNG CUỐI ]
                 (Trình duyệt Web Máy tính & Thiết bị Di động)
                                      │
                                      ▼ HTTPS (Port 443) / SSL TLS 1.3
                      ┌───────────────────────────────┐
                      │   NGINX REVERSE PROXY / WAF   │
                      │ (Rate Limiting, SSL Offloading│
                      │  CORS, Security Headers)      │
                      └───────────────┬───────────────┘
                                      │
            ┌─────────────────────────┴─────────────────────────┐
            │                                                   │
            ▼ Static Files                                      ▼ Proxy Pass /api/v1
┌───────────────────────┐                           ┌───────────────────────────────┐
│     FRONTEND SPA      │                           │      BACKEND RESTFUL API      │
│ (React 18 + Vite)     │                           │   (NestJS Application Server) │
│ • Module Hồ sơ Nhân sự│                           ├───────────────────────────────┤
│ • Module Chấm công/Đơn│◄──── JSON Payload ───────►│ • Auth Module (JWT, 2FA, RBAC)│
│ • Module Tính lương   │                           │ • Employee & Contract Service │
│ • Module Tuyển dụng   │                           │ • Attendance & Leave Service  │
│ • Module Quản trị KPI │                           │ • Payroll Calculation Engine  │
│ • Executive Dashboard │                           │ • Recruitment & KPI Service   │
└───────────────────────┘                           │ • Reporting & Export Worker   │
                                                    └───────┬───────────────┬───────┘
                                                            │               │
                            ┌───────────────────────────────┘               │
                            │                                               ▼ TCP/IP Socket
                            ▼ SQL Queries (TypeORM)                ┌─────────────────┐
┌────────────────────────────────────────────────────────┐         │ ZKTeco Adapter  │
│                DATA STORAGE LAYER                      │         │ Background Svc  │
│                                                        │         └────────┬────────┘
│  ┌───────────────────────┐   ┌──────────────────────┐  │                  │
│  │   PostgreSQL 15 DB    │   │     Redis 7 Cache    │  │                  ▼
│  │ • 9 Bảng dữ liệu 3NF  │   │ • User Sessions      │  │         ┌─────────────────┐
│  │ • Mã hóa cột AES-256  │   │ • Attendance Buffer  │  │         │ Máy quét vân tay│
│  │ • Daily Automated BKP │   │ • Rate Limit Counter │  │         │  ZKTeco K40 Pro │
│  └───────────────────────┘   └──────────────────────┘  │         └─────────────────┘
└────────────────────────────────────────────────────────┘
```

---

## 4. THIẾT KẾ KIẾN TRÚC AN NINH BẢO MẬT ĐA TẦNG (SECURITY ARCHITECTURE)

Hệ thống được thiết kế theo nguyên tắc "Bảo vệ theo chiều sâu" (Defense-in-Depth) với 4 lớp phòng thủ nghiêm ngặt:

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│ LỚP 1: BẢO MẬT HẠ TẦNG MẠNG (NETWORK SECURITY)                                                   │
│ • Bắt buộc mã hóa toàn bộ lưu lượng bằng giao thức HTTPS với chứng chỉ SSL/TLS 1.3.              │
│ • Cấu hình tường lửa Nginx giới hạn lưu lượng (Rate Limiting): Tối đa 100 requests/phút/IP để     │
│   ngăn chặn các cuộc tấn công từ chối dịch vụ (DDoS) và brute-force mật khẩu.                    │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ LỚP 2: XÁC THỰC VÀ PHÂN QUYỀN (AUTHENTICATION & RBAC)                                            │
│ • Cơ chế xác thực Token kép: Access Token (JWT thời hạn ngắn 15 phút) và Refresh Token (7 ngày).  │
│ • Phân quyền ma trận nghiêm ngặt theo 5 vai trò (RBAC): Admin, HR Manager, HR Staff, Manager,    │
│   Employee. Kiểm soát quyền ở mức từng API Endpoint thông qua NestJS Guards.                     │
│ • Bắt buộc xác thực 2 yếu tố (2FA TOTP qua Google Authenticator) đối với Admin và HR Manager.   │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ LỚP 3: MÃ HÓA CƠ SỞ DỮ LIỆU (DATA AT REST ENCRYPTION)                                            │
│ • Mật khẩu người dùng được băm một chiều bằng thuật toán Bcrypt với hệ số Salt Rounds = 12.      │
│ • Các trường dữ liệu tài chính và định danh cá nhân nhạy cảm (`base_salary`, `bank_account`,     │
│   `id_card_number`) được mã hóa đối xứng mức cột bằng thuật toán AES-256-GCM. Khóa bí mật        │
│   (Secret Key) được quản lý qua biến môi trường độc lập, không lưu trong mã nguồn Git.          │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ LỚP 4: PHÒNG CHỐNG CÁC LỖ HỔNG PHỔ BIẾN (OWASP TOP 10 MITIGATION)                               │
│ • Chống SQL Injection: Sử dụng 100% Parameterized Queries thông qua TypeORM.                     │
│ • Chống XSS (Cross-Site Scripting): React tự động escape HTML; tích hợp thư viện DOMPurify.      │
│ • Chống CSRF: Sử dụng cấu hình SameSite Cookie và kiểm tra Origin Header.                        │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 5. THIẾT KẾ HẠ TẦNG VẬN HÀNH VÀ ĐƯỜNG ỐNG CI/CD (DEVOPS & DEPLOYMENT)

Hệ thống được đóng gói hoàn toàn trong các container Docker độc lập và tự động hóa triển khai qua GitHub Actions:

```
[ Developer Push Code ] ──► [ GitHub Repository ]
                                    │
                                    ▼ Triggers GitHub Actions CI Pipeline
                            ┌───────────────────────────────────────────┐
                            │ 1. Run Linter (ESLint & Prettier)         │
                            │ 2. Run Automated Unit Tests (Jest)        │
                            │ 3. Build Docker Images (Client & Server)  │
                            │ 4. Scan Vulnerabilities (Trivy Security)  │
                            └─────────────────────┬─────────────────────┘
                                                  │ (If all Passed)
                                                  ▼ Deploy via SSH
                            ┌───────────────────────────────────────────┐
                            │          PRODUCTION CLOUD VPS             │
                            │ • Docker Compose Up -d --build            │
                            │ • Database Migration (TypeORM Migration)  │
                            │ • Zero-downtime Nginx Reload              │
                            └───────────────────────────────────────────┘
```

Bản vẽ thiết kế kiến trúc này bảo đảm hệ thống ABC-HRM đạt các tiêu chuẩn vận hành công nghiệp: Bảo mật tuyệt đối, hoạt động ổn định và sẵn sàng mở rộng quy mô khi doanh nghiệp phát triển lớn mạnh.
