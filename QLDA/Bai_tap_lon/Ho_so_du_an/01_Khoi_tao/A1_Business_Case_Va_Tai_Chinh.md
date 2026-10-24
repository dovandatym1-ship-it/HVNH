# TÀI LIỆU KHOA HỌC DỰ ÁN: BUSINESS CASE & PHÂN TÍCH TÀI CHÍNH
## Dự án: Xây dựng Hệ thống Quản trị Nhân sự Nội bộ (ABC-HRM)
### Đơn vị thụ hưởng: Công ty Cổ phần ABC (Quy mô 100 nhân sự)
### Mã tài liệu: BTL-QLDA-A1 | Giai đoạn: Khởi tạo (Initiating)

---

## 1. TỔNG QUAN VÀ BỐI CẢNH DOANH NGHIỆP

### 1.1. Thực trạng Quản trị Nhân sự tại Công ty ABC
Công ty Cổ phần ABC là doanh nghiệp hoạt động trong lĩnh vực dịch vụ công nghệ thông tin và giải pháp số với quy mô nhân sự hiện tại là 100 nhân viên (bao gồm 70 kỹ sư phần mềm, 15 nhân viên kinh doanh/marketing, và 15 nhân viên khối vận hành, kế toán, nhân sự).

Hiện tại, công tác quản trị nhân lực của công ty đang được vận hành bởi phòng Nhân sự (gồm 3 chuyên viên) thông qua các công cụ thủ công truyền thống:
1. **Quản lý hồ sơ:** Sử dụng các bảng tính Microsoft Excel độc lập phân tán trên máy tính cá nhân, lưu trữ hợp đồng lao động và bằng cấp qua hồ sơ giấy kết hợp thư mục Google Drive không phân quyền chặt chẽ.
2. **Chấm công:** Nhân viên chấm công bằng máy quét vân tay tại văn phòng, tuy nhiên dữ liệu quét thô chỉ được trích xuất thủ công vào cuối tháng qua USB hoặc phần mềm đóng gói cục bộ không có kết nối API.
3. **Quản lý nghỉ phép:** Tiếp nhận đơn xin nghỉ phép, làm ngoài giờ (OT), đi công tác thông qua email hoặc đơn giấy ký tay, sau đó chuyên viên nhân sự nhập thủ công lại vào file tổng hợp.
4. **Tính lương & Phúc lợi:** Chuyên viên tiền lương mất trung bình 2 đến 3 ngày làm việc mỗi tháng để tổng hợp giờ công, đối chiếu ngày phép, áp công thức tính thuế thu nhập cá nhân (TNCN) và các khoản trích nộp Bảo hiểm xã hội (BHXH, BHYT, BHTN) trên các file Excel chứa hàng trăm dòng tính phức tạp.
5. **Đánh giá hiệu suất & Tuyển dụng:** Chưa có hệ thống theo dõi KPI tập trung; quy trình tuyển dụng và tiếp nhận nhân sự mới (onboarding) không có checklist chuẩn hóa, dẫn đến trải nghiệm nhân viên mới bị phân mảnh.

---

### 1.2. Phân tích Vấn đề và Lãng phí Định lượng (Problem Statement & Waste Analysis)

Qua quá trình điều tra hiện trạng, nhóm nghiên cứu đã lượng hóa các tổn thất và lãng phí trực tiếp trong mô hình vận hành cũ:

| Mã vấn đề | Lĩnh vực | Mô tả thực trạng | Tổn thất định lượng đo lường được |
|---|---|---|---|
| **PB-01** | Thời gian vận hành | Xử lý thủ công bảng công, đơn từ nghỉ phép và đối soát chấm công | Mất **15 giờ/tuần** của toàn đội ngũ HR (~60 giờ công/tháng, tương đương 0,38 FTE chuyên viên bậc trung). |
| **PB-02** | Xử lý tiền lương | Chốt bảng lương cuối tháng, tính toán các khoản trích theo lương | Mất **16 đến 24 giờ làm việc** mỗi kỳ lương; áp lực cao dẫn tới thời gian phát hành phiếu lương bị trễ hạn từ 2 đến 4 ngày. |
| **PB-03** | Sai lệch dữ liệu | Công thức Excel bị lỗi tham chiếu, nhầm lẫn ca làm việc và mức giảm trừ gia cảnh | Tỷ lệ khiếu nại sai sót lương trung bình **5,2%/tháng** (tương đương 5–6 nhân viên khiếu nại mỗi tháng), gây giảm sút lòng tin vào bộ máy quản lý. |
| **PB-04** | Rủi ro pháp lý | Sai sót trong cập nhật mức trần đóng BHXH hoặc khai báo biến động lao động chậm | Rủi ro bị cơ quan quản lý xử phạt hành chính; chi phí khắc phục sai sót và truy thu ước tính **50 triệu VNĐ/năm**. |
| **PB-05** | Biến động nhân sự | Thiếu minh bạch trong đánh giá KPI và lộ trình thăng tiến | Tỷ lệ nhân viên tự nguyện nghỉ việc (Turnover rate) năm liền trước đạt **18%**; chi phí tuyển dụng và đào tạo thay thế tốn kém. |
| **PB-06** | Hỗ trợ quyết định | Ban Giám đốc không có báo cáo tức thời (real-time) về biến động nhân sự và quỹ lương | Phải chờ phòng HR tổng hợp báo cáo mất từ 3 đến 5 ngày làm việc khi cần dữ liệu ra quyết định chiến lược. |

---

## 2. ĐỀ XUẤT GIẢI PHÁP VÀ MỤC TIÊU CHIẾN LƯỢC

### 2.1. Đề xuất Giải pháp Xây dựng Hệ thống ABC-HRM
Dự án đề xuất nghiên cứu, thiết kế và phát triển Hệ thống Quản trị Nhân sự Nội bộ (**ABC-HRM**) tập trung trên nền tảng Web Application, triển khai trên hạ tầng máy chủ Cloud riêng của công ty, bao gồm 6 phân hệ cốt lõi:
1. **Phân hệ Quản lý Hồ sơ Nhân sự:** Số hóa toàn diện vòng đời nhân viên từ khi ký hợp đồng thử việc đến khi thôi việc.
2. **Phân hệ Chấm công & Quản lý Nghỉ phép:** Tích hợp trực tiếp API/Webhook máy chấm công văn phòng; quy trình phê duyệt nghỉ phép trực tuyến nhiều cấp.
3. **Phân hệ Tính lương & Phúc lợi:** Tự động hóa tính toán Gross-to-Net, khấu trừ BHXH, thuế TNCN lũy tiến từng phần theo quy định pháp luật Việt Nam.
4. **Phân hệ Tuyển dụng & Onboarding:** Quản trị hồ sơ ứng viên, lịch phỏng vấn và lộ trình hội nhập chuẩn hóa.
5. **Phân hệ Quản trị Hiệu suất (KPI):** Thiết lập mục tiêu phòng ban/cá nhân, đánh giá định kỳ 360 độ và theo dõi tiến độ hoàn thành.
6. **Phân hệ Dashboard & Báo cáo Quản trị:** Cung cấp báo cáo trực quan cho HR Manager và Ban Giám đốc với các chỉ số đo lường hiệu suất nhân sự tức thời.

### 2.2. Sự Phù hợp Chiến lược (Strategic Alignment)
Dự án phù hợp với Chiến lược Chuyển đổi số Nội bộ của Công ty ABC giai đoạn 2025–2027, đóng vai trò là xương sống vận hành để chuẩn bị cho kế hoạch mở rộng quy mô công ty lên 150–200 nhân sự trong 3 năm tới mà không cần tăng tỷ lệ nhân sự quản lý gián tiếp.

---

## 3. PHÂN TÍCH TÀI CHÍNH CHI TIẾT (FINANCIAL FEASIBILITY ANALYSIS)

### 3.1. Dự toán Ngân sách Đầu tư Ban đầu (Initial Capital Investment - Year 0)
Tổng mức đầu tư cho dự án phát triển hệ thống trong 6 tháng được xác lập là **850.000.000 VNĐ** (Tám trăm năm mươi triệu đồng), chi tiết cấu thành như sau:

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

---

### 3.2. Lượng hóa Dòng Tiền Lợi ích Hàng năm (Annual Cash Inflows)
Hệ thống ABC-HRM sau khi vận hành ổn định sẽ mang lại các giá trị kinh tế định lượng trực tiếp hàng năm cho tổ chức:

1. **Tiết kiệm chi phí quỹ lương bộ phận gián tiếp:** Tự động hóa 80% công việc thủ công, giúp tối ưu hóa định biên nhân sự. Công ty không cần tuyển thêm 1 chuyên viên HR bậc trung khi mở rộng quy mô:
   $$B_1 = 15.000.000 \text{ VNĐ/tháng} \times 12 \text{ tháng} = \mathbf{180.000.000 \text{ VNĐ/năm}}$$
2. **Triệt tiêu chi phí sai lệch và phạt pháp lý:** Loại bỏ sai số tính lương thủ công, chấm dứt tình trạng truy thu thuế TNCN hoặc chậm nộp hồ sơ bảo hiểm:
   $$B_2 = \mathbf{50.000.000 \text{ VNĐ/năm}}$$
3. **Tiết kiệm chi phí tuyển dụng và đào tạo do giảm tỷ lệ thôi việc:** Nhờ minh bạch hóa đánh giá KPI, cải thiện trải nghiệm nhân sự, dự kiến giảm tỷ lệ thôi việc tự nguyện từ 18% xuống dưới 12% (giảm bình quân 6 lượt thôi việc/năm; chi phí tuyển dụng và đào tạo bình quân 20 triệu/vị trí):
   $$B_3 = 6 \text{ lượt} \times 20.000.000 \text{ VNĐ} = \mathbf{120.000.000 \text{ VNĐ/năm}}$$

$$\Rightarrow \mathbf{\text{Tổng dòng lợi ích định lượng hàng năm } (CF_t) = B_1 + B_2 + B_3 = 350.000.000 \text{ VNĐ/năm}}$$

*(Ghi chú: Lợi ích vô hình như nâng cao tính bảo mật dữ liệu nhân sự, tạo văn hóa làm việc số hóa, và khả năng ra quyết định nhanh chóng của Ban Giám đốc chưa được quy đổi thành tiền, thể hiện phương pháp đánh giá tài chính mang tính bảo thủ và an toàn).*

---

### 3.3. Bảng Dòng Tiền và Tính toán các Chỉ số Tài chính (Kịch bản Cơ sở)

* **Thời gian thẩm định:** 5 năm (vòng đời công nghệ tiêu chuẩn của một hệ thống quản trị nội bộ trước khi cần nâng cấp lớn).
* **Tỷ suất chiết khấu (Discount Rate - $r$):** **10,0%/năm** (dựa trên chi phí sử dụng vốn bình quân WACC của doanh nghiệp công nghệ trong nước).

#### Bảng Dòng tiền Chiết khấu 5 Năm (Đơn vị tính: Triệu VNĐ):

| Năm ($t$) | Dòng tiền ($CF_t$) | Hệ số chiết khấu $\frac{1}{(1+r)^t}$ | Dòng tiền chiết khấu ($DCF_t$) | Dòng tiền lũy kế chưa CK | Dòng tiền lũy kế có CK |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **Năm 0** | $-850,00$ | 1,0000 | $-850,00$ | $-850,00$ | $-850,00$ |
| **Năm 1** | $+350,00$ | 0,9091 | $+318,18$ | $-500,00$ | $-531,82$ |
| **Năm 2** | $+350,00$ | 0,8264 | $+289,26$ | $-150,00$ | $-242,56$ |
| **Năm 3** | $+350,00$ | 0,7513 | $+262,96$ | $+200,00$ | $+20,40$ |
| **Năm 4** | $+350,00$ | 0,6830 | $+239,06$ | $+550,00$ | $+259,46$ |
| **Năm 5** | $+350,00$ | 0,6209 | $+217,32$ | $+900,00$ | $+476,78$ |
| **Tổng cộng**| | | | **+900,00** | **+476,78** |

---

### 3.4. Kết quả Tính toán Các Chỉ số Đánh giá Hiệu quả Dự án

#### 1. Giá trị Hiện tại Thuần (Net Present Value - NPV):
$$NPV = \sum_{t=1}^{5} \frac{CF_t}{(1 + r)^t} - I_0 = 350 \times 3,79079 - 850 = 1.326,78 - 850 = \mathbf{+476,78 \text{ triệu VNĐ}}$$
* **Kết luận:** $NPV = +476,78 \text{ triệu VNĐ} > 0$. Dự án tạo ra giá trị gia tăng đáng kể cho tổ chức vượt trên chi phí cơ hội của vốn đầu tư.

#### 2. Tỷ suất Hoàn vốn Đầu tư (Return on Investment - ROI):
$$ROI = \frac{\text{Tổng lợi ích sau 5 năm} - \text{Vốn đầu tư ban đầu}}{\text{Vốn đầu tư ban đầu}} \times 100\% = \frac{1.750 - 850}{850} \times 100\% = \mathbf{105,88\%}$$
* **Kết luận:** Lợi nhuận ròng thu về đạt $105,88\%$ so với tổng vốn đầu tư, tương đương tỷ suất sinh lời bình quân hơn $21\%$/năm.

#### 3. Thời gian Hoàn vốn Thông thường (Simple Payback Period - PBP):
$$PBP_{\text{simple}} = \frac{850}{350} = \mathbf{2,43 \text{ năm}} \approx \mathbf{2 \text{ năm } 5 \text{ tháng}}$$
* Dự án thu hồi toàn bộ vốn đầu tư nguyên tệ vào giữa năm thứ 3.

#### 4. Thời gian Hoàn vốn Có Chiết khấu (Discounted Payback Period - DPBP):
Nhìn vào bảng dòng tiền lũy kế có chiết khấu, giá trị chuyển từ âm sang dương ở cuối Năm 2 sang Năm 3:
$$DPBP = 2 + \frac{|-242,56|}{262,96} = 2 + 0,922 = \mathbf{2,92 \text{ năm}} \approx \mathbf{2 \text{ năm } 11 \text{ tháng}}$$
* Kể cả khi tính đến giá trị thời gian của tiền tệ, dự án vẫn thu hồi xong toàn bộ vốn đầu tư trước khi kết thúc năm thứ 3 (trong chu kỳ khai thác 5 năm).

---

## 4. PHÂN TÍCH ĐỘ NHẠY (SENSITIVITY ANALYSIS)

Để lượng hóa mức độ rủi ro tài chính của dự án trước các biến động không lường trước từ thị trường và môi trường triển khai nội bộ, nhóm nghiên cứu xây dựng mô hình phân tích độ nhạy trên 3 kịch bản vận hành:

| Chỉ tiêu tài chính | Kịch bản Bi quan<br/>*(Dòng tiền giảm 20%)* | Kịch bản Cơ sở<br/>*(Dự báo chuẩn)* | Kịch bản Lạc quan<br/>*(Dòng tiền tăng 15%)* |
|---|:---:|:---:|:---:|
| **Dòng lợi ích hàng năm ($CF_t$)** | **280 triệu VNĐ** | **350 triệu VNĐ** | **402,5 triệu VNĐ** |
| Giả định tác động thực tế | Áp dụng chậm, chỉ giảm được 0,5 FTE, turnover giảm nhẹ | Vận hành chuẩn hóa theo kế hoạch sau 1 tháng go-live | Vận hành hoàn hảo, năng suất toàn công ty tăng vượt trội |
| **Tổng lợi ích 5 năm** | 1.400 triệu VNĐ | 1.750 triệu VNĐ | 2.012,5 triệu VNĐ |
| **NPV ($r = 10\%$)** | **+211,42 triệu VNĐ** | **+476,78 triệu VNĐ** | **+675,79 triệu VNĐ** |
| **ROI (5 năm)** | **64,71%** | **105,88%** | **136,76%** |
| **Thời gian hoàn vốn giản đơn** | **3,04 năm** | **2,43 năm** | **2,11 năm** |
| **Thời gian hoàn vốn có CK (DPBP)** | **3,73 năm** | **2,92 năm** | **2,46 năm** |
| **Đánh giá rủi ro** | Khả thi an toàn (NPV vẫn > 200 tr) | Đạt mục tiêu chiến lược | Hiệu quả vượt kỳ vọng |

> [!NOTE]
> **Nhận xét kết quả phân tích độ nhạy:** Ngay cả trong kịch bản bi quan nhất (dòng tiền lợi ích giảm 20% do việc ứng dụng công nghệ trong nội bộ gặp trở ngại), chỉ số NPV của dự án vẫn đạt mức **+211,42 triệu VNĐ** và thời gian hoàn vốn có chiết khấu là **3,73 năm** (vẫn hoàn tất trong vòng đời 5 năm). Điều này chứng minh dự án có biên an toàn tài chính rất cao và rủi ro thua lỗ vốn đầu tư là cực kỳ thấp.

---

## 5. BÁO CÁO PHÂN TÍCH SO SÁNH ĐỐI CHIẾU 5 NĂM: HIỆN TRẠNG (AS-IS) VS ÁP DỤNG ABC-HRM (TO-BE)

Để trả lời câu hỏi cốt lõi của Ban Lãnh đạo: *"Nếu áp dụng hệ thống ABC-HRM thì doanh nghiệp được gì, và nếu tiếp tục duy trì phương thức cũ thì hậu quả ra sao trong vòng 5 năm tới?"*, nhóm nghiên cứu xây dựng mô hình phân tích đối chiếu động (Dynamic Comparative Horizon) gắn liền với kế hoạch tăng trưởng nhân sự của Công ty ABC từ **100 nhân sự $\rightarrow$ 120 $\rightarrow$ 150 $\rightarrow$ 175 $\rightarrow$ 200 nhân sự** trong 5 năm:

### 5.1. Mô hình Dự báo Tăng trưởng Quy mô Doanh nghiệp (5-Year Growth Horizon)
* **Năm 1:** Quy mô 100 nhân sự (Vận hành năm đầu tiên sau Go-Live).
* **Năm 2:** Quy mô 120 nhân sự (+20% tăng trưởng dự án CNTT).
* **Năm 3:** Quy mô 150 nhân sự (Mở thêm chi nhánh miền Trung).
* **Năm 4:** Quy mô 175 nhân sự (Mở rộng thị trường giải pháp số).
* **Năm 5:** Quy mô 200 nhân sự (Doanh nghiệp đạt ngưỡng công ty công nghệ quy mô trung bình).

---

### 5.2. Bảng Đối Chiếu Chi Phí & Tổn Thất Tổng Thể 5 Năm (Head-to-Head 5-Year Cost & Waste Audit)
Đơn vị tính: Triệu VNĐ (VND Millions)

| Khoản mục So sánh | Năm 1 *(100 NS)* | Năm 2 *(120 NS)* | Năm 3 *(150 NS)* | Năm 4 *(175 NS)* | Năm 5 *(200 NS)* | TỔNG CỘNG 5 NĂM |
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

---

### 5.3. Bảng So Sánh Các Chỉ Số Hiệu Suất Vận Hành Qua 5 Năm (Operational KPIs)

| Tiêu chí Đánh giá | Mô hình Cũ: Tiếp tục dùng Excel (As-Is) | Mô hình Mới: Ứng dụng ABC-HRM (To-Be) | Đột phá Đạt được |
|---|---|---|---|
| **Khả năng mở rộng (Scalability)** | **Gãy đổ khi vượt 100 người:** File Excel chậm, xung đột phiên bản, mất công thức, rò rỉ lương. | **Mở rộng mượt mà lên 200–500 nhân sự** nhờ kiến trúc CSDL PostgreSQL và Redis Cache. | Hệ thống vững chắc, không cần đập đi xây lại |
| **Thời gian chốt bảng lương** | Tăng dần từ 3 ngày $\rightarrow$ 5 ngày $\rightarrow$ **7 ngày làm việc** khi lên 200 người. | Duy trì ổn định **$< 30$ giây** tính toán tự động (thực tế test 8,4 giây). | Rút ngắn 99,9% thời gian chờ đợi |
| **Định biên nhân sự quản lý (HR FTE)** | Phải tuyển thêm từ 3 HR lên **5 HR chuyên trách** (tỷ lệ 1 HR / 40 nhân viên). | Giữ nguyên **3 HR** phục vụ tốt 200 nhân sự (tỷ lệ 1 HR / 67 nhân viên). | Tiết kiệm tối thiểu 2 biên chế HR cố định |
| **Tỷ lệ khiếu nại sai lương** | Tăng vọt theo độ phức tạp: Từ 5,2% lên **$8\% - 10\%$**. | Triệt tiêu hoàn toàn về **$0,0\%$**. | 100% nhân viên an tâm cống hiến |
| **Khả năng ra quyết định của Lãnh đạo** | Mất từ 3 đến 5 ngày chờ phòng HR tổng hợp báo cáo thủ công. | Báo cáo trực quan hóa **tức thời (Real-time Dashboard)** trong 3 giây. | Ra quyết định kinh doanh thần tốc |

---

## 6. KẾT LUẬN VÀ KHUYẾN NGHỊ ĐẦU TƯ

1. **Về mặt nghiệp vụ:** Báo cáo so sánh đối chiếu 5 năm đã chứng minh tính tất yếu sống còn của dự án. Nếu tiếp tục duy trì Excel, chi phí lãng phí và vận hành phình to lên tới **7,42 tỷ đồng**, bộ máy HR trở nên cồng kềnh và hệ thống chắc chắn sẽ gãy đổ khi doanh nghiệp mở rộng lên 150–200 người.
2. **Về mặt tài chính:** Khoản đầu tư ban đầu 850 triệu VNĐ giúp doanh nghiệp thu hồi vốn sau **2,43 năm**, tạo ra giá trị tiết kiệm ròng lên tới **1,76 tỷ đồng** sau 5 năm và tỷ suất sinh lời $ROI = 105,88\%$.
3. **Khuyến nghị:** Kính đề nghị Ban Giám đốc Công ty Cổ phần ABC phê duyệt chủ trương đầu tư, thông qua bản Business Case này và tiến hành ký ban hành **Hiến chương Dự án (Project Charter)** để chính thức khởi động dự án theo kế hoạch.

