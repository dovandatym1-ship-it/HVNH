// ================================================================
// CHƯƠNG 3: ĐỀ XUẤT KIẾN TRÚC VÀ GIẢI PHÁP KỸ THUẬT BẢO MẬT
// ================================================================
const {
  Paragraph, TextRun, Table, TableRow, TableCell,
  AlignmentType, HeadingLevel, BorderStyle, WidthType, ShadingType, PageBreak
} = require('docx');

const BORDER = { style: BorderStyle.SINGLE, size: 1, color: "AAAAAA" };
const BORDERS = { top: BORDER, bottom: BORDER, left: BORDER, right: BORDER };
const CM = { top: 80, bottom: 80, left: 120, right: 120 };
const LINE = { before: 80, after: 80, line: 360, lineRule: "auto" };

function hCell(text, w) {
  return new TableCell({ borders: BORDERS, width: { size: w, type: WidthType.DXA },
    shading: { fill: "1F3864", type: ShadingType.CLEAR }, margins: CM,
    children: [new Paragraph({ alignment: AlignmentType.CENTER,
      children: [new TextRun({ text, bold: true, color: "FFFFFF", size: 20, font: "Times New Roman" })] })] });
}
function bCell(text, w, shade, bold) {
  return new TableCell({ borders: BORDERS, width: { size: w, type: WidthType.DXA },
    shading: { fill: shade || "FFFFFF", type: ShadingType.CLEAR }, margins: CM,
    children: [new Paragraph({ children: [new TextRun({ text, size: 20, bold: !!bold, font: "Times New Roman" })] })] });
}
function cCell(text, w, shade, bold) {
  return new TableCell({ borders: BORDERS, width: { size: w, type: WidthType.DXA },
    shading: { fill: shade || "FFFFFF", type: ShadingType.CLEAR }, margins: CM,
    children: [new Paragraph({ alignment: AlignmentType.CENTER,
      children: [new TextRun({ text, size: 20, bold: !!bold, font: "Times New Roman" })] })] });
}
function alt(i) { return i % 2 === 0 ? "FFFFFF" : "EEF2F8"; }
function p(runs, ind) {
  return new Paragraph({ alignment: AlignmentType.BOTH, spacing: LINE,
    indent: ind || { firstLine: 720 }, children: runs });
}
function t(text, opts) { return new TextRun({ text, font: "Times New Roman", size: 26, ...opts }); }
function tb(text) { return t(text, { bold: true }); }
function blank() { return new Paragraph({ children: [new TextRun("")], spacing: { before: 60, after: 60 } }); }
function h1(text) {
  return new Paragraph({ heading: HeadingLevel.HEADING_1, spacing: { before: 400, after: 200 },
    children: [new TextRun({ text, bold: true, size: 32, font: "Times New Roman", color: "1F3864" })] });
}
function h2(text) {
  return new Paragraph({ heading: HeadingLevel.HEADING_2, spacing: { before: 320, after: 160 },
    children: [new TextRun({ text, bold: true, size: 28, font: "Times New Roman", color: "2E5096" })] });
}
function h3(text) {
  return new Paragraph({ heading: HeadingLevel.HEADING_3, spacing: { before: 240, after: 120 },
    children: [new TextRun({ text, bold: true, italics: true, size: 26, font: "Times New Roman", color: "1F3864" })] });
}
function caption(text) {
  return new Paragraph({ spacing: { before: 200, after: 80 }, alignment: AlignmentType.CENTER,
    children: [new TextRun({ text, bold: true, size: 22, italics: true, font: "Times New Roman" })] });
}

function buildChapter3() {
  const c = [];

  c.push(
    new Paragraph({ children: [new PageBreak()] }),
    h1("CHƯƠNG 3: ĐỀ XUẤT KIẾN TRÚC VÀ GIẢI PHÁP KỸ THUẬT BẢO MẬT CHO CRM 1.0"),
    blank(),
    p([t("Chương này trình bày các đề xuất kiến trúc và giải pháp kỹ thuật cụ thể nhằm giảm thiểu các rủi ro đã được nhận diện và đánh giá ở Chương 2. Mỗi đề xuất được thiết kế theo nguyên tắc "), tb("Defense in Depth"), t(" – xử lý rủi ro tại nhiều tầng đồng thời, không phụ thuộc vào sự hoàn hảo của bất kỳ một biện pháp đơn lẻ nào. Đặc biệt, các giải pháp được đặt trong tương quan trực tiếp với các rủi ro đã nhận diện (R01–R10) để đảm bảo tính truy xuất nguồn gốc (Traceability) trong quản lý rủi ro.")]),
    blank(),

    h2("3.1. Thiết kế kiến trúc phòng vệ nhiều lớp (Defense in Depth) cho CRM 1.0"),
    blank(),
    h3("3.1.1. Mô hình phân vùng mạng 3-Tier nghiêm ngặt"),
    p([t("Để xử lý rủi ro R02 (API Injection), R05 (DDoS) và R04 (Lateral Movement), kiến trúc đề xuất triển khai mô hình "), tb("phân vùng mạng 3-Tier"), t(" dựa trên nguyên tắc cô lập vùng tin cậy (Trust Zone Isolation). Ba tier được phân định rõ ràng bằng tường lửa và chính sách mạng nghiêm ngặt:")]),
    blank(),
    p([tb("Tier 1 – Vùng DMZ (Demilitarized Zone):"), t(" Đây là vùng \"vô chủ\" nằm giữa Internet và mạng nội bộ, chứa các thành phần phải tiếp xúc với lưu lượng bên ngoài: "), tb("WAF (Web Application Firewall)"), t(" phân tích và lọc mọi HTTP/HTTPS request từ iPay, eFast và trình duyệt của cán bộ; "), tb("DDoS Mitigation Appliance/Cloud Scrubbing"), t(" lọc lưu lượng tấn công volumetric; và "), tb("Load Balancer"), t(" phân phối tải đến API Gateway. Nguyên tắc vàng của DMZ: "), tb("không có kết nối trực tiếp từ Internet vào mạng nội bộ"), t(", mọi traffic phải đi qua ít nhất một lớp kiểm tra trong DMZ.")], { indent: { left: 360 } }),
    blank(),
    p([tb("Tier 2 – Vùng Application (Internal Network):"), t(" Chứa API Gateway và toàn bộ Worker Nodes OpenShift chạy các microservices. Vùng này chỉ nhận traffic đã được WAF và Load Balancer kiểm tra từ DMZ – không có kết nối trực tiếp nào từ Internet. Bên trong vùng này, "), tb("OpenShift NetworkPolicy"), t(" được áp dụng để thực thi nguyên tắc "), tb("Default-Deny East-West"), t(": mặc định không một microservice nào được phép gọi microservice khác, trừ khi được định nghĩa tường minh trong NetworkPolicy. Điều này cô lập hiệu quả các microservice trong trường hợp một service bị xâm nhập.")], { indent: { left: 360 } }),
    blank(),
    p([tb("Tier 3 – Vùng Database (Isolated Database Zone):"), t(" Cô lập hoàn toàn khỏi cả DMZ và một phần Application Zone. Các CSDL (PostgreSQL, Oracle, Redis) chỉ có thể được truy cập bởi các microservices tương ứng theo chính sách whitelist IP/Port nghiêm ngặt. "), tb("Không có microservice nào được kết nối trực tiếp đến CSDL của microservice khác"), t(" – đây là điểm then chốt trong mô hình Database per Service. NIPS (Network Intrusion Prevention System) được triển khai tại lớp mạng của tier này để phát hiện các query bất thường.")], { indent: { left: 360 } }),
    blank(),

    caption("Bảng 3.1: Ánh xạ rủi ro – Giải pháp kiến trúc phòng vệ theo 3-Tier"),
    new Table({
      width: { size: 9360, type: WidthType.DXA }, columnWidths: [600, 2200, 2000, 2360, 2200],
      rows: [
        new TableRow({ children: [hCell("Tier", 600), hCell("Vùng", 2200), hCell("Thành phần triển khai", 2000), hCell("Rủi ro được xử lý", 2360), hCell("Cơ chế kiểm soát", 2200)] }),
        ...([
          ["Tier 1", "DMZ (Public-Facing)", "WAF, DDoS Scrubber, Load Balancer", "R02 (SQLi/API Injection), R05 (DDoS)", "OWASP ruleset, Rate Limiting, IP Reputation"],
          ["Tier 1", "DMZ – API Entry", "API Gateway (Kong/NGINX)", "R06 (JWT Abuse), R02 (Auth Bypass)", "JWT Validation, OAuth2, Rate Limiting per user"],
          ["Tier 2", "Application Zone", "OpenShift Worker Nodes, Microservices", "R04 (Lateral Movement)", "NetworkPolicy Default-Deny, mTLS giữa services"],
          ["Tier 2", "Application Zone", "HIPS trên container, Runtime Security", "R08 (Supply Chain Attack)", "Falco Runtime Security, Seccomp/AppArmor profiles"],
          ["Tier 3", "Database Zone", "PostgreSQL, Oracle, Redis, S3 WORM", "R07 (Data Inconsistency), R01 (Insider)", "TDE, Row-Level Security, Audit Vault, WORM"],
        ]).map((row, i) => new TableRow({ children: [cCell(row[0], 600, alt(i), true), bCell(row[1], 2200, alt(i), true), bCell(row[2], 2000, alt(i)), bCell(row[3], 2360, alt(i)), bCell(row[4], 2200, alt(i))] }))
      ]
    }),
    blank(),

    h3("3.1.2. Triển khai mTLS – Xác thực lẫn nhau giữa các Microservices"),
    p([t("Để giải quyết triệt để rủi ro R04 (giao tiếp nội bộ không xác thực), kiến trúc đề xuất triển khai "), tb("Mutual TLS (mTLS)"), t(" cho toàn bộ giao tiếp East-West giữa các microservices trong cluster OpenShift, thông qua "), tb("Service Mesh (Istio)")  , t(". Trong mTLS, "), tb("cả hai phía"), t(" (client và server) đều phải xác thực chứng chỉ số của nhau trước khi thiết lập kết nối – khác với TLS thông thường chỉ có server xác thực danh tính. Với mTLS, ngay cả khi kẻ tấn công đã xâm nhập vào trong cluster, chúng cũng không thể giả mạo là một microservice hợp lệ để gọi các service khác, vì thiếu chứng chỉ số hợp lệ được phát hành bởi CA nội bộ.")]),
    blank(),
    p([t("Istio Service Mesh cung cấp khả năng triển khai mTLS ở chế độ "), tb("STRICT"), t(" (bắt buộc mTLS cho mọi giao tiếp trong mesh) mà không cần thay đổi code của ứng dụng – mTLS được xử lý ở tầng sidecar proxy (Envoy), hoàn toàn trong suốt với logic nghiệp vụ. Ngoài mTLS, Istio còn cung cấp "), tb("Authorization Policy"), t(" để định nghĩa tường minh service nào được phép gọi service nào, với granularity đến tầng HTTP method và path.")]),
    blank(),

    h2("3.2. Mã hóa và Bảo mật Dữ liệu"),
    blank(),
    h3("3.2.1. Bảo mật Dữ liệu lưu trữ (Data at Rest)"),
    p([t("Dữ liệu lưu trữ trong các CSDL của CRM 1.0 bao gồm thông tin cá nhân nhạy cảm và dữ liệu tài chính của hàng chục triệu khách hàng. Chiến lược mã hóa data at rest được đề xuất theo "), tb("mô hình phân lớp")  , t(":")]),
    blank(),
    p([tb("Tầng đĩa (Disk-level Encryption):"), t(" Toàn bộ block device lưu trữ dữ liệu của các CSDL được mã hóa bằng "), tb("AES-256-XTS"), t(" (chế độ tối ưu cho mã hóa đĩa) ở tầng Persistent Volume của OpenShift. Đây là lớp bảo vệ vật lý: nếu ổ đĩa vật lý bị đánh cắp hoặc retired mà không được xóa đúng cách, dữ liệu vẫn không thể đọc được.")], { indent: { left: 360 } }),
    blank(),
    p([tb("Tầng CSDL (TDE – Transparent Data Encryption):"), t(" Đối với PostgreSQL, sử dụng "), tb("pgcrypto"), t(" kết hợp với column-level encryption cho các trường dữ liệu siêu nhạy cảm (số CCCD, số hộ chiếu, số điện thoại). Đối với Oracle, kích hoạt "), tb("Oracle TDE"), t(" ở mức Tablespace để mã hóa toàn bộ tablespace chứa dữ liệu khách hàng với thuật toán AES-256-GCM. Quan trọng là khóa mã hóa (Master Encryption Key) không được lưu cùng với dữ liệu mà phải được quản lý trong "), tb("Hardware Security Module (HSM)"), t(" hoặc dịch vụ quản lý khóa tập trung (Key Management Service – KMS) đáp ứng tiêu chuẩn FIPS 140-2.")], { indent: { left: 360 } }),
    blank(),
    p([tb("Tầng ứng dụng (Application-level Encryption):"), t(" Một số trường dữ liệu cực kỳ nhạy cảm (mã PIN, số hợp đồng tín dụng CIC full) được mã hóa thêm ở tầng ứng dụng trước khi ghi xuống CSDL, sử dụng AES-256-GCM với khóa riêng biệt cho từng loại dữ liệu. Điều này đảm bảo rằng ngay cả DBA (Database Administrator) truy cập trực tiếp vào CSDL cũng không thể đọc được các trường này mà không có khóa ứng dụng – triển khai nguyên tắc "), tb("Separation of Duties"), t(" ở tầng dữ liệu.")], { indent: { left: 360 } }),
    blank(),

    h3("3.2.2. Bảo mật Dữ liệu truyền tải (Data in Transit)"),
    p([t("Chính sách đề xuất là "), tb("\"TLS Everywhere\""), t(" – mọi kênh truyền thông trong hệ thống đều phải sử dụng TLS 1.3, không có ngoại lệ:")]),
    blank(),
    p([tb("Kênh ngoại vi (External):"), t(" Giao tiếp giữa trình duyệt/ứng dụng mobile và API Gateway bắt buộc dùng "), tb("TLS 1.3"), t(" với suite mã hóa chỉ bao gồm các thuật toán mạnh (TLS_AES_256_GCM_SHA384, TLS_CHACHA20_POLY1305_SHA256). Chứng chỉ số sử dụng ECDSA-P256 (hiệu quả hơn RSA), được phát hành bởi CA uy tín và được "), tb("Certificate Pinning"), t(" trong ứng dụng iPay/eFast để ngăn chặn tấn công MITM ngay cả khi kẻ tấn công có chứng chỉ giả mạo.")], { indent: { left: 360 } }),
    blank(),
    p([tb("Kênh nội bộ Kafka:"), t(" Kafka broker được cấu hình "), tb("SASL/SCRAM-SHA-512"), t(" cho authentication và "), tb("TLS 1.3"), t(" cho mã hóa đường truyền giữa producer/consumer và broker. Ngoài ra, "), tb("ACL (Access Control List)"), t(" trên Kafka được cấu hình tường minh: chỉ có microservice được ủy quyền mới có thể produce/consume từ topic nhạy cảm (ví dụ: topic chứa dữ liệu CDC từ Core Banking).")], { indent: { left: 360 } }),
    blank(),

    h3("3.2.3. Data Masking – Bảo vệ quyền riêng tư trên giao diện người dùng"),
    p([t("Để giải quyết rủi ro R09 (Shoulder Surfing) và củng cố tính bí mật tại tầng giao diện, kiến trúc đề xuất triển khai "), tb("Data Masking (che mờ dữ liệu)"), t(" động trên lớp Front-end NextJS. Cơ chế hoạt động như sau:")]),
    blank(),
    p([t("Theo mặc định, các trường dữ liệu nhạy cảm được hiển thị ở dạng che mờ (ví dụ: số điện thoại "), tb("\"0912***456\""), t(", số CCCD "), tb("\"0380****1234\""), t(", số tài khoản "), tb("\"1000****5678\""), t("). Người dùng chỉ có thể xem giá trị đầy đủ bằng cách nhấn vào icon \"hiển thị\" – thao tác này sẽ ghi nhận một "), tb("Audit Log Event"), t(" kèm theo thông tin: ai đã xem, xem thông tin của khách hàng nào, vào thời điểm nào, từ IP nào. Cơ chế này vừa bảo vệ khỏi Shoulder Surfing, vừa tạo "), tb("deterrence effect"), t(" (ngăn chặn bằng tâm lý): nhân viên biết rằng mọi thao tác xem dữ liệu nhạy cảm đều được ghi lại và có thể bị kiểm tra bất kỳ lúc nào.")]),
    blank(),

    caption("Bảng 3.2: Chính sách mã hóa theo loại dữ liệu – CRM 1.0 VietinBank"),
    new Table({
      width: { size: 9360, type: WidthType.DXA }, columnWidths: [1800, 1400, 1800, 2160, 2200],
      rows: [
        new TableRow({ children: [hCell("Loại dữ liệu", 1800), hCell("Mức độ nhạy cảm", 1400), hCell("Thuật toán mã hóa", 1800), hCell("Vị trí lưu trữ", 2160), hCell("Kiểm soát truy cập", 2200)] }),
        ...([
          ["Số CCCD/Hộ chiếu", "Rất cao", "AES-256-GCM (App-level)", "PostgreSQL (column encrypt)", "Chỉ RM phụ trách + Auditor (masked)"],
          ["Điểm tín dụng CIC", "Rất cao", "AES-256-GCM (App-level)", "Oracle TDE Tablespace", "RM + Trưởng phòng + Audit Log"],
          ["Số dư tài khoản", "Cao", "Oracle TDE + TLS in-transit", "Oracle, đồng bộ CDC từ Core", "RM, Trưởng phòng (masked mặc định)"],
          ["Hồ sơ ảnh (CCCD photo)", "Cao", "AES-256 SSE-KMS", "S3 WORM (immutable)", "RM + Trưởng phòng, presigned URL 15 phút"],
          ["Nhật ký kiểm toán", "Cao", "SHA-256 hash chain", "S3 WORM (immutable)", "Auditor + Security Team (read-only)"],
          ["Thông tin liên lạc", "Trung bình", "TDE + Data Masking UI", "PostgreSQL", "Teller, RM (masked trừ khi cần thiết)"],
          ["Metadata hệ thống", "Thấp", "TLS in-transit", "Redis (cache, TTL ngắn)", "Internal services only"],
        ]).map((row, i) => new TableRow({ children: [bCell(row[0], 1800, alt(i), true), cCell(row[1], 1400, alt(i)), bCell(row[2], 1800, alt(i)), bCell(row[3], 2160, alt(i)), bCell(row[4], 2200, alt(i))] }))
      ]
    }),
    blank(),

    h2("3.3. Tăng cường Điều khiển truy nhập và Quản lý định danh (IAM)"),
    blank(),
    h3("3.3.1. Hệ thống SSO kết hợp OAuth2/OIDC và JWT ngắn hạn"),
    p([t("Để giải quyết rủi ro R10 (Phishing dẫn đến đánh cắp credentials), R06 (JWT bị đánh cắp) và củng cố kiểm soát truy cập tập trung, kiến trúc đề xuất triển khai "), tb("hệ thống Single Sign-On (SSO)"), t(" dựa trên giao thức "), tb("OpenID Connect (OIDC)"), t(" làm lớp trên của OAuth2.0. SSO cho phép người dùng chỉ cần đăng nhập một lần để truy cập tất cả các ứng dụng ngân hàng nội bộ (CRM, Email, Portal nội bộ,...), loại bỏ vấn đề quản lý nhiều bộ credentials khác nhau.")]),
    blank(),
    p([t("Luồng xác thực được thiết kế như sau: "), tb("(1)"), t(" Người dùng truy cập CRM từ trình duyệt, được chuyển hướng đến "), tb("Identity Provider (IdP)"), t(" – ví dụ Keycloak hoặc Microsoft Entra ID; "), tb("(2)"), t(" IdP xác thực người dùng qua Active Directory/LDAP và yêu cầu xác thực bổ sung bằng "), tb("MFA (Multi-Factor Authentication)"), t(" – OTP qua ứng dụng authenticator hoặc SMS OTP; "), tb("(3)"), t(" Sau xác thực thành công, IdP phát hành "), tb("ID Token + Access Token (JWT)"), t(" với thời gian sống tối đa "), tb("30 phút"), t(" và "), tb("Refresh Token"), t(" có thời gian sống 8 giờ (tương đương một ca làm việc); "), tb("(4)"), t(" Access Token được gửi kèm mỗi request đến API Gateway; API Gateway xác minh chữ ký JWT và kiểm tra thông tin role/claim trước khi cho phép request đi tiếp đến microservice tương ứng.")]),
    blank(),
    p([t("Thời gian sống JWT ngắn (30 phút) là biện pháp quan trọng để giới hạn thiệt hại trong trường hợp token bị đánh cắp: kẻ tấn công chỉ có thể sử dụng token trong tối đa 30 phút. Cơ chế "), tb("Token Revocation"), t(" thông qua danh sách thu hồi (Revocation List) hoặc Redis-based denylist được triển khai để xử lý các trường hợp cần vô hiệu hóa token ngay lập tức (khi phát hiện bất thường hoặc nhân viên nghỉ việc).")]),
    blank(),

    h3("3.3.2. RBAC kết hợp ABAC – Kiểm soát truy cập theo ngữ cảnh"),
    p([t("Để giải quyết rủi ro R01 (lạm dụng quyền hạn nội bộ) – rủi ro được đánh giá nghiêm trọng nhất trong ma trận (điểm 20), kiến trúc đề xuất triển khai mô hình "), tb("RBAC kết hợp ABAC"), t(" theo ba lớp kiểm soát:")]),
    blank(),
    p([tb("Lớp 1 – RBAC tại API Gateway (Coarse-grained Authorization):"), t(" API Gateway kiểm tra role của người dùng trong JWT claims và quyết định có cho phép request đến microservice hay không ở mức độ thô (ví dụ: role Teller không được gọi API /credit-report/* của Credit Service).")], { indent: { left: 360 } }),
    blank(),
    p([tb("Lớp 2 – ABAC tại Business Logic (Fine-grained Authorization):"), t(" Bên trong từng microservice, logic phân quyền chi tiết hơn được triển khai dựa trên thuộc tính ngữ cảnh. Ví dụ điển hình: khi RM gọi API "), tb("GET /customers/{customerId}"), t(", hệ thống không chỉ kiểm tra role mà còn kiểm tra: "), tb("(a)"), t(" customerId có thuộc danh sách khách hàng được phân công cho RM này không? "), tb("(b)"), t(" Request có xuất phát từ IP trong whitelist nội bộ ngân hàng không? "), tb("(c)"), t(" Thời điểm request có trong giờ làm việc (8:00–17:00) không? Chỉ khi cả ba điều kiện thỏa mãn, request mới được cho phép thực thi.")], { indent: { left: 360 } }),
    blank(),
    p([tb("Lớp 3 – Row-Level Security tại CSDL (Data-level Authorization):"), t(" Tầng bảo vệ cuối cùng tại tầng CSDL. PostgreSQL Row-Level Security (RLS) policy được cấu hình để ") , tb("mỗi kết nối CSDL từ microservice chỉ có thể đọc/ghi các hàng dữ liệu thuộc quyền của context hiện tại"), t(". Ngay cả khi có lỗi logic ở tầng ứng dụng (ví dụ: bug cho phép RM xem khách hàng ngoài danh mục), RLS tại CSDL vẫn là lớp kiểm soát cuối cùng ngăn chặn truy cập trái phép.")], { indent: { left: 360 } }),
    blank(),

    caption("Bảng 3.3: Đối chiếu Rủi ro – Giải pháp kiểm soát truy cập theo lớp"),
    new Table({
      width: { size: 9360, type: WidthType.DXA }, columnWidths: [600, 2200, 1800, 2360, 2400],
      rows: [
        new TableRow({ children: [hCell("Lớp", 600), hCell("Cơ chế kiểm soát", 2200), hCell("Công nghệ", 1800), hCell("Rủi ro xử lý", 2360), hCell("Cơ chế hoạt động", 2400)] }),
        ...([
          ["L1", "SSO + MFA (Xác thực)", "Keycloak / Entra ID, TOTP/OTP", "R10 (Phishing credentials)", "Xác thực 2 yếu tố bắt buộc, token JWT TTL 30 phút"],
          ["L1", "API Gateway – Coarse RBAC", "Kong Gateway với JWT plugin", "R06 (Token abuse), R02 (API Bypass)", "Role check tại gateway, rate limit per user"],
          ["L2", "ABAC tại Business Logic", "OPA (Open Policy Agent)", "R01 (Insider Threat)", "Policy: RM chỉ xem KH phụ trách, trong giờ, từ IP nội bộ"],
          ["L3", "Row-Level Security (RLS)", "PostgreSQL RLS Policy", "R01 (Data leakage tại DB)", "SQL policy tự động lọc dữ liệu theo context user"],
          ["L3", "Database Audit Vault", "Oracle Audit Vault / pgAudit", "R01 (Insider Threat audit)", "Ghi toàn bộ SELECT/UPDATE nhạy cảm vào audit log WORM"],
        ]).map((row, i) => new TableRow({ children: [cCell(row[0], 600, alt(i), true), bCell(row[1], 2200, alt(i), true), bCell(row[2], 1800, alt(i)), bCell(row[3], 2360, alt(i)), bCell(row[4], 2400, alt(i))] }))
      ]
    }),
    blank(),

    h2("3.4. Phòng chống rủi ro hệ thống phân tán"),
    blank(),
    h3("3.4.1. Circuit Breaker Pattern – Ngắt mạch chống lỗi dây chuyền"),
    p([t("Để giải quyết triệt để rủi ro R03 (Cascading Failures từ Core Banking Legacy), kiến trúc đề xuất áp dụng "), tb("Circuit Breaker Pattern"), t(" – một design pattern trong lập trình phân tán lấy cảm hứng từ cầu dao điện (circuit breaker) trong kỹ thuật điện. Ý tưởng cốt lõi là: thay vì để các microservice liên tục gọi một service đang lỗi (gây ra việc hàng nghìn request chờ timeout và chiếm giữ tài nguyên), Circuit Breaker sẽ "), tb("\"ngắt mạch\" tạm thời"), t(" – trả về lỗi ngay lập tức mà không cần chờ timeout – cho đến khi service đích hồi phục.")]),
    blank(),
    p([t("Circuit Breaker hoạt động theo ba trạng thái:")]),
    blank(),
    p([tb("CLOSED (Đóng – Hoạt động bình thường):"), t(" Các request được chuyển tiếp bình thường đến service đích. Circuit Breaker theo dõi tỷ lệ lỗi (error rate). Nếu tỷ lệ lỗi vượt ngưỡng cấu hình (ví dụ: >50% trong 60 giây), chuyển sang trạng thái OPEN.")], { indent: { left: 360 } }),
    blank(),
    p([tb("OPEN (Mở – Ngắt mạch):"), t(" Mọi request đến service đích bị từ chối ngay lập tức với lỗi định sẵn (ví dụ: trả về dữ liệu cache cũ hoặc thông báo \"Dịch vụ tạm thời không khả dụng\"). Không có request nào được gửi đến service đích, ngăn chặn overload thêm. Sau một khoảng thời gian timeout (ví dụ: 30 giây), chuyển sang HALF-OPEN.")], { indent: { left: 360 } }),
    blank(),
    p([tb("HALF-OPEN (Nửa mở – Thử nghiệm phục hồi):"), t(" Cho phép một số lượng nhỏ request thử tiếp cận service đích. Nếu thành công, chuyển về CLOSED. Nếu vẫn lỗi, quay lại OPEN. Thư viện "), tb("Resilience4j"), t(" (cho Java/Spring Boot) hoặc "), tb("Hystrix"), t(" (Netflix OSS) là các lựa chọn triển khai Circuit Breaker phổ biến trong hệ sinh thái Kubernetes/OpenShift.")], { indent: { left: 360 } }),
    blank(),
    p([t("Trong trường hợp kết nối đến Core Banking bị ngắt, CRM 1.0 sẽ "), tb("không sụp đổ hoàn toàn"), t(" mà chuyển sang chế độ "), tb("Degraded Mode"), t(": các chức năng không phụ thuộc Core Banking (tìm kiếm thông tin KH đã có trong CSDL CRM, cập nhật metadata, ghi chú tương tác) vẫn hoạt động bình thường, trong khi các chức năng cần dữ liệu real-time từ Core Banking hiển thị thông báo rõ ràng cho người dùng.")]),
    blank(),

    h3("3.4.2. Saga Pattern – Đảm bảo toàn vẹn giao dịch phân tán"),
    p([t("Để giải quyết rủi ro R07 (không nhất quán dữ liệu phân tán), kiến trúc đề xuất áp dụng "), tb("Saga Pattern"), t(" cho tất cả các nghiệp vụ đòi hỏi cập nhật dữ liệu trên nhiều microservices cùng lúc. Saga Pattern là giải pháp thay thế cho giao thức 2PC (Two-Phase Commit) vốn không phù hợp với kiến trúc Microservices do gây ra blocking và phụ thuộc chặt chẽ giữa các service.")]),
    blank(),
    p([t("Trong Saga Pattern theo kiểu "), tb("Choreography-based"), t(" (phù hợp với CRM 1.0 đã sử dụng Kafka): mỗi microservice thực hiện giao dịch cục bộ của mình và phát một "), tb("domain event"), t(" lên Kafka topic. Các microservice khác lắng nghe event và thực hiện giao dịch của mình tiếp theo. Quan trọng hơn, "), tb("mỗi bước trong Saga phải có một giao dịch đền bù (Compensating Transaction)"), t(" tương ứng: nếu bất kỳ bước nào thất bại, hệ thống tự động phát compensating transactions để hoàn tác các bước trước đó, đưa hệ thống về trạng thái nhất quán ban đầu. Để đảm bảo "), tb("Exactly-Once Delivery"), t(" trên Kafka (tránh duplicate events gây ra cập nhật trùng lặp), cần bật "), tb("Kafka Transactions (Idempotent Producer + Transactional API)"), t(".")]),
    blank(),

    caption("Bảng 3.4: Tổng hợp giải pháp – Ánh xạ trực tiếp tới rủi ro đã nhận diện"),
    new Table({
      width: { size: 9360, type: WidthType.DXA }, columnWidths: [500, 2000, 3060, 1900, 1900],
      rows: [
        new TableRow({ children: [hCell("Rủi ro", 500), hCell("Tên rủi ro", 2000), hCell("Giải pháp kỹ thuật đề xuất", 3060), hCell("Chương/Mục", 1900), hCell("Mức giảm thiểu", 1900)] }),
        ...([
          ["R01", "Lạm dụng quyền nội bộ", "ABAC (OPA) + RLS PostgreSQL + Audit Log WORM + Data Masking", "3.3.2, 3.2.3", "Cao → Thấp"],
          ["R02", "SQL/API Injection", "WAF OWASP ruleset + Input Validation tại microservice + Parameterized Query", "3.1.1", "Rất cao → Thấp"],
          ["R03", "Cascading Failures", "Circuit Breaker (Resilience4j) + Degraded Mode + Timeout policy", "3.4.1", "Rất cao → Trung bình"],
          ["R04", "Lateral Movement (East-West)", "mTLS (Istio STRICT mode) + NetworkPolicy Default-Deny + Istio AuthzPolicy", "3.1.2", "Rất cao → Thấp"],
          ["R05", "DDoS", "Cloud DDoS Scrubbing + WAF Rate Limiting + CDN + Anycast routing", "3.1.1", "Rất cao → Trung bình"],
          ["R06", "JWT Token Abuse", "JWT TTL 30 phút + Token Revocation List (Redis) + Certificate Pinning", "3.3.1", "Cao → Rất thấp"],
          ["R07", "Data Inconsistency", "Saga Pattern + Kafka Transactions + Outbox Pattern", "3.4.2", "Cao → Thấp"],
          ["R08", "Supply Chain Attack", "Container Image Scanning (Trivy/Clair) trong CI/CD + Image signing (Cosign)", "3.1.1", "Cao → Thấp"],
          ["R09", "Shoulder Surfing", "Data Masking động trên NextJS UI + Screen Lock Policy", "3.2.3", "TB → Rất thấp"],
          ["R10", "Phishing credentials", "SSO + MFA bắt buộc (TOTP) + Security Awareness Training", "3.3.1", "Cao → Thấp"],
        ]).map((row, i) => new TableRow({ children: [cCell(row[0], 500, alt(i), true), bCell(row[1], 2000, alt(i)), bCell(row[2], 3060, alt(i)), cCell(row[3], 1900, alt(i)), cCell(row[4], 1900, alt(i), true)] }))
      ]
    }),
    blank(),

    // Summary Chương 3
    new Paragraph({ spacing: { before: 300, after: 120 },
      children: [new TextRun({ text: "Tóm tắt Chương 3", bold: true, size: 28, font: "Times New Roman", color: "1F3864" })] }),
    p([t("Chương 3 đã đề xuất một kiến trúc bảo mật đa lớp toàn diện, có truy xuất nguồn gốc rõ ràng từ từng rủi ro đã nhận diện trong Chương 2 đến từng giải pháp kỹ thuật cụ thể. Kiến trúc phòng vệ 3-Tier (DMZ – Application Zone – Database Zone) kết hợp mTLS nội bộ đảm bảo không có luồng tấn công nào, dù từ ngoài vào hay từ trong ra, có thể tiếp cận tài sản dữ liệu mà không qua ít nhất hai lớp kiểm soát. Chiến lược mã hóa đa tầng (disk → TDE → application-level) cùng với Data Masking UI bảo vệ tính bí mật ở mọi trạng thái của dữ liệu. Mô hình RBAC kết hợp ABAC ba lớp và JWT TTL ngắn giải quyết bài toán khó nhất – ngăn chặn lạm dụng quyền hạn nội bộ. Circuit Breaker và Saga Pattern giải quyết các rủi ro đặc thù của kiến trúc Microservices. Tổng thể, các giải pháp này khi triển khai đồng bộ sẽ đưa mức rủi ro tổng hợp của hệ thống CRM 1.0 từ mức \"Rất cao\" (điểm trung bình 14/25) xuống mức \"Trung bình – Thấp\" (điểm mục tiêu ≤ 6/25) theo ma trận rủi ro.")]),
    blank(),
  );

  return c;
}

module.exports = { buildChapter3 };
