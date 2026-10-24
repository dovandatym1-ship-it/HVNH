# GIÁO TRÌNH VÀ TÀI LIỆU: XỬ LÝ VÀ KHÁM PHÁ DỮ LIỆU TRONG KINH DOANH
**Học phần:** Phân tích kinh doanh (Business Analytics)  
**Đơn vị:** Học viện Ngân hàng (Banking Academy of Vietnam)  

---

## 🎯 MỤC TIÊU HỌC TẬP
1. **Vai trò của phân tích kinh doanh:** Hiểu các khái niệm cơ bản về Business Analytics (BA), phân biệt với Business Intelligence (BI) và Data Science (DS), nắm vững vai trò ra quyết định dựa trên dữ liệu.
2. **Khám phá và tiền xử lý dữ liệu:** Nắm vững các bước làm sạch dữ liệu (data cleaning), xử lý giá trị thiếu (missing values), giá trị ngoại lai (outliers), tính toán thống kê mô tả và trực quan hóa dữ liệu (data visualization).
3. **Khai phá dữ liệu và Thống kê suy luận:** Áp dụng các phương pháp phân cụm (Clustering), ước lượng khoảng tin cậy (Confidence Interval) và kiểm định giả thuyết thống kê (Hypothesis Testing) trong bài toán thực tế.

---

# PHẦN 1: ĐỊNH VỊ VÀ BỐI CẢNH PHÂN TÍCH KINH DOANH

## 1. Phân tích kinh doanh là gì?
**Phân tích kinh doanh (Business Analytics - BA)** là quá trình sử dụng dữ liệu, các phương pháp định lượng (toán học, thống kê, học máy) và công nghệ nhằm chuyển đổi dữ liệu thô thành các **quyết định kinh doanh có căn cứ**.

### Phân biệt BI, BA và Data Science

```
        ┌─────────────────────────────────────────────────────────┐
        │                       DỮ LIỆU                           │
        └──────────────────────────┬──────────────────────────────┘
                                   │
         ┌─────────────────────────┼─────────────────────────┐
         ▼                         ▼                         ▼
┌──────────────────┐      ┌──────────────────┐      ┌──────────────────┐
│        BI        │      │        BA        │      │   Data Science   │
│  (Trí tuệ KD)    │      │  (Phân tích KD)  │      │  (Khoa học DL)   │
├──────────────────┤      ├──────────────────┤      ├──────────────────┤
│ Báo cáo,         │      │ Mô hình hoá, suy │      │ Phương pháp toán │
│ Dashboard, DL    │      │ diễn, dự báo,    │      │ và công nghệ xử  │
│ quá khứ          │      │ đề xuất giải pháp│      │ lý dữ liệu       │
│ "Chuyện gì đã    │      │ "Vì sao? Sẽ ra   │      │ "Khai thác DL    │
│ xảy ra?"         │      │ sao? Nên làm gì?"│      │ bằng cách nào?"  │
└──────────────────┘      └──────────────────┘      └──────────────────┘
```

> **Ba thành tố không thể tách rời:**  
> **Dữ liệu ➔ Mô hình ➔ Quyết định**  
> *(Nếu thiếu đi thành tố thứ ba - **Quyết định**, phân tích dữ liệu chỉ đơn thuần là một bài tập kỹ thuật).*

---

## 2. Bối cảnh: Vì sao BA trở thành năng lực cốt lõi?

### 2.1. Động lực thúc đẩy
* **Áp lực từ môi trường:** Biên lợi nhuận ngày càng mỏng, chu kỳ ra quyết định bị rút ngắn, khách hàng đòi hỏi trải nghiệm cá nhân hóa cao, và biến động kinh tế vĩ mô khó lường.
* **Điều kiện đủ đã hình thành:** Dữ liệu giao dịch và hành vi khách hàng bùng nổ ở quy mô lớn (Big Data); chi phí tính toán và lưu trữ đám mây giảm mạnh; các thư viện mã nguồn mở (`pandas`, `scikit-learn`, `xgboost`...) đã rất hoàn thiện.
* **Dữ liệu là tài sản chiến lược:** Chuyển dịch từ việc coi dữ liệu là *"sản phẩm phụ của vận hành"* sang *nguồn lực cốt lõi có thể định giá và tạo lợi thế cạnh tranh bền vững*.

### 2.2. Bằng chứng thực nghiệm (Empirical Evidence)
Nghiên cứu của **Brynjolfsson, Hitt, Kim** và **Brynjolfsson, McElheran** chứng minh:
> Doanh nghiệp áp dụng cơ chế **ra quyết định dựa trên dữ liệu (Data-driven Decision Making - DDD)** đạt **năng suất lao động và hiệu quả tài chính cao hơn 5% đến 6%** so với nhóm đối chứng sau khi kiểm soát các yếu tố ngoại cảnh.  
> ➔ **Chuyển dịch tất yếu:** Từ quyết định theo *kinh nghiệm hoặc trực giác* sang quyết định dựa trên *bằng chứng định lượng*.

---

## 3. Thang giá trị: 4 cấp độ phân tích dữ liệu

| Cấp độ | Tên bài toán | Câu hỏi cốt lõi | Công cụ và phương pháp | Vai trò và giá trị mang lại |
| :---: | :--- | :--- | :--- | :--- |
| **1** | **Mô tả** *(Descriptive)* | *Điều gì đã xảy ra?* | Thống kê mô tả, Dashboard, phân rã chỉ số, báo cáo trực quan | Tạo sự hiểu biết chung, theo dõi và đo lường hiệu quả vận hành |
| **2** | **Chẩn đoán** *(Diagnostic)* | *Vì sao điều đó lại xảy ra?* | Kiểm định giả thuyết, phân tích tương quan, suy luận nhân quả (DiD, PSM, IV) | Tìm nguyên nhân gốc rễ (root cause) của biến động |
| **3** | **Dự báo** *(Predictive)* | *Điều gì sẽ xảy ra trong tương lai?* | Hồi quy, Machine Learning, Chuỗi thời gian, Random Forest, XGBoost | Dự đoán xu hướng, dự báo nhu cầu, cảnh báo sớm rủi ro |
| **4** | **Đề xuất** *(Prescriptive)* | *Nên làm gì để tối ưu kết quả?* | Tối ưu hóa (Optimization), Mô phỏng (Simulation), Ma trận quyết định | Đưa ra hành động cụ thể để đạt mục tiêu kinh doanh tối đa |

---

## 4. Phạm vi ứng dụng theo chức năng doanh nghiệp

* **Marketing và Khách hàng:** Phân khúc khách hàng, dự báo khách hàng rời bỏ (churn prediction), ước lượng giá trị vòng đời khách hàng (CLV), mô hình hóa lực đẩy (uplift modeling), thử nghiệm A/B.
* **Vận hành và Chuỗi cung ứng:** Dự báo nhu cầu thị trường, tối ưu hóa mức tồn kho an toàn, lập lịch trình sản xuất, bảo trì dự đoán thiết bị.
* **Tài chính - Ngân hàng:** Chấm điểm tín dụng (Credit Scoring), ước lượng tham số tổn thất (PD, LGD, EAD theo chuẩn Basel), cảnh báo sớm nợ xấu, dự báo dòng tiền, kiểm định sức chịu đựng (stress testing).
* **Quản trị Rủi ro và Tuân thủ:** Phát hiện gian lận giao dịch (fraud detection), phòng chống rửa tiền (AML), định lượng rủi ro thị trường và rủi ro vận hành.
* **Định giá và Doanh thu:** Ước tính độ co giãn của cầu theo giá ($E_p$), định giá động (dynamic pricing theo thời gian thực), tối ưu hóa chương trình khuyến mãi.
* **Quản trị Nhân sự (HR Analytics):** Dự báo tỷ lệ nhân viên nghỉ việc (turnover rate), phân tích hiệu suất làm việc, hoạch định định biên nhân sự theo kịch bản kinh doanh.

> **Điểm hội tụ điển hình:** Bài toán **Chấm điểm tín dụng (Credit Scoring)** trong ngân hàng kết hợp toàn bộ 4 cấp độ phân tích, đồng thời thể hiện sự đánh đổi rõ ràng giữa *độ chính xác dự báo* và *khả năng giải thích mô hình* theo yêu cầu của cơ quan quản lý.

---

## 5. Phương pháp luận: Thống kê so với Học máy (Machine Learning)

| Tiêu chí | Tiếp cận Thống kê (Statistical Inference) | Tiếp cận Học máy (Machine Learning) |
| :--- | :--- | :--- |
| **Mục tiêu cốt lõi** | **SUY DIỄN (Inference)**: Hiểu cơ chế nguyên nhân - kết quả | **DỰ BÁO (Prediction)**: Dự báo ngoài mẫu chính xác nhất |
| **Giả định mô hình** | Rất chặt chẽ (phân phối chuẩn, phương sai đồng nhất, không đa cộng tuyến) | Linh hoạt, lỏng lẻo, để dữ liệu tự quyết định dạng hàm |
| **Đầu ra chính** | Hệ số hồi quy (Coefficients), p-value, khoảng tin cậy 95% | Điểm số dự báo, xác suất vỡ nợ, nhãn phân loại |
| **Thế mạnh** | Dễ giải thích bản chất kinh tế, kiểm soát sai lầm Loại I và Loại II | Xử lý tốt quan hệ phi tuyến, tương tác đa chiều, dữ liệu lớn |
| **Rủi ro chính** | Dễ bỏ sót dạng quan hệ phức tạp, chệch do xác định sai mô hình | Quá khớp (Overfitting), mô hình "hộp đen", khó bảo vệ trước cơ quan quản lý |

> **Nguyên tắc lựa chọn công cụ:** Luôn xuất phát từ **câu hỏi quản trị**, không chạy theo độ thời thượng của thuật toán:
> * *"Nếu giảm lãi suất cho vay 1%, tác động đến tỷ lệ nợ xấu thế nào?"* ➔ Dùng **Suy diễn nhân quả / Thống kê kinh tế lượng**.
> * *"Những khách hàng nào có xác suất vỡ nợ cao nhất trong 30 ngày tới?"* ➔ Dùng **Học máy / Dự báo**.

---

## 6. Vòng đời bài toán phân tích và Tạo lập giá trị

### 6.1. Quy trình chuẩn CRISP-DM
**Hiểu bài toán KD ➔ Hiểu dữ liệu ➔ Chuẩn bị dữ liệu ➔ Mô hình hóa ➔ Đánh giá ➔ Triển khai và Giám sát**

### 6.2. Ba điểm nghẽn làm thất thoát giá trị (Value Leakage)
1. **Đóng khung sai bài toán (Wrong Problem Framing):** Xây dựng mô hình kỹ thuật rất hoàn hảo nhưng lại giải quyết một câu hỏi kinh doanh không mang lại giá trị.
2. **Khoảng cách giữa mô hình và hành động:** Doanh nghiệp không thiết lập quy trình vận hành để đưa kết quả dự báo thành hành động cụ thể cho nhân viên kinh doanh.
3. **Không giám sát sau triển khai:** Bỏ qua hiện tượng **Trôi dạt dữ liệu (Data Drift / Concept Drift)** khiến hiệu quả mô hình suy giảm mạnh theo thời gian.

### 6.3. Cầu nối Kỹ thuật và Kinh doanh
* **Chỉ số kỹ thuật:** AUC, RMSE, Precision, Recall, F1-score.
* **Chỉ số kinh doanh:** Tỷ lệ nợ xấu thực tế giảm, chi phí tồn kho tiết kiệm được, doanh thu biên tăng thêm, chi phí thu hút khách hàng (CAC) tối ưu.
* *Lưu ý:* Một mô hình có AUC = 0.95 vẫn có thể làm doanh nghiệp thua lỗ nặng nếu ngưỡng cắt (cutoff threshold) không được tối ưu theo ma trận chi phí - lợi ích của việc chặn nhầm khách hàng tốt.

---

## 7. Các tình huống thực tế (Business Case Studies)

| Ngành / Lĩnh vực | Tình huống nghiệp vụ và Ứng dụng phân tích | Lợi ích kinh doanh mang lại |
| :--- | :--- | :--- |
| **1. Bán lẻ** *(BigC, WinMart)* | Dự đoán nhu cầu mua sắm theo mùa vụ tại chuỗi siêu thị bằng mô hình chuỗi thời gian và dự báo. | Giảm 20% đến 30% tồn kho thừa, tăng doanh thu và chọn đúng thời điểm khuyến mại. |
| **2. E-Commerce** *(Shopee, Lazada)* | Gợi ý sản phẩm cá nhân hóa (Recommender System) dựa trên lịch sử click và giỏ hàng. | Tăng trải nghiệm khách hàng, tăng tỷ lệ click (CTR), nâng cao giá trị đơn hàng bán chéo. |
| **3. Ngân hàng** *(Retail Banking)* | Chấm điểm tín dụng (Credit Scoring) đánh giá xác suất vỡ nợ của hồ sơ vay tiêu dùng. | Giảm nợ xấu, tự động phê duyệt hồ sơ nhanh chóng và chính xác. |
| **4. Sản xuất** *(Supply Chain)* | Dự báo nhu cầu tiêu thụ và lượng nguyên vật liệu cần nhập, tránh đứt gãy dây chuyền. | Tiết kiệm chi phí lưu kho, tối ưu chuỗi cung ứng, tránh gián đoạn sản xuất. |
| **5. Marketing** *(Digital Ads)* | Đo lường ROI chiến dịch qua phân tích chuyển đổi (Conversion Rate), chi phí CAC và LTV. | Phân bổ ngân sách quảng cáo vào kênh tối ưu, nâng cao hiệu quả truyền thông. |
| **6. Quản trị nhân sự** *(HR Analytics)* | Xây dựng Dashboard đánh giá KPI, năng suất và dự báo nhân sự có nguy cơ nghỉ việc cao. | Giữ chân nhân tài, quy hoạch đào tạo kịp thời, tối ưu cơ cấu nhân sự. |

---

# PHẦN 2: KHÁM PHÁ VÀ TIỀN XỬ LÝ DỮ LIỆU (DATA EXPLORATION AND PREPROCESSING)

## 1. Phân loại dữ liệu

### 1.1. Phân loại theo bản chất dữ liệu
* **Dữ liệu định tính (Qualitative / Categorical Data):**
  * **Định danh (Nominal):** Không có thứ bậc hay quan hệ so sánh hơn kém.  
    *Ví dụ:* Giới tính (*Nam, Nữ*), Tình trạng hôn nhân (*Độc thân, Kết hôn, Ly hôn*), Kênh liên hệ (*Email, Điện thoại*).
  * **Thứ bậc (Ordinal):** Có thứ tự, cấp bậc rõ ràng nhưng không đo chính xác được khoảng cách số học.  
    *Ví dụ:* Mức độ hài lòng (*Rất không hài lòng < Trung bình < Hài lòng < Rất hài lòng*), Học lực (*Yếu < Trung bình < Khá < Giỏi*).
* **Dữ liệu định lượng (Quantitative / Numerical Data):**
  * **Rời rạc (Discrete):** Nhận giá trị nguyên, đếm được.  
    *Ví dụ:* Số người phụ thuộc trong gia đình (0, 1, 2...), số giao dịch trong tháng, số sản phẩm mua.
  * **Liên tục (Continuous):** Nhận giá trị thực trong một khoảng liên tục, đo lường được.  
    *Ví dụ:* Thu nhập hàng tháng, số dư tài khoản, tuổi khách hàng, nhiệt độ, chiều cao.

> **Biến giả (Dummy Variable / Binary Indicator):**  
> Là biến nhị phân chỉ nhận giá trị 0 hoặc 1 dùng để mã hóa các biến định tính đưa vào các mô hình hồi quy và học máy định lượng.  
> *Ví dụ:* `Is_Married = 1` nếu đã kết hôn, `= 0` nếu độc thân.

### 1.2. Phân loại theo cấu trúc thời gian và đơn vị phân tích
* **Dữ liệu chéo (Cross-sectional Data):**
  * *Bản chất:* Thu thập tại **cùng một thời điểm** (hoặc trong khoảng thời gian ngắn) trên **nhiều đơn vị khác nhau** (cá nhân, hộ gia đình, doanh nghiệp, quốc gia...).
  * *Đặc điểm:* Dữ liệu **không có yếu tố thay đổi theo thời gian** trên từng đơn vị.
  * *Ví dụ:* Thu nhập của 100 hộ gia đình trong năm 2024; Doanh thu của 50 doanh nghiệp trong Quý 1/2025.
* **Dữ liệu chuỗi thời gian (Time Series Data):**
  * *Bản chất:* Thu thập theo **trình tự thời gian liên tiếp** trên **một đơn vị duy nhất**.
  * *Đặc điểm:* Thời gian là yếu tố cốt lõi, thường dùng để phân tích xu hướng (trend), tính mùa vụ (seasonality) và dự báo tương lai.
  * *Ví dụ:* GDP của Việt Nam từ năm 2000 đến 2025; Giá cổ phiếu Vinamilk (VNM) biến động theo từng ngày giao dịch.
* **Dữ liệu bảng (Panel / Longitudinal Data):**
  * *Bản chất:* Là **sự kết hợp giữa dữ liệu chéo và chuỗi thời gian** — thu thập dữ liệu trên **nhiều đơn vị qua nhiều mốc thời gian**.
  * *Đặc điểm:* Cho phép phân tích đồng thời sự thay đổi theo thời gian của từng đơn vị và sự khác biệt giữa các đơn vị với nhau.
  * *Ví dụ:* Thu nhập của 100 hộ gia đình được theo dõi liên tục trong 5 năm (2020–2024); Lợi nhuận và đòn bẩy nợ của 500 doanh nghiệp niêm yết trong 8 quý liên tiếp.

---

## 2. Các khái niệm thống kê nền tảng

```
       ┌──────────────────────────────────────────────────────────┐
       │                 TỔNG THỂ (POPULATION)                    │
       │    Toàn bộ tập hợp cá thể/đơn vị đang nghiên cứu         │
       │    (Ví dụ: Tất cả khách hàng của ngân hàng - N)          │
       │                                                          │
       │         ┌──────────────────────────────────────┐         │
       │         │           MẪU (SAMPLE)               │         │
       │         │   Tập hợp con đại diện được rút ra   │         │
       │         │   để khảo sát và tính toán (n)       │         │
       │         │                                      │         │
       │         └──────────────────────────────────────┘         │
       └──────────────────────────────────────────────────────────┘
```

* **Quan sát (Observation / Record):** Mỗi dòng dữ liệu tương ứng với một đối tượng cụ thể (ví dụ: hồ sơ của 1 khách hàng).
* **Biến số (Variable / Feature):** Mỗi cột dữ liệu thể hiện một thuộc tính của đối tượng (ví dụ: Tuổi, Thu nhập, Điểm tín dụng).

---

## 3. Tổng hợp 8 dạng bài toán phân tích trong thực tế

1. **Mô tả (Descriptive):** Tóm tắt hiện trạng kinh doanh (Doanh số trung bình theo tháng, tỷ lệ khách hàng theo độ tuổi).
2. **Chẩn đoán (Diagnostic):** Tìm nguyên nhân biến động (Vì sao khách hàng VIP huỷ thẻ? Phân tích hồi quy và ANOVA).
3. **Dự đoán (Predictive):** Dự báo tương lai (Dự báo doanh số quý tới bằng Machine Learning và Time Series).
4. **Phân loại (Classification):** Dự đoán nhãn rời rạc (Hồ sơ vay có rủi ro hay an toàn? Dùng Logistic, Random Forest, XGBoost).
5. **Hồi quy (Regression):** Dự đoán giá trị liên tục (Dự báo giá trị doanh nghiệp EV, giá bất động sản).
6. **Phân cụm (Clustering):** Gom nhóm tự động không cần nhãn (Phân khúc khách hàng mua sắm bằng K-Means, PCA).
7. **Định tính (Qualitative):** Khám phá cảm xúc, lý do sâu kín qua phỏng vấn sâu, phân tích chủ đề (Thematic Analysis).
8. **Định lượng (Quantitative):** Đo lường quy mô, kiểm định giả thuyết thống kê trên mẫu dữ liệu lớn bằng Python, R, Stata.

---

## 4. Thống kê mô tả (Descriptive Statistics)

### 4.1. Đo lường xu hướng trung tâm (Measures of Central Tendency)
* **Giá trị trung bình (Mean - ký hiệu là X̄):** Tổng tất cả các giá trị chia cho số quan sát:
  $$X̄ = \frac{1}{n} \sum_{i=1}^n X_i$$
  *Đặc điểm:* Rất nhạy cảm với các giá trị ngoại lai (outliers) quá lớn hoặc quá nhỏ.
* **Trung vị (Median):** Giá trị nằm chính giữa tập dữ liệu sau khi đã sắp xếp thứ tự tăng dần.  
  *Đặc điểm:* Không bị ảnh hưởng bởi outliers, rất hữu ích khi phân tích thu nhập, giá nhà đất.
* **Yếu vị (Mode):** Giá trị xuất hiện với tần suất nhiều nhất trong tập dữ liệu.  
  *Đặc điểm:* Là đại lượng duy nhất có thể sử dụng cho cả dữ liệu định tính và phân loại (Nominal data).

### 4.2. Đo lường độ phân tán (Measures of Dispersion)
* **Khoảng biến thiên (Range):** $\text{Range} = \text{Max} - \text{Min}$.
* **Phương sai (Variance - $s^2$) và Độ lệch chuẩn (Standard Deviation - $s$):**
  $$s = \sqrt{\frac{1}{n-1}\sum_{i=1}^n (X_i - X̄)^2}$$
  *Ý nghĩa:* Thể hiện mức độ biến động hoặc rủi ro của dữ liệu quanh giá trị trung bình. Độ lệch chuẩn càng lớn thì độ phân tán càng cao.

### 4.3. Đo lường tương quan tuyến tính (Correlation Analysis)
Hệ số tương quan Pearson ($r$) nhận giá trị từ $[-1, +1]$:
$$r_{xy} = \frac{\sum (X_i - X̄)(Y_i - \bar{Y})}{\sqrt{\sum (X_i - X̄)^2 \sum (Y_i - \bar{Y})^2}}$$

```
-1.0 ──────────── -0.7 ──────────── -0.4 ──────────── -0.1 ──── 0 ──── 0.1 ──────────── 0.4 ──────────── 0.7 ──────────── 1.0
│ Tương quan âm mạnh │ Tương quan âm vừa │ Tương quan yếu │ Không tương quan │ Tương quan yếu │ Tương quan vừa │ Tương quan dương mạnh │
```

* **Quy ước mức độ tương quan:**
  * $|r|$ từ $0.0$ đến $0.1$: Không có mối quan hệ tuyến tính.
  * $|r|$ từ $0.1$ đến $0.4$: Tương quan yếu.
  * $|r|$ từ $0.4$ đến $0.7$: Tương quan mức độ vừa phải.
  * $|r| \ge 0.7$: Tương quan mạnh (cần lưu ý hiện tượng **Đa cộng tuyến - Multicollinearity** khi đưa vào mô hình hồi quy).

---

## 5. Các biểu đồ thống kê chuyên sâu

### 5.1. Biểu đồ hộp (Box Plot / Box-and-Whisker Plot)
```
          Outlier           Min            Q1          Median (Q2)       Q3            Max          Outlier
             *          ├───[───────────────┬───────────────]───┤             *
                                            │<───── IQR ───>│
```
* **Các thành phần:**
  * **$Q_1$ (25th percentile):** $25\%$ giá trị nhỏ hơn điểm này.
  * **$Q_2$ (Median / 50th percentile):** Điểm trung vị của dữ liệu.
  * **$Q_3$ (75th percentile):** $75\%$ giá trị nhỏ hơn điểm này.
  * **Khoảng liên tứ phân vị (Interquartile Range - IQR):** $\text{IQR} = Q_3 - Q_1$.
  * **Ngưỡng xác định Outliers:** Nằm ngoài khoảng $[Q_1 - 1.5 \times \text{IQR}, \; Q_3 + 1.5 \times \text{IQR}]$.

### 5.2. Biểu đồ tần số (Histogram)
* Trực quan hóa hình dạng phân phối của dữ liệu định lượng liên tục qua các khoảng giá trị (**bins** liền kề).
* Giúp phát hiện: Dữ liệu phân phối chuẩn (hình chuông cân đối), lệch trái (Left-skewed), lệch phải (Right-skewed), hay phân phối đa đỉnh.

### 5.3. Biểu đồ phân tán (Scatter Plot)
* Mỗi điểm $(X_i, Y_i)$ biểu thị một quan sát trên hệ trục tọa độ 2 chiều.
* Giúp nhận diện:
  1. *Tuyến tính đồng biến (Positive Linear):* Mây điểm dốc lên từ trái qua phải.
  2. *Tuyến tính nghịch biến (Negative Linear):* Mây điểm dốc xuống từ trái qua phải.
  3. *Mối quan hệ phi tuyến (Nonlinear):* Dạng parabol, chữ U, chữ S.
  4. *Không tương quan:* Phân tán ngẫu nhiên, không theo quy luật.
  5. *Điểm ngoại lai (Outliers):* Nằm tách biệt xa cụm điểm chung.

---

## 6. Cẩm nang trực quan hóa dữ liệu (Data Visualization Guide)

### 6.1. Quy trình 6 bước thiết kế Dashboard và Visual Storytelling
1. **Hiểu bối cảnh và đối tượng tiếp nhận:**
   * *Lãnh đạo cấp cao (C-level):* Cần thông tin tổng quan, xu hướng vĩ mô, KPI chiến lược dài hạn.
   * *Quản lý cấp trung (Middle Manager):* Cần dữ liệu hiệu quả chiến dịch, doanh số theo ngành hàng, khách hàng.
   * *Chuyên viên vận hành:* Cần dữ liệu chi tiết từng giao dịch để xử lý nghiệp vụ hàng ngày.
2. **Lựa chọn loại biểu đồ phù hợp** với bản chất thông tin cần truyền đạt.
3. **Loại bỏ yếu tố gây nhiễu:** Xóa bỏ các đường lưới thừa, hiệu ứng 3D lòe loẹt, màu sắc gây rối mắt.
4. **Tập trung sự chú ý:** Sử dụng màu sắc tương phản để làm nổi bật thông điệp quan trọng nhất.
5. **Hoàn thiện thiết kế và chú thích:** Ghi rõ đơn vị đo, nguồn dữ liệu, tiêu đề súc tích.
6. **Kể câu chuyện dữ liệu (Data Storytelling):** Dẫn dắt người xem từ số liệu hiện tại đến nguyên nhân và giải pháp hành động.

### 6.2. Ma trận lựa chọn biểu đồ theo mục đích phân tích

| Mục đích biểu đồ | Dạng biểu đồ khuyến nghị | Lưu ý khi sử dụng |
| :--- | :--- | :--- |
| **Xu hướng theo thời gian** *(Trend over time)* | • **Line Chart:** Chuỗi thời gian liên tục.; • **Column Chart:** So sánh các mốc thời gian rời rạc.; • **Area Chart:** Biến động tổng thể tích lũy theo thời gian.; • **Slope Chart:** So sánh sự thay đổi thứ hạng giữa 2 thời điểm. | Trục thời gian luôn đặt ở trục hoành (X-axis). Tránh dùng quá 4 đường trên 1 Line Chart. |
| **Cơ cấu và Thành phần** *(Composition / Part-to-whole)* | • **Stacked Bar / Column:** So sánh cơ cấu giữa nhiều nhóm.; • **Donut / Pie Chart:** Cơ cấu đơn giản (dưới hoặc bằng 4 phần).; • **Treemap:** Cơ cấu dữ liệu phân cấp nhiều nhóm nhỏ.; • **Waterfall Chart:** Thể hiện các yếu tố cộng và trừ vào tổng. | Hạn chế dùng Pie chart nếu có quá nhiều lát cắt nhỏ. |
| **Phân phối dữ liệu** *(Distribution)* | • **Histogram:** Phân phối tần suất dữ liệu số liên tục.; • **Box Plot:** So sánh phân phối và tìm outliers đa nhóm.; • **Violin Plot:** Phân phối dữ liệu đa đỉnh phức tạp.; • **Population Pyramid:** Tháp dân số theo độ tuổi và giới tính. | Chọn số lượng bin (khoảng chia) hợp lý trên Histogram. |
| **Mối quan hệ và Tương quan** *(Relationship / Correlation)* | • **Scatter Plot:** Quan hệ giữa 2 biến liên tục.; • **Bubble Chart:** Bổ sung biến thứ 3 qua kích thước điểm.; • **Heatmap:** Ma trận tương quan đa biến số. | Dùng màu sắc phân kỳ rõ ràng cho Heatmap. |
| **Xếp hạng và So sánh** *(Ranking and Comparison)* | • **Ordered Bar Chart:** Xếp hạng danh mục có nhãn dài.; • **Lollipop Chart:** Thay thế Bar chart để giao diện thanh thoát.; • **Diverging Bar Chart:** Trình bày khảo sát ý kiến (Đồng ý / Không đồng ý). | Luôn sắp xếp thứ tự tăng dần hoặc giảm dần để người đọc nắm bắt nhanh. |

---

# PHẦN 3: KHAI PHÁ DỮ LIỆU VÀ THỐNG KÊ SUY LUẬN (DATA MINING AND INFERENTIAL STATISTICS)

## 1. Khai phá dữ liệu mô tả (Descriptive Data Mining)
* **Bản chất:** Là phương pháp **Học không giám sát (Unsupervised Learning)** nhằm khám phá cấu trúc, quy luật và phân nhóm tự nhiên trong tập dữ liệu lớn mà **không có biến mục tiêu (nhãn) định sẵn**.
* **Mục tiêu:**
  1. Tóm tắt thông tin đa chiều quan trọng.
  2. Phát hiện hành vi tiêu dùng tiềm ẩn.
  3. Hỗ trợ ra quyết định phân khúc thị trường.

---

## 2. Phân tích phân cụm (Clustering Analysis)

```
        Cụm 1 (Chi tiêu cao)                      Cụm 2 (Khách hàng trẻ)
              ●  ●                                      ▲  ▲
            ●  ★1  ●                                  ▲  ★2  ▲
              ●  ●                                      ▲  ▲
                             [Khoảng cách Euclid]
                                      ⟷
                                              ■  ■
                                            ■  ★3  ■
                                              ■  ■
                                      Cụm 3 (Khách hàng tiết kiệm)
```

### 2.1. Mục tiêu phân cụm
Gom nhóm các đối tượng quan sát sao cho:
* **Độ tương đồng nội cụm cao nhất (High Intra-cluster Similarity):** Các khách hàng trong cùng 1 cụm có đặc điểm rất giống nhau.
* **Độ khác biệt giữa các cụm lớn nhất (High Inter-cluster Dissimilarity):** Các cụm tách biệt rõ rệt nhau.

### 2.2. Đo lường khoảng cách (Distance Metric)
Khoảng cách Euclid giữa 2 điểm dữ liệu $A(x_1, x_2, \dots, x_p)$ và $B(y_1, y_2, \dots, y_p)$:
$$d(A, B) = \sqrt{\sum_{j=1}^p (x_j - y_j)^2}$$

### 2.3. Hai phương pháp phân cụm chính
1. **Phân cụm phân cấp (Hierarchical Clustering):**
   * **Agglomerative (Gom cụm / Bottom-up):** Ban đầu mỗi đối tượng là 1 cụm riêng lẻ, ở mỗi bước sẽ hợp nhất 2 cụm gần nhau nhất lại cho đến khi toàn bộ dữ liệu tạo thành 1 cây phân cấp (**Dendrogram**).
   * **Divisive (Tách cụm / Top-down):** Bắt đầu từ 1 cụm chứa toàn bộ dữ liệu, sau đó tách nhỏ dần.
2. **Phân cụm K-Means (K-Means Clustering):**
   * Chia tập dữ liệu thành $k$ cụm định trước.
   * Thuật toán tự động cập nhật vị trí tâm cụm (**centroid**) qua các vòng lặp cho đến khi hội tụ.

---

## 3. Thống kê suy luận (Inferential Statistics)

### 3.1. Lý do chọn mẫu (Sampling)
* **Tiết kiệm chi phí và thời gian:** Khảo sát toàn bộ tổng thể (ví dụ hàng triệu công dân) cực kỳ tốn kém; việc lấy mẫu ngẫu nhiên khoa học cho kết quả nhanh và chính xác.
* **Tính khả thi và Thử nghiệm phá hủy:** Trong kiểm tra chất lượng (ví dụ độ bền bóng đèn, thử nghiệm va chạm ô tô), việc kiểm tra toàn bộ sẽ phá hủy hết sản phẩm.
* **Quy trình mẫu quần thể vô hạn (Infinite Population):** Áp dụng khi dữ liệu sinh ra liên tục theo thời gian (dòng giao dịch thẻ ngân hàng, khách hàng ghé thăm chuỗi cửa hàng McDonald's).

### 3.2. Ước lượng khoảng (Interval Estimation)
Thay vì chỉ đưa ra một giá trị duy nhất (**Ước lượng điểm - Point Estimate**), ước lượng khoảng cung cấp một phạm vi tin cậy chứa tham số thực của tổng thể:

$$\text{Ước lượng khoảng} = \text{Ước lượng điểm} \pm \text{Biên sai số (Margin of Error)}$$

$$\text{Khoảng tin cậy: } X̄ \pm Z_{\alpha/2} \times \frac{\sigma}{\sqrt{n}}$$

### 3.3. Kiểm định giả thuyết (Hypothesis Testing)
* **Giả thuyết thống kê:** Phát biểu hoặc khẳng định về một tham số tổng thể (Trung bình $\mu$, Tỷ lệ $p$, Phương sai $\sigma^2$).
* **Cặp giả thuyết:**
  * Giả thuyết Không ($H_0$): Khẳng định không có sự khác biệt hoặc không có tác động.
  * Giả thuyết Đối ($H_1$): Khẳng định có sự khác biệt có ý nghĩa thống kê.
* **Quy tắc ra quyết định qua p-value:**
  * Nếu $p\text{-value} < \alpha$ (thường chọn $\alpha = 0.05$): Bác bỏ $H_0$ (kết quả có ý nghĩa thống kê ở mức tin cậy 95%).
  * Nếu $p\text{-value} \ge \alpha$: Chưa đủ bằng chứng để bác bỏ $H_0$.

---

## 📌 BẢNG TỔNG KẾT CÂU HỎI THỰC HÀNH PHÂN TÍCH KHÁCH HÀNG

| Nhóm phân tích | Câu hỏi kinh doanh cần trả lời | Công cụ và Biểu đồ sử dụng |
| :--- | :--- | :--- |
| **1. Nhân khẩu học** | • Cơ cấu giới tính và tình trạng hôn nhân?; • Phân bố độ tuổi khách hàng thế nào? | Pie Chart / Bar Chart; Histogram / Box Plot |
| **2. Học vấn và Thu nhập** | • Số lượng khách hàng theo nghề nghiệp?; • Học vấn có ảnh hưởng đến thu nhập? | Ordered Bar Chart; Boxplot Thu nhập theo Học vấn |
| **3. Hành vi giao dịch** | • Phân phối tổng số giao dịch (`Total_Trans_Ct`)?; • Khách hàng chi tiêu nhiều nhất gồm những ai? | Histogram và Thống kê độ lệch; Top N Ranking Bar Chart |
| **4. Tương quan đa biến** | • Tuổi và Thu nhập có tương quan với nhau không?; • Mối quan hệ giữa Điểm hài lòng và Tỷ lệ rời bỏ? | Scatter Plot / Hệ số Pearson; Correlation Heatmap |
| **5. Phân khúc và Nhóm** | • Các cụm khách hàng theo thói quen mua sắm?; • Tỷ lệ sở hữu nhà/xe theo từng nhóm nghề nghiệp? | K-Means và PCA 2D/3D Plot; Stacked Column Chart |

---
*Tài liệu học tập nội bộ - Học viện Ngân hàng (Banking Academy of Vietnam)*  
*Địa chỉ: 12 Chùa Bộc, Quang Trung, Đống Đa, Hà Nội*
