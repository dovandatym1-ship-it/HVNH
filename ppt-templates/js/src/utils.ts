/**
 * Mô-đun hàm tiện ích
 * Cung cấp các chức năng chung như chuyển đổi màu sắc, tính toán vị trí, hỗ trợ hình khối
 */

/** Đối tượng màu RGB */
export interface RGBColor {
  r: number;
  g: number;
  b: number;
}

/**
 * Chuyển đổi màu thập lục phân (hex) sang đối tượng RGB
 * @param hex - Giá trị màu hex (như "FF5733" hoặc "#FF5733")
 * @returns Đối tượng màu RGB
 */
export function hexToRgb(hex: string): RGBColor {
  const cleanHex = hex.replace('#', '');
  return {
    r: parseInt(cleanHex.substring(0, 2), 16),
    g: parseInt(cleanHex.substring(2, 4), 16),
    b: parseInt(cleanHex.substring(4, 6), 16),
  };
}

/**
 * Chuyển đổi đối tượng RGB sang chuỗi màu hex
 * @param rgb - Đối tượng màu RGB
 * @returns Chuỗi màu hex (không chứa ký tự #)
 */
export function rgbToHex(rgb: RGBColor): string {
  const toHex = (n: number) => Math.max(0, Math.min(255, Math.round(n))).toString(16).padStart(2, '0');
  return `${toHex(rgb.r)}${toHex(rgb.g)}${toHex(rgb.b)}`;
}

/**
 * Pha trộn màu sắc (Nội suy tuyến tính)
 * @param color1 - Màu bắt đầu
 * @param color2 - Màu mục tiêu
 * @param factor - Hệ số pha trộn (0~1)
 * @returns Màu hex sau khi pha trộn
 */
export function blendColors(color1: string, color2: string, factor: number): string {
  const rgb1 = hexToRgb(color1);
  const rgb2 = hexToRgb(color2);
  return rgbToHex({
    r: rgb1.r + (rgb2.r - rgb1.r) * factor,
    g: rgb1.g + (rgb2.g - rgb1.g) * factor,
    b: rgb1.b + (rgb2.b - rgb1.b) * factor,
  });
}

/**
 * Tạo biến thể màu sáng hơn
 * @param hex - Màu gốc
 * @param factor - Mức độ làm sáng (0~1, giá trị càng lớn màu càng sáng)
 * @returns Biến thể màu sáng
 */
export function lightenColor(hex: string, factor: number = 0.3): string {
  const rgb = hexToRgb(hex);
  return rgbToHex({
    r: rgb.r + (255 - rgb.r) * factor,
    g: rgb.g + (255 - rgb.g) * factor,
    b: rgb.b + (255 - rgb.b) * factor,
  });
}

/**
 * Tạo biến thể màu tối hơn
 * @param hex - Màu gốc
 * @param factor - Mức độ làm tối (0~1, giá trị càng lớn màu càng tối)
 * @returns Biến thể màu tối
 */
export function darkenColor(hex: string, factor: number = 0.3): string {
  const rgb = hexToRgb(hex);
  return rgbToHex({
    r: rgb.r * (1 - factor),
    g: rgb.g * (1 - factor),
    b: rgb.b * (1 - factor),
  });
}

/** Tọa độ vị trí */
export interface Position {
  x: number;
  y: number;
}

/**
 * Tạo tọa độ vị trí sắp xếp theo hình tròn
 * @param centerX - Tọa độ X tâm tròn
 * @param centerY - Tọa độ Y tâm tròn
 * @param radius - Bán kính hình tròn
 * @param count - Số lượng phần tử
 * @param startAngle - Góc bắt đầu (độ, mặc định -90, tức bắt đầu từ đỉnh)
 * @returns Mảng tọa độ vị trí
 */
export function createCirclePositions(
  centerX: number,
  centerY: number,
  radius: number,
  count: number,
  startAngle: number = -90
): Position[] {
  const positions: Position[] = [];
  const angleStep = (2 * Math.PI) / count;
  for (let i = 0; i < count; i++) {
    const angle = (startAngle * Math.PI) / 180 + i * angleStep;
    positions.push({
      x: centerX + radius * Math.cos(angle),
      y: centerY + radius * Math.sin(angle),
    });
  }
  return positions;
}

/**
 * Tạo tọa độ vị trí sắp xếp theo dạng lưới
 * @param startX - Tọa độ X bắt đầu
 * @param startY - Tọa độ Y bắt đầu
 * @param itemWidth - Chiều rộng mỗi phần tử
 * @param itemHeight - Chiều cao mỗi phần tử
 * @param cols - Số cột
 * @param rows - Số hàng
 * @param gapX - Khoảng cách ngang
 * @param gapY - Khoảng cách dọc
 * @returns Mảng tọa độ vị trí
 */
export function createGridPositions(
  startX: number,
  startY: number,
  itemWidth: number,
  itemHeight: number,
  cols: number,
  rows: number,
  gapX: number = 0.2,
  gapY: number = 0.2
): Position[] {
  const positions: Position[] = [];
  for (let row = 0; row < rows; row++) {
    for (let col = 0; col < cols; col++) {
      positions.push({
        x: startX + col * (itemWidth + gapX),
        y: startY + row * (itemHeight + gapY),
      });
    }
  }
  return positions;
}

/**
 * Tạo tọa độ vị trí sắp xếp theo lưới lục giác
 * @param startX - Tọa độ X bắt đầu
 * @param startY - Tọa độ Y bắt đầu
 * @param size - Kích thước lục giác
 * @param cols - Số cột
 * @param rows - Số hàng
 * @returns Mảng tọa độ vị trí
 */
export function createHexagonPositions(
  startX: number,
  startY: number,
  size: number,
  cols: number,
  rows: number
): Position[] {
  const positions: Position[] = [];
  const hexWidth = size * 2;
  const hexHeight = size * Math.sqrt(3);

  for (let row = 0; row < rows; row++) {
    for (let col = 0; col < cols; col++) {
      const offsetX = row % 2 === 1 ? size : 0;
      positions.push({
        x: startX + col * (hexWidth * 0.75) + offsetX,
        y: startY + row * (hexHeight * 0.5),
      });
    }
  }
  return positions;
}

/**
 * Tạo mảng vị trí phân bổ đều theo chiều ngang
 * @param startX - Tọa độ X bắt đầu
 * @param endX - Tọa độ X kết thúc
 * @param count - Số lượng
 * @returns Mảng tọa độ X
 */
export function distributeHorizontal(startX: number, endX: number, count: number): number[] {
  if (count <= 1) return [(startX + endX) / 2];
  const step = (endX - startX) / (count - 1);
  return Array.from({ length: count }, (_, i) => startX + i * step);
}

/**
 * Tạo mảng vị trí phân bổ đều theo chiều dọc
 * @param startY - Tọa độ Y bắt đầu
 * @param endY - Tọa độ Y kết thúc
 * @param count - Số lượng
 * @returns Mảng tọa độ Y
 */
export function distributeVertical(startY: number, endY: number, count: number): number[] {
  if (count <= 1) return [(startY + endY) / 2];
  const step = (endY - startY) / (count - 1);
  return Array.from({ length: count }, (_, i) => startY + i * step);
}

/**
 * Hỗ trợ định dạng văn bản - Tạo tiêu đề có số thứ tự
 * @param index - Số thứ tự
 * @param title - Văn bản tiêu đề
 * @param format - Mẫu định dạng, {index} đại diện cho số thứ tự, {title} đại diện cho tiêu đề
 * @returns Văn bản sau khi định dạng
 */
export function formatNumberedTitle(index: number, title: string, format?: string): string {
  const template = format || '{index}. {title}';
  return template.replace('{index}', String(index)).replace('{title}', title);
}

/**
 * Cắt ngắn văn bản theo độ dài chỉ định
 * @param text - Văn bản gốc
 * @param maxLength - Độ dài tối đa
 * @param suffix - Hậu tố sau khi cắt ngắn
 * @returns Văn bản sau khi cắt ngắn
 */
export function truncateText(text: string, maxLength: number, suffix: string = '...'): string {
  if (text.length <= maxLength) return text;
  return text.substring(0, maxLength - suffix.length) + suffix;
}

/**
 * Tạo ID ngẫu nhiên
 * @param length - Độ dài ID
 * @returns Chuỗi ngẫu nhiên
 */
export function generateId(length: number = 8): string {
  const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
  let result = '';
  for (let i = 0; i < length; i++) {
    result += chars.charAt(Math.floor(Math.random() * chars.length));
  }
  return result;
}

/**
 * Ước tính số dòng văn bản (dựa trên chiều rộng và cỡ chữ)
 * @param text - Nội dung văn bản
 * @param width - Chiều rộng khả dụng (inch)
 * @param fontSize - Cỡ chữ (point)
 * @returns Số dòng ước tính
 */
export function estimateTextLines(text: string, width: number, fontSize: number): number {
  const avgCharWidth = fontSize * 0.012; // Chiều rộng ký tự xấp xỉ
  const charsPerLine = Math.floor(width / avgCharWidth);
  return Math.ceil(text.length / charsPerLine);
}

/**
 * Phép chia an toàn, tránh lỗi chia cho số 0
 * @param a - Số bị chia
 * @param b - Số chia
 * @param defaultVal - Giá trị mặc định khi số chia bằng 0
 * @returns Kết quả phép chia
 */
export function safeDivide(a: number, b: number, defaultVal: number = 0): number {
  return b === 0 ? defaultVal : a / b;
}

/**
 * Giới hạn giá trị số trong khoảng chỉ định
 * @param value - Giá trị đầu vào
 * @param min - Giá trị nhỏ nhất
 * @param max - Giá trị lớn nhất
 * @returns Giá trị sau khi giới hạn
 */
export function clamp(value: number, min: number, max: number): number {
  return Math.max(min, Math.min(max, value));
}
