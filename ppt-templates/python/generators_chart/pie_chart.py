"""Trang biểu đồ tròn - Vẽ hình quạt bằng đường dẫn freeform, chú giải bên phải, nhãn phần trăm"""

import math
from pptx.enum.shapes import MSO_SHAPE
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from python.base import TemplateGenerator


class PieChart(TemplateGenerator):
    """Trang biểu đồ tròn"""

    def __init__(self, theme=None):
        super().__init__(theme)
        self._title = ""
        self._subtitle = ""
        self._data = []  # list of dicts: {label, value, color}
        self._pie_colors = [
            RGBColor(52, 152, 219),
            RGBColor(231, 76, 60),
            RGBColor(46, 204, 113),
            RGBColor(155, 89, 182),
            RGBColor(241, 196, 15),
            RGBColor(230, 126, 34),
            RGBColor(26, 188, 156),
            RGBColor(243, 156, 18),
        ]
        self._show_percentage = True

    def set_title(self, title, subtitle=""):
        self._title = title
        self._subtitle = subtitle
        return self

    def set_data(self, data):
        """Thiết lập dữ liệu biểu đồ tròn

        Args:
            data: list of dict, mỗi mục gồm:
                label (str): Tên danh mục
                value (float): Giá trị số
                color (RGBColor, optional): Màu tùy chỉnh
        """
        self._data = data
        return self

    def _draw_pie_freeform(self, cx, cy, radius, start_angle, end_angle, color):
        """Vẽ hình quạt bằng đường dẫn custGeom

        Args:
            cx, cy: Tọa độ tâm (EMU)
            radius: Bán kính (EMU)
            start_angle: Góc bắt đầu (radian)
            end_angle: Góc kết thúc (radian)
            color: RGBColor
        """
        from lxml import etree

        ns_a = 'http://schemas.openxmlformats.org/drawingml/2006/main'
        ns_p = 'http://schemas.openxmlformats.org/presentationml/2006/main'

        shape_id = self._get_next_shape_id()

        # Điểm đầu và điểm cuối
        x1 = cx + int(radius * math.cos(start_angle))
        y1 = cy + int(radius * math.sin(start_angle))

        # Đơn vị swAng của OOXML arcTo là 60000ths của 1 độ
        sw_ang = int(math.degrees(end_angle - start_angle) * 60000)

        # Kích thước đường dẫn bằng kích thước hộp bao quanh
        path_w = int(radius * 2)
        path_h = int(radius * 2)

        xml_str = f'''<p:sp xmlns:p="{ns_p}" xmlns:a="{ns_a}">
          <p:nvSpPr>
            <p:cNvPr id="{shape_id}" name="Slice"/>
            <p:cNvSpPr/>
            <p:nvPr/>
          </p:nvSpPr>
          <p:spPr>
            <a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/></a:xfrm>
            <a:custGeom>
              <a:avLst/>
              <a:gdLst/>
              <a:ahLst/>
              <a:cxnLst/>
              <a:rect l="0" t="0" r="0" b="0"/>
              <a:pathLst>
                <a:path w="{path_w}" h="{path_h}">
                  <a:moveTo><a:pt x="{cx}" y="{cy}"/></a:moveTo>
                  <a:lnTo><a:pt x="{x1}" y="{y1}"/></a:lnTo>
                  <a:arcTo wR="{radius}" hR="{radius}" stAng="0" swAng="{sw_ang}"/>
                  <a:close/>
                </a:path>
              </a:pathLst>
            </a:custGeom>
            <a:solidFill><a:srgbClr val="{color[0]:02X}{color[1]:02X}{color[2]:02X}"/></a:solidFill>
            <a:ln><a:solidFill><a:srgbClr val="FFFFFF"/></a:solidFill><a:width val="12700"/></a:ln>
          </p:spPr>
          <p:txBody><a:bodyPr/><a:lstStyle/><a:p><a:endParaRPr lang="vi-VN"/></a:p></p:txBody>
        </p:sp>'''

        elem = etree.fromstring(xml_str)
        self.slide._element.append(elem)
        return elem

    def generate(self):
        """Tạo trang biểu đồ tròn"""
        self.create_slide()
        slide_w = self.prs.slide_width
        slide_h = self.prs.slide_height

        # Tiêu đề
        if self._title:
            self.add_textbox(
                self._title, Inches(0.5), Inches(0.3),
                slide_w - Inches(1), Inches(0.5),
                font_size=26, bold=True,
                font_color=RGBColor(44, 62, 80),
                alignment=PP_ALIGN.LEFT
            )
        if self._subtitle:
            self.add_textbox(
                self._subtitle, Inches(0.5), Inches(0.75),
                slide_w - Inches(1), Inches(0.35),
                font_size=13,
                font_color=RGBColor(127, 140, 141),
                alignment=PP_ALIGN.LEFT
            )

        n = len(self._data)
        if n == 0:
            return self

        # Tính tổng và tỷ lệ phần trăm
        total = sum(d["value"] for d in self._data)
        percentages = [d["value"] / total * 100 for d in self._data]

        # Tâm và bán kính biểu đồ tròn
        pie_cx = int(slide_w * 0.38)
        pie_cy = int(slide_h * 0.55)
        pie_radius = int(min(slide_w, slide_h) * 0.30)

        # Vẽ từng lát cắt
        current_angle = -math.pi / 2  # Bắt đầu từ hướng 12 giờ
        slice_centers = []

        for i, item in enumerate(self._data):
            color = item.get("color") or self._pie_colors[i % len(self._pie_colors)]
            slice_angle = 2 * math.pi * percentages[i] / 100

            end_angle = current_angle + slice_angle

            self._draw_pie_freeform(
                pie_cx, pie_cy, pie_radius,
                current_angle, end_angle, color
            )

            # Ghi lại góc tâm lát cắt để đặt nhãn tỷ lệ phần trăm
            mid_angle = current_angle + slice_angle / 2
            label_radius = pie_radius * 0.6
            label_x = pie_cx + int(label_radius * math.cos(mid_angle))
            label_y = pie_cy + int(label_radius * math.sin(mid_angle))
            slice_centers.append((label_x, label_y, percentages[i]))

            current_angle = end_angle

        # Nhãn tỷ lệ phần trăm
        if self._show_percentage:
            for lx, ly, pct in slice_centers:
                self.add_textbox(
                    f"{pct:.1f}%",
                    lx - Inches(0.35), ly - Inches(0.12),
                    Inches(0.7), Inches(0.24),
                    font_size=10, bold=True,
                    font_color=RGBColor(255, 255, 255),
                    alignment=PP_ALIGN.CENTER
                )

        # Chú giải bên phải
        legend_x = int(slide_w * 0.72)
        legend_y_start = int(slide_h * 0.25)
        legend_item_h = Inches(0.4)

        for i, item in enumerate(self._data):
            color = item.get("color") or self._pie_colors[i % len(self._pie_colors)]
            label = item.get("label", "")
            pct = percentages[i]

            y = legend_y_start + int(legend_item_h * i)

            # Khối màu
            self.add_shape(
                MSO_SHAPE.ROUNDED_RECTANGLE,
                legend_x, y,
                Inches(0.25), Inches(0.25),
                fill_color=color
            )
            # Văn bản nhãn
            self.add_textbox(
                f"{label}  {pct:.1f}%",
                legend_x + Inches(0.35), y - Inches(0.02),
                Inches(2.0), Inches(0.3),
                font_size=11,
                font_color=RGBColor(85, 85, 85),
                alignment=PP_ALIGN.LEFT
            )

        # Văn bản tâm (tổng lượng)
        self.add_textbox(
            f"{total:.0f}",
            pie_cx - Inches(0.5), pie_cy - Inches(0.2),
            Inches(1.0), Inches(0.35),
            font_size=18, bold=True,
            font_color=RGBColor(44, 62, 80),
            alignment=PP_ALIGN.CENTER
        )

        return self


if __name__ == "__main__":
    chart = PieChart()
    chart.set_title("Phân tích thị phần", "Market Share Distribution")
    chart.set_data([
        {"label": "Sản phẩm A", "value": 35},
        {"label": "Sản phẩm B", "value": 25},
        {"label": "Sản phẩm C", "value": 20},
        {"label": "Sản phẩm D", "value": 12},
        {"label": "Khác", "value": 8},
    ])
    chart.save("output/pie_chart.pptx")
    print("Đã tạo biểu đồ tròn: output/pie_chart.pptx")
