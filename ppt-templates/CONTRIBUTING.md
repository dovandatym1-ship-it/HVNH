# Hướng dẫn đóng góp

Cảm ơn bạn đã quan tâm và muốn đóng góp cho Kho Mẫu Slide PPT. Tài liệu này mô tả cấu trúc kho lưu trữ và quy trình đóng góp.

## Cấu trúc kho lưu trữ

```
templates/                  230+ mẫu .pptx dựng sẵn (được tạo bởi scripts/generate_all.py)
python/                     Bộ sinh mã Python (dựa trên python-pptx)
  base.py                   Lớp cơ sở TemplateGenerator cho mọi bộ sinh
  animation.py              Động cơ chèn XML hoạt ảnh
  utils.py                  Hàm tiện ích về màu sắc, bố cục, bóng đổ,...
  generators_<nhóm>/        8 nhóm bộ sinh, tổng cộng 39 lớp sinh slide
themes/                     7 bộ chủ đề phối màu (kế thừa từ BaseTheme)
js/                         Bộ sinh mã TypeScript (dựa trên pptxgenjs), đối ứng 1:1 với phía Python
scripts/                    Kịch bản xây dựng và kiểm tra hợp đồng
tests/                      Bộ kiểm thử tự động pytest
```

## Phát triển cục bộ

```bash
# Phía Python
pip install -r requirements.txt
pip install -e .
pytest

# Phía TypeScript
cd js && npm install && npx tsc --noEmit

# Kiểm tra tính tương đồng giữa hai nền tảng
python scripts/check_parity.py
```

## Xác nhận trước khi gửi commit / PR

1. `pytest` vượt qua toàn bộ 100%
2. `npx tsc --noEmit` không có bất kỳ lỗi kiểu dữ liệu nào
3. `python scripts/check_parity.py` báo cáo hai phía hoàn toàn đồng nhất
4. Nếu thêm mới bộ sinh mã, **bắt buộc phải triển khai ở cả Python lẫn TypeScript**, nếu không luồng kiểm tra CI sẽ thất bại

## Quy ước

### Thêm bộ sinh mã mới

1. Tạo module mới trong thư mục `python/generators_<nhóm>/` tương ứng, lớp phải kế thừa từ `TemplateGenerator`
2. Xuất lớp trong `__init__.py` của nhóm đó và thêm vào danh sách `__all__`
3. Cập nhật đồng bộ vào tệp xuất tổng hợp `python/__init__.py`
4. Triển khai phiên bản tương đương trong `js/src/generators/<nhóm>.ts` và `export`
5. Bổ sung ca kiểm thử (test case) tương ứng

### Thêm chủ đề mới

1. Tạo module mới trong thư mục `themes/`, kế thừa từ lớp `BaseTheme`
2. Ghi đè tối thiểu 6 thuộc tính màu sắc: `primary`, `secondary`, `accent`, `background`, `text`, `muted`
3. Đăng ký chủ đề vào từ điển `ALL_THEMES` trong `themes/__init__.py`
4. Bộ kiểm thử chủ đề sẽ tự động bao phủ chủ đề mới, không cần thêm kiểm thử thủ công

> Lưu ý: Trong `ALL_THEMES` lưu trữ **lớp chủ đề** chứ không phải thể hiện (instance). Khi sử dụng cần khởi tạo: `ALL_THEMES["tên_chủ_đề"]()`.

### Không commit các nội dung sau

- Tệp kết quả sinh tạm thời như `output_*.pptx` (đã có trong `.gitignore`)
- Tệp font chữ, hình ảnh nhị phân dung lượng lớn
- Khóa bí mật API hoặc thông tin cấu hình cá nhân

## Quy cách viết Commit Message

Sử dụng tiền tố Conventional Commits để thuận tiện tự động tạo CHANGELOG:

```
feat:     Tính năng mới
fix:      Sửa lỗi
docs:     Tài liệu
test:     Kiểm thử
chore:    Cấu hình build / phụ thuộc / việc vặt
refactor: Tái cấu trúc mã nguồn
```

## Giấy phép

Mọi nội dung đóng góp mặc định được phát hành theo Giấy phép MIT.
