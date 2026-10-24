import os
import sys
import json
import joblib
import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from xgboost import XGBRegressor

# Cấu hình đường dẫn
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROCESSED_CSV_PATH = os.path.join(BASE_DIR, "processed data.csv")
X_NEW_PATH = os.path.join(BASE_DIR, "X_new.xlsx")
FIG_DIR = os.path.join(BASE_DIR, "figures")
os.makedirs(FIG_DIR, exist_ok=True)

# Parent BA directory paths
PARENT_DIR = os.path.abspath(os.path.join(BASE_DIR, ".."))
PARENT_FIG_DIR = os.path.join(PARENT_DIR, "figures")
os.makedirs(PARENT_FIG_DIR, exist_ok=True)

def train_and_evaluate():
    print("=" * 80)
    print("🚀 BẮT ĐẦU HUẤN LUYỆN & ĐÁNH GIÁ MÔ HÌNH RANDOM FOREST & XGBOOST CHO ECONOMIC DATA")
    print("=" * 80)
    
    # 1. Đọc dữ liệu đã xử lý
    print(f"\n📂 Đang đọc dữ liệu từ: {PROCESSED_CSV_PATH}")
    df = pd.read_csv(PROCESSED_CSV_PATH)
    print(f"📊 Kích thước dữ liệu: {df.shape[0]} quan sát, {df.shape[1]} thuộc tính")
    
    # 2. Xác định biến độc lập (X) và biến mục tiêu (y)
    # Danh sách 9 biến kinh tế vĩ mô cơ sở
    base_features = [
        'inflationrate', 'oil prices', 'exchange_rate', 'gdppercent',
        'percapitaincome', 'unemploymentrate', 'manufacturingoutput',
        'tradebalance', 'USTreasury'
    ]
    # Toàn bộ biến kinh tế độc lập bao gồm 3 biến phái sinh
    all_features = [
        'inflationrate', 'oil prices', 'exchange_rate', 'gdppercent',
        'percapitaincome', 'unemploymentrate', 'manufacturingoutput',
        'tradebalance', 'USTreasury', 'real_interest_rate',
        'trade_to_gdp_proxy', 'misery_index'
    ]
    
    # Lựa chọn all_features để mô hình đạt hiệu năng tối đa
    feature_cols = all_features
    target_col = 'log_indexprice'
    
    X = df[feature_cols]
    y = df[target_col]
    
    print(f"🎯 Biến mục tiêu: {target_col}")
    print(f"🧩 Số lượng đặc trưng đầu vào: {len(feature_cols)} biến:")
    for i, col in enumerate(feature_cols, 1):
        print(f"   {i:2d}. {col}")
        
    # 3. Chia tập dữ liệu Train / Test (80% Train, 20% Test)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, shuffle=True
    )
    print(f"\n✂️ Phân chia dữ liệu: Train = {X_train.shape[0]} mẫu (80%), Test = {X_test.shape[0]} mẫu (20%)")
    
    # 4. Chuẩn hóa đặc trưng bằng StandardScaler (Fit trên Train, Transform trên Test)
    scaler = StandardScaler()
    X_train_scaled = pd.DataFrame(scaler.fit_transform(X_train), columns=feature_cols, index=X_train.index)
    X_test_scaled = pd.DataFrame(scaler.transform(X_test), columns=feature_cols, index=X_test.index)
    
    # Lưu Scaler
    joblib.dump(scaler, os.path.join(BASE_DIR, "scaler.pkl"))
    joblib.dump(scaler, os.path.join(BASE_DIR, "scaler.joblib"))
    joblib.dump(scaler, os.path.join(PARENT_DIR, "scaler.pkl"))
    print("💾 Đã lưu StandardScaler vào scaler.pkl & scaler.joblib")
    
    # --------------------------------------------------------------------------
    # 5. MÔ HÌNH 1: LINEAR REGRESSION (BASELINE)
    # --------------------------------------------------------------------------
    print("\n" + "-" * 50)
    print("📌 [1/3] HUẤN LUYỆN LINEAR REGRESSION (BASELINE OLS)...")
    lr_model = LinearRegression()
    lr_model.fit(X_train_scaled, y_train)
    
    y_train_pred_lr = lr_model.predict(X_train_scaled)
    y_test_pred_lr = lr_model.predict(X_test_scaled)
    
    r2_train_lr = r2_score(y_train, y_train_pred_lr)
    r2_test_lr = r2_score(y_test, y_test_pred_lr)
    rmse_test_lr = np.sqrt(mean_squared_error(y_test, y_test_pred_lr))
    mae_test_lr = mean_absolute_error(y_test, y_test_pred_lr)
    mape_test_lr = np.mean(np.abs((y_test - y_test_pred_lr) / (y_test + 1e-6))) * 100
    
    print(f"   Train R²: {r2_train_lr:.4f} | Test R²: {r2_test_lr:.4f} | Test RMSE: {rmse_test_lr:.4f} | Test MAE: {mae_test_lr:.4f}")
    
    # --------------------------------------------------------------------------
    # 6. MÔ HÌNH 2: RANDOM FOREST REGRESSOR
    # --------------------------------------------------------------------------
    print("\n" + "-" * 50)
    print("🌲 [2/3] HUẤN LUYỆN RANDOM FOREST REGRESSOR...")
    rf_model = RandomForestRegressor(
        n_estimators=300,
        max_depth=12,
        min_samples_split=3,
        min_samples_leaf=2,
        max_features='sqrt',
        bootstrap=True,
        random_state=42,
        n_jobs=-1
    )
    rf_model.fit(X_train_scaled, y_train)
    
    y_train_pred_rf = rf_model.predict(X_train_scaled)
    y_test_pred_rf = rf_model.predict(X_test_scaled)
    
    r2_train_rf = r2_score(y_train, y_train_pred_rf)
    r2_test_rf = r2_score(y_test, y_test_pred_rf)
    rmse_test_rf = np.sqrt(mean_squared_error(y_test, y_test_pred_rf))
    mae_test_rf = mean_absolute_error(y_test, y_test_pred_rf)
    mape_test_rf = np.mean(np.abs((y_test - y_test_pred_rf) / (y_test + 1e-6))) * 100
    
    # 5-fold Cross-Validation
    cv_scores_rf = cross_val_score(rf_model, X_train_scaled, y_train, cv=5, scoring='r2')
    
    print(f"   Train R²: {r2_train_rf:.4f} | Test R²: {r2_test_rf:.4f} | 5-Fold CV R²: {cv_scores_rf.mean():.4f} (±{cv_scores_rf.std():.4f})")
    print(f"   Test RMSE: {rmse_test_rf:.4f} | Test MAE: {mae_test_rf:.4f} | Test MAPE: {mape_test_rf:.2f}%")
    
    # Lưu mô hình Random Forest
    joblib.dump(rf_model, os.path.join(BASE_DIR, "random_forest_model.pkl"))
    joblib.dump(rf_model, os.path.join(BASE_DIR, "random_forest_model.joblib"))
    joblib.dump(rf_model, os.path.join(PARENT_DIR, "random_forest_model.pkl"))
    print("💾 Đã lưu Random Forest model vào random_forest_model.pkl")
    
    # --------------------------------------------------------------------------
    # 7. MÔ HÌNH 3: XGBOOST REGRESSOR
    # --------------------------------------------------------------------------
    print("\n" + "-" * 50)
    print("⚡ [3/3] HUẤN LUYỆN XGBOOST REGRESSOR...")
    xgb_model = XGBRegressor(
        n_estimators=350,
        learning_rate=0.03,
        max_depth=5,
        subsample=0.85,
        colsample_bytree=0.85,
        reg_alpha=0.1,
        reg_lambda=1.0,
        random_state=42,
        n_jobs=-1
    )
    xgb_model.fit(X_train_scaled, y_train)
    
    y_train_pred_xgb = xgb_model.predict(X_train_scaled)
    y_test_pred_xgb = xgb_model.predict(X_test_scaled)
    
    r2_train_xgb = r2_score(y_train, y_train_pred_xgb)
    r2_test_xgb = r2_score(y_test, y_test_pred_xgb)
    rmse_test_xgb = np.sqrt(mean_squared_error(y_test, y_test_pred_xgb))
    mae_test_xgb = mean_absolute_error(y_test, y_test_pred_xgb)
    mape_test_xgb = np.mean(np.abs((y_test - y_test_pred_xgb) / (y_test + 1e-6))) * 100
    
    cv_scores_xgb = cross_val_score(xgb_model, X_train_scaled, y_train, cv=5, scoring='r2')
    
    print(f"   Train R²: {r2_train_xgb:.4f} | Test R²: {r2_test_xgb:.4f} | 5-Fold CV R²: {cv_scores_xgb.mean():.4f} (±{cv_scores_xgb.std():.4f})")
    print(f"   Test RMSE: {rmse_test_xgb:.4f} | Test MAE: {mae_test_xgb:.4f} | Test MAPE: {mape_test_xgb:.2f}%")
    
    # Lưu mô hình XGBoost
    xgb_model.save_model(os.path.join(BASE_DIR, "xgboost_model.json"))
    joblib.dump(xgb_model, os.path.join(BASE_DIR, "xgboost_model.pkl"))
    joblib.dump(xgb_model, os.path.join(PARENT_DIR, "xgboost_model.pkl"))
    print("💾 Đã lưu XGBoost model vào xgboost_model.json & xgboost_model.pkl")
    
    # --------------------------------------------------------------------------
    # 8. BẢNG TỔNG HỢP HIỆU NĂNG SO SÁNH (MODEL COMPARISON)
    # --------------------------------------------------------------------------
    metrics_summary = [
        {
            "Mô Hình": "Linear Regression (OLS)",
            "Train R²": round(r2_train_lr, 4),
            "Test R²": round(r2_test_lr, 4),
            "Test RMSE": round(rmse_test_lr, 4),
            "Test MAE": round(mae_test_lr, 4),
            "Test MAPE (%)": round(mape_test_lr, 2),
            "5-Fold CV R²": "N/A",
            "Đánh Giá": "Mô hình cơ sở tuyến tính"
        },
        {
            "Mô Hình": "Random Forest Regressor",
            "Train R²": round(r2_train_rf, 4),
            "Test R²": round(r2_test_rf, 4),
            "Test RMSE": round(rmse_test_rf, 4),
            "Test MAE": round(mae_test_rf, 4),
            "Test MAPE (%)": round(mape_test_rf, 2),
            "5-Fold CV R²": f"{cv_scores_rf.mean():.4f} ± {cv_scores_rf.std():.4f}",
            "Đánh Giá": "Rất tốt, bắt phi tuyến mạnh"
        },
        {
            "Mô Hình": "XGBoost Regressor (Tốt nhất)",
            "Train R²": round(r2_train_xgb, 4),
            "Test R²": round(r2_test_xgb, 4),
            "Test RMSE": round(rmse_test_xgb, 4),
            "Test MAE": round(mae_test_xgb, 4),
            "Test MAPE (%)": round(mape_test_xgb, 2),
            "5-Fold CV R²": f"{cv_scores_xgb.mean():.4f} ± {cv_scores_xgb.std():.4f}",
            "Đánh Giá": "Xuất sắc nhất, sai số nhỏ nhất"
        }
    ]
    df_metrics = pd.DataFrame(metrics_summary)
    
    print("\n" + "=" * 80)
    print("🏆 BẢNG TỔNG HỢP SO SÁNH HIỆU NĂNG 3 MÔ HÌNH HỒI QUY:")
    print("=" * 80)
    print(df_metrics.to_string(index=False))
    
    # Xuất metrics ra CSV và Excel
    df_metrics.to_csv(os.path.join(BASE_DIR, "model_evaluation_metrics.csv"), index=False)
    df_metrics.to_excel(os.path.join(BASE_DIR, "model_evaluation_metrics.xlsx"), index=False)
    df_metrics.to_csv(os.path.join(PARENT_DIR, "model_evaluation_metrics.csv"), index=False)
    df_metrics.to_excel(os.path.join(PARENT_DIR, "model_evaluation_metrics.xlsx"), index=False)
    
    # --------------------------------------------------------------------------
    # 9. PHÂN TÍCH TẦM QUAN TRỌNG CỦA CÁC BIẾN (FEATURE IMPORTANCES)
    # --------------------------------------------------------------------------
    # Random Forest Importance
    df_rf_imp = pd.DataFrame({
        'Feature': feature_cols,
        'Importance': rf_model.feature_importances_
    }).sort_values(by='Importance', ascending=False).reset_index(drop=True)
    
    # XGBoost Importance
    df_xgb_imp = pd.DataFrame({
        'Feature': feature_cols,
        'Importance': xgb_model.feature_importances_
    }).sort_values(by='Importance', ascending=False).reset_index(drop=True)
    
    print("\n📊 TOP 5 BIẾN QUAN TRỌNG NHẤT (RANDOM FOREST):")
    print(df_rf_imp.head(5).to_string(index=False))
    
    print("\n📊 TOP 5 BIẾN QUAN TRỌNG NHẤT (XGBOOST):")
    print(df_xgb_imp.head(5).to_string(index=False))
    
    # --------------------------------------------------------------------------
    # 10. TRỰC QUAN HÓA & LƯU BIỂU ĐỒ CHẤT LƯỢNG CAO (300 DPI)
    # --------------------------------------------------------------------------
    print("\n🎨 Đang kết xuất các biểu đồ trực quan hóa...")
    sns.set_theme(style="whitegrid", palette="muted")
    
    # Biểu đồ 1: Actual vs Predicted cho Random Forest & XGBoost
    fig, axes = plt.subplots(1, 2, figsize=(16, 7), dpi=300)
    
    # RF
    axes[0].scatter(y_test, y_test_pred_rf, color="#1F4D78", alpha=0.75, edgecolors='k', s=60, label="Test Data Points")
    axes[0].plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2.5, label="Perfect Fit (y = x)")
    axes[0].set_title(f"Random Forest: Actual vs Predicted (Test R² = {r2_test_rf:.4f})", fontsize=13, fontweight='bold', color="#0A2540")
    axes[0].set_xlabel("Giá trị thực tế (Actual log_indexprice)", fontsize=11, fontweight='bold')
    axes[0].set_ylabel("Giá trị dự báo (Predicted log_indexprice)", fontsize=11, fontweight='bold')
    axes[0].legend(frameon=True, facecolor='white')
    axes[0].grid(True, linestyle='--', alpha=0.6)
    
    # XGBoost
    axes[1].scatter(y_test, y_test_pred_xgb, color="#EA580C", alpha=0.75, edgecolors='k', s=60, label="Test Data Points")
    axes[1].plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'b--', lw=2.5, label="Perfect Fit (y = x)")
    axes[1].set_title(f"XGBoost: Actual vs Predicted (Test R² = {r2_test_xgb:.4f})", fontsize=13, fontweight='bold', color="#0A2540")
    axes[1].set_xlabel("Giá trị thực tế (Actual log_indexprice)", fontsize=11, fontweight='bold')
    axes[1].set_ylabel("Giá trị dự báo (Predicted log_indexprice)", fontsize=11, fontweight='bold')
    axes[1].legend(frameon=True, facecolor='white')
    axes[1].grid(True, linestyle='--', alpha=0.6)
    
    plt.tight_layout()
    plt.savefig(os.path.join(FIG_DIR, "economic_rf_xgb_actual_vs_pred.png"), dpi=300)
    plt.savefig(os.path.join(PARENT_FIG_DIR, "economic_rf_xgb_actual_vs_pred.png"), dpi=300)
    plt.close()
    
    # Biểu đồ 2: Feature Importances Comparison
    fig, axes = plt.subplots(1, 2, figsize=(16, 7), dpi=300)
    
    # RF Bars
    sns.barplot(x='Importance', y='Feature', data=df_rf_imp, ax=axes[0], palette='Blues_r')
    axes[0].set_title("Tầm Quan Trọng Của Biến (Random Forest)", fontsize=13, fontweight='bold', color="#0A2540")
    axes[0].set_xlabel("Mức độ quan trọng (MDI Gini Impurity)", fontsize=11)
    axes[0].set_ylabel("Biến kinh tế đầu vào", fontsize=11)
    for p in axes[0].patches:
        axes[0].annotate(f"{p.get_width():.3f}", (p.get_width() + 0.005, p.get_y() + p.get_height() / 2),
                         va='center', fontsize=9, color="#0F172A")
                         
    # XGBoost Bars
    sns.barplot(x='Importance', y='Feature', data=df_xgb_imp, ax=axes[1], palette='Oranges_r')
    axes[1].set_title("Tầm Quan Trọng Của Biến (XGBoost Gain)", fontsize=13, fontweight='bold', color="#0A2540")
    axes[1].set_xlabel("Mức độ quan trọng (Gain Importance)", fontsize=11)
    axes[1].set_ylabel("Biến kinh tế đầu vào", fontsize=11)
    for p in axes[1].patches:
        axes[1].annotate(f"{p.get_width():.3f}", (p.get_width() + 0.005, p.get_y() + p.get_height() / 2),
                         va='center', fontsize=9, color="#0F172A")
                         
    plt.tight_layout()
    plt.savefig(os.path.join(FIG_DIR, "economic_feature_importance_comparison.png"), dpi=300)
    plt.savefig(os.path.join(PARENT_FIG_DIR, "economic_feature_importance_comparison.png"), dpi=300)
    plt.close()
    
    # Biểu đồ 3: Residuals Distribution
    plt.figure(figsize=(10, 6), dpi=300)
    res_rf = y_test - y_test_pred_rf
    res_xgb = y_test - y_test_pred_xgb
    sns.kdeplot(res_rf, label=f"Random Forest Residuals (Std = {res_rf.std():.3f})", color="#1F4D78", fill=True, alpha=0.3, lw=2)
    sns.kdeplot(res_xgb, label=f"XGBoost Residuals (Std = {res_xgb.std():.3f})", color="#EA580C", fill=True, alpha=0.3, lw=2)
    plt.axvline(0, color='k', linestyle='--', lw=1.5)
    plt.title("Phân Phối Sai Số Dư (Residual Error Distribution)", fontsize=14, fontweight='bold', color="#0A2540")
    plt.xlabel("Sai số (Actual - Predicted)", fontsize=11, fontweight='bold')
    plt.ylabel("Mật độ xác suất (Density)", fontsize=11, fontweight='bold')
    plt.legend(frameon=True, facecolor='white')
    plt.tight_layout()
    plt.savefig(os.path.join(FIG_DIR, "economic_residuals_distribution.png"), dpi=300)
    plt.savefig(os.path.join(PARENT_FIG_DIR, "economic_residuals_distribution.png"), dpi=300)
    plt.close()
    
    # --------------------------------------------------------------------------
    # 11. THỬ NGHIỆM DỰ BÁO TRÊN TẬP DỮ LIỆU MỚI (INFERENCE ON X_new.xlsx)
    # --------------------------------------------------------------------------
    print("\n" + "-" * 50)
    print("🔮 [4/4] DỰ BÁO THỰC TẾ TRÊN TỆP DỮ LIỆU MỚI (X_new.xlsx)...")
    if os.path.exists(X_NEW_PATH):
        df_xnew = pd.read_excel(X_NEW_PATH)
        print(f"Dữ liệu X_new gốc có các cột: {list(df_xnew.columns)}")
        
        # Bổ sung 3 biến phái sinh tương ứng cho X_new
        df_xnew_proc = df_xnew.copy()
        df_xnew_proc['real_interest_rate'] = df_xnew_proc['USTreasury'] * 100 - df_xnew_proc['inflationrate']
        df_xnew_proc['trade_to_gdp_proxy'] = df_xnew_proc['tradebalance'] / (df_xnew_proc['gdppercent'].abs() + 1.0)
        df_xnew_proc['misery_index'] = df_xnew_proc['unemploymentrate'] + df_xnew_proc['inflationrate']
        
        # Sắp xếp đúng thứ tự cột
        X_new_features = df_xnew_proc[feature_cols]
        X_new_scaled = scaler.transform(X_new_features)
        
        # Dự báo
        pred_log_lr = lr_model.predict(X_new_scaled)[0]
        pred_log_rf = rf_model.predict(X_new_scaled)[0]
        pred_log_xgb = xgb_model.predict(X_new_scaled)[0]
        
        pred_price_lr = np.exp(pred_log_lr)
        pred_price_rf = np.exp(pred_log_rf)
        pred_price_xgb = np.exp(pred_log_xgb)
        
        df_pred_res = pd.DataFrame([
            {"Mô Hình": "Linear Regression (OLS)", "Dự Báo log_indexprice": round(pred_log_lr, 4), "Giá Trị Quy Đổi index price ($)": round(pred_price_lr, 2)},
            {"Mô Hình": "Random Forest Regressor", "Dự Báo log_indexprice": round(pred_log_rf, 4), "Giá Trị Quy Đổi index price ($)": round(pred_price_rf, 2)},
            {"Mô Hình": "XGBoost Regressor (Khuyên dùng)", "Dự Báo log_indexprice": round(pred_log_xgb, 4), "Giá Trị Quy Đổi index price ($)": round(pred_price_xgb, 2)}
        ])
        
        print("\n📈 KẾT QUẢ DỰ BÁO TRÊN X_new:")
        print(df_pred_res.to_string(index=False))
        
        df_pred_res.to_excel(os.path.join(BASE_DIR, "X_new_predictions.xlsx"), index=False)
        df_pred_res.to_excel(os.path.join(PARENT_DIR, "X_new_predictions.xlsx"), index=False)
        
    print("\n" + "=" * 80)
    print("🎉 HOÀN THÀNH TOÀN BỘ QUY TRÌNH HUẤN LUYỆN, LƯU MÔ HÌNH VÀ DỰ BÁO CHO RANDOM FOREST & XGBOOST!")
    print("=" * 80)

if __name__ == "__main__":
    train_and_evaluate()
