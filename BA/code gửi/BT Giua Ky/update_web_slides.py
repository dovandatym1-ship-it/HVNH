import os
import sys
import base64

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FIG_DIR = os.path.join(BASE_DIR, "figures")
HTML_PATH = os.path.join(BASE_DIR, "Slide_Thuyet_Trinh_BankChurners.html")
MARP_PATH = os.path.join(BASE_DIR, "Slide_Thuyet_Trinh_BankChurners.md")
SCRIPT_PATH = os.path.join(BASE_DIR, "Kich_Ban_Thuyet_Trinh_va_Cau_Hoi_Phan_Bien.md")

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

# ==============================================================================
# 1. GENERATE ULTRA-PREMIUM INTERACTIVE HTML PRESENTATION (EXECUTIVE SUITE)
# ==============================================================================
html_content = f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Slide Thuyết Trình Cao Học: Khai Phá Dữ Liệu BankChurners - Đỗ Văn Đạt HVNH</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <style>
        :root {{
            --hvnh-navy: #0A2540;
            --hvnh-orange: #EA580C;
            --hvnh-gold: #F59E0B;
            --blue-cyan: #0284C7;
            --accent-red: #DC2626;
            --accent-green: #10B981;
            --bg: #F8FAFC;
            --card-bg: #FFFFFF;
            --text-dark: #0F172A;
            --text-muted: #64748B;
            --border: #E2E8F0;
            --shadow: 0 10px 25px -5px rgba(15, 23, 42, 0.06), 0 8px 10px -6px rgba(15, 23, 42, 0.04);
        }}
        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        }}
        body {{
            background-color: var(--hvnh-navy);
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
            max-width: 1440px;
            max-height: 810px;
            background-color: var(--bg);
            border-radius: 16px;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.6);
            overflow: hidden;
            display: flex;
            flex-direction: column;
        }}
        .slide {{
            display: none;
            flex: 1;
            padding: 35px 50px;
            overflow-y: auto;
            animation: slideIn 0.35s cubic-bezier(0.16, 1, 0.3, 1);
        }}
        .slide.active {{
            display: flex;
            flex-direction: column;
        }}
        @keyframes slideIn {{
            from {{ opacity: 0; transform: translateY(12px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        .slide-header {{
            margin-bottom: 18px;
            border-bottom: 2px solid #E2E8F0;
            padding-bottom: 12px;
            position: relative;
        }}
        .slide-header::after {{
            content: '';
            position: absolute;
            bottom: -2px;
            left: 0;
            width: 120px;
            height: 2px;
            background: var(--hvnh-orange);
        }}
        .slide-tag {{
            font-size: 11px;
            font-weight: 700;
            color: var(--hvnh-navy);
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 4px;
            display: flex;
            align-items: center;
            gap: 6px;
        }}
        .slide-tag span.badge-tag {{
            color: var(--hvnh-orange);
        }}
        .slide-title {{
            font-size: 22px;
            font-weight: 800;
            color: var(--hvnh-navy);
            line-height: 1.25;
        }}
        .slide-content {{
            flex: 1;
            display: grid;
            gap: 20px;
            align-items: stretch;
        }}
        .grid-2 {{ grid-template-columns: 1.15fr 0.85fr; }}
        .grid-3 {{ grid-template-columns: 1fr 1fr 1fr; }}
        .grid-4 {{ grid-template-columns: 1fr 1fr 1fr 1fr; }}
        
        .card {{
            background-color: var(--card-bg);
            border-radius: 12px;
            padding: 22px;
            border: 1px solid var(--border);
            box-shadow: var(--shadow);
            display: flex;
            flex-direction: column;
            position: relative;
        }}
        .card.card-accent-top {{
            border-top: 4px solid var(--hvnh-navy);
        }}
        .card.card-accent-orange {{
            border-top: 4px solid var(--hvnh-orange);
        }}
        .card.card-accent-red {{
            border-top: 4px solid var(--accent-red);
        }}
        .card.card-accent-green {{
            border-top: 4px solid var(--accent-green);
        }}
        .card h3 {{
            font-size: 16px;
            font-weight: 700;
            color: var(--hvnh-navy);
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        .big-kpi {{
            font-size: 32px;
            font-weight: 900;
            color: var(--hvnh-navy);
            margin-bottom: 4px;
            line-height: 1;
        }}
        .kpi-sub {{
            font-size: 12px;
            font-weight: 700;
            color: var(--hvnh-orange);
            margin-bottom: 14px;
        }}
        .card p, .card ul {{
            font-size: 13px;
            color: var(--text-dark);
            line-height: 1.6;
        }}
        .card ul {{
            padding-left: 18px;
        }}
        .card li {{
            margin-bottom: 6px;
        }}
        .card li b {{
            color: var(--hvnh-navy);
        }}
        .img-container {{
            background: #fff;
            border-radius: 12px;
            border: 1px solid var(--border);
            padding: 12px;
            box-shadow: var(--shadow);
            text-align: center;
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

        /* Hero Slide Custom */
        .slide-hero {{
            background: linear-gradient(135deg, #0A2540 0%, #061727 100%);
            color: #fff;
            justify-content: center;
            align-items: center;
            text-align: center;
            padding: 50px 60px;
            position: relative;
        }}
        .slide-hero::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 6px;
            background: var(--hvnh-orange);
        }}
        .hero-bav {{
            color: var(--hvnh-gold);
            font-size: 14px;
            font-weight: 800;
            letter-spacing: 2px;
            margin-bottom: 16px;
        }}
        .hero-title {{
            font-size: 32px;
            font-weight: 900;
            color: #FFFFFF;
            line-height: 1.25;
            margin-bottom: 10px;
        }}
        .hero-sub {{
            font-size: 20px;
            font-weight: 700;
            color: #FED7AA;
            margin-bottom: 28px;
            line-height: 1.4;
        }}
        .hero-grid {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 16px;
            width: 100%;
            margin-top: 15px;
        }}
        .hero-card {{
            background: rgba(255, 255, 255, 0.06);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.12);
            border-radius: 10px;
            padding: 16px;
            text-align: left;
        }}
        .hero-card .tag {{
            font-size: 10px;
            font-weight: 700;
            color: var(--hvnh-gold);
            margin-bottom: 4px;
        }}
        .hero-card .val1 {{
            font-size: 13px;
            font-weight: 700;
            color: #FFFFFF;
            margin-bottom: 2px;
        }}
        .hero-card .val2 {{
            font-size: 11px;
            color: #94A3B8;
        }}

        /* Controls */
        .controls {{
            height: 48px;
            background: #FFFFFF;
            border-top: 1px solid var(--border);
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0 30px;
            z-index: 10;
        }}
        .controls-info {{
            font-size: 12.5px;
            font-weight: 600;
            color: var(--text-muted);
        }}
        .btn {{
            background: var(--bg);
            border: 1px solid var(--border);
            padding: 6px 16px;
            border-radius: 6px;
            font-size: 12.5px;
            font-weight: 600;
            color: var(--text-dark);
            cursor: pointer;
            transition: all 0.2s;
        }}
        .btn:hover {{
            background: var(--hvnh-navy);
            color: #fff;
            border-color: var(--hvnh-navy);
        }}
    </style>
</head>
<body>

<div class="deck-container">
    <!-- SLIDE 1: HERO TITLE -->
    <div class="slide slide-hero active" id="slide-1">
        <div class="hero-bav">🏛️ HỌC VIỆN NGÂN HÀNG (BANKING ACADEMY)  •  KHOA HỆ THỐNG THÔNG TIN QUẢN LÝ</div>
        <div style="font-size:14px; font-weight:700; color:#BAE6FD; margin-bottom:8px;">BÁO CÁO BÀI TẬP GIỮA KỲ CHUYÊN ĐỀ CAO HỌC</div>
        <div class="hero-title">XỬ LÝ DỮ LIỆU & KHAI PHÁ DỮ LIỆU</div>
        <div class="hero-sub">PHÂN TÍCH HÀNH VI, PHÂN CỤM & DỰ BÁO NGUY CƠ RỜI BỎ<br>CỦA KHÁCH HÀNG THẺ TÍN DỤNG (BANK CHURN ANALYSIS)</div>
        
        <div class="hero-grid">
            <div class="hero-card">
                <div class="tag">👤 HỌC VIÊN THỰC HIỆN</div>
                <div class="val1">ĐỖ VĂN ĐẠT</div>
                <div class="val2">Chuyên ngành Business Analytics</div>
            </div>
            <div class="hero-card">
                <div class="tag">📚 HỌC PHẦN</div>
                <div class="val1">PHÂN TÍCH DỮ LIỆU KINH DOANH</div>
                <div class="val2">Học viện Ngân hàng</div>
            </div>
            <div class="hero-card">
                <div class="tag">📊 BỘ DỮ LIỆU</div>
                <div class="val1">BANKCHURNERS.CSV</div>
                <div class="val2">10,127 quan sát • 23 thuộc tính</div>
            </div>
            <div class="hero-card">
                <div class="tag">📅 NIÊN KHÓA</div>
                <div class="val1">NĂM HỌC 2025 - 2026</div>
                <div class="val2">Hà Nội, Năm 2026</div>
            </div>
        </div>
    </div>

    <!-- SLIDE 2: EXECUTIVE SUMMARY -->
    <div class="slide" id="slide-2">
        <div class="slide-header">
            <div class="slide-tag">HỌC VIỆN NGÂN HÀNG | BÀI TẬP GIỮA KỲ <span class="badge-tag">[TỔNG QUAN ĐIỀU HÀNH]</span></div>
            <div class="slide-title">Executive Summary: Tổng Hợp 4 Phát Hiện & Đóng Góp Giá Trị Của Đề Tài</div>
        </div>
        <div class="slide-content grid-4">
            <div class="card card-accent-red">
                <div class="bigpi" style="color:var(--accent-red); font-size:30px; font-weight:900;">16.07%</div>
                <div class="kpi-sub" style="color:var(--accent-red);">Tỷ lệ rời bỏ nghiêm trọng</div>
                <ul>
                    <li><b>Thực trạng:</b> Mất 1,627/10,127 khách hàng.</li>
                    <li><b>Chi phí:</b> CAC gấp 5-7 LẦN CRC.</li>
                    <li><b>Tổn thất:</b> $800,000 USD/năm.</li>
                </ul>
            </div>
            <div class="card card-accent-orange">
                <div class="bigpi" style="color:var(--hvnh-orange); font-size:30px; font-weight:900;">&lt; 55 GD</div>
                <div class="kpi-sub" style="color:var(--hvnh-orange);">Vùng nguy cơ báo động đỏ</div>
                <ul>
                    <li>Quẹt thẻ &lt; 55 lần & &lt; $3,000.</li>
                    <li>Dư nợ quay vòng Median = $0.00.</li>
                    <li>Gọi CSKH lần 3: Churn vọt 20.2%.</li>
                </ul>
            </div>
            <div class="card card-accent-top">
                <div class="bigpi" style="color:var(--blue-cyan); font-size:30px; font-weight:900;">0.9930</div>
                <div class="kpi-sub" style="color:var(--blue-cyan);">ROC-AUC XGBoost vượt trội</div>
                <ul>
                    <li><b>Recall:</b> 91.38% (bắt trúng &gt;9/10 khách).</li>
                    <li><b>Precision:</b> 87.61% | Accuracy: 96.54%.</li>
                    <li>Tối ưu ngưỡng kinh tế t = 0.42.</li>
                </ul>
            </div>
            <div class="card card-accent-green">
                <div class="bigpi" style="color:var(--accent-green); font-size:30px; font-weight:900;">ROI 500%</div>
                <div class="kpi-sub" style="color:var(--accent-green);">+$400,000 USD / Năm</div>
                <ul>
                    <li>Cứu vãn 960 khách hàng rủi ro.</li>
                    <li>Chi phí can thiệp: $80,000 USD.</li>
                    <li>Khung giữ chân 4 tầng & EWS.</li>
                </ul>
            </div>
        </div>
    </div>

    <!-- SLIDE 3: BỐI CẢNH & BÀI TOÁN KINH TẾ -->
    <div class="slide" id="slide-3">
        <div class="slide-header">
            <div class="slide-tag">HỌC VIỆN NGÂN HÀNG | BÀI TẬP GIỮA KỲ <span class="badge-tag">[BỐI CẢNH KINH DOANH]</span></div>
            <div class="slide-title">Bối Cảnh Thị Trường Thẻ & Bài Toán Kinh Tế Giữ Chân (CAC vs CRC)</div>
        </div>
        <div class="slide-content grid-3">
            <div class="card card-accent-top">
                <h3>💳 3 Trụ Cột Lợi Nhuận Thẻ</h3>
                <ul>
                    <li><b>Phí Quẹt Thẻ (Interchange):</b> Doanh thu chiết khấu từ đơn vị chấp nhận POS/E-commerce.</li>
                    <li><b>Lãi Suất Quay Vòng (Revolving):</b> Lãi vay biên cao nhất khi duy trì số dư nợ quá hạn miễn lãi.</li>
                    <li><b>Phí Dịch Vụ Định Kỳ:</b> Thường niên, chậm thanh toán, rút tiền mặt, chuyển đổi ngoại tệ.</li>
                </ul>
            </div>
            <div class="card card-accent-top">
                <h3>⚖️ Đòn Bẩy Chi Phí 5:1</h3>
                <ul>
                    <li><b>Quy tắc 5:1:</b> Chi phí tìm khách mới (CAC) gấp <b>5-7 LẦN</b> chi phí giữ chân khách cũ (CRC).</li>
                    <li><b>Tác động lợi nhuận:</b> Tăng 5% giữ chân giúp tăng <b>25% - 95%</b> lợi nhuận (Bain & Co).</li>
                    <li><b>Mất mát kép:</b> Mất doanh thu phí/lãi tương lai và lãng phí chi phí thẩm định ban đầu.</li>
                </ul>
            </div>
            <div class="card card-accent-red">
                <h3>🚨 Thực Trạng Rời Bỏ (16.07%)</h3>
                <ul>
                    <li><b>Tỷ lệ Churn:</b> 1,627 / 10,127 khách hàng đã hủy hoặc đóng thẻ tín dụng.</li>
                    <li><b>Cạnh tranh khốc liệt:</b> Fintech và ngân hàng đối thủ liên tục tung ưu đãi hoàn tiền hấp dẫn.</li>
                    <li><b>Yêu cầu cấp thiết:</b> Xây dựng mô hình AI phát hiện sớm tín hiệu rủi ro trước khi đóng thẻ.</li>
                </ul>
            </div>
        </div>
    </div>

    <!-- SLIDE 4: PIPELINE ARCHITECTURE -->
    <div class="slide" id="slide-4">
        <div class="slide-header">
            <div class="slide-tag">HỌC VIỆN NGÂN HÀNG | BÀI TẬP GIỮA KỲ <span class="badge-tag">[PHƯƠNG PHÁP LUẬN]</span></div>
            <div class="slide-title">Kiến Trúc Pipeline Xử Lý Dữ Liệu & Khai Phá Máy Học Toàn Diện</div>
        </div>
        <div class="slide-content grid-4">
            <div class="card card-accent-top">
                <h3>1. Tiền Xử Lý</h3>
                <ul>
                    <li>Loại bỏ 2 cột Naive Bayes</li>
                    <li>Điền Median cho Missing</li>
                    <li>Giữ nhóm 'Unknown' độc lập</li>
                    <li>Tạo 5 biến phái sinh mới</li>
                </ul>
            </div>
            <div class="card card-accent-top">
                <h3>2. Khám Phá (EDA)</h3>
                <ul>
                    <li>Phân tích phân phối Churn</li>
                    <li>Khảo sát nhân khẩu học & χ²</li>
                    <li>Nhận diện Vùng rủi ro GD</li>
                    <li>Phát hiện Dư nợ về 0 & CSKH</li>
                </ul>
            </div>
            <div class="card card-accent-orange">
                <h3>3. Khai Phá (ML)</h3>
                <ul>
                    <li>Phân cụm 4 nhóm K-Means/PCA</li>
                    <li>Huấn luyện LR, DT, RF, XGB</li>
                    <li>Đánh giá ROC-AUC & Recall</li>
                    <li>Tối ưu ngưỡng kinh tế (t=0.42)</li>
                </ul>
            </div>
            <div class="card card-accent-green">
                <h3>4. Quản Trị</h3>
                <ul>
                    <li>3 Chân dung rủi ro (Personas)</li>
                    <li>Khung Giữ chân 4 Tầng</li>
                    <li>Hệ thống Cảnh báo Sớm EWS</li>
                    <li>Mô phỏng ROI tài chính 500%</li>
                </ul>
            </div>
        </div>
    </div>

    <!-- SLIDE 5: PREPROCESSING & FEATURE ENGINEERING -->
    <div class="slide" id="slide-5">
        <div class="slide-header">
            <div class="slide-tag">HỌC VIỆN NGÂN HÀNG | BÀI TẬP GIỮA KỲ <span class="badge-tag">[TIỀN XỬ LÝ DỮ LIỆU]</span></div>
            <div class="slide-title">Tiền Xử Lý Dữ Liệu: Loại Bỏ Nhiễu & Kiến Tạo 5 Đặc Trưng Phái Sinh</div>
        </div>
        <div class="slide-content grid-2">
            <div class="card card-accent-top">
                <h3>🧹 Chiến Lược Làm Sạch & Chuẩn Hóa</h3>
                <ul>
                    <li><b>Loại trừ Data Leakage:</b> Xóa bỏ 2 cột Naive Bayes được phân loại sẵn ở cuối bảng để đảm bảo tính khách quan thực nghiệm.</li>
                    <li><b>Xử lý Missing bằng Median:</b> Điền giá trị Trung vị cho các ô trống trong biến số nhằm đảm bảo tính vững chắc (robust) trước các điểm ngoại lai.</li>
                    <li><b>Bảo toàn Danh mục 'Unknown':</b> Giữ nguyên nhóm 'Unknown' trong Học vấn (15.0%), Thu nhập (11.0%), Hôn nhân (7.4%) như một phân lớp thông tin hành vi độc lập.</li>
                </ul>
            </div>
            <div class="card card-accent-orange">
                <h3>⚙️ Kỹ Thuật Tạo 5 Đặc Trưng Mới</h3>
                <ul>
                    <li><b>Avg_Trans_Value:</b> Giá trị chi tiêu trung bình / lần quẹt thẻ (<code>Total_Trans_Amt / Total_Trans_Ct</code>).</li>
                    <li><b>Revolving_Ratio:</b> Tỷ lệ dư nợ quay vòng trên hạn mức cấp (<code>Revolving_Bal / Credit_Limit</code>).</li>
                    <li><b>Contact_Intensity:</b> Cường độ bất mãn (<code>Contacts / (Inactive_Months + 1)</code>).</li>
                    <li><b>Age_Group:</b> Phân 5 nhóm tuổi: &lt;35, 35-44, 45-54, 55-64, 65+.</li>
                    <li><b>Churn_Binary:</b> Mã hóa nhị phân 1 (Attrited) / 0 (Existing).</li>
                </ul>
            </div>
        </div>
    </div>

    <!-- SLIDE 6: TARGET DISTRIBUTION -->
    <div class="slide" id="slide-6">
        <div class="slide-header">
            <div class="slide-tag">HỌC VIỆN NGÂN HÀNG | BÀI TẬP GIỮA KỲ <span class="badge-tag">[EDA — BIẾN MỤC TIÊU]</span></div>
            <div class="slide-title">Phân Bố Biến Mục Tiêu: Thách Thức Mất Cân Bằng Lớp (Imbalance Ratio 1:5.22)</div>
        </div>
        <div class="slide-content grid-2">
            <div class="img-container">
                <img src="{img_map['churn_dist']}" alt="Churn Distribution">
            </div>
            <div class="card card-accent-top">
                <h3>📊 Phân Tích Mất Cân Bằng Lớp</h3>
                <ul>
                    <li><b>Cơ cấu Khách hàng:</b> 8,500 khách hàng Ở lại (83.93%) vs 1,627 khách hàng Rời bỏ (16.07%).</li>
                    <li><b>Tỷ lệ mất cân bằng:</b> Xấp xỉ 1:5.22 (Cứ 6 khách hàng mở thẻ thì có 1 khách hàng rời bỏ).</li>
                    <li><b>Bẫy Accuracy:</b> Nếu mô hình đoán toàn bộ ở lại, Accuracy vẫn đạt 83.93% nhưng bỏ sót 100% khách rời bỏ.</li>
                    <li><b>Bộ chỉ số tối ưu:</b> Bắt buộc phải ưu tiên <b>Recall (Độ nhạy)</b>, <b>Precision</b>, <b>F1-Score</b> và diện tích dưới đường cong <b>ROC-AUC</b>.</li>
                </ul>
            </div>
        </div>
    </div>

    <!-- SLIDE 7: DEMOGRAPHIC CHURN -->
    <div class="slide" id="slide-7">
        <div class="slide-header">
            <div class="slide-tag">HỌC VIỆN NGÂN HÀNG | BÀI TẬP GIỮA KỲ <span class="badge-tag">[EDA — NHÂN KHẨU HỌC]</span></div>
            <div class="slide-title">Phân Tích Nhân Khẩu Học: Khách Nữ & Hiện Tượng Rủi Ro Phân Hóa 2 Đầu Thu Nhập</div>
        </div>
        <div class="slide-content grid-2">
            <div class="img-container">
                <img src="{img_map['demographic']}" alt="Demographic Analysis">
            </div>
            <div class="card card-accent-top">
                <h3>🔍 3 Phát Hiện Nhân Khẩu Cốt Lõi</h3>
                <ul>
                    <li><b>Chênh lệch Giới tính:</b> Khách hàng Nữ có tỷ lệ rời bỏ <b>17.36%</b> cao hơn Nam là <b>14.62%</b> (kiểm định χ² có ý nghĩa p = 0.0002).</li>
                    <li><b>Rủi ro 2 đầu Thu nhập (Bimodal Risk):</b>
                        <ul>
                            <li>Thu nhập &lt; $40K: Churn <b>17.19%</b> (áp lực phí).</li>
                            <li>Thu nhập ≥ $120K: Churn <b>17.33%</b> (đối thủ lôi kéo).</li>
                            <li>Thu nhập $60K-$80K: Trung thành nhất (13.48%).</li>
                        </ul>
                    </li>
                    <li><b>Trình độ Học vấn:</b> Học vị Tiến sĩ (Doctorate) có tỷ lệ rời bỏ cao nhất (<b>21.06%</b>).</li>
                </ul>
            </div>
        </div>
    </div>

    <!-- SLIDE 8: TRANSACTION BEHAVIOR -->
    <div class="slide" id="slide-8">
        <div class="slide-header">
            <div class="slide-tag">HỌC VIỆN NGÂN HÀNG | BÀI TẬP GIỮA KỲ <span class="badge-tag">[EDA — HÀNH VI GIAO DỊCH]</span></div>
            <div class="slide-title">Hành Vi Giao Dịch: Nhận Diện 'Vùng Nguy Cơ Cao' (&lt; 55 Giao Dịch & &lt; $3,000)</div>
        </div>
        <div class="slide-content grid-2">
            <div class="img-container">
                <img src="{img_map['trans_scatter']}" alt="Transaction Behavior">
            </div>
            <div class="card card-accent-red">
                <h3>🚨 Điểm Báo Động Hành Vi</h3>
                <ul>
                    <li><b>Tổng số lần GD (Total_Trans_Ct):</b> Khách ở lại 68.7 lần vs Khách churn 44.9 lần (-34.6%, p &lt; 0.0001).</li>
                    <li><b>Tổng tiền GD (Total_Trans_Amt):</b> Khách ở lại $4,655 vs Khách churn $3,095 (-33.5%, p &lt; 0.0001).</li>
                    <li><b>VÙNG NGUY CƠ CAO (RED CLUSTER):</b> Toàn bộ khách hàng quẹt thẻ dưới <b>55 lần/năm</b> và chi tiêu <b>dưới $3,000</b> tập trung dày đặc các điểm rời bỏ. Tần suất quẹt thẻ là "nhịp tim" gắn kết.</li>
                </ul>
            </div>
        </div>
    </div>

    <!-- SLIDE 9: FINANCIAL RATIOS -->
    <div class="slide" id="slide-9">
        <div class="slide-header">
            <div class="slide-tag">HỌC VIỆN NGÂN HÀNG | BÀI TẬP GIỮA KỲ <span class="badge-tag">[EDA — TÀI CHÍNH]</span></div>
            <div class="slide-title">Chỉ Số Tài Chính: Hiện Tượng 'Dư Nợ Quay Vòng Về 0' Trước Khi Đóng Thẻ</div>
        </div>
        <div class="slide-content grid-2">
            <div class="img-container">
                <img src="{img_map['financial_box']}" alt="Financial Ratios">
            </div>
            <div class="card card-accent-top">
                <h3>📉 Tín Hiệu Dọn Đường Đóng Thẻ</h3>
                <ul>
                    <li><b>Dư nợ quay vòng (Total_Revolving_Bal):</b>
                        <ul>
                            <li>Khách ở lại: Mean $1,257 (Median $1,364).</li>
                            <li>Khách rời bỏ: Mean $673 (<b>MEDIAN = $0.00!</b>).</li>
                        </ul>
                    </li>
                    <li><b>Tỷ lệ sử dụng hạn mức (Utilization):</b>
                        <ul>
                            <li>Khách ở lại: 29.64% (Median 21.1%).</li>
                            <li>Khách rời bỏ: 16.25% (<b>MEDIAN = 0.00%!</b>).</li>
                        </ul>
                    </li>
                    <li><b>Quy luật tâm lý:</b> Khách hàng trước khi hủy thẻ luôn tất toán sạch nợ để tránh phát sinh lãi phạt và hoàn toàn dừng quẹt thẻ.</li>
                </ul>
            </div>
        </div>
    </div>

    <!-- SLIDE 10: CUSTOMER INTERACTIONS -->
    <div class="slide" id="slide-10">
        <div class="slide-header">
            <div class="slide-tag">HỌC VIỆN NGÂN HÀNG | BÀI TẬP GIỮA KỲ <span class="badge-tag">[EDA — DỊCH VỤ CSKH]</span></div>
            <div class="slide-title">Tương Tác CSKH & Mức Độ Ngủ Đông: 'Ngưỡng Báo Động 3 Lần Liên Hệ'</div>
        </div>
        <div class="slide-content grid-2">
            <div class="img-container">
                <img src="{img_map['interaction']}" alt="Interaction Decay">
            </div>
            <div class="card card-accent-orange">
                <h3>📞 Ngưỡng Bức Xúc 3 Lần Gọi</h3>
                <ul>
                    <li><b>Gọi CSKH 0 - 1 lần:</b> Tỷ lệ rời bỏ dưới 8% (mức thông thường).</li>
                    <li><b>Gọi CSKH 3 lần:</b> Tỷ lệ rời bỏ vọt lên <b>20.21%</b> (Báo động vàng).</li>
                    <li><b>Gọi CSKH 4 lần:</b> Tỷ lệ rời bỏ đạt <b>34.11%</b> (Báo động đỏ).</li>
                    <li><b>Gọi CSKH 5 - 6 lần:</b> Tỷ lệ rời bỏ lên tới <b>55% - 100%</b> (Bất mãn cực độ).</li>
                    <li><b>Bài học vận hành:</b> Cần áp dụng KPI First-Contact Resolution (FCR) xử lý dứt điểm khiếu nại trong 24 giờ.</li>
                </ul>
            </div>
        </div>
    </div>

    <!-- SLIDE 11: RELATIONSHIP & ECOSYSTEM -->
    <div class="slide" id="slide-11">
        <div class="slide-header">
            <div class="slide-tag">HỌC VIỆN NGÂN HÀNG | BÀI TẬP GIỮA KỲ <span class="badge-tag">[EDA — BÁN CHÉO]</span></div>
            <div class="slide-title">Hệ Sinh Thái Sản Phẩm: Rào Cản Chuyển Đổi Khi Khách Hàng Dùng ≥ 4 Sản Phẩm</div>
        </div>
        <div class="slide-content grid-2">
            <div class="img-container">
                <img src="{img_map['relationship']}" alt="Relationship Count">
            </div>
            <div class="card card-accent-green">
                <h3>🔗 Sức Mạnh của Bán Chéo (Cross-selling)</h3>
                <ul>
                    <li><b>Dùng 1 - 2 sản phẩm:</b> Tỷ lệ rời bỏ lên tới <b>26.15% - 27.81%</b> (Gắn kết lỏng lẻo).</li>
                    <li><b>Dùng 3 sản phẩm:</b> Tỷ lệ rời bỏ giảm xuống 17.77%.</li>
                    <li><b>Dùng ≥ 4 đến 6 sản phẩm:</b> Tỷ lệ rời bỏ giảm mạnh chỉ còn <b>10.49% - 11.78%</b> (Giảm gần 3 lần!).</li>
                    <li><b>Kết luận chiến lược:</b> Càng tích hợp nhiều dịch vụ (tài khoản lương, tiết kiệm, vay thế chấp), chi phí chuyển đổi càng cao, giữ chân khách hàng tự nhiên.</li>
                </ul>
            </div>
        </div>
    </div>

    <!-- SLIDE 12: K-MEANS CLUSTERING -->
    <div class="slide" id="slide-12">
        <div class="slide-header">
            <div class="slide-tag">HỌC VIỆN NGÂN HÀNG | BÀI TẬP GIỮA KỲ <span class="badge-tag">[DATA MINING — PHÂN CỤM]</span></div>
            <div class="slide-title">Khai Phá Dữ Liệu: Phân Cụm 4 Nhóm Khách Hàng Hành Vi (K-Means & PCA)</div>
        </div>
        <div class="slide-content grid-2">
            <div class="img-container">
                <img src="{img_map['kmeans_pca']}" alt="K-Means PCA">
            </div>
            <div class="card card-accent-top">
                <h3>👥 Hồ Sơ Đặc Trưng 4 Phân Cụm</h3>
                <ul>
                    <li><b>Cụm 0 (37.6%): Tiêu dùng ổn định:</b> Chi tiêu $4.1K, Dư nợ $1.4K, Churn = <b>9.2%</b> (Thấp).</li>
                    <li><b>Cụm 1 (24.0%): Ngủ đông & Nguy cơ cao:</b> Chi tiêu $1.8K, Dư nợ $210, Churn = <b style="color:var(--accent-red);">41.8%!</b> (Cực cao, ưu tiên can thiệp số 1).</li>
                    <li><b>Cụm 2 (18.7%): VIP Chi tiêu lớn:</b> Chi tiêu $9.5K, Hạn mức cao, Churn = <b>14.5%</b> (Nhạy bén ưu đãi).</li>
                    <li><b>Cụm 3 (19.7%): Vay nợ quay vòng:</b> Dư nợ $2.2K sinh lãi, Churn = <b>7.6%</b> (Gắn kết nhất).</li>
                </ul>
            </div>
        </div>
    </div>

    <!-- SLIDE 13: SUPERVISED ML COMPARISON -->
    <div class="slide" id="slide-13">
        <div class="slide-header">
            <div class="slide-tag">HỌC VIỆN NGÂN HÀNG | BÀI TẬP GIỮA KỲ <span class="badge-tag">[MACHINE LEARNING]</span></div>
            <div class="slide-title">Mô Hình Hóa Dự Báo: XGBoost Vượt Trội Toàn Diện (ROC-AUC = 0.9930, Recall = 91.38%)</div>
        </div>
        <div class="slide-content grid-2">
            <div class="img-container">
                <img src="{img_map['roc_auc']}" alt="ROC-AUC Curve">
            </div>
            <div class="card card-accent-top">
                <h3>🏆 So Sánh Hiệu Năng 4 Thuật Toán</h3>
                <ul>
                    <li><b>Logistic Regression:</b> ROC-AUC = 0.9348 | Recall = 83.38% | F1 = 67.25%</li>
                    <li><b>Decision Tree:</b> ROC-AUC = 0.9458 | Recall = 88.92% | F1 = 76.15%</li>
                    <li><b>Random Forest:</b> ROC-AUC = 0.9838 | Recall = 87.08% | F1 = 84.23%</li>
                    <li><b style="color:var(--accent-green);">🌟 XGBOOST CLASSIFIER (TOP 1):</b>
                        <ul>
                            <li><b>ROC-AUC:</b> <span style="color:var(--accent-green); font-weight:800;">0.9930</span> (Gần như tuyệt đối)</li>
                            <li><b>Recall:</b> <span style="color:var(--accent-green); font-weight:800;">91.38%</span> (Bắt trúng &gt;9/10 khách churn)</li>
                            <li><b>Precision:</b> 87.61% | <b>Accuracy:</b> 96.54%</li>
                        </ul>
                    </li>
                </ul>
            </div>
        </div>
    </div>

    <!-- SLIDE 14: CONFUSION MATRIX -->
    <div class="slide" id="slide-14">
        <div class="slide-header">
            <div class="slide-tag">HỌC VIỆN NGÂN HÀNG | BÀI TẬP GIỮA KỲ <span class="badge-tag">[ĐÁNH GIÁ MÔ HÌNH]</span></div>
            <div class="slide-title">Đánh Giá Sai Số: Ma Trận Nhầm Lẫn & Khả Năng Kiểm Soát Báo Động Giả</div>
        </div>
        <div class="slide-content grid-2">
            <div class="img-container">
                <img src="{img_map['confusion']}" alt="Confusion Matrix">
            </div>
            <div class="card card-accent-top">
                <h3>🎯 Kiểm Soát Sai Số Loại I & II</h3>
                <ul>
                    <li><b>Sai số Loại II (False Negative):</b> Chỉ bỏ sót 28/325 khách hàng rời bỏ trên tập kiểm thử độc lập (Tỷ lệ lỗi &lt; 8.6%).</li>
                    <li><b>Sai số Loại I (False Positive):</b> Chỉ có 42/1,701 khách hàng ở lại bị dự đoán nhầm (Tỷ lệ báo động giả &lt; 2.5%).</li>
                    <li><b>Ý nghĩa kinh tế thực tế:</b> Giúp ngân hàng can thiệp trúng đích khách hàng nguy cơ mà không lãng phí ngân sách ưu đãi cho khách hàng trung thành.</li>
                </ul>
            </div>
        </div>
    </div>

    <!-- SLIDE 15: FEATURE IMPORTANCE -->
    <div class="slide" id="slide-15">
        <div class="slide-header">
            <div class="slide-tag">HỌC VIỆN NGÂN HÀNG | BÀI TẬP GIỮA KỲ <span class="badge-tag">[GIẢI THÍCH MÔ HÌNH]</span></div>
            <div class="slide-title">Giải Thích Mô Hình: 5 Đòn Bẩy Hành Vi Quyết Định Đến Nguy Cơ Rời Bỏ</div>
        </div>
        <div class="slide-content grid-2">
            <div class="img-container">
                <img src="{img_map['feat_imp']}" alt="Feature Importance">
            </div>
            <div class="card card-accent-top">
                <h3>🔑 5 Đòn Bẩy Hành Vi Cốt Lõi</h3>
                <ul>
                    <li><b>1. Total_Trans_Ct (Số lần giao dịch):</b> Đóng góp quan trọng nhất. Tần suất quẹt thẻ phản ánh nhịp tim gắn kết.</li>
                    <li><b>2. Total_Ct_Chng_Q4_Q1:</b> Mức độ sụt giảm số giao dịch trong quý cuối so với đầu năm.</li>
                    <li><b>3. Total_Revolving_Bal:</b> Dấu hiệu tất toán đưa dư nợ quay vòng về 0.</li>
                    <li><b>4. Total_Trans_Amt:</b> Quy mô ngân sách chi tiêu phân bổ qua thẻ.</li>
                    <li><b>5. Relationship_Count & Contacts:</b> Ràng buộc hệ sinh thái và mức độ bức xúc dịch vụ.</li>
                </ul>
            </div>
        </div>
    </div>

    <!-- SLIDE 16: THRESHOLD OPTIMIZATION -->
    <div class="slide" id="slide-16">
        <div class="slide-header">
            <div class="slide-tag">HỌC VIỆN NGÂN HÀNG | BÀI TẬP GIỮA KỲ <span class="badge-tag">[TỐI ƯU HÓA KINH TẾ]</span></div>
            <div class="slide-title">Tối Ưu Hóa Ngưỡng Quyết Định: Điểm Cân Bằng Lợi Nhuận Ròng Tại t = 0.42</div>
        </div>
        <div class="slide-content grid-2">
            <div class="img-container">
                <img src="{img_map['cost_benefit']}" alt="Cost Benefit Optimization">
            </div>
            <div class="card card-accent-green">
                <h3>💰 Mô Hình Hóa Chi Phí - Lợi Ích</h3>
                <ul>
                    <li><b>Giả định bài toán kinh tế:</b>
                        <ul>
                            <li>Giá trị CLV giữ chân: $500 / khách.</li>
                            <li>Chi phí can thiệp ưu đãi: $50 / khách.</li>
                            <li>Mất khách không can thiệp: -$500 / khách.</li>
                        </ul>
                    </li>
                    <li><b>ĐIỂM CẮT TỐI ƯU (t = 0.42):</b>
                        <ul>
                            <li>Thay vì dùng ngưỡng 0.50, dịch chuyển sang t = 0.42 giúp tối đa hóa lợi nhuận ròng.</li>
                            <li>Recall đạt 94.0%, Precision đạt 86.2%.</li>
                            <li>Lợi nhuận ròng tối đa trên tập Test: <b>&gt; $112,000 USD</b>.</li>
                        </ul>
                    </li>
                </ul>
            </div>
        </div>
    </div>

    <!-- SLIDE 17: CUSTOMER PERSONAS -->
    <div class="slide" id="slide-17">
        <div class="slide-header">
            <div class="slide-tag">HỌC VIỆN NGÂN HÀNG | BÀI TẬP GIỮA KỲ <span class="badge-tag">[CHÂN DUNG KHÁCH HÀNG]</span></div>
            <div class="slide-title">Phác Họa 3 Chân Dung Khách Hàng Rời Bỏ Điển Hình & Hành Động Can Thiệp</div>
        </div>
        <div class="slide-content grid-3">
            <div class="card card-accent-top">
                <div style="font-size:11px; font-weight:700; color:var(--hvnh-navy); margin-bottom:4px;">55% TỔNG CHURN</div>
                <h3>1. The Silent Defector<br><small>(Ngủ đông & Rút lui)</small></h3>
                <ul>
                    <li>Dư nợ quay vòng = $0 USD.</li>
                    <li>Quẹt thẻ &lt; 45 lần/năm.</li>
                    <li>Ngủ đông liên tiếp ≥ 3 tháng.</li>
                    <li>Chi tiêu Q4 giảm &gt; 50%.</li>
                    <li><b>Can thiệp:</b> Gửi E-voucher quẹt thẻ cuối tuần, hoàn tiền 5% cho 3 GD đầu.</li>
                </ul>
            </div>
            <div class="card card-accent-red">
                <div style="font-size:11px; font-weight:700; color:var(--accent-red); margin-bottom:4px;">25% TỔNG CHURN</div>
                <h3>2. Frustrated Complainer<br><small>(Bức xúc & Khiếu nại)</small></h3>
                <ul>
                    <li>Gọi CSKH ≥ 3 - 6 lần/năm.</li>
                    <li>Chỉ dùng 1 - 2 sản phẩm.</li>
                    <li>Bất mãn về lỗi POS / phí phạt.</li>
                    <li>Tỷ lệ Churn lên tới 35% - 100%.</li>
                    <li><b>Can thiệp:</b> VIP Taskforce gọi hỗ trợ 24h, miễn giảm phí thường niên linh hoạt.</li>
                </ul>
            </div>
            <div class="card card-accent-top">
                <div style="font-size:11px; font-weight:700; color:var(--blue-cyan); margin-bottom:4px;">20% TỔNG CHURN</div>
                <h3>3. The VIP Switcher<br><small>(Khách VIP Chuyển dịch)</small></h3>
                <ul>
                    <li>Thu nhập ≥ $120K, Thẻ Gold/Plat.</li>
                    <li>Hạn mức tín dụng &gt; $15K.</li>
                    <li>Chi tiêu Q4 sụt giảm đột ngột.</li>
                    <li>Bị đối thủ lôi kéo bằng đặc quyền.</li>
                    <li><b>Can thiệp:</b> Cán bộ RM tặng lượt phòng chờ sân bay, nhân đôi điểm tích dặm bay.</li>
                </ul>
            </div>
        </div>
    </div>

    <!-- SLIDE 18: 4-TIER STRATEGY -->
    <div class="slide" id="slide-18">
        <div class="slide-header">
            <div class="slide-tag">HỌC VIỆN NGÂN HÀNG | BÀI TẬP GIỮA KỲ <span class="badge-tag">[KHUYẾN NGHỊ QUẢN TRỊ]</span></div>
            <div class="slide-title">Khung Chiến Lược Giữ Chân Khách Hàng 4 Tầng & Hệ Thống Cảnh Báo Sớm (EWS)</div>
        </div>
        <div class="slide-content grid-2">
            <div class="card card-accent-top">
                <h3>Tầng 1: Cảnh Báo Sớm (EWS)</h3>
                <p>Giám sát tự động thời gian thực các Trigger Point (Ngủ đông 2 tháng, gọi CSKH lần 3) để kích hoạt Push Notification & E-voucher.</p>
                <div style="margin-top:8px; font-weight:700; color:var(--hvnh-navy);">KPI: Tỷ lệ phát hiện sớm &gt; 90%</div>
            </div>
            <div class="card card-accent-top">
                <h3>Tầng 2: CSKH Chủ Động (Proactive)</h3>
                <p>Áp dụng chỉ tiêu First-Contact Resolution (FCR) giải quyết dứt điểm khiếu nại trong 24h; Trao quyền Miễn giảm phí (Fee Waiver) linh hoạt.</p>
                <div style="margin-top:8px; font-weight:700; color:var(--blue-cyan);">KPI: FCR &gt; 85%, Churn CSKH &lt; 5%</div>
            </div>
            <div class="card card-accent-orange">
                <h3>Tầng 3: Gamified Loyalty</h3>
                <p>Chiến dịch "Quẹt Thẻ Mỗi Tuần" tích điểm theo tần suất quẹt thẻ thay vì chỉ tính theo số tiền; Tự chọn danh mục hoàn tiền ưa thích.</p>
                <div style="margin-top:8px; font-weight:700; color:var(--hvnh-orange);">KPI: Tần suất GD ≥ 5 lần/tháng</div>
            </div>
            <div class="card card-accent-green">
                <h3>Tầng 4: Bán Chéo (Cross-selling)</h3>
                <p>Combo "Tài chính Toàn diện" liên kết thẻ tín dụng với tài khoản lương, tiết kiệm và thanh toán hóa đơn tự động (Auto-billing).</p>
                <div style="margin-top:8px; font-weight:700; color:var(--accent-green);">KPI: Sở hữu ≥ 4 SP đạt &gt; 65%</div>
            </div>
        </div>
    </div>

    <!-- SLIDE 19: FINANCIAL ROI -->
    <div class="slide" id="slide-19">
        <div class="slide-header">
            <div class="slide-tag">HỌC VIỆN NGÂN HÀNG | BÀI TẬP GIỮA KỲ <span class="badge-tag">[TÀI CHÍNH & ROI]</span></div>
            <div class="slide-title">Mô Phỏng Tài Chính: Lợi Nhuận Ròng Tăng +$400,000 USD/Năm (ROI = 500%)</div>
        </div>
        <div class="slide-content grid-2">
            <div class="card card-accent-top">
                <h3>📊 Giả Định Quy Mô 10,000 Khách Hàng</h3>
                <ul>
                    <li>Quy mô cơ sở: 10,000 chủ thẻ tín dụng.</li>
                    <li>Tỷ lệ rời bỏ tự nhiên: 16% (1,600 khách hàng/năm).</li>
                    <li>Giá trị CLV trung bình: $500 USD / khách hàng.</li>
                    <li><b>TỔN THẤT NẾU KHÔNG CAN THIỆP:</b><br><span style="color:var(--accent-red); font-size:18px; font-weight:800;">$800,000 USD / NĂM</span></li>
                    <li><b>Mục tiêu giữ chân với XGBoost:</b><br>Cứu vãn thành công 60% = <b>960 KHÁCH HÀNG</b>.</li>
                </ul>
            </div>
            <div class="card card-accent-green">
                <h3>💵 Tính Toán Lợi Nhuận & ROI</h3>
                <ul>
                    <li><b>Giá trị CLV cứu vãn được:</b> 960 × $500 = $480,000 USD.</li>
                    <li><b>Chi phí can thiệp ưu đãi:</b> 1,600 × $50 = $80,000 USD.</li>
                    <li><b>LỢI NHUẬN RÒNG GIA TĂNG:</b><br><span style="color:var(--accent-green); font-size:20px; font-weight:800;">+$400,000 USD / NĂM!</span></li>
                    <li><b>TỶ SUẤT HOÀN VỐN ĐẦU TƯ (ROI):</b><br><span style="color:var(--blue-cyan); font-size:22px; font-weight:800;">ROI = 500%</span></li>
                </ul>
            </div>
        </div>
    </div>

    <!-- SLIDE 20: CLOSING & Q&A -->
    <div class="slide slide-hero" id="slide-20">
        <div class="hero-bav">HỌC VIỆN NGÂN HÀNG (BANKING ACADEMY OF VIETNAM) — KHOA HTTTQL</div>
        <div class="hero-title" style="font-size:38px;">XIN TRÂN TRỌNG CẢM ƠN QUÝ THẦY/CÔ VÀ CÁC BẠN!</div>
        <div class="hero-sub" style="color:#E2E8F0; font-size:18px;">Kính chúc Quý Thầy/Cô nhiều sức khỏe & thành công!</div>
        <div style="font-size:24px; font-weight:800; color:var(--hvnh-gold); margin-top:15px;">HỎI & ĐÁP (Q&A SESSION)</div>
        <div style="font-size:13px; color:#94A3B8; margin-top:8px;">Rất mong nhận được các ý kiến nhận xét và câu hỏi phản biện từ Hội đồng!</div>
    </div>

    <!-- Controls Bar -->
    <div class="controls">
        <div class="controls-info" id="slide-indicator">Slide 1 / 20</div>
        <div class="nav-btns">
            <button class="btn" id="prev-btn" onclick="prevSlide()">◀ Trước</button>
            <button class="btn" id="next-btn" onclick="nextSlide()">Sau ▶</button>
        </div>
    </div>
</div>

<script>
    let currentSlide = 1;
    const totalSlides = 20;

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
print(f"🎉 Đã cập nhật Web Slide HTML tại: {HTML_PATH}")

# Mirror to root directory
os.system(f'cp "{HTML_PATH}" "{os.path.join(BASE_DIR, "..", "BT_Giua_Ky_BankChurners", "Slide_Thuyet_Trinh_BankChurners.html")}"')
os.system(f'cp "{PPTX_PATH}" "{os.path.join(BASE_DIR, "..", "BT_Giua_Ky_BankChurners", "Slide_Thuyet_Trinh_BankChurners.pptx")}"')
print("🎉 Đã đồng bộ sang BT_Giua_Ky_BankChurners/")
