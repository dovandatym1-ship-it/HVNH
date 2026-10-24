/**
 * Ví dụ bắt đầu nhanh
 * Hướng dẫn cách sử dụng bộ tạo PPT để tạo một bài thuyết trình đơn giản
 *
 * Cách chạy:
 *   npx ts-node examples/quick-start.ts
 */

import { TemplateGenerator, blueTechnology } from '../src';
import { GeometricRotation } from '../src/generators/cover';
import { Sidebar } from '../src/generators/directory';
import { ThreeColumn, Comparison } from '../src/generators/content';
import { Horizontal } from '../src/generators/timeline';
import { BarChart, PieChart } from '../src/generators/chart';
import { PersonCard } from '../src/generators/team';
import { ThankYou } from '../src/generators/ending';

/**
 * Hàm chính - Tạo bài thuyết trình mẫu
 */
async function main(): Promise<void> {
  console.log('Bắt đầu tạo bài thuyết trình...');

  // Khởi tạo bộ tạo slide, áp dụng chủ đề Công nghệ xanh dương
  const generator = new TemplateGenerator(blueTechnology);
  generator.setTitle('Bài thuyết trình mẫu');

  // 1. Trang bìa
  console.log('  - Đang tạo trang bìa...');
  const cover = new GeometricRotation(generator, blueTechnology);
  cover.generate({
    title: 'Giới thiệu sản phẩm & Phân tích thị trường',
    subtitle: 'Báo cáo thường niên 2024',
    presenter: 'Nguyễn Văn A',
    date: 'Tháng 6 năm 2024',
    company: 'Công ty Cổ phần Công nghệ Mẫu',
  });

  // 2. Trang mục lục
  console.log('  - Đang tạo trang mục lục...');
  const directory = new Sidebar(generator, blueTechnology);
  directory.generate({
    pageTitle: 'Mục lục',
    items: [
      { index: 1, title: 'Tổng quan dự án', description: 'Bối cảnh và mục tiêu dự án' },
      { index: 2, title: 'Phân tích thị trường', description: 'Xu hướng ngành và bối cảnh cạnh tranh' },
      { index: 3, title: 'Giải pháp sản phẩm', description: 'Tính năng cốt lõi và kiến trúc kỹ thuật' },
      { index: 4, title: 'Giới thiệu đội ngũ', description: 'Đội ngũ phát triển nòng cốt' },
      { index: 5, title: 'Dự báo tài chính', description: 'Kế hoạch doanh thu và chi phí' },
    ],
  });

  // 3. Trang nội dung - Bố cục 3 cột
  console.log('  - Đang tạo trang nội dung (3 cột)...');
  const threeCol = new ThreeColumn(generator, blueTechnology);
  threeCol.generate({
    pageTitle: 'Tổng quan dự án',
    blocks: [
      {
        index: 1,
        title: 'Bối cảnh dự án',
        content: 'Cùng với sự tăng tốc chuyển đổi số, nhu cầu của doanh nghiệp đối với các giải pháp thông minh ngày càng cấp thiết. Dự án này hướng tới nền tảng văn phòng thông minh toàn diện.',
      },
      {
        index: 2,
        title: 'Mục tiêu dự án',
        content: 'Xây dựng nền tảng văn phòng thông minh dẫn đầu thị trường, giúp doanh nghiệp nâng cao 30% hiệu suất làm việc và tiết kiệm 20% chi phí vận hành.',
      },
      {
        index: 3,
        title: 'Giá trị cốt lõi',
        content: 'Ứng dụng công nghệ AI và phân tích dữ liệu lớn nhằm cung cấp hỗ trợ ra quyết định thông minh, tự động hóa quy trình nghiệp vụ và tối ưu hóa vận hành dựa trên dữ liệu.',
      },
    ],
  });

  // 4. Trang nội dung - Bố cục so sánh
  console.log('  - Đang tạo trang so sánh đối thủ...');
  const comparison = new Comparison(generator, blueTechnology);
  comparison.generate({
    pageTitle: 'Phân tích lợi thế cạnh tranh',
    blocks: [
      {
        title: 'Giải pháp của chúng tôi',
        content: '- Mức độ thông minh hóa cao\n- Trải nghiệm người dùng vượt trội\n- Dịch vụ hỗ trợ 24/7\n- Tỷ suất hiệu quả chi phí cao\n- Khả năng tùy biến linh hoạt',
      },
      {
        title: 'Giải pháp truyền thống',
        content: '- Phụ thuộc thao tác thủ công\n- Hiệu suất xử lý còn thấp\n- Thời gian hỗ trợ bị giới hạn\n- Chi phí vận hành và bảo trì lớn\n- Khó mở rộng và chuẩn hóa',
      },
    ],
  });

  // 5. Trang dòng thời gian
  console.log('  - Đang tạo trang dòng thời gian...');
  const timeline = new Horizontal(generator, blueTechnology);
  timeline.generate({
    pageTitle: 'Các cột mốc dự án',
    items: [
      { date: '2024 Q1', title: 'Khảo sát nhu cầu', description: 'Hoàn tất phân tích nhu cầu người dùng' },
      { date: '2024 Q2', title: 'Thiết kế sản phẩm', description: 'Hoàn tất thiết kế UI/UX' },
      { date: '2024 Q3', title: 'Phát triển kiểm thử', description: 'Hoàn tất tính năng cốt lõi' },
      { date: '2024 Q4', title: 'Phát hành chính thức', description: 'Chính thức ra mắt sản phẩm' },
    ],
  });

  // 6. Trang biểu đồ - Biểu đồ cột
  console.log('  - Đang tạo biểu đồ cột...');
  const barChart = new BarChart(generator, blueTechnology);
  barChart.generate({
    pageTitle: 'Dự báo thị trường',
    chartTitle: 'Dự báo doanh thu hàng năm (tỷ đồng)',
    data: [
      { label: 'Năm 2024', value: 800 },
      { label: 'Năm 2025', value: 1500 },
      { label: 'Năm 2026', value: 2800 },
      { label: 'Năm 2027', value: 4500 },
    ],
    description: 'Dựa trên khảo sát thị trường và kỳ vọng tăng trưởng kinh doanh, dự kiến doanh thu 4 năm tới sẽ duy trì tốc độ phát triển mạnh mẽ.',
  });

  // 7. Trang biểu đồ - Biểu đồ tròn
  console.log('  - Đang tạo biểu đồ tròn...');
  const pieChart = new PieChart(generator, blueTechnology);
  pieChart.generate({
    pageTitle: 'Phân tích cơ cấu doanh thu',
    chartTitle: 'Tỷ trọng nguồn doanh thu',
    data: [
      { label: 'Thuê bao SaaS', value: 45 },
      { label: 'Tùy chỉnh doanh nghiệp', value: 25 },
      { label: 'Dịch vụ dữ liệu', value: 20 },
      { label: 'Tư vấn đào tạo', value: 10 },
    ],
  });

  // 8. Trang đội ngũ
  console.log('  - Đang tạo trang đội ngũ...');
  const team = new PersonCard(generator, blueTechnology);
  team.generate({
    pageTitle: 'Đội ngũ nòng cốt',
    members: [
      { name: 'Trần Minh', title: 'CEO', description: '10 năm kinh nghiệm Internet, từng giữ chức VP công ty niêm yết' },
      { name: 'Lê Hoa', title: 'CTO', description: 'Chuyên gia trí tuệ nhân tạo, sở hữu nhiều bằng sáng chế' },
      { name: 'Vương Phương', title: 'CPO', description: 'Chuyên gia sản phẩm kỳ cựu, thế mạnh thiết kế trải nghiệm người dùng' },
    ],
  });

  // 9. Trang kết thúc
  console.log('  - Đang tạo trang kết thúc...');
  const ending = new ThankYou(generator, blueTechnology);
  ending.generate({
    title: 'Xin chân thành cảm ơn',
    subtitle: 'Thank You',
    company: 'Công ty Cổ phần Công nghệ Mẫu',
  });

  // Lưu tệp
  console.log('Đang lưu tệp...');
  const filePath = await generator.save('Bài thuyết trình mẫu');
  console.log(`Bài thuyết trình đã được tạo: ${filePath}`);
  console.log('Hoàn thành!');
}

// Thực thi
main().catch(err => {
  console.error('Tạo bài thuyết trình thất bại:', err);
  process.exit(1);
});
