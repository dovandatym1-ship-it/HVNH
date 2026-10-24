[![CI](https://github.com/wuhua2026/ppt-templates/actions/workflows/ci.yml/badge.svg)](https://github.com/wuhua2026/ppt-templates/actions/workflows/ci.yml)
# Kho Mẫu Slide PPT

> Bộ sưu tập mẫu PPT hiện đại, bao gồm các mẫu hoạt họa (animated) và tĩnh (static), hỗ trợ sinh tự động bằng mã Python và JavaScript.

## Tính năng nổi bật

- **237 mẫu .pptx dựng sẵn** (231 mẫu slide đơn trang + 6 bài thuyết trình hoàn chỉnh, hoạt họa + tĩnh)
- **32 kiểu bố cục trang đơn × 7 bộ chủ đề màu sắc**, kèm thêm 6 bộ bài thuyết trình đầy đủ
- **7 bộ chủ đề màu sắc** (Công nghệ xanh dương, Tím chuyển sắc, Vàng kim sang trọng, Đen trắng tối giản, Xanh đại dương, Xanh thiên nhiên, Đỏ thương mại)
- **Mã nguồn sinh bằng Python** (dựa trên python-pptx)
- **Mã nguồn sinh bằng JavaScript/TypeScript** (dựa trên pptxgenjs)
- **Bài thuyết trình hoàn chỉnh** (16-22 trang) × 6 kịch bản thực tế
- **Mẫu đơn trang** có thể tự do kết hợp linh hoạt
- **Khả năng tái tạo tuyệt đối**: Toàn bộ mẫu được tạo ra bằng mã lệnh, chạy lại cho kết quả từng trang đồng nhất (CI đã tích hợp kiểm tra mẫu rỗng tự động)

## Bắt đầu nhanh

### Cách 1: Tải về và sử dụng trực tiếp

1. Duyệt thư mục `templates/`, tìm theo phân loại `animated/` (hoạt họa) và `static/` (tĩnh)
2. Tải về file `.pptx` mong muốn
3. Mở bằng PowerPoint 2016+ hoặc WPS Office

### Cách 2: Sinh mã bằng Python

```bash
# Cài đặt thư viện phụ thuộc
pip install -r requirements.txt

# Tùy chọn: cài đặt ở chế độ editable để có thể import từ bất cứ đâu
pip install -e .

# Chạy ví dụ cơ bản
python examples/quick_start.py

# Chạy ví dụ phối màu tùy chỉnh
python examples/custom_colors.py

# Sinh hàng loạt toàn bộ mẫu
python examples/batch_generate.py
```

### Cách 3: Sinh mã bằng JavaScript

```bash
cd js && npm install && npm run example
```

## Phân loại mẫu

### Mẫu trang bìa (Cover)

| Tên mẫu | Phân loại | Mô tả |
|---------|-----------|-------|
| Bìa xoay hình học (Geometric Rotation) | Hoạt họa | Bố cục xoay hình học đa lớp |
| Bìa chuyển cảnh vòng tròn (Circle Ring) | Hoạt họa | Bố cục chuyển cảnh vòng tròn đồng tâm chuyển sắc |
| Bìa tàu xuyên sương (Train Mist) | Hoạt họa | Bìa phong cách sương mù tối giản |
| Bìa hé lộ hình thoi (Diamond Reveal) | Hoạt họa | Bìa điểm nhấn hình thoi mở màn |
| Bìa chuyển sắc tối giản (Minimalist Gradient) | Tĩnh | Phong cách chuyển sắc tối giản |
| Bìa chia đôi màn hình (Split Screen) | Tĩnh | Bố cục chia đôi màn hình trái - phải |
| Bìa mặt nạ chữ rỗng (Hollow Mask) | Tĩnh | Hiệu ứng mặt nạ chữ rỗng ấn tượng |
| Bìa chiều sâu đa tầng (Layered Depth) | Tĩnh | Thiết kế tạo chiều sâu đa tầng |

### Mẫu mục lục (Directory)

| Tên mẫu | Phân loại | Mô tả |
|---------|-----------|-------|
| Mục lục hoạt họa hình thoi (Diamond Animated) | Hoạt họa | Trang mục lục lưới hình thoi sống động |
| Mục lục vòng tròn (Circular Ring) | Hoạt họa | Mục lục tỏa tròn dạng nan hoa |
| Mục lục lục giác (Hexagon) | Hoạt họa | Mục lục tổ ong lục giác hiện đại |
| Mục lục thanh bên (Sidebar) | Tĩnh | Mục lục dạng thanh điều hướng bên trái |
| Mục lục thẻ lưới (Card Grid) | Tĩnh | Mục lục lưới dạng thẻ trực quan |
| Mục lục dòng thời gian (Timeline Style) | Tĩnh | Mục lục theo trục thời gian dọc |

### Mẫu dòng thời gian (Timeline)

| Tên mẫu | Phân loại | Mô tả |
|---------|-----------|-------|
| Dòng thời gian ngang (Horizontal Timeline) | Tĩnh | Dòng thời gian đường thẳng ngang cổ điển |
| Dòng thời gian dọc (Vertical Timeline) | Tĩnh | Dòng thời gian dạng thác đổ dọc |
| Dòng thời gian xoắn ốc (Spiral Timeline) | Tĩnh | Dòng thời gian đường xoắn ốc độc đáo |
| Dòng thời gian sóng đôi (Dual Wave Timeline) | Tĩnh | Dòng thời gian sóng đôi mềm mại |

### Mẫu giới thiệu đội ngũ (Team)

| Tên mẫu | Phân loại | Mô tả |
|---------|-----------|-------|
| Lưới đội ngũ (Team Grid) | Tĩnh | Sắp xếp thẻ thành viên dạng lưới |
| Thẻ nhân vật (Person Card) | Tĩnh | Giới thiệu cá nhân nổi bật khổ lớn |
| Sơ đồ tổ chức (Org Chart) | Tĩnh | Sơ đồ cơ cấu tổ chức phân cấp hình cây |

### Bài thuyết trình hoàn chỉnh (Complete Decks)

Số trang là cố định — chuỗi slide của từng bộ bài được lập trình cố định trong hàm `generate()`, không chứa nhánh rẽ động, đảm bảo kết quả mỗi lần sinh luôn đồng nhất.

| Kịch bản | Mô tả | Số trang |
|----------|-------|----------|
| Kế hoạch kinh doanh (Business Plan) | Thuyết trình kế hoạch kinh doanh toàn diện | 18 trang |
| Định hướng sự nghiệp (Career Planning) | Trình bày lộ trình phát triển bản thân | 16 trang |
| Ra mắt sản phẩm (Product Launch) | Giới thiệu và ra mắt sản phẩm mới | 20 trang |
| Báo cáo thường niên (Annual Report) | Báo cáo tổng kết năm của doanh nghiệp | 22 trang |
| Bài giảng giáo dục (Education Course) | Giáo án đào tạo và giảng dạy | 18 trang |
| Chủ đề công nghệ (Technology Theme) | Trình diễn giải pháp công nghệ | 16 trang |

## Bộ chủ đề màu sắc (Themes)

| Tên chủ đề | Khóa (Key) | Màu chính | Màu phụ | Màu nền | Phù hợp với |
|------------|------------|-----------|---------|---------|-------------|
| Công nghệ xanh dương | `blue_technology` | `#0066CC` | `#00CC99` | `#FFFFFF` | Công nghệ, Internet, Phần mềm |
| Tím chuyển sắc | `purple_gradient` | `#7B2FBE` | `#E040FB` | `#FFFFFF` | Sáng tạo, Thiết kế, Nghệ thuật |
| Vàng kim sang trọng | `dark_gold` | `#C9A96E` | `#B48C50` | `#1A1A2E` | Cao cấp, Tài chính, Sự kiện lớn |
| Đen trắng tối giản | `minimalist_bw` | `#000000` | `#333333` | `#FFFFFF` | Đa dụng, Học thuật, Nghiên cứu |
| Xanh đại dương | `ocean_blue` | `#0077B6` | `#00B4D8` | `#FFFFFF` | Giáo dục, Đào tạo, Dịch vụ |
| Xanh thiên nhiên | `green_nature` | `#2D6A4F` | `#52B788` | `#FFFFFF` | Môi trường, Nông nghiệp, Sức khỏe |
| Đỏ thương mại | `red_business` | `#C0392B` | `#E74C3C` | `#FFFFFF` | Thương mại, Bán hàng, Tiếp thị |

> Giá trị màu sắc chuẩn xác tuân theo `themes/*.py`. Bảng trên được trích xuất trực tiếp từ mã nguồn. "Vàng kim sang trọng" là chủ đề duy nhất sử dụng màu nền tối, trong đó màu chính là màu vàng kim thay vì màu nền.

## Ví dụ sử dụng Python API

### Sinh nhanh trang bìa

```python
from python.generators_cover import GeometricRotationCover

# Khởi tạo bìa xoay hình học
cover = GeometricRotationCover()
cover.set_title("Báo cáo thường niên").set_subtitle("Annual Report 2026")
cover.generate().save("output/report_cover.pptx")
print("Đã sinh trang bìa thành công!")
```

### Dùng chủ đề để sinh mục lục

```python
from themes import ALL_THEMES
from python.generators_directory.diamond_animated import DiamondAnimatedGenerator

# Sử dụng chủ đề Tím chuyển sắc
theme = ALL_THEMES["purple_gradient"]()

gen = DiamondAnimatedGenerator(theme=theme)
gen.set_title("Nội dung chính")
gen.set_items([
    {"number": "01", "title": "Phân tích thị trường"},
    {"number": "02", "title": "Thiết kế sản phẩm"},
    {"number": "03", "title": "Chiến lược vận hành"},
])
gen.generate()
gen.save("output/themed_directory.pptx")
```

### Sử dụng bộ dựng bài thuyết trình hoàn chỉnh

```python
from themes import ALL_THEMES
from python.generators_complete import BusinessPlanAssembler

# Sinh toàn bộ slide Kế hoạch kinh doanh (cố định 18 trang)
prs = BusinessPlanAssembler(theme=ALL_THEMES["blue_technology"]())
prs.set_title("Giải pháp văn phòng thông minh")
prs.set_subtitle("Smart Office Solution")
prs.generate().save("output/business_plan.pptx")
```

Tham số `theme` có thể bỏ qua; khi đó bộ dựng sẽ sử dụng màu mặc định được cấu hình sẵn bên trong.

## Ví dụ sử dụng JavaScript API

```typescript
import { TemplateGenerator } from './src/base';
import { blueTechnology } from './src/themes';

// Tạo generator và chỉ định chủ đề
const gen = new TemplateGenerator(blueTechnology);
const slide = gen.createSlide();

// Thêm văn bản
gen.addText(slide, {
  x: 1, y: 2, w: 8, h: 1,
  text: 'Xin chào PowerPoint',
  fontSize: 36,
  bold: true,
  align: 'center',
  color: gen.getTheme().primary,
});

// Lưu tệp
await gen.save('output/js_example');
```

## Quy ước đặt tên file

Mẫu đơn trang được đặt tên theo quy tắc: `[Tên mẫu]_[Khóa chủ đề].pptx` và lưu trong thư mục `templates/[static|animated]/[loại]/`:

```
[tên_mẫu]_[khóa_chủ_đề].pptx
```

Ví dụ:
- `static/cover/split_screen_ocean_blue.pptx`
- `static/chart/bar_chart_ocean_blue.pptx`
- `animated/directory/diamond_animated_purple_gradient.pptx`

Các bài thuyết trình hoàn chỉnh không nhân bản theo từng chủ đề mà đặt trực tiếp trong `templates/complete/`, tên tệp chính là tên kịch bản:
- `complete/business_plan.pptx`

## Cấu trúc thư mục

```
ppt-templates/
├── python/                  # Mã nguồn bộ sinh bằng Python
│   ├── base.py             # Lớp cơ sở TemplateGenerator
│   ├── utils.py            # Hàm tiện ích (màu sắc, bố cục, độ trong suốt, bóng đổ)
│   ├── animation.py        # Động cơ chèn hoạt ảnh XML
│   ├── generators_cover/   # Bộ sinh trang bìa (Cover)
│   ├── generators_directory/ # Bộ sinh mục lục (Directory)
│   ├── generators_timeline/  # Bộ sinh dòng thời gian (Timeline)
│   ├── generators_chart/     # Bộ sinh biểu đồ (Chart)
│   ├── generators_team/      # Bộ sinh giới thiệu đội ngũ (Team)
│   ├── generators_ending/    # Bộ sinh trang kết thúc (Ending)
│   └── generators_complete/  # Bộ dựng bài thuyết trình hoàn chỉnh (Complete Decks)
├── js/                     # Mã nguồn bộ sinh bằng JavaScript / TypeScript
│   ├── src/
│   │   ├── base.ts         # Lớp cơ sở TypeScript
│   │   ├── utils.ts        # Hàm tiện ích
│   │   └── themes/         # Định nghĩa các chủ đề màu
│   └── package.json
├── themes/                 # Chủ đề màu sắc cho Python
├── templates/              # Mẫu .pptx được tạo sẵn (237 mẫu)
│   ├── animated/           # Mẫu hoạt họa (70 mẫu)
│   │   ├── cover/          # Bìa (28 mẫu)
│   │   ├── directory/      # Mục lục (21 mẫu)
│   │   ├── timeline/       # Dòng thời gian (14 mẫu)
│   │   └── chart/          # Biểu đồ (7 mẫu)
│   ├── static/             # Mẫu tĩnh (161 mẫu)
│   │   ├── cover/          # Bìa (28 mẫu)
│   │   ├── directory/      # Mục lục (21 mẫu)
│   │   ├── content/        # Trang nội dung (35 mẫu)
│   │   ├── timeline/       # Dòng thời gian (14 mẫu)
│   │   ├── chart/          # Biểu đồ (21 mẫu)
│   │   ├── team/           # Giới thiệu đội ngũ (21 mẫu)
│   │   └── ending/         # Trang kết (21 mẫu)
│   └── complete/           # Bài thuyết trình hoàn chỉnh (6 bài)
├── examples/               # Kịch bản mã mẫu
├── scripts/                # Kịch bản sinh và kiểm thử
│   ├── generate_all.py     # Sinh hàng loạt 231 mẫu đơn trang
│   ├── generate_decks.py   # Sinh 6 bài thuyết trình hoàn chỉnh
│   ├── verify_templates.py # Tự kiểm tra tệp sinh (chặn mẫu rỗng)
│   └── check_parity.py     # Kiểm tra tính tương đồng giữa Python và TypeScript
└── tests/                  # Kiểm thử tự động pytest
```

## Khả năng tương thích

- **PowerPoint 2016+** (Windows/Mac)
- **WPS Office 2019+**
- **Google Slides** (Hỗ trợ hoạt ảnh có giới hạn, tương thích hoàn toàn với mẫu tĩnh)

## Khả năng xác minh và kiểm thử

Các mẫu trong kho lưu trữ không phải là các tệp nhị phân tải lên thủ công mà được sinh hoàn toàn tất định bằng mã nguồn và có thể tự động kiểm tra lại bất cứ lúc nào:

```bash
# 1) Tái tạo lại toàn bộ 231 mẫu đơn trang (khoảng 6 giây)
python scripts/generate_all.py --output ./out

# 2) Tái tạo lại 6 bài thuyết trình hoàn chỉnh
python scripts/generate_decks.py --output ./out_complete

# 3) Xác minh chất lượng: Bất kỳ mẫu nào có 0 trang hoặc trang đầu chỉ có tiêu đề sẽ trả về mã lỗi
python scripts/verify_templates.py templates
```

Bước 3 đã được tích hợp vào luồng CI (job có tên "Tự kiểm tra sản phẩm"). Tiêu chuẩn đánh giá là **số lượng hình khối trang đầu không dưới 4** — các trang rỗng chỉ có tiêu đề thường chỉ có 1~3 hình khối, trong khi trang có nội dung thực chất có từ 12~53 hình khối.

Ngoài ra CI còn chạy `scripts/check_parity.py` để kiểm tra hợp đồng tương thích hai đầu: ánh xạ tên lớp của 39 bộ sinh mã, đối chiếu từng mã màu của 7 bộ chủ đề. Khi sửa màu sắc hoặc thêm mới bộ sinh ở bất kỳ phía nào, phía còn lại bắt buộc phải đồng bộ, nếu không CI sẽ báo lỗi.

> Lưu ý: So sánh trực tiếp mã MD5 của file `.pptx` sẽ không bao giờ khớp vì tệp nén zip chứa dấu thời gian tạo. Nếu cần xác định hai lần sinh có tương đương nhau không, hãy giải nén và so sánh chữ ký nội dung của `ppt/slides/*` và `ppt/theme/*`.

## Yêu cầu môi trường

- Python 3.10+ (Phía Python, CI hỗ trợ 3.10 / 3.11 / 3.12)
- Node.js 18+ (Phía JavaScript)
- Hệ thống nên có font Microsoft YaHei hoặc font Unicode hỗ trợ tốt để đạt chất lượng hiển thị tối ưu

## Câu hỏi thường gặp (FAQ)

### Q: Hoạt ảnh không chạy được trên WPS?
A: WPS Office hỗ trợ định dạng hoạt ảnh OOXML có phần hạn chế. Khuyến nghị sử dụng Microsoft PowerPoint 2016+ để phát đầy đủ các hiệu ứng động.

### Q: Làm thế nào để tùy chỉnh bảng màu?
A: Kế thừa lớp `BaseTheme`, ghi đè các thuộc tính màu như `primary`, `secondary`,... để tạo chủ đề riêng. Chi tiết xem tại `examples/custom_colors.py`.

### Q: Tệp xuất ra nằm ở đâu?
A: Mặc định tệp được lưu tại thư mục làm việc hiện tại. Bạn có thể truyền đường dẫn xuất qua hàm `generator.save("duong_dan/file.pptx")`.

### Q: Tại sao trang biểu đồ tôi sinh ra lại bị trống?
A: Bộ sinh biểu đồ không tự sinh dữ liệu mặc định ngầm định, bạn bắt buộc phải gọi tường minh phương thức `set_data()`. Mỗi loại biểu đồ có định dạng dữ liệu riêng: Biểu đồ cột/tròn nhận `[{label, value}]`, trong khi biểu đồ đường nhận `set_data(series, x_labels)` với `series = [{name, data: [danh_sách_giá_trị]}]` — **`data` là danh sách các số thực, không phải từ điển `{x, y}`**.

### Q: Tại sao trang nội dung không sinh ra trang slide nào?
A: Bộ sinh trang nội dung cũng không chứa dữ liệu mặc định ngầm định và hoạt động theo cơ chế "duyệt qua từng item, mỗi item tạo 1 trang". Nếu danh sách items rỗng, nó sẽ xuất ra 0 trang mà không báo lỗi. Bạn có thể tham khảo cấu trúc dữ liệu mẫu trong các hằng số `DEFAULT_CONTENT_*` tại tệp `scripts/generate_all.py`.

### Q: Tại sao khi đổi chủ đề cho trang nội dung thì một số màu vẫn giữ nguyên?
A: Màu chính/màu phụ/màu nhấn của trang nội dung đều đổi theo chủ đề, tuy nhiên **màu nền thẻ và đường phân cách trung tính được cố ý giữ màu cố định** — nền sáng giúp đảm bảo độ tương phản của chữ nội dung, tránh việc khi đổi sang chủ đề tối như Vàng kim sang trọng sẽ làm giảm độ tương phản và khó đọc chữ. Chỉ các "màu cấu trúc" như gạch chân tiêu đề, thẻ danh mục, màu icon mới biến đổi theo chủ đề.

### Q: Tỷ lệ khung hình tạo bởi Python và TypeScript có giống nhau không?
A: Không giống, và đây là sự khác biệt có chủ đích: Lớp cơ sở Python mặc định tỷ lệ 10×7.5 inch (4:3), trong khi TypeScript mặc định 13.33×7.5 inch (16:9). Tọa độ của hơn 230 mẫu phía Python được tính toán theo 4:3, việc đồng nhất kích thước khung hình đòi hỏi phải căn chỉnh lại toàn bộ layout, vì vậy hiện tại chưa gộp chung.

### Q: Thêm một bộ sinh mã mới cần sửa đổi ở những nơi nào?
A: Cần sửa 3 vị trí: file `__init__.py` của nhóm tương ứng, file `python/__init__.py` ở thư mục gốc, và nhóm tương ứng phía TypeScript. Nếu muốn đưa vào kịch bản sinh hàng loạt, bạn cần đăng ký mục đó vào `TEMPLATE_REGISTRY` trong `scripts/generate_all.py` kèm theo dữ liệu mẫu `sample` — nếu thiếu dữ liệu mẫu sẽ sinh ra slide rỗng và bị CI chặn lại.

## Giấy phép

Giấy phép MIT - Xem chi tiết tại tệp [LICENSE](LICENSE)
