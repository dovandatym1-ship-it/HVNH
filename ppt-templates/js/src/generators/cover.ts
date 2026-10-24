/**
 * Mô-đun bộ tạo trang bìa (Cover)
 * Bao gồm 8 mẫu trang bìa phong cách đa dạng:
 * - Nhóm hoạt họa: Xoay hình học, Chuyển cảnh vòng tròn, Tàu xuyên sương, Hé lộ hình thoi
 * - Nhóm tĩnh: Chuyển sắc tối giản, Chia đôi màn hình, Mặt nạ chữ rỗng, Chiều sâu đa tầng
 */

import pptxgen from 'pptxgenjs';
import { TemplateGenerator, Theme } from '../base';
import { lightenColor, darkenColor } from '../utils';

/** Giao diện dữ liệu trang bìa */
export interface CoverData {
  /** Tiêu đề chính */
  title: string;
  /** Tiêu đề phụ */
  subtitle?: string;
  /** Diễn giả / Tác giả */
  presenter?: string;
  /** Ngày tháng */
  date?: string;
  /** Tên công ty / Tổ chức */
  company?: string;
}

/** Lớp trang bìa cơ sở */
abstract class BaseCover {
  protected generator: TemplateGenerator;
  protected theme: Theme;

  constructor(generator: TemplateGenerator, theme: Theme) {
    this.generator = generator;
    this.theme = theme;
  }

  /** Tạo trang bìa */
  abstract generate(data: CoverData): pptxgen.Slide;

  /** Thêm văn bản tiêu đề chính */
  protected addTitle(slide: pptxgen.Slide, data: CoverData, options: any = {}): void {
    this.generator.addText(slide, {
      x: options.x || 0.8,
      y: options.y || 2.5,
      w: options.w || 11.5,
      h: options.h || 1.5,
      text: data.title,
      fontSize: options.fontSize || 40,
      fontFace: 'Arial',
      color: options.color || this.theme.text,
      bold: true,
      align: options.align || 'center',
      valign: 'middle',
    });
  }

  /** Thêm tiêu đề phụ */
  protected addSubtitle(slide: pptxgen.Slide, data: CoverData, options: any = {}): void {
    if (!data.subtitle) return;
    this.generator.addText(slide, {
      x: options.x || 0.8,
      y: options.y || 4.0,
      w: options.w || 11.5,
      h: options.h || 0.8,
      text: data.subtitle,
      fontSize: options.fontSize || 20,
      fontFace: 'Arial',
      color: options.color || this.theme.muted,
      align: options.align || 'center',
      valign: 'middle',
    });
  }

  /** Thêm thông tin ngày tháng và tác giả */
  protected addInfo(slide: pptxgen.Slide, data: CoverData, options: any = {}): void {
    const info = [
      data.presenter,
      data.date,
      data.company,
    ].filter(Boolean).join(' | ');

    if (info) {
      this.generator.addText(slide, {
        x: options.x || 0.8,
        y: options.y || 5.5,
        w: options.w || 11.5,
        h: options.h || 0.5,
        text: info,
        fontSize: options.fontSize || 12,
        fontFace: 'Arial',
        color: options.color || this.theme.muted,
        align: options.align || 'center',
        valign: 'middle',
      });
    }
  }
}

/**
 * Bìa xoay hình học (Geometric Rotation)
 * Sử dụng nhiều khối hình học xoay đa lớp làm điểm nhấn trang trí
 */
export class GeometricRotation extends BaseCover {
  constructor(generator: TemplateGenerator, theme: Theme) {
    super(generator, theme);
  }

  generate(data: CoverData): pptxgen.Slide {
    const slide = this.generator.createSlide();
    const pptx = this.generator.getPresentation();

    // Nền
    slide.background = { fill: this.theme.background };

    // Khối hình học trang trí bên trái
    const shapes: Array<{ x: number; y: number; w: number; h: number; color: string; rotate: number }> = [
      { x: -0.5, y: -0.5, w: 3, h: 3, color: this.theme.primary, rotate: 15 },
      { x: -0.2, y: 4.5, w: 2.5, h: 2.5, color: this.theme.secondary, rotate: -30 },
      { x: 10.5, y: 0.5, w: 2, h: 2, color: this.theme.accent, rotate: 45 },
      { x: 11, y: 5, w: 2.5, h: 2.5, color: this.theme.primary, rotate: 60 },
      { x: 5, y: -0.3, w: 1.5, h: 1.5, color: this.theme.secondary, rotate: 30 },
      { x: 8, y: 6, w: 2, h: 2, color: this.theme.accent, rotate: -20 },
    ];

    shapes.forEach(shape => {
      slide.addShape(this.generator.getShapes().RECTANGLE as any, {
        x: shape.x,
        y: shape.y,
        w: shape.w,
        h: shape.h,
        fill: { color: shape.color, transparency: 85 },
        rotate: shape.rotate,
      });
    });

    // Đường phân cách trung tâm
    slide.addShape(this.generator.getShapes().LINE as any, {
      x: 4.5,
      y: 2.0,
      w: 4.3,
      h: 0,
      line: { color: this.theme.primary, width: 2 },
    });

    // Tiêu đề chính
    this.addTitle(slide, data, { y: 2.2, fontSize: 44, color: this.theme.text });

    // Đường phân cách
    slide.addShape(this.generator.getShapes().LINE as any, {
      x: 4.5,
      y: 3.8,
      w: 4.3,
      h: 0,
      line: { color: this.theme.primary, width: 2 },
    });

    // Tiêu đề phụ
    this.addSubtitle(slide, data, { y: 4.0 });

    // Thông tin phía dưới
    this.addInfo(slide, data, { y: 5.8 });

    return slide;
  }
}

/**
 * Bìa chuyển cảnh vòng tròn (Circle Ring)
 * Sử dụng các vòng tròn đồng tâm chuyển sắc làm yếu tố thị giác chính
 */
export class CircleRing extends BaseCover {
  constructor(generator: TemplateGenerator, theme: Theme) {
    super(generator, theme);
  }

  generate(data: CoverData): pptxgen.Slide {
    const slide = this.generator.createSlide();
    const pptx = this.generator.getPresentation();

    // Nền
    slide.background = { fill: this.theme.darkBg };

    // Các vòng tròn đồng tâm
    const rings = [
      { x: 4.16, y: 1.5, w: 5, h: 5, color: this.theme.primary, transparency: 70 },
      { x: 4.66, y: 2.0, w: 4, h: 4, color: this.theme.secondary, transparency: 60 },
      { x: 5.16, y: 2.5, w: 3, h: 3, color: this.theme.accent, transparency: 50 },
    ];

    rings.forEach(ring => {
      slide.addShape(this.generator.getShapes().OVAL as any, {
        x: ring.x,
        y: ring.y,
        w: ring.w,
        h: ring.h,
        line: { color: ring.color, width: 2, transparency: ring.transparency },
        fill: { color: ring.color, transparency: 95 },
      });
    });

    // Đường trang trí bên phải
    slide.addShape(this.generator.getShapes().LINE as any, {
      x: 10,
      y: 1,
      w: 0,
      h: 5.5,
      line: { color: this.theme.primary, width: 1, transparency: 50 },
    });

    // Tiêu đề (màu trắng, phù hợp nền tối)
    this.addTitle(slide, data, {
      y: 3.0,
      color: 'FFFFFF',
      fontSize: 42,
      align: 'center',
    });

    // Tiêu đề phụ
    this.addSubtitle(slide, data, {
      y: 4.2,
      color: 'CCCCCC',
    });

    // Thông tin phía dưới
    this.addInfo(slide, data, {
      y: 6.0,
      color: '999999',
    });

    return slide;
  }
}

/**
 * Bìa tàu xuyên sương (Train Mist)
 * Sử dụng nhiều lớp hình chữ nhật bán trong suốt tạo hiệu ứng chiều sâu sương mù
 */
export class TrainMist extends BaseCover {
  constructor(generator: TemplateGenerator, theme: Theme) {
    super(generator, theme);
  }

  generate(data: CoverData): pptxgen.Slide {
    const slide = this.generator.createSlide();
    const pptx = this.generator.getPresentation();

    // Nền
    slide.background = { fill: this.theme.background };

    // Nhiều lớp hình chữ nhật bán trong suốt (tạo hiệu ứng sương mù)
    const layers = [
      { x: -1, y: 0, w: 6, h: 7.5, color: this.theme.primary, transparency: 90 },
      { x: 0, y: -0.5, w: 5, h: 8, color: this.theme.secondary, transparency: 85 },
      { x: 1, y: 0.5, w: 4, h: 6.5, color: this.theme.accent, transparency: 80 },
    ];

    layers.forEach(layer => {
      slide.addShape(this.generator.getShapes().RECTANGLE as any, {
        x: layer.x,
        y: layer.y,
        w: layer.w,
        h: layer.h,
        fill: { color: layer.color, transparency: layer.transparency },
      });
    });

    // Dải trang trí bên phải
    slide.addShape(this.generator.getShapes().RECTANGLE as any, {
      x: 10,
      y: 0,
      w: 3.33,
      h: 7.5,
      fill: { color: this.theme.primary, transparency: 80 },
    });

    // Tiêu đề chính
    this.addTitle(slide, data, {
      x: 3,
      y: 2.5,
      w: 8,
      fontSize: 38,
      align: 'left',
      color: this.theme.text,
    });

    // Tiêu đề phụ
    this.addSubtitle(slide, data, {
      x: 3,
      y: 4.0,
      w: 8,
      align: 'left',
    });

    // Thông tin phía dưới
    this.addInfo(slide, data, {
      x: 3,
      y: 5.8,
      w: 8,
      align: 'left',
    });

    return slide;
  }
}

/**
 * Bìa hé lộ hình thoi (Diamond Reveal)
 * Sử dụng cụm hình thoi làm nổi bật chủ đề chính
 */
export class DiamondReveal extends BaseCover {
  constructor(generator: TemplateGenerator, theme: Theme) {
    super(generator, theme);
  }

  generate(data: CoverData): pptxgen.Slide {
    const slide = this.generator.createSlide();
    const pptx = this.generator.getPresentation();

    // Nền
    slide.background = { fill: this.theme.background };

    // Họa tiết hình thoi trang trí
    const diamonds = [
      { x: 6, y: 1, w: 2.5, h: 2.5, color: this.theme.primary, transparency: 80 },
      { x: 7, y: 2, w: 2, h: 2, color: this.theme.secondary, transparency: 70 },
      { x: 5, y: 3.5, w: 3, h: 3, color: this.theme.accent, transparency: 85 },
      { x: 8, y: 4, w: 1.5, h: 1.5, color: this.theme.primary, transparency: 75 },
    ];

    diamonds.forEach(d => {
      slide.addShape(this.generator.getShapes().RECTANGLE as any, {
        x: d.x,
        y: d.y,
        w: d.w,
        h: d.h,
        fill: { color: d.color, transparency: d.transparency },
        rotate: 45,
      });
    });

    // Đường trang trí bên trái
    slide.addShape(this.generator.getShapes().LINE as any, {
      x: 2,
      y: 0.5,
      w: 0,
      h: 6.5,
      line: { color: this.theme.primary, width: 3 },
    });

    // Tiêu đề chính
    this.addTitle(slide, data, {
      x: 0.5,
      y: 2.5,
      w: 6,
      fontSize: 36,
      align: 'left',
    });

    // Tiêu đề phụ
    this.addSubtitle(slide, data, {
      x: 0.5,
      y: 4.0,
      w: 6,
      align: 'left',
    });

    // Thông tin phía dưới
    this.addInfo(slide, data, {
      x: 0.5,
      y: 5.8,
      w: 6,
      align: 'left',
    });

    return slide;
  }
}

/**
 * Bìa chuyển sắc tối giản (Minimalist Gradient)
 * Khối màu chuyển sắc diện rộng, phong cách tinh gọn trang nhã
 */
export class MinimalistGradient extends BaseCover {
  constructor(generator: TemplateGenerator, theme: Theme) {
    super(generator, theme);
  }

  generate(data: CoverData): pptxgen.Slide {
    const slide = this.generator.createSlide();
    const pptx = this.generator.getPresentation();

    // Nền chuyển sắc (mô phỏng bằng màu đơn sắc)
    slide.background = { fill: this.theme.background };

    // Khối màu lớn bên trái
    slide.addShape(this.generator.getShapes().RECTANGLE as any, {
      x: 0,
      y: 0,
      w: 6,
      h: 7.5,
      fill: { color: this.theme.primary },
    });

    // Đường trang trí trên khối màu
    slide.addShape(this.generator.getShapes().LINE as any, {
      x: 0.8,
      y: 3.0,
      w: 4,
      h: 0,
      line: { color: 'FFFFFF', width: 1, transparency: 50 },
    });

    // Tiêu đề bên trái (màu trắng)
    this.addTitle(slide, data, {
      x: 0.8,
      y: 3.2,
      w: 4.5,
      fontSize: 36,
      align: 'left',
      color: 'FFFFFF',
    });

    // Tiêu đề phụ bên trái (màu trắng)
    this.addSubtitle(slide, data, {
      x: 0.8,
      y: 4.5,
      w: 4.5,
      align: 'left',
      color: 'DDDDDD',
    });

    // Thông tin bên phải
    const info = [data.presenter, data.company].filter(Boolean).join('\n');
    if (info) {
      this.generator.addText(slide, {
        x: 7,
        y: 3.5,
        w: 5,
        h: 1.5,
        text: info,
        fontSize: 14,
        fontFace: 'Arial',
        color: this.theme.muted,
        align: 'left',
        valign: 'top',
        lineSpacingMultiple: 1.5,
      });
    }

    // Ngày tháng bên phải
    if (data.date) {
      this.generator.addText(slide, {
        x: 7,
        y: 5.5,
        w: 5,
        h: 0.5,
        text: data.date,
        fontSize: 12,
        fontFace: 'Arial',
        color: this.theme.muted,
        align: 'left',
      });
    }

    return slide;
  }
}

/**
 * Bìa chia đôi màn hình (Split Screen)
 * Chia bố cục thành hai nửa trái - phải, một bên văn bản và một bên đồ họa
 */
export class SplitScreen extends BaseCover {
  constructor(generator: TemplateGenerator, theme: Theme) {
    super(generator, theme);
  }

  generate(data: CoverData): pptxgen.Slide {
    const slide = this.generator.createSlide();
    const pptx = this.generator.getPresentation();

    // Nền
    slide.background = { fill: 'FFFFFF' };

    // Khối màu nửa bên phải
    slide.addShape(this.generator.getShapes().RECTANGLE as any, {
      x: 6.5,
      y: 0,
      w: 6.83,
      h: 7.5,
      fill: { color: this.theme.primary },
    });

    // Vòng tròn trang trí bên phải
    slide.addShape(this.generator.getShapes().OVAL as any, {
      x: 7.5,
      y: 1.5,
      w: 4.5,
      h: 4.5,
      fill: { color: this.theme.secondary, transparency: 60 },
    });

    // Đường phân cách ở giữa
    slide.addShape(this.generator.getShapes().LINE as any, {
      x: 6.5,
      y: 0.5,
      w: 0,
      h: 6.5,
      line: { color: this.theme.accent, width: 3 },
    });

    // Tiêu đề bên trái
    this.addTitle(slide, data, {
      x: 0.5,
      y: 2.5,
      w: 5.5,
      fontSize: 38,
      align: 'left',
    });

    // Tiêu đề phụ bên trái
    this.addSubtitle(slide, data, {
      x: 0.5,
      y: 4.0,
      w: 5.5,
      align: 'left',
    });

    // Thông tin phía dưới bên trái
    this.addInfo(slide, data, {
      x: 0.5,
      y: 5.8,
      w: 5.5,
      align: 'left',
    });

    // Văn bản trang trí bên phải
    this.generator.addText(slide, {
      x: 7.5,
      y: 6.2,
      w: 4.5,
      h: 0.5,
      text: data.date || '',
      fontSize: 12,
      fontFace: 'Arial',
      color: 'FFFFFF',
      align: 'center',
    });

    return slide;
  }
}

/**
 * Bìa mặt nạ chữ rỗng (Hollow Mask)
 * Sử dụng hiệu ứng khung rỗng làm nổi bật nền
 */
export class HollowMask extends BaseCover {
  constructor(generator: TemplateGenerator, theme: Theme) {
    super(generator, theme);
  }

  generate(data: CoverData): pptxgen.Slide {
    const slide = this.generator.createSlide();
    const pptx = this.generator.getPresentation();

    // Nền
    slide.background = { fill: this.theme.darkBg };

    // Khối chữ nhật mặt nạ ngoài
    slide.addShape(this.generator.getShapes().RECTANGLE as any, {
      x: 0,
      y: 0,
      w: 13.33,
      h: 7.5,
      fill: { color: this.theme.darkBg },
    });

    // Vùng rỗng - Khối chữ nhật màu sáng ở giữa
    slide.addShape(this.generator.getShapes().RECTANGLE as any, {
      x: 2.5,
      y: 1.5,
      w: 8.33,
      h: 4.5,
      fill: { color: this.theme.background },
      rectRadius: 0.1,
    });

    // Viền của vùng rỗng
    slide.addShape(this.generator.getShapes().RECTANGLE as any, {
      x: 2.5,
      y: 1.5,
      w: 8.33,
      h: 4.5,
      line: { color: this.theme.primary, width: 2 },
      fill: { color: '000000', transparency: 100 },
      rectRadius: 0.1,
    });

    // Tiêu đề chính
    this.addTitle(slide, data, {
      y: 2.5,
      fontSize: 40,
      color: this.theme.text,
    });

    // Tiêu đề phụ
    this.addSubtitle(slide, data, { y: 3.8 });

    // Thông tin phía dưới
    this.addInfo(slide, data, {
      y: 6.5,
      color: 'CCCCCC',
    });

    return slide;
  }
}

/**
 * Bìa chiều sâu đa tầng (Layered Depth)
 * Xếp lớp nhiều khối chữ nhật tạo hiệu ứng chiều sâu đa tầng
 */
export class LayeredDepth extends BaseCover {
  constructor(generator: TemplateGenerator, theme: Theme) {
    super(generator, theme);
  }

  generate(data: CoverData): pptxgen.Slide {
    const slide = this.generator.createSlide();
    const pptx = this.generator.getPresentation();

    // Nền
    slide.background = { fill: this.theme.background };

    // Các khối chữ nhật xếp lớp đa tầng
    const layers = [
      { x: 0.5, y: 0.5, w: 12, h: 6.5, color: this.theme.primary, transparency: 90 },
      { x: 1.0, y: 1.0, w: 11, h: 5.5, color: this.theme.secondary, transparency: 85 },
      { x: 1.5, y: 1.5, w: 10, h: 4.5, color: this.theme.accent, transparency: 80 },
    ];

    layers.forEach((layer, i) => {
      slide.addShape(this.generator.getShapes().RECTANGLE as any, {
        x: layer.x,
        y: layer.y,
        w: layer.w,
        h: layer.h,
        fill: { color: layer.color, transparency: layer.transparency },
        rectRadius: 0.05,
        shadow: i === 2 ? {
          type: 'outer' as any,
          color: '000000',
          blur: 10,
          offset: 3,
          angle: 135,
          opacity: 0.15,
        } : undefined,
      });
    });

    // Tiêu đề chính
    this.addTitle(slide, data, {
      y: 2.5,
      fontSize: 42,
      color: this.theme.text,
    });

    // Tiêu đề phụ
    this.addSubtitle(slide, data, { y: 4.0 });

    // Thông tin phía dưới
    this.addInfo(slide, data, { y: 5.8 });

    return slide;
  }
}
