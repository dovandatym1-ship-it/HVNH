## Loại thay đổi

- [ ] Sửa lỗi (fix)
- [ ] Tính năng mới (feat)
- [ ] Tài liệu (docs)
- [ ] Kiểm thử (test)
- [ ] Tái cấu trúc mã (refactor)
- [ ] Cấu hình build / phụ thuộc / việc vặt (chore)

## Giải thích

<!-- Thay đổi này đã làm những gì và tại sao cần thiết -->

## Issue liên kết

<!-- Ví dụ: Closes #1 -->

## Danh sách tự kiểm tra

Trước khi gửi, vui lòng xác nhận:

- [ ] Toàn bộ `pytest` vượt qua 100%
- [ ] `cd js && npx tsc --noEmit` không có lỗi kiểu dữ liệu
- [ ] `python scripts/check_parity.py` báo cáo hai phía hoàn toàn đồng nhất
- [ ] Nếu thêm/xóa bộ sinh mã, **Python và TypeScript đã được đồng bộ cả hai phía**
- [ ] Nếu thêm chủ đề mới, đã đăng ký vào `ALL_THEMES` trong `themes/__init__.py`
- [ ] Không commit các tệp sản phẩm như `output_*.pptx`
- [ ] Đã cập nhật README / CHANGELOG (nếu liên quan)

## Tác động

- [ ] Không phá vỡ API hiện tại (non-breaking change)
- [ ] Có thể phá vỡ API hiện tại (vui lòng mô tả hướng dẫn chuyển đổi bên dưới)

## Bổ sung

- Ảnh chụp màn hình / So sánh kết quả sinh:
- Những điểm reviewers cần đặc biệt lưu ý:
