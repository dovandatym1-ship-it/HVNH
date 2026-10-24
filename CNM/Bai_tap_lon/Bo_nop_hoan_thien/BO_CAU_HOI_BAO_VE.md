# Bộ câu hỏi ôn bảo vệ

1. **Bài toán của MB đã được xác nhận chưa?** Chưa. MB là bối cảnh nghiên cứu; chưa có phỏng vấn hay dữ liệu nội bộ. Bài toán trong báo cáo là đề xuất cần xác minh.
2. **Vì sao dùng dữ liệu tổng hợp?** Để minh họa pipeline khi chưa có dữ liệu ngân hàng được phép dùng. Dữ liệu tổng hợp không thể chứng minh mô hình có hiệu quả ở MB.
3. **Nhãn gian lận được tạo thế nào?** Một latent risk score tổng hợp từ 8 đặc trưng cùng nhiễu Gaussian; nhóm lấy 1,8% quan sát có điểm latent cao nhất. Đây là nhãn thiết kế của nhóm, không phải kết luận từ điều tra.
4. **Có data leakage không?** Không dùng test để chọn ngưỡng; split stratified trước train/validation/test. Tuy nhiên generator đặt nhãn dựa trên cùng nhóm đặc trưng, làm tác vụ dễ hơn thực tế và tạo giới hạn construct validity.
5. **Vì sao chọn XGBoost?** Dữ liệu dạng bảng, XGBoost là mô hình gradient-boosted trees có tài liệu nghiên cứu và triển khai trưởng thành. Bài này không khẳng định nó tối ưu hơn mọi mô hình.
6. **Tại sao có baseline luôn âm?** Accuracy ở lớp lệch có thể đánh lừa; dummy cho thấy mốc không cảnh báo có recall 0 dù có thể có accuracy gần bằng tỷ lệ lớp đa số.
7. **Vì sao chọn F2?** F2 đặt trọng số recall cao hơn precision để làm tiêu chí thực nghiệm. Đây là quyết định học thuật, không phải hàm chi phí do ngân hàng phê duyệt.
8. **Ngưỡng được chọn thế nào?** Dò các score duy nhất trên validation, chọn F2 cao nhất; hòa thì ưu tiên alert rate thấp hơn, sau đó threshold cao hơn. Test chỉ dùng đánh giá.
9. **Tại sao dùng ba seed trên cùng split?** Để xem độ nhạy do yếu tố ngẫu nhiên khi huấn luyện. Ba seed không phải ba bộ dữ liệu độc lập và không chứng minh khái quát hóa.
10. **Precision thấp có ý nghĩa gì?** Một phần đáng kể cảnh báo dương là false positive theo nhãn tổng hợp; không thể tự động khóa/chặn chỉ theo điểm.
11. **ROC-AUC cao nhưng Precision thấp có mâu thuẫn không?** Không. ROC-AUC đánh giá xếp hạng trên nhiều ngưỡng; precision tại ngưỡng cụ thể phụ thuộc tỷ lệ lớp và tải cảnh báo.
12. **Score có phải xác suất đã hiệu chỉnh không?** Không. UI gọi là điểm/score, không tuyên bố xác suất thực tế.
13. **TreeSHAP chứng minh lý do gian lận không?** Không. Nó phân rã đầu ra mô hình; không xác định quan hệ nhân quả hay kết luận giao dịch gian lận.
14. **Tại sao không có Kafka/real-time?** Phạm vi là PoC cục bộ. Streaming là kiến trúc mở rộng, chưa được cài và chưa đo p95 đầu-cuối.
15. **Latency 0,xx ms có phải thời gian giao dịch?** Không. Đó là inference một hàng trên máy nghiên cứu sau warm-up, không gồm mạng, feature service, xác thực hay Core Banking.
16. **Có thể gọi giải pháp là đổi mới quy trình không?** Có thể định vị là đề xuất cải tiến quy trình hỗ trợ quyết định. Theo Oslo Manual, việc gọi là innovation đã thực hiện cần có thay đổi đáng kể được đưa vào sử dụng; PoC chưa đạt điều kiện đó.
17. **Làm sao tính ROI?** Cần dữ liệu về tổn thất đã xác nhận, tỷ lệ tổn thất ngăn được, chi phí hạ tầng, công xử lý và thiệt hại do báo sai. Báo cáo chỉ đưa công thức, chưa kết luận số.
18. **Nếu model/artifact lỗi thì hành vi là gì?** App fail-closed, dừng chấm; không diễn giải thành “an toàn”, dùng kiểm soát thông thường/chuyển xử lý thủ công.
19. **Vì sao không đưa quy định cụ thể vào kết luận tuân thủ?** PoC không tích hợp hệ thống xác thực, không đánh giá đầy đủ nghĩa vụ pháp lý và chưa có rà soát chuyên trách. Các quy định cần xác minh theo văn bản chính thức ở thời điểm triển khai.
20. **Bước tiếp theo trước production?** Xác nhận quy trình với chủ nghiệp vụ, quyền xử lý dữ liệu, định nghĩa nhãn, backtest theo thời gian, đánh giá cost-sensitive, shadow mode, human review, monitoring drift và phê duyệt bảo mật/pháp lý.
