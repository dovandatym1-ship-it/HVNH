// ================================================================
// CHƯƠNG 4 + KẾT LUẬN
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

function buildChapter4AndConclusion() {
  const c = [];

  // ─── CHƯƠNG 4 ───
  c.push(
    new Paragraph({ children: [new PageBreak()] }),
    h1("CHƯƠNG 4: XÂY DỰNG CHÍNH SÁCH QUẢN LÝ, TUÂN THỦ VÀ ĐẠO ĐỨC AN TOÀN THÔNG TIN"),
    blank(),
    p([t("Các giải pháp kỹ thuật được đề xuất trong Chương 3, dù tinh vi đến đâu, cũng chỉ là một trong ba trụ cột của kiến trúc bảo mật toàn diện theo mô hình "), tb("People – Process – Technology"), t(". Một hệ thống với tường lửa thế hệ mới và mã hóa mạnh nhất vẫn có thể bị phá vỡ bởi một nhân viên thiếu ý thức bảo mật, một quy trình quản lý thay đổi lỏng lẻo, hoặc sự tuân thủ pháp luật không đầy đủ. Chương 4 tập trung vào hai trụ cột còn lại: "), tb("Quy trình (Process)"), t(" thông qua ISMS và DevSecOps, và "), tb("Con người (People)"), t(" thông qua quản trị, đạo đức và đào tạo.")]),
    blank(),

    h2("4.1. Hệ thống Quản lý An toàn thông tin (ISMS) theo chuẩn ISO/IEC 27001"),
    blank(),
    h3("4.1.1. Chu trình PDCA – Khung quản lý ATTT liên tục"),
    p([t("ISO/IEC 27001 là tiêu chuẩn quốc tế được công nhận rộng rãi nhất về quản lý ATTT doanh nghiệp, cung cấp một framework có hệ thống để thiết lập, triển khai, vận hành, giám sát, xem xét, duy trì và cải tiến liên tục Hệ thống Quản lý An toàn thông tin (Information Security Management System – ISMS). Trái tim của ISO 27001 là chu trình "), tb("PDCA (Plan – Do – Check – Act)"), t(" – một vòng lặp cải tiến không ngừng được áp dụng vào toàn bộ quy trình quản lý ATTT:")]),
    blank(),
    p([tb("PLAN (Lập kế hoạch):"), t(" Xác định phạm vi ISMS, thực hiện đánh giá rủi ro toàn diện (như đã trình bày trong Chương 2), định nghĩa chính sách ATTT, xây dựng kế hoạch xử lý rủi ro với các biện pháp kiểm soát cụ thể (như đề xuất trong Chương 3), và thiết lập các mục tiêu bảo mật có thể đo lường được. Đối với CRM 1.0, giai đoạn Plan cần được thực hiện trước mỗi lần release lớn và định kỳ hàng năm.")], { indent: { left: 360 } }),
    blank(),
    p([tb("DO (Thực hiện):"), t(" Triển khai kế hoạch xử lý rủi ro và các biện pháp kiểm soát đã được lập kế hoạch. Đối với CRM 1.0, đây là việc thực thi toàn bộ các giải pháp kỹ thuật ở Chương 3 (triển khai WAF, mTLS, ABAC, Circuit Breaker,...) kết hợp với đào tạo nhân sự và ban hành chính sách nội bộ. Tài liệu hóa đầy đủ mọi quyết định và cấu hình là yêu cầu bắt buộc của ISO 27001.")], { indent: { left: 360 } }),
    blank(),
    p([tb("CHECK (Kiểm tra):"), t(" Giám sát, đo lường và đánh giá hiệu quả của ISMS. Bao gồm: "), tb("Internal Audit"), t(" định kỳ (ít nhất 6 tháng/lần) để đánh giá sự tuân thủ; "), tb("Penetration Testing"), t(" (kiểm tra xâm nhập có kiểm soát) ít nhất 1 lần/năm và sau mỗi thay đổi kiến trúc lớn; phân tích nhật ký Security Information and Event Management "), tb("(SIEM)"), t(" để phát hiện bất thường; và đánh giá KPI bảo mật (số lượng sự cố, thời gian phát hiện và phản hồi sự cố – MTTD/MTTR).")], { indent: { left: 360 } }),
    blank(),
    p([tb("ACT (Hành động cải tiến):"), t(" Dựa trên kết quả Check, xác định các biện pháp khắc phục và cải tiến phòng ngừa. Cập nhật chính sách, thủ tục và kiến trúc kỹ thuật khi cần. Đặc biệt, khi có sự cố bảo mật xảy ra, quy trình "), tb("Lessons Learned"), t(" phải được thực hiện nghiêm túc để tránh tái diễn – đây là cơ chế học hỏi từ kinh nghiệm thực tiễn mà không thể thay thế bằng bất kỳ công cụ tự động nào.")], { indent: { left: 360 } }),
    blank(),

    caption("Bảng 4.1: Ánh xạ chu trình PDCA vào lịch trình vận hành CRM 1.0"),
    new Table({
      width: { size: 9360, type: WidthType.DXA }, columnWidths: [800, 2200, 2760, 3600],
      rows: [
        new TableRow({ children: [hCell("Giai đoạn", 800), hCell("Hoạt động chính", 2200), hCell("Tần suất/Thời điểm", 2760), hCell("Đầu ra / Sản phẩm bàn giao", 3600)] }),
        ...([
          ["PLAN", "Đánh giá rủi ro, cập nhật Threat Model", "Hàng năm + sau mỗi kiến trúc thay đổi lớn", "Báo cáo đánh giá rủi ro cập nhật, Risk Treatment Plan"],
          ["DO", "Triển khai biện pháp kiểm soát, đào tạo nhân viên", "Liên tục theo sprint DevSecOps", "Security tickets đã hoàn thành, Training completion record"],
          ["CHECK", "Internal ISMS Audit, Penetration Test, SIEM Review", "6 tháng/lần (Audit), 1 năm/lần (PenTest)", "Audit Report, PenTest Report, Security KPI Dashboard"],
          ["CHECK", "Phân tích sự cố bảo mật (Incident Analysis)", "Sau mỗi sự cố được phát hiện", "Incident Report, Root Cause Analysis, MTTD/MTTR metrics"],
          ["ACT", "Cải tiến chính sách, vá lỗ hổng, cập nhật kiến trúc", "Liên tục dựa trên kết quả Check", "Policy revision, Patch notes, Architecture Decision Records (ADR)"],
        ]).map((row, i) => new TableRow({ children: [cCell(row[0], 800, alt(i), true), bCell(row[1], 2200, alt(i)), bCell(row[2], 2760, alt(i)), bCell(row[3], 3600, alt(i))] }))
      ]
    }),
    blank(),

    h3("4.1.2. Tích hợp DevSecOps – Bảo mật tự động trong vòng đời phát triển"),
    p([t("Trong môi trường phát triển phần mềm hiện đại theo mô hình "), tb("Agile/CI-CD"), t(", các lỗ hổng bảo mật nếu chỉ được phát hiện vào cuối vòng đời phát triển (sau khi code đã lên Production) sẽ tốn kém gấp nhiều lần chi phí khắc phục so với phát hiện từ sớm (Shift-Left Security). Đây là lý do mô hình "), tb("DevSecOps"), t(" – tích hợp Security vào mọi giai đoạn của vòng đời CI/CD – là yêu cầu bắt buộc cho CRM 1.0:")]),
    blank(),
    p([tb("Giai đoạn CODE:"), t(" Lập trình viên sử dụng IDE plugin (ví dụ: SonarLint) để phát hiện lỗ hổng bảo mật ngay khi gõ code (SAST – Static Application Security Testing real-time). Code review bắt buộc có tiêu chí security checklist (ví dụ: có dùng parameterized query không? Có lộ thông tin nhạy cảm trong log không?)")], { indent: { left: 360 } }),
    blank(),
    p([tb("Giai đoạn BUILD:"), t(" Pipeline CI tích hợp "), tb("SonarQube"), t(" để quét toàn bộ mã nguồn tìm lỗ hổng bảo mật (SQL Injection, XSS, hardcoded credentials, insecure dependencies). Build sẽ "), tb("FAIL"), t(" tự động nếu phát hiện lỗ hổng mức độ Critical hoặc High chưa được xử lý. Đây là \"Security Gate\" đầu tiên ngăn code có lỗ hổng không được merge vào nhánh chính.")], { indent: { left: 360 } }),
    blank(),
    p([tb("Giai đoạn PACKAGE (Container):"), t(" Trước khi Docker image được đẩy lên OpenShift Registry, công cụ "), tb("Trivy"), t(" hoặc "), tb("Clair"), t(" quét toàn bộ image tìm CVE (Common Vulnerabilities and Exposures) đã biết trong OS packages và application dependencies. Image có CVE Critical chưa có bản vá sẽ bị từ chối đẩy lên registry. Ngoài ra, "), tb("Cosign"), t(" được dùng để ký số Docker image, đảm bảo image không bị giả mạo trong quá trình truyền tải. OpenShift chỉ chạy các image có chữ ký hợp lệ từ registry nội bộ, ngăn chặn triệt để rủi ro R08 (Supply Chain Attack).")], { indent: { left: 360 } }),
    blank(),
    p([tb("Giai đoạn DEPLOY & RUNTIME:"), t(" "), tb("Falco"), t(" – công cụ Runtime Security mã nguồn mở cho Kubernetes – được triển khai trên tất cả Worker Nodes để phát hiện hành vi bất thường tại tầng runtime: container đang cố gắng ghi file ra ngoài mount path cho phép, tiến trình thực thi lệnh shell không mong đợi ("), tb("exec /bin/sh"), t(" trong container production), kết nối mạng đến địa chỉ IP không nằm trong danh sách whitelist,... Mọi cảnh báo từ Falco được đẩy về "), tb("SIEM"), t(" để phân tích tập trung và kích hoạt cảnh báo cho đội ngũ SOC (Security Operations Center).")], { indent: { left: 360 } }),
    blank(),

    h2("4.2. Khía cạnh Tuân thủ Pháp luật Việt Nam"),
    blank(),
    p([t("VietinBank là tổ chức tín dụng hoạt động trong lãnh thổ Việt Nam, do đó hệ thống CRM 1.0 phải tuân thủ toàn diện các quy định pháp luật hiện hành, trong đó nổi bật nhất là hai đạo luật sau:")]),
    blank(),
    p([tb("Luật An toàn thông tin mạng số 86/2015/QH13"), t(": Đây là luật nền tảng điều chỉnh hoạt động bảo đảm an toàn thông tin mạng tại Việt Nam. Điều 17 của Luật quy định rõ trách nhiệm của chủ quản hệ thống thông tin quan trọng quốc gia (và hệ thống ngân hàng thuộc diện này) trong việc "), tb("bảo vệ thông tin cá nhân"), t(": phải thu thập đúng mục đích, có sự đồng ý của chủ thể, không được tiết lộ cho bên thứ ba khi chưa có sự cho phép, và phải thực hiện các biện pháp kỹ thuật để ngăn ngừa truy cập trái phép. CRM 1.0, với tư cách là hệ thống lưu trữ dữ liệu cá nhân nhạy cảm của hàng triệu khách hàng, phải tuân thủ nghiêm ngặt các quy định này.")]),
    blank(),
    p([tb("Luật An ninh mạng số 24/2018/QH14"), t(": Điều 26 quy định các doanh nghiệp cung cấp dịch vụ trên mạng viễn thông, mạng Internet, và các dịch vụ gia tăng trên không gian mạng tại Việt Nam phải "), tb("lưu trữ dữ liệu người dùng Việt Nam trên lãnh thổ Việt Nam"), t(" (Data Localization) và phải cung cấp dữ liệu cho cơ quan nhà nước có thẩm quyền khi được yêu cầu. Đối với CRM 1.0, điều này có nghĩa là toàn bộ hạ tầng Cloud-Native và OpenShift cluster "), tb("phải được đặt tại các Data Center trên lãnh thổ Việt Nam"), t(", không được phép đặt trên các Cloud Region nước ngoài mà không có biện pháp đảm bảo tuân thủ.")]),
    blank(),
    p([t("Ngoài ra, "), tb("Nghị định 13/2023/NĐ-CP về Bảo vệ dữ liệu cá nhân"), t(" (có hiệu lực từ 1/7/2023) đặt ra các yêu cầu cụ thể hơn về xử lý dữ liệu cá nhân: bắt buộc có "), tb("Đánh giá tác động xử lý dữ liệu cá nhân"), t(" trước khi triển khai hệ thống mới có xử lý dữ liệu nhạy cảm quy mô lớn; bổ nhiệm "), tb("Nhân viên Bảo vệ Dữ liệu Cá nhân (DPO)"), t("; và thông báo cho Bộ Công an trong vòng 72 giờ khi xảy ra vi phạm dữ liệu. Đây là các yêu cầu pháp lý mà VietinBank phải tích hợp vào Incident Response Plan của mình.")]),
    blank(),

    caption("Bảng 4.2: Ánh xạ yêu cầu pháp lý – Biện pháp kỹ thuật tuân thủ"),
    new Table({
      width: { size: 9360, type: WidthType.DXA }, columnWidths: [2400, 1800, 2560, 2600],
      rows: [
        new TableRow({ children: [hCell("Quy định pháp lý", 2400), hCell("Điều khoản liên quan", 1800), hCell("Yêu cầu đối với CRM 1.0", 2560), hCell("Biện pháp kỹ thuật tuân thủ", 2600)] }),
        ...([
          ["Luật ATTT Mạng 86/2015", "Điều 17 – Bảo vệ thông tin cá nhân", "Mã hóa, kiểm soát truy cập, không tiết lộ trái phép", "AES-256 TDE, RBAC/ABAC, Audit Log WORM"],
          ["Luật An ninh mạng 24/2018", "Điều 26 – Data Localization", "Toàn bộ dữ liệu KH Việt Nam phải lưu tại Việt Nam", "OpenShift cluster đặt tại DC trong nước; S3 WORM on-premise"],
          ["Nghị định 13/2023/NĐ-CP", "Điều 24 – Đánh giá tác động BVDLCN", "DPIA trước khi triển khai hệ thống xử lý dữ liệu lớn", "Tài liệu DPIA đầy đủ; DPO được bổ nhiệm"],
          ["Nghị định 13/2023/NĐ-CP", "Điều 23 – Thông báo vi phạm 72h", "Thông báo Bộ Công an trong 72h khi có vi phạm", "Incident Response Plan; SIEM tự động phát hiện vi phạm"],
          ["Thông tư 09/2020/TT-NHNN", "Quy định an toàn HTTT ngành NH", "Kiểm tra xâm nhập định kỳ, quản lý lỗ hổng", "PenTest hàng năm, Vulnerability Management (Tenable)"],
        ]).map((row, i) => new TableRow({ children: [bCell(row[0], 2400, alt(i), true), bCell(row[1], 1800, alt(i)), bCell(row[2], 2560, alt(i)), bCell(row[3], 2600, alt(i))] }))
      ]
    }),
    blank(),

    h2("4.3. Quản trị Con người và Đạo đức nghề nghiệp trong An toàn thông tin"),
    blank(),
    h3("4.3.1. Cơ chế giám sát và Audit Log bất biến (WORM)"),
    p([t("Từ phân tích rủi ro R01 (lạm dụng quyền hạn nội bộ) ở Chương 2, rõ ràng rằng biện pháp ngăn chặn kỹ thuật (ABAC, RLS) là cần thiết nhưng chưa đủ. Nguyên tắc "), tb("\"Trust but Verify\" (Tin tưởng nhưng Xác minh)"), t(" đòi hỏi phải có cơ chế giám sát hành vi người dùng và lưu trữ bằng chứng kiểm toán không thể bác bỏ. Đây chính là vai trò của hệ thống "), tb("Audit Log bất biến trên S3 WORM.")]),
    blank(),
    p([t("Mỗi sự kiện sau đây trong CRM 1.0 phải được ghi nhật ký kiểm toán đầy đủ và không thể sửa đổi:")]),
    blank(),
    p([tb("Sự kiện xem dữ liệu nhạy cảm:"), t(" Mỗi lần người dùng click \"Hiển thị\" để xem số CCCD, số tài khoản, điểm CIC, hoặc tải hồ sơ PDF của khách hàng, hệ thống ghi: userId, customerId, trường dữ liệu được xem, timestamp, IP, user-agent, sessionId. Các bản ghi này được đẩy real-time lên S3 WORM bucket qua Kafka – không đi qua bất kỳ lớp nào có thể bị nhân viên IT can thiệp.")], { indent: { left: 360 } }),
    blank(),
    p([tb("Sự kiện đăng nhập và đăng xuất:"), t(" Mọi sự kiện đăng nhập thành công, đăng nhập thất bại (ghi rõ lý do), và đăng xuất. Phát hiện bất thường dựa trên hành vi: cùng tài khoản đăng nhập từ hai địa điểm địa lý khác nhau trong khoảng thời gian không thể di chuyển được (Impossible Travel Detection) sẽ kích hoạt cảnh báo tức thì.")], { indent: { left: 360 } }),
    blank(),
    p([tb("Sự kiện thay đổi dữ liệu:"), t(" Mọi INSERT/UPDATE/DELETE trên dữ liệu khách hàng đều được ghi lại với "), tb("giá trị trước (before) và sau (after) thay đổi"), t(", cùng userId thực hiện thay đổi. Đây là bằng chứng không thể bác bỏ trong các vụ điều tra gian lận nội bộ.")], { indent: { left: 360 } }),
    blank(),
    p([t("Toàn bộ Audit Log được lưu trữ trên S3 WORM với chính sách giữ tối thiểu "), tb("5 năm"), t(" (theo yêu cầu của Thông tư Ngân hàng Nhà nước), được ký số bằng SHA-256 theo cấu trúc "), tb("hash chain"), t(" (mỗi bản ghi hash chứa hash của bản ghi trước, tạo thành chuỗi bất biến – tương tự blockchain) để bất kỳ sự can thiệp nào vào log đều lập tức bị phát hiện. Các báo cáo từ hệ thống Audit Log được tự động tổng hợp và gửi cho "), tb("Ban Kiểm soát nội bộ"), t(" hàng tháng, và cho "), tb("cơ quan thanh tra NHNN"), t(" khi được yêu cầu.")]),
    blank(),

    h3("4.3.2. Xây dựng văn hóa An toàn thông tin và Đạo đức nghề nghiệp"),
    p([t("Công nghệ bảo mật tốt nhất cũng không thể thay thế "), tb("con người có ý thức và đạo đức"), t(". Đặc biệt trong môi trường ngân hàng, nơi nhân viên tiếp xúc hàng ngày với tài sản có giá trị cao nhất (dữ liệu tài chính của khách hàng), việc xây dựng văn hóa tôn trọng quyền riêng tư và đạo đức nghề nghiệp là nền tảng không thể thiếu.")]),
    blank(),
    p([tb("Chương trình đào tạo nhận thức bảo mật (Security Awareness Training):"), t(" Toàn bộ 11.000+ nhân viên có quyền truy cập CRM bắt buộc hoàn thành chương trình đào tạo bảo mật trực tuyến hàng năm, bao gồm các module: nhận biết và phòng tránh Phishing; quy tắc xử lý thông tin khách hàng; báo cáo sự cố bảo mật; và các trường hợp vi phạm thực tế trong ngành ngân hàng (anonymized case studies). Tỷ lệ hoàn thành và điểm kiểm tra được ghi nhận vào hồ sơ nhân sự.")], { indent: { left: 360 } }),
    blank(),
    p([tb("Bộ Quy tắc Ứng xử An toàn thông tin (Information Security Code of Conduct):"), t(" Văn bản chính thức quy định rõ: những hành vi bị nghiêm cấm tuyệt đối (chia sẻ credentials, xuất dữ liệu khách hàng ra ngoài hệ thống, sử dụng thông tin khách hàng cho mục đích cá nhân); cơ chế báo cáo vi phạm (whistleblowing) ẩn danh để nhân viên có thể tố cáo hành vi bất thường của đồng nghiệp mà không sợ bị trả thù; và "), tb("chế tài xử lý vi phạm"), t(" từ cảnh cáo đến sa thải và truy cứu trách nhiệm hình sự tùy mức độ. Bộ quy tắc này được ký cam kết bởi toàn bộ nhân viên khi onboarding và khi nội dung có thay đổi.")], { indent: { left: 360 } }),
    blank(),
    p([tb("Chính sách Need-to-Know và Clean Desk:"), t(" Nhân viên chỉ được truy cập thông tin thực sự cần thiết cho công việc của mình. Màn hình máy tính không được để các thông tin nhạy cảm hiển thị khi không có mặt tại bàn làm việc (áp dụng screen lock tự động sau 3 phút). Tài liệu giấy chứa thông tin khách hàng phải được hủy đúng cách bằng máy hủy tài liệu.")], { indent: { left: 360 } }),
    blank(),

    caption("Bảng 4.3: Chương trình quản trị con người – Đối chiếu với rủi ro"),
    new Table({
      width: { size: 9360, type: WidthType.DXA }, columnWidths: [2400, 1800, 2360, 2800],
      rows: [
        new TableRow({ children: [hCell("Biện pháp quản trị con người", 2400), hCell("Đối tượng áp dụng", 1800), hCell("Rủi ro giảm thiểu", 2360), hCell("Cơ chế đo lường hiệu quả", 2800)] }),
        ...([
          ["Security Awareness Training bắt buộc hàng năm", "Toàn bộ 11.000+ nhân viên", "R10 (Phishing), R01 (Insider)", "Tỷ lệ hoàn thành ≥ 95%, điểm kiểm tra ≥ 80%"],
          ["Phishing Simulation định kỳ", "Toàn bộ nhân viên (bất ngờ)", "R10 (Phishing)", "Tỷ lệ click link giả giảm ≤ 5% sau 2 lần"],
          ["Bộ Quy tắc Ứng xử ATTT", "Toàn bộ nhân viên có quyền truy CRM", "R01 (Insider Threat)", "100% nhân viên ký cam kết; 0 vi phạm nghiêm trọng/năm"],
          ["Background check định kỳ cho nhân sự nhạy cảm", "RM, Trưởng phòng, SysAdmin", "R01 (Insider Threat)", "100% vị trí nhạy cảm được review định kỳ 2 năm/lần"],
          ["Offboarding Security Checklist", "Nhân viên nghỉ việc/chuyển vị trí", "R01, R10 (Stale accounts)", "Tài khoản bị thu hồi ≤ 4 giờ sau ngày nghỉ hiệu lực"],
        ]).map((row, i) => new TableRow({ children: [bCell(row[0], 2400, alt(i), true), bCell(row[1], 1800, alt(i)), bCell(row[2], 2360, alt(i)), bCell(row[3], 2800, alt(i))] }))
      ]
    }),
    blank(),

    // Summary Chapter 4
    new Paragraph({ spacing: { before: 300, after: 120 },
      children: [new TextRun({ text: "Tóm tắt Chương 4", bold: true, size: 28, font: "Times New Roman", color: "1F3864" })] }),
    p([t("Chương 4 đã hoàn thiện bức tranh bảo mật toàn diện cho hệ thống CRM 1.0 bằng cách bổ sung hai trụ cột còn lại trong mô hình People – Process – Technology. Chu trình PDCA của ISO/IEC 27001 cung cấp khung quản trị liên tục và có hệ thống, đảm bảo rằng bảo mật không phải là trạng thái đạt được một lần mà là một quá trình cải tiến không ngừng. DevSecOps tích hợp bảo mật vào vòng đời phát triển phần mềm theo nguyên tắc \"Shift-Left\", phát hiện và xử lý lỗ hổng trước khi chúng đến môi trường Production. Khung pháp lý Việt Nam – đặc biệt là Nghị định 13/2023/NĐ-CP – đặt ra các nghĩa vụ pháp lý cụ thể mà VietinBank phải tuân thủ. Cuối cùng, Audit Log WORM và chương trình quản trị con người tạo nên lớp bảo vệ phi kỹ thuật không thể thiếu, đặc biệt trong việc phòng chống và phát hiện gian lận nội bộ – rủi ro đặc thù và nghiêm trọng nhất trong môi trường ngân hàng.")]),
    blank(),

    // ─── KẾT LUẬN ───
    new Paragraph({ children: [new PageBreak()] }),
    new Paragraph({ heading: HeadingLevel.HEADING_1, spacing: { before: 400, after: 200 }, alignment: AlignmentType.CENTER,
      children: [new TextRun({ text: "KẾT LUẬN", bold: true, size: 32, font: "Times New Roman", color: "1F3864" })] }),
    blank(),
    p([t("Bài tập lớn này đã triển khai một nghiên cứu có hệ thống về an toàn thông tin cho một trong những hệ thống thông tin trọng yếu nhất của VietinBank – hệ thống CRM 1.0 với kiến trúc Cloud-Native Microservices trên Red Hat OpenShift. Xuyên suốt bốn chương, từ nền tảng lý thuyết đến phân tích thực tiễn và đề xuất giải pháp, một kết luận trung tâm nổi lên rõ ràng: "), tb("kiến trúc Microservices mang lại năng lực mở rộng và tốc độ triển khai vượt trội, nhưng đồng thời tạo ra một hồ sơ rủi ro bảo mật phức tạp và đa chiều mà các phương pháp bảo mật truyền thống không đủ để xử lý.")]),
    blank(),
    p([t("Thông qua việc áp dụng mô hình "), tb("CIA Triad"), t(" và "), tb("Defense in Depth"), t(" làm khung phân tích, phương pháp "), tb("đánh giá rủi ro 9 bước"), t(" làm công cụ nhận diện, và bộ công nghệ bảo mật hiện đại (AES-256, mTLS/Istio, ABAC/OPA, Circuit Breaker, Saga Pattern, DevSecOps) làm giải pháp kỹ thuật, bài viết đã đề xuất một kiến trúc bảo mật "), tb("toàn diện theo nguyên tắc ba lớp People – Process – Technology"), t(". Kiến trúc này không chỉ xử lý các rủi ro hiện tại mà còn tạo nền tảng bền vững cho sự phát triển trong tương lai, đặc biệt trong bối cảnh VietinBank đang hướng đến "), tb("Open Banking"), t(" và tích hợp với hệ sinh thái tài chính số rộng lớn hơn.")]),
    blank(),
    p([t("Về mặt tuân thủ, kiến trúc đề xuất đảm bảo VietinBank đáp ứng đầy đủ các yêu cầu của "), tb("Luật An ninh mạng 2018, Nghị định 13/2023/NĐ-CP và ISO/IEC 27001"), t(", giảm thiểu rủi ro pháp lý và gia tăng niềm tin của khách hàng, cơ quan quản lý và đối tác. Audit Log bất biến trên S3 WORM không chỉ là yêu cầu kỹ thuật mà còn là "), tb("công cụ quản trị đạo đức"), t(", tạo ra môi trường trách nhiệm rõ ràng, ngăn ngừa và phát hiện kịp thời các hành vi gian lận nội bộ – bảo vệ cả tổ chức lẫn sự liêm chính của từng cán bộ nhân viên.")]),
    blank(),
    p([t("Tóm lại, bảo mật không phải là đích đến mà là một "), tb("hành trình cải tiến liên tục"), t(". Chu trình PDCA của ISMS, kết hợp với văn hóa DevSecOps và đào tạo nhận thức bảo mật thường xuyên, tạo ra cơ chế tự học hỏi và thích nghi trước các mối đe dọa mới nổi. Khi VietinBank tiếp tục hành trình chuyển đổi số, kiến trúc bảo mật toàn diện được đề xuất trong bài viết này sẽ là nền tảng vững chắc để bảo vệ tài sản số quý giá nhất – "), tb("niềm tin của hàng triệu khách hàng"), t(".")]),
    blank(),
  );

  return c;
}

module.exports = { buildChapter4AndConclusion };
