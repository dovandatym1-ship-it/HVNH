# KẾ HOẠCH QUẢN LÝ RỦI RO (RISK MANAGEMENT PLAN) & SỔ ĐĂNG KÝ 12 RỦI RO
## Dự án: Xây dựng Hệ thống Quản trị Nhân sự Nội bộ (ABC-HRM)
### Mã tài liệu: BTL-QLDA-B9 | Giai đoạn: Lập kế hoạch (Planning)
### Tiêu chuẩn áp dụng: PMI PMBOK Guide / ISO 31000:2018 | Học phần: QLDA CNTT Nâng cao (HVNH)

---

## 1. KHUNG TIẾP CẬN BẢN CHẤT: LÀM GÌ? TẠI SAO LÀM? LÀM THẾ NÀO?

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                             MÔ HÌNH TAM GIÁC QUẢN TRỊ RỦI RO DỰ ÁN                              │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. TẠI SAO LÀM? (WHY)                                                                           │
│    • Dự án phát triển phần mềm nội bộ có tỷ lệ thất bại hoặc vỡ ngân sách lên tới 45% (Standish │
│      Group Chaos Report) do các rủi ro kỹ thuật ẩn giấu và sự thay đổi kỳ vọng người dùng.     │
│    • Nếu không chủ động nhận diện rủi ro, dự án sẽ rơi vào trạng thái "chữa cháy" bị động, dẫn  │
│      tới cạn kiệt ngân sách 850 triệu và chậm trễ ngày go-live cam kết 30/04/2026.               │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 2. LÀM GÌ? (WHAT)                                                                                │
│    • Xây dựng Sổ Đăng ký Rủi ro (Risk Register) bao quát toàn diện 12 rủi ro thực tế (gồm 10    │
│      mối đe dọa tiêu cực và 02 cơ hội tích cực) phát sinh trong suốt vòng đời dự án.            │
│    • Thiết lập Ma trận Đánh giá Định tính 5x5 (Probability x Impact) để xếp hạng ưu tiên.       │
│    • Xác lập Kế hoạch Ứng phó Rủi ro cụ thể kèm dấu hiệu cảnh báo (Trigger Events).             │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 3. LÀM THẾ NÀO? (HOW)                                                                           │
│    • Áp dụng 4 chiến lược cho Mối đe dọa (Tránh né, Giảm thiểu, Chuyển giao, Chấp nhận) và 3   │
│      chiến lược cho Cơ hội (Khai thác, Tăng cường, Chia sẻ).                                     │
│    • Gán quyền sở hữu rủi ro (Risk Owner) cho từng cá nhân cụ thể trong nhóm dự án.             │
│    • Phân bổ Quỹ Dự trữ Dự phòng (Contingency Reserve = 106,5 triệu VNĐ) để sẵn sàng kích hoạt  │
│      kinh phí khi rủi ro chuyển thành vấn đề thực tế (Issues).                                   │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. PHƯƠNG PHÁP ĐÁNH GIÁ RỦI RO ĐỊNH TÍNH (QUALITATIVE RISK ANALYSIS)

### 2.1. Thang đo Xác suất (Probability - P)
* **Mức 1 (Rất thấp - Very Low):** Xác suất xảy ra $< 10\%$.
* **Mức 2 (Thấp - Low):** Xác suất xảy ra $10\% - 30\%$.
* **Mức 3 (Trung bình - Medium):** Xác suất xảy ra $31\% - 50\%$.
* **Mức 4 (Cao - High):** Xác suất xảy ra $51\% - 70\%$.
* **Mức 5 (Rất cao - Very High):** Xác suất xảy ra $> 70\%$.

### 2.2. Thang đo Tác động (Impact - I)
* **Mức 1 (Không đáng kể):** Chi phí phát sinh $< 5$ triệu VNĐ; tiến độ trễ $< 2$ ngày; không ảnh hưởng phạm vi.
* **Mức 2 (Nhẹ):** Chi phí $5 - 15$ triệu VNĐ; tiến độ trễ $3 - 5$ ngày; ảnh hưởng nhỏ tới tính năng phụ.
* **Mức 3 (Vừa phải):** Chi phí $15 - 35$ triệu VNĐ; tiến độ trễ $6 - 10$ ngày; cần tái phân bổ nhân lực.
* **Mức 4 (Nghiêm trọng):** Chi phí $35 - 70$ triệu VNĐ; tiến độ trễ $11 - 20$ ngày; đe dọa đường găng CPM.
* **Mức 5 (Thảm họa):** Chi phí $> 70$ triệu VNĐ; trễ tiến độ $> 20$ ngày; có nguy cơ đổ vỡ dự án hoặc vi phạm pháp luật.

### 2.3. Ma trận Nhiệt 5x5 và Phân Vùng Rủi ro (Risk Score = P x I)
* **Vùng Đỏ (Rủi ro Cao, Điểm 15 – 25):** Bắt buộc phải có kế hoạch ứng phó chi tiết, theo dõi hàng tuần, báo cáo trực tiếp tới PM và Sponsor.
* **Vùng Vàng (Rủi ro Trung bình, Điểm 8 – 14):** Chủ động theo dõi qua các buổi họp Sprint, thực hiện biện pháp giảm thiểu từ sớm.
* **Vùng Xanh (Rủi ro Thấp, Điểm 1 – 6):** Ghi vào danh sách theo dõi định kỳ (Watchlist), chấp nhận rủi ro có kiểm soát.

```
                  TÁC ĐỘNG (IMPACT)
           1: Rất nhẹ   2: Nhẹ    3: Vừa    4: Nặng   5: Rất nặng
        ┌───────────┬─────────┬─────────┬─────────┬───────────┐
  5: RC │     5     │   10    │ 15 (R8) │ 20 (R4) │    25     │
        ├───────────┼─────────┼─────────┼─────────┼───────────┤
  4: C  │     4     │ 8 (O12) │ 12 (R5) │ 16 (R3) │    20     │
XÁC     ├───────────┼─────────┼─────────┼─────────┼───────────┤
SUẤT    │     3     │    6    │ 9 (R6)  │ 12 (R2) │  15 (R1)  │
 (P)    │           │         │ 9 (O11) │ 9 (R9)  │           │
        ├───────────┼─────────┼─────────┼─────────┼───────────┤
  2: T  │     2     │    4    │    6    │ 8 (R7)  │  10 (R10) │
        ├───────────┼─────────┼─────────┼─────────┼───────────┤
  1: RT │     1     │    2    │    3    │    4    │     5     │
        └───────────┴─────────┴─────────┴─────────┴───────────┘
```

---

## 3. SỔ ĐĂNG KÝ RỦI RO CHI TIẾT (RISK REGISTER - 12 RỦI RO)

### 3.1. Danh mục 10 Mối Đe Dọa Tiêu cực (Negative Risks / Threats)

| Mã RR | Phân loại | Tên & Mô tả Chi tiết Rủi ro | $P$ | $I$ | Điểm | Dấu hiệu Cảnh báo (Trigger Event) | Chiến lược Ứng phó | Kế hoạch Hành động Cụ thể (Làm thế nào?) | Chủ sở hữu (Risk Owner) |
|:---:|---|---|:---:|:---:|:---:|---|:---:|---|:---:|
| **R1** | **Nhân sự** | Kỹ sư phần mềm cao cấp (Senior Dev) nghỉ việc đột xuất hoặc chuyển dự án | 3 | 5 | **15** *(Đỏ)* | Senior Dev vắng mặt thường xuyên, giảm tương tác trong Daily Stand-up | **Giảm thiểu (Mitigate)** | • Thực hiện Pair-Programming với Dev 1 ở các module găng.<br/>• Bắt buộc viết tài liệu API Swagger và review code 100%.<br/>• Duy trì cam kết thưởng hoàn thành dự án từ Sponsor. | **PM** |
| **R2** | **Pháp lý** | Thay đổi chính sách thuế TNCN hoặc trần đóng BHXH/BHYT trong quá trình phát triển | 3 | 4 | **12** *(Vàng)* | Quốc hội hoặc Chính phủ ban hành dự thảo Nghị định mới về tiền lương/bảo hiểm | **Giảm thiểu (Mitigate)** | • Thiết kế module tính lương dạng Rule-Engine cấu hình tham số động.<br/>• Tách bảng tham số thuế ra khỏi mã nguồn cứng (Hard-code).<br/>• Tham vấn luật sư lao động định kỳ mỗi tháng. | **BA & Senior Dev** |
| **R3** | **Kỹ thuật** | API/SDK máy chấm công ZKTeco không tương thích hoặc tài liệu kỹ thuật bị sai lệch | 4 | 4 | **16** *(Đỏ)* | Không nhận được tín hiệu Socket sau 2 ngày thử nghiệm tích hợp | **Tránh né & Giảm thiểu** | • Làm bản thử nghiệm kết nối kỹ thuật (PoC) ngay trong Sprint 1.<br/>• Xây dựng cơ chế dự phòng nạp file dữ liệu chấm công định dạng CSV.<br/>• Ký hợp đồng hỗ trợ kỹ thuật trực tiếp với nhà phân phối thiết bị. | **Senior Dev** |
| **R4** | **Phạm vi** | Lạm phát phạm vi (Scope Creep): Phòng HR hoặc Giám đốc liên tục đòi hỏi tính năng mới | 4 | 5 | **20** *(Đỏ)* | Các bên liên quan gửi yêu cầu bổ sung module ngoài SRS đã ký | **Tránh né (Avoid)** | • Ký văn bản Đóng băng Phạm vi (Scope Freeze) sau giai đoạn SRS.<br/>• Thực hiện nguyên tắc kiểm soát thay đổi nghiêm ngặt qua Hội đồng CCB.<br/>• Các yêu cầu ngoài phạm vi chuyển toàn bộ sang Giai đoạn 2 (Phase 2). | **PM & BA** |
| **R5** | **Dữ liệu** | Dữ liệu nhân sự từ 15 file Excel cũ bị sai lệch, trùng mã định danh nhân viên | 4 | 3 | **12** *(Vàng)* | Script kiểm tra phát hiện lỗi trùng khóa chính (Primary Key) khi chạy thử ETL | **Giảm thiểu (Mitigate)** | • Thành lập tổ công tác làm sạch dữ liệu (Data Cleansing) từ Tuần 4.<br/>• Xuất danh sách nhân viên trùng lặp gửi Trưởng phòng HR ký duyệt chuẩn hóa.<br/>• Khóa sổ nhập liệu trên Excel cũ trước ngày go-live 7 ngày. | **BA & Dev 1** |
| **R6** | **Tổ chức** | Cán bộ nhân viên phản đối, ngại thay đổi và không chịu chuyển sang thao tác phần mềm mới | 3 | 3 | **9** *(Vàng)* | Tỷ lệ nhân viên kích hoạt tài khoản thử nghiệm sau 1 tuần đạt $< 50\%$ | **Giảm thiểu (Mitigate)** | • Truyền thông nội bộ nhấn mạnh lợi ích: không phải làm đơn giấy, xem lương minh bạch.<br/>• Tổ chức đào tạo trực quan bằng video clip 3 phút.<br/>• Ban hành quy chế: Mọi đề xuất nghỉ phép chỉ được duyệt qua phần mềm. | **PM & HRM** |
| **R7** | **Hiệu năng** | Hệ thống bị nghẽn (Bottleneck) khi toàn bộ 100 nhân viên truy cập xem phiếu lương đồng thời | 2 | 4 | **8** *(Vàng)* | Thời gian phản hồi trang tăng vọt $> 5$ giây trong buổi chạy thử tải | **Giảm thiểu (Mitigate)** | • Áp dụng bộ nhớ đệm Redis Cache cho các dữ liệu ít biến động.<br/>• Tối ưu hóa câu truy vấn CSDL, đánh chỉ mục (Index) trên các bảng lớn.<br/>• Thực hiện Load Test bằng JMeter trước khi cấp quyền toàn diện. | **Senior Dev & QA** |
| **R8** | **Bảo mật** | Lộ lọt thông tin nhạy cảm về mức lương và số CCCD của cán bộ nhân viên | 3 | 5 | **15** *(Đỏ)* | Xuất hiện cảnh báo truy cập trái phép hoặc quét cổng từ bên ngoài | **Giảm thiểu (Mitigate)** | • Mã hóa dữ liệu cột lương bằng thuật toán đối xứng AES-256.<br/>• Bắt buộc xác thực 2 lớp (2FA) đối với tài khoản Admin và HR.<br/>• Kiểm thử bảo mật (Pentest) rà quét toàn diện OWASP Top 10. | **Tech Lead** |
| **R9** | **Tiến độ** | Khối Nghiệp vụ (HR, Kế toán) chậm trễ phản hồi và trì hoãn nghiệm thu các kịch bản UAT | 3 | 3 | **9** *(Vàng)* | Các ticket kiểm thử UAT bị treo quá 3 ngày làm việc mà không có xác nhận | **Giảm thiểu (Mitigate)** | • Thỏa thuận quy định thời hạn phản hồi (SLA) tối đa 48 giờ.<br/>• Cố định lịch họp nghiệm thu trực tiếp 2 buổi/tuần có mặt PM và Trưởng phòng HR.<br/>• Báo cáo Sponsor can thiệp khi tiến độ nghiệm thu bị tắc nghẽn. | **PM & BA** |
| **R10**| **Hạ tầng** | Sự cố máy chủ Cloud VPS bị sập nguồn hoặc mất kết nối mạng vào ngày Go-Live | 2 | 5 | **10** *(Vàng)* | Nhà cung cấp Cloud gửi cảnh báo bảo trì khẩn cấp hoặc mất kết nối mạng | **Chuyển giao & Giảm thiểu**| • Thuê Cloud VPS cam kết chất lượng dịch vụ SLA $\ge 99,9\%$.<br/>• Thiết lập kịch bản sao lưu CSDL tự động hàng ngày (Daily Backup).<br/>• Chuẩn bị sẵn máy chủ dự phòng Staging để chuyển hướng (Failover) trong $< 30$ phút. | **SysAdmin & Dev 2** |

---

### 3.2. Danh mục 02 Cơ Hội Tích Cực (Positive Risks / Opportunities)

| Mã CH | Phân loại | Tên & Mô tả Cơ hội Tích cực | $P$ | $I$ | Điểm | Dấu hiệu Kích hoạt (Trigger) | Chiến lược Tận dụng | Kế hoạch Hành động Cụ thể | Người phụ trách |
|:---:|---|---|:---:|:---:|:---:|---|:---:|---|:---:|
| **O11**| **Kinh doanh** | Doanh nghiệp mở thêm 2 chi nhánh mới, quy mô nhân sự tăng vọt lên 180 người | 3 | 3 | **9** *(Vàng)* | Ban Giám đốc công bố kế hoạch mở rộng thị trường miền Trung và miền Nam | **Khai thác (Exploit)** | • Thiết kế kiến trúc CSDL đa chi nhánh (Multi-branch) ngay từ đầu.<br/>• Đề xuất Ban Giám đốc ký kết Phụ lục hợp đồng mở rộng hệ thống (Phase 2), gia tăng giá trị kinh tế cho tổ chức. | **PM & BA** |
| **O12**| **Năng lực** | Đội ngũ kỹ sư dự án làm chủ hoàn toàn công nghệ mới (NestJS, Docker, React Hooks) | 4 | 2 | **8** *(Vàng)* | Tốc độ hoàn thành các User Stories trong Sprint 3 và Sprint 4 vượt 20% định mức | **Tăng cường (Enhance)** | • Đóng gói các thư viện nghiệp vụ dùng chung thành các gói nội bộ (NPM package).<br/>• Tổ chức Tech-sharing toàn công ty, nâng cao uy tín chuyên môn của nhóm dự án. | **Senior Dev** |

---

## 4. QUY TRÌNH THEO DÕI VÀ KÍCH HOẠT QUỸ DỰ PHÒNG RỦI RO (CONTINGENCY WORKFLOW)

```
        Sự kiện Rủi ro Xuất hiện Dấu hiệu Cảnh báo (Trigger Event)
                                  │
                                  ▼
             Risk Owner Báo cáo Ngay cho Quản lý Dự án (PM)
                                  │
                                  ▼
             PM Đánh giá Mức độ Tác động đến Đường Găng & Chi phí
                                  │
         ┌────────────────────────┴────────────────────────┐
         ▼                                                 ▼
[Tác động Nhỏ: Chi phí < 20 tr]            [Tác động Lớn: Đe dọa PMB]
  • Kích hoạt Kế hoạch Ứng phó               • Triệu tập Họp CCB Khẩn cấp
  • Giải ngân từ Quỹ Contingency             • Phân tích Tác động Toàn diện
  • Cập nhật Sổ Đăng ký Rủi ro               • Trình Sponsor Phê duyệt Điều chỉnh
```

---

## 5. KẾT LUẬN VỀ KẾ HOẠCH QUẢN TRỊ RỦI RO

Kế hoạch Quản lý Rủi ro với 12 rủi ro định danh chi tiết, ma trận nhiệt 5x5, và cơ chế ứng phó định lượng là "tấm khiên" bảo vệ vững chắc cho dự án **ABC-HRM**. Việc kết nối mật thiết giữa Sổ đăng ký Rủi ro với Quỹ Dự trữ Dự phòng (106,5 triệu VNĐ) đảm bảo mọi tình huống bất trắc đều có sẵn nguồn lực giải quyết, giữ vững mục tiêu hoàn thành dự án an toàn, đúng hạn và trong ngân sách.
