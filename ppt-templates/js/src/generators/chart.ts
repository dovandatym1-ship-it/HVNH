/**
 * Mô-đun bộ tạo biểu đồ (Chart)
 * Bao gồm 4 mẫu biểu đồ phong cách đa dạng:
 * - Biểu đồ cột, Biểu đồ tròn, Biểu đồ đường, Biểu đồ hoạt họa
 */

import pptxgen from 'pptxgenjs';
import { TemplateGenerator, Theme } from '../base';

/** Giao diện dữ liệu mục biểu đồ */
export interface ChartDataItem {
  /** Nhãn danh mục */
  label: string;
  /** Giá trị số */
  value: number;
  /** Màu sắc (tùy chọn) */
  color?: string;
}

/** Giao diện dữ liệu trang biểu đồ */
export interface ChartPageData {
  /** Tiêu đề trang */
  pageTitle: string;
  /** Tiêu đề biểu đồ */
  chartTitle?: string;
  /** Dữ liệu biểu đồ */
  data: ChartDataItem[];
  /** Ghi chú / Diễn giải biểu đồ */
  description?: string;
}

/** Lớp biểu đồ cơ sở */
abstract class BaseChart {
  protected generator: TemplateGenerator;
  protected theme: Theme;

  constructor(generator: TemplateGenerator, theme: Theme) {
    this.generator = generator;
    this.theme = theme;
  }

  /** Tạo trang biểu đồ */
  abstract generate(data: ChartPageData): pptxgen.Slide;

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

  /** Lấy bảng màu */
  protected getColors(count: number): string[] {
    const palette = [
      this.theme.primary,
      this.theme.secondary,
      this.theme.accent,
      '4CAF50',
      'FF9800',
      '9C27B0',
      '00BCD4',
      'E91E63',
    ];
    const colors: string[] = [];
    for (let i = 0; i < count; i++) {
      colors.push(palette[i % palette.length]);
    }
    return colors;
  }
}

/**
 * Trang biểu đồ cột (Bar Chart)
 * Sử dụng tính năng biểu đồ tích hợp của pptxgenjs để tạo biểu đồ cột
 */
export class BarChart extends BaseChart {
  constructor(generator: TemplateGenerator, theme: Theme) {
    super(generator, theme);
  }

  generate(data: ChartPageData): pptxgen.Slide {
    const slide = this.generator.createSlide();
    const pptx = this.generator.getPresentation();

    slide.background = { fill: this.theme.background };

    // Tiêu đề trang
    this.addPageTitle(slide, data.pageTitle);

    // Tiêu đề biểu đồ
    if (data.chartTitle) {
      this.generator.addText(slide, {
        x: 0.5,
        y: 1.1,
        w: 12,
        h: 0.5,
        text: data.chartTitle,
        fontSize: 16,
        fontFace: 'Arial',
        color: this.theme.text,
        bold: true,
        align: 'left',
        valign: 'middle',
      });
    }

    // Biểu đồ cột
    const chartData = [
      {
        name: 'Dữ liệu',
        labels: data.data.map(d => d.label),
        values: data.data.map(d => d.value),
      },
    ];

    slide.addChart(this.generator.getCharts().BAR as any, chartData, {
      x: 0.8,
      y: 1.8,
      w: 11.5,
      h: 4.8,
      barDir: 'bar',
      barGrouping: 'clustered',
      chartColors: this.getColors(data.data.length),
      showLegend: true,
      legendPos: 'b',
      legendFontSize: 10,
      showValue: true,
      dataLabelFontSize: 10,
      catAxisLabelFontSize: 10,
      catAxisLabelColor: this.theme.text,
      valAxisLabelFontSize: 9,
      valAxisLabelColor: this.theme.muted,
      plotArea: { fill: { color: 'FFFFFF' } },
      showTitle: false,
    });

    // Mô tả
    if (data.description) {
      this.generator.addText(slide, {
        x: 0.8,
        y: 6.8,
        w: 11.5,
        h: 0.5,
        text: data.description,
        fontSize: 10,
        fontFace: 'Arial',
        color: this.theme.muted,
        align: 'left',
        valign: 'middle',
      });
    }

    return slide;
  }
}

/**
 * Trang biểu đồ tròn (Pie Chart)
 * Sử dụng tính năng biểu đồ tích hợp của pptxgenjs để tạo biểu đồ tròn
 */
export class PieChart extends BaseChart {
  constructor(generator: TemplateGenerator, theme: Theme) {
    super(generator, theme);
  }

  generate(data: ChartPageData): pptxgen.Slide {
    const slide = this.generator.createSlide();
    const pptx = this.generator.getPresentation();

    slide.background = { fill: this.theme.background };

    // Tiêu đề trang
    this.addPageTitle(slide, data.pageTitle);

    // Tiêu đề biểu đồ
    if (data.chartTitle) {
      this.generator.addText(slide, {
        x: 0.5,
        y: 1.1,
        w: 12,
        h: 0.5,
        text: data.chartTitle,
        fontSize: 16,
        fontFace: 'Arial',
        color: this.theme.text,
        bold: true,
        align: 'left',
        valign: 'middle',
      });
    }

    // Biểu đồ tròn
    const chartData = [
      {
        name: 'Dữ liệu',
        labels: data.data.map(d => d.label),
        values: data.data.map(d => d.value),
      },
    ];

    slide.addChart(this.generator.getCharts().PIE as any, chartData, {
      x: 0.5,
      y: 1.8,
      w: 7,
      h: 5.2,
      chartColors: this.getColors(data.data.length),
      showLegend: true,
      legendPos: 'r',
      legendFontSize: 11,
      showPercent: true,
      showTitle: false,
    });

    // Giải thích dữ liệu bên phải
    const total = data.data.reduce((sum, d) => sum + d.value, 0);
    const colors = this.getColors(data.data.length);
    const startY = 2.0;

    data.data.forEach((item, i) => {
      const y = startY + i * 0.6;
      const pct = ((item.value / total) * 100).toFixed(1);

      // Ô màu
      slide.addShape(this.generator.getShapes().RECTANGLE as any, {
        x: 8.2,
        y: y + 0.1,
        w: 0.3,
        h: 0.3,
        fill: { color: colors[i] },
        rectRadius: 0.03,
      });

      // Nhãn
      this.generator.addText(slide, {
        x: 8.7,
        y: y,
        w: 3,
        h: 0.25,
        text: item.label,
        fontSize: 12,
        fontFace: 'Arial',
        color: this.theme.text,
        bold: true,
        align: 'left',
        valign: 'middle',
      });

      // Giá trị số và phần trăm
      this.generator.addText(slide, {
        x: 8.7,
        y: y + 0.25,
        w: 3,
        h: 0.25,
        text: `${item.value} (${pct}%)`,
        fontSize: 10,
        fontFace: 'Arial',
        color: this.theme.muted,
        align: 'left',
        valign: 'middle',
      });
    });

    // Mô tả
    if (data.description) {
      this.generator.addText(slide, {
        x: 0.8,
        y: 6.8,
        w: 11.5,
        h: 0.5,
        text: data.description,
        fontSize: 10,
        fontFace: 'Arial',
        color: this.theme.muted,
        align: 'left',
        valign: 'middle',
      });
    }

    return slide;
  }
}

/**
 * Trang biểu đồ đường (Line Chart)
 * Sử dụng tính năng biểu đồ tích hợp của pptxgenjs để tạo biểu đồ đường
 */
export class LineChart extends BaseChart {
  constructor(generator: TemplateGenerator, theme: Theme) {
    super(generator, theme);
  }

  generate(data: ChartPageData): pptxgen.Slide {
    const slide = this.generator.createSlide();
    const pptx = this.generator.getPresentation();

    slide.background = { fill: this.theme.background };

    // Tiêu đề trang
    this.addPageTitle(slide, data.pageTitle);

    // Tiêu đề biểu đồ
    if (data.chartTitle) {
      this.generator.addText(slide, {
        x: 0.5,
        y: 1.1,
        w: 12,
        h: 0.5,
        text: data.chartTitle,
        fontSize: 16,
        fontFace: 'Arial',
        color: this.theme.text,
        bold: true,
        align: 'left',
        valign: 'middle',
      });
    }

    // Biểu đồ đường
    const chartData = [
      {
        name: 'Xu hướng',
        labels: data.data.map(d => d.label),
        values: data.data.map(d => d.value),
      },
    ];

    slide.addChart(this.generator.getCharts().LINE as any, chartData, {
      x: 0.8,
      y: 1.8,
      w: 11.5,
      h: 4.5,
      lineSmooth: true,
      lineSize: 3,
      chartColors: [this.theme.primary],
      showLegend: false,
      showValue: true,
      dataLabelFontSize: 9,
      catAxisLabelFontSize: 10,
      catAxisLabelColor: this.theme.text,
      valAxisLabelFontSize: 9,
      valAxisLabelColor: this.theme.muted,
      plotArea: { fill: { color: 'FFFFFF' } },
      lineDataSymbol: 'circle',
      lineDataSymbolSize: 8,
      showTitle: false,
    });

    // Tóm tắt thống kê phía dưới
    const values = data.data.map(d => d.value);
    const max = Math.max(...values);
    const min = Math.min(...values);
    const avg = (values.reduce((a, b) => a + b, 0) / values.length).toFixed(1);
    const maxItem = data.data.find(d => d.value === max);
    const minItem = data.data.find(d => d.value === min);

    const summaryItems = [
      { label: 'Cao nhất', value: `${max}`, detail: maxItem?.label || '' },
      { label: 'Thấp nhất', value: `${min}`, detail: minItem?.label || '' },
      { label: 'Trung bình', value: avg, detail: '' },
      { label: 'Số điểm dữ liệu', value: String(data.data.length), detail: '' },
    ];

    summaryItems.forEach((item, i) => {
      const x = 0.8 + i * 3;

      slide.addShape(this.generator.getShapes().RECTANGLE as any, {
        x: x,
        y: 6.5,
        w: 2.5,
        h: 0.8,
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

      this.generator.addText(slide, {
        x: x + 0.1,
        y: 6.5,
        w: 1,
        h: 0.35,
        text: item.label,
        fontSize: 9,
        fontFace: 'Arial',
        color: this.theme.muted,
        align: 'left',
        valign: 'middle',
      });

      this.generator.addText(slide, {
        x: x + 0.1,
        y: 6.8,
        w: 1.5,
        h: 0.4,
        text: item.value,
        fontSize: 18,
        fontFace: 'Arial',
        color: this.theme.primary,
        bold: true,
        align: 'left',
        valign: 'middle',
      });
    });

    // Mô tả
    if (data.description) {
      this.generator.addText(slide, {
        x: 11.3,
        y: 6.55,
        w: 2,
        h: 0.5,
        text: data.description,
        fontSize: 9,
        fontFace: 'Arial',
        color: this.theme.muted,
        align: 'right',
        valign: 'middle',
      });
    }

    return slide;
  }
}

/**
 * Trang biểu đồ hoạt họa (Animated Chart)
 * Trình bày biểu đồ trực quan với hiệu ứng bậc thang tiến dần
 */
export class AnimatedChart extends BaseChart {
  constructor(generator: TemplateGenerator, theme: Theme) {
    super(generator, theme);
  }

  generate(data: ChartPageData): pptxgen.Slide {
    const slide = this.generator.createSlide();
    const pptx = this.generator.getPresentation();

    slide.background = { fill: this.theme.background };

    // Tiêu đề trang
    this.addPageTitle(slide, data.pageTitle);

    // Tiêu đề biểu đồ
    if (data.chartTitle) {
      this.generator.addText(slide, {
        x: 0.5,
        y: 1.1,
        w: 12,
        h: 0.5,
        text: data.chartTitle,
        fontSize: 16,
        fontFace: 'Arial',
        color: this.theme.text,
        bold: true,
        align: 'left',
        valign: 'middle',
      });
    }

    // Hiệu ứng cột đồ họa (kèm màu chuyển sắc)
    const items = data.data;
    const maxValue = Math.max(...items.map(d => d.value));
    const chartX = 1.0;
    const chartY = 2.0;
    const chartW = 10;
    const chartH = 4.5;
    const barWidth = chartW / (items.length * 1.5);
    const gap = barWidth * 0.5;
    const colors = this.getColors(items.length);

    // Đường lưới nền
    for (let i = 0; i <= 5; i++) {
      const gridY = chartY + (chartH / 5) * i;
      slide.addShape(this.generator.getShapes().LINE as any, {
        x: chartX,
        y: gridY,
        w: chartW,
        h: 0,
        line: { color: this.theme.muted, width: 0.3, transparency: 70 },
      });

      // Nhãn trục Y
      const value = Math.round(maxValue * (5 - i) / 5);
      this.generator.addText(slide, {
        x: chartX - 0.6,
        y: gridY - 0.15,
        w: 0.5,
        h: 0.3,
        text: String(value),
        fontSize: 8,
        fontFace: 'Arial',
        color: this.theme.muted,
        align: 'right',
        valign: 'middle',
      });
    }

    items.forEach((item, i) => {
      const barHeight = (item.value / maxValue) * chartH;
      const x = chartX + i * (barWidth + gap) + gap / 2;
      const y = chartY + chartH - barHeight;

      // Cột biểu đồ
      slide.addShape(this.generator.getShapes().RECTANGLE as any, {
        x: x,
        y: y,
        w: barWidth,
        h: barHeight,
        fill: { color: colors[i] },
        rectRadius: 0.05,
        shadow: {
          type: 'outer' as any,
          color: '000000',
          blur: 4,
          offset: 2,
          angle: 135,
          opacity: 0.1,
        },
      });

      // Nhãn giá trị số
      this.generator.addText(slide, {
        x: x,
        y: y - 0.3,
        w: barWidth,
        h: 0.3,
        text: String(item.value),
        fontSize: 10,
        fontFace: 'Arial',
        color: this.theme.text,
        bold: true,
        align: 'center',
        valign: 'middle',
      });

      // Nhãn trục X
      this.generator.addText(slide, {
        x: x - 0.2,
        y: chartY + chartH + 0.1,
        w: barWidth + 0.4,
        h: 0.35,
        text: item.label,
        fontSize: 9,
        fontFace: 'Arial',
        color: this.theme.text,
        align: 'center',
        valign: 'top',
      });
    });

    // Mô tả phía dưới
    if (data.description) {
      this.generator.addText(slide, {
        x: 0.8,
        y: 6.8,
        w: 11.5,
        h: 0.5,
        text: data.description,
        fontSize: 10,
        fontFace: 'Arial',
        color: this.theme.muted,
        align: 'left',
        valign: 'middle',
      });
    }

    return slide;
  }
}
