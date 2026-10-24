/**
 * Mô-đun bộ tạo trang mục lục (Directory)
 * Bao gồm 6 mẫu trang mục lục phong cách đa dạng:
 * - Mục lục hình thoi hoạt họa, Mục lục vòng tròn, Mục lục lục giác
 * - Mục lục thanh bên, Mục lục thẻ lưới, Mục lục dòng thời gian
 */

import pptxgen from 'pptxgenjs';
import { TemplateGenerator, Theme } from '../base';
import { createCirclePositions, createGridPositions } from '../utils';

/** Giao diện dữ liệu mục lục */
export interface DirectoryItem {
  /** Số thứ tự */
  index: number;
  /** Tiêu đề */
  title: string;
  /** Mô tả */
  description?: string;
  /** Biểu tượng (tùy chọn) */
  icon?: string;
}

/** Giao diện dữ liệu toàn trang mục lục */
export interface DirectoryData {
  /** Tiêu đề trang */
  pageTitle?: string;
  /** Danh sách các mục */
  items: DirectoryItem[];
}

/** Lớp mục lục cơ sở */
abstract class BaseDirectory {
  protected generator: TemplateGenerator;
  protected theme: Theme;

  constructor(generator: TemplateGenerator, theme: Theme) {
    this.generator = generator;
    this.theme = theme;
  }

  /** Tạo trang mục lục */
  abstract generate(data: DirectoryData): pptxgen.Slide;

  /** Thêm tiêu đề trang */
  protected addPageTitle(slide: pptxgen.Slide, title: string): void {
    this.generator.addText(slide, {
      x: 0.5,
      y: 0.3,
      w: 12,
      h: 0.8,
      text: title,
      fontSize: 28,
      fontFace: 'Arial',
      color: this.theme.primary,
      bold: true,
      align: 'left',
      valign: 'middle',
    });
  }

  /** Thêm đường trang trí trang */
  protected addUnderline(slide: pptxgen.Slide, x: number, y: number, width: number): void {
    this.generator.getPresentation();
    slide.addShape((this.generator.getShapes().LINE as any), {
      x: x,
      y: y,
      w: width,
      h: 0,
      line: { color: this.theme.accent, width: 3 },
    });
  }
}

/**
 * Mục lục hoạt họa hình thoi (Diamond Animated)
 * Sử dụng hình thoi đánh số thứ tự tạo cảm giác chiều sâu
 */
export class DiamondAnimated extends BaseDirectory {
  constructor(generator: TemplateGenerator, theme: Theme) {
    super(generator, theme);
  }

  generate(data: DirectoryData): pptxgen.Slide {
    const slide = this.generator.createSlide();
    const pptx = this.generator.getPresentation();

    slide.background = { fill: this.theme.background };

    // Tiêu đề trang
    this.addPageTitle(slide, data.pageTitle || 'Mục lục');
    this.addUnderline(slide, 0.5, 1.1, 2);

    const items = data.items;
    const startY = 1.8;
    const itemHeight = 0.85;

    items.forEach((item, i) => {
      const y = startY + i * itemHeight;

      // Nền hình thoi đánh số
      slide.addShape(this.generator.getShapes().RECTANGLE as any, {
        x: 0.8,
        y: y,
        w: 0.5,
        h: 0.5,
        fill: { color: this.theme.primary },
        rotate: 45,
      });

      // Văn bản số thứ tự
      this.generator.addText(slide, {
        x: 0.8,
        y: y,
        w: 0.5,
        h: 0.5,
        text: String(item.index),
        fontSize: 14,
        fontFace: 'Arial',
        color: 'FFFFFF',
        bold: true,
        align: 'center',
        valign: 'middle',
      });

      // Tiêu đề
      this.generator.addText(slide, {
        x: 1.8,
        y: y - 0.05,
        w: 5,
        h: 0.35,
        text: item.title,
        fontSize: 18,
        fontFace: 'Arial',
        color: this.theme.text,
        bold: true,
        align: 'left',
        valign: 'middle',
      });

      // Mô tả
      if (item.description) {
        this.generator.addText(slide, {
          x: 1.8,
          y: y + 0.3,
          w: 5,
          h: 0.3,
          text: item.description,
          fontSize: 11,
          fontFace: 'Arial',
          color: this.theme.muted,
          align: 'left',
          valign: 'top',
        });
      }

      // Đường liên kết
      if (i < items.length - 1) {
        slide.addShape(this.generator.getShapes().LINE as any, {
          x: 1.05,
          y: y + 0.5,
          w: 0,
          h: itemHeight - 0.5,
          line: { color: this.theme.secondary, width: 1, dashType: 'dash' as any },
        });
      }
    });

    // Trang trí bên phải
    slide.addShape(this.generator.getShapes().RECTANGLE as any, {
      x: 10,
      y: 0,
      w: 3.33,
      h: 7.5,
      fill: { color: this.theme.primary, transparency: 90 },
    });

    // Số thứ tự lớn trang trí bên phải
    if (items.length > 0) {
      this.generator.addText(slide, {
        x: 10.5,
        y: 2,
        w: 2.5,
        h: 3.5,
        text: String(items.length).padStart(2, '0'),
        fontSize: 100,
        fontFace: 'Arial',
        color: this.theme.primary,
        bold: true,
        align: 'center',
        valign: 'middle',
      });
    }

    return slide;
  }
}

/**
 * Mục lục vòng tròn (Circular Ring)
 * Sắp xếp các mục mục lục theo bố cục tỏa tròn
 */
export class CircularRing extends BaseDirectory {
  constructor(generator: TemplateGenerator, theme: Theme) {
    super(generator, theme);
  }

  generate(data: DirectoryData): pptxgen.Slide {
    const slide = this.generator.createSlide();
    const pptx = this.generator.getPresentation();

    slide.background = { fill: this.theme.background };

    // Tiêu đề trang
    this.addPageTitle(slide, data.pageTitle || 'Mục lục');
    this.addUnderline(slide, 0.5, 1.1, 2);

    const items = data.items;
    const centerX = 6.665;
    const centerY = 4.2;
    const radius = 2.5;

    const positions = createCirclePositions(centerX, centerY, radius, items.length);

    items.forEach((item, i) => {
      const pos = positions[i];
      const nodeSize = 1.4;

      // Nút tròn
      slide.addShape(this.generator.getShapes().OVAL as any, {
        x: pos.x - nodeSize / 2,
        y: pos.y - nodeSize / 2,
        w: nodeSize,
        h: nodeSize,
        fill: { color: i === 0 ? this.theme.primary : this.theme.secondary },
        shadow: {
          type: 'outer' as any,
          color: '000000',
          blur: 5,
          offset: 2,
          angle: 135,
          opacity: 0.1,
        },
      });

      // Số thứ tự
      this.generator.addText(slide, {
        x: pos.x - nodeSize / 2,
        y: pos.y - nodeSize / 2 - 0.1,
        w: nodeSize,
        h: 0.5,
        text: String(item.index),
        fontSize: 18,
        fontFace: 'Arial',
        color: 'FFFFFF',
        bold: true,
        align: 'center',
        valign: 'middle',
      });

      // Tiêu đề
      this.generator.addText(slide, {
        x: pos.x - 1.2,
        y: pos.y + nodeSize / 2 - 0.1,
        w: 2.4,
        h: 0.4,
        text: item.title,
        fontSize: 12,
        fontFace: 'Arial',
        color: this.theme.text,
        bold: true,
        align: 'center',
        valign: 'top',
      });
    });

    // Tiêu đề trung tâm
    slide.addShape(this.generator.getShapes().OVAL as any, {
      x: centerX - 1,
      y: centerY - 1,
      w: 2,
      h: 2,
      fill: { color: this.theme.primary },
    });

    this.generator.addText(slide, {
      x: centerX - 1,
      y: centerY - 0.5,
      w: 2,
      h: 1,
      text: 'Mục lục',
      fontSize: 20,
      fontFace: 'Arial',
      color: 'FFFFFF',
      bold: true,
      align: 'center',
      valign: 'middle',
    });

    return slide;
  }
}

/**
 * Mục lục lục giác (Hexagon)
 * Hiển thị các mục mục lục theo dạng tổ ong lục giác hiện đại
 */
export class Hexagon extends BaseDirectory {
  constructor(generator: TemplateGenerator, theme: Theme) {
    super(generator, theme);
  }

  generate(data: DirectoryData): pptxgen.Slide {
    const slide = this.generator.createSlide();
    const pptx = this.generator.getPresentation();

    slide.background = { fill: this.theme.background };

    // Tiêu đề trang
    this.addPageTitle(slide, data.pageTitle || 'Mục lục');
    this.addUnderline(slide, 0.5, 1.1, 2);

    const items = data.items;
    const cols = 3;
    const rows = Math.ceil(items.length / cols);
    const hexSize = 1.2;
    const startX = 1.5;
    const startY = 2.0;
    const gapX = 3.5;
    const gapY = 2.5;

    items.forEach((item, i) => {
      const col = i % cols;
      const row = Math.floor(i / cols);
      const offsetX = row % 2 === 1 ? gapX / 2 : 0;
      const x = startX + col * gapX + offsetX;
      const y = startY + row * gapY;

      // Lục giác (mô phỏng bằng hình chữ nhật)
      slide.addShape(this.generator.getShapes().RECTANGLE as any, {
        x: x,
        y: y,
        w: hexSize * 2,
        h: hexSize * 1.73,
        fill: { color: i === 0 ? this.theme.primary : this.theme.secondary },
        rectRadius: 0.1,
        rotate: 30,
        shadow: {
          type: 'outer' as any,
          color: '000000',
          blur: 8,
          offset: 3,
          angle: 135,
          opacity: 0.12,
        },
      });

      // Số thứ tự
      this.generator.addText(slide, {
        x: x,
        y: y - 0.2,
        w: hexSize * 2,
        h: 0.5,
        text: String(item.index).padStart(2, '0'),
        fontSize: 16,
        fontFace: 'Arial',
        color: 'FFFFFF',
        bold: true,
        align: 'center',
        valign: 'middle',
      });

      // Tiêu đề
      this.generator.addText(slide, {
        x: x,
        y: y + 0.25,
        w: hexSize * 2,
        h: 0.4,
        text: item.title,
        fontSize: 12,
        fontFace: 'Arial',
        color: 'FFFFFF',
        bold: true,
        align: 'center',
        valign: 'middle',
      });
    });

    return slide;
  }
}

/**
 * Mục lục thanh bên (Sidebar)
 * Thanh điều hướng cố định bên trái + danh sách mục bên phải
 */
export class Sidebar extends BaseDirectory {
  constructor(generator: TemplateGenerator, theme: Theme) {
    super(generator, theme);
  }

  generate(data: DirectoryData): pptxgen.Slide {
    const slide = this.generator.createSlide();
    const pptx = this.generator.getPresentation();

    slide.background = { fill: this.theme.background };

    // Thanh nền tối bên trái
    slide.addShape(this.generator.getShapes().RECTANGLE as any, {
      x: 0,
      y: 0,
      w: 4,
      h: 7.5,
      fill: { color: this.theme.primary },
    });

    // Tiêu đề bên trái
    this.generator.addText(slide, {
      x: 0.5,
      y: 2,
      w: 3,
      h: 1,
      text: data.pageTitle || 'Mục lục',
      fontSize: 32,
      fontFace: 'Arial',
      color: 'FFFFFF',
      bold: true,
      align: 'left',
      valign: 'middle',
    });

    // Đường trang trí bên trái
    slide.addShape(this.generator.getShapes().LINE as any, {
      x: 0.5,
      y: 3.2,
      w: 2.5,
      h: 0,
      line: { color: 'FFFFFF', width: 2, transparency: 50 },
    });

    // Số lượng mục bên trái
    this.generator.addText(slide, {
      x: 0.5,
      y: 3.5,
      w: 3,
      h: 0.5,
      text: `Tổng cộng ${data.items.length} chương`,
      fontSize: 14,
      fontFace: 'Arial',
      color: 'CCCCCC',
      align: 'left',
      valign: 'top',
    });

    // Danh sách mục lục bên phải
    const items = data.items;
    const startY = 0.8;
    const itemHeight = 1.0;

    items.forEach((item, i) => {
      const y = startY + i * itemHeight;

      // Khung tròn số thứ tự
      slide.addShape(this.generator.getShapes().OVAL as any, {
        x: 5,
        y: y + 0.15,
        w: 0.5,
        h: 0.5,
        fill: { color: this.theme.primary },
      });

      this.generator.addText(slide, {
        x: 5,
        y: y + 0.15,
        w: 0.5,
        h: 0.5,
        text: String(item.index),
        fontSize: 12,
        fontFace: 'Arial',
        color: 'FFFFFF',
        bold: true,
        align: 'center',
        valign: 'middle',
      });

      // Tiêu đề
      this.generator.addText(slide, {
        x: 5.8,
        y: y + 0.05,
        w: 6.5,
        h: 0.35,
        text: item.title,
        fontSize: 16,
        fontFace: 'Arial',
        color: this.theme.text,
        bold: true,
        align: 'left',
        valign: 'middle',
      });

      // Mô tả
      if (item.description) {
        this.generator.addText(slide, {
          x: 5.8,
          y: y + 0.4,
          w: 6.5,
          h: 0.3,
          text: item.description,
          fontSize: 11,
          fontFace: 'Arial',
          color: this.theme.muted,
          align: 'left',
          valign: 'top',
        });
      }

      // Đường phân cách
      if (i < items.length - 1) {
        slide.addShape(this.generator.getShapes().LINE as any, {
          x: 5,
          y: y + itemHeight - 0.05,
          w: 7.5,
          h: 0,
          line: { color: this.theme.muted, width: 0.5, transparency: 50 },
        });
      }
    });

    return slide;
  }
}

/**
 * Mục lục thẻ lưới (Card Grid)
 * Hiển thị các mục mục lục theo bố cục lưới dạng thẻ
 */
export class CardGrid extends BaseDirectory {
  constructor(generator: TemplateGenerator, theme: Theme) {
    super(generator, theme);
  }

  generate(data: DirectoryData): pptxgen.Slide {
    const slide = this.generator.createSlide();
    const pptx = this.generator.getPresentation();

    slide.background = { fill: this.theme.background };

    // Tiêu đề trang
    this.addPageTitle(slide, data.pageTitle || 'Mục lục');
    this.addUnderline(slide, 0.5, 1.1, 2);

    const items = data.items;
    const cols = 3;
    const cardWidth = 3.5;
    const cardHeight = 2.5;
    const startX = 0.8;
    const startY = 1.8;
    const gapX = 0.5;
    const gapY = 0.4;

    items.forEach((item, i) => {
      const col = i % cols;
      const row = Math.floor(i / cols);
      const x = startX + col * (cardWidth + gapX);
      const y = startY + row * (cardHeight + gapY);

      // Nền thẻ
      slide.addShape(this.generator.getShapes().RECTANGLE as any, {
        x: x,
        y: y,
        w: cardWidth,
        h: cardHeight,
        fill: { color: 'FFFFFF' },
        rectRadius: 0.1,
        shadow: {
          type: 'outer' as any,
          color: '000000',
          blur: 8,
          offset: 3,
          angle: 135,
          opacity: 0.1,
        },
      });

      // Dải màu trên cùng
      slide.addShape(this.generator.getShapes().RECTANGLE as any, {
        x: x,
        y: y,
        w: cardWidth,
        h: 0.08,
        fill: { color: this.theme.primary },
        rectRadius: 0.1,
      });

      // Số thứ tự
      this.generator.addText(slide, {
        x: x + 0.3,
        y: y + 0.3,
        w: 0.6,
        h: 0.5,
        text: String(item.index).padStart(2, '0'),
        fontSize: 24,
        fontFace: 'Arial',
        color: this.theme.primary,
        bold: true,
        align: 'left',
        valign: 'middle',
      });

      // Tiêu đề
      this.generator.addText(slide, {
        x: x + 0.3,
        y: y + 0.9,
        w: cardWidth - 0.6,
        h: 0.4,
        text: item.title,
        fontSize: 16,
        fontFace: 'Arial',
        color: this.theme.text,
        bold: true,
        align: 'left',
        valign: 'middle',
      });

      // Mô tả
      if (item.description) {
        this.generator.addText(slide, {
          x: x + 0.3,
          y: y + 1.4,
          w: cardWidth - 0.6,
          h: 0.8,
          text: item.description,
          fontSize: 11,
          fontFace: 'Arial',
          color: this.theme.muted,
          align: 'left',
          valign: 'top',
          wrap: true,
        });
      }
    });

    return slide;
  }
}

/**
 * Mục lục dòng thời gian (Timeline Style)
 * Hiển thị cấu trúc mục lục theo trục thời gian dọc
 */
export class TimelineStyle extends BaseDirectory {
  constructor(generator: TemplateGenerator, theme: Theme) {
    super(generator, theme);
  }

  generate(data: DirectoryData): pptxgen.Slide {
    const slide = this.generator.createSlide();
    const pptx = this.generator.getPresentation();

    slide.background = { fill: this.theme.background };

    // Tiêu đề trang
    this.addPageTitle(slide, data.pageTitle || 'Mục lục');
    this.addUnderline(slide, 0.5, 1.1, 2);

    const items = data.items;
    const centerX = 6.665;
    const startY = 1.8;
    const itemHeight = 0.9;

    // Trục thời gian ở giữa
    slide.addShape(this.generator.getShapes().LINE as any, {
      x: centerX,
      y: startY,
      w: 0,
      h: items.length * itemHeight,
      line: { color: this.theme.primary, width: 3 },
    });

    items.forEach((item, i) => {
      const y = startY + i * itemHeight;
      const isLeft = i % 2 === 0;

      // Điểm mốc tròn trên trục thời gian
      slide.addShape(this.generator.getShapes().OVAL as any, {
        x: centerX - 0.2,
        y: y + 0.15,
        w: 0.4,
        h: 0.4,
        fill: { color: this.theme.primary },
        line: { color: 'FFFFFF', width: 2 },
      });

      // Đường liên kết
      const lineStart = isLeft ? centerX - 0.2 : centerX + 0.6;
      const lineWidth = isLeft ? 2 : 2;

      slide.addShape(this.generator.getShapes().LINE as any, {
        x: isLeft ? centerX - 2.5 : centerX + 0.6,
        y: y + 0.35,
        w: 2.3,
        h: 0,
        line: { color: this.theme.secondary, width: 1, dashType: 'dash' as any },
      });

      // Văn bản (so le trái phải)
      const textX = isLeft ? centerX - 6 : centerX + 1.5;
      const textAlign = isLeft ? 'right' as const : 'left' as const;

      // Số thứ tự
      this.generator.addText(slide, {
        x: textX,
        y: y + 0.05,
        w: 3.5,
        h: 0.35,
        text: `${String(item.index).padStart(2, '0')} - ${item.title}`,
        fontSize: 14,
        fontFace: 'Arial',
        color: this.theme.text,
        bold: true,
        align: textAlign,
        valign: 'middle',
      });

      // Mô tả
      if (item.description) {
        this.generator.addText(slide, {
          x: textX,
          y: y + 0.4,
          w: 3.5,
          h: 0.35,
          text: item.description,
          fontSize: 10,
          fontFace: 'Arial',
          color: this.theme.muted,
          align: textAlign,
          valign: 'top',
        });
      }
    });

    return slide;
  }
}
