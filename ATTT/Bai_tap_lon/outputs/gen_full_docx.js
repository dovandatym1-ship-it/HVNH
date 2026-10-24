const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  AlignmentType, HeadingLevel, BorderStyle, WidthType, ShadingType,
  Header, Footer, PageNumber, PageBreak
} = require('docx');
const fs = require('fs');

// ── shared helpers ──────────────────────────────────────────────
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
  return new Paragraph({ alignment: AlignmentType.BOTH, spacing: LINE, indent: ind || { firstLine: 720 }, children: runs });
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

// ── load chapters ───────────────────────────────────────────────
const { buildChapter2 } = require('./chuong2_content.js');
const { buildChapter3 } = require('./chuong3_content.js');
const { buildChapter4AndConclusion } = require('./chuong4_content.js');

// ── CHAPTER 1 (inline) ─────────────────────────────────────────
function buildChapter1() {
  const c = [];
  // ── LỜI MỞ ĐẦU ──
  c.push(
    new Paragraph({ heading: HeadingLevel.HEADING_1, spacing: { before: 400, after: 200 }, alignment: AlignmentType.CENTER,
      children: [new TextRun({ text: "LỜI MỞ ĐẦU", bold: true, size: 32, font: "Times New Roman", color: "1F3864" })] }),
    blank(),
    h2("1. Tính cấp thiết của đề tài"),
    p([t("Trong bối cảnh chuyển đổi số diễn ra với tốc độ chưa từng có, hệ thống tài chính – ngân hàng Việt Nam đang đứng trước những thách thức bảo mật thông tin vừa cấp bách, vừa phức tạp hơn bất kỳ thời điểm nào trong lịch sử. Theo báo cáo của Cục An toàn thông tin – Bộ Thông tin và Truyền thông, trong giai đoạn 2022–2024, lĩnh vực tài chính – ngân hàng liên tục nằm trong nhóm các ngành bị tấn công mạng nhiều nhất, với số lượng sự cố được ghi nhận tăng trưởng bình quân trên 35% mỗi năm. Các hình thức tấn công ngày càng tinh vi, từ các chiến dịch APT (Advanced Persistent Threat) nhắm vào hệ thống lõi, cho đến các kỹ thuật khai thác API, đánh cắp phiên đăng nhập và lạm dụng quyền hạn nội bộ.")]),
    blank(),
    p([tb("Ngân hàng TMCP Công Thương Việt Nam (VietinBank)"), t(", với mạng lưới hơn 150 chi nhánh, hơn 1.000 phòng giao dịch và đội ngũ hơn 25.000 nhân viên, đang vận hành một trong những hệ sinh thái công nghệ thông tin quy mô nhất trong khối ngân hàng thương mại trong nước. Trong chiến lược hiện đại hóa hạ tầng công nghệ giai đoạn 2022–2025, VietinBank đã triển khai "), tb("Hệ thống Quản lý Quan hệ Khách hàng phiên bản 1.0 (CRM 1.0)"), t(" theo kiến trúc "), tb("Cloud-Native Microservices"), t(" trên nền tảng "), tb("Red Hat OpenShift Container Platform (OCP)"), t(". Đây là một cuộc cách mạng về mặt kiến trúc phần mềm, chuyển đổi hoàn toàn từ mô hình nguyên khối (Monolithic Architecture) sang mô hình dịch vụ vi phân tán, nhằm đạt được khả năng mở rộng linh hoạt, tốc độ triển khai cao và hiệu quả vận hành vượt trội.")]),
    blank(),
    p([t("Kiến trúc Microservices, dù mang lại nhiều lợi thế về kỹ thuật, đồng thời cũng mở ra một "), tb("bề mặt tấn công (Attack Surface) rộng hơn và phức tạp hơn"), t(": hàng chục đầu điểm API cần được bảo vệ; dữ liệu phân tán trên nhiều loại cơ sở dữ liệu (PostgreSQL, Oracle, Redis) đòi hỏi chiến lược bảo mật nhất quán; giao tiếp dịch vụ nội bộ qua Message Queue (Apache Kafka) có thể trở thành điểm yếu nếu không được mã hóa và xác thực nghiêm ngặt; và sự phụ thuộc vào hệ thống di sản (Legacy Core Banking) tạo ra những điểm nghẽn cổ chai không dễ xử lý. Trước thực tiễn đó, "), tb("việc nghiên cứu một cách hệ thống các rủi ro bảo mật và đề xuất một kiến trúc bảo mật toàn diện là nhiệm vụ vừa có giá trị học thuật, vừa có ý nghĩa ứng dụng thực tiễn cao"), t(".")]),
    blank(),

    h2("2. Mục tiêu nghiên cứu"),
    p([t("Bài tập lớn hướng tới ba mục tiêu: "), tb("(1)"), t(" Hệ thống hóa kiến thức lý thuyết nền tảng về ATTT (CIA Triad, Defense in Depth, đánh giá rủi ro 9 bước, các công nghệ bảo mật lõi); "), tb("(2)"), t(" Phân tích hiện trạng kiến trúc CRM 1.0 và nhận diện, đánh giá định tính các rủi ro bảo mật tương ứng từng vùng hạ tầng CNTT; "), tb("(3)"), t(" Đề xuất kiến trúc bảo mật đa lớp cụ thể bao gồm giải pháp kỹ thuật và chính sách quản trị nhằm bảo vệ toàn diện hệ thống.")]),
    blank(),

    h2("3. Đối tượng và Phạm vi nghiên cứu"),
    p([t("Đối tượng: Kiến trúc bảo mật thông tin và các giải pháp kỹ thuật, quản trị đảm bảo ATTT cho hệ thống ngân hàng. Phạm vi: "), tb("Hệ thống CRM 1.0 (giai đoạn MVP1) của VietinBank"), t(", bao gồm toàn bộ stack công nghệ từ lớp Front-end (NextJS v.14), API Gateway, Kafka, microservices trên OpenShift, đến lớp dữ liệu (PostgreSQL, Oracle, Redis, S3 WORM), và các điểm tích hợp với Core Banking, iPay, eFast.")]),
    blank(),

    h2("4. Phương pháp nghiên cứu"),
    p([t("Bài viết sử dụng phương pháp "), tb("nghiên cứu định tính kết hợp phân tích hệ thống"), t(": phân tích tài liệu (giáo trình ATTT, ISO/IEC 27001, NIST SP 800-30, tài liệu kỹ thuật CRM 1.0); tiếp cận theo mô hình (Defense in Depth, Combined Risk Assessment); và đối chiếu thực tiễn với best-practice bảo mật trong ngành công nghiệp phần mềm tài chính.")]),
    blank(),
    new Paragraph({ children: [new PageBreak()] }),

    // ── CHƯƠNG 1 ──
    h1("CHƯƠNG 1: CƠ SỞ LÝ THUYẾT VỀ AN TOÀN THÔNG TIN TRONG HỆ THỐNG DOANH NGHIỆP"),
    blank(),
    h2("1.1. Tổng quan về An toàn thông tin"),
    blank(),
    h3("1.1.1. Khái niệm An toàn thông tin"),
    p([tb("An toàn thông tin (Information Security – ATTT)"), t(" là lĩnh vực khoa học tập trung vào việc bảo vệ thông tin và hệ thống thông tin khỏi truy cập trái phép, sử dụng sai mục đích, tiết lộ ngoài ý muốn, gián đoạn hoạt động, sửa đổi bất hợp pháp hoặc phá hủy. Theo định nghĩa của Viện Tiêu chuẩn và Công nghệ Quốc gia Hoa Kỳ (NIST), ATTT là \"việc bảo vệ thông tin và hệ thống thông tin khỏi truy cập, sử dụng, tiết lộ, gián đoạn, sửa đổi, hoặc phá hủy trái phép nhằm đảm bảo tính bí mật, toàn vẹn và sẵn dùng.\"")]),
    blank(),
    p([t("Hệ thống thông tin dựa trên máy tính bao gồm năm thành phần cốt lõi: "), tb("(1) Phần cứng (Hardware)"), t(" – máy chủ, thiết bị lưu trữ, mạng; "), tb("(2) Phần mềm (Software)"), t(" – hệ điều hành, ứng dụng; "), tb("(3) Dữ liệu (Data)"), t(" – tài nguyên cần bảo vệ quan trọng nhất; "), tb("(4) Con người (People)"), t("; và "), tb("(5) Quy trình (Procedures)"), t(". Điểm yếu trong bất kỳ thành phần nào đều có thể trở thành cánh cửa để kẻ tấn công khai thác.")]),
    blank(),

    h3("1.1.2. Tam giác CIA Triad – Nền tảng lý thuyết An toàn thông tin"),
    p([t("Mô hình "), tb("CIA Triad (Confidentiality – Integrity – Availability)"), t(" là nền tảng lý thuyết căn bản của khoa học ATTT, cung cấp tiêu chí đo lường thực tiễn để đánh giá mức độ bảo mật của bất kỳ hệ thống thông tin nào.")]),
    blank(),

    caption("Bảng 1.1: Phân tích CIA Triad và áp dụng vào hệ thống CRM 1.0 – VietinBank"),
    new Table({
      width: { size: 9360, type: WidthType.DXA }, columnWidths: [1800, 2000, 2160, 3400],
      rows: [
        new TableRow({ children: [hCell("Thuộc tính", 1800), hCell("Định nghĩa kỹ thuật", 2000), hCell("Mối đe dọa điển hình", 2160), hCell("Áp dụng tại CRM 1.0", 3400)] }),
        new TableRow({ children: [bCell("Tính Bí mật\n(Confidentiality)", 1800, "DDEEFF", true), bCell("Thông tin chỉ được tiếp cận bởi chủ thể được phép", 2000), bCell("Eavesdropping, Credential Theft, MITM, rò rỉ qua API", 2160), bCell("11.000+ cán bộ truy cập KH; CCCD, CIC, số dư cần mã hóa và kiểm soát theo vai trò", 3400)] }),
        new TableRow({ children: [bCell("Tính Toàn vẹn\n(Integrity)", 1800, "DDEEFF", true), bCell("Dữ liệu không bị sửa đổi trái phép, luôn chính xác và đáng tin cậy", 2000), bCell("SQL Injection, gian lận nội bộ, lỗi đồng bộ giao dịch phân tán", 2160), bCell("Luồng CDC đồng bộ real-time phải chống can thiệp; hồ sơ CIC cần chữ ký số", 3400)] }),
        new TableRow({ children: [bCell("Tính Sẵn dùng\n(Availability)", 1800, "DDEEFF", true), bCell("Hệ thống luôn sẵn sàng phục vụ chủ thể được phép đúng thời điểm", 2000), bCell("DDoS, cascading failures, lỗi phần cứng không có dự phòng", 2160), bCell("CRM phải uptime cao giờ giao dịch (8:00–17:00); nghẽn từ Core Banking làm cả hệ thống ngừng", 3400)] }),
      ]
    }),
    blank(),
    p([t("Thuộc tính "), tb("Tính Bí mật"), t(" trong ngữ cảnh ngân hàng là thuộc tính nhạy cảm nhất vì dữ liệu khách hàng thuộc loại "), tb("Dữ liệu Cá nhân Nhạy cảm"), t(". "), tb("Tính Toàn vẹn"), t(" đối mặt thách thức đặc thù của Microservices là "), tb("tính nhất quán phân tán (Distributed Consistency)"), t(" – cần cơ chế Saga Pattern và WORM Audit Log. "), tb("Tính Sẵn dùng"), t(" quan trọng vì gián đoạn dịch vụ dù vài phút cũng gây thiệt hại hàng trăm triệu đồng. Ba thuộc tính có "), tb("mối quan hệ đánh đổi (Trade-off)"), t(" tinh tế mà kiến trúc sư bảo mật phải cân bằng tối ưu.")]),
    blank(),

    h2("1.2. Mô hình tổng quát đảm bảo An toàn thông tin"),
    blank(),
    h3("1.2.1. Nguyên tắc Phòng vệ nhiều lớp có chiều sâu (Defense in Depth)"),
    p([tb("Phòng vệ nhiều lớp có chiều sâu (Defense in Depth – DiD)"), t(" là nguyên tắc kiến trúc quan trọng nhất trong ATTT: xây dựng nhiều lớp phòng thủ chồng chéo, sao cho ngay cả khi kẻ tấn công vượt qua được một lớp, chúng vẫn phải đối mặt với các lớp tiếp theo. Sức mạnh của DiD nằm ở tư duy "), tb("\"giả định thất bại\" (Assume Breach)"), t(": mỗi lớp hoạt động độc lập và không phụ thuộc vào sự hoàn hảo của lớp khác. Ba lớp phòng vệ chính: "), tb("Lớp Tổ chức"), t(" (chính sách, đào tạo, kiểm soát vật lý); "), tb("Lớp Mạng"), t(" (Firewall, WAF, DMZ, IDS/IPS); và "), tb("Lớp Hệ thống/Ứng dụng"), t(" (kiểm soát truy cập, mã hóa, audit logging).")]),
    blank(),

    h3("1.2.2. Bảy vùng hạ tầng CNTT"),
    caption("Bảng 1.2: Bảy vùng hạ tầng CNTT – Đặc điểm và mối đe dọa điển hình"),
    new Table({
      width: { size: 9360, type: WidthType.DXA }, columnWidths: [360, 1800, 1500, 2400, 3300],
      rows: [
        new TableRow({ children: [hCell("STT", 360), hCell("Vùng hạ tầng", 1800), hCell("Mô tả", 1500), hCell("Mối đe dọa chính", 2400), hCell("Biện pháp kiểm soát", 3300)] }),
        ...([
          ["1", "Vùng Người dùng\n(User Domain)", "Con người tương tác với hệ thống", "Lạm dụng quyền, rò rỉ credentials, Phishing", "Đào tạo nhận thức, MFA, Chính sách mật khẩu mạnh"],
          ["2", "Vùng Máy trạm\n(Workstation)", "Máy tính cá nhân, laptop", "Malware, Keylogger, truy cập vật lý", "EDR/Antivirus, Mã hóa ổ đĩa (BitLocker)"],
          ["3", "Vùng LAN", "Mạng nội bộ tổ chức", "ARP Spoofing, MITM nội bộ, Lateral Movement", "802.1X NAC, VLAN phân vùng, IDS/IPS nội bộ"],
          ["4", "Vùng LAN-to-WAN", "Điểm nối mạng nội bộ – Internet", "DDoS, SQL Injection qua API, khai thác web", "Stateful Firewall, WAF, IPS, DMZ, Rate Limiting"],
          ["5", "Vùng WAN", "Hạ tầng Internet công cộng", "Nghe lén đường truyền, BGP Hijacking", "SSL/TLS 1.3 bắt buộc, DNSSEC, VPN"],
          ["6", "Vùng Truy cập từ xa", "Nhân viên/đối tác truy cập ngoài mạng", "Brute Force đăng nhập từ xa, VPN credential theft", "ZTNA, MFA, Just-in-Time Access"],
          ["7", "Vùng Hệ thống/Ứng dụng", "Máy chủ, CSDL, ứng dụng", "SQLi, Privilege Escalation, Ransomware", "RBAC, Mã hóa CSDL, Audit Log, Patch Mgmt"],
        ]).map((row, i) => new TableRow({ children: [cCell(row[0], 360, alt(i)), bCell(row[1], 1800, alt(i), true), bCell(row[2], 1500, alt(i)), bCell(row[3], 2400, alt(i)), bCell(row[4], 3300, alt(i))] }))
      ]
    }),
    blank(),
    p([t("Điểm đặc biệt của mô hình bảy vùng là tư duy "), tb("phân tách ranh giới tin cậy (Trust Boundary)"), t(": mỗi khi thông tin di chuyển từ vùng này sang vùng khác, cần có cơ chế xác thực và kiểm soát bổ sung – nền tảng của triết lý "), tb("Zero Trust Architecture"), t(" (\"Không bao giờ tin tưởng mặc định, luôn luôn xác minh\").")]),
    blank(),

    h2("1.3. Phương pháp đánh giá rủi ro An toàn thông tin"),
    blank(),
    h3("1.3.1. Khái niệm và phương pháp tiếp cận"),
    p([tb("Rủi ro an toàn thông tin"), t(" = Xác suất xảy ra đe dọa × Mức độ tổn hại. Đánh giá rủi ro phải xem xét đồng thời: "), tb("Mối đe dọa (Threat)"), t(", "), tb("Lỗ hổng (Vulnerability)"), t(", và "), tb("Tác động (Impact)"), t(". Phương pháp "), tb("kết hợp (Combined Approach)"), t(" – tận dụng ưu điểm của định tính (nhanh, linh hoạt) và định lượng (chính xác) – được áp dụng trong bài viết này.")]),
    blank(),

    h3("1.3.2. Quy trình 9 bước theo NIST SP 800-30"),
    caption("Bảng 1.3: Quy trình đánh giá rủi ro ATTT 9 bước"),
    new Table({
      width: { size: 9360, type: WidthType.DXA }, columnWidths: [500, 2500, 3560, 2800],
      rows: [
        new TableRow({ children: [hCell("Bước", 500), hCell("Tên bước", 2500), hCell("Nội dung", 3560), hCell("Đầu ra", 2800)] }),
        ...([
          ["1", "Mô tả hệ thống", "Xác định phạm vi, ranh giới, thành phần HW/SW/Data/People/Procedures", "Hồ sơ đặc tả hệ thống"],
          ["2", "Nhận diện mối đe dọa", "Lập danh sách mối đe dọa theo nguồn gốc (ngoài, trong, môi trường)", "Threat Catalog"],
          ["3", "Nhận diện lỗ hổng", "Xác định điểm yếu kỹ thuật và phi kỹ thuật có thể bị khai thác", "Vulnerability List"],
          ["4", "Phân tích kiểm soát hiện có", "Đánh giá biện pháp kiểm soát đã triển khai và đang kế hoạch", "Control List"],
          ["5", "Xác định khả năng xảy ra", "Đánh giá xác suất đe dọa thành công khai thác lỗ hổng (Cao/TB/Thấp)", "Likelihood Score"],
          ["6", "Phân tích tác động", "Mức độ tổn hại tài chính, danh tiếng, pháp lý nếu đe dọa thành công", "Impact Score"],
          ["7", "Xác định mức độ rủi ro", "Tổng hợp XS × Tác động lên Ma trận Rủi ro 5×5", "Risk Matrix"],
          ["8", "Đề xuất biện pháp kiểm soát", "Đề xuất giải pháp kỹ thuật/quy trình giảm rủi ro xuống mức chấp nhận", "Control Recommendations"],
          ["9", "Lập tài liệu kết quả", "Ghi chép toàn bộ kết quả thành báo cáo cho lãnh đạo và nhóm kỹ thuật", "Risk Assessment Report"],
        ]).map((row, i) => new TableRow({ children: [cCell(row[0], 500, alt(i), true), bCell(row[1], 2500, alt(i), true), bCell(row[2], 3560, alt(i)), bCell(row[3], 2800, alt(i))] }))
      ]
    }),
    blank(),
    caption("Bảng 1.4: Ma trận Rủi ro tổng quát 5×5"),
    new Table({
      width: { size: 9360, type: WidthType.DXA }, columnWidths: [1760, 1520, 1520, 1520, 1520, 1520],
      rows: [
        new TableRow({ children: [hCell("XS xảy ra \\ Tác động", 1760), hCell("Rất thấp (1)", 1520), hCell("Thấp (2)", 1520), hCell("Trung bình (3)", 1520), hCell("Cao (4)", 1520), hCell("Rất cao (5)", 1520)] }),
        ...([
          ["Rất cao (5)", ["5\nTB","10\nCao","15\nRất cao","20\nRất cao","25\nRất cao"], ["FFFFFF","FFCC99","FF6666","FF0000","CC0000"]],
          ["Cao (4)",     ["4\nThấp","8\nTB","12\nCao","16\nRất cao","20\nRất cao"],    ["FFFFFF","FFFF99","FFCC99","FF6666","FF0000"]],
          ["Trung bình (3)",["3\nThấp","6\nTB","9\nTB","12\nCao","15\nRất cao"],       ["FFFFFF","FFFFFF","FFFF99","FFCC99","FF6666"]],
          ["Thấp (2)",    ["2\nRất thấp","4\nThấp","6\nTB","8\nTB","10\nCao"],         ["FFFFFF","FFFFFF","FFFFFF","FFFF99","FFCC99"]],
          ["Rất thấp (1)",["1\nRất thấp","2\nRất thấp","3\nThấp","4\nThấp","5\nTB"],  ["FFFFFF","FFFFFF","FFFFFF","FFFFFF","FFFF99"]],
        ]).map((row, i) => new TableRow({ children: [bCell(row[0], 1760, "E8EDF5", true), ...row[1].map((cell, j) => cCell(cell, 1520, row[2][j]))] }))
      ]
    }),
    blank(),

    h2("1.4. Các công nghệ bảo mật lõi"),
    blank(),
    h3("1.4.1. Mật mã học"),
    p([tb("Mật mã học (Cryptography)"), t(" cung cấp nền tảng toán học cho ba dịch vụ bảo mật: bảo mật (Confidentiality) qua mã hóa; toàn vẹn (Integrity) qua hàm băm; và xác thực (Authentication) qua chữ ký số. "), tb("AES-256-GCM"), t(" là chuẩn mã hóa đối xứng bắt buộc cho dữ liệu lưu trữ (tốc độ cao, xác thực toàn vẹn tích hợp). "), tb("RSA-4096/ECDSA-P256"), t(" cho trao đổi khóa và chữ ký số. "), tb("SHA-256"), t(" cho kiểm tra toàn vẹn và audit log. "), tb("TLS 1.3"), t(" cho toàn bộ kênh truyền thông, hỗ trợ Perfect Forward Secrecy.")]),
    blank(),
    caption("Bảng 1.5: So sánh các thuật toán mật mã lõi áp dụng tại CRM 1.0"),
    new Table({
      width: { size: 9360, type: WidthType.DXA }, columnWidths: [1600, 1200, 1600, 2760, 2200],
      rows: [
        new TableRow({ children: [hCell("Thuật toán", 1600), hCell("Loại", 1200), hCell("Độ dài khóa", 1600), hCell("Ứng dụng tại CRM 1.0", 2760), hCell("Tốc độ", 2200)] }),
        ...([
          ["AES-256-GCM", "Đối xứng", "256-bit", "Mã hóa CSDL at-rest, hồ sơ ảnh trên S3", "Rất nhanh (~1 GB/s)"],
          ["RSA-4096", "Bất đối xứng", "4096-bit", "Trao đổi khóa TLS, ký số hồ sơ KH", "Chậm – dùng cho dữ liệu nhỏ"],
          ["ECDSA-P256", "Bất đối xứng (ECC)", "256-bit", "Chứng chỉ TLS API Gateway, ký JWT", "Nhanh, hiệu quả mobile"],
          ["SHA-256", "Hàm băm", "Output 256-bit", "Kiểm tra toàn vẹn, lưu mật khẩu, Audit Log", "Cực nhanh"],
          ["TLS 1.3", "Giao thức", "N/A", "Toàn bộ giao tiếp Browser ↔ API Gateway ↔ Services", "Overhead tối thiểu"],
        ]).map((row, i) => new TableRow({ children: [bCell(row[0], 1600, alt(i), true), cCell(row[1], 1200, alt(i)), cCell(row[2], 1600, alt(i)), bCell(row[3], 2760, alt(i)), bCell(row[4], 2200, alt(i))] }))
      ]
    }),
    blank(),

    h3("1.4.2. Kiểm soát truy cập – RBAC và ABAC"),
    p([tb("RBAC (Role-Based Access Control)"), t(" gán quyền cho Vai trò (Role), người dùng được gán vào vai trò theo chức danh – phù hợp nhất cho môi trường doanh nghiệp ngân hàng. Nguyên tắc cốt lõi: "), tb("Least Privilege"), t(" (quyền tối thiểu) và "), tb("Separation of Duties"), t(" (phân tách nhiệm vụ – SysAdmin không được truy cập dữ liệu KH). "), tb("ABAC (Attribute-Based Access Control)"), t(" mở rộng RBAC bằng ngữ cảnh động: RM chỉ được xem CIC nếu (1) trong giờ làm việc; (2) từ IP nội bộ; VÀ (3) KH đó thuộc danh mục phụ trách – triển khai kiểm soát truy cập theo ngữ cảnh (Context-Aware Access Control).")]),
    blank(),
    caption("Bảng 1.6: Ma trận phân quyền RBAC cho CRM VietinBank"),
    new Table({
      width: { size: 9360, type: WidthType.DXA }, columnWidths: [1600, 1000, 900, 900, 800, 900, 1260, 1100, 900],
      rows: [
        new TableRow({ children: [hCell("Vai trò", 1600), hCell("Xem TT KH", 1000), hCell("Tạo Leads", 900), hCell("Sửa hồ sơ", 900), hCell("Xem CIC", 800), hCell("Tải PDF", 900), hCell("Phê duyệt HM", 1260), hCell("Quản trị HT", 1100), hCell("Báo cáo", 900)] }),
        ...([
          ["Giao dịch viên (Teller)", "✅ CN mình", "✅", "❌", "❌", "❌", "❌", "❌", "❌"],
          ["Chuyên viên QHKH (RM)", "✅ KH p.trách", "✅", "✅", "✅", "✅", "❌", "❌", "❌"],
          ["Trưởng phòng KH", "✅ Toàn CN", "✅", "✅", "✅", "✅", "✅", "❌", "✅"],
          ["Giám đốc Chi nhánh", "✅ Toàn CN", "✅", "✅", "✅", "✅", "✅", "❌", "✅"],
          ["Kiểm soát viên (Auditor)", "✅ Chỉ đọc", "❌", "❌", "✅", "✅", "❌", "❌", "✅"],
          ["Quản trị hệ thống", "❌", "❌", "❌", "❌", "❌", "❌", "✅", "❌"],
        ]).map((row, i) => new TableRow({ children: row.map((cell, j) => {
          const ws = [1600, 1000, 900, 900, 800, 900, 1260, 1100, 900][j];
          const shade = alt(i);
          if (j === 0) return bCell(cell, ws, shade, true);
          const bg = cell === "❌" ? "FFEBEE" : cell.startsWith("✅") ? "E8F5E9" : shade;
          return cCell(cell, ws, bg);
        })}))
      ]
    }),
    blank(),

    h3("1.4.3. Tường lửa và IDS/IPS"),
    caption("Bảng 1.7: So sánh các công nghệ kiểm soát và giám sát an ninh mạng"),
    new Table({
      width: { size: 9360, type: WidthType.DXA }, columnWidths: [1600, 1400, 1800, 1960, 2600],
      rows: [
        new TableRow({ children: [hCell("Công nghệ", 1600), hCell("Tầng OSI", 1400), hCell("Khả năng chính", 1800), hCell("Hạn chế", 1960), hCell("Vị trí triển khai", 2600)] }),
        ...([
          ["Packet Filter FW", "Tầng 3–4", "Lọc IP/Port nhanh", "Không hiểu ngữ cảnh kết nối", "Router biên giới Internet"],
          ["Stateful FW", "Tầng 3–4 + state", "Theo dõi trạng thái phiên", "Không phân tích payload", "Ranh giới vùng mạng DMZ"],
          ["WAF", "Tầng 7 (App)", "Phát hiện SQLi, XSS, CSRF, API Attack", "Chi phí xử lý cao", "Trước API Gateway trong DMZ"],
          ["NGFW", "Tầng 3–7", "DPI, phát hiện malware, lọc URL", "Chi phí đầu tư cao", "Điểm tập trung luồng lưu lượng"],
          ["NIDS/NIPS", "Tầng 3–7", "Phát hiện mẫu tấn công, anomaly", "False positive cần tinh chỉnh", "Trong vùng nội bộ, switch lõi"],
          ["HIDS/HIPS", "Tầng ứng dụng", "Phát hiện hành vi bất thường container", "Tốn tài nguyên tính toán", "Trực tiếp trên Worker Nodes OCP"],
        ]).map((row, i) => new TableRow({ children: [bCell(row[0], 1600, alt(i), true), cCell(row[1], 1400, alt(i)), bCell(row[2], 1800, alt(i)), bCell(row[3], 1960, alt(i)), bCell(row[4], 2600, alt(i))] }))
      ]
    }),
    blank(),
    new Paragraph({ spacing: { before: 300, after: 120 },
      children: [new TextRun({ text: "Tóm tắt Chương 1", bold: true, size: 28, font: "Times New Roman", color: "1F3864" })] }),
    p([t("Chương 1 đã hệ thống hóa nền tảng lý thuyết toàn diện qua bốn trụ cột: CIA Triad (với mối quan hệ đánh đổi tinh tế); Defense in Depth và 7 vùng hạ tầng CNTT (framework phân tích rủi ro có cấu trúc); quy trình đánh giá rủi ro 9 bước với Ma trận 5×5; và bộ công nghệ bảo mật lõi gồm mật mã học, RBAC/ABAC, Firewall/IDS/IPS. Toàn bộ nền tảng lý thuyết này sẽ được vận dụng trực tiếp và liên tục trong Chương 2 (phân tích rủi ro) và Chương 3 (đề xuất giải pháp) như những \"hòn gạch xây dựng\" cụ thể của kiến trúc bảo mật.")]),
    blank(),
  );
  return c;
}

// ── ASSEMBLE ALL ───────────────────────────────────────────────
const allChildren = [
  // Cover
  new Paragraph({ spacing: { before: 800 }, alignment: AlignmentType.CENTER,
    children: [new TextRun({ text: "BỘ GIÁO DỤC VÀ ĐÀO TẠO", bold: true, size: 24, font: "Times New Roman" })] }),
  new Paragraph({ alignment: AlignmentType.CENTER,
    children: [new TextRun({ text: "[TÊN TRƯỜNG ĐẠI HỌC]", bold: true, size: 24, font: "Times New Roman" })] }),
  blank(), blank(), blank(),
  new Paragraph({ alignment: AlignmentType.CENTER,
    children: [new TextRun({ text: "BÀI TẬP LỚN CUỐI KỲ", bold: true, size: 36, font: "Times New Roman", color: "1F3864" })] }),
  blank(),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 200, after: 200 },
    children: [new TextRun({ text: "NGHIÊN CỨU, ĐÁNH GIÁ RỦI RO VÀ ĐỀ XUẤT KIẾN TRÚC BẢO MẬT\nTOÀN DIỆN CHO HỆ THỐNG QUẢN LÝ QUAN HỆ KHÁCH HÀNG (CRM 1.0)\nTẠI NGÂN HÀNG TMCP CÔNG THƯƠNG VIỆT NAM (VIETINBANK)", bold: true, size: 28, font: "Times New Roman", color: "C00000" })] }),
  blank(), blank(),
  new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: "Môn học: An toàn thông tin trong Hệ thống thông tin quản lý", size: 26, font: "Times New Roman" })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: "Học viên: [Họ và tên]", size: 26, font: "Times New Roman" })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: "Năm học: 2025 – 2026", size: 26, font: "Times New Roman" })] }),
  blank(), blank(), blank(), blank(),
  new Paragraph({ children: [new PageBreak()] }),
  ...buildChapter1(),
  ...buildChapter2(),
  ...buildChapter3(),
  ...buildChapter4AndConclusion(),
];

const doc = new Document({
  styles: {
    default: { document: { run: { font: "Times New Roman", size: 26 } } },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 32, bold: true, font: "Times New Roman", color: "1F3864" },
        paragraph: { spacing: { before: 400, after: 200 }, outlineLevel: 0 } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 28, bold: true, font: "Times New Roman", color: "2E5096" },
        paragraph: { spacing: { before: 320, after: 160 }, outlineLevel: 1 } },
      { id: "Heading3", name: "Heading 3", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 26, bold: true, italics: true, font: "Times New Roman", color: "1F3864" },
        paragraph: { spacing: { before: 240, after: 120 }, outlineLevel: 2 } },
    ]
  },
  numbering: { config: [] },
  sections: [{
    properties: {
      page: {
        size: { width: 11906, height: 16838 },
        margin: { top: 1418, bottom: 1134, left: 1701, right: 1134 }
      }
    },
    headers: { default: new Header({ children: [
      new Paragraph({ border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: "1F3864", space: 4 } }, alignment: AlignmentType.RIGHT,
        children: [new TextRun({ text: "Bài tập lớn: Bảo mật CRM 1.0 – VietinBank", size: 18, font: "Times New Roman", color: "555555", italics: true })] })
    ]})},
    footers: { default: new Footer({ children: [
      new Paragraph({ border: { top: { style: BorderStyle.SINGLE, size: 6, color: "1F3864", space: 4 } }, alignment: AlignmentType.CENTER,
        children: [new TextRun({ text: "- ", size: 20, font: "Times New Roman" }),
                   new TextRun({ children: [PageNumber.CURRENT], size: 20, font: "Times New Roman" }),
                   new TextRun({ text: " -", size: 20, font: "Times New Roman" })] })
    ]})},
    children: allChildren
  }]
});

Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync('/sessions/funny-affectionate-sagan/mnt/outputs/ATTT_CRM_VietinBank_HOAN_CHINH.docx', buf);
  console.log('Done: ATTT_CRM_VietinBank_HOAN_CHINH.docx');
});
