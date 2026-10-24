# QA và giới hạn của gói bàn giao

## Trạng thái nghiệm thu
- **Báo cáo Word:** OfficeCLI v1.0.150 chỉnh tiêu đề bìa và xác thực OpenXML, không còn lỗi schema. Word theo mẫu tham chiếu HVNH, 32 trang A4; phần mở đầu và 5 chương chiếm 25 trang (trang 3–27). Một trường TOC có cache số trang; `w:updateFields=true` để Word cập nhật nếu thay đổi headings/pagination.
- **Mẫu:** section A4 dọc và lề giữ như reference; SHA-256 reference vẫn `74fd217cd9e51527ebcee9ec91100e8c673b0cbdbe8f3e57413e36591a60e4ec`.
- **PDF:** Word PDF 32 trang; slide PDF 18 trang. Đã render và kiểm tra hình ảnh các trang, bảng chính, TOC, sơ đồ và biểu đồ.
- **Slide:** 18 slide; deck được mở rộng từ 16 lên 18 để bổ sung tổng quan nghiên cứu/case và tạo nhịp chuyển riêng từ phần học thuật sang demo, sau đó slide 18 chốt kết luận, số liệu, giới hạn và bước tiếp theo. Finalizer kiểm tra cấu trúc, slide size, font, bảng và biểu đồ native, không báo finding; PDF 18 trang đã render và kiểm tra trực quan. Chưa mở trong Microsoft PowerPoint.
- **PoC:** 22/22 pytest/AppTest đạt. Bộ model, metrics và manifest khớp SHA-256. Chạy lại ba seed trên cùng split tái tạo model hash và các metric số học đã ghi.
- **UI:** mở tại `http://localhost:8501`; đã chấm thử giao dịch tổng hợp ít tín hiệu (score 0,01, gợi ý rủi ro thấp) và nhiều tín hiệu (score 99,92, gợi ý chuyển chuyên viên). Đây là kết quả demo, không phải nhãn điều tra. Ảnh UI được hiển thị trong task, không có file ảnh nhị phân riêng; video chưa ghi.

## Việc nhóm cần hoàn thiện trước khi nộp
1. Thay placeholders trên bìa và bảng đóng góp bằng thông tin thật của 2–4 thành viên, giảng viên, lớp/khóa.
2. Đối chiếu số trang, yêu cầu trích dẫn và thời lượng trình bày với hướng dẫn của giảng viên nếu có bản chi tiết hơn.
3. Nếu nhóm sửa nội dung Word, dùng Word để Update Table of Contents và xuất lại PDF; sau đó chạy lại OfficeCLI validation và kiểm tra hình thức.
4. Nếu thay đổi mã, dữ liệu hoặc môi trường, chạy lại training/test và cập nhật báo cáo + slide từ cùng run ID.

**Ranh giới:** báo cáo, slide, UI và metrics chỉ chứng minh PoC trên dữ liệu tổng hợp. Không có dữ liệu/nhãn MB, không có tích hợp, không có kết luận pháp lý, không có ROI thực tế và không có quyết định giao dịch thật.
