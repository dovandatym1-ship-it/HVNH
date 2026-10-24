---
marp: true
theme: gaia
_class: lead
paginate: true
backgroundColor: #181c22
color: #f8fafc
style: |
  section {
    font-family: 'Calibri', 'Segoe UI', 'Arimo', sans-serif;
  }
  h1, h2, h3 {
    font-family: 'Bebas Neue', 'Calibri', sans-serif;
    color: #ffffff;
  }
  .highlight-orange { color: #ea580c; }
  .highlight-gold { color: #f59e0b; }
  .highlight-cyan { color: #38bdf8; }
  .highlight-green { color: #10b981; }
  .highlight-red { color: #ef4444; }
---

# 🏛️ HỌC VIỆN NGÂN HÀNG (BANKING ACADEMY OF VIETNAM)
## BÁO CÁO BÀI TẬP GIỮA KỲ CHUYÊN ĐỀ CAO HỌC: XỬ LÝ & KHAI PHÁ DỮ LIỆU
### PHÂN TÍCH HÀNH VI, PHÂN CỤM & DỰ BÁO NGUY CƠ RỜI BỎ CỦA KHÁCH HÀNG THẺ TÍN DỤNG

* **Học viên thực hiện:** Đỗ Văn Đạt (Chuyên ngành Business Analytics)
* **Học phần đào tạo:** Xử lý và Khai phá Dữ liệu Sau Đại học (Khoa HTTTQL)
* **Tập dữ liệu thực nghiệm:** `BankChurners.csv` (10,127 quan sát • 23 thuộc tính)
* **Kết quả cốt lõi:** XGBoost ROC-AUC 0.9930 • Ngưỡng tối ưu $t^* = 0.42$ • Lợi nhuận ròng +$400,000 USD/năm (ROI 500%)
* **Niên khóa đào tạo:** 2025 - 2026 (Hà Nội, 2026)

<!--
Speaker Notes:
Kính thưa Thầy/Cô trong Hội đồng chấm bảo vệ và toàn thể các bạn học viên cao học. Hôm nay tôi xin phép được báo cáo kết quả nghiên cứu bài tập giữa kỳ môn Xử lý và Khai phá Dữ liệu với đề tài: 'Phân tích hành vi, Phân cụm và Dự báo nguy cơ rời bỏ của khách hàng thẻ tín dụng tại Ngân hàng thương mại'. Đề tài được thực hiện trên bộ dữ liệu thực tế 10,127 khách hàng với mục tiêu chuyển hóa năng lực dự báo Machine Learning thành giá trị kinh tế ròng cho ngân hàng.
-->

---

## 📋 MỤC LỤC & CẤU TRÚC BÁO CÁO (5 TRỤ CỘT CHIẾN LƯỢC)

* **TRỤ CỘT 01: TỔNG QUAN & BỐI CẢNH (Slide 03 — 04):** Bối cảnh kinh tế thẻ tín dụng, bài toán chi phí CAC ($250-300) vs CRC ($40-50, gấp 5:1) và Executive Abstract.
* **TRỤ CỘT 02: PHƯƠNG PHÁP & TIỀN XỬ LÝ (Slide 05 — 06):** Kiến trúc Pipeline 4 giai đoạn, làm sạch dữ liệu, kiểm soát rò rỉ nhãn Naive Bayes và 5 biến phái sinh tài chính.
* **TRỤ CỘT 03: KHÁM PHÁ EDA & PHÂN CỤM (Slide 07 — 13):** Khai phá EDA 6 chiều hành vi then chốt, kiểm định thống kê và phân cụm K-Means & PCA ($k=4$, Cụm 1 tập trung 52.6% Churn).
* **TRỤ CỘT 04: MÔ HÌNH HÓA DỰ BÁO & XAI (Slide 14 — 16):** Huấn luyện & so sánh 4 thuật toán Machine Learning, XGBoost dẫn đầu (ROC-AUC 0.9930, Recall 91.38%), kiểm soát sai số Loại II (8.62%) và giải thích XAI qua 5 đòn bẩy.
* **TRỤ CỘT 05: CHIẾN LƯỢC GIỮ CHÂN & ROI (Slide 17 — 21):** Tối ưu hóa ngưỡng kinh tế $t^* = 0.42$, 3 Chân dung khách hàng (Personas), Khung can thiệp 4 tầng EWS, mô phỏng tài chính ROI 500% và tổng kết Q&A.

<!--
Speaker Notes:
Báo cáo được cấu trúc thành 5 trụ cột chiến lược logic và chặt chẽ theo nguyên lý Pyramid Principle: Bắt đầu từ Bối cảnh thị trường và Bài toán chi phí CAC vs CRC; Tiếp nối là Phương pháp luận và Tiền xử lý dữ liệu ngăn ngừa rò rỉ; Kế đến là Khai phá EDA 6 chiều hành vi then chốt và Phân cụm khách hàng; Trọng tâm thực nghiệm là Mô hình hóa dự báo với XGBoost và Giải thích XAI; Và cuối cùng là Tối ưu hóa ngưỡng quyết định kinh tế cùng Khung chiến lược giữ chân 4 tầng tạo ROI 500%.
-->

---

## 🚀 01. EXECUTIVE SUMMARY: 4 PHÁT HIỆN TRỌNG TÂM

1. **16.07% Tỷ lệ rời bỏ tự nhiên:** 1,627/10,127 khách hàng đóng thẻ, gây thất thoát dòng tiền lãi quay vòng và phí giao dịch. Mất cân bằng lớp 1:5.22 đặt ra cạm bẫy 'Accuracy Paradox'.
2. **0.9930 ROC-AUC (XGBoost Classifier):** Vượt trội hoàn toàn so với Logistic Regression (0.9348) và Random Forest (0.9892), đạt Recall 91.38% (chỉ bỏ sót đúng 28/325 khách churn trong tập kiểm thử).
3. **t* = 0.42 Ngưỡng tối ưu kinh tế:** Thay thế ngưỡng 0.50 mặc định bằng hàm tối ưu Chi phí - Lợi ích, bảo vệ thêm nhiều khách hàng có giá trị cao, tạo thêm +$24,500 USD trên tập test.
4. **+$400,000 USD Lợi nhuận ròng / năm (ROI = 500%):** Trên quy mô 10,000 chủ thẻ, giữ chân thành công 960 khách hàng, bảo toàn $480,000 USD CLV với chi phí can thiệp chỉ $80,000 USD.

<!--
Speaker Notes:
Tại slide Tóm tắt điều hành này, tôi xin nhấn mạnh 4 kết quả then chốt nhất của toàn bộ nghiên cứu: Thứ nhất: Tỷ lệ rời bỏ tự nhiên 16.07% với tỷ lệ mất cân bằng 1:5.22, đòi hỏi không thể dùng Accuracy mà phải tập trung vào Recall và ROC-AUC. Thứ hai: Mô hình XGBoost Classifier đạt ROC-AUC 0.9930 và Recall 91.38%, chỉ bỏ sót 28 khách hàng rời bỏ. Thứ ba: Thay vì áp dụng ngưỡng cắt 0.50 mặc định, đề tài xác lập điểm cắt tối ưu t* = 0.42 mang lại lợi nhuận cao nhất. Và thứ tư: Mô phỏng tài chính chứng minh giải pháp tạo ra 400,000 USD lợi nhuận ròng hàng năm trên 10,000 khách hàng, đạt tỷ suất sinh lời ROI lên tới 500%.
-->

---

## 💰 02. BỐI CẢNH THỊ TRƯỜNG THẺ & BÀI TOÁN KINH TẾ (CAC VS CRC)

* **Chi phí thu hút khách hàng mới (CAC): $250 — $300 USD**
  * Marketing, tài trợ điểm bán, chi phí tra cứu CIC, thẩm định thu nhập, dập phôi thẻ và chuyển phát nhanh. Thời gian hoàn vốn kéo dài 18 - 24 tháng.
* **Chi phí giữ chân khách hàng (CRC): $40 — $50 USD (Quy tắc 5:1)**
  * E-voucher ưu đãi hoàn tiền, miễn phí thường niên có điều kiện, gọi điện chăm sóc giải quyết khiếu nại. Giữ lại ngay dòng tiền lãi thẻ hiện hữu.
* **Hệ thống Cảnh báo Sớm (Early Warning System - EWS):**
  * Chuyển đổi từ *ứng phó bị động* (khi khách hàng đã làm thủ tục đóng thẻ, tỷ lệ giữ chân ~0%) sang *cảnh báo sớm chủ động* bằng Machine Learning trước 2 - 3 tháng.

<!--
Speaker Notes:
Để hiểu rõ tại sao đề tài này có ý nghĩa sống còn đối với ngân hàng, chúng ta cần nhìn vào bài toán kinh tế học mảng thẻ: Quy tắc kinh tế 5:1 chỉ ra rằng chi phí thu hút một khách hàng thẻ mới (CAC) tiêu tốn tới 250 - 300 USD cho marketing, thẩm định CIC và phát hành thẻ. Trong khi đó, chi phí giữ chân một khách hàng cũ (CRC) chỉ tiêu tốn từ 40 - 50 USD. Nếu ngân hàng chỉ đợi khách hàng nộp đơn hủy thẻ mới can thiệp thì đã quá muộn. Mô hình Machine Learning đóng vai trò là một Hệ thống Cảnh báo sớm (EWS) giúp ngân hàng can thiệp trước 2 đến 3 tháng khi các tín hiệu sụt giảm giao dịch vừa chớm xuất hiện.
-->

---

## 🏗️ 03. PHƯƠNG PHÁP NGHIÊN CỨU: KIẾN TRÚC PIPELINE 4 BƯỚC

1. **Giai đoạn 01 — Tiền xử lý & Feature Engineering:** Xử lý Null, loại bỏ triệt để 2 cột rò rỉ nhãn Naive Bayes, mã hóa nhị phân Target và kiến tạo 5 biến phái sinh tài chính.
2. **Giai đoạn 02 — Khám phá Dữ liệu (EDA) & Phân cụm:** Phân tích đơn/đa biến 6 chiều hành vi, kiểm định thống kê (T-Test, Chi-Square), phân cụm K-Means ($k=4$) và giảm chiều PCA.
3. **Giai đoạn 03 — Mô hình hóa Dự báo:** Phân chia Stratified 80/20, huấn luyện & tối ưu 4 mô hình (LR, RF, SVM, XGBoost) qua Stratified 5-Fold Cross Validation.
4. **Giai đoạn 04 — Ứng dụng Quản trị & ROI:** Giải thích đòn bẩy bằng XAI (SHAP/Gain), tối ưu hóa ngưỡng cắt xác suất $t^*=0.42$, xây dựng 3 Personas và Khung chiến lược 4 tầng.

<!--
Speaker Notes:
Để đảm bảo tính chặt chẽ về mặt khoa học dữ liệu, đề tài tuân thủ quy trình Pipeline 4 giai đoạn khép kín: Giai đoạn 1 tập trung vào Tiền xử lý dữ liệu và Ngăn chặn rò rỉ dữ liệu (Data Leakage) — một lỗi rất phổ biến khi sử dụng bộ dữ liệu BankChurners. Giai đoạn 2 thực hiện Khám phá EDA trên 6 chiều dữ liệu kết hợp Phân cụm K-Means để bóc tách phân khúc. Giai đoạn 3 là Huấn luyện và Đánh giá 4 thuật toán Machine Learning qua Stratified 5-Fold Cross Validation. Và Giai đoạn 4 là Chuyển giao ứng dụng quản trị: Giải thích XAI, Tối ưu ngưỡng cắt kinh tế và Đo lường ROI định lượng.
-->

---

## ⚙️ 04. TIỀN XỬ LÝ DỮ LIỆU & KIẾN TẠO 5 BIẾN PHÁI SINH

* **Làm sạch & Kiểm soát Rò rỉ Nhãn (Data Leakage):**
  * Bộ dữ liệu 10,127 bản ghi đầy đủ, không phát hiện giá trị Null.
  * **Loại bỏ triệt để 2 cột Naive Bayes** ở cuối bảng gốc để ngăn ngừa Data Leakage làm mô hình đạt kết quả hoàn hảo giả tạo.
  * Mã hóa Target: `Attrited Customer` = 1 (1,627 khách), `Existing Customer` = 0 (8,500 khách).
* **5 Biến Phái Sinh Tài Chính Mới (Feature Engineering):**
  1. `Trans_Ct_Density`: Mật độ quẹt thẻ ($Total\_Trans\_Ct / Months\_on\_book$).
  2. `Trans_Amt_per_Capita`: Chi tiêu bình quân ($Total\_Trans\_Amt / Total\_Trans\_Ct$).
  3. `Revolving_Ratio`: Tỷ lệ dư nợ quay vòng trên hạn mức ($Revolving\_Bal / Credit\_Limit$).
  4. `Total_Interaction_Ct`: Tổng tương tác rủi ro ($Contacts + Months\_Inactive$).
  5. `Open_To_Buy_Ratio`: Tỷ lệ hạn mức khả dụng ($Avg\_Open\_To\_Buy / Credit\_Limit$).

<!--
Speaker Notes:
Về mặt kỹ thuật dữ liệu, đề tài đặc biệt lưu ý đến tính hợp lệ của bài toán: Nhiều nghiên cứu trước đây đã mắc lỗi nghiêm trọng khi giữ lại 2 cột Naive Bayes ở cuối bảng BankChurners, dẫn đến hiện tượng Data Leakage làm mô hình đạt kết quả hoàn hảo giả tạo. Nghiên cứu của tôi đã loại bỏ triệt để 2 cột này trước mọi bước xử lý. Đồng thời, đề tài kiến tạo 5 biến phái sinh tài chính mới: nổi bật nhất là biến Mật độ quẹt thẻ (Trans_Ct_Density) và Tỷ lệ đòn bẩy nợ (Revolving_Ratio). Các biến này sau đó được chứng minh là có giá trị giải thích vượt trội trong mô hình XGBoost.
-->

---

## 📊 05. EDA 1 — PHÂN BỐ BIẾN MỤC TIÊU & MẤT CÂN BẰNG LỚP

* **Tỷ lệ khách hàng rời bỏ (Churn):** 16.07% ($1,627$ khách hàng đã đóng thẻ).
* **Tỷ lệ khách hàng duy trì (Existing):** 83.93% ($8,500$ khách hàng đang hoạt động).
* **Tỷ lệ mất cân bằng (Imbalance Ratio):** Xấp xỉ **$1 : 5.22$**.
* **Cạm bẫy độ chính xác (Accuracy Paradox):** Dự báo toàn bộ khách hàng ở lại vẫn đạt Accuracy 83.93% nhưng thất bại hoàn toàn trong việc phát hiện khách Churn.
* **Chiến lược Metric:** Ưu tiên tối thượng cho **Recall**, **F1-Score** và diện tích dưới đường cong **ROC-AUC / PR-AUC**.
* *(Xem biểu đồ chi tiết tại `figures/01_churn_distribution.png`)*

<!--
Speaker Notes:
Kính thưa Hội đồng, bước vào phần Khám phá dữ liệu EDA, phát hiện đầu tiên là sự mất cân bằng lớp 1:5.22 với 16.07% khách hàng rời bỏ. Nếu chỉ nhìn vào Accuracy, một mô hình dự báo toàn bộ khách hàng ở lại vẫn đạt tới gần 84% độ chính xác nhưng hoàn toàn vô giá trị về mặt thực tiễn. Vì vậy, toàn bộ nghiên cứu này tập trung vào Recall (khả năng phát hiện đúng khách hàng churn) và diện tích dưới đường cong ROC-AUC.
-->

---

## 👥 06. EDA 2 — NHÂN KHẨU HỌC: HIỆN TƯỢNG PHÂN HÓA 2 ĐẦU THU NHẬP

* **Khác biệt giới tính:** Nữ giới có tỷ lệ rời bỏ **17.36%**, cao hơn đáng kể so với Nam giới (14.62%), phản ánh sự nhạy cảm cao với các chương trình hoàn tiền mua sắm.
* **Độ tuổi tập trung:** Khách hàng trung niên **40 - 50 tuổi** (trung bình 46.3 tuổi) có xu hướng chuyển đổi dịch vụ thẻ cao nhất.
* **Hiện tượng rủi ro phân hóa 2 đầu thu nhập (Bimodal Churn Risk):**
  * Nhóm thu nhập thấp **< $40K** (Churn 17.19%): Nhạy cảm với phí thường niên và lãi suất vay.
  * Nhóm thu nhập cao **> $120K** (Churn 17.33%): Nhạy cảm với đặc quyền thẻ VIP phòng chờ sân bay/golf.
  * Nhóm thu nhập trung bình **$60K - $80K** có tỷ lệ rời bỏ thấp nhất (chỉ 13.48%).
* *(Xem biểu đồ chi tiết tại `figures/02_demographic_churn.png`)*

<!--
Speaker Notes:
Khám phá nhân khẩu học chỉ ra một phát hiện rất thú vị: Hiện tượng rủi ro phân hóa 2 đầu thu nhập. Nhóm thu nhập thấp dưới 40K USD và nhóm thu nhập cao trên 120K USD đều có tỷ lệ đóng thẻ cao trên 17%, nhưng nguyên nhân hoàn toàn khác nhau. Nhóm thu nhập thấp nhạy cảm với biểu phí thường niên, trong khi nhóm VIP dễ bị ngân hàng đối thủ lôi kéo bởi các đặc quyền thẻ thượng lưu.
-->

---

## 💳 07. EDA 3 — HÀNH VI GIAO DỊCH: VÙNG BÁO ĐỘNG ĐỎ

* **Tần suất quẹt thẻ (Total_Trans_Ct):** Khách hàng Churn chỉ quẹt thẻ trung bình **44.9 lần/năm** (so với 68.7 lần của khách hàng ở lại, sụt giảm 34.6%).
* **VÙNG BÁO ĐỘNG ĐỎ:** Khách hàng có **dưới 55 lần quẹt thẻ** và **chi tiêu dưới $3,000 USD** có xác suất rời bỏ tăng vọt lên trên 60%.
* **Tổng giá trị chi tiêu (Total_Trans_Amt):** Khách hàng Churn chi tiêu trung bình $3,095 USD/năm so với $4,654 USD của nhóm duy trì.
* **Ý nghĩa thực tiễn:** Tần suất sử dụng thẻ chính là "nhịp tim" phản ánh mức độ gắn bó hàng ngày của khách hàng với ngân hàng.
* *(Xem biểu đồ chi tiết tại `figures/03_transaction_behavior_churn.png`)*

<!--
Speaker Notes:
Về hành vi giao dịch, tần suất quẹt thẻ chính là chiếc 'nhiệt kế' đo lường sức khỏe khách hàng. Khách hàng rời bỏ chỉ quẹt thẻ trung bình 44 lần một năm, sụt giảm tới 35%. Khi phân tích biểu đồ phân tán, chúng tôi phát hiện ra một 'Vùng báo động đỏ': Khách hàng có dưới 55 lần quẹt thẻ và chi tiêu dưới 3,000 USD có nguy cơ đóng thẻ lên tới hơn 60%.
-->

---

## 📉 08. EDA 4 — CHỈ SỐ TÀI CHÍNH: HIỆN TƯỢNG DƯ NỢ VỀ $0 (SILENT CHURN)

* **Dư nợ quay vòng (Total_Revolving_Bal):** Khách hàng Churn có dư nợ trung bình chỉ **$672 USD** so với $1,256 USD của khách hàng ở lại.
* **Hiện tượng rút lui lặng lẽ (Silent Churn):** Gần **55% khách hàng rời bỏ có dư nợ bằng đúng $0 USD**, cho thấy hành vi chủ động thanh toán hết nợ trước khi hủy thẻ.
* **Tỷ lệ sử dụng hạn mức:** Sụt giảm về mức **16.2%** (so với 29.6% của nhóm ở lại).
* **Biến thiên chi tiêu Q4/Q1:** Tần suất giao dịch quý gần nhất sụt giảm tới **45%** trước khi đóng thẻ.
* *(Xem biểu đồ chi tiết tại `figures/04_financial_ratios_churn.png`)*

<!--
Speaker Notes:
Khám phá thứ tư mang tên 'Hiện tượng rút lui lặng lẽ' (Silent Churn). Gần 55% khách hàng rời bỏ có dư nợ quay vòng bằng đúng 0 USD tại thời điểm ghi nhận dữ liệu. Họ không thông báo trước cho ngân hàng mà lặng lẽ trả hết nợ thẻ, ngưng quẹt thẻ mới, và sau đó 1-2 tháng mới chính thức yêu cầu đóng tài khoản. Đây là cơ hội bằng vàng để ngân hàng kích hoạt ưu đãi giữ chân.
-->

---

## 📞 09. EDA 5 — TƯƠNG TÁC CSKH: NGƯỠNG BÙNG PHÁT TẠI LẦN GỌI THỨ 3

* **Tương quan số cuộc gọi tổng đài (Contacts_Count_12_mon):**
  * Gọi 1 - 2 lần: Tỷ lệ Churn ở mức bình thường (~14%).
  * **Gọi 3 lần: Tỷ lệ Churn tăng gấp đôi lên 28.6%.**
  * **Gọi 4 lần: Tỷ lệ Churn tăng vọt lên 52.4%.**
  * **Gọi 6 lần: Tỷ lệ Churn đạt tuyệt đối 100%.**
* **Bản chất nghiệp vụ:** Phản ánh sự thất bại trong chỉ tiêu First-Contact Resolution (FCR), khiếu nại biểu phí hoặc tra soát bị kéo dài.
* **Mức độ ngủ đông:** Không phát sinh giao dịch $\ge 3$ tháng làm tăng nguy cơ Churn gấp 2.5 lần.
* *(Xem biểu đồ chi tiết tại `figures/05_interaction_decay_churn.png`)*

<!--
Speaker Notes:
Phân tích về kênh liên hệ tổng đài CSKH bộc lộ một sự thật nghiêm túc về mặt trải nghiệm khách hàng. Nếu khách hàng chỉ gọi 1-2 lần, tỷ lệ rời bỏ ở mức bình thường. Nhưng đến cuộc gọi thứ 3, tỷ lệ Churn tăng gấp đôi lên 28.6%, gọi lần 4 tăng lên 52% và gọi lần 6 thì 100% khách hàng đóng thẻ. Điều này phản ánh các khiếu nại của khách hàng bị đùn đẩy, xử lý chậm trễ khiến họ bức xúc và quyết định hủy thẻ.
-->

---

## 🔗 10. EDA 6 — HỆ SINH THÁI SẢN PHẨM: HIỆU ỨNG KHÓA CHÂN (LOCK-IN)

* **Số lượng sản phẩm nắm giữ (Total_Relationship_Count):**
  * Sử dụng 1 - 2 sản phẩm: Tỷ lệ Churn lên tới **25.4%** (Chi phí chuyển đổi = 0).
  * **Sử dụng $\ge 4$ sản phẩm: Tỷ lệ Churn giảm mạnh chỉ còn 9.8% - 12.5%.**
* **Hiệu ứng khóa chân (Lock-in Effect):** Sử dụng đa sản phẩm (tài khoản lương, tiết kiệm, thấu chi, bảo hiểm) tạo rào cản chuyển đổi tự nhiên rất vững chắc.
* **Phân hạng thẻ:** Dòng thẻ Blue chiếm 93.2%; các dòng thẻ cao cấp Silver/Gold/Platinum có tỷ lệ Churn cao hơn do kỳ vọng đặc quyền dịch vụ VIP khắt khe.
* *(Xem biểu đồ chi tiết tại `figures/08_relationship_and_card.png`)*

<!--
Speaker Notes:
Điểm chạm cuối cùng của phần EDA là Hệ sinh thái sản phẩm và Hiệu ứng khóa chân (Lock-in Effect). Nếu khách hàng chỉ dùng 1-2 sản phẩm, chi phí chuyển đổi của họ bằng 0 nên tỷ lệ rời bỏ lên tới trên 25%. Ngược lại, nếu khách hàng sử dụng từ 4 sản phẩm trở lên, tỷ lệ rời bỏ giảm ngoạn mục xuống dưới 10%. Đây là bằng chứng đanh thép ủng hộ chiến lược bán chéo các sản phẩm gắn kết như tài khoản nhận lương và tiền gửi thanh toán.
-->

---

## 🎯 11. KHAI PHÁ DỮ LIỆU — PHÂN CỤM K-MEANS & PCA (k=4)

* **Tối ưu hóa số cụm:** Phương pháp Elbow và Silhouette Score (0.34) xác nhận $k=4$ là cấu trúc phân cụm tối ưu.
* **Đặc trưng 4 phân cụm hành vi:**
  * **Cụm 1 — Tâm điểm Rủi ro (52.6% tổng Churn):** Quẹt thẻ ít (42 lần), chi tiêu thấp ($2,850), dư nợ về 0 $\rightarrow$ *Trọng tâm can thiệp số 1*.
  * **Cụm 0 — Phổ thông Tích cực (38.5% danh mục):** Quẹt thẻ đều (65 lần), Churn thấp (11.2%).
  * **Cụm 2 — Khách hàng VIP:** Hạn mức cao (>$20,000), thu nhập $120K+, nhạy cảm với đặc quyền.
  * **Cụm 3 — Siêu giao dịch (Super Users):** Quẹt thẻ >105 lần, chi tiêu >$14,000, Churn < 2%.
* *(Xem biểu đồ chi tiết tại `figures/10_kmeans_clusters_pca.png`)*

<!--
Speaker Notes:
Trước khi bước vào huấn luyện Machine Learning có giám sát, nghiên cứu áp dụng thuật toán học không giám sát K-Means kết hợp giảm chiều PCA. Kết quả chỉ ra cấu trúc 4 phân cụm tối ưu. Trong đó, Cụm 1 được định danh là 'Tâm điểm rủi ro' khi tập trung tới 52.6% tổng lượng khách hàng rời bỏ của toàn bộ ngân hàng. Nhờ phân đoạn này, ngân hàng tránh được việc áp dụng các chính sách chăm sóc cào bằng tốn kém, mà tập trung ngân sách chính xác vào Cụm 1.
-->

---

## 🏆 12. MÔ HÌNH HÓA MÁY HỌC — SO SÁNH 4 MÔ HÌNH (WINNER: XGBOOST)

| Mô hình thuật toán | ROC-AUC | Recall | Precision | F1-Score | Đánh giá kỹ thuật |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **1. Logistic Regression** | 0.9348 | 83.38% | 56.32% | 67.25% | Baseline tuyến tính, bắt sót tương tác phức tạp |
| **2. Random Forest** | 0.9892 | 88.31% | 91.69% | 89.97% | Rất mạnh, kiểm soát tốt Overfitting |
| **3. SVM** | 0.9702 | 84.62% | 78.30% | 81.34% | Nhạy cảm với phân bố biên dữ liệu |
| **4. XGBoost Classifier** | **0.9930** | **91.38%** | **91.08%** | **91.23%** | 🏆 **TOP PERFORMER — Vượt trội toàn diện** |

* *(Xem biểu đồ chi tiết tại `figures/11_ml_model_comparison_roc.png`)*

<!--
Speaker Notes:
Kính thưa Hội đồng, đây là kết quả thực nghiệm mô hình hóa cốt lõi của đề tài. Bốn thuật toán Machine Learning đại diện đã được thử nghiệm độc lập trên tập kiểm thử 2,026 quan sát. Kết quả cho thấy XGBoost Classifier là mô hình chiến thắng toàn diện, đạt diện tích ROC-AUC lên tới 0.9930, Recall 91.38% và Precision 91.08%. Đường cong ROC màu cam của XGBoost áp sát góc trên bên trái, thể hiện năng lực phân tách thực nghiệm vượt trội so với Random Forest và Logistic Regression.
-->

---

## 🎯 13. ĐÁNH GIÁ SAI SỐ: MA TRẬN NHẦM LẪN (CONFUSION MATRIX)

* **Tập kiểm thử Test Set:** Gồm 2,026 khách hàng (1,701 Existing và 325 Attrited).
* **Kiểm soát Sai số Loại II (False Negative - Bỏ sót Churn):**
  * Bắt đúng $297 / 325$ khách hàng rời bỏ thực tế.
  * Chỉ bỏ sót **28 khách hàng** (Tỷ lệ sai sót cực thấp: **8.62%**).
* **Kiểm soát Sai số Loại I (False Positive - Báo động giả):**
  * Chỉ có **36 / 1,701** khách hàng ở lại bị dự báo nhầm thành Churn (Tỷ lệ báo động giả: **2.12%**).
* **Precision đạt 91.08%:** Cứ 100 cảnh báo đưa ra thì có hơn 91 cảnh báo chính xác tuyệt đối.
* *(Xem biểu đồ chi tiết tại `figures/12_ml_confusion_matrices.png`)*

<!--
Speaker Notes:
Trong bài toán ngân hàng, việc hiểu rõ Ma trận nhầm lẫn là yếu tố quyết định hiệu quả triển khai. Sai số Loại II (bỏ sót khách rời bỏ) là sai số gây tổn thất nặng nề nhất. Mô hình XGBoost đã kiểm soát sai số này ở mức ấn tượng: Trong 325 khách rời bỏ, chỉ bỏ sót duy nhất 28 khách (tỷ lệ 8.6%). Đồng thời, tỷ lệ báo động giả (Sai số Loại I) chỉ ở mức 2.12%, đảm bảo bộ phận CSKH không bị lãng phí công sức gọi điện chăm sóc những khách hàng vốn dĩ đang rất hài lòng.
-->

---

## 🔑 14. GIẢI THÍCH MÔ HÌNH (XAI): 5 ĐÒN BẨY HÀNH VI QUYẾT ĐỊNH

1. **`Total_Trans_Ct` (Tần suất quẹt thẻ - Top 1 > 25% Feature Importance):** Yếu tố quyết định sống còn. Khách hàng ngưng quẹt thẻ là dấu hiệu rời bỏ rõ nét nhất.
2. **`Total_Amt_Chng_Q4_Q1` (Tốc độ sụt giảm chi tiêu):** Đòn bẩy cảnh báo sớm số 2, phản ánh dòng tiền thanh toán bị rút dần sang đối thủ.
3. **`Total_Revolving_Bal` (Dư nợ quay vòng):** Tín hiệu tất toán nợ về $0 USD trước 30-60 ngày đóng thẻ.
4. **`Total_Trans_Amt` (Tổng giá trị chi tiêu):** Đo lường quy mô tài chính của chủ thẻ.
5. **`Total_Relationship_Count` (Số lượng sản phẩm):** Rào cản chuyển đổi bảo vệ hệ sinh thái.
* *(Xem biểu đồ chi tiết tại `figures/13_feature_importance_xgb.png`)*

<!--
Speaker Notes:
Để giải quyết vấn đề mô hình 'Hộp đen' (Black-box), nghiên cứu đã áp dụng kỹ thuật Explainable AI để trích xuất 5 đòn bẩy quan trọng nhất. Đứng đầu bảng với hơn 25% trọng số là Tổng số lần giao dịch, tiếp theo là Mức độ sụt giảm chi tiêu quý 4 so với quý 1 và Dư nợ quay vòng. Điều này hoàn toàn khớp với logic ngân hàng: Khách hàng không bao giờ bỏ đi đột ngột mà luôn trải qua quá trình giảm tần suất quẹt thẻ và thanh toán hết nợ trước đó vài tháng.
-->

---

## 💰 15. TỐI ƯU HÓA NGƯỠNG QUYẾT ĐỊNH KINH TẾ (t* = 0.42)

* **Hạn chế của ngưỡng mặc định $t = 0.50$:** Bỏ lỡ các khách hàng có xác suất churn 40% - 49% nhưng có giá trị vòng đời (CLV) rất lớn.
* **Hàm tối ưu Chi phí - Lợi ích (Cost-Benefit Function):**
  $$\text{Net Profit}(t) = \text{CLV} \times \text{Success\_Rate} \times \text{TP}(t) - \text{Cost} \times [\text{TP}(t) + \text{FP}(t)]$$
* **Xác lập điểm tối ưu $t^* = 0.42$:** Điểm cực đại của đường cong Net Benefit Curve, tối đa hóa lợi nhuận ròng và gia tăng thêm **+$24,500 USD** so với ngưỡng 0.50.
* *(Xem biểu đồ chi tiết tại `figures/14_cost_benefit_threshold_optimization.png`)*

<!--
Speaker Notes:
Một đóng góp quan trọng của đề tài là không áp dụng máy móc ngưỡng cắt xác suất 0.50 mặc định, mà xây dựng hàm tối ưu hóa Chi phí - Lợi ích thực tế cho ngân hàng. Với giá trị khách hàng giữ lại được là 500 USD và chi phí can thiệp chỉ 50 USD, việc hạ ngưỡng cắt xác suất xuống t = 0.42 cho phép ngân hàng chủ động can thiệp sớm vào nhóm khách hàng chớm có nguy cơ. Đường cong Net Benefit chứng minh tại t = 0.42, ngân hàng thu được lợi nhuận kinh tế ròng tối đa, cao hơn 24,500 USD so với ngưỡng 0.50 trên tập test.
-->

---

## 🎭 16. PHÁC HỌA 3 CHÂN DUNG KHÁCH HÀNG RỜI BỎ (PERSONAS)

* **1. The Silent Defector (55% tổng Churn - Ngủ đông & Rút lui lặng lẽ):**
  * *Hành vi:* Dư nợ = $0, quẹt thẻ < 45 lần, chi tiêu giảm > 40%.
  * *Can thiệp:* Push notification tặng E-voucher 100K khi quẹt thẻ đầu tuần, hoàn tiền 5% ăn uống.
* **2. Frustrated Complainer (25% tổng Churn - Bức xúc Trải nghiệm Dịch vụ):**
  * *Hành vi:* Gọi CSKH $\ge 3-6$ lần/năm, bức xúc tra soát và biểu phí.
  * *Can thiệp:* Tổng đài viên cấp cao gọi xin lỗi, miễn phí thường niên 1 năm, xử lý khiếu nại trong 24h.
* **3. The VIP Switcher (20% tổng Churn - Khách hàng Cao cấp Chuyển dịch):**
  * *Hành vi:* Thu nhập $\ge \$120\text{K}$, thẻ Gold/Platinum, hạn mức $> \$20\text{K}$.
  * *Can thiệp:* Chuyên viên Priority RM chăm sóc riêng 1-1, nâng cấp quyền lợi Golf/Phòng chờ sân bay.

<!--
Speaker Notes:
Để chính sách can thiệp đi vào thực tế của ngân hàng, nghiên cứu đã xây dựng 3 chân dung khách hàng rời bỏ điển hình: Thứ nhất là 'The Silent Defector' chiếm 55% Churn: nhóm này lặng lẽ đưa dư nợ về 0 USD và giảm quẹt thẻ. Giải pháp là tặng voucher hoàn tiền kích hoạt lại chi tiêu. Thứ hai là 'Frustrated Complainer' chiếm 25% Churn: nhóm bức xúc gọi CSKH trên 3 lần. Giải pháp là cấp quản lý gọi điện xử lý dứt điểm trong 24h và miễn phí thường niên. Thứ ba là 'The VIP Switcher' chiếm 20% Churn: nhóm khách hàng giàu có thu nhập trên 120K USD. Giải pháp là chuyên viên Priority RM chăm sóc 1-1 và nâng cấp đặc quyền phòng chờ sân bay.
-->

---

## 🛡️ 17. KHUNG CHIẾN LƯỢC GIỮ CHÂN 4 TẦNG & HỆ THỐNG CẢNH BÁO SỚM

* **TẦNG 1: CẢNH BÁO SỚM THỜI GIAN THỰC (EWS):** Giám sát tự động Trigger Points (ngủ đông 2 tháng, giảm chi tiêu 30%) $\rightarrow$ *KPI: Phát hiện sớm > 90%*.
* **TẦNG 2: CSKH CHỦ ĐỘNG (PROACTIVE CARE):** Áp dụng chỉ tiêu First-Contact Resolution (FCR), khách gọi đến lần 3 tự động chuyển tiếp chuyên viên cấp cao $\rightarrow$ *KPI: FCR > 85%, Churn CSKH < 5%*.
* **TẦNG 3: GAMIFIED LOYALTY & TÍCH ĐIỂM:** Chiến dịch 'Quẹt Thẻ Mỗi Tuần' tích điểm theo tần suất quẹt thẻ thay vì chỉ tính theo doanh số $\rightarrow$ *KPI: Tần suất $\ge$ 5 lần/tháng*.
* **TẦNG 4: BÁN CHÉO HỆ SINH THÁI (CROSS-SELLING):** Combo liên kết thẻ tín dụng với tài khoản lương, miễn phí trọn đời và tích hợp ví điện tử $\rightarrow$ *KPI: Sở hữu $\ge$ 4 SP đạt > 65%*.

<!--
Speaker Notes:
Từ các phát hiện nghiên cứu, đề tài đề xuất Khung chiến lược giữ chân khách hàng 4 tầng toàn diện kèm KPI định lượng: Tầng 1 là Hệ thống Cảnh báo sớm EWS kích hoạt tự động theo thời gian thực. Tầng 2 là Quy trình CSKH chủ động nhằm nâng chỉ tiêu giải quyết lần đầu FCR lên trên 85%. Tầng 3 là Chương trình Gamified Loyalty kích thích tần suất quẹt thẻ định kỳ hàng tuần. Và Tầng 4 là Bán chéo hệ sinh thái nhằm tạo rào cản chuyển đổi tự nhiên bền vững. Bốn tầng này phối hợp đồng bộ tạo thành pháo đài vững chắc bảo vệ danh mục thẻ của ngân hàng.
-->

---

## 💵 18. MÔ PHỎNG TÀI CHÍNH: LỢI NHUẬN RÒNG +$400,000 USD (ROI = 500%)

* **Giả định quy mô 10,000 khách hàng:**
  * Lượng khách hàng rời bỏ tự nhiên: **1,607 khách** (16.07%).
  * Mô hình XGBoost nhận diện rủi ro ($t^*=0.42$): **1,468 khách**.
  * Tỷ lệ can thiệp thành công kỳ vọng (75%): **960 khách hàng được cứu vãn**.
* **Hiệu quả tài chính định lượng:**
  1. Tổng giá trị CLV bảo vệ thành công: $960 \times \$500 = \mathbf{\$480,000\text{ USD}}$.
  2. Tổng chi phí can thiệp ưu đãi: $1,600 \times \$50 = \mathbf{\$80,000\text{ USD}}$.
  3. **Lợi nhuận ròng tăng thêm:** $\$480,000 - \$80,000 = \mathbf{+\$400,000\text{ USD/năm}}$.
  4. **Tỷ suất sinh lời đầu tư (ROI):** $(\$400,000 / \$80,000) \times 100\% = \mathbf{500\%}$.

<!--
Speaker Notes:
Để chứng minh tính khả thi kinh tế của đề tài, nghiên cứu xây dựng mô phỏng tài chính trên quy mô danh mục 10,000 khách hàng: Với tỷ lệ rời bỏ tự nhiên 16.07%, mô hình XGBoost phát hiện được 1,468 khách hàng có nguy cơ. Khi triển khai gói can thiệp ưu đãi 50 USD/khách với tỷ lệ cứu vãn kỳ vọng 75%, ngân hàng giữ lại thành công 960 khách hàng, tương đương bảo tồn 480,000 USD giá trị CLV. Sau khi trừ đi toàn bộ 80,000 USD chi phí thực hiện, dự án đem lại +400,000 USD lợi nhuận ròng hàng năm, đạt tỷ suất sinh lời danh nghĩa ROI lên tới 500%.
-->

---

## 🎓 19. TỔNG KẾT HỌC THUẬT: ĐÓNG GÓP, HẠN CHẾ & HƯỚNG ĐI

* **🎯 Đóng góp then chốt:** Pipeline hoàn chỉnh từ tiền xử lý, kiểm soát rò rỉ dữ liệu đến mô hình XGBoost đạt ROC-AUC 0.9930 và tối ưu hóa kinh tế ROI 500%.
* **⚠️ Hạn chế nghiên cứu:** Dữ liệu dạng bảng cắt ngang (Cross-sectional), chưa ghi nhận chuỗi thời gian liên tục từng giao dịch POS và dữ liệu nhật ký ghi âm CSKH.
* **🚀 Định hướng phát triển:**
  1. Thử nghiệm kiến trúc Deep Learning cho dữ liệu bảng (**TabNet** / Tabular Transformers).
  2. Triển khai kiến trúc **MLOps Real-time** trên Kafka / Spark Streaming tại ngân hàng.
  3. Tích hợp XAI cá thể hóa bằng biểu đồ SHAP Waterfall cho từng Relationship Manager.

<!--
Speaker Notes:
Kính thưa Thầy/Cô và các bạn, bài báo cáo nghiên cứu của tôi đã tổng kết được 3 đóng góp lớn: từ kiểm soát chặt chẽ dữ liệu, huấn luyện mô hình XGBoost đạt ROC-AUC 0.9930 đến lượng hóa lợi nhuận ròng kinh tế. Về hạn chế, đề tài chỉ ra tính chất cắt ngang của dữ liệu và đề xuất 3 hướng đi tiếp theo: ứng dụng TabNet, triển khai MLOps trên Kafka và đưa XAI SHAP Waterfall đến từng cán bộ quản lý khách hàng.
-->

---

## 🏛️ 20. LỜI CẢM ƠN & PHIÊN HỎI ĐÁP (Q&A SESSION)

# XIN TRÂN TRỌNG CẢM ƠN QUÝ THẦY/CÔ VÀ CÁC BẠN HỌC VIÊN!
### HỌC VIỆN NGÂN HÀNG (BANKING ACADEMY OF VIETNAM) — KHOA HỆ THỐNG THÔNG TIN QUẢN LÝ
* **Học viên thực hiện:** Đỗ Văn Đạt  |  **Chuyên ngành:** Business Analytics
* **Email liên hệ:** `datdv@bav.edu.vn`
* **Rất mong nhận được các ý kiến nhận xét, góp ý và câu hỏi phản biện từ Hội đồng chấm bảo vệ!**

<!--
Speaker Notes:
Tôi xin trân trọng cảm ơn Quý Thầy/Cô và các bạn đã chú ý lắng nghe bài thuyết trình. Tôi rất mong nhận được những nhận xét, đóng góp quý báu và các câu hỏi phản biện từ Hội đồng chấm bảo vệ để hoàn thiện đề tài nghiên cứu hơn nữa. Xin trân trọng cảm ơn!
-->
