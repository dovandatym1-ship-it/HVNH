"""Dòng thời gian sóng đôi - Hai đường sóng sin chạy ngang slide, các nút nằm ở đỉnh/đáy sóng"""

import math
from pptx.enum.shapes import MSO_SHAPE
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from python.base import TemplateGenerator
from python.utils import hex_to_rgb


class DualWaveTimeline(TemplateGenerator):
    """Dòng thời gian sóng đôi"""

    def __init__(self, theme=None):
        super().__init__(theme)
        self._title = ""
        self._subtitle = ""
        self._events = []  # list of dicts: {label, date, detail, is_future}
        self._wave_amplitude = Inches(0.6)
        self._node_radius = Inches(0.18)
        self._past_color = RGBColor(52, 152, 219)       # Xanh dương - Đã qua
        self._future_color = RGBColor(231, 76, 60)      # Đỏ - Tương lai
        self._wave1_color = RGBColor(52, 152, 219)
        self._wave2_color = RGBColor(46, 204, 113)
        self._line_color = RGBColor(189, 195, 199)

    def set_title(self, title, subtitle=""):
        self._title = title
        self._subtitle = subtitle
        return self

    def set_data(self, events):
        """Thiết lập danh sách sự kiện

        Args:
            events: list of dict, mỗi mục chứa:
                label (str): Tên sự kiện
                date (str): Ngày / mốc thời gian
                detail (str): Mô tả chi tiết
                is_future (bool): Có phải sự kiện tương lai không
                wave (int): Nằm trên sóng 1 hay sóng 2
        """
        self._events = events
        return self

    def _draw_wave_path(self, start_x, end_x, center_y, amplitude,
                        phase_shift, color, num_segments=80):
        """Vẽ đường cong hình sóng"""
        from lxml import etree
        nsmap = {
            'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
            'p': 'http://schemas.openxmlformats.org/presentationml/2006/main',
        }

        points = []
        for i in range(num_segments + 1):
            t = i / num_segments
            x = start_x + int((end_x - start_x) * t)
            y_offset = int(amplitude * math.sin(2 * math.pi * t * 1.5 + phase_shift))
            y = center_y + y_offset
            points.append((x, y))

        # Xây dựng XML hình tự do
        path_data = f'M {points[0][0]},{points[0][1]} '
        for px, py in points[1:]:
            path_data += f'L {px},{py} '

        freeform_xml = f'''<p:sp xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main"
                                 xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
          <p:nvSpPr><p:cNvPr id="{self._get_next_shape_id()}" name="WavePath"/>
            <p:cNvSpPr/><p:nvPr/></p:nvSpPr>
          <p:spPr>
            <a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/></a:xfrm>
            <a:prstGeom prst="line"><a:avLst/></a:prstGeom>
            <a:ln w="{Pt(2.5)}" cap="round" cmpd="sng">
              <a:solidFill><a:srgbClr val="{color}"/></a:solidFill>
            </a:ln>
          </p:spPr>
          <p:txBody><a:bodyPr/><a:lstStyle/><a:p><a:endParaRPr lang="vi-VN"/></a:p></p:txBody>
          <p:spPr>
            <a:pathLst>
              <a:path w="0" h="0">
                <a:moveTo><a:pt x="{points[0][0]}" y="{points[0][1]}"/></a:moveTo>'''

        for px, py in points[1:]:
            freeform_xml += f'''
                <a:lnTo><a:pt x="{px}" y="{py}"/></a:lnTo>'''

        freeform_xml += f'''
              </a:path>
            </a:pathLst>
          </p:spPr>
        </p:sp>'''

        elem = etree.fromstring(freeform_xml)
        self.slide._element.append(elem)

    def _get_wave_y(self, t, amplitude, phase_shift):
        """Tính toán độ lệch trục Y của sóng tại điểm t"""
        return int(amplitude * math.sin(2 * math.pi * t * 1.5 + phase_shift))

    def generate(self):
        """Sinh slide dòng thời gian sóng đôi"""
        self.create_slide()
        slide_w = self.prs.slide_width
        slide_h = self.prs.slide_height

        # Tiêu đề
        if self._title:
            self.add_textbox(
                self._title, Inches(0.5), Inches(0.3),
                slide_w - Inches(1), Inches(0.6),
                font_size=28, bold=True,
                font_color=RGBColor(44, 62, 80),
                alignment=PP_ALIGN.LEFT
            )
        if self._subtitle:
            self.add_textbox(
                self._subtitle, Inches(0.5), Inches(0.85),
                slide_w - Inches(1), Inches(0.4),
                font_size=14,
                font_color=RGBColor(127, 140, 141),
                alignment=PP_ALIGN.LEFT
            )

        margin_x = Inches(0.8)
        wave_start_x = int(margin_x)
        wave_end_x = int(slide_w - margin_x)
        wave_center_y_1 = int(slide_h * 0.4)
        wave_center_y_2 = int(slide_h * 0.6)

        color1_hex = f"{self._wave1_color[0]:02X}{self._wave1_color[1]:02X}{self._wave1_color[2]:02X}"
        color2_hex = f"{self._wave2_color[0]:02X}{self._wave2_color[1]:02X}{self._wave2_color[2]:02X}"

        # Vẽ 2 đường sóng
        self._draw_wave_path(wave_start_x, wave_end_x, wave_center_y_1,
                             self._wave_amplitude, 0, color1_hex)
        self._draw_wave_path(wave_start_x, wave_end_x, wave_center_y_2,
                             self._wave_amplitude, math.pi, color2_hex)

        # Đặt các nút và sự kiện trên sóng
        if self._events:
            n = len(self._events)
            for i, event in enumerate(self._events):
                t = (i + 0.5) / n
                x = wave_start_x + int((wave_end_x - wave_start_x) * t)

                wave_num = event.get("wave", 1 if i % 2 == 0 else 2)
                if wave_num == 1:
                    y_offset = self._get_wave_y(t, self._wave_amplitude, 0)
                    center_y = wave_center_y_1
                else:
                    y_offset = self._get_wave_y(t, self._wave_amplitude, math.pi)
                    center_y = wave_center_y_2

                node_y = center_y + y_offset
                is_future = event.get("is_future", False)
                node_color = self._future_color if is_future else self._past_color

                # Nút tròn
                r = self._node_radius
                self.add_shape(
                    MSO_SHAPE.OVAL,
                    x - r, node_y - r, r * 2, r * 2,
                    fill_color=node_color
                )

                # Đường nối (tới vị trí tương ứng của đường sóng kia)
                other_center_y = wave_center_y_2 if wave_num == 1 else wave_center_y_1
                other_phase = math.pi if wave_num == 1 else 0
                other_y_offset = self._get_wave_y(t, self._wave_amplitude, other_phase)
                other_y = other_center_y + other_y_offset

                connector = self.slide.shapes.add_connector(
                    1,  # đường thẳng nối
                    x, node_y,
                    x, other_y
                )
                connector.line.color.rgb = self._line_color
                connector.line.width = Pt(1)
                connector.line.dash_style = 2  # nét đứt

                # Nhãn sự kiện - xen kẽ phía trên hoặc phía dưới
                above = (wave_num == 1)
                label = event.get("label", "")
                date_str = event.get("date", "")
                detail = event.get("detail", "")

                label_y = node_y - r - Inches(1.2) if above else node_y + r + Inches(0.15)
                label_h = Inches(1.0)

                # Ngày tháng
                self.add_textbox(
                    date_str,
                    x - Inches(0.8), label_y,
                    Inches(1.6), Inches(0.25),
                    font_size=10, bold=True,
                    font_color=node_color,
                    alignment=PP_ALIGN.CENTER
                )
                # Tiêu đề
                self.add_textbox(
                    label,
                    x - Inches(0.8), label_y + Inches(0.25),
                    Inches(1.6), Inches(0.3),
                    font_size=12, bold=True,
                    font_color=RGBColor(44, 62, 80),
                    alignment=PP_ALIGN.CENTER
                )
                # Mô tả
                if detail:
                    self.add_textbox(
                        detail,
                        x - Inches(0.8), label_y + Inches(0.55),
                        Inches(1.6), Inches(0.35),
                        font_size=9,
                        font_color=RGBColor(127, 140, 141),
                        alignment=PP_ALIGN.CENTER
                    )

        # Chú thích (Legend)
        legend_y = slide_h - Inches(0.5)
        legend_x = Inches(0.5)
        self.add_shape(MSO_SHAPE.OVAL, legend_x, legend_y, Inches(0.15), Inches(0.15),
                        fill_color=self._past_color)
        self.add_textbox("Đã hoàn thành", legend_x + Inches(0.2), legend_y - Inches(0.02),
                          Inches(1.0), Inches(0.2), font_size=9,
                          font_color=RGBColor(127, 140, 141))

        self.add_shape(MSO_SHAPE.OVAL, legend_x + Inches(1.4), legend_y,
                        Inches(0.15), Inches(0.15), fill_color=self._future_color)
        self.add_textbox("Tương lai", legend_x + Inches(1.6), legend_y - Inches(0.02),
                          Inches(0.8), Inches(0.2), font_size=9,
                          font_color=RGBColor(127, 140, 141))

        return self


if __name__ == "__main__":
    timeline = DualWaveTimeline()
    timeline.set_title("Lộ trình phát triển dự án", "Dual Wave Timeline")
    timeline.set_data([
        {"label": "Khởi động dự án", "date": "2024-01", "detail": "Hoàn tất phân tích yêu cầu", "is_future": False, "wave": 1},
        {"label": "Thiết kế nguyên mẫu", "date": "2024-03", "detail": "Bàn giao thiết kế UI/UX", "is_future": False, "wave": 2},
        {"label": "Giai đoạn phát triển", "date": "2024-06", "detail": "Lập trình chức năng cốt lõi", "is_future": False, "wave": 1},
        {"label": "Thử nghiệm nội bộ", "date": "2024-09", "detail": "Kiểm thử nghiệm thu nội bộ", "is_future": False, "wave": 2},
        {"label": "Phát hành rộng rãi", "date": "2024-12", "detail": "Mở cổng đăng ký người dùng", "is_future": True, "wave": 1},
        {"label": "Nâng cấp phiên bản", "date": "2025-03", "detail": "Mở rộng tính năng nâng cao", "is_future": True, "wave": 2},
    ])
    timeline.save("output/dual_wave_timeline.pptx")
    print("Đã sinh dòng thời gian sóng đôi: output/dual_wave_timeline.pptx")
