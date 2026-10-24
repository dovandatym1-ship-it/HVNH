# 🎙️ KỊCH BẢN THUYẾT TRÌNH CHI TIẾT (SPEAKER NOTES)
## VÀ BỘ 10 CÂU HỎI PHẢN BIỆN KINH ĐIỂN CỦA GIẢNG VIÊN (Q&A DEFENSE GUIDE)

* **Học phần:** Phân tích Dữ liệu trong Kinh doanh (Business Analytics) — Học viện Ngân hàng
* **Đề tài:** Xử lý dữ liệu và Khai phá dữ liệu với bộ dữ liệu BankChurners
* **Sinh viên thực hiện:** Đỗ Văn Đạt
* **Thời lượng thuyết trình đề xuất:** 12 - 15 phút

---

## ⏱️ PHẦN I: KỊCH BẢN THUYẾT TRÌNH TỪNG SLIDE (SPEAKER SCRIPT)

### Slide 1: Bìa Thuyết trình (Thời lượng: 1 phút)
> *"Kính chào Thầy/Cô và các bạn sinh viên. Em tên là Đỗ Văn Đạt, sinh viên chuyên ngành Phân tích Dữ liệu Kinh doanh - Học viện Ngân hàng. Hôm nay, em xin phép được đại diện nhóm nghiên cứu trình bày Báo cáo bài tập giữa kỳ với đề tài: **Xử lý dữ liệu và Khai phá dữ liệu trên bộ dữ liệu khách hàng thẻ tín dụng rời bỏ (Bank Customer Churn Analysis & Data Mining)**. Báo cáo sẽ đưa Thầy/Cô đi từ những góc nhìn thực tiễn về bài toán kinh tế mảng thẻ, qua quy trình tiền xử lý, khám phá dữ liệu chuyên sâu và ứng dụng các thuật toán máy học tân tiến để kiến tạo giải pháp giữ chân khách hàng hiệu quả nhất."*

---

### Slide 2: Bối cảnh Kinh doanh & Bài toán Kinh tế (Thời lượng: 1.5 phút)
> *"Kính thưa Thầy/Cô, thẻ tín dụng luôn được xem là 'con gà đẻ trứng vàng' của các ngân hàng thương mại bán lẻ nhờ 3 trụ cột thu nhập: phí quẹt thẻ POS/E-commerce, lãi suất tín dụng quay vòng và các loại phí thường niên. Tuy nhiên, thị trường đang chứng kiến sự cạnh tranh gay gắt từ các tổ chức tín dụng và Fintech.*  
> *Theo nghiên cứu của Bain & Company và Harvard Business Review, chi phí thu hút một khách hàng mới (CAC) đắt gấp 5 đến 7 lần chi phí giữ chân một khách hàng hiện hữu (CRC), trong khi chỉ cần tăng 5% tỷ lệ giữ chân có thể thúc đẩy lợi nhuận tăng từ 25% đến 95%. Trong bộ dữ liệu của chúng ta, tỷ lệ rời bỏ lên tới 16.07% — tức cứ 6 khách hàng mở thẻ thì có 1 khách hàng rời bỏ. Đây là tổn thất vô cùng lớn nếu ngân hàng không có biện pháp ngăn chặn kịp thời."*

---

### Slide 3: Kiến trúc Pipeline Toàn diện (Thời lượng: 1 phút)
> *"Để giải quyết triệt để bài toán, đề tài được cấu trúc theo 4 giai đoạn chuẩn mực:*  
> *1. Tiền xử lý dữ liệu và làm sạch: Loại trừ rò rỉ dữ liệu, xử lý missing và tạo đặc trưng mới.*  
> *2. Phân tích khám phá dữ liệu (EDA): Bóc tách các yếu tố nhân khẩu học, hành vi quẹt thẻ và tương tác CSKH.*  
> *3. Khai phá dữ liệu nâng cao (Data Mining): Phân cụm khách hàng qua K-Means/PCA và huấn luyện 4 mô hình máy học dự báo rời bỏ.*  
> *4. Ứng dụng quản trị: Xây dựng 3 chân dung khách hàng, Khung chiến lược giữ chân 4 tầng và mô phỏng hiệu quả tài chính ROI 500%."*

---

### Slide 4: Tiền xử lý & Kỹ thuật Tạo biến (Thời lượng: 1.5 phút)
> *"Ở khâu tiền xử lý, nhóm đã đưa ra 3 quyết định kỹ thuật quan trọng:*  
> *Thứ nhất, loại bỏ hoàn toàn 2 cột Naive Bayes ở cuối bảng gốc để ngăn ngừa triệt để hiện tượng rò rỉ dữ liệu (Data Leakage).*  
> *Thứ hai, xử lý các ô trống bằng giá trị Trung vị (Median Imputation) để đảm bảo tính vững chắc trước các giá trị ngoại lai.*  
> *Thứ ba, bảo toàn danh mục 'Unknown' trong học vấn và thu nhập như một phân lớp hành vi độc lập thay vì xóa bỏ.*  
> *Đặc biệt, nhóm đã kiến tạo 5 biến phái sinh có giá trị kinh tế cao như: `Avg_Trans_Value` (giá trị chi tiêu bình quân/giao dịch), `Revolving_Ratio` (tỷ lệ nợ quay vòng trên hạn mức) và `Contact_Intensity` (chỉ số cường độ bất mãn)."*

---

### Slide 5: Biến mục tiêu & Mất cân bằng lớp (Thời lượng: 1 phút)
> *"Quan sát phân phối biến mục tiêu, chúng ta có 8,500 khách hàng ở lại (83.9%) và 1,627 khách hàng rời bỏ (16.1%), tương ứng tỷ lệ mất cân bằng xấp xỉ 1:5.22.*  
> *Điểm mấu chốt ở đây là chúng ta không thể sử dụng độ chính xác thuần túy (Accuracy) làm thước đo chính. Nhóm bắt buộc phải tập trung tối ưu hóa chỉ số **Recall (Độ nhạy)**, **F1-Score** và **ROC-AUC** để đảm bảo mô hình không bỏ sót bất kỳ khách hàng nào đang có ý định rời bỏ."*

---

### Slide 6: Phân tích Nhân khẩu học (Thời lượng: 1 phút)
> *"Phân tích nhân khẩu học mang lại 3 phát hiện bất ngờ:*  
> *1. Khách hàng Nữ có tỷ lệ rời bỏ cao hơn Nam (17.36% vs 14.62%, kiểm định Chi-square p = 0.0002).*  
> *2. Hiện tượng rủi ro phân hóa hai đầu thu nhập (Bimodal Risk): Nhóm thu nhập thấp dưới $40K và nhóm thu nhập cao trên $120K có tỷ lệ rời bỏ cao nhất (~17.2% - 17.3%), trong khi nhóm thu nhập trung bình $60K-$80K lại là nhóm trung thành nhất.*  
> *3. Khách hàng có học vị Tiến sĩ có tỷ lệ rời bỏ cao nhất (21.06%)."*

---

### Slide 7: Hành vi Giao dịch - Vùng Nguy cơ Cao (Thời lượng: 1.5 phút)
> *"Khi phân tích biểu đồ phân tán giữa số lần giao dịch và tổng tiền chi tiêu, chúng ta phát hiện một 'Vùng nguy cơ cao' cực kỳ rõ ràng.*  
> *Khách hàng rời bỏ có số lần quẹt thẻ bình quân chỉ 44.9 lần/năm (giảm 34.6% so với nhóm ở lại là 68.7 lần). Toàn bộ các khách hàng có **dưới 55 lần giao dịch** và **chi tiêu dưới $3,000 USD** tập trung dày đặc các điểm màu đỏ rời bỏ. Tần suất quẹt thẻ chính là 'nhịp tim' phản ánh mức độ trung thành của khách hàng."*

---

### Slide 8: Chỉ số Tài chính - Dư nợ Quay vòng về 0 (Thời lượng: 1 phút)
> *"Một quy luật tài chính vô cùng đặc sắc được phát hiện: Khách hàng ở lại duy trì dư nợ quay vòng bình quân $1,257 USD (trung vị $1,364 USD). Nhưng ở nhóm khách hàng rời bỏ, **giá trị trung vị dư nợ quay vòng chính xác bằng $0.00 USD** và tỷ lệ sử dụng hạn mức trung vị bằng 0%.*  
> *Điều này phản ánh hành vi tâm lý thực tế: Trước khi chính thức yêu cầu đóng thẻ, khách hàng luôn chủ động tất toán sạch sẽ dư nợ để tránh phát sinh lãi phạt và hoàn toàn dừng quẹt thẻ."*

---

### Slide 9: Tương tác CSKH & Rào cản Hệ sinh thái (Thời lượng: 1 phút)
> *"Tại slide này, chúng ta nhìn thấy 'Ngưỡng bức xúc 3 lần liên hệ': Khách hàng gọi tổng đài 0-1 lần có tỷ lệ rời bỏ dưới 8%. Nhưng khi số lần gọi tăng lên 3 lần, tỷ lệ rời bỏ vọt lên 20.2%, lên 34.1% ở 4 lần và đạt tới 100% khi gọi 6 lần.*  
> *Đồng thời, đồ thị bên phải chứng minh: Khách hàng chỉ dùng 1-2 sản phẩm có tỷ lệ rời bỏ 26-28%, nhưng khi sở hữu từ 4 sản phẩm trở lên, tỷ lệ rời bỏ giảm xuống chỉ còn xấp xỉ 10%. Bán chéo đa sản phẩm chính là rào cản chuyển đổi vững chắc nhất."*

---

### Slide 10: Khai phá Phân cụm K-Means & PCA (Thời lượng: 1.5 phút)
> *"Bước sang phần Khai phá Dữ liệu, thuật toán K-Means kết hợp phương pháp Elbow và Silhouette Score đã xác định số cụm tối ưu là k = 4:*  
> *• Cụm 0 (37.6%): Khách hàng tiêu dùng phổ thông ổn định (Churn = 9.2%).*  
> *• Cụm 1 (24.0%): Khách hàng Ngủ đông & Nguy cơ cực cao (Dư nợ chỉ $210, Churn lên tới 41.8%!).*  
> *• Cụm 2 (18.7%): Khách hàng VIP chi tiêu lớn (Chi tiêu $9.5K, Churn = 14.5%).*  
> *• Cụm 3 (19.7%): Khách hàng vay tín dụng quay vòng (Dư nợ $2.2K, Churn thấp nhất 7.6%).*  
> *Phân cụm giúp ngân hàng định vị chính xác phân khúc rủi ro để phân bổ nguồn lực giữ chân tối ưu."*

---

### Slide 11 & 12: Hiệu năng Mô hình Máy học & Ma trận Nhầm lẫn (Thời lượng: 2 phút)
> *"Nhóm đã thử nghiệm và so sánh 4 mô hình phân loại:*  
> *• Logistic Regression (Baseline): ROC-AUC 0.9348, Recall 83.38%.*  
> *• Decision Tree: ROC-AUC 0.9458, Recall 88.92%.*  
> *• Random Forest: ROC-AUC 0.9838, Recall 87.08%.*  
> *🌟 **XGBoost Classifier vượt trội hoàn toàn** với **ROC-AUC đạt 0.9930**, **Recall đạt 91.38%**, **Precision 87.61%** và **Accuracy 96.54%**.*  
> *Nhìn vào ma trận nhầm lẫn, trên tập kiểm thử độc lập 2,026 khách hàng, XGBoost bắt trúng 297/325 khách hàng rời bỏ, chỉ bỏ sót 28 khách hàng và tỷ lệ báo động giả chỉ 2.4%."*

---

### Slide 13 & 14: Feature Importance & Tối ưu hóa Ngưỡng Kinh tế (Thời lượng: 1.5 phút)
> *"Phân tích Feature Importance khẳng định 3 nhân tố chi phối lớn nhất là: Tổng số lần giao dịch (`Total_Trans_Ct`), mức độ sụt giảm giao dịch quý cuối (`Total_Ct_Chng_Q4_Q1`) và dư nợ quay vòng (`Total_Revolving_Bal`).*  
> *Về mặt kinh tế, bằng cách mô hình hóa bài toán chi phí - lợi ích (CLV $500 vs Chi phí ưu đãi $50), nhóm đã xác định được **ngưỡng cắt xác suất tối ưu tại t = 0.42** (thay vì 0.50 mặc định), giúp tối đa hóa lợi nhuận ròng thu về đạt hơn $112,000 USD trên tập Test."*

---

### Slide 15: Ba Chân dung Khách hàng Rời bỏ (Thời lượng: 1.5 phút)
> *"Từ các bằng chứng thực nghiệm, nhóm đúc kết 3 chân dung khách hàng điển hình:*  
> *1. **The Silent Defector (Chiếm 55% Churn):** Ngủ đông, dư nợ về 0, không khiếu nại, lặng lẽ bỏ thẻ $ightarrow$ Can thiệp bằng E-voucher kích hoạt giao dịch cuối tuần.*  
> *2. **Frustrated Complainer (Chiếm 25% Churn):** Bất mãn vì gọi CSKH 3-6 lần $ightarrow$ Đội ngũ VIP Taskforce liên hệ giải quyết dứt điểm trong 24 giờ và miễn giảm phí linh hoạt.*  
> *3. **The VIP Switcher (Chiếm 20% Churn):** Thu nhập cao, bị đối thủ lôi kéo $ightarrow$ Cán bộ RM chủ động tặng lượt phòng chờ sân bay và nhân đôi điểm tích dặm bay."*

---

### Slide 16 & 17: Khung Chiến lược 4 Tầng & Hiệu quả Tài chính ROI 500% (Thời lượng: 1.5 phút)
> *"Nhóm đề xuất Khung chiến lược giữ chân 4 tầng khép kín: Tầng 1 - Cảnh báo sớm (EWS), Tầng 2 - CSKH chủ động, Tầng 3 - Gamified Loyalty và Tầng 4 - Bán chéo hệ sinh thái.*  
> *Mô phỏng trên quy mô 10,000 khách hàng thẻ:*  
> *• Nếu không can thiệp, ngân hàng mất $800,000 USD/năm.*  
> *• Ứng dụng mô hình XGBoost giúp cứu vãn thành công 960 khách hàng, mang lại giá trị CLV $480,000 USD.*  
> *• Trừ đi $80,000 USD chi phí can thiệp, ngân hàng thu về **lợi nhuận ròng tăng thêm $400,000 USD/năm**, tương ứng **tỷ suất hoàn vốn ROI lên tới 500%**."*

---

### Slide 18 & 19: Kết luận & Q&A (Thời lượng: 1 phút)
> *"Tóm lại, đề tài đã hoàn thành xuất sắc toàn diện từ làm sạch dữ liệu, khám phá quy luật hành vi, khai phá phân cụm K-Means, xây dựng mô hình XGBoost đạt ROC-AUC 0.9930 và đề xuất giải pháp kinh doanh mang lại ROI 500%.*  
> *Em xin chân thành cảm ơn Thầy/Cô và các bạn đã chú ý lắng nghe. Em rất mong nhận được những câu hỏi và ý kiến đóng góp quý báu từ Thầy/Cô!"*

---

## 🎯 PHẦN II: BỘ 10 CÂU HỎI PHẢN BIỆN KINH ĐIỂN CỦA GIẢNG VIÊN (Q&A DEFENSE)

### Câu hỏi 1: Vì sao nhóm lại loại bỏ 2 cột Naive Bayes ở cuối bảng mà không đưa vào huấn luyện mô hình?
* **Đáp án chuẩn:**  
  Hai cột này là kết quả dự báo xác suất rời bỏ được tạo sẵn bởi tác giả bộ dữ liệu trong một thử nghiệm trước đó. Nếu giữ lại trong ma trận đặc trưng $X$, mô hình máy học sẽ học trực tiếp từ nhãn dự đoán sẵn có này, dẫn đến hiện tượng **rò rỉ dữ liệu (Data Leakage)**. Khi đó, mô hình sẽ đạt điểm cao giả tạo trong môi trường thử nghiệm nhưng hoàn toàn vô dụng khi triển khai thực tế trên dữ liệu khách hàng mới. Việc loại bỏ là bắt buộc theo chuẩn mực khoa học dữ liệu.

### Câu hỏi 2: Tại sao nhóm lại giữ nguyên danh mục 'Unknown' trong các biến định tính thay vì xóa bỏ hoặc điền Mode?
* **Đáp án chuẩn:**  
  Biến `Education_Level` có 15.0%, `Income_Category` có 11.0% và `Marital_Status` có 7.4% giá trị 'Unknown'. Nếu xóa toàn bộ các dòng chứa 'Unknown', chúng ta sẽ mất đi gần 30% mẫu quan sát quý giá (gần 3,000 khách hàng). Nếu điền Mode (gán ép theo giá trị phổ biến nhất), chúng ta sẽ làm méo mó phân phối thực tế. Việc giữ nguyên 'Unknown' như một phân lớp thông tin độc lập phản ánh đúng thực tế ngành ngân hàng: Những khách hàng từ chối tiết lộ thu nhập/học vấn thường có tâm lý bảo mật cao hoặc thuộc phân khúc tài chính đặc thù cần được theo dõi riêng.

### Câu hỏi 3: Tập dữ liệu bị mất cân bằng lớp (16% Churn vs 84% Retained), nhóm đã xử lý kỹ thuật như thế nào?
* **Đáp án chuẩn:**  
  Nhóm đã áp dụng chiến lược đa tầng:  
  1. Sử dụng kỹ thuật chia mẫu phân tầng (`StratifiedKFold` và `stratify=y` trong `train_test_split`) để tỷ lệ 16% Churn được bảo toàn nguyên vẹn ở cả tập Train và Test.  
  2. Gán trọng số phạt lớp thiểu số (`class_weight='balanced'` trong Logistic/Random Forest và `scale_pos_weight = 8500/1627 ≈ 5.22` trong XGBoost).  
  3. Không sử dụng Accuracy làm thước đo chính mà tập trung tối ưu hóa **Recall (Độ nhạy)**, **F1-Score** và diện tích dưới đường cong **ROC-AUC**.

### Câu hỏi 4: Ý nghĩa nghiệp vụ thực tế của hiện tượng "Dư nợ quay vòng về 0" là gì?
* **Đáp án chuẩn:**  
  Trong nghiệp vụ thẻ, khách hàng duy trì dư nợ quay vòng (`Total_Revolving_Bal`) là những người đang tích cực sử dụng thẻ và trả góp định kỳ sinh lãi cho ngân hàng. Khi một khách hàng chuẩn bị đóng tài khoản, họ có xu hướng thanh toán dứt điểm toàn bộ số dư nợ để tránh bị tính lãi hoặc phát sinh phí trễ hạn, sau đó cất thẻ vào ngăn kéo (ngủ đông) trước khi gọi tổng đài yêu cầu hủy. Do đó, việc dư nợ quay vòng giảm đột ngột về $0.00 USD kết hợp với tần suất quẹt thẻ giảm là một chỉ báo trễ trực tiếp báo hiệu khách hàng chuẩn bị rời bỏ.

### Câu hỏi 5: Ngưỡng báo động 3 lần liên hệ tổng đài mang lại bài học gì cho khối Vận hành CSKH?
* **Đáp án chuẩn:**  
  Dữ liệu EDA chứng minh: Khách hàng liên hệ tổng đài 0-1 lần có tỷ lệ rời bỏ < 8%, nhưng khi liên hệ lần thứ 3, tỷ lệ rời bỏ tăng vọt lên 20.21%, lên 34.11% ở lần 4 và đạt 100% ở lần 6. Điều này chứng minh rằng khách hàng không tự nhiên gọi nhiều lần nếu sự cố của họ được giải quyết thỏa đáng ngay lần đầu. Ngân hàng cần áp dụng chỉ số **First-Contact Resolution (FCR)** và thiết lập cơ chế cảnh báo tự động: Ngay khi khách hàng phát sinh cuộc gọi thứ 3, hệ thống CRM phải lập tức gán cờ ưu tiên (VIP Ticket) để quản lý ca trực trực tiếp xử lý dứt điểm khiếu nại trong 24 giờ.

### Câu hỏi 6: Tại sao XGBoost lại đạt hiệu năng vượt trội hơn hẳn Logistic Regression trong bài toán này?
* **Đáp án chuẩn:**  
  Hành vi khách hàng thẻ tín dụng có tính chất phi tuyến tính phức tạp và chứa đựng nhiều tương tác chéo (ví dụ: mối quan hệ tương tác giữa số lần giao dịch, mức độ sụt giảm quý cuối và số sản phẩm sở hữu). Logistic Regression là mô hình tuyến tính nên gặp hạn chế khi phân tách các ranh giới phi tuyến này. Trong khi đó, XGBoost là thuật toán Ensemble dạng Boosting, xây dựng tuần tự các cây quyết định để sửa chữa sai số của các cây trước đó, kết hợp cơ chế phạt chính quy hóa L1/L2 (Regularization) giúp kiểm soát overfitting xuất sắc và tối ưu hóa ranh giới quyết định phi tuyến, đạt ROC-AUC lên tới 0.9930.

### Câu hỏi 7: Phân cụm K-Means phân loại được 4 nhóm khách hàng nào và ứng dụng thực tiễn ra sao?
* **Đáp án chuẩn:**  
  K-Means chia cơ sở khách hàng thành 4 nhóm hành vi tự nhiên:  
  • **Cụm 0 (37.6% - Phổ thông):** Giữ chân bằng tích điểm tiêu dùng định kỳ.  
  • **Cụm 1 (24.0% - Ngủ đông & Nguy cơ cao, Churn 41.8%):** Đối tượng ưu tiên số 1 cần can thiệp khẩn cấp bằng Voucher hoàn tiền kích hoạt lại giao dịch.  
  • **Cụm 2 (18.7% - VIP Chi tiêu lớn):** Chăm sóc qua cán bộ RM, tặng phòng chờ sân bay, tăng hạn mức thẻ.  
  • **Cụm 3 (19.7% - Vay tín dụng quay vòng, Churn thấp nhất 7.6%):** Khách hàng mang lại biên lợi nhuận lãi suất cao nhất, cần bán chéo thêm các gói vay tiêu dùng tín chấp.

### Câu hỏi 8: Nhóm đã tối ưu hóa ngưỡng cắt xác suất (Threshold Optimization) như thế nào?
* **Đáp án chuẩn:**  
  Ngưỡng mặc định 0.5 chỉ tối ưu về mặt thống kê xác suất thuần túy chứ không tối ưu về mặt kinh tế. Nhóm đã xây dựng hàm mục tiêu lợi nhuận ròng dựa trên bài toán chi phí: Lợi ích giữ được 1 khách là $500 (CLV), chi phí can thiệp là $50, và thiệt hại bỏ sót khách churn là -$500. Bằng cách quét ngưỡng xác suất từ 0.05 đến 0.95, nhóm tìm ra điểm cực đại của hàm lợi nhuận tại **ngưỡng t = 0.42**, giúp ngân hàng tối đa hóa lợi nhuận ròng thu về đạt hơn $112,000 USD trên tập kiểm thử.

### Câu hỏi 9: Hai biến `Credit_Limit` và `Avg_Open_To_Buy` có tương quan $r = 0.996$, việc này ảnh hưởng gì và nhóm xử lý ra sao?
* **Đáp án chuẩn:**  
  Tương quan $r = 0.996$ phản ánh hiện tượng gần như đa cộng tuyến hoàn hảo (Multicollinearity). Đối với mô hình Logistic Regression, đa cộng tuyến làm tăng phương sai của các hệ số hồi quy, khiến việc diễn giải trọng số biến bị sai lệch. Tuy nhiên, đối với các mô hình cây quyết định và Ensemble như Random Forest hay XGBoost, đa cộng tuyến không làm giảm độ chính xác dự báo (mô hình sẽ tự động chọn biến có thông tin phân tách tốt nhất tại mỗi nút rẽ). Khi huấn luyện Logistic Regression chuẩn mực, chúng ta có thể loại bỏ 1 trong 2 biến dựa trên hệ số VIF (Variance Inflation Factor).

### Câu hỏi 10: Đóng góp giá trị nhất mà nhóm muốn khuyến nghị cho Ban Giám đốc Khối Bán lẻ là gì?
* **Đáp án chuẩn:**  
  Khuyến nghị cốt lõi nhất là: **"Đừng đợi khách hàng gọi điện hủy thẻ mới bắt đầu giữ chân — hãy chuyển từ thế bị động sang chủ động bằng Hệ thống Cảnh báo Sớm (EWS) và Chiến lược Bán chéo Hệ sinh thái"**. Cụ thể:  
  1. Theo dõi chặt chẽ nhịp tim giao dịch: Ngay khi khách hàng quẹt thẻ dưới 5 lần/tháng hoặc không phát sinh giao dịch 2 tháng liên tiếp, hệ thống phải tự động đẩy ưu đãi kích hoạt ngay.  
  2. Gia tăng rào cản chuyển đổi: Đẩy mạnh bán chéo để mỗi khách hàng sở hữu $\ge 4$ sản phẩm tài chính, giúp tỷ lệ rời bỏ tự động giảm xuống chỉ còn xấp xỉ 10%, mang lại ROI 500% cho ngân hàng.
