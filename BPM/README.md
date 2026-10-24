# Môn học: Quản trị Quy trình Nghiệp vụ (BPM - Business Process Management)

> **Khoa Hệ thống Thông tin Quản lý & Chuyển đổi số — Học viện Ngân hàng (HVNH)**  
> Thư mục lưu trữ bài giảng, giáo trình quốc tế, bộ khung phân loại quy trình APQC Banking PCF mới nhất, hệ thống ghi chú chuyên sâu và toàn bộ học liệu đã được chuyển đổi sang chuẩn Markdown (`.md`) bằng công cụ **MarkItDown**.

---

## 📁 Cấu trúc thư mục chuẩn mực

```text
BPM/
├── README.md                                   # Tổng quan môn học, cấu trúc dữ liệu & hướng dẫn
├── Tai_lieu/                                   # Giáo trình, bộ khung chuẩn quốc tế & công cụ đối chuẩn
│   ├── Banking_722_March_2025 (1).pdf          # APQC Banking PCF v7.2.2 (Bản cập nhật tháng 03/2025)
│   ├── Banking_722_March_2025.md               # [MarkItDown] Dữ liệu số hóa toàn văn APQC Banking v7.2.2
│   ├── K06640_ Banking_v721_vs_Banking_v610...xlsx # Bảng đối chiếu vi sai APQC Banking v7.2.1 vs v6.1.0
│   ├── K06640_Banking_v721_vs_Banking_v610.md  # [MarkItDown] Dữ liệu đối chiếu chi tiết 13 danh mục APQC
│   ├── TextBook FundamentalsOfBPM.pdf          # Giáo trình chuẩn quốc tế Fundamentals of BPM (Marlon Dumas et al.)
│   └── TextBook_FundamentalsOfBPM.md           # [MarkItDown] Toàn văn giáo trình dạng Markdown có cấu trúc
├── Slide/                                      # Slide bài giảng các chương lý thuyết & bài tập mô hình hóa
│   ├── Chapter01-Introduction.pdf / .md        # Chương 1: Giới thiệu Quản trị Quy trình Nghiệp vụ & Vòng đời BPM
│   ├── Chapter-02-ProcessIdentification.pdf / .md # Chương 2: Nhận diện quy trình, Kiến trúc quy trình & Lựa chọn
│   ├── Chapter03-EssentialProcessModeling.pdf / .md # Chương 3: Mô hình hóa quy trình cơ bản với BPMN 2.0
│   ├── Chapter04-AdvancedProcessModeling.pdf / .md # Chương 4: Mô hình hóa nâng cao (Sự kiện, Ngoại lệ, Phân rã)
│   └── Your First Process - Vacation Request.pdf / .md # Hướng dẫn thực hành mô hình hóa quy trình đầu tiên
├── Bai_tap_lon/                                # Đề bài, tiêu chí đánh giá, mẫu đồ án & báo cáo hoàn thiện
│   ├── BÀI TẬP NHÓM - Nhận diện và đánh giá quy trình.md # [BÀI TẬP NHÓM] Đề bài thực hành lớn (BSC, APQC, EA, Cải tiến)
│   ├── TIÊU CHÍ ĐÁNH GIÁ BÀI TẬP NHÓM.md        # [BÀI TẬP NHÓM] Rubric thang điểm 100đ chi tiết
│   ├── Bao_cao_BPM_Tin_dung_Giai_ngan_LPBank_HOAN_THIEN.docx / .md # [BÀI TẬP NHÓM] Báo cáo mẫu hoàn chỉnh LPBank
│   └── Final Project - LoanAssessment K28.pdf / .md # [BÀI TẬP CÁ NHÂN CUỐI KHÓA] Đề bài & Hướng dẫn Bizagi BPM Suite
└── Ghi_chu/                                    # Hệ thống tri thức tổng hợp, cẩm nang thực chiến & đối chuẩn
    ├── 01_Khung_Chuan_APQC_PCF_Banking_Toan_Dien.md # Phân tích chuyên sâu APQC PCF Banking (v7.2.2/v7.2.1 vs v6.1.0)
    ├── 02_Tong_Hop_Ly_Thuyet_BPM_Va_Chuan_Mo_Hinh_BPMN.md # Tóm tắt lý thuyết 4 Chapter, Vòng đời BPM & BPMN 2.0
    ├── 03_Cam_Nang_Lam_Bai_Tap_Nhom_BPM_100_Diem.md # Hướng dẫn làm bài tập nhóm đạt điểm tối đa A/A+
    └── 04_Huong_Dan_Bai_Tap_Ca_Nhan_Bizagi_LoanAssessment.md # Hướng dẫn thực hành & đóng gói nộp bài cá nhân Bizagi
```

---

## 🎯 Giới thiệu Môn học & Mục tiêu Đào tạo

Môn học **Quản trị Quy trình Nghiệp vụ (BPM)** trang bị cho học viên cao học/sinh viên chuyên ngành Ngân hàng & HTTT phương pháp luận chuẩn quốc tế để:
1. **Tư duy hướng quy trình (Process Thinking):** Phá vỡ tư duy "ốc đảo phòng ban" (Functional Silos), nhìn nhận tổ chức dưới góc độ dòng giá trị xuyên chức năng (End-to-End Value Stream).
2. **Quản trị vòng đời quy trình (BPM Lifecycle):** Nắm vững 6 giai đoạn: *Nhận diện (Identification) $\rightarrow$ Khám phá (Discovery) $\rightarrow$ Phân tích (Analysis) $\rightarrow$ Tái thiết kế (Redesign) $\rightarrow$ Triển khai thực thi (Implementation) $\rightarrow$ Giám sát & Đo lường (Monitoring)*.
3. **Mô hình hóa chuẩn quốc tế BPMN 2.0:** Sử dụng chính xác các thành phần ký hiệu nghiệp vụ (Flow Objects, Gateways, Events, Pools, Swimlanes, Data Objects).
4. **Đối chuẩn nghiệp vụ với Khung APQC PCF (Banking Edition):** Ánh xạ và so sánh hệ thống quy trình của ngân hàng thương mại với thông lệ quốc tế tốt nhất (Best Practices) và bộ chỉ số Open Standards Benchmarking (OSB).
5. **Tối ưu hóa & Chuyển đổi số:** Loại bỏ lãng phí không tạo ra giá trị (Non-Value-Added - NVA), tự động hóa luồng phê duyệt và ứng dụng công nghệ (RPA, AI Scoring, Core Banking, Loan Origination System - LOS).

---

## 📚 Tổng hợp Tài liệu & Khung Chuẩn

### 1. Bộ chuẩn APQC Process Classification Framework (PCF) - Banking
- **Bản quyền & Xuất xứ:** Phát triển bởi APQC (*American Productivity & Quality Center* - Hoa Kỳ).
- **Mục đích:**
  - Cung cấp **ngôn ngữ chung (common language)** về quy trình cho các ngân hàng và định chế tài chính toàn cầu.
  - Cho phép đo lường và đối chuẩn hiệu suất (Benchmarking) nội bộ cũng như liên ngành (Cross-industry).
  - Làm nền tảng tái thiết kế quy trình kinh doanh (BPR), triển khai Core Banking, CRM, ERP và phân định kiến trúc doanh nghiệp (Enterprise Architecture).
- **Cấu trúc phân cấp 4 tầng của APQC:**
  - **Level 1 - Category:** Danh mục cấp cao nhất (ví dụ: `5.0 Deliver Services`).
  - **Level 2 - Process Group:** Nhóm quy trình liên quan (ví dụ: `5.3 Deliver banking services to customers` - `17416`).
  - **Level 3 - Process:** Quy trình chi tiết (ví dụ: `5.3.1 Open Accounts` - `17417`, `5.3.2 Maintain accounts` - `17422`).
  - **Level 4 - Activity:** Hoạt động cụ thể kèm **mã 5 chữ số (5-digit ID)** (ví dụ: `5.3.1.1 Analyze customer creditworthiness` - mã `13964`, `5.3.1.6 Evaluate collateral/guarantee` - mã `17420`, `5.3.1.8 Fund and disburse proceeds` - mã `13961`).
- **Phiên bản mới nhất:**
  - `Banking_722_March_2025`: Phiên bản cập nhật tháng 03/2025.
  - `K06640_ Banking_v721_vs_Banking_v610`: Bảng phân tích vi sai giữa bản mới và bản cũ v6.1.0 (phân tách danh mục dịch vụ `5.0` độc lập với sản phẩm vật lý `4.0`, nâng cấp mạnh mẽ hạ tầng CNTT `8.0` và Quản trị rủi ro `11.0`).

### 2. Giáo trình & Slide bài giảng
- **Textbook:** *Fundamentals of Business Process Management* (Marlon Dumas, Marcello La Rosa, Jan Mendling, Hajo A. Reijers - Springer).
- **Hệ thống Slide:**
  - `Chapter 1`: Tổng quan, lịch sử BPM, Functional Organization vs Process Thinking, Vòng đời BPM.
  - `Chapter 2`: Nhận diện quy trình (Process Identification), Kiến trúc quy trình (Core, Support, Management), Ma trận đánh giá & lựa chọn (Process Portfolio).
  - `Chapter 3`: Kỹ thuật mô hình hóa cơ bản (BPMN 2.0: Activities, XOR/AND gateways, Pools/Lanes).
  - `Chapter 4`: Kỹ thuật mô hình hóa nâng cao (OR gateway, Event-based gateway, Timer/Message/Error/Cancel events, Boundary events, Sub-processes).

---

## 🏆 Hướng Dẫn Hai Bài Tập Đánh Giá Môn Học

Trong chương trình môn học Quản trị Quy trình Nghiệp vụ (BPM), học viên thực hiện **2 bài tập đánh giá độc lập**:

### A. Bài Tập Nhóm: Đánh Giá & Hoàn Thiện Hệ Thống Quy Trình (Team Assignment)
- **Hình thức:** Làm theo nhóm (~5 thành viên). Báo cáo Word/PDF (10–15 trang) hoặc Slide (15–20 slides).
- **Trọng số:** 100 điểm với 4 phần nội dung:
  - **Phần 1 (20%):** Bối cảnh chiến lược (BSC 4 lăng kính) & Nhận diện quy trình (Core, Support, Management, Process Checklist).
  - **Phần 2 (30%):** Đối chuẩn Khung APQC PCF (Mapping 3 cấp độ kèm mã 5 số & Phân tích khoảng trống Gap Analysis).
  - **Phần 3 (20%):** Lựa chọn quy trình ưu tiên & Phân tích Enterprise Architecture (Tổ chức - Handoffs, IT/Dữ liệu - Silos, Khách hàng - CX).
  - **Phần 4 (30%):** Đề xuất giải pháp (Lean/NVA, Công nghệ LOS/API, Bộ 3–5 KPIs Open Standards Benchmarking).
- **Tài liệu hướng dẫn:** [03_Cam_Nang_Lam_Bai_Tap_Nhom_BPM_100_Diem.md](file:///Users/dovandat/WORKSPACE/HVNH/BPM/Ghi_chu/03_Cam_Nang_Lam_Bai_Tap_Nhom_BPM_100_Diem.md)

### B. Bài Tập Lớn Cuối Khóa Cá Nhân: Tự Động Hóa Quy Trình Trên Bizagi (Individual Final Project)
- **Hình thức:** Làm cá nhân từng học viên trên phần mềm **Bizagi BPM Suite** (Modeler, Studio, Work Portal).
- **Đề bài & Yêu cầu:** [Final_Project_LoanAssessment_K28.md](file:///Users/dovandat/WORKSPACE/HVNH/BPM/Bai_tap_lon/Final_Project_LoanAssessment_K28.md)
- **Nội dung thực hành:**
  1. Mô hình hóa quy trình **Loan Assessment Process** (4 vai trò: Loan Officer, Financial Officer, Property Appraiser, Insurance Sales Rep).
  2. Xây dựng Data Model (LoanAssessment, Applicant, Property, InsuranceQuote).
  3. Thiết kế User Forms nhập liệu cho từng bước.
  4. Cấu hình Business Rules, Gateways điều kiện và cơ chế Dual Control (Two-man Rule).
  5. Thiết lập thông báo Email tự động (SMTP Server) và sinh chứng từ PDF.
  6. Kiểm thử toàn diện các Case trên Bizagi Work Portal.
- **Yêu cầu nộp bài:** *"Hãy làm bài tập theo các hướng dẫn cụ thể dưới đây, đóng gói và nén file project với tên riêng của bạn và submit tại đây"*  
  $\rightarrow$ Đóng gói Project Bizagi thành file `.zip` theo quy ước `[HọTên]_[MãHV]_LoanAssessment_Bizagi.zip`.
- **Tài liệu hướng dẫn:** [04_Huong_Dan_Bai_Tap_Ca_Nhan_Bizagi_LoanAssessment.md](file:///Users/dovandat/WORKSPACE/HVNH/BPM/Ghi_chu/04_Huong_Dan_Bai_Tap_Ca_Nhan_Bizagi_LoanAssessment.md)

---

*Học viện Ngân hàng — Khoa HTTTQL — Hệ thống dữ liệu học thuật số hóa cao cấp.*
