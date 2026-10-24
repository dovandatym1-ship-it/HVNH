# HIẾN CHƯƠNG DỰ ÁN (PROJECT CHARTER)
## Dự án: Xây dựng Hệ thống Quản trị Nhân sự Nội bộ (ABC-HRM)
### Mã dự án: ABC-HRM-2025 | Phiên bản: 1.0 (Chính thức)
### Đơn vị chủ quản: Công ty Cổ phần ABC | Học phần: Quản lý Dự án CNTT Nâng cao (HVNH)

---

## 1. THÔNG TIN CHUNG DỰ ÁN

| Hạng mục | Chi tiết xác lập |
|---|---|
| **Tên dự án** | Hệ thống Quản trị Nhân sự Nội bộ Doanh nghiệp (ABC-HRM) |
| **Mã dự án** | **ABC-HRM-2025** |
| **Nhà tài trợ (Sponsor)** | Giám đốc Điều hành (CEO) — Công ty Cổ phần ABC |
| **Giám đốc Dự án (PM)** | Trưởng nhóm dự án / [Họ và tên Học viên 1 - Trưởng nhóm] |
| **Khách hàng / Đơn vị thụ hưởng** | Khối Quản trị Nhân sự và toàn thể 100 Cán bộ Nhân viên Công ty ABC |
| **Thời gian thực hiện** | 24 tuần (06 tháng), dự kiến từ **01/11/2025 đến 30/04/2026** |
| **Tổng ngân sách phê duyệt (BAC)** | **850.000.000 VNĐ** (Tám trăm năm mươi triệu đồng chẵn) |
| **Mô hình quản lý áp dụng** | **Hybrid** (Waterfall cho quản lý phạm vi, chi phí, tiến độ tổng thể; Scrum/Agile trong các vòng lặp phát triển phần mềm) |

---

## 2. BỐI CẢNH VÀ LÝ DO KHỞI ĐỘNG DỰ ÁN (BUSINESS NEED)

Công ty Cổ phần ABC hiện có 100 nhân viên đang quản lý các hoạt động nhân sự phân tán qua các bảng tính Excel và hồ sơ giấy. Mô hình quản lý thủ công này đang phát sinh các hạn chế nghiêm trọng:
1. **Lãng phí nguồn lực:** Đội ngũ 3 nhân sự HR mất hơn 60 giờ công mỗi tháng cho các tác vụ sự vụ đối soát chấm công và nhập liệu đơn nghỉ phép.
2. **Sai lệch và rủi ro tính lương:** Tỷ lệ khiếu nại sai sót tiền lương chiếm 5,2%/tháng; thời gian chốt bảng lương mất 2–3 ngày làm việc mỗi tháng.
3. **Thiếu tập trung dữ liệu:** Hồ sơ nhân viên, hợp đồng lao động, đánh giá năng lực phân mảnh, không thể trích xuất báo cáo động cho Ban Giám đốc phục vụ hoạch định nguồn nhân lực.

Căn cứ vào bản Nghiên cứu khả thi và Xác nhận giá trị (**Business Case A1**) đã được Hội đồng Quản trị thông qua với chỉ số hiệu quả kinh tế cao ($NPV = +476,78$ triệu VNĐ, $ROI = 105,88\%$, Thời gian hoàn vốn 2,43 năm), Giám đốc Doanh nghiệp quyết định ban hành Hiến chương Dự án này để chính thức cấp phép thành lập và khởi động dự án **ABC-HRM**.

---

## 3. MỤC TIÊU DỰ ÁN THEO NGUYÊN TẮC SMART

| Tiêu chí SMART | Định nghĩa cam kết của Dự án ABC-HRM |
|---|---|
| **S (Specific - Cụ thể)** | Thiết kế, phát triển và đóng gói triển khai hoàn thiện 01 hệ thống ứng dụng Web Quản trị Nhân sự tập trung bao gồm 06 phân hệ nghiệp vụ: Quản lý Hồ sơ, Chấm công, Tính lương, Tuyển dụng, Đánh giá KPI, và Dashboard Báo cáo. |
| **M (Measurable - Đo lường được)** | • 100% cán bộ nhân viên (100 người) được khởi tạo tài khoản và vận hành trên hệ thống.<br/>• Thời gian chốt kỳ lương giảm từ 3 ngày xuống **dưới 4 giờ làm việc**.<br/>• Tỷ lệ sai sót trong tính lương và đóng bảo hiểm giảm xuống **dưới 0,1%**.<br/>• Tỷ lệ nhân viên tích cực sử dụng hệ thống (User Adoption) đạt **≥ 90%** sau 30 ngày go-live. |
| **A (Achievable - Khả thi)** | Đội ngũ dự án gồm 5 thành viên có chuyên môn sâu về phân tích nghiệp vụ, phát triển công nghệ web hiện đại (React/NestJS/PostgreSQL), kế thừa máy chấm công vân tay sẵn có, áp dụng công cụ quản lý dự án chuẩn mực. |
| **R (Relevant - Phù hợp chiến lược)** | Đóng vai trò là dự án trụ cột trong Kế hoạch Chuyển đổi số Nội bộ của Công ty ABC giai đoạn 2025–2027, chuẩn bị nền tảng vận hành khi mở rộng quy mô lên 150–200 nhân sự. |
| **T (Time-bound - Có thời hạn)** | Hoàn thành toàn bộ công tác bàn giao và chính thức go-live vào ngày **30/04/2026** (không vượt quá 24 tuần làm việc). |

---

## 4. PHẠM VI DỰ ÁN CẤP CAO (HIGH-LEVEL SCOPE)

### 4.1. Phạm vi Sản phẩm Bàn giao (In-Scope Deliverables)
1. **Phần mềm ứng dụng Web ABC-HRM hoàn chỉnh:**
   - *Phân hệ 1:* Quản lý Hồ sơ Nhân sự điện tử & Hợp đồng số.
   - *Phân hệ 2:* Chấm công tự động (kết nối máy chấm công ZKTeco) & Duyệt nghỉ phép trực tuyến.
   - *Phân hệ 3:* Công cụ tính lương Gross-Net tự động theo luật lao động và BHXH Việt Nam.
   - *Phân hệ 4:* Quản lý Quy trình Tuyển dụng & Onboarding nhân sự mới.
   - *Phân hệ 5:* Quản lý Đánh giá Hiệu suất (KPI) đa chiều theo định kỳ.
   - *Phân hệ 6:* Báo cáo phân tích và Dashboard nhân sự điều hành dành cho Ban Giám đốc.
2. **Hồ sơ Quản lý Dự án & Kỹ thuật:**
   - Bộ hồ sơ QLDA theo chuẩn PMBOK (Charter, Scope, WBS, Schedule, Cost Baseline, RACI, Risk Register, Change Log, EVM Report, Lessons Learned, Closure Report).
   - Hồ sơ kỹ thuật: Đặc tả SRS, Thiết kế Kiến trúc, Bản vẽ CSDL (ERD), Kế hoạch Kiểm thử & Biên bản UAT.
3. **Chuyển giao & Vận hành:**
   - Chuyển đổi và làm sạch 100% dữ liệu hồ sơ nhân sự hiện có từ Excel vào CSDL hệ thống mới.
   - Tổ chức đào tạo người dùng: 02 buổi chuyên sâu cho phòng HR; 01 buổi hướng dẫn chung cho toàn bộ nhân viên.
   - Tài liệu Hướng dẫn Sử dụng (User Guide) và Tài liệu Quản trị Vận hành Hệ thống (Ops Manual).

### 4.2. Phạm vi Loại trừ Cấp cao (Key Exclusions)
Nhằm kiểm soát rủi ro lạm phát phạm vi (Scope Creep), các hạng mục sau **không nằm trong phạm vi** của dự án này:
- ❌ Không phát triển ứng dụng di động bản địa (Native Mobile App trên iOS/Android); hệ thống chỉ tối ưu hóa hiển thị trên trình duyệt di động (Responsive Web).
- ❌ Không tích hợp hai chiều với các phần mềm ERP kế toán bên thứ ba (SAP, MISA, Oracle).
- ❌ Không xây dựng phân hệ Quản lý Đào tạo Nội bộ chuyên sâu (E-Learning/LMS); hạng mục này dời sang Giai đoạn 2 sau go-live.
- ❌ Không hỗ trợ đa ngôn ngữ (chỉ hỗ trợ Tiếng Việt).

---

## 5. DỰ TOÁN NGÂN SÁCH VÀ NGUỒN VỐN (PRELIMINARY BUDGET)

Tổng ngân sách dự án được cấp trần tối đa là **850.000.000 VNĐ** trích từ Quỹ Đầu tư Phát triển Công nghệ Nội bộ của Công ty ABC, phân bổ cấu trúc:
* **Chi phí trực tiếp (Direct Project Costs):** **710.000.000 VNĐ** (bao gồm nhân sự dự án 575 tr, hạ tầng & bản quyền 68 tr, tích hợp thiết bị 12 tr, đào tạo & chuyển đổi dữ liệu 55 tr).
* **Dự trữ Dự phòng rủi ro (Contingency Reserve - 15%):** **106.500.000 VNĐ** $\rightarrow$ **Đường cơ sở Chi phí (Cost Baseline) = 816.500.000 VNĐ**.
* **Dự trữ Quản lý (Management Reserve - ~4%):** **33.500.000 VNĐ** (do Sponsor nắm quyền phê duyệt khi có tình huống bất khả kháng ngoài phạm vi).

---

## 6. LỊCH TRÌNH CÁC MỐC QUAN TRỌNG (MILESTONE SCHEDULE)

| Mốc tiến độ | Sự kiện / Sản phẩm bàn giao chính | Thời hạn mục tiêu | Đơn vị nghiệm thu |
|:---:|---|:---:|:---:|
| **M1** | Phê duyệt Hiến chương & Khởi động Dự án (Project Kick-off) | Tuần 3 (21/11/2025) | Sponsor & PM |
| **M2** | Hoàn thành Đặc tả Yêu cầu (SRS) & Bản vẽ Thiết kế Kiến trúc/CSDL | Tuần 8 (26/12/2025) | Trưởng phòng HR & IT Lead |
| **M3** | Hoàn tất Phát triển Mã nguồn 6 Phân hệ & Kiểm thử Đơn vị | Tuần 18 (06/03/2026) | Nhóm Phát triển (Dev/QA) |
| **M4** | Hoàn thành Kiểm thử Tích hợp, Di chuyển Dữ liệu & Nghiệm thu UAT | Tuần 22 (03/04/2026) | Phòng HR & Kế toán |
| **M5** | Đào tạo Người dùng, Triển khai Production & Go-live Toàn công ty | Tuần 24 (24/04/2026) | Toàn thể Ban Lãnh đạo |
| **M6** | Tổng kết Bài học Kinh nghiệm & Đóng Dự án Chính thức | Tuần 24 (30/04/2026) | Sponsor & Giảng viên HVNH |

---

## 7. CƠ CẤU TỔ CHỨC VÀ PHÂN QUYỀN TRÁCH NHIỆM

### 7.1. Đội ngũ Triển khai Dự án (Project Team - 5 thành viên)
1. **Quản lý Dự án (Project Manager - PM / TV1):** Chịu trách nhiệm toàn diện về tiến độ, chất lượng, chi phí, quản lý rủi ro và điều phối chung.
2. **Chuyên viên Phân tích Nghiệp vụ (Business Analyst - BA / TV2):** Khảo sát hiện trạng, làm việc trực tiếp với phòng HR, xây dựng tài liệu SRS và từ điển WBS.
3. **Kỹ sư Phần mềm Cao cấp (Senior Full-Stack Dev / TV3):** Thiết kế kiến trúc, thiết kế CSDL, chịu trách nhiệm các module lõi (Chấm công & Engine tính lương), lập lịch CPM/PERT.
4. **Kỹ sư Phần mềm (Full-Stack Dev / TV4):** Phát triển phân hệ Hồ sơ, Tuyển dụng, KPI, Dashboard và xây dựng Sổ đăng ký rủi ro, Quản lý thay đổi.
5. **Kỹ sư Đảm bảo Chất lượng & Kiểm thử (QA Engineer / TV5):** Xây dựng Test Plan, thực hiện kiểm thử tự động, điều phối UAT, đóng gói bài học kinh nghiệm và báo cáo đóng dự án.

### 7.2. Thẩm quyền Ủy quyền cho Quản lý Dự án (PM Authority)
Giám đốc Doanh nghiệp (Sponsor) chính thức ủy quyền cho PM các quyền hạn sau:
* **Quyền điều động nhân sự:** Toàn quyền phân công công việc, giao chỉ tiêu và đánh giá hiệu quả đóng góp của 4 thành viên trong suốt thời gian triển khai.
* **Quyền tài chính:** Được quyền chủ động phê duyệt các khoản chi tiêu trực tiếp nằm trong danh mục Đường cơ sở chi phí đã duyệt (tối đa không quá 20.000.000 VNĐ cho mỗi hạng mục phát sinh nằm trong Contingency Reserve).
* **Quyền kiểm soát thay đổi:** Được quyền từ chối hoặc yêu cầu phân tích lại đối với các yêu cầu thay đổi (CR) không mang lại giá trị hoặc đe dọa trực tiếp tới PMB; có quyền triệu tập cuộc họp Hội đồng Kiểm soát Thay đổi (CCB) khẩn cấp khi có rủi ro nghiêm trọng.

---

## 8. CÁC RÀNG BUỘC VÀ GIẢ ĐỊNH CHÍNH (CONSTRAINTS & ASSUMPTIONS)

### 8.1. Ràng buộc Dự án (Constraints)
* **Thời gian cứng:** Dự án phải hoàn thành trước 30/04/2026 để kịp áp dụng cho chu kỳ đánh giá và chi trả lương tháng 05/2026.
* **Ngân sách trần:** Tổng chi phí giải ngân không được vượt quá 850 triệu VNĐ đã phê duyệt.
* **Pháp lý bắt buộc:** Công thức tính lương và thuế phải tuân thủ nghiêm ngặt Luật Lao động 2019, Luật BHXH 2014, Luật Thuế TNCN hiện hành và các nghị định hướng dẫn liên quan.
* **Hạ tầng sẵn có:** Bắt buộc phải tương thích với hạ tầng máy quét vân tay ZKTeco hiện đang đặt tại văn phòng công ty.

### 8.2. Giả định Dự án (Assumptions)
* Đội ngũ nhân sự dự án (5 thành viên) duy trì mức độ cam kết làm việc liên tục trong suốt 6 tháng, không có xáo trộn nhân sự chủ chốt.
* Lãnh đạo và chuyên viên phòng Nhân sự bố trí thời gian tối thiểu 4 giờ/tuần để tham gia các buổi phỏng vấn làm rõ nghiệp vụ và thẩm định nghiệm thu từng Sprint.
* Dữ liệu hồ sơ nhân sự dạng file Excel cũ cung cấp bởi phòng HR có độ chính xác cơ bản trên 90%, đủ điều kiện để thực hiện làm sạch dữ liệu.

---

## 9. CÁC RỦI RO SƠ BỘ BAN ĐẦU (INITIAL HIGH-LEVEL RISKS)

| Mã | Rủi ro sơ bộ | Mức độ | Biện pháp ứng phó sơ bộ |
|:---:|---|:---:|---|
| **IR-01** | SDK máy chấm công vân tay không cung cấp tài liệu API chuẩn hoặc cổng kết nối bị gián đoạn | **Cao** | Thực hiện thử nghiệm kết nối kỹ thuật (PoC) ngay trong Tuần 2; chuẩn bị phương án dự phòng đồng bộ qua định dạng trung gian CSV. |
| **IR-02** | Phòng Nhân sự liên tục phát sinh thêm các yêu cầu mới trong quá trình kiểm thử (Scope Creep) | **Cao** | Ký cam kết đóng băng phạm vi (Scope Freeze) sau giai đoạn phê duyệt SRS; mọi phát sinh bắt buộc phải thông qua quy trình CCB. |
| **IR-03** | Dữ liệu bảng lương cũ bị phân mảnh, có sự trùng lặp mã định danh nhân viên | **Trung bình**| Thành lập tổ công tác BA và HR để rà soát, chuẩn hóa mã nhân viên (Staff ID) trước khi viết script nạp dữ liệu. |
| **IR-04** | Thay đổi chính sách thuế hoặc mức lương cơ sở trích đóng bảo hiểm của nhà nước | **Trung bình**| Thiết kế module tính lương theo cơ chế cấu hình tham số động (Configurable Rule Engine), không hard-code công thức trong mã nguồn. |

---

## 10. PHÊ DUYỆT VÀ CHẤP THUẬN (SIGN-OFF & APPROVAL)

Văn bản Hiến chương Dự án này có hiệu lực kể từ ngày ký. Mọi điều chỉnh liên quan đến mục tiêu, ngân sách trần, hoặc thời hạn kết thúc dự án bắt buộc phải có văn bản phê chuẩn chính thức của Nhà tài trợ Dự án.

| Đại diện Nhà tài trợ (Sponsor) | Đại diện Nhóm Triển khai (PM) | Đại diện Đơn vị Thụ hưởng (HR Head) |
|:---:|:---:|:---:|
| *(Ký và ghi rõ họ tên)* | *(Ký và ghi rõ họ tên)* | *(Ký và ghi rõ họ tên)* |
| <br/><br/><br/>**Nguyễn Văn A**<br/>Tổng Giám đốc Công ty CP ABC | <br/><br/><br/>**[Họ và tên Học viên 1]**<br/>Giám đốc Dự án (PM) | <br/><br/><br/>**Trần Thị B**<br/>Trưởng phòng Quản trị Nhân sự |
| Ngày ký: 01/11/2025 | Ngày ký: 01/11/2025 | Ngày ký: 01/11/2025 |
