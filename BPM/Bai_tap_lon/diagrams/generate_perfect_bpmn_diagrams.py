#!/usr/bin/env python3
"""
Bộ công cụ tạo và kết xuất 4 sơ đồ Draw.io CHUẨN BPMN 2.0 & ENTERPRISE ARCHITECTURE
Đạt chuẩn mực thẩm mỹ cao nhất (C-level / Hội đồng chấm thi HVNH), sắc nét Retina 2x.
"""

import os
import subprocess
from pathlib import Path

DIAGRAM_DIR = Path('/Users/dovandat/WORKSPACE/HVNH/BPM/Bai_tap_lon/diagrams')
DRAWIO_BIN = '/Applications/draw.io.app/Contents/MacOS/draw.io'

def wrap_mxfile(diagram_name: str, cells_xml: str, width: int = 1460, height: int = 800) -> str:
    return f"""<mxfile host="app.diagrams.net" version="24.0.0">
  <diagram id="{diagram_name}" name="{diagram_name}">
    <mxGraphModel dx="1460" dy="800" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="{width}" pageHeight="{height}" background="#ffffff" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
{cells_xml}
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>"""

# ==============================================================================
# HÌNH 1: BẢN ĐỒ CHIẾN LƯỢC CẤP QUY TRÌNH (BALANCED SCORECARD STRATEGY MAP)
# ==============================================================================
def generate_hinh1():
    cells = """
        <!-- BANNER TIÊU ĐỀ -->
        <mxCell id="h1_banner" value="&lt;b style='font-size:16px;'&gt;BẢN ĐỒ CHIẾN LƯỢC QUY TRÌNH GIẢI NGÂN TÍN DỤNG (BALANCED SCORECARD STRATEGY MAP)&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:12px;color:#cbd5e1;'&gt;Đối chuẩn Chiến lược Chuyển đổi số &amp;amp; Tinh gọn vận hành LPBank (2024 - 2026)&lt;/span&gt;" style="rounded=1;arcSize=8;fillColor=#0f172a;strokeColor=#1e293b;fontColor=#ffffff;align=center;verticalAlign=middle;html=1;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="40" y="25" width="1340" height="60" as="geometry" />
        </mxCell>

        <!-- TẦNG 1: TÀI CHÍNH -->
        <mxCell id="h1_p_fin" value="&lt;b style='font-size:13px;'&gt;TÀI CHÍNH&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:10.5px;color:#c2410c;'&gt;(Financial)&lt;/span&gt;" style="rounded=1;arcSize=10;fillColor=#fff7ed;strokeColor=#ea580c;strokeWidth=2;fontColor=#9a3412;align=center;verticalAlign=middle;html=1;fontFamily=Arial;" vertex="1" parent="1">
          <mxGeometry x="40" y="105" width="160" height="120" as="geometry" />
        </mxCell>
        <mxCell id="h1_c_fin_bg" value="" style="rounded=1;arcSize=6;fillColor=#fafaf9;strokeColor=#ea580c;strokeWidth=1;dashed=1;html=1;" vertex="1" parent="1">
          <mxGeometry x="220" y="105" width="1160" height="120" as="geometry" />
        </mxCell>
        <mxCell id="h1_f1" value="&lt;b style='font-size:12.5px;color:#9a3412;'&gt;TĂNG TRƯỞNG TÍN DỤNG BÁN LẺ&lt;/b&gt;&lt;br&gt;&lt;div style='font-size:11px;color:#44403c;margin-top:5px;line-height:1.4;'&gt;• Tăng trưởng dư nợ an toàn +20%/năm&lt;br&gt;• Mở rộng tệp KH vay tiêu dùng &amp;amp; SXKD&lt;br&gt;&lt;b style='color:#c2410c;'&gt;KPI: Dư nợ bán lẻ đạt 180 nghìn tỷ VNĐ&lt;/b&gt;&lt;/div&gt;" style="rounded=1;arcSize=12;fillColor=#ffffff;strokeColor=#fdba74;strokeWidth=1.5;html=1;align=left;spacingLeft=15;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="240" y="120" width="345" height="90" as="geometry" />
        </mxCell>
        <mxCell id="h1_f2" value="&lt;b style='font-size:12.5px;color:#9a3412;'&gt;TỐI ƯU HÓA CHI PHÍ VẬN HÀNH&lt;/b&gt;&lt;br&gt;&lt;div style='font-size:11px;color:#44403c;margin-top:5px;line-height:1.4;'&gt;• Giảm 60% chi phí xử lý trên mỗi món vay&lt;br&gt;• Loại bỏ in ấn, lưu trữ hồ sơ giấy tờ&lt;br&gt;&lt;b style='color:#c2410c;'&gt;KPI: Tỷ lệ CIR toàn hàng duy trì ≤ 29%&lt;/b&gt;&lt;/div&gt;" style="rounded=1;arcSize=12;fillColor=#ffffff;strokeColor=#fdba74;strokeWidth=1.5;html=1;align=left;spacingLeft=15;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="625" y="120" width="345" height="90" as="geometry" />
        </mxCell>
        <mxCell id="h1_f3" value="&lt;b style='font-size:12.5px;color:#9a3412;'&gt;KIỂM SOÁT CHẤT LƯỢNG NỢ XẤU&lt;/b&gt;&lt;br&gt;&lt;div style='font-size:11px;color:#44403c;margin-top:5px;line-height:1.4;'&gt;• Cảnh báo sớm tín dụng tự động qua Core T24&lt;br&gt;• Giảm thiểu rủi ro gian lận chứng từ giải ngân&lt;br&gt;&lt;b style='color:#c2410c;'&gt;KPI: NPL duy trì mức an toàn ≤ 1.5%&lt;/b&gt;&lt;/div&gt;" style="rounded=1;arcSize=12;fillColor=#ffffff;strokeColor=#fdba74;strokeWidth=1.5;html=1;align=left;spacingLeft=15;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="1010" y="120" width="350" height="90" as="geometry" />
        </mxCell>

        <!-- TẦNG 2: KHÁCH HÀNG -->
        <mxCell id="h1_p_cust" value="&lt;b style='font-size:13px;'&gt;KHÁCH HÀNG&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:10.5px;color:#0f766e;'&gt;(Customer)&lt;/span&gt;" style="rounded=1;arcSize=10;fillColor=#f0fdfa;strokeColor=#0d9488;strokeWidth=2;fontColor=#115e59;align=center;verticalAlign=middle;html=1;fontFamily=Arial;" vertex="1" parent="1">
          <mxGeometry x="40" y="245" width="160" height="120" as="geometry" />
        </mxCell>
        <mxCell id="h1_c_cust_bg" value="" style="rounded=1;arcSize=6;fillColor=#fafaf9;strokeColor=#0d9488;strokeWidth=1;dashed=1;html=1;" vertex="1" parent="1">
          <mxGeometry x="220" y="245" width="1160" height="120" as="geometry" />
        </mxCell>
        <mxCell id="h1_c1" value="&lt;b style='font-size:12.5px;color:#115e59;'&gt;RÚT NGẮN THỜI GIAN GIẢI NGÂN&lt;/b&gt;&lt;br&gt;&lt;div style='font-size:11px;color:#334155;margin-top:5px;line-height:1.4;'&gt;• Tiền về tài khoản ngay trong ngày làm việc&lt;br&gt;• Tự động giải ngân luồng STP không chờ đợi&lt;br&gt;&lt;b style='color:#0f766e;'&gt;KPI: TAT chuẩn ≤ 8h (Khoản vay nhỏ &amp;lt; 15p)&lt;/b&gt;&lt;/div&gt;" style="rounded=1;arcSize=12;fillColor=#ffffff;strokeColor=#5eead4;strokeWidth=1.5;html=1;align=left;spacingLeft=15;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="240" y="260" width="345" height="90" as="geometry" />
        </mxCell>
        <mxCell id="h1_c2" value="&lt;b style='font-size:12.5px;color:#115e59;'&gt;MINH BẠCH TIẾN ĐỘ HỒ SƠ 24/7&lt;/b&gt;&lt;br&gt;&lt;div style='font-size:11px;color:#334155;margin-top:5px;line-height:1.4;'&gt;• Tra cứu trạng thái xử lý theo thời gian thực&lt;br&gt;• Thông báo biến động số dư &amp;amp; hợp đồng tức thì&lt;br&gt;&lt;b style='color:#0f766e;'&gt;KPI: 100% hồ sơ hiển thị Realtime Tracking&lt;/b&gt;&lt;/div&gt;" style="rounded=1;arcSize=12;fillColor=#ffffff;strokeColor=#5eead4;strokeWidth=1.5;html=1;align=left;spacingLeft=15;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="625" y="260" width="345" height="90" as="geometry" />
        </mxCell>
        <mxCell id="h1_c3" value="&lt;b style='font-size:12.5px;color:#115e59;'&gt;NÂNG TẦM TRẢI NGHIỆM SỐ VƯỢT TRỘI&lt;/b&gt;&lt;br&gt;&lt;div style='font-size:11px;color:#334155;margin-top:5px;line-height:1.4;'&gt;• Ký số hợp đồng từ xa qua SmartCA / eSign&lt;br&gt;• Khách hàng không cần trực tiếp tới quầy&lt;br&gt;&lt;b style='color:#0f766e;'&gt;KPI: Tỷ lệ CSAT ≥ 90%, Chỉ số NPS ≥ 65&lt;/b&gt;&lt;/div&gt;" style="rounded=1;arcSize=12;fillColor=#ffffff;strokeColor=#5eead4;strokeWidth=1.5;html=1;align=left;spacingLeft=15;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="1010" y="260" width="350" height="90" as="geometry" />
        </mxCell>

        <!-- TẦNG 3: QUY TRÌNH NỘI BỘ -->
        <mxCell id="h1_p_proc" value="&lt;b style='font-size:13px;'&gt;QUY TRÌNH NỘI BỘ&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:10.5px;color:#1d4ed8;'&gt;(Internal Process)&lt;/span&gt;" style="rounded=1;arcSize=10;fillColor=#eff6ff;strokeColor=#2563eb;strokeWidth=2;fontColor=#1e40af;align=center;verticalAlign=middle;html=1;fontFamily=Arial;" vertex="1" parent="1">
          <mxGeometry x="40" y="385" width="160" height="120" as="geometry" />
        </mxCell>
        <mxCell id="h1_c_proc_bg" value="" style="rounded=1;arcSize=6;fillColor=#fafaf9;strokeColor=#2563eb;strokeWidth=1;dashed=1;html=1;" vertex="1" parent="1">
          <mxGeometry x="220" y="385" width="1160" height="120" as="geometry" />
        </mxCell>
        <mxCell id="h1_i1" value="&lt;b style='font-size:12.5px;color:#1e40af;'&gt;CHUẨN HÓA RULE ENGINE &amp;amp; PRE-CHECK&lt;/b&gt;&lt;br&gt;&lt;div style='font-size:11px;color:#334155;margin-top:5px;line-height:1.4;'&gt;• Khóa tự động trường dữ liệu nguồn (LOS/ECM)&lt;br&gt;• Tự động kiểm tra điều kiện tiên quyết trước thẩm định&lt;br&gt;&lt;b style='color:#1d4ed8;'&gt;KPI: Tỷ lệ tự động hóa Pre-check đạt 100%&lt;/b&gt;&lt;/div&gt;" style="rounded=1;arcSize=12;fillColor=#ffffff;strokeColor=#93c5fd;strokeWidth=1.5;html=1;align=left;spacingLeft=15;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="240" y="400" width="345" height="90" as="geometry" />
        </mxCell>
        <mxCell id="h1_i2" value="&lt;b style='font-size:12.5px;color:#1e40af;'&gt;TÍCH HỢP LIỀN MẠCH SMART BPM &amp;amp; T24&lt;/b&gt;&lt;br&gt;&lt;div style='font-size:11px;color:#334155;margin-top:5px;line-height:1.4;'&gt;• Xử lý giao dịch thẳng (STP) tự động hạch toán&lt;br&gt;• Cơ chế Idempotency Key chống hạch toán trùng lặp&lt;br&gt;&lt;b style='color:#1d4ed8;'&gt;KPI: Tỷ lệ STP đạt ≥ 35% tổng hồ sơ&lt;/b&gt;&lt;/div&gt;" style="rounded=1;arcSize=12;fillColor=#ffffff;strokeColor=#93c5fd;strokeWidth=1.5;html=1;align=left;spacingLeft=15;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="625" y="400" width="345" height="90" as="geometry" />
        </mxCell>
        <mxCell id="h1_i3" value="&lt;b style='font-size:12.5px;color:#1e40af;'&gt;TRIỆT TIÊU LÃNG PHÍ &amp;amp; LỖI REWORK&lt;/b&gt;&lt;br&gt;&lt;div style='font-size:11px;color:#334155;margin-top:5px;line-height:1.4;'&gt;• Cắt bỏ hoàn toàn bước kiểm tra trùng lặp 3 cấp&lt;br&gt;• Chuyển đổi ký số thay thế in ấn, đóng dấu bản cứng&lt;br&gt;&lt;b style='color:#1d4ed8;'&gt;KPI: Tỷ lệ Rework giảm từ 28% xuống &amp;lt; 5%&lt;/b&gt;&lt;/div&gt;" style="rounded=1;arcSize=12;fillColor=#ffffff;strokeColor=#93c5fd;strokeWidth=1.5;html=1;align=left;spacingLeft=15;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="1010" y="400" width="350" height="90" as="geometry" />
        </mxCell>

        <!-- TẦNG 4: HỌC TẬP & PHÁT TRIỂN -->
        <mxCell id="h1_p_learn" value="&lt;b style='font-size:13px;'&gt;HỌC TẬP &amp;amp; PHÁT TRIỂN&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:10.5px;color:#6d28d9;'&gt;(Learning &amp;amp; Growth)&lt;/span&gt;" style="rounded=1;arcSize=10;fillColor=#faf5ff;strokeColor=#7c3aed;strokeWidth=2;fontColor=#5b21b6;align=center;verticalAlign=middle;html=1;fontFamily=Arial;" vertex="1" parent="1">
          <mxGeometry x="40" y="525" width="160" height="120" as="geometry" />
        </mxCell>
        <mxCell id="h1_c_learn_bg" value="" style="rounded=1;arcSize=6;fillColor=#fafaf9;strokeColor=#7c3aed;strokeWidth=1;dashed=1;html=1;" vertex="1" parent="1">
          <mxGeometry x="220" y="525" width="1160" height="120" as="geometry" />
        </mxCell>
        <mxCell id="h1_l1" value="&lt;b style='font-size:12.5px;color:#5b21b6;'&gt;NÂNG CAO NĂNG LỰC THẨM ĐỊNH SỐ&lt;/b&gt;&lt;br&gt;&lt;div style='font-size:11px;color:#334155;margin-top:5px;line-height:1.4;'&gt;• Đào tạo kỹ năng phân tích rủi ro &amp;amp; dữ liệu số cho RM&lt;br&gt;• 100% nhân sự thành thạo thao tác hệ thống Smart BPM&lt;br&gt;&lt;b style='color:#6d28d9;'&gt;KPI: 100% cán bộ tín dụng vượt qua kỳ sát hạch&lt;/b&gt;&lt;/div&gt;" style="rounded=1;arcSize=12;fillColor=#ffffff;strokeColor=#d8b4fe;strokeWidth=1.5;html=1;align=left;spacingLeft=15;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="240" y="540" width="345" height="90" as="geometry" />
        </mxCell>
        <mxCell id="h1_l2" value="&lt;b style='font-size:12.5px;color:#5b21b6;'&gt;XÁC LẬP QUYỀN SỞ HỮU QUY TRÌNH (BPO)&lt;/b&gt;&lt;br&gt;&lt;div style='font-size:11px;color:#334155;margin-top:5px;line-height:1.4;'&gt;• Bổ nhiệm Business Process Owner chuyên trách&lt;br&gt;• Thiết lập cơ chế đo lường &amp;amp; cải tiến liên tục PDCA&lt;br&gt;&lt;b style='color:#6d28d9;'&gt;KPI: Họp rà soát hiệu năng Process Review định kỳ tháng&lt;/b&gt;&lt;/div&gt;" style="rounded=1;arcSize=12;fillColor=#ffffff;strokeColor=#d8b4fe;strokeWidth=1.5;html=1;align=left;spacingLeft=15;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="625" y="540" width="345" height="90" as="geometry" />
        </mxCell>
        <mxCell id="h1_l3" value="&lt;b style='font-size:12.5px;color:#5b21b6;'&gt;XÂY DỰNG VĂN HÓA DỮ LIỆU &amp;amp; KỶ LUẬT SLA&lt;/b&gt;&lt;br&gt;&lt;div style='font-size:11px;color:#334155;margin-top:5px;line-height:1.4;'&gt;• Gắn kết quả SLA giải ngân vào đánh giá KPI cá nhân&lt;br&gt;• Văn hóa minh bạch, không đổ lỗi lỗi hồ sơ giữa các khâu&lt;br&gt;&lt;b style='color:#6d28d9;'&gt;KPI: Tỷ lệ tuân thủ cam kết SLA toàn trình ≥ 98%&lt;/b&gt;&lt;/div&gt;" style="rounded=1;arcSize=12;fillColor=#ffffff;strokeColor=#d8b4fe;strokeWidth=1.5;html=1;align=left;spacingLeft=15;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="1010" y="540" width="350" height="90" as="geometry" />
        </mxCell>

        <!-- ĐƯỜNG LIÊN KẾT NHÂN QUẢ -->
        <mxCell id="h1_arr_l1_i1" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;strokeColor=#7c3aed;strokeWidth=2;" edge="1" parent="1" source="h1_l1" target="h1_i1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="h1_arr_l2_i2" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;strokeColor=#7c3aed;strokeWidth=2;" edge="1" parent="1" source="h1_l2" target="h1_i2">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="h1_arr_l3_i3" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;strokeColor=#7c3aed;strokeWidth=2;" edge="1" parent="1" source="h1_l3" target="h1_i3">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <mxCell id="h1_arr_i1_c1" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;strokeColor=#2563eb;strokeWidth=2;" edge="1" parent="1" source="h1_i1" target="h1_c1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="h1_arr_i2_c2" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;strokeColor=#2563eb;strokeWidth=2;" edge="1" parent="1" source="h1_i2" target="h1_c2">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="h1_arr_i3_c3" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;strokeColor=#2563eb;strokeWidth=2;" edge="1" parent="1" source="h1_i3" target="h1_c3">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <mxCell id="h1_arr_c1_f1" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;strokeColor=#0d9488;strokeWidth=2;" edge="1" parent="1" source="h1_c1" target="h1_f1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="h1_arr_c2_f2" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;strokeColor=#0d9488;strokeWidth=2;" edge="1" parent="1" source="h1_c2" target="h1_f2">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="h1_arr_c3_f3" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;strokeColor=#0d9488;strokeWidth=2;" edge="1" parent="1" source="h1_c3" target="h1_f3">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
    """
    return wrap_mxfile("Hinh1_Ban_do_chien_luoc_LPBank", cells, 1420, 680)

# ==============================================================================
# HÌNH 2: CẢNH QUAN QUY TRÌNH CẤP CAO & CHUỖI GIÁ TRỊ (PROCESS LANDSCAPE)
# ==============================================================================
def generate_hinh2():
    cells = """
        <!-- BANNER TIÊU ĐỀ -->
        <mxCell id="h2_banner" value="&lt;b style='font-size:16px;'&gt;SƠ ĐỒ CẢNH QUAN QUY TRÌNH NGÂN HÀNG LPBANK (PROCESS LANDSCAPE &amp;amp; VALUE CHAIN MAP)&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:12px;color:#cbd5e1;'&gt;Chuẩn hóa theo Khung quy trình ngành Ngân hàng APQC PCF v7.2.2 &amp;amp; Định hướng Tinh gọn Enterprise Architecture&lt;/span&gt;" style="rounded=1;arcSize=8;fillColor=#0f172a;strokeColor=#1e293b;fontColor=#ffffff;align=center;verticalAlign=middle;html=1;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="40" y="25" width="1340" height="60" as="geometry" />
        </mxCell>

        <!-- 1. QUY TRÌNH QUẢN LÝ -->
        <mxCell id="h2_mgmt_box" value="" style="rounded=1;arcSize=8;fillColor=#fef2f2;strokeColor=#dc2626;strokeWidth=1.5;html=1;" vertex="1" parent="1">
          <mxGeometry x="40" y="105" width="1340" height="100" as="geometry" />
        </mxCell>
        <mxCell id="h2_mgmt_title" value="&lt;b style='color:#991b1b;font-size:12px;'&gt;QUY TRÌNH QUẢN LÝ (MANAGEMENT PROCESSES - APQC 1.0, 7.0, 11.0, 12.0)&lt;/b&gt;" style="text;html=1;align=center;verticalAlign=middle;fontColor:#991b1b;" vertex="1" parent="1">
          <mxGeometry x="40" y="107" width="1340" height="24" as="geometry" />
        </mxCell>
        <mxCell id="h2_m1" value="&lt;b style='font-size:12px;'&gt;1.0 Hoạch định Chiến lược&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:10px;color:#64748b;'&gt;Định hướng kinh doanh &amp;amp; Ngân sách&lt;/span&gt;" style="rounded=1;arcSize=10;fillColor=#ffffff;strokeColor=#f87171;strokeWidth=1.2;align=center;verticalAlign=middle;html=1;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="60" y="135" width="300" height="56" as="geometry" />
        </mxCell>
        <mxCell id="h2_m2" value="&lt;b style='font-size:12px;'&gt;11.0 Quản trị Rủi ro &amp;amp; ALM&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:10px;color:#64748b;'&gt;Quản lý thanh khoản, tỷ giá &amp;amp; rủi ro TT&lt;/span&gt;" style="rounded=1;arcSize=10;fillColor=#ffffff;strokeColor=#f87171;strokeWidth=1.2;align=center;verticalAlign=middle;html=1;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="385" y="135" width="300" height="56" as="geometry" />
        </mxCell>
        <mxCell id="h2_m3" value="&lt;b style='font-size:12px;'&gt;12.0 Kiểm toán &amp;amp; Tuân thủ&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:10px;color:#64748b;'&gt;Giám sát NHNN &amp;amp; Kiểm soát nội bộ&lt;/span&gt;" style="rounded=1;arcSize=10;fillColor=#ffffff;strokeColor=#f87171;strokeWidth=1.2;align=center;verticalAlign=middle;html=1;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="710" y="135" width="300" height="56" as="geometry" />
        </mxCell>
        <mxCell id="h2_m4" value="&lt;b style='font-size:12px;'&gt;7.0 Quản trị Thay đổi &amp;amp; Dự án&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:10px;color:#64748b;'&gt;Quản lý danh mục Chuyển đổi số&lt;/span&gt;" style="rounded=1;arcSize=10;fillColor=#ffffff;strokeColor=#f87171;strokeWidth=1.2;align=center;verticalAlign=middle;html=1;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="1035" y="135" width="325" height="56" as="geometry" />
        </mxCell>

        <!-- 2. QUY TRÌNH CỐT LÕI (VALUE CHAIN) -->
        <mxCell id="h2_core_box" value="" style="rounded=1;arcSize=8;fillColor=#eff6ff;strokeColor=#2563eb;strokeWidth=2;html=1;" vertex="1" parent="1">
          <mxGeometry x="40" y="225" width="1340" height="190" as="geometry" />
        </mxCell>
        <mxCell id="h2_core_title" value="&lt;b style='color:#1e40af;font-size:13px;'&gt;QUY TRÌNH CỐT LÕI: CHUỖI GIÁ TRỊ CẤP TÍN DỤNG TOÀN TRÌNH END-TO-END (APQC 3.0, 5.0, 6.0)&lt;/b&gt;" style="text;html=1;align=center;verticalAlign=middle;fontColor:#1e40af;" vertex="1" parent="1">
          <mxGeometry x="40" y="228" width="1340" height="24" as="geometry" />
        </mxCell>

        <!-- INPUT CỦA KHÁCH HÀNG -->
        <mxCell id="h2_inp" value="&lt;b style='font-size:11.5px;color:#0f172a;'&gt;NHU CẦU&lt;br&gt;KHÁCH HÀNG&lt;br&gt;&amp;amp; THỊ TRƯỜNG&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:9.5px;color:#64748b;'&gt;Vốn vay SXKD / Tiêu dùng&lt;/span&gt;" style="shape=note;whiteSpace=wrap;html=1;backgroundOutline=1;darkOpacity=0.05;fillColor=#f1f5f9;strokeColor=#64748b;strokeWidth=1.5;size=16;align=center;verticalAlign=middle;" vertex="1" parent="1">
          <mxGeometry x="55" y="265" width="115" height="125" as="geometry" />
        </mxCell>

        <!-- CÁC BƯỚC VALUE CHAIN -->
        <mxCell id="h2_c1" value="&lt;b style='font-size:11px;'&gt;Phát triển Sản phẩm&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:9.5px;color:#475569;'&gt;Gói tín dụng ưu đãi&lt;br&gt;(APQC 3.0)&lt;/span&gt;" style="rounded=1;arcSize=10;fillColor=#ffffff;strokeColor=#3b82f6;strokeWidth=1.5;html=1;align=center;verticalAlign=middle;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="195" y="290" width="130" height="75" as="geometry" />
        </mxCell>
        <mxCell id="h2_c2" value="&lt;b style='font-size:11px;'&gt;Tiếp thị &amp;amp; Bán hàng&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:9.5px;color:#475569;'&gt;Tiếp cận KH, tư vấn&lt;br&gt;(APQC 3.5)&lt;/span&gt;" style="rounded=1;arcSize=10;fillColor=#ffffff;strokeColor=#3b82f6;strokeWidth=1.5;html=1;align=center;verticalAlign=middle;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="350" y="290" width="130" height="75" as="geometry" />
        </mxCell>
        <mxCell id="h2_c3" value="&lt;b style='font-size:11px;'&gt;Tiếp nhận &amp;amp; Khởi tạo&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:9.5px;color:#475569;'&gt;Nhập hồ sơ trên LOS&lt;br&gt;(APQC 5.3.1)&lt;/span&gt;" style="rounded=1;arcSize=10;fillColor=#ffffff;strokeColor=#3b82f6;strokeWidth=1.5;html=1;align=center;verticalAlign=middle;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="505" y="290" width="135" height="75" as="geometry" />
        </mxCell>
        <mxCell id="h2_c4" value="&lt;b style='font-size:11px;'&gt;Thẩm định &amp;amp; Duyệt&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:9.5px;color:#475569;'&gt;Xếp hạng tín dụng&lt;br&gt;&amp;amp; Duyệt hạn mức&lt;/span&gt;" style="rounded=1;arcSize=10;fillColor=#ffffff;strokeColor=#3b82f6;strokeWidth=1.5;html=1;align=center;verticalAlign=middle;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="665" y="290" width="135" height="75" as="geometry" />
        </mxCell>

        <!-- HIGHLIGHT TRỌNG TÂM -->
        <mxCell id="h2_c5_focus" value="&lt;div style='font-size:10px;color:#166534;font-weight:bold;margin-bottom:2px;'&gt;★ QUY TRÌNH TRỌNG TÂM ★&lt;/div&gt;&lt;b style='font-size:12px;color:#14532d;'&gt;TRIỂN KHAI TÍN DỤNG&lt;br&gt;&amp;amp; GIẢI NGÂN VỐN VAY&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:10px;color:#166534;'&gt;(APQC 5.3.1 - 13961)&lt;/span&gt;" style="rounded=1;arcSize=12;fillColor=#dcfce7;strokeColor=#16a34a;strokeWidth=2.5;html=1;align=center;verticalAlign=middle;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="825" y="275" width="180" height="105" as="geometry" />
        </mxCell>

        <mxCell id="h2_c6" value="&lt;b style='font-size:11px;'&gt;Quản lý Sau vay&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:9.5px;color:#475569;'&gt;Giám sát dòng tiền&lt;br&gt;&amp;amp; Thu hồi gốc lãi&lt;/span&gt;" style="rounded=1;arcSize=10;fillColor=#ffffff;strokeColor=#3b82f6;strokeWidth=1.5;html=1;align=center;verticalAlign=middle;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="1030" y="290" width="130" height="75" as="geometry" />
        </mxCell>

        <!-- OUTPUT: GIÁ TRỊ KHÁCH HÀNG -->
        <mxCell id="h2_out" value="&lt;b style='font-size:11.5px;color:#14532d;'&gt;GIÁ TRỊ&lt;br&gt;MANG LẠI CHO&lt;br&gt;KHÁCH HÀNG&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:9.5px;color:#15803d;'&gt;Vốn vay kịp thời,&lt;br&gt;Hài lòng vượt trội&lt;/span&gt;" style="shape=note;whiteSpace=wrap;html=1;backgroundOutline=1;darkOpacity=0.05;fillColor=#ecfdf5;strokeColor=#10b981;strokeWidth=1.5;size=16;align=center;verticalAlign=middle;" vertex="1" parent="1">
          <mxGeometry x="1245" y="265" width="120" height="125" as="geometry" />
        </mxCell>

        <!-- CONNECTORS -->
        <mxCell id="h2_a_inp" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;strokeColor=#64748b;strokeWidth=2;" edge="1" parent="1" source="h2_inp" target="h2_c1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="h2_a1" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;strokeColor=#2563eb;strokeWidth=2;" edge="1" parent="1" source="h2_c1" target="h2_c2">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="h2_a2" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;strokeColor=#2563eb;strokeWidth=2;" edge="1" parent="1" source="h2_c2" target="h2_c3">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="h2_a3" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;strokeColor=#2563eb;strokeWidth=2;" edge="1" parent="1" source="h2_c3" target="h2_c4">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="h2_a4" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;strokeColor=#16a34a;strokeWidth=2.5;" edge="1" parent="1" source="h2_c4" target="h2_c5_focus">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="h2_a5" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;strokeColor=#2563eb;strokeWidth=2;" edge="1" parent="1" source="h2_c5_focus" target="h2_c6">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="h2_a_out" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;strokeColor=#10b981;strokeWidth=2;" edge="1" parent="1" source="h2_c6" target="h2_out">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- 3. QUY TRÌNH HỖ TRỢ -->
        <mxCell id="h2_sup_box" value="" style="rounded=1;arcSize=8;fillColor=#f8fafc;strokeColor=#64748b;strokeWidth=1.5;html=1;" vertex="1" parent="1">
          <mxGeometry x="40" y="435" width="1340" height="100" as="geometry" />
        </mxCell>
        <mxCell id="h2_sup_title" value="&lt;b style='color:#334155;font-size:12px;'&gt;QUY TRÌNH HỖ TRỢ (SUPPORT PROCESSES - APQC 4.0, 8.0, 9.0, 10.0)&lt;/b&gt;" style="text;html=1;align=center;verticalAlign=middle;fontColor:#334155;" vertex="1" parent="1">
          <mxGeometry x="40" y="437" width="1340" height="24" as="geometry" />
        </mxCell>
        <mxCell id="h2_s1" value="&lt;b style='font-size:12px;'&gt;8.0 Quản trị CNTT &amp;amp; Core T24&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:10px;color:#64748b;'&gt;Hạ tầng hệ thống, Smart BPM, LOS&lt;/span&gt;" style="rounded=1;arcSize=10;fillColor=#ffffff;strokeColor=#94a3b8;strokeWidth=1.2;align=center;verticalAlign=middle;html=1;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="60" y="465" width="245" height="56" as="geometry" />
        </mxCell>
        <mxCell id="h2_s2" value="&lt;b style='font-size:12px;'&gt;4.0 Quản trị Nhân sự &amp;amp; Đào tạo&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:10px;color:#64748b;'&gt;Phát triển năng lực cán bộ tín dụng&lt;/span&gt;" style="rounded=1;arcSize=10;fillColor=#ffffff;strokeColor=#94a3b8;strokeWidth=1.2;align=center;verticalAlign=middle;html=1;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="325" y="465" width="245" height="56" as="geometry" />
        </mxCell>
        <mxCell id="h2_s3" value="&lt;b style='font-size:12px;'&gt;9.0 Tài chính, Kế toán &amp;amp; Thuế&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:10px;color:#64748b;'&gt;Hạch toán kế toán, quản trị nguồn vốn&lt;/span&gt;" style="rounded=1;arcSize=10;fillColor=#ffffff;strokeColor=#94a3b8;strokeWidth=1.2;align=center;verticalAlign=middle;html=1;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="590" y="465" width="245" height="56" as="geometry" />
        </mxCell>
        <mxCell id="h2_s4" value="&lt;b style='font-size:12px;'&gt;10.0 Quản trị Tài sản &amp;amp; ECM&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:10px;color:#64748b;'&gt;Kho tài sản đảm bảo &amp;amp; Lưu trữ hồ sơ&lt;/span&gt;" style="rounded=1;arcSize=10;fillColor=#ffffff;strokeColor=#94a3b8;strokeWidth=1.2;align=center;verticalAlign=middle;html=1;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="855" y="465" width="245" height="56" as="geometry" />
        </mxCell>
        <mxCell id="h2_s5" value="&lt;b style='font-size:12px;'&gt;An toàn Thông tin &amp;amp; Bảo mật&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:10px;color:#64748b;'&gt;Xác thực số, phòng chống gian lận&lt;/span&gt;" style="rounded=1;arcSize=10;fillColor=#ffffff;strokeColor=#94a3b8;strokeWidth=1.2;align=center;verticalAlign=middle;html=1;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="1120" y="465" width="240" height="56" as="geometry" />
        </mxCell>
    """
    return wrap_mxfile("Hinh2_Process_Landscape_LPBank", cells, 1420, 580)

# ==============================================================================
# HÌNH 3: SƠ ĐỒ QUY TRÌNH HIỆN TRẠNG AS-IS (CHUẨN BPMN 2.0 ENTERPRISE SWIMLANE)
# ==============================================================================
def generate_hinh3():
    cells = """
        <!-- BANNER TIÊU ĐỀ SƠ ĐỒ -->
        <mxCell id="h3_banner" value="&lt;b style='font-size:16px;'&gt;QUY TRÌNH TRIỂN KHAI TÍN DỤNG VÀ GIẢI NGÂN VỐN VAY - HIỆN TRẠNG (AS-IS)&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:12px;color:#cbd5e1;'&gt;Ký hiệu chuẩn BPMN 2.0 | Minh họa 3 Điểm nghẽn nghiêm trọng (Bottlenecks) &amp;amp; 2 Vòng lặp xử lý lại (Rework Loops)&lt;/span&gt;" style="rounded=1;arcSize=8;fillColor=#0f172a;strokeColor=#1e293b;fontColor=#ffffff;align=center;verticalAlign=middle;html=1;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="40" y="20" width="1360" height="55" as="geometry" />
        </mxCell>

        <!-- SWIMLANE BACKGROUND CONTAINER (POOL) -->
        <!-- Lane 1: RM / ĐVKD -->
        <mxCell id="h3_lane1_hdr" value="&lt;b style='font-size:11px;'&gt;ĐƠN VỊ KINH DOANH&lt;/b&gt;&lt;br&gt;Chuyên viên QLKH (RM)" style="rounded=0;fillColor=#e2e8f0;strokeColor=#94a3b8;strokeWidth=1;fontColor=#0f172a;align=center;verticalAlign=middle;html=1;" vertex="1" parent="1">
          <mxGeometry x="40" y="90" width="180" height="135" as="geometry" />
        </mxCell>
        <mxCell id="h3_lane1_body" value="" style="rounded=0;fillColor=#ffffff;strokeColor=#cbd5e1;strokeWidth=1;html=1;" vertex="1" parent="1">
          <mxGeometry x="220" y="90" width="1180" height="135" as="geometry" />
        </mxCell>

        <!-- Lane 2: Kiểm soát Chi nhánh -->
        <mxCell id="h3_lane2_hdr" value="&lt;b style='font-size:11px;'&gt;KIỂM SOÁT CHI NHÁNH&lt;/b&gt;&lt;br&gt;Trưởng phòng / Kiểm soát viên" style="rounded=0;fillColor=#f1f5f9;strokeColor=#94a3b8;strokeWidth=1;fontColor=#0f172a;align=center;verticalAlign=middle;html=1;" vertex="1" parent="1">
          <mxGeometry x="40" y="225" width="180" height="130" as="geometry" />
        </mxCell>
        <mxCell id="h3_lane2_body" value="" style="rounded=0;fillColor=#fafaf9;strokeColor=#cbd5e1;strokeWidth=1;html=1;" vertex="1" parent="1">
          <mxGeometry x="220" y="225" width="1180" height="130" as="geometry" />
        </mxCell>

        <!-- Lane 3: CSU -->
        <mxCell id="h3_lane3_hdr" value="&lt;b style='font-size:11px;'&gt;HỖ TRỢ TÍN DỤNG (CSU)&lt;/b&gt;&lt;br&gt;Chuyên viên Xử lý Hồ sơ TD" style="rounded=0;fillColor=#e2e8f0;strokeColor=#94a3b8;strokeWidth=1;fontColor=#0f172a;align=center;verticalAlign=middle;html=1;" vertex="1" parent="1">
          <mxGeometry x="40" y="355" width="180" height="145" as="geometry" />
        </mxCell>
        <mxCell id="h3_lane3_body" value="" style="rounded=0;fillColor=#ffffff;strokeColor=#cbd5e1;strokeWidth=1;html=1;" vertex="1" parent="1">
          <mxGeometry x="220" y="355" width="1180" height="145" as="geometry" />
        </mxCell>

        <!-- Lane 4: Cấp Phê duyệt & Core T24 -->
        <mxCell id="h3_lane4_hdr" value="&lt;b style='font-size:11px;'&gt;CẤP PHÊ DUYỆT &amp;amp; CORE T24&lt;/b&gt;&lt;br&gt;Lãnh đạo phê duyệt / Kế toán GD" style="rounded=0;fillColor=#f1f5f9;strokeColor=#94a3b8;strokeWidth=1;fontColor=#0f172a;align=center;verticalAlign=middle;html=1;" vertex="1" parent="1">
          <mxGeometry x="40" y="500" width="180" height="140" as="geometry" />
        </mxCell>
        <mxCell id="h3_lane4_body" value="" style="rounded=0;fillColor=#fafaf9;strokeColor=#cbd5e1;strokeWidth=1;html=1;" vertex="1" parent="1">
          <mxGeometry x="220" y="500" width="1180" height="140" as="geometry" />
        </mxCell>

        <!-- ==================== BPMN ELEMENTS TRONG LANE 1 ==================== -->
        <!-- Start Event: Standard BPMN Green Circle -->
        <mxCell id="h3_start" value="" style="ellipse;whiteSpace=wrap;html=1;aspect=fixed;fillColor=#ecfdf5;strokeColor=#10b981;strokeWidth=2;" vertex="1" parent="1">
          <mxGeometry x="250" y="135" width="40" height="40" as="geometry" />
        </mxCell>
        <mxCell id="h3_lbl_start" value="&lt;span style='font-size:10px;color:#0f766e;font-weight:bold;'&gt;Nhận phương án&lt;br&gt;từ LOS&lt;/span&gt;" style="text;html=1;align=center;verticalAlign=middle;" vertex="1" parent="1">
          <mxGeometry x="225" y="177" width="90" height="30" as="geometry" />
        </mxCell>

        <!-- Task 1: Khởi tạo phương án -->
        <mxCell id="h3_t1" value="&lt;b style='font-size:11px;'&gt;[1] Khởi tạo phương án&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:10px;color:#475569;'&gt;Tải lên hồ sơ, chứng từ giải ngân&lt;br&gt;qua giao diện LOS&lt;/span&gt;" style="rounded=1;arcSize=15;fillColor=#ffffff;strokeColor=#475569;strokeWidth=1.2;align=center;verticalAlign=middle;html=1;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="330" y="125" width="150" height="60" as="geometry" />
        </mxCell>

        <!-- Task 2: Nhập thông tin & First check -->
        <mxCell id="h3_t2" value="&lt;b style='font-size:11px;'&gt;[2] Nhập thông tin GN&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:10px;color:#475569;'&gt;Nhập tài khoản, số tiền&lt;br&gt;&lt;b style='color:#dc2626;'&gt;Thực hiện First Check lần 1&lt;/b&gt;&lt;/span&gt;" style="rounded=1;arcSize=15;fillColor=#ffffff;strokeColor=#475569;strokeWidth=1.2;align=center;verticalAlign=middle;html=1;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="520" y="125" width="160" height="60" as="geometry" />
        </mxCell>

        <!-- ==================== BPMN ELEMENTS TRONG LANE 2 ==================== -->
        <!-- Task 3: Kiểm soát chi nhánh (KÈM BADGE BOTTLENECK #1) -->
        <mxCell id="h3_t3" value="&lt;div style='display:inline-block;background-color:#dc2626;color:#ffffff;font-size:8.5px;font-weight:bold;padding:1px 6px;border-radius:4px;margin-bottom:2px;'&gt;BOTTLENECK #1: KIỂM TRA TRÙNG LẶP 3 CẤP&lt;/div&gt;&lt;br&gt;&lt;b style='font-size:11px;'&gt;[3] Kiểm soát đề xuất&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:10px;color:#b91c1c;'&gt;⚠ Kiểm tra First Check lần 2 (Trùng lặp nội dung)&lt;/span&gt;" style="rounded=1;arcSize=15;fillColor=#fef2f2;strokeColor=#ef4444;strokeWidth=1.5;align=center;verticalAlign=middle;html=1;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="490" y="255" width="220" height="70" as="geometry" />
        </mxCell>

        <!-- Gateway 1: Hồ sơ hợp lệ? -->
        <mxCell id="h3_gw1" value="&lt;b style='font-size:16px;color:#d97706;'&gt;✕&lt;/b&gt;" style="rhombus;whiteSpace=wrap;html=1;aspect=fixed;fillColor=#ffffff;strokeColor=#d97706;strokeWidth=2;" vertex="1" parent="1">
          <mxGeometry x="755" y="265" width="50" height="50" as="geometry" />
        </mxCell>
        <mxCell id="h3_lbl_gw1" value="&lt;span style='font-size:10px;color:#92400e;font-weight:bold;font-style:italic;'&gt;Hồ sơ hợp lệ?&lt;/span&gt;" style="text;html=1;align=center;verticalAlign=middle;" vertex="1" parent="1">
          <mxGeometry x="740" y="235" width="80" height="22" as="geometry" />
        </mxCell>

        <!-- ==================== BPMN ELEMENTS TRONG LANE 3 ==================== -->
        <!-- Task 4: Thẩm tra điều kiện tại CSU (KÈM BADGE BOTTLENECK #2) -->
        <mxCell id="h3_t4" value="&lt;div style='display:inline-block;background-color:#dc2626;color:#ffffff;font-size:8.5px;font-weight:bold;padding:1px 6px;border-radius:4px;margin-bottom:2px;'&gt;BOTTLENECK #2: NHẬP LIỆU LẠI THỦ CÔNG&lt;/div&gt;&lt;br&gt;&lt;b style='font-size:11px;'&gt;[4] Thẩm tra lại điều kiện&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:10px;color:#b91c1c;'&gt;⚠ Kiểm tra First Check lần 3, nhập lại biểu lãi suất&lt;/span&gt;" style="rounded=1;arcSize=15;fillColor=#fef2f2;strokeColor=#ef4444;strokeWidth=1.5;align=center;verticalAlign=middle;html=1;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="670" y="390" width="220" height="70" as="geometry" />
        </mxCell>

        <!-- Task 5: Lập báo cáo kiểm soát CSU -->
        <mxCell id="h3_t5" value="&lt;b style='font-size:11px;'&gt;[5] Lập Báo cáo kiểm soát&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:10px;color:#475569;'&gt;Soạn tờ trình kiểm soát,&lt;br&gt;Đề xuất phê duyệt giải ngân&lt;/span&gt;" style="rounded=1;arcSize=15;fillColor=#ffffff;strokeColor=#475569;strokeWidth=1.2;align=center;verticalAlign=middle;html=1;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="930" y="390" width="160" height="70" as="geometry" />
        </mxCell>

        <!-- Task 8: In ký hồ sơ bản cứng (KÈM BADGE LÃNG PHÍ NVA) -->
        <mxCell id="h3_t8" value="&lt;div style='display:inline-block;background-color:#ea580c;color:#ffffff;font-size:8.5px;font-weight:bold;padding:1px 6px;border-radius:4px;margin-bottom:2px;'&gt;LÃNG PHÍ NVA: IN ẤN THỦ CÔNG&lt;/div&gt;&lt;br&gt;&lt;b style='font-size:11px;'&gt;[8] In ấn &amp;amp; Ký hồ sơ giấy&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:10px;color:#c2410c;'&gt;Trình ký mực &amp;amp; Đóng dấu cơ học&lt;/span&gt;" style="rounded=1;arcSize=15;fillColor=#fff7ed;strokeColor=#ea580c;strokeWidth=1.5;align=center;verticalAlign=middle;html=1;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="1140" y="390" width="180" height="70" as="geometry" />
        </mxCell>

        <!-- ==================== BPMN ELEMENTS TRONG LANE 4 ==================== -->
        <!-- Task 6: Cấp thẩm quyền phê duyệt -->
        <mxCell id="h3_t6" value="&lt;b style='font-size:11px;'&gt;[6] Kiểm soát viên duyệt&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:10px;color:#475569;'&gt;Kiểm tra hạn mức, thẩm quyền,&lt;br&gt;Ký duyệt lệnh giải ngân&lt;/span&gt;" style="rounded=1;arcSize=15;fillColor=#ffffff;strokeColor=#475569;strokeWidth=1.2;align=center;verticalAlign=middle;html=1;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="930" y="535" width="160" height="70" as="geometry" />
        </mxCell>

        <!-- Gateway 2: Phê duyệt đạt? -->
        <mxCell id="h3_gw2" value="&lt;b style='font-size:16px;color:#d97706;'&gt;✕&lt;/b&gt;" style="rhombus;whiteSpace=wrap;html=1;aspect=fixed;fillColor=#ffffff;strokeColor=#d97706;strokeWidth=2;" vertex="1" parent="1">
          <mxGeometry x="1125" y="545" width="50" height="50" as="geometry" />
        </mxCell>
        <mxCell id="h3_lbl_gw2" value="&lt;span style='font-size:10px;color:#92400e;font-weight:bold;font-style:italic;'&gt;Duyệt đạt?&lt;/span&gt;" style="text;html=1;align=center;verticalAlign=middle;" vertex="1" parent="1">
          <mxGeometry x="1110" y="518" width="80" height="22" as="geometry" />
        </mxCell>

        <!-- Task 7: Hạch toán Core T24 -->
        <mxCell id="h3_t7" value="&lt;b style='font-size:11px;'&gt;[7] Hạch toán Core T24&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:10px;color:#15803d;'&gt;Kế toán giao dịch hạch toán,&lt;br&gt;Đẩy lệnh chuyển tiền liên NH&lt;/span&gt;" style="rounded=1;arcSize=15;fillColor=#f0fdf4;strokeColor=#16a34a;strokeWidth=1.5;align=center;verticalAlign=middle;html=1;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="1235" y="535" width="155" height="70" as="geometry" />
        </mxCell>

        <!-- End Event: BPMN Double Circle Terminate -->
        <mxCell id="h3_end_outer" value="" style="ellipse;whiteSpace=wrap;html=1;aspect=fixed;fillColor=#fee2e2;strokeColor=#ef4444;strokeWidth=3;" vertex="1" parent="1">
          <mxGeometry x="1355" y="270" width="40" height="40" as="geometry" />
        </mxCell>
        <mxCell id="h3_end_inner" value="" style="ellipse;whiteSpace=wrap;html=1;aspect=fixed;fillColor=#dc2626;strokeColor=none;" vertex="1" parent="1">
          <mxGeometry x="1365" y="280" width="20" height="20" as="geometry" />
        </mxCell>
        <mxCell id="h3_lbl_end" value="&lt;span style='font-size:10px;color:#b91c1c;font-weight:bold;'&gt;Giải ngân&lt;br&gt;hoàn tất&lt;/span&gt;" style="text;html=1;align=center;verticalAlign=middle;" vertex="1" parent="1">
          <mxGeometry x="1340" y="315" width="70" height="26" as="geometry" />
        </mxCell>

        <!-- ==================== SEQUENCE FLOWS & REWORK LOOPS ==================== -->
        <mxCell id="h3_flow1" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;strokeColor=#1e293b;strokeWidth=1.5;" edge="1" parent="1" source="h3_start" target="h3_t1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="h3_flow2" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;strokeColor=#1e293b;strokeWidth=1.5;" edge="1" parent="1" source="h3_t1" target="h3_t2">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="h3_flow3" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;strokeColor=#1e293b;strokeWidth=1.5;" edge="1" parent="1" source="h3_t2" target="h3_t3">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="h3_flow4" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;strokeColor=#1e293b;strokeWidth=1.5;" edge="1" parent="1" source="h3_t3" target="h3_gw1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Rẽ nhánh Hợp lệ từ GW1 sang Task 4 -->
        <mxCell id="h3_flow_gw1_ok" value="&lt;span style='font-size:10px;color:#15803d;background-color:#ffffff;padding:2px;'&gt;Hợp lệ&lt;/span&gt;" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;strokeColor=#15803d;strokeWidth=1.5;" edge="1" parent="1" source="h3_gw1" target="h3_t4">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- VÒNG LẶP 1: REWORK LOOP 1 (Thiếu hồ sơ từ GW1 quay lại RM) -->
        <mxCell id="h3_rework1" value="&lt;b style='font-size:10px;color:#dc2626;background-color:#ffffff;padding:2px;'&gt;Thiếu hồ sơ / Sai sót (Vòng lặp 1 - Rework)&lt;/b&gt;" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;dashed=1;strokeColor=#dc2626;strokeWidth=2;" edge="1" parent="1" source="h3_gw1" target="h3_t1">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="780" y="100" />
              <mxPoint x="405" y="100" />
            </Array>
          </mxGeometry>
        </mxCell>

        <mxCell id="h3_flow5" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;strokeColor=#1e293b;strokeWidth=1.5;" edge="1" parent="1" source="h3_t4" target="h3_t5">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="h3_flow6" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;strokeColor=#1e293b;strokeWidth=1.5;" edge="1" parent="1" source="h3_t5" target="h3_t6">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="h3_flow7" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;strokeColor=#1e293b;strokeWidth=1.5;" edge="1" parent="1" source="h3_t6" target="h3_gw2">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- VÒNG LẶP 2: REWORK LOOP 2 (Yêu cầu sửa đổi từ Lãnh đạo quay lại CSU) -->
        <mxCell id="h3_rework2" value="&lt;b style='font-size:10px;color:#dc2626;background-color:#ffffff;padding:2px;'&gt;Yêu cầu sửa đổi tờ trình (Vòng lặp 2)&lt;/b&gt;" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;dashed=1;strokeColor=#dc2626;strokeWidth=2;" edge="1" parent="1" source="h3_gw2" target="h3_t4">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="1150" y="475" />
              <mxPoint x="780" y="475" />
            </Array>
          </mxGeometry>
        </mxCell>

        <!-- Rẽ nhánh Phê duyệt đạt từ GW2 sang Task 7 -->
        <mxCell id="h3_flow_gw2_ok" value="&lt;span style='font-size:10px;color:#15803d;background-color:#ffffff;padding:2px;'&gt;Chấp thuận&lt;/span&gt;" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;strokeColor=#15803d;strokeWidth=1.5;" edge="1" parent="1" source="h3_gw2" target="h3_t7">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Hạch toán T24 xong sang In ký hồ sơ giấy Task 8 -->
        <mxCell id="h3_flow8" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;strokeColor=#1e293b;strokeWidth=1.5;" edge="1" parent="1" source="h3_t7" target="h3_t8">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="1312" y="480" />
              <mxPoint x="1230" y="480" />
            </Array>
          </mxGeometry>
        </mxCell>

        <!-- Từ Task 8 đến End Event -->
        <mxCell id="h3_flow_end" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;strokeColor=#1e293b;strokeWidth=1.5;" edge="1" parent="1" source="h3_t8" target="h3_end_outer">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="1230" y="290" />
            </Array>
          </mxGeometry>
        </mxCell>
    """
    return wrap_mxfile("Hinh3_Quy_trinh_Hien_trang_AsIs_LPBank", cells, 1440, 680)

# ==============================================================================
# HÌNH 4: SƠ ĐỒ QUY TRÌNH TƯƠNG LAI TO-BE (CHUẨN BPMN 2.0 NGÂN HÀNG SỐ STP)
# ==============================================================================
def generate_hinh4():
    cells = """
        <!-- BANNER TIÊU ĐỀ SƠ ĐỒ -->
        <mxCell id="h4_banner" value="&lt;b style='font-size:16px;'&gt;QUY TRÌNH TRIỂN KHAI TÍN DỤNG VÀ GIẢI NGÂN VỐN VAY - TƯƠNG LAI (TO-BE)&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:12px;color:#cbd5e1;'&gt;Ký hiệu chuẩn BPMN 2.0 | Kiến trúc Smart BPM Orchestrator, Ký số SmartCA &amp;amp; Xử lý giao dịch thẳng STP tự động 100%&lt;/span&gt;" style="rounded=1;arcSize=8;fillColor=#0f172a;strokeColor=#1e293b;fontColor=#ffffff;align=center;verticalAlign=middle;html=1;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="40" y="20" width="1380" height="55" as="geometry" />
        </mxCell>

        <!-- SWIMLANE BACKGROUND CONTAINER (POOL) -->
        <!-- Lane 1: Khách hàng (Mobile Banking / Web) -->
        <mxCell id="h4_lane1_hdr" value="&lt;b style='font-size:11px;'&gt;KHÁCH HÀNG&lt;/b&gt;&lt;br&gt;Mobile App / LPBank Web" style="rounded=0;fillColor=#e2e8f0;strokeColor=#94a3b8;strokeWidth=1;fontColor=#0f172a;align=center;verticalAlign=middle;html=1;" vertex="1" parent="1">
          <mxGeometry x="40" y="90" width="180" height="135" as="geometry" />
        </mxCell>
        <mxCell id="h4_lane1_body" value="" style="rounded=0;fillColor=#ffffff;strokeColor=#cbd5e1;strokeWidth=1;html=1;" vertex="1" parent="1">
          <mxGeometry x="220" y="90" width="1200" height="135" as="geometry" />
        </mxCell>

        <!-- Lane 2: Chuyên viên Quan hệ Khách hàng (RM) -->
        <mxCell id="h4_lane2_hdr" value="&lt;b style='font-size:11px;'&gt;CHUYÊN VIÊN QLKH (RM)&lt;/b&gt;&lt;br&gt;Đơn vị Kinh doanh Chi nhánh" style="rounded=0;fillColor=#f1f5f9;strokeColor=#94a3b8;strokeWidth=1;fontColor=#0f172a;align=center;verticalAlign=middle;html=1;" vertex="1" parent="1">
          <mxGeometry x="40" y="225" width="180" height="130" as="geometry" />
        </mxCell>
        <mxCell id="h4_lane2_body" value="" style="rounded=0;fillColor=#fafaf9;strokeColor=#cbd5e1;strokeWidth=1;html=1;" vertex="1" parent="1">
          <mxGeometry x="220" y="225" width="1200" height="130" as="geometry" />
        </mxCell>

        <!-- Lane 3: Kiểm soát viên & Quản trị Rủi ro -->
        <mxCell id="h4_lane3_hdr" value="&lt;b style='font-size:11px;'&gt;KIỂM SOÁT VIÊN PHÊ DUYỆT&lt;/b&gt;&lt;br&gt;Phê duyệt rủi ro theo hạn mức" style="rounded=0;fillColor=#e2e8f0;strokeColor=#94a3b8;strokeWidth=1;fontColor=#0f172a;align=center;verticalAlign=middle;html=1;" vertex="1" parent="1">
          <mxGeometry x="40" y="355" width="180" height="130" as="geometry" />
        </mxCell>
        <mxCell id="h4_lane3_body" value="" style="rounded=0;fillColor=#ffffff;strokeColor=#cbd5e1;strokeWidth=1;html=1;" vertex="1" parent="1">
          <mxGeometry x="220" y="355" width="1200" height="130" as="geometry" />
        </mxCell>

        <!-- Lane 4: Hệ thống tự động Smart BPM & Core T24 -->
        <mxCell id="h4_lane4_hdr" value="&lt;b style='font-size:11px;color:#1e40af;'&gt;SMART BPM &amp;amp; CORE T24&lt;/b&gt;&lt;br&gt;Hệ thống tự động hóa trung tâm" style="rounded=0;fillColor=#eff6ff;strokeColor=#93c5fd;strokeWidth=1;fontColor=#1e40af;align=center;verticalAlign=middle;html=1;" vertex="1" parent="1">
          <mxGeometry x="40" y="485" width="180" height="155" as="geometry" />
        </mxCell>
        <mxCell id="h4_lane4_body" value="" style="rounded=0;fillColor=#f8fafc;strokeColor=#cbd5e1;strokeWidth=1;html=1;" vertex="1" parent="1">
          <mxGeometry x="220" y="485" width="1200" height="155" as="geometry" />
        </mxCell>

        <!-- ==================== BPMN ELEMENTS TRONG LANE 4 ==================== -->
        <!-- Start Event: Standard BPMN Green Circle -->
        <mxCell id="h4_start" value="" style="ellipse;whiteSpace=wrap;html=1;aspect=fixed;fillColor=#ecfdf5;strokeColor=#10b981;strokeWidth=2;" vertex="1" parent="1">
          <mxGeometry x="245" y="540" width="40" height="40" as="geometry" />
        </mxCell>
        <mxCell id="h4_lbl_start" value="&lt;span style='font-size:10px;color:#0f766e;font-weight:bold;'&gt;Nhận hồ sơ từ LOS&lt;br&gt;(Correlation ID)&lt;/span&gt;" style="text;html=1;align=center;verticalAlign=middle;" vertex="1" parent="1">
          <mxGeometry x="215" y="583" width="100" height="30" as="geometry" />
        </mxCell>

        <!-- Task 1 (Service Task): Tự động Pre-check Rule Engine -->
        <mxCell id="h4_t1" value="&lt;div style='font-size:9.5px;color:#1e40af;font-weight:bold;margin-bottom:2px;'&gt;⚙ SERVICE TASK (AUTOMATED)&lt;/div&gt;&lt;b style='font-size:11px;'&gt;[1] Tự động Pre-check Rule Engine&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:10px;color:#334155;'&gt;Khóa trường nguồn, kiểm tra hạn mức&lt;br&gt;Đối chiếu AML &amp;amp; Danh sách đen tập trung&lt;/span&gt;" style="rounded=1;arcSize=15;fillColor=#ffffff;strokeColor=#2563eb;strokeWidth=2;align=center;verticalAlign=middle;html=1;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="330" y="525" width="210" height="70" as="geometry" />
        </mxCell>

        <!-- Gateway 1: Phân luồng rủi ro -->
        <mxCell id="h4_gw1" value="&lt;b style='font-size:16px;color:#d97706;'&gt;✕&lt;/b&gt;" style="rhombus;whiteSpace=wrap;html=1;aspect=fixed;fillColor=#ffffff;strokeColor=#d97706;strokeWidth=2;" vertex="1" parent="1">
          <mxGeometry x="560" y="535" width="50" height="50" as="geometry" />
        </mxCell>
        <mxCell id="h4_lbl_gw1" value="&lt;span style='font-size:10px;color:#92400e;font-weight:bold;font-style:italic;'&gt;Phân luồng&lt;br&gt;xử lý?&lt;/span&gt;" style="text;html=1;align=center;verticalAlign=middle;" vertex="1" parent="1">
          <mxGeometry x="545" y="498" width="80" height="28" as="geometry" />
        </mxCell>

        <!-- Task 2 (User Task): RM Xác nhận phương án (Món lớn/Ngoại lệ) -->
        <mxCell id="h4_t2" value="&lt;div style='font-size:9.5px;color:#475569;font-weight:bold;margin-bottom:2px;'&gt;👤 USER TASK (ĐVKD)&lt;/div&gt;&lt;b style='font-size:11px;'&gt;[2] RM Xác nhận Phương án&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:10px;color:#475569;'&gt;Khóa dữ liệu, bổ sung lịch giải ngân&lt;br&gt;(Chỉ kích hoạt khi món vay lớn)&lt;/span&gt;" style="rounded=1;arcSize=15;fillColor=#ffffff;strokeColor=#475569;strokeWidth=1.2;align=center;verticalAlign=middle;html=1;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="510" y="260" width="180" height="60" as="geometry" />
        </mxCell>

        <!-- Task 3 (User Task): Phê duyệt rủi ro tinh gọn -->
        <mxCell id="h4_t3" value="&lt;div style='font-size:9.5px;color:#475569;font-weight:bold;margin-bottom:2px;'&gt;👤 USER TASK (APPROVAL)&lt;/div&gt;&lt;b style='font-size:11px;'&gt;[3] Phê duyệt Rủi ro Tinh gọn&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:10px;color:#475569;'&gt;SLA cam kết ≤ 2 giờ,&lt;br&gt;Tra cứu Reason Code chuẩn hóa&lt;/span&gt;" style="rounded=1;arcSize=15;fillColor=#ffffff;strokeColor=#475569;strokeWidth=1.2;align=center;verticalAlign=middle;html=1;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="720" y="390" width="180" height="60" as="geometry" />
        </mxCell>

        <!-- ==================== BPMN ELEMENTS TRONG LANE 1 ==================== -->
        <!-- Task 4 (User Task trên App): Ký số SmartCA -->
        <mxCell id="h4_t4_sign" value="&lt;div style='font-size:9.5px;color:#2563eb;font-weight:bold;margin-bottom:2px;'&gt;📱 KHÁCH HÀNG (MOBILE / WEB)&lt;/div&gt;&lt;b style='font-size:11.5px;color:#1e40af;'&gt;[4] KÝ SỐ TỪ XA QUA SMARTCA&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:10px;color:#334155;'&gt;Ký hợp đồng tín dụng &amp;amp; khế ước điện tử,&lt;br&gt;Không in một tờ giấy nào (100% Paperless)&lt;/span&gt;" style="rounded=1;arcSize=15;fillColor=#eff6ff;strokeColor=#3b82f6;strokeWidth=2;align=center;verticalAlign=middle;html=1;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="720" y="125" width="220" height="70" as="geometry" />
        </mxCell>

        <!-- Task 5 (Service Task STP): Tự động Hạch toán Core T24 -->
        <mxCell id="h4_t5_stp" value="&lt;div style='font-size:9.5px;color:#15803d;font-weight:bold;margin-bottom:2px;'&gt;⚡ LUỒNG THẲNG STP TỰ ĐỘNG 100%&lt;/div&gt;&lt;b style='font-size:11px;color:#14532d;'&gt;[5] Tự động Hạch toán &amp;amp; Chuyển tiền&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:10px;color:#166534;'&gt;Cơ chế Idempotency Key &amp;amp; Circuit Breaker&lt;br&gt;Hạch toán thẳng vào Core T24 tức thì&lt;/span&gt;" style="rounded=1;arcSize=15;fillColor=#dcfce7;strokeColor=#16a34a;strokeWidth=2.5;align=center;verticalAlign=middle;html=1;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="950" y="520" width="215" height="75" as="geometry" />
        </mxCell>

        <!-- Task 6 (Customer Milestone): Nhận tiền & Đánh giá CSAT -->
        <mxCell id="h4_t6_csat" value="&lt;div style='font-size:9.5px;color:#15803d;font-weight:bold;margin-bottom:2px;'&gt;★ ĐIỂM CHẠM KHÁCH HÀNG&lt;/div&gt;&lt;b style='font-size:11px;color:#14532d;'&gt;[6] Nhận tiền &amp;amp; Đánh giá CSAT&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:10px;color:#166534;'&gt;Tài khoản nổi tiền ngay,&lt;br&gt;Chấm điểm độ hài lòng 5 sao trên App&lt;/span&gt;" style="rounded=1;arcSize=15;fillColor=#f0fdf4;strokeColor=#22c55e;strokeWidth=1.5;align=center;verticalAlign=middle;html=1;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="980" y="125" width="200" height="70" as="geometry" />
        </mxCell>

        <!-- Task 7 (Service Task): Đóng gói ECM & Đẩy Log KPIs -->
        <mxCell id="h4_t7_ecm" value="&lt;div style='font-size:9.5px;color:#1e40af;font-weight:bold;margin-bottom:2px;'&gt;⚙ SERVICE TASK (AUTOMATED)&lt;/div&gt;&lt;b style='font-size:11px;'&gt;[7] Đóng gói ECM &amp;amp; Ghi Log KPIs&lt;/b&gt;&lt;br&gt;&lt;span style='font-size:10px;color:#475569;'&gt;Lưu trữ hợp đồng điện tử vào ECM,&lt;br&gt;Cập nhật Dashboard thời gian thực&lt;/span&gt;" style="rounded=1;arcSize=15;fillColor=#ffffff;strokeColor=#2563eb;strokeWidth=1.5;align=center;verticalAlign=middle;html=1;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="1205" y="522" width="175" height="70" as="geometry" />
        </mxCell>

        <!-- End Event: BPMN Double Circle Terminate -->
        <mxCell id="h4_end_outer" value="" style="ellipse;whiteSpace=wrap;html=1;aspect=fixed;fillColor=#fee2e2;strokeColor=#ef4444;strokeWidth=3;" vertex="1" parent="1">
          <mxGeometry x="1360" y="270" width="40" height="40" as="geometry" />
        </mxCell>
        <mxCell id="h4_end_inner" value="" style="ellipse;whiteSpace=wrap;html=1;aspect=fixed;fillColor=#dc2626;strokeColor=none;" vertex="1" parent="1">
          <mxGeometry x="1370" y="280" width="20" height="20" as="geometry" />
        </mxCell>
        <mxCell id="h4_lbl_end" value="&lt;span style='font-size:10px;color:#b91c1c;font-weight:bold;'&gt;Quy trình&lt;br&gt;hoàn tất&lt;/span&gt;" style="text;html=1;align=center;verticalAlign=middle;" vertex="1" parent="1">
          <mxGeometry x="1345" y="315" width="70" height="26" as="geometry" />
        </mxCell>

        <!-- ==================== SEQUENCE FLOWS CHUẨN BPMN 2.0 ==================== -->
        <!-- Start -> Task 1 -->
        <mxCell id="h4_f1" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;strokeColor=#1e293b;strokeWidth=1.5;" edge="1" parent="1" source="h4_start" target="h4_t1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Task 1 -> Gateway 1 -->
        <mxCell id="h4_f2" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;strokeColor=#1e293b;strokeWidth=1.5;" edge="1" parent="1" source="h4_t1" target="h4_gw1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Nhánh STP: Đẩy thẳng lên Khách hàng Ký số Task 4 -->
        <mxCell id="h4_flow_stp" value="&lt;b style='font-size:10px;color:#15803d;background-color:#ffffff;padding:2px;'&gt;STP: Tự động gửi HĐ&lt;/b&gt;" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;strokeColor=#16a34a;strokeWidth=2.5;" edge="1" parent="1" source="h4_gw1" target="h4_t4_sign">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="460" y="560" />
              <mxPoint x="460" y="160" />
            </Array>
          </mxGeometry>
        </mxCell>

        <!-- Nhánh Ngoại lệ / Món vay lớn -> Task 2 RM -->
        <mxCell id="h4_flow_exc" value="&lt;span style='font-size:9.5px;color:#475569;background-color:#ffffff;padding:2px;'&gt;Ngoại lệ / Món lớn&lt;/span&gt;" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;strokeColor=#475569;strokeWidth=1.5;" edge="1" parent="1" source="h4_gw1" target="h4_t2">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="585" y="290" />
            </Array>
          </mxGeometry>
        </mxCell>

        <!-- Task 2 -> Task 3 Kiểm soát -->
        <mxCell id="h4_f3" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;strokeColor=#475569;strokeWidth=1.5;" edge="1" parent="1" source="h4_t2" target="h4_t3">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="600" y="420" />
            </Array>
          </mxGeometry>
        </mxCell>

        <!-- Task 3 Kiểm soát -> Task 4 Khách hàng Ký số -->
        <mxCell id="h4_f4" value="&lt;span style='font-size:9.5px;color:#475569;background-color:#ffffff;padding:2px;'&gt;Phê duyệt đạt &amp;gt; Gửi HĐ&lt;/span&gt;" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;exitX=0.5;exitY=0;entryX=0.5;entryY=1;endArrow=block;endFill=1;strokeColor=#475569;strokeWidth=1.5;" edge="1" parent="1" source="h4_t3" target="h4_t4_sign">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Task 4 Ký số -> Task 5 Hạch toán Core T24 STP -->
        <mxCell id="h4_flow_signed_to_stp" value="&lt;b style='font-size:9.5px;color:#15803d;background-color:#ffffff;padding:2px;'&gt;Ký số thành công &amp;gt; Kích hoạt GN&lt;/b&gt;" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;strokeColor=#16a34a;strokeWidth=2.5;" edge="1" parent="1" source="h4_t4_sign" target="h4_t5_stp">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="930" y="230" />
              <mxPoint x="970" y="230" />
              <mxPoint x="970" y="557" />
            </Array>
          </mxGeometry>
        </mxCell>

        <!-- Task 5 Hạch toán -> Task 6 Khách hàng Nhận tiền -->
        <mxCell id="h4_flow_disbursed_to_csat" value="&lt;b style='font-size:9.5px;color:#2563eb;background-color:#ffffff;padding:2px;'&gt;Tiền vào tài khoản&lt;/b&gt;" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;strokeColor=#2563eb;strokeWidth=2;" edge="1" parent="1" source="h4_t5_stp" target="h4_t6_csat">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="1080" y="350" />
            </Array>
          </mxGeometry>
        </mxCell>

        <!-- Task 5 Hạch toán -> Task 7 Đóng gói ECM -->
        <mxCell id="h4_f6" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;strokeColor=#1e293b;strokeWidth=1.5;" edge="1" parent="1" source="h4_t5_stp" target="h4_t7_ecm">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Task 6 Khách hàng & Task 7 -> End Event -->
        <mxCell id="h4_f7" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;strokeColor=#1e293b;strokeWidth=1.5;" edge="1" parent="1" source="h4_t6_csat" target="h4_end_outer">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="1260" y="160" />
              <mxPoint x="1260" y="290" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="h4_f8" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;strokeColor=#1e293b;strokeWidth=1.5;" edge="1" parent="1" source="h4_t7_ecm" target="h4_end_outer">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="1380" y="557" />
            </Array>
          </mxGeometry>
        </mxCell>
    """
    return wrap_mxfile("Hinh4_Quy_trinh_Tuong_lai_ToBe_LPBank", cells, 1440, 680)

def main():
    print(">>> Đang tái tạo 4 sơ đồ Draw.io CHUẨN BPMN 2.0 & THẨM MỸ CAO...")

    diagrams = {
        'Hinh1_Ban_do_chien_luoc_LPBank.drawio': generate_hinh1(),
        'Hinh2_Process_Landscape_LPBank.drawio': generate_hinh2(),
        'Hinh3_Quy_trinh_Hien_trang_AsIs_LPBank.drawio': generate_hinh3(),
        'Hinh4_Quy_trinh_Tuong_lai_ToBe_LPBank.drawio': generate_hinh4(),
    }

    for filename, xml_content in diagrams.items():
        file_path = DIAGRAM_DIR / filename
        file_path.write_text(xml_content, encoding='utf-8')

        png_path = DIAGRAM_DIR / f"{filename}.png"
        cmd = [
            DRAWIO_BIN,
            '-x',
            '-f', 'png',
            '-s', '2',            # Scale 2x Retina
            '-b', '10',           # Border padding
            '-o', str(png_path),
            str(file_path)
        ]
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode == 0:
            print(f"  [✓] Xuất PNG Retina 2x: {png_path.name} ({os.path.getsize(png_path)/1024:.1f} KB)")
        else:
            print(f"  [✗] Lỗi {filename}: {res.stderr}")

    print("\n>>> HOÀN TẤT XUẤT 4 SƠ ĐỒ HOÀN HẢO!")

if __name__ == '__main__':
    main()
