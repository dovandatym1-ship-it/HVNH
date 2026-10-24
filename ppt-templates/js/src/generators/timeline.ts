/**
 * Mô-đun bộ tạo dòng thời gian (Timeline)
 * Bao gồm 4 mẫu dòng thời gian phong cách đa dạng:
 * - Dòng thời gian sóng đôi, Dòng thời gian ngang, Dòng thời gian dọc, Dòng thời gian xoắn ốc
 */

import pptxgen from 'pptxgenjs';
import { TemplateGenerator, Theme } from '../base';

/** Giao diện dữ liệu từng mục mốc thời gian */
export interface TimelineItem {
  /** Thời gian / Ngày tháng */
  date: string;
  /** Tiêu đề */
  title: string;
  /** Mô tả */
  description?: string;
  /** Có làm nổi bật hay không */
  highlight?: boolean;
}

/** Giao diện dữ liệu toàn trang dòng thời gian */
export interface TimelineData {
  /** Tiêu đề trang */
  pageTitle: string;
  /** Danh sách các mốc thời gian */
  items: TimelineItem[];
}

/** Lớp dòng thời gian cơ sở */
abstract class BaseTimeline {
  protected generator: TemplateGenerator;
  protected theme: Theme;

  constructor(generator: TemplateGenerator, theme: Theme) {
    this.generator = generator;
    this.theme = theme;
  }

  /** Tạo trang dòng thời gian */
  abstract generate(data: TimelineData): pptxgen.Slide;

  /** Thêm tiêu đề trang */
  protected addPageTitle(slide: pptxgen.Slide, title: string): void {
    this.generator.addText(slide, {
      x: 0.5,
      y: 0.3,
      w: 12,
      h: 0.7,
      text: title,
      fontSize: 24,
      fontFace: 'Arial',
      color: this.theme.primary,
      bold: true,
      align: 'left',
      valign: 'middle',
    });
  }
}

/**
 * Dòng thời gian sóng đôi (Dual Wave Timeline)
 * Các mốc thời gian sắp xếp so le trên dưới, mô phỏng hiệu ứng lượn sóng
 */
export class DualWave extends BaseTimeline {
  constructor(generator: TemplateGenerator, theme: Theme) {
    super(generator, theme);
  }

  generate(data: TimelineData): pptxgen.Slide {
    const slide = this.generator.createSlide();
    const pptx = this.generator.getPresentation();

    slide.background = { fill: this.theme.background };

    // Tiêu đề trang
    this.addPageTitle(slide, data.pageTitle);

    const items = data.items;
    const totalWidth = 11.5;
    const startX = 0.9;
    const topY = 1.8;
    const bottomY = 4.8;
    const spacing = totalWidth / Math.max(items.length - 1, 1);

    // Trục sóng trung tâm (nằm ngang)
    const waveY = 3.75;
    slide.addShape(this.generator.getShapes().LINE as any, {
      x: startX,
      y: waveY,
      w: totalWidth,
      h: 0,
      line: { color: this.theme.primary, width: 3 },
    });

    items.forEach((item, i) => {
      const x = startX + i * spacing;
      const isTop = i % 2 === 0;
      const cardY = isTop ? topY : bottomY;
      const cardW = 2.2;
      const cardH = 1.5;

      // Đường liên kết dọc
      slide.addShape(this.generator.getShapes().LINE as any, {
        x: x + cardW / 2,
        y: isTop ? cardY + cardH : waveY,
        w: 0,
        h: isTop ? waveY - cardY - cardH : cardY - waveY,
        line: { color: this.theme.secondary, width: 1.5 },
      });

      // Điểm mốc thời gian
      slide.addShape(this.generator.getShapes().OVAL as any, {
        x: x + cardW / 2 - 0.15,
        y: waveY - 0.15,
        w: 0.3,
        h: 0.3,
        fill: { color: item.highlight ? this.theme.accent : this.theme.primary },
      });

      // Thẻ
      slide.addShape(this.generator.getShapes().RECTANGLE as any, {
        x: x,
        y: cardY,
        w: cardW,
        h: cardH,
        fill: { color: 'FFFFFF' },
        rectRadius: 0.08,
        shadow: {
          type: 'outer' as any,
          color: '000000',
          blur: 6,
          offset: 2,
          angle: 135,
          opacity: 0.1,
        },
      });

      // Ngày tháng
      this.generator.addText(slide, {
        x: x + 0.1,
        y: cardY + 0.1,
        w: cardW - 0.2,
        h: 0.35,
        text: item.date,
        fontSize: 11,
        fontFace: 'Arial',
        color: item.highlight ? this.theme.accent : this.theme.primary,
        bold: true,
        align: 'center',
        valign: 'middle',
      });

      // Tiêu đề
      this.generator.addText(slide, {
        x: x + 0.1,
        y: cardY + 0.45,
        w: cardW - 0.2,
        h: 0.35,
        text: item.title,
        fontSize: 12,
        fontFace: 'Arial',
        color: this.theme.text,
        bold: true,
        align: 'center',
        valign: 'middle',
      });

      // Mô tả
      if (item.description) {
        this.generator.addText(slide, {
          x: x + 0.1,
          y: cardY + 0.85,
          w: cardW - 0.2,
          h: 0.55,
          text: item.description,
          fontSize: 9,
          fontFace: 'Arial',
          color: this.theme.muted,
          align: 'center',
          valign: 'top',
          wrap: true,
        });
      }
    });

    return slide;
  }
}

/**
 * Dòng thời gian ngang (Horizontal Timeline)
 * Trục thời gian tuyến tính cổ điển chạy từ trái sang phải
 */
export class Horizontal extends BaseTimeline {
  constructor(generator: TemplateGenerator, theme: Theme) {
    super(generator, theme);
  }

  generate(data: TimelineData): pptxgen.Slide {
    const slide = this.generator.createSlide();
    const pptx = this.generator.getPresentation();

    slide.background = { fill: this.theme.background };

    // Tiêu đề trang
    this.addPageTitle(slide, data.pageTitle);

    const items = data.items;
    const lineY = 3.5;
    const startX = 0.8;
    const endX = 12.5;
    const totalWidth = endX - startX;

    // Trục đường chính nằm ngang
    slide.addShape(this.generator.getShapes().LINE as any, {
      x: startX,
      y: lineY,
      w: totalWidth,
      h: 0,
      line: { color: this.theme.primary, width: 3 },
    });

    // Mũi tên điểm bắt đầu
    slide.addShape(this.generator.getShapes().OVAL as any, {
      x: startX - 0.1,
      y: lineY - 0.1,
      w: 0.2,
      h: 0.2,
      fill: { color: this.theme.primary },
    });

    // Mũi tên điểm kết thúc
    slide.addShape(this.generator.getShapes().OVAL as any, {
      x: endX - 0.1,
      y: lineY - 0.1,
      w: 0.2,
      h: 0.2,
      fill: { color: this.theme.accent },
    });

    const spacing = totalWidth / (items.length + 1);

    items.forEach((item, i) => {
      const x = startX + spacing * (i + 1);
      const isAbove = i % 2 === 0;
      const cardW = 2;
      const cardH = 1.2;

      // Điểm mốc
      slide.addShape(this.generator.getShapes().OVAL as any, {
        x: x - 0.15,
        y: lineY - 0.15,
        w: 0.3,
        h: 0.3,
        fill: { color: item.highlight ? this.theme.accent : this.theme.primary },
      });

      // Đường liên kết dọc
      const lineStart = isAbove ? lineY - 0.3 : lineY + 0.3;
      const lineLen = isAbove ? 0.8 : 0.8;

      slide.addShape(this.generator.getShapes().LINE as any, {
        x: x,
        y: lineStart,
        w: 0,
        h: lineLen,
        line: { color: this.theme.secondary, width: 1 },
      });

      // Vị trí thẻ
      const cardX = x - cardW / 2;
      const cardY = isAbove ? lineY - 0.3 - lineLen - cardH : lineY + 0.3 + lineLen;

      // Nền thẻ
      slide.addShape(this.generator.getShapes().RECTANGLE as any, {
        x: cardX,
        y: cardY,
        w: cardW,
        h: cardH,
        fill: { color: 'FFFFFF' },
        rectRadius: 0.05,
        shadow: {
          type: 'outer' as any,
          color: '000000',
          blur: 5,
          offset: 2,
          angle: 135,
          opacity: 0.08,
        },
      });

      // Ngày tháng
      this.generator.addText(slide, {
        x: cardX + 0.05,
        y: cardY + 0.05,
        w: cardW - 0.1,
        h: 0.3,
        text: item.date,
        fontSize: 10,
        fontFace: 'Arial',
        color: this.theme.primary,
        bold: true,
        align: 'center',
        valign: 'middle',
      });

      // Tiêu đề
      this.generator.addText(slide, {
        x: cardX + 0.05,
        y: cardY + 0.35,
        w: cardW - 0.1,
        h: 0.3,
        text: item.title,
        fontSize: 11,
        fontFace: 'Arial',
        color: this.theme.text,
        bold: true,
        align: 'center',
        valign: 'middle',
      });

      // Mô tả
      if (item.description) {
        this.generator.addText(slide, {
          x: cardX + 0.05,
          y: cardY + 0.65,
          w: cardW - 0.1,
          h: 0.5,
          text: item.description,
          fontSize: 8,
          fontFace: 'Arial',
          color: this.theme.muted,
          align: 'center',
          valign: 'top',
          wrap: true,
        });
      }
    });

    return slide;
  }
}

/**
 * Dòng thời gian dọc (Vertical Timeline)
 * Trục thời gian dạng thác đổ chạy từ trên xuống dưới
 */
export class Vertical extends BaseTimeline {
  constructor(generator: TemplateGenerator, theme: Theme) {
    super(generator, theme);
  }

  generate(data: TimelineData): pptxgen.Slide {
    const slide = this.generator.createSlide();
    const pptx = this.generator.getPresentation();

    slide.background = { fill: this.theme.background };

    // Tiêu đề trang
    this.addPageTitle(slide, data.pageTitle);

    const items = data.items;
    const lineX = 6.665;
    const startY = 1.4;
    const itemSpacing = 1.15;

    // Trục đường chính thẳng đứng
    slide.addShape(this.generator.getShapes().LINE as any, {
      x: lineX,
      y: startY,
      w: 0,
      h: items.length * itemSpacing + 0.3,
      line: { color: this.theme.primary, width: 3 },
    });

    items.forEach((item, i) => {
      const y = startY + i * itemSpacing;
      const isLeft = i % 2 === 0;
      const cardW = 4.5;
      const cardH = 0.9;

      // Vòng tròn điểm mốc
      slide.addShape(this.generator.getShapes().OVAL as any, {
        x: lineX - 0.2,
        y: y + 0.15,
        w: 0.4,
        h: 0.4,
        fill: { color: item.highlight ? this.theme.accent : this.theme.primary },
        line: { color: 'FFFFFF', width: 2 },
      });

      // Thẻ
      const cardX = isLeft ? lineX - cardW - 0.5 : lineX + 0.5;

      slide.addShape(this.generator.getShapes().RECTANGLE as any, {
        x: cardX,
        y: y,
        w: cardW,
        h: cardH,
        fill: { color: 'FFFFFF' },
        rectRadius: 0.05,
        shadow: {
          type: 'outer' as any,
          color: '000000',
          blur: 4,
          offset: 2,
          angle: 135,
          opacity: 0.08,
        },
      });

      // Dải màu bên trái
      slide.addShape(this.generator.getShapes().RECTANGLE as any, {
        x: cardX,
        y: y,
        w: 0.06,
        h: cardH,
        fill: { color: item.highlight ? this.theme.accent : this.theme.primary },
      });

      // Ngày tháng
      this.generator.addText(slide, {
        x: cardX + 0.2,
        y: y + 0.05,
        w: 1.2,
        h: 0.3,
        text: item.date,
        fontSize: 10,
        fontFace: 'Arial',
        color: this.theme.primary,
        bold: true,
        align: isLeft ? 'right' : 'left',
        valign: 'middle',
      });

      // Tiêu đề
      this.generator.addText(slide, {
        x: cardX + 1.5,
        y: y + 0.05,
        w: cardW - 1.7,
        h: 0.3,
        text: item.title,
        fontSize: 13,
        fontFace: 'Arial',
        color: this.theme.text,
        bold: true,
        align: isLeft ? 'right' : 'left',
        valign: 'middle',
      });

      // Mô tả
      if (item.description) {
        this.generator.addText(slide, {
          x: cardX + 0.2,
          y: y + 0.4,
          w: cardW - 0.4,
          h: 0.45,
          text: item.description,
          fontSize: 10,
          fontFace: 'Arial',
          color: this.theme.muted,
          align: isLeft ? 'right' : 'left',
          valign: 'top',
          wrap: true,
        });
      }
    });

    return slide;
  }
}

/**
 * Dòng thời gian xoắn ốc (Spiral Timeline)
 * Sắp xếp các mốc thời gian theo quỹ đạo xoắn ốc độc đáo
 */
export class Spiral extends BaseTimeline {
  constructor(generator: TemplateGenerator, theme: Theme) {
    super(generator, theme);
  }

  generate(data: TimelineData): pptxgen.Slide {
    const slide = this.generator.createSlide();
    const pptx = this.generator.getPresentation();

    slide.background = { fill: this.theme.background };

    // Tiêu đề trang
    this.addPageTitle(slide, data.pageTitle);

    const items = data.items;
    const centerX = 6.665;
    const centerY = 4.2;
    const maxRadius = 2.8;

    // Đường trang trí xoắn ốc (mô phỏng bằng các vòng tròn đồng tâm)
    for (let r = 0.8; r <= maxRadius; r += 0.5) {
      slide.addShape(this.generator.getShapes().OVAL as any, {
        x: centerX - r,
        y: centerY - r * 0.6,
        w: r * 2,
        h: r * 1.2,
        line: { color: this.theme.primary, width: 0.5, transparency: 70 },
        fill: { color: '000000', transparency: 100 },
      });
    }

    // Các mục sắp xếp theo quỹ đạo xoắn ốc
    items.forEach((item, i) => {
      const angle = (i / items.length) * 2 * Math.PI - Math.PI / 2;
      const radius = 0.8 + (i / items.length) * (maxRadius - 0.8);
      const x = centerX + radius * Math.cos(angle) - 1;
      const y = centerY + radius * 0.6 * Math.sin(angle) - 0.35;

      // Điểm mốc
      slide.addShape(this.generator.getShapes().OVAL as any, {
        x: x + 0.8,
        y: y + 0.25,
        w: 0.3,
        h: 0.3,
        fill: { color: item.highlight ? this.theme.accent : this.theme.primary },
      });

      // Đường nối về trung tâm
      slide.addShape(this.generator.getShapes().LINE as any, {
        x: x + 0.95,
        y: y + 0.4,
        w: centerX - x - 0.95,
        h: centerY - y - 0.4,
        line: { color: this.theme.secondary, width: 0.5, transparency: 60 },
      });

      // Ngày tháng
      this.generator.addText(slide, {
        x: x,
        y: y - 0.15,
        w: 2,
        h: 0.3,
        text: item.date,
        fontSize: 9,
        fontFace: 'Arial',
        color: this.theme.primary,
        bold: true,
        align: 'center',
        valign: 'middle',
      });

      // Tiêu đề
      this.generator.addText(slide, {
        x: x,
        y: y + 0.6,
        w: 2,
        h: 0.3,
        text: item.title,
        fontSize: 11,
        fontFace: 'Arial',
        color: this.theme.text,
        bold: true,
        align: 'center',
        valign: 'middle',
      });
    });

    // Nhãn trung tâm
    slide.addShape(this.generator.getShapes().OVAL as any, {
      x: centerX - 0.6,
      y: centerY - 0.4,
      w: 1.2,
      h: 0.8,
      fill: { color: this.theme.primary },
    });

    this.generator.addText(slide, {
      x: centerX - 0.6,
      y: centerY - 0.4,
      w: 1.2,
      h: 0.8,
      text: 'Dòng thời gian',
      fontSize: 12,
      fontFace: 'Arial',
      color: 'FFFFFF',
      bold: true,
      align: 'center',
      valign: 'middle',
    });

    return slide;
  }
}
