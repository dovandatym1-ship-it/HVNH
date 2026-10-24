/**
 * Mô-đun bộ tạo trang kết thúc (Ending)
 * Bao gồm 3 mẫu kết thúc phong cách đa dạng:
 * - Trang cảm ơn, Trang mã QR, Trang thông tin liên hệ
 */

import pptxgen from 'pptxgenjs';
import { TemplateGenerator, Theme } from '../base';

/** Giao diện dữ liệu trang kết thúc */
export interface EndingData {
  /** Tiêu đề chính (như "Xin cảm ơn") */
  title?: string;
  /** Tiêu đề phụ */
  subtitle?: string;
  /** Tên công ty */
  company?: string;
  /** Website */
  website?: string;
  /** Email */
  email?: string;
  /** Điện thoại */
  phone?: string;
  /** Địa chỉ */
  address?: string;
  /** Mô tả mã QR */
  qrDescription?: string;
  /** Mạng xã hội */
  social?: { platform: string; handle: string }[];
}

/** Lớp trang kết thúc cơ sở */
abstract class BaseEnding {
  protected generator: TemplateGenerator;
  protected theme: Theme;

  constructor(generator: TemplateGenerator, theme: Theme) {
    this.generator = generator;
    this.theme = theme;
  }

  /** Tạo trang kết thúc */
  abstract generate(data: EndingData): pptxgen.Slide;
}

/**
 * Trang cảm ơn (Thank You)
 * Trang cảm ơn tinh tế và trang nhã
 */
export class ThankYou extends BaseEnding {
  constructor(generator: TemplateGenerator, theme: Theme) {
    super(generator, theme);
  }

  generate(data: EndingData): pptxgen.Slide {
    const slide = this.generator.createSlide();
    const pptx = this.generator.getPresentation();

    // Nền tối
    slide.background = { fill: this.theme.darkBg };

    // Vòng tròn trang trí
    slide.addShape(this.generator.getShapes().OVAL as any, {
      x: 5.165,
      y: 1.5,
      w: 3,
      h: 3,
      line: { color: this.theme.primary, width: 1, transparency: 60 },
      fill: { color: '000000', transparency: 100 },
    });

    slide.addShape(this.generator.getShapes().OVAL as any, {
      x: 4.665,
      y: 1.0,
      w: 4,
      h: 4,
      line: { color: this.theme.secondary, width: 0.5, transparency: 70 },
      fill: { color: '000000', transparency: 100 },
    });

    // Tiêu đề chính
    this.generator.addText(slide, {
      x: 1,
      y: 2.5,
      w: 11.33,
      h: 1.5,
      text: data.title || 'Xin cảm ơn',
      fontSize: 52,
      fontFace: 'Arial',
      color: 'FFFFFF',
      bold: true,
      align: 'center',
      valign: 'middle',
    });

    // Đường trang trí
    slide.addShape(this.generator.getShapes().LINE as any, {
      x: 5.165,
      y: 4.1,
      w: 3,
      h: 0,
      line: { color: this.theme.accent, width: 2 },
    });

    // Tiêu đề phụ
    this.generator.addText(slide, {
      x: 1,
      y: 4.3,
      w: 11.33,
      h: 0.8,
      text: data.subtitle || 'Thank You',
      fontSize: 22,
      fontFace: 'Arial',
      color: this.theme.primary,
      align: 'center',
      valign: 'middle',
    });

    // Tên công ty
    if (data.company) {
      this.generator.addText(slide, {
        x: 1,
        y: 5.5,
        w: 11.33,
        h: 0.5,
        text: data.company,
        fontSize: 14,
        fontFace: 'Arial',
        color: '999999',
        align: 'center',
        valign: 'middle',
      });
    }

    return slide;
  }
}

/**
 * Trang mã QR (QRCode)
 * Gồm khung giữ chỗ mã QR và thông tin liên hệ
 */
export class QRCode extends BaseEnding {
  constructor(generator: TemplateGenerator, theme: Theme) {
    super(generator, theme);
  }

  generate(data: EndingData): pptxgen.Slide {
    const slide = this.generator.createSlide();
    const pptx = this.generator.getPresentation();

    slide.background = { fill: this.theme.background };

    // Khu vực nền tối bên trái
    slide.addShape(this.generator.getShapes().RECTANGLE as any, {
      x: 0,
      y: 0,
      w: 5,
      h: 7.5,
      fill: { color: this.theme.primary },
    });

    // Tiêu đề bên trái
    this.generator.addText(slide, {
      x: 0.5,
      y: 2,
      w: 4,
      h: 1,
      text: data.title || 'Liên hệ với chúng tôi',
      fontSize: 30,
      fontFace: 'Arial',
      color: 'FFFFFF',
      bold: true,
      align: 'center',
      valign: 'middle',
    });

    // Đường trang trí bên trái
    slide.addShape(this.generator.getShapes().LINE as any, {
      x: 1.5,
      y: 3.2,
      w: 2,
      h: 0,
      line: { color: 'FFFFFF', width: 2, transparency: 50 },
    });

    // Tên công ty bên trái
    if (data.company) {
      this.generator.addText(slide, {
        x: 0.5,
        y: 3.5,
        w: 4,
        h: 0.5,
        text: data.company,
        fontSize: 14,
        fontFace: 'Arial',
        color: 'CCCCCC',
        align: 'center',
        valign: 'middle',
      });
    }

    // Vùng giữ chỗ mã QR bên phải
    const qrX = 6.5;
    const qrY = 1.5;
    const qrSize = 2.5;

    slide.addShape(this.generator.getShapes().RECTANGLE as any, {
      x: qrX,
      y: qrY,
      w: qrSize,
      h: qrSize,
      fill: { color: 'FFFFFF' },
      rectRadius: 0.1,
      line: { color: this.theme.muted, width: 1 },
    });

    // Khung giữ chỗ mã QR
    this.generator.addText(slide, {
      x: qrX,
      y: qrY + qrSize / 2 - 0.3,
      w: qrSize,
      h: 0.6,
      text: '[Mã QR]',
      fontSize: 14,
      fontFace: 'Arial',
      color: this.theme.muted,
      align: 'center',
      valign: 'middle',
    });

    // Mô tả mã QR
    this.generator.addText(slide, {
      x: qrX,
      y: qrY + qrSize + 0.2,
      w: qrSize,
      h: 0.4,
      text: data.qrDescription || 'Quét mã kết nối',
      fontSize: 11,
      fontFace: 'Arial',
      color: this.theme.muted,
      align: 'center',
      valign: 'top',
    });

    // Thông tin liên hệ
    const infoItems: Array<{ icon: string; text: string }> = [];
    if (data.email) infoItems.push({ icon: 'Email', text: data.email });
    if (data.phone) infoItems.push({ icon: 'Tel', text: data.phone });
    if (data.website) infoItems.push({ icon: 'Web', text: data.website });
    if (data.address) infoItems.push({ icon: 'Addr', text: data.address });

    infoItems.forEach((item, i) => {
      const y = 4.5 + i * 0.6;

      // Khung tròn biểu tượng
      slide.addShape(this.generator.getShapes().OVAL as any, {
        x: qrX,
        y: y,
        w: 0.4,
        h: 0.4,
        fill: { color: this.theme.primary, transparency: 85 },
      });

      this.generator.addText(slide, {
        x: qrX,
        y: y,
        w: 0.4,
        h: 0.4,
        text: item.icon.charAt(0),
        fontSize: 10,
        fontFace: 'Arial',
        color: this.theme.primary,
        bold: true,
        align: 'center',
        valign: 'middle',
      });

      // Văn bản thông tin
      this.generator.addText(slide, {
        x: qrX + 0.6,
        y: y,
        w: 4,
        h: 0.4,
        text: item.text,
        fontSize: 12,
        fontFace: 'Arial',
        color: this.theme.text,
        align: 'left',
        valign: 'middle',
      });
    });

    return slide;
  }
}

/**
 * Trang thông tin liên hệ (Contact)
 * Trình bày tập trung và đầy đủ các kênh liên hệ
 */
export class Contact extends BaseEnding {
  constructor(generator: TemplateGenerator, theme: Theme) {
    super(generator, theme);
  }

  generate(data: EndingData): pptxgen.Slide {
    const slide = this.generator.createSlide();
    const pptx = this.generator.getPresentation();

    slide.background = { fill: this.theme.background };

    // Dải trang trí trên cùng
    slide.addShape(this.generator.getShapes().RECTANGLE as any, {
      x: 0,
      y: 0,
      w: 13.33,
      h: 0.1,
      fill: { color: this.theme.primary },
    });

    // Tiêu đề
    this.generator.addText(slide, {
      x: 0.5,
      y: 0.8,
      w: 12,
      h: 1,
      text: data.title || 'Thông tin liên hệ',
      fontSize: 32,
      fontFace: 'Arial',
      color: this.theme.primary,
      bold: true,
      align: 'center',
      valign: 'middle',
    });

    // Tiêu đề phụ
    this.generator.addText(slide, {
      x: 0.5,
      y: 1.8,
      w: 12,
      h: 0.5,
      text: data.subtitle || 'Rất hân hạnh được hợp tác cùng Quý đối tác',
      fontSize: 16,
      fontFace: 'Arial',
      color: this.theme.muted,
      align: 'center',
      valign: 'middle',
    });

    // Đường trang trí
    slide.addShape(this.generator.getShapes().LINE as any, {
      x: 5.165,
      y: 2.5,
      w: 3,
      h: 0,
      line: { color: this.theme.accent, width: 2 },
    });

    // Lưới thông tin liên hệ
    const infoGrid: Array<{ label: string; value: string; icon: string }> = [
      { label: 'Công ty', value: data.company || '-', icon: 'C' },
      { label: 'Website', value: data.website || '-', icon: 'W' },
      { label: 'Email', value: data.email || '-', icon: 'E' },
      { label: 'Điện thoại', value: data.phone || '-', icon: 'T' },
      { label: 'Địa chỉ', value: data.address || '-', icon: 'A' },
    ];

    const cols = 2;
    const cardW = 5.5;
    const cardH = 0.9;
    const startX = 1.5;
    const startY = 3.0;
    const gapX = 4.5;
    const gapY = 0.2;

    infoGrid.forEach((item, i) => {
      const col = i % cols;
      const row = Math.floor(i / cols);
      const x = startX + col * gapX;
      const y = startY + row * (cardH + gapY);

      // Nền
      slide.addShape(this.generator.getShapes().RECTANGLE as any, {
        x: x,
        y: y,
        w: cardW,
        h: cardH,
        fill: { color: 'FFFFFF' },
        rectRadius: 0.05,
        shadow: {
          type: 'outer' as any,
          color: '000000',
          blur: 4,
          offset: 1,
          angle: 135,
          opacity: 0.06,
        },
      });

      // Khung tròn biểu tượng
      slide.addShape(this.generator.getShapes().OVAL as any, {
        x: x + 0.2,
        y: y + (cardH - 0.5) / 2,
        w: 0.5,
        h: 0.5,
        fill: { color: this.theme.primary },
      });

      this.generator.addText(slide, {
        x: x + 0.2,
        y: y + (cardH - 0.5) / 2,
        w: 0.5,
        h: 0.5,
        text: item.icon,
        fontSize: 14,
        fontFace: 'Arial',
        color: 'FFFFFF',
        bold: true,
        align: 'center',
        valign: 'middle',
      });

      // Nhãn
      this.generator.addText(slide, {
        x: x + 0.9,
        y: y + 0.05,
        w: 1.5,
        h: 0.35,
        text: item.label,
        fontSize: 11,
        fontFace: 'Arial',
        color: this.theme.muted,
        align: 'left',
        valign: 'middle',
      });

      // Giá trị
      this.generator.addText(slide, {
        x: x + 0.9,
        y: y + 0.4,
        w: cardW - 1.2,
        h: 0.4,
        text: item.value,
        fontSize: 14,
        fontFace: 'Arial',
        color: this.theme.text,
        bold: true,
        align: 'left',
        valign: 'middle',
      });
    });

    // Mạng xã hội
    if (data.social && data.social.length > 0) {
      const socialY = 5.5;
      const socialStartX = (13.33 - data.social.length * 1.5) / 2;

      this.generator.addText(slide, {
        x: 0.5,
        y: socialY - 0.3,
        w: 12,
        h: 0.4,
        text: 'Theo dõi chúng tôi',
        fontSize: 12,
        fontFace: 'Arial',
        color: this.theme.muted,
        align: 'center',
        valign: 'middle',
      });

      data.social.forEach((s, i) => {
        const x = socialStartX + i * 1.5;

        slide.addShape(this.generator.getShapes().OVAL as any, {
          x: x,
          y: socialY + 0.2,
          w: 0.6,
          h: 0.6,
          fill: { color: this.theme.primary },
        });

        this.generator.addText(slide, {
          x: x,
          y: socialY + 0.2,
          w: 0.6,
          h: 0.6,
          text: s.platform.charAt(0),
          fontSize: 14,
          fontFace: 'Arial',
          color: 'FFFFFF',
          bold: true,
          align: 'center',
          valign: 'middle',
        });

        this.generator.addText(slide, {
          x: x - 0.2,
          y: socialY + 0.9,
          w: 1,
          h: 0.3,
          text: s.handle,
          fontSize: 8,
          fontFace: 'Arial',
          color: this.theme.muted,
          align: 'center',
          valign: 'middle',
        });
      });
    }

    return slide;
  }
}
