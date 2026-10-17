# QUY TRÌNH KIỂM SOÁT THAY ĐỔI TÍCH HỢP (INTEGRATED CHANGE CONTROL) & CHANGE LOG
## Dự án: Xây dựng Hệ thống Quản trị Nhân sự Nội bộ (ABC-HRM)
### Mã tài liệu: BTL-QLDA-C1 | Giai đoạn: Thực hiện & Giám sát (Execution & M&C)
### Tiêu chuẩn áp dụng: PMI PMBOK Guide / Change Control Governance | Học phần: QLDA CNTT Nâng cao (HVNH)

---

## 1. KHUNG TIẾP CẬN BẢN CHẤT: LÀM GÌ? TẠI SAO LÀM? LÀM THẾ NÀO?

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                   MÔ HÌNH QUẢN TRỊ THAY ĐỔI TÍCH HỢP TRONG DỰ ÁN PHẦN MỀM                        │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. TẠI SAO LÀM? (WHY)                                                                           │
│    • Trong các dự án phần mềm, sự thay đổi yêu cầu là điều tất yếu. Tuy nhiên, nếu chấp nhận   │
│      thay đổi tùy tiện mà không đánh giá tác động sẽ dẫn đến hiện tượng Lạm phát Phạm vi        │
│      (Scope Creep), làm vỡ đường cơ sở chi phí (Cost Baseline) và chậm trễ ngày go-live.        │
│    • Quy trình Kiểm soát Thay đổi Tích hợp đảm bảo mọi thay đổi đều được phân tích đa chiều     │
│      (Phạm vi, Thời gian, Chi phí, Rủi ro, Chất lượng) trước khi trình Hội đồng CCB phê duyệt.  │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 2. LÀM GÌ? (WHAT)                                                                                │
│    • Thành lập Hội đồng Kiểm soát Thay đổi (Change Control Board - CCB) lâm thời của dự án.     │
│    • Xử lý hồ sơ phân tích tác động cho 02 Yêu cầu Thay đổi giả định điển hình:                 │
│      - CR-001: Bổ sung tính năng tự động cảnh báo hợp đồng hết hạn trước 30 ngày (Được DUYỆT).  │
│      - CR-002: Bổ sung phân hệ Quản lý Đào tạo nội bộ - LMS (Bị TỪ CHỐI / Hoãn sang Phase 2).   │
│    • Thiết lập Nhật ký Thay đổi (Change Log) để theo dõi xuyên suốt vòng đời xử lý yêu cầu.    │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 3. LÀM THẾ NÀO? (HOW)                                                                           │
│    • Thiết lập quy trình 5 bước: Đề xuất $\rightarrow$ Đánh giá Tác động $\rightarrow$ Trình    │
│      CCB Thẩm định $\rightarrow$ Ra Quyết định $\rightarrow$ Cập nhật PMB và Truyền thông.     │
│    • Dùng công thức lượng hóa tác động thời gian lên Đường Găng (CPM) và chi phí tài chính.      │
│    • Lưu trữ minh bạch mọi quyết định phê duyệt có chữ ký đại diện của các bên liên quan.       │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. QUY CHẾ HOẠT ĐỘNG CỦA HỘI ĐỒNG KIỂM SOÁT THAY ĐỔI (CCB CHARTER)

### 2.1. Thành phần Hội đồng CCB Dự án ABC-HRM
1. **Chủ tịch Hội đồng:** Ông Nguyễn Văn A — Tổng Giám đốc (Project Sponsor).
2. **Thành viên Thường trực:** [Họ và tên Học viên 1] — Quản lý Dự án (Project Manager).
3. **Thành viên Nghiệp vụ:** Bà Trần Thị B — Trưởng phòng Quản trị Nhân sự (HR Head).
4. **Thành viên Kỹ thuật:** [Họ và tên Học viên 3] — Kỹ sư Phần mềm Cao cấp (Technical Lead).
5. **Thành viên Tài chính:** Ông Lê Văn C — Trưởng phòng Kế toán - Tài chính.

### 2.2. Thẩm quyền và Nguyên tắc Ra Quyết định
* **Nguyên tắc đồng thuận:** Mọi quyết định thay đổi làm tăng tổng chi phí $> 20$ triệu VNĐ hoặc làm dịch chuyển thời điểm Go-Live $> 5$ ngày làm việc bắt buộc phải có sự đồng thuận bằng văn bản của Chủ tịch Hội đồng (Sponsor).
* **Quyền hạn của PM:** Được quyền tự phê duyệt các thay đổi kỹ thuật nhỏ nội bộ không làm thay đổi ngày bàn giao mốc quan trọng và chi phí phát sinh $< 10$ triệu VNĐ (trích từ Quỹ Dự trữ Dự phòng Contingency Reserve).

---

## 3. PHÂN TÍCH CHI TIẾT 02 YÊU CẦU THAY ĐỔI GIẢ ĐỊNH (CHANGE REQUESTS)

### 3.1. Yêu cầu Thay đổi số 01 (CR-001): Tự động Cảnh báo Hợp đồng Lao động Hết hạn

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                         PHIẾU PHÂN TÍCH YÊU CẦU THAY ĐỔI (CR-001)                                │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ • Mã yêu cầu: CR-001                              • Ngày gửi yêu cầu: 15/01/2026 (Sprint 3)     │
│ • Người đề xuất: Bà Trần Thị B - Trưởng phòng HR  • Phân hệ ảnh hưởng: 1.4.1 (Hồ sơ & Hợp đồng)  │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. MÔ TẢ YÊU CẦU THAY ĐỔI:                                                                       │
│    Bổ sung tính năng quét tự động định kỳ vào 08h00 sáng mỗi ngày: Hệ thống tự động gửi email     │
│    thông báo tới HR Manager và chuyên viên nhân sự danh sách các hợp đồng lao động sẽ hết hạn    │
│    trong vòng 30 ngày tới, đồng thời tự động tạo bản nháp phụ lục gia hạn hợp đồng (Draft).       │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 2. LÝ DO ĐỀ XUẤT (WHY):                                                                          │
│    Theo quy định Bộ luật Lao động, người sử dụng lao động phải thông báo trước bằng văn bản cho  │
│    người lao động ít nhất 15 ngày trước khi hết hạn hợp đồng. Quy trình thủ công hiện tại dễ     │
│    quên, dẫn tới rủi ro hợp đồng tự động chuyển thành vô thời hạn hoặc bị phạt hành chính.      │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 3. ĐÁNH GIÁ TÁC ĐỘNG LÊN ĐƯỜNG CƠ SỞ HIỆU SUẤT (PMB IMPACT ANALYSIS):                           │
│    • Tác động Phạm vi (Scope): Bổ sung thêm 01 Job Cron-service Backend và 01 mẫu email HTML.   │
│    • Tác động Lịch trình (Schedule): Phát sinh thêm 03 ngày công phát triển của Dev 1. Do phân  │
│      hệ Hồ sơ Nhân sự (D) có Total Float = 18 ngày, việc tăng 03 ngày KHÔNG làm thay đổi         │
│      Đường Găng (CPM) và KHÔNG làm chậm ngày Go-Live 30/04/2026.                                │
│    • Tác động Chi phí (Cost): Chi phí nhân công phát sinh = 3 ngày x 1.250.000 đ = 3.750.000 đ;  │
│      chi phí kiểm thử = 1.750.000 đ. Tổng chi phí phát sinh = 5.500.000 VNĐ.                    │
│      -> Sử dụng Quỹ Dự trữ Dự phòng (Contingency Reserve), không làm vượt ngân sách trần 850 tr. │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 4. QUYẾT ĐỊNH CỦA HỘI ĐỒNG CCB:                                                                  │
│    [x] PHÊ DUYỆT CHÍNH THỨC (APPROVED)            [ ] TỪ CHỐI (REJECTED)                         │
│    Lý do: Lợi ích nghiệp vụ cao, rủi ro pháp lý giảm mạnh, không ảnh hưởng đường găng tiến độ.  │
│    Chữ ký Chủ tịch CCB: Nguyễn Văn A (Đã ký ngày 18/01/2026)                                     │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

### 3.2. Yêu cầu Thay đổi số 02 (CR-002): Bổ sung Phân hệ Quản lý Đào tạo Nội bộ (LMS)

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                         PHIẾU PHÂN TÍCH YÊU CẦU THAY ĐỔI (CR-002)                                │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ • Mã yêu cầu: CR-002                              • Ngày gửi yêu cầu: 10/02/2026 (Sprint 5)     │
│ • Người đề xuất: Ông Nguyễn Văn A - Tổng Giám đốc • Phân hệ ảnh hưởng: Thêm Module mới hoàn toàn │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. MÔ TẢ YÊU CẦU THAY ĐỔI:                                                                       │
│    Xây dựng thêm 01 phân hệ "Quản lý Đào tạo Nội bộ" cho phép phòng HR đăng tải tài liệu học tập,│
│    theo dõi tiến độ học của nhân viên mới và tổ chức các bài thi trắc nghiệm sát hạch chuyên môn.│
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 2. LÝ DO ĐỀ XUẤT (WHY):                                                                          │
│    Ban Giám đốc mong muốn tích hợp đồng bộ công tác đào tạo nhân sự nội bộ vào chung một phần   │
│    mềm duy nhất để nâng cao năng lực cho đội ngũ kỹ sư công nghệ.                               │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 3. ĐÁNH GIÁ TÁC ĐỘNG LÊN ĐƯỜNG CƠ SỞ HIỆU SUẤT (PMB IMPACT ANALYSIS):                           │
│    • Tác động Phạm vi (Scope): Bổ sung thêm 01 Module lớn cấp 3 trong WBS với 8 màn hình giao   │
│      diện và 12 bảng CSDL mới. Đây là một sự lạm phát phạm vi nghiêm trọng (Severe Scope Creep). │
│    • Tác động Lịch trình (Schedule): Dự toán thời gian phân tích, thiết kế, lập trình và kiểm   │
│      thử phát sinh tối thiểu **20 ngày làm việc (4 tuần)**. Thời điểm đề xuất (10/02) là giai   │
│      đoạn cao điểm phát triển module Tính lương. Nếu thực hiện sẽ làm ngày Go-Live bị đẩy lùi   │
│      từ 30/04 sang cuối tháng 05/2026, vi phạm cam kết mốc tiến độ M5.                          │
│    • Tác động Chi phí (Cost): Chi phí nhân công và hạ tầng phát sinh ước tính **85.000.000 VNĐ**.│
│      Khoản chi này vượt quá toàn bộ số dư Quỹ Contingency và vượt trần ngân sách 850 triệu.    │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 4. QUYẾT ĐỊNH CỦA HỘI ĐỒNG CCB:                                                                  │
│    [ ] PHÊ DUYỆT CHÍNH THỨC                       [x] BÁC BỎ / DỜI LẠI (REJECTED / DEFERRED)     │
│    Lý do bác bỏ: Đe dọa trực tiếp tới Đường Găng tiến độ và vượt trần ngân sách dự án.          │
│    Nghị quyết: Chuyển toàn bộ yêu cầu CR-002 vào Danh mục Sản phẩm bàn giao của Giai đoạn 2     │
│    (Phase 2) sau khi hệ thống cốt lõi đã go-live và vận hành ổn định trong 03 tháng.            │
│    Chữ ký Chủ tịch CCB: Nguyễn Văn A (Đã ký ngày 14/02/2026)                                     │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 4. NHẬT KÝ THEO DÕI THAY ĐỔI DỰ ÁN (CHANGE LOG)

Bảng Nhật ký Thay đổi cập nhật liên tục tình trạng xử lý các yêu cầu thay đổi:

| Mã CR | Ngày tiếp nhận | Người đề xuất | Tóm tắt Yêu cầu Thay đổi | Tác động Lịch trình | Tác động Chi phí (VNĐ) | Quyết định CCB | Ngày phê chuẩn | Trạng thái Thực thi |
|:---:|:---:|:---:|---|:---:|:---:|:---:|:---:|:---:|
| **CR-001** | 15/01/2026 | Trần Thị B *(HR Head)* | Tự động cảnh báo hợp đồng lao động hết hạn trước 30 ngày kèm tạo draft phụ lục. | +3 ngày *(Không đổi ngày Go-live)* | +5.500.000 *(Trích từ Contingency)* | **APPROVED** | 18/01/2026 | Đã lập trình & Đóng gói vào Sprint 4 |
| **CR-002** | 10/02/2026 | Nguyễn Văn A *(Sponsor)* | Xây dựng thêm Phân hệ Quản lý Đào tạo Nội bộ (LMS trắc nghiệm online). | +20 ngày *(Trễ Go-live 4 tuần)* | +85.000.000 *(Vượt ngân sách trần)* | **REJECTED** | 14/02/2026 | Đã chuyển sang Kế hoạch Phase 2 |

---

## 5. BÀI HỌC VỀ KIỂM SOÁT THAY ĐỔI

Việc kiên quyết từ chối CR-002 và chỉ chấp thuận CR-001 thể hiện tính kỷ luật và bản lĩnh quản trị dự án chuyên nghiệp của nhóm thực hiện:
* **Không thỏa hiệp với Scope Creep:** Việc một bên liên quan quyền lực cao nhất (Sponsor) đưa ra yêu cầu mới không đồng nghĩa với việc chấp nhận mù quáng. Vai trò của PM là phân tích định lượng tác động rõ ràng để giúp Sponsor đưa ra quyết định sáng suốt nhất cho tổng thể dự án.
* **Bảo vệ Đường Cơ sở Hiệu suất (PMB):** Mọi sự chấp thuận đều có nguồn lực dự phòng bảo đảm (Contingency Reserve) và nằm trong giới hạn Float an toàn của đường găng CPM.
