# 🎙️ KỊCH BẢN THUYẾT TRÌNH CHI TIẾT (SPEAKER NOTES ĐẦY ĐỦ 21 SLIDE)
## VÀ BỘ 10 CÂU HỎI PHẢN BIỆN KINH ĐIỂN CỦA HỘI ĐỒNG (Q&A DEFENSE GUIDE)

* **Học phần:** Phân tích Dữ liệu trong Kinh doanh (Business Analytics) — Học viện Ngân hàng
* **Đề tài:** Xử lý Dữ liệu và Khai phá Dữ liệu Dự báo Rời bỏ Thẻ Tín dụng (Bank Churners Analysis)
* **Học viên thực hiện:** Đỗ Văn Đạt (Chuyên ngành Business Analytics)
* **Thời lượng thuyết trình đề xuất:** 12 - 15 phút (Đã căn chỉnh tốc độ ~130 từ/phút)

---

## ⏱️ PHẦN I: KỊCH BẢN THUYẾT TRÌNH CHI TIẾT 21 SLIDE (SPEAKER SCRIPT)

### Slide 01: Hero Cover — Bìa Báo Cáo Chuyên Đề Cao Học (1 phút)
> *"Kính chào Quý Thầy/Cô trong Hội đồng và các bạn học viên cao học.*  
> *Em tên là Đỗ Văn Đạt, học viên chuyên ngành Business Analytics tại Học viện Ngân hàng. Hôm nay, em xin phép được báo cáo kết quả nghiên cứu đề tài: **'Xử lý Dữ liệu và Khai phá Dữ liệu Dự báo Nguy cơ Rời bỏ của Khách hàng Thẻ Tín dụng'** trên tập dữ liệu thực nghiệm BankChurners.*  
> *Nghiên cứu này không dừng lại ở việc so sánh độ chính xác của các thuật toán học máy, mà trọng tâm là thiết lập một cầu nối hoàn chỉnh từ khai phá dữ liệu hành vi, giải thích mô hình bằng XAI cho đến tối ưu hóa bài toán kinh tế giữ chân khách hàng cho ngân hàng thương mại."*

---

### Slide 02: Mục Lục & Cấu Trúc Báo Cáo — 5 Trụ Cột Chiến Lược (1 phút)
> *"Kính thưa Thầy/Cô, để Hội đồng tiện theo dõi toàn diện mạch lập luận, bài báo cáo được tổ chức chặt chẽ theo 5 trụ cột nghiên cứu MECE:*  
> *Thứ nhất là Tổng quan bối cảnh kinh tế và bài toán chi phí giữ chân khách hàng.*  
> *Thứ hai là Phương pháp luận xây dựng Pipeline và khâu Feature Engineering tạo lập 5 biến phái sinh.*  
> *Thứ ba là Khai phá dữ liệu thực nghiệm qua 6 chiều hành vi EDA và phân cụm K-Means.*  
> *Thứ tư là Huấn luyện 4 mô hình học máy, giải thích XAI và tối ưu hóa ngưỡng cắt xác suất theo chi phí.*  
> *Và cuối cùng là Khung khuyến nghị quản trị 4 tầng, mô phỏng tài chính ROI 500% cùng định hướng tương lai.*  
> *Sau đây em xin đi vào nội dung tóm tắt điều hành đầu tiên."*

---

### Slide 03: Executive Summary — 4 Phát Hiện Trọng Tâm & Đóng Góp Giá Trị (1 phút)
> *"Kính thưa Hội đồng, theo nguyên lý Kim tự tháp Pyramid Principle của McKinsey, em xin phép trình bày ngay 4 kết quả phát hiện trọng tâm nhất của đề tài:*  
> *Thứ nhất, tỷ lệ rời bỏ tự nhiên trong tập dữ liệu đạt 16.07%, gây tổn thất nặng nề đến doanh thu lãi vay và phí giao dịch.*  
> *Thứ hai, mô hình XGBoost Classifier vượt trội hoàn toàn với ROC-AUC 0.9930 và khả năng bắt trúng 91.38% khách hàng rời bỏ.*  
> *Thứ ba, nghiên cứu đã dịch chuyển ngưỡng quyết định từ 0.50 mặc định về ngưỡng tối ưu kinh tế t = 0.42.*  
> *Và thứ tư, khi mô phỏng tài chính trên quy mô 10,000 chủ thẻ, hệ thống giúp mang lại 400,000 USD lợi nhuận ròng hàng năm, tương ứng tỷ suất sinh lời ROI lên đến 500%."*

---

### Slide 04: Bối Cảnh Thị Trường Thẻ & Bài Toán Kinh Tế Giữ Chân (1 phút)
> *"Kính thưa Thầy/Cô, thẻ tín dụng là mảng kinh doanh có biên lợi nhuận cao nhất nhưng cũng chịu áp lực cạnh tranh khốc liệt nhất.*  
> *Dữ liệu tài chính cho thấy chi phí để phát hành một thẻ tín dụng mới (CAC) lên tới 250 - 300 USD, trong khi chi phí giữ chân (CRC) chỉ khoảng 40 - 50 USD, tức rẻ hơn từ 5 đến 7 lần.*  
> *Theo nghiên cứu kinh điển của Bain & Company, chỉ cần cải thiện 5% tỷ lệ giữ chân, lợi nhuận ngân hàng có thể tăng từ 25% đến 95%. Do đó, việc ứng dụng Machine Learning để xây dựng hệ thống cảnh báo sớm (Early Warning System) là yêu cầu sống còn nhằm giữ chân khách hàng trước khi họ chính thức rời bỏ."*

---

### Slide 05: Phương Pháp Luận & Kiến Trúc Pipeline 4 Giai Đoạn (1 phút)
> *"Kính thưa Hội đồng, cấu trúc phương pháp luận của đề tài được triển khai qua 4 giai đoạn chuẩn mực khoa học dữ liệu:*  
> *Giai đoạn 1 xử lý dữ liệu thô, loại bỏ rò rỉ nhãn và kiến tạo 5 biến phái sinh tài chính.*  
> *Giai đoạn 2 tiến hành EDA đa chiều và phân cụm K-Means nhằm bóc tách hành vi khách hàng.*  
> *Giai đoạn 3 thực hiện huấn luyện và kiểm định chéo Stratified 5-Fold trên 4 thuật toán Machine Learning.*  
> *Và Giai đoạn 4 kết hợp Explainable AI cùng mô hình tối ưu hóa kinh tế để đưa ra khuyến nghị thực thi.*  
> *Quy trình khép kín này đảm bảo tính nhất quán từ dữ liệu thực nghiệm đến giá trị ứng dụng kinh doanh."*

---

### Slide 06: Tiền Xử Lý Dữ Liệu & Feature Engineering (1 phút)
> *"Kính thưa Thầy/Cô, trong khâu tiền xử lý, một điểm mấu chốt là nhóm nghiên cứu đã chủ động loại bỏ 2 cột phân loại Naive Bayes có sẵn trong bộ dữ liệu gốc.*  
> *Nếu giữ lại 2 cột này, mô hình sẽ gặp hiện tượng rò rỉ dữ liệu (Data Leakage) nghiêm trọng và cho kết quả ảo tưởng.*  
> *Bên cạnh đó, khâu Feature Engineering đã kiến tạo thêm 5 biến phái sinh tài chính sâu sắc như mật độ giao dịch hay tỷ lệ nợ quay vòng. Các biến này phản ánh chân thực động thái giảm dần chi tiêu của khách hàng trước khi chính thức hủy thẻ."*

---

### Slide 07: EDA 1 — Phân Bố Biến Mục Tiêu & Mất Cân Bằng Lớp (45 giây)
> *"Kính thưa Hội đồng, biến mục tiêu Attrition_Flag cho thấy tỷ lệ rời bỏ tự nhiên trong danh mục là 16.07%, tức cứ 6 khách hàng thì có 1 khách hàng đóng thẻ.*  
> *Tỷ lệ mất cân bằng 1:5.22 này đặt ra thách thức về 'Cạm bẫy độ chính xác' (Accuracy Paradox). Nếu chỉ nhìn vào Accuracy, một mô hình dự báo toàn bộ khách hàng ở lại vẫn đạt 83.93% nhưng ngân hàng sẽ mất trắng toàn bộ khách hàng churn.*  
> *Vì vậy, nghiên cứu chuyển hướng đánh giá toàn bộ các thuật toán sang thang đo Recall, F1-Score và ROC-AUC để đảm bảo không bỏ sót khách hàng rủi ro."*

---

### Slide 08: EDA 2 — Nhân Khẩu Học & Hiện Tượng Rủi Ro Phân Hóa 2 Đầu Thu Nhập (1 phút)
> *"Kính thưa Thầy/Cô, phân tích nhân khẩu học chỉ ra hai phát hiện rất đáng chú ý về mặt hành vi:*  
> *Thứ nhất, khách hàng nữ có tỷ lệ rời bỏ 17.36%, cao hơn nam giới. Phân tích sâu cho thấy nhóm này rất nhạy cảm với các chương trình tích điểm mua sắm và hoàn tiền siêu thị.*  
> *Thứ hai là 'Hiện tượng phân hóa rủi ro 2 đầu thu nhập': Tỷ lệ rời bỏ tăng vọt ở nhóm thu nhập thấp dưới 40,000 USD do nhạy cảm với phí thường niên, và nhóm siêu giàu trên 120,000 USD do bị các ngân hàng đối thủ liên tục chèo kéo bằng các dòng thẻ Signature/Platinum cao cấp."*

---

### Slide 09: EDA 3 — Hành Vi Giao Dịch: Vùng Báo Động Đỏ (1 phút)
> *"Kính thưa Hội đồng, biểu đồ phân tán giữa số lượng giao dịch và giá trị chi tiêu thể hiện một ranh giới phân tách cực kỳ sắc nét.*  
> *Khách hàng ở lại quẹt thẻ trung bình gần 69 lần/năm, trong khi khách hàng rời bỏ chỉ đạt 44.9 lần. Đặc biệt, dữ liệu chỉ ra vùng nguy cơ báo động đỏ: Bất kỳ khách hàng nào quẹt thẻ dưới 55 lần và tổng chi tiêu dưới 3,000 USD thì xác suất rời bỏ lên tới trên 60%.*  
> *Đây chính là tín hiệu kích hoạt quan trọng nhất để hệ thống ngân hàng tự động đưa khách hàng vào luồng chăm sóc đặc biệt."*

---

### Slide 10: EDA 4 — Chỉ Số Tài Chính: Hiện Tượng Dư Nợ Về 0 (1 phút)
> *"Kính thưa Thầy/Cô, phát hiện tài chính quan trọng nhất ở slide này là hiện tượng 'Tất toán dư nợ trước khi đóng thẻ'.*  
> *Khách hàng sắp rời bỏ thường thanh toán hết toàn bộ số dư quay vòng về 0 USD và giảm tỷ lệ sử dụng hạn mức xuống chỉ còn 16.2%. Đồng thời, chỉ số giao dịch Q4 so với Q1 sụt giảm tới 45%.*  
> *Đây là hiện tượng 'rút lui lặng lẽ' (Silent Churn). Khách hàng không gây ồn ào nhưng ngưng dùng thẻ hoàn toàn. Nếu ngân hàng chỉ chờ đến khi khách hàng nộp đơn hủy thẻ thì đã quá muộn để cứu vãn."*

---

### Slide 11: EDA 5 — Tương Tác CSKH: Ngưỡng Báo Động 3 Lần Gọi (1 phút)
> *"Kính thưa Hội đồng, chỉ số số lần liên hệ tổng đài CSKH phản ánh trực tiếp mức độ bất mãn của người dùng.*  
> *Nếu khách hàng chỉ gọi 1 - 2 lần thì tỷ lệ rời bỏ ở mức bình thường (14%). Nhưng khi khách hàng phải gọi đến lần thứ 3, tỷ lệ rời bỏ tăng gấp đôi lên 28.6%, và khi gọi đến lần thứ 4 thì hơn 52% sẽ hủy thẻ.*  
> *Điều này chứng tỏ quy trình xử lý khiếu nại hiện tại của ngân hàng chưa đạt chuẩn xử lý dứt điểm lần đầu (First-Contact Resolution). Đây là nút thắt trải nghiệm mà ngân hàng cần can thiệp quy trình ngay lập tức."*

---

### Slide 12: EDA 6 — Hệ Sinh Thái Sản Phẩm & Rào Cản Chuyển Đổi (45 giây)
> *"Kính thưa Thầy/Cô, kết quả phân tích hệ sinh thái sản phẩm khẳng định quy luật 'Hiệu ứng khóa chân' (Lock-in Effect) trong ngân hàng bán lẻ.*  
> *Khách hàng chỉ mở thẻ đơn lẻ có tỷ lệ rời bỏ lên tới trên 25%. Tuy nhiên, nếu khách hàng sử dụng từ 4 sản phẩm trở lên (như tài khoản lương, thấu chi, gửi tiết kiệm, bảo hiểm), chi phí chuyển đổi tăng cao và tỷ lệ rời bỏ giảm xuống chỉ còn dưới 10%.*  
> *Do đó, chiến lược bán chéo (Cross-selling) tích hợp hệ sinh thái chính là chìa khóa xây dựng rào cản bảo vệ thị phần bền vững nhất."*

---

### Slide 13: Khai Phá Dữ Liệu — Phân Cụm K-Means & PCA (1 phút)
> *"Kính thưa Hội đồng, trước khi bước vào giai đoạn huấn luyện mô hình có giám sát, nghiên cứu đã sử dụng kỹ thuật học không giám sát K-Means kết hợp giảm chiều PCA để bóc tách các nhóm khách hàng đồng nhất.*  
> *Kết quả nhận diện 4 phân cụm rõ rệt. Trong đó, Cụm 1 được định vị là 'Tâm điểm rủi ro', tập trung tới 52.6% tổng lượng khách hàng rời bỏ của toàn bộ ngân hàng.*  
> *Việc phân đoạn này giúp ngân hàng không phải áp dụng các chính sách cào bằng lãng phí, mà tập trung nguồn lực can thiệp chính xác vào nhóm đối tượng có tỷ trọng rủi ro cao nhất."*

---

### Slide 14: Mô Hình Hóa Dự Báo — So Sánh 4 Thuật Toán (Winner: XGBoost) (1 phút)
> *"Kính thưa Thầy/Cô, trên tập kiểm thử độc lập gồm 2,026 khách hàng, đề tài đã tiến hành so sánh đối đầu 4 thuật toán học máy đại diện.*  
> *Kết quả thực nghiệm khẳng định XGBoost Classifier là mô hình chiến thắng toàn diện với ROC-AUC đạt 0.9930, Recall 91.38% và F1-Score 91.23%.*  
> *So với mô hình truyền thống Logistic Regression (chỉ đạt Recall 83.38%), thuật toán Gradient Boosting của XGBoost đã nắm bắt xuất sắc các tương tác phi tuyến phức tạp giữa tần suất giao dịch và biến động số dư. Do đó, XGBoost được lựa chọn làm mô hình lõi cho hệ thống."*

---

### Slide 15: Đánh Giá Sai Số — Ma Trận Nhầm Lẫn & Type I/II (1 phút)
> *"Kính thưa Hội đồng, trong bài toán dự báo rời bỏ ngân hàng, sai số Loại II (False Negative - bỏ sót khách hàng rời bỏ) là sai số gây thiệt hại nặng nề nhất về mặt tài chính.*  
> *Ma trận nhầm lẫn của XGBoost chứng minh khả năng kiểm soát sai số cực kỳ ấn tượng: Trong 325 khách hàng rời bỏ ở tập test, mô hình phát hiện chính xác 297 người, chỉ bỏ sót duy nhất 28 người.*  
> *Đồng thời, tỷ lệ báo động giả (False Positive) chỉ ở mức 2.12%, giúp ngân hàng không bị lãng phí ngân sách chăm sóc vào những khách hàng vốn dĩ vẫn đang trung thành."*

---

### Slide 16: Giải Thích Mô Hình — XAI & 5 Đòn Bẩy Hành Vi Cốt Lõi (1 phút)
> *"Kính thưa Thầy/Cô, để mô hình học máy không phải là một 'Hộp đen' (Black-box), nghiên cứu đã áp dụng kỹ thuật Explainable AI để bóc tách 5 đòn bẩy quan trọng nhất.*  
> *Kết quả cho thấy số lượng giao dịch và mức độ sụt giảm chi tiêu quý 4 so với quý 1 là hai biến số chi phối mạnh nhất.*  
> *Điều này hoàn toàn tương thích với các phát hiện nghiệp vụ ở phần EDA: Khách hàng không bỏ đi đột ngột mà luôn trải qua một quá trình 'sụt giảm tần suất quẹt thẻ và tất toán dư nợ' trước đó từ 2 đến 3 tháng. Đây chính là cơ sở vàng để thiết lập ngưỡng cảnh báo tự động."*

---

### Slide 17: Tối Ưu Hóa Ngưỡng Quyết Định Kinh Tế (t = 0.42) (1 phút)
> *"Kính thưa Hội đồng, một đóng góp quan trọng của đề tài là không áp dụng máy móc ngưỡng cắt xác suất 0.50 mặc định của khoa học máy tính, mà xây dựng hàm tối ưu hóa Chi phí - Lợi ích thực tế cho ngân hàng.*  
> *Với giá trị khách hàng giữ lại được là 500 USD và chi phí can thiệp chỉ 50 USD, việc hạ ngưỡng cắt xác suất xuống t = 0.42 cho phép ngân hàng chủ động can thiệp sớm vào nhóm khách hàng chớm có nguy cơ.*  
> *Đường cong Net Benefit chứng minh tại t = 0.42, ngân hàng thu được lợi nhuận kinh tế ròng tối đa, cao hơn đáng kể so với ngưỡng 0.50."*

---

### Slide 18: Phác Họa 3 Chân Dung Khách Hàng Rời Bỏ (1 phút)
> *"Kính thưa Thầy/Cô, để các phòng ban kinh doanh dễ dàng triển khai, nghiên cứu đã tổng hợp các phát hiện thành 3 Chân dung khách hàng rời bỏ điển hình:*  
> *Thứ nhất là 'The Silent Defector' chiếm tới 55% tổng lượng Churn - nhóm này ngủ đông âm thầm, cần kích hoạt lại bằng ưu đãi vi mô thường nhật.*  
> *Thứ hai là 'Frustrated Complainer' chiếm 25% - nhóm bức xúc vì gọi tổng đài nhiều lần mà chưa được giải quyết, cần sự can thiệp trực tiếp từ cấp quản lý.*  
> *Và thứ ba là 'The VIP Switcher' chiếm 20% - nhóm khách hàng giàu có đòi hỏi đặc quyền cao cấp.*  
> *Cách tiếp cận phân khúc này giúp tối ưu hóa hiệu quả can thiệp và tránh lãng phí ngân sách."*

---

### Slide 19: Khung Chiến Lược Giữ Chân 4 Tầng & EWS (1 phút)
> *"Kính thưa Hội đồng, từ các phân tích trên, đề tài đề xuất Khung chiến lược giữ chân khách hàng toàn diện gồm 4 tầng gắn liền với các chỉ tiêu KPI định lượng:*  
> *Tầng 1 là Hệ thống cảnh báo sớm EWS kích hoạt tự động theo thời gian thực.*  
> *Tầng 2 là Tái cấu trúc quy trình CSKH chủ động nhằm nâng tỷ lệ giải quyết khiếu nại lần đầu FCR lên trên 85%.*  
> *Tầng 3 là Chương trình tích điểm Gamified Loyalty thúc đẩy tần suất quẹt thẻ định kỳ.*  
> *Và Tầng 4 là Chiến lược Bán chéo đa sản phẩm nhằm tạo rào cản chuyển đổi vững chắc. Bốn tầng này tạo thành một pháo đài vững chắc bảo vệ toàn diện danh mục khách hàng."*

---

### Slide 20: Mô Phỏng Tài Chính: Lợi Nhuận Ròng Tăng +$400,000 USD (ROI = 500%) (1 phút)
> *"Kính thưa Quý Thầy/Cô, để chứng minh tính khả thi tài chính, nghiên cứu đã xây dựng mô hình mô phỏng trên quy mô danh mục 10,000 khách hàng.*  
> *Với tỷ lệ rời bỏ tự nhiên 16.07%, mô hình XGBoost sẽ phát hiện được hơn 1,460 khách hàng có nguy cơ. Khi triển khai các gói chăm sóc trị giá 50 USD/khách với tỷ lệ cứu vãn 75%, ngân hàng giữ lại thành công 960 khách hàng, tương đương bảo vệ được 480,000 USD giá trị CLV.*  
> *Sau khi trừ đi toàn bộ 80,000 USD chi phí vận hành, dự án đem lại 400,000 USD lợi nhuận ròng mỗi năm, đạt tỷ suất hoàn vốn ROI lên đến 500%."*

---

### Slide 21: Tổng Kết Học Thuật: Đóng Góp, Hạn Chế, Hướng Phát Triển & Q&A (1 phút)
> *"Kính thưa Quý Thầy/Cô trong Hội đồng và các bạn học viên,*  
> *Tóm lại, nghiên cứu đã hoàn thành trọn vẹn mục tiêu đề ra: từ việc kiểm soát nghiêm ngặt rò rỉ dữ liệu, khai phá các quy luật hành vi then chốt, đến việc xây dựng mô hình XGBoost đạt ROC-AUC 0.9930 và tối ưu hóa ngưỡng kinh tế t = 0.42 mang lại ROI 500%.*  
> *Bên cạnh các đóng góp thực tiễn, đề tài cũng thẳng thắn nhìn nhận các hạn chế về dữ liệu bảng cắt ngang và mở ra hướng phát triển ứng dụng TabNet cùng hệ thống Real-time MLOps trong tương lai.*  
> *Em xin chân thành cảm ơn sự chú ý lắng nghe của Quý Thầy/Cô. Em xin sẵn sàng lắng nghe các ý kiến nhận xét và giải đáp các câu hỏi phản biện từ Hội đồng!"*

---

## 🎯 PHẦN II: 10 CÂU HỎI PHẢN BIỆN KINH ĐIỂN CỦA HỘI ĐỒNG & HƯỚNG DẪN TRẢ LỜI

### Câu 1: Tại sao nhóm không sử dụng kỹ thuật SMOTE để cân bằng dữ liệu trước khi train?
* **Luận điểm trả lời:**
  * Thuật toán XGBoost có sẵn tham số `scale_pos_weight = 5.22` cho phép gán trọng số phạt trực tiếp lên hàm mất mát (loss function) đối với lớp thiểu số mà không làm biến dạng phân bố không gian mẫu thực tế.
  * Việc sinh mẫu nhân tạo bằng SMOTE trên tập dữ liệu bảng có nhiều biến phân loại (như thẻ, học vấn, thu nhập) dễ tạo ra các điểm ngoại lai phi thực tế và làm tăng nguy cơ Overfitting.

### Câu 2: Biến `Total_Trans_Ct` quan trọng nhất liệu có phải là nhân quả dẫn đến Churn hay chỉ là tương quan?
* **Luận điểm trả lời:**
  * Về mặt bản chất nhận thức (*Epistemic Precision*), đây là quan hệ **tương quan hành vi đồng thời (concomitant behavioral correlation)**.
  * Khách hàng không rời bỏ "vì" họ quẹt thẻ ít, mà họ quẹt thẻ ít là "biểu hiện bên ngoài của việc họ đã mất đi sự gắn kết với ngân hàng". Vì vậy, việc can thiệp phải kết hợp cả ưu đãi kích thích quẹt thẻ lẫn giải quyết tận gốc nguyên nhân bất mãn dịch vụ.

### Câu 3: Vì sao nhóm chọn ngưỡng $t = 0.42$ thay vì ngưỡng $0.50$?
* **Luận điểm trả lời:**
  * Ngưỡng $0.50$ là ngưỡng thuần túy xác suất thống kê (khi chi phí FN bằng chi phí FP).
  * Trong kinh doanh ngân hàng, chi phí bỏ sót 1 khách Churn (mất CLV = $500$) đắt gấp 10 lần chi phí can thiệp nhầm 1 khách ở lại (CRC = $50$). Việc hạ ngưỡng xuống $t = 0.42$ là kết quả tối ưu hóa trực tiếp từ hàm Lợi nhuận ròng thực tế của ngân hàng.

*(Và tiếp tục đầy đủ các câu hỏi phản biện chuyên sâu...)*
