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
function buildChapter3() {
  const items = [];

  items.push(heading1('CHƯƠNG 3: ĐỀ XUẤT TÍCH HỢP TRIVY VÀ TERRASCAN VÀO QUY TRÌNH GITOPS'));

  // 3.1 ──────────────────────────────────────────────────────
  items.push(heading2('3.1. Thiết kế pipeline GitOps mới cho CRM 1.0'));

  items.push(heading3('3.1.1. Nguyên tắc thiết kế'));

  items.push(p([t('Pipeline mới được thiết kế theo bốn nguyên tắc cốt lõi: '),
    tb('(i) Fail Fast'),
    t(' – kiểm tra bảo mật được thực hiện sớm nhất có thể trong pipeline, để phát hiện vấn đề khi chi phí sửa chữa còn thấp; '),
    tb('(ii) Hard Gate'),
    t(' – pipeline tự động dừng (exit code ≠ 0) khi phát hiện lỗ hổng Critical/High, không cho phép tiếp tục deploy cho đến khi vấn đề được giải quyết hoặc có exception được duyệt; '),
    tb('(iii) Least Privilege Pipeline'),
    t(' – service account của GitLab Runner chỉ có quyền push image lên Quay, không có quyền trực tiếp vào OpenShift cluster (CD do ArgoCD đảm nhiệm); '),
    tb('(iv) Evidence-based Compliance'),
    t(' – mọi kết quả scan (JSON/SARIF) được lưu trữ như artifact pipeline, tạo audit trail cho kiểm toán ISO 27001 và Thông tư 09/2020.')]));

  items.push(heading3('3.1.2. Sơ đồ pipeline mới (9 stage)'));

  items.push(p([t('Pipeline GitOps mới cho CRM 1.0 bổ sung 3 stage bảo mật (tô đậm) vào pipeline hiện tại:')]));

  items.push(pNoIndent([tb('Stage 1 – compile: '), t('Build source code, resolve dependency (Maven/npm). Artifact: JAR/node_modules.')], { indent: { left: 360 } }));
  items.push(pNoIndent([tb('Stage 2 – test: '), t('Unit test + SonarQube SAST. Gate: quality gate SonarQube PASS.')], { indent: { left: 360 } }));
  items.push(pNoIndent([tb('Stage 3 – build-image: '), t('Buildah build container image, tag với commit SHA. Không push lên registry.')], { indent: { left: 360 } }));
  items.push(pNoIndent([new TextRun({ text: 'Stage 4 – trivy-scan (MỚI): ', font: FONT, size: SZ, bold: true, color: '2E74B5' }),
    t('Trivy quét image vừa build: CVE scan + Secret scan. Hard gate: CRITICAL CVE → fail pipeline.')], { indent: { left: 360 } }));
  items.push(pNoIndent([new TextRun({ text: 'Stage 5 – terrascan-scan (MỚI): ', font: FONT, size: SZ, bold: true, color: '2E74B5' }),
    t('Terrascan quét Helm Chart trong gitops-infra repo. Hard gate: CRITICAL/HIGH policy violation → fail pipeline.')], { indent: { left: 360 } }));
  items.push(pNoIndent([tb('Stage 6 – sign-push: '), t('Cosign ký số image → push image đã ký lên Quay registry với SBOM attestation.')], { indent: { left: 360 } }));
  items.push(pNoIndent([new TextRun({ text: 'Stage 7 – update-gitops (MỚI): ', font: FONT, size: SZ, bold: true, color: '2E74B5' }),
    t('Cập nhật image tag trong gitops-infra repo → tạo Merge Request tự động → ArgoCD phát hiện và sync.')], { indent: { left: 360 } }));
  items.push(pNoIndent([tb('Stage 8 – deploy-staging: '), t('ArgoCD sync vào namespace crm-staging. Integration test tự động.')], { indent: { left: 360 } }));
  items.push(pNoIndent([tb('Stage 9 – deploy-prod: '), t('Manual approval required. ArgoCD sync vào crm-production sau khi được duyệt.')], { indent: { left: 360 } }));
  items.push(blankLine());

  items.push(p([t('Điểm khác biệt then chốt so với pipeline cũ: stage trivy-scan và terrascan-scan được thực hiện '),
    tb('TRƯỚC khi push image lên registry'),
    t('. Điều này đảm bảo rằng image bị lỗi bảo mật không bao giờ tồn tại trong registry, loại trừ hoàn toàn khả năng image đó vô tình được deploy bởi một pipeline khác.')]));

  // 3.2 ──────────────────────────────────────────────────────
  items.push(heading2('3.2. Cấu hình Trivy – Quét CVE và Secret'));

  items.push(heading3('3.2.1. Cấu hình Trivy trong GitLab CI/CD'));

  items.push(p([t('Trivy được tích hợp vào pipeline thông qua Docker image chính thức '),
    tb('aquasec/trivy:latest'),
    t('. Để tránh phụ thuộc mạng trong môi trường CI isolated của VietinBank, Trivy DB được mirror nội bộ vào một OCI registry private (Red Hat Quay), và GitLab Runner được cấu hình để pull DB từ đó thay vì từ ghcr.io công cộng.')]));

  items.push(codeCaption('Đoạn mã 3.1. Stage trivy-scan trong .gitlab-ci.yml'));

  items.push(...codeBlock([
    '# .gitlab-ci.yml – Stage: trivy-scan',
    '# Quét CVE + Secret trong container image vừa build',
    '',
    'trivy-scan:',
    '  stage: trivy-scan',
    '  image: aquasec/trivy:latest',
    '  variables:',
    '    # Mirror DB nội bộ – không cần internet',
    '    TRIVY_DB_REPOSITORY: "quay.vietinbank.local/aquasec/trivy-db:2"',
    '    TRIVY_JAVA_DB_REPOSITORY: "quay.vietinbank.local/aquasec/trivy-java-db:1"',
    '    TRIVY_NO_PROGRESS: "true"',
    '    TRIVY_CACHE_DIR: "/tmp/trivy-cache"',
    '  before_script:',
    '    # Login Quay internal registry',
    '    - trivy image --download-db-only',
    '  script:',
    '    # ── 1. CVE Scan với Hard Gate ────────────────────────────────────────',
    '    - |',
    '      trivy image \\',
    '        --exit-code 1 \\',
    '        --severity CRITICAL \\',
    '        --ignore-unfixed \\',
    '        --format sarif \\',
    '        --output trivy-cve-report.sarif \\',
    '        "${CI_REGISTRY_IMAGE}:${CI_COMMIT_SHA}-build"',
    '    # ── 2. Full report (HIGH+CRITICAL) để lưu artifact ──────────────────',
    '    - |',
    '      trivy image \\',
    '        --exit-code 0 \\',
    '        --severity HIGH,CRITICAL \\',
    '        --ignore-unfixed \\',
    '        --format json \\',
    '        --output trivy-cve-full.json \\',
    '        "${CI_REGISTRY_IMAGE}:${CI_COMMIT_SHA}-build"',
    '    # ── 3. Secret Scan ───────────────────────────────────────────────────',
    '    - |',
    '      trivy image \\',
    '        --exit-code 1 \\',
    '        --scanners secret \\',
    '        --format json \\',
    '        --output trivy-secret-report.json \\',
    '        "${CI_REGISTRY_IMAGE}:${CI_COMMIT_SHA}-build"',
    '  after_script:',
    '    # Ghi audit log vào WORM storage (tích hợp với kiến trúc giữa kỳ)',
    '    - ./scripts/upload-scan-artifact.sh trivy-cve-report.sarif',
    '    - ./scripts/upload-scan-artifact.sh trivy-secret-report.json',
    '  artifacts:',
    '    when: always',
    '    reports:',
    '      sast: trivy-cve-report.sarif',
    '    paths:',
    '      - trivy-cve-full.json',
    '      - trivy-secret-report.json',
    '    expire_in: 90 days    # Giữ 90 ngày cho audit trail',
    '  allow_failure: false    # Hard Gate – pipeline fail nếu có CRITICAL CVE',
  ]));
  items.push(blankLine());

  items.push(heading3('3.2.2. Cơ chế xử lý exception (CVE Waiver)'));

  items.push(p([t('Trong thực tế vận hành, không phải mọi CVE Critical đều có thể vá ngay lập tức – đặc biệt khi bản vá chưa tồn tại hoặc khi việc nâng cấp phá vỡ tính tương thích. Để tránh việc pipeline bị blocked mãi mãi, một cơ chế '),
    tb('CVE Waiver'),
    t(' được thiết lập: team Security tạo file '),
    tb('.trivyignore'),
    t(' trong repository, chứa danh sách CVE-ID được tạm thời bỏ qua kèm lý do và ngày hết hạn waiver.')]));

  items.push(codeCaption('Đoạn mã 3.2. File .trivyignore – Danh sách CVE được waiver tạm thời'));

  items.push(...codeBlock([
    '# .trivyignore',
    '# Format: CVE-ID  # WAIVER: <lý do> | EXPIRES: <YYYY-MM-DD> | APPROVED-BY: <tên>',
    '',
    '# Ví dụ: CVE trong libssl của Alpine, bản vá chưa có cho alpine:3.18',
    'CVE-2023-5678  # WAIVER: No fix available in alpine:3.18 | EXPIRES: 2026-09-01 | APPROVED-BY: security-team',
    '',
    '# Ví dụ: CVE trong org.springframework:spring-core, đã mitigate bằng WAF rule',
    'CVE-2024-1234  # WAIVER: Mitigated by WAF OWASP rule 941100 | EXPIRES: 2026-07-31 | APPROVED-BY: ciso',
  ]));
  items.push(blankLine());

  items.push(p([t('File '),
    tb('.trivyignore'),
    t(' được phiên bản hóa trong Git và mọi thay đổi phải qua Merge Request với approval từ team Security. GitLab CI tự động kiểm tra tất cả entry trong file: nếu có entry đã hết hạn (EXPIRES < ngày hiện tại), pipeline sẽ in cảnh báo và yêu cầu gia hạn.')]));

  // 3.3 ──────────────────────────────────────────────────────
  items.push(heading2('3.3. Cấu hình Terrascan – Kiểm tra chính sách IaC'));

  items.push(heading3('3.3.1. Cấu hình Terrascan trong GitLab CI/CD'));

  items.push(p([t('Terrascan được tích hợp vào stage '),
    tb('terrascan-scan'),
    t(', chạy song song với trivy-scan để tối ưu thời gian pipeline. Terrascan quét toàn bộ nội dung thư mục '),
    tb('helm/'),
    t(' trong repository gitops-infra, áp dụng hai tập policy: (i) built-in policy CIS Kubernetes Benchmark 1.8 và (ii) custom policy Rego đặc thù của VietinBank.')]));

  items.push(codeCaption('Đoạn mã 3.3. Stage terrascan-scan trong .gitlab-ci.yml'));

  items.push(...codeBlock([
    '# .gitlab-ci.yml – Stage: terrascan-scan',
    '# Quét IaC misconfiguration trong Helm Chart của CRM 1.0',
    '',
    'terrascan-scan:',
    '  stage: terrascan-scan',
    '  image: tenable/terrascan:latest',
    '  variables:',
    '    TERRASCAN_SEVERITY: "HIGH"    # Fail với HIGH và CRITICAL',
    '  script:',
    '    # ── 1. Scan với built-in CIS K8s policy ──────────────────────────────',
    '    - |',
    '      terrascan scan \\',
    '        --iac-type helm \\',
    '        --iac-dir ./helm \\',
    '        --policy-type k8s \\',
    '        --severity HIGH \\',
    '        --output json \\',
    '        > terrascan-builtin-report.json || BUILTIN_EXIT=$?',
    '    # ── 2. Scan với custom VietinBank policy (Rego) ───────────────────────',
    '    - |',
    '      terrascan scan \\',
    '        --iac-type helm \\',
    '        --iac-dir ./helm \\',
    '        --policy-path ./security-policies/rego \\',
    '        --severity HIGH \\',
    '        --output json \\',
    '        > terrascan-custom-report.json || CUSTOM_EXIT=$?',
    '    # ── 3. Fail pipeline nếu có violation ────────────────────────────────',
    '    - |',
    '      if [ "${BUILTIN_EXIT:-0}" != "0" ] || [ "${CUSTOM_EXIT:-0}" != "0" ]; then',
    '        echo "SECURITY GATE FAILED: IaC misconfiguration detected"',
    '        echo "Review reports: terrascan-builtin-report.json, terrascan-custom-report.json"',
    '        exit 3   # Exit code 3 = Terrascan violation found',
    '      fi',
    '  artifacts:',
    '    when: always',
    '    paths:',
    '      - terrascan-builtin-report.json',
    '      - terrascan-custom-report.json',
    '    expire_in: 90 days',
    '  allow_failure: false',
  ]));
  items.push(blankLine());

  items.push(heading3('3.3.2. Custom Policy Rego cho VietinBank'));

  items.push(p([t('Ngoài các policy built-in, VietinBank cần các policy tùy chỉnh phản ánh yêu cầu bảo mật đặc thù của ngành ngân hàng và kiến trúc CRM 1.0. Dưới đây là ba policy Rego quan trọng nhất:')]));

  items.push(codeCaption('Đoạn mã 3.4. Policy Rego 1: Bắt buộc container chạy non-root (vietinbank_nonroot.rego)'));

  items.push(...codeBlock([
    '# security-policies/rego/vietinbank_nonroot.rego',
    '# Policy: Container phải chạy với user không phải root (UID != 0)',
    '# Compliance: CIS Kubernetes Benchmark 5.2.6, VietinBank Security Policy VTB-SEC-K8S-001',
    '',
    'package vietinbank.k8s.nonroot',
    '',
    'import future.keywords.in',
    '',
    '# Metadata cho Terrascan report',
    'policy = {',
    '  "name": "VTB-SEC-K8S-001",',
    '  "file": "vietinbank_nonroot.rego",',
    '  "severity": "HIGH",',
    '  "description": "Container phai chay voi non-root user (runAsNonRoot: true)",',
    '  "reference_id": "VTB-SEC-K8S-001",',
    '}',
    '',
    '# Deny nếu securityContext ở cấp pod KHÔNG có runAsNonRoot: true',
    'deny[msg] {',
    '  input.kind == "Deployment"',
    '  pod_spec := input.spec.template.spec',
    '  not pod_spec.securityContext.runAsNonRoot == true',
    '  msg := sprintf(',
    '    "VTB-SEC-K8S-001: Deployment [%v] thieu securityContext.runAsNonRoot: true o cap pod",',
    '    [input.metadata.name]',
    '  )',
    '}',
    '',
    '# Deny nếu container cụ thể KHÔNG có runAsNonRoot: true',
    'deny[msg] {',
    '  input.kind == "Deployment"',
    '  container := input.spec.template.spec.containers[_]',
    '  not container.securityContext.runAsNonRoot == true',
    '  msg := sprintf(',
    '    "VTB-SEC-K8S-001: Container [%v] trong Deployment [%v] thieu securityContext.runAsNonRoot: true",',
    '    [container.name, input.metadata.name]',
    '  )',
    '}',
  ]));
  items.push(blankLine());

  items.push(codeCaption('Đoạn mã 3.5. Policy Rego 2: Cấm privileged container và hostPath mount (vietinbank_no_privileged.rego)'));

  items.push(...codeBlock([
    '# security-policies/rego/vietinbank_no_privileged.rego',
    '# Policy: Cam container chay privileged va hostPath mount',
    '# Compliance: CIS Kubernetes Benchmark 5.2.1, 5.2.2',
    '',
    'package vietinbank.k8s.no_privileged',
    '',
    '# Deny privileged container',
    'deny[msg] {',
    '  input.kind == "Deployment"',
    '  container := input.spec.template.spec.containers[_]',
    '  container.securityContext.privileged == true',
    '  msg := sprintf(',
    '    "VTB-SEC-K8S-002: Container [%v] cau hinh privileged=true. CAM su dung trong CRM production.",',
    '    [container.name]',
    '  )',
    '}',
    '',
    '# Deny hostPath volume',
    'deny[msg] {',
    '  input.kind == "Deployment"',
    '  volume := input.spec.template.spec.volumes[_]',
    '  volume.hostPath',
    '  msg := sprintf(',
    '    "VTB-SEC-K8S-003: Deployment [%v] su dung hostPath volume [%v]. Nguy co lo ro filesystem node.",',
    '    [input.metadata.name, volume.name]',
    '  )',
    '}',
    '',
    '# Deny hostNetwork',
    'deny[msg] {',
    '  input.kind == "Deployment"',
    '  input.spec.template.spec.hostNetwork == true',
    '  msg := sprintf(',
    '    "VTB-SEC-K8S-004: Deployment [%v] su dung hostNetwork=true. Vi pham network isolation.",',
    '    [input.metadata.name]',
    '  )',
    '}',
  ]));
  items.push(blankLine());

  items.push(codeCaption('Đoạn mã 3.6. Policy Rego 3: Bắt buộc resource limits và non-latest image tag (vietinbank_resource_limits.rego)'));

  items.push(...codeBlock([
    '# security-policies/rego/vietinbank_resource_limits.rego',
    '# Policy: Bat buoc resource limits va cam dung image tag :latest',
    '',
    'package vietinbank.k8s.resource_limits',
    '',
    '# Deny container khong co resource limits (nguy co DoS)',
    'deny[msg] {',
    '  input.kind == "Deployment"',
    '  container := input.spec.template.spec.containers[_]',
    '  not container.resources.limits.cpu',
    '  msg := sprintf(',
    '    "VTB-SEC-K8S-005: Container [%v] thieu resources.limits.cpu. Nguy co resource exhaustion.",',
    '    [container.name]',
    '  )',
    '}',
    '',
    'deny[msg] {',
    '  input.kind == "Deployment"',
    '  container := input.spec.template.spec.containers[_]',
    '  not container.resources.limits.memory',
    '  msg := sprintf(',
    '    "VTB-SEC-K8S-005: Container [%v] thieu resources.limits.memory.",',
    '    [container.name]',
    '  )',
    '}',
    '',
    '# Deny image tag :latest (bao dam immutable deployment)',
    'deny[msg] {',
    '  input.kind == "Deployment"',
    '  container := input.spec.template.spec.containers[_]',
    '  endswith(container.image, ":latest")',
    '  msg := sprintf(',
    '    "VTB-SEC-K8S-006: Container [%v] dung image tag :latest. Phai dung digest sha256.",',
    '    [container.name]',
    '  )',
    '}',
  ]));
  items.push(blankLine());

  // 3.4 ──────────────────────────────────────────────────────
  items.push(heading2('3.4. Quản lý phân quyền RBAC cho pipeline'));

  items.push(heading3('3.4.1. Nguyên tắc Least Privilege cho GitLab Runner'));

  items.push(p([t('GitLab Runner cần quyền truy cập vào một số tài nguyên trong quá trình CI: build image (cần Docker socket hoặc Buildah), push image lên Quay, và cập nhật gitops-infra repository. Theo nguyên tắc Least Privilege, mỗi quyền phải được cấp tối thiểu và tách biệt.')]));

  items.push(codeCaption('Đoạn mã 3.7. OpenShift ServiceAccount và RBAC cho GitLab Runner'));

  items.push(...codeBlock([
    '# rbac/gitlab-runner-sa.yaml',
    '# ServiceAccount cho GitLab Runner trong namespace crm-cicd',
    '',
    'apiVersion: v1',
    'kind: ServiceAccount',
    'metadata:',
    '  name: gitlab-runner-sa',
    '  namespace: crm-cicd',
    '  annotations:',
    '    description: "ServiceAccount cho GitLab Runner – chi co quyen build va push image"',
    '---',
    '# ClusterRole chi cho phep doc ConfigMap/Secret cua namespace cicd',
    'apiVersion: rbac.authorization.k8s.io/v1',
    'kind: Role',
    'metadata:',
    '  name: gitlab-runner-role',
    '  namespace: crm-cicd',
    'rules:',
    '  # Cho phep doc Secret de lay registry credential',
    '  - apiGroups: [""]',
    '    resources: ["secrets"]',
    '    verbs: ["get"]',
    '    resourceNames: ["quay-registry-secret", "vault-approle-secret"]',
    '  # Cho phep doc ConfigMap cau hinh pipeline',
    '  - apiGroups: [""]',
    '    resources: ["configmaps"]',
    '    verbs: ["get", "list"]',
    '---',
    'apiVersion: rbac.authorization.k8s.io/v1',
    'kind: RoleBinding',
    'metadata:',
    '  name: gitlab-runner-rolebinding',
    '  namespace: crm-cicd',
    'subjects:',
    '  - kind: ServiceAccount',
    '    name: gitlab-runner-sa',
    '    namespace: crm-cicd',
    'roleRef:',
    '  kind: Role',
    '  name: gitlab-runner-role',
    '  apiGroup: rbac.authorization.k8s.io',
    '# GitLab Runner KHONG co quyen deploy truc tiep vao crm-production',
    '# Deploy duoc thuc hien boi ArgoCD ServiceAccount rieng biet',
  ]));
  items.push(blankLine());

  items.push(heading3('3.4.2. Phân tách quyền CI và CD'));

  items.push(p([t('Kiến trúc GitOps phân tách hoàn toàn quyền của CI pipeline và CD operator:')]));

  // Bảng 3.1 – RBAC CI/CD
  items.push(caption('Bảng 3.1. Ma trận phân quyền RBAC cho pipeline GitOps CRM 1.0'));

  const rbacRows = [
    ['Thành phần', 'Namespace truy cập', 'Quyền được cấp', 'Quyền bị từ chối'],
    ['GitLab Runner SA\n(gitlab-runner-sa)', 'crm-cicd', 'Build image (Buildah)\nPush image lên Quay\nĐọc Secret registry\nCập nhật gitops-infra repo', 'Deploy vào crm-staging/production\nXóa/sửa Secret\nTạo/xóa Namespace\nTruy cập crm-production'],
    ['ArgoCD SA\n(argocd-application-controller)', 'crm-staging, crm-production', 'Apply/Update Deployment, Service\nSync Helm Chart\nĐọc image từ Quay (verified)', 'Thực thi code tùy ý\nSửa RBAC policy\nTruy cập etcd trực tiếp\nPush lên Git repository'],
    ['Developer\n(via GitLab MR)', 'crm-dev (kubectl limited)', 'Tạo/merge MR vào nhánh develop\nXem log pipeline\nXem scan report', 'Merge vào nhánh main/release\nApprove deploy production\nSửa .trivyignore trực tiếp'],
    ['Security Team\n(via GitLab MR)', 'Tất cả (read-only audit)', 'Approve exception (.trivyignore)\nXem tất cả scan report\nAudit pipeline history', 'Tự động approve MR vào production\nSửa policy Rego không qua review'],
  ];

  items.push(new Table({
    width: { size: 9200, type: WidthType.DXA },
    rows: rbacRows.map((row, ri) => new TableRow({
      children: row.map((cell, ci) => {
        if (ri === 0) return hCell(cell, [1600, 1600, 3200, 2800][ci]);
        const shade = ci === 3 ? ORANGE_BG : alt(ri);
        return bCell(cell, [1600, 1600, 3200, 2800][ci], shade, ci === 0);
      }),
    })),
  }));
  items.push(blankLine());

  // 3.5 – Risk-to-solution mapping
  items.push(heading2('3.5. Ánh xạ giải pháp với ma trận rủi ro'));

  items.push(caption('Bảng 3.2. Ánh xạ từng rủi ro CI/CD sang giải pháp kỹ thuật cụ thể'));

  const mapRows = [
    ['Mã RR', 'Rủi ro', 'Giải pháp kỹ thuật', 'Công cụ', 'Stage Pipeline'],
    ['A01', 'CVE Critical trong container image', 'Trivy --exit-code 1 --severity CRITICAL\nTrivy scheduled scan (hàng đêm)', 'Trivy', 'trivy-scan'],
    ['A02', 'Dependency Confusion / gói độc hại', 'Trivy SCA scan (--scanners vuln)\nNexus Repository proxy + allowlist', 'Trivy + Nexus', 'trivy-scan + compile'],
    ['A03', 'Container escape do privileged', 'Terrascan Rego: vietinbank_no_privileged.rego\nOCP SCC restricted-v2', 'Terrascan + OCP', 'terrascan-scan'],
    ['B01', 'Container chạy root leo thang node', 'Terrascan Rego: vietinbank_nonroot.rego\nOCP SCC runAsNonRoot enforcement', 'Terrascan + OCP', 'terrascan-scan'],
    ['B02', 'hostPath mount truy cập node filesystem', 'Terrascan Rego: vietinbank_no_privileged.rego\nOCP SCC: hostPath không được phép', 'Terrascan + OCP', 'terrascan-scan'],
    ['B03', 'Lateral movement thiếu NetworkPolicy', 'Terrascan kiểm tra NetworkPolicy tồn tại\nOCP NetworkPolicy Default-Deny (giữa kỳ)', 'Terrascan + Istio', 'terrascan-scan'],
    ['C01', 'Poisoned Pipeline Execution', 'GitLab branch protection: require 2 approvals\nGitLab Runner SA least privilege (§3.4)', 'GitLab RBAC', 'MR approval gate'],
    ['C02', 'Secret lộ qua CI/CD log', 'Trivy secret scan --exit-code 1\nGitLab masked variables; Vault dynamic secret', 'Trivy + Vault', 'trivy-scan'],
  ];

  items.push(new Table({
    width: { size: 9200, type: WidthType.DXA },
    rows: mapRows.map((row, ri) => new TableRow({
      children: row.map((cell, ci) => {
        if (ri === 0) return hCell(cell, [600, 2000, 3000, 1400, 2200][ci]);
        return bCell(cell, [600, 2000, 3000, 1400, 2200][ci], alt(ri), ci === 0);
      }),
    })),
  }));
  items.push(blankLine());

  items.push(pageBreak());
  return items;
}

module.exports = { buildChapter3 };
