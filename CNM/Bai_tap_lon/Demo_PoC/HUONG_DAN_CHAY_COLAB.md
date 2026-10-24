# Hướng dẫn chạy PoC phát hiện giao dịch nghi ngờ

## Cảnh báo phạm vi
PoC chỉ dùng dữ liệu và nhãn tổng hợp, không phải hệ thống MB. Không nhập dữ liệu khách hàng thật. Ứng dụng không kết nối Core Banking, Kafka, xác thực khách hàng hay lệnh chuyển/giữ/chặn tiền. Gợi ý ở UI chỉ phục vụ minh họa.

## Chạy local
Từ thư mục chứa các file PoC:

```bash
python3 -m venv .venv
source .venv/bin/activate           # Windows: .venv\\Scripts\\activate
python -m pip install -r requirements.txt
python train_model.py
python -m pytest -q
python -m streamlit run app.py
```

`train_model.py` tạo `fraud_model.json`, `metrics.json`, `artifact_manifest.json`, `test_predictions.csv`, `seed_results.csv`, `threshold_tradeoff.csv`, `pr_curve_seed42.csv` và `feature_importance_seed42.csv`. UI dừng nếu artifact không khớp manifest; hãy chạy lại training khi thay đổi mã nguồn hoặc schema.

## Chạy Google Colab
1. Upload `MB_Bank_Fraud_Detection_GoogleColab.ipynb` lên Colab.
2. Chạy notebook từ đầu; cell setup ghi mã nguồn và requirements vào thư mục làm việc rồi cài thư viện.
3. Chạy huấn luyện và kiểm tra metrics.
4. Cell cuối khởi động Streamlit rồi gọi `google.colab.output.serve_kernel_port_as_window(8501)` để mở cửa sổ ứng dụng trong phiên Colab. Không tạo localtunnel hoặc URL công khai.
5. Colab/runtime proxy chưa được xác minh trong buổi kiểm thử hiện tại. Nếu cửa sổ không mở được, dùng local làm phương án demo chính.

## Kịch bản minh chứng
- Giao dịch ít tín hiệu: 1.500.000 VND, giờ 14, thiết bị cũ, vị trí bình thường, sai OTP 0, tần suất 1, người nhận cũ. Ghi nhận kết quả thực tế; không bảo đảm score.
- Giao dịch nhiều tín hiệu: 85.000.000 VND, giờ 2, thiết bị mới, vị trí bất thường, sai OTP 2, tần suất 6, người nhận mới. Chỉ mô tả “điểm cao trong mô phỏng”.
- Sinh batch 20 giao dịch tổng hợp, đối chiếu history/run ID và xuất CSV.
- Mở tab đánh giá, chỉ confusion matrix, AP/PR, false positive và lưu ý dữ liệu tổng hợp.

## Lỗi thường gặp
- Thiếu/hỏng model hoặc manifest: app báo lỗi và dừng scoring; không coi lỗi là giao dịch an toàn.
- Cài package fail: kiểm tra Python/pip và chạy `pip install -r requirements.txt` trong đúng môi trường.
- Local demo không mở: chạy `python -m streamlit run app.py`, sau đó mở `http://localhost:8501`.
- Kết quả sau khi thay code khác metrics trong báo cáo: chạy lại training, xác nhận run ID, rồi cập nhật báo cáo/slide đồng bộ.
