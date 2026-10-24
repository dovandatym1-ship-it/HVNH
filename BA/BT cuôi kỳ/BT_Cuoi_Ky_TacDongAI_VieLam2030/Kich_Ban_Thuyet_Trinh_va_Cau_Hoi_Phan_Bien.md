# Kịch bản thuyết trình & Câu hỏi phản biện
## Đề tài: Tác động của Trí tuệ nhân tạo (AI) đến Việc làm năm 2030
**Sinh viên thực hiện:** Đỗ Văn Đạt — Học phần Phân tích Kinh doanh — Học viện Ngân hàng

Thời lượng đề xuất: 12–15 phút thuyết trình (18 slide, ~45 giây/slide) + 5–10 phút hỏi đáp.

---

## PHẦN 1 — LỜI THOẠI THUYẾT TRÌNH THEO TỪNG SLIDE

### Slide 1 — Cover
Kính chào Hội đồng. Em xin trình bày đồ án cuối kỳ học phần Phân tích Kinh doanh với đề tài Tác
động của Trí tuệ nhân tạo đến Việc làm năm 2030. Bài trình bày gồm ba phần chính: bối cảnh và cơ
sở lý thuyết, phương pháp phân tích dữ liệu, và kết quả thực nghiệm cùng hàm ý quản trị nhân sự.
Toàn bộ phân tích được thực hiện trên bộ dữ liệu mô phỏng 3.000 quan sát gắn với 20 nghề nghiệp,
sử dụng quy trình tiền xử lý, phân tích khám phá dữ liệu, phân cụm và hai mô hình dự báo độc lập.

### Slide 2 — Tóm tắt điều hành
Phát hiện trung tâm của toàn bộ nghiên cứu là: biến định danh nghề nghiệp Job_Title giải thích
tới 85,7% phương sai của xác suất tự động hoá, trong khi mọi biến đặc điểm cá nhân như kỹ năng,
kinh nghiệm, học vấn và lương gần như không có giá trị dự báo. Khi đưa Job_Title vào mô hình,
F1-macro của bài toán phân loại ba nhóm rủi ro đạt 0,9947 và ROC-AUC đạt 0,998, được xác nhận
độc lập bởi mô hình hồi quy với R² đạt 0,86. Bốn con số này sẽ được giải thích chi tiết qua các
slide tiếp theo, đi từ bối cảnh nghiên cứu đến bằng chứng thực nghiệm.

### Slide 3 — Bối cảnh nghiên cứu
Câu hỏi nghiên cứu trung tâm của đồ án là: trong bộ dữ liệu này, điều gì thực sự quyết định rủi
ro tự động hoá của một công việc — đặc điểm cá nhân của người đang làm công việc đó, hay bản chất
của chính nghề nghiệp? Đây không phải câu hỏi hiển nhiên, vì trực giác thông thường thường cho
rằng người có kỹ năng cao, học vấn cao sẽ ít bị ảnh hưởng hơn bất kể họ làm nghề gì. Chúng ta sẽ
kiểm định giả thuyết này bằng một quy trình phân tích dữ liệu đầy đủ, bắt đầu từ nền tảng lý
thuyết ở slide tiếp theo.

### Slide 4 — Cơ sở lý thuyết
Khung lý thuyết trung tâm mà nghiên cứu dựa vào là task-based approach của Autor, Levy và Murnane
công bố năm 2003, cho rằng rủi ro tự động hoá gắn với tỷ trọng tác vụ thủ tục của công việc chứ
không phải năng lực cá nhân người thực hiện. Các nghiên cứu thực nghiệm sau đó của Frey và
Osborne, Acemoglu và Restrepo, cũng như báo cáo của McKinsey và Diễn đàn Kinh tế Thế giới đều
củng cố quan điểm này ở quy mô quốc gia và toàn cầu. Từ khung lý thuyết này, nhóm xây dựng giả
thuyết cụ thể để kiểm định trên dữ liệu của bài tập: biến Job_Title sẽ có sức giải thích vượt
trội so với các biến đặc điểm cá nhân.

### Slide 5 — Dữ liệu nghiên cứu
Bộ dữ liệu gồm 3.000 quan sát và 18 biến gốc, mô tả 20 nghề nghiệp phổ biến từ bác sĩ, giáo viên
đến nhân viên bảo vệ, bán lẻ. Mỗi hồ sơ có đầy đủ thông tin lương, số năm kinh nghiệm, trình độ
học vấn, hai chỉ số công nghệ là AI Exposure Index và Tech Growth Factor, mười điểm kỹ năng
chuẩn hoá, và hai biến mục tiêu là xác suất tự động hoá liên tục và nhóm rủi ro rời rạc ba mức.
Dữ liệu không có ô thiếu, không trùng lặp — đây là một bộ dữ liệu mô phỏng sạch, phù hợp để luyện
tập kỹ thuật phân tích trước khi mở rộng sang dữ liệu thực tế.

### Slide 6 — Tiền xử lý dữ liệu
Quy trình tiền xử lý gồm bốn bước. Bước một kiểm tra chất lượng dữ liệu và không phát hiện vấn đề
nào. Bước hai là phát hiện quan trọng nhất: nhóm rủi ro Risk_Category thực chất là hàm ngưỡng cố
định của xác suất tự động hoá liên tục, nên nếu đưa cả hai biến này vào cùng một mô hình phân
loại sẽ gây rò rỉ dữ liệu. Bước ba tạo thêm bảy biến đặc trưng mới và mã hoá một-nóng biến nghề
nghiệp thành mười chín biến giả. Bước bốn hoàn tất, cho ra bộ dữ liệu sẵn sàng huấn luyện mô hình.

### Slide 7 — EDA 1/3
Biểu đồ phân bố xác suất tự động hoá không có dạng đường cong chuẩn trơn thông thường mà thể
hiện ba vùng mật độ tách biệt khá rõ. Ba nhóm rủi ro Low, Medium, High được chia theo ngưỡng cố
định của xác suất này, trong đó nhóm Medium chiếm hơn một nửa mẫu quan sát. Hình dạng ba cụm mật
độ này là một gợi ý quan trọng: rất có thể có một biến phân loại tiềm ẩn nào đó đang quyết định
giá trị của biến mục tiêu. Chúng ta sẽ xác định chính xác biến đó là gì ở các slide tiếp theo.

### Slide 8 — EDA 2/3
Ma trận tương quan tổng hợp xác nhận: không một biến cá nhân nào — kể cả chỉ số phơi nhiễm AI vốn
tưởng như liên quan trực tiếp đến chủ đề — có tương quan đáng kể với xác suất tự động hoá. Tất cả
hệ số tương quan đều nhỏ hơn 0,05 về giá trị tuyệt đối. Điều này có nghĩa nếu chỉ dựa vào hồ sơ cá
nhân, chúng ta gần như không thể dự báo được rủi ro tự động hoá.

### Slide 9 — EDA 3/3 (Bằng chứng then chốt)
Đây là phát hiện quan trọng nhất của toàn bộ bài phân tích. Khi xếp hạng 20 nghề theo xác suất tự
động hoá trung bình, dữ liệu tách thành ba tầng rất rõ rệt. Tầng thấp gồm những nghề đòi hỏi phán
đoán chuyên môn sâu hoặc chăm sóc con người như bác sĩ, giáo viên, y tá, nhà nghiên cứu và kỹ sư
AI. Tầng cao gồm những nghề có tỷ trọng tác vụ lặp lại, thủ tục cao như nhân viên bán lẻ, bảo vệ,
xây dựng, hỗ trợ khách hàng và lái xe tải. Kiểm định eta bình phương định lượng phát hiện này:
riêng biến nghề nghiệp giải thích tới tám mươi lăm phẩy bảy phần trăm phương sai của xác suất tự
động hoá.

### Slide 10 — Phân cụm không giám sát
Ở bước phân cụm không giám sát, nhóm thử tìm các hồ sơ kỹ năng tự nhiên bằng thuật toán K-Means.
Kết quả chỉ số Silhouette chỉ dao động trong khoảng từ 0,055 đến 0,063 ở mọi giá trị k thử nghiệm
— mức rất gần không, cho thấy các cụm không tách biệt rõ ràng. Bốn cụm được chọn cho mục đích
diễn giải nghiệp vụ đều có xác suất tự động hoá trung bình gần như bằng nhau. Kết quả này càng
củng cố kết luận: sự khác biệt về rủi ro không nằm ở hồ sơ kỹ năng cá nhân mà nằm ở chính nghề
nghiệp.

### Slide 11 — Mô hình phân loại
Sau khi đưa biến Job_Title vào tập đặc trưng, ba mô hình phân loại được huấn luyện và so sánh.
Logistic Regression và XGBoost đạt kết quả gần như tuyệt đối và đồng hạng nhất với F1-macro
0,9947. Random Forest đạt kết quả thấp hơn một chút. Đây là bước ngoặt so với vòng thử nghiệm
trước đó khi chưa có Job_Title, lúc đó F1-macro chỉ đạt khoảng 0,22 đến 0,34, xấp xỉ mức dự đoán
ngẫu nhiên.

### Slide 12 — Mức độ quan trọng của biến
Biểu đồ mức độ quan trọng của biến từ mô hình XGBoost cho thấy nhóm biến nghề nghiệp chiếm tới
98,5% tổng mức độ quan trọng của mô hình. Toàn bộ các biến còn lại cộng lại chỉ chiếm chưa đến
2%. Đây là bằng chứng định lượng trực tiếp và thuyết phục nhất cho khung lý thuyết tiếp cận theo
tác vụ đã trình bày ở phần cơ sở lý thuyết.

### Slide 13 — Mô hình hồi quy
Để kiểm chứng phát hiện chính bằng một góc nhìn độc lập, nhóm xây dựng thêm mô hình hồi quy dự
báo trực tiếp giá trị liên tục của xác suất tự động hoá. Kết quả nhất quán hoàn toàn: mô hình
Linear Regression đạt R² bằng 0,862, với sai số tuyệt đối trung bình chỉ khoảng 8 điểm phần trăm
xác suất. Việc hai phương pháp đánh giá độc lập đều cho cùng kết luận giúp tăng đáng kể độ tin
cậy của phát hiện chính.

### Slide 14 — Ba chân dung nghề nghiệp
Để chuyển kết quả phân tích thành thông tin dễ sử dụng cho quản trị nhân sự, nhóm tổng hợp ba
tầng nghề nghiệp thành ba chân dung minh hoạ: tầng thấp gồm nghề chuyên môn sâu/chăm sóc con
người, tầng trung bình chiếm hơn một nửa mẫu, và tầng cao gồm những nghề có tỷ trọng tác vụ lặp
lại cao. Mỗi tầng đi kèm một hướng hành động quản trị nhân sự cụ thể.

### Slide 15 — Hàm ý quản trị nhân sự
Từ phát hiện thực nghiệm, hàm ý quan trọng nhất là: chiến lược đào tạo lại nên được thiết kế theo
NHÓM NGHỀ NGHIỆP thay vì chỉ dựa trên đánh giá năng lực cá nhân, vì hai người có hồ sơ kỹ năng
giống hệt nhau nhưng làm khác nghề có thể đối mặt mức rủi ro hoàn toàn khác nhau.

### Slide 16 — Hạn chế nghiên cứu
Trước khi kết luận, cần nêu rõ ba giới hạn quan trọng: đây là dữ liệu mô phỏng nên phát hiện chỉ
có giá trị nội tại; dữ liệu không có chiều thời gian hay biến ngành/vùng địa lý; và hiệu suất mô
hình gần như tuyệt đối phản ánh cách dữ liệu được sinh ra có kiểm soát, không nên xem là bằng
chứng cho khả năng dự báo tương tự trong thực tế.

### Slide 17 — Kết luận
Tóm lại, đồ án đã thực hiện trọn vẹn quy trình phân tích kinh doanh trên bộ dữ liệu mô phỏng.
Phát hiện xuyên suốt là biến nghề nghiệp quyết định gần như hoàn toàn rủi ro tự động hoá trong
khi đặc điểm cá nhân gần như không có vai trò — kết quả này nhất quán về mặt định tính với các lý
thuyết và nghiên cứu quốc tế đã trình bày ở đầu bài. Đây là một minh hoạ phương pháp luận có giá
trị, mở đường cho các phân tích sâu hơn trên dữ liệu thực tế trong tương lai. Em xin cảm ơn Hội
đồng đã lắng nghe và sẵn sàng trả lời các câu hỏi.

### Slide 18 — Q&A
Cảm ơn Hội đồng đã theo dõi phần trình bày. Em xin mời Hội đồng đặt câu hỏi.

---

## PHẦN 2 — CÂU HỎI PHẢN BIỆN DỰ KIẾN & GỢI Ý TRẢ LỜI

**Câu 1. Vì sao không đưa Automation_Probability_2030 vào tập đặc trưng khi dự báo Risk_Category?**
Vì kiểm tra ở Bước 2 (mục 2.2 báo cáo) cho thấy Risk_Category là hàm ngưỡng cố định của chính
biến này (Low 0,05–0,30; Medium 0,31–0,70; High 0,71–0,95, không chồng lấn). Đưa vào sẽ gây rò rỉ
dữ liệu — mô hình "biết trước đáp án" thay vì học quy luật thực sự.

**Câu 2. Vì sao phân cụm K-Means trên hồ sơ kỹ năng thất bại (Silhouette ≈ 0,06)?**
Vì 10 biến Skill_1..10 trong bộ dữ liệu mô phỏng được sinh độc lập ngẫu nhiên, không mang thông
tin phân biệt nghề nghiệp hay rủi ro. Đây là bằng chứng phụ trợ, không phải lỗi phương pháp — xác
nhận rằng khác biệt về rủi ro không nằm ở hồ sơ kỹ năng.

**Câu 3. Vì sao chọn k=4 dù Silhouette cao nhất ở k=2?**
Vì chênh lệch Silhouette giữa các k gần như không đáng kể (0,055–0,063, đều rất yếu) — không có k
nào thực sự "tốt hơn" về mặt thống kê. k=4 được chọn vì mục đích diễn giải nghiệp vụ (phân khúc
dễ truyền thông), điều này được nêu rõ là một giới hạn trong báo cáo, không phải khẳng định thống
kê mạnh.

**Câu 4. Kết luận "nghề nghiệp quyết định rủi ro" có áp dụng được cho thị trường lao động thực tế
không?**
Chỉ ở mức định tính (phù hợp hướng với task-based approach và Frey & Osborne). Về định lượng,
không — vì đây là dữ liệu mô phỏng có Automation_Probability_2030 được gán sẵn theo Job_Title.
Cần dữ liệu thực nghiệm (O*NET, WEF Future of Jobs Survey) để kiểm định định lượng cho thị trường
thực tế.

**Câu 5. Vì sao Logistic Regression và XGBoost cho kết quả giống hệt nhau (F1-macro 0,9947)?**
Vì tín hiệu Job_Title trong dữ liệu là gần như tất định (một nghề gần như luôn rơi vào đúng một
nhóm rủi ro) — bài toán trở nên gần như tách biệt tuyến tính hoàn hảo (linearly separable), nên
cả mô hình tuyến tính đơn giản lẫn mô hình cây phức tạp đều đạt trần hiệu suất tương tự.

**Câu 6. Vì sao Random Forest lại thấp hơn hai mô hình còn lại?**
Do giới hạn max_depth=10 áp đặt trong huấn luyện khiến một số cây chưa tách hết 19 biến giả
Job_Title ở độ sâu cho phép, dẫn đến một số hồ sơ Low bị phân loại nhầm sang Medium. Có thể khắc
phục bằng tăng max_depth hoặc số cây, đánh đổi với nguy cơ overfitting.

**Câu 7. Độ chính xác gần 100% có phải dấu hiệu overfitting không?**
Không, vì được đánh giá trên tập test độc lập (25%, chưa từng dùng để huấn luyện) và do bản chất
dữ liệu mô phỏng có tín hiệu Job_Title gần tất định (xem Câu 5) — đây là đặc điểm của DỮ LIỆU chứ
không phải lỗi mô hình học vẹt. Báo cáo (mục 3.5) đã nêu rõ đây là giới hạn cần lưu ý khi diễn
giải.

**Câu 8. Human_Edge_Score tự xây dựng có ý nghĩa thống kê không?**
Chỉ mang tính minh hoạ khái niệm (50% (1-AI_Exposure_Index) + 50% Skill_Diversity_Score), chưa
được kiểm định thống kê độc lập — biểu đồ 2.11/Hình 11 cho thấy chỉ số này cũng không phân biệt
được nhóm rủi ro, nhất quán với các thành phần cấu thành nó.

**Câu 9. Nếu áp dụng quy trình này cho dữ liệu thực tế, cần bổ sung gì?**
Cần: (i) dữ liệu đo lường tác vụ theo O*NET Task Ratings thay vì điểm kỹ năng tổng hợp; (ii)
chiều thời gian để theo dõi biến động; (iii) biến ngành/vùng địa lý; (iv) validation với khảo sát
độc lập (WEF Future of Jobs Survey) để tránh vòng lặp tự tham chiếu.

**Câu 10. Tại sao báo cáo đưa Job_Title vào cả hai mô hình phân loại VÀ hồi quy — có phải chỉ
đang "học thuộc" bảng tra cứu nghề nghiệp thay vì thực sự phân tích không?**
Đúng một phần — đây chính là điều báo cáo chủ động nêu ra ở mục 3.5 (Hạn chế): với 20 nghề cố
định, mô hình có xu hướng gần với "tra bảng" hơn là ngoại suy. Giá trị của phân tích không nằm ở
việc "mô hình dự báo giỏi" mà ở việc XÁC MINH có hệ thống rằng biến nghề nghiệp — chứ không phải
biến cá nhân — mới là nguồn thông tin thực sự trong dữ liệu, một kết luận có ý nghĩa phương pháp
luận dù mô hình cụ thể khó tổng quát hoá sang nghề nghiệp mới ngoài 20 nghề đã biết.
