'use strict';
const {
  Paragraph, TextRun, Table, TableRow, TableCell,
  WidthType, BorderStyle, AlignmentType, HeadingLevel,
  ShadingType, PageBreak, VerticalAlign
} = require('docx');

const FONT = 'Times New Roman';
const CODE_FONT = 'Courier New';
const SZ = 26;

function t(text, opts = {}) { return new TextRun({ text, font: FONT, size: SZ, ...opts }); }
function tb(text) { return new TextRun({ text, font: FONT, size: SZ, bold: true }); }
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
    spacing: { after: 80, line: 360, lineRule: 'auto' },
    ...extra,
  });
}
function heading1(text) {
  return new Paragraph({
    children: [new TextRun({ text, font: FONT, size: 32, bold: true, allCaps: true })],
    heading: HeadingLevel.HEADING_1, spacing: { before: 400, after: 200 }, indent: {},
  });
}
function heading2(text) {
  return new Paragraph({
    children: [new TextRun({ text, font: FONT, size: 28, bold: true })],
    heading: HeadingLevel.HEADING_2, spacing: { before: 320, after: 160 }, indent: {},
  });
}
function heading3(text) {
  return new Paragraph({
    children: [new TextRun({ text, font: FONT, size: 26, bold: true, italics: true })],
    heading: HeadingLevel.HEADING_3, spacing: { before: 240, after: 120 }, indent: {},
  });
}
function blankLine() { return new Paragraph({ children: [new TextRun('')], spacing: { after: 80 } }); }
function pageBreak() { return new Paragraph({ children: [new PageBreak()] }); }
function caption(text) {
  return pNoIndent([new TextRun({ text, font: FONT, size: 24, bold: true, italics: true })], {
    alignment: AlignmentType.CENTER, spacing: { before: 80, after: 160 },
  });
}
function codeCaption(text) {
  return pNoIndent([new TextRun({ text, font: FONT, size: 24, bold: true, italics: true })], {
    spacing: { before: 160, after: 60 },
  });
}
function codeBlock(lines) {
  return lines.map(line => new Paragraph({
    children: [new TextRun({ text: line, font: CODE_FONT, size: 20 })],
    spacing: { after: 0, line: 260, lineRule: 'auto' },
    indent: { left: 360 },
    shading: { type: ShadingType.CLEAR, fill: 'F8F8F8' },
    border: {
      top:    { style: BorderStyle.SINGLE, size: 1, color: 'CCCCCC' },
      bottom: { style: BorderStyle.SINGLE, size: 1, color: 'CCCCCC' },
      left:   { style: BorderStyle.THICK,  size: 8, color: '2E74B5' },
      right:  { style: BorderStyle.SINGLE, size: 1, color: 'CCCCCC' },
    },
  }));
}

const DARK_BLUE  = '1F3864';
const LIGHT_BLUE = 'DEEAF1';
const ORANGE_BG  = 'FCE4D6';
const GREEN_BG   = 'E2EFDA';
const YELLOW_BG  = 'FFFF99';

function hCell(text, width, span = 1) {
  return new TableCell({
    children: [new Paragraph({
      children: [new TextRun({ text, font: FONT, size: 22, bold: true, color: 'FFFFFF' })],
      alignment: AlignmentType.CENTER, spacing: { after: 60 },
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
    shading: shade ? { type: ShadingType.CLEAR, fill: shade } : undefined,
    verticalAlign: VerticalAlign.CENTER,
    width: { size: width, type: WidthType.DXA },
  });
}
function cCell(text, width, shade = null, bold = false) { return bCell(text, width, shade, bold, true); }
function alt(i) { return i % 2 === 0 ? LIGHT_BLUE : null; }

// ─────────────────────────────────────────────────────────────────────────────
function buildChapter4AndConclusion() {
  const items = [];

  items.push(heading1('CHƯƠNG 4: THỰC NGHIỆM PoC VÀ QUẢN TRỊ BẢO MẬT'));

  // 4.1 ──────────────────────────────────────────────────────
  items.push(heading2('4.1. Kịch bản thực nghiệm Proof-of-Concept (PoC)'));

  items.push(heading3('4.1.1. Môi trường thực nghiệm'));

  items.push(p([t('Thực nghiệm PoC được thực hiện trên môi trường lab mô phỏng CRM 1.0, bao gồm: GitLab CE 16.x (self-hosted), Red Hat OpenShift Local 4.14 (CRC – CodeReady Containers), Trivy v0.50.0, Terrascan v1.19.0, và Helm Chart mẫu của microservice Customer Profile. Mục tiêu PoC là xác nhận: (i) pipeline phát hiện và chặn đúng các trường hợp vi phạm; (ii) kết quả scan chính xác và có thể hành động; (iii) thời gian thực thi pipeline chấp nhận được (< 5 phút cho toàn bộ security stage).')]));

  items.push(heading3('4.1.2. Kịch bản PoC 1: Trivy phát hiện CVE Critical trong image NextJS'));

  items.push(p([t('Kịch bản này mô phỏng tình huống developer build image NextJS từ base image '),
    tb('node:18-alpine3.17'),
    t(' – một phiên bản đã biết có CVE-2023-0464 (OpenSSL, mức CRITICAL, CVSS 9.1) và CVE-2023-2650 (OpenSSL, HIGH, CVSS 7.5). Đây là loại lỗ hổng thực tế xuất hiện thường xuyên trong các base image Node.js.')]));

  items.push(codeCaption('Đoạn mã 4.1. Dockerfile mẫu chứa base image lỗi thời (mô phỏng)'));
  items.push(...codeBlock([
    '# Dockerfile – customer-profile-service (phiên bản có lỗ hổng – MÔ PHỎNG)',
    'FROM node:18-alpine3.17',
    '# node:18-alpine3.17 chứa openssl 3.0.8 có CVE-2023-0464 (CRITICAL)',
    '',
    'WORKDIR /app',
    'COPY package*.json ./',
    'RUN npm ci --only=production',
    'COPY . .',
    'RUN npm run build',
    '',
    '# KHÔNG có: USER nonroot – container sẽ chạy root (vi phạm VTB-SEC-K8S-001)',
    'CMD ["node", "server.js"]',
  ]));
  items.push(blankLine());

  items.push(p([tb('Kết quả mô phỏng Trivy scan (log pipeline):')]));

  items.push(codeCaption('Đoạn mã 4.2. Output mô phỏng của Trivy khi phát hiện CVE Critical'));
  items.push(...codeBlock([
    '$ trivy image --exit-code 1 --severity CRITICAL --ignore-unfixed \\',
    '    crm-customer-profile:abc123-build',
    '',
    'customer-profile:abc123-build (alpine 3.17.x)',
    '=============================================',
    'Total: 3 (CRITICAL: 2, HIGH: 1)',
    '',
    '┌─────────────┬────────────────┬──────────┬───────────────────┬──────────────────┬────────────────────────────────────────────┐',
    '│  Library    │ Vulnerability  │ Severity │ Installed Version │  Fixed Version   │                   Title                    │',
    '├─────────────┼────────────────┼──────────┼───────────────────┼──────────────────┼────────────────────────────────────────────┤',
    '│ libssl3     │ CVE-2023-0464  │ CRITICAL │ 3.0.8-r0          │ 3.0.9-r0         │ OpenSSL: Excessive Resource Usage          │',
    '│             │                │          │                   │                  │ Verifying Policy Constraints               │',
    '├─────────────┼────────────────┼──────────┼───────────────────┼──────────────────┼────────────────────────────────────────────┤',
    '│ libcrypto3  │ CVE-2023-0464  │ CRITICAL │ 3.0.8-r0          │ 3.0.9-r0         │ OpenSSL: Excessive Resource Usage          │',
    '├─────────────┼────────────────┼──────────┼───────────────────┼──────────────────┼────────────────────────────────────────────┤',
    '│ libssl3     │ CVE-2023-2650  │ HIGH     │ 3.0.8-r0          │ 3.0.9-r1         │ OpenSSL: Possible DoS translating          │',
    '│             │                │          │                   │                  │ ASN.1 object identifiers                   │',
    '└─────────────┴────────────────┴──────────┴───────────────────┴──────────────────┴────────────────────────────────────────────┘',
    '',
    'SECURITY GATE: 2 CRITICAL CVE found. Pipeline FAILED.',
    'Fix: Update base image to node:18-alpine3.18 or higher.',
    '',
    '$ echo $?',
    '1    # exit code 1 → GitLab CI stage FAILED → Pipeline dừng, KHÔNG push image',
  ]));
  items.push(blankLine());

  items.push(p([t('Hành động tiếp theo: Developer cập nhật Dockerfile sang '),
    tb('FROM node:18-alpine3.20'),
    t(' (OpenSSL 3.1.4, không có CVE Critical), commit lên branch và pipeline chạy lại. Lần này Trivy scan PASS (exit code 0), pipeline tiếp tục sang stage sign-push.')]));

  items.push(heading3('4.1.3. Kịch bản PoC 2: Terrascan phát hiện container chạy root'));

  items.push(p([t('Kịch bản này mô phỏng Helm Chart của microservice Java Spring Boot thiếu '),
    tb('securityContext.runAsNonRoot: true'),
    t('. Đây là lỗi cấu hình thực tế rất phổ biến, đặc biệt với các service được migrate từ VM sang container mà không review lại securityContext.')]));

  items.push(codeCaption('Đoạn mã 4.3. Helm Chart deployment.yaml có sai cấu hình (mô phỏng)'));
  items.push(...codeBlock([
    '# helm/crm-account-service/templates/deployment.yaml (phiên bản lỗi – MÔ PHỎNG)',
    'apiVersion: apps/v1',
    'kind: Deployment',
    'metadata:',
    '  name: account-service',
    '  namespace: crm-production',
    'spec:',
    '  replicas: 3',
    '  template:',
    '    spec:',
    '      # THIEU: securityContext ở cấp pod',
    '      containers:',
    '        - name: account-service',
    '          image: quay.vietinbank.local/crm/account-service:latest  # Lỗi: tag :latest',
    '          # THIEU: securityContext ở cấp container',
    '          resources:',
    '            requests:',
    '              cpu: "200m"',
    '              memory: "512Mi"',
    '            # THIEU: limits (nguy co resource exhaustion)',
  ]));
  items.push(blankLine());

  items.push(codeCaption('Đoạn mã 4.4. Output mô phỏng Terrascan phát hiện 4 vi phạm policy'));
  items.push(...codeBlock([
    '$ terrascan scan --iac-type helm --iac-dir ./helm \\',
    '    --policy-path ./security-policies/rego --severity HIGH',
    '',
    'Scan Summary -',
    '  File/Folder      : ./helm/crm-account-service',
    '  IaC Type         : helm',
    '  Scanned At       : 2026-06-08 09:15:33 UTC',
    '  Policies Scanned : 187',
    '  Scan Duration    : 2.3 seconds',
    '',
    'Violation Details -',
    '',
    '  Description    : VTB-SEC-K8S-001: Deployment [account-service] thieu',
    '                   securityContext.runAsNonRoot: true o cap pod',
    '  File           : helm/crm-account-service/templates/deployment.yaml',
    '  Line           : 8',
    '  Severity       : HIGH',
    '  Rule Name      : VTB-SEC-K8S-001',
    '',
    '  Description    : VTB-SEC-K8S-001: Container [account-service] trong',
    '                   Deployment [account-service] thieu securityContext.runAsNonRoot',
    '  File           : helm/crm-account-service/templates/deployment.yaml',
    '  Line           : 12',
    '  Severity       : HIGH',
    '',
    '  Description    : VTB-SEC-K8S-005: Container [account-service] thieu',
    '                   resources.limits.cpu',
    '  File           : helm/crm-account-service/templates/deployment.yaml',
    '  Line           : 20',
    '  Severity       : HIGH',
    '',
    '  Description    : VTB-SEC-K8S-006: Container [account-service] dung image',
    '                   tag :latest. Phai dung digest sha256.',
    '  File           : helm/crm-account-service/templates/deployment.yaml',
    '  Line           : 14',
    '  Severity       : HIGH',
    '',
    'Total Violations: 4 (HIGH: 4)',
    'SECURITY GATE: Violations found (exit code 3). Pipeline FAILED.',
    '$ echo $?',
    '3',
  ]));
  items.push(blankLine());

  items.push(p([tb('Hành động khắc phục: '),
    t('Developer cập nhật Helm Chart để thêm '),
    tb('securityContext.runAsNonRoot: true'),
    t(' ở cả cấp pod và container, thêm '),
    tb('resources.limits'),
    t(', và thay '),
    tb(':latest'),
    t(' bằng image digest cụ thể ('),
    tb('sha256:abc123...'),
    t('). Sau khi fix và re-run pipeline, Terrascan scan PASS với 0 violation.')]));

  // 4.2 ──────────────────────────────────────────────────────
  items.push(heading2('4.2. Hoàn thiện ISMS theo ISO/IEC 27001 – Vòng lặp PDCA'));

  items.push(heading3('4.2.1. Tích hợp DevSecOps vào khung ISMS hiện có'));

  items.push(p([t('Bài tập giữa kỳ đã thiết lập khung ISMS theo ISO/IEC 27001 với vòng lặp PDCA (Plan-Do-Check-Act) cho VietinBank. Bài này bổ sung các hoạt động DevSecOps vào từng giai đoạn PDCA, hoàn thiện khung quản trị bảo mật toàn vòng đời phần mềm:')]));

  items.push(caption('Bảng 4.1. Tích hợp DevSecOps GitOps vào vòng lặp PDCA – ISO/IEC 27001'));

  const pdcaRows = [
    ['Giai đoạn PDCA', 'Hoạt động ISO 27001', 'Tích hợp DevSecOps mới', 'Tần suất', 'Bằng chứng kiểm toán'],
    ['PLAN\n(Lập kế hoạch)', 'Xác định phạm vi ISMS\nPhân tích rủi ro (NIST 800-30)\nXác định mục tiêu bảo mật', 'Định nghĩa policy Rego mới\nCập nhật ngưỡng CVE (CRITICAL/HIGH)\nPlanning sprint bảo mật', 'Hàng quý', 'Git commit lịch sử policy Rego\nRisk register cập nhật'],
    ['DO\n(Triển khai)', 'Triển khai kiểm soát bảo mật\nĐào tạo nhân viên\nVận hành hệ thống', 'Tích hợp Trivy + Terrascan vào pipeline\nScan định kỳ hàng đêm (scheduled)\nImage signing với Cosign', 'Liên tục (mỗi commit)', 'Pipeline artifact (SARIF/JSON)\nQuay registry scan history\nCosign attestation log'],
    ['CHECK\n(Kiểm tra)', 'Kiểm tra nội bộ ISMS\nDo lường hiệu quả kiểm soát\nPenetration testing (TT09/2020)', 'Dashboard CVE trend (GitLab Security)\nBáo cáo tuần: số CVE mới/đã vá\nQuét lại image đang chạy (Trivy Operator)', 'Hàng tuần / Hàng năm (pentest)', 'GitLab Security Dashboard export\nBáo cáo Trivy Operator weekly\nPentest report (Thông tư 09)'],
    ['ACT\n(Cải tiến)', 'Hành động khắc phục và phòng ngừa\nCập nhật chính sách ISMS\nCải tiến liên tục', 'Cập nhật .trivyignore (waiver hết hạn)\nBổ sung Rego policy mới khi phát sinh RR\nNâng cấp base image định kỳ', 'Theo sự kiện\n(CVE công bố, audit finding)', 'Jira ticket khắc phục có deadline\nMR approval trail trong Git\nISMS review meeting minutes'],
  ];

  items.push(new Table({
    width: { size: 9200, type: WidthType.DXA },
    rows: pdcaRows.map((row, ri) => new TableRow({
      children: row.map((cell, ci) => {
        if (ri === 0) return hCell(cell, [1500, 2000, 2500, 1200, 2000][ci]);
        const shade = ri === 1 ? 'E2EFDA' : ri === 2 ? LIGHT_BLUE : ri === 3 ? YELLOW_BG : ORANGE_BG;
        return bCell(cell, [1500, 2000, 2500, 1200, 2000][ci], shade, ci === 0);
      }),
    })),
  }));
  items.push(blankLine());

  items.push(heading3('4.2.2. Kiểm soát A.14 – Security in Development and Support Processes'));

  items.push(p([t('ISO/IEC 27001:2022 Annex A.14 (Security of Application Systems in Development) yêu cầu tổ chức đảm bảo bảo mật được tích hợp vào toàn bộ quy trình phát triển phần mềm. Pipeline DevSecOps GitOps của CRM 1.0 đáp ứng trực tiếp các kiểm soát sau:')]));

  items.push(p([tb('A.14.2.1 – Secure development policy: '),
    t('Quy định rõ ràng rằng mọi code change phải qua pipeline tự động bao gồm Trivy scan và Terrascan scan. Quy định này được enforce thông qua GitLab branch protection rules (không thể push trực tiếp vào nhánh main/release).')]));

  items.push(p([tb('A.14.2.5 – Secure system engineering principles: '),
    t('Nguyên tắc Shift-Left và Defense in Depth được áp dụng trong toàn bộ SDLC. Policy Rego mã hóa các nguyên tắc bảo mật thành quy tắc có thể thực thi và kiểm tra tự động.')]));

  items.push(p([tb('A.14.2.8 – System security testing: '),
    t('Trivy và Terrascan thực hiện kiểm tra bảo mật tự động tại mỗi lần commit. Kết quả được lưu trữ 90 ngày dưới dạng artifact có thể kiểm toán.')]));

  items.push(p([tb('A.14.3.1 – Protection of test data: '),
    t('Trivy secret scan đảm bảo không có credential production nào bị hardcode trong source code hoặc Dockerfile, ngăn chặn rủi ro rò rỉ dữ liệu test sang môi trường development.')]));

  // 4.3 ──────────────────────────────────────────────────────
  items.push(heading2('4.3. Quản trị con người và tuân thủ pháp luật'));

  items.push(heading3('4.3.1. WORM Audit Log cho hoạt động pipeline'));

  items.push(p([t('Kế thừa từ bài giữa kỳ, kiến trúc WORM Audit Log (Write-Once-Read-Many với chuỗi hash SHA-256) được mở rộng để ghi nhận các sự kiện bảo mật trong pipeline CI/CD. Điều này đáp ứng yêu cầu truy xuất nguồn gốc (auditability) của ISO 27001 và Nghị định 13/2023/NĐ-CP (trách nhiệm giải trình trong xử lý dữ liệu cá nhân).')]));

  items.push(caption('Bảng 4.2. Danh mục sự kiện audit được ghi nhận trong pipeline DevSecOps'));

  const auditRows = [
    ['Sự kiện', 'Trigger', 'Thông tin ghi nhận', 'Mức độ', 'Lưu trữ'],
    ['Trivy scan PASS', 'Sau mỗi stage trivy-scan', 'commit SHA, image ID, số CVE được phát hiện, số CVE waiver, thời gian scan', 'INFO', 'S3 WORM 90 ngày'],
    ['Trivy scan FAIL', 'Khi pipeline bị fail bởi CVE Critical', 'Toàn bộ CVE list (ID, CVSS, package, version), developer triggering, branch name', 'CRITICAL', 'S3 WORM 1 năm'],
    ['Terrascan PASS', 'Sau mỗi stage terrascan-scan', 'Policy set version, số policy áp dụng, 0 violation confirmed', 'INFO', 'S3 WORM 90 ngày'],
    ['Terrascan FAIL', 'Khi có IaC violation HIGH/CRITICAL', 'Chi tiết violation (file, line, rule ID, mô tả), developer triggering', 'CRITICAL', 'S3 WORM 1 năm'],
    ['CVE Waiver tạo/sửa', 'Khi .trivyignore được commit', 'CVE-ID được waiver, lý do, ngày hết hạn, người approve (từ Git commit)', 'HIGH', 'S3 WORM 2 năm'],
    ['Image signing', 'Sau stage sign-push', 'Image digest, Cosign signature, SBOM hash, kube-chain attestation', 'INFO', 'S3 WORM 5 năm'],
    ['Deploy production', 'Khi ArgoCD sync vào crm-production', 'Người approve (GitLab MR approver), image digest được deploy, thời gian', 'HIGH', 'S3 WORM 5 năm'],
    ['Policy Rego thay đổi', 'Khi file Rego được merge vào main', 'Git diff của file Rego, người review, người approve', 'HIGH', 'S3 WORM 2 năm'],
  ];

  items.push(new Table({
    width: { size: 9200, type: WidthType.DXA },
    rows: auditRows.map((row, ri) => new TableRow({
      children: row.map((cell, ci) => {
        if (ri === 0) return hCell(cell, [1800, 1800, 2600, 900, 1100][ci]);
        const shade = row[3] === 'CRITICAL' ? 'FF9090' : row[3] === 'HIGH' ? ORANGE_BG : alt(ri);
        return bCell(cell, [1800, 1800, 2600, 900, 1100][ci], shade, ci === 0);
      }),
    })),
  }));
  items.push(blankLine());

  items.push(heading3('4.3.2. Tuân thủ pháp lý Việt Nam'));

  items.push(p([t('Giải pháp DevSecOps GitOps đề xuất đáp ứng trực tiếp các quy định pháp luật bắt buộc đối với ngân hàng thương mại tại Việt Nam:')]));

  items.push(p([tb('Thông tư 09/2020/TT-NHNN (Điều 15 – Kiểm tra bảo mật): '),
    t('Yêu cầu thực hiện kiểm tra bảo mật ứng dụng trước khi đưa vào vận hành chính thức và định kỳ hàng năm. Pipeline Trivy + Terrascan thực hiện kiểm tra tự động '),
    tb('tại mỗi lần deploy'),
    t(', vượt xa yêu cầu "định kỳ hàng năm" của thông tư.')]));

  items.push(p([tb('Luật An toàn thông tin mạng 86/2015 (Điều 17 – Kiểm tra đánh giá): '),
    t('Yêu cầu kiểm tra, đánh giá hệ thống thông tin quan trọng trước khi khai thác, sử dụng. Trivy scan và Terrascan scan trong pipeline CI/CD hiện thực hóa yêu cầu này ở tầng kỹ thuật.')]));

  items.push(p([tb('Nghị định 13/2023/NĐ-CP (Điều 26 – Bảo mật dữ liệu cá nhân): '),
    t('Yêu cầu áp dụng các biện pháp kỹ thuật để bảo vệ dữ liệu cá nhân. Trivy secret scan ngăn chặn rò rỉ thông tin định danh khách hàng (PII) qua hardcoded credential; WORM Audit Log cung cấp bằng chứng tuân thủ khi có yêu cầu kiểm tra từ cơ quan có thẩm quyền.')]));

  items.push(p([tb('Luật An ninh mạng 24/2018 (Điều 26 – Lưu trữ dữ liệu): '),
    t('Yêu cầu lưu trữ dữ liệu tại Việt Nam. Toàn bộ artifact scan (Trivy JSON/SARIF, Terrascan report), WORM Audit Log, và SBOM được lưu trữ trên S3 WORM storage đặt tại datacenter của VietinBank ở Việt Nam.')]));

  items.push(heading3('4.3.3. Quản trị con người – Nhận thức bảo mật DevOps'));

  items.push(p([t('Công nghệ tốt nhất cũng chỉ hiệu quả khi đội ngũ con người hiểu và chấp nhận nó. Kế hoạch quản trị con người bao gồm:')]));

  items.push(p([tb('Đào tạo DevSecOps Awareness (hàng năm): '),
    t('Toàn bộ developer, DevOps engineer và QA engineer được đào tạo về: ý nghĩa của CVE và cách đọc Trivy report; cách viết Helm Chart bảo mật (securityContext, resource limits, NetworkPolicy); quy trình xin CVE waiver đúng cách; tác hại của hardcoded secret.')]));

  items.push(p([tb('Secure Coding Guideline cho IaC: '),
    t('VietinBank ban hành tài liệu hướng dẫn viết Helm Chart an toàn, bao gồm template mẫu đã được pre-configured với đầy đủ securityContext, resource limits, và các annotation bảo mật. Developer chỉ cần thay đổi giá trị cụ thể của ứng dụng, không cần tự viết lại từ đầu.')]));

  items.push(p([tb('KPI Bảo mật cho team DevOps: '),
    t('Số lượng CVE Critical tồn đọng trong production (target: 0); thời gian trung bình từ khi CVE được công bố đến khi được vá (target: < 30 ngày); số lần pipeline bị fail do IaC misconfiguration (target: giảm 50% mỗi quý). Các KPI này được báo cáo hàng tháng lên CISO.')]));

  items.push(pageBreak());

  // ══════════════════════════════════════════════════════════
  // KẾT LUẬN
  // ══════════════════════════════════════════════════════════
  items.push(heading1('KẾT LUẬN'));

  items.push(p([t('Bài tập lớn này đã hoàn thành một cách toàn diện mục tiêu nghiên cứu đặt ra: thiết kế và đề xuất giải pháp tự động hoá đánh giá an ninh hạ tầng mã nguồn (IaC) và Container Image trong quy trình GitOps cho hệ thống CRM 1.0 của VietinBank, qua đó lấp đầy khoảng trống Shift-Left Security còn tồn tại sau bài tập giữa kỳ và hoàn thiện bức tranh bảo mật toàn vòng đời phần mềm theo yêu cầu đề bài môn học.')]));

  items.push(p([tb('Về lý thuyết: '),
    t('Nghiên cứu đã hệ thống hóa mô hình Phòng vệ chiều sâu mở rộng lên 8 tầng với tầng System Integrity (Build/Supply Chain) là phát kiến chính, khẳng định rằng bảo mật Runtime không thể tách rời bảo mật Build-time. Khung OWASP Top 10 CI/CD Security Risks được ánh xạ cụ thể vào kiến trúc CRM 1.0, tạo nền tảng phân tích rủi ro sắc bén.')]));

  items.push(p([tb('Về phân tích rủi ro: '),
    t('Ma trận rủi ro 8 sự kiện đe dọa được xây dựng theo phương pháp 9 bước NIST SP 800-30, với hai rủi ro ưu tiên cao nhất được phân tích chuyên sâu: CVE Critical trong Container Image (Risk Score 20/25) và container chạy root leo thang node (16/25). Kết quả phân tích cung cấp cơ sở định lượng rõ ràng để ưu tiên đầu tư bảo mật.')]));

  items.push(p([tb('Về giải pháp kỹ thuật: '),
    t('Pipeline GitOps 9 stage được thiết kế với 3 stage bảo mật mới (trivy-scan, terrascan-scan, sign-push). Sáu đoạn mã tham khảo cụ thể được cung cấp: cấu hình Trivy trong GitLab CI/CD với CVE Waiver mechanism; ba policy Rego tùy chỉnh cho VietinBank (non-root, no-privileged, resource-limits); cấu hình Terrascan; và RBAC least privilege cho GitLab Runner ServiceAccount. Bảng ánh xạ Rủi ro ↔ Giải pháp (Bảng 3.2) đảm bảo không có rủi ro nào bị bỏ sót.')]));

  items.push(p([tb('Về thực nghiệm PoC: '),
    t('Hai kịch bản PoC cụ thể với output pipeline mô phỏng đã xác nhận rằng giải pháp hoạt động đúng như thiết kế: Trivy phát hiện và chặn image có CVE-2023-0464 (CRITICAL); Terrascan phát hiện và báo cáo 4 vi phạm policy trong Helm Chart, bao gồm container chạy root, thiếu resource limits, và tag :latest.')]));

  items.push(p([tb('Về quản trị: '),
    t('Khung ISMS ISO/IEC 27001 được hoàn thiện với vòng lặp PDCA tích hợp đầy đủ hoạt động DevSecOps. WORM Audit Log được mở rộng ghi nhận 8 loại sự kiện bảo mật mới trong pipeline. Toàn bộ giải pháp đáp ứng đồng thời Thông tư 09/2020/TT-NHNN, Luật ATTT Mạng 86/2015, Nghị định 13/2023/NĐ-CP và Luật An ninh mạng 24/2018.')]));

  items.push(p([t('Kết hợp với kiến trúc Runtime đã được xây dựng trong bài giữa kỳ, VietinBank hiện có một kiến trúc bảo mật toàn diện theo mô hình '),
    tb('Security Everywhere'),
    t(': từ khi developer gõ dòng code đầu tiên (Policy-as-Code), qua quá trình build và đóng gói (Trivy + Terrascan Hard Gate), ký số và xác thực (Cosign + Quay), triển khai có kiểm soát (ArgoCD + GitOps), cho đến vận hành và giám sát (Istio mTLS + Falco + SOC/SIEM). Đây là câu trả lời xuất sắc và hoàn chỉnh cho đề bài '),
    tb('"Đề xuất kiến trúc chung và các giải pháp để bảo mật hệ thống thông tin cho 01 doanh nghiệp/tổ chức cụ thể."')]));

  items.push(p([tb('Hướng phát triển tiếp theo: '),
    t('(i) Tích hợp '),
    tb('Sigstore Rekor'),
    t(' transparency log để tạo audit trail công khai không thể giả mạo cho toàn bộ artifact; (ii) Triển khai '),
    tb('Trivy Operator'),
    t(' trên OpenShift để quét liên tục tất cả image đang chạy và tự động tạo VulnerabilityReport CRD; (iii) Xây dựng '),
    tb('SBOM Registry'),
    t(' tập trung để quản lý dependency toàn bộ portfolio ứng dụng của VietinBank; (iv) Mở rộng mô hình sang các hệ thống Banking Core và Digital Banking trong khuôn khổ chiến lược Open Banking của VietinBank đến năm 2030.')]));

  // Tài liệu tham khảo
  items.push(heading1('TÀI LIỆU THAM KHẢO'));

  const refs = [
    '[1] NIST SP 800-30 Rev.1 (2012). Guide for Conducting Risk Assessments. National Institute of Standards and Technology.',
    '[2] NIST SP 800-160 Vol. 2 Rev.1 (2021). Developing Cyber-Resilient Systems: A Systems Security Engineering Approach.',
    '[3] NIST SP 800-190 (2017). Application Container Security Guide. National Institute of Standards and Technology.',
    '[4] OWASP (2022). Top 10 CI/CD Security Risks. Open Web Application Security Project. https://owasp.org/www-project-top-10-ci-cd-security-risks/',
    '[5] ISO/IEC 27001:2022. Information security, cybersecurity and privacy protection – Information security management systems – Requirements.',
    '[6] CIS Kubernetes Benchmark v1.8.0 (2023). Center for Internet Security.',
    '[7] Aqua Security (2024). Trivy Documentation – Comprehensive security scanner. https://trivy.dev',
    '[8] Tenable (2024). Terrascan Documentation. https://runterrascan.io',
    '[9] Open Policy Agent (2024). OPA Documentation and Rego Language Reference. https://www.openpolicyagent.org',
    '[10] Palo Alto Networks (2023). State of Cloud Native Security Report 2023.',
    '[11] Gartner (2024). How to Manage the Growing Risk of Software Supply Chain Attacks.',
    '[12] Red Hat (2024). OpenShift Security Guide – Security Context Constraints (SCC).',
    '[13] CISA & NSA (2022). Kubernetes Hardening Guidance. Cybersecurity and Infrastructure Security Agency.',
    '[14] Ngân hàng Nhà nước Việt Nam (2020). Thông tư 09/2020/TT-NHNN về an toàn hệ thống thông tin trong hoạt động ngân hàng.',
    '[15] Quốc hội Việt Nam (2015). Luật An toàn thông tin mạng số 86/2015/QH13.',
    '[16] Quốc hội Việt Nam (2018). Luật An ninh mạng số 24/2018/QH14.',
    '[17] Chính phủ Việt Nam (2023). Nghị định 13/2023/NĐ-CP về bảo vệ dữ liệu cá nhân.',
    '[18] Sigstore (2024). Cosign – Container Signing and Verification. https://docs.sigstore.dev',
    '[19] SLSA (Supply-chain Levels for Software Artifacts) (2024). Framework Overview. https://slsa.dev',
    '[20] GitLab (2024). GitLab CI/CD Security Integration Documentation. https://docs.gitlab.com/ee/user/application_security/',
  ];

  refs.forEach(ref => {
    items.push(pNoIndent([new TextRun({ text: ref, font: FONT, size: 24 })], {
      spacing: { after: 100, line: 300, lineRule: 'auto' },
      indent: { left: 360, hanging: 360 },
    }));
  });

  return items;
}

module.exports = { buildChapter4AndConclusion };
