# Gói nộp bài tập lớn CNM

## Đề tài
**Ứng dụng học máy hỗ trợ phát hiện giao dịch nghi ngờ gian lận: xây dựng và đánh giá PoC trên dữ liệu tổng hợp trong bối cảnh nghiên cứu MB.**

## Sản phẩm
- `Bao_cao_CNM_Fraud_PoC.docx` / `Bao_cao_CNM_Fraud_PoC.pdf`: báo cáo theo mẫu tham chiếu HVNH; 32 trang tổng cộng, trong đó 25 trang mở đầu + nội dung chính (trang 3–27), tài liệu tham khảo và phụ lục.
- `Bao_cao_CNM_Fraud_PoC.pptx` / `Bao_cao_CNM_Fraud_PoC_slides.pdf`: 18 slide bảo vệ theo mạch mở bài → thân bài → chuyển demo ở slide 17 → kết luận/Q&A ở slide 18, kèm nguồn trong speaker notes.
- `CNM_Demo_PoC/`: mã nguồn, môi trường phụ thuộc, model và metrics có manifest, notebook Colab, hướng dẫn chạy và 22 kiểm thử.
- `MA_TRAN_TRUY_VET.md`, `nguon/NGUON_VA_TRICH_DAN.md`, `KICH_BAN_DEMO.md`, `BO_CAU_HOI_BAO_VE.md`, `QA_REPORT.md` và `minh_chung/` (sơ đồ, biểu đồ, nhật ký UI).

## Chạy PoC local
```bash
cd CNM_Demo_PoC
python3 -m venv .venv
source .venv/bin/activate            # Windows: .venv\\Scripts\\activate
python -m pip install -r requirements.txt
python train_model.py
python -m pytest -q
python -m streamlit run app.py
```

## Giới hạn
Dữ liệu và nhãn là tổng hợp, không phải dữ liệu MB. Không nhập dữ liệu khách hàng thật. PoC không kết nối ngân hàng, không chạy Kafka/streaming, không xác thực khách hàng, không ra lệnh thanh toán/giữ/chặn tiền và không đánh giá tuân thủ production. Tên nhóm, thành viên/mã học viên, lớp và giảng viên trên bìa cần được điền theo thông tin thực tế trước khi nộp.

## Tái lập và OfficeCLI
Metrics được sinh từ `metrics.json`; model và kết quả được liên kết bằng SHA-256 manifest. Mục lục trong Word có cache số trang, cùng trường TOC để cập nhật lại khi headings thay đổi. DOCX đã được chỉnh tiêu đề bìa bằng OfficeCLI và xác thực OpenXML bằng OfficeCLI; xem `OFFICECLI_VALIDATION.txt`.

## Lưu ý Colab
Notebook đã đồng bộ với mã nguồn hiện tại và dùng proxy cửa sổ của Colab thay cho tunnel công khai. Runtime Colab chưa được xác minh; ưu tiên demo local. Không có video ghi màn hình; kịch bản chạy live và nhật ký UI nằm trong gói. Ảnh UI đã được hiển thị trong task nhưng không được lưu thành file riêng.
