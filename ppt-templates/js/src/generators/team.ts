/**
 * Mô-đun bộ tạo trang đội ngũ (Team)
 * Bao gồm 3 mẫu giới thiệu đội ngũ phong cách đa dạng:
 * - Thẻ nhân vật, Lưới đội ngũ, Sơ đồ tổ chức
 */

import pptxgen from 'pptxgenjs';
import { TemplateGenerator, Theme } from '../base';
import { createGridPositions } from '../utils';

/** Giao diện dữ liệu thành viên đội ngũ */
export interface TeamMember {
  /** Họ và tên */
  name: string;
  /** Chức vụ */
  title: string;
  /** Tiểu sử tóm tắt */
  description?: string;
  /** Đường dẫn ảnh đại diện */
  avatar?: string;
  /** Email */
  email?: string;
  /** Phòng ban */
  department?: string;
}

/** Giao diện dữ liệu trang đội ngũ */
export interface TeamData {
  /** Tiêu đề trang */
  pageTitle: string;
  /** Danh sách thành viên đội ngũ */
  members: TeamMember[];
}

/** Lớp đội ngũ cơ sở */
abstract class BaseTeam {
  protected generator: TemplateGenerator;
  protected theme: Theme;

  constructor(generator: TemplateGenerator, theme: Theme) {
    this.generator = generator;
    this.theme = theme;
  }

  /** Tạo trang đội ngũ */
  abstract generate(data: TeamData): pptxgen.Slide;

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
 * Thẻ nhân vật (Person Card)
 * Thẻ khổ lớn giới thiệu chi tiết từng thành viên nổi bật
 */
export class PersonCard extends BaseTeam {
  constructor(generator: TemplateGenerator, theme: Theme) {
    super(generator, theme);
  }

  generate(data: TeamData): pptxgen.Slide {
    const slide = this.generator.createSlide();
    const pptx = this.generator.getPresentation();

    slide.background = { fill: this.theme.background };

    // Tiêu đề trang
    this.addPageTitle(slide, data.pageTitle);

    const members = data.members.slice(0, 3); // Hiển thị tối đa 3 thành viên
    const cardWidth = 3.6;
    const cardHeight = 5.5;
    const startX = 0.65;
    const startY = 1.4;
    const gap = 0.5;

    members.forEach((member, i) => {
      const x = startX + i * (cardWidth + gap);

      // Nền thẻ
      slide.addShape(this.generator.getShapes().RECTANGLE as any, {
        x: x,
        y: startY,
        w: cardWidth,
        h: cardHeight,
        fill: { color: 'FFFFFF' },
        rectRadius: 0.1,
        shadow: {
          type: 'outer' as any,
          color: '000000',
          blur: 10,
          offset: 4,
          angle: 135,
          opacity: 0.1,
        },
      });

      // Vùng giữ chỗ ảnh đại diện
      slide.addShape(this.generator.getShapes().OVAL as any, {
        x: x + (cardWidth - 1.8) / 2,
        y: startY + 0.4,
        w: 1.8,
        h: 1.8,
        fill: { color: this.theme.primary, transparency: 85 },
        line: { color: this.theme.primary, width: 2 },
      });

      // Chữ cái đầu tên đại diện
      const initial = member.name.charAt(0);
      this.generator.addText(slide, {
        x: x + (cardWidth - 1.8) / 2,
        y: startY + 0.4,
        w: 1.8,
        h: 1.8,
        text: initial,
        fontSize: 36,
        fontFace: 'Arial',
        color: this.theme.primary,
        bold: true,
        align: 'center',
        valign: 'middle',
      });

      // Họ và tên
      this.generator.addText(slide, {
        x: x + 0.2,
        y: startY + 2.5,
        w: cardWidth - 0.4,
        h: 0.5,
        text: member.name,
        fontSize: 20,
        fontFace: 'Arial',
        color: this.theme.text,
        bold: true,
        align: 'center',
        valign: 'middle',
      });

      // Chức danh
      this.generator.addText(slide, {
        x: x + 0.2,
        y: startY + 3.0,
        w: cardWidth - 0.4,
        h: 0.4,
        text: member.title,
        fontSize: 13,
        fontFace: 'Arial',
        color: this.theme.primary,
        align: 'center',
        valign: 'middle',
      });

      // Đường phân cách
      slide.addShape(this.generator.getShapes().LINE as any, {
        x: x + 0.5,
        y: startY + 3.5,
        w: cardWidth - 1,
        h: 0,
        line: { color: this.theme.muted, width: 0.5, transparency: 50 },
      });

      // Tiểu sử
      if (member.description) {
        this.generator.addText(slide, {
          x: x + 0.3,
          y: startY + 3.6,
          w: cardWidth - 0.6,
          h: 1.5,
          text: member.description,
          fontSize: 10,
          fontFace: 'Arial',
          color: this.theme.muted,
          align: 'center',
          valign: 'top',
          wrap: true,
          lineSpacingMultiple: 1.4,
        });
      }

      // Email
      if (member.email) {
        this.generator.addText(slide, {
          x: x + 0.3,
          y: startY + 5.0,
          w: cardWidth - 0.6,
          h: 0.3,
          text: member.email,
          fontSize: 9,
          fontFace: 'Arial',
          color: this.theme.muted,
          align: 'center',
          valign: 'middle',
        });
      }
    });

    return slide;
  }
}

/**
 * Lưới đội ngũ (Team Grid)
 * Bố cục dạng lưới sắp xếp các thành viên đội ngũ
 */
export class TeamGrid extends BaseTeam {
  constructor(generator: TemplateGenerator, theme: Theme) {
    super(generator, theme);
  }

  generate(data: TeamData): pptxgen.Slide {
    const slide = this.generator.createSlide();
    const pptx = this.generator.getPresentation();

    slide.background = { fill: this.theme.background };

    // Tiêu đề trang
    this.addPageTitle(slide, data.pageTitle);

    const members = data.members;
    const cols = 4;
    const rows = Math.ceil(members.length / cols);
    const cardWidth = 2.8;
    const cardHeight = 2.0;
    const startX = 0.5;
    const startY = 1.4;
    const gapX = 0.3;
    const gapY = 0.3;

    members.forEach((member, i) => {
      const col = i % cols;
      const row = Math.floor(i / cols);
      const x = startX + col * (cardWidth + gapX);
      const y = startY + row * (cardHeight + gapY);
      const colors = [this.theme.primary, this.theme.secondary, this.theme.accent, '4CAF50'];
      const color = colors[i % colors.length];

      // Thẻ
      slide.addShape(this.generator.getShapes().RECTANGLE as any, {
        x: x,
        y: y,
        w: cardWidth,
        h: cardHeight,
        fill: { color: 'FFFFFF' },
        rectRadius: 0.08,
        shadow: {
          type: 'outer' as any,
          color: '000000',
          blur: 5,
          offset: 2,
          angle: 135,
          opacity: 0.08,
        },
      });

      // Khung tròn ảnh đại diện
      slide.addShape(this.generator.getShapes().OVAL as any, {
        x: x + 0.2,
        y: y + 0.3,
        w: 0.8,
        h: 0.8,
        fill: { color: color, transparency: 80 },
        line: { color: color, width: 1.5 },
      });

      // Chữ cái đầu tên đại diện
      this.generator.addText(slide, {
        x: x + 0.2,
        y: y + 0.3,
        w: 0.8,
        h: 0.8,
        text: member.name.charAt(0),
        fontSize: 18,
        fontFace: 'Arial',
        color: color,
        bold: true,
        align: 'center',
        valign: 'middle',
      });

      // Họ và tên
      this.generator.addText(slide, {
        x: x + 1.1,
        y: y + 0.25,
        w: cardWidth - 1.3,
        h: 0.4,
        text: member.name,
        fontSize: 14,
        fontFace: 'Arial',
        color: this.theme.text,
        bold: true,
        align: 'left',
        valign: 'middle',
      });

      // Chức danh
      this.generator.addText(slide, {
        x: x + 1.1,
        y: y + 0.65,
        w: cardWidth - 1.3,
        h: 0.35,
        text: member.title,
        fontSize: 10,
        fontFace: 'Arial',
        color: this.theme.muted,
        align: 'left',
        valign: 'middle',
      });

      // Tiểu sử (cắt ngắn)
      if (member.description) {
        const desc = member.description.length > 40
          ? member.description.substring(0, 40) + '...'
          : member.description;
        this.generator.addText(slide, {
          x: x + 0.2,
          y: y + 1.2,
          w: cardWidth - 0.4,
          h: 0.7,
          text: desc,
          fontSize: 9,
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
 * Sơ đồ tổ chức (Org Chart)
 * Cấu trúc hình cây phân cấp hiển thị cơ cấu tổ chức
 */
export class OrgChart extends BaseTeam {
  constructor(generator: TemplateGenerator, theme: Theme) {
    super(generator, theme);
  }

  generate(data: TeamData): pptxgen.Slide {
    const slide = this.generator.createSlide();
    const pptx = this.generator.getPresentation();

    slide.background = { fill: this.theme.background };

    // Tiêu đề trang
    this.addPageTitle(slide, data.pageTitle);

    const members = data.members;
    const nodeW = 2.2;
    const nodeH = 1.0;

    // Giả định người đầu tiên là lãnh đạo, còn lại là cấp dưới
    if (members.length === 0) return slide;

    // Nút lãnh đạo trên cùng
    const leaderX = (13.33 - nodeW) / 2;
    const leaderY = 1.6;

    this.drawOrgNode(slide, pptx, members[0], leaderX, leaderY, nodeW, nodeH, true);

    // Các nút cấp dưới
    const subordinates = members.slice(1);
    if (subordinates.length > 0) {
      const subStartX = (13.33 - subordinates.length * (nodeW + 0.3) + 0.3) / 2;
      const subY = 3.5;

      // Đường liên kết (từ lãnh đạo đến cấp dưới)
      slide.addShape(this.generator.getShapes().LINE as any, {
        x: 13.33 / 2,
        y: leaderY + nodeH,
        w: 0,
        h: subY - leaderY - nodeH,
        line: { color: this.theme.primary, width: 1.5 },
      });

      // Đường liên kết ngang
      if (subordinates.length > 1) {
        const firstSubX = subStartX + nodeW / 2;
        const lastSubX = subStartX + (subordinates.length - 1) * (nodeW + 0.3) + nodeW / 2;

        slide.addShape(this.generator.getShapes().LINE as any, {
          x: firstSubX,
          y: subY,
          w: lastSubX - firstSubX,
          h: 0,
          line: { color: this.theme.primary, width: 1.5 },
        });
      }

      subordinates.forEach((member, i) => {
        const x = subStartX + i * (nodeW + 0.3);

        // Đường liên kết dọc
        slide.addShape(this.generator.getShapes().LINE as any, {
          x: x + nodeW / 2,
          y: leaderY + nodeH,
          w: 0,
          h: subY - leaderY - nodeH + 0.3,
          line: { color: this.theme.primary, width: 1 },
        });

        this.drawOrgNode(slide, pptx, member, x, subY, nodeW, nodeH, false);
      });
    }

    return slide;
  }

  /** Vẽ nút trong sơ đồ tổ chức */
  private drawOrgNode(
    slide: pptxgen.Slide,
    pptx: pptxgen,
    member: TeamMember,
    x: number,
    y: number,
    w: number,
    h: number,
    isLeader: boolean
  ): void {
    const color = isLeader ? this.theme.primary : this.theme.secondary;

    // Thẻ nút tổ chức
    slide.addShape(this.generator.getShapes().RECTANGLE as any, {
      x: x,
      y: y,
      w: w,
      h: h,
      fill: { color: 'FFFFFF' },
      rectRadius: 0.08,
      line: { color: color, width: isLeader ? 2 : 1 },
      shadow: {
        type: 'outer' as any,
        color: '000000',
        blur: 5,
        offset: 2,
        angle: 135,
        opacity: 0.08,
      },
    });

    // Dải màu trên cùng
    slide.addShape(this.generator.getShapes().RECTANGLE as any, {
      x: x,
      y: y,
      w: w,
      h: 0.06,
      fill: { color: color },
    });

    // Họ và tên
    this.generator.addText(slide, {
      x: x + 0.1,
      y: y + 0.15,
      w: w - 0.2,
      h: 0.4,
      text: member.name,
      fontSize: isLeader ? 14 : 12,
      fontFace: 'Arial',
      color: this.theme.text,
      bold: true,
      align: 'center',
      valign: 'middle',
    });

    // Chức danh
    this.generator.addText(slide, {
      x: x + 0.1,
      y: y + 0.55,
      w: w - 0.2,
      h: 0.35,
      text: member.title,
      fontSize: isLeader ? 11 : 9,
      fontFace: 'Arial',
      color: this.theme.muted,
      align: 'center',
      valign: 'middle',
    });
  }
}
