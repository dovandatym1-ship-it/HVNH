const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  Header, Footer, AlignmentType, LevelFormat, ImageRun, NumberFormat,
  TableOfContents, HeadingLevel, BorderStyle, WidthType, ShadingType,
  VerticalAlign, PageNumber, PageBreak, TabStopType, TabStopPosition
} = require("docx");

const FONT = "Times New Roman";
const SZ = 26;        // 13pt
const LINE = 360;     // 1.5 spacing

// ---------- helpers ----------
// Justified body paragraph with first-line indent
function P(text, opts = {}) {
  const runs = Array.isArray(text)
    ? text
    : [new TextRun({ text, italics: opts.italics || false, bold: opts.bold || false })];
  return new Paragraph({
    alignment: opts.align || AlignmentType.JUSTIFIED,
    spacing: { line: LINE, after: opts.after === undefined ? 120 : opts.after, before: opts.before || 0 },
    indent: opts.noIndent ? undefined : { firstLine: 567 },
    children: runs,
  });
}
function center(text, opts = {}) {
  return new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { line: LINE, after: opts.after === undefined ? 120 : opts.after, before: opts.before || 0 },
    children: [new TextRun({ text, bold: opts.bold || false, italics: opts.italics || false,
      size: opts.size || SZ, allCaps: opts.caps || false })],
  });
}
function H1(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_1,
    spacing: { before: 280, after: 160, line: LINE },
    children: [new TextRun({ text })],
  });
}
function H2(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_2,
    spacing: { before: 200, after: 120, line: LINE },
    children: [new TextRun({ text })],
  });
}
function H3(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_3,
    spacing: { before: 160, after: 100, line: LINE },
    children: [new TextRun({ text })],
  });
}
function caption(text) {
  return new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { after: 160, before: 60, line: LINE },
    children: [new TextRun({ text, italics: true, size: 24 })],
  });
}
function img(path, w, h, title) {
  return new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 120, after: 40 },
    children: [new ImageRun({
      type: "png", data: fs.readFileSync(path),
      transformation: { width: w, height: h },
      altText: { title, description: title, name: title },
    })],
  });
}

// ---------- table helper ----------
const bd = { style: BorderStyle.SINGLE, size: 2, color: "888888" };
const borders = { top: bd, bottom: bd, left: bd, right: bd };
function cell(text, w, opts = {}) {
  const runs = (Array.isArray(text) ? text : [text]).map(t =>
    new Paragraph({
      alignment: opts.align || AlignmentType.LEFT,
      spacing: { line: 276, after: 20 },
      children: [new TextRun({ text: t, bold: opts.bold || false, size: 24 })],
    }));
  return new TableCell({
    borders, width: { size: w, type: WidthType.DXA },
    shading: opts.fill ? { fill: opts.fill, type: ShadingType.CLEAR } : undefined,
    margins: { top: 60, bottom: 60, left: 110, right: 110 },
    verticalAlign: VerticalAlign.CENTER,
    children: runs,
  });
}
function table(widths, rows) {
  const total = widths.reduce((a, b) => a + b, 0);
  return new Table({
    width: { size: total, type: WidthType.DXA },
    columnWidths: widths,
    rows: rows.map(r => new TableRow({
      children: r.cells.map((c, i) =>
        cell(c.t, widths[i], { bold: c.bold || r.head, fill: r.head ? "D9E2F3" : c.fill, align: c.align })),
    })),
  });
}

// =====================================================================
//  FRONT MATTER (roman numerals)
// =====================================================================
const front = [];

// --- Cover page ---
front.push(center("HỌC VIỆN CÔNG NGHỆ BƯU CHÍNH VIỄN THÔNG", { bold: true, after: 40 }));
front.push(center("KHOA CÔNG NGHỆ THÔNG TIN", { bold: true, after: 600 }));
front.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 200 },
  children: [new ImageRun({ type: "png", data: fs.readFileSync("hinh_throughput.png"),
    transformation: { width: 1, height: 1 }, altText: { title: "x", description: "x", name: "x" } })] }));
// (remove the dummy image line effect by spacing instead)
front.pop();
front.push(center("", { after: 400 }));
front.push(center("BÀI TIỂU LUẬN", { bold: true, size: 30, after: 120 }));
front.push(center("MÔN: CƠ SỞ DỮ LIỆU NÂNG CAO", { bold: true, size: 28, after: 500 }));
front.push(center("ĐỀ TÀI", { bold: true, after: 60 }));
front.push(center("BLOCKCHAIN VÀ QUẢN LÝ CHUỖI CUNG ỨNG", { bold: true, size: 30, caps: true, after: 100 }));
front.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 600 },
  border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: "2E75B6", space: 6 } }, children: [new TextRun("")] }));
front.push(new Paragraph({
  alignment: AlignmentType.LEFT, spacing: { line: LINE, after: 80 }, indent: { left: 2600 },
  children: [new TextRun({ text: "Giảng viên hướng dẫn:  ......................................", size: SZ })] }));
front.push(new Paragraph({
  alignment: AlignmentType.LEFT, spacing: { line: LINE, after: 80 }, indent: { left: 2600 },
  children: [new TextRun({ text: "Sinh viên thực hiện:    ......................................", size: SZ })] }));
front.push(new Paragraph({
  alignment: AlignmentType.LEFT, spacing: { line: LINE, after: 80 }, indent: { left: 2600 },
  children: [new TextRun({ text: "Mã sinh viên:           ......................................", size: SZ })] }));
front.push(new Paragraph({
  alignment: AlignmentType.LEFT, spacing: { line: LINE, after: 600 }, indent: { left: 2600 },
  children: [new TextRun({ text: "Lớp:                    ......................................", size: SZ })] }));
front.push(center("HÀ NỘI – 2026", { bold: true }));
front.push(new Paragraph({ children: [new PageBreak()] }));

// --- Nhận xét của GVHD ---
front.push(center("NHẬN XÉT CỦA GIẢNG VIÊN HƯỚNG DẪN", { bold: true, after: 240 }));
for (let i = 0; i < 10; i++) {
  front.push(new Paragraph({ spacing: { line: 480 },
    border: { bottom: { style: BorderStyle.DOTTED, size: 4, color: "AAAAAA", space: 4 } },
    children: [new TextRun("")] }));
}
front.push(new Paragraph({ spacing: { before: 200 }, alignment: AlignmentType.RIGHT,
  children: [new TextRun({ text: "Hà Nội, ngày … tháng … năm 2026", italics: true, size: SZ })] }));
front.push(new Paragraph({ alignment: AlignmentType.RIGHT,
  children: [new TextRun({ text: "Giảng viên hướng dẫn", bold: true, size: SZ })] }));
front.push(new Paragraph({ children: [new PageBreak()] }));

// --- Lời cam đoan ---
front.push(center("LỜI CAM ĐOAN", { bold: true, after: 200 }));
front.push(P("Tôi xin cam đoan bài tiểu luận với đề tài “Blockchain và quản lý chuỗi cung ứng” là công trình tìm hiểu và tổng hợp của riêng tôi dưới sự hướng dẫn của giảng viên bộ môn Cơ sở dữ liệu nâng cao. Các số liệu, ví dụ minh chứng và kết quả phân tích được trích dẫn trung thực từ những nguồn tài liệu đã công bố và được liệt kê đầy đủ trong mục Tài liệu tham khảo. Tôi không sao chép nguyên văn từ bất kỳ công trình nào khác mà không ghi rõ nguồn gốc. Nếu phát hiện có sự gian lận, tôi xin hoàn toàn chịu trách nhiệm trước bộ môn và nhà trường."));
front.push(new Paragraph({ spacing: { before: 240 }, alignment: AlignmentType.RIGHT,
  children: [new TextRun({ text: "Sinh viên thực hiện", bold: true, size: SZ })] }));
front.push(new Paragraph({ children: [new PageBreak()] }));

// --- Lời cảm ơn ---
front.push(center("LỜI CẢM ƠN", { bold: true, after: 200 }));
front.push(P("Để hoàn thành bài tiểu luận này, trước hết tôi xin gửi lời cảm ơn chân thành đến giảng viên phụ trách học phần Cơ sở dữ liệu nâng cao. Những bài giảng về hệ quản trị cơ sở dữ liệu phân tán, mô hình giao dịch và các nguyên lý nhất quán dữ liệu đã cho tôi một khung tư duy để nhìn nhận Blockchain không chỉ như một hiện tượng công nghệ, mà như một lựa chọn kiến trúc dữ liệu với những đánh đổi rất cụ thể. Tôi cũng xin cảm ơn các bạn trong nhóm học tập đã cùng trao đổi, phản biện và chia sẻ tài liệu trong quá trình thực hiện. Do kiến thức và thời gian còn hạn chế, bài viết khó tránh khỏi thiếu sót; tôi rất mong nhận được ý kiến đóng góp của thầy/cô để hoàn thiện hơn."));
front.push(new Paragraph({ children: [new PageBreak()] }));

// --- Mục lục ---
front.push(center("MỤC LỤC", { bold: true, after: 160 }));
front.push(new TableOfContents("Mục lục", { hyperlink: true, headingStyleRange: "1-3" }));
front.push(new Paragraph({ children: [new PageBreak()] }));

// --- Danh mục hình & bảng ---
front.push(center("DANH MỤC HÌNH VẼ VÀ BẢNG BIỂU", { bold: true, after: 160 }));
front.push(P("Hình 1. Kiến trúc luồng dữ liệu của Blockchain trong một chuỗi cung ứng điển hình.", { noIndent: true, after: 80 }));
front.push(P("Hình 2. So sánh thông lượng giao dịch (Throughput) giữa Blockchain và cơ sở dữ liệu truyền thống.", { noIndent: true, after: 200 }));
front.push(P("Bảng 1. So sánh Blockchain với RDBMS và NoSQL trên các tiêu chí quản trị dữ liệu.", { noIndent: true, after: 80 }));
front.push(P("Bảng 2. Đối chiếu mô hình nhất quán ACID và BASE trong ngữ cảnh sổ cái phân tán.", { noIndent: true, after: 80 }));
front.push(P("Bảng 3. Tổng hợp một số dự án ứng dụng Blockchain trong chuỗi cung ứng.", { noIndent: true, after: 200 }));
front.push(new Paragraph({ children: [new PageBreak()] }));

// --- Danh mục chữ viết tắt ---
front.push(center("DANH MỤC CHỮ VIẾT TẮT", { bold: true, after: 160 }));
front.push(table([1900, 7300], [
  { head: true, cells: [{ t: "Viết tắt" }, { t: "Diễn giải" }] },
  { cells: [{ t: "ACID", bold: true }, { t: "Atomicity, Consistency, Isolation, Durability – bốn tính chất giao dịch của CSDL truyền thống" }] },
  { cells: [{ t: "BASE", bold: true }, { t: "Basically Available, Soft state, Eventual consistency – mô hình nhất quán nới lỏng" }] },
  { cells: [{ t: "CSDL", bold: true }, { t: "Cơ sở dữ liệu (Database)" }] },
  { cells: [{ t: "DLT", bold: true }, { t: "Distributed Ledger Technology – công nghệ sổ cái phân tán" }] },
  { cells: [{ t: "ERP", bold: true }, { t: "Enterprise Resource Planning – hệ hoạch định nguồn lực doanh nghiệp" }] },
  { cells: [{ t: "PBFT", bold: true }, { t: "Practical Byzantine Fault Tolerance – đồng thuận chịu lỗi Byzantine" }] },
  { cells: [{ t: "PoS", bold: true }, { t: "Proof of Stake – bằng chứng cổ phần" }] },
  { cells: [{ t: "PoW", bold: true }, { t: "Proof of Work – bằng chứng công việc" }] },
  { cells: [{ t: "RDBMS", bold: true }, { t: "Relational Database Management System – hệ quản trị CSDL quan hệ" }] },
  { cells: [{ t: "TPS", bold: true }, { t: "Transactions Per Second – số giao dịch xử lý mỗi giây (thông lượng)" }] },
]));

// =====================================================================
//  MAIN BODY (arabic numerals)
// =====================================================================
const body = [];

// ---- MỞ ĐẦU ----
body.push(H1("MỞ ĐẦU"));
body.push(H2("1. Lý do chọn đề tài"));
body.push(P("Chuỗi cung ứng hiện đại hiếm khi còn là một đường thẳng đơn giản từ nhà sản xuất đến người tiêu dùng. Một hộp sữa, một viên thuốc hay một chiếc điện thoại có thể đi qua hàng chục pháp nhân khác nhau ở nhiều quốc gia: nông trại, nhà chế biến, hãng vận tải, kho ngoại quan, đại lý phân phối, rồi mới đến quầy bán lẻ. Mỗi mắt xích lại lưu trữ dữ liệu trong hệ thống riêng của mình – thường là một cơ sở dữ liệu quan hệ đặt sau một phần mềm ERP. Vấn đề nằm ở chỗ các cơ sở dữ liệu này tách rời nhau, mỗi bên chỉ nắm một mảnh sự thật và không bên nào hoàn toàn tin tưởng dữ liệu của bên còn lại."));
body.push(P("Từ góc nhìn của môn Cơ sở dữ liệu nâng cao, đây thực chất là bài toán kinh điển về tính toàn vẹn (integrity) và nhất quán (consistency) của dữ liệu trên nhiều nguồn phân tán nhưng không có quản trị tập trung đáng tin cậy. Khi xảy ra sự cố – chẳng hạn một lô thực phẩm nhiễm khuẩn – việc truy ngược nguồn gốc qua các CSDL rời rạc có thể mất nhiều ngày, bởi dữ liệu phải được đối chiếu thủ công, và không gì bảo đảm một bản ghi đã không bị sửa lại sau khi sự việc xảy ra. Chính khoảng trống về niềm tin dữ liệu này là mảnh đất mà Blockchain, với tư cách một sổ cái phân tán chống giả mạo, hứa hẹn lấp đầy. Đó là lý do tôi chọn đề tài “Blockchain và quản lý chuỗi cung ứng”, nhưng tiếp cận nó trước hết như một mô hình cơ sở dữ liệu mới chứ không phải như một loại tiền mã hóa."));
body.push(H2("2. Mục đích và phạm vi nghiên cứu"));
body.push(P("Bài viết hướng tới ba mục tiêu. Thứ nhất, làm rõ nguyên lý hoạt động của Blockchain dưới lăng kính hệ quản trị dữ liệu phân tán, thay vì lăng kính tài chính quen thuộc. Thứ hai, phân tích lợi ích và thách thức khi đưa Blockchain vào quản lý chuỗi cung ứng, đặc biệt nhấn mạnh những đánh đổi (trade-off) về hiệu năng và tính nhất quán so với RDBMS và NoSQL. Thứ ba, đối chiếu lý thuyết với một vài trường hợp ứng dụng thực tế để thấy đâu là thành công, đâu là thất bại và vì sao."));
body.push(P("Phạm vi của bài tập trung vào khía cạnh quản trị dữ liệu: cấu trúc lưu trữ, cơ chế đồng thuận, mô hình nhất quán, thông lượng và khả năng mở rộng. Bài không đi sâu vào kinh tế học tiền mã hóa hay chi tiết mật mã học, mà chỉ sử dụng những khái niệm này ở mức cần thiết để giải thích hành vi của hệ thống dữ liệu."));
body.push(H2("3. Kết cấu đề tài"));
body.push(P("Ngoài phần Mở đầu và Kết luận, nội dung chính được chia thành ba chương. Chương 1 trình bày cơ sở lý thuyết: đặc thù dữ liệu của chuỗi cung ứng, hạn chế của CSDL truyền thống và nguyên lý hoạt động của Blockchain. Chương 2 phân tích mô hình ứng dụng, làm rõ lợi ích cùng các thách thức về hiệu năng và tích hợp. Chương 3 khảo sát một số ví dụ thực tế, đề xuất một sơ đồ kiến trúc dữ liệu và đánh giá hiệu quả trước – sau khi áp dụng."));

// ---- CHƯƠNG 1 ----
body.push(new Paragraph({ children: [new PageBreak()] }));
body.push(H1("CHƯƠNG 1. CƠ SỞ LÝ THUYẾT VÀ TỔNG QUAN VẤN ĐỀ"));

body.push(H2("1.1. Khái quát về hệ thống quản lý chuỗi cung ứng"));
body.push(P("Một hệ thống quản lý chuỗi cung ứng, xét cho cùng, là một hệ thống dữ liệu liên tổ chức. Dữ liệu ở đây có vài đặc thù đáng chú ý. Nó mang tính tuần tự và phụ thuộc thời gian: mỗi sự kiện (thu hoạch, đóng gói, vận chuyển, kiểm định) sinh ra một bản ghi gắn với mốc thời gian, và thứ tự các bản ghi mang ý nghĩa nghiệp vụ. Nó mang tính liên kết: một mã lô (lot code) phải nối được với chứng từ vận tải, kết quả kiểm nghiệm, hóa đơn… giống như các khóa ngoại trong lược đồ quan hệ. Và quan trọng nhất, nó mang tính đa chủ thể: không có một “người sở hữu cơ sở dữ liệu” duy nhất, mà mỗi pháp nhân tự quản một phần."));
body.push(P("Trong mô hình truyền thống, mỗi doanh nghiệp vận hành một RDBMS tập trung (Oracle, SQL Server, PostgreSQL…) phía sau hệ ERP. Cách làm này có ưu điểm rõ ràng: lược đồ (schema) chặt chẽ, giao dịch tuân thủ ACID, truy vấn nhanh bằng SQL, và việc kiểm soát phân quyền tương đối đơn giản vì chỉ có một quản trị viên. Tuy nhiên, khi đặt nhiều CSDL tập trung như vậy cạnh nhau trong một chuỗi cung ứng, ba hạn chế lộ ra."));
body.push(P([
  new TextRun({ text: "Thứ nhất là tính cát cứ và sai lệch dữ liệu. ", bold: true, size: SZ }),
  new TextRun({ text: "Vì mỗi bên giữ một bản sao “sự thật” riêng, dữ liệu giữa các hệ thống dễ lệch nhau do nhập liệu thủ công, do định dạng khác biệt hoặc đơn giản vì độ trễ đồng bộ. Việc đối soát trở thành một quy trình tốn kém.", size: SZ }),
]));
body.push(P([
  new TextRun({ text: "Thứ hai là khả năng bị can thiệp. ", bold: true, size: SZ }),
  new TextRun({ text: "Một bản ghi trong RDBMS hoàn toàn có thể bị UPDATE hoặc DELETE bởi người có đủ quyền, và nếu không bật cơ chế nhật ký kiểm toán (audit log) đầy đủ thì gần như không còn dấu vết. Trong các tình huống cần quy trách nhiệm – ai đã sửa nhiệt độ bảo quản của lô vắc-xin? – đặc tính “dễ sửa” này lại trở thành điểm yếu.", size: SZ }),
]));
body.push(P([
  new TextRun({ text: "Thứ ba là khó truy xuất nguồn gốc xuyên tổ chức. ", bold: true, size: SZ }),
  new TextRun({ text: "Do không có lược đồ chung và không bên nào được phép truy vấn trực tiếp CSDL của bên khác, việc lần theo lịch sử một sản phẩm đòi hỏi gửi yêu cầu, chờ phản hồi và ghép nối thủ công qua nhiều ranh giới doanh nghiệp.", size: SZ }),
]));
body.push(P("Những hạn chế này không phải do RDBMS kém, mà do mô hình tập trung không phù hợp với một bài toán vốn dĩ phân tán và thiếu niềm tin lẫn nhau. Đây chính là điểm khởi đầu để xem xét Blockchain như một kiến trúc dữ liệu thay thế."));

body.push(H2("1.2. Tổng quan về cơ sở dữ liệu Blockchain"));
body.push(H3("1.2.1. Định nghĩa dưới góc nhìn hệ quản trị dữ liệu"));
body.push(P("Nếu gạt bỏ lớp vỏ tiền mã hóa, Blockchain có thể được định nghĩa là một cơ sở dữ liệu phân tán chỉ-ghi-thêm (append-only), được nhân bản (replicated) trên nhiều nút (node) ngang hàng, trong đó các bản ghi được nhóm thành khối (block) và liên kết với nhau bằng hàm băm mật mã, còn việc thống nhất trạng thái chung giữa các nút được bảo đảm bởi một giao thức đồng thuận thay cho một máy chủ trung tâm. Nói cách khác, nó là một sổ cái phân tán (Distributed Ledger) mà mọi nút đều giữ một bản sao đầy đủ và logic gần như giống hệt nhau."));
body.push(P("So sánh với mô hình nhân bản của RDBMS giúp thấy rõ sự khác biệt. Trong RDBMS phân tán, ta cũng có replication, nhưng thường theo kiểu chủ – tớ (master–slave): một nút chủ quyết định thứ tự ghi, các nút tớ chép lại. Niềm tin được đặt vào nút chủ. Blockchain thì giả định ngược lại – rằng một số nút có thể gian lận hoặc hỏng – nên không trao quyền quyết định cho bất kỳ nút riêng lẻ nào, mà để cả mạng cùng “bỏ phiếu” theo giao thức đồng thuận. Đây là sự dịch chuyển từ niềm tin vào chủ thể sang niềm tin vào giao thức."));

body.push(H3("1.2.2. Nguyên lý hoạt động cơ bản"));
body.push(P("Vòng đời của một giao dịch trên Blockchain có thể tóm gọn qua bốn bước. (i) Một nút khởi tạo giao dịch – ví dụ “lô hàng X rời kho Y lúc Z” – và ký số bằng khóa riêng của mình. (ii) Giao dịch được phát tán tới các nút khác và đưa vào vùng chờ. (iii) Theo cơ chế đồng thuận, một (hoặc một nhóm) nút gom các giao dịch hợp lệ thành một khối mới; khối này chứa giá trị băm của khối liền trước, tạo thành chuỗi liên kết. (iv) Khối được nhân bản về mọi nút và trở thành một phần bất biến của sổ cái."));
body.push(P("Ba thành phần cốt lõi đỡ lấy cơ chế trên. Mạng lưới phi tập trung (peer-to-peer) loại bỏ điểm chết đơn lẻ (single point of failure): không nút nào là không thể thay thế. Liên kết băm theo kiểu cây Merkle khiến mọi thay đổi dù nhỏ ở một bản ghi cũ cũng làm sai lệch toàn bộ chuỗi băm phía sau, nhờ đó hệ thống tự phát hiện được giả mạo. Và cơ chế đồng thuận – Proof of Work, Proof of Stake với mạng công khai, hay PBFT/Raft với mạng cấp phép – quyết định nút nào được quyền ghi khối tiếp theo và làm sao để mọi bản sao hội tụ về cùng một trạng thái. Chính lựa chọn cơ chế đồng thuận sẽ chi phối phần lớn hiệu năng và độ trễ mà ta phân tích ở Chương 2."));

body.push(H3("1.2.3. Các đặc điểm cốt lõi từ góc độ dữ liệu"));
body.push(P([
  new TextRun({ text: "Tính chống giả mạo (tamper-resistance). ", bold: true, size: SZ }),
  new TextRun({ text: "Đây là đặc điểm có ý nghĩa nhất với quản trị dữ liệu. Vì mỗi khối khóa chặt vào khối trước bằng hàm băm và dữ liệu được nhân bản trên nhiều nút, muốn sửa một bản ghi cũ kẻ tấn công phải tính lại toàn bộ chuỗi băm phía sau trên đa số nút cùng lúc – điều gần như bất khả thi trong một mạng đủ lớn. So với một dòng UPDATE âm thầm trong RDBMS, đây là một bảo đảm toàn vẹn ở cấp độ kiến trúc.", size: SZ }),
]));
body.push(P([
  new TextRun({ text: "Tính không thể chối bỏ (non-repudiation). ", bold: true, size: SZ }),
  new TextRun({ text: "Mỗi giao dịch được ký số, nên chủ thể đã ghi không thể phủ nhận hành động của mình. Trong chuỗi cung ứng, điều này gắn liền trách nhiệm với từng mắt xích – một thứ mà nhật ký của CSDL tập trung khó cung cấp một cách đáng tin cho các bên đối tác.", size: SZ }),
]));
body.push(P([
  new TextRun({ text: "Tính ẩn danh / bút danh (pseudonymity). ", bold: true, size: SZ }),
  new TextRun({ text: "Các bên tham gia được nhận diện qua địa chỉ khóa công khai thay vì danh tính thật. Đặc điểm này hữu ích khi cần bảo mật quan hệ thương mại, song trong mạng cấp phép phục vụ doanh nghiệp, người ta thường gắn lại bút danh với pháp nhân thực để phục vụ kiểm toán.", size: SZ }),
]));
body.push(P([
  new TextRun({ text: "Hợp đồng thông minh (smart contract). ", bold: true, size: SZ }),
  new TextRun({ text: "Đây là phần “logic” chạy ngay trên sổ cái, tương tự stored procedure hoặc trigger trong RDBMS, nhưng được thực thi đồng thời và nhất quán trên mọi nút. Nhờ đó các quy tắc nghiệp vụ – ví dụ “tự động thanh toán khi cảm biến xác nhận hàng đã giao đúng nhiệt độ” – được thực thi tự động mà không cần một bên trung gian đứng ra đảm bảo.", size: SZ }),
]));
body.push(P("Bốn đặc điểm này cùng nhau biến Blockchain thành một loại CSDL mà điểm mạnh không nằm ở tốc độ hay sự linh hoạt của lược đồ, mà nằm ở khả năng tạo ra một “sự thật chung” đáng tin giữa các bên không tin nhau. Đó cũng chính là tiền đề để Chương 2 bàn về việc đặc điểm ấy đem lại lợi ích gì cho chuỗi cung ứng và phải trả giá bằng những đánh đổi nào."));

// ---- CHƯƠNG 2 ----
body.push(new Paragraph({ children: [new PageBreak()] }));
body.push(H1("CHƯƠNG 2. ỨNG DỤNG BLOCKCHAIN TRONG CHUỖI CUNG ỨNG – LỢI ÍCH VÀ THÁCH THỨC"));

body.push(H2("2.1. Mô hình Blockchain trong chuỗi cung ứng"));
body.push(P("Điểm thay đổi căn bản khi áp dụng Blockchain nằm ở luồng dữ liệu (data flow). Trong mô hình cũ, dữ liệu của mỗi mắt xích chảy về CSDL riêng rồi được trao đổi qua các kết nối điểm-điểm hoặc qua một máy chủ trung gian (EDI, cổng tích hợp). Trong mô hình Blockchain, mỗi mắt xích ghi sự kiện trực tiếp lên sổ cái chung, và bản ghi ấy lập tức được nhân bản tới mọi nút. Không còn “bản sao của tôi” và “bản sao của anh” lệch nhau, mà chỉ còn một sổ cái duy nhất mà tất cả cùng nhìn thấy và không ai sửa lén được."));
body.push(P("Trong thực tế triển khai cho doanh nghiệp, người ta hầu như luôn dùng Blockchain cấp phép (permissioned), tiêu biểu là Hyperledger Fabric, thay vì mạng công khai như Bitcoin hay Ethereum. Lý do thuần túy là về quản trị dữ liệu: mạng cấp phép cho phép kiểm soát ai được tham gia, phân quyền đọc/ghi theo vai trò, dùng cơ chế đồng thuận nhẹ hơn (như Raft) nên đạt thông lượng cao hơn nhiều, và bảo vệ được dữ liệu thương mại nhạy cảm. Có thể nói mạng cấp phép là nỗ lực giữ lại tính chống giả mạo của Blockchain trong khi mượn lại sự kiểm soát và hiệu năng vốn là thế mạnh của CSDL doanh nghiệp."));

body.push(H2("2.2. Các lợi ích mang lại"));
body.push(H3("2.2.1. Truy xuất nguồn gốc minh bạch (Data Provenance)"));
body.push(P("Vì toàn bộ lịch sử của một sản phẩm được ghi tuần tự và bất biến trên cùng một sổ cái, việc truy ngược nguồn gốc trở thành một thao tác đọc dữ liệu đơn giản thay vì một cuộc điều tra liên tổ chức. Đây là lợi ích được chứng minh rõ nhất trên thực tế: trong thử nghiệm của Walmart và IBM, thời gian truy vết nguồn gốc một lô xoài giảm từ khoảng bảy ngày xuống còn 2,2 giây. Con số ấy không phản ánh “Blockchain nhanh hơn”, mà phản ánh việc dữ liệu vốn nằm rải rác ở nhiều CSDL nay đã được hợp nhất về một nơi có thể truy vấn tức thì."));
body.push(H3("2.2.2. Tính toàn vẹn của dữ liệu (Data Integrity)"));
body.push(P("Như đã phân tích ở Chương 1, liên kết băm và nhân bản đa nút khiến mỗi bản ghi gần như không thể bị sửa sau khi đã ghi. Trong chuỗi cung ứng dược phẩm hay thực phẩm, điều này nâng chuẩn niềm tin: một kết quả kiểm nghiệm hay một mốc nhiệt độ, một khi đã lên sổ cái, sẽ tồn tại như một bằng chứng không thể chỉnh sửa âm thầm. So với RDBMS, nơi tính toàn vẹn phụ thuộc vào kỷ luật vận hành và quyền hạn của quản trị viên, ở Blockchain tính toàn vẹn được bảo đảm bởi chính cấu trúc dữ liệu."));
body.push(H3("2.2.3. Tự động hóa giao dịch qua Smart Contract"));
body.push(P("Hợp đồng thông minh cho phép số hóa các điều khoản thương mại và để chúng tự thực thi khi điều kiện được thỏa mãn. Chẳng hạn, một smart contract có thể tự động giải ngân cho nhà cung cấp ngay khi cảm biến IoT xác nhận container đã cập cảng đúng hạn và đủ điều kiện bảo quản. Việc này rút ngắn chu trình thanh toán, giảm tranh chấp và loại bớt khâu trung gian – một dạng tự động hóa quy trình mà nếu làm bằng nhiều CSDL tách rời sẽ cần một lớp điều phối phức tạp và vẫn phụ thuộc vào niềm tin giữa các bên."));

body.push(H2("2.3. Các thách thức và giới hạn"));
body.push(P("Phần này là trọng tâm dưới góc độ Cơ sở dữ liệu nâng cao, vì mọi lợi ích nêu trên đều phải trả giá. Định lý CAP nhắc rằng một hệ phân tán không thể đồng thời tối đa hóa nhất quán (Consistency), sẵn sàng (Availability) và chịu phân vùng (Partition tolerance). Blockchain công khai chọn nghiêng về nhất quán và chịu phân vùng, và cái giá phải trả lộ ra ở hiệu năng."));
body.push(H3("2.3.1. Thông lượng và khả năng mở rộng (Throughput & Scalability)"));
body.push(P("Đây là điểm yếu cố hữu. Vì mọi nút phải lưu và xác thực lại cùng một dữ liệu, năng lực của cả mạng bị kéo về ngang với một nút đơn lẻ – trái ngược với triết lý phân mảnh (sharding) để tăng quy mô của NoSQL. Hệ quả là thông lượng rất thấp: Bitcoin xử lý khoảng 7 giao dịch mỗi giây, Ethereum công khai vào khoảng vài chục TPS, trong khi một RDBMS như PostgreSQL hay một hệ Visa có thể xử lý hàng chục nghìn TPS. Hình 2 minh họa khoảng cách này (lưu ý trục tung theo thang logarit)."));
body.push(img("hinh_throughput.png", 560, 286, "So sánh throughput"));
body.push(caption("Hình 2. So sánh thông lượng giao dịch giữa Blockchain và CSDL truyền thống (thang log)."));
body.push(P("Mạng cấp phép cải thiện đáng kể tình hình: Hyperledger Fabric có thể đạt vài nghìn TPS trong cấu hình thông thường, và các nghiên cứu tối ưu (FastFabric) đẩy con số lên tới gần 20.000 TPS. Tuy vậy, ngay cả khi đó, đặc tính “mọi nút cùng lưu mọi thứ” vẫn đặt ra trần mở rộng theo chiều ngang khó vượt qua như cách NoSQL phân mảnh dữ liệu ra nhiều cụm độc lập."));
body.push(H3("2.3.2. Độ trễ trong xử lý giao dịch (Latency)"));
body.push(P("Bên cạnh thông lượng là độ trễ tới khi giao dịch được coi là “chốt” (finality). Với cơ chế PoW, một giao dịch Bitcoin chỉ thực sự an toàn sau khoảng sáu khối, tức gần một giờ. Độ trễ này đến từ bản chất của đồng thuận xác suất và từ việc phải chờ nhân bản trên toàn mạng. Với chuỗi cung ứng, độ trễ vài giây tới vài phút của mạng cấp phép thường chấp nhận được vì các sự kiện logistics không đòi hỏi phản hồi mili-giây; nhưng nó vẫn là một bước lùi so với độ trễ dưới mili-giây của một truy vấn RDBMS được đánh chỉ mục tốt."));
body.push(H3("2.3.3. Chi phí lưu trữ và tích hợp với hệ thống cũ (Legacy)"));
body.push(P("Vì dữ liệu được nhân bản toàn phần trên mọi nút, chi phí lưu trữ tăng tuyến tính theo số nút – một sự lãng phí dung lượng mà các kiến trúc CSDL truyền thống tránh được nhờ chuẩn hóa và phân mảnh. Đây là lý do trong thực tế người ta thường chỉ đưa lên chuỗi phần dữ liệu cốt lõi và giá trị băm (on-chain), còn dữ liệu lớn như hình ảnh, chứng từ thì lưu ngoài chuỗi (off-chain) rồi neo bằng hàm băm. Thách thức lớn không kém là tích hợp: doanh nghiệp đã đầu tư hàng chục năm vào ERP và RDBMS, nên Blockchain hiếm khi thay thế hoàn toàn mà phải sống chung qua các lớp trung gian (oracle, API), kéo theo bài toán đồng bộ và ánh xạ lược đồ giữa hai thế giới dữ liệu."));

body.push(H3("2.3.4. So sánh tổng hợp với RDBMS và NoSQL"));
body.push(P("Để hệ thống hóa, Bảng 1 đối chiếu Blockchain với RDBMS và NoSQL trên các tiêu chí quản trị dữ liệu chủ chốt."));
body.push(table([2300, 2350, 2350, 2350], [
  { head: true, cells: [{ t: "Tiêu chí" }, { t: "RDBMS (SQL)" }, { t: "NoSQL" }, { t: "Blockchain" }] },
  { cells: [{ t: "Mô hình lưu trữ", bold: true }, { t: "Bảng quan hệ, schema cứng" }, { t: "Document/Key-Value/Graph, schema linh hoạt" }, { t: "Chuỗi khối liên kết băm, append-only" }] },
  { cells: [{ t: "Quản trị", bold: true }, { t: "Tập trung, 1 admin" }, { t: "Tập trung/cụm phân tán" }, { t: "Phi tập trung, đa chủ thể" }] },
  { cells: [{ t: "Thao tác ghi", bold: true }, { t: "CRUD đầy đủ" }, { t: "CRUD đầy đủ" }, { t: "Chỉ ghi thêm (không sửa/xóa)" }] },
  { cells: [{ t: "Nhất quán", bold: true }, { t: "Mạnh (ACID)" }, { t: "Thường là eventual (BASE)" }, { t: "Theo đồng thuận, hội tụ dần" }] },
  { cells: [{ t: "Throughput", bold: true }, { t: "Rất cao (vạn TPS)" }, { t: "Rất cao, mở rộng ngang" }, { t: "Thấp–trung bình (7→vài nghìn TPS)" }] },
  { cells: [{ t: "Chống giả mạo", bold: true }, { t: "Phụ thuộc phân quyền" }, { t: "Phụ thuộc phân quyền" }, { t: "Cao, ở cấp kiến trúc" }] },
  { cells: [{ t: "Mở rộng quy mô", bold: true }, { t: "Theo chiều dọc là chính" }, { t: "Sharding theo chiều ngang" }, { t: "Hạn chế (mọi nút lưu mọi thứ)" }] },
]));
body.push(caption("Bảng 1. So sánh Blockchain với RDBMS và NoSQL trên các tiêu chí quản trị dữ liệu."));
body.push(P("Bảng 2 đi sâu hơn vào trục nhất quán, đối chiếu hai triết lý ACID và BASE để định vị Blockchain. Có thể coi Blockchain công khai là một biến thể đặc biệt: nó hướng tới nhất quán mạnh về cuối (mọi nút cuối cùng đồng ý về một lịch sử duy nhất) nhưng đạt được điều đó một cách dần dần qua đồng thuận, nên về cảm nhận vận hành lại gần với “eventual consistency” của BASE hơn là sự tức thời của ACID."));
body.push(table([3100, 3100, 3150], [
  { head: true, cells: [{ t: "Khía cạnh" }, { t: "ACID (RDBMS)" }, { t: "BASE (NoSQL/Blockchain)" }] },
  { cells: [{ t: "Ưu tiên", bold: true }, { t: "Nhất quán tức thời" }, { t: "Sẵn sàng & chịu phân vùng" }] },
  { cells: [{ t: "Trạng thái", bold: true }, { t: "Luôn hợp lệ sau mỗi giao dịch" }, { t: "Có thể tạm “mềm”, hội tụ dần" }] },
  { cells: [{ t: "Phù hợp", bold: true }, { t: "Giao dịch tài chính nội bộ" }, { t: "Hệ phân tán quy mô lớn, đa chủ thể" }] },
  { cells: [{ t: "Đánh đổi", bold: true }, { t: "Khó mở rộng ngang" }, { t: "Lập trình viên phải chấp nhận độ trễ nhất quán" }] },
]));
body.push(caption("Bảng 2. Đối chiếu mô hình nhất quán ACID và BASE trong ngữ cảnh sổ cái phân tán."));
body.push(P("Tóm lại, Blockchain không phải là “CSDL tốt hơn” một cách phổ quát. Nó là một đánh đổi rất có chủ đích: hy sinh thông lượng, độ trễ và hiệu quả lưu trữ để đổi lấy tính toàn vẹn và niềm tin không cần trung gian. Lựa chọn dùng hay không, vì thế, phải xuất phát từ việc bài toán có thực sự cần đến niềm tin phân tán hay không."));

// ---- CHƯƠNG 3 ----
body.push(new Paragraph({ children: [new PageBreak()] }));
body.push(H1("CHƯƠNG 3. VÍ DỤ THỰC TẾ VÀ MÔ PHỎNG"));

body.push(H2("3.1. Phân tích một số case study thực tế"));
body.push(H3("3.1.1. Walmart – IBM Food Trust (Hyperledger Fabric)"));
body.push(P("Walmart phối hợp với IBM xây dựng nền tảng truy xuất nguồn gốc thực phẩm trên Hyperledger Fabric, qua hai thử nghiệm tiêu biểu: truy vết xoài tại Mỹ và thịt lợn tại Trung Quốc. Kết quả nổi bật nhất là thời gian truy xuất nguồn gốc một lô xoài giảm từ khoảng bảy ngày xuống còn 2,2 giây. Sau giai đoạn thử nghiệm, hệ thống được mở rộng cho hơn 25 dòng sản phẩm từ nhiều nhà cung cấp. Dưới góc độ dữ liệu, thành công ở đây đến từ việc thay nhiều CSDL rời rạc bằng một sổ cái chung được nhân bản, biến một quy trình đối soát liên tổ chức thành một truy vấn đọc tức thời."));
body.push(H3("3.1.2. De Beers – Tracr (truy xuất nguồn gốc kim cương)"));
body.push(P("Tracr là nền tảng Blockchain do De Beers phát triển nhằm tạo bản ghi xuất xứ chống giả mạo cho từng viên kim cương, giúp khẳng định nguồn gốc và loại trừ kim cương xung đột. Tính tới năm 2024, gần ba triệu viên kim cương đã được đăng ký trên Tracr, và nền tảng hỗ trợ truy xuất nguồn gốc tới từng quốc gia khai thác cho các viên trên một carat. Đây là ví dụ cho thấy đặc tính non-repudiation và chống giả mạo của Blockchain phát huy giá trị cao nhất khi tài sản có giá trị lớn và nguồn gốc là yếu tố sống còn."));
body.push(H3("3.1.3. Maersk – IBM TradeLens: một thất bại đáng học hỏi"));
body.push(P("Không phải dự án nào cũng thành công. TradeLens, nền tảng số hóa thương mại toàn cầu trên nền Blockchain do Maersk và IBM khởi xướng năm 2018, đã bị đóng cửa vào đầu năm 2023 vì không đạt được mức độ hợp tác toàn ngành cần thiết để duy trì như một doanh nghiệp độc lập. Bài học ở đây mang đậm màu sắc quản trị dữ liệu: giá trị của một sổ cái dùng chung tỉ lệ thuận với số lượng bên cùng ghi vào nó. Khi các đối thủ cạnh tranh ngần ngại đặt dữ liệu của mình lên một nền tảng do một hãng vận tải kiểm soát, hiệu ứng mạng không hình thành, và lợi thế “một sự thật chung” cũng tan biến. Công nghệ không phải là điểm yếu; vấn đề là mô hình quản trị và niềm tin giữa các bên."));
body.push(P("Bảng 3 tổng hợp ba trường hợp trên để dễ đối chiếu."));
body.push(table([1900, 2050, 2450, 2950], [
  { head: true, cells: [{ t: "Dự án" }, { t: "Nền tảng" }, { t: "Lĩnh vực" }, { t: "Kết quả" }] },
  { cells: [{ t: "Food Trust", bold: true }, { t: "Hyperledger Fabric" }, { t: "Thực phẩm" }, { t: "Truy vết 7 ngày → 2,2 giây; mở rộng 25+ sản phẩm" }] },
  { cells: [{ t: "Tracr", bold: true }, { t: "Blockchain riêng" }, { t: "Kim cương" }, { t: "~3 triệu viên được đăng ký (2024)" }] },
  { cells: [{ t: "TradeLens", bold: true }, { t: "Hyperledger Fabric" }, { t: "Vận tải biển" }, { t: "Đóng cửa 2023 do thiếu hợp tác toàn ngành" }] },
]));
body.push(caption("Bảng 3. Tổng hợp một số dự án ứng dụng Blockchain trong chuỗi cung ứng."));

body.push(H2("3.2. Mô hình hóa kiến trúc đề xuất"));
body.push(P("Để hình dung luồng dữ liệu, Hình 1 mô tả một kiến trúc tham chiếu áp dụng Blockchain cho chuỗi cung ứng nông sản hoặc dược phẩm. Bốn mắt xích – nông trại, nhà chế biến, đơn vị logistics và nhà bán lẻ – vừa trao đổi hàng hóa theo luồng vật lý, vừa ghi các sự kiện tương ứng (giao dịch) xuống một sổ cái phân tán chung."));
body.push(img("hinh_kientruc.png", 600, 339, "Kiến trúc luồng dữ liệu"));
body.push(caption("Hình 1. Kiến trúc luồng dữ liệu của Blockchain trong một chuỗi cung ứng điển hình."));
body.push(P("Trong sơ đồ, sổ cái không nằm trên một máy chủ trung tâm mà được nhân bản (replication) trên nhiều nút thuộc các bên khác nhau; cơ chế đồng thuận giữ cho mọi bản sao hội tụ về cùng một trạng thái. Các khối được móc nối bằng giá trị băm, nên mọi nỗ lực sửa một sự kiện cũ sẽ phá vỡ chuỗi và bị phát hiện. Hợp đồng thông minh đóng vai trò lớp logic, tự động kích hoạt các hành động như thanh toán hay cảnh báo khi một điều kiện trên sổ cái được thỏa mãn. So với kiến trúc cũ nơi mỗi bên ghi vào CSDL riêng rồi đồng bộ qua trung gian, điểm khác biệt cốt lõi là toàn bộ dữ liệu sự kiện cùng tồn tại trên một sổ cái dùng chung, bất biến và minh bạch với mọi bên được cấp quyền."));

body.push(H2("3.3. Đánh giá hiệu quả trước và sau khi áp dụng"));
body.push(P("Đặt mô hình truyền thống và mô hình Blockchain cạnh nhau, có thể rút ra một vài nhận định về mặt quản trị dữ liệu. Về truy xuất nguồn gốc, thời gian từ hàng ngày rút xuống còn vài giây, vì dữ liệu không còn phải ghép nối thủ công qua nhiều CSDL. Về tính toàn vẹn, niềm tin chuyển từ chỗ phụ thuộc thiện chí và quyền hạn của từng quản trị viên sang chỗ được bảo đảm bởi cấu trúc băm và nhân bản – nghĩa là “tin vào hệ thống” thay vì “tin vào con người”. Về quy trình, smart contract thay thế nhiều khâu đối soát và trung gian thủ công."));
body.push(P("Tuy nhiên, đánh giá sẽ phiến diện nếu bỏ qua chi phí. Doanh nghiệp đổi lấy những lợi ích trên bằng thông lượng thấp hơn, độ trễ cao hơn, chi phí lưu trữ và vận hành nút lớn hơn, cùng gánh nặng tích hợp với hệ thống cũ. Bài học từ TradeLens còn cho thấy một chi phí phi kỹ thuật: cần đạt được sự đồng thuận tham gia của đủ nhiều bên thì giá trị mạng mới hình thành. Vì vậy, kết luận hợp lý không phải “Blockchain luôn tốt hơn”, mà là Blockchain phù hợp cho những chuỗi cung ứng nơi truy xuất nguồn gốc và chống giả mạo có giá trị đủ lớn để bù lại cái giá về hiệu năng – ví dụ dược phẩm, thực phẩm an toàn hay hàng hóa giá trị cao – trong khi với các nghiệp vụ cần thông lượng cực lớn và độ trễ thấp, RDBMS hay NoSQL vẫn là lựa chọn hợp lý hơn."));

// ---- KẾT LUẬN ----
body.push(new Paragraph({ children: [new PageBreak()] }));
body.push(H1("KẾT LUẬN"));
body.push(P("Xuyên suốt bài viết, Blockchain được nhìn nhận không phải như một loại tiền mã hóa mà như một kiến trúc cơ sở dữ liệu phân tán với những đặc tính riêng: append-only, nhân bản đa nút, liên kết băm chống giả mạo và đồng thuận thay cho quản trị tập trung. Chính những đặc tính đó giải quyết được điểm yếu cố hữu của mô hình nhiều CSDL tập trung rời rạc trong chuỗi cung ứng – sự cát cứ dữ liệu, nguy cơ bị sửa đổi và khó truy xuất nguồn gốc – bằng cách tạo ra một “sự thật chung” đáng tin giữa các bên không tin nhau."));
body.push(P("Song song với lợi ích là những đánh đổi không thể bỏ qua, và đây là điều quan trọng nhất dưới góc độ Cơ sở dữ liệu nâng cao. So với RDBMS và NoSQL, Blockchain thua thiệt rõ rệt về thông lượng, độ trễ, hiệu quả lưu trữ và khả năng mở rộng ngang. Các ví dụ thực tế – Food Trust, Tracr và cả thất bại của TradeLens – cho thấy công nghệ chỉ phát huy giá trị khi bài toán thực sự cần đến niềm tin phân tán và khi đủ nhiều bên cùng tham gia."));
body.push(P("Hướng phát triển trong tương lai nhiều khả năng không phải là thay thế hoàn toàn các hệ quản trị dữ liệu hiện hành, mà là kiến trúc lai (hybrid): kết hợp dữ liệu off-chain trên RDBMS/NoSQL cho khối lượng lớn với neo băm on-chain cho phần cần bất biến, cùng với các giải pháp mở rộng (Layer-2, sharding cho Blockchain) nhằm thu hẹp khoảng cách hiệu năng. Trong viễn cảnh đó, hiểu Blockchain như một công cụ trong hộp công cụ dữ liệu – với điểm mạnh và đánh đổi rõ ràng – sẽ hữu ích hơn nhiều so với việc xem nó như một giải pháp vạn năng."));

// ---- TÀI LIỆU THAM KHẢO ----
body.push(new Paragraph({ children: [new PageBreak()] }));
body.push(H1("TÀI LIỆU THAM KHẢO"));
const refs = [
  "Antonopoulos, A. M., Mastering Bitcoin: Programming the Open Blockchain, O’Reilly Media, 2017.",
  "Casino, F., Dasaklis, T. K., Patsakis, C., “A systematic literature review of blockchain-based applications”, Telematics and Informatics, 2019.",
  "De Beers Group, Tracr: Blockchain Diamond Provenance Platform – Báo cáo phát triển bền vững, 2024.",
  "Kamath, R., “Food Traceability on Blockchain: Walmart’s Pork and Mango Pilots with IBM”, The Journal of the British Blockchain Association, 2018.",
  "A.P. Moller – Maersk & IBM, Discontinuation of the TradeLens Platform – Thông cáo, 2022.",
  "Nakamoto, S., Bitcoin: A Peer-to-Peer Electronic Cash System, 2008.",
  "Nasir, Q. và cộng sự, “Performance Analysis of Hyperledger Fabric Platforms”, Security and Communication Networks, 2018.",
  "Nguyễn Đình Thọ, Phương pháp nghiên cứu khoa học trong kinh doanh, NXB Tài chính, 2013.",
  "Tapscott, D., Tapscott, A., Blockchain Revolution, Penguin, 2016.",
  "Wood, G., Ethereum: A Secure Decentralised Generalised Transaction Ledger (Yellow Paper), 2014.",
  "Xu, X., Weber, I., Staples, M., Architecture for Blockchain Applications, Springer, 2019.",
];
refs.forEach((r, i) => {
  body.push(new Paragraph({
    alignment: AlignmentType.JUSTIFIED,
    spacing: { line: LINE, after: 100 },
    indent: { left: 567, hanging: 567 },
    children: [new TextRun({ text: `[${i + 1}] ${r}`, size: SZ })],
  }));
});

// =====================================================================
//  DOCUMENT
// =====================================================================
const doc = new Document({
  styles: {
    default: { document: { run: { font: FONT, size: SZ } } },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 30, bold: true, font: FONT, color: "1F3864", allCaps: true },
        paragraph: { spacing: { before: 280, after: 160, line: LINE }, outlineLevel: 0 } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 27, bold: true, font: FONT, color: "2E5496" },
        paragraph: { spacing: { before: 200, after: 120, line: LINE }, outlineLevel: 1 } },
      { id: "Heading3", name: "Heading 3", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 26, bold: true, italics: true, font: FONT, color: "2E5496" },
        paragraph: { spacing: { before: 160, after: 100, line: LINE }, outlineLevel: 2 } },
    ],
  },
  sections: [
    {
      properties: {
        page: {
          size: { width: 12240, height: 15840 },
          margin: { top: 1440, right: 1440, bottom: 1440, left: 1701 },
          pageNumbers: { start: 1, formatType: NumberFormat.LOWER_ROMAN },
        },
      },
      footers: {
        default: new Footer({ children: [new Paragraph({
          alignment: AlignmentType.CENTER,
          children: [new TextRun({ children: [PageNumber.CURRENT], size: 22 })] })] }),
      },
      children: front,
    },
    {
      properties: {
        page: {
          size: { width: 12240, height: 15840 },
          margin: { top: 1440, right: 1440, bottom: 1440, left: 1701 },
          pageNumbers: { start: 1, formatType: NumberFormat.DECIMAL },
        },
      },
      headers: {
        default: new Header({ children: [new Paragraph({
          alignment: AlignmentType.RIGHT,
          border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: "BBBBBB", space: 2 } },
          children: [new TextRun({ text: "Blockchain và quản lý chuỗi cung ứng", italics: true, size: 20, color: "666666" })] })] }),
      },
      footers: {
        default: new Footer({ children: [new Paragraph({
          alignment: AlignmentType.CENTER,
          children: [new TextRun({ text: "Trang ", size: 22 }), new TextRun({ children: [PageNumber.CURRENT], size: 22 })] })] }),
      },
      children: body,
    },
  ],
});

Packer.toBuffer(doc).then(buffer => {
  fs.writeFileSync("Tieu_luan_Blockchain_chuoi_cung_ung.docx", buffer);
  console.log("DOCX written");
});
