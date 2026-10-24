// Build báo cáo bài tập lớn - HTTT Quản lý nâng cao
// Output: BaiTapLon_HTTTQL_VNPT.docx

const fs = require('fs');
const path = require('path');
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, ImageRun,
  Header, Footer, AlignmentType, PageOrientation, LevelFormat, ExternalHyperlink,
  TableOfContents, HeadingLevel, BorderStyle, WidthType, ShadingType,
  VerticalAlign, PageNumber, PageBreak, TabStopType, TabStopPosition
} = require('docx');

const ASSETS = path.join(__dirname, 'assets');

// ============== HELPERS ==============
const FONT = "Times New Roman";

function P(text, opts = {}) {
  const { bold = false, italic = false, size = 26, align = AlignmentType.JUSTIFIED, spacing = { line: 360, after: 120 }, indent = { firstLine: 720 } } = opts;
  return new Paragraph({
    alignment: align,
    spacing: spacing,
    indent: opts.indent === false ? undefined : indent,
    children: [new TextRun({ text, bold, italics: italic, size, font: FONT })]
  });
}

function H1(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_1,
    alignment: AlignmentType.LEFT,
    spacing: { before: 360, after: 200 },
    children: [new TextRun({ text, bold: true, size: 32, font: FONT, color: "1F4E79" })]
  });
}

function H2(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_2,
    alignment: AlignmentType.LEFT,
    spacing: { before: 240, after: 160 },
    children: [new TextRun({ text, bold: true, size: 28, font: FONT, color: "2E75B6" })]
  });
}

function H3(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_3,
    alignment: AlignmentType.LEFT,
    spacing: { before: 200, after: 120 },
    children: [new TextRun({ text, bold: true, italics: true, size: 26, font: FONT, color: "404040" })]
  });
}

function CENTER(text, opts = {}) {
  const { bold = false, size = 26, color = "000000", italic = false } = opts;
  return new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { line: 360, after: 80, ...(opts.spacing || {}) },
    children: [new TextRun({ text, bold, italics: italic, size, font: FONT, color })]
  });
}

function BULLET(text) {
  return new Paragraph({
    numbering: { reference: "bullets", level: 0 },
    alignment: AlignmentType.JUSTIFIED,
    spacing: { line: 320, after: 80 },
    children: [new TextRun({ text, size: 26, font: FONT })]
  });
}

function BULLET_MIX(parts) {
  return new Paragraph({
    numbering: { reference: "bullets", level: 0 },
    alignment: AlignmentType.JUSTIFIED,
    spacing: { line: 320, after: 80 },
    children: parts.map(p => new TextRun({ text: p.text, size: 26, font: FONT, bold: !!p.bold, italics: !!p.italic }))
  });
}

function IMG(file, w, h, caption) {
  const data = fs.readFileSync(path.join(ASSETS, file));
  return [
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { before: 240, after: 80 },
      children: [new ImageRun({
        type: "png",
        data,
        transformation: { width: w, height: h },
        altText: { title: caption, description: caption, name: file }
      })]
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { after: 240 },
      children: [new TextRun({ text: caption, italics: true, size: 22, font: FONT, color: "595959" })]
    })
  ];
}

// ============== TABLE HELPERS ==============
const tableBorder = { style: BorderStyle.SINGLE, size: 6, color: "808080" };
const cellBorders = { top: tableBorder, bottom: tableBorder, left: tableBorder, right: tableBorder };

function TCell(text, opts = {}) {
  const { bold = false, fill = null, width = 1800, align = AlignmentType.LEFT, size = 22 } = opts;
  const cellOpts = {
    borders: cellBorders,
    width: { size: width, type: WidthType.DXA },
    margins: { top: 80, bottom: 80, left: 100, right: 100 },
    verticalAlign: VerticalAlign.CENTER,
    children: [new Paragraph({
      alignment: align,
      spacing: { line: 280 },
      children: [new TextRun({ text, bold, size, font: FONT })]
    })]
  };
  if (fill) cellOpts.shading = { fill, type: ShadingType.CLEAR };
  return new TableCell(cellOpts);
}

// ============== CONTENT ==============

const coverPage = [
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 60 }, children: [new TextRun({ text: "HỌC VIỆN NGÂN HÀNG", bold: true, size: 28, font: FONT })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 60 }, children: [new TextRun({ text: "KHOA CÔNG NGHỆ THÔNG TIN & KINH TẾ SỐ", bold: true, size: 26, font: FONT })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 600 }, children: [new TextRun({ text: "------------- o0o -------------", size: 26, font: FONT })] }),

  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 240 }, children: [new TextRun({ text: "BÀI TẬP LỚN KẾT THÚC HỌC PHẦN", bold: true, size: 36, font: FONT, color: "1F4E79" })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 120 }, children: [new TextRun({ text: "Môn học: HỆ THỐNG THÔNG TIN QUẢN LÝ NÂNG CAO", bold: true, size: 28, font: FONT })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 600 }, children: [new TextRun({ text: "(Chương trình Thạc sĩ ngành Hệ thống thông tin quản lý)", italics: true, size: 24, font: FONT })] }),

  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 240 }, children: [new TextRun({ text: "ĐỀ TÀI", bold: true, size: 28, font: FONT })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 120 }, children: [new TextRun({ text: "KIẾN TRÚC HỆ THỐNG THÔNG TIN VÀ ĐỀ XUẤT ỨNG DỤNG", bold: true, size: 30, font: FONT, color: "C00000" })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 120 }, children: [new TextRun({ text: "GENERATIVE AI ĐỂ CẢI TIẾN QUY TRÌNH CUNG CẤP", bold: true, size: 30, font: FONT, color: "C00000" })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 600 }, children: [new TextRun({ text: "DỊCH VỤ FTTH TẠI TẬP ĐOÀN VNPT", bold: true, size: 30, font: FONT, color: "C00000" })] }),

  new Paragraph({ alignment: AlignmentType.LEFT, spacing: { after: 120 }, indent: { left: 2880 }, children: [new TextRun({ text: "Học viên thực hiện: ", bold: true, size: 26, font: FONT }), new TextRun({ text: "Nguyễn Minh Hiếu", size: 26, font: FONT })] }),
  new Paragraph({ alignment: AlignmentType.LEFT, spacing: { after: 120 }, indent: { left: 2880 }, children: [new TextRun({ text: "Lớp: ", bold: true, size: 26, font: FONT }), new TextRun({ text: "Cao học HTTTQL - K27", size: 26, font: FONT })] }),
  new Paragraph({ alignment: AlignmentType.LEFT, spacing: { after: 120 }, indent: { left: 2880 }, children: [new TextRun({ text: "Đơn vị công tác: ", bold: true, size: 26, font: FONT }), new TextRun({ text: "VNPT AI Hà Nội", size: 26, font: FONT })] }),
  new Paragraph({ alignment: AlignmentType.LEFT, spacing: { after: 600 }, indent: { left: 2880 }, children: [new TextRun({ text: "Năm học: ", bold: true, size: 26, font: FONT }), new TextRun({ text: "2025 - 2026", size: 26, font: FONT })] }),

  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 60 }, children: [new TextRun({ text: "HÀ NỘI, THÁNG 5 NĂM 2026", bold: true, size: 26, font: FONT })] }),
  new Paragraph({ children: [new PageBreak()] }),
];

// ============== INTRODUCTION ==============
const intro = [
  H1("LỜI MỞ ĐẦU"),
  P("Báo cáo này được thực hiện trong khuôn khổ học phần Hệ thống thông tin quản lý nâng cao. Xuất phát điểm của báo cáo gắn với thực tiễn công tác phân tích nghiệp vụ (Business Analyst) tại VNPT AI Hà Nội - nơi nhiều yêu cầu thoạt nghe rất nhỏ, kiểu \"thêm một trường nhập liệu vào màn hình đăng ký dịch vụ\", nhưng khi phân tích sâu lại kéo theo CRM, BSS, hệ thống tính cước và cả quy trình đối soát. Thực tế từng có trường hợp mất gần hai tuần chỉ để truy ngược một thông tin thuê bao bị lệch giữa hai hệ thống. Chính những tình huống như vậy cho thấy giá trị của cách tiếp cận tổng thể mà học phần này hướng tới, thay vì chỉ nhìn từng phần mềm riêng lẻ."),
  P("Đối tượng nghiên cứu được chọn là Tập đoàn Bưu chính Viễn thông Việt Nam (VNPT), một phần nhờ thuận lợi trong việc tiếp cận thông tin, một phần vì VNPT có hệ thống thông tin tương đối lớn và đang trong giai đoạn chuyển dịch sang doanh nghiệp công nghệ số. Quy trình được chọn để phân tích sâu là quy trình cung cấp dịch vụ Internet cáp quang FTTH cho khách hàng cá nhân, vì đây là một trong số ít quy trình đi qua gần như tất cả các hệ thống thông tin chính của Tập đoàn."),
  P("Bài làm gồm 5 phần tương ứng 5 câu hỏi của đề, trình bày đi từ tổng thể đến chi tiết: bức tranh chung về VNPT, kiến trúc hệ thống thông tin theo khung TOGAF, một quy trình cụ thể, đánh giá hiện trạng và cuối cùng là một đề xuất cải tiến bằng Generative AI - hướng công nghệ mà VNPT đang đầu tư qua các sản phẩm như VNPT SmartBot, VNPT AMI."),
  P("Cũng cần nói trước về giới hạn của báo cáo: nhiều dữ liệu vận hành nội bộ của Tập đoàn không thể công bố, nên nội dung chủ yếu dựa trên ba nguồn - tài liệu công khai (báo cáo, website, báo chí chính thống), quan sát thực tế trong quá trình công tác, và một số giả định phân tích được ghi rõ ở từng chỗ. Các con số ước lượng trong phần đề xuất, vì vậy, nên được hiểu là mục tiêu để theo dõi chứ chưa phải kết quả đã kiểm chứng."),
  new Paragraph({ children: [new PageBreak()] }),
];

// ============== CÂU 1 ==============
const cau1 = [
  H1("CÂU 1. GIỚI THIỆU VỀ TẬP ĐOÀN VNPT"),
  H2("1.1. Giới thiệu chung và lịch sử ra đời"),
  P("Tập đoàn Bưu chính Viễn thông Việt Nam (VNPT - Vietnam Posts and Telecommunications Group) là doanh nghiệp nhà nước có vai trò lớn trong hạ tầng viễn thông và dịch vụ số tại Việt Nam, đặc biệt ở mảng cố định, băng rộng, trung tâm dữ liệu và các giải pháp số cho khối cơ quan nhà nước, doanh nghiệp."),
  P("VNPT được thành lập theo Quyết định số 06/2006/QĐ-TTg ngày 09/01/2006 của Thủ tướng Chính phủ, trên cơ sở tổ chức lại Tổng công ty Bưu chính Viễn thông Việt Nam (có lịch sử gắn với ngành Bưu điện từ năm 1945). Trụ sở chính đặt tại Tòa nhà VNPT, số 57 Huỳnh Thúc Kháng, Đống Đa, Hà Nội. Thông tin dịch vụ được công bố trên website vnpt.com.vn, vnpt.vn và tổng đài chăm sóc khách hàng 18001166."),
  P("Theo Quyết định 1019/QĐ-TTg ngày 23/9/2024 của Thủ tướng Chính phủ phê duyệt Chiến lược phát triển VNPT đến năm 2030, tầm nhìn 2035, Tập đoàn được định hướng chuyển đổi thành công từ doanh nghiệp viễn thông truyền thống sang doanh nghiệp công nghệ số, làm chủ một số nền tảng quan trọng để dẫn dắt chuyển đổi số quốc gia. Đây là một định hướng có tính lịch sử, đặt nền cho việc tổ chức lại bộ máy và đầu tư công nghệ những năm gần đây."),

  H2("1.2. Sản phẩm và dịch vụ chính"),
  P("Là một tập đoàn viễn thông - công nghệ tổng hợp, danh mục sản phẩm dịch vụ của VNPT khá rộng, có thể nhóm thành bốn cụm chính cho dễ hình dung:"),
  BULLET_MIX([{ text: "Dịch vụ viễn thông cho khách hàng cá nhân (B2C): ", bold: true }, { text: "thuê bao di động VinaPhone (đã phủ sóng 5G trên 63 tỉnh thành kể từ năm 2024), Internet cáp quang FTTH (thương hiệu FiberVNN, gói Home cho hộ gia đình), truyền hình MyTV và VNPT Smart Home." }]),
  BULLET_MIX([{ text: "Dịch vụ cho doanh nghiệp (B2B): ", bold: true }, { text: "đường truyền MetroNet, MegaWAN, dịch vụ kết nối liên tỉnh - quốc tế, dịch vụ trung tâm dữ liệu VNPT IDC, dịch vụ điện toán đám mây VNPT Smart Cloud, các giải pháp an toàn thông tin của VNPT-Cyber Immunity." }]),
  BULLET_MIX([{ text: "Dịch vụ số và nền tảng công nghệ: ", bold: true }, { text: "trợ lý ảo VNPT SmartBot và AMI, nền tảng AI vnptai.io, giải pháp eKYC, hệ sinh thái thanh toán VNPT Money/VNPT Pay, hệ thống VNPT iOffice cho khối hành chính." }]),
  BULLET_MIX([{ text: "Dịch vụ phục vụ Chính phủ điện tử: ", bold: true }, { text: "VNPT là đơn vị triển khai hạ tầng cho nhiều dự án quan trọng như Trục liên thông văn bản quốc gia, Cổng dịch vụ công, Cơ sở dữ liệu quốc gia về dân cư, hệ thống định danh điện tử quốc gia." }]),

  H2("1.3. Bối cảnh thị trường và tình hình sản xuất kinh doanh"),
  P("Thị trường viễn thông Việt Nam hiện do ba \"ông lớn\" thống trị: Viettel, VNPT và MobiFone. Sau giai đoạn tăng trưởng nóng của di động, từ năm 2020 trở lại đây thị trường viễn thông truyền thống dần bão hòa, ARPU di động giảm và áp lực cạnh tranh ngày càng gắt gao. Trong khi đó, các dịch vụ số (Cloud, AI, eKYC, thanh toán số…) lại đang là khoảng trống lớn để khai phá. Năm 2024 còn có thêm một số yếu tố làm khó nhà mạng như: quy định dừng phát triển SIM mới qua đại lý, chi tiêu công cho chuyển đổi số chậm lại, và làn sóng OTT thay thế dịch vụ viễn thông truyền thống."),
  P("Trong bối cảnh đó, VNPT vẫn duy trì được tăng trưởng. Theo công bố tại Hội nghị tổng kết năm 2024, tổng doanh thu toàn Tập đoàn ước đạt 58.540 tỷ đồng, hoàn thành kế hoạch và tăng khoảng 7% so với năm trước. Lợi nhuận trước thuế hợp nhất đạt 6.086 tỷ đồng, riêng Công ty mẹ là 4.565 tỷ đồng (đạt 103,3% kế hoạch). Một con số rất đáng chú ý là tỷ suất lợi nhuận trên vốn chủ sở hữu của Công ty mẹ tăng 29,5% so với kế hoạch - cho thấy hiệu quả sử dụng vốn đã được cải thiện rõ rệt."),
  P("Cũng trong năm 2024, VNPT đưa mạng 5G VinaPhone thương mại hóa rộng rãi, đồng thời mở rộng hệ sinh thái Smart Home (camera AI, Smart WiFi, MyTV…). Bước sang 2025, Chính phủ ban hành Nghị quyết 186/NQ-CP ngày 25/6/2025 phê duyệt chủ trương sáp nhập VNPT-VinaPhone và VNPT-Media vào Công ty mẹ Tập đoàn, theo mô hình \"Lõi hợp nhất\" - đây là một thay đổi tổ chức rất lớn nhằm tinh gọn bộ máy và rút ngắn ra quyết định."),

  H2("1.4. Cơ cấu tổ chức"),
  P("Sau giai đoạn tái cơ cấu 2014 - 2015, mô hình VNPT được chia thành \"3 lớp\": (i) hạ tầng mạng - do VNPT-Net đảm trách, (ii) kinh doanh dịch vụ - do VNPT-VinaPhone đảm trách, (iii) giá trị gia tăng và nội dung số - do VNPT-Media đảm trách. Bên cạnh đó còn có VNPT-IT (thành lập 2018) chuyên phát triển phần mềm và VNPT-Technology chuyên về thiết bị, phần cứng. Mạng lưới hiện diện trên cả nước thông qua 63 chi nhánh tỉnh/thành (gọi là VNPT các tỉnh)."),
  P("Từ tháng 6/2025, theo chủ trương mới, VNPT-VinaPhone và VNPT-Media được sáp nhập trở lại vào Công ty mẹ; mô hình mới sẽ tổ chức theo trục dọc nghiệp vụ (mobile, broadband, digital service, B2B…) thay vì trục công ty con. Mục tiêu là đến hết năm 2025 tổng doanh thu toàn Tập đoàn đạt trên 287 nghìn tỷ đồng cho cả giai đoạn 2021 - 2025 và VNPT trở thành tập đoàn công nghệ chứ không còn thuần túy là nhà mạng nữa."),

  H2("1.5. Chiến lược cạnh tranh và chuỗi giá trị"),
  P("Theo khung phân tích của M. Porter, ba chiến lược cạnh tranh phổ biến gồm dẫn đầu chi phí, khác biệt hóa và tập trung. Cần lưu ý đây là nhận định mang tính phân tích chứ không phải tuyên bố chính thức của Tập đoàn. Qua quan sát các gói Home Combo, MyTV, Smart Home và các giải pháp số cho khối cơ quan nhà nước, cùng việc đối chiếu với Chiến lược phát triển VNPT đến 2030, có thể nhận định VNPT có xu hướng kết hợp giữa khác biệt hóa dịch vụ và khai thác nhóm khách hàng có nhu cầu ổn định, thay vì cạnh tranh chủ yếu bằng giá thấp. Ba điểm VNPT thường nhấn mạnh là: chất lượng hạ tầng mạng (cáp quang biển, trục IP-MPLS, hệ thống IDC), hệ sinh thái dịch vụ số gắn với chính phủ điện tử và doanh nghiệp, và định hướng \"Make in Vietnam\" với một số sản phẩm AI - Big Data tự phát triển. Để khẳng định chắc chắn về định vị giá, sẽ cần thêm dữ liệu so sánh ARPU và bảng giá giữa các nhà mạng - phần này nằm ngoài phạm vi báo cáo."),
  P("Để thực thi được chiến lược đó, chuỗi giá trị của VNPT (theo mô hình Porter) có thể nhìn thành các hoạt động chính và hỗ trợ sau. Bảng dưới đây tổng hợp lại cho dễ tra cứu:"),

  new Table({
    width: { size: 9360, type: WidthType.DXA },
    columnWidths: [2200, 7160],
    rows: [
      new TableRow({ tableHeader: true, children: [
        TCell("Hoạt động trong chuỗi giá trị", { bold: true, fill: "1F4E79", width: 2200, size: 22 }),
        TCell("Vai trò trong việc thực thi chiến lược cạnh tranh của VNPT", { bold: true, fill: "1F4E79", width: 7160, size: 22 })
      ]}),
      new TableRow({ children: [
        TCell("Hậu cần đầu vào", { bold: true, width: 2200 }),
        TCell("Mua sắm thiết bị mạng (Huawei, Nokia, ZTE…), thuê dung lượng quốc tế, hợp tác với các đối tác hạ tầng. VNPT-Technology còn tự sản xuất một phần thiết bị đầu cuối (modem GPON, set-top-box MyTV) để chủ động và giảm phụ thuộc nhập khẩu.", { width: 7160 })
      ]}),
      new TableRow({ children: [
        TCell("Vận hành", { bold: true, fill: "F2F2F2", width: 2200 }),
        TCell("Vận hành mạng truy nhập di động VinaPhone 4G/5G, mạng cáp quang FTTH, mạng truyền dẫn IP-MPLS, các trung tâm dữ liệu VNPT IDC. Đây là khâu trực tiếp tạo ra dịch vụ và ảnh hưởng lớn đến trải nghiệm khách hàng.", { width: 7160, fill: "F2F2F2" })
      ]}),
      new TableRow({ children: [
        TCell("Hậu cần đầu ra", { bold: true, width: 2200 }),
        TCell("Phân phối dịch vụ thông qua 63 chi nhánh VNPT tỉnh, hệ thống điểm giao dịch, đại lý, kênh online (website, My VNPT app), tổng đài 18001166 và các đội kỹ thuật triển khai tại nhà khách hàng.", { width: 7160 })
      ]}),
      new TableRow({ children: [
        TCell("Marketing & bán hàng", { bold: true, fill: "F2F2F2", width: 2200 }),
        TCell("Truyền thông thương hiệu VinaPhone, FiberVNN, MyTV; chương trình khuyến mại, combo dịch vụ Home Combo; bán hàng B2B cho khối doanh nghiệp và chính phủ.", { width: 7160, fill: "F2F2F2" })
      ]}),
      new TableRow({ children: [
        TCell("Dịch vụ sau bán", { bold: true, width: 2200 }),
        TCell("Tổng đài 18001166, chatbot SmartBot, đội kỹ thuật xử lý sự cố tại địa bàn, ứng dụng My VNPT cho tra cứu và thanh toán.", { width: 7160 })
      ]}),
      new TableRow({ children: [
        TCell("Hoạt động hỗ trợ", { bold: true, fill: "FFF2CC", width: 2200 }),
        TCell("Hạ tầng quản trị (tài chính, kế toán, ERP), quản trị nhân lực (HRM), nghiên cứu phát triển (VNPT-IT, VNPT AI, VNPT Technology), mua sắm tập trung và an toàn thông tin (VNPT-Cyber Immunity).", { width: 7160, fill: "FFF2CC" })
      ]})
    ]
  }),
  P("Một điểm đáng nhấn mạnh là trong chuỗi giá trị này, hệ thống thông tin đóng vai trò kết nối các hoạt động lại với nhau. Một CRM rời rạc sẽ ảnh hưởng đến khâu chăm sóc khách hàng; một OSS chậm sẽ kéo dài việc cung cấp dịch vụ; còn hệ thống BI thiếu dữ liệu sẽ khiến việc ra quyết định khó chính xác. Đây cũng là lý do cần nhìn lại kiến trúc hệ thống thông tin ở Câu 2 trước khi đi vào quy trình cụ thể."),

  new Paragraph({ children: [new PageBreak()] }),
];

// ============== CÂU 2 ==============
const cau2 = [
  H1("CÂU 2. KIẾN TRÚC HỆ THỐNG THÔNG TIN CỦA VNPT THEO KHUNG TOGAF"),
  H2("2.1. Lý do chọn khung TOGAF"),
  P("Có vài khung kiến trúc doanh nghiệp phổ biến: Zachman, TOGAF, FEAF, Gartner. Zachman không được chọn vì khung này thiên về việc phân loại các \"hiện vật\" kiến trúc theo ma trận, phù hợp khi muốn kiểm kê tài liệu hơn là khi muốn đi từ kiến trúc tổng thể xuống một quy trình cụ thể. Cách tiếp cận của Gartner cũng được cân nhắc nhưng nghiêng về tư vấn và ít chuẩn hóa tài liệu công khai. TOGAF (The Open Group Architecture Framework) phù hợp với báo cáo này hơn, vì bốn tầng của nó cho phép nối quy trình FTTH với các ứng dụng, dữ liệu và hạ tầng công nghệ phía dưới - đúng mạch lập luận từ Câu 2 sang Câu 3, Câu 4."),
  P("Bốn tầng đó gồm: tầng nghiệp vụ (Business Architecture), tầng ứng dụng (Application Architecture), tầng dữ liệu (Data Architecture) và tầng công nghệ (Technology Architecture). Cách chia này khá hợp với một tập đoàn viễn thông như VNPT, nơi người làm nghiệp vụ, người làm phần mềm, người quản trị dữ liệu và đội vận hành hạ tầng mạng thường là các nhóm khác nhau. Đặt bốn tầng cạnh nhau giúp thấy rõ vì sao một thay đổi ở tầng này thường kéo theo thay đổi ở tầng khác."),

  H2("2.2. Sơ đồ kiến trúc tổng thể"),
  P("Các hệ thống thông tin chính của VNPT được tổng hợp thành sơ đồ kiến trúc 4 tầng sau:"),
  ...IMG("togaf.png", 620, 442, "Hình 2.1. Kiến trúc doanh nghiệp VNPT theo khung TOGAF - 4 tầng kiến trúc"),

  H2("2.3. Mô tả chi tiết từng tầng kiến trúc"),
  H3("2.3.1. Tầng nghiệp vụ (Business Layer)"),
  P("Tầng này mô tả các nhóm hoạt động nghiệp vụ - thuật ngữ phân tích nghiệp vụ thường gọi là \"value streams\" hoặc \"business capabilities\". Với VNPT, có thể nhận diện sáu nhóm nghiệp vụ lõi:"),
  BULLET("Bán hàng & chăm sóc khách hàng: tư vấn gói cước, tiếp nhận yêu cầu lắp đặt mới/nâng cấp, xử lý khiếu nại và CSKH định kỳ."),
  BULLET("Cung cấp dịch vụ (Service Provisioning): khảo sát hạ tầng, lắp đặt, kích hoạt dịch vụ tại nhà khách hàng - đây là khâu được phân tích kỹ ở Câu 3."),
  BULLET("Vận hành mạng lưới: giám sát chất lượng mạng 24/7, phát hiện và xử lý sự cố, bảo dưỡng định kỳ - vốn là phần \"khó nhìn\" nhưng quyết định trải nghiệm khách hàng."),
  BULLET("Tính cước và thu cước: ghi nhận CDR, áp giá, phát hành hóa đơn, thu nợ - liên quan trực tiếp tới dòng tiền của Tập đoàn."),
  BULLET("Tài chính - kế toán: sổ cái, quản lý doanh thu - chi phí, lập báo cáo tài chính theo chuẩn VAS/IFRS, quản lý tài sản và đầu tư."),
  BULLET("Quản trị nhân sự và hành chính: tuyển dụng, đào tạo, KPI, quản lý văn bản nội bộ, điều hành hành chính."),

  H3("2.3.2. Tầng ứng dụng (Application Layer)"),
  P("Tầng ứng dụng là tập hợp các phần mềm/HTTT được triển khai để hiện thực hóa các hoạt động nghiệp vụ ở trên. Một lưu ý về phương pháp: bảng dưới đây mô tả ở mức nhóm hệ thống, không phản ánh nguyên văn tên gọi hay chi tiết kiến trúc nội bộ của Tập đoàn (vốn không thể công bố). Một số tên được chuẩn hóa theo thuật ngữ phổ biến trong ngành viễn thông như CRM, BSS, OSS để người đọc dễ đối chiếu. Ở mức nhóm, có thể nhận diện khoảng 12 hệ thống lõi:"),

  new Table({
    width: { size: 9360, type: WidthType.DXA },
    columnWidths: [1300, 2200, 5860],
    rows: [
      new TableRow({ tableHeader: true, children: [
        TCell("Nhóm", { bold: true, fill: "70AD47", width: 1300, size: 22, align: AlignmentType.CENTER }),
        TCell("Tên hệ thống", { bold: true, fill: "70AD47", width: 2200, size: 22 }),
        TCell("Chức năng chính", { bold: true, fill: "70AD47", width: 5860, size: 22 })
      ]}),
      new TableRow({ children: [
        TCell("Khách hàng", { bold: true, width: 1300 }),
        TCell("CRM (Customer Relationship Mgmt)", { bold: true, width: 2200 }),
        TCell("Quản lý hồ sơ khách hàng (cá nhân, doanh nghiệp), lead, cơ hội bán hàng, ticket chăm sóc, lịch sử tương tác đa kênh.", { width: 5860 })
      ]}),
      new TableRow({ children: [
        TCell("Khách hàng", { bold: true, fill: "F2F2F2", width: 1300 }),
        TCell("My VNPT App / Portal khách hàng", { bold: true, fill: "F2F2F2", width: 2200 }),
        TCell("Kênh giao dịch số tự phục vụ (self-service): tra cứu cước, đăng ký gói mới, báo hỏng, thanh toán.", { width: 5860, fill: "F2F2F2" })
      ]}),
      new TableRow({ children: [
        TCell("Bán hàng", { bold: true, width: 1300 }),
        TCell("BSS (Business Support Systems)", { bold: true, width: 2200 }),
        TCell("Order Management (quản lý đơn hàng), Product Catalog (catalog sản phẩm - gói cước), Pricing & Rating, Billing - phát hành hóa đơn và quản lý cước.", { width: 5860 })
      ]}),
      new TableRow({ children: [
        TCell("Mạng lưới", { bold: true, fill: "F2F2F2", width: 1300 }),
        TCell("OSS - Service Fulfillment", { bold: true, fill: "F2F2F2", width: 2200 }),
        TCell("Tự động hóa việc cung cấp dịch vụ: nhận work order từ BSS, gọi xuống thiết bị (OLT, BRAS, IMS…) để cấu hình, kích hoạt thuê bao.", { width: 5860, fill: "F2F2F2" })
      ]}),
      new TableRow({ children: [
        TCell("Mạng lưới", { bold: true, width: 1300 }),
        TCell("OSS - NMS / Service Assurance", { bold: true, width: 2200 }),
        TCell("Network Management System: giám sát thiết bị, cảnh báo sự cố, đo chất lượng dịch vụ (KPI), điều phối xử lý lỗi.", { width: 5860 })
      ]}),
      new TableRow({ children: [
        TCell("Mạng lưới", { bold: true, fill: "F2F2F2", width: 1300 }),
        TCell("Network Inventory", { bold: true, fill: "F2F2F2", width: 2200 }),
        TCell("Quản lý tài nguyên mạng vật lý và logic: OLT - ODF - splitter - port, dải IP, VLAN, vùng phục vụ, bản đồ cáp GIS.", { width: 5860, fill: "F2F2F2" })
      ]}),
      new TableRow({ children: [
        TCell("Quản trị", { bold: true, width: 1300 }),
        TCell("ERP (Oracle / SAP)", { bold: true, width: 2200 }),
        TCell("Tài chính - kế toán, mua sắm, quản lý tài sản cố định, quản lý dự án đầu tư.", { width: 5860 })
      ]}),
      new TableRow({ children: [
        TCell("Quản trị", { bold: true, fill: "F2F2F2", width: 1300 }),
        TCell("HRM", { bold: true, fill: "F2F2F2", width: 2200 }),
        TCell("Quản lý nhân sự, chấm công, tính lương, KPI, đào tạo, lộ trình thăng tiến.", { width: 5860, fill: "F2F2F2" })
      ]}),
      new TableRow({ children: [
        TCell("Quản trị", { bold: true, width: 1300 }),
        TCell("VNPT iOffice (EDMS)", { bold: true, width: 2200 }),
        TCell("Hệ thống quản lý văn bản và điều hành nội bộ; đã tích hợp AI/Chatbot để hỗ trợ tra cứu, soạn thảo công văn.", { width: 5860 })
      ]}),
      new TableRow({ children: [
        TCell("Phân tích", { bold: true, fill: "F2F2F2", width: 1300 }),
        TCell("DWH & BI", { bold: true, fill: "F2F2F2", width: 2200 }),
        TCell("Data Warehouse hợp nhất dữ liệu các hệ thống nguồn (CRM, BSS, OSS), Business Intelligence cho lãnh đạo và phân tích kinh doanh.", { width: 5860, fill: "F2F2F2" })
      ]}),
      new TableRow({ children: [
        TCell("AI", { bold: true, width: 1300 }),
        TCell("VNPT SmartBot / AMI", { bold: true, width: 2200 }),
        TCell("Nền tảng chatbot - voicebot - callbot dựa trên NLP, OCR và Generative AI; CSKH tự động đa kênh (Web, Zalo, Facebook, Viber, tổng đài).", { width: 5860 })
      ]}),
      new TableRow({ children: [
        TCell("Thanh toán", { bold: true, fill: "F2F2F2", width: 1300 }),
        TCell("VNPT Money / VNPT Pay", { bold: true, fill: "F2F2F2", width: 2200 }),
        TCell("Cổng thanh toán điện tử và ví VNPT Money - kênh thu cước viễn thông và thanh toán dịch vụ số.", { width: 5860, fill: "F2F2F2" })
      ]})
    ]
  }),

  H3("2.3.3. Tầng dữ liệu (Data Layer)"),
  P("Một đặc thù của doanh nghiệp viễn thông là khối lượng dữ liệu cực lớn - vài tỷ bản ghi CDR mỗi ngày, hàng chục triệu hồ sơ thuê bao, log thiết bị mạng phát sinh liên tục. VNPT tổ chức dữ liệu thành các kho chính sau:"),
  BULLET_MIX([{ text: "Master Customer Data: ", bold: true }, { text: "kho dữ liệu khách hàng tập trung (single customer view), giúp các kênh tiếp xúc khác nhau cùng nhìn một khách hàng theo một định danh duy nhất." }]),
  BULLET_MIX([{ text: "Product / Service Catalog: ", bold: true }, { text: "danh mục các gói cước, dịch vụ, combo - là \"nguồn sự thật\" cho cả BSS, kênh bán và website." }]),
  BULLET_MIX([{ text: "Network Inventory DB: ", bold: true }, { text: "dữ liệu hạ tầng mạng vật lý và logic, kèm thông tin GIS - phục vụ trực tiếp khâu khảo sát và cung cấp dịch vụ." }]),
  BULLET_MIX([{ text: "Billing & Revenue DB: ", bold: true }, { text: "CDR, cước phát sinh, hóa đơn, công nợ, lịch sử thanh toán - dữ liệu nhạy cảm cao và bị giám sát chặt bởi pháp luật về kế toán - thuế." }]),
  BULLET_MIX([{ text: "Data Lake / DWH: ", bold: true }, { text: "kho dữ liệu phân tích, gom dữ liệu từ các nguồn nói trên cộng với log thiết bị mạng, hành vi sử dụng app… - đây là nguồn dữ liệu quan trọng để VNPT huấn luyện các mô hình AI, dù việc khai thác còn phụ thuộc vào mức độ làm sạch và chuẩn hóa dữ liệu." }]),

  H3("2.3.4. Tầng công nghệ (Technology Layer)"),
  P("Tầng này chính là phần cơ sở hạ tầng - nơi VNPT có lợi thế lớn so với nhiều doanh nghiệp khác, với sáu nhóm chính:"),
  BULLET("Hạ tầng mạng truy nhập: mạng di động VinaPhone 4G/5G phủ 63 tỉnh thành, mạng cáp quang FTTH GPON/XGS-PON, mạng cố định băng rộng FiberVNN, mạng IoT NB-IoT."),
  BULLET("Mạng truyền dẫn: trục backbone IP/MPLS Bắc - Nam, DWDM dung lượng lớn, các tuyến cáp quang biển AAG, SMW3, APG, AAE-1 mà VNPT tham gia đầu tư."),
  BULLET("Trung tâm dữ liệu: tổ hợp 8 IDC tiêu chuẩn quốc tế (Tier III/IV), trong đó hai trung tâm lớn nhất ở Hòa Lạc (Hà Nội) và Tân Thuận (TP.HCM)."),
  BULLET("Nền tảng đám mây VNPT Smart Cloud: cung cấp IaaS - PaaS - SaaS, hỗ trợ Kubernetes, AI Platform với GPU dành cho huấn luyện mô hình ML/GenAI."),
  BULLET("An toàn thông tin: Trung tâm SOC VNPT-Cyber Immunity, hệ thống SIEM, IDS/IPS, dịch vụ chống DDoS, hạ tầng PKI và chữ ký số."),
  BULLET("Tích hợp và API: ESB / API Gateway nội bộ, Message Bus (Kafka) cho luồng sự kiện thời gian thực, hệ thống LDAP / SSO dùng chung cho toàn Tập đoàn."),
  P("Nhìn lại bốn tầng, có thể thấy VNPT có một kiến trúc tương đối đầy đủ so với mặt bằng doanh nghiệp Việt cùng quy mô. Tuy nhiên, theo quan sát thực tế, sự đầy đủ này đi kèm thách thức về tính nhất quán: với 63 chi nhánh tỉnh, một số nơi có thể triển khai phiên bản con của hệ thống lõi, dẫn tới nguy cơ phân mảnh dữ liệu nếu việc đồng bộ chưa tốt. Đây là lý do báo cáo đi sâu vào một quy trình cụ thể ở Câu 3, để xem các hệ thống thực sự phối hợp với nhau ra sao."),

  new Paragraph({ children: [new PageBreak()] }),
];

// ============== CÂU 3 ==============
const cau3 = [
  H1("CÂU 3. QUY TRÌNH LÕI: CUNG CẤP DỊCH VỤ INTERNET FTTH"),
  H2("3.1. Lý do chọn quy trình này"),
  P("Trong rất nhiều quy trình ở VNPT, quy trình cung cấp dịch vụ Internet cáp quang FTTH cho khách hàng cá nhân (mã sản phẩm FiberVNN Home) được chọn với mấy lý do thực tế:"),
  BULLET("Đây là một trong những quy trình tạo doanh thu cố định lớn nhất - thuê bao FTTH có ARPU cao, vòng đời dài và là nền cho các dịch vụ giá trị gia tăng khác như MyTV, Smart Home, VNPT Camera."),
  BULLET("Quy trình đụng vào hầu hết các HTTT lõi: CRM, BSS, OSS Service Fulfillment, OSS NMS, Network Inventory, ERP, DWH - tức là rất giàu \"đất diễn\" để phân tích ở Câu 4 và Câu 5."),
  BULLET("Khâu khảo sát - lắp đặt - kích hoạt là điểm trải nghiệm khách hàng nhạy cảm (thời gian chờ, độ chính xác, sự minh bạch). Nếu cải tiến được, tác động NPS rất rõ - đây cũng là không gian rất tốt để đề xuất AI/RPA ở Câu 5."),

  H2("3.2. Vai trò của quy trình trong chuỗi giá trị VNPT"),
  P("Trong chuỗi giá trị Porter đã trình bày ở Câu 1, quy trình này nằm gọn ở hai mắt xích \"Hậu cần đầu ra\" và \"Vận hành\" - tức là khâu biến năng lực hạ tầng mạng thành dịch vụ thực tế đến tay khách hàng. Nói cách khác, đây là điểm mà mọi đầu tư mạng lưới, mọi sản phẩm thiết kế bởi marketing đều phải đi qua. Một quy trình tốt sẽ rút ngắn thời gian từ lúc khách hàng có nhu cầu đến lúc dùng được dịch vụ (lead time), tăng tỉ lệ chuyển đổi và giảm chi phí đi lại của đội kỹ thuật."),
  P("Theo cam kết chất lượng (SLA) công bố của VNPT, thời gian lắp đặt từ khi đăng ký đến khi kích hoạt thành công thường là 3-5 ngày làm việc tại khu vực đô thị. Qua thực tế công tác, có thể thấy SLA bị trễ thường rơi vào hai khâu: khảo sát hạ tầng và đợi vật tư - cáp - những điểm rất phù hợp để phân tích sâu ở Câu 4."),

  H2("3.3. Mô tả các bước của quy trình hiện tại (As-is)"),
  P("Quy trình As-is gồm 4 giai đoạn chính, tổng cộng 12 hoạt động nghiệp vụ, có sự tham gia của 5 vai trò (khách hàng, CSKH tổng đài, Kinh doanh, Kỹ thuật, Billing/Hậu kiểm), mô tả ngắn gọn như sau:"),

  H3("Giai đoạn 1: Tiếp nhận yêu cầu"),
  BULLET("Bước 1 - Khách hàng phát sinh nhu cầu lắp Internet, liên hệ VNPT qua tổng đài 18001166, website vnpt.com.vn, ứng dụng My VNPT hoặc điểm giao dịch."),
  BULLET("Bước 2 - CSKH tiếp nhận yêu cầu, tạo lead trên CRM, ghi nhận thông tin khách hàng và nhu cầu."),
  BULLET("Bước 3 - CSKH tra cứu vùng phục vụ trên Network Inventory để xem có hạ tầng FTTH ở khu vực đó không. Nếu không có, từ chối yêu cầu (kết thúc bất thành); nếu có, chuyển sang bộ phận Kinh doanh."),

  H3("Giai đoạn 2: Bán hàng và ký hợp đồng"),
  BULLET("Bước 4 - Nhân viên Kinh doanh gọi lại tư vấn gói cước (Home 1, Home 2, Home Combo MyTV…), khuyến mại, cam kết. Gửi báo giá và mẫu hợp đồng."),
  BULLET("Bước 5 - Khách hàng ký hợp đồng giấy (hoặc HĐ điện tử nếu đăng ký online), cung cấp CCCD/Hộ khẩu."),
  BULLET("Bước 6 - Kinh doanh nhập thông tin hợp đồng vào hệ thống BSS, tạo đơn hàng (sales order)."),
  BULLET("Bước 7 - BSS phát hành work order tới Kỹ thuật để khảo sát và lắp đặt."),

  H3("Giai đoạn 3: Khảo sát và lắp đặt"),
  BULLET("Bước 8 - Điều phối kỹ thuật phân công kỹ thuật viên (KTV) theo địa bàn, lên lịch hẹn khách hàng."),
  BULLET("Bước 9 - KTV đến khảo sát thực địa: kiểm tra điểm đấu (ODF/splitter), khoảng cách kéo cáp, mặt bằng lắp ONU. Nếu không khả thi (ví dụ vị trí xa, không còn port trống) thì trả về Kinh doanh để chốt lại với khách hàng."),
  BULLET("Bước 10 - Nếu khả thi, KTV tiến hành kéo cáp, đấu nối ONU và modem WiFi tại nhà khách hàng."),
  BULLET("Bước 11 - KTV cấu hình và kích hoạt dịch vụ qua OSS Service Fulfillment (tạo VLAN, gán port, mở dịch vụ trên BRAS, đẩy cấu hình ACS lên ONU)."),

  H3("Giai đoạn 4: Nghiệm thu và mở cước"),
  BULLET("Bước 12 - Khách hàng kiểm tra tốc độ, ký biên bản nghiệm thu. Hậu kiểm/Billing đóng work order, mở cước trên BSS Billing, phát hành hóa đơn đầu tiên qua VNPT Money/email/SMS. CRM cập nhật trạng thái thuê bao thành \"đang hoạt động\"."),

  H2("3.4. Mô hình hóa BPMN (Bizagi Modeler)"),
  P("Quy trình trên được mô hình hóa bằng ký pháp BPMN 2.0 chuẩn, có thể export ra file .bpmn của Bizagi Modeler. Sơ đồ sử dụng hai pool (VNPT và Khách hàng), bốn lane bên trong pool VNPT (CSKH, Kinh doanh, Kỹ thuật, Billing) cùng các phần tử Task, Gateway XOR, Start/End Event, Sequence flow và Message flow theo đúng BPMN."),
  ...IMG("bpmn_asis.png", 620, 365, "Hình 3.1. Sơ đồ BPMN As-is - Quy trình cung cấp dịch vụ FTTH tại VNPT"),
  P("Một số điểm cần lưu ý trong sơ đồ: (i) gateway XOR đầu tiên ở lane CSKH dùng để xử lý trường hợp không có hạ tầng - nhánh từ chối kết thúc tại End Event \"Từ chối\"; (ii) gateway thứ hai ở lane Kỹ thuật xử lý trường hợp khảo sát không khả thi, quay vòng về Kinh doanh để thương lượng lại với khách hàng; (iii) toàn bộ tương tác với khách hàng được vẽ bằng message flow nét đứt theo chuẩn BPMN."),

  new Paragraph({ children: [new PageBreak()] }),
];

// ============== CÂU 4 ==============
const cau4 = [
  H1("CÂU 4. PHÂN TÍCH HIỆN TRẠNG CÁC HTTT LIÊN QUAN QUY TRÌNH"),
  H2("4.1. Nguyên tắc nhận diện"),
  P("Theo gợi ý của đề bài, quan hệ giữa quy trình nghiệp vụ (BP) và hệ thống thông tin (IS) là quan hệ nhiều - nhiều (N:M). Một BP có thể không cần IS nào, hoặc cần nhiều IS cùng tham gia; ngược lại một IS bắt buộc gắn với ít nhất một BP (vì IS sinh ra để phục vụ nghiệp vụ). Phần này trình bày theo hai bước: (i) liệt kê IS có liên quan tới quy trình FTTH, (ii) lập ma trận N:M để nhìn rõ mức độ tham gia."),

  H2("4.2. Danh mục HTTT liên quan và vai trò trong quy trình"),
  P("Rà soát lại sơ đồ As-is ở Câu 3 cho thấy có 8 hệ thống thông tin trực tiếp tham gia quy trình:"),

  new Table({
    width: { size: 9360, type: WidthType.DXA },
    columnWidths: [800, 2200, 3000, 3360],
    rows: [
      new TableRow({ tableHeader: true, children: [
        TCell("STT", { bold: true, fill: "1F4E79", width: 800, size: 22, align: AlignmentType.CENTER }),
        TCell("Hệ thống (IS)", { bold: true, fill: "1F4E79", width: 2200, size: 22 }),
        TCell("Bước nghiệp vụ tham gia", { bold: true, fill: "1F4E79", width: 3000, size: 22 }),
        TCell("Vai trò trong quy trình", { bold: true, fill: "1F4E79", width: 3360, size: 22 })
      ]}),
      new TableRow({ children: [
        TCell("1", { width: 800, align: AlignmentType.CENTER }),
        TCell("CRM", { bold: true, width: 2200 }),
        TCell("Bước 1, 2, 4, 12", { width: 3000 }),
        TCell("Tiếp nhận yêu cầu, tạo lead, ghi nhận tương tác CSKH, cập nhật trạng thái thuê bao sau lắp.", { width: 3360 })
      ]}),
      new TableRow({ children: [
        TCell("2", { width: 800, align: AlignmentType.CENTER, fill: "F2F2F2" }),
        TCell("Network Inventory", { bold: true, width: 2200, fill: "F2F2F2" }),
        TCell("Bước 3, 9", { width: 3000, fill: "F2F2F2" }),
        TCell("Tra cứu vùng phục vụ, kiểm tra port/ODF còn trống, cấp phát tài nguyên mạng cho thuê bao mới.", { width: 3360, fill: "F2F2F2" })
      ]}),
      new TableRow({ children: [
        TCell("3", { width: 800, align: AlignmentType.CENTER }),
        TCell("BSS - Order Management", { bold: true, width: 2200 }),
        TCell("Bước 6, 7, 12", { width: 3000 }),
        TCell("Tạo và quản lý đơn hàng, đẩy work order xuống OSS, ghi nhận trạng thái đơn.", { width: 3360 })
      ]}),
      new TableRow({ children: [
        TCell("4", { width: 800, align: AlignmentType.CENTER, fill: "F2F2F2" }),
        TCell("BSS - Billing & Rating", { bold: true, width: 2200, fill: "F2F2F2" }),
        TCell("Bước 12", { width: 3000, fill: "F2F2F2" }),
        TCell("Mở cước, áp giá gói cước, phát hành hóa đơn đầu tiên, gửi thông báo cước.", { width: 3360, fill: "F2F2F2" })
      ]}),
      new TableRow({ children: [
        TCell("5", { width: 800, align: AlignmentType.CENTER }),
        TCell("OSS - Service Fulfillment", { bold: true, width: 2200 }),
        TCell("Bước 7, 11", { width: 3000 }),
        TCell("Tự động cấu hình thiết bị mạng (OLT, BRAS, ACS), kích hoạt dịch vụ trên hạ tầng.", { width: 3360 })
      ]}),
      new TableRow({ children: [
        TCell("6", { width: 800, align: AlignmentType.CENTER, fill: "F2F2F2" }),
        TCell("OSS - NMS/Assurance", { bold: true, width: 2200, fill: "F2F2F2" }),
        TCell("Bước 11, 12", { width: 3000, fill: "F2F2F2" }),
        TCell("Đo chất lượng đường truyền sau lắp, ghi nhận cảnh báo sớm để hỗ trợ nghiệm thu.", { width: 3360, fill: "F2F2F2" })
      ]}),
      new TableRow({ children: [
        TCell("7", { width: 800, align: AlignmentType.CENTER }),
        TCell("My VNPT App / Portal", { bold: true, width: 2200 }),
        TCell("Bước 1, 12", { width: 3000 }),
        TCell("Kênh tự đăng ký dịch vụ và xem tiến độ lắp đặt, kích hoạt eContract.", { width: 3360 })
      ]}),
      new TableRow({ children: [
        TCell("8", { width: 800, align: AlignmentType.CENTER, fill: "F2F2F2" }),
        TCell("VNPT Money / VNPT Pay", { bold: true, width: 2200, fill: "F2F2F2" }),
        TCell("Bước 12", { width: 3000, fill: "F2F2F2" }),
        TCell("Thu cước lắp đặt và phí thuê bao tháng đầu qua kênh số.", { width: 3360, fill: "F2F2F2" })
      ]})
    ]
  }),

  H2("4.3. Ma trận N:M giữa Business Process và Information System"),
  P("Để minh họa rõ quan hệ N:M, ma trận dưới đây có dòng là các hoạt động (BP1 đến BP12 - tương ứng 12 bước ở Câu 3), cột là 8 hệ thống đã liệt kê. Dấu ✓ ở giao điểm thể hiện IS đó có tham gia vào hoạt động tương ứng:"),

  new Table({
    width: { size: 9360, type: WidthType.DXA },
    columnWidths: [2160, 900, 900, 900, 900, 900, 900, 900, 900],
    rows: [
      new TableRow({ tableHeader: true, children: [
        TCell("Bước", { bold: true, fill: "ED7D31", width: 2160, size: 20, align: AlignmentType.CENTER }),
        TCell("CRM", { bold: true, fill: "ED7D31", width: 900, size: 20, align: AlignmentType.CENTER }),
        TCell("Inv", { bold: true, fill: "ED7D31", width: 900, size: 20, align: AlignmentType.CENTER }),
        TCell("BSS-OM", { bold: true, fill: "ED7D31", width: 900, size: 20, align: AlignmentType.CENTER }),
        TCell("BSS-Bill", { bold: true, fill: "ED7D31", width: 900, size: 20, align: AlignmentType.CENTER }),
        TCell("OSS-SF", { bold: true, fill: "ED7D31", width: 900, size: 20, align: AlignmentType.CENTER }),
        TCell("OSS-NMS", { bold: true, fill: "ED7D31", width: 900, size: 20, align: AlignmentType.CENTER }),
        TCell("MyVNPT", { bold: true, fill: "ED7D31", width: 900, size: 20, align: AlignmentType.CENTER }),
        TCell("VNPT Money", { bold: true, fill: "ED7D31", width: 900, size: 20, align: AlignmentType.CENTER })
      ]}),
      ...[
        ["BP1. Khách phát sinh nhu cầu, liên hệ VNPT", ["", "", "", "", "", "", "✓", ""]],
        ["BP2. CSKH ghi nhận, tạo lead trên CRM", ["✓", "", "", "", "", "", "", ""]],
        ["BP3. Tra cứu vùng phục vụ", ["", "✓", "", "", "", "", "", ""]],
        ["BP4. Tư vấn gói cước, gửi báo giá", ["✓", "", "", "", "", "", "✓", ""]],
        ["BP5. Khách ký HĐ, cung cấp CCCD", ["", "", "", "", "", "", "✓", ""]],
        ["BP6. Tạo đơn hàng trên BSS", ["", "", "✓", "", "", "", "", ""]],
        ["BP7. Phát hành work order", ["", "", "✓", "", "✓", "", "", ""]],
        ["BP8. Điều phối phân công KTV", ["", "✓", "✓", "", "", "", "", ""]],
        ["BP9. Khảo sát thực địa", ["", "✓", "", "", "", "", "", ""]],
        ["BP10. Kéo cáp, đấu nối ONU/modem", ["", "✓", "", "", "", "", "", ""]],
        ["BP11. Cấu hình & kích hoạt qua OSS", ["", "", "", "", "✓", "✓", "", ""]],
        ["BP12. Nghiệm thu, mở cước, xuất hóa đơn", ["✓", "", "✓", "✓", "", "✓", "✓", "✓"]]
      ].map((row, i) => new TableRow({
        children: [
          TCell(row[0], { width: 2160, size: 20, fill: i % 2 === 0 ? null : "FFF2CC" }),
          ...row[1].map(c => TCell(c, { width: 900, size: 22, align: AlignmentType.CENTER, bold: c === "✓", fill: i % 2 === 0 ? null : "FFF2CC" }))
        ]
      }))
    ]
  }),
  P("Ma trận này cho thấy hai điểm đáng chú ý:", { indent: false, spacing: { before: 200, line: 360, after: 120 } }),
  BULLET("Một bước nghiệp vụ thường gọi đến nhiều IS cùng lúc (đặc biệt bước 12 - mở cước - đụng đến 6 hệ thống). Đây chính là minh chứng quan hệ N:M."),
  BULLET("Trục \"nóng\" nhất là cụm BSS Order Management - OSS Service Fulfillment - Network Inventory. Nếu ba hệ thống này không nói chuyện được tốt với nhau (ví dụ qua API/ESB), quy trình sẽ tắc nghẽn ngay ở giữa."),

  H2("4.4. Đánh giá hiện trạng - điểm mạnh và điểm yếu"),
  P("Phần này dựa trên quan sát thực tế từ một số dự án liên quan đến bán hàng và chăm sóc khách hàng, kết hợp với ma trận ở trên. Vì không có quyền truy cập đầy đủ số liệu vận hành nội bộ, các nhận định được trình bày ở mức thận trọng - tức là nêu ra như những vấn đề có thể xảy ra hoặc thường gặp, chứ không khẳng định đúng với mọi địa bàn."),

  H3("Điểm mạnh"),
  BULLET("Bộ HTTT khá đầy đủ, gần như mỗi bước nghiệp vụ đều đã có IS hỗ trợ - đây là tài sản lớn so với nhiều doanh nghiệp Việt cùng quy mô."),
  BULLET("OSS Service Fulfillment đã có khả năng tự động cấu hình thiết bị qua API, nhờ vậy khâu kích hoạt dịch vụ (bước 11) thường chỉ mất vài phút sau khi KTV xác nhận."),
  BULLET("Hệ thống thanh toán VNPT Money/VNPT Pay đã được tích hợp ngay từ bước phát hành hóa đơn đầu tiên - giúp dòng tiền chảy nhanh."),
  BULLET("Bắt đầu có sự hiện diện của AI: VNPT SmartBot đã tham gia trả lời tự động một phần các yêu cầu ở bước 1, dù còn ở mức cơ bản."),

  H3("Điểm yếu và nút thắt (theo quan sát cá nhân)"),
  BULLET_MIX([{ text: "Dữ liệu khách hàng giữa các đơn vị địa bàn có thể chưa đồng nhất: ", bold: true }, { text: "tuy đã có Master Customer Data, theo quan sát thực tế, trong một số tình huống cùng một khách hàng vẫn có lịch sử tương tác nằm ở nhiều hệ thống khác nhau, khiến nhân viên phải kiểm tra chéo thủ công và dễ trùng đơn." }]),
  BULLET_MIX([{ text: "Khâu khảo sát (Bước 9) phụ thuộc nhiều vào con người: ", bold: true }, { text: "nếu Network Inventory chưa cập nhật kịp thời, KTV thường phải đến tận nơi mới biết khả thi hay không. Đây là một trong những khâu có thể làm chậm thời gian lắp đặt." }]),
  BULLET_MIX([{ text: "OCR và eKYC chưa được áp dụng đồng đều: ", bold: true }, { text: "ở nhiều trường hợp khách vẫn nộp CCCD bản cứng và nhân viên nhập tay vào hệ thống - thao tác này dễ phát sinh sai sót thông tin." }]),
  BULLET_MIX([{ text: "Việc chăm sóc khách hàng phần lớn còn mang tính phản ứng: ", bold: true }, { text: "OSS NMS có khả năng phát hiện sự cố sớm, nhưng nếu dữ liệu chưa kết nối liền mạch sang CRM/SmartBot thì khó chủ động báo trước cho khách hàng." }]),
  BULLET_MIX([{ text: "Bài toán điều phối kỹ thuật (Bước 8) chủ yếu dựa trên kinh nghiệm: ", bold: true }, { text: "khi chưa có công cụ tối ưu tuyến đường và tải công việc, có thể xảy ra tình trạng một số KTV quá tải trong khi người khác lại nhàn hơn." }]),

  H3("Cơ hội cải tiến"),
  P("Điểm chung của các vấn đề trên là chúng chủ yếu nằm ở khâu nhập liệu thủ công, tra cứu thông tin và tương tác với khách hàng - những việc lặp lại nhiều và phụ thuộc con người. Đây là nhóm bài toán mà các công nghệ AI hiện nay, đặc biệt là Generative AI kết hợp OCR/eKYC, có thể hỗ trợ tốt. Đó là tiền đề cho phương án cải tiến có phạm vi vừa phải được trình bày ở Câu 5, thay vì cố gắng tự động hóa toàn bộ quy trình."),

  new Paragraph({ children: [new PageBreak()] }),
];

// ============== CÂU 5 ==============
const cau5 = [
  H1("CÂU 5. GIẢI PHÁP CẢI TIẾN BẰNG GENERATIVE AI"),
  H2("5.1. Phạm vi đề xuất"),
  P("Cần xác định rõ phạm vi ngay từ đầu để tránh ôm đồm. Báo cáo không đề xuất tự động hóa toàn bộ quy trình cung cấp dịch vụ FTTH, vì quy trình này liên quan đến nhiều hệ thống lõi như CRM, BSS, OSS, Network Inventory và đội kỹ thuật tại địa bàn - tự động hóa hết một lúc vừa rủi ro vừa vượt quá khả năng chứng minh của một bài tập. Thay vào đó, phạm vi đề xuất tập trung vào giai đoạn đầu của quy trình: tiếp nhận nhu cầu, tư vấn gói cước, xác thực thông tin khách hàng và tạo hồ sơ đăng ký. Đây là nhóm bước có tần suất cao, còn nhiều thao tác nhập liệu thủ công, và phù hợp hơn với khả năng hiện tại của Generative AI kết hợp OCR/eKYC."),
  P("Trong phạm vi báo cáo, Generative AI được hiểu không chỉ là một chatbot trả lời khách hàng, mà là lớp công nghệ hỗ trợ xử lý các dữ liệu bán cấu trúc và phi cấu trúc trong quy trình FTTH: nội dung hội thoại bằng ngôn ngữ tự nhiên, giấy tờ của khách hàng, yêu cầu dịch vụ và thông tin gói cước. OCR/eKYC được ghép thêm vì hai kỹ thuật này gắn liền với khâu đọc và xác thực CCCD - vốn là điểm nhập liệu dễ sai nhất trong giai đoạn tiếp nhận."),
  P("Một thuận lợi là các thành phần này phần lớn đã có sẵn trong nội bộ VNPT. Sản phẩm VNPT SmartBot đã ứng dụng GenAI, NLP và OCR, từng đạt giải Bạc Stevie Awards 2022 ở hạng mục B2B Product; nền tảng vnptai.io cũng đã cung cấp các API liên quan. Nói cách khác, đề xuất thiên về lắp ghép và tinh chỉnh những gì đã có hơn là xây mới từ đầu."),

  H2("5.2. Lý do chọn Generative AI cho giai đoạn này"),
  P("GenAI được chọn (thay vì chỉ RPA hay Blockchain) cho khâu tiếp nhận - tư vấn vì ba lý do gắn với đặc thù của chính giai đoạn này:"),
  BULLET_MIX([{ text: "Tương tác khách hàng rất đa dạng: ", bold: true }, { text: "khách hỏi tự do bằng tiếng Việt, nhiều ngữ cảnh khác nhau. GenAI qua mô hình ngôn ngữ lớn (LLM) thường hiểu ý định tốt hơn chatbot theo kịch bản cứng." }]),
  BULLET_MIX([{ text: "Hồ sơ khách hàng mang tính bán cấu trúc: ", bold: true }, { text: "CCCD, giấy tờ là dữ liệu phi cấu trúc; tổ hợp OCR và LLM xử lý được phần trích xuất và kiểm tra thông tin." }]),
  BULLET_MIX([{ text: "Nhu cầu tư vấn gói cước cần ngữ cảnh: ", bold: true }, { text: "mỗi hộ gia đình có nhu cầu khác nhau. GenAI có thể hỏi đúng vài câu rồi gợi ý gói phù hợp, nhưng - như sẽ phân tích ở phần rủi ro - phải tra cứu từ danh mục gói cước chính thức chứ không để mô hình tự bịa." }]),

  H2("5.3. Quy trình To-be sau cải tiến"),
  P("Khung quy trình As-is được giữ nguyên, chỉ thay đổi cách vận hành ở giai đoạn đầu. Quy trình To-be không thay thế hoàn toàn vai trò của nhân viên kinh doanh và kỹ thuật viên, mà tập trung giảm tải các thao tác lặp lại ở khâu tiếp nhận và lập hồ sơ. Khách hàng có thể bắt đầu đăng ký qua chatbot trên website, Zalo hoặc My VNPT; chatbot dùng GenAI để hiểu nhu cầu bằng ngôn ngữ tự nhiên, sau đó truy xuất thông tin gói cước từ danh mục đã được kiểm duyệt. Khi khách chọn gói phù hợp, hệ thống yêu cầu chụp CCCD để OCR/eKYC trích xuất thông tin, tạo hồ sơ đăng ký sơ bộ và chuyển sang CRM/BSS. Nhân viên kinh doanh kiểm tra lại thông tin, xử lý các ngoại lệ và chuyển đơn sang bước khảo sát/lắp đặt."),
  ...IMG("bpmn_tobe.png", 620, 388, "Hình 5.1. Sơ đồ BPMN To-be - Cải tiến giai đoạn tiếp nhận, tư vấn và lập hồ sơ FTTH bằng GenAI + OCR/eKYC"),

  H3("Bốn điểm cải tiến chính (trong phạm vi bài)"),
  BULLET_MIX([{ text: "GenAI chatbot tiếp nhận nhu cầu. ", bold: true }, { text: "Chatbot hỏi khách về địa chỉ, số người dùng, mục đích sử dụng, có cần MyTV/Smart Home không, yêu cầu lắp đặt - thay cho việc khách phải tự dò gói trên website hoặc chờ tổng đài viên." }]),
  BULLET_MIX([{ text: "RAG tra cứu thông tin gói cước chính thức. ", bold: true }, { text: "GenAI không tự bịa thông tin gói cước, mà dùng kỹ thuật Retrieval Augmented Generation để tra cứu từ Product Catalog hoặc kho tri thức đã được kiểm duyệt, rồi mới tư vấn." }]),
  BULLET_MIX([{ text: "OCR/eKYC xử lý giấy tờ. ", bold: true }, { text: "Khách chụp CCCD, hệ thống trích xuất thông tin và đối chiếu, giúp giảm nhập tay và giảm lỗi sai thông tin ngay từ đầu vào." }]),
  BULLET_MIX([{ text: "Tự động tạo hồ sơ đăng ký trên CRM/BSS. ", bold: true }, { text: "Sau khi khách xác nhận, dữ liệu được chuyển sang CRM/BSS để tạo hồ sơ sơ bộ. Nhân viên chỉ tập trung kiểm tra các trường hợp ngoại lệ thay vì nhập lại toàn bộ." }]),

  H2("5.4. Tính hợp lý của giải pháp"),
  H3("Về công nghệ"),
  P("Các thành phần trong phạm vi đề xuất đều đã có sẵn và được kiểm chứng: VNPT SmartBot đã có module OCR, NLP và chatbot GenAI đang thương mại hóa; kỹ thuật RAG để giảm bịa thông tin đã phổ biến trong các ứng dụng LLM doanh nghiệp. Vì vậy về mặt công nghệ, đây là giải pháp khả thi chứ không phải ý tưởng xa vời."),
  H3("Về vận hành"),
  P("Phương án hợp lý là triển khai dạng thí điểm tại một vài địa bàn trước khi nhân rộng. Pha thí điểm tập trung vào ba việc: bật chatbot GenAI tiếp nhận, bật OCR/eKYC, và tạo hồ sơ sơ bộ trên CRM/BSS. Các pha này chủ yếu chạm vào trải nghiệm khách hàng và khâu nhập liệu, ít ảnh hưởng tới đội kỹ thuật ngoài hiện trường, nên rủi ro thay đổi vận hành ở mức kiểm soát được. Việc giữ nhân viên kinh doanh ở vai trò kiểm tra ngoại lệ cũng giúp đảm bảo an toàn trong giai đoạn đầu."),
  H3("Về hiệu quả - các chỉ tiêu nên theo dõi khi thí điểm"),
  P("Báo cáo không đưa ra con số lợi ích cụ thể vì chưa có dữ liệu đo lường thực tế. Thay vào đó, dưới đây là bộ chỉ tiêu đề xuất để theo dõi trước/sau khi thí điểm:"),

  new Table({
    width: { size: 9360, type: WidthType.DXA },
    columnWidths: [3300, 3030, 3030],
    rows: [
      new TableRow({ tableHeader: true, children: [
        TCell("Chỉ tiêu theo dõi", { bold: true, fill: "70AD47", width: 3300, size: 22 }),
        TCell("Hiện trạng", { bold: true, fill: "70AD47", width: 3030, size: 22, align: AlignmentType.CENTER }),
        TCell("Kỳ vọng sau thí điểm", { bold: true, fill: "70AD47", width: 3030, size: 22, align: AlignmentType.CENTER })
      ]}),
      ...[
        ["Thời gian tiếp nhận và tạo hồ sơ", "Phụ thuộc nhiều vào nhân viên", "Giảm thời gian nhập liệu và kiểm tra thông tin"],
        ["Tỉ lệ sai thông tin khách hàng", "Có thể xảy ra do nhập tay", "Giảm nhờ OCR/eKYC"],
        ["Tỉ lệ khách tự phục vụ", "Còn hạn chế", "Tăng qua chatbot/app"],
        ["Khối lượng câu hỏi lặp lại cho CSKH", "Nhân viên xử lý nhiều câu đơn giản", "GenAI trả lời theo kho tri thức đã kiểm duyệt"],
        ["Trải nghiệm khách hàng", "Khác nhau theo kênh và nhân viên", "Đồng nhất hơn trên các kênh số"]
      ].map((row, i) => new TableRow({
        children: [
          TCell(row[0], { width: 3300, fill: i % 2 === 0 ? null : "F2F2F2" }),
          TCell(row[1], { width: 3030, align: AlignmentType.CENTER, fill: i % 2 === 0 ? null : "F2F2F2" }),
          TCell(row[2], { width: 3030, align: AlignmentType.CENTER, fill: i % 2 === 0 ? null : "F2F2F2" })
        ]
      }))
    ]
  }),
  P("Lưu ý: các chỉ tiêu trên là mục tiêu theo dõi trong giai đoạn thí điểm, không phải kết quả đã được kiểm chứng. Để đánh giá hiệu quả, VNPT cần đo trước/sau tại một số địa bàn thí điểm trong thời gian tối thiểu 3-6 tháng.", { indent: false, spacing: { before: 160, line: 360, after: 120 } }),

  H2("5.5. Hướng phát triển sau (ngoài phạm vi bài)"),
  P("Trong quá trình phân tích còn xuất hiện một số ý tưởng mở rộng, nhưng chúng nên được xem là giai đoạn sau - khi dữ liệu quy trình đã đủ sạch và các hệ thống CRM-BSS-OSS được tích hợp ổn định. Các ý tưởng này được ghi lại để báo cáo có hướng phát triển tiếp, nhưng không tính vào đề xuất chính:"),
  BULLET("Dùng ML dự đoán khả thi lắp đặt từ dữ liệu Inventory và lịch sử khảo sát, để có thể trả lời sớm cho khách thay vì chờ kỹ thuật viên ra hiện trường."),
  BULLET("Tối ưu lịch phân công kỹ thuật viên bằng bài toán định tuyến (Vehicle Routing Problem) kết hợp ML ước lượng thời lượng từng đơn."),
  BULLET("Dùng RPA tự động cấu hình thiết bị qua OSS API và tự động mở cước, xuất hóa đơn điện tử ở khâu cuối."),
  P("Lý do đẩy các ý này về sau là chúng đụng vào hệ thống lõi (OSS, BSS Billing) và yêu cầu dữ liệu chất lượng cao - nếu làm sớm khi nền dữ liệu chưa sẵn sàng thì rủi ro lớn hơn lợi ích."),

  H2("5.6. Rủi ro và hạn chế"),
  P("Để tránh lý tưởng hóa, cần ghi nhận một số rủi ro của ngay cả phần đề xuất đã thu hẹp:"),
  BULLET("Dữ liệu cá nhân: GenAI và OCR làm việc với CCCD, thông tin liên lạc - cần tuân thủ Nghị định 13/2023/NĐ-CP về bảo vệ dữ liệu cá nhân, có cơ chế ẩn danh khi huấn luyện và lưu vết truy cập."),
  BULLET("Rủi ro mô hình trả lời sai (hallucination): chatbot có thể tư vấn sai về gói cước. Vì vậy bắt buộc dùng RAG dựa trên danh mục chính thức và giữ nhân viên kiểm tra ở các bước nhạy cảm như báo giá, ký hợp đồng."),
  BULLET("Thay đổi tổ chức: khi chatbot xử lý phần lớn câu hỏi đơn giản, vai trò của tổng đài viên sẽ thay đổi. Cần kế hoạch đào tạo lại nhân lực sang việc giám sát AI và xử lý ca khó, thay vì cắt giảm thuần túy."),
  BULLET("Tích hợp với hệ thống cũ: kết nối với CRM/BSS hiện hữu có thể tốn công hơn dự kiến, cần phối hợp với VNPT-IT ngay từ đầu."),
  P("Cuối cùng, cũng cần thẳng thắn về hạn chế của chính báo cáo: do không có dữ liệu vận hành nội bộ, chưa thể lượng hóa chi phí đầu tư hay hiệu quả tài chính của giải pháp. Những gì trình bày ở đây là một hướng đi được đánh giá là hợp lý và khả thi, nhưng để ra quyết định thực sự thì VNPT cần một giai đoạn thí điểm có đo lường cụ thể."),

  new Paragraph({ children: [new PageBreak()] }),
];

// ============== CONCLUSION ==============
const conclusion = [
  H1("KẾT LUẬN"),
  P("Báo cáo đã phân tích VNPT dưới góc độ hệ thống thông tin quản lý, đi từ tổng thể tới chi tiết, và rút ra một số điểm có giá trị cho thực tiễn công tác."),
  P("Điểm thứ nhất là về tư duy hệ thống. Khung TOGAF với bốn tầng kiến trúc cung cấp một cách định vị mỗi khi có yêu cầu mới: tính năng đó nằm ở tầng nghiệp vụ nào, đụng vào ứng dụng nào, dữ liệu ra sao và có cần thay đổi hạ tầng không. Câu hỏi nghe đơn giản nhưng giúp tránh được khá nhiều tình huống làm rồi mới phát hiện thiếu."),
  P("Điểm thứ hai là về việc mô hình hóa quy trình bằng BPMN. So với mô tả bằng văn bản, sơ đồ BPMN As-is buộc người phân tích phải nói rõ ai làm gì, khi nào, dữ liệu đi qua đâu. Khi vẽ xong As-is, các nút thắt lộ ra khá rõ, và sơ đồ To-be cũng vì thế mà tự nhiên hơn."),
  P("Điểm thứ ba là về vai trò của Generative AI. Sau khi thu hẹp phạm vi đề xuất, có thể thấy rõ một điều: với một bài toán thực tế, việc chọn đúng phạm vi quan trọng không kém việc chọn công nghệ. Một đề xuất vừa sức, có thí điểm và có đo lường sẽ thuyết phục hơn nhiều so với một bản vẽ tự động hóa toàn bộ nhưng khó chứng minh. AI khó thay thế con người trong viễn thông ở tương lai gần, nhưng ở khâu tiếp nhận và lập hồ sơ thì GenAI kết hợp OCR/eKYC là một hướng đáng thử."),
  P("Cũng cần nhắc lại hạn chế của báo cáo: do không tiếp cận được dữ liệu vận hành nội bộ, chưa thể lượng hóa chi phí đầu tư và hiệu quả tài chính; phần đánh giá hiện trạng chủ yếu dựa trên quan sát thực tế nên có thể không đúng với mọi địa bàn. Đây là những điểm cần được bổ sung nếu có điều kiện nghiên cứu sâu hơn."),
  new Paragraph({ children: [new PageBreak()] }),
];

// ============== REFERENCES ==============
const refs = [
  H1("TÀI LIỆU THAM KHẢO"),
  P("Báo cáo đã tham khảo các nguồn chính sau:", { indent: false }),
  BULLET("Thủ tướng Chính phủ (2024). Quyết định số 1019/QĐ-TTg ngày 23/9/2024 phê duyệt Chiến lược phát triển VNPT đến năm 2030, tầm nhìn 2035."),
  BULLET("Báo Chính phủ (2024). \"Chiến lược phát triển VNPT đến năm 2030, tầm nhìn đến năm 2035\". baochinhphu.vn"),
  BULLET("VnEconomy (2025). \"Cơ cấu lại Tập đoàn VNPT: Mục tiêu hết 2025, tổng doanh thu đạt hơn 287 nghìn tỷ\". vneconomy.vn"),
  BULLET("VNPT (2024). \"Tập đoàn VNPT năm 2024: Giữ nhịp phát triển trong bối cảnh khó khăn, khai phá không gian tăng trưởng mới\". vnpt.com.vn"),
  BULLET("VnExpress (2025). \"Doanh thu VNPT hơn 58.000 tỷ đồng\". vnexpress.net"),
  BULLET("VNPT (2024). Trang giới thiệu cơ cấu tổ chức. vnpt.com.vn/gioi-thieu/to-chuc/"),
  BULLET("VNPT (2024). \"Phần mềm giải pháp hỗ trợ chăm sóc, tư vấn khách hàng (VNPT Smartbot)\". vnpt.com.vn"),
  BULLET("VNPT AI (2025). Trang sản phẩm VNPT SmartBot. vnptai.io/smartbot/vi"),
  BULLET("VNPT (2024). \"Hướng dẫn đăng ký lắp mạng Internet VNPT - 4 bước\". vnpt.com.vn/tu-van"),
  BULLET("The Open Group (2022). TOGAF Standard, Version 9.2."),
  BULLET("OMG (2014). Business Process Model and Notation (BPMN) Version 2.0.2."),
  BULLET("M. E. Porter (1985). Competitive Advantage: Creating and Sustaining Superior Performance. The Free Press."),
  BULLET("SRM Tech (2024). \"The Role of OSS and BSS in Telecom Management\". srmtech.com"),
  BULLET("Microsoft AI (2024). \"What Are OSS and BSS?\". microsoft.com/en-us/ai/telecommunications"),
];

// ============== BUILD DOC ==============

const doc = new Document({
  creator: "Nguyen Minh Hieu - HV K27",
  title: "Bai Tap Lon HTTTQL - VNPT",
  description: "Bao cao Hoc phan He thong thong tin quan ly nang cao",
  styles: {
    default: {
      document: { run: { font: FONT, size: 26 } }
    },
    paragraphStyles: [
      {
        id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 32, bold: true, font: FONT, color: "1F4E79" },
        paragraph: { spacing: { before: 360, after: 200 }, outlineLevel: 0 }
      },
      {
        id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 28, bold: true, font: FONT, color: "2E75B6" },
        paragraph: { spacing: { before: 240, after: 160 }, outlineLevel: 1 }
      },
      {
        id: "Heading3", name: "Heading 3", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 26, bold: true, italics: true, font: FONT, color: "404040" },
        paragraph: { spacing: { before: 200, after: 120 }, outlineLevel: 2 }
      }
    ]
  },
  numbering: {
    config: [
      {
        reference: "bullets",
        levels: [
          { level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT,
            style: { paragraph: { indent: { left: 720, hanging: 360 } } } }
        ]
      }
    ]
  },
  sections: [{
    properties: {
      page: {
        size: { width: 11906, height: 16838 }, // A4
        margin: { top: 1440, right: 1440, bottom: 1440, left: 1800 }
      }
    },
    headers: {
      default: new Header({
        children: [new Paragraph({
          alignment: AlignmentType.RIGHT,
          children: [new TextRun({ text: "Bài tập lớn HTTTQL nâng cao - VNPT", italics: true, size: 20, font: FONT, color: "808080" })]
        })]
      })
    },
    footers: {
      default: new Footer({
        children: [new Paragraph({
          alignment: AlignmentType.CENTER,
          children: [
            new TextRun({ text: "Trang ", size: 20, font: FONT, color: "808080" }),
            new TextRun({ children: [PageNumber.CURRENT], size: 20, font: FONT, color: "808080" }),
            new TextRun({ text: " / ", size: 20, font: FONT, color: "808080" }),
            new TextRun({ children: [PageNumber.TOTAL_PAGES], size: 20, font: FONT, color: "808080" })
          ]
        })]
      })
    },
    children: [
      ...coverPage,
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 200 }, children: [new TextRun({ text: "MỤC LỤC", bold: true, size: 32, font: FONT })] }),
      new TableOfContents("Mục lục", { hyperlink: true, headingStyleRange: "1-3" }),
      new Paragraph({ children: [new PageBreak()] }),
      ...intro,
      ...cau1,
      ...cau2,
      ...cau3,
      ...cau4,
      ...cau5,
      ...conclusion,
      ...refs
    ]
  }]
});

Packer.toBuffer(doc).then(buffer => {
  const outPath = path.join(__dirname, 'BaiTapLon_HTTTQL_VNPT.docx');
  fs.writeFileSync(outPath, buffer);
  console.log("DONE: " + outPath + " (" + buffer.length + " bytes)");
}).catch(err => {
  console.error("ERROR:", err);
  process.exit(1);
});
