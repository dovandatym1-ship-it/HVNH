import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RAW_CSV_PATH = os.path.join(BASE_DIR, "Economic Data.csv")
OUT_CSV_PATH_1 = os.path.join(BASE_DIR, "processed data.csv")
OUT_XLSX_PATH_1 = os.path.join(BASE_DIR, "processed data.xlsx")

# Also save to parent BA directory
PARENT_DIR = os.path.abspath(os.path.join(BASE_DIR, ".."))
OUT_CSV_PATH_2 = os.path.join(PARENT_DIR, "processed data.csv")
OUT_XLSX_PATH_2 = os.path.join(PARENT_DIR, "processed data.xlsx")

def process_economic_data():
    print(f"🔄 Đang đọc tệp dữ liệu gốc từ: {RAW_CSV_PATH}")
    df_raw = pd.read_csv(RAW_CSV_PATH)
    print(f"📊 Kích thước ban đầu: {df_raw.shape[0]} dòng, {df_raw.shape[1]} cột")
    
    df = df_raw.copy()
    
    # --------------------------------------------------------------------------
    # BƯỚC 1: XỬ LÝ GIÁ TRỊ KHUYẾT THIẾU (MISSING VALUES)
    # --------------------------------------------------------------------------
    num_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    cols_to_impute = [c for c in num_cols if c not in ['year']]
    
    print("\n🔍 Đang xử lý khuyết thiếu bằng phương pháp Trung vị theo từng Quốc gia (Grouped Median Imputation)...")
    for col in cols_to_impute:
        country_medians = df.groupby('country')[col].transform('median')
        df[col] = df[col].fillna(country_medians)
        if df[col].isnull().sum() > 0:
            global_med = df[col].median()
            df[col] = df[col].fillna(global_med)
            
    print(f"Kiểm tra missing sau khi điền: {df.isnull().sum().sum()} ô trống (Sạch 100%).")
    
    # --------------------------------------------------------------------------
    # BƯỚC 2: XỬ LÝ NGOẠI LAI (OUTLIER TREATMENT - IQR WINSORIZATION / CAPPING)
    # --------------------------------------------------------------------------
    print("\n📈 Đang xử lý ngoại lai bằng phương pháp IQR Winsorization (Capping)...")
    feature_cols = [c for c in cols_to_impute if c not in ['index price', 'log_indexprice']]
    
    outlier_stats = []
    for col in feature_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        n_outliers = ((df[col] < lower_bound) | (df[col] > upper_bound)).sum()
        outlier_stats.append({
            'Tên Biến': col,
            'Q1 (25%)': Q1,
            'Q3 (75%)': Q3,
            'IQR': IQR,
            'Cận Dưới (Lower Bound)': lower_bound,
            'Cận Trên (Upper Bound)': upper_bound,
            'Số Lượng Ngoại Lai (Capped)': n_outliers
        })
        df[col] = np.clip(df[col], lower_bound, upper_bound)
        
    df_outlier_stats = pd.DataFrame(outlier_stats)
    
    # --------------------------------------------------------------------------
    # BƯỚC 3: KIẾN TẠO BIẾN PHÁI SINH (FEATURE ENGINEERING)
    # --------------------------------------------------------------------------
    print("\n💡 Đang tạo các biến phái sinh kinh tế vĩ mô...")
    df['real_interest_rate'] = df['USTreasury'] * 100 - df['inflationrate']
    df['trade_to_gdp_proxy'] = df['tradebalance'] / (df['gdppercent'].abs() + 1.0)
    df['misery_index'] = df['unemploymentrate'] + df['inflationrate']
    
    # --------------------------------------------------------------------------
    # BƯỚC 4: CHUẨN HÓA DỮ LIỆU (STANDARDIZATION - Z-SCORE SCALING)
    # --------------------------------------------------------------------------
    df_clean_unscaled = df.copy()
    
    all_num_features = df.select_dtypes(include=[np.number]).columns.tolist()
    scale_cols = [c for c in all_num_features if c not in ['year', 'log_indexprice', 'index price']]
    
    scaler = StandardScaler()
    df_scaled = df.copy()
    df_scaled[scale_cols] = scaler.fit_transform(df[scale_cols])
    
    # Thống kê mô tả & Ma trận tương quan
    df_desc = df.describe().T.reset_index().rename(columns={'index': 'Tên Biến'})
    df_corr = df[all_num_features].corr(method='pearson').reset_index().rename(columns={'index': 'Biến Số'})
    
    # --------------------------------------------------------------------------
    # BƯỚC 5: XUẤT FILE ĐẦU RA 'processed data.csv' & 'processed data.xlsx'
    # --------------------------------------------------------------------------
    for csv_p, xlsx_p in [(OUT_CSV_PATH_1, OUT_XLSX_PATH_1), (OUT_CSV_PATH_2, OUT_XLSX_PATH_2)]:
        # Lưu file CSV
        df.to_csv(csv_p, index=False)
        
        # Lưu file Excel đa sheet chuyên nghiệp
        with pd.ExcelWriter(xlsx_p, engine='openpyxl') as writer:
            df.to_excel(writer, sheet_name='Processed_Data', index=False)
            df_scaled.to_excel(writer, sheet_name='Standardized_ZScore_Data', index=False)
            df_desc.to_excel(writer, sheet_name='Summary_Statistics', index=False)
            df_corr.to_excel(writer, sheet_name='Correlation_Matrix', index=False)
            df_outlier_stats.to_excel(writer, sheet_name='Outlier_Capping_Stats', index=False)
            
        print(f"✅ Đã lưu file đã xử lý tại: {csv_p}")
        print(f"✅ Đã lưu file Excel đa sheet tại: {xlsx_p}")
        
    print("\n🎉 Hoàn thành xuất toàn diện các tệp processed data!")

if __name__ == "__main__":
    process_economic_data()
