import os
import subprocess
import html

DIAGRAM_DIR = '/Users/dovandat/WORKSPACE/HVNH/BPM/Bai_tap_lon/diagrams'
HELPER_SCRIPT = '/Users/dovandat/Work/agent-skills-lib/skills/diagram/scripts/drawio_helper.py'

def create_mxfile(diagram_name, content_xml, width=1400, height=850):
    return f"""<mxfile host="app.diagrams.net" version="24.0.0">
  <diagram id="{diagram_name}" name="{diagram_name}">
    <mxGraphModel dx="1400" dy="900" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="{width}" pageHeight="{height}" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
{content_xml}
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>"""

# ==========================================
# 1. HÌNH 3: AS-IS BPMN SWIMLANE DIAGRAM
# ==========================================
def build_hinh3_xml():
    xml = """
        <!-- POOL: LPBank Giải ngân As-Is -->
        <mxCell id="pool_asis" value="LPBANK - QUY TRÌNH TRIỂN KHAI TÍN DỤNG VÀ GIẢI NGÂN (HIỆN TRẠNG AS-IS)" style="swimlane;html=1;childLayout=stackLayout;horizontal=0;startSize=32;horizontalStack=0;fillColor=#1e293b;strokeColor=#0f172a;strokeWidth=2;fontFamily=Arial;fontSize=13;fontStyle=1;fontColor=#ffffff;" vertex="1" parent="1">
          <mxGeometry x="40" y="40" width="1320" height="580" as="geometry" />
        </mxCell>

        <!-- Lane 1: ĐVKD / RM -->
        <mxCell id="lane_rm" value="ĐƠN VỊ KINH DOANH / CHUYÊN VIÊN QLKH (RM)" style="swimlane;html=1;startSize=30;strokeColor=#cbd5e1;strokeWidth=1;fillColor=#ffffff;fontFamily=Arial;fontSize=11;fontStyle=1;fontColor=#334155;align=left;spacingLeft=10;" vertex="1" parent="pool_asis">
          <mxGeometry y="32" width="1320" height="130" as="geometry" />
        </mxCell>

        <!-- Lane 2: Kiểm soát Chi nhánh -->
        <mxCell id="lane_ks_cn" value="KIỂM SOÁT CHI NHÁNH" style="swimlane;html=1;startSize=30;strokeColor=#cbd5e1;strokeWidth=1;fillColor=#f8fafc;fontFamily=Arial;fontSize=11;fontStyle=1;fontColor=#334155;align=left;spacingLeft=10;" vertex="1" parent="pool_asis">
          <mxGeometry y="162" width="1320" height="130" as="geometry" />
        </mxCell>

        <!-- Lane 3: Xử lý hồ sơ (CSU) -->
        <mxCell id="lane_csu" value="CHUYÊN VIÊN XỬ LÝ HỒ SƠ (CSU)" style="swimlane;html=1;startSize=30;strokeColor=#cbd5e1;strokeWidth=1;fillColor=#ffffff;fontFamily=Arial;fontSize=11;fontStyle=1;fontColor=#334155;align=left;spacingLeft=10;" vertex="1" parent="pool_asis">
          <mxGeometry y="292" width="1320" height="140" as="geometry" />
        </mxCell>

        <!-- Lane 4: Cấp phê duyệt & Core T24 -->
        <mxCell id="lane_t24" value="CẤP PHÊ DUYỆT &amp; HỆ THỐNG CORE T24" style="swimlane;html=1;startSize=30;strokeColor=#cbd5e1;strokeWidth=1;fillColor=#f8fafc;fontFamily=Arial;fontSize=11;fontStyle=1;fontColor=#334155;align=left;spacingLeft=10;" vertex="1" parent="pool_asis">
          <mxGeometry y="432" width="1320" height="148" as="geometry" />
        </mxCell>

        <!-- NODES IN LANE 1 (RM) -->
        <mxCell id="asis_start" value="" style="ellipse;shape=bpmnEvent;html=1;symbol=none;fillColor=#dcfce7;strokeColor=#16a34a;strokeWidth=2;" vertex="1" parent="lane_rm">
          <mxGeometry x="50" y="45" width="40" height="40" as="geometry" />
        </mxCell>
        <mxCell id="asis_lbl_start" value="Nhận phương án&lt;br&gt;từ LOS" style="text;html=1;align=center;verticalAlign=middle;fontSize=10;fontFamily=Arial;fontColor=#475569;" vertex="1" parent="lane_rm">
          <mxGeometry x="30" y="88" width="80" height="30" as="geometry" />
        </mxCell>

        <mxCell id="asis_t1" value="&lt;b&gt;[1] Khởi tạo phương án&lt;/b&gt;&lt;br&gt;Tải lên hồ sơ chứng từ" style="rounded=1;arcSize=12;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#475569;strokeWidth=1.5;fontFamily=Arial;fontSize=11;fontColor=#0f172a;" vertex="1" parent="lane_rm">
          <mxGeometry x="130" y="38" width="140" height="54" as="geometry" />
        </mxCell>

        <mxCell id="asis_t2" value="&lt;b&gt;[2] Nhập thông tin giải ngân&lt;/b&gt;&lt;br&gt;Thực hiện First Check" style="rounded=1;arcSize=12;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#475569;strokeWidth=1.5;fontFamily=Arial;fontSize=11;fontColor=#0f172a;" vertex="1" parent="lane_rm">
          <mxGeometry x="310" y="38" width="150" height="54" as="geometry" />
        </mxCell>

        <!-- NODES IN LANE 2 (Kiểm soát CN) -->
        <mxCell id="asis_t3" value="&lt;b&gt;[3] Kiểm soát đề xuất&lt;/b&gt;&lt;br&gt;&lt;font color='#b91c1c'&gt;⚠️ Lặp lại kiểm tra First Check&lt;/font&gt;" style="rounded=1;arcSize=12;whiteSpace=wrap;html=1;fillColor=#fef2f2;strokeColor=#ef4444;strokeWidth=1.8;fontFamily=Arial;fontSize=11;fontColor=#0f172a;" vertex="1" parent="lane_ks_cn">
          <mxGeometry x="310" y="38" width="160" height="54" as="geometry" />
        </mxCell>

        <mxCell id="asis_g1" value="" style="rhombus;whiteSpace=wrap;html=1;fillColor=#fffbeb;strokeColor=#d97706;strokeWidth=1.8;" vertex="1" parent="lane_ks_cn">
          <mxGeometry x="510" y="40" width="50" height="50" as="geometry" />
        </mxCell>
        <mxCell id="asis_lbl_g1" value="Hồ sơ&lt;br&gt;hợp lệ?" style="text;html=1;align=center;verticalAlign=middle;fontSize=10;fontFamily=Arial;fontStyle=2;fontColor=#0f172a;" vertex="1" parent="lane_ks_cn">
          <mxGeometry x="500" y="12" width="70" height="25" as="geometry" />
        </mxCell>

        <!-- NODES IN LANE 3 (CSU) -->
        <mxCell id="asis_t4" value="&lt;b&gt;[4] Thẩm tra lại điều kiện&lt;/b&gt;&lt;br&gt;Nhập biểu lãi suất, kỳ hạn" style="rounded=1;arcSize=12;whiteSpace=wrap;html=1;fillColor=#fef2f2;strokeColor=#ef4444;strokeWidth=1.8;fontFamily=Arial;fontSize=11;fontColor=#0f172a;" vertex="1" parent="lane_csu">
          <mxGeometry x="600" y="43" width="150" height="54" as="geometry" />
        </mxCell>

        <mxCell id="asis_t5" value="&lt;b&gt;[5] Lập Báo cáo kiểm soát&lt;/b&gt;&lt;br&gt;Đề xuất phê duyệt giải ngân" style="rounded=1;arcSize=12;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#475569;strokeWidth=1.5;fontFamily=Arial;fontSize=11;fontColor=#0f172a;" vertex="1" parent="lane_csu">
          <mxGeometry x="790" y="43" width="150" height="54" as="geometry" />
        </mxCell>

        <mxCell id="asis_t8" value="&lt;b&gt;[8] In ký hồ sơ bản cứng&lt;/b&gt;&lt;br&gt;&lt;font color='#b91c1c'&gt;⚠️ Đóng dấu thủ công (NVA)&lt;/font&gt;" style="rounded=1;arcSize=12;whiteSpace=wrap;html=1;fillColor=#fff7ed;strokeColor=#ea580c;strokeWidth=1.8;fontFamily=Arial;fontSize=11;fontColor=#0f172a;" vertex="1" parent="lane_csu">
          <mxGeometry x="1080" y="43" width="150" height="54" as="geometry" />
        </mxCell>

        <!-- NODES IN LANE 4 (Phê duyệt & Core T24) -->
        <mxCell id="asis_t6" value="&lt;b&gt;[6] Kiểm soát viên duyệt&lt;/b&gt;&lt;br&gt;Thẩm quyền phê duyệt" style="rounded=1;arcSize=12;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#475569;strokeWidth=1.5;fontFamily=Arial;fontSize=11;fontColor=#0f172a;" vertex="1" parent="lane_t24">
          <mxGeometry x="790" y="47" width="150" height="54" as="geometry" />
        </mxCell>

        <mxCell id="asis_g2" value="" style="rhombus;whiteSpace=wrap;html=1;fillColor=#fffbeb;strokeColor=#d97706;strokeWidth=1.8;" vertex="1" parent="lane_t24">
          <mxGeometry x="970" y="49" width="50" height="50" as="geometry" />
        </mxCell>
        <mxCell id="asis_lbl_g2" value="Phê duyệt&lt;br&gt;đạt?" style="text;html=1;align=center;verticalAlign=middle;fontSize=10;fontFamily=Arial;fontStyle=2;fontColor=#0f172a;" vertex="1" parent="lane_t24">
          <mxGeometry x="960" y="20" width="70" height="25" as="geometry" />
        </mxCell>

        <mxCell id="asis_t7" value="&lt;b&gt;[7] Tích hợp T24 hạch toán&lt;/b&gt;&lt;br&gt;Thực hiện lệnh chuyển tiền" style="rounded=1;arcSize=12;whiteSpace=wrap;html=1;fillColor=#f0fdf4;strokeColor=#16a34a;strokeWidth=1.8;fontFamily=Arial;fontSize=11;fontColor=#0f172a;" vertex="1" parent="lane_t24">
          <mxGeometry x="1060" y="47" width="160" height="54" as="geometry" />
        </mxCell>

        <mxCell id="asis_end" value="" style="ellipse;shape=bpmnEvent;html=1;symbol=terminate;fillColor=#fef2f2;strokeColor=#dc2626;strokeWidth=2.5;" vertex="1" parent="lane_t24">
          <mxGeometry x="1255" y="54" width="40" height="40" as="geometry" />
        </mxCell>
        <mxCell id="asis_lbl_end" value="Giải ngân&lt;br&gt;hoàn tất" style="text;html=1;align=center;verticalAlign=middle;fontSize=10;fontFamily=Arial;fontColor=#475569;" vertex="1" parent="lane_t24">
          <mxGeometry x="1235" y="97" width="80" height="30" as="geometry" />
        </mxCell>

        <!-- SEQUENCE FLOWS -->
        <mxCell id="e_a1" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;strokeColor=#1e293b;strokeWidth=1.5;" edge="1" parent="1" source="asis_start" target="asis_t1"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e_a2" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;strokeColor=#1e293b;strokeWidth=1.5;" edge="1" parent="1" source="asis_t1" target="asis_t2"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e_a3" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;strokeColor=#1e293b;strokeWidth=1.5;" edge="1" parent="1" source="asis_t2" target="asis_t3"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e_a4" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;strokeColor=#1e293b;strokeWidth=1.5;" edge="1" parent="1" source="asis_t3" target="asis_g1"><mxGeometry relative="1" as="geometry" /></mxCell>

        <!-- REWORK LOOP 1 (Đỏ nét đứt uốn ngược về RM) -->
        <mxCell id="e_rew1" value="Thiếu hồ sơ (Vòng lặp 1)" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;strokeColor=#dc2626;strokeWidth=1.8;dashed=1;fontFamily=Arial;fontSize=10;fontColor=#dc2626;" edge="1" parent="1" source="asis_g1" target="asis_t1">
          <mxGeometry relative="1" as="geometry"><Array as="points"><mxPoint x="575" y="140" /><mxPoint x="240" y="140" /></Array></mxGeometry>
        </mxCell>

        <mxCell id="e_a5" value="Hợp lệ" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;strokeColor=#1e293b;strokeWidth=1.5;fontFamily=Arial;fontSize=10;fontColor=#0f172a;" edge="1" parent="1" source="asis_g1" target="asis_t4"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e_a6" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;strokeColor=#1e293b;strokeWidth=1.5;" edge="1" parent="1" source="asis_t4" target="asis_t5"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e_a7" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;strokeColor=#1e293b;strokeWidth=1.5;" edge="1" parent="1" source="asis_t5" target="asis_t6"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e_a8" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;strokeColor=#1e293b;strokeWidth=1.5;" edge="1" parent="1" source="asis_t6" target="asis_g2"><mxGeometry relative="1" as="geometry" /></mxCell>

        <!-- REWORK LOOP 2 (Đỏ nét đứt uốn ngược về CSU) -->
        <mxCell id="e_rew2" value="Sửa đổi (Vòng lặp 2)" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;strokeColor=#dc2626;strokeWidth=1.8;dashed=1;fontFamily=Arial;fontSize=10;fontColor=#dc2626;" edge="1" parent="1" source="asis_g2" target="asis_t4">
          <mxGeometry relative="1" as="geometry"><Array as="points"><mxPoint x="1035" y="445" /><mxPoint x="715" y="445" /></Array></mxGeometry>
        </mxCell>

        <mxCell id="e_a9" value="Chấp thuận" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;strokeColor=#1e293b;strokeWidth=1.5;fontFamily=Arial;fontSize=10;fontColor=#0f172a;" edge="1" parent="1" source="asis_g2" target="asis_t7"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e_a10" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;strokeColor=#1e293b;strokeWidth=1.5;" edge="1" parent="1" source="asis_t7" target="asis_t8"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e_a11" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;strokeColor=#1e293b;strokeWidth=1.5;" edge="1" parent="1" source="asis_t8" target="asis_end"><mxGeometry relative="1" as="geometry" /></mxCell>
    """
    return create_mxfile("Hinh3_Quy_trinh_Hien_trang_AsIs_LPBank", xml, width=1400, height=660)

# ==========================================
# 2. HÌNH 4: TO-BE BPMN SWIMLANE DIAGRAM
# ==========================================
def build_hinh4_xml():
    xml = """
        <!-- POOL: LPBank Giải ngân To-Be -->
        <mxCell id="pool_tobe" value="LPBANK - QUY TRÌNH TRIỂN KHAI TÍN DỤNG VÀ GIẢI NGÂN (TƯƠNG LAI TO-BE)" style="swimlane;html=1;childLayout=stackLayout;horizontal=0;startSize=32;horizontalStack=0;fillColor=#0f172a;strokeColor=#0f172a;strokeWidth=2;fontFamily=Arial;fontSize=13;fontStyle=1;fontColor=#ffffff;" vertex="1" parent="1">
          <mxGeometry x="40" y="40" width="1340" height="580" as="geometry" />
        </mxCell>

        <!-- Lane 1: Khách hàng (Digital) -->
        <mxCell id="lane_cust" value="KHÁCH HÀNG (MOBILE BANKING APP / WEB)" style="swimlane;html=1;startSize=30;strokeColor=#cbd5e1;strokeWidth=1;fillColor=#ffffff;fontFamily=Arial;fontSize=11;fontStyle=1;fontColor=#1e3a8a;align=left;spacingLeft=10;" vertex="1" parent="pool_tobe">
          <mxGeometry y="32" width="1340" height="130" as="geometry" />
        </mxCell>

        <!-- Lane 2: RM / ĐVKD -->
        <mxCell id="lane_rm2" value="CHUYÊN VIÊN QUAN HỆ KHÁCH HÀNG (RM)" style="swimlane;html=1;startSize=30;strokeColor=#cbd5e1;strokeWidth=1;fillColor=#f8fafc;fontFamily=Arial;fontSize=11;fontStyle=1;fontColor=#334155;align=left;spacingLeft=10;" vertex="1" parent="pool_tobe">
          <mxGeometry y="162" width="1340" height="130" as="geometry" />
        </mxCell>

        <!-- Lane 3: Kiểm soát & Phê duyệt rủi ro -->
        <mxCell id="lane_appr2" value="KIỂM SOÁT VIÊN PHÊ DUYỆT RỦI RO" style="swimlane;html=1;startSize=30;strokeColor=#cbd5e1;strokeWidth=1;fillColor=#ffffff;fontFamily=Arial;fontSize=11;fontStyle=1;fontColor=#334155;align=left;spacingLeft=10;" vertex="1" parent="pool_tobe">
          <mxGeometry y="292" width="1340" height="130" as="geometry" />
        </mxCell>

        <!-- Lane 4: Smart BPM Orchestrator & Core T24 -->
        <mxCell id="lane_sys2" value="HỆ THỐNG SMART BPM (ORCHESTRATOR) &amp; CORE T24" style="swimlane;html=1;startSize=30;strokeColor=#cbd5e1;strokeWidth=1;fillColor=#f8fafc;fontFamily=Arial;fontSize=11;fontStyle=1;fontColor=#14532d;align=left;spacingLeft=10;" vertex="1" parent="pool_tobe">
          <mxGeometry y="422" width="1340" height="158" as="geometry" />
        </mxCell>

        <!-- NODES IN LANE 4 (Hệ thống khởi tạo tự động) -->
        <mxCell id="tb_start" value="" style="ellipse;shape=bpmnEvent;html=1;symbol=none;fillColor=#dcfce7;strokeColor=#16a34a;strokeWidth=2;" vertex="1" parent="lane_sys2">
          <mxGeometry x="40" y="55" width="40" height="40" as="geometry" />
        </mxCell>
        <mxCell id="tb_lbl_start" value="Nhận duyệt từ LOS&lt;br&gt;(Correlation ID)" style="text;html=1;align=center;verticalAlign=middle;fontSize=10;fontFamily=Arial;fontColor=#475569;" vertex="1" parent="lane_sys2">
          <mxGeometry x="15" y="98" width="90" height="30" as="geometry" />
        </mxCell>

        <mxCell id="tb_precheck" value="&lt;b&gt;[1] Tự động Pre-check Rule&lt;/b&gt;&lt;br&gt;Khóa trường nguồn dữ liệu" style="rounded=1;arcSize=12;whiteSpace=wrap;html=1;fillColor=#f0fdf4;strokeColor=#16a34a;strokeWidth=1.8;fontFamily=Arial;fontSize=11;fontColor=#14532d;" vertex="1" parent="lane_sys2">
          <mxGeometry x="130" y="48" width="160" height="54" as="geometry" />
        </mxCell>

        <!-- NODES IN LANE 2 (RM) -->
        <mxCell id="tb_rm" value="&lt;b&gt;[2] RM xác nhận phương án&lt;/b&gt;&lt;br&gt;Bổ sung lịch giải ngân" style="rounded=1;arcSize=12;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#475569;strokeWidth=1.5;fontFamily=Arial;fontSize=11;fontColor=#0f172a;" vertex="1" parent="lane_rm2">
          <mxGeometry x="340" y="38" width="160" height="54" as="geometry" />
        </mxCell>

        <!-- GATEWAY PHÂN LUỒNG RỦI RO IN LANE 4 -->
        <mxCell id="tb_gw_risk" value="" style="rhombus;whiteSpace=wrap;html=1;fillColor=#fef9c3;strokeColor=#ca8a04;strokeWidth=1.8;" vertex="1" parent="lane_sys2">
          <mxGeometry x="540" y="50" width="50" height="50" as="geometry" />
        </mxCell>
        <mxCell id="tb_lbl_gw_risk" value="Phân luồng&lt;br&gt;rủi ro?" style="text;html=1;align=center;verticalAlign=middle;fontSize=10;fontFamily=Arial;fontStyle=2;fontColor=#0f172a;" vertex="1" parent="lane_sys2">
          <mxGeometry x="530" y="20" width="70" height="25" as="geometry" />
        </mxCell>

        <!-- NODES IN LANE 3 (Kiểm soát ngoại lệ) -->
        <mxCell id="tb_appr" value="&lt;b&gt;[3] Phê duyệt theo rủi ro&lt;/b&gt;&lt;br&gt;SLA ≤ 2h, Reason code chuẩn" style="rounded=1;arcSize=12;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#475569;strokeWidth=1.5;fontFamily=Arial;fontSize=11;fontColor=#0f172a;" vertex="1" parent="lane_appr2">
          <mxGeometry x="640" y="38" width="180" height="54" as="geometry" />
        </mxCell>

        <!-- HẠCH TOÁN T24 IN LANE 4 -->
        <mxCell id="tb_t24" value="&lt;b&gt;[4] Hạch toán Core T24 &amp; Chuyển tiền&lt;/b&gt;&lt;br&gt;Idempotency Key &amp; Circuit Breaker" style="rounded=1;arcSize=12;whiteSpace=wrap;html=1;fillColor=#f0fdf4;strokeColor=#16a34a;strokeWidth=2;fontFamily=Arial;fontSize=11;fontColor=#14532d;" vertex="1" parent="lane_sys2">
          <mxGeometry x="870" y="48" width="190" height="54" as="geometry" />
        </mxCell>

        <!-- KÝ SỐ IN LANE 1 (Khách hàng) -->
        <mxCell id="tb_sign" value="&lt;b&gt;[5] KÝ SỐ ĐIỆN TỬ TỪ XA&lt;/b&gt;&lt;br&gt;SmartCA / FPT.eSign (Không in giấy)" style="rounded=1;arcSize=12;whiteSpace=wrap;html=1;fillColor=#eff6ff;strokeColor=#2563eb;strokeWidth=2;fontFamily=Arial;fontSize=11;fontColor=#1e3a8a;" vertex="1" parent="lane_cust">
          <mxGeometry x="870" y="38" width="190" height="54" as="geometry" />
        </mxCell>

        <mxCell id="tb_track" value="&lt;b&gt;[6] Nhận tiền &amp; Đánh giá&lt;/b&gt;&lt;br&gt;Khảo sát độ hài lòng CSAT" style="rounded=1;arcSize=12;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#2563eb;strokeWidth=1.5;fontFamily=Arial;fontSize=11;fontColor=#1e3a8a;" vertex="1" parent="lane_cust">
          <mxGeometry x="1110" y="38" width="160" height="54" as="geometry" />
        </mxCell>

        <!-- LƯU TRỮ VÀ EVENT LOG IN LANE 4 -->
        <mxCell id="tb_archive" value="&lt;b&gt;[7] Đóng gói ECM &amp; Đẩy log KPIs&lt;/b&gt;&lt;br&gt;Đối soát trạng thái tài chính cuối" style="rounded=1;arcSize=12;whiteSpace=wrap;html=1;fillColor=#f8fafc;strokeColor=#475569;strokeWidth=1.5;fontFamily=Arial;fontSize=11;fontColor=#0f172a;" vertex="1" parent="lane_sys2">
          <mxGeometry x="1110" y="48" width="170" height="54" as="geometry" />
        </mxCell>

        <mxCell id="tb_end" value="" style="ellipse;shape=bpmnEvent;html=1;symbol=terminate;fillColor=#fef2f2;strokeColor=#dc2626;strokeWidth=2.5;" vertex="1" parent="lane_sys2">
          <mxGeometry x="1310" y="55" width="40" height="40" as="geometry" />
        </mxCell>
        <mxCell id="tb_lbl_end" value="Giải ngân&lt;br&gt;hoàn tất" style="text;html=1;align=center;verticalAlign=middle;fontSize=10;fontFamily=Arial;fontColor=#475569;" vertex="1" parent="lane_sys2">
          <mxGeometry x="1290" y="98" width="80" height="30" as="geometry" />
        </mxCell>

        <!-- EDGES -->
        <mxCell id="e_t1" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;strokeColor=#1e293b;strokeWidth=1.5;" edge="1" parent="1" source="tb_start" target="tb_precheck"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e_t2" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;strokeColor=#1e293b;strokeWidth=1.5;" edge="1" parent="1" source="tb_precheck" target="tb_rm"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e_t3" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;strokeColor=#1e293b;strokeWidth=1.5;" edge="1" parent="1" source="tb_rm" target="tb_gw_risk"><mxGeometry relative="1" as="geometry" /></mxCell>

        <!-- NHÁNH STP (MÀU XANH LÁ THẲNG TẮP) -->
        <mxCell id="e_stp" value="Khoản vay chuẩn / Rủi ro thấp (LUỒNG STP)" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;strokeColor=#16a34a;strokeWidth=2.2;fontFamily=Arial;fontSize=10;fontColor=#15803d;fontStyle=1;" edge="1" parent="1" source="tb_gw_risk" target="tb_t24">
          <mxGeometry relative="1" as="geometry"><Array as="points"><mxPoint x="640" y="540" /><mxPoint x="640" y="540" /></Array></mxGeometry>
        </mxCell>

        <!-- NHÁNH PHÊ DUYỆT NGOẠI LỆ -->
        <mxCell id="e_appr_flow" value="Ngoại lệ / Quy mô lớn" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;strokeColor=#475569;strokeWidth=1.5;fontFamily=Arial;fontSize=10;fontColor=#334155;" edge="1" parent="1" source="tb_gw_risk" target="tb_appr"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e_appr_done" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;strokeColor=#1e293b;strokeWidth=1.5;" edge="1" parent="1" source="tb_appr" target="tb_t24"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="e_sign_flow" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;strokeColor=#2563eb;strokeWidth=1.8;" edge="1" parent="1" source="tb_t24" target="tb_sign"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e_track_flow" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;strokeColor=#2563eb;strokeWidth=1.5;" edge="1" parent="1" source="tb_sign" target="tb_track"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e_arch_flow" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;strokeColor=#1e293b;strokeWidth=1.5;" edge="1" parent="1" source="tb_sign" target="tb_archive"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e_end_flow" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;strokeColor=#1e293b;strokeWidth=1.5;" edge="1" parent="1" source="tb_archive" target="tb_end"><mxGeometry relative="1" as="geometry" /></mxCell>
    """
    return create_mxfile("Hinh4_Quy_trinh_Tuong_lai_ToBe_LPBank", xml, width=1420, height=660)

# ==========================================
# 3. HÌNH 1: BẢN ĐỒ CHIẾN LƯỢC STRATEGY MAP (KAPLAN & NORTON)
# ==========================================
def build_hinh1_xml():
    xml = """
        <!-- BANNER HEADER -->
        <mxCell id="hdr_sm" value="BẢN ĐỒ CHIẾN LƯỢC CHO QUY TRÌNH GIẢI NGÂN (BALANCED SCORECARD STRATEGY MAP)" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#1e293b;strokeColor=#0f172a;strokeWidth=2;fontFamily=Arial;fontSize=14;fontStyle=1;fontColor=#ffffff;align=center;" vertex="1" parent="1">
          <mxGeometry x="40" y="30" width="1120" height="45" as="geometry" />
        </mxCell>

        <!-- TẦNG 4: TÀI CHÍNH -->
        <mxCell id="box_fin" value="TÀI CHÍNH&#xa;(Financial)" style="swimlane;html=1;startSize=28;horizontal=0;fillColor=#fff7ed;strokeColor=#ea580c;strokeWidth=1.8;fontFamily=Arial;fontSize=11;fontStyle=1;fontColor=#c2410c;" vertex="1" parent="1">
          <mxGeometry x="40" y="95" width="1120" height="130" as="geometry" />
        </mxCell>
        <mxCell id="f1" value="&lt;b&gt;Tăng trưởng tín dụng bán lẻ&lt;/b&gt;&lt;br&gt;An toàn, bền vững (+20%/năm)" style="rounded=1;arcSize=16;fillColor=#ffffff;strokeColor=#ea580c;strokeWidth=1.5;fontFamily=Arial;fontSize=11;fontColor=#0f172a;align=center;" vertex="1" parent="box_fin">
          <mxGeometry x="60" y="35" width="280" height="65" as="geometry" />
        </mxCell>
        <mxCell id="f2" value="&lt;b&gt;Tối ưu hóa chi phí vận hành&lt;/b&gt;&lt;br&gt;Giảm tỷ lệ CIR ≤ 29%" style="rounded=1;arcSize=16;fillColor=#ffffff;strokeColor=#ea580c;strokeWidth=1.5;fontFamily=Arial;fontSize=11;fontColor=#0f172a;align=center;" vertex="1" parent="box_fin">
          <mxGeometry x="420" y="35" width="280" height="65" as="geometry" />
        </mxCell>
        <mxCell id="f3" value="&lt;b&gt;Kiểm soát chất lượng nợ xấu&lt;/b&gt;&lt;br&gt;NPL ≤ 1.5% &amp; Chi phí dự phòng" style="rounded=1;arcSize=16;fillColor=#ffffff;strokeColor=#ea580c;strokeWidth=1.5;fontFamily=Arial;fontSize=11;fontColor=#0f172a;align=center;" vertex="1" parent="box_fin">
          <mxGeometry x="780" y="35" width="280" height="65" as="geometry" />
        </mxCell>

        <!-- TẦNG 3: KHÁCH HÀNG -->
        <mxCell id="box_cust" value="KHÁCH HÀNG&#xa;(Customer)" style="swimlane;html=1;startSize=28;horizontal=0;fillColor=#f0fdf4;strokeColor=#16a34a;strokeWidth=1.8;fontFamily=Arial;fontSize=11;fontStyle=1;fontColor=#15803d;" vertex="1" parent="1">
          <mxGeometry x="40" y="245" width="1120" height="130" as="geometry" />
        </mxCell>
        <mxCell id="c1" value="&lt;b&gt;Rút ngắn thời gian giải ngân&lt;/b&gt;&lt;br&gt;TAT ≤ 8h (Khoản vay nhỏ STP &lt; 15p)" style="rounded=1;arcSize=16;fillColor=#ffffff;strokeColor=#16a34a;strokeWidth=1.5;fontFamily=Arial;fontSize=11;fontColor=#0f172a;align=center;" vertex="1" parent="box_cust">
          <mxGeometry x="60" y="35" width="280" height="65" as="geometry" />
        </mxCell>
        <mxCell id="c2" value="&lt;b&gt;Minh bạch tiến độ hồ sơ&lt;/b&gt;&lt;br&gt;Tra cứu đa kênh trên Mobile App" style="rounded=1;arcSize=16;fillColor=#ffffff;strokeColor=#16a34a;strokeWidth=1.5;fontFamily=Arial;fontSize=11;fontColor=#0f172a;align=center;" vertex="1" parent="box_cust">
          <mxGeometry x="420" y="35" width="280" height="65" as="geometry" />
        </mxCell>
        <mxCell id="c3" value="&lt;b&gt;Nâng cao trải nghiệm dịch vụ&lt;/b&gt;&lt;br&gt;Tỷ lệ hài lòng CSAT ≥ 90%, NPS ≥ 65" style="rounded=1;arcSize=16;fillColor=#ffffff;strokeColor=#16a34a;strokeWidth=1.5;fontFamily=Arial;fontSize=11;fontColor=#0f172a;align=center;" vertex="1" parent="box_cust">
          <mxGeometry x="780" y="35" width="280" height="65" as="geometry" />
        </mxCell>

        <!-- TẦNG 2: QUY TRÌNH NỘI BỘ -->
        <mxCell id="box_int" value="QUY TRÌNH NỘI BỘ&#xa;(Internal Process)" style="swimlane;html=1;startSize=28;horizontal=0;fillColor=#f0f9ff;strokeColor=#0284c7;strokeWidth=1.8;fontFamily=Arial;fontSize=11;fontStyle=1;fontColor=#0369a1;" vertex="1" parent="1">
          <mxGeometry x="40" y="395" width="1120" height="130" as="geometry" />
        </mxCell>
        <mxCell id="i1" value="&lt;b&gt;Chuẩn hóa Rule Engine&lt;/b&gt;&lt;br&gt;Tự động Pre-check, ngăn lỗi hồ sơ" style="rounded=1;arcSize=16;fillColor=#ffffff;strokeColor=#0284c7;strokeWidth=1.5;fontFamily=Arial;fontSize=11;fontColor=#0f172a;align=center;" vertex="1" parent="box_int">
          <mxGeometry x="60" y="35" width="280" height="65" as="geometry" />
        </mxCell>
        <mxCell id="i2" value="&lt;b&gt;Tích hợp dữ liệu liền mạch&lt;/b&gt;&lt;br&gt;Smart BPM ↔ Core T24 ↔ LOS" style="rounded=1;arcSize=16;fillColor=#ffffff;strokeColor=#0284c7;strokeWidth=1.5;fontFamily=Arial;fontSize=11;fontColor=#0f172a;align=center;" vertex="1" parent="box_int">
          <mxGeometry x="420" y="35" width="280" height="65" as="geometry" />
        </mxCell>
        <mxCell id="i3" value="&lt;b&gt;Giảm tỷ lệ xử lý lại (Rework)&lt;/b&gt;&lt;br&gt;Tinh gọn các tầng phê duyệt lặp" style="rounded=1;arcSize=16;fillColor=#ffffff;strokeColor=#0284c7;strokeWidth=1.5;fontFamily=Arial;fontSize=11;fontColor=#0f172a;align=center;" vertex="1" parent="box_int">
          <mxGeometry x="780" y="35" width="280" height="65" as="geometry" />
        </mxCell>

        <!-- TẦNG 1: HỌC TẬP & PHÁT TRIỂN -->
        <mxCell id="box_lg" value="HỌC TẬP &amp; PHÁT TRIỂN&#xa;(Learning &amp; Growth)" style="swimlane;html=1;startSize=28;horizontal=0;fillColor=#f8fafc;strokeColor=#64748b;strokeWidth=1.8;fontFamily=Arial;fontSize=11;fontStyle=1;fontColor=#334155;" vertex="1" parent="1">
          <mxGeometry x="40" y="545" width="1120" height="130" as="geometry" />
        </mxCell>
        <mxCell id="l1" value="&lt;b&gt;Nâng cao năng lực thẩm định số&lt;/b&gt;&lt;br&gt;Đào tạo kỹ năng phân tích rủi ro RM" style="rounded=1;arcSize=16;fillColor=#ffffff;strokeColor=#64748b;strokeWidth=1.5;fontFamily=Arial;fontSize=11;fontColor=#0f172a;align=center;" vertex="1" parent="box_lg">
          <mxGeometry x="60" y="35" width="280" height="65" as="geometry" />
        </mxCell>
        <mxCell id="l2" value="&lt;b&gt;Xác lập quyền sở hữu quy trình&lt;/b&gt;&lt;br&gt;Chỉ định End-to-End Process Owner" style="rounded=1;arcSize=16;fillColor=#ffffff;strokeColor=#64748b;strokeWidth=1.5;fontFamily=Arial;fontSize=11;fontColor=#0f172a;align=center;" vertex="1" parent="box_lg">
          <mxGeometry x="420" y="35" width="280" height="65" as="geometry" />
        </mxCell>
        <mxCell id="l3" value="&lt;b&gt;Xây dựng văn hóa kỷ luật dữ liệu&lt;/b&gt;&lt;br&gt;Cam kết tuân thủ SLA theo vai trò" style="rounded=1;arcSize=16;fillColor=#ffffff;strokeColor=#64748b;strokeWidth=1.5;fontFamily=Arial;fontSize=11;fontColor=#0f172a;align=center;" vertex="1" parent="box_lg">
          <mxGeometry x="780" y="35" width="280" height="65" as="geometry" />
        </mxCell>

        <!-- CAUSAL ARROWS FROM BOTTOM TO TOP -->
        <mxCell id="e_l1_i1" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=classic;endFill=1;strokeColor=#0284c7;strokeWidth=1.5;" edge="1" parent="1" source="l1" target="i1"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e_l2_i3" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=classic;endFill=1;strokeColor=#0284c7;strokeWidth=1.5;" edge="1" parent="1" source="l2" target="i3"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e_l3_i2" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=classic;endFill=1;strokeColor=#0284c7;strokeWidth=1.5;" edge="1" parent="1" source="l3" target="i2"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="e_i1_c1" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=classic;endFill=1;strokeColor=#16a34a;strokeWidth=1.5;" edge="1" parent="1" source="i1" target="c1"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e_i2_c2" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=classic;endFill=1;strokeColor=#16a34a;strokeWidth=1.5;" edge="1" parent="1" source="i2" target="c2"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e_i3_c1" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=classic;endFill=1;strokeColor=#16a34a;strokeWidth=1.5;" edge="1" parent="1" source="i3" target="c1"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e_i3_c3" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=classic;endFill=1;strokeColor=#16a34a;strokeWidth=1.5;" edge="1" parent="1" source="i3" target="c3"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="e_c1_f1" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=classic;endFill=1;strokeColor=#ea580c;strokeWidth=1.5;" edge="1" parent="1" source="c1" target="f1"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e_c1_f2" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=classic;endFill=1;strokeColor=#ea580c;strokeWidth=1.5;" edge="1" parent="1" source="c1" target="f2"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e_c2_c3" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=classic;endFill=1;strokeColor=#16a34a;strokeWidth=1.5;" edge="1" parent="1" source="c2" target="c3"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e_c3_f1" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=classic;endFill=1;strokeColor=#ea580c;strokeWidth=1.5;" edge="1" parent="1" source="c3" target="f1"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e_i1_f3" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=classic;endFill=1;strokeColor=#ea580c;strokeWidth=1.5;" edge="1" parent="1" source="i1" target="f3"><mxGeometry relative="1" as="geometry" /></mxCell>
    """
    return create_mxfile("Hinh1_Ban_do_chien_luoc_LPBank", xml, width=1200, height=720)

# ==========================================
# 4. HÌNH 2: PROCESS LANDSCAPE VALUE CHAIN MAP
# ==========================================
def build_hinh2_xml():
    xml = """
        <!-- BANNER HEADER -->
        <mxCell id="hdr_pl" value="SƠ ĐỒ CẢNH QUAN QUY TRÌNH CẤP CAO LPBANK (PROCESS LANDSCAPE &amp; VALUE CHAIN MAP)" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#1e293b;strokeColor=#0f172a;strokeWidth=2;fontFamily=Arial;fontSize=14;fontStyle=1;fontColor=#ffffff;align=center;" vertex="1" parent="1">
          <mxGeometry x="40" y="30" width="1280" height="45" as="geometry" />
        </mxCell>

        <!-- TẦNG QUẢN LÝ -->
        <mxCell id="box_mgt" value="QUY TRÌNH QUẢN LÝ (MANAGEMENT PROCESSES)" style="swimlane;html=1;startSize=26;fillColor=#fef2f2;strokeColor=#dc2626;strokeWidth=1.8;fontFamily=Arial;fontSize=11;fontStyle=1;fontColor=#991b1b;" vertex="1" parent="1">
          <mxGeometry x="40" y="95" width="1280" height="110" as="geometry" />
        </mxCell>
        <mxCell id="m1" value="&lt;b&gt;Hoạch định Chiến lược&lt;/b&gt;&lt;br&gt;&amp; Kế hoạch Kinh doanh" style="rounded=1;arcSize=14;fillColor=#ffffff;strokeColor=#dc2626;strokeWidth=1.2;fontFamily=Arial;fontSize=10;fontColor=#0f172a;align=center;" vertex="1" parent="box_mgt">
          <mxGeometry x="40" y="38" width="260" height="52" as="geometry" />
        </mxCell>
        <mxCell id="m2" value="&lt;b&gt;Quản trị Rủi ro&lt;/b&gt;&lt;br&gt;&amp; Cân đối Vốn (ALM)" style="rounded=1;arcSize=14;fillColor=#ffffff;strokeColor=#dc2626;strokeWidth=1.2;fontFamily=Arial;fontSize=10;fontColor=#0f172a;align=center;" vertex="1" parent="box_mgt">
          <mxGeometry x="360" y="38" width="260" height="52" as="geometry" />
        </mxCell>
        <mxCell id="m3" value="&lt;b&gt;Kiểm toán Nội bộ&lt;/b&gt;&lt;br&gt;&amp; Tuân thủ Giám sát NHNN" style="rounded=1;arcSize=14;fillColor=#ffffff;strokeColor=#dc2626;strokeWidth=1.2;fontFamily=Arial;fontSize=10;fontColor=#0f172a;align=center;" vertex="1" parent="box_mgt">
          <mxGeometry x="680" y="38" width="260" height="52" as="geometry" />
        </mxCell>
        <mxCell id="m4" value="&lt;b&gt;Quản trị Thay đổi&lt;/b&gt;&lt;br&gt;&amp; Danh mục Dự án Số" style="rounded=1;arcSize=14;fillColor=#ffffff;strokeColor=#dc2626;strokeWidth=1.2;fontFamily=Arial;fontSize=10;fontColor=#0f172a;align=center;" vertex="1" parent="box_mgt">
          <mxGeometry x="980" y="38" width="260" height="52" as="geometry" />
        </mxCell>

        <!-- TẦNG CỐT LÕI (VALUE CHAIN) -->
        <mxCell id="box_core" value="QUY TRÌNH CỐT LÕI (CORE PROCESSES / CHUỖI GIÁ TRỊ CẤP TÍN DỤNG END-TO-END)" style="swimlane;html=1;startSize=26;fillColor=#eff6ff;strokeColor=#2563eb;strokeWidth=2;fontFamily=Arial;fontSize=11;fontStyle=1;fontColor=#1e40af;" vertex="1" parent="1">
          <mxGeometry x="40" y="225" width="1280" height="210" as="geometry" />
        </mxCell>

        <!-- INPUT CHEVRON -->
        <mxCell id="in_cust" value="NHU CẦU&lt;br&gt;KHÁCH HÀNG&lt;br&gt;&amp; THỊ TRƯỜNG" style="shape=card;whiteSpace=wrap;html=1;fillColor=#e2e8f0;strokeColor=#475569;strokeWidth=1.5;fontFamily=Arial;fontSize=10;fontStyle=1;fontColor=#1e293b;align=center;" vertex="1" parent="box_core">
          <mxGeometry x="20" y="45" width="85" height="140" as="geometry" />
        </mxCell>

        <!-- CHUỖI 7 BƯỚC CỐT LÕI -->
        <mxCell id="c_1" value="&lt;b&gt;Phát triển SP&lt;/b&gt;&lt;br&gt;&amp; Dịch vụ Tín dụng" style="rounded=1;arcSize=10;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#2563eb;strokeWidth=1.2;fontFamily=Arial;fontSize=10;fontColor=#0f172a;align=center;" vertex="1" parent="box_core">
          <mxGeometry x="130" y="45" width="125" height="60" as="geometry" />
        </mxCell>
        <mxCell id="c_2" value="&lt;b&gt;Marketing &amp; Bán hàng&lt;/b&gt;&lt;br&gt;Tiếp cận Khách hàng" style="rounded=1;arcSize=10;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#2563eb;strokeWidth=1.2;fontFamily=Arial;fontSize=10;fontColor=#0f172a;align=center;" vertex="1" parent="box_core">
          <mxGeometry x="275" y="45" width="125" height="60" as="geometry" />
        </mxCell>
        <mxCell id="c_3" value="&lt;b&gt;Tiếp nhận Hồ sơ&lt;/b&gt;&lt;br&gt;Khởi tạo Đề nghị vay" style="rounded=1;arcSize=10;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#2563eb;strokeWidth=1.2;fontFamily=Arial;fontSize=10;fontColor=#0f172a;align=center;" vertex="1" parent="box_core">
          <mxGeometry x="420" y="45" width="125" height="60" as="geometry" />
        </mxCell>
        <mxCell id="c_4" value="&lt;b&gt;Thẩm định Năng lực&lt;/b&gt;&lt;br&gt;&amp; Phê duyệt Khoản vay" style="rounded=1;arcSize=10;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#2563eb;strokeWidth=1.2;fontFamily=Arial;fontSize=10;fontColor=#0f172a;align=center;" vertex="1" parent="box_core">
          <mxGeometry x="565" y="45" width="125" height="60" as="geometry" />
        </mxCell>
        <mxCell id="c_5" value="&lt;b&gt;Hoàn thiện Văn kiện&lt;/b&gt;&lt;br&gt;&amp; Tài sản Bảo đảm" style="rounded=1;arcSize=10;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#2563eb;strokeWidth=1.2;fontFamily=Arial;fontSize=10;fontColor=#0f172a;align=center;" vertex="1" parent="box_core">
          <mxGeometry x="710" y="45" width="125" height="60" as="geometry" />
        </mxCell>

        <!-- QUY TRÌNH TRỌNG TÂM: GIẢI NGÂN (HIGHLIGHT TO BẢNG XANH LÁ) -->
        <mxCell id="c_6" value="&lt;b&gt;TRIỂN KHAI TÍN DỤNG&lt;br&gt;&amp; GIẢI NGÂN VỐN VAY&lt;/b&gt;&lt;br&gt;&lt;font color='#16a34a'&gt;⭐ QUY TRÌNH TRỌNG TÂM&lt;/font&gt;" style="rounded=1;arcSize=10;whiteSpace=wrap;html=1;fillColor=#dcfce7;strokeColor=#16a34a;strokeWidth=2.5;fontFamily=Arial;fontSize=11;fontColor=#14532d;align=center;" vertex="1" parent="box_core">
          <mxGeometry x="855" y="40" width="145" height="70" as="geometry" />
        </mxCell>

        <mxCell id="c_7" value="&lt;b&gt;Quản lý Sau vay&lt;/b&gt;&lt;br&gt;Giám sát nợ &amp; Thu hồi" style="rounded=1;arcSize=10;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#2563eb;strokeWidth=1.2;fontFamily=Arial;fontSize=10;fontColor=#0f172a;align=center;" vertex="1" parent="box_core">
          <mxGeometry x="1020" y="45" width="120" height="60" as="geometry" />
        </mxCell>

        <!-- OUTPUT CHEVRON -->
        <mxCell id="out_cust" value="GIÁ TRỊ&lt;br&gt;KHÁCH HÀNG&lt;br&gt;&amp; HÀI LÒNG" style="shape=card;whiteSpace=wrap;html=1;fillColor=#dcfce7;strokeColor=#16a34a;strokeWidth=1.5;fontFamily=Arial;fontSize=10;fontStyle=1;fontColor=#15803d;align=center;" vertex="1" parent="box_core">
          <mxGeometry x="1165" y="45" width="95" height="140" as="geometry" />
        </mxCell>

        <!-- ARROWS CONNECTING CORE VALUE CHAIN -->
        <mxCell id="ec1" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=classic;endFill=1;strokeColor=#2563eb;strokeWidth=1.5;" edge="1" parent="1" source="in_cust" target="c_1"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="ec2" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=classic;endFill=1;strokeColor=#2563eb;strokeWidth=1.5;" edge="1" parent="1" source="c_1" target="c_2"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="ec3" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=classic;endFill=1;strokeColor=#2563eb;strokeWidth=1.5;" edge="1" parent="1" source="c_2" target="c_3"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="ec4" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=classic;endFill=1;strokeColor=#2563eb;strokeWidth=1.5;" edge="1" parent="1" source="c_3" target="c_4"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="ec5" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=classic;endFill=1;strokeColor=#2563eb;strokeWidth=1.5;" edge="1" parent="1" source="c_4" target="c_5"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="ec6" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=classic;endFill=1;strokeColor=#16a34a;strokeWidth=2.2;" edge="1" parent="1" source="c_5" target="c_6"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="ec7" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=classic;endFill=1;strokeColor=#2563eb;strokeWidth=1.5;" edge="1" parent="1" source="c_6" target="c_7"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="ec8" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=classic;endFill=1;strokeColor=#16a34a;strokeWidth=2;" edge="1" parent="1" source="c_7" target="out_cust"><mxGeometry relative="1" as="geometry" /></mxCell>

        <!-- TẦNG HỖ TRỢ -->
        <mxCell id="box_sup" value="QUY TRÌNH HỖ TRỢ (SUPPORT PROCESSES)" style="swimlane;html=1;startSize=26;fillColor=#f8fafc;strokeColor=#475569;strokeWidth=1.8;fontFamily=Arial;fontSize=11;fontStyle=1;fontColor=#334155;" vertex="1" parent="1">
          <mxGeometry x="40" y="455" width="1280" height="110" as="geometry" />
        </mxCell>
        <mxCell id="s1" value="&lt;b&gt;Quản trị CNTT&lt;/b&gt;&lt;br&gt;&amp; Ngân hàng lõi T24" style="rounded=1;arcSize=14;fillColor=#ffffff;strokeColor=#475569;strokeWidth=1.2;fontFamily=Arial;fontSize=10;fontColor=#0f172a;align=center;" vertex="1" parent="box_sup">
          <mxGeometry x="30" y="38" width="180" height="52" as="geometry" />
        </mxCell>
        <mxCell id="s2" value="&lt;b&gt;Quản trị Nhân sự&lt;/b&gt;&lt;br&gt;&amp; Đào tạo Nghiệp vụ" style="rounded=1;arcSize=14;fillColor=#ffffff;strokeColor=#475569;strokeWidth=1.2;fontFamily=Arial;fontSize=10;fontColor=#0f172a;align=center;" vertex="1" parent="box_sup">
          <mxGeometry x="240" y="38" width="180" height="52" as="geometry" />
        </mxCell>
        <mxCell id="s3" value="&lt;b&gt;Tài chính, Kế toán&lt;/b&gt;&lt;br&gt;&amp; Quản lý Nguồn vốn" style="rounded=1;arcSize=14;fillColor=#ffffff;strokeColor=#475569;strokeWidth=1.2;fontFamily=Arial;fontSize=10;fontColor=#0f172a;align=center;" vertex="1" parent="box_sup">
          <mxGeometry x="450" y="38" width="180" height="52" as="geometry" />
        </mxCell>
        <mxCell id="s4" value="&lt;b&gt;Pháp chế &amp; Xử lý Nợ&lt;/b&gt;&lt;br&gt;Quản trị Rủi ro Pháp lý" style="rounded=1;arcSize=14;fillColor=#ffffff;strokeColor=#475569;strokeWidth=1.2;fontFamily=Arial;fontSize=10;fontColor=#0f172a;align=center;" vertex="1" parent="box_sup">
          <mxGeometry x="660" y="38" width="180" height="52" as="geometry" />
        </mxCell>
        <mxCell id="s5" value="&lt;b&gt;Quản lý Tài sản&lt;/b&gt;&lt;br&gt;&amp; Lưu trữ Hồ sơ ECM" style="rounded=1;arcSize=14;fillColor=#ffffff;strokeColor=#475569;strokeWidth=1.2;fontFamily=Arial;fontSize=10;fontColor=#0f172a;align=center;" vertex="1" parent="box_sup">
          <mxGeometry x="870" y="38" width="180" height="52" as="geometry" />
        </mxCell>
        <mxCell id="s6" value="&lt;b&gt;An toàn Thông tin&lt;/b&gt;&lt;br&gt;&amp; Bảo mật Dữ liệu KH" style="rounded=1;arcSize=14;fillColor=#ffffff;strokeColor=#475569;strokeWidth=1.2;fontFamily=Arial;fontSize=10;fontColor=#0f172a;align=center;" vertex="1" parent="box_sup">
          <mxGeometry x="1080" y="38" width="180" height="52" as="geometry" />
        </mxCell>
    """
    return create_mxfile("Hinh2_Process_Landscape_LPBank", xml, width=1360, height=600)

tasks = [
    ("Hinh1_Ban_do_chien_luoc_LPBank", build_hinh1_xml()),
    ("Hinh2_Process_Landscape_LPBank", build_hinh2_xml()),
    ("Hinh3_Quy_trinh_Hien_trang_AsIs_LPBank", build_hinh3_xml()),
    ("Hinh4_Quy_trinh_Tuong_lai_ToBe_LPBank", build_hinh4_xml()),
]

for name, xml_content in tasks:
    drawio_path = os.path.join(DIAGRAM_DIR, f"{name}.drawio")
    png_path = os.path.join(DIAGRAM_DIR, f"{name}.drawio.png")
    
    with open(drawio_path, "w", encoding="utf-8") as f:
        f.write(xml_content)
    print(f"Wrote native Draw.io XML: {drawio_path}")
    
    # Export to high-res png using drawio desktop CLI with scale 2
    cmd = ["python3", HELPER_SCRIPT, "export", drawio_path, "-o", png_path, "-s", "2", "-b", "20"]
    subprocess.run(cmd, check=True)
    print(f"Exported high-res PNG: {png_path}")

print("Successfully regenerated all 4 expert-grade Draw.io diagrams!")
