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
function tb(text, opts = {}) { return new TextRun({ text, font: FONT, size: SZ, bold: true, ...opts }); }
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
function blankLine() { return new Paragraph({ children: [new TextRun('')], spacing: { after: 80 } }); }
function pageBreak() { return new Paragraph({ children: [new PageBreak()] }); }
function caption(text) {
  return pNoIndent([new TextRun({ text, font: FONT, size: 24, bold: true, italics: true })], {
    alignment: AlignmentType.CENTER,
    spacing: { before: 80, after: 160 },
  });
}

// Code block helper – monospace, gray background, bordered
function codeBlock(lines) {
  return lines.map(line => new Paragraph({
    children: [new TextRun({ text: line, font: CODE_FONT, size: 20 })],
    spacing: { after: 0, line: 280, lineRule: 'auto' },
    indent: { left: 360 },
    shading: { type: ShadingType.CLEAR, fill: 'F2F2F2' },
    border: {
      top: { style: BorderStyle.SINGLE, size: 1, color: 'CCCCCC' },
      bottom: { style: BorderStyle.SINGLE, size: 1, color: 'CCCCCC' },
      left: { style: BorderStyle.THICK, size: 8, color: '2E74B5' },
      right: { style: BorderStyle.SINGLE, size: 1, color: 'CCCCCC' },
    },
  }));
}

// Table helpers
const DARK_BLUE  = '1F3864';
const LIGHT_BLUE = 'DEEAF1';
const ORANGE_BG  = 'FCE4D6';
const RED_BG     = 'FF7070';
const YELLOW_BG  = 'FFFF99';
const GREEN_BG   = 'E2EFDA';

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
    shading: shade ? { type: ShadingType.CLEAR, fill: shade } : undefined,
    verticalAlign: VerticalAlign.CENTER,
    width: { size: width, type: WidthType.DXA },
  });
}
function cCell(text, width, shade = null, bold = false) { return bCell(text, width, shade, bold, true); }
function alt(i) { return i % 2 === 0 ? LIGHT_BLUE : null; }

// ─────────────────────────────────────────────────────────────────────────────
function buildChapter2() {
  const items = [];

  items.push(heading1('CHƯƠNG 2: PHÂN TÍCH RỦI RO HẠ TẦNG CI/CD CRM 1.0'));

  // 2.1 ──────────────────────────────────────────────────────
  items.push(heading2('2.1. Tổng quan CRM 1.0 và khoảng trống bảo mật CI/CD'));

  items.push(heading3('2.1.1. Kiến trúc tổng thể CRM 1.0'));

  items.push(p([t('Hệ thống CRM 1.0 của VietinBank là nền tảng quản lý quan hệ khách hàng thế hệ mới, được xây dựng theo kiến trúc Cloud-Native Microservices trên Red Hat OpenShift Container Platform (OCP). Hệ thống phục vụ hàng nghìn giao dịch khách hàng mỗi giờ, lưu trữ dữ liệu nhạy cảm bao gồm thông tin định danh khách hàng (PII), hồ sơ tài chính, lịch sử giao dịch và phân tích hành vi. Đặc điểm kiến trúc chính bao gồm:')]));

  items.push(p([tb('Frontend: '), t('NextJS v.14 với Server-Side Rendering (SSR), chạy trong container trên OCP, serve qua CDN và WAF (OWASP Core Rule Set).')]));
  items.push(p([tb('API Gateway: '), t('Kong Gateway và NGINX Ingress Controller xử lý routing, rate limiting, JWT validation, và ghi audit log request/response.')]));
  items.push(p([tb('Microservices: '), t('Khoảng 12–15 Java Spring Boot microservice độc lập, giao tiếp qua Apache Kafka (event-driven, CDC) và REST API nội bộ với mTLS (Istio Service Mesh). Bao gồm các service: Customer Profile, Account Management, Transaction History, Analytics, Notification, Document Management, v.v.')]));
  items.push(p([tb('Data layer: '), t('PostgreSQL (dữ liệu transactional chính), Oracle (kế thừa từ Core Banking), Redis (cache session), S3-compatible WORM storage (audit log, document lưu trữ dài hạn).')]));
  items.push(p([tb('Hạ tầng IaC: '), t('Toàn bộ manifest Kubernetes/OpenShift được quản lý bằng Helm Chart, versioned trong GitLab repository riêng (gitops-infra). Terraform được dùng để provisioning tài nguyên nền tảng (namespace, quota, secret, route).')]));
  items.push(p([tb('CI/CD: '), t('GitLab CI/CD với các stage: Compile → Unit Test → SonarQube SAST → Build Image → Push Image → Deploy to Dev → Integration Test → Deploy to Staging → Deploy to Production (manual approval).')]));

  items.push(heading3('2.1.2. Khoảng trống bảo mật trong pipeline hiện tại'));

  items.push(p([t('Bài tập giữa kỳ đã phân tích pipeline CI/CD hiện tại và xác định một khoảng trống nghiêm trọng: trong toàn bộ 9 stage của pipeline, chỉ có giai đoạn SonarQube thực hiện kiểm tra bảo mật, và SonarQube chỉ quét '),
    tb('mã nguồn ứng dụng (SAST)'),
    t(' – không quét Container Image, không kiểm tra Helm Chart, không phát hiện secret bị hardcode trong Dockerfile. Điều này tạo ra ba khoảng trống cụ thể:')]));

  items.push(p([tb('Khoảng trống 1 – Container Image CVE: '),
    t('Sau khi image được build từ Dockerfile và push lên Red Hat Quay registry, không có bước nào kiểm tra xem image đó có chứa OS package hoặc language dependency với CVE nghiêm trọng hay không. Image có thể chứa hàng chục CVE High/Critical mà không ai biết cho đến khi có sự cố.')]));

  items.push(p([tb('Khoảng trống 2 – IaC Misconfiguration: '),
    t('Các file Helm Chart và Kubernetes YAML trong repository gitops-infra không được quét bởi bất kỳ công cụ nào. Sai cấu hình như container chạy root, thiếu resource limit, hostPath mount, hay thiếu NetworkPolicy có thể tồn tại trong production mà không bị phát hiện.')]));

  items.push(p([tb('Khoảng trống 3 – Secret Detection: '),
    t('Không có công cụ nào chủ động quét xem có credential, API key, hay private key nào bị hardcode trong Dockerfile, file YAML, hay file .env đã commit lên Git hay không.')]));

  // Bảng 2.1 – Tình trạng hiện tại pipeline
  items.push(caption('Bảng 2.1. Đánh giá hiện trạng bảo mật pipeline CI/CD CRM 1.0'));

  const pipelineRows = [
    ['Stage Pipeline', 'Công cụ hiện tại', 'Phạm vi kiểm tra', 'Bảo mật?', 'Khoảng trống'],
    ['Compile', 'Maven/npm', 'Compile errors', 'Không', 'Dependency CVE không được kiểm tra'],
    ['Unit Test', 'JUnit/Jest', 'Logic ứng dụng', 'Không', 'Không có security unit test'],
    ['SAST', 'SonarQube', 'Mã nguồn Java/JS', 'Một phần', 'Chỉ code smell, không scan IaC'],
    ['Build Image', 'Docker/Buildah', 'Tạo container image', 'Không', 'Image CVE không được kiểm tra'],
    ['Push Image', 'Quay Registry', 'Lưu trữ image', 'Không', 'Không có image signing/attestation'],
    ['Deploy Dev', 'Helm/ArgoCD', 'Deploy lên Dev OCP', 'Không', 'IaC misconfiguration không được phát hiện'],
    ['Integration Test', 'Selenium/Postman', 'Chức năng API', 'Không', 'Không có DAST'],
    ['Deploy Staging', 'Helm/ArgoCD', 'Deploy lên Staging', 'Không', 'Dùng cùng Helm Chart chưa được quét'],
    ['Deploy Prod', 'Helm/ArgoCD (manual)', 'Deploy lên Production', 'Không', 'Không có gate bảo mật cuối cùng'],
  ];

  items.push(new Table({
    width: { size: 9200, type: WidthType.DXA },
    rows: pipelineRows.map((row, ri) => new TableRow({
      children: row.map((cell, ci) => {
        if (ri === 0) return hCell(cell, [1600, 1400, 1600, 900, 3700][ci]);
        const isGap = (row[3] === 'Không') ? ORANGE_BG : null;
        const shade = ri === 0 ? null : (ci === 3 && row[3] === 'Một phần') ? YELLOW_BG : (ci === 3 && row[3] === 'Không') ? RED_BG : alt(ri);
        return bCell(cell, [1600, 1400, 1600, 900, 3700][ci], shade, ci === 0);
      }),
    })),
  }));
  items.push(blankLine());

  // 2.2 ──────────────────────────────────────────────────────
  items.push(heading2('2.2. Đánh giá rủi ro theo phương pháp 9 bước NIST SP 800-30'));

  items.push(p([t('Phương pháp đánh giá rủi ro 9 bước của NIST SP 800-30 Rev.1 (Guide for Conducting Risk Assessments) được áp dụng đặc biệt cho tầng CI/CD của CRM 1.0, bổ sung cho phân tích rủi ro tầng Runtime đã thực hiện trong bài giữa kỳ. Trọng tâm của phân tích là hai nhóm mối đe dọa chính: '),
    tb('(i) Tấn công chuỗi cung ứng phần mềm'),
    t(' và '),
    tb('(ii) Sai cấu hình hạ tầng IaC.')]));

  items.push(heading3('2.2.1. Các bước đánh giá rủi ro'));

  const steps = [
    ['Bước 1', 'Xác định mục đích đánh giá', 'Đánh giá rủi ro tại tầng Build/Deploy của pipeline CI/CD CRM 1.0, tập trung vào lỗ hổng Container Image và sai cấu hình IaC (Helm Chart, K8s YAML).'],
    ['Bước 2', 'Xác định phạm vi', 'Pipeline GitLab CI/CD, Helm Chart repository (gitops-infra), Red Hat Quay registry, OpenShift Namespace crm-production. Loại trừ tầng Runtime (đã xử lý giữa kỳ).'],
    ['Bước 3', 'Xác định giả định và hạn chế', 'Giả định: kẻ tấn công có thể truy cập public registry. Hạn chế: không có dữ liệu CVE thực của image hiện tại vì môi trường lab.'],
    ['Bước 4', 'Xác định nguồn thông tin', 'NVD (nvd.nist.gov), Trivy DB, OWASP Top 10 CI/CD, báo cáo Palo Alto State of Cloud Native Security 2023, Gartner Cloud Security Survey 2024.'],
    ['Bước 5', 'Xác định mô hình rủi ro', 'Risk = Likelihood × Impact (thang 1–5). Likelihood đánh giá theo khả năng khai thác thực tế; Impact đánh giá theo CIA Triad (Confidentiality, Integrity, Availability).'],
    ['Bước 6', 'Nhận diện nguồn nguy cơ', '(i) Kẻ tấn công bên ngoài: APT, crim group; (ii) Insider malicious; (iii) Nhà cung cấp phần mềm bị compromise; (iv) Lỗi vô ý của kỹ sư DevOps.'],
    ['Bước 7', 'Nhận diện sự kiện đe dọa', 'Xem Bảng 2.2 – 8 sự kiện đe dọa được xác định cho tầng CI/CD.'],
    ['Bước 8', 'Đánh giá và phân tích rủi ro', 'Xem Bảng 2.3 – Ma trận rủi ro với điểm số Likelihood × Impact và mức độ ưu tiên xử lý.'],
    ['Bước 9', 'Truyền thông kết quả', 'Báo cáo rủi ro được trình bày trong chương này; đề xuất kiểm soát chi tiết được xây dựng trong Chương 3.'],
  ];

  items.push(new Table({
    width: { size: 9200, type: WidthType.DXA },
    rows: [
      new TableRow({ children: [hCell('Bước', 1000), hCell('Tên bước', 2200), hCell('Áp dụng cho CRM 1.0 – Tầng CI/CD', 6000)] }),
      ...steps.map((row, ri) => new TableRow({
        children: [
          cCell(row[0], 1000, alt(ri), true),
          bCell(row[1], 2200, alt(ri), true),
          bCell(row[2], 6000, alt(ri)),
        ],
      })),
    ],
  }));
  items.push(blankLine());

  items.push(heading3('2.2.2. Nhận diện sự kiện đe dọa (Bước 7)'));

  items.push(p([t('Dựa trên kiến trúc CRM 1.0, OWASP Top 10 CI/CD Security Risks, và lịch sử các sự cố thực tế trong ngành tài chính, 8 sự kiện đe dọa được xác định cho tầng CI/CD, phân thành 3 nhóm:')]));

  items.push(p([tb('Nhóm A – Tấn công Container Image (A01–A03): '),
    t('Khai thác lỗ hổng CVE trong base image hoặc dependency; đưa malware vào image qua compromised base image; leo thang đặc quyền qua container escape do thiếu securityContext.')]));

  items.push(p([tb('Nhóm B – Tấn công IaC (B01–B03): '),
    t('Khai thác container chạy root để chiếm quyền worker node; leo thang qua hostPath mount truy cập filesystem node; vượt qua phân vùng namespace do thiếu NetworkPolicy.')]));

  items.push(p([tb('Nhóm C – Tấn công Pipeline (C01–C02): '),
    t('Poisoned Pipeline Execution (PPE) – chèn lệnh độc vào script CI/CD; rò rỉ secret (token, API key) qua log hoặc artifact không được bảo vệ.')]));

  // Bảng 2.3 – Ma trận rủi ro
  items.push(caption('Bảng 2.2. Ma trận rủi ro tổng hợp – Tầng CI/CD CRM 1.0'));

  const riskRows = [
    ['Mã', 'Sự kiện đe dọa', 'Nguồn nguy cơ', 'Lỗ hổng khai thác', 'L\n(1-5)', 'I\n(1-5)', 'R=L×I', 'Mức độ'],
    ['A01', 'CVE Critical trong base image NextJS/Java được khai thác', 'External APT / Crim group', 'Không có image CVE scan trong pipeline', '4', '5', '20', 'RẤT CAO'],
    ['A02', 'Dependency Confusion – gói npm/Maven độc hại được cài', 'External attacker', 'Không xác thực provenance của dependency', '3', '5', '15', 'CAO'],
    ['A03', 'Container escape do container chạy privileged', 'Insider / External', 'Helm Chart thiếu securityContext.privileged: false', '3', '5', '15', 'CAO'],
    ['B01', 'Container chạy root leo thang chiếm worker node', 'External post-breach', 'runAsNonRoot chưa được enforce trong IaC policy', '4', '4', '16', 'CAO'],
    ['B02', 'hostPath mount truy cập /etc/kubernetes trên node', 'Insider malicious', 'Thiếu Terrascan policy kiểm tra hostPath', '2', '5', '10', 'TRUNG BÌNH'],
    ['B03', 'Lateral movement qua namespace thiếu NetworkPolicy', 'External post-breach', 'NetworkPolicy Default-Deny chưa được verify trong IaC', '3', '4', '12', 'TRUNG BÌNH'],
    ['C01', 'PPE: merge request độc hại trigger pipeline với quyền cao', 'Insider / Compromised account', 'Thiếu branch protection và pipeline permission control', '2', '4', '8', 'TRUNG BÌNH'],
    ['C02', 'Secret (DB password, Vault token) lộ qua CI/CD log', 'External attacker / Insider', 'Không có secret detection scan; log unmasked', '3', '4', '12', 'TRUNG BÌNH'],
  ];

  const riskColors = {
    'RẤT CAO': 'FF7070',
    'CAO': ORANGE_BG,
    'TRUNG BÌNH': YELLOW_BG,
  };

  items.push(new Table({
    width: { size: 9200, type: WidthType.DXA },
    rows: riskRows.map((row, ri) => {
      if (ri === 0) return new TableRow({
        children: [
          hCell(row[0], 500), hCell(row[1], 2100), hCell(row[2], 1600), hCell(row[3], 2000),
          hCell(row[4], 500), hCell(row[5], 500), hCell(row[6], 500), hCell(row[7], 1500),
        ],
      });
      const shade = riskColors[row[7]] || alt(ri);
      return new TableRow({
        children: [
          cCell(row[0], 500, shade, true),
          bCell(row[1], 2100, shade),
          bCell(row[2], 1600, shade),
          bCell(row[3], 2000, shade),
          cCell(row[4], 500, shade),
          cCell(row[5], 500, shade),
          cCell(row[6], 500, shade, true),
          cCell(row[7], 1500, shade, true),
        ],
      });
    }),
  }));
  items.push(blankLine());

  items.push(p([t('Ghi chú: L = Likelihood (Xác suất xảy ra); I = Impact (Mức độ tác động); R = Risk Score. Thang điểm: 1–4 = Thấp/Trung bình; 5–9 = Vừa; 10–14 = Trung bình; 15–20 = Cao; >20 = Rất cao. Màu đỏ (≥15): ưu tiên xử lý ngay; Cam (10–14): xử lý trong sprint tiếp theo; Vàng (<10): kế hoạch cải thiện dài hạn.')]));

  // 2.3 ──────────────────────────────────────────────────────
  items.push(heading2('2.3. Phân tích chuyên sâu hai rủi ro ưu tiên cao nhất'));

  items.push(heading3('2.3.1. A01 – CVE Critical trong Container Image (Risk Score: 20/25)'));

  items.push(p([t('Đây là rủi ro có điểm số cao nhất trong ma trận. Xác suất xảy ra được đánh giá ở mức 4/5 vì theo báo cáo Trivy 2023, image '),
    tb('node:20-alpine'),
    t(' – base image tiêu chuẩn cho frontend NextJS – thường xuyên có 5–15 CVE mức High/Critical tại bất kỳ thời điểm nào, và đội ngũ phát triển CRM 1.0 hiện tại không có quy trình kiểm tra định kỳ. Mức độ tác động được đánh giá tối đa 5/5 vì:')]));

  items.push(p([tb('Về Confidentiality: '),
    t('Lỗ hổng RCE (Remote Code Execution) trong container NextJS có thể cho phép kẻ tấn công đọc JWT session token, customer PII, hoặc secret được inject vào environment variable của container.')]));

  items.push(p([tb('Về Integrity: '),
    t('RCE cho phép chỉnh sửa dữ liệu hiển thị trong giao diện CRM, có thể dẫn đến sai lệch thông tin khách hàng hoặc giao dịch gian lận.')]));

  items.push(p([tb('Về Availability: '),
    t('Kẻ tấn công có thể trigger resource exhaustion (CPU/Memory) qua lỗ hổng trong container, gây ảnh hưởng dịch vụ cho toàn bộ namespace CRM trên OpenShift.')]));

  items.push(p([t('Ví dụ minh họa thực tế: CVE-2021-44228 (Log4Shell) ảnh hưởng đến hàng triệu ứng dụng Java. Nếu microservice Java Spring Boot trong CRM 1.0 dùng Log4j 2.x mà không quét image, lỗ hổng này có thể bị khai thác từ xa qua một request JNDI lookup đơn giản trong header HTTP – một cuộc tấn công chỉ mất vài phút để thực hiện nhưng có thể mất nhiều ngày để phát hiện.')]));

  items.push(heading3('2.3.2. B01 – Container chạy root leo thang chiếm worker node (Risk Score: 16/25)'));

  items.push(p([t('Helm Chart mặc định của nhiều microservice Spring Boot không khai báo '),
    tb('securityContext'),
    t(', dẫn đến container chạy với UID 0 (root). Trong môi trường OpenShift, pod chạy root bị chặn bởi SCC (Security Context Constraints) mặc định – tuy nhiên, nếu team DevOps cấu hình SCC '),
    tb('anyuid'),
    t(' cho namespace (một thao tác phổ biến để "fix" lỗi permission) thì container có thể thực sự chạy root.')]));

  items.push(p([t('Khi container chạy root trong OpenShift, một lỗ hổng container escape (ví dụ CVE-2022-0811 runc breakout) cho phép kẻ tấn công thoát khỏi container và chiếm quyền root trên worker node. Từ đó, kẻ tấn công có thể: đọc Secret và ConfigMap của tất cả pod trên node đó; can thiệp vào etcd nếu node là control plane; hoặc sử dụng node như một foothold để tấn công lateral vào các namespace khác, bao gồm cả namespace Core Banking Adapter.')]));

  items.push(p([t('Terrascan policy kiểm tra thuộc tính này sẽ được trình bày chi tiết trong Chương 3 (mã Rego mẫu). Chính sách này hoạt động bằng cách parse Helm Chart thành Kubernetes manifest, sau đó kiểm tra trường '),
    tb('spec.containers[].securityContext.runAsNonRoot'),
    t(' và '),
    tb('spec.securityContext.runAsNonRoot'),
    t(' ở cả cấp pod và container.')]));

  items.push(pageBreak());
  return items;
}

module.exports = { buildChapter2 };
