/**
 * Điểm vào chính của bộ tạo PPT
 * Xuất tất cả các mô-đun và chức năng
 */

// Mô-đun cơ sở
export { TemplateGenerator, Theme, SlideSize, TextBoxOptions, ShapeOptions, ImageOptions } from './base';

// Hàm tiện ích
export {
  hexToRgb,
  rgbToHex,
  blendColors,
  lightenColor,
  darkenColor,
  createCirclePositions,
  createGridPositions,
  createHexagonPositions,
  distributeHorizontal,
  distributeVertical,
  formatNumberedTitle,
  truncateText,
  generateId,
  estimateTextLines,
  safeDivide,
  clamp,
} from './utils';

// Bộ chủ đề màu sắc
export {
  blueTechnology,
  purpleGradient,
  darkGold,
  minimalistBW,
  oceanBlue,
  greenNature,
  redBusiness,
  allThemes,
  getThemeByName,
} from './themes';

// Bộ tạo trang bìa (Cover)
export {
  GeometricRotation,
  CircleRing,
  TrainMist,
  DiamondReveal,
  MinimalistGradient,
  SplitScreen,
  HollowMask,
  LayeredDepth,
  CoverData,
} from './generators/cover';

// Bộ tạo mục lục (Directory)
export {
  DiamondAnimated,
  CircularRing,
  Hexagon,
  Sidebar,
  CardGrid,
  TimelineStyle,
  DirectoryData,
  DirectoryItem,
} from './generators/directory';

// Bộ tạo trang nội dung (Content)
export {
  TextImageLayout,
  ThreeColumn,
  FourGrid,
  FullImageOverlay,
  Comparison,
  ContentData,
  ContentBlock,
} from './generators/content';

// Bộ tạo dòng thời gian (Timeline)
export {
  DualWave,
  Horizontal,
  Vertical,
  Spiral,
  TimelineData,
  TimelineItem,
} from './generators/timeline';

// Bộ tạo biểu đồ (Chart)
export {
  BarChart,
  PieChart,
  LineChart,
  AnimatedChart,
  ChartPageData,
  ChartDataItem,
} from './generators/chart';

// Bộ tạo đội ngũ (Team)
export {
  PersonCard,
  TeamGrid,
  OrgChart,
  TeamData,
  TeamMember,
} from './generators/team';

// Bộ tạo trang kết thúc (Ending)
export {
  ThankYou,
  QRCode,
  Contact,
  EndingData,
} from './generators/ending';

// Bộ bài thuyết trình hoàn chỉnh (Complete Decks)
export {
  BusinessPlan,
  CareerPlanning,
  ProductLaunch,
  AnnualReport,
  EducationCourse,
  TechnologyTheme,
  DeckConfig,
} from './generators/complete';
