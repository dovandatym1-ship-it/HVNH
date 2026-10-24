# Kịch bản trình diễn PoC (3–5 phút)

## Trước khi vào lớp
1. Mở terminal tại `CNM_Demo_PoC`.
2. Cài dependencies theo README, chạy `python train_model.py`, sau đó `streamlit run app.py`.
3. Mở giao diện local. Kiểm tra cảnh báo “dữ liệu tổng hợp”; không nhập bất kỳ dữ liệu cá nhân thật nào.
4. Nếu app không tải model, không tiếp tục demo như thể scoring chạy được. Chạy lại bước huấn luyện; dùng ảnh minh chứng và `metrics.json` làm dự phòng.

## Lời dẫn (20–30 giây)
“Đây là PoC học thuật trong bối cảnh nghiên cứu MB, chỉ dùng dữ liệu tổng hợp. Demo chấm điểm và gợi ý mức kiểm tra; không kết nối ngân hàng, không xác thực khách hàng và không chặn giao dịch.”

## Luồng trình diễn
1. **Nêu mục tiêu (20 giây):** minh họa pipeline đầu vào → kiểm tra → scoring → gợi ý cho người xem, không phải hệ thống ra quyết định giao dịch.
2. **Giao dịch rủi ro thấp (40 giây):** số tiền 1.500.000, giờ 14, kênh Mobile, thiết bị cũ, vị trí bình thường, sai OTP 0, tần suất 1, người nhận cũ. Ghi nhận kết quả thực tế trên UI; không hứa điểm cụ thể.
3. **Giao dịch có nhiều tín hiệu (50 giây):** số tiền 85.000.000, giờ 2, thiết bị mới, vị trí bất thường, sai OTP 2, tần suất 6, người nhận mới. Chỉ gọi là “điểm cao trong mô phỏng”; hành động là đề xuất chuyên viên xem xét.
4. **Giải thích (30 giây):** chỉ vào TreeSHAP raw margin. Nêu bias + feature contributions khớp raw margin nhưng không chứng minh nguyên nhân hay tính công bằng.
5. **Lịch sử (25 giây):** sinh 20 dòng tổng hợp, mở bảng lịch sử, xuất CSV, chỉ ra run ID/model seed.
6. **Đánh giá (45 giây):** mở bảng test và nói rõ trade-off: mô hình tìm được nhiều nhãn dương hơn baseline đơn giản theo protocol F2 đã chọn, nhưng vẫn tạo cảnh báo sai. Không dùng “bắt/chặn thành công”.
7. **Kết thúc (20 giây):** dữ liệu tổng hợp và nhãn sinh theo quy tắc là hạn chế chính; bước tiếp theo là xác minh nghiệp vụ, dữ liệu được phép dùng và pilot có giám sát.

## Dự phòng
- Không có mạng: UI chạy local sau khi cài dependencies và model artifacts đã sinh.
- App lỗi: dùng ảnh trong `minh_chung/` và đọc kết quả từ `metrics.json`; công khai rằng app không chạy tại thời điểm demo.
- Không có vùng ngưỡng trung bình ở một số cấu hình: dùng các dòng thực tế từ `test_predictions.csv`; không giả tạo score hoặc nhãn.
