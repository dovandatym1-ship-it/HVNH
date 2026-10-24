---
marp: true
theme: gaia
_class: lead
paginate: true
backgroundColor: #f8fafc
color: #0f172a
---

# 📊 BÀI TẬP GIỮA KỲ: XỬ LÝ & KHAI PHÁ DỮ LIỆU
## PHÂN TÍCH HÀNH VI, PHÂN CỤM & DỰ BÁO NGUY CƠ RỜI BỎ CỦA KHÁCH HÀNG THẺ TÍN DỤNG

**Học phần:** Phân tích Dữ liệu trong Kinh doanh (Business Analytics)  
**Đơn vị:** Học viện Ngân hàng (Banking Academy)  
**Sinh viên thực hiện:** Đỗ Văn Đạt  
**Tập dữ liệu:** `BankChurners.csv` (10,127 quan sát, 23 thuộc tính)  

---

## 🎯 1. BỐI CẢNH & BÀI TOÁN KINH TẾ

### Bối cảnh Ngân hàng Bán lẻ:
* **Thẻ tín dụng (Credit Card)** là nguồn thu lợi nhuận hàng đầu: Phí quẹt thẻ (Interchange), Lãi suất tín dụng quay vòng, Phí dịch vụ thường niên.
* **Quy tắc 5:1:** Chi phí tìm khách hàng mới (CAC) gấp **5-7 lần** chi phí giữ chân khách hàng cũ (CRC).
* **Tỷ lệ rời bỏ (Churn Rate)** trong dữ liệu là **16.07%** (Cứ 6 khách hàng mở thẻ thì có 1 khách hàng hủy thẻ).

---

## 🏗️ 2. KIẾN TRÚC PIPELINE XỬ LÝ & KHAI PHÁ DỮ LIỆU

1. **Giai đoạn 1 - Tiền xử lý dữ liệu:** Loại 2 cột Naive Bayes thừa, xử lý missing bằng median, bảo toàn nhóm Unknown, feature engineering 5 biến mới.
2. **Giai đoạn 2 - Khám phá dữ liệu (EDA):** Phân tích nhân khẩu học, nhận diện vùng rủi ro giao dịch (<55 lần, <$3000), hiện tượng dư nợ về 0, ngưỡng gọi CSKH 3 lần.
3. **Giai đoạn 3 - Khai phá dữ liệu (ML):** Phân cụm 4 nhóm K-Means & PCA, huấn luyện 4 mô hình ML (LR, DT, RF, XGBoost đạt ROC-AUC 0.9930), tối ưu ngưỡng kinh tế t = 0.42.
4. **Giai đoạn 4 - Ứng dụng quản trị:** 3 Chân dung rủi ro, Khung giữ chân 4 tầng (4-Tier), Hệ thống cảnh báo sớm EWS, ROI tài chính 500%.

---

## 🧹 3. TIỀN XỬ LÝ DỮ LIỆU & FEATURE ENGINEERING

* **Làm sạch dữ liệu:**
  - Xóa 2 cột Naive Bayes để loại bỏ rò rỉ dữ liệu (*Data Leakage*).
  - Điền Median cho các thuộc tính số bị khuyết lẻ tẻ.
  - Giữ nguyên nhóm 'Unknown' như một phân lớp thông tin độc lập.
* **Kỹ thuật tạo biến mới (Feature Engineering):**
  - `Avg_Trans_Value`: Giá trị chi tiêu trung bình / lần quẹt thẻ ($Total\_Trans\_Amt / Total\_Trans\_Ct$).
  - `Revolving_Ratio`: Tỷ lệ dư nợ quay vòng trên hạn mức cấp.
  - `Contact_Intensity`: Cường độ bức xúc ($Contacts / (Inactive\_Months + 1)$).
  - `Age_Group`: Phân khúc lứa tuổi (<35, 35-44, 45-54, 55-64, 65+).

---

## 📊 4. PHÂN BỐ BIẾN MỤC TIÊU (ATTRITION FLAG)

* **Ở lại (Existing Customer):** $8,500$ khách hàng ($83.93\%$).
* **Rời bỏ (Attrited Customer):** $1,627$ khách hàng ($16.07\%$).
* **Mất cân bằng lớp:** Xấp xỉ $1 : 5.22$.

> 🚨 **Chiến lược Đánh giá ML:** Không dùng Accuracy đơn thuần mà bắt buộc phải tối ưu hóa **Recall (Độ nhạy)**, **F1-Score** và **ROC-AUC** để không bỏ sót khách hàng rời bỏ.

---

## 👥 5. PHÂN TÍCH NHÂN KHẨU HỌC & RỦI RO RỜI BỎ

* **Giới tính (Gender):** Nữ có tỷ lệ rời bỏ cao hơn Nam đáng kể (**$17.36\%$** vs **$14.62\%$**, $p = 0.0002$).
* **Phân hóa Thu nhập 2 đầu (Bimodal Risk):**
  - Thu nhập thấp ($<\$40K$): Rời bỏ **$17.19\%$** (áp lực phí).
  - Thu nhập cao ($\ge \$120K$): Rời bỏ **$17.33\%$** (đối thủ lôi kéo).
  - Thu nhập trung bình ($\$60K-\$80K$): Trung thành nhất (**$13.48\%$**).
* **Học vấn:** Trình độ Tiến sĩ (Doctorate) có tỷ lệ rời bỏ cao nhất (**$21.06\%$**).

---

## 💳 6. HÀNH VI GIAO DỊCH: "VÙNG NGUY CƠ CAO"

* **Tổng số lần giao dịch (`Total_Trans_Ct`):** Khách ở lại $68.7$ lần vs Khách churn $44.9$ lần ($-34.6\%$, $p < 0.0001$).
* **Tổng giá trị giao dịch (`Total_Trans_Amt`):** Khách ở lại $\$4,655$ vs Khách churn $\$3,095$ ($-33.5\%$, $p < 0.0001$).

> 🚨 **VÙNG NGUY CƠ CAO (RED CLUSTER):** Khách hàng có **$< 55$ lần quẹt thẻ/năm** và **tổng chi tiêu $< \$3,000$** tập trung dày đặc các điểm rời bỏ. Tần suất quẹt thẻ là nhịp tim của lòng trung thành.

---

## 📉 7. CHỈ SỐ TÀI CHÍNH: HIỆN TƯỢNG "DƯ NỢ VỀ 0"

* **Dư nợ quay vòng (`Total_Revolving_Bal`):**
  - Khách ở lại: Mean $\$1,257$ (Median $\$1,364$).
  - Khách rời bỏ: Mean $\$673$ (**MEDIAN = $\$0.00$!**).
* **Tỷ lệ sử dụng hạn mức (`Avg_Utilization_Ratio`):**
  - Khách ở lại: $29.64\%$ (Median $21.1\%$).
  - Khách rời bỏ: $16.25\%$ (**MEDIAN = $0.00\%$!**).

> 📌 **Quy luật:** Trước khi đóng thẻ, khách hàng tất toán toàn bộ dư nợ về 0 để tránh phát sinh lãi phạt và hoàn toàn ngừng quẹt thẻ.

---

## 📞 8. TƯƠNG TÁC CSKH & RÀO CẢN ĐA SẢN PHẨM

* **Ngưỡng Báo Động 3 Lần Liên Hệ CSKH:**
  - Gọi $0-1$ lần: Churn $< 8\%$.
  - Gọi $3$ lần: Churn vọt lên **$20.21\%$**.
  - Gọi $4$ lần: Churn đạt **$34.11\%$**.
  - Gọi $5-6$ lần: Churn lên tới **$55\% - 100\%$**.
* **Số lượng sản phẩm sở hữu (`Relationship_Count`):**
  - Khách dùng $1-2$ sản phẩm: Churn **$26\% - 28\%$**.
  - Khách dùng $\ge 4$ sản phẩm: Churn giảm chỉ còn **$10\% - 11\%$** (giảm gần 3 lần).

---

## 🔍 9. KHAI PHÁ DỮ LIỆU: PHÂN CỤM K-MEANS & PCA

* **Cụm 0 (37.6%): Tiêu dùng phổ thông ổn định** (Chi tiêu $\$4.1K$, Dư nợ $\$1.4K$, Churn = $9.2\%$).
* **Cụm 1 (24.0%): Ngủ đông & Nguy cơ cao** (Chi tiêu $\$1.8K$, Dư nợ $\$210$, Churn = **$41.8\%$**).
* **Cụm 2 (18.7%): VIP Chi tiêu lớn** (Chi tiêu $\$9.5K$, Hạn mức cao, Churn = $14.5\%$).
* **Cụm 3 (19.7%): Vay tín dụng quay vòng** (Dư nợ $\$2.2K$ sinh lãi, Churn = $7.6\%$).

---

## 🤖 10. MÔ HÌNH HÓA MÁY HỌC (SUPERVISED ML)

| Thuật Toán | Accuracy | Precision | Recall (Độ Nhạy) | F1-Score | ROC-AUC |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Logistic Regression** | $86.97\%$ | $56.34\%$ | $83.38\%$ | $67.25\%$ | $0.9348$ |
| **Decision Tree** | $91.07\%$ | $66.59\%$ | $88.92\%$ | $76.15\%$ | $0.9458$ |
| **Random Forest** | $94.77\%$ | $81.56\%$ | $87.08\%$ | $84.23\%$ | $0.9838$ |
| **XGBoost (TOP 1)** | **$96.54\%$** | **$87.61\%$** | **$91.38\%$** | **$89.46\%$** | **$0.9930$** |

---

## 🔑 11. TOP ĐẶC TRƯNG QUYẾT ĐỊNH RỜI BỎ

1. `Total_Trans_Ct` (Số lần giao dịch): Đóng góp quan trọng nhất.
2. `Total_Ct_Chng_Q4_Q1` (Mức độ suy giảm giao dịch quý cuối).
3. `Total_Revolving_Bal` (Dư nợ tín dụng quay vòng về 0).
4. `Total_Trans_Amt` (Tổng giá trị chi tiêu).
5. `Total_Relationship_Count` & `Contacts_Count` (Ràng buộc sản phẩm & Bức xúc CSKH).

---

## 💰 12. TỐI ƯU HÓA NGƯỠNG KINH TẾ (COST-BENEFIT)

* **Giả định:** CLV giữ chân $=\$500$, Chi phí can thiệp $=\$50$, Mất khách $=-\$500$.
* **Ngưỡng cắt xác suất tối ưu:** **$t = 0.42$** (thay vì $0.50$ mặc định).
* **Kết quả:** Recall đạt $94\%$, Precision đạt $86\%$, Lợi nhuận ròng tối đa trên tập Test đạt **$> \$112,000$ USD**.

---

## 👥 13. BA CHÂN DUNG KHÁCH HÀNG RỜI BỎ (PERSONAS)

1. **The Silent Defector (55%):** Dư nợ $= \$0$, giao dịch $< 45$ lần, ngủ đông $\ge 3$ tháng $ightarrow$ Gửi Voucher kích hoạt cuối tuần, hoàn tiền $5\%$.
2. **Frustrated Complainer (25%):** Gọi CSKH $\ge 3-6$ lần, dùng $1-2$ sản phẩm $ightarrow$ VIP Taskforce hỗ trợ trong 24h, miễn giảm phí linh hoạt.
3. **The VIP Switcher (20%):** Thu nhập $\ge \$120K$, thẻ Gold/Plat $ightarrow$ Cán bộ RM tặng phòng chờ sân bay, x2 điểm dặm bay.

---

## 🏛️ 14. KHUNG CHIẾN LƯỢC GIỮ CHÂN 4 TẦNG (4-TIER)

* **Tầng 1: Cảnh Báo Sớm (EWS):** Giám sát thời gian thực các Trigger Point (Ngủ đông 2 tháng, gọi CSKH lần 3).
* **Tầng 2: CSKH Chủ Động (Proactive):** Áp dụng KPI First-Contact Resolution (FCR) xử lý dứt điểm khiếu nại trong 24h.
* **Tầng 3: Gamified Loyalty:** Tích điểm theo tần suất quẹt thẻ thay vì chỉ tính theo số tiền chi tiêu.
* **Tầng 4: Bán Chéo (Cross-selling):** Combo Tài chính Toàn diện ($\ge 4$ sản phẩm) nâng cao rào cản chuyển đổi.

---

## 💵 15. BÀI TOÁN KINH TẾ & ROI 500%

* **Quy mô:** $10,000$ khách hàng (16% Churn = $1,600$ khách).
* **Cứu vãn 60% với XGBoost:** Giữ lại thành công **$960$ khách hàng**.
* **Giá trị CLV cứu được:** $960 	imes \$500 = \$480,000$ USD.
* **Chi phí can thiệp:** $1,600 	imes \$50 = \$80,000$ USD.
* **LỢI NHUẬN RÒNG GIA TĂNG:** **$+\$400,000$ USD / NĂM!**
* **TỶ SUẤT HOÀN VỐN:** **$	ext{ROI} = 500\%$**.

---

## 🎯 16. KẾT LUẬN & HƯỚNG PHÁT TRIỂN

* **Đóng góp chính:** Làm sạch 10,127 bản ghi, phát hiện 4 quy luật hành vi then chốt, phân cụm 4 nhóm K-Means, XGBoost ROC-AUC 0.9930, chiến lược 4 tầng ROI 500%.
* **Hướng mở rộng cuối kỳ:** Ứng dụng Explainable AI (SHAP), Mô hình CLV Động (Dynamic CLV) và Tích hợp API Real-time Scoring trên CRM ngân hàng.

---

# XIN TRÂN TRỌNG CẢM ƠN!
### HỎI & ĐÁP (Q&A)
