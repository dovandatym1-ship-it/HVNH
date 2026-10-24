# KẾ HOẠCH CHI PHÍ: ƯỚC TÍNH TỪ DƯỚI LÊN (BOTTOM-UP) VÀ ĐƯỜNG CƠ SỞ CHI PHÍ (S-CURVE)
## Dự án: Xây dựng Hệ thống Quản trị Nhân sự Nội bộ (ABC-HRM)
### Mã tài liệu: BTL-QLDA-B7 | Giai đoạn: Lập kế hoạch (Planning)
### Tiêu chuẩn áp dụng: PMI PMBOK Guide / Cost Baseline Engineering | Học phần: QLDA CNTT Nâng cao (HVNH)

---

## 1. NGUYÊN TẮC THIẾT LẬP KẾ HOẠCH QUẢN LÝ CHI PHÍ

Quản lý Chi phí là quy trình xác lập ngân sách, phân bổ nguồn vốn và kiểm soát chi phí thực tế nhằm đảm bảo dự án hoàn thành trong giới hạn ngân sách đã được phê duyệt.

Nhóm nghiên cứu áp dụng kỹ thuật **Ước tính Chi phí từ Dưới lên (Bottom-Up Cost Estimating)**: Phân rã chi phí chi tiết từ các gói công việc Cấp 4 (Work Packages) của WBS, sau đó tổng hợp lũy kế lên các cấp cha để hình thành Tổng chi phí ước tính trực tiếp. Từ đó, cộng thêm các khoản dự trữ tài chính theo đúng chuẩn mực PMBOK:
$$\text{Chi phí Ước tính Trực tiếp} + \text{Dự trữ Dự phòng (Contingency Reserve)} = \mathbf{\text{Đường cơ sở Chi phí (Cost Baseline / PMB)}}$$
$$\mathbf{\text{Cost Baseline}} + \text{Dự trữ Quản lý (Management Reserve)} = \mathbf{\text{Tổng Ngân sách Dự án (BAC)}}$$

---

## 2. BẢNG DỰ TOÁN CHI PHÍ TỪ DƯỚI LÊN (BOTTOM-UP COST ESTIMATING)

### 2.1. Chi phí Nhân công Dự án (Labor Costs - 5 Vị trí Nòng cốt)
Đơn giá ngày công và tháng công được tính toán dựa trên mức lương thị trường ngành CNTT tại Hà Nội cho nhân sự phát triển phần mềm bậc trung và cao cấp:

| STT | Vị trí Nhân sự Dự án | Thời gian tham gia | Định mức lương (VNĐ/tháng) | Thành tiền (VNĐ) | Diễn giải trách nhiệm chính |
|:---:|---|:---:|:---:|:---:|---|
| 1 | **Quản lý Dự án (PM / TV1)** | 6,0 tháng | 25.000.000 | 150.000.000 | Quản lý điều hành toàn diện, giám sát tiến độ, EVM, điều phối CCB |
| 2 | **Chuyên viên Phân tích (BA / TV2)** | 2,0 tháng | 20.000.000 | 40.000.000 | Khảo sát nghiệp vụ, lập SRS, thiết kế luồng quy trình, đào tạo HR |
| 3 | **Kỹ sư Phần mềm Cao cấp (Senior Dev / TV3)**| 4,0 tháng | 35.000.000 | 140.000.000 | Thiết kế kiến trúc, CSDL, phát triển engine Chấm công và Tính lương |
| 4 | **Kỹ sư Phần mềm 1 (Dev 1 / TV4)** | 4,0 tháng | 25.000.000 | 100.000.000 | Phát triển phân hệ Hồ sơ nhân sự, Tuyển dụng, Quản trị KPI |
| 5 | **Kỹ sư Phần mềm 2 (Dev 2 / TV4)** | 4,0 tháng | 25.000.000 | 100.000.000 | Phát triển phân hệ Dashboard, Frontend UI toàn hệ thống |
| 6 | **Kỹ sư Đảm bảo Chất lượng (QA / TV5)** | 2,5 tháng | 18.000.000 | 45.000.000 | Viết kịch bản kiểm thử, kiểm thử tải JMeter, điều phối nghiệm thu UAT |
| **I** | **Tổng Chi phí Nhân công Phát triển** | | | **575.000.000** | *(Chiếm 81,0% chi phí trực tiếp)* |

---

### 2.2. Chi phí Phi Nhân công (Non-Labor Costs)

| STT | Khoản mục Chi phí | Số lượng / Thời lượng | Đơn giá (VNĐ) | Thành tiền (VNĐ) | Diễn giải chi tiết |
|:---:|---|:---:|:---:|:---:|---|
| 1 | **Thuê Máy chủ Cloud VPS** | 6 tháng | 8.000.000 / tháng | 48.000.000 | 4 vCPU, 16GB RAM, SSD 200GB (chia Staging và Production) |
| 2 | **Bản quyền Phần mềm & Công cụ** | Trọn gói dự án | 20.000.000 | 20.000.000 | GitHub Enterprise, Jira Software, Figma Professional, SSL Certificate |
| 3 | **Tích hợp Thiết bị Phần cứng** | Trọn gói | 12.000.000 | 12.000.000 | Bản quyền SDK ZKTeco, thiết bị quét vân tay thử nghiệm phòng Lab |
| 4 | **Chuyển đổi Dữ liệu & Đào tạo** | Trọn gói | 55.000.000 | 55.000.000 | Chi phí làm sạch 100 hồ sơ Excel, in ấn tài liệu hướng dẫn, hội thảo UAT |
| **II** | **Tổng Chi phí Phi Nhân công** | | | **135.000.000** | *(Chiếm 19,0% chi phí trực tiếp)* |

$$\mathbf{\text{TỔNG CHI PHÍ ƯỚC TÍNH TRỰC TIẾP (DIRECT COST)}} = \mathbf{I} + \mathbf{II} = \mathbf{710.000.000 \text{ VNĐ}}$$

---

## 3. CƠ CẤU DỰ TRỮ TÀI CHÍNH VÀ THIẾT LẬP ĐƯỜNG CƠ SỞ CHI PHÍ

Căn cứ vào mức độ rủi ro công nghệ và tính chất của các gói công việc phát triển phần mềm, hai quỹ dự trữ tài chính được thiết lập:

### 3.1. Dự trữ Dự phòng (Contingency Reserve - 15%)
* **Mục đích:** Dành riêng để ứng phó với **các rủi ro đã nhận diện (Known-Unknowns)** được ghi nhận trong Sổ đăng ký Rủi ro (ví dụ: phát sinh chi phí chuyên gia giải quyết lỗi SDK chấm công, biến động công thức thuế TNCN, chi phí làm thêm giờ khi xử lý lỗi UAT).
* **Định mức trích lập:** $15\%$ trên tổng chi phí ước tính trực tiếp:
  $$\text{Contingency Reserve} = 710.000.000 \text{ VNĐ} \times 15\% = \mathbf{106.500.000 \text{ VNĐ}}$$
* **Thẩm quyền giải ngân:** Quản lý Dự án (PM) có quyền chủ động phê duyệt các khoản chi từ quỹ này khi các sự kiện rủi ro đã nhận diện trở thành hiện thực, với điều kiện ghi chép minh bạch vào Nhật ký Rủi ro và Báo cáo EVM.

$$\mathbf{\text{ĐƯỜNG CƠ SỞ CHI PHÍ (COST BASELINE)}} = 710.000.000 + 106.500.000 = \mathbf{816.500.000 \text{ VNĐ}}$$

---

### 3.2. Dự trữ Quản lý (Management Reserve - ~4%)
* **Mục đích:** Dành riêng cho **các rủi ro chưa biết, không lường trước được (Unknown-Unknowns)** phát sinh từ biến động vĩ mô hoặc yêu cầu chiến lược đột xuất của tổ chức. Quỹ này **không nằm trong Cost Baseline** nhưng nằm trong Tổng ngân sách dự án.
* **Định mức trích lập:** Khoảng $3,94\%$ tổng ngân sách:
  $$\text{Management Reserve} = \mathbf{33.500.000 \text{ VNĐ}}$$
* **Thẩm quyền phê duyệt:** Thuộc toàn quyền của Nhà tài trợ (Sponsor - Tổng Giám đốc). Khi cần sử dụng, PM phải lập hồ sơ trình Hội đồng Quản lý Thay đổi (CCB) và Sponsor phê chuẩn.

$$\mathbf{\text{TỔNG NGÂN SÁCH DỰ ÁN KHI HOÀN THÀNH (BAC)}} = 816.500.000 + 33.500.000 = \mathbf{850.000.000 \text{ VNĐ}}$$

---

## 4. PHÂN BỔ DÒNG TIỀN THEO THỜI GIAN VÀ ĐƯỜNG CONG CHI PHÍ (S-CURVE)

Đường cơ sở Chi phí (Cost Baseline = 816.500.000 VNĐ) được phân bổ theo 6 tháng triển khai căn cứ vào tiến độ thực hiện các gói công việc WBS:

| Tháng Triển khai | Giai đoạn & Công việc Trọng tâm WBS | Chi phí Kế hoạch Tháng ($PV_m$) | Chi phí Lũy kế Kế hoạch ($\sum PV$) | Tỷ lệ Hoàn thành Kế hoạch Lũy kế (%) |
|:---:|---|---:|---:|:---:|
| **Tháng 1** *(11/2025)* | Khởi tạo, Khảo sát hiện trạng, Lập tài liệu SRS (WBS 1.1, 1.2) | 85.000.000 VNĐ | 85.000.000 VNĐ | **10,4%** |
| **Tháng 2** *(12/2025)* | Thiết kế Kiến trúc, CSDL ERD, UI/UX Mockup (WBS 1.3) | 110.000.000 VNĐ | 195.000.000 VNĐ | **23,9%** |
| **Tháng 3** *(01/2026)* | Phát triển Phân hệ Hồ sơ, Chấm công & Tích hợp ZKTeco (WBS 1.4.1, 1.4.2) | 165.000.000 VNĐ | 360.000.000 VNĐ | **44,1%** |
| **Tháng 4** *(02/2026)* | Phát triển Phân hệ Tính lương, Tuyển dụng, KPI (WBS 1.4.3, 1.4.4, 1.4.5) | 185.000.000 VNĐ | 545.000.000 VNĐ | **66,7%** |
| **Tháng 5** *(03/2026)* | Phát triển Dashboard, Kiểm thử Tích hợp, Load Test (WBS 1.4.6, 1.5) | 150.000.000 VNĐ | 695.000.000 VNĐ | **85,1%** |
| **Tháng 6** *(04/2026)* | Nghiệm thu UAT, Di chuyển dữ liệu, Đào tạo & Go-live (WBS 1.6, 1.7) | 121.500.000 VNĐ | 816.500.000 VNĐ | **100,0%** |
| **Tổng cộng** | **Cost Baseline (PMB)** | **816.500.000 VNĐ** | | **100,0%** |

---

### Biểu đồ Đường Cong Chi Phí Tích Lũy (S-Curve Profile):

```
 Ngân sách Lũy kế (Triệu VNĐ)
  850 ┼──────────────────────────────────────────────────────────── BAC = 850 tr
  816 ┼───────────────────────────────────────────────────────●──── Cost Baseline = 816.5 tr
      │                                                  •'
  700 ┼─────────────────────────────────────────────•'  (85.1%)
      │                                        •'
  545 ┼───────────────────────────────────•'  (66.7%)
      │                              •'
  360 ┼─────────────────────────•'  (44.1%)
      │                    •'
  195 ┼───────────────•'  (23.9%)
      │          •'
   85 ┼─────•'  (10.4%)
    0 ┼─────┴───────────┴───────────┴───────────┴───────────┴───────────► Thời gian
         Tháng 1     Tháng 2     Tháng 3     Tháng 4     Tháng 5     Tháng 6
        (11/2025)   (12/2025)   (01/2026)   (02/2026)   (03/2026)   (04/2026)
```

> [!NOTE]
> **Nhận xét Đặc trưng Đường Cong S-Curve:**
> Dòng chi phí tăng tốc mạnh nhất ở giai đoạn giữa dự án (**Tháng 3 và Tháng 4 chiếm hơn 42% tổng ngân sách**). Đây là giai đoạn cao điểm huy động đồng thời 3 kỹ sư phát triển phần mềm (Senior Dev, Dev 1, Dev 2) tập trung code các phân hệ nặng nhất về mặt logic nghiệp vụ (Chấm công và Động cơ Tính lương). Dòng tiền hạ nhiệt dần ở Tháng 5 và Tháng 6 khi chuyển trọng tâm sang công tác kiểm thử chất lượng, đào tạo và đóng gói bàn giao.
