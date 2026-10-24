# Nhật ký thay đổi (CHANGELOG)

Tài liệu này ghi lại những thay đổi đáng chú ý của dự án. Định dạng dựa trên [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
và tuân theo quy tắc [Semantic Versioning](https://semver.org/).

## [1.1.0] - 2026-09-08

### Thêm mới

- **Bảo vệ nhánh**: Nhánh `main` yêu cầu vượt qua CI (Python 3.12 / TypeScript / Đồng nhất song ngữ) mới được phép gộp mã (merge)
- **Tài liệu quản trị kho mã**: Mẫu Issue (Báo cáo lỗi / Đề xuất tính năng) và mẫu PR

### Thay đổi

- `examples/batch_generate.py` chuyển sang ủy quyền cho `scripts/generate_all.py`, loại bỏ mã sinh trùng lặp

## [1.0.0] - 2026-09-08

Phiên bản chính thức đầu tiên.

### Thêm mới

- **API công khai thống nhất**: `python/__init__.py` xuất tổng hợp 39 lớp sinh slide, `TemplateGenerator`,
  `ALL_THEMES` cùng các hàm tiện ích thông dụng, có thể sử dụng trực tiếp: `from python import BarChart, ALL_THEMES`
- **Hỗ trợ đóng gói Python**: Bổ sung `pyproject.toml`, hỗ trợ cài đặt dạng editable `pip install -e .` và xuất bản gói
- **Kiểm thử tự động**: Bổ sung 31 ca kiểm thử pytest, bao phủ lớp cơ sở, 4 bộ sinh biểu đồ chính và toàn bộ 7 bộ chủ đề
- **Quy trình CI**: `.github/workflows/ci.yml`, chạy kiểm thử trên Python 3.10 / 3.11 / 3.12,
  đồng thời kiểm tra kiểu dữ liệu `tsc --noEmit` cho phía TypeScript
- **Kiểm tra tính tương đồng song ngữ**: Bổ sung `scripts/check_parity.py`, so khớp số lượng và cấu trúc các bộ sinh giữa Python và TypeScript nhằm tránh sai lệch tính năng lâu dài

### Sửa lỗi

- Sửa lệnh chạy nhanh JS trong README không thể thực thi (`npx tsx` → `npm run example`; do `tsx` không có trong danh sách phụ thuộc, công cụ thực tế là `ts-node`)
- Xóa 3 tệp ví dụ xuất ra bị commit nhầm: `output_quick_*.pptx`
- Hoàn thiện `.gitignore`, bổ sung quy tắc loại trừ cho tệp build, cache và môi trường ảo của Python cùng Node

### Thay đổi

- Thu hẹp phiên bản Python yêu cầu từ "3.8+" thành "3.10+": Python 3.8 đã hết hạn hỗ trợ từ 10/2024 và CI không hỗ trợ
- Đổi tên gói JS từ `ppt-generator` thành `@wuhua2026/ppt-templates`: tên cũ đã bị chiếm dụng trên npm và không thể xuất bản

### Tài liệu

- Bổ sung `CONTRIBUTING.md`, `CHANGELOG.md`, cùng các mẫu Issue và Pull Request
- README bổ sung hướng dẫn cài đặt ở chế độ editable

[1.0.0]: https://github.com/wuhua2026/ppt-templates/releases/tag/v1.0.0
