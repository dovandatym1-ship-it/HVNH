import os
import sys
import base64

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FIG_DIR = os.path.join(BASE_DIR, "figures")
HTML_PATH = os.path.join(BASE_DIR, "Slide_Thuyet_Trinh_BankChurners.html")
MARP_PATH = os.path.join(BASE_DIR, "Slide_Thuyet_Trinh_BankChurners.md")
SCRIPT_PATH = os.path.join(BASE_DIR, "Kich_Ban_Thuyet_Trinh_va_Cau_Hoi_Phan_Bien.md")

# Load and encode images to base64 for self-contained HTML
def get_img_base64(name):
    p = os.path.join(FIG_DIR, name)
    if os.path.exists(p):
        with open(p, "rb") as f:
            return "data:image/png;base64," + base64.b64encode(f.read()).decode('utf-8')
    return ""

img_map = {
    'churn_dist': get_img_base64('01_churn_distribution.png'),
    'demographic': get_img_base64('02_demographic_churn.png'),
    'trans_scatter': get_img_base64('03_transaction_behavior_churn.png'),
    'financial_box': get_img_base64('04_financial_ratios_churn.png'),
    'interaction': get_img_base64('05_interaction_decay_churn.png'),
    'relationship': get_img_base64('08_relationship_and_card.png'),
    'kmeans_pca': get_img_base64('10_kmeans_clusters_pca.png'),
    'roc_auc': get_img_base64('11_ml_model_comparison_roc.png'),
    'confusion': get_img_base64('12_ml_confusion_matrices.png'),
    'feat_imp': get_img_base64('13_feature_importance_xgb.png'),
    'cost_benefit': get_img_base64('14_cost_benefit_threshold_optimization.png')
}

# ==========================================
# 1. GENERATE INTERACTIVE HTML PRESENTATION
# ==========================================
html_content = f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Slide Thuyết Trình: Xử Lý & Khai Phá Dữ Liệu BankChurners - Đỗ Văn Đạt HVNH</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        :root {{
            --navy: #0A2540;
            --blue: #0070F3;
            --cyan: #0284C7;
            --coral: #EF4444;
            --green: #10B981;
            --bg: #F8FAFC;
            --card-bg: #FFFFFF;
            --text-dark: #0F172A;
            --text-muted: #64748B;
            --border: #E2E8F0;
            --shadow: 0 10px 25px -5px rgba(15, 23, 42, 0.08), 0 8px 10px -6px rgba(15, 23, 42, 0.04);
        }}
        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        }}
        body {{
            background-color: var(--navy);
            color: var(--text-dark);
            overflow: hidden;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            width: 100vw;
        }}
        .deck-container {{
            position: relative;
            width: 95vw;
            height: 53.43vw; /* 16:9 ratio */
            max-width: 1400px;
            max-height: 787.5px;
            background-color: var(--bg);
            border-radius: 16px;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
            overflow: hidden;
            display: flex;
            flex-direction: column;
        }}
        .slide {{
            display: none;
            flex: 1;
            padding: 40px 50px;
            overflow-y: auto;
            animation: fadeIn 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        }}
        .slide.active {{
            display: flex;
            flex-direction: column;
        }}
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(10px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        .slide-header {{
            margin-bottom: 20px;
        }}
        .slide-tag {{
            font-size: 12px;
            font-weight: 700;
            color: var(--blue);
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 6px;
        }}
        .slide-title {{
            font-size: 26px;
            font-weight: 800;
            color: var(--navy);
            line-height: 1.2;
        }}
        .slide-content {{
            flex: 1;
            display: grid;
            gap: 24px;
            align-items: center;
        }}
        .grid-2 {{
            grid-template-columns: 1.1fr 0.9fr;
        }}
        .grid-3 {{
            grid-template-columns: 1fr 1fr 1fr;
        }}
        .grid-4 {{
            grid-template-columns: 1fr 1fr 1fr 1fr;
        }}
        .card {{
            background-color: var(--card-bg);
            border-radius: 12px;
            padding: 24px;
            border: 1px solid var(--border);
            box-shadow: var(--shadow);
            height: 100%;
            display: flex;
            flex-direction: column;
        }}
        .card h3 {{
            font-size: 17px;
            font-weight: 700;
            color: var(--navy);
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        .card p, .card ul {{
            font-size: 13.5px;
            color: var(--text-dark);
            line-height: 1.6;
        }}
        .card ul {{
            padding-left: 18px;
        }}
        .card li {{
            margin-bottom: 8px;
        }}
        .img-container {{
            background: #fff;
            border-radius: 12px;
            border: 1px solid var(--border);
            padding: 12px;
            box-shadow: var(--shadow);
            text-align: center;
            height: 100%;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        .img-container img {{
            max-width: 100%;
            max-height: 400px;
            border-radius: 8px;
            object-fit: contain;
        }}
        .badge {{
            display: inline-block;
            padding: 4px 10px;
            border-radius: 6px;
            font-size: 12px;
            font-weight: 700;
            margin-bottom: 8px;
        }}
        .badge-red {{ background: #FEE2E2; color: var(--coral); }}
        .badge-blue {{ background: #DBEAFE; color: var(--blue); }}
        .badge-green {{ background: #D1FAE5; color: var(--green); }}

        /* Title Slide Custom */
        .slide-title-hero {{
            background: linear-gradient(135deg, #0A2540 0%, #0F172A 100%);
            color: #fff;
            justify-content: center;
            align-items: center;
            text-align: center;
            padding: 60px;
        }}
        .hero-uni {{
            color: #38BDF8;
            font-size: 16px;
            font-weight: 700;
            letter-spacing: 2px;
            margin-bottom: 20px;
        }}
        .hero-main {{
            font-size: 34px;
            font-weight: 800;
            line-height: 1.25;
            margin-bottom: 16px;
            color: #FFFFFF;
        }}
        .hero-sub {{
            font-size: 20px;
            font-weight: 600;
            color: #FCA5A5;
            margin-bottom: 30px;
            line-height: 1.4;
        }}
        .hero-meta {{
            display: inline-flex;
            gap: 20px;
            background: rgba(255, 255, 255, 0.08);
            backdrop-filter: blur(8px);
            padding: 12px 24px;
            border-radius: 30px;
            border: 1px solid rgba(255, 255, 255, 0.15);
            font-size: 13.5px;
            color: #E2E8F0;
        }}

        /* Navigation Controls */
        .controls {{
            height: 50px;
            background: #FFFFFF;
            border-top: 1px solid var(--border);
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0 30px;
            z-index: 10;
        }}
        .controls-info {{
            font-size: 13px;
            font-weight: 600;
            color: var(--text-muted);
        }}
        .nav-btns {{
            display: flex;
            gap: 10px;
        }}
        .btn {{
            background: var(--bg);
            border: 1px solid var(--border);
            padding: 6px 16px;
            border-radius: 6px;
            font-size: 13px;
            font-weight: 600;
            color: var(--text-dark);
            cursor: pointer;
            transition: all 0.2s;
        }}
        .btn:hover {{
            background: var(--blue);
            color: #fff;
            border-color: var(--blue);
        }}
    </style>
</head>
<body>

<div class="deck-container">
    <!-- SLIDE 1 -->
    <div class="slide slide-title-hero active" id="slide-1">
        <div class="hero-uni">🏛️ HỌC VIỆN NGÂN HÀNG (BANKING ACADEMY)</div>
        <div class="hero-main">XỬ LÝ DỮ LIỆU & KHAI PHÁ DỮ LIỆU</div>
        <div class="hero-sub">PHÂN TÍCH HÀNH VI, PHÂN CỤM & DỰ BÁO NGUY CƠ RỜI BỎ<br>CỦA KHÁCH HÀNG THẺ TÍN DỤNG (BANK CHURN ANALYSIS)</div>
        <div class="hero-meta">
            <span>👤 <b>Sinh viên:</b> Đỗ Văn Đạt</span>
            <span>📚 <b>Môn:</b> Business Analytics</span>
            <span>📊 <b>Dữ liệu:</b> BankChurners.csv (10,127 bản ghi)</span>
            <span>📅 Năm học: 2025 - 2026</span>
        </div>
    </div>

    <!-- SLIDE 2 -->
    <div class="slide" id="slide-2">
        <div class="slide-header">
            <div class="slide-tag">BỐI CẢNH NGHIÊN CỨU</div>
            <div class="slide-title">1. Bối Cảnh Kinh Doanh & Bài Toán Kinh Tế Giữ Chân Khách Hàng</div>
        </div>
        <div class="slide-content grid-3">
            <div class="card">
                <h3>💳 Nguồn Thu Lợi Nhuận Thẻ</h3>
                <ul>
                    <li><b>Phí quẹt thẻ (Interchange Fees):</b> Doanh thu từ POS & E-commerce.</li>
                    <li><b>Lãi suất tín dụng quay vòng (Revolving Interest):</b> Lợi nhuận sinh lời cao nhất.</li>
                    <li><b>Phí dịch vụ:</b> Thường niên, chậm thanh toán, chuyển đổi ngoại tệ.</li>
                </ul>
            </div>
            <div class="card">
                <h3>⚖️ Quy Tắc 5:1 (CAC vs CRC)</h3>
                <ul>
                    <li>Chi phí tìm khách mới (CAC) gấp <b>5-7 LẦN</b> chi phí giữ chân khách cũ (CRC).</li>
                    <li>Tăng 5% giữ chân giúp tăng <b>25% - 95%</b> lợi nhuận (Bain & Company).</li>
                    <li>Mất khách = Mất toàn bộ dòng tiền phí và lãi suất trong tương lai.</li>
                </ul>
            </div>
            <div class="card">
                <span class="badge badge-red">RỦI RO CAO</span>
                <h3>🚨 Thực Trạng Tỷ Lệ Rời Bỏ</h3>
                <ul>
                    <li>Tỷ lệ Churn trong tập dữ liệu: <b>16.07%</b> (1,627 / 10,127 khách hàng).</li>
                    <li>Cứ <b>6 khách hàng</b> mở thẻ thì có <b>1 khách hàng hủy thẻ</b>.</li>
                    <li>Cần mô hình máy học phát hiện sớm các "dấu hiệu ngầm" trước khi đóng thẻ.</li>
                </ul>
            </div>
        </div>
    </div>

    <!-- SLIDE 3 -->
    <div class="slide" id="slide-3">
        <div class="slide-header">
            <div class="slide-tag">PHƯƠNG PHÁP LUẬN</div>
            <div class="slide-title">2. Kiến Trúc Pipeline Xử Lý & Khai Phá Dữ Liệu Toàn Diện</div>
        </div>
        <div class="slide-content grid-4">
            <div class="card">
                <span class="badge badge-blue">BƯỚC 1</span>
                <h3>Tiền Xử Lý Dữ Liệu</h3>
                <ul>
                    <li>Loại 2 cột Naive Bayes thừa</li>
                    <li>Xử lý Missing bằng Median</li>
                    <li>Giữ nhóm 'Unknown' độc lập</li>
                    <li>Tạo 5 biến phái sinh mới</li>
                </ul>
            </div>
            <div class="card">
                <span class="badge badge-blue">BƯỚC 2</span>
                <h3>Khám Phá Dữ Liệu (EDA)</h3>
                <ul>
                    <li>Phân tích Nhân khẩu học</li>
                    <li>Nhận diện Vùng rủi ro GD</li>
                    <li>Hiện tượng Dư nợ về 0</li>
                    <li>Ngưỡng báo động 3 lần gọi</li>
                </ul>
            </div>
            <div class="card">
                <span class="badge badge-green">BƯỚC 3</span>
                <h3>Khai Phá Nâng Cao (ML)</h3>
                <ul>
                    <li>Phân cụm 4 nhóm K-Means & PCA</li>
                    <li>Huấn luyện LR, DT, RF, XGBoost</li>
                    <li>Đánh giá ROC-AUC > 0.99</li>
                    <li>Tối ưu ngưỡng kinh tế giữ chân</li>
                </ul>
            </div>
            <div class="card">
                <span class="badge badge-green">BƯỚC 4</span>
                <h3>Ứng Dụng Quản Trị</h3>
                <ul>
                    <li>Xây dựng 3 Chân dung rủi ro</li>
                    <li>Khung Chiến lược 4 Tầng</li>
                    <li>Hệ thống Cảnh báo Sớm EWS</li>
                    <li>Mô phỏng ROI tài chính 500%</li>
                </ul>
            </div>
        </div>
    </div>

    <!-- SLIDE 4 -->
    <div class="slide" id="slide-4">
        <div class="slide-header">
            <div class="slide-tag">TIỀN XỬ LÝ DỮ LIỆU</div>
            <div class="slide-title">3. Chiến Lược Làm Sạch & Kỹ Thuật Tạo Biến (Feature Engineering)</div>
        </div>
        <div class="slide-content grid-2">
            <div class="card">
                <h3>🧹 Tiền Xử Lý & Chuẩn Hóa</h3>
                <ul>
                    <li><b>Loại bỏ Data Leakage:</b> Xóa 2 cột Naive Bayes được thêm sẵn từ trước để đảm bảo tính khách quan của mô hình.</li>
                    <li><b>Missing Values:</b> Điền giá trị Median cho các thuộc tính số bị khuyết lẻ tẻ để đảm bảo tính vững chắc (robust).</li>
                    <li><b>Bảo toàn 'Unknown':</b> Giữ nguyên danh mục 'Unknown' trong Học vấn (15%), Thu nhập (11%), Hôn nhân (7.4%) như một phân lớp thông tin hành vi độc lập.</li>
                </ul>
            </div>
            <div class="card">
                <h3>⚙️ Kỹ Thuật Tạo Đặc Trưng Mới</h3>
                <ul>
                    <li><b>Avg_Trans_Value:</b> Giá trị chi tiêu trung bình / lần quẹt thẻ (<code>Total_Trans_Amt / Total_Trans_Ct</code>).</li>
                    <li><b>Revolving_Ratio:</b> Tỷ lệ dư nợ quay vòng trên hạn mức cấp (<code>Revolving_Bal / Credit_Limit</code>).</li>
                    <li><b>Contact_Intensity:</b> Cường độ bức xúc (<code>Contacts / (Inactive_Months + 1)</code>).</li>
                    <li><b>Age_Group:</b> Phân 5 nhóm tuổi: &lt;35, 35-44, 45-54, 55-64, 65+.</li>
                </ul>
            </div>
        </div>
    </div>

    <!-- SLIDE 5 -->
    <div class="slide" id="slide-5">
        <div class="slide-header">
            <div class="slide-tag">EDA - BIẾN MỤC TIÊU</div>
            <div class="slide-title">4. Phân Bố Biến Mục Tiêu: Thách Thức Mất Cân Bằng Lớp</div>
        </div>
        <div class="slide-content grid-2">
            <div class="img-container">
                <img src="{img_map['churn_dist']}" alt="Churn Distribution">
            </div>
            <div class="card">
                <h3>📊 Phân Tích Mất Cân Bằng Lớp</h3>
                <ul>
                    <li><b>Ở lại (Existing):</b> 8,500 khách hàng (83.93%).</li>
                    <li><b>Rời bỏ (Attrited):</b> 1,627 khách hàng (16.07%).</li>
                    <li><b>Tỷ lệ mất cân bằng:</b> Xấp xỉ 1 : 5.22.</li>
                </ul>
                <div style="margin-top: 15px; padding: 12px; background: #FEF2F2; border-left: 4px solid var(--coral); border-radius: 4px;">
                    <b style="color: var(--coral);">🚨 Chiến lược Đánh giá ML:</b><br>
                    Không thể dùng Accuracy đơn thuần (đoán toàn bộ ở lại vẫn đạt 84%). Bắt buộc phải ưu tiên <b>Recall (Độ nhạy)</b>, <b>F1-Score</b> và <b>ROC-AUC</b> để không bỏ sót khách hàng rời bỏ.
                </div>
            </div>
        </div>
    </div>

    <!-- SLIDE 6 -->
    <div class="slide" id="slide-6">
        <div class="slide-header">
            <div class="slide-tag">EDA - NHÂN KHẨU HỌC</div>
            <div class="slide-title">5. Phân Tích Nhân Khẩu Học & Tỷ Lệ Rời Bỏ</div>
        </div>
        <div class="slide-content grid-2">
            <div class="img-container">
                <img src="{img_map['demographic']}" alt="Demographic Analysis">
            </div>
            <div class="card">
                <h3>🔍 Phát Hiện Nhân Khẩu Học Trọng Tâm</h3>
                <ul>
                    <li><b>Giới tính:</b> Nữ có tỷ lệ rời bỏ cao hơn Nam đáng kể (<b>17.36%</b> vs <b>14.62%</b>, p = 0.0002).</li>
                    <li><b>Rủi ro Phân hóa 2 Đầu Thu nhập (Bimodal Risk):</b>
                        <ul>
                            <li>Thu nhập thấp (&lt; $40K): Churn <b>17.19%</b> (áp lực phí/hạn mức thấp).</li>
                            <li>Thu nhập cao (≥ $120K): Churn <b>17.33%</b> (đối thủ lôi kéo).</li>
                            <li>Thu nhập trung bình ($60K-$80K): Trung thành nhất (13.48%).</li>
                        </ul>
                    </li>
                    <li><b>Học vấn:</b> Trình độ Tiến sĩ (Doctorate) có tỷ lệ rời bỏ cao nhất (<b>21.06%</b>).</li>
                </ul>
            </div>
        </div>
    </div>

    <!-- SLIDE 7 -->
    <div class="slide" id="slide-7">
        <div class="slide-header">
            <div class="slide-tag">EDA - HÀNH VI GIAO DỊCH</div>
            <div class="slide-title">6. Hành Vi Giao Dịch: Nhận Diện 'Vùng Nguy Cơ Cao'</div>
        </div>
        <div class="slide-content grid-2">
            <div class="img-container">
                <img src="{img_map['trans_scatter']}" alt="Transaction Behavior">
            </div>
            <div class="card">
                <span class="badge badge-red">ĐIỂM BÁO ĐỘNG ĐỎ</span>
                <h3>🚨 Vùng Nguy Cơ Cao (High-Risk Zone)</h3>
                <ul>
                    <li><b>Tổng số lần GD (Total_Trans_Ct):</b> Khách ở lại 68.7 lần vs Khách churn 44.9 lần (-34.6%, p &lt; 0.0001).</li>
                    <li><b>Tổng giá trị GD (Total_Trans_Amt):</b> Khách ở lại $4,655 vs Khách churn $3,095 (-33.5%, p &lt; 0.0001).</li>
                    <li><b>Quy luật phân tách:</b> Khách hàng có <b>&lt; 55 lần quẹt thẻ/năm</b> và <b>chi tiêu &lt; $3,000</b> tập trung dày đặc các trường hợp hủy thẻ.</li>
                </ul>
            </div>
        </div>
    </div>

    <!-- SLIDE 8 -->
    <div class="slide" id="slide-8">
        <div class="slide-header">
            <div class="slide-tag">EDA - CHỈ SỐ TÀI CHÍNH</div>
            <div class="slide-title">7. Chỉ Số Tài Chính: Hiện Tượng 'Dư Nợ Quay Vòng Về 0'</div>
        </div>
        <div class="slide-content grid-2">
            <div class="img-container">
                <img src="{img_map['financial_box']}" alt="Financial Ratios">
            </div>
            <div class="card">
                <h3>📉 Hành Vi Dọn Đường Đóng Thẻ</h3>
                <ul>
                    <li><b>Dư nợ tín dụng quay vòng (Total_Revolving_Bal):</b>
                        <ul>
                            <li>Khách ở lại: Mean $1,257 (Median $1,364).</li>
                            <li>Khách rời bỏ: Mean $673 (<b>MEDIAN = $0.00!</b>).</li>
                        </ul>
                    </li>
                    <li><b>Tỷ lệ sử dụng hạn mức (Utilization Ratio):</b>
                        <ul>
                            <li>Khách ở lại: 29.64% (Median 21.1%).</li>
                            <li>Khách rời bỏ: 16.25% (<b>MEDIAN = 0.00%!</b>).</li>
                        </ul>
                    </li>
                    <li><b>Kết luận:</b> Trước khi đóng thẻ, khách hàng có hành vi tất toán toàn bộ dư nợ về 0 để tránh phát sinh lãi và ngừng hẳn việc quẹt thẻ.</li>
                </ul>
            </div>
        </div>
    </div>

    <!-- SLIDE 9 -->
    <div class="slide" id="slide-9">
        <div class="slide-header">
            <div class="slide-tag">EDA - TƯƠNG TÁC & RÀO CẢN</div>
            <div class="slide-title">8. Tương Tác CSKH & Rào Cản Chuyển Đổi Hệ Sinh Thái</div>
        </div>
        <div class="slide-content grid-2">
            <div class="img-container">
                <img src="{img_map['interaction']}" alt="Interaction Decay">
            </div>
            <div class="img-container">
                <img src="{img_map['relationship']}" alt="Relationship Count">
            </div>
        </div>
    </div>

    <!-- SLIDE 10 -->
    <div class="slide" id="slide-10">
        <div class="slide-header">
            <div class="slide-tag">KHAI PHÁ DỮ LIỆU - PHÂN CỤM</div>
            <div class="slide-title">9. Khai Phá Dữ Liệu: Phân Cụm Hành Vi (K-Means & PCA)</div>
        </div>
        <div class="slide-content grid-2">
            <div class="img-container">
                <img src="{img_map['kmeans_pca']}" alt="K-Means PCA">
            </div>
            <div class="card">
                <h3>👥 4 Phân Cụm Khách Hàng (k=4)</h3>
                <ul>
                    <li><b>Cụm 0 (37.6%): Tiêu dùng phổ thông ổn định</b><br>Chi tiêu $4.1K, Dư nợ $1.4K, Churn = <b>9.2%</b> (Thấp).</li>
                    <li><b>Cụm 1 (24.0%): Ngủ đông & Nguy cơ cao</b><br>Chi tiêu $1.8K, Dư nợ $210, Churn = <b style="color:var(--coral);">41.8%!</b> (Cực cao).</li>
                    <li><b>Cụm 2 (18.7%): VIP Chi tiêu lớn</b><br>Chi tiêu $9.5K, Hạn mức cao, Churn = <b>14.5%</b> (Trung bình).</li>
                    <li><b>Cụm 3 (19.7%): Vay tín dụng quay vòng</b><br>Dư nợ $2.2K sinh lãi, Churn = <b>7.6%</b> (Thấp nhất).</li>
                </ul>
            </div>
        </div>
    </div>

    <!-- SLIDE 11 -->
    <div class="slide" id="slide-11">
        <div class="slide-header">
            <div class="slide-tag">KHAI PHÁ DỮ LIỆU - MÔ HÌNH HÓA</div>
            <div class="slide-title">10. Mô Hình Hóa Máy Học Dự Báo Rời Bỏ (Supervised ML)</div>
        </div>
        <div class="slide-content grid-2">
            <div class="img-container">
                <img src="{img_map['roc_auc']}" alt="ROC-AUC Curve">
            </div>
            <div class="card">
                <span class="badge badge-green">TOP 1 HIỆU NĂNG</span>
                <h3>🏆 So Sánh Hiệu Năng 4 Thuật Toán</h3>
                <ul>
                    <li><b>Logistic Regression:</b> ROC-AUC 0.9348, Recall 83.38%, F1 67.25%</li>
                    <li><b>Decision Tree:</b> ROC-AUC 0.9458, Recall 88.92%, F1 76.15%</li>
                    <li><b>Random Forest:</b> ROC-AUC 0.9838, Recall 87.08%, F1 84.23%</li>
                    <li><b style="color:var(--blue);">XGBOOST CLASSIFIER (VƯỢT TRỘI):</b>
                        <ul>
                            <li><b>ROC-AUC:</b> <span style="color:var(--green); font-weight:800;">0.9930</span> (Gần tuyệt đối)</li>
                            <li><b>Recall:</b> <span style="color:var(--green); font-weight:800;">91.38%</span> (Bắt trúng &gt;9/10 khách rời bỏ)</li>
                            <li><b>Precision:</b> 87.61% | <b>Accuracy:</b> 96.54%</li>
                        </ul>
                    </li>
                </ul>
            </div>
        </div>
    </div>

    <!-- SLIDE 12 -->
    <div class="slide" id="slide-12">
        <div class="slide-header">
            <div class="slide-tag">ĐÁNH GIÁ MÔ HÌNH</div>
            <div class="slide-title">11. Đánh Giá Chi Tiết Ma Trận Nhầm Lẫn (Confusion Matrix)</div>
        </div>
        <div class="slide-content grid-2">
            <div class="img-container">
                <img src="{img_map['confusion']}" alt="Confusion Matrix">
            </div>
            <div class="card">
                <h3>🎯 Kiểm Soát Sai Số Loại I & II</h3>
                <ul>
                    <li><b>Sai số Loại II (False Negative - Bỏ sót khách Churn):</b><br>XGBoost chỉ bỏ sót 28/325 khách hàng rời bỏ trên tập Test (tỷ lệ lỗi &lt; 8.6%).</li>
                    <li><b>Sai số Loại I (False Positive - Cảnh báo giả):</b><br>Chỉ có 42/1,701 khách hàng ở lại bị dự đoán nhầm (tỷ lệ báo động giả &lt; 2.5%).</li>
                    <li><b>Giá trị thực tế:</b> Đảm bảo ngân hàng can thiệp đúng khách hàng nguy cơ mà không lãng phí chi phí marketing.</li>
                </ul>
            </div>
        </div>
    </div>

    <!-- SLIDE 13 -->
    <div class="slide" id="slide-13">
        <div class="slide-header">
            <div class="slide-tag">GIẢI THÍCH MÔ HÌNH</div>
            <div class="slide-title">12. Top Nhân Tố Quyết Định Rời Bỏ (Feature Importance)</div>
        </div>
        <div class="slide-content grid-2">
            <div class="img-container">
                <img src="{img_map['feat_imp']}" alt="Feature Importance">
            </div>
            <div class="card">
                <h3>🔑 5 Đòn Bẩy Hành Vi Quyết Định</h3>
                <ul>
                    <li><b>1. Total_Trans_Ct (Số lần giao dịch):</b> Đóng góp quan trọng nhất. Tần suất quẹt thẻ là nhịp tim gắn kết.</li>
                    <li><b>2. Total_Ct_Chng_Q4_Q1:</b> Mức độ sụt giảm số giao dịch theo thời gian.</li>
                    <li><b>3. Total_Revolving_Bal:</b> Tín hiệu trả hết nợ về 0.</li>
                    <li><b>4. Total_Trans_Amt:</b> Quy mô ngân sách chi tiêu qua thẻ.</li>
                    <li><b>5. Relationship_Count & Contacts_Count:</b> Ràng buộc sản phẩm và mức độ bức xúc dịch vụ.</li>
                </ul>
            </div>
        </div>
    </div>

    <!-- SLIDE 14 -->
    <div class="slide" id="slide-14">
        <div class="slide-header">
            <div class="slide-tag">TỐI ƯU HÓA KINH TẾ</div>
            <div class="slide-title">13. Tối Ưu Hóa Ngưỡng Quyết Định & Bài Toán Chi Phí - Lợi Ích</div>
        </div>
        <div class="slide-content grid-2">
            <div class="img-container">
                <img src="{img_map['cost_benefit']}" alt="Cost Benefit Optimization">
            </div>
            <div class="card">
                <h3>💰 Tối Đa Hóa Lợi Nhuận Ròng</h3>
                <ul>
                    <li><b>Giả định bài toán kinh tế:</b>
                        <ul>
                            <li>Giá trị CLV giữ chân: $500 / khách hàng.</li>
                            <li>Chi phí can thiệp / ưu đãi: $50 / khách hàng.</li>
                            <li>Mất khách không can thiệp: -$500 / khách hàng.</li>
                        </ul>
                    </li>
                    <li><b>KẾT QUẢ TỐI ƯU:</b>
                        <ul>
                            <li>Ngưỡng cắt xác suất tối ưu: <b>t = 0.42</b> (thay vì 0.50).</li>
                            <li>Đạt điểm cân bằng tối ưu giữa Recall (94%) và Precision (86%).</li>
                            <li>Lợi nhuận ròng tối đa trên tập Test: <b>&gt; $112,000 USD</b>.</li>
                        </ul>
                    </li>
                </ul>
            </div>
        </div>
    </div>

    <!-- SLIDE 15 -->
    <div class="slide" id="slide-15">
        <div class="slide-header">
            <div class="slide-tag">CHÂN DUNG KHÁCH HÀNG</div>
            <div class="slide-title">14. Ba Chân Dung Khách Hàng Rời Bỏ Điển Hình (Personas)</div>
        </div>
        <div class="slide-content grid-3">
            <div class="card">
                <span class="badge badge-blue">55% TỔNG CHURN</span>
                <h3>1. The Silent Defector<br><small>(Ngủ đông & Rút lui)</small></h3>
                <ul>
                    <li>Dư nợ quay vòng = $0.</li>
                    <li>Quẹt thẻ &lt; 45 lần/năm.</li>
                    <li>Ngủ đông liên tiếp ≥ 3 tháng.</li>
                    <li>Chi tiêu Q4 giảm &gt; 50%.</li>
                    <li><b style="color:var(--blue);">Hành động:</b> Tặng Voucher quẹt thẻ cuối tuần, hoàn tiền 5% cho 3 GD đầu.</li>
                </ul>
            </div>
            <div class="card">
                <span class="badge badge-red">25% TỔNG CHURN</span>
                <h3>2. Frustrated Complainer<br><small>(Bức xúc & Khiếu nại)</small></h3>
                <ul>
                    <li>Gọi CSKH ≥ 3 - 6 lần.</li>
                    <li>Chỉ dùng 1 - 2 sản phẩm.</li>
                    <li>Bất mãn về lỗi POS / phí phạt.</li>
                    <li>Churn rate lên tới 35% - 100%.</li>
                    <li><b style="color:var(--coral);">Hành động:</b> VIP Taskforce gọi hỗ trợ 24h, miễn giảm phí thường niên linh hoạt.</li>
                </ul>
            </div>
            <div class="card">
                <span class="badge badge-green">20% TỔNG CHURN</span>
                <h3>3. The VIP Switcher<br><small>(Khách VIP Chuyển dịch)</small></h3>
                <ul>
                    <li>Thu nhập ≥ $120K, Thẻ Gold/Plat.</li>
                    <li>Hạn mức tín dụng &gt; $15K.</li>
                    <li>Chi tiêu Q4 sụt giảm đột ngột.</li>
                    <li>Bị đối thủ hút bằng ưu đãi VIP.</li>
                    <li><b style="color:var(--green);">Hành động:</b> Cán bộ RM tặng lượt phòng chờ sân bay, x2 điểm dặm bay.</li>
                </ul>
            </div>
        </div>
    </div>

    <!-- SLIDE 16 -->
    <div class="slide" id="slide-16">
        <div class="slide-header">
            <div class="slide-tag">CHIẾN LƯỢC QUẢN TRỊ</div>
            <div class="slide-title">15. Khung Chiến Lược Giữ Chân Khách Hàng 4 Tầng (4-Tier)</div>
        </div>
        <div class="slide-content grid-2">
            <div class="card">
                <h3>Tầng 1: Cảnh Báo Sớm (EWS)</h3>
                <p>Giám sát tự động thời gian thực các Trigger Point (Ngủ đông 2 tháng, gọi CSKH lần 3) để kích hoạt Push Notification và E-voucher kịp thời.</p>
                <div style="margin-top:10px; font-weight:700; color:var(--blue);">KPI: Tỷ lệ phát hiện sớm &gt; 90%</div>
            </div>
            <div class="card">
                <h3>Tầng 2: CSKH Chủ Động (Proactive)</h3>
                <p>Áp dụng chỉ tiêu First-Contact Resolution (FCR) xử lý dứt điểm khiếu nại trong 24h; chính sách Miễn giảm phí (Fee Waiver) linh hoạt.</p>
                <div style="margin-top:10px; font-weight:700; color:var(--blue);">KPI: FCR &gt; 85%, Hủy thẻ do CSKH &lt; 5%</div>
            </div>
            <div class="card">
                <h3>Tầng 3: Gamified Loyalty</h3>
                <p>Chiến dịch "Quẹt Thẻ Mỗi Tuần" tích điểm theo tần suất giao dịch thay vì chỉ tính theo số tiền; tự chọn danh mục hoàn tiền ưa thích.</p>
                <div style="margin-top:10px; font-weight:700; color:var(--green);">KPI: Tần suất giao dịch ≥ 5 lần/tháng</div>
            </div>
            <div class="card">
                <h3>Tầng 4: Bán Chéo (Cross-selling)</h3>
                <p>Combo "Tài chính Toàn diện" liên kết thẻ tín dụng với tài khoản lương, tiết kiệm và thanh toán hóa đơn tự động (Auto-billing).</p>
                <div style="margin-top:10px; font-weight:700; color:var(--green);">KPI: Khách hàng sở hữu ≥ 4 SP đạt &gt; 65%</div>
            </div>
        </div>
    </div>

    <!-- SLIDE 17 -->
    <div class="slide" id="slide-17">
        <div class="slide-header">
            <div class="slide-tag">HIỆU QUẢ TÀI CHÍNH</div>
            <div class="slide-title">16. Bài Toán Kinh Tế & Mô Phỏng Hiệu Quả Đầu Tư (ROI)</div>
        </div>
        <div class="slide-content grid-2">
            <div class="card">
                <h3>📊 Giả Định Quy Mô 10,000 Khách Hàng</h3>
                <ul>
                    <li>Tổng khách hàng thẻ: 10,000 người.</li>
                    <li>Tỷ lệ Churn hàng năm: 16% (1,600 khách rời bỏ).</li>
                    <li>Giá trị CLV trung bình: $500 / khách hàng.</li>
                    <li><b>Tổn thất nếu KHÔNG can thiệp:</b><br><span style="color:var(--coral); font-size:18px; font-weight:800;">$800,000 USD / năm</span></li>
                    <li><b>Mục tiêu giữ chân với XGBoost:</b><br>Cứu vãn thành công 60% = <b>960 khách hàng</b>.</li>
                </ul>
            </div>
            <div class="card">
                <h3>💵 Tính Toán Lợi Nhuận & ROI</h3>
                <ul>
                    <li><b>Giá trị CLV cứu vãn được:</b> 960 × $500 = $480,000 USD.</li>
                    <li><b>Chi phí can thiệp:</b> 1,600 × $50 = $80,000 USD.</li>
                    <li><b>LỢI NHUẬN RÒNG GIA TĂNG:</b><br><span style="color:var(--green); font-size:20px; font-weight:800;">+$400,000 USD / NĂM!</span></li>
                    <li><b>TỶ SUẤT HOÀN VỐN ĐẦU TƯ:</b><br><span style="color:var(--blue); font-size:22px; font-weight:800;">ROI = 500%</span></li>
                </ul>
            </div>
        </div>
    </div>

    <!-- SLIDE 18 -->
    <div class="slide" id="slide-18">
        <div class="slide-header">
            <div class="slide-tag">TỔNG KẾT</div>
            <div class="slide-title">17. Kết Luận & Hướng Phát Triển Đề Tài</div>
        </div>
        <div class="slide-content grid-2">
            <div class="card">
                <h3>🎯 Đóng Góp Chính của Đề Tài</h3>
                <ul>
                    <li>Tiền xử lý & làm sạch 10,127 bản ghi, tạo 5 đặc trưng phái sinh có ý nghĩa nghiệp vụ cao.</li>
                    <li>Khám phá các quy luật hành vi: Vùng nguy cơ GD &lt; 55 lần, dư nợ về 0, ngưỡng gọi CSKH 3 lần, rào cản chuyển đổi ≥ 4 sản phẩm.</li>
                    <li>XGBoost đạt ROC-AUC <b>0.9930</b>, Recall <b>91.38%</b>, tối ưu ngưỡng t = 0.42.</li>
                    <li>Khung chiến lược 4 tầng & EWS với ROI dự phóng <b>500%</b>.</li>
                </ul>
            </div>
            <div class="card">
                <h3>🚀 Hướng Phát Triển Cuối Kỳ</h3>
                <ul>
                    <li><b>Explainable AI (SHAP / LIME):</b> Giải thích nguyên nhân rủi ro cho từng cá nhân khách hàng trên CRM.</li>
                    <li><b>Dynamic CLV Modeling:</b> Mô hình hóa giá trị vòng đời động để cá nhân hóa ngân sách chi thưởng VIP.</li>
                    <li><b>Real-time API Scoring:</b> Chấm điểm rủi ro trực tiếp theo thời gian thực khi quẹt thẻ hoặc gọi điện.</li>
                </ul>
            </div>
        </div>
    </div>

    <!-- SLIDE 19 -->
    <div class="slide slide-title-hero" id="slide-19">
        <div class="hero-uni">HỌC VIỆN NGÂN HÀNG (BANKING ACADEMY)</div>
        <div class="hero-main" style="font-size:42px;">XIN TRÂN TRỌNG CẢM ƠN!</div>
        <div class="hero-sub" style="color:#E2E8F0; font-size:18px;">Kính chúc Thầy/Cô và các bạn nhiều sức khỏe & thành công!</div>
        <div style="font-size:24px; font-weight:800; color:#38BDF8; margin-top:20px;">HỎI & ĐÁP (Q&A)</div>
    </div>

    <!-- Controls Bar -->
    <div class="controls">
        <div class="controls-info" id="slide-indicator">Slide 1 / 19</div>
        <div class="nav-btns">
            <button class="btn" id="prev-btn" onclick="prevSlide()">◀ Trước</button>
            <button class="btn" id="next-btn" onclick="nextSlide()">Sau ▶</button>
        </div>
    </div>
</div>

<script>
    let currentSlide = 1;
    const totalSlides = 19;

    function showSlide(n) {{
        document.querySelectorAll('.slide').forEach(s => s.classList.remove('active'));
        const target = document.getElementById('slide-' + n);
        if (target) {{
            target.classList.add('active');
            document.getElementById('slide-indicator').innerText = `Slide ${{n}} / ${{totalSlides}}`;
        }}
    }}

    function nextSlide() {{
        if (currentSlide < totalSlides) {{
            currentSlide++;
            showSlide(currentSlide);
        }}
    }}

    function prevSlide() {{
        if (currentSlide > 1) {{
            currentSlide--;
            showSlide(currentSlide);
        }}
    }}

    document.addEventListener('keydown', (e) => {{
        if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') {{
            nextSlide();
        }} else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {{
            prevSlide();
        }}
    }});
</script>

</body>
</html>
"""

with open(HTML_PATH, "w", encoding="utf-8") as f:
    f.write(html_content)
print(f"🎉 Đã tạo Web Slide HTML tại: {HTML_PATH}")

# ==========================================
# 2. GENERATE MARP MARKDOWN SLIDES
# ==========================================
marp_content = """---
marp: true
theme: gaia
_class: lead
paginate: true
backgroundColor: #f8fafc
color: #0f172a
---

# 📊 BÀI TẬP GIỮA KỲ: XỬ LÝ & KHAI PHÁ DỮ LIỆU
## PHÂN TÍCH HÀNH VI, PHÂN CỤM & DỰ BÁO NGUY CƠ RỜI BỎ CỦA KHÁCH HÀNG THẺ TÍN DỤNG

**Học phần:** Phân tích Dữ liệu trong Kinh doanh (Business Analytics)  
**Đơn vị:** Học viện Ngân hàng (Banking Academy)  
**Sinh viên thực hiện:** Đỗ Văn Đạt  
**Tập dữ liệu:** `BankChurners.csv` (10,127 quan sát, 23 thuộc tính)  

---

## 🎯 1. BỐI CẢNH & BÀI TOÁN KINH TẾ

### Bối cảnh Ngân hàng Bán lẻ:
* **Thẻ tín dụng (Credit Card)** là nguồn thu lợi nhuận hàng đầu: Phí quẹt thẻ (Interchange), Lãi suất tín dụng quay vòng, Phí dịch vụ thường niên.
* **Quy tắc 5:1:** Chi phí tìm khách hàng mới (CAC) gấp **5-7 lần** chi phí giữ chân khách hàng cũ (CRC).
* **Tỷ lệ rời bỏ (Churn Rate)** trong dữ liệu là **16.07%** (Cứ 6 khách hàng mở thẻ thì có 1 khách hàng hủy thẻ).

---

## 🏗️ 2. KIẾN TRÚC PIPELINE XỬ LÝ & KHAI PHÁ DỮ LIỆU

1. **Giai đoạn 1 - Tiền xử lý dữ liệu:** Loại 2 cột Naive Bayes thừa, xử lý missing bằng median, bảo toàn nhóm Unknown, feature engineering 5 biến mới.
2. **Giai đoạn 2 - Khám phá dữ liệu (EDA):** Phân tích nhân khẩu học, nhận diện vùng rủi ro giao dịch (<55 lần, <$3000), hiện tượng dư nợ về 0, ngưỡng gọi CSKH 3 lần.
3. **Giai đoạn 3 - Khai phá dữ liệu (ML):** Phân cụm 4 nhóm K-Means & PCA, huấn luyện 4 mô hình ML (LR, DT, RF, XGBoost đạt ROC-AUC 0.9930), tối ưu ngưỡng kinh tế t = 0.42.
4. **Giai đoạn 4 - Ứng dụng quản trị:** 3 Chân dung rủi ro, Khung giữ chân 4 tầng (4-Tier), Hệ thống cảnh báo sớm EWS, ROI tài chính 500%.

---

## 🧹 3. TIỀN XỬ LÝ DỮ LIỆU & FEATURE ENGINEERING

* **Làm sạch dữ liệu:**
  - Xóa 2 cột Naive Bayes để loại bỏ rò rỉ dữ liệu (*Data Leakage*).
  - Điền Median cho các thuộc tính số bị khuyết lẻ tẻ.
  - Giữ nguyên nhóm 'Unknown' như một phân lớp thông tin độc lập.
* **Kỹ thuật tạo biến mới (Feature Engineering):**
  - `Avg_Trans_Value`: Giá trị chi tiêu trung bình / lần quẹt thẻ ($Total\_Trans\_Amt / Total\_Trans\_Ct$).
  - `Revolving_Ratio`: Tỷ lệ dư nợ quay vòng trên hạn mức cấp.
  - `Contact_Intensity`: Cường độ bức xúc ($Contacts / (Inactive\_Months + 1)$).
  - `Age_Group`: Phân khúc lứa tuổi (<35, 35-44, 45-54, 55-64, 65+).

---

## 📊 4. PHÂN BỐ BIẾN MỤC TIÊU (ATTRITION FLAG)

* **Ở lại (Existing Customer):** $8,500$ khách hàng ($83.93\%$).
* **Rời bỏ (Attrited Customer):** $1,627$ khách hàng ($16.07\%$).
* **Mất cân bằng lớp:** Xấp xỉ $1 : 5.22$.

> 🚨 **Chiến lược Đánh giá ML:** Không dùng Accuracy đơn thuần mà bắt buộc phải tối ưu hóa **Recall (Độ nhạy)**, **F1-Score** và **ROC-AUC** để không bỏ sót khách hàng rời bỏ.

---

## 👥 5. PHÂN TÍCH NHÂN KHẨU HỌC & RỦI RO RỜI BỎ

* **Giới tính (Gender):** Nữ có tỷ lệ rời bỏ cao hơn Nam đáng kể (**$17.36\%$** vs **$14.62\%$**, $p = 0.0002$).
* **Phân hóa Thu nhập 2 đầu (Bimodal Risk):**
  - Thu nhập thấp ($<\$40K$): Rời bỏ **$17.19\%$** (áp lực phí).
  - Thu nhập cao ($\ge \$120K$): Rời bỏ **$17.33\%$** (đối thủ lôi kéo).
  - Thu nhập trung bình ($\$60K-\$80K$): Trung thành nhất (**$13.48\%$**).
* **Học vấn:** Trình độ Tiến sĩ (Doctorate) có tỷ lệ rời bỏ cao nhất (**$21.06\%$**).

---

## 💳 6. HÀNH VI GIAO DỊCH: "VÙNG NGUY CƠ CAO"

* **Tổng số lần giao dịch (`Total_Trans_Ct`):** Khách ở lại $68.7$ lần vs Khách churn $44.9$ lần ($-34.6\%$, $p < 0.0001$).
* **Tổng giá trị giao dịch (`Total_Trans_Amt`):** Khách ở lại $\$4,655$ vs Khách churn $\$3,095$ ($-33.5\%$, $p < 0.0001$).

> 🚨 **VÙNG NGUY CƠ CAO (RED CLUSTER):** Khách hàng có **$< 55$ lần quẹt thẻ/năm** và **tổng chi tiêu $< \$3,000$** tập trung dày đặc các điểm rời bỏ. Tần suất quẹt thẻ là nhịp tim của lòng trung thành.

---

## 📉 7. CHỈ SỐ TÀI CHÍNH: HIỆN TƯỢNG "DƯ NỢ VỀ 0"

* **Dư nợ quay vòng (`Total_Revolving_Bal`):**
  - Khách ở lại: Mean $\$1,257$ (Median $\$1,364$).
  - Khách rời bỏ: Mean $\$673$ (**MEDIAN = $\$0.00$!**).
* **Tỷ lệ sử dụng hạn mức (`Avg_Utilization_Ratio`):**
  - Khách ở lại: $29.64\%$ (Median $21.1\%$).
  - Khách rời bỏ: $16.25\%$ (**MEDIAN = $0.00\%$!**).

> 📌 **Quy luật:** Trước khi đóng thẻ, khách hàng tất toán toàn bộ dư nợ về 0 để tránh phát sinh lãi phạt và hoàn toàn ngừng quẹt thẻ.

---

## 📞 8. TƯƠNG TÁC CSKH & RÀO CẢN ĐA SẢN PHẨM

* **Ngưỡng Báo Động 3 Lần Liên Hệ CSKH:**
  - Gọi $0-1$ lần: Churn $< 8\%$.
  - Gọi $3$ lần: Churn vọt lên **$20.21\%$**.
  - Gọi $4$ lần: Churn đạt **$34.11\%$**.
  - Gọi $5-6$ lần: Churn lên tới **$55\% - 100\%$**.
* **Số lượng sản phẩm sở hữu (`Relationship_Count`):**
  - Khách dùng $1-2$ sản phẩm: Churn **$26\% - 28\%$**.
  - Khách dùng $\ge 4$ sản phẩm: Churn giảm chỉ còn **$10\% - 11\%$** (giảm gần 3 lần).

---

## 🔍 9. KHAI PHÁ DỮ LIỆU: PHÂN CỤM K-MEANS & PCA

* **Cụm 0 (37.6%): Tiêu dùng phổ thông ổn định** (Chi tiêu $\$4.1K$, Dư nợ $\$1.4K$, Churn = $9.2\%$).
* **Cụm 1 (24.0%): Ngủ đông & Nguy cơ cao** (Chi tiêu $\$1.8K$, Dư nợ $\$210$, Churn = **$41.8\%$**).
* **Cụm 2 (18.7%): VIP Chi tiêu lớn** (Chi tiêu $\$9.5K$, Hạn mức cao, Churn = $14.5\%$).
* **Cụm 3 (19.7%): Vay tín dụng quay vòng** (Dư nợ $\$2.2K$ sinh lãi, Churn = $7.6\%$).

---

## 🤖 10. MÔ HÌNH HÓA MÁY HỌC (SUPERVISED ML)

| Thuật Toán | Accuracy | Precision | Recall (Độ Nhạy) | F1-Score | ROC-AUC |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Logistic Regression** | $86.97\%$ | $56.34\%$ | $83.38\%$ | $67.25\%$ | $0.9348$ |
| **Decision Tree** | $91.07\%$ | $66.59\%$ | $88.92\%$ | $76.15\%$ | $0.9458$ |
| **Random Forest** | $94.77\%$ | $81.56\%$ | $87.08\%$ | $84.23\%$ | $0.9838$ |
| **XGBoost (TOP 1)** | **$96.54\%$** | **$87.61\%$** | **$91.38\%$** | **$89.46\%$** | **$0.9930$** |

---

## 🔑 11. TOP ĐẶC TRƯNG QUYẾT ĐỊNH RỜI BỎ

1. `Total_Trans_Ct` (Số lần giao dịch): Đóng góp quan trọng nhất.
2. `Total_Ct_Chng_Q4_Q1` (Mức độ suy giảm giao dịch quý cuối).
3. `Total_Revolving_Bal` (Dư nợ tín dụng quay vòng về 0).
4. `Total_Trans_Amt` (Tổng giá trị chi tiêu).
5. `Total_Relationship_Count` & `Contacts_Count` (Ràng buộc sản phẩm & Bức xúc CSKH).

---

## 💰 12. TỐI ƯU HÓA NGƯỠNG KINH TẾ (COST-BENEFIT)

* **Giả định:** CLV giữ chân $=\$500$, Chi phí can thiệp $=\$50$, Mất khách $=-\$500$.
* **Ngưỡng cắt xác suất tối ưu:** **$t = 0.42$** (thay vì $0.50$ mặc định).
* **Kết quả:** Recall đạt $94\%$, Precision đạt $86\%$, Lợi nhuận ròng tối đa trên tập Test đạt **$> \$112,000$ USD**.

---

## 👥 13. BA CHÂN DUNG KHÁCH HÀNG RỜI BỎ (PERSONAS)

1. **The Silent Defector (55%):** Dư nợ $= \$0$, giao dịch $< 45$ lần, ngủ đông $\ge 3$ tháng $\rightarrow$ Gửi Voucher kích hoạt cuối tuần, hoàn tiền $5\%$.
2. **Frustrated Complainer (25%):** Gọi CSKH $\ge 3-6$ lần, dùng $1-2$ sản phẩm $\rightarrow$ VIP Taskforce hỗ trợ trong 24h, miễn giảm phí linh hoạt.
3. **The VIP Switcher (20%):** Thu nhập $\ge \$120K$, thẻ Gold/Plat $\rightarrow$ Cán bộ RM tặng phòng chờ sân bay, x2 điểm dặm bay.

---

## 🏛️ 14. KHUNG CHIẾN LƯỢC GIỮ CHÂN 4 TẦNG (4-TIER)

* **Tầng 1: Cảnh Báo Sớm (EWS):** Giám sát thời gian thực các Trigger Point (Ngủ đông 2 tháng, gọi CSKH lần 3).
* **Tầng 2: CSKH Chủ Động (Proactive):** Áp dụng KPI First-Contact Resolution (FCR) xử lý dứt điểm khiếu nại trong 24h.
* **Tầng 3: Gamified Loyalty:** Tích điểm theo tần suất quẹt thẻ thay vì chỉ tính theo số tiền chi tiêu.
* **Tầng 4: Bán Chéo (Cross-selling):** Combo Tài chính Toàn diện ($\ge 4$ sản phẩm) nâng cao rào cản chuyển đổi.

---

## 💵 15. BÀI TOÁN KINH TẾ & ROI 500%

* **Quy mô:** $10,000$ khách hàng (16% Churn = $1,600$ khách).
* **Cứu vãn 60% với XGBoost:** Giữ lại thành công **$960$ khách hàng**.
* **Giá trị CLV cứu được:** $960 \times \$500 = \$480,000$ USD.
* **Chi phí can thiệp:** $1,600 \times \$50 = \$80,000$ USD.
* **LỢI NHUẬN RÒNG GIA TĂNG:** **$+\$400,000$ USD / NĂM!**
* **TỶ SUẤT HOÀN VỐN:** **$\text{ROI} = 500\%$**.

---

## 🎯 16. KẾT LUẬN & HƯỚNG PHÁT TRIỂN

* **Đóng góp chính:** Làm sạch 10,127 bản ghi, phát hiện 4 quy luật hành vi then chốt, phân cụm 4 nhóm K-Means, XGBoost ROC-AUC 0.9930, chiến lược 4 tầng ROI 500%.
* **Hướng mở rộng cuối kỳ:** Ứng dụng Explainable AI (SHAP), Mô hình CLV Động (Dynamic CLV) và Tích hợp API Real-time Scoring trên CRM ngân hàng.

---

# XIN TRÂN TRỌNG CẢM ƠN!
### HỎI & ĐÁP (Q&A)
"""

with open(MARP_PATH, "w", encoding="utf-8") as f:
    f.write(marp_content)
print(f"🎉 Đã tạo Marp Markdown Slide tại: {MARP_PATH}")

# ==========================================
# 3. GENERATE SPEAKER NOTES & Q&A DEFENSE SCRIPT
# ==========================================
script_content = """# 🎙️ KỊCH BẢN THUYẾT TRÌNH CHI TIẾT (SPEAKER NOTES)
## VÀ BỘ 10 CÂU HỎI PHẢN BIỆN KINH ĐIỂN CỦA GIẢNG VIÊN (Q&A DEFENSE GUIDE)

* **Học phần:** Phân tích Dữ liệu trong Kinh doanh (Business Analytics) — Học viện Ngân hàng
* **Đề tài:** Xử lý dữ liệu và Khai phá dữ liệu với bộ dữ liệu BankChurners
* **Sinh viên thực hiện:** Đỗ Văn Đạt
* **Thời lượng thuyết trình đề xuất:** 12 - 15 phút

---

## ⏱️ PHẦN I: KỊCH BẢN THUYẾT TRÌNH TỪNG SLIDE (SPEAKER SCRIPT)

### Slide 1: Bìa Thuyết trình (Thời lượng: 1 phút)
> *"Kính chào Thầy/Cô và các bạn sinh viên. Em tên là Đỗ Văn Đạt, sinh viên chuyên ngành Phân tích Dữ liệu Kinh doanh - Học viện Ngân hàng. Hôm nay, em xin phép được đại diện nhóm nghiên cứu trình bày Báo cáo bài tập giữa kỳ với đề tài: **Xử lý dữ liệu và Khai phá dữ liệu trên bộ dữ liệu khách hàng thẻ tín dụng rời bỏ (Bank Customer Churn Analysis & Data Mining)**. Báo cáo sẽ đưa Thầy/Cô đi từ những góc nhìn thực tiễn về bài toán kinh tế mảng thẻ, qua quy trình tiền xử lý, khám phá dữ liệu chuyên sâu và ứng dụng các thuật toán máy học tân tiến để kiến tạo giải pháp giữ chân khách hàng hiệu quả nhất."*

---

### Slide 2: Bối cảnh Kinh doanh & Bài toán Kinh tế (Thời lượng: 1.5 phút)
> *"Kính thưa Thầy/Cô, thẻ tín dụng luôn được xem là 'con gà đẻ trứng vàng' của các ngân hàng thương mại bán lẻ nhờ 3 trụ cột thu nhập: phí quẹt thẻ POS/E-commerce, lãi suất tín dụng quay vòng và các loại phí thường niên. Tuy nhiên, thị trường đang chứng kiến sự cạnh tranh gay gắt từ các tổ chức tín dụng và Fintech.*  
> *Theo nghiên cứu của Bain & Company và Harvard Business Review, chi phí thu hút một khách hàng mới (CAC) đắt gấp 5 đến 7 lần chi phí giữ chân một khách hàng hiện hữu (CRC), trong khi chỉ cần tăng 5% tỷ lệ giữ chân có thể thúc đẩy lợi nhuận tăng từ 25% đến 95%. Trong bộ dữ liệu của chúng ta, tỷ lệ rời bỏ lên tới 16.07% — tức cứ 6 khách hàng mở thẻ thì có 1 khách hàng rời bỏ. Đây là tổn thất vô cùng lớn nếu ngân hàng không có biện pháp ngăn chặn kịp thời."*

---

### Slide 3: Kiến trúc Pipeline Toàn diện (Thời lượng: 1 phút)
> *"Để giải quyết triệt để bài toán, đề tài được cấu trúc theo 4 giai đoạn chuẩn mực:*  
> *1. Tiền xử lý dữ liệu và làm sạch: Loại trừ rò rỉ dữ liệu, xử lý missing và tạo đặc trưng mới.*  
> *2. Phân tích khám phá dữ liệu (EDA): Bóc tách các yếu tố nhân khẩu học, hành vi quẹt thẻ và tương tác CSKH.*  
> *3. Khai phá dữ liệu nâng cao (Data Mining): Phân cụm khách hàng qua K-Means/PCA và huấn luyện 4 mô hình máy học dự báo rời bỏ.*  
> *4. Ứng dụng quản trị: Xây dựng 3 chân dung khách hàng, Khung chiến lược giữ chân 4 tầng và mô phỏng hiệu quả tài chính ROI 500%."*

---

### Slide 4: Tiền xử lý & Kỹ thuật Tạo biến (Thời lượng: 1.5 phút)
> *"Ở khâu tiền xử lý, nhóm đã đưa ra 3 quyết định kỹ thuật quan trọng:*  
> *Thứ nhất, loại bỏ hoàn toàn 2 cột Naive Bayes ở cuối bảng gốc để ngăn ngừa triệt để hiện tượng rò rỉ dữ liệu (Data Leakage).*  
> *Thứ hai, xử lý các ô trống bằng giá trị Trung vị (Median Imputation) để đảm bảo tính vững chắc trước các giá trị ngoại lai.*  
> *Thứ ba, bảo toàn danh mục 'Unknown' trong học vấn và thu nhập như một phân lớp hành vi độc lập thay vì xóa bỏ.*  
> *Đặc biệt, nhóm đã kiến tạo 5 biến phái sinh có giá trị kinh tế cao như: `Avg_Trans_Value` (giá trị chi tiêu bình quân/giao dịch), `Revolving_Ratio` (tỷ lệ nợ quay vòng trên hạn mức) và `Contact_Intensity` (chỉ số cường độ bất mãn)."*

---

### Slide 5: Biến mục tiêu & Mất cân bằng lớp (Thời lượng: 1 phút)
> *"Quan sát phân phối biến mục tiêu, chúng ta có 8,500 khách hàng ở lại (83.9%) và 1,627 khách hàng rời bỏ (16.1%), tương ứng tỷ lệ mất cân bằng xấp xỉ 1:5.22.*  
> *Điểm mấu chốt ở đây là chúng ta không thể sử dụng độ chính xác thuần túy (Accuracy) làm thước đo chính. Nhóm bắt buộc phải tập trung tối ưu hóa chỉ số **Recall (Độ nhạy)**, **F1-Score** và **ROC-AUC** để đảm bảo mô hình không bỏ sót bất kỳ khách hàng nào đang có ý định rời bỏ."*

---

### Slide 6: Phân tích Nhân khẩu học (Thời lượng: 1 phút)
> *"Phân tích nhân khẩu học mang lại 3 phát hiện bất ngờ:*  
> *1. Khách hàng Nữ có tỷ lệ rời bỏ cao hơn Nam (17.36% vs 14.62%, kiểm định Chi-square p = 0.0002).*  
> *2. Hiện tượng rủi ro phân hóa hai đầu thu nhập (Bimodal Risk): Nhóm thu nhập thấp dưới $40K và nhóm thu nhập cao trên $120K có tỷ lệ rời bỏ cao nhất (~17.2% - 17.3%), trong khi nhóm thu nhập trung bình $60K-$80K lại là nhóm trung thành nhất.*  
> *3. Khách hàng có học vị Tiến sĩ có tỷ lệ rời bỏ cao nhất (21.06%)."*

---

### Slide 7: Hành vi Giao dịch - Vùng Nguy cơ Cao (Thời lượng: 1.5 phút)
> *"Khi phân tích biểu đồ phân tán giữa số lần giao dịch và tổng tiền chi tiêu, chúng ta phát hiện một 'Vùng nguy cơ cao' cực kỳ rõ ràng.*  
> *Khách hàng rời bỏ có số lần quẹt thẻ bình quân chỉ 44.9 lần/năm (giảm 34.6% so với nhóm ở lại là 68.7 lần). Toàn bộ các khách hàng có **dưới 55 lần giao dịch** và **chi tiêu dưới $3,000 USD** tập trung dày đặc các điểm màu đỏ rời bỏ. Tần suất quẹt thẻ chính là 'nhịp tim' phản ánh mức độ trung thành của khách hàng."*

---

### Slide 8: Chỉ số Tài chính - Dư nợ Quay vòng về 0 (Thời lượng: 1 phút)
> *"Một quy luật tài chính vô cùng đặc sắc được phát hiện: Khách hàng ở lại duy trì dư nợ quay vòng bình quân $1,257 USD (trung vị $1,364 USD). Nhưng ở nhóm khách hàng rời bỏ, **giá trị trung vị dư nợ quay vòng chính xác bằng $0.00 USD** và tỷ lệ sử dụng hạn mức trung vị bằng 0%.*  
> *Điều này phản ánh hành vi tâm lý thực tế: Trước khi chính thức yêu cầu đóng thẻ, khách hàng luôn chủ động tất toán sạch sẽ dư nợ để tránh phát sinh lãi phạt và hoàn toàn dừng quẹt thẻ."*

---

### Slide 9: Tương tác CSKH & Rào cản Hệ sinh thái (Thời lượng: 1 phút)
> *"Tại slide này, chúng ta nhìn thấy 'Ngưỡng bức xúc 3 lần liên hệ': Khách hàng gọi tổng đài 0-1 lần có tỷ lệ rời bỏ dưới 8%. Nhưng khi số lần gọi tăng lên 3 lần, tỷ lệ rời bỏ vọt lên 20.2%, lên 34.1% ở 4 lần và đạt tới 100% khi gọi 6 lần.*  
> *Đồng thời, đồ thị bên phải chứng minh: Khách hàng chỉ dùng 1-2 sản phẩm có tỷ lệ rời bỏ 26-28%, nhưng khi sở hữu từ 4 sản phẩm trở lên, tỷ lệ rời bỏ giảm xuống chỉ còn xấp xỉ 10%. Bán chéo đa sản phẩm chính là rào cản chuyển đổi vững chắc nhất."*

---

### Slide 10: Khai phá Phân cụm K-Means & PCA (Thời lượng: 1.5 phút)
> *"Bước sang phần Khai phá Dữ liệu, thuật toán K-Means kết hợp phương pháp Elbow và Silhouette Score đã xác định số cụm tối ưu là k = 4:*  
> *• Cụm 0 (37.6%): Khách hàng tiêu dùng phổ thông ổn định (Churn = 9.2%).*  
> *• Cụm 1 (24.0%): Khách hàng Ngủ đông & Nguy cơ cực cao (Dư nợ chỉ $210, Churn lên tới 41.8%!).*  
> *• Cụm 2 (18.7%): Khách hàng VIP chi tiêu lớn (Chi tiêu $9.5K, Churn = 14.5%).*  
> *• Cụm 3 (19.7%): Khách hàng vay tín dụng quay vòng (Dư nợ $2.2K, Churn thấp nhất 7.6%).*  
> *Phân cụm giúp ngân hàng định vị chính xác phân khúc rủi ro để phân bổ nguồn lực giữ chân tối ưu."*

---

### Slide 11 & 12: Hiệu năng Mô hình Máy học & Ma trận Nhầm lẫn (Thời lượng: 2 phút)
> *"Nhóm đã thử nghiệm và so sánh 4 mô hình phân loại:*  
> *• Logistic Regression (Baseline): ROC-AUC 0.9348, Recall 83.38%.*  
> *• Decision Tree: ROC-AUC 0.9458, Recall 88.92%.*  
> *• Random Forest: ROC-AUC 0.9838, Recall 87.08%.*  
> *🌟 **XGBoost Classifier vượt trội hoàn toàn** với **ROC-AUC đạt 0.9930**, **Recall đạt 91.38%**, **Precision 87.61%** và **Accuracy 96.54%**.*  
> *Nhìn vào ma trận nhầm lẫn, trên tập kiểm thử độc lập 2,026 khách hàng, XGBoost bắt trúng 297/325 khách hàng rời bỏ, chỉ bỏ sót 28 khách hàng và tỷ lệ báo động giả chỉ 2.4%."*

---

### Slide 13 & 14: Feature Importance & Tối ưu hóa Ngưỡng Kinh tế (Thời lượng: 1.5 phút)
> *"Phân tích Feature Importance khẳng định 3 nhân tố chi phối lớn nhất là: Tổng số lần giao dịch (`Total_Trans_Ct`), mức độ sụt giảm giao dịch quý cuối (`Total_Ct_Chng_Q4_Q1`) và dư nợ quay vòng (`Total_Revolving_Bal`).*  
> *Về mặt kinh tế, bằng cách mô hình hóa bài toán chi phí - lợi ích (CLV $500 vs Chi phí ưu đãi $50), nhóm đã xác định được **ngưỡng cắt xác suất tối ưu tại t = 0.42** (thay vì 0.50 mặc định), giúp tối đa hóa lợi nhuận ròng thu về đạt hơn $112,000 USD trên tập Test."*

---

### Slide 15: Ba Chân dung Khách hàng Rời bỏ (Thời lượng: 1.5 phút)
> *"Từ các bằng chứng thực nghiệm, nhóm đúc kết 3 chân dung khách hàng điển hình:*  
> *1. **The Silent Defector (Chiếm 55% Churn):** Ngủ đông, dư nợ về 0, không khiếu nại, lặng lẽ bỏ thẻ $\rightarrow$ Can thiệp bằng E-voucher kích hoạt giao dịch cuối tuần.*  
> *2. **Frustrated Complainer (Chiếm 25% Churn):** Bất mãn vì gọi CSKH 3-6 lần $\rightarrow$ Đội ngũ VIP Taskforce liên hệ giải quyết dứt điểm trong 24 giờ và miễn giảm phí linh hoạt.*  
> *3. **The VIP Switcher (Chiếm 20% Churn):** Thu nhập cao, bị đối thủ lôi kéo $\rightarrow$ Cán bộ RM chủ động tặng lượt phòng chờ sân bay và nhân đôi điểm tích dặm bay."*

---

### Slide 16 & 17: Khung Chiến lược 4 Tầng & Hiệu quả Tài chính ROI 500% (Thời lượng: 1.5 phút)
> *"Nhóm đề xuất Khung chiến lược giữ chân 4 tầng khép kín: Tầng 1 - Cảnh báo sớm (EWS), Tầng 2 - CSKH chủ động, Tầng 3 - Gamified Loyalty và Tầng 4 - Bán chéo hệ sinh thái.*  
> *Mô phỏng trên quy mô 10,000 khách hàng thẻ:*  
> *• Nếu không can thiệp, ngân hàng mất $800,000 USD/năm.*  
> *• Ứng dụng mô hình XGBoost giúp cứu vãn thành công 960 khách hàng, mang lại giá trị CLV $480,000 USD.*  
> *• Trừ đi $80,000 USD chi phí can thiệp, ngân hàng thu về **lợi nhuận ròng tăng thêm $400,000 USD/năm**, tương ứng **tỷ suất hoàn vốn ROI lên tới 500%**."*

---

### Slide 18 & 19: Kết luận & Q&A (Thời lượng: 1 phút)
> *"Tóm lại, đề tài đã hoàn thành xuất sắc toàn diện từ làm sạch dữ liệu, khám phá quy luật hành vi, khai phá phân cụm K-Means, xây dựng mô hình XGBoost đạt ROC-AUC 0.9930 và đề xuất giải pháp kinh doanh mang lại ROI 500%.*  
> *Em xin chân thành cảm ơn Thầy/Cô và các bạn đã chú ý lắng nghe. Em rất mong nhận được những câu hỏi và ý kiến đóng góp quý báu từ Thầy/Cô!"*

---

## 🎯 PHẦN II: BỘ 10 CÂU HỎI PHẢN BIỆN KINH ĐIỂN CỦA GIẢNG VIÊN (Q&A DEFENSE)

### Câu hỏi 1: Vì sao nhóm lại loại bỏ 2 cột Naive Bayes ở cuối bảng mà không đưa vào huấn luyện mô hình?
* **Đáp án chuẩn:**  
  Hai cột này là kết quả dự báo xác suất rời bỏ được tạo sẵn bởi tác giả bộ dữ liệu trong một thử nghiệm trước đó. Nếu giữ lại trong ma trận đặc trưng $X$, mô hình máy học sẽ học trực tiếp từ nhãn dự đoán sẵn có này, dẫn đến hiện tượng **rò rỉ dữ liệu (Data Leakage)**. Khi đó, mô hình sẽ đạt điểm cao giả tạo trong môi trường thử nghiệm nhưng hoàn toàn vô dụng khi triển khai thực tế trên dữ liệu khách hàng mới. Việc loại bỏ là bắt buộc theo chuẩn mực khoa học dữ liệu.

### Câu hỏi 2: Tại sao nhóm lại giữ nguyên danh mục 'Unknown' trong các biến định tính thay vì xóa bỏ hoặc điền Mode?
* **Đáp án chuẩn:**  
  Biến `Education_Level` có 15.0%, `Income_Category` có 11.0% và `Marital_Status` có 7.4% giá trị 'Unknown'. Nếu xóa toàn bộ các dòng chứa 'Unknown', chúng ta sẽ mất đi gần 30% mẫu quan sát quý giá (gần 3,000 khách hàng). Nếu điền Mode (gán ép theo giá trị phổ biến nhất), chúng ta sẽ làm méo mó phân phối thực tế. Việc giữ nguyên 'Unknown' như một phân lớp thông tin độc lập phản ánh đúng thực tế ngành ngân hàng: Những khách hàng từ chối tiết lộ thu nhập/học vấn thường có tâm lý bảo mật cao hoặc thuộc phân khúc tài chính đặc thù cần được theo dõi riêng.

### Câu hỏi 3: Tập dữ liệu bị mất cân bằng lớp (16% Churn vs 84% Retained), nhóm đã xử lý kỹ thuật như thế nào?
* **Đáp án chuẩn:**  
  Nhóm đã áp dụng chiến lược đa tầng:  
  1. Sử dụng kỹ thuật chia mẫu phân tầng (`StratifiedKFold` và `stratify=y` trong `train_test_split`) để tỷ lệ 16% Churn được bảo toàn nguyên vẹn ở cả tập Train và Test.  
  2. Gán trọng số phạt lớp thiểu số (`class_weight='balanced'` trong Logistic/Random Forest và `scale_pos_weight = 8500/1627 ≈ 5.22` trong XGBoost).  
  3. Không sử dụng Accuracy làm thước đo chính mà tập trung tối ưu hóa **Recall (Độ nhạy)**, **F1-Score** và diện tích dưới đường cong **ROC-AUC**.

### Câu hỏi 4: Ý nghĩa nghiệp vụ thực tế của hiện tượng "Dư nợ quay vòng về 0" là gì?
* **Đáp án chuẩn:**  
  Trong nghiệp vụ thẻ, khách hàng duy trì dư nợ quay vòng (`Total_Revolving_Bal`) là những người đang tích cực sử dụng thẻ và trả góp định kỳ sinh lãi cho ngân hàng. Khi một khách hàng chuẩn bị đóng tài khoản, họ có xu hướng thanh toán dứt điểm toàn bộ số dư nợ để tránh bị tính lãi hoặc phát sinh phí trễ hạn, sau đó cất thẻ vào ngăn kéo (ngủ đông) trước khi gọi tổng đài yêu cầu hủy. Do đó, việc dư nợ quay vòng giảm đột ngột về $0.00 USD kết hợp với tần suất quẹt thẻ giảm là một chỉ báo trễ trực tiếp báo hiệu khách hàng chuẩn bị rời bỏ.

### Câu hỏi 5: Ngưỡng báo động 3 lần liên hệ tổng đài mang lại bài học gì cho khối Vận hành CSKH?
* **Đáp án chuẩn:**  
  Dữ liệu EDA chứng minh: Khách hàng liên hệ tổng đài 0-1 lần có tỷ lệ rời bỏ < 8%, nhưng khi liên hệ lần thứ 3, tỷ lệ rời bỏ tăng vọt lên 20.21%, lên 34.11% ở lần 4 và đạt 100% ở lần 6. Điều này chứng minh rằng khách hàng không tự nhiên gọi nhiều lần nếu sự cố của họ được giải quyết thỏa đáng ngay lần đầu. Ngân hàng cần áp dụng chỉ số **First-Contact Resolution (FCR)** và thiết lập cơ chế cảnh báo tự động: Ngay khi khách hàng phát sinh cuộc gọi thứ 3, hệ thống CRM phải lập tức gán cờ ưu tiên (VIP Ticket) để quản lý ca trực trực tiếp xử lý dứt điểm khiếu nại trong 24 giờ.

### Câu hỏi 6: Tại sao XGBoost lại đạt hiệu năng vượt trội hơn hẳn Logistic Regression trong bài toán này?
* **Đáp án chuẩn:**  
  Hành vi khách hàng thẻ tín dụng có tính chất phi tuyến tính phức tạp và chứa đựng nhiều tương tác chéo (ví dụ: mối quan hệ tương tác giữa số lần giao dịch, mức độ sụt giảm quý cuối và số sản phẩm sở hữu). Logistic Regression là mô hình tuyến tính nên gặp hạn chế khi phân tách các ranh giới phi tuyến này. Trong khi đó, XGBoost là thuật toán Ensemble dạng Boosting, xây dựng tuần tự các cây quyết định để sửa chữa sai số của các cây trước đó, kết hợp cơ chế phạt chính quy hóa L1/L2 (Regularization) giúp kiểm soát overfitting xuất sắc và tối ưu hóa ranh giới quyết định phi tuyến, đạt ROC-AUC lên tới 0.9930.

### Câu hỏi 7: Phân cụm K-Means phân loại được 4 nhóm khách hàng nào và ứng dụng thực tiễn ra sao?
* **Đáp án chuẩn:**  
  K-Means chia cơ sở khách hàng thành 4 nhóm hành vi tự nhiên:  
  • **Cụm 0 (37.6% - Phổ thông):** Giữ chân bằng tích điểm tiêu dùng định kỳ.  
  • **Cụm 1 (24.0% - Ngủ đông & Nguy cơ cao, Churn 41.8%):** Đối tượng ưu tiên số 1 cần can thiệp khẩn cấp bằng Voucher hoàn tiền kích hoạt lại giao dịch.  
  • **Cụm 2 (18.7% - VIP Chi tiêu lớn):** Chăm sóc qua cán bộ RM, tặng phòng chờ sân bay, tăng hạn mức thẻ.  
  • **Cụm 3 (19.7% - Vay tín dụng quay vòng, Churn thấp nhất 7.6%):** Khách hàng mang lại biên lợi nhuận lãi suất cao nhất, cần bán chéo thêm các gói vay tiêu dùng tín chấp.

### Câu hỏi 8: Nhóm đã tối ưu hóa ngưỡng cắt xác suất (Threshold Optimization) như thế nào?
* **Đáp án chuẩn:**  
  Ngưỡng mặc định 0.5 chỉ tối ưu về mặt thống kê xác suất thuần túy chứ không tối ưu về mặt kinh tế. Nhóm đã xây dựng hàm mục tiêu lợi nhuận ròng dựa trên bài toán chi phí: Lợi ích giữ được 1 khách là $500 (CLV), chi phí can thiệp là $50, và thiệt hại bỏ sót khách churn là -$500. Bằng cách quét ngưỡng xác suất từ 0.05 đến 0.95, nhóm tìm ra điểm cực đại của hàm lợi nhuận tại **ngưỡng t = 0.42**, giúp ngân hàng tối đa hóa lợi nhuận ròng thu về đạt hơn $112,000 USD trên tập kiểm thử.

### Câu hỏi 9: Hai biến `Credit_Limit` và `Avg_Open_To_Buy` có tương quan $r = 0.996$, việc này ảnh hưởng gì và nhóm xử lý ra sao?
* **Đáp án chuẩn:**  
  Tương quan $r = 0.996$ phản ánh hiện tượng gần như đa cộng tuyến hoàn hảo (Multicollinearity). Đối với mô hình Logistic Regression, đa cộng tuyến làm tăng phương sai của các hệ số hồi quy, khiến việc diễn giải trọng số biến bị sai lệch. Tuy nhiên, đối với các mô hình cây quyết định và Ensemble như Random Forest hay XGBoost, đa cộng tuyến không làm giảm độ chính xác dự báo (mô hình sẽ tự động chọn biến có thông tin phân tách tốt nhất tại mỗi nút rẽ). Khi huấn luyện Logistic Regression chuẩn mực, chúng ta có thể loại bỏ 1 trong 2 biến dựa trên hệ số VIF (Variance Inflation Factor).

### Câu hỏi 10: Đóng góp giá trị nhất mà nhóm muốn khuyến nghị cho Ban Giám đốc Khối Bán lẻ là gì?
* **Đáp án chuẩn:**  
  Khuyến nghị cốt lõi nhất là: **"Đừng đợi khách hàng gọi điện hủy thẻ mới bắt đầu giữ chân — hãy chuyển từ thế bị động sang chủ động bằng Hệ thống Cảnh báo Sớm (EWS) và Chiến lược Bán chéo Hệ sinh thái"**. Cụ thể:  
  1. Theo dõi chặt chẽ nhịp tim giao dịch: Ngay khi khách hàng quẹt thẻ dưới 5 lần/tháng hoặc không phát sinh giao dịch 2 tháng liên tiếp, hệ thống phải tự động đẩy ưu đãi kích hoạt ngay.  
  2. Gia tăng rào cản chuyển đổi: Đẩy mạnh bán chéo để mỗi khách hàng sở hữu $\ge 4$ sản phẩm tài chính, giúp tỷ lệ rời bỏ tự động giảm xuống chỉ còn xấp xỉ 10%, mang lại ROI 500% cho ngân hàng.
"""

with open(SCRIPT_PATH, "w", encoding="utf-8") as f:
    f.write(script_content)
print(f"🎉 Đã tạo Kịch bản Thuyết trình & Q&A Defense Guide tại: {SCRIPT_PATH}")
