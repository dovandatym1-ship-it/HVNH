/**
 * Module bộ lắp ráp bài thuyết trình hoàn chỉnh
 * Chứa 6 mẫu bài thuyết trình hoàn chỉnh được thiết lập sẵn:
 * - Kế hoạch kinh doanh, Định hướng nghề nghiệp, Ra mắt sản phẩm, Báo cáo thường niên, Khóa học giáo dục, Chủ đề công nghệ
 */

import { TemplateGenerator, Theme } from '../base';
import { blueTechnology, purpleGradient, darkGold, minimalistBW, oceanBlue, greenNature, redBusiness } from '../themes';
import { GeometricRotation, CircleRing, MinimalistGradient, SplitScreen } from './cover';
import { CardGrid, Sidebar, DiamondAnimated } from './directory';
import { TextImageLayout, ThreeColumn, FourGrid, Comparison, FullImageOverlay } from './content';
import { Horizontal, Vertical, DualWave, TimelineData, TimelineItem } from './timeline';
import { BarChart, PieChart, LineChart, ChartPageData, ChartDataItem } from './chart';
import { PersonCard, TeamGrid, TeamData, TeamMember } from './team';
import { ThankYou, Contact, EndingData } from './ending';
import { CoverData } from './cover';
import { DirectoryData, DirectoryItem } from './directory';
import { ContentData, ContentBlock } from './content';

/** Giao diện cấu hình bài thuyết trình hoàn chỉnh */
export interface DeckConfig {
  /** Tiêu đề bài thuyết trình */
  title: string;
  /** Phụ đề */
  subtitle?: string;
  /** Tác giả / Người thuyết trình */
  presenter?: string;
  /** Ngày tháng */
  date?: string;
  /** Tên công ty */
  company?: string;
  /** Chủ đề */
  theme?: Theme;
  /** Dữ liệu tùy chỉnh */
  customData?: Record<string, any>;
}

/**
 * Bộ lắp ráp bài thuyết trình hoàn chỉnh cơ sở
 * Cung cấp quy trình xây dựng dùng chung
 */
abstract class BaseCompleteDeck {
  protected config: DeckConfig;
  protected generator: TemplateGenerator;
  protected theme: Theme;

  constructor(config: DeckConfig) {
    this.theme = config.theme || blueTechnology;
    this.generator = new TemplateGenerator(this.theme);
    this.config = config;
  }

  /** Tạo bài thuyết trình hoàn chỉnh */
  async generate(): Promise<void> {
    this.generator.setTitle(this.config.title);
    await this.addCover();
    await this.addDirectory();
    await this.addContent();
    await this.addTimeline();
    await this.addCharts();
    await this.addTeam();
    await this.addEnding();
  }

  /** Lưu tệp */
  async save(fileName: string): Promise<string> {
    return this.generator.save(fileName);
  }

  /** Lấy phiên bản bộ tạo */
  getGenerator(): TemplateGenerator {
    return this.generator;
  }

  protected abstract addCover(): Promise<void>;
  protected abstract addDirectory(): Promise<void>;
  protected abstract addContent(): Promise<void>;
  protected abstract addTimeline(): Promise<void>;
  protected abstract addCharts(): Promise<void>;
  protected abstract addTeam(): Promise<void>;
  protected abstract addEnding(): Promise<void>;
}

/**
 * Bài thuyết trình Kế hoạch kinh doanh
 * Bao gồm: Trang bìa, Mục lục, Phân tích thị trường, Mô hình kinh doanh, Giới thiệu đội ngũ, Dự báo tài chính, Thông tin liên hệ
 */
export class BusinessPlan extends BaseCompleteDeck {
  constructor(config: DeckConfig) {
    super({ ...config, theme: config.theme || blueTechnology });
  }

  protected async addCover(): Promise<void> {
    const cover = new GeometricRotation(this.generator, this.theme);
    cover.generate({
      title: this.config.title,
      subtitle: this.config.subtitle || 'Kế hoạch kinh doanh',
      presenter: this.config.presenter,
      date: this.config.date,
      company: this.config.company,
    });
  }

  protected async addDirectory(): Promise<void> {
    const dir = new Sidebar(this.generator, this.theme);
    dir.generate({
      pageTitle: 'Mục lục',
      items: [
        { index: 1, title: 'Tổng quan dự án', description: 'Bối cảnh và tầm nhìn dự án' },
        { index: 2, title: 'Phân tích thị trường', description: 'Xu hướng ngành và bối cảnh cạnh tranh' },
        { index: 3, title: 'Mô hình kinh doanh', description: 'Mô hình doanh thu và tuyên ngôn giá trị' },
        { index: 4, title: 'Đội ngũ phát triển', description: 'Các thành viên nòng cốt' },
        { index: 5, title: 'Dự báo tài chính', description: 'Dự báo doanh thu và chi phí' },
        { index: 6, title: 'Kế hoạch phát triển', description: 'Kế hoạch trong 3 năm tới' },
      ],
    });
  }

  protected async addContent(): Promise<void> {
    // Phân tích thị trường - Bố cục ba cột
    const threeCol = new ThreeColumn(this.generator, this.theme);
    threeCol.generate({
      pageTitle: 'Phân tích thị trường',
      blocks: [
        { index: 1, title: 'Quy mô thị trường', content: 'Quy mô thị trường mục tiêu dự kiến đạt 500 tỷ đồng vào năm 2025 với tốc độ tăng trưởng bình quân hàng năm 25%. Cùng với tiến bộ công nghệ và nâng cấp tiêu dùng, tiềm năng thị trường là rất lớn.' },
        { index: 2, title: 'Bối cảnh cạnh tranh', content: 'Hiện tại bối cảnh cạnh tranh trên thị trường còn phân tán, các doanh nghiệp dẫn đầu chiếm chưa đến 20% thị phần. Chiến lược cạnh tranh tạo sự khác biệt sẽ là yếu tố quyết định thành công.' },
        { index: 3, title: 'Nhu cầu người dùng', content: 'Yêu cầu của người dùng đối với chất lượng sản phẩm và trải nghiệm dịch vụ không ngừng nâng cao; cá nhân hóa và thông minh hóa trở thành xu hướng nhu cầu chính.' },
      ],
    });

    // Mô hình kinh doanh - Văn bản kết hợp hình ảnh
    const textImage = new TextImageLayout(this.generator, this.theme);
    textImage.generate({
      pageTitle: 'Mô hình kinh doanh',
      blocks: [
        {
          title: 'Tuyên ngôn giá trị cốt lõi',
          content: 'Chúng tôi ứng dụng các giải pháp công nghệ đổi mới sáng tạo nhằm mang đến cho người dùng giải pháp thông minh, tiện lợi và hiệu quả cao. Lấy nhu cầu người dùng làm định hướng, liên tục tối ưu hóa trải nghiệm sản phẩm để xây dựng giá trị lâu dài. Mô hình kinh doanh của chúng tôi được thúc đẩy bởi sự đổi mới công nghệ và trải nghiệm người dùng, đạt tăng trưởng doanh thu bền vững thông qua mô hình thuê bao SaaS.',
        },
      ],
    });

    // So sánh đối thủ cạnh tranh
    const comparison = new Comparison(this.generator, this.theme);
    comparison.generate({
      pageTitle: 'Lợi thế cạnh tranh',
      blocks: [
        { title: 'Lợi thế của chúng tôi', content: '- Công nghệ tiên phong, sở hữu bằng sáng chế cốt lõi\n- Trải nghiệm người dùng vượt trội, tỷ lệ hài lòng 95%\n- Đội ngũ giàu kinh nghiệm, năng lực thực thi mạnh mẽ\n- Kiểm soát chi phí tối ưu, tỷ suất lợi nhuận cao\n- Hệ sinh thái hoàn chỉnh, rào cản gia nhập cao' },
        { title: 'Hạn chế của đối thủ', content: '- Cập nhật công nghệ chậm, thiếu đổi mới sáng tạo\n- Trải nghiệm người dùng bình thường, tỷ lệ khiếu nại cao\n- Đội ngũ thiếu ổn định, tỷ lệ biến động nhân sự lớn\n- Cấu trúc chi phí chưa hợp lý\n- Định vị thị trường chưa rõ ràng' },
      ],
    });
  }

  protected async addTimeline(): Promise<void> {
    const timeline = new Horizontal(this.generator, this.theme);
    timeline.generate({
      pageTitle: 'Kế hoạch phát triển',
      items: [
        { date: '2024 Q1', title: 'Ra mắt sản phẩm', description: 'Hoàn thiện phát triển sản phẩm và chính thức ra mắt' },
        { date: '2024 Q3', title: 'Mở rộng thị trường', description: 'Thâm nhập các thị trường mục tiêu trọng điểm' },
        { date: '2025 Q1', title: 'Tăng trưởng người dùng', description: 'Đạt cột mốc 100.000 người dùng' },
        { date: '2025 Q3', title: 'Mục tiêu lợi nhuận', description: 'Đạt điểm hòa vốn' },
        { date: '2026 Q1', title: 'Mở rộng quy mô', description: 'Tiến ra thị trường quốc tế' },
      ],
    });
  }

  protected async addCharts(): Promise<void> {
    // Dự báo tài chính - Biểu đồ cột
    const barChart = new BarChart(this.generator, this.theme);
    barChart.generate({
      pageTitle: 'Dự báo tài chính',
      chartTitle: 'Dự báo doanh thu hàng năm (tỷ đồng)',
      data: [
        { label: 'Năm 2024', value: 500 },
        { label: 'Năm 2025', value: 1200 },
        { label: 'Năm 2026', value: 3000 },
        { label: 'Năm 2027', value: 5500 },
      ],
      description: 'Dựa trên xu hướng thị trường hiện tại và kỳ vọng tăng trưởng kinh doanh, dự kiến trong bốn năm tới doanh thu sẽ duy trì tốc độ tăng trưởng cao.',
    });

    // Cơ cấu doanh thu - Biểu đồ tròn
    const pieChart = new PieChart(this.generator, this.theme);
    pieChart.generate({
      pageTitle: 'Cơ cấu doanh thu',
      chartTitle: 'Tỷ trọng nguồn doanh thu dự kiến',
      data: [
        { label: 'Thuê bao SaaS', value: 45 },
        { label: 'Tùy chỉnh doanh nghiệp', value: 25 },
        { label: 'Dịch vụ dữ liệu', value: 20 },
        { label: 'Đào tạo & tư vấn', value: 10 },
      ],
    });
  }

  protected async addTeam(): Promise<void> {
    const team = new PersonCard(this.generator, this.theme);
    team.generate({
      pageTitle: 'Đội ngũ nòng cốt',
      members: [
        { name: 'Trần Minh', title: 'CEO / Nhà sáng lập', description: '10 năm kinh nghiệm ngành Internet, từng giữ chức Phó chủ tịch tại công ty niêm yết' },
        { name: 'Lê Hoa', title: 'CTO', description: 'Chuyên gia lĩnh vực trí tuệ nhân tạo, sở hữu nhiều bằng sáng chế công nghệ' },
        { name: 'Vương Phương', title: 'COO', description: 'Chuyên gia quản trị vận hành kỳ cựu, am hiểu hoạch định chiến lược doanh nghiệp' },
      ],
    });
  }

  protected async addEnding(): Promise<void> {
    const contact = new Contact(this.generator, this.theme);
    contact.generate({
      title: 'Liên hệ với chúng tôi',
      subtitle: 'Rất mong có cơ hội hợp tác cùng quý đối tác',
      company: this.config.company || 'Công ty Mẫu',
      email: 'contact@example.com',
      phone: '1900-8888',
      website: 'www.example.com',
      address: 'Tòa nhà văn phòng Mẫu, Quận Ba Đình, Hà Nội',
    });
  }
}

/**
 * Bài thuyết trình Định hướng nghề nghiệp
 */
export class CareerPlanning extends BaseCompleteDeck {
  constructor(config: DeckConfig) {
    super({ ...config, theme: config.theme || purpleGradient });
  }

  protected async addCover(): Promise<void> {
    const cover = new CircleRing(this.generator, this.theme);
    cover.generate({
      title: this.config.title,
      subtitle: this.config.subtitle || 'Kế hoạch phát triển nghề nghiệp',
      presenter: this.config.presenter,
      date: this.config.date,
    });
  }

  protected async addDirectory(): Promise<void> {
    const dir = new DiamondAnimated(this.generator, this.theme);
    dir.generate({
      pageTitle: 'Mục lục',
      items: [
        { index: 1, title: 'Phân tích bản thân', description: 'Đánh giá tính cách và năng lực' },
        { index: 2, title: 'Mục tiêu nghề nghiệp', description: 'Mục tiêu ngắn hạn và dài hạn' },
        { index: 3, title: 'Kế hoạch hành động', description: 'Các bước thực hiện cụ thể' },
        { index: 4, title: 'Đánh giá điều chỉnh', description: 'Định kỳ xem xét và hoàn thiện' },
      ],
    });
  }

  protected async addContent(): Promise<void> {
    const fourGrid = new FourGrid(this.generator, this.theme);
    fourGrid.generate({
      pageTitle: 'Phân tích bản thân',
      blocks: [
        { index: 1, title: 'Đặc điểm tính cách', content: 'Tính cách hướng ngoại, giỏi giao tiếp và điều phối, có năng lực lãnh đạo và làm việc nhóm tốt.' },
        { index: 2, title: 'Kỹ năng chuyên môn', content: 'Nền tảng chuyên ngành Khoa học Máy tính, thành thạo lập trình và năng lực phân tích dữ liệu.' },
        { index: 3, title: 'Sở thích đam mê', content: 'Quan tâm sâu sắc đến trí tuệ nhân tạo và các công nghệ mới nổi, đam mê đổi mới kỹ thuật.' },
        { index: 4, title: 'Hệ giá trị', content: 'Theo đuổi sự cân bằng giữa công việc và cuộc sống, coi trọng sự phát triển cá nhân và đóng góp cho xã hội.' },
      ],
    });
  }

  protected async addTimeline(): Promise<void> {
    const timeline = new DualWave(this.generator, this.theme);
    timeline.generate({
      pageTitle: 'Lộ trình phát triển sự nghiệp',
      items: [
        { date: 'Năm 1', title: 'Kỹ sư cơ sở', description: 'Tích lũy kinh nghiệm dự án' },
        { date: 'Năm 3', title: 'Kỹ sư cao cấp', description: 'Đào sâu chuyên môn kỹ thuật' },
        { date: 'Năm 5', title: 'Trưởng nhóm kỹ thuật', description: 'Dẫn dắt đội ngũ kỹ sư' },
        { date: 'Năm 8', title: 'Giám đốc kỹ thuật', description: 'Hoạch định chiến lược công nghệ' },
        { date: 'Năm 10', title: 'CTO', description: 'Ra quyết định công nghệ toàn diện' },
      ],
    });
  }

  protected async addCharts(): Promise<void> {
    const chart = new BarChart(this.generator, this.theme);
    chart.generate({
      pageTitle: 'Đánh giá năng lực',
      chartTitle: 'Điểm năng lực cốt lõi (Thang điểm 10)',
      data: [
        { label: 'Năng lực lập trình', value: 8 },
        { label: 'Kỹ năng giao tiếp', value: 9 },
        { label: 'Năng lực lãnh đạo', value: 7 },
        { label: 'Tư duy đổi mới', value: 8 },
        { label: 'Khả năng chịu áp lực', value: 7 },
      ],
    });
  }

  protected async addTeam(): Promise<void> {
    const team = new TeamGrid(this.generator, this.theme);
    team.generate({
      pageTitle: 'Người hướng dẫn & Hình mẫu',
      members: [
        { name: 'GS. Trần', title: 'Cố vấn học thuật', description: 'Giáo sư Viện Công nghệ Thông tin' },
        { name: 'GĐ. Lê', title: 'Cố vấn ngành', description: 'CTO doanh nghiệp công nghệ lớn' },
        { name: 'Tiền bối Vương', title: 'Hình mẫu nghề nghiệp', description: 'Doanh nhân khởi nghiệp thành công' },
      ],
    });
  }

  protected async addEnding(): Promise<void> {
    const thankYou = new ThankYou(this.generator, this.theme);
    thankYou.generate({
      title: 'Cảm ơn đã chú ý lắng nghe',
      subtitle: 'Làm chủ tương lai, kiến tạo thành công',
      company: this.config.presenter || 'Người thuyết trình',
    });
  }
}

/**
 * Bài thuyết trình Ra mắt sản phẩm
 */
export class ProductLaunch extends BaseCompleteDeck {
  constructor(config: DeckConfig) {
    super({ ...config, theme: config.theme || redBusiness });
  }

  protected async addCover(): Promise<void> {
    const cover = new MinimalistGradient(this.generator, this.theme);
    cover.generate({
      title: this.config.title,
      subtitle: this.config.subtitle || 'Lễ ra mắt sản phẩm mới',
      presenter: this.config.presenter,
      date: this.config.date,
      company: this.config.company,
    });
  }

  protected async addDirectory(): Promise<void> {
    const dir = new CardGrid(this.generator, this.theme);
    dir.generate({
      pageTitle: 'Nội dung sự kiện',
      items: [
        { index: 1, title: 'Triết lý sản phẩm', description: 'Lý do kiến tạo sản phẩm' },
        { index: 2, title: 'Tính năng cốt lõi', description: 'Trình diễn điểm nổi bật' },
        { index: 3, title: 'Kiến trúc công nghệ', description: 'Khám phá công nghệ nền tảng' },
        { index: 4, title: 'Tình huống ứng dụng', description: 'Kịch bản sử dụng thực tế' },
        { index: 5, title: 'Chính sách giá', description: 'Bảng giá và các gói dịch vụ' },
      ],
    });
  }

  protected async addContent(): Promise<void> {
    const fullImage = new FullImageOverlay(this.generator, this.theme);
    fullImage.generate({
      pageTitle: 'Triết lý sản phẩm',
      mainText: 'Chúng tôi tin rằng công nghệ phải giúp cuộc sống trở nên đơn giản hơn. Sản phẩm này xuất phát từ những trăn trở thực tế của người dùng, kết hợp thiết kế đổi mới và công nghệ tiên tiến để tạo nên trải nghiệm người dùng tuyệt vời nhất.',
    });

    const threeCol = new ThreeColumn(this.generator, this.theme);
    threeCol.generate({
      pageTitle: 'Tính năng cốt lõi',
      blocks: [
        { index: 1, title: 'Gợi ý thông minh', content: 'Dựa trên thuật toán AI nhằm cung cấp nội dung gợi ý cá nhân hóa cho người dùng với độ chính xác đạt trên 95%.' },
        { index: 2, title: 'Cộng tác theo thời gian thực', content: 'Hỗ trợ nhiều người dùng cộng tác chỉnh sửa đồng thời theo thời gian thực, độ trễ dưới 100ms, nâng cao hiệu quả làm việc nhóm.' },
        { index: 3, title: 'Phân tích dữ liệu', content: 'Công cụ trực quan hóa dữ liệu mạnh mẽ, giúp người dùng nhanh chóng nắm bắt và khai phá giá trị từ dữ liệu.' },
      ],
    });
  }

  protected async addTimeline(): Promise<void> {
    const timeline = new Vertical(this.generator, this.theme);
    timeline.generate({
      pageTitle: 'Kế hoạch phát hành',
      items: [
        { date: '2024.01', title: 'Giai đoạn thử nghiệm nội bộ', description: 'Mời 500 người dùng tham gia thử nghiệm nội bộ' },
        { date: '2024.03', title: 'Giai đoạn thử nghiệm công chúng', description: 'Mở đăng ký rộng rãi và thu thập ý kiến phản hồi' },
        { date: '2024.06', title: 'Phát hành chính thức', description: 'Triển khai đồng loạt trên tất cả các kênh' },
        { date: '2024.09', title: 'Nâng cấp phiên bản', description: 'Ra mắt phiên bản 2.0 cải tiến' },
      ],
    });
  }

  protected async addCharts(): Promise<void> {
    const pieChart = new PieChart(this.generator, this.theme);
    pieChart.generate({
      pageTitle: 'Phân bố người dùng mục tiêu',
      chartTitle: 'Tỷ trọng các nhóm khách hàng',
      data: [
        { label: 'Người dùng cá nhân', value: 40 },
        { label: 'Doanh nghiệp vừa và nhỏ', value: 35 },
        { label: 'Doanh nghiệp lớn', value: 20 },
        { label: 'Cơ quan nhà nước', value: 5 },
      ],
    });
  }

  protected async addTeam(): Promise<void> {
    const team = new PersonCard(this.generator, this.theme);
    team.generate({
      pageTitle: 'Đội ngũ phát triển sản phẩm',
      members: [
        { name: 'Triệu Cường', title: 'Trưởng nhóm sản phẩm', description: '10 năm kinh nghiệm thiết kế sản phẩm' },
        { name: 'Chu Mẫn', title: 'Trưởng nhóm kỹ thuật', description: 'Kỹ sư Full-stack, kiến trúc sư hệ thống' },
        { name: 'Ngô Tĩnh', title: 'Trưởng nhóm thiết kế', description: 'Chuyên gia thiết kế UI/UX' },
      ],
    });
  }

  protected async addEnding(): Promise<void> {
    const thankYou = new ThankYou(this.generator, this.theme);
    thankYou.generate({
      title: 'Trải nghiệm ngay hôm nay',
      subtitle: 'www.product-example.com',
      company: this.config.company || 'Công ty Sản phẩm',
    });
  }
}

/**
 * Bài thuyết trình Báo cáo thường niên
 */
export class AnnualReport extends BaseCompleteDeck {
  constructor(config: DeckConfig) {
    super({ ...config, theme: config.theme || darkGold });
  }

  protected async addCover(): Promise<void> {
    const cover = new SplitScreen(this.generator, this.theme);
    cover.generate({
      title: this.config.title,
      subtitle: this.config.subtitle || 'Báo cáo thường niên 2024',
      presenter: this.config.presenter,
      date: this.config.date,
      company: this.config.company,
    });
  }

  protected async addDirectory(): Promise<void> {
    const dir = new Sidebar(this.generator, this.theme);
    dir.generate({
      pageTitle: 'Nội dung báo cáo',
      items: [
        { index: 1, title: 'Tổng quan kết quả', description: 'Các chỉ số hiệu quả trọng yếu' },
        { index: 2, title: 'Phân tích hoạt động', description: 'Hiệu quả từng mảng nghiệp vụ' },
        { index: 3, title: 'Phát triển đội ngũ', description: 'Thành tựu xây dựng nguồn nhân lực' },
        { index: 4, title: 'Định hướng tương lai', description: 'Kế hoạch chiến lược năm mới' },
      ],
    });
  }

  protected async addContent(): Promise<void> {
    const fourGrid = new FourGrid(this.generator, this.theme);
    fourGrid.generate({
      pageTitle: 'Tổng quan kết quả',
      blocks: [
        { index: 1, title: 'Doanh thu thuần', content: 'Tổng doanh thu cả năm đạt 1.250 tỷ đồng, tăng trưởng 35% so với cùng kỳ, vượt chỉ tiêu đề ra từ đầu năm.' },
        { index: 2, title: 'Lợi nhuận ròng', content: 'Lợi nhuận sau thuế đạt 280 tỷ đồng, tỷ suất lợi nhuận đạt 22,4%, tăng 3 điểm phần trăm so với năm trước.' },
        { index: 3, title: 'Quy mô người dùng', content: 'Số lượng tài khoản đăng ký vượt mốc 5 triệu, người dùng hoạt động hàng tháng đạt 1,5 triệu, tỷ lệ giữ chân 85%.' },
        { index: 4, title: 'Thị phần', content: 'Thị phần nội địa đạt 15%, tăng 5 điểm phần trăm so với năm trước, vững vàng trong top 3 toàn ngành.' },
      ],
    });
  }

  protected async addTimeline(): Promise<void> {
    const timeline = new Horizontal(this.generator, this.theme);
    timeline.generate({
      pageTitle: 'Các mốc sự kiện quan trọng',
      items: [
        { date: 'Quý 1', title: 'Hoàn tất gọi vốn', description: 'Hoàn tất vòng gọi vốn Series B trị giá 200 tỷ đồng' },
        { date: 'Quý 2', title: 'Nâng cấp sản phẩm', description: 'Chính thức ra mắt phiên bản 3.0' },
        { date: 'Quý 3', title: 'Mở rộng thị trường', description: 'Bắt đầu vươn ra thị trường quốc tế' },
        { date: 'Quý 4', title: 'Hợp tác chiến lược', description: 'Ký kết hợp tác toàn diện với đối tác đầu ngành' },
      ],
    });
  }

  protected async addCharts(): Promise<void> {
    const lineChart = new LineChart(this.generator, this.theme);
    lineChart.generate({
      pageTitle: 'Xu hướng tăng trưởng',
      chartTitle: 'Xu hướng tăng trưởng doanh thu theo tháng (tỷ đồng)',
      data: [
        { label: 'Tháng 1', value: 800 },
        { label: 'Tháng 3', value: 950 },
        { label: 'Tháng 5', value: 1100 },
        { label: 'Tháng 7', value: 1050 },
        { label: 'Tháng 9', value: 1200 },
        { label: 'Tháng 11', value: 1350 },
        { label: 'Tháng 12', value: 1500 },
      ],
      description: 'Doanh thu cả năm duy trì đà tăng trưởng ổn định và bứt phá rõ rệt trong nửa cuối năm.',
    });
  }

  protected async addTeam(): Promise<void> {
    const team = new TeamGrid(this.generator, this.theme);
    team.generate({
      pageTitle: 'Ban điều hành',
      members: [
        { name: 'Ông Tôn', title: 'CEO', description: 'Nhà sáng lập công ty' },
        { name: 'Bà Tiền', title: 'CFO', description: 'Chuyên gia quản trị tài chính' },
        { name: 'Ông Trịnh', title: 'CMO', description: 'Chuyên gia tiếp thị & thị trường' },
        { name: 'Ông Phùng', title: 'CTO', description: 'Giám đốc công nghệ' },
      ],
    });
  }

  protected async addEnding(): Promise<void> {
    const thankYou = new ThankYou(this.generator, this.theme);
    thankYou.generate({
      title: 'Vững bước tiến lên',
      subtitle: 'Cùng nhau kiến tạo tương lai rực rỡ 2025',
      company: this.config.company || 'Công ty Mẫu',
    });
  }
}

/**
 * Bài thuyết trình Khóa học giáo dục
 */
export class EducationCourse extends BaseCompleteDeck {
  constructor(config: DeckConfig) {
    super({ ...config, theme: config.theme || greenNature });
  }

  protected async addCover(): Promise<void> {
    const cover = new MinimalistGradient(this.generator, this.theme);
    cover.generate({
      title: this.config.title,
      subtitle: this.config.subtitle || 'Giới thiệu khóa học',
      presenter: this.config.presenter,
      date: this.config.date,
      company: this.config.company,
    });
  }

  protected async addDirectory(): Promise<void> {
    const dir = new DiamondAnimated(this.generator, this.theme);
    dir.generate({
      pageTitle: 'Đề cương khóa học',
      items: [
        { index: 1, title: 'Tổng quan khóa học', description: 'Mục tiêu và tóm tắt nội dung' },
        { index: 2, title: 'Hệ thống kiến thức', description: 'Hệ thống hóa các chủ đề trọng tâm' },
        { index: 3, title: 'Tình huống thực tế', description: 'Phân tích các dự án thực chiến' },
        { index: 4, title: 'Lộ trình học tập', description: 'Tiến độ học tập khuyến nghị' },
        { index: 5, title: 'Phương thức đánh giá', description: 'Tiêu chí và thang điểm kiểm tra' },
      ],
    });
  }

  protected async addContent(): Promise<void> {
    const threeCol = new ThreeColumn(this.generator, this.theme);
    threeCol.generate({
      pageTitle: 'Hệ thống kiến thức',
      blocks: [
        { index: 1, title: 'Lý thuyết nền tảng', content: 'Giảng giải có hệ thống các khái niệm cốt lõi và nguyên lý cơ bản, xây dựng nền tảng lý thuyết vững chắc. Bao gồm định nghĩa cơ bản, lịch sử phát triển và các kịch bản ứng dụng.' },
        { index: 2, title: 'Phương pháp kỹ thuật', content: 'Giới thiệu chuyên sâu các phương pháp kỹ thuật trọng yếu và sử dụng công cụ, rèn luyện năng lực thao tác thực tế. Bao gồm các framework phổ biến và thực hành tốt nhất.' },
        { index: 3, title: 'Dự án thực chiến', content: 'Thông qua các dự án thực tế, vận dụng tổng hợp kiến thức đã học để giải quyết vấn đề cụ thể. Bao gồm quy trình phát triển dự án trọn vẹn.' },
      ],
    });

    const comparison = new Comparison(this.generator, this.theme);
    comparison.generate({
      pageTitle: 'Đặc điểm nổi bật',
      blocks: [
        { title: 'Khóa học truyền thống', content: '- Nặng về lý thuyết, thiếu thực hành\n- Nội dung cập nhật chậm\n- Giảng dạy một chiều, ít tương tác\n- Tiến độ cứng nhắc, thiếu cá nhân hóa\n- Hình thức đánh giá đơn điệu' },
        { title: 'Khóa học của chúng tôi', content: '- Coi trọng cả lý thuyết lẫn thực hành\n- Cập nhật nội dung hàng tháng\n- Giảng dạy tương tác đa chiều\n- Lộ trình học tập cá nhân hóa\n- Đánh giá toàn diện nhiều khía cạnh' },
      ],
    });
  }

  protected async addTimeline(): Promise<void> {
    const timeline = new DualWave(this.generator, this.theme);
    timeline.generate({
      pageTitle: 'Lộ trình học tập',
      items: [
        { date: 'Tuần 1-2', title: 'Giai đoạn nhập môn', description: 'Nắm vững kiến thức nền tảng' },
        { date: 'Tuần 3-4', title: 'Giai đoạn nâng cao', description: 'Làm chủ công nghệ cốt lõi' },
        { date: 'Tuần 5-6', title: 'Giai đoạn thực chiến', description: 'Thực hành dự án thực tế' },
        { date: 'Tuần 7-8', title: 'Giai đoạn tổng kết', description: 'Hệ thống hóa toàn bộ kiến thức' },
      ],
    });
  }

  protected async addCharts(): Promise<void> {
    const chart = new BarChart(this.generator, this.theme);
    chart.generate({
      pageTitle: 'Hiệu quả học tập',
      chartTitle: 'Mức độ nâng cao năng lực học viên các khóa trước (%)',
      data: [
        { label: 'Kiến thức lý thuyết', value: 85 },
        { label: 'Kỹ năng thực hành', value: 90 },
        { label: 'Kinh nghiệm dự án', value: 75 },
        { label: 'Năng lực cạnh tranh việc làm', value: 88 },
      ],
    });
  }

  protected async addTeam(): Promise<void> {
    const team = new PersonCard(this.generator, this.theme);
    team.generate({
      pageTitle: 'Đội ngũ giảng viên',
      members: [
        { name: 'GS. Vương', title: 'Giảng viên chính', description: 'Giáo sư đại học hàng đầu, 20 năm kinh nghiệm giảng dạy' },
        { name: 'Kỹ sư Lưu', title: 'Cố vấn thực hành', description: 'Kiến trúc sư hệ thống kỳ cựu, chủ trì nhiều dự án quy mô lớn' },
        { name: 'TS. Trần', title: 'Trợ giảng', description: 'Nghiên cứu sinh tiến sĩ, nền tảng học thuật vững vàng' },
      ],
    });
  }

  protected async addEnding(): Promise<void> {
    const thankYou = new ThankYou(this.generator, this.theme);
    thankYou.generate({
      title: 'Tham gia cùng chúng tôi',
      subtitle: 'Khởi đầu hành trình học tập và bứt phá của bạn',
      company: this.config.company || 'Tổ chức giáo dục',
    });
  }
}

/**
 * Bài thuyết trình Chủ đề công nghệ
 */
export class TechnologyTheme extends BaseCompleteDeck {
  constructor(config: DeckConfig) {
    super({ ...config, theme: config.theme || oceanBlue });
  }

  protected async addCover(): Promise<void> {
    const cover = new CircleRing(this.generator, this.theme);
    cover.generate({
      title: this.config.title,
      subtitle: this.config.subtitle || 'Chia sẻ đổi mới công nghệ',
      presenter: this.config.presenter,
      date: this.config.date,
      company: this.config.company,
    });
  }

  protected async addDirectory(): Promise<void> {
    const dir = new CardGrid(this.generator, this.theme);
    dir.generate({
      pageTitle: 'Mục lục nội dung',
      items: [
        { index: 1, title: 'Xu hướng công nghệ', description: 'Diễn biến công nghệ tiên phong trong ngành' },
        { index: 2, title: 'Thiết kế kiến trúc', description: 'Thực hành tối ưu kiến trúc hệ thống' },
        { index: 3, title: 'Tối ưu hiệu năng', description: 'Phương pháp luận điều chỉnh hiệu năng' },
        { index: 4, title: 'An toàn bảo mật', description: 'Xây dựng hệ thống bảo mật mạng' },
        { index: 5, title: 'Triển vọng tương lai', description: 'Định hướng phát triển công nghệ' },
      ],
    });
  }

  protected async addContent(): Promise<void> {
    const textImage = new TextImageLayout(this.generator, this.theme);
    textImage.generate({
      pageTitle: 'Xu hướng công nghệ',
      blocks: [
        {
          title: 'Trí tuệ nhân tạo & Mô hình lớn',
          content: 'Mô hình ngôn ngữ lớn đang tái định hình phương thức phát triển phần mềm. Từ sinh mã tự động đến dò lỗi thông minh, các công cụ AI hỗ trợ lập trình đang thúc đẩy mạnh mẽ năng suất công việc. Dự báo đến năm 2025, hơn 80% công việc phát triển phần mềm sẽ ứng dụng công cụ hỗ trợ AI.',
        },
      ],
    });

    const threeCol = new ThreeColumn(this.generator, this.theme);
    threeCol.generate({
      pageTitle: 'Nguyên tắc thiết kế kiến trúc',
      blocks: [
        { index: 1, title: 'Kiến trúc Microservices', content: 'Áp dụng kiến trúc dịch vụ vi mô nhằm phân tách dịch vụ và triển khai độc lập. Kết hợp container hóa và Kubernetes để điều phối và mở rộng linh hoạt.' },
        { index: 2, title: 'Kiến trúc hướng sự kiện', content: 'Sử dụng kiến trúc hướng sự kiện để xử lý tác vụ bất đồng bộ, sử dụng hàng đợi thông điệp để giao tiếp lỏng lẻo giữa các dịch vụ.' },
        { index: 3, title: 'Công nghệ Cloud-Native', content: 'Đón nhận toàn diện hệ sinh thái Cloud-Native, bao gồm container, Service Mesh, Declarative API, v.v.' },
      ],
    });
  }

  protected async addTimeline(): Promise<void> {
    const timeline = new Vertical(this.generator, this.theme);
    timeline.generate({
      pageTitle: 'Lộ trình tiến hóa công nghệ',
      items: [
        { date: 'Phase 1', title: 'Kiến trúc Monolith', description: 'Xác thực nguyên mẫu nhanh chóng', highlight: false },
        { date: 'Phase 2', title: 'Tách dịch vụ', description: 'Độc lập các dịch vụ cốt lõi', highlight: false },
        { date: 'Phase 3', title: 'Microservices', description: 'Chuyển đổi toàn diện sang Microservices', highlight: true },
        { date: 'Phase 4', title: 'Cloud-Native', description: 'Container hóa và điều phối hệ thống', highlight: false },
        { date: 'Phase 5', title: 'Vận hành thông minh', description: 'Áp dụng thực tiễn AIOps', highlight: false },
      ],
    });
  }

  protected async addCharts(): Promise<void> {
    const lineChart = new LineChart(this.generator, this.theme);
    lineChart.generate({
      pageTitle: 'Chỉ số hiệu năng',
      chartTitle: 'Xu hướng thời gian phản hồi hệ thống (ms)',
      data: [
        { label: 'v1.0', value: 500 },
        { label: 'v1.5', value: 350 },
        { label: 'v2.0', value: 200 },
        { label: 'v2.5', value: 120 },
        { label: 'v3.0', value: 80 },
        { label: 'v3.5', value: 50 },
      ],
      description: 'Thông qua việc tối ưu hóa liên tục, thời gian phản hồi của hệ thống đã giảm đến 90%.',
    });
  }

  protected async addTeam(): Promise<void> {
    const team = new TeamGrid(this.generator, this.theme);
    team.generate({
      pageTitle: 'Đội ngũ kỹ thuật',
      members: [
        { name: 'KTS. Lâm', title: 'Tổng kiến trúc sư', description: 'Chuyên gia hệ thống phân tán' },
        { name: 'KS. Hoàng', title: 'Trưởng nhóm AI', description: 'Chuyên gia học máy' },
        { name: 'KS. Dương', title: 'Trưởng nhóm bảo mật', description: 'Chuyên gia an ninh mạng' },
        { name: 'KS. Mã', title: 'Trưởng nhóm vận hành', description: 'Chuyên gia DevOps' },
      ],
    });
  }

  protected async addEnding(): Promise<void> {
    const contact = new Contact(this.generator, this.theme);
    contact.generate({
      title: 'Giao lưu công nghệ',
      subtitle: 'Rất hân hạnh cùng trao đổi và thảo luận kỹ thuật',
      company: this.config.company || 'Đội ngũ kỹ thuật',
      email: 'tech@example.com',
      website: 'github.com/example',
    });
  }
}
