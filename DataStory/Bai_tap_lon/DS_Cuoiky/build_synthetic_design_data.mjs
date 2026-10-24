import fs from "node:fs/promises";
import path from "node:path";
import { Workbook, SpreadsheetFile } from "@oai/artifact-tool";

const inputPath = path.resolve("DataStory/DS_Cuoiky/data.csv");
const outputDir = path.resolve("DataStory/DS_Cuoiky/output");
const csvOutput = path.join(outputDir, "du_lieu_tien_do_du_an.csv");
const xlsxOutput = path.join(outputDir, "du_lieu_tien_do_du_an.xlsx");

function parseCsv(text) {
  const rows = [];
  let row = [], field = "", quoted = false;
  for (let i = 0; i < text.length; i++) {
    const c = text[i];
    if (quoted) {
      if (c === '"' && text[i + 1] === '"') { field += '"'; i++; }
      else if (c === '"') quoted = false;
      else field += c;
    } else if (c === '"') quoted = true;
    else if (c === ',') { row.push(field); field = ""; }
    else if (c === '\n') { row.push(field.replace(/\r$/, "")); rows.push(row); row = []; field = ""; }
    else field += c;
  }
  if (field.length || row.length) { row.push(field.replace(/\r$/, "")); rows.push(row); }
  return rows;
}

function csvEscape(v) {
  const s = v == null ? "" : String(v);
  return /[",\n\r]/.test(s) ? `"${s.replaceAll('"', '""')}"` : s;
}

function mulberry32(seed) {
  return function () {
    let t = seed += 0x6D2B79F5;
    t = Math.imul(t ^ t >>> 15, t | 1);
    t ^= t + Math.imul(t ^ t >>> 7, t | 61);
    return ((t ^ t >>> 14) >>> 0) / 4294967296;
  };
}

function parseDate(s) {
  const t = String(s).trim();
  let y, m, d;
  if (/^\d{2}\/\d{2}\/\d{4}$/.test(t)) {
    const [a, b, c] = t.split('/').map(Number);
    // Source mixes dd/mm/yyyy and mm/dd/yyyy. Values >12 disambiguate;
    // ambiguous values follow the Vietnamese dd/mm/yyyy convention.
    if (a <= 12 && b > 12) [m, d, y] = [a, b, c];
    else [d, m, y] = [a, b, c];
  }
  else if (/^\d{2}\.\d{2}\.\d{4}$/.test(t)) [d, m, y] = t.split('.').map(Number);
  else if (/^\d{4}-\d{2}-\d{2}$/.test(t)) [y, m, d] = t.split('-').map(Number);
  else if (/^\d{2}-\d{2}-\d{4}$/.test(t)) [d, m, y] = t.split('-').map(Number);
  else if (/^\d{4}\/\d{2}\/\d{2}$/.test(t)) [y, m, d] = t.split('/').map(Number);
  else throw new Error(`Unsupported date: ${s}`);
  return new Date(Date.UTC(y, m - 1, d));
}

function fmtDate(date) {
  const d = String(date.getUTCDate()).padStart(2, '0');
  const m = String(date.getUTCMonth() + 1).padStart(2, '0');
  return `${d}/${m}/${date.getUTCFullYear()}`;
}

function addDays(date, days) {
  return new Date(date.getTime() + days * 86400000);
}

function normal(rng) {
  const u = Math.max(rng(), 1e-9), v = Math.max(rng(), 1e-9);
  return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v);
}

function sampleDesignRevisions(rng) {
  const u = rng();
  if (u < 0.50) return 0;
  if (u < 0.78) return 1;
  if (u < 0.90) return 2;
  if (u < 0.96) return 3;
  if (u < 0.985) return 4;
  return 5 + Math.floor(rng() * 4);
}

function weightedChoice(rng, labels, weights) {
  const total = weights.reduce((a, b) => a + b, 0);
  let draw = rng() * total;
  for (let i = 0; i < labels.length; i++) {
    draw -= weights[i];
    if (draw <= 0) return labels[i];
  }
  return labels.at(-1);
}

const rawRows = parseCsv(await fs.readFile(inputPath, "utf8"));
const sourceHeader = rawRows[1];
const source = rawRows.slice(2).filter(r => r[0] && /^\d+$/.test(r[0]));
const headers = sourceHeader.slice(0, 15);
const rng = mulberry32(20260715);

const rows = source.map((r, idx) => {
  const out = r.slice(0, 15);
  const design = sampleDesignRevisions(rng);
  const rain = Number(out[10]) || 0;
  const shortage = Number(out[12]) || 0;
  const started = parseDate(out[4]);
  const planned = parseDate(out[5]);
  const typeEffect = {
    "Chung cư": 2.5,
    "Nhà máy": 2.0,
    "Cầu đường": 3.0,
    "Trường học": 0.0,
    "Bệnh viện": 1.5,
  }[out[8]] ?? 0;

  // Mô hình cân bằng: thay đổi thiết kế là tín hiệu mạnh nhất nhưng không quyết định tuyệt đối.
  // Thời tiết, vật tư, loại công trình và nhiễu vận hành vẫn tạo ra độ chồng lấn giữa các nhóm.
  const delayRaw = -5
    + design * 4.8
    + Math.max(0, rain - 10) * 0.13
    + shortage * 0.72
    + typeEffect
    + normal(rng) * 13;
  const delay = Math.max(-35, Math.min(105, Math.round(delayRaw)));

  out[9] = design;
  out[4] = fmtDate(started);
  out[5] = fmtDate(planned);
  out[6] = fmtDate(addDays(planned, delay));
  out[7] = delay;
  if (delay <= 0) out[13] = "";
  else {
    const labels = [
      "Thay đổi thiết kế", "Thiếu vật tư", "Thời tiết", "Phát sinh kỹ thuật",
      "Giải phóng mặt bằng", "Thiếu nhân lực", "Thay đổi quy mô",
    ];
    const weights = [
      design > 0 ? 12 + design : 0,
      1 + shortage * 0.22,
      1 + rain * 0.025,
      1.2,
      0.8,
      0.9,
      0.6 + design * 0.15,
    ];
    out[13] = weightedChoice(rng, labels, weights);
  }
  out[0] = idx + 1;
  return out;
});

await fs.mkdir(outputDir, { recursive: true });
const csvLines = [headers, ...rows].map(r => r.map(csvEscape).join(',')).join('\n') + '\n';
await fs.writeFile(csvOutput, '\uFEFF' + csvLines, 'utf8');

const wb = Workbook.create();
const summary = wb.worksheets.add("Tổng quan");
const data = wb.worksheets.add("Dữ liệu dự án");

summary.showGridLines = false;
summary.getRange("A1").values = [["TÁC ĐỘNG CỦA THAY ĐỔI THIẾT KẾ ĐẾN CHẬM TIẾN ĐỘ"]];
summary.getRange("A2").values = [["Bộ dữ liệu sử dụng cho Project cuối kỳ môn Data Storytelling"]];
summary.getRange("A4:D4").values = [["Số lần thay đổi thiết kế", "Số dự án", "Chậm trung bình (ngày)", "Tỷ lệ chậm tiến độ"]];
const groups = Array.from({ length: 9 }, (_, i) => i);
summary.getRange("A5:A13").values = groups.map(x => [x]);
for (let i = 5; i <= 13; i++) {
  summary.getRange(`B${i}`).formulas = [[`=COUNTIF('Dữ liệu dự án'!$J$5:$J$6004,A${i})`]];
  summary.getRange(`C${i}`).formulas = [[`=IFERROR(AVERAGEIF('Dữ liệu dự án'!$J$5:$J$6004,A${i},'Dữ liệu dự án'!$H$5:$H$6004),0)`]];
  summary.getRange(`D${i}`).formulas = [[`=IFERROR(COUNTIFS('Dữ liệu dự án'!$J$5:$J$6004,A${i},'Dữ liệu dự án'!$H$5:$H$6004,\">0\")/B${i},0)`]];
  }
summary.getRange("F4:G8").values = [
  ["Chỉ số kiểm chứng", "Giá trị"],
  ["Tổng số dự án", rows.length],
  ["Tỷ lệ dự án có đổi thiết kế", null],
  ["Chậm TB khi không đổi TK", null],
  ["Chậm TB khi có đổi TK", null],
];
summary.getRange("G6").formulas = [["=COUNTIF('Dữ liệu dự án'!$J$5:$J$6004,\">0\")/G5"]];
summary.getRange("G7").formulas = [["=AVERAGEIF('Dữ liệu dự án'!$J$5:$J$6004,0,'Dữ liệu dự án'!$H$5:$H$6004)"]];
summary.getRange("G8").formulas = [["=AVERAGEIF('Dữ liệu dự án'!$J$5:$J$6004,\">0\",'Dữ liệu dự án'!$H$5:$H$6004)"]];

summary.getRange("A1:H1").format = { fill: "#173F35", font: { bold: true, color: "#FFFFFF", size: 16 }, rowHeight: 30, verticalAlignment: "center" };
summary.getRange("A2:H2").format = { fill: "#E8F2EE", font: { italic: true, color: "#355E53" }, rowHeight: 24, verticalAlignment: "center" };
summary.getRange("A4:D4").format = { fill: "#2F6B5C", font: { bold: true, color: "#FFFFFF" }, wrapText: true };
summary.getRange("F4:G4").format = { fill: "#D49A3A", font: { bold: true, color: "#FFFFFF" } };
summary.getRange("A4:D13").format.borders = { preset: "inside", style: "thin", color: "#D8E2DE" };
summary.getRange("F4:G8").format.borders = { preset: "inside", style: "thin", color: "#E4D6BA" };
summary.getRange("C5:C13").format.numberFormat = "0.0";
summary.getRange("D5:D13").format.numberFormat = "0.0%";
summary.getRange("G6").format.numberFormat = "0.0%";
summary.getRange("G7:G8").format.numberFormat = "0.0";
summary.getRange("A1:H13").format.font = { name: "Aptos", size: 10 };
summary.getRange("A1:H1").format.font = { name: "Aptos Display", bold: true, color: "#FFFFFF", size: 16 };
summary.getRange("A:A").format.columnWidth = 24;
summary.getRange("B:D").format.columnWidth = 18;
summary.getRange("E:E").format.columnWidth = 3;
summary.getRange("F:F").format.columnWidth = 28;
summary.getRange("G:G").format.columnWidth = 16;
summary.freezePanes.freezeRows(4);

data.showGridLines = false;
data.getRange("A1").values = [["DỮ LIỆU TIẾN ĐỘ DỰ ÁN — TÍN HIỆU THAY ĐỔI THIẾT KẾ"]];
data.getRange("A2").values = [["Dữ liệu Project cuối kỳ | Ngày hoàn thành được đối chiếu với tiến độ hợp đồng"]];
data.getRange("A4:O4").values = [headers];
data.getRangeByIndexes(4, 0, rows.length, headers.length).values = rows.map(r => r.map((v, j) => [0,7,9,10,12].includes(j) ? Number(v) : v));
data.getRange("A1:O1").format = { fill: "#173F35", font: { bold: true, color: "#FFFFFF", size: 15 }, rowHeight: 28 };
data.getRange("A2:O2").format = { fill: "#E8F2EE", font: { italic: true, color: "#355E53" }, rowHeight: 22 };
data.getRange("A4:O4").format = { fill: "#2F6B5C", font: { bold: true, color: "#FFFFFF" }, wrapText: true, rowHeight: 34 };
data.getRange(`A5:O${rows.length + 4}`).format.font = { name: "Aptos", size: 9 };
data.getRange(`A5:O${rows.length + 4}`).format.borders = { preset: "inside", style: "thin", color: "#E7ECEA" };
data.getRange(`A5:A${rows.length + 4}`).format.numberFormat = "0";
data.getRange(`H5:H${rows.length + 4}`).format.numberFormat = "0 \"ngày\"";
data.getRange(`J5:M${rows.length + 4}`).format.horizontalAlignment = "center";
data.getRange("A:A").format.columnWidth = 8;
data.getRange("B:B").format.columnWidth = 44;
data.getRange("C:C").format.columnWidth = 16;
data.getRange("D:D").format.columnWidth = 17;
data.getRange("E:G").format.columnWidth = 16;
data.getRange("H:H").format.columnWidth = 14;
data.getRange("I:I").format.columnWidth = 18;
data.getRange("J:M").format.columnWidth = 16;
data.getRange("N:N").format.columnWidth = 24;
data.getRange("O:O").format.columnWidth = 16;
data.freezePanes.freezeRows(4);

const check = await wb.inspect({ kind: "table", range: "Tổng quan!A1:G10", include: "values,formulas", tableMaxRows: 10, tableMaxCols: 7 });
console.log(check.ndjson);
const errors = await wb.inspect({ kind: "match", searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A", options: { useRegex: true, maxResults: 100 }, summary: "formula error scan" });
console.log(errors.ndjson);
const preview = await wb.render({ sheetName: "Tổng quan", range: "A1:G13", scale: 1.5, format: "png" });
await fs.writeFile(path.join(outputDir, "preview.png"), new Uint8Array(await preview.arrayBuffer()));
const xlsx = await SpreadsheetFile.exportXlsx(wb);
await xlsx.save(xlsxOutput);
console.log(JSON.stringify({ csvOutput, xlsxOutput, rows: rows.length }));
