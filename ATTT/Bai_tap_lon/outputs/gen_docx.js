const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  AlignmentType, HeadingLevel, BorderStyle, WidthType, ShadingType,
  Header, Footer, PageNumber, LevelFormat, PageBreak
} = require('docx');
const fs = require('fs');

const BORDER = { style: BorderStyle.SINGLE, size: 1, color: "AAAAAA" };
const BORDERS = { top: BORDER, bottom: BORDER, left: BORDER, right: BORDER };
const CELL_MARGINS = { top: 80, bottom: 80, left: 120, right: 120 };

// Header cell style
function hCell(text, widthDxa, colSpan) {
  const cell = {
    borders: BORDERS,
    width: { size: widthDxa, type: WidthType.DXA },
    shading: { fill: "1F3864", type: ShadingType.CLEAR },
    margins: CELL_MARGINS,
    children: [new Paragraph({
      alignment: AlignmentType.CENTER,
      children: [new TextRun({ text, bold: true, color: "FFFFFF", size: 20, font: "Times New Roman" })]
    })]
  };
  if (colSpan) cell.columnSpan = colSpan;
  return new TableCell(cell);
}

// Body cell
function bCell(text, widthDxa, shade, bold) {
  return new TableCell({
    borders: BORDERS,
    width: { size: widthDxa, type: WidthType.DXA },
    shading: { fill: shade || "FFFFFF", type: ShadingType.CLEAR },
    margins: CELL_MARGINS,
    children: [new Paragraph({
      children: [new TextRun({ text, size: 20, bold: !!bold, font: "Times New Roman" })]
    })]
  });
}

// Centered body cell
function cCell(text, widthDxa, shade, bold) {
  return new TableCell({
    borders: BORDERS,
    width: { size: widthDxa, type: WidthType.DXA },
    shading: { fill: shade || "FFFFFF", type: ShadingType.CLEAR },
    margins: CELL_MARGINS,
    children: [new Paragraph({
      alignment: AlignmentType.CENTER,
      children: [new TextRun({ text, size: 20, bold: !!bold, font: "Times New Roman" })]
    })]
  });
}

// Body row alternate shading
function altShade(i) { return i % 2 === 0 ? "FFFFFF" : "EEF2F8"; }

// Normal paragraph
function p(runs, spacing, indent) {
  return new Paragraph({
    alignment: AlignmentType.BOTH,
    spacing: spacing || { before: 60, after: 60, line: 360, lineRule: "auto" },
    indent: indent || null,
    children: runs
  });
}

function t(text, opts) {
  return new TextRun({ text, font: "Times New Roman", size: 26, ...opts });
}

function tb(text) { return t(text, { bold: true }); }

// Heading helpers
function h1(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_1,
    spacing: { before: 400, after: 200 },
    children: [new TextRun({ text, bold: true, size: 32, font: "Times New Roman", color: "1F3864" })]
  });
}
function h2(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_2,
    spacing: { before: 320, after: 160 },
    children: [new TextRun({ text, bold: true, size: 28, font: "Times New Roman", color: "2E5096" })]
  });
}
function h3(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_3,
    spacing: { before: 240, after: 120 },
    children: [new TextRun({ text, bold: true, italic: true, size: 26, font: "Times New Roman", color: "1F3864" })]
  });
}

function blank() {
  return new Paragraph({ children: [new TextRun("")], spacing: { before: 60, after: 60 } });
}

const LINE = { before: 80, after: 80, line: 360, lineRule: "auto" };

// ============================================================
// CONTENT
// ============================================================

const children = [];

// ─── COVER PAGE ───
children.push(
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
  blank(), blank(), blank(),
  new Paragraph({ alignment: AlignmentType.CENTER,
    children: [new TextRun({ text: "Môn học: An toàn thông tin trong Hệ thống thông tin quản lý", size: 26, font: "Times New Roman" })] }),
  new Paragraph({ alignment: AlignmentType.CENTER,
    children: [new TextRun({ text: "Học viên: [Họ và tên]", size: 26, font: "Times New Roman" })] }),
  new Paragraph({ alignment: AlignmentType.CENTER,
    children: [new TextRun({ text: "Năm học: 2025 – 2026", size: 26, font: "Times New Roman" })] }),
  blank(), blank(), blank(), blank(),
  new Paragraph({ children: [new PageBreak()] })
);

// ─── LỜI MỞ ĐẦU ───
children.push(
  new Paragraph({ heading: HeadingLevel.HEADING_1, spacing: { before: 400, after: 200 }, alignment: AlignmentType.CENTER,
    children: [new TextRun({ text: "LỜI MỞ ĐẦU", bold: true, size: 32, font: "Times New Roman", color: "1F3864" })] }),
  blank(),
  h2("1. Tính cấp thiết của đề tài"),
  p([t("Trong bối cảnh chuyển đổi số diễn ra với tốc độ chưa từng có, hệ thống tài chính – ngân hàng Việt Nam đang đứng trước những thách thức bảo mật thông tin vừa cấp bách, vừa phức tạp hơn bất kỳ thời điểm nào trong lịch sử. Theo báo cáo của Cục An toàn thông tin – Bộ Thông tin và Truyền thông, trong giai đoạn 2022–2024, lĩnh vực tài chính – ngân hàng liên tục nằm trong nhóm các ngành bị tấn công mạng nhiều nhất, với số lượng sự cố được ghi nhận tăng trưởng bình quân trên 35% mỗi năm. Các hình thức tấn công ngày càng tinh vi, từ các chiến dịch APT (Advanced Persistent Threat) nhắm vào hệ thống lõi, cho đến các kỹ thuật khai thác API, đánh cắp phiên đăng nhập và lạm dụng quyền hạn nội bộ.")], LINE, { firstLine: 720 }),
  blank(),
  p([tb("Ngân hàng TMCP Công Thương Việt Nam (VietinBank)"), t(", với mạng lưới hơn 150 chi nhánh, hơn 1.000 phòng giao dịch và đội ngũ hơn 25.000 nhân viên, đang vận hành một trong những hệ sinh thái công nghệ thông tin quy mô nhất trong khối ngân hàng thương mại trong nước. Trong chiến lược hiện đại hóa hạ tầng công nghệ giai đoạn 2022–2025, VietinBank đã triển khai "), tb("Hệ thống Quản lý Quan hệ Khách hàng phiên bản 1.0 (CRM 1.0)"), t(" theo kiến trúc "), tb("Cloud-Native Microservices"), t(" trên nền tảng "), tb("Red Hat OpenShift Container Platform (OCP)"), t(". Đây là một cuộc cách mạng về mặt kiến trúc phần mềm, chuyển đổi hoàn toàn từ mô hình nguyên khối (Monolithic Architecture) sang mô hình dịch vụ vi phân tán, nhằm đạt được khả năng mở rộng linh hoạt, tốc độ triển khai cao và hiệu quả vận hành vượt trội.")], LINE, { firstLine: 720 }),
  blank(),
  p([t("Tuy nhiên, mọi sự chuyển đổi kiến trúc đều mang theo những "), tb("rủi ro bảo mật đặc thù và mới nổi"), t(". Hệ thống CRM 1.0 của VietinBank lưu trữ và xử lý thông tin của hàng chục triệu khách hàng cá nhân và doanh nghiệp, bao gồm dữ liệu định danh (CCCD, hộ chiếu), thông tin tài chính (số dư, lịch sử giao dịch), hồ sơ tín dụng CIC (Credit Information Centre) và hàng loạt dữ liệu nhạy cảm khác. Sự rò rỉ, sai lệch hay gián đoạn trong việc truy cập các dữ liệu này không chỉ gây thiệt hại tài chính trực tiếp mà còn ảnh hưởng nghiêm trọng đến uy tín thương hiệu và niềm tin của khách hàng – vốn là tài sản cốt lõi của bất kỳ tổ chức tín dụng nào.")], LINE, { firstLine: 720 }),
  blank(),
  p([t("Kiến trúc Microservices, dù mang lại nhiều lợi thế về kỹ thuật, đồng thời cũng mở ra một "), tb("bề mặt tấn công (Attack Surface) rộng hơn và phức tạp hơn"), t(": hàng chục đầu điểm API cần được bảo vệ; dữ liệu phân tán trên nhiều loại cơ sở dữ liệu (PostgreSQL, Oracle, Redis) đòi hỏi chiến lược bảo mật nhất quán; giao tiếp dịch vụ nội bộ qua Message Queue (Apache Kafka) có thể trở thành điểm yếu nếu không được mã hóa và xác thực nghiêm ngặt; và sự phụ thuộc vào hệ thống di sản (Legacy Core Banking) tạo ra những điểm nghẽn cổ chai không dễ xử lý.")], LINE, { firstLine: 720 }),
  blank(),
  p([t("Trước thực tiễn đó, "), tb("việc nghiên cứu một cách hệ thống các rủi ro bảo mật và đề xuất một kiến trúc bảo mật toàn diện, phù hợp với đặc thù kiến trúc của hệ thống CRM 1.0 tại VietinBank là nhiệm vụ vừa có giá trị học thuật, vừa có ý nghĩa ứng dụng thực tiễn cao"), t(". Đây chính là lý do cốt lõi thôi thúc tác giả lựa chọn và theo đuổi đề tài này.")], LINE, { firstLine: 720 }),
  blank(),

  h2("2. Mục tiêu nghiên cứu"),
  p([t("Bài tập lớn này hướng tới ba mục tiêu nghiên cứu chính, có mối quan hệ logic và kế thừa lẫn nhau:")], LINE, { firstLine: 720 }),
  blank(),
  p([tb("Mục tiêu 1:"), t(" Hệ thống hóa các kiến thức lý thuyết nền tảng về An toàn thông tin doanh nghiệp, bao gồm mô hình CIA Triad, nguyên tắc Phòng vệ chiều sâu (Defense in Depth), phương pháp đánh giá rủi ro 9 bước và các công nghệ bảo mật lõi, làm cơ sở lý luận vững chắc cho toàn bộ bài viết.")], LINE, { indent: { left: 720 } }),
  blank(),
  p([tb("Mục tiêu 2:"), t(" Phân tích hiện trạng kiến trúc kỹ thuật của hệ thống CRM 1.0 tại VietinBank theo góc nhìn đa chiều (hạ tầng phần cứng, phần mềm, dữ liệu), sau đó nhận diện và đánh giá định tính các rủi ro bảo mật tiềm ẩn tương ứng với từng vùng hạ tầng CNTT của hệ thống.")], LINE, { indent: { left: 720 } }),
  blank(),
  p([tb("Mục tiêu 3:"), t(" Trên cơ sở các rủi ro đã được nhận diện, đề xuất một kiến trúc bảo mật đa lớp cụ thể, bao gồm các giải pháp kỹ thuật (mã hóa, kiểm soát truy cập, bảo mật API, xử lý lỗi phân tán) và các chính sách quản trị (ISMS theo ISO/IEC 27001, DevSecOps, tuân thủ pháp luật Việt Nam) nhằm bảo vệ toàn diện hệ thống CRM 1.0.")], LINE, { indent: { left: 720 } }),
  blank(),

  h2("3. Đối tượng và Phạm vi nghiên cứu"),
  p([tb("Đối tượng nghiên cứu:"), t(" Kiến trúc bảo mật thông tin và các giải pháp kỹ thuật, quản trị đảm bảo an toàn thông tin cho hệ thống thông tin doanh nghiệp trong lĩnh vực ngân hàng.")], LINE, { firstLine: 720 }),
  blank(),
  p([tb("Phạm vi nghiên cứu:"), t(" Bài viết tập trung vào "), tb("Hệ thống CRM 1.0 (giai đoạn MVP1)"), t(" của VietinBank, bao gồm toàn bộ stack công nghệ từ lớp Front-end (NextJS v.14), lớp trung gian (API Gateway, Apache Kafka), lớp ứng dụng vi dịch vụ (chạy trên Red Hat OpenShift), đến lớp dữ liệu (PostgreSQL, Oracle, Redis, lưu trữ S3). Phạm vi bảo mật được xem xét trải dài từ điểm truy cập của người dùng cuối (hơn 11.000 cán bộ, giao dịch viên) đến hạ tầng lưu trữ dữ liệu tập trung, bao gồm cả điểm tích hợp với Core Banking và các kênh số đối ngoại (iPay, eFast).")], LINE, { firstLine: 720 }),
  blank(),

  h2("4. Phương pháp nghiên cứu"),
  p([t("Bài viết sử dụng phương pháp "), tb("nghiên cứu định tính kết hợp phân tích hệ thống"), t(", cụ thể:")], LINE, { firstLine: 720 }),
  blank(),
  p([tb("Phương pháp phân tích tài liệu:"), t(" Tổng hợp và hệ thống hóa kiến thức từ giáo trình môn học An toàn thông tin, các tiêu chuẩn quốc tế (ISO/IEC 27001, NIST SP 800-30) và tài liệu kỹ thuật của hệ thống CRM 1.0 VietinBank.")], LINE, { indent: { left: 720 } }),
  blank(),
  p([tb("Phương pháp tiếp cận theo mô hình:"), t(" Vận dụng mô hình "), tb("Phòng vệ chiều sâu (Defense in Depth)"), t(" làm khung phân tích và thiết kế kiến trúc bảo mật; vận dụng "), tb("phương pháp đánh giá rủi ro kết hợp (Combined Approach)"), t(" để nhận diện và lượng giá rủi ro trên từng vùng hạ tầng.")], LINE, { indent: { left: 720 } }),
  blank(),
  p([tb("Phương pháp đối chiếu thực tiễn:"), t(" Đối chiếu kiến trúc thực tế của CRM 1.0 với các best-practice bảo mật trong ngành công nghiệp phần mềm tài chính, từ đó xây dựng các đề xuất có tính khả thi và phù hợp với đặc thù môi trường vận hành.")], LINE, { indent: { left: 720 } }),
  blank(),
  new Paragraph({ children: [new PageBreak()] })
);

// ─── CHƯƠNG 1 ───
children.push(
  h1("CHƯƠNG 1: CƠ SỞ LÝ THUYẾT VỀ AN TOÀN THÔNG TIN TRONG HỆ THỐNG DOANH NGHIỆP"),
  blank(),

  h2("1.1. Tổng quan về An toàn thông tin"),
  blank(),
  h3("1.1.1. Khái niệm An toàn thông tin"),
  p([tb("An toàn thông tin (Information Security – ATTT)"), t(" là một lĩnh vực khoa học và thực hành rộng lớn, tập trung vào việc bảo vệ thông tin và hệ thống thông tin khỏi sự truy cập trái phép, sử dụng sai mục đích, tiết lộ ngoài ý muốn, gián đoạn hoạt động, sửa đổi bất hợp pháp hoặc phá hủy. Theo định nghĩa của Viện Tiêu chuẩn và Công nghệ Quốc gia Hoa Kỳ (NIST), ATTT là \"việc bảo vệ thông tin và hệ thống thông tin khỏi truy cập, sử dụng, tiết lộ, gián đoạn, sửa đổi, hoặc phá hủy trái phép nhằm đảm bảo tính bí mật, toàn vẹn và sẵn dùng.\"")], LINE, { firstLine: 720 }),
  blank(),
  p([t("Trong môi trường ngân hàng hiện đại, ATTT không còn là vấn đề thuần túy kỹ thuật mà đã trở thành một "), tb("yếu tố chiến lược kinh doanh"), t(". Một sự cố bảo mật không chỉ gây thiệt hại tài chính trực tiếp (chi phí khắc phục, bồi thường) mà còn kéo theo hệ lụy pháp lý (vi phạm luật bảo vệ dữ liệu cá nhân), thiệt hại thương hiệu và mất niềm tin từ khách hàng – những thiệt hại vô hình nhưng có thể còn nghiêm trọng hơn về dài hạn.")], LINE, { firstLine: 720 }),
  blank(),
  p([t("Hệ thống thông tin dựa trên máy tính bao gồm năm thành phần cốt lõi có mối quan hệ tương tác chặt chẽ: "), tb("(1) Phần cứng (Hardware)"), t(" – máy chủ, thiết bị lưu trữ, thiết bị mạng; "), tb("(2) Phần mềm (Software)"), t(" – hệ điều hành, ứng dụng, middleware; "), tb("(3) Dữ liệu (Data)"), t(" – tài nguyên cần bảo vệ quan trọng nhất; "), tb("(4) Con người (People)"), t(" – người dùng, quản trị viên, nhà phát triển; và "), tb("(5) Quy trình (Procedures)"), t(" – chính sách vận hành và kiểm soát. Bất kỳ điểm yếu nào trong một trong năm thành phần trên đều có thể trở thành cánh cửa để kẻ tấn công khai thác, do đó một chiến lược ATTT toàn diện phải xem xét và bảo vệ đồng thời cả năm lớp này.")], LINE, { firstLine: 720 }),
  blank(),

  h3("1.1.2. Tam giác CIA Triad – Nền tảng lý thuyết của An toàn thông tin"),
  p([t("Mô hình "), tb("CIA Triad (Confidentiality – Integrity – Availability)"), t(" là nền tảng lý thuyết căn bản và bất biến của khoa học An toàn thông tin. Ba thuộc tính này không chỉ là khái niệm lý thuyết trừu tượng mà còn là "), tb("tiêu chí đo lường thực tiễn"), t(" để đánh giá mức độ bảo mật của bất kỳ hệ thống thông tin nào. Mỗi quyết định kiến trúc bảo mật, mỗi chính sách kiểm soát hay mỗi giải pháp kỹ thuật đều có thể và cần được lý giải dựa trên một hoặc nhiều thuộc tính trong bộ ba này.")], LINE, { firstLine: 720 }),
  blank(),

  // TABLE 1.1: CIA Triad
  new Paragraph({ spacing: { before: 200, after: 80 }, alignment: AlignmentType.CENTER,
    children: [new TextRun({ text: "Bảng 1.1: Phân tích CIA Triad và áp dụng vào hệ thống CRM 1.0 – VietinBank", bold: true, size: 22, italics: true, font: "Times New Roman" })] }),
  new Table({
    width: { size: 9360, type: WidthType.DXA },
    columnWidths: [1800, 2000, 2160, 3400],
    rows: [
      new TableRow({ children: [hCell("Thuộc tính", 1800), hCell("Định nghĩa kỹ thuật", 2000), hCell("Mối đe dọa điển hình", 2160), hCell("Áp dụng tại CRM 1.0", 3400)] }),
      new TableRow({ children: [
        bCell("Tính Bí mật\n(Confidentiality)", 1800, "DDEEFF", true),
        bCell("Đảm bảo thông tin chỉ được tiếp cận bởi những chủ thể được phép; ngăn chặn mọi hình thức tiết lộ trái phép", 2000),
        bCell("Nghe lén (Eavesdropping), đánh cắp thông tin xác thực, tấn công Man-in-the-Middle, rò rỉ qua API", 2160),
        bCell("Hơn 11.000 cán bộ truy cập dữ liệu KH; CCCD, CIC, số dư tài khoản cần mã hóa và kiểm soát hiển thị theo vai trò", 3400),
      ]}),
      new TableRow({ children: [
        bCell("Tính Toàn vẹn\n(Integrity)", 1800, "DDEEFF", true),
        bCell("Đảm bảo thông tin và quy trình xử lý không bị sửa đổi trái phép, dữ liệu luôn chính xác và đáng tin cậy", 2000),
        bCell("Tấn công SQL Injection, gian lận nội bộ thay đổi hồ sơ KH, lỗi đồng bộ trong giao dịch phân tán", 2160),
        bCell("Luồng CDC đồng bộ real-time từ Core Banking phải đảm bảo không bị can thiệp; hồ sơ CIC cần chữ ký số xác nhận tính gốc", 3400),
      ]}),
      new TableRow({ children: [
        bCell("Tính Sẵn dùng\n(Availability)", 1800, "DDEEFF", true),
        bCell("Đảm bảo hệ thống và dữ liệu luôn sẵn sàng phục vụ cho các chủ thể được phép, vào đúng thời điểm cần", 2000),
        bCell("Tấn công DDoS, cascading failures, lỗi phần cứng không có dự phòng", 2160),
        bCell("CRM phải đảm bảo uptime cao giờ giao dịch (8:00–17:00); nghẽn cổ chai từ Legacy Core Banking có thể làm toàn bộ CRM ngừng hoạt động", 3400),
      ]}),
    ]
  }),
  blank(),
  p([t("Thuộc tính "), tb("Tính Bí mật (Confidentiality)"), t(" đề cập đến quyền kiểm soát thông tin – ai được phép biết điều gì. Trong ngữ cảnh ngân hàng, đây là thuộc tính nhạy cảm nhất vì dữ liệu khách hàng thuộc loại "), tb("Dữ liệu Cá nhân Nhạy cảm (Sensitive Personal Data)"), t(" được bảo vệ bởi pháp luật. Tính bí mật không chỉ bị đe dọa từ bên ngoài (tin tặc) mà còn từ bên trong (insider threats): một giao dịch viên có thể truy xuất thông tin tài chính của khách hàng không thuộc phạm vi phục vụ của mình, hoặc một nhân viên rời việc nhưng tài khoản truy cập chưa bị thu hồi. Kỹ thuật bảo vệ tính bí mật bao gồm mã hóa dữ liệu, kiểm soát truy cập theo vai trò (RBAC), che mờ dữ liệu (Data Masking) và phân vùng mạng (Network Segmentation).")], LINE, { firstLine: 720 }),
  blank(),
  p([t("Thuộc tính "), tb("Tính Toàn vẹn (Integrity)"), t(" đề cập đến sự chính xác, nhất quán và đáng tin cậy của dữ liệu trong suốt vòng đời của nó. Trong kiến trúc Microservices của CRM 1.0, tính toàn vẹn đối mặt với thách thức đặc thù là "), tb("tính nhất quán phân tán (Distributed Consistency)"), t(": khi một giao dịch kinh doanh trải dài trên nhiều microservices và nhiều cơ sở dữ liệu, làm thế nào để đảm bảo hoặc tất cả các phần thay đổi cùng được áp dụng thành công, hoặc tất cả cùng bị hủy – không xảy ra trạng thái dở dang? Công nghệ bảo vệ toàn vẹn bao gồm hàm băm mật mã (SHA-256), chữ ký số (Digital Signature), giao thức giao dịch phân tán (2PC, Saga Pattern) và nhật ký kiểm toán chống giả mạo (WORM Audit Log).")], LINE, { firstLine: 720 }),
  blank(),
  p([t("Thuộc tính "), tb("Tính Sẵn dùng (Availability)"), t(" đảm bảo hệ thống luôn phục vụ được khi người dùng hợp pháp cần. Đây là thuộc tính thường bị đánh giá thấp trong các thiết kế bảo mật truyền thống, nhưng lại cực kỳ quan trọng trong môi trường ngân hàng vì gián đoạn dịch vụ dù chỉ vài phút cũng có thể gây thiệt hại hàng trăm triệu đồng và ảnh hưởng trực tiếp đến hàng nghìn giao dịch tài chính. Tính sẵn dùng bị đe dọa không chỉ bởi các cuộc tấn công chủ động (DDoS) mà còn bởi các lỗi kỹ thuật (cascading failures trong kiến trúc Microservices) và thiên tai. Các biện pháp bảo vệ bao gồm thiết kế dự phòng (Redundancy), cân bằng tải (Load Balancing), Circuit Breaker Pattern và kế hoạch khôi phục sau thảm họa (Disaster Recovery Plan).")], LINE, { firstLine: 720 }),
  blank(),
  p([t("Ba thuộc tính CIA không tồn tại độc lập mà có "), tb("mối quan hệ đánh đổi (Trade-off) tinh tế"), t(": tăng cường tính bí mật (ví dụ, thêm nhiều lớp xác thực) có thể làm giảm tính sẵn dùng; tăng cường tính sẵn dùng (nhân bản dữ liệu ra nhiều node) có thể làm tăng nguy cơ rò rỉ bí mật. Năng lực của một kiến trúc sư bảo mật chính là ở khả năng "), tb("tìm kiếm điểm cân bằng tối ưu"), t(" giữa ba thuộc tính này, phù hợp với yêu cầu nghiệp vụ và mức độ chấp nhận rủi ro của tổ chức.")], LINE, { firstLine: 720 }),
  blank(),

  h2("1.2. Mô hình tổng quát đảm bảo An toàn thông tin"),
  blank(),
  h3("1.2.1. Nguyên tắc Phòng vệ nhiều lớp có chiều sâu (Defense in Depth)"),
  p([tb("Phòng vệ nhiều lớp có chiều sâu (Defense in Depth – DiD)"), t(" là một trong những nguyên tắc kiến trúc quan trọng nhất trong lĩnh vực An toàn thông tin, được vay mượn từ học thuyết quân sự cổ điển: không bao giờ dựa vào một hàng rào phòng thủ duy nhất, mà phải xây dựng nhiều lớp phòng thủ chồng chéo, sao cho ngay cả khi kẻ tấn công vượt qua được một lớp, chúng vẫn phải đối mặt với các lớp tiếp theo trước khi chạm được vào tài sản cần bảo vệ.")], LINE, { firstLine: 720 }),
  blank(),
  p([t("Theo mô hình này, hệ thống phòng thủ được tổ chức thành "), tb("ba lớp chính"), t(" có tính chất bổ trợ lẫn nhau:")], LINE, { firstLine: 720 }),
  blank(),
  p([tb("Lớp An ninh Cơ quan/Tổ chức (Organizational Security):"), t(" Đây là lớp phòng vệ phi kỹ thuật nhưng không kém phần quan trọng, bao gồm chính sách bảo mật (Security Policy), quy trình quản lý nhân sự (đào tạo, sàng lọc nhân viên), các biện pháp kiểm soát vật lý và văn hóa an toàn thông tin. Lớp này nhắm vào yếu tố "), tb("Con người (People)"), t(" và "), tb("Quy trình (Procedures)"), t(" – vốn là nguồn gốc của hơn 70% các sự cố bảo mật theo thống kê từ IBM Security Reports.")], LINE, { indent: { left: 720, hanging: 360 } }),
  blank(),
  p([tb("Lớp An ninh Mạng (Network Security):"), t(" Bảo vệ hạ tầng mạng và luồng thông tin di chuyển giữa các thành phần hệ thống. Các công cụ tiêu biểu bao gồm Tường lửa (Firewall), Hệ thống phát hiện và ngăn chặn xâm nhập (IDS/IPS), Tường lửa ứng dụng web (WAF), phân vùng mạng DMZ và mã hóa đường truyền (TLS/SSL). Đây là lớp chịu trách nhiệm "), tb("lọc và kiểm soát luồng lưu lượng mạng"), t(" theo chính sách cho phép/từ chối.")], LINE, { indent: { left: 720, hanging: 360 } }),
  blank(),
  p([tb("Lớp An ninh Hệ thống & Ứng dụng (System/Application Security):"), t(" Bảo vệ trực tiếp tại tầng hệ điều hành, ứng dụng và cơ sở dữ liệu. Bao gồm kiểm soát truy cập (Access Control), quản lý bản vá (Patch Management), mã hóa dữ liệu lưu trữ (Encryption at Rest), kiểm toán và ghi nhật ký (Audit Logging). Đây là lớp cuối cùng trực tiếp bảo vệ "), tb("tài sản thông tin (Data)"), t(".")], LINE, { indent: { left: 720, hanging: 360 } }),
  blank(),
  p([t("Sức mạnh của DiD nằm ở tư duy "), tb("\"giả định thất bại\" (Assume Breach)"), t(": thiết kế hệ thống với giả định rằng một vài lớp phòng vệ sẽ bị vượt qua, do đó mỗi lớp phải hoạt động độc lập và không phụ thuộc vào sự hoàn hảo của lớp khác.")], LINE, { firstLine: 720 }),
  blank(),

  h3("1.2.2. Bảy vùng hạ tầng CNTT và các mối đe dọa tương ứng"),
  p([t("Mô hình bảy vùng hạ tầng CNTT (Seven Domains of IT Infrastructure) là một framework phân tích rủi ro cấu trúc, giúp kiến trúc sư bảo mật có cái nhìn toàn diện về mọi điểm có thể bị tấn công trong một tổ chức. Mỗi vùng có đặc điểm riêng biệt về các mối đe dọa tiềm ẩn và các biện pháp kiểm soát tương ứng.")], LINE, { firstLine: 720 }),
  blank(),

  new Paragraph({ spacing: { before: 200, after: 80 }, alignment: AlignmentType.CENTER,
    children: [new TextRun({ text: "Bảng 1.2: Bảy vùng hạ tầng CNTT – Đặc điểm và mối đe dọa điển hình", bold: true, size: 22, italics: true, font: "Times New Roman" })] }),
  new Table({
    width: { size: 9360, type: WidthType.DXA },
    columnWidths: [360, 1800, 1500, 2400, 3300],
    rows: [
      new TableRow({ children: [hCell("STT", 360), hCell("Vùng hạ tầng", 1800), hCell("Mô tả", 1500), hCell("Mối đe dọa chính", 2400), hCell("Biện pháp kiểm soát", 3300)] }),
      ...[
        ["1", "Vùng Người dùng\n(User Domain)", "Con người tương tác với hệ thống thông tin", "Lạm dụng quyền hạn, rò rỉ credentials, Social Engineering, Phishing", "Đào tạo nhận thức, Chính sách mật khẩu mạnh, Xác thực đa yếu tố (MFA)"],
        ["2", "Vùng Máy trạm\n(Workstation Domain)", "Máy tính cá nhân, laptop của người dùng cuối", "Phần mềm độc hại (Malware), Keylogger, truy cập vật lý trái phép", "Antivirus/EDR, Mã hóa ổ đĩa (BitLocker), Chính sách khóa màn hình"],
        ["3", "Vùng LAN\n(LAN Domain)", "Mạng nội bộ của tổ chức", "ARP Spoofing, Man-in-the-Middle nội bộ, Lateral Movement sau xâm nhập", "802.1X Network Access Control, VLAN phân vùng, IDS/IPS nội bộ"],
        ["4", "Vùng LAN-to-WAN", "Điểm kết nối giữa mạng nội bộ và Internet", "DDoS, SQL Injection qua API, tấn công ứng dụng web, khai thác lỗ hổng firewall", "Stateful Firewall, WAF, IPS, DMZ, Rate Limiting"],
        ["5", "Vùng WAN\n(WAN Domain)", "Hạ tầng Internet công cộng", "Nghe lén đường truyền, BGP Hijacking, DNS Poisoning", "SSL/TLS mã hóa đường truyền, DNSSEC, VPN"],
        ["6", "Vùng Truy cập từ xa", "Nhân viên/đối tác truy cập từ bên ngoài mạng", "Brute Force đăng nhập từ xa, đánh cắp VPN credentials", "Zero Trust Network Access (ZTNA), MFA, Just-in-Time Access"],
        ["7", "Vùng Hệ thống/\nỨng dụng", "Máy chủ, cơ sở dữ liệu, ứng dụng", "Khai thác lỗ hổng ứng dụng, SQL Injection, Privilege Escalation, Ransomware", "Patch Management, RBAC, Mã hóa CSDL, Audit Logging, Backup"],
      ].map((row, i) => new TableRow({ children: [
        cCell(row[0], 360, altShade(i)),
        bCell(row[1], 1800, altShade(i), true),
        bCell(row[2], 1500, altShade(i)),
        bCell(row[3], 2400, altShade(i)),
        bCell(row[4], 3300, altShade(i)),
      ]}))
    ]
  }),
  blank(),
  p([t("Điểm đặc biệt của mô hình bảy vùng là tư duy "), tb("phân tách ranh giới tin cậy (Trust Boundary)"), t(": mỗi khi thông tin di chuyển từ vùng này sang vùng khác, cần có cơ chế xác thực và kiểm soát bổ sung, không được mặc nhiên tin tưởng rằng thông tin đến từ vùng nội bộ là an toàn. Đây chính là nền tảng của triết lý "), tb("Zero Trust Architecture"), t(" – \"Không bao giờ tin tưởng mặc định, luôn luôn xác minh\" – một hướng tiếp cận ngày càng được các tổ chức tài chính lớn trên thế giới áp dụng.")], LINE, { firstLine: 720 }),
  blank(),

  h2("1.3. Phương pháp đánh giá rủi ro An toàn thông tin"),
  blank(),
  h3("1.3.1. Khái niệm Rủi ro và Phương pháp tiếp cận"),
  p([tb("Rủi ro an toàn thông tin (Information Security Risk)"), t(" được định nghĩa là khả năng xảy ra của một sự kiện đe dọa, kết hợp với mức độ tổn hại mà sự kiện đó gây ra. Về mặt toán học, công thức đơn giản hóa thường được sử dụng là:")], LINE, { firstLine: 720 }),
  blank(),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 120, after: 120 },
    children: [new TextRun({ text: "Rủi ro = Xác suất xảy ra đe dọa × Mức độ tổn hại", bold: true, italics: true, size: 26, font: "Times New Roman", color: "C00000" })] }),
  blank(),
  p([t("Trong thực tế, đánh giá rủi ro ATTT phức tạp hơn vì phải xem xét đồng thời ba yếu tố: "), tb("(1) Mối đe dọa (Threat)"), t(" – các tác nhân hay sự kiện có thể gây hại; "), tb("(2) Lỗ hổng (Vulnerability)"), t(" – các điểm yếu trong hệ thống có thể bị khai thác; và "), tb("(3) Tác động (Impact)"), t(" – mức độ thiệt hại nếu đe dọa thành hiện thực qua lỗ hổng. Có hai phương pháp đánh giá chính: "), tb("Phương pháp định tính (Qualitative)"), t(" sử dụng thang đánh giá mô tả (Cao/Trung bình/Thấp); "), tb("Phương pháp định lượng (Quantitative)"), t(" gán giá trị số học cho từng yếu tố. Trong thực tế, "), tb("phương pháp kết hợp (Combined Approach)"), t(" thường được áp dụng để tận dụng ưu điểm của cả hai.")], LINE, { firstLine: 720 }),
  blank(),

  h3("1.3.2. Quy trình đánh giá rủi ro 9 bước theo NIST SP 800-30"),
  p([t("Quy trình đánh giá rủi ro ATTT chuẩn hóa theo NIST SP 800-30 (và tương thích với ISO/IEC 27005) bao gồm "), tb("9 bước"), t(" có tính tuần tự và logic chặt chẽ:")], LINE, { firstLine: 720 }),
  blank(),

  new Paragraph({ spacing: { before: 200, after: 80 }, alignment: AlignmentType.CENTER,
    children: [new TextRun({ text: "Bảng 1.3: Quy trình đánh giá rủi ro ATTT 9 bước", bold: true, size: 22, italics: true, font: "Times New Roman" })] }),
  new Table({
    width: { size: 9360, type: WidthType.DXA },
    columnWidths: [500, 2500, 3560, 2800],
    rows: [
      new TableRow({ children: [hCell("Bước", 500), hCell("Tên bước", 2500), hCell("Nội dung thực hiện", 3560), hCell("Đầu ra (Output)", 2800)] }),
      ...[
        ["1", "Mô tả hệ thống\n(System Characterization)", "Xác định phạm vi, ranh giới, các thành phần phần cứng/phần mềm/dữ liệu/nhân sự/quy trình của hệ thống cần đánh giá", "Hồ sơ đặc tả hệ thống (System Profile)"],
        ["2", "Nhận diện mối đe dọa\n(Threat Identification)", "Lập danh sách toàn diện các mối đe dọa tiềm ẩn, phân loại theo nguồn gốc (bên ngoài, bên trong, môi trường)", "Danh sách đe dọa (Threat Catalog)"],
        ["3", "Nhận diện lỗ hổng\n(Vulnerability Identification)", "Xác định các điểm yếu kỹ thuật và phi kỹ thuật trong hệ thống có thể bị mối đe dọa khai thác", "Danh sách lỗ hổng (Vulnerability List)"],
        ["4", "Phân tích biện pháp kiểm soát\n(Control Analysis)", "Đánh giá các biện pháp kiểm soát bảo mật hiện có (đã triển khai và đang lên kế hoạch)", "Danh sách biện pháp kiểm soát"],
        ["5", "Xác định khả năng xảy ra\n(Likelihood Determination)", "Đánh giá xác suất một mối đe dọa cụ thể thành công khai thác lỗ hổng (thang: Cao/TB/Thấp)", "Điểm khả năng xảy ra"],
        ["6", "Phân tích tác động\n(Impact Analysis)", "Đánh giá mức độ tổn hại đến tổ chức nếu đe dọa thành công (tài chính, danh tiếng, pháp lý)", "Điểm mức độ tác động"],
        ["7", "Xác định mức độ rủi ro\n(Risk Determination)", "Tổng hợp xác suất xảy ra và mức độ tác động để xếp hạng rủi ro trên ma trận", "Ma trận rủi ro (Risk Matrix)"],
        ["8", "Đề xuất biện pháp kiểm soát\n(Control Recommendations)", "Đề xuất các biện pháp kỹ thuật/quy trình để giảm thiểu rủi ro xuống mức chấp nhận được", "Danh sách đề xuất biện pháp"],
        ["9", "Lập tài liệu kết quả\n(Documentation)", "Ghi chép toàn bộ kết quả đánh giá thành báo cáo chuẩn cho lãnh đạo và nhóm kỹ thuật", "Báo cáo đánh giá rủi ro chính thức"],
      ].map((row, i) => new TableRow({ children: [
        cCell(row[0], 500, altShade(i), true),
        bCell(row[1], 2500, altShade(i), true),
        bCell(row[2], 3560, altShade(i)),
        bCell(row[3], 2800, altShade(i)),
      ]}))
    ]
  }),
  blank(),
  p([t("Điểm mấu chốt của quy trình 9 bước là tính "), tb("vòng lặp liên tục"), t(": đánh giá rủi ro không phải là hoạt động một lần mà phải được thực hiện định kỳ (ít nhất mỗi năm một lần) và đặc biệt sau mỗi thay đổi lớn về kiến trúc hệ thống. Trong bối cảnh CRM 1.0 của VietinBank, mỗi lần triển khai một microservice mới hay thêm một điểm tích hợp với hệ thống bên ngoài đều nên kích hoạt một chu kỳ đánh giá rủi ro cập nhật.")], LINE, { firstLine: 720 }),
  blank(),

  h3("1.3.3. Ma trận Rủi ro – Công cụ trực quan hóa và ưu tiên hóa"),
  p([t("Sau khi hoàn thành bước 5 và bước 6, kết quả được ánh xạ lên "), tb("Ma trận Rủi ro (Risk Matrix)"), t(" – một công cụ trực quan hóa 2 chiều kết hợp trục xác suất xảy ra (Likelihood) và trục mức độ tác động (Impact). Ma trận này giúp lãnh đạo tổ chức ra quyết định ưu tiên nguồn lực theo nguyên tắc "), tb("Rủi ro cao nhất – Giải quyết trước tiên"), t(".")], LINE, { firstLine: 720 }),
  blank(),

  new Paragraph({ spacing: { before: 200, after: 80 }, alignment: AlignmentType.CENTER,
    children: [new TextRun({ text: "Bảng 1.4: Ma trận Rủi ro tổng quát 5×5", bold: true, size: 22, italics: true, font: "Times New Roman" })] }),
  new Table({
    width: { size: 9360, type: WidthType.DXA },
    columnWidths: [1760, 1520, 1520, 1520, 1520, 1520],
    rows: [
      new TableRow({ children: [hCell("XS xảy ra \\ Tác động", 1760), hCell("Rất thấp (1)", 1520), hCell("Thấp (2)", 1520), hCell("Trung bình (3)", 1520), hCell("Cao (4)", 1520), hCell("Rất cao (5)", 1520)] }),
      ...[
        ["Rất cao (5)", ["5\nTrung bình","10\nCao","15\nRất cao","20\nRất cao","25\nRất cao"], ["FFFFFF","FFCC99","FF6666","FF0000","CC0000"]],
        ["Cao (4)", ["4\nThấp","8\nTrung bình","12\nCao","16\nRất cao","20\nRất cao"], ["FFFFFF","FFFF99","FFCC99","FF6666","FF0000"]],
        ["Trung bình (3)", ["3\nThấp","6\nTrung bình","9\nTrung bình","12\nCao","15\nRất cao"], ["FFFFFF","FFFFFF","FFFF99","FFCC99","FF6666"]],
        ["Thấp (2)", ["2\nRất thấp","4\nThấp","6\nTrung bình","8\nTrung bình","10\nCao"], ["FFFFFF","FFFFFF","FFFFFF","FFFF99","FFCC99"]],
        ["Rất thấp (1)", ["1\nRất thấp","2\nRất thấp","3\nThấp","4\nThấp","5\nTrung bình"], ["FFFFFF","FFFFFF","FFFFFF","FFFFFF","FFFF99"]],
      ].map((row, i) => new TableRow({ children: [
        bCell(row[0], 1760, "E8EDF5", true),
        ...row[1].map((cell, j) => cCell(cell, 1520, row[2][j]))
      ]}))
    ]
  }),
  blank(),
  p([t("Chú thích: Ô màu đỏ đậm (điểm ≥ 15) là rủi ro cần xử lý ngay lập tức. Ô màu cam (điểm 8–14) là rủi ro cần lên kế hoạch xử lý. Ô màu vàng/trắng (điểm ≤ 7) là rủi ro có thể chấp nhận được hoặc giám sát định kỳ.")], LINE, { firstLine: 720 }),
  blank(),
  new Paragraph({ children: [new PageBreak()] }),

  h2("1.4. Các công nghệ bảo mật lõi"),
  blank(),
  h3("1.4.1. Mật mã học trong Bảo mật thông tin"),
  p([tb("Mật mã học (Cryptography)"), t(" là trụ cột kỹ thuật không thể thiếu trong kiến trúc bảo mật hiện đại, cung cấp nền tảng toán học cho ba dịch vụ bảo mật quan trọng nhất: "), tb("bảo mật thông tin (Confidentiality)"), t(" qua mã hóa; "), tb("xác minh tính toàn vẹn (Integrity)"), t(" qua hàm băm; và "), tb("xác thực nguồn gốc (Authentication)"), t(" qua chữ ký số.")], LINE, { firstLine: 720 }),
  blank(),
  p([tb("a) Mã hóa đối xứng (Symmetric Encryption):"), t(" Trong mã hóa đối xứng, "), tb("cùng một khóa (Secret Key)"), t(" được sử dụng cho cả quá trình mã hóa và giải mã. Thuật toán tiêu chuẩn vàng hiện nay là "), tb("AES (Advanced Encryption Standard)"), t(" với độ dài khóa 256-bit (AES-256), được chính phủ Mỹ thông qua là chuẩn mã hóa quốc gia từ năm 2001 và được NIST xác nhận là an toàn trước các cuộc tấn công lượng tử trong tương lai gần. Chế độ vận hành "), tb("GCM (Galois/Counter Mode)"), t(" kết hợp mã hóa với xác thực tính toàn vẹn (Authenticated Encryption with Associated Data – AEAD), là lựa chọn tối ưu cho môi trường ngân hàng. Ưu điểm của mã hóa đối xứng là "), tb("tốc độ xử lý cực nhanh"), t(" (phù hợp để mã hóa khối lượng dữ liệu lớn như cơ sở dữ liệu), nhưng nhược điểm là vấn đề phân phối khóa an toàn.")], LINE, { firstLine: 720 }),
  blank(),
  p([tb("b) Mã hóa bất đối xứng (Asymmetric Encryption):"), t(" Mã hóa bất đối xứng sử dụng "), tb("cặp khóa (Key Pair)"), t(": "), tb("Khóa công khai (Public Key)"), t(" để mã hóa dữ liệu hoặc xác minh chữ ký; và "), tb("Khóa bí mật (Private Key)"), t(" để giải mã dữ liệu hoặc tạo chữ ký số. Thuật toán phổ biến nhất là "), tb("RSA"), t(" với độ dài khóa tối thiểu 2048-bit (khuyến nghị 4096-bit cho môi trường ngân hàng). Thuật toán "), tb("ECDSA (Elliptic Curve Digital Signature Algorithm)"), t(" ngày càng được ưa chuộng vì cho phép đạt được mức độ bảo mật tương đương RSA-3072 với khóa chỉ 256-bit, tiết kiệm đáng kể tài nguyên tính toán. Trong thực tế, mã hóa bất đối xứng thường được dùng để "), tb("trao đổi khóa đối xứng một cách an toàn"), t(" trong bắt tay TLS, sau đó toàn bộ dữ liệu phiên được mã hóa bằng AES.")], LINE, { firstLine: 720 }),
  blank(),
  p([tb("c) Hàm băm mật mã (Cryptographic Hash Function):"), t(" Hàm băm mật mã (ví dụ: SHA-256, SHA-3) là hàm một chiều biến dữ liệu đầu vào có độ dài tùy ý thành chuỗi băm (Hash/Digest) có độ dài cố định. Ba đặc tính cốt lõi là: "), tb("Kháng tiền ảnh (Preimage Resistance)"), t(" – không thể tính ngược từ hash ra dữ liệu gốc; "), tb("Kháng va chạm (Collision Resistance)"), t(" – cực kỳ khó tìm hai đầu vào khác nhau cho cùng một hash; và "), tb("Hiệu ứng tuyết lở (Avalanche Effect)"), t(" – chỉ một thay đổi nhỏ trong dữ liệu gốc tạo ra hash hoàn toàn khác biệt. Hàm băm là nền tảng cho kiểm tra tính toàn vẹn dữ liệu, lưu trữ mật khẩu, chữ ký số và Audit Log chống giả mạo.")], LINE, { firstLine: 720 }),
  blank(),
  p([tb("d) Giao thức SSL/TLS:"), t(" "), tb("TLS 1.3"), t(" (phiên bản mới nhất, công bố năm 2018) là tiêu chuẩn bắt buộc trong môi trường tài chính, loại bỏ các thuật toán mã hóa yếu (RC4, DES, 3DES) và chỉ hỗ trợ "), tb("Perfect Forward Secrecy (PFS)"), t(" – đảm bảo rằng dù khóa phiên bị rò lộ trong tương lai, các phiên truyền thông đã hoàn thành trong quá khứ vẫn không bị giải mã được.")], LINE, { firstLine: 720 }),
  blank(),

  new Paragraph({ spacing: { before: 200, after: 80 }, alignment: AlignmentType.CENTER,
    children: [new TextRun({ text: "Bảng 1.5: So sánh các thuật toán mật mã lõi áp dụng tại CRM 1.0", bold: true, size: 22, italics: true, font: "Times New Roman" })] }),
  new Table({
    width: { size: 9360, type: WidthType.DXA },
    columnWidths: [1600, 1200, 1600, 2760, 1200 + 1000],
    rows: [
      new TableRow({ children: [hCell("Thuật toán", 1600), hCell("Loại", 1200), hCell("Độ dài khóa", 1600), hCell("Ứng dụng tại CRM 1.0", 2760), hCell("Tốc độ xử lý", 2200)] }),
      ...[
        ["AES-256-GCM", "Đối xứng", "256-bit", "Mã hóa CSDL (Data at Rest), hồ sơ hình ảnh trên S3", "Rất nhanh (~1 GB/s)"],
        ["RSA-4096", "Bất đối xứng", "4096-bit", "Trao đổi khóa TLS, ký số văn bản hồ sơ khách hàng", "Chậm – chỉ dùng cho dữ liệu nhỏ"],
        ["ECDSA-P256", "Bất đối xứng (ECC)", "256-bit", "Chứng chỉ TLS API Gateway, ký token JWT", "Nhanh, hiệu quả trên thiết bị di động"],
        ["SHA-256", "Hàm băm", "Output 256-bit", "Kiểm tra toàn vẹn hồ sơ, lưu mật khẩu (bcrypt+SHA), Audit Log", "Cực nhanh"],
        ["TLS 1.3", "Giao thức", "N/A", "Toàn bộ giao tiếp Browser ↔ API Gateway ↔ Microservices", "Overhead tối thiểu"],
      ].map((row, i) => new TableRow({ children: [
        bCell(row[0], 1600, altShade(i), true),
        cCell(row[1], 1200, altShade(i)),
        cCell(row[2], 1600, altShade(i)),
        bCell(row[3], 2760, altShade(i)),
        bCell(row[4], 2200, altShade(i)),
      ]}))
    ]
  }),
  blank(),

  h3("1.4.2. Kiểm soát truy cập – RBAC và ABAC"),
  p([tb("Kiểm soát truy cập (Access Control)"), t(" là cơ chế xác định "), tb("ai được làm gì với tài nguyên nào"), t(" trong hệ thống thông tin. Đây là một trong những biện pháp bảo mật quan trọng nhất để đảm bảo nguyên tắc "), tb("\"Quyền tối thiểu\" (Principle of Least Privilege – PoLP)"), t(": mỗi chủ thể (người dùng, tiến trình) chỉ được cấp đúng và đủ quyền cần thiết để thực hiện nhiệm vụ hợp pháp của mình, không hơn không kém.")], LINE, { firstLine: 720 }),
  blank(),
  p([tb("a) Mô hình RBAC (Role-Based Access Control):"), t(" RBAC là mô hình phổ biến và phù hợp nhất cho môi trường doanh nghiệp. Thay vì gán quyền trực tiếp cho từng người dùng (gây bùng nổ về số lượng chính sách và khó bảo trì), RBAC gán quyền cho "), tb("Vai trò (Role)"), t(", và người dùng được gán vào các vai trò phù hợp với chức danh công việc. Các thành phần cốt lõi của RBAC bao gồm: "), tb("Người dùng (User)"), t(" – danh tính cụ thể; "), tb("Vai trò (Role)"), t(" – nhóm quyền hạn theo chức năng nghiệp vụ; "), tb("Quyền hạn (Permission)"), t(" – thao tác cụ thể được phép; và "), tb("Phiên làm việc (Session)"), t(" – ánh xạ tạm thời giữa người dùng và vai trò.")], LINE, { firstLine: 720 }),
  blank(),

  new Paragraph({ spacing: { before: 200, after: 80 }, alignment: AlignmentType.CENTER,
    children: [new TextRun({ text: "Bảng 1.6: Ma trận phân quyền RBAC cho hệ thống CRM VietinBank", bold: true, size: 22, italics: true, font: "Times New Roman" })] }),
  new Table({
    width: { size: 9360, type: WidthType.DXA },
    columnWidths: [1500, 1000, 900, 900, 800, 900, 1260, 1100, 1000],
    rows: [
      new TableRow({ children: [
        hCell("Vai trò", 1500), hCell("Xem TT KH", 1000), hCell("Tạo Leads", 900), hCell("Sửa hồ sơ", 900),
        hCell("Xem CIC", 800), hCell("Tải hồ sơ PDF", 900), hCell("Phê duyệt hạn mức", 1260), hCell("Quản trị hệ thống", 1100), hCell("Xem báo cáo", 1000)
      ]}),
      ...[
        ["Giao dịch viên (Teller)", "✅ Chi nhánh mình", "✅", "❌", "❌", "❌", "❌", "❌", "❌"],
        ["Chuyên viên QHKH (RM)", "✅ KH phụ trách", "✅", "✅", "✅", "✅", "❌", "❌", "❌"],
        ["Trưởng phòng KH", "✅ Toàn CN", "✅", "✅", "✅", "✅", "✅", "❌", "✅"],
        ["Giám đốc Chi nhánh", "✅ Toàn CN", "✅", "✅", "✅", "✅", "✅", "❌", "✅"],
        ["Kiểm soát viên (Auditor)", "✅ Chỉ đọc", "❌", "❌", "✅", "✅", "❌", "❌", "✅"],
        ["Quản trị hệ thống (SysAdmin)", "❌", "❌", "❌", "❌", "❌", "❌", "✅", "❌"],
      ].map((row, i) => new TableRow({ children: row.map((cell, j) => {
        const w = [1500, 1000, 900, 900, 800, 900, 1260, 1100, 1000][j];
        const shade = altShade(i);
        const isGreen = cell === "✅" || cell.startsWith("✅");
        const isRed = cell === "❌";
        const cellShade = isGreen ? "E8F5E9" : isRed ? "FFEBEE" : shade;
        return j === 0 ? bCell(cell, w, shade, true) : cCell(cell, w, cellShade);
      })}))
    ]
  }),
  blank(),
  p([t("Lưu ý quan trọng: Nguyên tắc "), tb("\"Phân tách nhiệm vụ (Separation of Duties)\""), t(" được thể hiện qua việc SysAdmin có quyền quản trị hệ thống NHƯNG "), tb("không được truy cập dữ liệu khách hàng"), t(", ngăn chặn nguy cơ người có quyền cao nhất cũng là người có thể lạm dụng dữ liệu – một mối đe dọa nội bộ phổ biến trong môi trường ngân hàng.")], LINE, { firstLine: 720 }),
  blank(),
  p([tb("b) Mô hình ABAC (Attribute-Based Access Control):"), t(" ABAC mở rộng RBAC bằng cách bổ sung thêm "), tb("ngữ cảnh động (Dynamic Context)"), t(" vào quyết định kiểm soát truy cập. Thay vì chỉ dựa trên vai trò tĩnh, ABAC cho phép định nghĩa chính sách phức tạp hơn, ví dụ: \"Chuyên viên QHKH (RM) chỉ được xem thông tin CIC nếu: (1) đang trong giờ làm việc (8:00–17:00); (2) đang đăng nhập từ IP nội bộ của ngân hàng; VÀ (3) khách hàng đó đang được phân công cho họ.\" Đây là mô hình cho phép triển khai "), tb("kiểm soát truy cập theo ngữ cảnh (Context-Aware Access Control)"), t(" và sẽ được đề xuất áp dụng chi tiết trong Chương 3.")], LINE, { firstLine: 720 }),
  blank(),

  h3("1.4.3. Tường lửa và Hệ thống phát hiện/ngăn chặn xâm nhập (IDS/IPS)"),
  p([tb("Tường lửa (Firewall)"), t(" là thiết bị hoặc phần mềm kiểm soát luồng lưu lượng mạng dựa trên một tập hợp các quy tắc (Rules) được định nghĩa trước, hoạt động như một "), tb("trạm kiểm soát biên giới (Border Control)"), t(" giữa các vùng mạng với mức độ tin cậy khác nhau. Ba thế hệ tường lửa chính bao gồm: "), tb("Packet Filtering Firewall"), t(" (lọc theo IP/Port, thế hệ cơ bản nhất); "), tb("Stateful Inspection Firewall"), t(" (theo dõi trạng thái phiên kết nối, tiêu chuẩn tối thiểu cho doanh nghiệp); và "), tb("Next-Generation Firewall (NGFW)"), t(" (kết hợp Deep Packet Inspection, phát hiện malware, lọc URL và Threat Intelligence).")], LINE, { firstLine: 720 }),
  blank(),
  p([tb("Tường lửa ứng dụng web (Web Application Firewall – WAF)"), t(" là một dạng đặc biệt của NGFW, chuyên bảo vệ các ứng dụng web khỏi các cuộc tấn công tầng ứng dụng như SQL Injection, Cross-Site Scripting (XSS), Cross-Site Request Forgery (CSRF) và các kỹ thuật tấn công API phổ biến. WAF là thành phần không thể thiếu trong kiến trúc DMZ của hệ thống ngân hàng trực tuyến.")], LINE, { firstLine: 720 }),
  blank(),
  p([tb("Hệ thống phát hiện xâm nhập (IDS)"), t(" giám sát lưu lượng mạng để phát hiện các hành vi bất thường, sau đó "), tb("cảnh báo (Alert)"), t(" cho quản trị viên. "), tb("Hệ thống ngăn chặn xâm nhập (IPS)"), t(" là bước phát triển tiếp theo: ngoài phát hiện, IPS còn có thể "), tb("tự động ngăn chặn (Block)"), t(" các gói tin hoặc kết nối độc hại theo thời gian thực. IPS được phân loại theo vị trí triển khai: "), tb("NIPS (Network-based)"), t(" đặt tại các điểm then chốt của hạ tầng mạng, và "), tb("HIPS (Host-based)"), t(" cài đặt trực tiếp trên máy chủ/container để phát hiện các hành vi bất thường từ bên trong.")], LINE, { firstLine: 720 }),
  blank(),

  new Paragraph({ spacing: { before: 200, after: 80 }, alignment: AlignmentType.CENTER,
    children: [new TextRun({ text: "Bảng 1.7: So sánh các công nghệ kiểm soát và giám sát an ninh mạng", bold: true, size: 22, italics: true, font: "Times New Roman" })] }),
  new Table({
    width: { size: 9360, type: WidthType.DXA },
    columnWidths: [1600, 1400, 1800, 1960, 2600],
    rows: [
      new TableRow({ children: [hCell("Công nghệ", 1600), hCell("Tầng OSI", 1400), hCell("Khả năng chính", 1800), hCell("Hạn chế", 1960), hCell("Vị trí triển khai phù hợp", 2600)] }),
      ...[
        ["Packet Filter Firewall", "Tầng 3–4", "Lọc IP/Port nhanh", "Không hiểu ngữ cảnh kết nối", "Router biên giới Internet"],
        ["Stateful Firewall", "Tầng 3–4 + trạng thái", "Theo dõi trạng thái phiên kết nối", "Không phân tích nội dung payload", "Ranh giới vùng mạng DMZ"],
        ["WAF", "Tầng 7 (Application)", "Phát hiện SQLi, XSS, CSRF, API Attack", "Chi phí xử lý cao hơn", "Trước lớp API Gateway trong DMZ"],
        ["NGFW", "Tầng 3–7", "DPI, phát hiện malware, lọc URL", "Chi phí đầu tư cao", "Điểm tập trung luồng lưu lượng chính"],
        ["NIDS/NIPS", "Tầng 3–7", "Phát hiện mẫu tấn công, anomaly detection", "False positive cần tinh chỉnh", "Trong vùng nội bộ, tại switch lõi"],
        ["HIDS/HIPS", "Tầng ứng dụng (trên host)", "Phát hiện hành vi bất thường trên container", "Tốn tài nguyên tính toán", "Trực tiếp trên Worker Nodes OpenShift"],
      ].map((row, i) => new TableRow({ children: [
        bCell(row[0], 1600, altShade(i), true),
        cCell(row[1], 1400, altShade(i)),
        bCell(row[2], 1800, altShade(i)),
        bCell(row[3], 1960, altShade(i)),
        bCell(row[4], 2600, altShade(i)),
      ]}))
    ]
  }),
  blank(),

  // SUMMARY
  new Paragraph({ spacing: { before: 300, after: 120 },
    children: [new TextRun({ text: "Tóm tắt Chương 1", bold: true, size: 28, font: "Times New Roman", color: "1F3864" })] }),
  p([t("Chương 1 đã xây dựng một nền tảng lý thuyết vững chắc và toàn diện làm cơ sở cho toàn bộ nghiên cứu. Qua bốn phần chính, bài viết đã làm rõ bản chất và tầm quan trọng của An toàn thông tin thông qua mô hình CIA Triad với mối quan hệ đánh đổi tinh tế giữa ba thuộc tính; hệ thống hóa mô hình Phòng vệ chiều sâu (Defense in Depth) với ba lớp bảo vệ chính và bảy vùng hạ tầng CNTT như một framework phân tích rủi ro có cấu trúc; trình bày quy trình đánh giá rủi ro 9 bước theo NIST SP 800-30 kết hợp Ma trận Rủi ro 5×5 làm công cụ ưu tiên hóa; và giới thiệu các công nghệ bảo mật lõi bao gồm mật mã học (AES-256-GCM, RSA-4096, SHA-256, TLS 1.3), kiểm soát truy cập (RBAC kết hợp ABAC), Firewall thế hệ mới và IDS/IPS như những \"hòn gạch xây dựng\" cho kiến trúc bảo mật đề xuất ở Chương 3.")], LINE, { firstLine: 720 }),
  blank(),
  p([t("Với nền tảng lý thuyết này, Chương 2 sẽ chuyển từ lý luận tổng quát sang phân tích cụ thể, ánh xạ các lý thuyết đã học vào thực tiễn kiến trúc của hệ thống CRM 1.0 tại VietinBank để nhận diện các rủi ro thực sự và đặc thù mà hệ thống đang đối mặt.")], LINE, { firstLine: 720 }),
  blank()
);

// ─── BUILD DOC ───
const doc = new Document({
  styles: {
    default: {
      document: { run: { font: "Times New Roman", size: 26 } }
    },
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
    headers: {
      default: new Header({ children: [
        new Paragraph({
          border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: "1F3864", space: 4 } },
          alignment: AlignmentType.RIGHT,
          children: [new TextRun({ text: "Bài tập lớn: Bảo mật CRM 1.0 – VietinBank", size: 18, font: "Times New Roman", color: "555555", italics: true })]
        })
      ]})
    },
    footers: {
      default: new Footer({ children: [
        new Paragraph({
          border: { top: { style: BorderStyle.SINGLE, size: 6, color: "1F3864", space: 4 } },
          alignment: AlignmentType.CENTER,
          children: [new TextRun({ text: "- ", size: 20, font: "Times New Roman" }),
                     new TextRun({ children: [PageNumber.CURRENT], size: 20, font: "Times New Roman" }),
                     new TextRun({ text: " -", size: 20, font: "Times New Roman" })]
        })
      ]})
    },
    children
  }]
});

Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync('/sessions/funny-affectionate-sagan/mnt/outputs/ATTT_CRM_VietinBank_Chuong1.docx', buf);
  console.log('Done: ATTT_CRM_VietinBank_Chuong1.docx');
});
