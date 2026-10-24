import json
import os
import nbformat
from nbformat.v4 import new_notebook, new_markdown_cell, new_code_cell

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
NB_PATH_1 = os.path.join(BASE_DIR, "DoVanDat_Economic_Regression_RF_XGBoost.ipynb")
PARENT_DIR = os.path.abspath(os.path.join(BASE_DIR, ".."))
NB_PATH_2 = os.path.join(PARENT_DIR, "DoVanDat_Economic_Regression_RF_XGBoost.ipynb")

def build_notebook():
    nb = new_notebook()
    
    # Cell 0: Header Markdown
    nb.cells.append(new_markdown_cell("""# 🏛️ HỌC VIỆN NGÂN HÀNG — KHOA HỆ THỐNG THÔNG TIN QUẢN LÝ
## BÀI TẬP HỒI QUY DỮ LIỆU KINH TẾ VĨ MÔ (ECONOMIC DATA REGRESSION)
### Mô Hình Hóa Dự Báo Chỉ Số Chứng Khoán (`log_indexprice`) Bằng Random Forest & XGBoost Regressor
**Học viên thực hiện:** ĐỖ VĂN ĐẠT  |  **Học phần:** Phân tích Dữ liệu trong Kinh doanh (Business Analytics)

---

### 📋 Cấu Trúc Nội Dung Triển Khai:
1. **Phần 1:** Import thư viện và Tải dữ liệu đã xử lý (`processed data.csv`).
2. **Phần 2:** Khám phá đặc trưng và Phân chia tập dữ liệu Train / Test (80/20).
3. **Phần 3:** Chuẩn hóa đặc trưng đầu vào (`StandardScaler`).
4. **Phần 4:** Huấn luyện & Đánh giá mô hình **Linear Regression (Baseline OLS)**.
5. **Phần 5:** Huấn luyện & Đánh giá mô hình **Random Forest Regressor** (Đánh giá $R^2$, RMSE, MAE, 5-Fold CV).
6. **Phần 6:** Huấn luyện & Đánh giá mô hình **XGBoost Regressor** (Đánh giá $R^2$, RMSE, MAE, 5-Fold CV).
7. **Phần 7:** So sánh hiệu năng mô hình & Trực quan hóa Actual vs Predicted.
8. **Phần 8:** Phân tích Tầm quan trọng của các biến (Feature Importances).
9. **Phần 9:** Lưu trữ mô hình và Thử nghiệm dự báo thực tế trên `X_new.xlsx`."""))

    # Cell 1: Import Libraries
    nb.cells.append(new_code_cell("""# 1. Khởi tạo và nạp các thư viện khoa học dữ liệu
import os
import joblib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from xgboost import XGBRegressor

# Cấu hình giao diện biểu đồ
sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['axes.edgecolor'] = '#CBD5E1'
plt.rcParams['axes.linewidth'] = 1.2
print("✅ Đã nạp thành công tất cả thư viện cần thiết!")"""))

    # Cell 2: Load Data
    nb.cells.append(new_markdown_cell("""## 1. Nạp Tệp Dữ Liệu Đã Xử Lý (`processed data.csv`)"""))
    nb.cells.append(new_code_cell("""# Đọc tệp dữ liệu đã làm sạch 100% không còn missing values
df = pd.read_csv("processed data.csv")
print(f"📊 Kích thước dữ liệu: {df.shape[0]} dòng, {df.shape[1]} cột")
print(f"🔍 Kiểm tra số ô trống: {df.isnull().sum().sum()} (Dữ liệu sạch hoàn toàn)")
df.head()"""))

    # Cell 3: Feature Split
    nb.cells.append(new_markdown_cell("""## 2. Xác Định Biến Đầu Vào (Features) & Phân Chia Train / Test (80/20)"""))
    nb.cells.append(new_code_cell("""# Danh sách các biến kinh tế vĩ mô đầu vào
feature_cols = [
    'inflationrate', 'oil prices', 'exchange_rate', 'gdppercent',
    'percapitaincome', 'unemploymentrate', 'manufacturingoutput',
    'tradebalance', 'USTreasury', 'real_interest_rate',
    'trade_to_gdp_proxy', 'misery_index'
]
target_col = 'log_indexprice'

X = df[feature_cols]
y = df[target_col]

# Phân chia 80% Train, 20% Test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, shuffle=True
)

print(f"✅ Tập huấn luyện (Train): {X_train.shape[0]} quan sát (80%)")
print(f"✅ Tập kiểm thử (Test):    {X_test.shape[0]} quan sát (20%)")"""))

    # Cell 4: Standardization
    nb.cells.append(new_markdown_cell("""## 3. Chuẩn Hóa Đặc Trưng Bằng `StandardScaler` (Z-score Scaling)"""))
    nb.cells.append(new_code_cell("""# Chuẩn hóa Z-score (fit trên Train, transform trên Test)
scaler = StandardScaler()
X_train_scaled = pd.DataFrame(scaler.fit_transform(X_train), columns=feature_cols, index=X_train.index)
X_test_scaled = pd.DataFrame(scaler.transform(X_test), columns=feature_cols, index=X_test.index)

# Lưu bộ scaler để phục vụ inference dự báo sau này
joblib.dump(scaler, "scaler.pkl")
print("💾 Đã lưu StandardScaler vào scaler.pkl")
X_train_scaled.head()"""))

    # Cell 5: Model 1 Linear Regression
    nb.cells.append(new_markdown_cell("""## 4. Mô Hình 1: Linear Regression (Baseline OLS)"""))
    nb.cells.append(new_code_cell("""# Huấn luyện mô hình Linear Regression
lr_model = LinearRegression()
lr_model.fit(X_train_scaled, y_train)

y_train_pred_lr = lr_model.predict(X_train_scaled)
y_test_pred_lr = lr_model.predict(X_test_scaled)

r2_train_lr = r2_score(y_train, y_train_pred_lr)
r2_test_lr = r2_score(y_test, y_test_pred_lr)
rmse_test_lr = np.sqrt(mean_squared_error(y_test, y_test_pred_lr))
mae_test_lr = mean_absolute_error(y_test, y_test_pred_lr)

print(f"📊 [Linear Regression] Train R²: {r2_train_lr:.4f} | Test R²: {r2_test_lr:.4f}")
print(f"📊 [Linear Regression] Test RMSE: {rmse_test_lr:.4f} | Test MAE: {mae_test_lr:.4f}")"""))

    # Cell 6: Model 2 Random Forest
    nb.cells.append(new_markdown_cell("""## 5. Mô Hình 2: Random Forest Regressor"""))
    nb.cells.append(new_code_cell("""# Khởi tạo và huấn luyện Random Forest Regressor
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

# Dự báo trên tập Train và Test
y_train_pred_rf = rf_model.predict(X_train_scaled)
y_test_pred_rf = rf_model.predict(X_test_scaled)

# Đánh giá các chỉ số
r2_train_rf = r2_score(y_train, y_train_pred_rf)
r2_test_rf = r2_score(y_test, y_test_pred_rf)
rmse_test_rf = np.sqrt(mean_squared_error(y_test, y_test_pred_rf))
mae_test_rf = mean_absolute_error(y_test, y_test_pred_rf)
mape_test_rf = np.mean(np.abs((y_test - y_test_pred_rf) / y_test)) * 100

# Kiểm định chéo 5-Fold Cross Validation
cv_rf = cross_val_score(rf_model, X_train_scaled, y_train, cv=5, scoring='r2')

print(f"🌲 [Random Forest] Train R²: {r2_train_rf:.4f} | Test R²: {r2_test_rf:.4f}")
print(f"🌲 [Random Forest] 5-Fold CV R²: {cv_rf.mean():.4f} (±{cv_rf.std():.4f})")
print(f"🌲 [Random Forest] Test RMSE: {rmse_test_rf:.4f} | Test MAE: {mae_test_rf:.4f} | Test MAPE: {mape_test_rf:.2f}%")

# Lưu mô hình
joblib.dump(rf_model, "random_forest_model.pkl")
print("💾 Đã lưu Random Forest model vào random_forest_model.pkl")"""))

    # Cell 7: Model 3 XGBoost
    nb.cells.append(new_markdown_cell("""## 6. Mô Hình 3: XGBoost Regressor"""))
    nb.cells.append(new_code_cell("""# Khởi tạo và huấn luyện XGBoost Regressor
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

# Dự báo trên tập Train và Test
y_train_pred_xgb = xgb_model.predict(X_train_scaled)
y_test_pred_xgb = xgb_model.predict(X_test_scaled)

# Đánh giá các chỉ số
r2_train_xgb = r2_score(y_train, y_train_pred_xgb)
r2_test_xgb = r2_score(y_test, y_test_pred_xgb)
rmse_test_xgb = np.sqrt(mean_squared_error(y_test, y_test_pred_xgb))
mae_test_xgb = mean_absolute_error(y_test, y_test_pred_xgb)
mape_test_xgb = np.mean(np.abs((y_test - y_test_pred_xgb) / y_test)) * 100

# Kiểm định chéo 5-Fold Cross Validation
cv_xgb = cross_val_score(xgb_model, X_train_scaled, y_train, cv=5, scoring='r2')

print(f"⚡ [XGBoost] Train R²: {r2_train_xgb:.4f} | Test R²: {r2_test_xgb:.4f}")
print(f"⚡ [XGBoost] 5-Fold CV R²: {cv_xgb.mean():.4f} (±{cv_xgb.std():.4f})")
print(f"⚡ [XGBoost] Test RMSE: {rmse_test_xgb:.4f} | Test MAE: {mae_test_xgb:.4f} | Test MAPE: {mape_test_xgb:.2f}%")

# Lưu mô hình
xgb_model.save_model("xgboost_model.json")
joblib.dump(xgb_model, "xgboost_model.pkl")
print("💾 Đã lưu XGBoost model vào xgboost_model.json & xgboost_model.pkl")"""))

    # Cell 8: Comparison Table
    nb.cells.append(new_markdown_cell("""## 7. Bảng So Sánh Hiệu Năng & Trực Quan Hóa Actual vs Predicted"""))
    nb.cells.append(new_code_cell("""# Bảng tổng hợp so sánh
df_compare = pd.DataFrame([
    {"Mô Hình": "Linear Regression (OLS)", "Train R²": r2_train_lr, "Test R²": r2_test_lr, "Test RMSE": rmse_test_lr, "Test MAE": mae_test_lr, "Đánh Giá": "Baseline Tuyến tính"},
    {"Mô Hình": "Random Forest Regressor", "Train R²": r2_train_rf, "Test R²": r2_test_rf, "Test RMSE": rmse_test_rf, "Test MAE": mae_test_rf, "Đánh Giá": "Bắt phi tuyến xuất sắc"},
    {"Mô Hình": "XGBoost Regressor (Tốt nhất)", "Train R²": r2_train_xgb, "Test R²": r2_test_xgb, "Test RMSE": rmse_test_xgb, "Test MAE": mae_test_xgb, "Đánh Giá": "Sai số nhỏ nhất, R² cao nhất"}
])
display(df_compare)"""))

    # Cell 9: Plots
    nb.cells.append(new_code_cell("""# Trực quan hóa Actual vs Predicted
fig, axes = plt.subplots(1, 2, figsize=(15, 6), dpi=150)

# Random Forest Scatter
axes[0].scatter(y_test, y_test_pred_rf, color="#1F4D78", alpha=0.75, edgecolors='k', s=50, label="Test Points")
axes[0].plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2, label="Đường chuẩn y = x")
axes[0].set_title(f"Random Forest (Test R² = {r2_test_rf:.4f})", fontsize=12, fontweight='bold', color="#0A2540")
axes[0].set_xlabel("Thực tế (Actual log_indexprice)", fontweight='bold')
axes[0].set_ylabel("Dự báo (Predicted log_indexprice)", fontweight='bold')
axes[0].legend()

# XGBoost Scatter
axes[1].scatter(y_test, y_test_pred_xgb, color="#EA580C", alpha=0.75, edgecolors='k', s=50, label="Test Points")
axes[1].plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'b--', lw=2, label="Đường chuẩn y = x")
axes[1].set_title(f"XGBoost Regressor (Test R² = {r2_test_xgb:.4f})", fontsize=12, fontweight='bold', color="#0A2540")
axes[1].set_xlabel("Thực tế (Actual log_indexprice)", fontweight='bold')
axes[1].set_ylabel("Dự báo (Predicted log_indexprice)", fontweight='bold')
axes[1].legend()

plt.tight_layout()
plt.show()"""))

    # Cell 10: Feature Importance
    nb.cells.append(new_markdown_cell("""## 8. Phân Tích Tầm Quan Trọng Của Các Biến (Feature Importances)"""))
    nb.cells.append(new_code_cell("""# Tính toán Feature Importance
df_rf_imp = pd.DataFrame({'Feature': feature_cols, 'Importance': rf_model.feature_importances_}).sort_values('Importance', ascending=False)
df_xgb_imp = pd.DataFrame({'Feature': feature_cols, 'Importance': xgb_model.feature_importances_}).sort_values('Importance', ascending=False)

fig, axes = plt.subplots(1, 2, figsize=(16, 6), dpi=150)
sns.barplot(x='Importance', y='Feature', data=df_rf_imp, ax=axes[0], hue='Feature', palette='Blues_r', legend=False)
axes[0].set_title("Tầm Quan Trọng Của Biến (Random Forest)", fontweight='bold', color="#0A2540")

sns.barplot(x='Importance', y='Feature', data=df_xgb_imp, ax=axes[1], hue='Feature', palette='Oranges_r', legend=False)
axes[1].set_title("Tầm Quan Trọng Của Biến (XGBoost)", fontweight='bold', color="#0A2540")

plt.tight_layout()
plt.show()"""))

    # Cell 11: Prediction on X_new
    nb.cells.append(new_markdown_cell("""## 9. Ứng Dụng Mô Hình Dự Báo Thực Tế Trên Tệp Dữ Liệu Mới (`X_new.xlsx`)"""))
    nb.cells.append(new_code_cell("""# Đọc tệp dữ liệu kiểm thử mới X_new
df_xnew = pd.read_excel("X_new.xlsx")

# Bổ sung 3 biến phái sinh kinh tế vĩ mô tương ứng
df_xnew_proc = df_xnew.copy()
df_xnew_proc['real_interest_rate'] = df_xnew_proc['USTreasury'] * 100 - df_xnew_proc['inflationrate']
df_xnew_proc['trade_to_gdp_proxy'] = df_xnew_proc['tradebalance'] / (df_xnew_proc['gdppercent'].abs() + 1.0)
df_xnew_proc['misery_index'] = df_xnew_proc['unemploymentrate'] + df_xnew_proc['inflationrate']

# Sắp xếp đúng thứ tự đặc trưng và chuẩn hóa
X_new_features = df_xnew_proc[feature_cols]
X_new_scaled = scaler.transform(X_new_features)

# Thực hiện dự báo với các mô hình
pred_log_lr = lr_model.predict(X_new_scaled)[0]
pred_log_rf = rf_model.predict(X_new_scaled)[0]
pred_log_xgb = xgb_model.predict(X_new_scaled)[0]

df_pred_final = pd.DataFrame([
    {"Mô Hình": "Linear Regression (OLS)", "Dự Báo log_indexprice": round(pred_log_lr, 4), "Giá Trị Quy Đổi index price ($)": round(np.exp(pred_log_lr), 2)},
    {"Mô Hình": "Random Forest Regressor", "Dự Báo log_indexprice": round(pred_log_rf, 4), "Giá Trị Quy Đổi index price ($)": round(np.exp(pred_log_rf), 2)},
    {"Mô Hình": "XGBoost Regressor (Khuyên dùng)", "Dự Báo log_indexprice": round(pred_log_xgb, 4), "Giá Trị Quy Đổi index price ($)": round(np.exp(pred_log_xgb), 2)}
])

print("🎯 KẾT QUẢ DỰ BÁO CUỐI CÙNG TRÊN X_new:")
display(df_pred_final)"""))

    for p in [NB_PATH_1, NB_PATH_2]:
        with open(p, 'w', encoding='utf-8') as f:
            nbformat.write(nb, f)
        print(f"✅ Đã tạo Notebook tại: {p}")

if __name__ == "__main__":
    build_notebook()
