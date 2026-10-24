// ================================================================
// CHƯƠNG 2: PHÂN TÍCH HIỆN TRẠNG VÀ ĐÁNH GIÁ RỦI RO CRM 1.0
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
function cCell(text, w, shade, bold, color) {
  return new TableCell({ borders: BORDERS, width: { size: w, type: WidthType.DXA },
    shading: { fill: shade || "FFFFFF", type: ShadingType.CLEAR }, margins: CM,
    children: [new Paragraph({ alignment: AlignmentType.CENTER,
      children: [new TextRun({ text, size: 20, bold: !!bold, font: "Times New Roman", color: color || "000000" })] })] });
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

function buildChapter2() {
  const c = [];

  c.push(
    new Paragraph({ children: [new PageBreak()] }),
    h1("CHƯƠNG 2: PHÂN TÍCH HIỆN TRẠNG VÀ ĐÁNH GIÁ RỦI RO HỆ THỐNG CRM 1.0 TẠI VIETINBANK"),
    blank(),
    h2("2.1. Phân tích kiến trúc hệ thống CRM 1.0 tại VietinBank"),
    blank(),
    p([t("Để đánh giá rủi ro bảo mật một cách toàn diện và có hệ thống, bước đầu tiên theo phương pháp 9 bước (Bước 1: Mô tả hệ thống) là phải xây dựng một hồ sơ đặc tả kiến trúc chi tiết của hệ thống cần bảo vệ. Trong phần này, CRM 1.0 của VietinBank được phân tích theo góc nhìn ba chiều: "), tb("Hạ tầng & Phần cứng (Hardware), Phần mềm & Middleware (Software)"), t(", và "), tb("Dữ liệu (Data)"), t(" – tương ứng với ba trong năm thành phần cốt lõi của một hệ thống thông tin dựa trên máy tính đã được đề cập ở Chương 1.")]),
    blank(),

    h3("2.1.1. Hạ tầng & Phần cứng (Hardware Layer)"),
    p([t("Hệ thống CRM 1.0 của VietinBank được xây dựng trên kiến trúc "), tb("Cloud-Native"), t(", triển khai hoàn toàn trên nền tảng "), tb("Red Hat OpenShift Container Platform (OCP)"), t(" – một bản phân phối Kubernetes cấp doanh nghiệp với các tính năng bảo mật bổ sung như RBAC tích hợp, mạng SDN (Software-Defined Networking) và kiểm soát chính sách bảo mật (Security Context Constraints – SCC). Mô hình triển khai này mang lại khả năng mở rộng linh hoạt theo chiều ngang (Horizontal Scaling) và cô lập tài nguyên giữa các microservices thông qua Namespace và Pod, tuy nhiên cũng đặt ra yêu cầu quản lý bảo mật ở cấp độ container và orchestration platform.")]),
    blank(),
    p([t("Về hạ tầng lưu trữ, hệ thống sử dụng chiến lược "), tb("phân cấp lưu trữ hỗn hợp"), t(": "), tb("SAN/NAS (Storage Area Network/Network-Attached Storage)"), t(" phục vụ các cơ sở dữ liệu quan hệ đòi hỏi độ trễ thấp (PostgreSQL, Oracle); và "), tb("Tủ đĩa S3 chuẩn WORM (Write Once Read Many)"), t(" để lưu trữ hồ sơ chứng từ dạng ảnh/PDF và nhật ký kiểm toán hệ thống. Đặc biệt, chuẩn WORM là một lựa chọn đúng đắn về mặt bảo mật: dữ liệu được ghi lên S3 WORM không thể bị sửa đổi hay xóa bởi bất kỳ tiến trình hay người dùng nào (kể cả quản trị viên) trong một khoảng thời gian được định nghĩa trước, đảm bảo "), tb("tính bất biến (Immutability)"), t(" của dữ liệu kiểm toán – một yêu cầu quan trọng theo chuẩn ISO 27001 và Luật An ninh mạng Việt Nam.")]),
    blank(),

    caption("Bảng 2.1: Tổng quan hạ tầng phần cứng hệ thống CRM 1.0 – VietinBank"),
    new Table({
      width: { size: 9360, type: WidthType.DXA }, columnWidths: [1800, 2000, 2560, 3000],
      rows: [
        new TableRow({ children: [hCell("Thành phần", 1800), hCell("Công nghệ/Giải pháp", 2000), hCell("Vai trò trong CRM 1.0", 2560), hCell("Rủi ro bảo mật cần lưu ý", 3000)] }),
        ...([
          ["Nền tảng Container", "Red Hat OpenShift (OCP)", "Orchestrate toàn bộ microservices, quản lý Pod/Namespace", "Misconfiguration RBAC trên OCP; Pod chạy với quyền root; SCC không được siết chặt"],
          ["Tính toán (Compute)", "Worker Nodes (vật lý/ảo hóa)", "Chạy các container microservices của CRM", "Kernel exploit nếu không vá bản vá kịp thời; side-channel attacks giữa containers"],
          ["Lưu trữ CSDL", "SAN/NAS hiệu suất cao", "Lưu trữ PostgreSQL, Oracle, Redis", "Truy cập vật lý trái phép vào storage; thiếu mã hóa at-rest trên block device"],
          ["Lưu trữ tài liệu", "Tủ đĩa S3 chuẩn WORM", "Lưu hồ sơ ảnh, PDF, Audit Log bất biến", "Cấu hình sai Bucket Policy có thể cho phép đọc công khai; hết hạn WORM lock"],
          ["Mạng nội bộ", "SDN trên OpenShift (OVN-Kubernetes)", "Kết nối giữa các microservices trong cluster", "East-West traffic không được kiểm soát; thiếu NetworkPolicy"],
        ]).map((row, i) => new TableRow({ children: [bCell(row[0], 1800, alt(i), true), bCell(row[1], 2000, alt(i)), bCell(row[2], 2560, alt(i)), bCell(row[3], 3000, alt(i))] }))
      ]
    }),
    blank(),

    h3("2.1.2. Phần mềm & Middleware (Software Layer)"),
    p([t("Kiến trúc phần mềm của CRM 1.0 tuân theo mô hình "), tb("Microservices thuần túy"), t(", trong đó mỗi chức năng nghiệp vụ độc lập (quản lý khách hàng, quản lý leads, xử lý hồ sơ tín dụng, thông báo,…) được đóng gói thành một microservice riêng biệt, có vòng đời triển khai độc lập. Các lớp phần mềm chính bao gồm:")]),
    blank(),
    p([tb("Front-end – NextJS v.14 (Server-Side Rendering):"), t(" Lớp giao diện người dùng được xây dựng bằng Next.js phiên bản 14 với cơ chế Server-Side Rendering (SSR). Cơ chế SSR có ưu điểm về hiệu năng và SEO, nhưng đặt ra thách thức bảo mật đặc thù: mã JavaScript phía máy chủ có thể bị khai thác nếu không được kiểm soát chặt chẽ (ví dụ: Server-Side Request Forgery – SSRF, khai thác lỗ hổng trong các npm packages). Hơn 11.000 cán bộ, giao dịch viên và Relationship Manager (RM) truy cập hệ thống thông qua lớp này.")], { indent: { left: 360 } }),
    blank(),
    p([tb("API Gateway – Điểm kiểm soát tập trung:"), t(" API Gateway đóng vai trò là "), tb("Single Entry Point"), t(" (điểm vào duy nhất) cho mọi request từ Front-end đến các microservices nội bộ. Đây là nơi triển khai xác thực token (JWT validation), phân quyền sơ bộ (coarse-grained authorization), Rate Limiting chống DDoS và ghi nhật ký truy cập tập trung. Tuy nhiên, API Gateway cũng trở thành "), tb("Single Point of Failure"), t(" và là mục tiêu tấn công có giá trị cao nhất trong hệ thống.")], { indent: { left: 360 } }),
    blank(),
    p([tb("Apache Kafka – Message Queue bất đồng bộ:"), t(" Kafka đảm nhiệm vai trò "), tb("backbone giao tiếp bất đồng bộ"), t(" giữa các microservices, đặc biệt là luồng nhận thông tin khách hàng từ Core Banking qua cơ chế Change Data Capture (CDC) real-time. Kafka cũng được dùng để phát sự kiện thông báo (notification events) và đồng bộ trạng thái giữa các service. Nếu Kafka broker không được bảo mật đúng cách (thiếu authentication SASL, thiếu mã hóa TLS giữa producer/consumer), kẻ tấn công có thể nghe lén hoặc inject message giả mạo vào các topic nhạy cảm.")], { indent: { left: 360 } }),
    blank(),

    caption("Bảng 2.2: Kiến trúc phần mềm và đánh giá sơ bộ rủi ro bảo mật"),
    new Table({
      width: { size: 9360, type: WidthType.DXA }, columnWidths: [1600, 1800, 2160, 3800],
      rows: [
        new TableRow({ children: [hCell("Thành phần", 1600), hCell("Công nghệ", 1800), hCell("Chức năng", 2160), hCell("Rủi ro bảo mật đặc thù", 3800)] }),
        ...([
          ["Front-end", "NextJS v.14 (SSR)", "Giao diện người dùng cho 11.000+ cán bộ", "SSRF từ SSR; XSS/CSRF; lộ thông tin nhạy cảm trong HTML source; npm dependency vulnerabilities"],
          ["API Gateway", "Kong/NGINX (API GW)", "Single Entry Point, JWT validation, Rate Limiting", "Single Point of Failure; bypass nếu microservices expose port trực tiếp; JWT không có expiry ngắn"],
          ["Microservices", "Container trên OCP", "Logic nghiệp vụ phân tán, mỗi service một database", "Inter-service trust: service A gọi service B không xác thực; thiếu mTLS nội bộ"],
          ["Message Queue", "Apache Kafka", "CDC từ Core Banking, event-driven giữa services", "Thiếu SASL authentication; thiếu mã hóa TLS broker; message poisoning injection"],
          ["Core Banking Adapter", "Integration Layer (Tight Coupling)", "Đồng bộ dữ liệu từ hệ thống Legacy", "Điểm nghẽn cổ chai; lỗi Core Banking propagate sang CRM; không có Circuit Breaker"],
        ]).map((row, i) => new TableRow({ children: [bCell(row[0], 1600, alt(i), true), bCell(row[1], 1800, alt(i)), bCell(row[2], 2160, alt(i)), bCell(row[3], 3800, alt(i))] }))
      ]
    }),
    blank(),

    h3("2.1.3. Dữ liệu (Data Layer)"),
    p([t("Chiến lược quản lý dữ liệu của CRM 1.0 tuân theo mô hình "), tb("Database per Service"), t(" – một best practice của kiến trúc Microservices, trong đó mỗi microservice sở hữu và quản lý cơ sở dữ liệu riêng của mình, không service nào được truy cập trực tiếp database của service khác mà phải thông qua API. Điều này tăng cường sự độc lập và giảm coupling, nhưng đồng thời tạo ra thách thức lớn về "), tb("nhất quán dữ liệu phân tán"), t(" và đòi hỏi chiến lược bảo mật đa tầng cho nhiều loại datastore khác nhau:")]),
    blank(),
    p([tb("PostgreSQL"), t(" (cơ sở dữ liệu quan hệ mã nguồn mở): Lưu trữ dữ liệu hồ sơ khách hàng có cấu trúc (thông tin cá nhân, danh mục sản phẩm, lịch sử tương tác). PostgreSQL hỗ trợ Transparent Data Encryption (TDE) và Row-Level Security (RLS) – cho phép chính sách bảo mật ngay tại tầng CSDL, không phụ thuộc hoàn toàn vào lớp ứng dụng."), new TextRun({ text: "" })], { indent: { left: 360 } }),
    blank(),
    p([tb("Oracle Database"), t(": Lưu trữ dữ liệu giao dịch tài chính quan trọng được đồng bộ từ Core Banking (số dư, lịch sử giao dịch, thông tin hợp đồng tín dụng). Oracle có bộ tính năng bảo mật doanh nghiệp mạnh mẽ (Oracle Label Security, Database Vault, Audit Vault) nhưng đòi hỏi cấu hình chuyên sâu."), new TextRun({ text: "" })], { indent: { left: 360 } }),
    blank(),
    p([tb("Redis"), t(" (In-memory Key-Value Store): Sử dụng làm cache tầng ứng dụng (lưu session, token, dữ liệu thường xuyên truy cập) và làm pub/sub message broker cho một số luồng event nhẹ. Redis mặc định không bật authentication, và dữ liệu được lưu in-memory nên rủi ro rò rỉ qua memory dump nếu không được bảo vệ đúng cách."), new TextRun({ text: "" })], { indent: { left: 360 } }),
    blank(),
    p([tb("S3 WORM Storage"), t(": Lưu trữ hồ sơ dạng ảnh (CCCD, chứng từ) và nhật ký kiểm toán bất biến. Dữ liệu trên S3 cần được kiểm soát chặt chẽ về quyền truy cập (Bucket Policy, IAM Policies) và đảm bảo mã hóa server-side (SSE-KMS) với khóa được quản lý trong Hardware Security Module (HSM)."), new TextRun({ text: "" })], { indent: { left: 360 } }),
    blank(),
    p([t("Đặc biệt quan trọng, toàn bộ dữ liệu trên được đồng bộ "), tb("real-time"), t(" từ hệ thống Core Banking thông qua cơ chế "), tb("CDC (Change Data Capture)"), t(" sử dụng Kafka làm kênh truyền. Cơ chế này đảm bảo CRM 1.0 luôn có dữ liệu khách hàng cập nhật nhất, nhưng đồng thời tạo ra "), tb("luồng dữ liệu nhạy cảm liên tục không ngừng"), t(" từ hệ thống lõi sang CRM – một vector tấn công tiềm ẩn nếu kênh truyền không được bảo mật.")]),
    blank(),

    h2("2.2. Nhận diện và đánh giá rủi ro bảo mật trong hệ thống"),
    blank(),
    p([t("Áp dụng phương pháp đánh giá rủi ro 9 bước (đã trình bày ở mục 1.3), bước 2 đến bước 7 được thực hiện bằng cách ánh xạ các đặc điểm kiến trúc của CRM 1.0 vào từng vùng hạ tầng CNTT trong mô hình 7 vùng (đã trình bày ở mục 1.2.2). Kết quả phân tích được tổ chức theo bốn nhóm rủi ro chính, từ vùng người dùng đến tầng hệ thống phân tán.")]),
    blank(),

    h3("2.2.1. Rủi ro Vùng Người dùng & Máy trạm (User & Workstation Domain)"),
    p([t("Đây là vùng rủi ro mang tính "), tb("con người (Human Factor)"), t(" – thống kê toàn cầu từ Verizon Data Breach Investigations Report (DBIR) chỉ ra rằng hơn 82% các vụ vi phạm dữ liệu có sự tham gia của yếu tố con người, dù vô ý hay cố ý. Với quy mô hơn "), tb("11.000 cán bộ"), t(" có quyền truy cập CRM 1.0 tại VietinBank, vùng người dùng là bề mặt tấn công rộng nhất và khó kiểm soát nhất.")]),
    blank(),
    p([tb("Rủi ro 1 – Lạm dụng quyền hạn nội bộ (Privilege Abuse / Insider Threat):"), t(" Đây là rủi ro đặc trưng và nghiêm trọng nhất trong môi trường ngân hàng. Một Relationship Manager (RM) có thể truy xuất thông tin tài chính của khách hàng không thuộc danh mục phụ trách của mình (ví dụ: xem số dư tài khoản của người quen để trục lợi thông tin). Trường hợp nghiêm trọng hơn là RM cấu kết với bên thứ ba để bán thông tin khách hàng CIC – loại dữ liệu có giá trị cao trên thị trường ngầm. Rủi ro này đặc biệt nguy hiểm vì kẻ vi phạm là người đã được xác thực và có quyền truy cập hợp lệ, khiến các hệ thống phát hiện tấn công truyền thống (dựa trên chữ ký tấn công) gần như vô hiệu."), new TextRun({ text: "" })], { indent: { left: 360 } }),
    blank(),
    p([tb("Rủi ro 2 – Rò rỉ thông tin qua màn hình và vai trò lướt mắt (Shoulder Surfing):"), t(" Trong môi trường làm việc đông đúc tại chi nhánh ngân hàng, thông tin nhạy cảm hiển thị trên màn hình máy trạm (số tài khoản, số CCCD, số dư) có thể bị nhìn trộm bởi khách hàng, đồng nghiệp không có quyền, hoặc camera quan sát nếu màn hình đặt sai hướng."), new TextRun({ text: "" })], { indent: { left: 360 } }),
    blank(),
    p([tb("Rủi ro 3 – Tấn công Phishing nhằm vào tài khoản nhân viên:"), t(" Email giả mạo danh nghĩa IT department hoặc Ban lãnh đạo yêu cầu nhân viên đăng nhập vào trang web giả mạo CRM để \"cập nhật mật khẩu\" là kịch bản tấn công phổ biến. Với hơn 11.000 điểm tiếp xúc tiềm năng, xác suất ít nhất một nhân viên bị lừa là rất cao nếu không có đào tạo nhận thức bảo mật thường xuyên."), new TextRun({ text: "" })], { indent: { left: 360 } }),
    blank(),

    h3("2.2.2. Rủi ro Vùng LAN-to-WAN & WAN (Tấn công từ bên ngoài)"),
    p([t("Hệ thống CRM 1.0 không chỉ phục vụ người dùng nội bộ. Khách hàng VietinBank có thể đẩy "), tb("Lead (yêu cầu tư vấn sản phẩm)"), t(" vào CRM thông qua các kênh số đối ngoại như "), tb("iPay (mobile banking)"), t(" và "), tb("eFast (internet banking doanh nghiệp)"), t(". Điều này có nghĩa là CRM 1.0 tiếp nhận luồng dữ liệu từ Internet công cộng, và bề mặt tấn công mở rộng ra ngoài ranh giới mạng nội bộ.")]),
    blank(),
    p([tb("Rủi ro 4 – Tấn công SQL Injection và API Injection vào các endpoint:"), t(" API Gateway của CRM 1.0 tiếp nhận các request từ iPay/eFast và chuyển tiếp đến các microservices. Nếu không có WAF và validation dữ liệu đầu vào đúng cách, kẻ tấn công có thể gửi payload SQL Injection (ví dụ: "), tb("' OR 1=1--"), t(") hoặc NoSQL Injection vào các tham số API để đọc trộm, sửa đổi hoặc xóa dữ liệu trong CSDL. Đây là loại tấn công thuộc top OWASP API Security Top 10 (API1:2023 – Broken Object Level Authorization, API3:2023 – Broken Object Property Level Authorization)."), new TextRun({ text: "" })], { indent: { left: 360 } }),
    blank(),
    p([tb("Rủi ro 5 – Tấn công từ chối dịch vụ phân tán (DDoS):"), t(" Các kênh số đối ngoại (iPay API, eFast API) có thể bị tấn công DDoS volumetric (SYN Flood, UDP Flood) làm cạn kiệt băng thông và tài nguyên mạng; hoặc tấn công DDoS tầng ứng dụng (HTTP Flood, Slowloris) làm cạn kiệt connection pool của API Gateway. Trong giờ giao dịch cao điểm (đặc biệt là cuối tháng, cuối quý), tác động của DDoS thành công là cực kỳ nghiêm trọng khi hàng nghìn giao dịch bị gián đoạn."), new TextRun({ text: "" })], { indent: { left: 360 } }),
    blank(),
    p([tb("Rủi ro 6 – Khai thác lỗ hổng xác thực và quản lý phiên:"), t(" Nếu token JWT được phát hành với thời gian sống dài (ví dụ: 24 giờ hoặc không có expiry), và không có cơ chế revocation (thu hồi token), kẻ tấn công sau khi đánh cắp được token (qua XSS, MITM) có thể sử dụng token đó trong thời gian dài mà nạn nhân không hay biết. Đây là lỗ hổng API2:2023 – Broken Authentication trong OWASP API Security Top 10."), new TextRun({ text: "" })], { indent: { left: 360 } }),
    blank(),

    h3("2.2.3. Rủi ro đặc thù kiến trúc Microservices (System/Application Domain)"),
    p([t("Đây là nhóm rủi ro "), tb("mới và đặc thù nhất"), t(" của CRM 1.0, xuất phát trực tiếp từ sự phức tạp nội tại của kiến trúc Microservices và không tồn tại (hoặc tồn tại với mức độ thấp hơn nhiều) trong kiến trúc nguyên khối truyền thống. Đây là lý do vì sao việc đánh giá rủi ro phải được thực hiện lại từ đầu khi kiến trúc hệ thống thay đổi cơ bản.")]),
    blank(),
    p([tb("Rủi ro 7 – Nghẽn cổ chai và lỗi dây chuyền (Cascading Failures):"), t(" CRM 1.0 phụ thuộc vào hệ thống Core Banking Legacy để lấy dữ liệu tài chính của khách hàng theo thời gian thực (số dư, hạn mức tín dụng,…). Kết nối giữa CRM và Core Banking được mô tả là "), tb("Tight Coupling"), t(" – tức là CRM gọi trực tiếp API của Core Banking một cách đồng bộ. Trong trường hợp Core Banking chậm phản hồi (do bảo trì, quá tải cuối ngày, hoặc sự cố kỹ thuật), các microservices của CRM đang chờ phản hồi sẽ "), tb("chiếm giữ thread pool"), t(" ngày càng nhiều hơn. Nếu không có cơ chế ngắt mạch (Circuit Breaker), toàn bộ luồng xử lý của CRM sẽ bị đóng băng và hệ thống sụp đổ theo hiệu ứng domino, ngay cả khi bản thân CRM không có lỗi gì."), new TextRun({ text: "" })], { indent: { left: 360 } }),
    blank(),
    p([tb("Rủi ro 8 – Phân mảnh và không nhất quán dữ liệu (Data Inconsistency):"), t(" Trong mô hình Database per Service, khi một nghiệp vụ yêu cầu cập nhật dữ liệu trên nhiều microservices cùng lúc (ví dụ: tạo hồ sơ khách hàng mới đồng thời cập nhật vào cả service Customer, service Lead, service Notification và service Analytics), nếu không có cơ chế giao dịch phân tán (Distributed Transaction), một phần các bước có thể thành công trong khi phần còn lại thất bại. Kết quả là "), tb("trạng thái dữ liệu không nhất quán"), t(" – một khách hàng tồn tại trong service Customer nhưng không có trong service Lead, dẫn đến lỗi nghiệp vụ và có thể bị khai thác để gian lận."), new TextRun({ text: "" })], { indent: { left: 360 } }),
    blank(),
    p([tb("Rủi ro 9 – Giao tiếp nội bộ giữa services không xác thực (East-West Traffic):"), t(" Trong môi trường Kubernetes/OpenShift, mặc định các Pod trong cùng một Namespace có thể giao tiếp với nhau tự do mà không cần xác thực. Điều này có nghĩa là nếu một microservice bị xâm nhập (qua lỗ hổng phần mềm hoặc supply chain attack vào Docker image), kẻ tấn công có thể "), tb("di chuyển ngang (Lateral Movement)"), t(" trong cluster, gọi các microservices khác có quyền cao hơn mà không gặp trở ngại. Đây là lỗ hổng theo mô hình \"perimeter security\" cổ điển – hệ thống được bảo vệ chắc chắn từ bên ngoài nhưng không có cơ chế kiểm soát ở tầng East-West bên trong."), new TextRun({ text: "" })], { indent: { left: 360 } }),
    blank(),
    p([tb("Rủi ro 10 – Tấn công chuỗi cung ứng phần mềm (Software Supply Chain Attack):"), t(" Kiến trúc Microservices sử dụng hàng chục container Docker image khác nhau, mỗi image chứa hàng trăm thư viện (npm packages, Java JARs, Python wheels,…). Một thư viện mã nguồn mở có lỗ hổng bảo mật (ví dụ: Log4Shell/CVE-2021-44228, Spring4Shell) trong bất kỳ image nào cũng có thể trở thành điểm xâm nhập. Nếu quy trình CI/CD không tích hợp quét lỗ hổng container image (Container Image Scanning) trước khi đẩy lên OpenShift, rủi ro này tích lũy theo thời gian."), new TextRun({ text: "" })], { indent: { left: 360 } }),
    blank(),

    h3("2.2.4. Ma trận đánh giá rủi ro tổng hợp cho CRM 1.0 – VietinBank"),
    p([t("Bảng sau tổng hợp toàn bộ 10 rủi ro đã nhận diện, đánh giá định tính theo ma trận 5×5 (Bước 5, 6, 7 của quy trình 9 bước) và xếp loại ưu tiên xử lý. Đây là kết quả của việc kết hợp đánh giá chuyên gia với đặc điểm kiến trúc thực tế của hệ thống.")]),
    blank(),

    caption("Bảng 2.3: Ma trận đánh giá rủi ro tổng hợp cho hệ thống CRM 1.0 – VietinBank"),
    new Table({
      width: { size: 9360, type: WidthType.DXA }, columnWidths: [360, 2000, 1400, 1200, 1200, 800, 600, 1800],
      rows: [
        new TableRow({ children: [
          hCell("STT", 360), hCell("Rủi ro", 2000), hCell("Vùng CNTT", 1400),
          hCell("Mối đe dọa", 1200), hCell("Lỗ hổng", 1200),
          hCell("XS\nXảy ra", 800), hCell("Tác\nĐộng", 600), hCell("Mức Rủi ro", 1800)
        ]}),
        ...([
          ["R01", "Lạm dụng quyền hạn nội bộ (RM truy xuất trái phép)", "Vùng Người dùng", "Insider Threat", "Thiếu ABAC, không giám sát hành vi", "4", "5", "Rất cao (20)", "FF4444"],
          ["R02", "Tấn công SQL/API Injection vào RESTful API", "LAN-to-WAN", "External Attacker", "Thiếu WAF, thiếu input validation", "4", "5", "Rất cao (20)", "FF4444"],
          ["R03", "Nghẽn cổ chai – Cascading Failures từ Core Banking", "Vùng Hệ thống", "Sự cố kỹ thuật", "Tight Coupling, thiếu Circuit Breaker", "4", "4", "Rất cao (16)", "FF6666"],
          ["R04", "Giao tiếp nội bộ không xác thực (East-West)", "Vùng Hệ thống", "Lateral Movement", "Thiếu mTLS, thiếu NetworkPolicy", "3", "5", "Rất cao (15)", "FF6666"],
          ["R05", "Tấn công DDoS vào kênh iPay/eFast", "WAN/LAN-to-WAN", "External Attacker", "Thiếu CDN DDoS Protection, Rate Limiting yếu", "3", "5", "Rất cao (15)", "FF6666"],
          ["R06", "Rò rỉ dữ liệu qua token JWT bị đánh cắp", "LAN-to-WAN", "Session Hijacking", "JWT TTL quá dài, thiếu revocation", "3", "4", "Cao (12)", "FFAA44"],
          ["R07", "Không nhất quán dữ liệu phân tán", "Vùng Hệ thống", "Lỗi phần mềm/Transaction", "Thiếu Saga Pattern, thiếu Outbox Pattern", "4", "3", "Cao (12)", "FFAA44"],
          ["R08", "Tấn công chuỗi cung ứng (Docker Image)", "Vùng Hệ thống", "Supply Chain Attack", "Thiếu Image Scanning trong CI/CD pipeline", "3", "4", "Cao (12)", "FFAA44"],
          ["R09", "Rò rỉ thông tin qua màn hình/Shoulder Surfing", "Vùng Máy trạm", "Physical Observation", "Thiếu Data Masking trên UI, thiếu screen lock", "3", "3", "Trung bình (9)", "FFEE44"],
          ["R10", "Phishing nhằm vào tài khoản nhân viên", "Vùng Người dùng", "Social Engineering", "Thiếu MFA, thiếu đào tạo nhận thức", "4", "3", "Cao (12)", "FFAA44"],
        ]).map((row, i) => new TableRow({ children: [
          cCell(row[0], 360, alt(i), true),
          bCell(row[1], 2000, alt(i)),
          bCell(row[2], 1400, alt(i)),
          bCell(row[3], 1200, alt(i)),
          bCell(row[4], 1200, alt(i)),
          cCell(row[5], 800, alt(i), true),
          cCell(row[6], 600, alt(i), true),
          cCell(row[7], 1800, alt(i), true, row[8]),
        ]}))
      ]
    }),
    blank(),
    p([t("Phân tích ma trận rủi ro cho thấy có "), tb("5 rủi ro được xếp loại Rất cao"), t(" (điểm ≥ 15), đòi hỏi xử lý ưu tiên ngay lập tức; "), tb("4 rủi ro Cao"), t(" (điểm 10–14) cần có kế hoạch xử lý trong ngắn hạn; và "), tb("1 rủi ro Trung bình"), t(" có thể giải quyết dần trong trung hạn. Đáng chú ý là R01 (Lạm dụng quyền nội bộ) và R02 (API Injection) đều đạt điểm tối đa 20 – phản ánh thực tế là đây là hai vector tấn công được ghi nhận thường xuyên nhất trong các vụ vi phạm dữ liệu tại ngân hàng Việt Nam trong những năm gần đây.")]),
    blank(),

    // Summary Chapter 2
    new Paragraph({ spacing: { before: 300, after: 120 },
      children: [new TextRun({ text: "Tóm tắt Chương 2", bold: true, size: 28, font: "Times New Roman", color: "1F3864" })] }),
    p([t("Chương 2 đã hoàn thành hai nhiệm vụ cốt lõi theo quy trình đánh giá rủi ro 9 bước: Thứ nhất, xây dựng hồ sơ đặc tả chi tiết kiến trúc hệ thống CRM 1.0 theo ba chiều Hardware–Software–Data, làm rõ đặc điểm kỹ thuật đặc thù của nền tảng Cloud-Native Microservices trên Red Hat OpenShift. Thứ hai, nhận diện và đánh giá 10 rủi ro bảo mật trọng yếu, ánh xạ chúng vào 7 vùng hạ tầng CNTT và định vị trên ma trận rủi ro 5×5. Kết quả phân tích là đầu vào trực tiếp và tường minh cho Chương 3 – mỗi rủi ro được nhận diện sẽ có ít nhất một giải pháp kỹ thuật đối ứng cụ thể trong kiến trúc bảo mật đề xuất.")]),
    blank(),
  );

  return c;
}

module.exports = { buildChapter2 };
