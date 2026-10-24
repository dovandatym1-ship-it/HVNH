/**
 * Mô-đun bộ tạo trang nội dung (Content)
 * Bao gồm 5 mẫu nội dung phong cách đa dạng:
 * - Bố cục hình ảnh & chữ, Bố cục ba cột, Bố cục lưới 4 ô
 * - Lớp phủ toàn ảnh, Bố cục so sánh
 */

import pptxgen from 'pptxgenjs';
import { TemplateGenerator, Theme } from '../base';
import { createGridPositions } from '../utils';

/** Giao diện dữ liệu khối nội dung */
export interface ContentBlock {
  /** Tiêu đề */
  title: string;
  /** Văn bản nội dung */
  content?: string;
  /** Đường dẫn hình ảnh */
  image?: string;
  /** Số thứ tự / Mã số */
  index?: number;
}

/** Giao diện dữ liệu trang nội dung */
export interface ContentData {
  /** Tiêu đề trang */
  pageTitle: string;
  /** Các khối nội dung */
  blocks?: ContentBlock[];
  /** Văn bản nội dung chính */
  mainText?: string;
  /** Văn bản phụ */
  subText?: string;
  /** Đường dẫn hình ảnh */
  imagePath?: string;
}

/** Lớp nội dung cơ sở */
abstract class BaseContent {
  protected generator: TemplateGenerator;
  protected theme: Theme;

  constructor(generator: TemplateGenerator, theme: Theme) {
    this.generator = generator;
    this.theme = theme;
  }

  /** Tạo trang nội dung */
  abstract generate(data: ContentData): pptxgen.Slide;

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

    slide.addShape(this.generator.getShapes().LINE as any, {
      x: 0.5,
      y: 1.0,
      w: 2,
      h: 0,
      line: { color: this.theme.accent, width: 2 },
    });
  }
}

/**
 * Trang bố cục hình ảnh và văn bản (TextImageLayout)
 * Bố cục ảnh trái chữ phải hoặc chữ trái ảnh phải
 */
export class TextImageLayout extends BaseContent {
  constructor(generator: TemplateGenerator, theme: Theme) {
    super(generator, theme);
  }

  generate(data: ContentData): pptxgen.Slide {
    const slide = this.generator.createSlide();
    const pptx = this.generator.getPresentation();

    slide.background = { fill: this.theme.background };

    // Tiêu đề trang
    this.addPageTitle(slide, data.pageTitle);

    // Vùng giữ chỗ ảnh
    slide.addShape(this.generator.getShapes().RECTANGLE as any, {
      x: 0.5,
      y: 1.5,
      w: 5.5,
      h: 5.5,
      fill: { color: this.theme.primary, transparency: 85 },
      rectRadius: 0.1,
    });

    // Văn bản khung giữ chỗ ảnh
    this.generator.addText(slide, {
      x: 0.5,
      y: 3.5,
      w: 5.5,
      h: 1,
      text: '[Khung ảnh]',
      fontSize: 16,
      fontFace: 'Arial',
      color: this.theme.muted,
      align: 'center',
      valign: 'middle',
    });

    // Tiêu đề bên phải
    this.generator.addText(slide, {
      x: 6.5,
      y: 1.8,
      w: 6,
      h: 0.6,
      text: data.blocks?.[0]?.title || data.pageTitle,
      fontSize: 22,
      fontFace: 'Arial',
      color: this.theme.text,
      bold: true,
      align: 'left',
      valign: 'middle',
    });

    // Đường phân cách
    slide.addShape(this.generator.getShapes().LINE as any, {
      x: 6.5,
      y: 2.5,
      w: 3,
      h: 0,
      line: { color: this.theme.accent, width: 2 },
    });

    // Nội dung bên phải
    this.generator.addText(slide, {
      x: 6.5,
      y: 2.8,
      w: 6,
      h: 4,
      text: data.blocks?.[0]?.content || data.mainText || '',
      fontSize: 14,
      fontFace: 'Arial',
      color: this.theme.text,
      align: 'left',
      valign: 'top',
      wrap: true,
      lineSpacingMultiple: 1.5,
    });

    return slide;
  }
}

/**
 * Trang bố cục ba cột (ThreeColumn)
 * Chia nội dung thành 3 cột đồng đều trực quan
 */
export class ThreeColumn extends BaseContent {
  constructor(generator: TemplateGenerator, theme: Theme) {
    super(generator, theme);
  }

  generate(data: ContentData): pptxgen.Slide {
    const slide = this.generator.createSlide();
    const pptx = this.generator.getPresentation();

    slide.background = { fill: this.theme.background };

    // Tiêu đề trang
    this.addPageTitle(slide, data.pageTitle);

    const blocks = data.blocks || [];
    const colWidth = 3.6;
    const startX = 0.65;
    const startY = 1.5;
    const colors = [this.theme.primary, this.theme.secondary, this.theme.accent];

    for (let i = 0; i < Math.min(3, blocks.length); i++) {
      const x = startX + i * (colWidth + 0.45);
      const block = blocks[i];
      const color = colors[i % colors.length];

      // Khối màu đỉnh cột
      slide.addShape(this.generator.getShapes().RECTANGLE as any, {
        x: x,
        y: startY,
        w: colWidth,
        h: 0.08,
        fill: { color: color },
      });

      // Nền thẻ
      slide.addShape(this.generator.getShapes().RECTANGLE as any, {
        x: x,
        y: startY + 0.08,
        w: colWidth,
        h: 5.4,
        fill: { color: 'FFFFFF' },
        rectRadius: 0.05,
        shadow: {
          type: 'outer' as any,
          color: '000000',
          blur: 6,
          offset: 2,
          angle: 135,
          opacity: 0.08,
        },
      });

      // Vòng tròn số thứ tự
      slide.addShape(this.generator.getShapes().OVAL as any, {
        x: x + 0.3,
        y: startY + 0.4,
        w: 0.6,
        h: 0.6,
        fill: { color: color },
      });

      this.generator.addText(slide, {
        x: x + 0.3,
        y: startY + 0.4,
        w: 0.6,
        h: 0.6,
        text: String(block.index || i + 1),
        fontSize: 16,
        fontFace: 'Arial',
        color: 'FFFFFF',
        bold: true,
        align: 'center',
        valign: 'middle',
      });

      // Tiêu đề
      this.generator.addText(slide, {
        x: x + 1.1,
        y: startY + 0.45,
        w: colWidth - 1.4,
        h: 0.5,
        text: block.title,
        fontSize: 16,
        fontFace: 'Arial',
        color: this.theme.text,
        bold: true,
        align: 'left',
        valign: 'middle',
      });

      // Khung giữ chỗ ảnh
      slide.addShape(this.generator.getShapes().RECTANGLE as any, {
        x: x + 0.3,
        y: startY + 1.3,
        w: colWidth - 0.6,
        h: 2,
        fill: { color: color, transparency: 88 },
        rectRadius: 0.05,
      });

      // Văn bản nội dung
      this.generator.addText(slide, {
        x: x + 0.3,
        y: startY + 3.5,
        w: colWidth - 0.6,
        h: 1.8,
        text: block.content || '',
        fontSize: 11,
        fontFace: 'Arial',
        color: this.theme.text,
        align: 'left',
        valign: 'top',
        wrap: true,
        lineSpacingMultiple: 1.4,
      });
    }

    return slide;
  }
}

/**
 * Trang bố cục lưới 4 ô (FourGrid)
 * Lưới 2x2 hiển thị 4 khối nội dung cân đối
 */
export class FourGrid extends BaseContent {
  constructor(generator: TemplateGenerator, theme: Theme) {
    super(generator, theme);
  }

  generate(data: ContentData): pptxgen.Slide {
    const slide = this.generator.createSlide();
    const pptx = this.generator.getPresentation();

    slide.background = { fill: this.theme.background };

    // Tiêu đề trang
    this.addPageTitle(slide, data.pageTitle);

    const blocks = data.blocks || [];
    const gridWidth = 5.8;
    const gridHeight = 2.6;
    const startX = 0.6;
    const startY = 1.4;
    const gap = 0.4;
    const positions = createGridPositions(startX, startY, gridWidth, gridHeight, 2, 2, gap, gap);

    for (let i = 0; i < Math.min(4, blocks.length); i++) {
      const pos = positions[i];
      const block = blocks[i];
      const color = i % 2 === 0 ? this.theme.primary : this.theme.secondary;

      // Nền thẻ
      slide.addShape(this.generator.getShapes().RECTANGLE as any, {
        x: pos.x,
        y: pos.y,
        w: gridWidth,
        h: gridHeight,
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

      // Dải màu bên trái
      slide.addShape(this.generator.getShapes().RECTANGLE as any, {
        x: pos.x,
        y: pos.y,
        w: 0.1,
        h: gridHeight,
        fill: { color: color },
      });

      // Số thứ tự
      this.generator.addText(slide, {
        x: pos.x + 0.3,
        y: pos.y + 0.2,
        w: 0.8,
        h: 0.5,
        text: String(block.index || i + 1).padStart(2, '0'),
        fontSize: 28,
        fontFace: 'Arial',
        color: color,
        bold: true,
        align: 'left',
        valign: 'middle',
      });

      // Tiêu đề
      this.generator.addText(slide, {
        x: pos.x + 1.2,
        y: pos.y + 0.25,
        w: gridWidth - 1.5,
        h: 0.4,
        text: block.title,
        fontSize: 16,
        fontFace: 'Arial',
        color: this.theme.text,
        bold: true,
        align: 'left',
        valign: 'middle',
      });

      // Đường phân cách
      slide.addShape(this.generator.getShapes().LINE as any, {
        x: pos.x + 0.3,
        y: pos.y + 0.85,
        w: gridWidth - 0.6,
        h: 0,
        line: { color: this.theme.muted, width: 0.5, transparency: 50 },
      });

      // Văn bản nội dung
      this.generator.addText(slide, {
        x: pos.x + 0.3,
        y: pos.y + 1.0,
        w: gridWidth - 0.6,
        h: 1.4,
        text: block.content || '',
        fontSize: 12,
        fontFace: 'Arial',
        color: this.theme.text,
        align: 'left',
        valign: 'top',
        wrap: true,
        lineSpacingMultiple: 1.4,
      });
    }

    return slide;
  }
}

/**
 * Trang lớp phủ toàn ảnh (FullImageOverlay)
 * Phủ lớp văn bản bán trong suốt trên nền hình ảnh toàn trang
 */
export class FullImageOverlay extends BaseContent {
  constructor(generator: TemplateGenerator, theme: Theme) {
    super(generator, theme);
  }

  generate(data: ContentData): pptxgen.Slide {
    const slide = this.generator.createSlide();
    const pptx = this.generator.getPresentation();

    // Nền tối mô phỏng hình ảnh
    slide.background = { fill: this.theme.darkBg };

    // Vùng giữ chỗ ảnh (toàn màn hình)
    slide.addShape(this.generator.getShapes().RECTANGLE as any, {
      x: 0,
      y: 0,
      w: 13.33,
      h: 7.5,
      fill: { color: this.theme.primary, transparency: 70 },
    });

    // Khung giữ chỗ
    this.generator.addText(slide, {
      x: 4,
      y: 3,
      w: 5,
      h: 1,
      text: '[Khung ảnh nền]',
      fontSize: 18,
      fontFace: 'Arial',
      color: 'FFFFFF',
      align: 'center',
      valign: 'middle',
    });

    // Lớp phủ bán trong suốt phía dưới
    slide.addShape(this.generator.getShapes().RECTANGLE as any, {
      x: 0,
      y: 4.5,
      w: 13.33,
      h: 3,
      fill: { color: '000000', transparency: 40 },
    });

    // Tiêu đề
    this.generator.addText(slide, {
      x: 0.8,
      y: 4.8,
      w: 11.5,
      h: 0.8,
      text: data.pageTitle,
      fontSize: 28,
      fontFace: 'Arial',
      color: 'FFFFFF',
      bold: true,
      align: 'left',
      valign: 'middle',
    });

    // Văn bản nội dung
    const content = data.blocks?.map(b => `${b.title}: ${b.content || ''}`).join('\n') || data.mainText || '';
    this.generator.addText(slide, {
      x: 0.8,
      y: 5.6,
      w: 11.5,
      h: 1.5,
      text: content,
      fontSize: 14,
      fontFace: 'Arial',
      color: 'DDDDDD',
      align: 'left',
      valign: 'top',
      wrap: true,
      lineSpacingMultiple: 1.5,
    });

    return slide;
  }
}

/**
 * Trang bố cục so sánh (Comparison)
 * Bố cục hai cột đối chiếu song song trái - phải
 */
export class Comparison extends BaseContent {
  constructor(generator: TemplateGenerator, theme: Theme) {
    super(generator, theme);
  }

  generate(data: ContentData): pptxgen.Slide {
    const slide = this.generator.createSlide();
    const pptx = this.generator.getPresentation();

    slide.background = { fill: this.theme.background };

    // Tiêu đề trang
    this.addPageTitle(slide, data.pageTitle);

    const leftBlock = data.blocks?.[0];
    const rightBlock = data.blocks?.[1];

    // Nền nửa bên trái
    slide.addShape(this.generator.getShapes().RECTANGLE as any, {
      x: 0.5,
      y: 1.5,
      w: 5.8,
      h: 5.5,
      fill: { color: this.theme.primary, transparency: 90 },
      rectRadius: 0.1,
    });

    // Nền nửa bên phải
    slide.addShape(this.generator.getShapes().RECTANGLE as any, {
      x: 6.8,
      y: 1.5,
      w: 5.8,
      h: 5.5,
      fill: { color: this.theme.accent, transparency: 90 },
      rectRadius: 0.1,
    });

    // Dải phân cách VS ở giữa
    slide.addShape(this.generator.getShapes().OVAL as any, {
      x: 6.05,
      y: 3.5,
      w: 1.2,
      h: 1.2,
      fill: { color: this.theme.primary },
    });

    this.generator.addText(slide, {
      x: 6.05,
      y: 3.5,
      w: 1.2,
      h: 1.2,
      text: 'VS',
      fontSize: 20,
      fontFace: 'Arial',
      color: 'FFFFFF',
      bold: true,
      align: 'center',
      valign: 'middle',
    });

    // Tiêu đề bên trái
    this.generator.addText(slide, {
      x: 1,
      y: 1.8,
      w: 4.8,
      h: 0.5,
      text: leftBlock?.title || 'Phương án A',
      fontSize: 18,
      fontFace: 'Arial',
      color: this.theme.primary,
      bold: true,
      align: 'center',
      valign: 'middle',
    });

    // Nội dung bên trái
    this.generator.addText(slide, {
      x: 1,
      y: 2.5,
      w: 4.8,
      h: 4,
      text: leftBlock?.content || '',
      fontSize: 13,
      fontFace: 'Arial',
      color: this.theme.text,
      align: 'left',
      valign: 'top',
      wrap: true,
      lineSpacingMultiple: 1.5,
    });

    // Tiêu đề bên phải
    this.generator.addText(slide, {
      x: 7.3,
      y: 1.8,
      w: 4.8,
      h: 0.5,
      text: rightBlock?.title || 'Phương án B',
      fontSize: 18,
      fontFace: 'Arial',
      color: this.theme.accent,
      bold: true,
      align: 'center',
      valign: 'middle',
    });

    // Nội dung bên phải
    this.generator.addText(slide, {
      x: 7.3,
      y: 2.5,
      w: 4.8,
      h: 4,
      text: rightBlock?.content || '',
      fontSize: 13,
      fontFace: 'Arial',
      color: this.theme.text,
      align: 'left',
      valign: 'top',
      wrap: true,
      lineSpacingMultiple: 1.5,
    });

    return slide;
  }
}
