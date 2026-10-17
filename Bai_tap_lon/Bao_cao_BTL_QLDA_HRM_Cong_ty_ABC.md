# HỌC VIỆN NGÂN HÀNG
## KHOA HỆ THỐNG THÔNG TIN QUẢN LÝ / SAU ĐẠI HỌC
***

# BÀI TẬP LỚN HỌC PHẦN: QUẢN LÝ DỰ ÁN CNTT NÂNG CAO

### ĐỀ TÀI:
# QUẢN LÝ DỰ ÁN PHÁT TRIỂN HỆ THỐNG QUẢN TRỊ NHÂN SỰ NỘI BỘ (ABC-HRM) CHO CÔNG TY QUY MÔ 100 NHÂN SỰ

---

* **Giảng viên hướng dẫn:** TS. [Họ và tên Giảng viên Hướng dẫn]
* **Học phần:** Quản lý Dự án Công nghệ Thông tin Nâng cao
* **Nhóm học viên thực hiện:** Nhóm 01 (Lớp QLDA CNTT NC - Khóa Cao học)
  1. [Học viên 1 - Trưởng nhóm / Quản lý Dự án - PM] — Mã HV: [Mã HV 1]
  2. [Học viên 2 - Chuyên viên Phân tích Nghiệp vụ - BA] — Mã HV: [Mã HV 2]
  3. [Học viên 3 - Kỹ sư Phần mềm Cao cấp / Tech Lead] — Mã HV: [Mã HV 3]
  4. [Học viên 4 - Kỹ sư Phần mềm / Risk & Change] — Mã HV: [Mã HV 4]
  5. [Học viên 5 - Kỹ sư Đảm bảo Chất lượng / QA Lead] — Mã HV: [Mã HV 5]

---

*Hà Nội, Năm 2026*

\newpage

# BẢNG NHẬN XÉT VÀ ĐÁNH GIÁ CỦA GIẢNG VIÊN

| Tiêu chí Đánh giá | Trọng số | Điểm tối đa | Điểm đánh giá | Nhận xét chi tiết của Giảng viên |
|---|:---:|:---:|:---:|---|
| **1. Tính cấp thiết & Phân tích Khởi tạo (Business Case, Charter, Stakeholders)** | 20% | 2,0 | | |
| **2. Chất lượng Kế hoạch Cơ sở (Scope, SRS, WBS Cấp 4, PERT/CPM, S-Curve, RACI, Risk)** | 35% | 3,5 | | |
| **3. Giám sát & Quản lý Thay đổi (EVM 2 thời điểm, Hội đồng CCB, Traffic Light)** | 25% | 2,5 | | |
| **4. Kết thúc Dự án & Hồ sơ Kỹ thuật (Lessons Learned, Closure Report, Architecture, ERD, UAT)** | 20% | 2,0 | | |
| **TỔNG CỘNG** | **100%** | **10,0** | | |

**Nhận xét chung của Giảng viên chấm thi:**
........................................................................................................................................................................
........................................................................................................................................................................
........................................................................................................................................................................
........................................................................................................................................................................

*Hà Nội, ngày ...... tháng ...... năm 2026*
**GIẢNG VIÊN CHẤM THI**
*(Ký và ghi rõ họ tên)*

\newpage

# LỜI CAM ĐOAN

Chúng tôi xin cam đoan bản Báo cáo tổng hợp Bài tập lớn học phần Quản lý Dự án CNTT Nâng cao với đề tài *"Quản lý Dự án Phát triển Hệ thống Quản trị Nhân sự Nội bộ (ABC-HRM) cho Công ty Quy mô 100 Nhân sự"* là công trình nghiên cứu và xây dựng độc lập, nghiêm túc của Nhóm 01.

Mọi số liệu tài chính (NPV, ROI, Payback), dữ liệu hiệu suất tiến độ và chi phí (EVM mốc 15/10 và 20/10), sơ đồ mạng lịch trình (PERT/CPM), danh mục rủi ro và các bản vẽ kỹ thuật (Kiến trúc 3 lớp, CSDL ERD 3NF) trình bày trong báo cáo đều được tính toán khoa học, dựa trên bối cảnh doanh nghiệp thực tế giả định và tuân thủ chặt chẽ các chuẩn mực quốc tế của Viện Quản lý Dự án Hoa Kỳ (PMI PMBOK Guide 7th Edition) cùng các hướng dẫn chuyên môn của Giảng viên học phần. Nhóm chịu hoàn toàn trách nhiệm về tính trung thực và liêm chính học thuật của tài liệu này.

*Đại diện Nhóm học viên thực hiện:*
**[Họ và tên Học viên 1 - Trưởng nhóm]**

---

# LỜI CẢM ƠN

Nhóm nghiên cứu xin bày tỏ lòng biết ơn sâu sắc và chân thành nhất tới Giảng viên phụ trách học phần **Quản lý Dự án CNTT Nâng cao** tại Học viện Ngân hàng. Trong suốt quá trình học tập và nghiên cứu trên lớp, thầy/cô đã truyền thụ những nền tảng tri thức học thuật sâu rộng, các phương pháp luận quản trị dự án hiện đại và những kinh nghiệm thực chiến vô cùng quý báu trong lĩnh vực quản lý các dự án công nghệ thông tin phức tạp.

Những bài giảng nhiệt huyết về xây dựng Đường cơ sở Hiệu suất (PMB), kỹ thuật kiểm soát giá trị thu được (EVM), quản trị rủi ro định tính và quản lý thay đổi tích hợp (CCB) đã trở thành kim chỉ nam dẫn đường giúp nhóm hoàn thiện tập hồ sơ báo cáo toàn văn này một cách chuẩn mực, logic và có tính ứng dụng thực tiễn cao.

Nhóm cũng xin chân thành cảm ơn Ban Lãnh đạo Khoa Hệ thống Thông tin Quản lý và Khoa Sau Đại học — Học viện Ngân hàng đã tạo điều kiện học tập và nghiên cứu tốt nhất cho học viên.

*Tập thể Nhóm 01 kính dâng!*

\newpage

# TÓM TẮT ĐIỀU HÀNH DỰ ÁN (EXECUTIVE SUMMARY)

Báo cáo này trình bày trọn vẹn hồ sơ quản lý dự án cấp chuyên nghiệp cho Dự án **"Xây dựng Hệ thống Quản trị Nhân sự Nội bộ (ABC-HRM)"** tại Công ty Cổ phần ABC — một doanh nghiệp dịch vụ công nghệ quy mô 100 cán bộ nhân viên. Dự án được triển khai nhằm giải quyết triệt để 6 nhóm vấn đề nan giải trong công tác quản trị nhân lực thủ công bằng Excel cũ (lãng phí 15 giờ/tuần đối soát công, mất 3 ngày tính lương, sai lệch lương 5,2%, rủi ro xử phạt BHXH và tỷ lệ thôi việc 18%).

Dự án áp dụng mô hình quản lý **Hybrid** tiên tiến (kết hợp kỷ luật quản lý phạm vi, chi phí, tiến độ tổng thể của Waterfall/PMBOK với tính linh hoạt của Scrum trong các vòng lặp phát triển phần mềm), bao quát đầy đủ 4 nhóm quy trình quản lý dự án chính:
1. **Giai đoạn Khởi tạo (Initiating):** Xác lập Business Case vững chắc với $NPV = +476,78$ triệu VNĐ ($r = 10\%$), $ROI = 105,88\%$, thời gian hoàn vốn $PBP = 2,43$ năm. Ban hành Hiến chương Dự án (Project Charter) chuẩn SMART, ngân sách 850 triệu VNĐ, thời gian 24 tuần (01/11/2025 – 30/04/2026), và Sổ đăng ký 10 bên liên quan trọng yếu kèm Ma trận Quyền lực/Quan tâm 2x2.
2. **Giai đoạn Lập kế hoạch (Planning):** Thiết lập Đường cơ sở Đo lường Hiệu suất (Performance Measurement Baseline - PMB) toàn diện:
   - *Phạm vi:* Tuyên bố phạm vi và danh mục loại trừ (Exclusions) triệt tiêu Scope Creep; đặc tả SRS gồm 12 FR và 6 NFR; cấu trúc WBS Cấp 4 (7 nhánh chính) kèm Từ điển WBS chi tiết.
   - *Thời gian:* Ước tính PERT 3 điểm cho 13 hoạt động nòng cốt; mô hình mạng PDM xác định **Đường Găng (Critical Path) dài 84,5 ngày công (24 tuần)** đi qua chuỗi hoạt động: *Khảo sát $\rightarrow$ Thiết kế Kiến trúc $\rightarrow$ Dev Chấm công $\rightarrow$ Dev Tính lương $\rightarrow$ Kiểm thử Tích hợp $\rightarrow$ UAT $\rightarrow$ Di chuyển DL $\rightarrow$ Go-Live*.
   - *Chi phí:* Dự toán chi phí Bottom-Up trực tiếp 710 triệu VNĐ; lập Quỹ Dự trữ Dự phòng 15% (106,5 tr) $\rightarrow$ **Cost Baseline = 816,5 triệu VNĐ**; Quỹ Dự trữ Quản lý 4% (33,5 tr) $\rightarrow$ **Tổng ngân sách BAC = 850 triệu VNĐ**; phân bổ dòng tiền tích lũy S-Curve theo 6 tháng.
   - *Nhân sự & Rủi ro:* Ma trận RACI 16 công việc, chiến lược tạo động lực nội tại và hóa giải rủi ro phụ thuộc Senior Dev; Sổ đăng ký 12 rủi ro (10 mối đe dọa, 2 cơ hội) với ma trận nhiệt 5x5 và cơ chế kích hoạt quỹ dự phòng.
3. **Giai đoạn Thực hiện & Giám sát (Execution & M&C):**
   - Vận hành Hội đồng CCB: Phê duyệt CR-001 (Cảnh báo tự động hợp đồng hết hạn trước 30 ngày, +5,5 tr, không đổi ngày go-live) và kiên quyết bác bỏ CR-002 (Thêm module Đào tạo LMS, +85 tr, trễ 4 tuần) dời sang Phase 2.
   - Quản lý Giá trị Thu được (EVM) chi tiết tại 2 thời điểm:
     * *Mốc 15/10 (Tuần 14):* $PV = 476,76$ tr, $EV = 452,10$ tr, $AC = 470,00$ tr $\rightarrow$ $CPI = 0,962$, $SPI = 0,948$, $EAC = 854,47$ tr. Phát hiện sự cố tích hợp SDK máy chấm công; kích hoạt 15 triệu dự phòng thuê chuyên gia và áp dụng Fast-tracking.
     * *Mốc 20/10 (Tuần 18):* $PV = 616,50$ tr, $EV = 608,28$ tr, $AC = 612,00$ tr $\rightarrow$ $CPI = 0,994$, $SPI = 0,987$, $EAC = 826,96$ tr. Phục hồi ngoạn mục, bảo toàn tiến độ và ngân sách.
   - Báo cáo Tình trạng Đèn Giao Thông (chuyển từ Vàng sang Xanh) và giải quyết dứt điểm 3 Issues trong Issue Log.
4. **Giai đoạn Kết thúc (Closing):**
   - Đóng gói 4 bài học tri thức hữu hình (Explicit) và 3 bài học tri thức vô hình (Tacit).
   - Đánh giá hiệu suất vượt trội so với PMB: Hoàn thành 108% phạm vi, chi phí thực tế giải ngân **$AC_{\text{final}} = 826,96$ triệu VNĐ (tiết kiệm 23,04 triệu VNĐ = 2,7%)**, Uptime 99,8%, tỷ lệ nhân viên áp dụng đạt 95%.
   - Ký Biên bản Chấp thuận Nghiệm thu Chính thức (Formal Acceptance), chuyển giao toàn bộ mã nguồn Git, tài liệu Ops Manual, User Guide và thanh lý dự án an toàn.
5. **Hồ sơ Kỹ thuật Bổ trợ:** Thiết kế Kiến trúc 3 tầng (React / NestJS / PostgreSQL / Docker) bảo mật đa lớp (AES-256, Bcrypt, 2FA, RBAC); Thiết kế CSDL chuẩn hóa 3NF gồm 10 bảng cốt lõi; Kế hoạch Kiểm thử & UAT hoàn thành 50/50 Test Cases.

\newpage

# MỤC LỤC TỔNG THỂ

* **LỜI CAM ĐOAN**
* **LỜI CẢM ƠN**
* **TÓM TẮT ĐIỀU HÀNH DỰ ÁN (EXECUTIVE SUMMARY)**
* **DANH MỤC CÁC TỪ VIẾT TẮT**
* **DANH MỤC BẢNG BIỂU**
* **DANH MỤC HÌNH VẼ & SƠ ĐỒ**
* **LỜI MỞ ĐẦU**
* **CHƯƠNG 1: TỔNG QUAN DOANH NGHIỆP VÀ GIAI ĐOẠN KHỞI TẠO DỰ ÁN (INITIATING)**
  * 1.1. Thực trạng Quản trị Nhân lực và Vấn đề Nghiệp vụ của Công ty ABC
  * 1.2. Nghiên cứu Khởi đầu và Xác nhận Giá trị (Business Case)
  * 1.3. Phân tích Hiệu quả Tài chính Chi tiết (NPV, ROI, Payback, Phân tích Độ nhạy)
  * 1.4. Hiến chương Dự án (Project Charter) Chuẩn PMI và HVNH
  * 1.5. Quản lý Các Bên Liên quan (Stakeholder Register, Ma trận Power/Interest và Kế hoạch Truyền thông)
* **CHƯƠNG 2: KẾ HOẠCH QUẢN LÝ DỰ ÁN & ĐƯỜNG CƠ SỞ HIỆU SUẤT (PLANNING - PMB)**
  * 2.1. Quản lý Phạm vi: Tuyên bố Phạm vi (Scope Statement), Danh mục Loại trừ và Đặc tả Yêu cầu (SRS)
  * 2.2. Cấu trúc Phân chia Công việc (WBS Cấp 4) và Từ điển WBS (WBS Dictionary)
  * 2.3. Quản lý Thời gian: Ước tính PERT 3 Điểm, Sơ đồ Mạng PDM, Đường Găng (CPM) và Biểu đồ Gantt
  * 2.4. Quản lý Chi phí: Ước tính Bottom-Up, Cơ cấu Quỹ Dự phòng và Đường cơ sở Chi phí (S-Curve)
  * 2.5. Quản trị Nguồn nhân lực CNTT: Ma trận RACI, Giải tỏa Rủi ro Phụ thuộc và Động lực Nội tại
  * 2.6. Quản lý Rủi ro: Sổ Đăng ký 12 Rủi ro, Ma trận Nhiệt 5x5 và Kế hoạch Ứng phó Kích hoạt Dự phòng
* **CHƯƠNG 3: GIAI ĐOẠN THỰC HIỆN, GIÁM SÁT VÀ KIỂM SOÁT DỰ ÁN (EXECUTION & M&C)**
  * 3.1. Quản lý Thay đổi Tích hợp: Quy chế Hội đồng CCB, Xử lý Chi tiết 2 CRs và Nhật ký Thay đổi (Change Log)
  * 3.2. Quản lý Giá trị Thu được (EVM) Chi tiết tại Hai Thời điểm Báo cáo (15/10 và 20/10)
  * 3.3. Báo cáo Tình trạng Dự án Đèn Giao Thông (Traffic Light System)
  * 3.4. Sổ Theo dõi Vấn đề Phát sinh Thực tế (Issue Log)
* **CHƯƠNG 4: GIAI ĐOẠN KẾT THÚC DỰ ÁN VÀ BÀI HỌC KINH NGHIỆM (CLOSING)**
  * 4.1. Bài học Kinh nghiệm Dự án: Biên bản Retrospective, Tri thức Hữu hình và Vô hình
  * 4.2. Báo cáo Đóng Dự án Cuối cùng (Final Project Closure Report) So với Đường Cơ sở PMB
  * 4.3. Bàn giao Sản phẩm, Kế hoạch Giải tán Nhóm, Quyết toán Tài chính và Biên bản Formal Acceptance
* **CHƯƠNG 5: HỒ SƠ THIẾT KẾ KỸ THUẬT VÀ PHẦN MỀM (TECHNICAL SPECIFICATIONS)**
  * 5.1. Thiết kế Kiến trúc Hệ thống 3 Tầng và Kiến trúc An ninh Bảo mật Đa lớp
  * 5.2. Thiết kế Cơ sở Dữ liệu Quan hệ 3NF (Sơ đồ ERD và Từ điển Dữ liệu 10 Bảng)
  * 5.3. Kế hoạch Kiểm thử Đa tầng và Biên bản Nghiệm thu Kỹ thuật Chấp thuận (UAT Signoff)
* **TÀI LIỆU THAM KHẢO**

\newpage

# DANH MỤC CÁC TỪ VIẾT TẮT

| Từ viết tắt | Thuật ngữ Tiếng Anh | Diễn giải Nghĩa Tiếng Việt |
|---|---|---|
| **AC** | Actual Cost | Chi phí Thực tế đã giải ngân |
| **BAC** | Budget at Completion | Tổng Ngân sách Kế hoạch Khi Hoàn thành Dự án |
| **CCB** | Change Control Board | Hội đồng Kiểm soát Thay đổi |
| **CPM** | Critical Path Method | Phương pháp Phân tích Đường Găng |
| **CPI** | Cost Performance Index | Chỉ số Hiệu suất Chi phí |
| **CR** | Change Request | Yêu cầu Thay đổi |
| **CV** | Cost Variance | Phương sai Chi phí ($EV - AC$) |
| **EAC** | Estimate at Completion | Ước tính Chi phí Dự kiến Khi Hoàn thành Dự án |
| **ERD** | Entity-Relationship Diagram | Sơ đồ Thực thể Quan hệ Cơ sở Dữ liệu |
| **ETC** | Estimate to Complete | Ước tính Chi phí Cần thêm Để Hoàn tất Dự án |
| **EV** | Earned Value | Giá trị Thu được (Khối lượng công việc hoàn thành) |
| **EVM** | Earned Value Management | Phương pháp Quản lý Giá trị Thu được |
| **FR** | Functional Requirement | Yêu cầu Chức năng Phần mềm |
| **FS / SS / FF**| Finish-to-Start / Start-to-Start / Finish-to-Finish | Mối quan hệ phụ thuộc trước - sau giữa các công việc |
| **NFR** | Non-Functional Requirement | Yêu cầu Phi chức năng Phần mềm |
| **NPV** | Net Present Value | Giá trị Hiện tại Thuần của Dự án Đầu tư |
| **PBP / DPBP** | Payback Period / Discounted Payback Period | Thời gian Hoàn vốn Giản đơn / Thời gian Hoàn vốn Có Chiết khấu |
| **PDM** | Precedence Diagramming Method | Phương pháp Lập Sơ đồ Lịch trình Theo Thứ tự Ưu tiên |
| **PERT** | Program Evaluation and Review Technique | Kỹ thuật Đánh giá và Rà soát Chương trình (Ước tính 3 điểm) |
| **PMB** | Performance Measurement Baseline | Đường cơ sở Đo lường Hiệu suất Dự án (Phạm vi + Thời gian + Chi phí) |
| **PMBOK** | Project Management Body of Knowledge | Bộ Kiến thức Cốt lõi về Quản lý Dự án của Viện PMI Hoa Kỳ |
| **PV** | Planned Value | Giá trị Kế hoạch theo Phân bổ Ngân sách |
| **RACI** | Responsible - Accountable - Consulted - Informed | Ma trận Phân công Trách nhiệm |
| **ROI** | Return on Investment | Tỷ suất Hoàn vốn Đầu tư |
| **RTM** | Requirements Traceability Matrix | Ma trận Truy vết Nguồn gốc Yêu cầu |
| **SPI** | Schedule Performance Index | Chỉ số Hiệu suất Lịch trình Tiến độ |
| **SRS** | Software Requirements Specification | Tài liệu Đặc tả Yêu cầu Phần mềm |
| **SV** | Schedule Variance | Phương sai Lịch trình ($EV - PV$) |
| **TCPI** | To-Complete Performance Index | Chỉ số Hiệu suất Chi phí Cần đạt trong Tương lai |
| **UAT** | User Acceptance Testing | Kiểm thử Chấp nhận Người dùng Cuối |
| **WBS** | Work Breakdown Structure | Cấu trúc Phân chia Công việc |

\newpage

# LỜI MỞ ĐẦU

### 1. Tính Cấp Thiết của Đề Tài (Tại Sao Làm? - Why)
Trong kỷ nguyên số hóa và chuyển đổi số doanh nghiệp, nguồn nhân lực được coi là tài sản chiến lược quý giá nhất quyết định năng lực cạnh tranh của mọi tổ chức. Tuy nhiên, tại nhiều doanh nghiệp vừa và nhỏ (SMEs) ở Việt Nam hiện nay, công tác quản trị nhân lực vẫn đang phụ thuộc nặng nề vào các công cụ thủ công truyền thống như bảng tính Microsoft Excel rời rạc, lưu trữ hồ sơ giấy tờ và quản lý đơn từ qua email.

Thực trạng này tại Công ty Cổ phần ABC (quy mô 100 cán bộ nhân viên) đang bộc lộ những hạn chế mang tính hệ thống: Tiêu tốn hơn 60 giờ công sự vụ mỗi tháng của phòng Nhân sự cho việc đối soát thủ công; thời gian chốt bảng lương kéo dài từ 2 đến 3 ngày làm việc; tỷ lệ khiếu nại sai sót tiền lương chiếm tới 5,2%/tháng; tiềm ẩn các rủi ro pháp lý nghiêm trọng về thanh tra Bảo hiểm Xã hội và thuế Thu nhập Cá nhân; đồng thời Ban Giám đốc hoàn toàn thiếu vắng các báo cáo nhân sự tức thời (real-time) để hoạch định chiến lược kinh doanh. 

Do đó, việc nghiên cứu, xây dựng và quản trị dự án phát triển một **Hệ thống Quản trị Nhân sự Nội bộ tập trung (ABC-HRM)** là một đòi hỏi tất yếu, cấp thiết, có ý nghĩa sống còn đối với sự phát triển bền vững của doanh nghiệp.

### 2. Mục Tiêu của Bài Tập Lớn và Sản Phẩm Bàn Giao (Làm Gì? - What)
Mục tiêu cốt lõi của Bài tập lớn này là vận dụng toàn diện, chuẩn mực và sáng tạo các nguyên tắc, mô hình, công cụ quản lý dự án công nghệ thông tin tiên tiến (theo chuẩn PMI PMBOK Guide 7th Edition) vào một bài toán chuyển đổi số cụ thể. 

Sản phẩm của dự án là một hệ thống ứng dụng Web ABC-HRM hoàn chỉnh gồm 6 phân hệ cốt lõi (Hồ sơ, Chấm công, Tính lương, Tuyển dụng, Đánh giá KPI, Dashboard Báo cáo), đi kèm với **trọn bộ hồ sơ Quản lý Dự án chính thức (20 Deliverables)** bao quát đầy đủ 4 nhóm quy trình quản trị dự án chuẩn mực và **hồ sơ thiết kế kỹ thuật chuyên môn** (SRS, Kiến trúc, ERD, Test Plan).

### 3. Phương Pháp Luận và Mô Hình Quản Trị Áp Dụng (Làm Thế Nào? - How)
Dự án áp dụng mô hình quản lý **Hybrid (Lai ghép)**:
* **Khung Quản trị Tổng thể (Waterfall / Predictive):** Áp dụng cho các giai đoạn thiết lập Đường cơ sở Đo lường Hiệu suất (PMB: Scope Baseline, Schedule Baseline, Cost Baseline), quản lý hợp đồng, kiểm soát thay đổi qua Hội đồng CCB và nghiệm thu tài chính.
* **Quy trình Phát triển Phần mềm (Agile / Scrum):** Áp dụng trong các vòng lặp phát triển kỹ thuật (chia thành các Sprint 2 tuần) với các nghi thức Daily Standup, Sprint Planning, Sprint Review và Retrospective, giúp nhóm thích ứng nhanh với phản hồi thực tế của người dùng và bàn giao sản phẩm sớm.
* **Toàn bộ nội dung báo cáo được cấu trúc và dẫn dắt nhất quán xuyên suốt bởi hệ thống câu hỏi bản chất:**
  - **Làm gì? (What is to be done?):** Định nghĩa cụ thể mục tiêu, phạm vi, sản phẩm bàn giao của từng hạng mục.
  - **Tại sao làm? (Why is it to be done?):** Lý giải căn nguyên nghiệp vụ, lợi ích kinh tế, giá trị chiến lược và cơ sở lý luận khoa học.
  - **Làm thế nào? (How will it be done?):** Trình bày quy trình thực thi, công thức toán học, công nghệ, ma trận phân quyền và tiêu chí kiểm chứng nghiệm thu.

\newpage

# CHƯƠNG 1: TỔNG QUAN DOANH NGHIỆP VÀ GIAI ĐOẠN KHỞI TẠO DỰ ÁN (INITIATING)

---

## KHUNG TIẾP CẬN BẢN CHẤT CỦA GIAI ĐOẠN KHỞI TẠO

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                             GIAI ĐOẠN KHỞI TẠO DỰ ÁN (INITIATING PHASE)                          │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. TẠI SAO LÀM? (WHY)                                                                           │
│    • Mọi dự án CNTT đều bắt đầu từ một nhu cầu kinh doanh (Business Need) hoặc một nỗi đau vận   │
│      hành cụ thể. Nếu không chứng minh được tính khả thi về mặt tài chính và sự phù hợp chiến    │
│      lược, dự án sẽ lãng phí nguồn lực đầu tư mà không mang lại giá trị cho tổ chức.            │
│    • Cần một văn bản ủy quyền chính thức (Project Charter) từ cấp lãnh đạo cao nhất để hợp thức │
│      hóa sự tồn tại của dự án và trao quyền hạn pháp lý cho Quản lý Dự án (PM).                  │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 2. LÀM GÌ? (WHAT)                                                                                │
│    • Nghiên cứu khởi đầu, phân tích chi phí - lợi ích và tính toán các chỉ số kinh tế:           │
│      NPV (+476,78 triệu VNĐ), ROI (105,88%), Thời gian hoàn vốn PBP (2,43 năm).                 │
│    • Ban hành Hiến chương Dự án (Project Charter) xác lập mục tiêu SMART, ngân sách trần 850 tr, │
│      mốc thời gian 24 tuần (Go-live 30/04/2026) và quyền hạn điều hành của PM.                  │
│    • Lập Sổ đăng ký 10 Bên liên quan (Stakeholder Register) và Ma trận Quyền lực/Quan tâm 2x2.   │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 3. LÀM THẾ NÀO? (HOW)                                                                           │
│    • Thu thập số liệu vận hành hiện tại, xây dựng mô hình chiết khấu dòng tiền 5 năm (DCF, r=10%)│
│      và chạy kiểm tra phân tích độ nhạy (Sensitivity Analysis) 3 kịch bản.                      │
│    • Áp dụng mẫu chuẩn Project Charter của Viện PMI và phân loại bên liên quan theo 4 chiến lược │
│      tương tác: Manage Closely, Keep Satisfied, Keep Informed, Monitor.                          │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 1.1. THỰC TRẠNG QUẢN TRỊ NHÂN LỰC VÀ VẤN ĐỀ NGHIỆP VỤ CỦA CÔNG TY ABC

### 1.1.1. Bối cảnh Doanh nghiệp Thụ hưởng
Công ty Cổ phần ABC là doanh nghiệp hoạt động trong lĩnh vực dịch vụ công nghệ thông tin và giải pháp số với quy mô nhân sự hiện tại là **100 nhân viên** (bao gồm 70 kỹ sư phần mềm, 15 nhân viên kinh doanh/marketing, và 15 nhân viên khối vận hành, kế toán, nhân sự).

Hiện tại, công tác quản trị nhân lực của công ty đang được vận hành bởi phòng Nhân sự (gồm 3 chuyên viên) thông qua các công cụ thủ công truyền thống:
1. **Quản lý hồ sơ:** Sử dụng các bảng tính Microsoft Excel độc lập phân tán trên máy tính cá nhân, lưu trữ hợp đồng lao động và bằng cấp qua hồ sơ giấy kết hợp thư mục Google Drive không phân quyền chặt chẽ.
2. **Chấm công:** Nhân viên chấm công bằng máy quét vân tay tại văn phòng, tuy nhiên dữ liệu quét thô chỉ được trích xuất thủ công vào cuối tháng qua USB hoặc phần mềm đóng gói cục bộ không có kết nối API.
3. **Quản lý nghỉ phép:** Tiếp nhận đơn xin nghỉ phép, làm ngoài giờ (OT), đi công tác thông qua email hoặc đơn giấy ký tay, sau đó chuyên viên nhân sự nhập thủ công lại vào file tổng hợp.
4. **Tính lương & Phúc lợi:** Chuyên viên tiền lương mất trung bình 2 đến 3 ngày làm việc mỗi tháng để tổng hợp giờ công, đối chiếu ngày phép, áp công thức tính thuế thu nhập cá nhân (TNCN) và các khoản trích nộp Bảo hiểm xã hội (BHXH, BHYT, BHTN) trên các file Excel chứa hàng trăm dòng tính phức tạp.
5. **Đánh giá hiệu suất & Tuyển dụng:** Chưa có hệ thống theo dõi KPI tập trung; quy trình tuyển dụng và tiếp nhận nhân sự mới (onboarding) không có checklist chuẩn hóa, dẫn đến trải nghiệm nhân viên mới bị phân mảnh.

### 1.1.2. Lượng hóa Các Tổn Thất và Lãng Phí Vận Hành (Problem Statement)

Bảng 1.1 tổng hợp các điểm nghẽn nghiêm trọng đã được nhóm nghiên cứu lượng hóa cụ thể:

| Mã vấn đề | Lĩnh vực | Mô tả thực trạng | Tổn thất định lượng đo lường được |
|---|---|---|---|
| **PB-01** | Thời gian vận hành | Xử lý thủ công bảng công, đơn từ nghỉ phép và đối soát chấm công | Mất **15 giờ/tuần** của toàn đội ngũ HR (~60 giờ công/tháng, tương đương 0,38 FTE chuyên viên bậc trung). |
| **PB-02** | Xử lý tiền lương | Chốt bảng lương cuối tháng, tính toán các khoản trích theo lương | Mất **16 đến 24 giờ làm việc** mỗi kỳ lương; áp lực cao dẫn tới thời gian phát hành phiếu lương bị trễ hạn từ 2 đến 4 ngày. |
| **PB-03** | Sai lệch dữ liệu | Công thức Excel bị lỗi tham chiếu, nhầm lẫn ca làm việc và mức giảm trừ gia cảnh | Tỷ lệ khiếu nại sai sót lương trung bình **5,2%/tháng** (tương đương 5–6 nhân viên khiếu nại mỗi tháng), gây giảm sút lòng tin vào bộ máy quản lý. |
| **PB-04** | Rủi ro pháp lý | Sai sót trong cập nhật mức trần đóng BHXH hoặc khai báo biến động lao động chậm | Rủi ro bị cơ quan quản lý xử phạt hành chính; chi phí khắc phục sai sót và truy thu ước tính **50 triệu VNĐ/năm**. |
| **PB-05** | Biến động nhân sự | Thiếu minh bạch trong đánh giá KPI và lộ trình thăng tiến | Tỷ lệ nhân viên tự nguyện nghỉ việc (Turnover rate) năm liền trước đạt **18%**; chi phí tuyển dụng và đào tạo thay thế tốn kém. |
| **PB-06** | Hỗ trợ quyết định | Ban Giám đốc không có báo cáo tức thời (real-time) về biến động nhân sự và quỹ lương | Phải chờ phòng HR tổng hợp báo cáo mất từ 3 đến 5 ngày làm việc khi cần dữ liệu ra quyết định chiến lược. |

---

## 1.2. NGHIÊN CỨU KHỞI ĐẦU VÀ XÁC NHẬN GIÁ TRỊ (BUSINESS CASE)

### 1.2.1. Đề xuất Giải pháp Hệ thống ABC-HRM
Dự án đề xuất nghiên cứu, thiết kế và phát triển Hệ thống Quản trị Nhân sự Nội bộ (**ABC-HRM**) tập trung trên nền tảng Web Application, triển khai trên hạ tầng máy chủ Cloud riêng của công ty, bao gồm 6 phân hệ cốt lõi:
1. **Phân hệ Quản lý Hồ sơ Nhân sự:** Số hóa toàn diện vòng đời nhân viên từ khi ký hợp đồng thử việc đến khi thôi việc.
2. **Phân hệ Chấm công & Quản lý Nghỉ phép:** Tích hợp trực tiếp API/Webhook máy chấm công văn phòng; quy trình phê duyệt nghỉ phép trực tuyến nhiều cấp.
3. **Phân hệ Tính lương & Phúc lợi:** Tự động hóa tính toán Gross-to-Net, khấu trừ BHXH, thuế TNCN lũy tiến từng phần theo quy định pháp luật Việt Nam.
4. **Phân hệ Tuyển dụng & Onboarding:** Quản trị hồ sơ ứng viên, lịch phỏng vấn và lộ trình hội nhập chuẩn hóa.
5. **Phân hệ Quản trị Hiệu suất (KPI):** Thiết lập mục tiêu phòng ban/cá nhân, đánh giá định kỳ 360 độ và theo dõi tiến độ hoàn thành.
6. **Phân hệ Dashboard & Báo cáo Quản trị:** Cung cấp báo cáo trực quan cho HR Manager và Ban Giám đốc với các chỉ số đo lường hiệu suất nhân sự tức thời.

### 1.2.2. Sự Phù hợp Chiến lược (Strategic Alignment)
Dự án phù hợp với Chiến lược Chuyển đổi số Nội bộ của Công ty ABC giai đoạn 2025–2027, đóng vai trò là xương sống vận hành để chuẩn bị cho kế hoạch mở rộng quy mô công ty lên 150–200 nhân sự trong 3 năm tới mà không cần tăng tỷ lệ nhân sự quản lý gián tiếp.

---

## 1.3. PHÂN TÍCH HIỆU QUẢ TÀI CHÍNH CHI TIẾT (FINANCIAL ANALYSIS)

### 1.3.1. Dự toán Ngân sách Đầu tư Ban đầu (Year 0)
Tổng mức đầu tư cho dự án phát triển hệ thống trong 6 tháng được xác lập là **850.000.000 VNĐ** (Tám trăm năm mươi triệu đồng chẵn), chi tiết cấu thành như sau:

| STT | Khoản mục chi phí | Diễn giải chi tiết | Giá trị (VNĐ) | Tỷ trọng (%) |
|:---:|---|---|---:|:---:|
| 1 | Chi phí Nhân công Phát triển | 5 thành viên nòng cốt tham gia triển khai dự án trong 6 tháng (PM, BA, 2 Dev, 1 QA) | 575.000.000 | 67,6% |
| 2 | Chi phí Hạ tầng & Bản quyền | Máy chủ Cloud thử nghiệm, tên miền, chứng chỉ SSL, bản quyền công cụ quản lý dự án và UI/UX | 68.000.000 | 8,0% |
| 3 | Chi phí Tích hợp Phần cứng | SDK tích hợp API máy chấm công vân tay ZKTeco và thiết bị kiểm thử | 12.000.000 | 1,4% |
| 4 | Chi phí Đào tạo & Di chuyển dữ liệu | Làm sạch dữ liệu Excel cũ, số hóa hồ sơ và đào tạo người dùng cuối | 55.000.000 | 6,5% |
| **I** | **Tổng chi phí ước tính trực tiếp** | | **710.000.000** | **83,5%** |
| 5 | Dự trữ Dự phòng (Contingency Reserve) | 15% tổng chi phí trực tiếp — dùng ứng phó các rủi ro kỹ thuật và tích hợp đã nhận diện | 106.500.000 | 12,5% |
| **II** | **Đường cơ sở Chi phí (Cost Baseline)** | **I + Khoản mục 5** | **816.500.000** | **96,1%** |
| 6 | Dự trữ Quản lý (Management Reserve) | Khoảng 4% — do Ban Giám đốc phê duyệt cho các phát sinh phạm vi chưa biết | 33.500.000 | 3,9% |
| **III**| **TỔNG NGÂN SÁCH DỰ ÁN (BAC)** | **Tổng mức đầu tư Year 0** | **850.000.000** | **100,0%** |

### 1.3.2. Lượng hóa Dòng Tiền Lợi ích Hàng năm (Annual Cash Inflows)
Hệ thống ABC-HRM sau khi vận hành ổn định sẽ mang lại các giá trị kinh tế định lượng trực tiếp hàng năm cho tổ chức:
1. **Tiết kiệm chi phí quỹ lương bộ phận gián tiếp:** Tự động hóa 80% công việc thủ công, tối ưu hóa định biên nhân sự. Công ty không cần tuyển thêm 1 chuyên viên HR bậc trung khi mở rộng quy mô:
   $$B_1 = 15.000.000 \text{ VNĐ/tháng} \times 12 \text{ tháng} = \mathbf{180.000.000 \text{ VNĐ/năm}}$$
2. **Triệt tiêu chi phí sai lệch và phạt pháp lý:** Loại bỏ sai số tính lương thủ công, chấm dứt tình trạng truy thu thuế TNCN hoặc chậm nộp hồ sơ bảo hiểm:
   $$B_2 = \mathbf{50.000.000 \text{ VNĐ/năm}}$$
3. **Tiết kiệm chi phí tuyển dụng và đào tạo do giảm tỷ lệ thôi việc:** Nhờ minh bạch hóa đánh giá KPI, cải thiện trải nghiệm nhân sự, dự kiến giảm tỷ lệ thôi việc tự nguyện từ 18% xuống dưới 12% (giảm bình quân 6 lượt thôi việc/năm; chi phí tuyển dụng và đào tạo bình quân 20 triệu/vị trí):
   $$B_3 = 6 \text{ lượt} \times 20.000.000 \text{ VNĐ} = \mathbf{120.000.000 \text{ VNĐ/năm}}$$

$$\Rightarrow \mathbf{\text{Tổng dòng lợi ích định lượng hàng năm } (CF_t) = B_1 + B_2 + B_3 = 350.000.000 \text{ VNĐ/năm}}$$

### 1.3.3. Bảng Dòng Tiền và Tính toán các Chỉ số Tài chính (Kịch bản Cơ sở)
* **Thời gian thẩm định:** 5 năm (vòng đời công nghệ tiêu chuẩn của hệ thống).
* **Tỷ suất chiết khấu (Discount Rate - $r$):** **10,0%/năm** (chi phí sử dụng vốn bình quân WACC).

Bảng 1.2: Dòng tiền Chiết khấu 5 Năm (Đơn vị tính: Triệu VNĐ):

| Năm ($t$) | Dòng tiền ($CF_t$) | Hệ số chiết khấu $\frac{1}{(1+r)^t}$ | Dòng tiền chiết khấu ($DCF_t$) | Dòng tiền lũy kế chưa CK | Dòng tiền lũy kế có CK |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **Năm 0** | $-850,00$ | 1,0000 | $-850,00$ | $-850,00$ | $-850,00$ |
| **Năm 1** | $+350,00$ | 0,9091 | $+318,18$ | $-500,00$ | $-531,82$ |
| **Năm 2** | $+350,00$ | 0,8264 | $+289,26$ | $-150,00$ | $-242,56$ |
| **Năm 3** | $+350,00$ | 0,7513 | $+262,96$ | $+200,00$ | $+20,40$ |
| **Năm 4** | $+350,00$ | 0,6830 | $+239,06$ | $+550,00$ | $+259,46$ |
| **Năm 5** | $+350,00$ | 0,6209 | $+217,32$ | $+900,00$ | $+476,78$ |
| **Tổng cộng**| | | | **+900,00** | **+476,78** |

### 1.3.4. Kết quả Tính toán Các Chỉ số Hiệu quả Tài chính
1. **Giá trị Hiện tại Thuần (NPV):**
   $$NPV = \sum_{t=1}^{5} \frac{CF_t}{(1 + r)^t} - I_0 = 350 \times 3,79079 - 850 = 1.326,78 - 850 = \mathbf{+476,78 \text{ triệu VNĐ}}$$
   $\rightarrow NPV > 0$: Dự án sinh lời vượt trội, tạo ra giá trị gia tăng lớn cho doanh nghiệp.
2. **Tỷ suất Hoàn vốn Đầu tư (ROI):**
   $$ROI = \frac{\text{Tổng lợi ích sau 5 năm} - \text{Vốn đầu tư ban đầu}}{\text{Vốn đầu tư ban đầu}} \times 100\% = \frac{1.750 - 850}{850} \times 100\% = \mathbf{105,88\%}$$
3. **Thời gian Hoàn vốn Thông thường (PBP):**
   $$PBP_{\text{simple}} = \frac{850}{350} = \mathbf{2,43 \text{ năm (2 năm 5 tháng)}}$$
4. **Thời gian Hoàn vốn Có Chiết khấu (DPBP):**
   $$DPBP = 2 + \frac{|-242,56|}{262,96} = 2 + 0,922 = \mathbf{2,92 \text{ năm (2 năm 11 tháng)}}$$

### 1.3.5. Phân tích Độ nhạy (Sensitivity Analysis)
Để kiểm tra độ an toàn tài chính, nhóm nghiên cứu phân tích trên 3 kịch bản:

Bảng 1.3: Kết quả Phân tích Độ nhạy 3 Kịch bản Tài chính:

| Chỉ tiêu tài chính | Kịch bản Bi quan<br/>*(Dòng tiền giảm 20%)* | Kịch bản Cơ sở<br/>*(Dự báo chuẩn)* | Kịch bản Lạc quan<br/>*(Dòng tiền tăng 15%)* |
|---|:---:|:---:|:---:|
| **Dòng lợi ích hàng năm ($CF_t$)** | **280 triệu VNĐ** | **350 triệu VNĐ** | **402,5 triệu VNĐ** |
| **Tổng lợi ích 5 năm** | 1.400 triệu VNĐ | 1.750 triệu VNĐ | 2.012,5 triệu VNĐ |
| **NPV ($r = 10\%$)** | **+211,42 triệu VNĐ** | **+476,78 triệu VNĐ** | **+675,79 triệu VNĐ** |
| **ROI (5 năm)** | **64,71%** | **105,88%** | **136,76%** |
| **Thời gian hoàn vốn giản đơn** | **3,04 năm** | **2,43 năm** | **2,11 năm** |
| **Thời gian hoàn vốn có CK (DPBP)** | **3,73 năm** | **2,92 năm** | **2,46 năm** |
| **Đánh giá rủi ro** | Khả thi an toàn (NPV vẫn > 200 tr) | Đạt mục tiêu chiến lược | Hiệu quả vượt kỳ vọng |

### 1.3.6. Báo Cáo Phân Tích So Sánh Đối Chiếu 5 Năm: Hiện Trạng (As-Is) vs Áp Dụng ABC-HRM (To-Be)

Để trả lời câu hỏi cốt lõi của Ban Lãnh đạo: *"Nếu áp dụng hệ thống ABC-HRM thì doanh nghiệp được gì, và nếu tiếp tục duy trì phương thức cũ thì hậu quả ra sao trong vòng 5 năm tới?"*, nhóm nghiên cứu xây dựng mô hình phân tích đối chiếu động (Dynamic Comparative Horizon) gắn liền với kế hoạch tăng trưởng nhân sự của Công ty ABC từ **100 nhân sự $\rightarrow$ 120 $\rightarrow$ 150 $\rightarrow$ 175 $\rightarrow$ 200 nhân sự** trong 5 năm:

Bảng 1.3b: Bảng Đối Chiếu Chi Phí & Tổn Thất Tổng Thể 5 Năm (Đơn vị tính: Triệu VNĐ):

| Khoản mục So sánh Đối đầu | Năm 1 *(100 NS)* | Năm 2 *(120 NS)* | Năm 3 *(150 NS)* | Năm 4 *(175 NS)* | Năm 5 *(200 NS)* | TỔNG CỘNG 5 NĂM |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| **KỊCH BẢN A: TIẾP TỤC DÙNG EXCEL & THỦ CÔNG (AS-IS)** | | | | | | |
| 1. Quỹ lương phòng HR *(180 tr/năm/FTE)* | 540 tr *(3 HR)* | 630 tr *(3,5 HR)* | 720 tr *(4 HR)* | 810 tr *(4,5 HR)* | 900 tr *(5 HR)* | **3.600 triệu VNĐ** |
| 2. Tổn thất sai sót lương, phạt thuế & BHXH | 50 tr | 60 tr | 75 tr | 85 tr | 100 tr | **370 triệu VNĐ** |
| 3. Chi phí tuyển dụng do thôi việc cao *(Turnover 18%)* | 360 tr *(18 lượt)* | 440 tr *(22 lượt)* | 540 tr *(27 lượt)* | 640 tr *(32 lượt)* | 720 tr *(36 lượt)* | **2.700 triệu VNĐ** |
| 4. Chi phí thời gian lãng phí sự vụ *(15–25h/tuần)* | 120 tr | 135 tr | 150 tr | 165 tr | 180 tr | **750 triệu VNĐ** |
| **TỔNG CHI PHÍ & TỔN THẤT MÔ HÌNH CŨ (A)** | **1.070 tr** | **1.265 tr** | **1.485 tr** | **1.700 tr** | **1.900 tr** | $\mathbf{7.420 \text{ TRIỆU VNĐ}}$ |
| | | | | | | |
| **KỊCH BẢN B: TRIỂN KHAI HỆ THỐNG ABC-HRM (TO-BE)** | | | | | | |
| 1. Vốn đầu tư ban đầu phát triển hệ thống (Year 0) | 850 tr | 0 tr | 0 tr | 0 tr | 0 tr | **850 triệu VNĐ** |
| 2. Chi phí bảo trì & thuê máy chủ Cloud hàng năm | 48 tr | 55 tr | 65 tr | 75 tr | 85 tr | **328 triệu VNĐ** |
| 3. Quỹ lương phòng HR *(Giữ nguyên 3 HR nhờ tự động)*| 540 tr *(3 HR)* | 540 tr *(3 HR)* | 540 tr *(3 HR)* | 540 tr *(3 HR)* | 540 tr *(3 HR)* | **2.700 triệu VNĐ** |
| 4. Tổn thất sai sót lương, phạt thuế & BHXH | **0 tr** | **0 tr** | **0 tr** | **0 tr** | **0 tr** | **0 triệu VNĐ** |
| 5. Chi phí tuyển dụng *(Turnover giảm còn 12%)* | 240 tr *(12 lượt)* | 280 tr *(14 lượt)* | 360 tr *(18 lượt)* | 420 tr *(21 lượt)* | 480 tr *(24 lượt)* | **1.780 triệu VNĐ** |
| 6. Chi phí thời gian lãng phí sự vụ | **0 tr** | **0 tr** | **0 tr** | **0 tr** | **0 tr** | **0 triệu VNĐ** |
| **TỔNG CHI PHÍ MÔ HÌNH MỚI (B)** | **1.678 tr** | **875 tr** | **965 tr** | **1.035 tr** | **1.105 tr** | $\mathbf{5.658 \text{ TRIỆU VNĐ}}$ |
| | | | | | | |
| $\mathbf{\Delta = \text{SỐ TIỀN TIẾT KIỆM RÒNG CHO DOANH NGHIỆP}}$ | **−608 tr** *(Đầu tư)*| **+390 tr** | **+520 tr** | **+665 tr** | **+795 tr** | $\mathbf{+1.762 \text{ TRIỆU VNĐ}}$ |

$$\mathbf{\text{TỔNG LỢI ÍCH TIẾT KIỆM TÍCH LŨY SAU 5 NĂM}} = 7.420.000.000 - 5.658.000.000 = \mathbf{1.762.000.000 \text{ VNĐ (1,76 TỶ ĐỒNG)}}$$

Bảng 1.3c: So Sánh Các Chỉ Số Hiệu Suất Vận Hành Qua 5 Năm:

| Tiêu chí Đánh giá | Mô hình Cũ: Tiếp tục dùng Excel (As-Is) | Mô hình Mới: Ứng dụng ABC-HRM (To-Be) | Đột phá Đạt được |
|---|---|---|---|
| **Khả năng mở rộng (Scalability)** | **Gãy đổ khi vượt 100 người:** File Excel chậm, xung đột phiên bản, mất công thức, rò rỉ lương. | **Mở rộng mượt mà lên 200–500 nhân sự** nhờ kiến trúc CSDL PostgreSQL và Redis Cache. | Hệ thống vững chắc, không cần đập đi xây lại |
| **Thời gian chốt bảng lương** | Tăng dần từ 3 ngày $\rightarrow$ 5 ngày $\rightarrow$ **7 ngày làm việc** khi lên 200 người. | Duy trì ổn định **$< 30$ giây** tính toán tự động (thực tế test 8,4 giây). | Rút ngắn 99,9% thời gian chờ đợi |
| **Định biên nhân sự quản lý (HR FTE)** | Phải tuyển thêm từ 3 HR lên **5 HR chuyên trách** (tỷ lệ 1 HR / 40 nhân viên). | Giữ nguyên **3 HR** phục vụ tốt 200 nhân sự (tỷ lệ 1 HR / 67 nhân viên). | Tiết kiệm tối thiểu 2 biên chế HR cố định |
| **Tỷ lệ khiếu nại sai lương** | Tăng vọt theo độ phức tạp: Từ 5,2% lên **$8\% - 10\%$**. | Triệt tiêu hoàn toàn về **$0,0\%$**. | 100% nhân viên an tâm cống hiến |
| **Khả năng ra quyết định của Lãnh đạo** | Mất từ 3 đến 5 ngày chờ phòng HR tổng hợp báo cáo thủ công. | Báo cáo trực quan hóa **tức thời (Real-time Dashboard)** trong 3 giây. | Ra quyết định kinh doanh thần tốc |

---

## 1.4. HIẾN CHƯƠNG DỰ ÁN (PROJECT CHARTER)

Hiến chương Dự án là văn bản chính thức ủy quyền cho Quản lý Dự án (PM) huy động nguồn lực tổ chức. Nội dung cốt lõi của Hiến chương Dự án ABC-HRM được thiết lập như sau:

Bảng 1.4: Tóm tắt Nội dung Hiến chương Dự án ABC-HRM:

| Mục Nội dung | Đặc tả Chi tiết trong Hiến chương |
|---|---|
| **Tên dự án & Mã số** | Hệ thống Quản trị Nhân sự Nội bộ Doanh nghiệp (**ABC-HRM**) — Mã: **ABC-HRM-2025** |
| **Nhà tài trợ (Sponsor)** | Ông Nguyễn Văn A — Tổng Giám đốc Công ty Cổ phần ABC |
| **Quản lý Dự án (PM)** | [Họ và tên Học viên 1] — Toàn quyền điều phối kỹ thuật và nhân sự 5 thành viên |
| **Thời gian cam kết** | 24 tuần làm việc (từ 01/11/2025 đến ngày Go-Live chính thức **30/04/2026**) |
| **Tổng ngân sách trần (BAC)** | **850.000.000 VNĐ** (Bao gồm Direct Costs 710 tr, Contingency 106,5 tr, Management Reserve 33,5 tr) |
| **Mục tiêu SMART** | • Hoàn thành 100% 6 phân hệ phần mềm phục vụ 100 cán bộ nhân viên.<br/>• Thời gian chốt lương giảm từ 3 ngày xuống $< 4$ giờ.<br/>• Tỷ lệ sai sót tính lương $< 0,1\%$.<br/>• Tỷ lệ nhân viên tích cực sử dụng đạt $\ge 90\%$ sau 30 ngày Go-Live. |
| **Mốc tiến độ chính** | M1: Kick-off (T3) $\rightarrow$ M2: Xong SRS & Thiết kế (T8) $\rightarrow$ M3: Xong Code 6 Module (T18) $\rightarrow$ M4: Xong UAT (T22) $\rightarrow$ M5: Go-Live (T24) $\rightarrow$ M6: Đóng Dự án (T24). |
| **Thẩm quyền PM** | Chủ động giải ngân trong hạn mức Contingency Reserve (tối đa 20 triệu/hạng mục); điều phối 5 nhân sự; triệu tập phiên họp CCB khi có rủi ro đe dọa PMB. |

---

## 1.5. QUẢN LÝ CÁC BÊN LIÊN QUAN (STAKEHOLDER MANAGEMENT)

Dự án xác định và quản lý danh bạ **10 bên liên quan trọng yếu**:

Bảng 1.5: Sổ Đăng Ký Các Bên Liên Quan (Stakeholder Register):

| Mã | Bên liên quan / Vai trò | Vị trí / Phòng ban | Quyền lực (1–5) | Quan tâm (1–5) | Kỳ vọng cốt lõi | Chiến lược Quản lý |
|:---:|---|---|:---:|:---:|---|:---:|
| **SH-01** | **Nguyễn Văn A** *(Sponsor / Tổng GĐ)* | Ban Giám đốc | **5** | **5** | Đúng hạn 30/04, không vượt 850 tr, có dashboard số liệu nhân sự real-time | **Manage Closely** |
| **SH-02** | **Trần Thị B** *(Trưởng phòng HR)* | Khối Nhân sự | **4** | **5** | Giảm tải sự vụ, tính lương chuẩn xác 100%, quản lý KPI minh bạch | **Manage Closely** |
| **SH-03** | **03 Chuyên viên HR** *(Thao tác nghiệp vụ)* | Khối Nhân sự | **2** | **5** | Giao diện dễ dùng, không nhập liệu trùng lặp, giải phóng tính lương thủ công | **Keep Informed & Involve** |
| **SH-04** | **Lê Văn C** *(Trưởng phòng Kế toán)* | Khối Tài chính | **4** | **3** | Chi phí giải ngân đúng dự toán, bảng lương khớp hạch toán thuế TNCN | **Keep Satisfied** |
| **SH-05** | **Kế toán Tiền lương** | Khối Tài chính | **3** | **4** | Bảng lương xuất file Excel định dạng chuẩn ngân hàng để chuyển khoản | **Keep Informed & Consult** |
| **SH-06** | **Toàn thể 100 Cán bộ Nhân viên** | Toàn công ty | **1** | **3** | Xem công minh bạch, nộp đơn phép online, nhận phiếu lương điện tử bảo mật | **Keep Informed** |
| **SH-07** | **Phạm Quốc D** *(Trưởng phòng CNTT)* | Khối Kỹ thuật | **3** | **4** | Hệ thống bảo mật cao, mã hóa AES-256, dễ bảo trì sau khi bàn giao | **Keep Informed & Consult** |
| **SH-08** | **SysAdmin IT** *(Vận hành máy chủ)* | Khối Kỹ thuật | **2** | **2** | Cấu hình Docker đơn giản, kịch bản backup tự động, tài liệu vận hành rõ | **Monitor** |
| **SH-09** | **Nhà cung cấp Máy chấm công ZKTeco** | Đối tác bên ngoài | **3** | **2** | Cung cấp SDK/API chuẩn, hỗ trợ kỹ thuật theo hợp đồng dịch vụ | **Keep Satisfied** |
| **SH-10** | **Tư vấn Luật Lao động** | Đơn vị bên ngoài | **2** | **1** | Thuật toán tính thuế và trích đóng bảo hiểm tuân thủ Luật Lao động 2019 | **Monitor** |

### Ma trận 2x2 Quyền lực / Quan tâm (Power/Interest Grid):

```
                      MỨC ĐỘ QUYỀN LỰC (POWER / INFLUENCE)
                                  CAO (4 - 5)
                                       ▲
                ┌──────────────────────┼──────────────────────┐
                │   KEEP SATISFIED     │    MANAGE CLOSELY    │
                │  (GIỮ THỎA MÃN)      │  (QUẢN LÝ CHẶT CHẼ)  │
                │ • SH-04: TP Kế toán  │ • SH-01: Tổng GĐ     │
                │   (P=4, I=3)         │   (Sponsor) (P=5,I=5)│
                │                      │ • SH-02: TP Nhân sự  │
                │                      │   (P=4, I=5)         │
         ───────┼──────────────────────┼──────────────────────┼───────► MỨC ĐỘ QUAN TÂM
                │       MONITOR        │    KEEP INFORMED     │         (INTEREST)
                │     (THEO DÕI)       │  (CUNG CẤP THÔNG TIN)│         CAO (4 - 5)
                │ • SH-08: SysAdmin IT │ • SH-03: 03 CV HR    │
                │ • SH-09: NCC ZKTeco  │ • SH-05: Kế toán lương
                │ • SH-10: Tư vấn Luật │ • SH-07: TP CNTT     │
                │                      │ • SH-06: 100 CBNV    │
                └──────────────────────┼──────────────────────┘
                                  THẤP (1 - 3)
```

\newpage

# CHƯƠNG 2: KẾ HOẠCH QUẢN LÝ DỰ ÁN VÀ ĐƯỜNG CƠ SỞ HIỆU SUẤT (PLANNING - PMB)

---

## KHUNG TIẾP CẬN BẢN CHẤT CỦA GIAI ĐOẠN LẬP KẾ HOẠCH

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                             GIAI ĐOẠN LẬP KẾ HOẠCH DỰ ÁN (PLANNING PHASE)                        │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. TẠI SAO LÀM? (WHY)                                                                           │
│    • Lập kế hoạch là giai đoạn quan trọng nhất của quản trị dự án nhằm thiết lập Đường cơ sở    │
│      Đo lường Hiệu suất (Performance Measurement Baseline - PMB), tích hợp đồng thời 3 yếu tố:  │
│      Phạm vi (Scope), Thời gian (Schedule) và Chi phí (Cost).                                    │
│    • Nếu không có PMB chuẩn mực, người quản lý dự án sẽ không có căn cứ để đo lường độ lệch,   │
│      không thể áp dụng kỹ thuật EVM và chắc chắn sẽ đối mặt với thất bại.                        │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 2. LÀM GÌ? (WHAT)                                                                                │
│    • Quản lý Phạm vi: Tuyên bố phạm vi, Danh mục Loại trừ (Exclusions), SRS (12 FR + 6 NFR),     │
│      Ma trận RTM, và Cấu trúc Phân chia Công việc (WBS Cấp 4) kèm Từ điển WBS.                  │
│    • Quản lý Thời gian: Ước tính PERT 3 điểm, Sơ đồ mạng PDM, xác lập Đường Găng (CPM = 24 tuần) │
│      và xây dựng Biểu đồ Gantt.                                                                 │
│    • Quản lý Chi phí: Dự toán Bottom-Up 710 tr, Contingency 15% (106,5 tr) -> Cost Baseline     │
│      816,5 tr, Management Reserve 4% (33,5 tr) -> Tổng BAC 850 tr, và Đường cong S-Curve.       │
│    • Quản lý Nguồn lực & Rủi ro: Ma trận RACI 16 công việc, Sổ đăng ký 12 rủi ro và Kế hoạch    │
│      ứng phó chi tiết với ma trận nhiệt 5x5.                                                     │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 3. LÀM THẾ NÀO? (HOW)                                                                           │
│    • Áp dụng kỹ thuật phân rã WBS định hướng Deliverable theo quy tắc 100%.                     │
│    • Sử dụng thuật toán duyệt thuận/duyệt nghịch Forward & Backward Pass để tính Float và CPM.   │
│    • Sử dụng phương pháp thống kê Beta phân phối để tính kỳ vọng thời gian và độ lệch chuẩn.    │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2.1. QUẢN LÝ PHẠM VI (SCOPE MANAGEMENT)

### 2.1.1. Tuyên Bố Phạm Vi và Danh Mục Loại Trừ (Exclusions)
Nhằm kiểm soát rủi ro lạm phát phạm vi (Scope Creep), dự án xác lập ranh giới cứng:
* **Thuộc phạm vi (In-Scope):** Ứng dụng Web Responsive bao gồm 6 phân hệ cốt lõi; tích hợp thiết bị quét vân tay ZKTeco; chuyển đổi 100% hồ sơ từ Excel sang PostgreSQL; đào tạo người dùng và bảo hành 3 tháng.
* **Loại trừ khỏi phạm vi (Exclusions):**
  1. *Không phát triển Native Mobile App (iOS/Android):* Chỉ hỗ trợ Responsive Web trên trình duyệt di động để tối ưu hóa ngân sách.
  2. *Không tích hợp hai chiều với ERP kế toán bên ngoài (SAP, MISA):* Chỉ xuất file Excel bảng lương chuẩn để kế toán nạp thủ công.
  3. *Không xây dựng phân hệ Đào tạo LMS trực tuyến:* Chuyển sang Giai đoạn 2 (Phase 2).
  4. *Không hỗ trợ đa ngôn ngữ:* Chỉ hỗ trợ Tiếng Việt.
  5. *Không mua sắm thay thế máy chấm công mới:* Tận dụng thiết bị phần cứng ZKTeco hiện có.

### 2.1.2. Đặc Tả Yêu Cầu Chức Năng (12 Functional Requirements)
1. **FR-01 (Quản lý Hồ sơ):** CRUD thông tin nhân viên, mã nhân viên định dạng `ABC-XXXX`, số CCCD, mã số thuế, số BHXH, người phụ thuộc.
2. **FR-02 (Quản lý Hợp đồng):** Quản lý vòng đời hợp đồng thử việc, xác định thời hạn, không xác định thời hạn; quét và tự động gửi email cảnh báo trước 30 ngày hết hạn.
3. **FR-03 (Tích hợp Chấm công):** Nhận dữ liệu chấm công từ máy quét vân tay ZKTeco qua giao thức Socket/Webhook theo thời gian thực (độ trễ $< 5$ giây).
4. **FR-04 (Quản lý Đơn từ Online):** Nộp và duyệt đơn nghỉ phép năm, nghỉ ốm, làm ngoài giờ (OT) theo quy trình duyệt 2 cấp (Manager $\rightarrow$ HR Head).
5. **FR-05 (Tổng hợp Bảng công):** Tự động tổng hợp số công chuẩn, công thực tế, giờ OT, ngày nghỉ phép có lương/không lương.
6. **FR-06 (Động cơ Tính lương Gross-Net):** Tính toán lương thực nhận (Net) theo công thức cấu hình tham số linh hoạt.
7. **FR-07 (Khấu trừ Thuế & Bảo hiểm):** Tự động tính trích nộp BHXH (8%), BHYT (1,5%), BHTN (1%) và thuế TNCN lũy tiến từng phần 7 bậc theo luật Việt Nam.
8. **FR-08 (Xuất Phiếu lương PDF):** Tự động sinh phiếu lương cá nhân định dạng PDF có mật khẩu mã hóa (6 số cuối CCCD) và gửi email tự động.
9. **FR-09 (Quản lý Tuyển dụng):** Quản lý định biên, đăng tin tuyển dụng và theo dõi phễu ứng viên (Pipeline).
10. **FR-10 (Onboarding Nhân sự Mới):** Checklist tự động giao việc cấp máy tính, cấp tài khoản email, bàn giao chỗ ngồi.
11. **FR-11 (Quản trị Hiệu suất KPI):** Thiết lập chỉ tiêu, đánh giá 360 độ định kỳ và xếp loại A/B/C/D.
12. **FR-12 (Executive Dashboard & RBAC):** Báo cáo trực quan hóa nhân sự/quỹ lương cho Ban Giám đốc; phân quyền bảo mật 5 vai trò.

### 2.1.3. Đặc Tả Yêu Cầu Phi Chức Năng (6 Non-Functional Requirements)
* **NFR-01 (Hiệu năng):** Tải trang $< 1,5$s; tính toán bảng lương 100 người $< 30$s; hỗ trợ 50 người dùng đồng thời.
* **NFR-02 (Bảo mật):** Băm mật khẩu Bcrypt (Salt rounds = 12); mã hóa cột lương AES-256; xác thực 2FA cho Admin; chống OWASP Top 10.
* **NFR-03 (Khả dụng):** Uptime $\ge 99,5\%$ giờ hành chính; Daily backup lúc 02h00; RPO $\le 24$h, RTO $\le 4$h.
* **NFR-04 (Khả mở rộng):** Kiến trúc tách rời Modular cho phép mở rộng lên 500 nhân sự không cần refactor code.
* **NFR-05 (Tương thích):** Hoạt động mượt mà trên Chrome, Edge, Safari; hiển thị Responsive trên thiết bị di động.
* **NFR-06 (Tuân thủ Pháp lý):** Tuân thủ Bộ luật Lao động 2019, Luật BHXH 2014 và Luật Thuế TNCN hiện hành.

---

## 2.2. CẤU TRÚC PHÂN CHIA CÔNG VIỆC (WBS) VÀ TỪ ĐIỂN WBS

WBS của dự án được phân rã định hướng sản phẩm bàn giao (Deliverable-oriented) đến Cấp độ 4 theo quy tắc 100%:

```
1.0 HỆ THỐNG ABC-HRM (Cấp 1 - Dự án)
├── 1.1 Quản lý Dự án (1.1.1 Khởi tạo | 1.1.2 Lập kế hoạch | 1.1.3 Giám sát EVM/CCB | 1.1.4 Đóng dự án)
├── 1.2 Khảo sát & Phân tích (1.2.1 Hiện trạng Excel | 1.2.2 SRS & RTM | 1.2.3 Wireframe UI/UX)
├── 1.3 Thiết kế Kỹ thuật (1.3.1 Kiến trúc 3 lớp & An ninh | 1.3.2 CSDL ERD 3NF | 1.3.3 Mockup Figma)
├── 1.4 Phát triển Phần mềm (1.4.1 Hồ sơ | 1.4.2 Chấm công | 1.4.3 Tính lương | 1.4.4 Tuyển dụng | 1.4.5 KPI | 1.4.6 Dashboard)
├── 1.5 Kiểm thử Chất lượng (1.5.1 Unit/Integration | 1.5.2 Load Test | 1.5.3 Security | 1.5.4 Nghiệm thu UAT)
├── 1.6 Triển khai & Đào tạo (1.6.1 Cloud Production & CI/CD | 1.6.2 Di chuyển Dữ liệu ETL | 1.6.3 Đào tạo HR/User | 1.6.4 Go-Live)
└── 1.7 Bàn giao & Bảo hành (1.7.1 Chuyển giao Git & Ops Manual | 1.7.2 Bảo hành 3 tháng | 1.7.3 Quyết toán Tài chính)
```

Bảng 2.1: Trích lược Từ Điển WBS (WBS Dictionary) Các Gói Công Việc Trọng Yếu:

| Mã WBS | Tên Gói Công việc | Mô tả Kỹ thuật | Sản phẩm Bàn giao | Người chịu TN (RACI) | Thời lượng | Dự toán Chi phí (VNĐ) | Tiêu chí Nghiệm thu |
|:---:|---|---|---|:---:|:---:|---:|---|
| **1.4.2.1** | Adapter SDK Chấm công | Viết Socket Service kết nối máy ZKTeco | Module mã nguồn SDK | Senior Dev *(R)* | 12 ngày | 21.000.000 | Quét vân tay, log đẩy về web $< 5$ giây |
| **1.4.3.1** | Engine Tính lương Gross-Net | Lập trình engine tính lương Gross-to-Net | Module Payroll Engine | Senior Dev *(R)* | 15 ngày | 26.250.000 | Pass 100% test cases mẫu; sai số 0% |
| **1.4.3.2** | Khấu trừ Bảo hiểm & Thuế | Thuật toán tính trần BHXH và thuế TNCN 7 bậc | Logic Deductions | Dev 1 *(R)* | 8 ngày | 10.000.000 | Khớp tuyệt đối bảng tính tay kế toán |
| **1.5.4.2** | Tổ chức Đợt Kiểm thử UAT | Điều phối HR và Kế toán thử nghiệm 50 kịch bản | Defect Log & Biên bản UAT| PM & BA *(R)* | 5 ngày | 6.000.000 | 100% test case pass; 0 lỗi Critical |
| **1.6.2.1** | ETL Di chuyển Dữ liệu | Viết script chuyển đổi từ 15 file Excel | Script ETL + Báo cáo | Senior Dev *(R)* | 5 ngày | 8.750.000 | 100% hồ sơ nạp thành công, 0% mất mát |

---

## 2.3. QUẢN LÝ THỜI GIAN: PERT, SƠ ĐỒ MẠNG PDM VÀ ĐƯỜNG GĂNG (CPM)

### 2.3.1. Bảng Ước Tính Ba Điểm PERT (13 Hoạt động Cốt lõi)
Áp dụng công thức: $T_e = \frac{O + 4M + P}{6}$ và $\sigma^2 = \left( \frac{P - O}{6} \right)^2$:

Bảng 2.2: Tính toán Thời lượng Kỳ vọng PERT:

| Mã | Hoạt động Dự án | Tiền nhiệm | $O$ *(Lạc quan)* | $M$ *(Khả dĩ)* | $P$ *(Bi quan)* | $T_e$ *(ngày)* | Phương sai $\sigma^2$ |
|:---:|---|:---:|:---:|:---:|:---:|:---:|:---:|
| **A** | Khảo sát Hiện trạng & Đặc tả SRS | — | 8,0 | 12,0 | 20,0 | **12,67** | 4,00 |
| **B** | Thiết kế Kiến trúc Hệ thống & CSDL | A | 5,0 | 8,0 | 14,0 | **8,50** | 2,25 |
| **C** | Thiết kế Giao diện Chi tiết UI/UX | A | 5,0 | 7,0 | 12,0 | **7,50** | 1,36 |
| **D** | Lập trình Module Hồ sơ Nhân sự | B, C | 8,0 | 10,0 | 15,0 | **10,50** | 1,36 |
| **E** | Lập trình Module Chấm công & SDK | B | 10,0 | 14,0 | 22,0 | **14,67** | 4,00 |
| **F** | Lập trình Module Tính lương & Thuế | E | 12,0 | 18,0 | 28,0 | **18,67** | 7,11 |
| **G** | Lập trình Tuyển dụng & Onboarding | D (SS) | 6,0 | 8,0 | 12,0 | **8,33** | 1,00 |
| **H** | Lập trình Module Quản trị KPI | D | 8,0 | 10,0 | 16,0 | **10,67** | 1,78 |
| **I** | Lập trình Dashboard & Báo cáo | F, H | 6,0 | 8,0 | 14,0 | **8,67** | 1,78 |
| **J** | Kiểm thử Tích hợp & Kiểm thử Tải | D, F, G, I | 8,0 | 12,0 | 18,0 | **12,33** | 2,78 |
| **K** | Kiểm thử Nghiệm thu UAT | J | 5,0 | 7,0 | 10,0 | **7,17** | 0,69 |
| **L** | Cài đặt Production & Di chuyển DL | K | 3,0 | 5,0 | 10,0 | **5,50** | 1,36 |
| **M** | Đào tạo Người dùng & Go-Live | L | 3,0 | 5,0 | 7,0 | **5,00** | 0,44 |

### 2.3.2. Tính Toán Thông Số CPM và Xác Lập Đường Găng

Bảng 2.3: Bảng Thông số Sớm/Muộn và Phân tích Float:

| Mã | Hoạt động | $T_e$ | $ES$ | $EF$ | $LS$ | $LF$ | Total Float ($TF$) | Trạng thái |
|:---:|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **A** | Khảo sát & SRS | 12,67 | **0,00** | **12,67** | **0,00** | **12,67** | **0,00** | **GĂNG (Critical)** |
| **B** | Kiến trúc & DB | 8,50 | **12,67** | **21,17** | **12,67** | **21,17** | **0,00** | **GĂNG (Critical)** |
| **C** | UI/UX Mockup | 7,50 | 12,67 | 20,17 | 13,67 | 21,17 | 1,00 | Không găng (Float 1d) |
| **D** | Dev Hồ sơ NS | 10,50 | 21,17 | 31,67 | 39,34 | 49,84 | 18,17 | Không găng (Float 18,17d) |
| **E** | Dev Chấm công & SDK | 14,67 | **21,17** | **35,84** | **21,17** | **35,84** | **0,00** | **GĂNG (Critical)** |
| **F** | Dev Tính lương | 18,67 | **35,84** | **54,51** | **35,84** | **54,51** | **0,00** | **GĂNG (Critical)** |
| **G** | Dev Tuyển dụng | 8,33 | 25,00 | 33,33 | 41,51 | 49,84 | 16,51 | Không găng (Float 16,51d) |
| **H** | Dev Quản trị KPI | 10,67 | 31,67 | 42,34 | 35,17 | 45,84 | 3,50 | Không găng (Float 3,50d) |
| **I** | Dev Dashboard | 8,67 | 54,51 | 63,18 | 54,51 | 63,18 | 8,66 | Không găng (Float 8,66d) |
| **J** | Kiểm thử Tích hợp | 12,33 | **54,51** | **66,84** | **54,51** | **66,84** | **0,00** | **GĂNG (Critical)** |
| **K** | Nghiệm thu UAT | 7,17 | **66,84** | **74,01** | **66,84** | **74,01** | **0,00** | **GĂNG (Critical)** |
| **L** | Production & Di chuyển DL | 5,50 | **74,01** | **79,51** | **74,01** | **79,51** | **0,00** | **GĂNG (Critical)** |
| **M** | Đào tạo & Go-Live | 5,00 | **79,51** | **84,51** | **79,51** | **84,51** | **0,00** | **GĂNG (Critical)** |

* **Đường Găng (Critical Path):** $\mathbf{A \longrightarrow B \longrightarrow E \longrightarrow F \longrightarrow J \longrightarrow K \longrightarrow L \longrightarrow M}$
* **Tổng thời lượng đường găng:** $\mathbf{84,51 \text{ ngày làm việc}} \approx \mathbf{24 \text{ tuần (6 tháng)}}$.
* **Luận giải cốt lõi:** Phân hệ Chấm công (E) và Tính lương (F) bắt buộc nằm trên đường găng vì mối quan hệ phụ thuộc dữ liệu Finish-to-Start (FS): Lương không thể tính được nếu thiếu bảng công đối soát. Bất kỳ sự chậm trễ nào tại E và F đều trực tiếp làm trễ ngày Go-Live toàn công ty.

---

## 2.4. QUẢN LÝ CHI PHÍ: DỰ TOÁN BOTTOM-UP VÀ ĐƯỜNG CƠ SỞ S-CURVE

* Chi phí Nhân công trực tiếp (5 vị trí trong 6 tháng): **575.000.000 VNĐ**
* Chi phí Phi nhân công (Cloud, Bản quyền, Tích hợp ZKTeco, Đào tạo): **135.000.000 VNĐ**
* **Tổng Chi phí Ước tính Trực tiếp:** **710.000.000 VNĐ**
* **Dự trữ Dự phòng (Contingency Reserve - 15%):** **106.500.000 VNĐ**
* $\mathbf{\text{ĐƯỜNG CƠ SỞ CHI PHÍ (COST BASELINE):}}$ **816.500.000 VNĐ**
* **Dự trữ Quản lý (Management Reserve - ~4%):** **33.500.000 VNĐ**
* $\mathbf{\text{TỔNG NGÂN SÁCH DỰ ÁN (BAC):}}$ **850.000.000 VNĐ**

Bảng 2.4: Phân Bổ Dòng Tiền Tích Lũy S-Curve (Đơn vị tính: Triệu VNĐ):

| Tháng | Giai đoạn WBS Trọng tâm | Chi phí Tháng ($PV_m$) | Lũy kế Kế hoạch ($\sum PV$) | Tỷ lệ Hoàn thành Lũy kế (%) |
|:---:|---|---:|---:|:---:|
| **Tháng 1** | Khởi tạo, Khảo sát, SRS (WBS 1.1, 1.2) | 85,0 tr | 85,0 tr | **10,4%** |
| **Tháng 2** | Kiến trúc, CSDL ERD, Mockup UI (WBS 1.3) | 110,0 tr | 195,0 tr | **23,9%** |
| **Tháng 3** | Dev Hồ sơ, Chấm công & SDK ZKTeco (WBS 1.4.1, 1.4.2) | 165,0 tr | 360,0 tr | **44,1%** |
| **Tháng 4** | Dev Tính lương, Tuyển dụng, KPI (WBS 1.4.3, 1.4.4, 1.4.5) | 185,0 tr | 545,0 tr | **66,7%** |
| **Tháng 5** | Dev Dashboard, Kiểm thử Tích hợp & Tải (WBS 1.4.6, 1.5) | 150,0 tr | 695,0 tr | **85,1%** |
| **Tháng 6** | UAT, Di chuyển DL, Đào tạo & Go-Live (WBS 1.6, 1.7) | 121,5 tr | 816,5 tr | **100,0%** |

---

## 2.5. QUẢN LÝ NGUỒN NHÂN LỰC: MA TRẬN RACI VÀ ĐỘNG LỰC CNTT

Bảng 2.5: Ma Trận RACI Dự Án ABC-HRM:

| Công việc Chính (WBS) | PM | BA | Sr Dev | Dev 1 | Dev 2 | QA | HRM | ITL |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Business Case & Charter | **A/R** | C | I | I | I | I | C | I |
| Khảo sát & SRS | A | **R** | C | I | I | C | C | I |
| Thiết kế Kiến trúc & CSDL | A | C | **R** | C | I | I | I | C |
| Thiết kế UI/UX Mockup | A | C | C | I | **R** | I | C | I |
| Dev Module Chấm công & SDK | A | I | **R** | C | C | I | I | C |
| Dev Module Tính lương & Thuế | A | C | **R** | C | C | I | C | I |
| Dev Module Tuyển dụng, KPI | A | I | C | **R** | C | I | I | I |
| Kiểm thử Tích hợp & Tải | A | I | C | C | C | **R** | I | C |
| Nghiệm thu UAT | A | **R** | C | I | I | C | **R** | I |
| Di chuyển Dữ liệu ETL | A | C | **R** | C | I | C | C | I |
| Đào tạo & Go-Live | **A** | **R** | C | I | I | I | C | C |

* **Giải tỏa rủi ro phụ thuộc Senior Dev:** Bắt buộc áp dụng Pair-Programming với Dev 1 ở phân hệ Chấm công và Tính lương; 100% mã nguồn phải qua Pull Request review trước khi merge.
* **Động lực nội tại (Daniel Pink):** Tự chủ (Autonomy trong giải pháp kỹ thuật), Tinh thông (Mastery tech-stack hiện đại), Mục đích (Purpose giải phóng sự vụ cho 100 đồng nghiệp).

---

## 2.6. QUẢN LÝ RỦI RO: SỔ ĐĂNG KÝ 12 RỦI RO VÀ MA TRẬN NHIỆT

Bảng 2.6: Sổ Đăng Ký 12 Rủi Ro Dự Án (Risk Register):

| Mã | Phân loại | Tên Rủi ro | $P$ (1–5) | $I$ (1–5) | Điểm | Chiến lược | Hành động Ứng phó Cụ thể | Risk Owner |
|:---:|---|---|:---:|:---:|:---:|:---:|---|:---:|
| **R1** | Nhân sự | Senior Dev nghỉ việc đột xuất | 3 | 5 | **15** *(Đỏ)* | Giảm thiểu | Pair-programming với Dev 1, review code 100%, thưởng dự án | PM |
| **R2** | Pháp lý | Luật thuế TNCN hoặc trần BHXH thay đổi | 3 | 4 | **12** *(Vàng)* | Giảm thiểu | Thiết kế Rule-Engine tham số động, không hard-code | BA & Sr Dev |
| **R3** | Kỹ thuật | SDK máy chấm công ZKTeco lỗi kết nối | 4 | 4 | **16** *(Đỏ)* | Giảm thiểu | Làm PoC sớm Tuần 2, chuẩn bị cơ chế nạp CSV, thuê chuyên gia | Sr Dev |
| **R4** | Phạm vi | Lạm phát phạm vi (Scope Creep) từ HR/Sponsor | 4 | 5 | **20** *(Đỏ)* | Tránh né | Đóng băng phạm vi sau SRS; kiểm soát nghiêm qua CCB | PM & BA |
| **R5** | Dữ liệu | Dữ liệu Excel cũ bị trùng số CCCD | 4 | 3 | **12** *(Vàng)* | Giảm thiểu | Thành lập tổ làm sạch dữ liệu từ Tháng 1, HR ký chuẩn hóa | BA & Dev 1 |
| **R6** | Tổ chức | Nhân viên ngại thay đổi không chịu dùng | 3 | 3 | **9** *(Vàng)* | Giảm thiểu | Video clip 3 phút, ban hành quy chế duyệt phép 100% online | PM & HRM |
| **R7** | Hiệu năng | Nghẽn mạng khi 100 người xem lương cùng lúc | 2 | 4 | **8** *(Vàng)* | Giảm thiểu | Redis cache, tối ưu chỉ mục index CSDL, Load test JMeter | Sr Dev & QA |
| **R8** | Bảo mật | Lộ lọt thông tin lương và CCCD nhân viên | 3 | 5 | **15** *(Đỏ)* | Giảm thiểu | Mã hóa AES-256 cột lương, 2FA Admin, pentest OWASP Top 10 | Tech Lead |
| **R9** | Tiến độ | HR/Kế toán chậm trễ nghiệm thu UAT | 3 | 3 | **9** *(Vàng)* | Giảm thiểu | Thỏa thuận SLA phản hồi 48h, lịch review cố định 2 buổi/tuần | PM & BA |
| **R10**| Hạ tầng | Cloud VPS sập nguồn vào ngày Go-Live | 2 | 5 | **10** *(Vàng)* | Chuyển giao | Thuê Cloud SLA 99,9%, backup hàng ngày, sẵn sàng Staging | SysAdmin |
| **O11**| Cơ hội | Mở rộng thêm 2 chi nhánh (+80 nhân sự) | 3 | 3 | **9** *(Vàng)* | Khai thác | Thiết kế CSDL multi-branch, đề xuất ký HĐ mở rộng Phase 2 | PM & BA |
| **O12**| Cơ hội | Team làm chủ toàn diện tech-stack mới | 4 | 2 | **8** *(Vàng)* | Tăng cường | Đóng gói thư viện nội bộ NPM, tổ chức Tech-sharing | Sr Dev |

\newpage

# CHƯƠNG 3: GIAI ĐOẠN THỰC HIỆN, GIÁM SÁT VÀ KIỂM SOÁT DỰ ÁN (EXECUTION & M&C)

---

## KHUNG TIẾP CẬN BẢN CHẤT CỦA GIAI ĐOẠN GIÁM SÁT & KIỂM SOÁT

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                   GIAI ĐOẠN GIÁM SÁT & KIỂM SOÁT DỰ ÁN (MONITORING & CONTROLLING)                │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. TẠI SAO LÀM? (WHY)                                                                           │
│    • Mọi kế hoạch dù hoàn hảo đến đâu cũng sẽ xuất hiện sai lệch khi bước vào thực tế triển khai.│
│    • Nếu không có hệ thống đo lường hiệu suất định lượng (EVM) và quy trình kiểm soát thay đổi  │
│      tích hợp (CCB), dự án sẽ bị trôi dạt tự do, vượt ngân sách và trễ hạn mà không thể cứu vãn. │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 2. LÀM GÌ? (WHAT)                                                                                │
│    • Vận hành Hội đồng CCB: Xử lý 02 Yêu cầu Thay đổi (CR-001 duyệt, CR-002 bác bỏ dời Phase 2). │
│    • Tính toán và phân tích 10 chỉ số EVM tại 2 mốc báo cáo bắt buộc (15/10 và 20/10).           │
│    • Báo cáo Tình trạng Đèn Giao Thông và giải quyết dứt điểm 3 vấn đề trong Issue Log.          │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 3. LÀM THẾ NÀO? (HOW)                                                                           │
│    • Sử dụng các công thức chuẩn: CV, SV, CPI, SPI, EAC, TCPI.                                   │
│    • Áp dụng kỹ thuật phân tích nguyên nhân sâu xa (Root Cause Analysis) và Kế hoạch can thiệp   │
│      điều chỉnh (Fast-tracking, huy động chuyên gia ZKTeco từ Quỹ Dự phòng).                     │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 3.1. QUẢN LÝ THAY ĐỔI TÍCH HỢP VÀ HỘI ĐỒNG CCB

Hội đồng Kiểm soát Thay đổi (CCB) bao gồm: Tổng Giám đốc (Chủ tịch), Quản lý Dự án, Trưởng phòng HR, Trưởng phòng Kế toán và Technical Lead.

### Phân Tích 02 Yêu Cầu Thay Đổi Giả Định Điển Hình:
1. **Yêu cầu CR-001 (Được Duyệt):** Trưởng phòng HR đề xuất ngày 15/01/2026 bổ sung tính năng *"Tự động cảnh báo hợp đồng hết hạn trước 30 ngày kèm tạo draft phụ lục gia hạn"*.
   - *Phân tích tác động:* Phạm vi tăng nhẹ 1 Cron-job; Thời gian phát triển +3 ngày (nằm trong Float của module Hồ sơ = 18 ngày, **không làm thay đổi đường găng và ngày Go-live**); Chi phí phát sinh 5.500.000 VNĐ (trích từ Quỹ Dự phòng).
   - *Quyết định CCB:* **PHÊ DUYỆT (Approved)** vì giá trị nghiệp vụ cao và rủi ro pháp lý giảm mạnh. Cập nhật Baseline $BAC = 822$ triệu VNĐ.
2. **Yêu cầu CR-002 (Bị Bác Bỏ):** Tổng Giám đốc đề xuất ngày 10/02/2026 bổ sung *"Phân hệ Quản lý Đào tạo Nội bộ (LMS trắc nghiệm online)"*.
   - *Phân tích tác động:* Phạm vi tăng 1 phân hệ lớn (8 màn hình, 12 bảng DB); Thời gian phát triển **+20 ngày công (4 tuần)** làm trễ ngày Go-Live từ 30/04 sang cuối tháng 5; Chi phí phát sinh **85.000.000 VNĐ** (vượt số dư quỹ dự phòng và trần ngân sách 850 triệu).
   - *Quyết định CCB:* **BÁC BỎ / DỜI LẠI (Rejected / Deferred)** nhằm bảo vệ tính toàn vẹn của Đường cơ sở Hiệu suất PMB; chuyển toàn bộ sang Giai đoạn 2 (Phase 2).

Bảng 3.1: Nhật Ký Theo Dõi Thay Đổi Dự Án (Change Log):

| Mã CR | Ngày | Người đề xuất | Mô tả Yêu cầu | Tác động Tiến độ | Tác động Chi phí | Quyết định CCB | Trạng thái |
|:---:|:---:|:---:|---|:---:|:---:|:---:|:---:|
| **CR-001** | 15/01/2026 | Trần Thị B *(HR)* | Cảnh báo tự động hợp đồng hết hạn 30 ngày | +3 ngày *(Float = 18d)* | +5.500.000 VNĐ | **APPROVED** | Đã hoàn thành |
| **CR-002** | 10/02/2026 | Nguyễn Văn A *(Sponsor)* | Xây dựng phân hệ Đào tạo LMS online | +20 ngày *(Trễ 4 tuần)* | +85.000.000 VNĐ | **REJECTED** | Chuyển Phase 2 |

---

## 3.2. BÁO CÁO GIÁ TRỊ THU ĐƯỢC (EVM) TẠI HAI THỜI ĐIỂM

Baseline áp dụng sau CR-001: **$BAC = 822.000.000$ VNĐ**.

Bảng 3.2: Bảng Tính Toán và So Sánh Chỉ Số EVM tại Hai Mốc Báo Cáo:

| Chỉ số EVM | Công thức Toán học | Mốc 1: Ngày 15/10 (Tuần 14) | Mốc 2: Ngày 20/10 (Tuần 18) | Đánh giá Xu hướng Phục hồi |
|---|---|:---:|:---:|---|
| **Kế hoạch hoàn thành** | Mục tiêu phân bổ lịch trình | **58,0%** | **75,0%** | Bước vào giai đoạn tăng tốc |
| **Thực tế hoàn thành** | Khối lượng nghiệm thu thực tế | **55,0%** | **74,0%** | Tốc độ thực tế vượt tốc độ kế hoạch |
| **Planned Value (PV)** | $PV = \% \text{ Kế hoạch} \times BAC$ | **476.760.000 VNĐ** | **616.500.000 VNĐ** | Chuẩn đo lường kế hoạch |
| **Earned Value (EV)** | $EV = \% \text{ Thực tế} \times BAC$ | **452.100.000 VNĐ** | **608.280.000 VNĐ** | Giá trị công việc tạo ra |
| **Actual Cost (AC)** | Chi phí thực tế giải ngân | **470.000.000 VNĐ** | **612.000.000 VNĐ** | Ghi nhận chi tiêu thực tế |
| **Cost Variance (CV)** | $CV = EV - AC$ | **−17.900.000 VNĐ** *(Vượt chi)* | **−3.720.000 VNĐ** | ✅ **Giảm 79,2% mức vượt chi** |
| **Schedule Variance (SV)**| $SV = EV - PV$ | **−24.660.000 VNĐ** *(Chậm trễ)* | **−8.220.000 VNĐ** | ✅ **Bù đắp 66,7% độ trễ tiến độ** |
| **Cost Performance (CPI)**| $CPI = \frac{EV}{AC}$ | **0,962** *(Dưới chuẩn)* | **0,994** *(Tiệm cận 1,0)* | ✅ **Hiệu suất chi phí phục hồi ngoạn mục** |
| **Schedule Perf. (SPI)** | $SPI = \frac{EV}{PV}$ | **0,948** *(Chậm 5,2%)* | **0,987** *(Đạt 98,7%)* | ✅ **Tiến độ bắt kịp kế hoạch** |
| **Dự báo Chi phí (EAC)** | $EAC = \frac{BAC}{CPI}$ | **854.469.854 VNĐ** *(Cảnh báo)* | **826.961.770 VNĐ** *(An toàn)* | ✅ **Chi phí cuối cùng nằm an toàn trong BAC** |
| **Chỉ số Cần đạt (TCPI)**| $TCPI = \frac{BAC - EV}{BAC - AC}$ | **1,051** *(Áp lực cao)* | **1,018** *(Áp lực thấp)* | ✅ **Dự án trở lại tầm kiểm soát** |

### Luận Giải Diễn Biến và Hành Động Điều Chỉnh:
* **Tại Mốc 15/10 (Cảnh báo Vàng):** Rủi ro R3 xảy ra khi Socket kết nối máy chấm công ZKTeco bị lỗi Keep-Alive, làm phát sinh 5 ngày công sửa chữa ngoài kế hoạch $\rightarrow CPI = 0,962$ và $SPI = 0,948$. PM ban hành ngay 3 hành động can thiệp: (1) Kích hoạt 15 triệu dự phòng thuê chuyên gia ZKTeco xử lý dứt điểm socket; (2) Áp dụng Fast-tracking lập trình song song giao diện Tuyển dụng/KPI; (3) Pair-programming đẩy tiến độ phân hệ Tính lương.
* **Tại Mốc 20/10 (Phục hồi Xanh):** Các biện pháp điều chỉnh phát huy hiệu quả xuất sắc, đưa $CPI$ lên **0,994** và $SPI$ lên **0,987**. Dự báo chi phí hoàn thành $EAC \approx 826,96$ triệu VNĐ nằm an toàn dưới trần ngân sách 850 triệu.

---

## 3.3. BÁO CÁO TÌNH TRẠNG ĐÈN GIAO THÔNG VÀ SỔ THEO DÕI VẤN ĐỀ

Bảng 3.3: Báo Cáo Tình Trạng Đèn Giao Thông (Traffic Light Status Report):

| Lĩnh vực Quản trị | Trạng thái tại Mốc 15/10 | Trạng thái tại Mốc 20/10 | Nhận xét Tiến trình Quản trị |
|---|:---:|:---:|---|
| **Phạm vi (Scope)** | 🟢 **XANH** | 🟢 **XANH** | Phạm vi ổn định tuyệt đối; CR-001 kiểm soát tốt; CR-002 bác bỏ dời Phase 2 |
| **Tiến độ (Schedule)** | 🟡 **VÀNG** *(SPI = 0,948)* | 🟢 **XANH** *(SPI = 0,987)* | Khắc phục xong độ trễ máy chấm công; bắt kịp tiến độ đường găng |
| **Chi phí (Cost)** | 🟡 **VÀNG** *(CPI = 0,962)* | 🟢 **XANH** *(CPI = 0,994)* | Vượt chi giảm từ -17,9 tr xuống -3,7 tr; dự báo EAC an toàn |
| **Kỹ thuật / Chất lượng** | 🟡 **VÀNG** *(Lỗi Socket)* | 🟢 **XANH** *(Unit Test 87%)* | Hoàn thành sửa lỗi SDK; pass 100% kiểm thử phân hệ tính lương |

Bảng 3.4: Sổ Theo Dõi Vấn Đề Phát Sinh Thực Tế (Issue Log):

| Mã Issue | Ngày ghi | Mô tả Vấn đề Kỹ thuật / Vận hành | Mức độ | Người xử lý | Giải pháp Khắc phục Đã Thực hiện | Ngày Đóng | Trạng thái |
|:---:|:---:|---|:---:|:---:|---|:---:|:---:|
| **ISS-001** | 08/01/2026 | Adapter chấm công mất kết nối Socket với ZKTeco sau mỗi 6 giờ hoạt động. | **Cao** | Senior Dev | Thuê chuyên gia ZKTeco, bổ sung cơ chế Heartbeat ping 30s và Auto-reconnect. | 18/01/2026 | ✅ **CLOSED** |
| **ISS-002** | 20/01/2026 | Dữ liệu Excel cũ có 12 nhân viên bị trùng số CCCD và thiếu mã số thuế cá nhân. | **Vừa** | BA & Dev 1 | Xuất danh sách đối soát trực tiếp với HR; chuẩn hóa mã nhân viên `ABC-XXXX`. | 23/01/2026 | ✅ **CLOSED** |
| **ISS-003** | 15/02/2026 | Thuật toán tính thuế TNCN tính sai giảm trừ cho người phụ thuộc sinh giữa năm. | **Cao** | Senior Dev | Bổ sung trường `start_month`, viết lại logic giảm trừ theo số tháng thực tế. | 17/02/2026 | ✅ **CLOSED** |

\newpage

# CHƯƠNG 4: GIAI ĐOẠN KẾT THÚC DỰ ÁN VÀ BÀI HỌC KINH NGHIỆM (CLOSING)

---

## KHUNG TIẾP CẬN BẢN CHẤT CỦA GIAI ĐOẠN KẾT THÚC

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                             GIAI ĐOẠN KẾT THÚC DỰ ÁN (PROJECT CLOSING)                           │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. TẠI SAO LÀM? (WHY)                                                                           │
│    • Đóng dự án là bước thủ tục pháp lý bắt buộc để chuyển giao sản phẩm, thanh lý hợp đồng và   │
│      bảo toàn tri thức tổ chức (Organizational Process Assets - OPAs).                           │
│    • Nếu không tổ chức họp tổng kết bài học kinh nghiệm, các sai lầm trong ước tính và kỹ thuật  │
│      sẽ tiếp tục lặp lại ở các dự án tiếp theo của công ty.                                      │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 2. LÀM GÌ? (WHAT)                                                                                │
│    • Tổ chức họp Retrospective, đóng gói 4 bài học Hữu hình (Explicit) và 3 bài học Vô hình      │
│      (Tacit Knowledge).                                                                          │
│    • Lập Báo cáo Đóng Dự án Cuối cùng (Final Closure Report) đối chiếu 5 tiêu chí PMB.           │
│    • Thực hiện Bàn giao Sản phẩm, Kế hoạch Giải tán Nhóm, Quyết toán Tài chính và ký Biên bản    │
│      Chấp thuận Nghiệm thu Chính thức (Formal Acceptance Sign-off).                              │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 3. LÀM THẾ NÀO? (HOW)                                                                           │
│    • Đối chiếu định lượng chi phí thực tế giải ngân (826,96 triệu VNĐ < BAC 850 triệu VNĐ).      │
│    • Bàn giao mã nguồn Git, tài liệu Ops Manual, User Guide và ký biên bản nghiệm thu 4 bên.     │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 4.1. BÀI HỌC KINH NGHIỆM DỰ ÁN (LESSONS LEARNED & RETROSPECTIVE)

### 4.1.1. Khối Tri Thức Hữu Hình (Explicit Knowledge)
1. **Quy tắc Đệm 25% cho Module Pháp lý / Tài chính:** Module Tính lương bị thiếu 20% công sức ban đầu do phức tạp về thuế. Hành động chuẩn hóa: Mọi module tài chính/thuế trong tương lai bắt buộc phải cộng thêm hệ số dự phòng kỹ thuật tối thiểu **$25\%$ thời lượng**.
2. **Quy chuẩn Thử nghiệm Tích hợp Sớm (Sprint 0 PoC):** Mất 10 ngày xử lý SDK máy chấm công do tài liệu thiếu Keep-Alive. Hành động chuẩn hóa: Bắt buộc làm PoC tích hợp phần cứng bên thứ ba ngay trong **Sprint 0** trước khi phê duyệt Baseline.
3. **Quy tắc Đánh giá Mã nguồn Kép (2-Reviewer Rule):** Code review đã bắt 15 lỗi sai lệch làm tròn tiền lương. Hành động chuẩn hóa: Mã nguồn module tài chính bắt buộc có **$\ge 2$ Senior Reviewers** và Unit Test coverage **$\ge 85\%$**.
4. **Quy chuẩn Làm sạch Dữ liệu Sớm:** Dữ liệu Excel cũ chứa 12 bản ghi trùng lặp. Hành động chuẩn hóa: Thành lập tổ làm sạch dữ liệu ngay từ **Giai đoạn Phân tích Yêu cầu (Tháng 1)**.

### 4.1.2. Khối Tri Thức Vô Hình (Tacit Knowledge)
1. **Nghệ thuật Hóa giải Sự E ngại Thay đổi (Stakeholder Empathy):** Trưởng phòng HR ban đầu rất lo sợ phần mềm làm mất dữ liệu lương cũ. Nhóm xử lý bằng cách cho thao tác thử nghiệm Prototype Figma từ Tuần 3. Nhìn thấy bảng lương chạy thử chính xác sau 3 giây, HR Head đã chuyển biến từ e ngại thành **Đại sứ Cổ vũ Nhiệt thành nhất (Change Champion)**.
2. **Nghệ thuật Trao quyền (Empowerment):** Trao quyền tự chủ cho kỹ sư trẻ Dev 2 tự thiết kế luồng Tuyển dụng/Onboarding đã giúp năng suất tăng 40%, tạo ra giao diện Kanban kéo-thả được Ban Giám đốc đánh giá cao nhất.
3. **Giá trị của Minh bạch Trực tiếp:** Khi EVM sụt giảm ở mốc 15/10, việc PM gặp trực tiếp Tổng Giám đốc trình bày thẳng thắn nguyên nhân đi kèm Kế hoạch 3 điểm đã tạo dựng niềm tin tuyệt đối, giúp được phê duyệt ngay 15 triệu dự phòng mà không bị khiển trách.

---

## 4.2. BÁO CÁO ĐÓNG DỰ ÁN CUỐI CÙNG (FINAL PROJECT CLOSURE REPORT)

Bảng 4.1: Đánh Giá Hiệu Suất Tổng Thể Dự Án ABC-HRM So Với PMB:

| Tiêu chí | Mục tiêu Kế hoạch Ban đầu (PMB) | Kết quả Thực tế Đạt được | Mức độ Đạt | Đánh giá Tổng thể |
|---|---|---|:---:|---|
| **Phạm vi (Scope)** | 06 phân hệ theo đặc tả SRS (12 FR + 6 NFR) | **06 phân hệ cốt lõi + tính năng CR-001** | **108,3%** | 🟢 Vượt mục tiêu, kiểm soát chặt chẽ Scope Creep |
| **Tiến độ (Schedule)**| 24 tuần (Mục tiêu Go-Live: **30/04/2026**) | Go-Live chính thức: **04/05/2026** (24,5 tuần) | **98,0%** | 🟢 Đạt chuẩn (+2 ngày làm việc sau nghỉ lễ do CR-001) |
| **Chi phí (Cost)** | Tổng ngân sách trần: **850.000.000 VNĐ** | Chi phí thực tế: **826.960.000 VNĐ** | **97,3%** | 🟢 **Tiết kiệm 23.040.000 VNĐ (2,7% ngân sách)** |
| **Chất lượng (Quality)**| Lỗi UAT $< 0,01\%$, tính lương $< 30$s | 0 lỗi Critical/Major; tính lương mất **8,4 giây** | **100,0%** | 🟢 Đạt chuẩn xuất sắc toàn diện |
| **Ứng dụng (Adoption)**| Tỷ lệ áp dụng sau 30 ngày $\ge 90\%$ | **95,0%** nhân viên chủ động sử dụng hệ thống | **105,5%** | 🟢 Vượt kỳ vọng của Ban Giám đốc |

---

## 4.3. BÀN GIAO SẢN PHẨM, GIẢI TÁN NHÓM VÀ BIÊN BẢN CHẤP THUẬN

1. **Bàn giao Sản phẩm Chính thức:**
   - Mã nguồn Git phiên bản `v1.0.0-RELEASE` bàn giao cho phòng CNTT (`gitlab.abc.internal/tech/abc-hrm.git`).
   - Tài liệu Vận hành Ops Manual, Docker Compose, kịch bản Backup tự động và API Swagger Docs.
   - Tài liệu Hướng dẫn Người dùng (User Guide 45 trang) và 03 video clips đào tạo bàn giao cho phòng HR.
2. **Kế hoạch Giải tán Đội ngũ (Team Demobilization):**
   - PM chuyển sang lập kế hoạch Phase 2 (Phân hệ Đào tạo LMS).
   - Senior Dev giữ vai trò Cố vấn Kỹ thuật trong 3 tháng bảo hành miễn phí.
   - Dev 1, Dev 2 và QA hoàn thành nhiệm vụ và trở về nguồn lực công ty nhận dự án mới.
3. **Quyết toán Tài chính:**
   - Thanh lý hợp đồng máy chủ Cloud và bản quyền ZKTeco.
   - Hoàn nhập **23.040.000 VNĐ** số dư tiết kiệm vào quỹ chuyển đổi số nội bộ của công ty.
   - Đóng mã chi phí dự án `ABC-HRM-2025` trên hệ thống kế toán doanh nghiệp ngày 05/05/2026.
4. **Biên bản Chấp thuận Nghiệm thu Chính thức (Formal Acceptance Sign-Off):**

*Hà Nội, ngày 04 tháng 05 năm 2026*

| ĐẠI DIỆN NHÀ TÀI TRỢ (SPONSOR)<br/>*Tổng Giám đốc Công ty CP ABC* | ĐẠI DIỆN BAN QUẢN LÝ DỰ ÁN<br/>*Giám đốc Dự án (PM)* |
|:---:|:---:|
| *(Ký và đóng dấu)* | *(Ký và ghi rõ họ tên)* |
| <br/><br/><br/>**Nguyễn Văn A** | <br/><br/><br/>**[Họ và tên Học viên 1]** |
| **ĐẠI DIỆN ĐƠN VỊ THỤ HƯỞNG (HR HEAD)**<br/>*Trưởng phòng Quản trị Nhân sự* | **ĐẠI DIỆN TIẾP NHẬN VẬN HÀNH (IT LEAD)**<br/>*Trưởng phòng Công nghệ Thông tin* |
| *(Ký và ghi rõ họ tên)* | *(Ký và ghi rõ họ tên)* |
| <br/><br/><br/>**Trần Thị B** | <br/><br/><br/>**Phạm Quốc D** |

\newpage

# CHƯƠNG 5: HỒ SƠ THIẾT KẾ KỸ THUẬT VÀ PHẦN MỀM (TECHNICAL SPECIFICATIONS)

---

## KHUNG TIẾP CẬN BẢN CHẤT CỦA HỒ SƠ KỸ THUẬT

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                             HỒ SƠ THIẾT KẾ KỸ THUẬT (TECHNICAL SPECIFICATIONS)                   │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. TẠI SAO LÀM? (WHY)                                                                           │
│    • Tài liệu quản lý dự án chỉ có giá trị khi được bảo chứng bởi một thiết kế kỹ thuật khả thi, │
│      vững chắc, an toàn thông tin và đáp ứng đúng các tiêu chuẩn công nghiệp phần mềm.           │
│    • Hệ thống xử lý dữ liệu tiền lương bắt buộc phải có thiết kế kiến trúc phân tầng rõ ràng,    │
│      CSDL quan hệ chuẩn hóa 3NF và quy trình kiểm thử UAT chặt chẽ để loại bỏ mọi rủi ro lỗi.    │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 2. LÀM GÌ? (WHAT)                                                                                │
│    • Thiết kế Kiến trúc Hệ thống 3 lớp (React SPA, NestJS REST API, PostgreSQL 15, Redis).      │
│    • Thiết kế CSDL Quan hệ chuẩn hóa 3NF gồm 10 bảng cốt lõi kèm Từ điển Dữ liệu chi tiết.      │
│    • Lập Kế hoạch Kiểm thử Đa tầng và Biên bản Nghiệm thu UAT với 50 kịch bản kiểm thử.          │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 3. LÀM THẾ NÀO? (HOW)                                                                           │
│    • Tuân thủ tiêu chuẩn ISO/IEC/IEEE 42010 về mô tả kiến trúc và IEEE 829 về kiểm thử.         │
│    • Áp dụng mã hóa AES-256 mức cột cho dữ liệu lương và Bcrypt cho mật khẩu người dùng.        │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 5.1. THIẾT KẾ KIẾN TRÚC HỆ THỐNG VÀ AN NINH BẢO MẬT

Hệ thống được thiết kế theo mô hình Kiến trúc 3 tầng (3-tier Architecture) phân tách độc lập:
1. **Tầng Trình diễn (Presentation Layer - Frontend):** Xây dựng bằng React 18, Vite, TailwindCSS. Cung cấp giao diện Single Page Application (SPA) phản hồi tức thì, tối ưu hóa hiển thị Responsive trên thiết bị di động.
2. **Tầng Nghiệp vụ (Application Layer - Backend API):** Xây dựng bằng Node.js với framework NestJS hướng đối tượng TypeScript. Quản lý toàn bộ logic nghiệp vụ qua các dịch vụ độc lập: Auth, Employee, Attendance, Payroll Engine, Recruitment, KPI. Tích hợp ZKTeco Adapter Background Worker kết nối Socket TCP/IP với máy quét vân tay văn phòng.
3. **Tầng Dữ liệu (Data Storage Layer):** Hệ quản trị CSDL quan hệ PostgreSQL 15 đảm bảo giao dịch ACID; Redis 7 làm bộ nhớ đệm lưu phiên làm việc (Session) và bộ đệm log chấm công.

```
[ FRONTEND SPA (React 18) ] ◄── HTTPS/REST API ──► [ BACKEND API (NestJS) ] ◄── Socket ──► [ MÁY CHẤM CÔNG ZKTeco ]
                                                             │
                                         ┌───────────────────┴───────────────────┐
                                         ▼                                       ▼
                              [ PostgreSQL 15 (3NF DB) ]               [ Redis 7 Cache ]
```

### Kiến Trúc An Ninh Bảo Mật 4 Lớp:
* *Lớp 1 (Mạng):* HTTPS SSL/TLS 1.3, Nginx Reverse Proxy giới hạn Rate Limiting 100 req/phút/IP.
* *Lớp 2 (Xác thực & Phân quyền):* Access Token JWT (15 phút) + Refresh Token (7 ngày); RBAC 5 vai trò; 2FA TOTP qua Google Authenticator cho Admin và HR Manager.
* *Lớp 3 (Mã hóa CSDL):* Mật khẩu băm Bcrypt (Salt rounds = 12); cột dữ liệu nhạy cảm (`base_salary`, `bank_account`, `id_card_number`) mã hóa đối xứng **AES-256-GCM**.
* *Lớp 4 (OWASP Top 10):* 100% Parameterized queries qua TypeORM chống SQL Injection; escape HTML chống XSS; SameSite Cookie chống CSRF.

---

## 5.2. THIẾT KẾ CƠ SỞ DỮ LIỆU CHUẨN HÓA 3NF (ERD & DATA DICTIONARY)

Hệ thống thiết kế CSDL quan hệ gồm **10 bảng chuẩn hóa 3NF**:
* `roles` (Nhóm quyền RBAC)
* `users` (Tài khoản người dùng, email, mật khẩu băm Bcrypt, 2FA)
* `departments` (Phòng ban công ty)
* `employees` (Hồ sơ nhân sự, mã nhân viên `ABC-XXXX`, lương và CCCD mã hóa AES-256)
* `contracts` (Hợp đồng lao động, ngày hiệu lực, ngày hết hạn, file PDF)
* `attendance_logs` (Nhật ký quét vân tay từ ZKTeco)
* `leave_requests` (Đơn xin nghỉ phép, làm ngoài giờ OT, quy trình duyệt 2 cấp)
* `payroll_records` (Bảng lương tháng, công chuẩn, công thực tế, lương Gross, BHXH, thuế TNCN, lương Net)
* `dependents` (Người phụ thuộc đăng ký giảm trừ gia cảnh thuế TNCN)
* `kpi_evaluations` (Đánh giá hiệu suất quý, xếp loại A/B/C/D)

Bảng 5.1: Trích Lược Từ Điển Dữ Liệu Bảng Lương `payroll_records`:

| Tên Cột | Kiểu Dữ Liệu | Ràng Buộc | Ý Nghĩa / Mô Tả | Dữ Liệu Mẫu |
|---|---|:---:|---|---|
| `id` | `VARCHAR(36)` | PK, Not Null | Khóa chính bản ghi lương (UUID) | `'pr-2026-03-015'` |
| `employee_id` | `VARCHAR(36)` | FK $\rightarrow$ `employees.id` | Nhân viên hưởng lương | `'emp-101'` |
| `month` / `year` | `INT` / `INT` | Not Null | Kỳ lương tháng/năm | `3` / `2026` |
| `standard_days`| `DECIMAL(4,1)`| Not Null | Số ngày công chuẩn của tháng | `22.0` |
| `actual_days` | `DECIMAL(4,1)`| Not Null | Số ngày công đi làm thực tế | `21.5` |
| `ot_hours` | `DECIMAL(5,1)`| Default 0.0 | Tổng số giờ làm ngoài giờ OT | `12.0` |
| `gross_salary`| `DECIMAL(14,2)`| Not Null | Tổng thu nhập Gross tính thuế | `22.450.000,00` |
| `bhxh_deduction`| `DECIMAL(14,2)`| Not Null | Tiền BHXH trừ lương (8%) | `1.440.000,00` |
| `personal_tax`| `DECIMAL(14,2)`| Not Null | Thuế Thu nhập Cá nhân (TNCN) | `865.000,00` |
| `net_salary` | `DECIMAL(14,2)`| Not Null | **LƯƠNG THỰC NHẬN (NET)** | `19.695.000,00` |
| `payslip_pdf_path`| `VARCHAR(255)`| Nullable | File PDF phiếu lương có mật khẩu | `'/payslips/015.pdf'` |

---

## 5.3. KẾ HOẠCH KIỂM THỬ ĐA TẦNG VÀ BIÊN BẢN NGHIỆM THU UAT

Chiến lược kiểm thử áp dụng mô hình chữ V (V-Model):
1. **Unit Test (Jest):** Coverage toàn hệ thống đạt **$87,5\%$** (vượt chỉ tiêu $\ge 80\%$).
2. **Integration Test (Supertest):** Kiểm tra liên thông luồng Chấm công $\rightarrow$ Bảng công $\rightarrow$ Tính lương.
3. **Load Test (Apache JMeter):** Chạy tải 50 users đồng thời trong 15 phút $\rightarrow$ Thời gian phản hồi trung bình **1,2 giây**, tỷ lệ lỗi 0%.
4. **Kiểm thử UAT:** Thực hiện với phòng HR và Kế toán trên 50 kịch bản thử nghiệm nghiệp vụ.

Bảng 5.2: Bảng Tổng Kết Kết Quả Kiểm Thử UAT:
* **Tổng số kịch bản kiểm thử (Test Cases):** **50 kịch bản** (Bao phủ 12 FR và 6 NFR).
* **Số kịch bản Đạt (Passed):** **50 kịch bản (100%)**.
* **Số kịch bản Không Đạt (Failed):** **0 kịch bản (0%)**.
* **Lỗi Critical / Major:** **0 lỗi**.

### Biên Bản Nghiệm Thu Kỹ Thuật Chấp Thuận (UAT Signoff Certificate):
*Hà Nội, ngày 03 tháng 11 năm 2025*

Hội đồng Nghiệm thu Kỹ thuật gồm đại diện QA Lead ([Họ tên Học viên 5]), Tech Lead ([Họ tên Học viên 3]), Lead BA ([Họ tên Học viên 2]) và Trưởng phòng Quản trị Nhân sự (Bà Trần Thị B) đồng thuận ký xác nhận: **Hệ thống ABC-HRM đạt 100% các tiêu chí chất lượng kỹ thuật, tính toán tiền lương và thuế TNCN chính xác tuyệt đối, đủ điều kiện đưa lên môi trường máy chủ sản xuất (Production).**

\newpage

# TÀI LIỆU THAM KHẢO

### I. Tài Liệu Tiếng Việt
1. **Bộ Lao động - Thương binh và Xã hội (2019)**, *Bộ luật Lao động số 45/2019/QH14*, Nhà xuất bản Lao động, Hà Nội.
2. **Chính phủ nước CHXHCN Việt Nam (2020)**, *Nghị định số 145/2020/NĐ-CP: Quy định chi tiết và hướng dẫn thi hành một số điều của Bộ luật Lao động về điều kiện lao động và quan hệ lao động*, Hà Nội.
3. **Khoa Hệ thống Thông tin Quản lý — Học viện Ngân hàng (2024)**, *Giáo trình Quản lý Dự án Công nghệ Thông tin*, Nhà xuất bản Tài chính, Hà Nội.
4. **Quốc hội nước CHXHCN Việt Nam (2014)**, *Luật Bảo hiểm Xã hội số 58/2014/QH13*, Nhà xuất bản Chính trị Quốc gia Sự thật, Hà Nội.
5. **Tổng cục Thuế — Bộ Tài chính (2023)**, *Cẩm nang Hướng dẫn Quyết toán Thuế Thu nhập Cá nhân và các Biểu thuế Lũy tiến Từng phần*, Hà Nội.

### II. Tài Liệu Tiếng Anh
6. **IEEE Computer Society (1998)**, *IEEE Std 830-1998: IEEE Recommended Practice for Software Requirements Specifications*, Institute of Electrical and Electronics Engineers, New York.
7. **IEEE Computer Society (2008)**, *IEEE Std 829-2008: IEEE Standard for Software and System Test Documentation*, Institute of Electrical and Electronics Engineers, New York.
8. **Kerzner, H. (2017)**, *Project Management: A Systems Approach to Planning, Scheduling, and Controlling* (12th ed.), John Wiley & Sons, Hoboken, New Jersey.
9. **Project Management Institute (2019)**, *The Standard for Earned Value Management*, Project Management Institute, Newtown Square, Pennsylvania.
10. **Project Management Institute (2021)**, *A Guide to the Project Management Body of Knowledge (PMBOK® Guide) – Seventh Edition and The Standard for Project Management*, Project Management Institute, Newtown Square, Pennsylvania.
11. **Schwaber, K. and Sutherland, J. (2020)**, *The Scrum Guide: The Definitive Guide to Scrum: The Rules of the Game*, Scrum.org.
