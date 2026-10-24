# Slide thuyết trình — Tác động của AI đến Việc làm năm 2030
### (Bản Markdown mirror của `Slide_Thuyet_Trinh_TacDongAI_ViecLam2030.pptx` — 18 slide)

---

## Slide 1 — Cover
# Tác động của Trí tuệ nhân tạo (AI) đến Việc làm năm 2030
Bài tập cuối kỳ — Học phần Phân tích Kinh doanh — Học viện Ngân hàng
Sinh viên thực hiện: Đỗ Văn Đạt — Năm học 2025–2026

---

## Slide 2 — [TÓM TẮT ĐIỀU HÀNH]
### Nghề nghiệp Quyết định 85,7% Rủi ro Tự động hoá — Đặc điểm Cá nhân Gần như Vô nghĩa

| 85,7% | 0,9947 | 0,9979 | 0,862 |
|---|---|---|---|
| Phương sai giải thích bởi Job_Title (eta²) | F1-macro tốt nhất (phân loại) | ROC-AUC (OvR) tốt nhất | R² hồi quy tốt nhất |

---

## Slide 3 — [BỐI CẢNH NGHIÊN CỨU]
### Rủi ro Tự động hoá Phân bố Không Đồng đều — Yếu tố Nào Thực sự Quyết định?
- **Bối cảnh:** AI mở rộng tự động hoá từ tác vụ thủ tục sang tác vụ nhận thức phức tạp.
- **Vấn đề:** Frey & Osborne, McKinsey, WEF đồng thuận rủi ro không đồng đều giữa các nhóm nghề.
- **Câu hỏi nghiên cứu:** Yếu tố nào giải thích rủi ro tốt hơn — đặc điểm CÁ NHÂN hay NGHỀ NGHIỆP?
- **Cách tiếp cận:** Tiền xử lý → EDA → phân cụm → phân loại → hồi quy trên 3.000 quan sát, 20 nghề.

---

## Slide 4 — [CƠ SỞ LÝ THUYẾT]
### Task-Based Approach: Rủi ro Gắn với Bản chất Công việc, Không phải Người Lao động
- Autor, Levy & Murnane (2003): rủi ro quyết định ở cấp NGHỀ, không phải NGƯỜI.
- Frey & Osborne (2017): ~47% việc làm Hoa Kỳ có nguy cơ tự động hoá cao.
- Acemoglu & Restrepo (2019): displacement vs. reinstatement effect.
- McKinsey (2017) & WEF (2023): hàng trăm triệu lao động toàn cầu cần chuyển đổi nghề.
- **Giả thuyết kiểm định:** Job_Title giải thích rủi ro tốt hơn đặc trưng cá nhân.

---

## Slide 5 — [DỮ LIỆU NGHIÊN CỨU]
### 3.000 Hồ sơ x 20 Nghề nghiệp — Đầy đủ Chỉ số Kỹ năng, Lương, Học vấn và Công nghệ

| 3.000 | 20 | 10 | 3 |
|---|---|---|---|
| Quan sát (18 biến gốc) | Nghề nghiệp khảo sát | Nhóm điểm kỹ năng | Nhóm rủi ro (Low 24,6% · Medium 50,7% · High 24,7%) |

---

## Slide 6 — [TIỀN XỬ LÝ DỮ LIỆU]
### Tiền xử lý Phát hiện Rủi ro Rò rỉ Dữ liệu giữa Risk_Category và Automation_Probability
1. **Kiểm tra chất lượng:** 0 thiếu, 0 trùng, 0 vi phạm miền, 0 ngoại lai.
2. **Phát hiện rò rỉ:** Risk_Category = f(ngưỡng cố định của Automation_Probability_2030) → loại khỏi đặc trưng.
3. **Feature engineering:** +7 biến mới, one-hot Job_Title (+19 biến giả).
4. **Dữ liệu sẵn sàng:** 3.000 dòng x 25 cột, train/test 75/25 stratify.

---

## Slide 7 — [EDA 1/3]
### Nhóm Medium Chiếm 50,7% — Phân bố Xác suất Ẩn chứa Ba Cụm Mật độ Tách biệt
![](figures/02_automation_probability_distribution.png)
- Hình dạng KHÔNG phải đường cong chuẩn — có 3 vùng mật độ tách biệt.
- Cơ cấu 3 nhóm: Low 24,6% · Medium 50,7% · High 24,7%.
- Gợi ý một biến phân loại tiềm ẩn — xác định ở Slide 9.

---

## Slide 8 — [EDA 2/3]
### Lương, Học vấn, Kinh nghiệm, AI Exposure: Tương quan Xấp xỉ Bằng 0 với Rủi ro
![](figures/06_correlation_heatmap.png)
- Mọi |r| < 0,05 với Automation_Probability_2030.
- Nhất quán qua boxplot lương/học vấn/kinh nghiệm.
- Hệ quả: mô hình chỉ dùng đặc điểm cá nhân sẽ không tốt hơn ngẫu nhiên.

---

## Slide 9 — [EDA 3/3 — BẰNG CHỨNG THEN CHỐT]
### 20 Nghề Tách 3 Tầng Rõ rệt — Job_Title Giải thích 85,7% Phương sai (Eta²)
![](figures/08_jobtitle_automation_ranked.png)
- **Tầng thấp (~0,18):** AI Engineer, Research Scientist, Nurse, Teacher, Doctor.
- **Tầng trung bình (~0,50):** 10 nghề chuyên môn/văn phòng còn lại.
- **Tầng cao (~0,83):** Retail Worker, Security Guard, Construction Worker, Customer Support, Truck Driver.
- Kiểm định eta²: SSB/SST = 0,857.

---

## Slide 10 — [PHÂN CỤM KHÔNG GIÁM SÁT]
### Phân cụm Hồ sơ Kỹ năng Thất bại (Silhouette ≈ 0,06) — Xác nhận Kỹ năng Không Quyết định
![](figures/13_kmeans_clusters_pca.png)
- K-Means trên 12 biến kỹ năng/công nghệ, k=4 (chọn vì diễn giải nghiệp vụ).
- Silhouette Score chỉ 0,055–0,063 ở mọi k — gần 0.
- 4 cụm có xác suất tự động hoá TB gần như bằng nhau (0,49–0,52).

---

## Slide 11 — [MÔ HÌNH PHÂN LOẠI]
### Logistic Regression & XGBoost Đồng hạng Nhất: F1-macro 0,9947 · AUC ≈ 0,998

| Mô hình | F1-macro | ROC-AUC | Accuracy |
|---|---|---|---|
| **Logistic Regression ★ WINNER** | 0,9947 | 0,9979 | 0,9947 |
| Random Forest | 0,9345 | 0,9959 | 0,9387 |
| XGBoost Classifier | 0,9947 | 0,9964 | 0,9947 |

---

## Slide 12 — [MỨC ĐỘ QUAN TRỌNG CỦA BIẾN]
### 98,5% Tầm quan trọng Mô hình Thuộc về Nhóm biến Job_Title
![](figures/16_feature_importance.png)
- Feature importance XGBoost, gộp 19 biến giả Job_Title thành 1 mục.
- Job_Title (gộp) chiếm 98,5% tổng importance; phần còn lại ~1,5%.

---

## Slide 13 — [MÔ HÌNH HỒI QUY]
### Hồi quy Độc lập Xác nhận: R² = 0,862 khi Đưa Nghề nghiệp vào Mô hình
![](figures/17_regression_pred_vs_actual.png)
- Linear Regression: R²=0,862, MAE=0,078 (~8 điểm % xác suất).
- Kênh đánh giá ĐỘC LẬP — cùng kết luận với bài toán phân loại.

---

## Slide 14 — [CHÂN DUNG BA TẦNG NGHỀ NGHIỆP]
### Từ Rủi ro Thấp (Bác sĩ, Giáo viên) đến Rủi ro Cao (Bán lẻ, Bảo vệ)

| Tầng Rủi ro THẤP | Tầng Rủi ro TRUNG BÌNH | Tầng Rủi ro CAO |
|---|---|---|
| ~24,6% mẫu · XS TB ≈ 0,18 | ~50,7% mẫu · XS TB ≈ 0,50 | ~24,7% mẫu · XS TB ≈ 0,83 |
| AI Engineer, Research Scientist, Nurse, Teacher, Doctor | 10 nghề chuyên môn/văn phòng | Retail Worker, Security Guard, Construction Worker, Customer Support, Truck Driver |
| Đầu tư phát triển chuyên sâu | Bổ sung kỹ năng số định kỳ | Ưu tiên đào tạo lại (reskilling) |

---

## Slide 15 — [HÀM Ý QUẢN TRỊ NHÂN SỰ]
### Khung Hành động 3 Tầng: Ưu tiên Đào tạo lại Theo Nhóm nghề, Không Theo Cá nhân
- **Tầng Thấp:** đầu tư chuyên môn sâu/kỹ năng chăm sóc con người.
- **Tầng Trung bình:** theo dõi định kỳ, chủ động bổ sung kỹ năng số.
- **Tầng Cao:** ưu tiên reskilling THEO NHÓM NGHỀ, lộ trình chuyển đổi sớm.

---

## Slide 16 — [HẠN CHẾ NGHIÊN CỨU]
### Giới hạn: Dữ liệu Mô phỏng — Kết luận Có giá trị Nội tại, Cần Đối chiếu Thực tế
- Dữ liệu mô phỏng (synthetic) — không suy rộng trực tiếp cho thực tế.
- Thiếu chiều thời gian, biến ngành/vùng địa lý.
- Hiệu suất mô hình gần tuyệt đối phản ánh cơ chế sinh dữ liệu, không nên overclaim.

---

## Slide 17 — [KẾT LUẬN]
### Nghề nghiệp — Không phải Kỹ năng Cá nhân — Là Biến số Quyết định Rủi ro
- Job_Title giải thích 85,7% phương sai; F1-macro 0,9947; R² hồi quy 0,862.
- Nhất quán với task-based approach (Autor et al., 2003) và Frey & Osborne (2017).
- Đào tạo lại nên thiết kế theo nhóm nghề, không chỉ theo cá nhân.
- Kết luận từ dữ liệu mô phỏng — minh hoạ phương pháp luận.
- Hướng phát triển: dữ liệu thời gian/ngành/vùng thực tế; đối chiếu O*NET, WEF Future of Jobs Survey.

---

## Slide 18 — Q&A
# CẢM ƠN HỘI ĐỒNG — HỎI & ĐÁP
Đỗ Văn Đạt · Phân tích Kinh doanh · Học viện Ngân hàng

> Xem đầy đủ Speaker Notes (lời thoại 80-150 từ/slide) và 3 câu hỏi phản biện dự kiến tại
> [`Kich_Ban_Thuyet_Trinh_va_Cau_Hoi_Phan_Bien.md`](Kich_Ban_Thuyet_Trinh_va_Cau_Hoi_Phan_Bien.md).
