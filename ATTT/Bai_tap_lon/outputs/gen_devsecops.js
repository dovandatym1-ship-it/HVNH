'use strict';
const path = require('path');
const fs   = require('fs');
const { Document, Packer, Paragraph, TextRun, AlignmentType } = require('docx');

const { buildIntroAndChapter1 }    = require('./devsecops_ch1_content');
const { buildChapter2 }             = require('./devsecops_ch2_content');
const { buildChapter3 }             = require('./devsecops_ch3_content');
const { buildChapter4AndConclusion }= require('./devsecops_ch4_content');

const FONT = 'Times New Roman';

function coverPage() {
  const cp = (text, size, bold = false, spacing = 200) =>
    new Paragraph({
      children: [new TextRun({ text, font: FONT, size, bold })],
      alignment: AlignmentType.CENTER,
      spacing: { after: spacing },
    });
  return [
    cp('', 26, false, 800),
    cp('NGÂN HÀNG TMCP CÔNG THƯƠNG VIỆT NAM – VIETINBANK', 26, true),
    cp('HỌC VIỆN CÔNG NGHỆ BƯU CHÍNH VIỄN THÔNG', 26, true),
    cp('', 26, false, 400),
    cp('BÀI TẬP LỚN CUỐI KỲ', 36, true),
    cp('MÔN: AN TOÀN HỆ THỐNG THÔNG TIN', 28, true),
    cp('', 26, false, 600),
    cp('ĐỀ TÀI:', 28, true),
    cp('Nghiên cứu áp dụng tự động hoá đánh giá an ninh', 32, true),
    cp('hạ tầng mã nguồn (IaC) và Container Image', 32, true),
    cp('bằng Trivy và Terrascan trong quy trình GitOps:', 32, true),
    cp('Mở rộng kiến trúc bảo mật cho hệ thống CRM 1.0', 32, true),
    cp('tại Ngân hàng TMCP Công Thương Việt Nam (VietinBank)', 32, true),
    cp('', 26, false, 800),
    cp('Phần nộp: Lời mở đầu và Chương 1 – Cơ sở lý thuyết', 26, false),
    cp('', 26, false, 400),
    cp('Hà Nội, tháng 6 năm 2026', 26, false),
  ];
}

async function main() {
  const sections = [
    ...coverPage(),
    ...buildIntroAndChapter1(),
    ...buildChapter2(),
    ...buildChapter3(),
    ...buildChapter4AndConclusion(),
  ];

  const doc = new Document({
    styles: {
      default: {
        document: {
          run: { font: FONT, size: 26 },
          paragraph: { spacing: { line: 360, lineRule: 'auto' } },
        },
      },
    },
    sections: [{
      properties: {
        page: {
          size: { width: 11906, height: 16838 },
          margin: { top: 1134, bottom: 1134, left: 1701, right: 1134 },
        },
      },
      children: sections,
    }],
  });

  const buf = await Packer.toBuffer(doc);
  const outPath = path.join(__dirname, 'DevSecOps_CRM_VietinBank_HOAN_CHINH.docx');
  fs.writeFileSync(outPath, buf);
  console.log('Done:', outPath);
  console.log('Size:', (buf.length / 1024).toFixed(1), 'KB');
  console.log('Paragraphs:', sections.length);
}

main().catch(e => { console.error(e); process.exit(1); });
