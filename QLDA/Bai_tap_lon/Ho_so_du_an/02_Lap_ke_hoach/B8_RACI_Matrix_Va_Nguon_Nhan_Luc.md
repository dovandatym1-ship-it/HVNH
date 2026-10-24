# MA TRẬN PHÂN CÔNG TRÁCH NHIỆM (RACI MATRIX) VÀ QUẢN TRỊ NGUỒN NHÂN LỰC CNTT
## Dự án: Xây dựng Hệ thống Quản trị Nhân sự Nội bộ (ABC-HRM)
### Mã tài liệu: BTL-QLDA-B8 | Giai đoạn: Lập kế hoạch (Planning)
### Tiêu chuẩn áp dụng: PMI PMBOK Guide / Human Resource Management | Học phần: QLDA CNTT Nâng cao (HVNH)

---

## 1. TỔNG QUAN VỀ PHÂN BỔ TRÁCH NHIỆM TRONG DỰ ÁN CNTT

Quản lý Nguồn nhân lực dự án bao gồm các quy trình tổ chức, quản lý và dẫn dắt đội ngũ dự án. Để xóa bỏ hiện tượng đùn đẩy trách nhiệm, chồng chéo công việc hoặc bỏ sót đầu mối bàn giao giữa các chuyên môn kỹ thuật khác nhau, nhóm dự án thiết lập **Ma trận Phân công Trách nhiệm (RACI Matrix)**.

Ma trận RACI định nghĩa rõ 4 vai trò tham gia cho từng gói công việc:
* **R - Responsible (Người thực hiện):** Người trực tiếp chịu trách nhiệm triển khai, viết mã nguồn, thiết kế hoặc tạo ra sản phẩm bàn giao của gói công việc.
* **A - Accountable (Người giải trình / Chịu trách nhiệm cuối cùng):** Người duy nhất nắm quyền quyết định, phê duyệt và chịu trách nhiệm toàn diện về kết quả nghiệm thu của gói công việc (nguyên tắc: mỗi gói công việc chỉ có duy nhất **01 chữ A**).
* **C - Consulted (Người được tham vấn):** Chuyên gia hoặc bên liên quan sở hữu tri thức nghiệp vụ, kỹ thuật cần được lấy ý kiến đóng góp hai chiều trước khi hoàn thành công việc.
* **I - Informed (Người được thông báo):** Cá nhân hoặc bộ phận cần được cập nhật thông tin một chiều về tiến độ hoặc kết quả hoàn thành của công việc.

---

## 2. MA TRẬN RACI DỰ ÁN ABC-HRM (16 GÓI CÔNG VIỆC TRỌNG TÂM)

Các vai trò được ký hiệu trong ma trận:
* **PM:** Quản lý Dự án (Project Manager - TV1)
* **BA:** Chuyên viên Phân tích Nghiệp vụ (Business Analyst - TV2)
* **Sr Dev:** Kỹ sư Phần mềm Cao cấp / Trưởng nhóm Kỹ thuật (TV3)
* **Dev 1:** Kỹ sư Phần mềm phụ trách Backend (TV4)
* **Dev 2:** Kỹ sư Phần mềm phụ trách Frontend (TV4)
* **QA:** Kỹ sư Đảm bảo Chất lượng / Kiểm thử (TV5)
* **HRM:** Trưởng phòng Nhân sự (Chủ sở hữu nghiệp vụ)
* **ITL:** Trưởng phòng CNTT (Quản trị hạ tầng nội bộ)

| STT | Gói Công việc Chính (WBS) | PM | BA | Sr Dev | Dev 1 | Dev 2 | QA | HRM | ITL |
|:---:|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | Lập Business Case & Project Charter | **A/R** | C | I | I | I | I | C | I |
| 2 | Khảo sát Hiện trạng & Thu thập Biểu mẫu | A | **R** | C | I | I | I | C | I |
| 3 | Xây dựng Đặc tả Yêu cầu SRS & RTM | A | **R** | C | I | I | C | **C** | I |
| 4 | Thiết kế Kiến trúc Hệ thống & An ninh | A | C | **R** | C | C | I | I | **C** |
| 5 | Thiết kế CSDL (ERD & Data Dictionary) | A | C | **R** | C | I | I | I | I |
| 6 | Thiết kế Giao diện Wireframe & UI/UX | A | C | C | I | **R** | I | C | I |
| 7 | Lập trình Phân hệ Hồ sơ Nhân sự | A | I | C | **R** | C | I | I | I |
| 8 | Lập trình Phân hệ Chấm công & SDK ZKTeco | A | I | **R** | C | C | I | I | C |
| 9 | Lập trình Động cơ Tính lương & Thuế TNCN | A | C | **R** | C | C | I | **C** | I |
| 10 | Lập trình Phân hệ Tuyển dụng & Onboarding | A | I | C | **R** | C | I | I | I |
| 11 | Lập trình Phân hệ Quản trị Hiệu suất KPI | A | I | C | **R** | C | I | C | I |
| 12 | Lập trình Executive Dashboard & Báo cáo | A | I | C | I | **R** | I | I | I |
| 13 | Kiểm thử Tích hợp, Kiểm thử Tải & Bảo mật | A | I | C | C | C | **R** | I | C |
| 14 | Điều phối Kiểm thử Chấp nhận Người dùng (UAT) | A | **R** | C | I | I | C | **R** | I |
| 15 | Viết Script ETL & Di chuyển Dữ liệu Excel | A | C | **R** | C | I | C | C | I |
| 16 | Đào tạo Người dùng, Triển khai & Go-Live | **A** | **R** | C | I | I | I | C | C |

---

## 3. THÁCH THỨC QUẢN TRỊ NGUỒN NHÂN LỰC ĐẶC THÙ TRONG DỰ ÁN CNTT

Triển khai dự án phần mềm nội bộ đòi hỏi giải quyết hai thách thức nhân lực mang tính kinh điển trong ngành CNTT:

### 3.1. Rủi ro Phụ thuộc Nhân sự Chủ chốt (Key Person Dependency Risk)
* **Thực trạng nhận diện:** Kỹ sư Phần mềm Cao cấp (**Senior Dev**) nắm giữ vai trò sống còn trong việc thiết kế kiến trúc lõi, viết SDK kết nối máy chấm công và lập trình động cơ tính lương phức tạp. Nếu nhân sự này nghỉ việc đột xuất hoặc gặp sự cố sức khỏe, toàn bộ dự án sẽ bị tê liệt do không ai hiểu tường tận mã nguồn lõi.
* **Chiến lược Quản trị & Ứng phó Chủ động:**
  1. **Quy tắc Lập trình Cặp (Pair Programming):** Đối với các module phức tạp (Chấm công và Động cơ Tính lương), Senior Dev bắt buộc phải làm việc song hành cùng Dev 1 tối thiểu 30% thời lượng. Dev 1 đóng vai trò là "Shadow Resource" hiểu rõ logic nghiệp vụ.
  2. **Quy chuẩn Đánh giá Mã nguồn Bắt buộc (Mandatory Code Review):** 100% dòng lệnh đẩy lên nhánh chính của Git phải qua Pull Request (PR) và có sự phê duyệt của ít nhất 01 thành viên khác trong nhóm.
  3. **Tài liệu hóa Kiến trúc & API Docs Chuẩn OpenAPI (Swagger):** Mọi endpoint API phải được tự động sinh tài liệu giải thích rõ tham số đầu vào/đầu ra, không chấp nhận việc "giữ bí quyết kỹ thuật trong đầu".

---

### 3.2. Cơ chế Tạo Động lực Nội tại (Intrinsic Motivation Framework)
Kỹ sư CNTT không chỉ làm việc vì thù lao tài chính mà chịu sự chi phối mạnh mẽ bởi động lực nội tại. Nhóm áp dụng **Lý thuyết Động lực 3 Yếu tố của Daniel Pink (Drive)**:

1. **Quyền Tự chủ (Autonomy):**
   - Đội ngũ kỹ sư được tự do quyết định cách thức hiện thực hóa kỹ thuật, lựa chọn thư viện mã nguồn mở tối ưu (React hooks, NestJS modules, TailwindCSS) và tự tổ chức phân chia công việc trong từng Sprint 2 tuần mà không bị PM can thiệp vi mô (No Micromanagement).
2. **Sự Tinh thông & Nâng cao Tay nghề (Mastery):**
   - Dự án là cơ hội để 2 kỹ sư phần mềm trẻ (Dev 1, Dev 2) được tiếp cận các bài toán kỹ thuật cao cấp: Xử lý dữ liệu socket thời gian thực, lập trình động cơ tính toán tài chính và thiết kế CSDL tối ưu hóa chỉ mục.
   - Tổ chức các buổi chia sẻ công nghệ nội bộ (Tech Talk 45 phút vào chiều Thứ Sáu hàng tuần) để các thành viên chia sẻ kiến thức mới học được.
3. **Mục đích Ý nghĩa (Purpose):**
   - Các thành viên hiểu rõ sản phẩm mình làm ra không phải là một bài tập giả lập, mà là giải pháp chuyển đổi số thực tế giúp xóa bỏ hoàn toàn nỗi vất vả, áp lực sai sót lương hàng tháng của 3 đồng nghiệp phòng HR và phục vụ trực tiếp 100 cán bộ nhân viên công ty.

---

## 4. CƠ CHẾ GIẢI QUYẾT XUNG ĐỘT VÀ QUY ƯỚC LÀM VIỆC NHÓM (TEAM CHARTER)

1. **Quy ước Giao tiếp & Nghi thức Làm việc (Agile Ceremonies):**
   - **Họp đứng hàng ngày (Daily Stand-up 15 phút):** Diễn ra lúc 09h00 sáng mỗi ngày làm việc. Mỗi thành viên trả lời 3 câu hỏi: *Hôm qua đã làm gì? Hôm nay sẽ làm gì? Có khó khăn/điểm nghẽn (Blocker) nào cần hỗ trợ không?*
   - **Họp Rà soát Sprint & Cải tiến (Sprint Review & Retrospective 60 phút):** Tổ chức vào ngày cuối cùng của mỗi chu kỳ Sprint 2 tuần để trình diễn tính năng mới và rút ra bài học cải tiến quy trình.
2. **Quy tắc Giải quyết Bất đồng Ý kiến Kỹ thuật:**
   - Mọi tranh cãi về mặt giải pháp kiến trúc không được giải quyết bằng cảm tính hoặc thâm niên.
   - Các bên phải tiến hành làm thử nghiệm thực chứng kỹ thuật (**PoC - Proof of Concept**) trong vòng tối đa 04 giờ làm việc; giải pháp nào chứng minh được hiệu năng cao hơn, mã nguồn gọn hơn và dễ kiểm thử hơn sẽ được lựa chọn. Quyết định cuối cùng thuộc về Technical Lead (Senior Dev) và PM.
