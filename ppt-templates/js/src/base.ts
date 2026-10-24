/**
 * Lớp cơ sở của bộ tạo PPT
 * Cung cấp các chức năng cốt lõi như tạo slide, thêm phần tử, cấu hình chủ đề v.v.
 */

import pptxgen from 'pptxgenjs';

/** Giao diện cấu hình màu sắc chủ đề */
export interface Theme {
  /** Tên chủ đề */
  name: string;
  /** Màu chính */
  primary: string;
  /** Màu phụ */
  secondary: string;
  /** Màu nhấn */
  accent: string;
  /** Màu nền */
  background: string;
  /** Màu văn bản */
  text: string;
  /** Màu văn bản phụ mờ */
  muted: string;
  /** Màu nền tối */
  darkBg: string;
}

/** Tùy chọn kích thước slide */
export interface SlideSize {
  /** Chiều rộng (inch) */
  width: number;
  /** Chiều cao (inch) */
  height: number;
}

/** Tùy chọn hộp văn bản */
export interface TextBoxOptions {
  x: number;
  y: number;
  w: number;
  h: number;
  text: string;
  fontSize?: number;
  fontFace?: string;
  color?: string;
  bold?: boolean;
  italic?: boolean;
  align?: 'left' | 'center' | 'right';
  valign?: 'top' | 'middle' | 'bottom';
  wrap?: boolean;
  lineSpacingMultiple?: number;
}

/** Tùy chọn hình khối */
export interface ShapeOptions {
  x: number;
  y: number;
  w: number;
  h: number;
  fill?: { color: string };
  line?: { color: string; width: number };
  shadow?: {
    type: 'outer';
    color: string;
    blur: number;
    offset: number;
    angle: number;
    opacity: number;
  };
  rectRadius?: number;
}

/** Tùy chọn hình ảnh */
export interface ImageOptions {
  x: number;
  y: number;
  w: number;
  h: number;
  path?: string;
  data?: string;
  rounding?: boolean;
}

/**
 * Lớp cơ sở bộ tạo mẫu PPT
 * Đóng gói các chức năng của pptxgenjs, cung cấp API tinh gọn
 */
export class TemplateGenerator {
  /** Thể hiện bản thuyết trình pptxgenjs */
  protected pptx: pptxgen;
  /** Chủ đề hiện tại */
  protected theme: Theme;
  /** Kích thước slide */
  protected slideSize: SlideSize;

  /**
   * Khởi tạo thể hiện bộ tạo mẫu
   * @param theme - Cấu hình chủ đề
   * @param slideSize - Kích thước slide, mặc định màn ảnh rộng 16:9
   */
  constructor(theme?: Theme, slideSize?: SlideSize) {
    this.pptx = new pptxgen();
    this.theme = theme || {
      name: 'Chủ đề mặc định',
      primary: '2B579A',
      secondary: '4472C4',
      accent: 'ED7D31',
      background: 'FFFFFF',
      text: '333333',
      muted: '999999',
      darkBg: '1F1F1F'
    };
    this.slideSize = slideSize || { width: 13.33, height: 7.5 };
    this.configurePresentation();
  }

  /**
   * Cấu hình thuộc tính cơ bản của bản thuyết trình
   */
  private configurePresentation(): void {
    this.pptx.defineLayout({
      name: 'CUSTOM',
      width: this.slideSize.width,
      height: this.slideSize.height
    });
    this.pptx.layout = 'CUSTOM';
    this.pptx.author = 'PPT Generator';
    this.pptx.company = 'PPT Generator';
    this.pptx.subject = 'Bản thuyết trình tự động tạo';
    this.pptx.title = 'Bản thuyết trình';
  }

  /**
   * Thiết lập tiêu đề bản thuyết trình
   * @param title - Văn bản tiêu đề
   */
  setTitle(title: string): void {
    this.pptx.title = title;
  }

  /**
   * Tạo slide mới
   * @returns Đối tượng slide mới
   */
  createSlide(): pptxgen.Slide {
    return this.pptx.addSlide();
  }

  /**
   * Thêm hình khối vào slide
   * @param slide - Slide mục tiêu
   * @param shapeType - Loại hình khối
   * @param options - Tùy chọn hình khối
   */
  addShape(
    slide: pptxgen.Slide,
    shapeType: pptxgen.ShapeType,
    options: ShapeOptions
  ): void {
    slide.addShape(shapeType, options as any);
  }

  /**
   * Thêm hộp văn bản vào slide
   * @param slide - Slide mục tiêu
   * @param options - Tùy chọn hộp văn bản
   */
  addText(slide: pptxgen.Slide, options: TextBoxOptions): void {
    const textOptions: any = {
      x: options.x,
      y: options.y,
      w: options.w,
      h: options.h,
      fontSize: options.fontSize || 14,
      fontFace: options.fontFace || 'Arial',
      color: options.color || this.theme.text,
      bold: options.bold || false,
      italic: options.italic || false,
      align: options.align || 'left',
      valign: options.valign || 'top',
      wrap: options.wrap !== false,
    };
    if (options.lineSpacingMultiple) {
      textOptions.lineSpacingMultiple = options.lineSpacingMultiple;
    }
    slide.addText(options.text, textOptions);
  }

  /**
   * Thêm hình ảnh vào slide
   * @param slide - Slide mục tiêu
   * @param options - Tùy chọn hình ảnh
   */
  addImage(slide: pptxgen.Slide, options: ImageOptions): void {
    const imageOptions: any = {
      x: options.x,
      y: options.y,
      w: options.w,
      h: options.h,
    };
    if (options.path) imageOptions.path = options.path;
    if (options.data) imageOptions.data = options.data;
    if (options.rounding !== undefined) imageOptions.rounding = options.rounding;
    slide.addImage(imageOptions);
  }

  /**
   * Lưu bản thuyết trình ra tập tin
   * @param fileName - Tên tập tin (không bao gồm phần mở rộng)
   * @returns Promise trả về đường dẫn tập tin khi hoàn tất
   */
  async save(fileName: string): Promise<string> {
    const filePath = `${fileName}.pptx`;
    await this.pptx.writeFile({ fileName: filePath });
    return filePath;
  }

  /**
   * Lấy thể hiện bản thuyết trình (dùng cho các thao tác nâng cao)
   * @returns Đối tượng bản thuyết trình pptxgenjs
   */
  getPresentation(): pptxgen {
    return this.pptx;
  }

  /**
   * Lấy cấu hình chủ đề hiện tại
   * @returns Đối tượng cấu hình chủ đề
   */
  getTheme(): Theme {
    return this.theme;
  }

  /**
   * Lấy hằng số các loại hình khối
   * Lấy từ thể hiện pptx tại thời điểm chạy để tránh giới hạn kiểu của TypeScript
   */
  get shapes(): any {
    return (this.pptx as any).shapes;
  }

  /**
   * Lấy hằng số các loại biểu đồ
   * Lấy từ thể hiện pptx tại thời điểm chạy để tránh giới hạn kiểu của TypeScript
   */
  get charts(): any {
    return (this.pptx as any).charts;
  }

  /**
   * Lấy thuộc tính shapes của thể hiện bản thuyết trình
   */
  getShapes(): any {
    return (this.pptx as any).shapes;
  }

  /**
   * Lấy thuộc tính charts của thể hiện bản thuyết trình
   */
  getCharts(): any {
    return (this.pptx as any).charts;
  }
}
