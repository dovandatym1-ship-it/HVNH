---
name: ppt-generator
description: "Generate PowerPoint presentations from a template library with 230+ templates, 7 color themes, Python and JavaScript generators. Triggers on PPT, slides, or presentation creation requests."
---

# Bộ Sinh Mẫu Slide PPT

## Tổng quan

Skill này dùng để gọi thư viện mẫu PPT trên GitHub (https://github.com/wuhua2026/ppt-templates),
thông qua mã Python hoặc JavaScript để tự động tạo các bản trình bày PowerPoint chuyên nghiệp.

Thư viện mẫu bao gồm:
- 230+ mẫu .pptx dựng sẵn (hoạt họa + tĩnh + bài thuyết trình hoàn chỉnh)
- 7 bộ chủ đề màu sắc chuyên nghiệp
- Hỗ trợ song ngữ lập trình: Python (python-pptx) và JavaScript (pptxgenjs)

## Bước 1: Chuẩn bị môi trường

Trước mỗi lần sử dụng, xác nhận thư viện mẫu đã được cài đặt. Chạy script cài đặt:

```bash
python "path/to/ppt-generator/scripts/setup.py"
```

Thư viện mẫu được cài đặt tại thư mục `~/.ppt-templates/`. Nếu đã tồn tại, script sẽ tự động cập nhật (`git pull`).

## Bước 2: Chọn sử dụng Python hay JavaScript

- **Python** (Khuyến nghị): Tính năng đầy đủ nhất, hỗ trợ can thiệp XML hoạt họa, nhiều mẫu hơn
- **JavaScript**: Thích hợp cho lập trình viên Web, xây dựng trên pptxgenjs

## Hướng dẫn sử dụng với Python

Đường dẫn thư viện mẫu: `~/.ppt-templates/`

### Import cơ bản

```python
import sys, os
sys.path.insert(0, os.path.expanduser("~/.ppt-templates"))

# Import chủ đề màu
from themes import ALL_THEMES
theme = ALL_THEMES["blue_technology"]()  # Chủ đề công nghệ xanh dương

# Import bộ sinh
from python.generators_cover import GeometricRotationCover
from python.generators_complete import BusinessPlanAssembler
```

### 7 bộ chủ đề màu sẵn có

| Khóa (Key) | Tên tiếng Việt | Màu chính | Phù hợp với |
|------------|----------------|-----------|-------------|
| `blue_technology` | Công nghệ xanh dương | #0066CC | Công nghệ, Internet, Phần mềm |
| `purple_gradient` | Tím chuyển sắc | #7B2FBE | Sáng tạo, Thiết kế |
| `dark_gold` | Vàng kim sang trọng | #1A1A2E | Cao cấp, Doanh nghiệp |
| `minimalist_bw` | Đen trắng tối giản | #000000 | Đa dụng, Học thuật |
| `ocean_blue` | Xanh đại dương | #0077B6 | Giáo dục, Đào tạo |
| `green_nature` | Xanh thiên nhiên | #2D6A4F | Môi trường, Sức khỏe |
| `red_business` | Đỏ thương mại | #C0392B | Kinh doanh, Marketing |

### Danh sách bộ sinh sẵn có

**Bộ sinh trang bìa (Cover - 8 loại):**
- `GeometricRotationCover` - Bìa xoay hình học (hoạt họa)
- `CircleRingCover` - Bìa chuyển cảnh vòng tròn (hoạt họa)
- `TrainMistCover` - Bìa tàu xuyên sương mù (hoạt họa)
- `DiamondRevealCover` - Bìa mở màn hình thoi (hoạt họa)
- `MinimalistGradientCover` - Bìa chuyển sắc tối giản (tĩnh)
- `SplitScreenCover` - Bìa chia đôi màn hình (tĩnh)
- `HollowMaskCover` - Bìa mặt nạ chữ rỗng (tĩnh)
- `LayeredDepthCover` - Bìa chiều sâu đa tầng (tĩnh)

**Bộ sinh mục lục (Directory - 6 loại):**
- `DiamondAnimatedGenerator` - Mục lục hoạt họa hình thoi
- `CircularRingGenerator` - Mục lục vòng tròn
- `HexagonGenerator` - Mục lục tổ ong lục giác
- `SidebarGenerator` - Mục lục thanh điều hướng cạnh
- `CardGridGenerator` - Mục lục lưới thẻ
- `TimelineStyleGenerator` - Mục lục phong cách dòng thời gian

**Bộ sinh trang nội dung (Content - 5 loại):**
- `TextImageLayoutGenerator` - Bố cục văn bản kèm hình ảnh
- `ThreeColumnGenerator` - Bố cục 3 cột
- `FourGridGenerator` - Bố cục 4 ô lưới
- `FullImageOverlayGenerator` - Phủ toàn màn hình
- `ComparisonGenerator` - Bố cục so sánh đối chiếu

**Bộ sinh dòng thời gian (Timeline - 4 loại):**
- `DualWaveTimeline` - Dòng thời gian sóng đôi (hoạt họa)
- `HorizontalTimeline` - Dòng thời gian ngang
- `VerticalTimeline` - Dòng thời gian dọc
- `SpiralTimeline` - Dòng thời gian xoắn ốc (hoạt họa)

**Bộ sinh biểu đồ (Chart - 4 loại):**
- `BarChart` - Biểu đồ cột
- `PieChart` - Biểu đồ tròn
- `LineChart` - Biểu đồ đường
- `AnimatedBarChart` - Biểu đồ cột hoạt họa

**Bộ sinh trang đội ngũ (Team - 3 loại):**
- `PersonCardGenerator` - Thẻ giới thiệu cá nhân
- `TeamGridGenerator` - Lưới đội ngũ
- `OrgChartGenerator` - Sơ đồ cơ cấu tổ chức

**Bộ sinh trang kết thúc (Ending - 3 loại):**
- `ThankYouGenerator` - Trang cảm ơn
- `QRCodeGenerator` - Trang mã QR
- `ContactPageGenerator` - Trang thông tin liên hệ

**Bộ dựng bài thuyết trình hoàn chỉnh (Complete Decks - 6 loại):**
- `BusinessPlanAssembler` - Kế hoạch kinh doanh (18 trang)
- `CareerPlanningAssembler` - Định hướng nghề nghiệp (16 trang)
- `ProductLaunchAssembler` - Lễ ra mắt sản phẩm (20 trang)
- `AnnualReportAssembler` - Báo cáo thường niên (22 trang)
- `EducationCourseAssembler` - Bài giảng giáo dục (18 trang)
- `TechnologyThemeAssembler` - Trình diễn công nghệ (16 trang)

### Ví dụ sinh trang bìa đơn

```python
import sys, os
sys.path.insert(0, os.path.expanduser("~/.ppt-templates"))

from python.generators_cover.geometric_rotation import GeometricRotationCover
from themes.blue_technology import BlueTechnologyTheme

# Tạo bìa
cover = GeometricRotationCover(theme=BlueTechnologyTheme())
cover.set_title("Bản thuyết trình của tôi")
cover.set_subtitle("Nội dung tiêu đề phụ")
cover.generate()
cover.save("output_cover.pptx")
```

### Ví dụ sinh bài thuyết trình hoàn chỉnh

```python
import sys, os
sys.path.insert(0, os.path.expanduser("~/.ppt-templates"))

from python.generators_complete.business_plan import BusinessPlanAssembler
from themes.blue_technology import BlueTechnologyTheme

deck = BusinessPlanAssembler(theme=BlueTechnologyTheme())
deck.set_title("Kế hoạch kinh doanh dự án")
deck.set_subtitle("Kế hoạch phát triển năm 2026")
deck.generate()
deck.save("output_business_plan.pptx")
```

### Tùy chỉnh chủ đề riêng

```python
from themes import BaseTheme
from pptx.dml.color import RGBColor

class MyTheme(BaseTheme):
    name = "Chủ đề tùy chỉnh"
    primary = RGBColor(255, 107, 107)    # Màu chính tùy chỉnh
    secondary = RGBColor(78, 205, 196)   # Màu phụ tùy chỉnh
    accent = RGBColor(255, 195, 0)       # Màu nhấn tùy chỉnh

cover = GeometricRotationCover(theme=MyTheme())
```

## Hướng dẫn sử dụng với JavaScript

```bash
cd ~/.ppt-templates/js
npm install
```

```javascript
const pptxgen = require("pptxgenjs");
const { GeometricRotation } = require("./src/generators/cover");
const { blueTechnology } = require("./src/themes");

const gen = new GeometricRotation({ theme: blueTechnology });
gen.setTitle("Bản thuyết trình của tôi");
gen.setSubtitle("Tiêu đề phụ");
const pres = gen.generate();
pres.writeFile({ fileName: "output.pptx" });
```

## Sử dụng trực tiếp mẫu dựng sẵn

Nếu không cần sinh bằng code, bạn có thể sử dụng trực tiếp các file `.pptx` trong thư mục `~/.ppt-templates/templates/`:

```
templates/
├── animated/          # Mẫu hoạt họa (70 mẫu)
│   ├── cover/         # Bìa (28 mẫu)
│   ├── directory/     # Mục lục (21 mẫu)
│   ├── timeline/      # Dòng thời gian (14 mẫu)
│   └── chart/         # Biểu đồ (7 mẫu)
├── static/            # Mẫu tĩnh (154 mẫu)
│   ├── cover/         # Bìa (28 mẫu)
│   ├── directory/     # Mục lục (14 mẫu)
│   ├── content/       # Trang nội dung (35 mẫu)
│   ├── timeline/      # Dòng thời gian (14 mẫu)
│   ├── chart/         # Biểu đồ (21 mẫu)
│   ├── team/          # Đội ngũ (21 mẫu)
│   └── ending/        # Trang kết thúc (21 mẫu)
└── complete/          # Bài thuyết trình hoàn chỉnh (6 bài)
```

Quy tắc đặt tên file: `{loại_mẫu}_{tên_chủ_đề}.pptx`
Ví dụ: `geometric_rotation_blue_technology.pptx`

## Lưu ý

- Hiệu ứng hoạt họa hiển thị đầy đủ nhất trên Microsoft PowerPoint 2016+
- WPS Office hỗ trợ hoạt ảnh có phần hạn chế, khuyến nghị dùng các mẫu tĩnh
- Tất cả các bộ sinh đều hỗ trợ gọi phương thức dạng chuỗi: `generator.set_title("...").set_subtitle("...").generate()`
- Tệp xuất ra mặc định được lưu tại thư mục làm việc hiện tại
