'use strict';
const {
  Paragraph, TextRun, Table, TableRow, TableCell,
  WidthType, BorderStyle, AlignmentType, HeadingLevel,
  ShadingType, PageBreak, VerticalAlign
} = require('docx');

// ── helpers ──────────────────────────────────────────────────────────────────
const FONT = 'Times New Roman';
const SZ   = 26; // 13pt * 2
const SZ_H = 26;

function t(text, opts = {}) {
  return new TextRun({ text, font: FONT, size: SZ, ...opts });
}
function tb(text, opts = {}) {
  return new TextRun({ text, font: FONT, size: SZ, bold: true, ...opts });
}
function p(runs, extra = {}) {
  return new Paragraph({
    children: Array.isArray(runs) ? runs : [runs],
    spacing: { after: 120, line: 360, lineRule: 'auto' },
    indent: { firstLine: 720 },
    ...extra,
  });
}
function pNoIndent(runs, extra = {}) {
  return new Paragraph({
    children: Array.isArray(runs) ? runs : [runs],
    spacing: { after: 120, line: 360, lineRule: 'auto' },
    ...extra,
  });
}
function heading1(text) {
  return new Paragraph({
    children: [new TextRun({ text, font: FONT, size: 32, bold: true, allCaps: true })],
    heading: HeadingLevel.HEADING_1,
    spacing: { before: 400, after: 200 },
    indent: {},
  });
}
function heading2(text) {
  return new Paragraph({
    children: [new TextRun({ text, font: FONT, size: 28, bold: true })],
    heading: HeadingLevel.HEADING_2,
    spacing: { before: 320, after: 160 },
    indent: {},
  });
}
function heading3(text) {
  return new Paragraph({
    children: [new TextRun({ text, font: FONT, size: 26, bold: true, italics: true })],
    heading: HeadingLevel.HEADING_3,
    spacing: { before: 240, after: 120 },
    indent: {},
  });
}
function blankLine() {
  return new Paragraph({ children: [new TextRun('')], spacing: { after: 80 } });
}
function pageBreak() {
  return new Paragraph({ children: [new PageBreak()] });
}
function caption(text) {
  return pNoIndent([new TextRun({ text, font: FONT, size: 24, bold: true, italics: true })], {
    alignment: AlignmentType.CENTER,
    spacing: { before: 80, after: 160 },
  });
}

// Table helpers
const DARK_BLUE  = '1F3864';
const MID_BLUE   = '2E74B5';
const LIGHT_BLUE = 'DEEAF1';
const LIGHT_GRAY = 'F2F2F2';
const ORANGE_BG  = 'FCE4D6';
const RED_BG     = 'FF0000';
const YELLOW_BG  = 'FFFF00';

function cellShade(shade) {
  if (!shade) return {};
  return { shading: { type: ShadingType.CLEAR, fill: shade } };
}
function hCell(text, width, span = 1) {
  return new TableCell({
    children: [new Paragraph({
      children: [new TextRun({ text, font: FONT, size: 22, bold: true, color: 'FFFFFF' })],
      alignment: AlignmentType.CENTER,
      spacing: { after: 60 },
    })],
    shading: { type: ShadingType.CLEAR, fill: DARK_BLUE },
    verticalAlign: VerticalAlign.CENTER,
    width: { size: width, type: WidthType.DXA },
    columnSpan: span,
  });
}
function bCell(text, width, shade = null, bold = false, center = false) {
  return new TableCell({
    children: [new Paragraph({
      children: [new TextRun({ text, font: FONT, size: 22, bold })],
      alignment: center ? AlignmentType.CENTER : AlignmentType.LEFT,
      spacing: { after: 60 },
    })],
    ...cellShade(shade),
    verticalAlign: VerticalAlign.CENTER,
    width: { size: width, type: WidthType.DXA },
  });
}
function cCell(text, width, shade = null, bold = false) {
  return bCell(text, width, shade, bold, true);
}
function alt(i) { return i % 2 === 0 ? LIGHT_BLUE : null; }

// ─────────────────────────────────────────────────────────────────────────────
function buildIntroAndChapter1() {
  const items = [];

  // ══════════════════════════════════════════════════════════
  // LỜI MỞ ĐẦU
  // ══════════════════════════════════════════════════════════
  items.push(heading1('LỜI MỞ ĐẦU'));

  items.push(heading2('1. Đề bài môn học và tính phù hợp của đề tài'));

  items.push(p([tb('Yêu cầu đề bài môn học được giao nguyên văn như sau: '),
    t('"Đề xuất kiến trúc chung và các giải pháp để bảo mật hệ thống thông tin cho 01 doanh nghiệp/tổ chức cụ thể."')]));

  items.push(p([t('Đây là một yêu cầu mở, bao trùm toàn bộ vòng đời bảo mật – từ giai đoạn thiết kế kiến trúc, xây dựng phần mềm, triển khai hệ thống, cho đến vận hành và giám sát liên tục. Một đề xuất thực sự xuất sắc không thể chỉ dừng lại ở tầng Runtime (bảo vệ khi hệ thống đang chạy), mà phải bao phủ cả tầng Build/Deploy (bảo vệ ngay từ khi viết code và đóng gói Image) – tức là phải triển khai chiến lược '),
    tb('Shift-Left Security'), t(' toàn diện.')]));

  items.push(p([t('Bài tập lớn giữa kỳ của nhóm đã xây dựng kiến trúc Runtime vững chắc cho hệ thống CRM 1.0 tại Ngân hàng TMCP Công Thương Việt Nam (VietinBank): kiến trúc 3-Tier DMZ, mTLS qua Istio Service Mesh, RBAC/ABAC phân tầng, WORM Audit Log dạng chuỗi hash, cùng hệ thống giám sát SOC/SIEM/Falco. Tuy nhiên, một khoảng trống nghiêm trọng vẫn còn tồn tại: '),
    tb('pipeline CI/CD hiện tại của CRM 1.0 chưa có cơ chế tự động phát hiện lỗ hổng bảo mật trong Container Image và các tệp cấu hình hạ tầng mã nguồn (Infrastructure as Code – IaC)'),
    t('. Đây chính là véc-tơ tấn công chuỗi cung ứng phần mềm (Software Supply Chain Attack) – loại tấn công được Gartner dự báo sẽ ảnh hưởng đến 45% tổ chức toàn cầu vào năm 2025.')]));

  items.push(p([t('Đề tài cuối kỳ này – '),
    tb('"Nghiên cứu áp dụng tự động hoá đánh giá an ninh hạ tầng mã nguồn (IaC) và Container Image bằng Trivy và Terrascan trong quy trình GitOps: Mở rộng kiến trúc bảo mật cho hệ thống CRM 1.0 tại VietinBank"'),
    t(' – được thiết kế để lấp đầy đúng khoảng trống đó. Đây là sự kế thừa hữu cơ và hoàn thiện bức tranh bảo mật tổng thể, đáp ứng trọn vẹn yêu cầu đề bài: '),
    tb('kiến trúc bảo mật toàn diện từ Code đến Runtime cho một tổ chức cụ thể.')]));

  items.push(heading2('2. Tính cấp thiết'));

  items.push(p([t('Ngành tài chính – ngân hàng đang trở thành mục tiêu ưu tiên của các chiến dịch tấn công chuỗi cung ứng phần mềm. Vụ tấn công SolarWinds Orion năm 2020 đã làm lộ ra nguyên tắc nghiêm trọng: kẻ tấn công không cần bẻ khóa hệ thống đích – chúng chỉ cần nhiễm độc công cụ build và image nơi nạn nhân tin tưởng tuyệt đối. Năm 2024, lỗ hổng backdoor trong thư viện nén '),
    tb('xz-utils (CVE-2024-3094)'),
    t(' đã xâm nhập vào các bản phân phối Linux phổ biến thông qua chính pipeline CI/CD nguồn mở, gây chấn động cộng đồng bảo mật toàn cầu.')]));

  items.push(p([t('Trong bối cảnh CRM 1.0 vận hành trên nền tảng container hóa (Red Hat OpenShift), sử dụng hàng trăm image từ registry bên ngoài và deploy bằng các file YAML Helm/Kubernetes – mỗi image chưa được quét, mỗi file YAML cấu hình sai đều là một cánh cửa mở cho kẻ tấn công. Theo báo cáo State of Cloud Native Security 2023 của Palo Alto Networks, '),
    tb('87% tổ chức phát hiện ít nhất một lỗ hổng nghiêm trọng (Critical/High) trong container image production trong năm qua'),
    t(', và 59% thừa nhận rằng các lỗ hổng này không được phát hiện trước khi triển khai.')]));

  items.push(p([t('Thông tư 09/2020/TT-NHNN về an toàn hệ thống thông tin trong hoạt động ngân hàng yêu cầu kiểm tra bảo mật định kỳ và liên tục. Việc tích hợp Trivy và Terrascan vào pipeline GitOps là câu trả lời kỹ thuật trực tiếp cho yêu cầu pháp lý này, đồng thời nâng tầm trưởng thành bảo mật (Security Maturity) của VietinBank lên mức '),
    tb('Level 4 – Proactive'), t(' trong mô hình BSIMM (Building Security In Maturity Model).')]));

  items.push(heading2('3. Sự kế thừa từ bài tập giữa kỳ'));

  items.push(p([t('Bài tập giữa kỳ đã thiết lập nền tảng bảo mật tầng Runtime vững chắc cho CRM 1.0, bao gồm: (i) Kiến trúc mạng 3-Tier DMZ phân vùng WAF → Application Zone → Database Zone; (ii) mTLS toàn diện qua Istio Service Mesh ở chế độ STRICT; (iii) mô hình phân quyền ABAC 3 lớp (API Gateway RBAC → OPA ABAC → PostgreSQL RLS); (iv) WORM Audit Log dạng chuỗi hash SHA-256; (v) pipeline DevSecOps cơ bản với SonarQube quét mã tĩnh.')]));

  items.push(p([t('Bài tập cuối kỳ này kế thừa toàn bộ kiến trúc đó và bổ sung tầng kiểm soát '),
    tb('Build-Time Security'), t(' còn thiếu, đặc biệt là: (i) Quét lỗ hổng CVE tự động trong Container Image bằng Trivy; (ii) Kiểm tra sai cấu hình IaC (Helm, Kubernetes YAML, Terraform) bằng Terrascan; (iii) Tích hợp cả hai công cụ vào pipeline GitLab CI/CD theo mô hình GitOps; (iv) Cơ chế chặn deploy (Hard Gate) khi phát hiện lỗ hổng Critical/High chưa được vá.')]));

  items.push(p([t('Sự bổ sung này hoàn thiện chu trình bảo mật khép kín: '),
    tb('Code → Build → Test → Package (Scan) → Deploy → Runtime → Audit'),
    t(' – đáp ứng đầy đủ yêu cầu đề bài về "kiến trúc chung và các giải pháp bảo mật" cho VietinBank.')]));

  items.push(heading2('4. Mục tiêu và phạm vi'));

  items.push(p([tb('Mục tiêu nghiên cứu: '),
    t('(i) Hệ thống hóa cơ sở lý thuyết về DevSecOps, GitOps và bảo mật hạ tầng mã nguồn; (ii) Phân tích và đánh giá rủi ro tại tầng CI/CD của CRM 1.0 theo phương pháp 9 bước NIST SP 800-30; (iii) Thiết kế và đề xuất pipeline GitOps tích hợp Trivy và Terrascan với cấu hình cụ thể, bao gồm các đoạn mã tham khảo; (iv) Thực nghiệm PoC để xác nhận hiệu quả giải pháp; (v) Hoàn thiện khung ISMS theo ISO/IEC 27001 cho toàn bộ vòng đời DevSecOps.')]));

  items.push(p([tb('Phạm vi nghiên cứu: '),
    t('Hệ thống CRM 1.0 tại VietinBank, bao gồm: frontend NextJS v.14, các microservices Java Spring Boot, container image trên Red Hat OpenShift Container Platform (OCP), file IaC dạng Helm Chart và Kubernetes YAML, pipeline GitLab CI/CD. Nghiên cứu không bao gồm tầng mạng vật lý và hệ thống Core Banking Legacy (đã được xử lý trong bài giữa kỳ).')]));

  items.push(pageBreak());

  // ══════════════════════════════════════════════════════════
  // CHƯƠNG 1
  // ══════════════════════════════════════════════════════════
  items.push(heading1('CHƯƠNG 1: CƠ SỞ LÝ THUYẾT'));

  // 1.1 ──────────────────────────────────────────────────────
  items.push(heading2('1.1. Mở rộng mô hình Phòng vệ chiều sâu – Tầng System Integrity'));

  items.push(heading3('1.1.1. Mô hình Phòng vệ chiều sâu truyền thống'));

  items.push(p([t('Phòng vệ chiều sâu (Defense in Depth – DiD) là chiến lược bảo mật nền tảng, khởi nguồn từ học thuyết quân sự cổ điển: thay vì dựa vào một tuyến phòng thủ duy nhất, hệ thống được bảo vệ bằng nhiều lớp kiểm soát độc lập, sao cho kẻ tấn công phải vượt qua tất cả các lớp đó mới có thể xâm phạm tài sản mục tiêu. Trong an toàn thông tin, mô hình này được chuẩn hóa bởi NIST và được thể hiện qua 7 miền hạ tầng CNTT (IT Infrastructure Domains): Data, Application, Host, LAN, LAN-to-WAN, WAN, Remote Access.')]));

  items.push(p([t('Bài tập giữa kỳ đã triển khai đầy đủ các biện pháp kiểm soát cho 7 miền truyền thống này trong kiến trúc Runtime của CRM 1.0. Tuy nhiên, tài liệu NIST SP 800-160 Vol. 2 '),
    tb('(Systems Security Engineering: Cyber Resiliency Considerations)'),
    t(' và mô hình OWASP Software Assurance Maturity Model (SAMM) đều nhấn mạnh sự tồn tại của một tầng bảo vệ thứ tám, ít được chú trọng hơn trong các triển khai truyền thống: '),
    tb('System Integrity – tính toàn vẹn của hệ thống tại tầng Build/Supply Chain.')]));

  items.push(heading3('1.1.2. Tầng System Integrity trong vòng đời phần mềm'));

  items.push(p([t('System Integrity là tập hợp các biện pháp đảm bảo rằng mỗi artifact phần mềm (source code, container image, IaC template, binary) được tạo ra và triển khai đúng như thiết kế, không bị can thiệp bởi bên thứ ba trong toàn bộ chuỗi cung ứng. NIST SP 800-160 phân loại System Integrity thành ba loại kiểm soát chính: '),
    tb('(i) Source Integrity'),
    t(' – xác thực tính toàn vẹn của mã nguồn và dependency; '),
    tb('(ii) Build Integrity'),
    t(' – đảm bảo quá trình build không bị nhiễm độc; '),
    tb('(iii) Deployment Integrity'),
    t(' – xác thực image/artifact trước khi đưa vào production.')]));

  items.push(p([t('Đối với CRM 1.0 chạy trên OpenShift, tầng System Integrity được hiện thực hóa cụ thể thông qua: quét lỗ hổng CVE trong base image và dependency; kiểm tra sai cấu hình bảo mật trong Helm Chart và Kubernetes YAML; ký số image (Image Signing) bằng Cosign; và tạo Software Bill of Materials (SBOM) để truy xuất nguồn gốc toàn bộ dependency. Trivy và Terrascan là hai công cụ cốt lõi để hiện thực hóa hai đặc tính đầu tiên trong số này.')]));

  // Bảng 1.1
  items.push(caption('Bảng 1.1. Mô hình Phòng vệ chiều sâu mở rộng – 8 tầng kiểm soát cho CRM 1.0'));

  const tbl11Rows = [
    ['Tầng', 'Miền / Domain', 'Biện pháp kiểm soát chính', 'Trạng thái (Giữa kỳ)', 'Bổ sung (Cuối kỳ)'],
    ['1', 'Data', 'TDE AES-256-GCM, Row-Level Security, WORM Audit Log', 'Hoàn thiện', '–'],
    ['2', 'Application', 'mTLS, JWT TTL 30 phút, OPA ABAC, Dynamic Masking', 'Hoàn thiện', '–'],
    ['3', 'Host / Container', 'Falco Runtime Security, Seccomp, NetworkPolicy Default-Deny', 'Hoàn thiện', 'Trivy Image Scan'],
    ['4', 'LAN', 'OpenShift NetworkPolicy East-West Default-Deny, VLAN', 'Hoàn thiện', '–'],
    ['5', 'LAN-to-WAN', 'WAF OWASP ruleset, API Gateway Kong, DDoS scrubbing', 'Hoàn thiện', '–'],
    ['6', 'WAN', 'TLS 1.3, Certificate Pinning, DNSSEC', 'Hoàn thiện', '–'],
    ['7', 'Remote Access', 'SSO OIDC/OAuth2, MFA TOTP, Zero Trust VPN', 'Hoàn thiện', '–'],
    ['8', 'System Integrity (Build/Supply Chain)', 'CVE scan Image, IaC scan, SBOM, Image Signing', 'Khoảng trống', 'Trivy + Terrascan'],
  ];

  items.push(new Table({
    width: { size: 9200, type: WidthType.DXA },
    rows: tbl11Rows.map((row, ri) => new TableRow({
      children: row.map((cell, ci) => {
        if (ri === 0) return hCell(cell, [900, 1600, 2800, 1900, 2000][ci]);
        const shade = ci === 4 && ri === tbl11Rows.length - 1 ? 'E2EFDA' :
                      ri === tbl11Rows.length - 1 ? 'FCE4D6' : alt(ri);
        const bold  = ci === 0 || (ri === tbl11Rows.length - 1 && ci === 1);
        return bCell(cell, [900, 1600, 2800, 1900, 2000][ci], shade, bold);
      }),
    })),
  }));

  items.push(blankLine());

  items.push(p([t('Hàng cuối (tô màu cam) của Bảng 1.1 thể hiện khoảng trống nghiên cứu: Tầng System Integrity chưa được hiện thực hóa trong bài giữa kỳ và là đối tượng trọng tâm của bài cuối kỳ này.')]));

  // 1.2 ──────────────────────────────────────────────────────
  items.push(heading2('1.2. Mối đe dọa phần mềm và Container trong môi trường Cloud-Native'));

  items.push(heading3('1.2.1. Tấn công chuỗi cung ứng phần mềm (Software Supply Chain Attack)'));

  items.push(p([t('Tấn công chuỗi cung ứng phần mềm là nhóm tấn công nhắm vào các điểm yếu trong chuỗi xây dựng và phân phối phần mềm, thay vì tấn công trực tiếp vào hệ thống đích. Kẻ tấn công lợi dụng lòng tin ngầm định: tổ chức tin rằng thư viện từ registry uy tín, image từ Docker Hub official, hay IaC template từ Terraform Registry là an toàn. Thực tế cho thấy giả định này ngày càng không còn đúng.')]));

  items.push(p([t('Các véc-tơ tấn công phổ biến nhất trong môi trường container hóa bao gồm: '),
    tb('(i) Dependency Confusion'),
    t(' – kẻ tấn công đẩy gói độc hại lên public registry với tên trùng với gói nội bộ, khai thác cơ chế ưu tiên resolution của npm/pip/Maven; '),
    tb('(ii) Typosquatting'),
    t(' – đặt tên gói gần giống gói phổ biến (ví dụ: "requets" thay vì "requests") để lừa developer cài nhầm; '),
    tb('(iii) Compromised Base Image'),
    t(' – tấn công vào registry nguồn (Docker Hub, Red Hat Quay) để đưa layer độc hại vào base image; '),
    tb('(iv) IaC Misconfiguration Exploitation'),
    t(' – khai thác các file YAML cấu hình sai (container chạy root, privileged pod, hostPath mount, missing NetworkPolicy) để leo thang đặc quyền trong cluster.')]));

  items.push(heading3('1.2.2. Lỗ hổng CVE trong Container Image'));

  items.push(p([t('Container Image được xây dựng theo kiến trúc phân lớp (layered filesystem). Mỗi lệnh '),
    tb('RUN'),
    t(' trong Dockerfile tạo ra một layer độc lập, và mỗi layer có thể chứa các gói phần mềm với lỗ hổng đã biết (Known Vulnerability) được theo dõi bởi hệ thống CVE (Common Vulnerabilities and Exposures). Một image NextJS điển hình trong CRM 1.0 kế thừa từ '),
    tb('node:20-alpine'),
    t(' sẽ kéo theo toàn bộ dependency chain của Alpine Linux, Node.js runtime, các npm package trong '),
    tb('package.json'),
    t(', và các system library. Bất kỳ CVE nào tồn tại trong chuỗi đó đều ảnh hưởng đến image cuối cùng.')]));

  items.push(p([t('Điểm quan trọng là lỗ hổng CVE không phải lúc nào cũng xuất hiện ngay khi image được build. Nhiều CVE '),
    tb('(zero-day và n-day)'),
    t(' được công bố sau khi image đã triển khai vào production. Do đó, việc quét image chỉ một lần tại thời điểm build là chưa đủ; cần có cơ chế quét định kỳ (scheduled scan) đối với toàn bộ image đang chạy trong cluster – một tính năng mà Trivy hỗ trợ thông qua chế độ '),
    tb('Kubernetes Node Collector.')]));

  items.push(heading3('1.2.3. Sai cấu hình IaC (IaC Misconfiguration)'));

  items.push(p([t('Infrastructure as Code (IaC) là phương pháp quản lý và cung cấp hạ tầng thông qua các tệp cấu hình có thể đọc bằng máy (machine-readable), thay vì quy trình thủ công. Trong môi trường CRM 1.0, IaC bao gồm: Helm Chart cho việc đóng gói ứng dụng OpenShift, Kubernetes YAML manifest cho các thành phần core (Deployment, Service, NetworkPolicy, RBAC), và Terraform template cho việc cung cấp tài nguyên cloud (nếu có).')]));

  items.push(p([t('Sai cấu hình IaC (IaC Misconfiguration) là loại lỗi phổ biến nhất trong môi trường cloud-native, chiếm 70% nguyên nhân gốc rễ của các sự cố bảo mật cloud theo Gartner 2024. Các sai cấu hình nghiêm trọng thường gặp nhất bao gồm: container chạy với quyền root ('),
    tb('runAsNonRoot: false'),
    t('); pod được cấp quyền đặc quyền ('),
    tb('privileged: true'),
    t('); mount filesystem của host ('),
    tb('hostPath'),
    t('); không giới hạn tài nguyên CPU/Memory (thiếu '),
    tb('resources.limits'),
    t('); thiếu chính sách NetworkPolicy dẫn đến kết nối ngang không kiểm soát; và sử dụng image tag '),
    tb(':latest'),
    t(' thay vì digest cố định.')]));

  // Bảng 1.2 – OWASP Top 10 CI/CD
  items.push(caption('Bảng 1.2. OWASP Top 10 CI/CD Security Risks và ánh xạ sang CRM 1.0'));

  const owasp = [
    ['CICD-SEC-01', 'Insufficient Flow Control Mechanisms', 'Thiếu gate bảo mật trong pipeline, không yêu cầu security scan pass trước khi deploy', 'Trivy/Terrascan Hard Gate'],
    ['CICD-SEC-02', 'Inadequate Identity and Access Management', 'Service account CI/CD có quá nhiều quyền trong OpenShift cluster', 'RBAC pipeline (§3.4)'],
    ['CICD-SEC-03', 'Dependency Chain Abuse', 'npm/Maven dependency chứa gói độc hại hoặc CVE chưa vá', 'Trivy SCA + Dependency scan'],
    ['CICD-SEC-04', 'Poisoned Pipeline Execution (PPE)', 'Kẻ tấn công push code độc vào nhánh feature, trigger pipeline với quyền đặc quyền', 'Branch protection + Signed commit'],
    ['CICD-SEC-05', 'Insufficient PBAC (Pipeline-Based Access Controls)', 'Secret CI/CD (token, password) bị lộ qua log hoặc artifact', 'Vault secret injection; masked variables'],
    ['CICD-SEC-06', 'Insufficient Credential Hygiene', 'Hardcode credential trong Dockerfile hoặc file YAML', 'Trivy Secret Detection'],
    ['CICD-SEC-07', 'Insecure System Configuration', 'Container image build từ base image lỗi thời; Helm chart thiếu securityContext', 'Terrascan IaC policy'],
    ['CICD-SEC-08', 'Ungoverned Usage of 3rd Party Services', 'Kéo image từ Docker Hub public không kiểm soát', 'Image provenance policy (Cosign)'],
    ['CICD-SEC-09', 'Improper Artifact Integrity Validation', 'Không xác thực chữ ký image trước khi deploy lên OCP', 'Cosign verify trong pipeline'],
    ['CICD-SEC-10', 'Insufficient Logging and Visibility', 'Không có audit log cho các sự kiện pipeline (ai push, ai approve)', 'GitLab Audit Events + WORM Log'],
  ];

  items.push(new Table({
    width: { size: 9200, type: WidthType.DXA },
    rows: [
      new TableRow({ children: [hCell('Mã', 900), hCell('Rủi ro', 2000), hCell('Biểu hiện trong CRM 1.0', 3200), hCell('Biện pháp đề xuất', 3100)] }),
      ...owasp.map((row, ri) => new TableRow({
        children: [
          cCell(row[0], 900, alt(ri), true),
          bCell(row[1], 2000, alt(ri), true),
          bCell(row[2], 3200, alt(ri)),
          bCell(row[3], 3100, alt(ri)),
        ],
      })),
    ],
  }));
  items.push(blankLine());

  // 1.3 ──────────────────────────────────────────────────────
  items.push(heading2('1.3. DevSecOps và mô hình GitOps'));

  items.push(heading3('1.3.1. DevSecOps – Tích hợp bảo mật vào vòng đời phát triển'));

  items.push(p([t('DevSecOps là phương pháp luận mở rộng của DevOps, tích hợp các hoạt động bảo mật vào toàn bộ vòng đời phát triển phần mềm (SDLC) thay vì để chúng như một giai đoạn độc lập ở cuối chu trình. Triết lý cốt lõi là '),
    tb('"Security as Code"'),
    t(' – mọi chính sách bảo mật đều được viết dưới dạng mã, kiểm tra tự động, và phiên bản hóa cùng với mã ứng dụng. Điều này cho phép bảo mật trở thành một phần không thể tách rời của quá trình phát triển, không phải là rào cản của nó.')]));

  items.push(p([t('Nguyên tắc '),
    tb('Shift-Left'),
    t(' là trụ cột của DevSecOps: dịch chuyển các hoạt động bảo mật về phía trái (sớm hơn) trong pipeline. Chi phí sửa lỗi bảo mật tăng theo hàm mũ khi phát hiện muộn: sửa trong giai đoạn code chỉ tốn 1 đơn vị chi phí, trong giai đoạn test tốn 10 đơn vị, khi đến production tốn 100 đơn vị, và sau khi bị khai thác có thể tốn hàng nghìn đơn vị (thiệt hại tài chính và uy tín). Đối với VietinBank – nơi mỗi sự cố bảo mật có thể dẫn đến vi phạm pháp luật (Nghị định 13/2023/NĐ-CP, Thông tư 09/2020/TT-NHNN) và thiệt hại cho hàng triệu khách hàng – Shift-Left là bắt buộc, không phải tùy chọn.')]));

  items.push(p([t('Vòng đời DevSecOps cho CRM 1.0 được chia thành 8 giai đoạn liên tiếp theo mô hình vòng lặp (loop): '),
    tb('Plan → Code → Build → Test → Package → Release → Deploy → Operate'),
    t('. Bài giữa kỳ đã bảo vệ các giai đoạn Deploy và Operate (Runtime). Bài cuối kỳ bổ sung bảo vệ cho giai đoạn Package (Container Image scan) và giai đoạn Build (IaC scan), hoàn thiện toàn bộ vòng lặp.')]));

  items.push(heading3('1.3.2. GitOps – Triết lý vận hành hạ tầng theo mô hình Git'));

  items.push(p([t('GitOps là mô hình vận hành hạ tầng và ứng dụng cloud-native sử dụng Git làm '),
    tb('Single Source of Truth'),
    t('. Mọi thay đổi về hạ tầng – từ số lượng replica, cấu hình resource limit, đến chính sách NetworkPolicy – đều phải đi qua quy trình Git chuẩn: branch → pull request (merge request) → code review → merge vào nhánh chính. Sau khi merge, một operator (ArgoCD hoặc Flux) sẽ tự động đồng bộ trạng thái cluster với trạng thái được khai báo trong Git repository.')]));

  items.push(p([t('Từ góc độ bảo mật, GitOps mang lại ba lợi ích nền tảng: '),
    tb('(i) Auditability'),
    t(' – mọi thay đổi hạ tầng đều có Git commit history đầy đủ (ai thay đổi, khi nào, thay đổi gì); '),
    tb('(ii) Declarative Security'),
    t(' – chính sách bảo mật được viết dưới dạng mã (Rego/OPA, Terrascan policy) và phiên bản hóa cùng IaC; '),
    tb('(iii) Immutable Deployments'),
    t(' – cluster không bao giờ bị thay đổi trực tiếp (no-kubectl-exec-in-production), mọi thay đổi phải qua GitOps workflow, loại trừ rủi ro '),
    tb('configuration drift.')]));

  items.push(p([t('Trong kiến trúc GitOps của CRM 1.0, pipeline được chia làm hai luồng: '),
    tb('CI (Continuous Integration)'),
    t(' – chạy trên GitLab CI/CD, thực hiện build image, scan CVE (Trivy), scan IaC (Terrascan), ký số image (Cosign), đẩy image lên Red Hat Quay registry; '),
    tb('CD (Continuous Deployment)'),
    t(' – ArgoCD watch Helm Chart repository, khi phát hiện image tag mới đã được ký và scan sạch, tự động sync vào OpenShift cluster. Hai luồng này tách biệt hoàn toàn (decoupled), đảm bảo nguyên tắc least privilege cho từng thành phần.')]));

  // 1.4 ──────────────────────────────────────────────────────
  items.push(heading2('1.4. Công nghệ Trivy và Terrascan'));

  items.push(heading3('1.4.1. Trivy – Bộ quét bảo mật đa năng cho Container và IaC'));

  items.push(p([t('Trivy là công cụ quét bảo mật nguồn mở do Aqua Security phát triển, được phát hành theo giấy phép Apache 2.0. Kể từ phiên bản 0.30 (2022), Trivy đã phát triển từ một công cụ quét Container Image đơn thuần thành một bộ quét bảo mật đa năng (comprehensive security scanner) với khả năng phát hiện nhiều loại vấn đề bảo mật trong nhiều loại artifact khác nhau.')]));

  items.push(p([tb('Các loại Scanner của Trivy:'),
    t(' (i) '),
    tb('Vulnerability (vuln)'),
    t(' – quét CVE trong OS package (Alpine, Debian, RHEL), language package (npm, Maven, pip, Go modules); (ii) '),
    tb('Misconfiguration (config)'),
    t(' – kiểm tra sai cấu hình trong Kubernetes YAML, Helm Chart, Dockerfile, Terraform; (iii) '),
    tb('Secret'),
    t(' – phát hiện secret bị hardcode (API key, password, token); (iv) '),
    tb('License'),
    t(' – kiểm tra license của dependency (AGPL, GPL có thể vi phạm nếu dùng trong phần mềm thương mại); (v) '),
    tb('SBOM'),
    t(' – tạo Software Bill of Materials theo chuẩn CycloneDX hoặc SPDX.')]));

  items.push(p([tb('Database CVE của Trivy'),
    t(' được tổng hợp từ nhiều nguồn: NVD (National Vulnerability Database), Red Hat OVAL, Alpine Linux SecDB, GitHub Advisory Database. Database được cập nhật tự động mỗi 6 giờ và có thể được mirror nội bộ (airgap environment) – phù hợp với yêu cầu bảo mật của VietinBank về việc không cho phép kết nối internet trực tiếp từ môi trường CI.')]));

  items.push(p([tb('Tích hợp với OpenShift:'),
    t(' Trivy được tích hợp vào pipeline GitLab CI/CD thông qua Docker-in-Docker (DinD) hoặc chế độ rootless scanner. Kết quả quét được xuất ra định dạng JSON, SARIF (để tích hợp GitLab Security Dashboard), hoặc table để hiển thị trực tiếp trong log pipeline. Chế độ '),
    tb('--exit-code 1'),
    t(' cho phép fail pipeline tự động khi phát hiện lỗ hổng đạt ngưỡng severity đã cấu hình (CRITICAL, HIGH).')]));

  items.push(heading3('1.4.2. Terrascan – Công cụ phân tích tĩnh IaC theo Policy-as-Code'));

  items.push(p([t('Terrascan là công cụ phân tích tĩnh IaC (Static Analysis for Infrastructure as Code) được phát triển bởi Tenable (trước đây là Accurics), phát hành nguồn mở theo Apache 2.0. Terrascan sử dụng mô hình '),
    tb('Policy-as-Code'),
    t(' dựa trên ngôn ngữ Rego của Open Policy Agent (OPA) để định nghĩa các chính sách bảo mật và compliance.')]));

  items.push(p([tb('Các IaC platform được hỗ trợ:'),
    t(' Terraform (HCL), Kubernetes YAML/JSON, Helm Chart, Dockerfiles, AWS CloudFormation, Azure ARM Templates, Google Cloud Deployment Manager. Đối với CRM 1.0, hai platform quan trọng nhất là '),
    tb('Kubernetes + Helm.')]));

  items.push(p([tb('Cơ chế hoạt động:'),
    t(' Terrascan đọc file IaC, parse thành Abstract Syntax Tree (AST), sau đó đánh giá AST đó với từng policy Rego. Một policy Rego điển hình kiểm tra một thuộc tính cụ thể (ví dụ: '),
    tb('securityContext.runAsNonRoot'),
    t(') và trả về '),
    tb('DENY'),
    t(' nếu thuộc tính đó vi phạm quy tắc. Ngoài policy tùy chỉnh, Terrascan đi kèm hàng trăm policy built-in ánh xạ với các framework compliance: CIS Kubernetes Benchmark, NIST SP 800-190 (Application Container Security), PCI-DSS, HIPAA, SOC2.')]));

  items.push(p([tb('So sánh Trivy config scan vs Terrascan:'),
    t(' Trivy cũng có khả năng scan IaC (module "config"), tuy nhiên Terrascan mạnh hơn ở khả năng viết custom policy Rego phức tạp, hỗ trợ compliance framework mapping chi tiết, và khả năng tích hợp với Terraform Cloud/Enterprise state. Trong pipeline CRM 1.0, hai công cụ được sử dụng song song: Trivy quét CVE và secret, Terrascan kiểm tra compliance policy và custom rule đặc thù của VietinBank.')]));

  // Bảng 1.3 – So sánh Trivy vs Terrascan
  items.push(caption('Bảng 1.3. So sánh đặc điểm kỹ thuật Trivy và Terrascan'));

  const cmpRows = [
    ['Tiêu chí', 'Trivy (Aqua Security)', 'Terrascan (Tenable)'],
    ['Loại quét chính', 'CVE / Vulnerability, Secret, License, SBOM', 'IaC Misconfiguration, Compliance Policy'],
    ['Ngôn ngữ policy', 'Built-in rules (Go), một số Rego', 'OPA Rego (hoàn toàn tùy chỉnh)'],
    ['IaC support', 'Helm, K8s YAML, Terraform, Dockerfile', 'Helm, K8s YAML, Terraform, CloudFormation, ARM'],
    ['Container Image scan', 'Có (core feature)', 'Chỉ Dockerfile, không scan image binary'],
    ['SBOM generation', 'CycloneDX, SPDX', 'Không'],
    ['Compliance mapping', 'CIS, NIST (một phần)', 'CIS, NIST, PCI-DSS, HIPAA, SOC2 (đầy đủ)'],
    ['Chế độ fail pipeline', '--exit-code 1 + severity filter', '--exit-code 3 + severity filter'],
    ['Tích hợp GitLab CI', 'Native SARIF output + Security Dashboard', 'JSON/SARIF output, cần config thêm'],
    ['Airgap support', 'Có (tự host DB)', 'Có (policy bundle offline)'],
    ['License', 'Apache 2.0', 'Apache 2.0'],
  ];

  items.push(new Table({
    width: { size: 9200, type: WidthType.DXA },
    rows: cmpRows.map((row, ri) => new TableRow({
      children: row.map((cell, ci) => {
        if (ri === 0) return hCell(cell, [2200, 3500, 3500][ci]);
        return bCell(cell, [2200, 3500, 3500][ci], alt(ri), ci === 0);
      }),
    })),
  }));
  items.push(blankLine());

  items.push(heading3('1.4.3. Open Policy Agent (OPA) và ngôn ngữ Rego'));

  items.push(p([t('Open Policy Agent (OPA, phát âm "oh-pa") là một policy engine nguồn mở, độc lập với domain, cho phép tách biệt chính sách (policy) ra khỏi code ứng dụng và cơ sở hạ tầng. OPA nhận vào một document dữ liệu (ví dụ: Kubernetes manifest dưới dạng JSON) và đánh giá nó với một tập policy viết bằng ngôn ngữ Rego, trả về quyết định ALLOW/DENY kèm lý do chi tiết.')]));

  items.push(p([t('Rego là ngôn ngữ declarative dựa trên Datalog, được thiết kế để viết các điều kiện logic phức tạp một cách ngắn gọn và dễ kiểm thử (unit-testable). Một policy Rego điển hình có cấu trúc: khai báo '),
    tb('package'),
    t(', import thư viện cần thiết ('),
    tb('import future.keywords'),
    t('), định nghĩa rule '),
    tb('deny'),
    t(' hoặc '),
    tb('violation'),
    t(' với điều kiện boolean. Khi Terrascan load policy Rego để quét Helm Chart của CRM 1.0, nó truyền từng resource Kubernetes (Deployment, Pod, Service) như một input object vào OPA engine và thu thập tất cả kết quả '),
    tb('deny'),
    t(' để tổng hợp báo cáo.')]));

  items.push(p([t('Ưu điểm then chốt của Rego trong ngữ cảnh VietinBank: chính sách bảo mật có thể được '),
    tb('phiên bản hóa, review qua pull request, và test tự động'),
    t(' như bất kỳ đoạn mã nào khác – đây là hiện thực hóa của triết lý "Security as Code" và cho phép ISMS của ngân hàng có bằng chứng kiểm toán (audit evidence) cụ thể cho từng chính sách bảo mật.')]));

  items.push(heading3('1.4.4. Tóm tắt framework lý thuyết'));

  items.push(p([t('Toàn bộ kiến trúc đề xuất trong bài này được xây dựng trên nền tảng lý thuyết liên kết chặt chẽ: '),
    tb('Defense in Depth mở rộng'),
    t(' (System Integrity tầng 8) cung cấp khung tổng quát; '),
    tb('NIST SP 800-30'),
    t(' cung cấp phương pháp đánh giá rủi ro 9 bước cho tầng CI/CD; '),
    tb('OWASP Top 10 CI/CD'),
    t(' cung cấp danh mục rủi ro cụ thể để ưu tiên; '),
    tb('DevSecOps + GitOps'),
    t(' cung cấp mô hình vận hành; '),
    tb('Trivy + Terrascan'),
    t(' là công cụ kỹ thuật để hiện thực hóa; và '),
    tb('ISO/IEC 27001 PDCA'),
    t(' (kế thừa từ giữa kỳ) là khung quản trị bao trùm toàn bộ.')]));

  items.push(pageBreak());

  return items;
}

module.exports = { buildIntroAndChapter1 };
