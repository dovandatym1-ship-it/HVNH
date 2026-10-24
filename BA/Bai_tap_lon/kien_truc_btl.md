## KHUNG KIẾN TRÚC VÀ HƯỚNG DẪN TRIỂN KHAI BÀI TẬP LỚN (BTL)

**Học phần:** Phân tích kinh doanh (Business Analytics - BA)  
**Đơn vị đào tạo:** Học viện Ngân hàng (Banking Academy of Vietnam)

## 📌 TỔNG QUAN CẤU TRÚC ĐỀ TÀI

```plaintext
MỤC LỤC &amp; DANH MỤC HÌNH ẢNH / BẢNG BIỂU
PHẦN MỞ ĐẦU (Viết sau cùng khi đã hoàn thành các chương)
│  1. Lý do chọn đề tài (Tính cấp thiết)
│  2. Mục tiêu nghiên cứu (Mục tiêu chung và mục tiêu cụ thể)
│  3. Đối tượng và Phạm vi nghiên cứu (Không gian, thời gian, nguồn dữ liệu)
│  4. Phương pháp nghiên cứu
│
CHƯƠNG 1: TỔNG QUAN VÀ BỐI CẢNH ĐỀ TÀI
│  1.1. Giới thiệu bối cảnh ngành và bài toán kinh doanh
│  1.2. Thực trạng và sự cần thiết ứng dụng phân tích dữ liệu
│
CHƯƠNG 2: CƠ SỞ LÝ THUYẾT VÀ PHƯƠNG PHÁP NGHIÊN CỨU
│  2.1. Tổng quan lý thuyết nền tảng và các nghiên cứu liên quan
│  2.2. Khung quy trình phân tích dữ liệu (CRISP-DM)
│  2.3. Các mô hình và thuật toán áp dụng (Hồi quy / Phân loại / Phân cụm)
│  2.4. Tiêu chí và thước đo đánh giá mô hình (RMSE, AUC-ROC, Accuracy, F1, Silhouette)
│
CHƯƠNG 3: KẾT QUẢ THỰC HIỆN VÀ PHÂN TÍCH THỰC NGHIỆM
│  3.1. Thu thập và tiền xử lý dữ liệu (Làm sạch, Missing values, Outliers, Mã hóa)
│  3.2. Khám phá và trực quan hóa dữ liệu (EDA, Thống kê mô tả, Tương quan)
│  3.3. Xây dựng, huấn luyện và tinh chỉnh mô hình (Training và Hyperparameter Tuning)
│  3.4. So sánh hiệu năng mô hình và phân tích tầm quan trọng của biến (Feature Importance)
│
CHƯƠNG 4: KẾT LUẬN VÀ HÀM Ý QUẢN TRỊ / ĐỀ XUẤT CHÍNH SÁCH
│  4.1. Tóm tắt các phát hiện chính từ mô hình
│  4.2. Đề xuất chính sách và giải pháp kinh doanh cụ thể
│  4.3. Hạn chế của đề tài và định hướng phát triển
TÀI LIỆU THAM KHẢO VÀ PHỤ LỤC (Source code Python, từ điển biến dữ liệu)
```

## CHI TIẾT CÁCH VIẾT TỪNG PHẦcòn bài táonN

## PHẦN MỞ ĐẦU

\> **Lưu ý chiến lược:** Nên viết phần này sau cùng, sau khi đã chạy xong kết quả thực nghiệm ở Chương 3 và đưa ra đề xuất ở Chương 4 để đảm bảo tính nhất quán tuyệt đối.

**Lý do chọn đề tài (Tính cấp thiết):**

*   Nêu bối cảnh thị trường thực tế (ví dụ: áp lực gia tăng rủi ro nợ xấu trong ngân hàng bán lẻ, sự cạnh tranh gay gắt trong việc giữ chân khách hàng dùng thẻ).
*   Sự bùng nổ của dữ liệu lớn nhưng doanh nghiệp còn thiếu công cụ ra quyết định định lượng.
*   Khẳng định việc nghiên cứu đề tài này sẽ mang lại giá trị thiết thực gì cho doanh nghiệp.

**Mục tiêu nghiên cứu:**

*   _Mục tiêu chung:_ Ứng dụng các kỹ thuật phân tích dữ liệu và học máy để giải quyết bài toán kinh doanh cụ thể.
*   _Mục tiêu cụ thể:_
    *   Khám phá đặc trưng hành vi và các yếu tố ảnh hưởng chính từ tập dữ liệu.
    *   Xây dựng, đánh giá và lựa chọn mô hình dự báo / phân loại tối ưu nhất.
    *   Đề xuất các giải pháp quản trị, chính sách nghiệp vụ dựa trên bằng chứng định lượng từ mô hình.

**Đối tượng và Phạm vi nghiên cứu:**

*   _Đối tượng nghiên cứu:_ Tập trung vào hành vi tài chính, lịch sử giao dịch thẻ, sức khỏe tài chính doanh nghiệp hoặc phản hồi chiến dịch marketing.
*   _Phạm vi không gian:_ Bộ dữ liệu của tổ chức / ngân hàng / ngành hàng nào.
*   _Phạm vi thời gian:_ Giai đoạn thu thập dữ liệu (ví dụ: giai đoạn 2020–2024).

**Phương pháp nghiên cứu:**

*   Phương pháp định lượng kết hợp quy trình khoa học dữ liệu chuẩn CRISP-DM.
*   Sử dụng ngôn ngữ lập trình Python và các thư viện chuyên dụng (`pandas`, `numpy`, `scikit-learn`, `xgboost`, `matplotlib`, `seaborn`).

## CHƯƠNG 1: TỔNG QUAN VÀ BỐI CẢNH ĐỀ TÀI

\> **Lưu ý chiến lược:** Giới thiệu ngắn gọn, súc tích (khoảng 2 đến 3 trang), tập trung đúng vào bài toán nghiệp vụ, không viết lan man lý thuyết chung chung.

*   **1.1. Giới thiệu bối cảnh ngành và bài toán kinh doanh:**
    *   Giới thiệu ngắn gọn về lĩnh vực nghiên cứu (Ngân hàng bán lẻ, E-commerce, Chuỗi cung ứng, Tài chính doanh nghiệp).
    *   Mô tả bài toán kinh doanh thực tế cần giải quyết (ví dụ: Nhận diện sớm khách hàng rời bỏ - Churn Prediction, hoặc Chấm điểm tín dụng - Credit Scoring).
*   **1.2. Thực trạng và sự cần thiết ứng dụng phân tích dữ liệu:**
    *   Doanh nghiệp đang gặp khó khăn gì nếu chỉ dựa vào cảm tính hoặc quy tắc truyền thống?
    *   Việc áp dụng mô hình phân tích dữ liệu giúp chuyển đổi từ quyết định bị động sang chủ động dự báo như thế nào.

## CHƯƠNG 2: CƠ SỞ LÝ THUYẾT VÀ PHƯƠNG PHÁP NGHIÊN CỨU

\> **Lưu ý chiến lược:** Thể hiện rõ tính chuẩn mực học thuật, trích dẫn các nghiên cứu nền tảng và giải thích rõ bản chất toán học / thống kê của các thuật toán.

*   **2.1. Tổng quan nghiên cứu (Literature Review):**
    *   Tóm tắt ngắn gọn các công trình nghiên cứu trong và ngoài nước đã từng tiếp cận bài toán này.
    *   Các mô hình thường được sử dụng và kết quả đạt được trong thực tế.
*   **2.2. Khung quy trình phân tích dữ liệu (CRISP-DM):**
    *   Sơ đồ và diễn giải 6 bước: Hiểu bài toán kinh doanh ➔ Hiểu dữ liệu ➔ Chuẩn bị dữ liệu ➔ Mô hình hóa ➔ Đánh giá ➔ Đề xuất triển khai.
*   **2.3. Chi tiết các mô hình và thuật toán áp dụng:**
    *   Giải thích nguyên lý, cơ chế hoạt động, ưu điểm và nhược điểm của từng thuật toán bạn chọn (ví dụ: Logistic Regression, Decision Tree, Random Forest, XGBoost, K-Means Clustering).
    *   Trình bày công thức toán học cốt lõi (ví dụ: hàm Sigmoid, hàm mất mát Log-loss, khoảng cách Euclid).
*   **2.4. Tiêu chí và thước đo đánh giá mô hình:**
    *   Định nghĩa và ý nghĩa thực tế của các chỉ số:
        *   _Bài toán Phân loại:_ Confusion Matrix, Accuracy, Precision, Recall, F1-Score, ROC-AUC.
        *   _Bài toán Hồi quy:_ R-squared, MAE, MSE, RMSE.
        *   _Bài toán Phân cụm:_ Silhouette Score, Elbow Method (Inertia).

## CHƯƠNG 3: KẾT QUẢ THỰC HIỆN VÀ PHÂN TÍCH THỰC NGHIỆM

\> **Lưu ý chiến lược:** Đây là phần trọng tâm quyết định điểm số của bài báo cáo. Mọi bảng biểu và đồ thị đều phải có phân tích ý nghĩa kinh doanh đi kèm.

*   **3.1. Thu thập và tiền xử lý dữ liệu:**
    *   Mô tả tập dữ liệu (số lượng quan sát, số lượng biến số, biến mục tiêu $Y$ và các biến độc lập $X$).
    *   Quy trình xử lý giá trị khuyết thiếu (Missing values): Điền trung vị (Median) cho biến định lượng, điền Yếu vị (Mode) cho biến định tính.
    *   Nhận diện và xử lý giá trị ngoại lai (Outliers) bằng phương pháp Boxplot và IQR.
    *   Chuẩn hóa thang đo (StandardScaler / MinMaxScaler) và mã hóa biến phân loại (One-Hot Encoding / Dummy Variables).
*   **3.2. Khám phá và trực quan hóa dữ liệu (EDA):**
    *   Bảng thống kê mô tả: Trung bình, Trung vị, Độ lệch chuẩn, Giá trị nhỏ nhất, Giá trị lớn nhất.
    *   Trực quan hóa phân phối biến số (Histogram, Box Plot) và cơ cấu danh mục (Bar Chart, Pie Chart).
    *   Phân tích tương quan đa biến: Ma trận tương quan (Correlation Heatmap) và biểu đồ phân tán (Scatter Plot) để phát hiện đa cộng tuyến.
*   **3.3. Xây dựng, huấn luyện và tinh chỉnh mô hình:**
    *   Phân chia tập dữ liệu Train / Test (tỷ lệ 80/20 hoặc 70/30).
    *   Huấn luyện mô hình cơ sở (Baseline Model) và các mô hình nâng cao (Advanced Models).
    *   Áp dụng kỹ thuật kiểm chuẩn chéo (K-Fold Cross Validation) và tinh chỉnh siêu tham số (GridSearchCV) để tránh quá khớp (Overfitting).
*   **3.4. So sánh hiệu năng mô hình và phân tích tầm quan trọng của biến:**
    *   Bảng tổng hợp so sánh chỉ số đánh giá giữa các mô hình trên tập kiểm thử (Test set).
    *   Lựa chọn mô hình tốt nhất (Best Model) dựa trên sự cân bằng giữa độ chính xác và tính ứng dụng nghiệp vụ.
    *   Phân tích đồ thị tầm quan trọng của biến (Feature Importance / SHAP values) để chỉ ra các nhân tố then chốt quyết định đến kết quả đầu ra.

## CHƯƠNG 4: KẾT LUẬN VÀ HÀM Ý QUẢN TRỊ / ĐỀ XUẤT CHÍNH SÁCH

\> **Lưu ý chiến lược:** Không đề xuất giải pháp chung chung theo lý thuyết sách vở; tất cả chính sách phải xuất phát trực tiếp từ các biến quan trọng tìm thấy ở Chương 3.

*   **4.1. Tóm tắt các phát hiện chính:**
    *   Tóm lược ngắn gọn mô hình nào cho kết quả tốt nhất và mức độ tin cậy đạt bao nhiêu.
    *   Điểm danh 3 đến 5 yếu tố có tác động mạnh mẽ nhất đến bài toán (ví dụ: Số lượng giao dịch thẻ, Hạn mức tín dụng, Thời gian gắn kết).
*   **4.2. Đề xuất chính sách và giải pháp kinh doanh cụ thể:**
    *   _Chính sách phòng ngừa / Giữ chân khách hàng:_ Ví dụ thiết lập hệ thống cảnh báo sớm tự động khi khách hàng giảm số lần giao dịch dưới ngưỡng $k$.
    *   _Chính sách phân khúc và cá nhân hóa:_ Đưa ra gói sản phẩm / ưu đãi riêng cho từng cụm khách hàng đã phân tích.
    *   _Ma trận chi phí - lợi ích:_ Ước tính mức độ tiết kiệm chi phí hoặc mức giảm tỷ lệ nợ xấu khi doanh nghiệp áp dụng mô hình vào thực tế vận hành.
*   **4.3. Hạn chế của đề tài và định hướng phát triển:**
    *   Các hạn chế khách quan (ví dụ: dữ liệu chưa bao quát được toàn bộ chu kỳ kinh tế, còn thiếu dữ liệu phi cấu trúc như phản hồi văn bản).
    *   Hướng mở rộng cho các nghiên cứu tiếp theo (thử nghiệm mô hình Deep Learning, thu thập thêm dữ liệu thời gian thực).

## TÀI LIỆU THAM KHẢO VÀ PHỤ LỤC

*   **Tài liệu tham khảo:** Trình bày theo chuẩn trích dẫn học thuật (APA hoặc IEEE), liệt kê đầy đủ sách, giáo trình, bài báo khoa học và nguồn dữ liệu.
*   **Phụ lục:**
    *   Phụ lục 1: Bảng giải thích chi tiết ý nghĩa toàn bộ các biến số (Data Dictionary).
    *   Phụ lục 2: Toàn bộ mã nguồn thực thi bằng Python (Jupyter Notebook code).

## 💡 CHECKLIST VÀ NGUYÊN TẮC ĐẠT ĐIỂM TỐI ĐA (A+)

| Hạng mục | Tiêu chí kiểm tra | Đạt chuẩn |
| --- | --- | --- |
| **1\. Trình bày biểu đồ** | Mọi hình ảnh/đồ thị đều có: Số thứ tự hình, Tên biểu đồ, Đơn vị tính, Nguồn dữ liệu và tối thiểu 2-3 câu phân tích kết quả bên dưới. | \[ \] |
| **2\. Bảng biểu so sánh** | Có bảng tổng hợp so sánh định lượng giữa các mô hình (không chỉ nhận xét bằng chữ). | \[ \] |
| **3\. Cầu nối kinh doanh** | Kết quả kỹ thuật (Accuracy, AUC) được diễn giải thành giá trị tài chính/nghiệp vụ (giảm nợ xấu, tăng doanh số, tiết kiệm thời gian). | \[ \] |
| **4\. Tính nhất quán** | Số liệu từ phần Mở đầu, Thống kê mô tả ở Chương 3, đến phần Đề xuất ở Chương 4 khớp nhau 100%. | \[ \] |
| **5\. Tránh lỗi font & rác** | Không còn các ký tự rác từ OCR slide (`&amp;`, `\x0c`, lỗi mã hóa tiếng Việt). | \[ \] |

_Tài liệu hướng dẫn thực hiện Bài tập lớn môn Business Analytics - Học viện Ngân hàng_