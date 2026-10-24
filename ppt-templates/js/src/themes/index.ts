/**
 * Module chủ đề màu sắc
 * Định nghĩa trước 7 bảng màu chủ đề cho bản trình bày PPT
 *
 * Các giá trị màu sắc đối ứng chính xác từng mục với themes/*.py phía Python (được kiểm tra bởi scripts/check_parity.py).
 * Khi sửa đổi ở bất kỳ phía nào, bắt buộc phải đồng bộ phía còn lại để tránh CI thất bại.
 */

import { Theme } from '../base';

/** Chủ đề Công nghệ xanh dương - Phù hợp với ngành công nghệ, phần mềm, internet */
export const blueTechnology: Theme = {
  name: 'Công nghệ xanh dương',
  primary: '0066CC',
  secondary: '00CC99',
  accent: '00B4D8',
  background: 'FFFFFF',
  text: '212121',
  muted: '9E9E9E',
  darkBg: '0A1931',
};

/** Chủ đề Tím chuyển sắc - Phù hợp với sáng tạo, thiết kế nghệ thuật */
export const purpleGradient: Theme = {
  name: 'Tím chuyển sắc',
  primary: '7B2FBE',
  secondary: 'E040FB',
  accent: 'A882FF',
  background: 'FFFFFF',
  text: '212121',
  muted: '9E9E9E',
  darkBg: '1E0F32',
};

/** Chủ đề Vàng kim sang trọng - Phù hợp với cao cấp, doanh nghiệp; chủ đề duy nhất dùng nền tối */
export const darkGold: Theme = {
  name: 'Vàng kim sang trọng',
  primary: 'C9A96E',
  secondary: 'B48C50',
  accent: 'FFD700',
  background: '1A1A2E',
  text: 'F0F0F0',
  muted: 'A0A0A0',
  darkBg: '0F0F1E',
};

/** Chủ đề Đen trắng tối giản - Phù hợp với đa dụng, nghiên cứu, học thuật */
export const minimalistBW: Theme = {
  name: 'Đen trắng tối giản',
  primary: '000000',
  secondary: '333333',
  accent: 'C8C8C8',
  background: 'FFFFFF',
  text: '000000',
  muted: '808080',
  darkBg: '000000',
};

/** Chủ đề Xanh đại dương - Phù hợp với giáo dục, đào tạo, dịch vụ */
export const oceanBlue: Theme = {
  name: 'Xanh đại dương',
  primary: '0077B6',
  secondary: '00B4D8',
  accent: '90E0EF',
  background: 'FFFFFF',
  text: '212121',
  muted: '9E9E9E',
  darkBg: '081E34',
};

/** Chủ đề Xanh thiên nhiên - Phù hợp với môi trường, sức khỏe, nông nghiệp */
export const greenNature: Theme = {
  name: 'Xanh thiên nhiên',
  primary: '2D6A4F',
  secondary: '52B788',
  accent: 'A8DAB5',
  background: 'FFFFFF',
  text: '212121',
  muted: '9E9E9E',
  darkBg: '0F281E',
};

/** Chủ đề Đỏ thương mại - Phù hợp với kinh doanh, thương mại, marketing */
export const redBusiness: Theme = {
  name: 'Đỏ thương mại',
  primary: 'C0392B',
  secondary: 'E74C3C',
  accent: 'FF6B6B',
  background: 'FFFFFF',
  text: '212121',
  muted: '9E9E9E',
  darkBg: '320A0A',
};

/** Tập hợp toàn bộ chủ đề */
export const allThemes: Theme[] = [
  blueTechnology,
  purpleGradient,
  darkGold,
  minimalistBW,
  oceanBlue,
  greenNature,
  redBusiness,
];

/**
 * Lấy chủ đề theo tên
 * @param name - Tên chủ đề
 * @returns Đối tượng chủ đề tương ứng, mặc định trả về Công nghệ xanh dương nếu không tìm thấy
 */
export function getThemeByName(name: string): Theme {
  const theme = allThemes.find(t => t.name === name);
  return theme || blueTechnology;
}
