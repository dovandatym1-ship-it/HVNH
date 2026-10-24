# Nhật ký chạy UI PoC

**Chạy local:** Streamlit tại `http://localhost:8501` trong phiên kiểm thử. Run ID: `SYN25K-S42-SPLIT42-MODEL42_52_62-235575dfaf24`. Tất cả giá trị dưới đây là dữ liệu giả lập.

| Kịch bản | Đầu vào chính | Kết quả UI quan sát được | Diễn giải |
|---|---|---|---|
| Ít tín hiệu | 1.500.000 VND; 14 giờ; Mobile; thiết bị/vị trí cũ; sai OTP 0; tần suất 1; người nhận cũ | Score 0,01; “Rủi ro thấp; giữ nguyên các kiểm soát thông thường”; inference UI 5,687 ms | Không phải xác suất hiệu chỉnh; không miễn mandatory controls |
| Nhiều tín hiệu | 85.000.000 VND; 2 giờ; Mobile; thiết bị mới; vị trí bất thường; sai OTP 2; tần suất 6; người nhận mới | Score 99,92; “Đề xuất chuyển chuyên viên xem xét”; inference UI 3,749 ms | Không kết luận gian lận; không có lệnh giữ/chặn giao dịch |

Inference UI là một lần chạy trong phiên trình duyệt; không đại diện p95/SLA. Benchmark lặp 30 warm-up + 250 lời gọi được ghi riêng trong `metrics.json`.

Giao diện PoC đã được mở và các kết quả được quan sát trực tiếp trong task này. Ảnh màn hình được hiển thị trong luồng hội thoại; thư mục này giữ bảng kết quả kiểm tra, không lưu ảnh nhị phân riêng. Không có video ghi màn hình đính kèm.
