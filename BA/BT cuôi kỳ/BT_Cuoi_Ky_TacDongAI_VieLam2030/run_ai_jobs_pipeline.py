"""
Pipeline tổng hợp: Tác động của AI đến Việc làm năm 2030
Học phần: Phân tích Kinh doanh - Học viện Ngân hàng
Sinh viên thực hiện: Đỗ Văn Đạt

Cấu trúc pipeline (mô phỏng theo bố cục bài tập giữa kỳ BankChurners):
  B1. Đọc & khám phá dữ liệu thô (Load and show first rows)
  B2. Tiền xử lý dữ liệu (kiểm tra thiếu/trùng/ngoại lai, mã hoá biến định tính,
      feature engineering)
  B3. Phân tích khám phá dữ liệu - EDA (≈12 biểu đồ)
  B4. Phân cụm K-Means trên hồ sơ kỹ năng (skill profile clustering)
  B5. Mô hình phân loại nhóm rủi ro tự động hoá (Risk_Category) - so sánh 3 mô hình
  B6. Mô hình hồi quy xác suất tự động hoá (Automation_Probability_2030)
  B7. Xuất dữ liệu sạch/đã gắn cụm + toàn bộ hình + pipeline_summary.json

Tham khảo phong cách trình bày (Load and show first rows, cấu trúc notebook
tiền xử lý -> EDA -> mô hình hoá) từ:
https://www.kaggle.com/code/denvermagtibay/predicting-uber-ride-cancellations
"""

import json
import warnings
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import (
    ConfusionMatrixDisplay,
    accuracy_score,
    f1_score,
    mean_absolute_error,
    precision_score,
    r2_score,
    recall_score,
    roc_auc_score,
    roc_curve,
    silhouette_score,
)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from xgboost import XGBClassifier, XGBRegressor

warnings.filterwarnings("ignore")

RANDOM_STATE = 42
BASE_DIR = Path(__file__).resolve().parent
FIG_DIR = BASE_DIR / "figures"
FIG_DIR.mkdir(exist_ok=True)

# ---------------------------------------------------------------------------
# Cấu hình hiển thị biểu đồ theo màu HVNH (cam-navy) cho đồng bộ với slide/docx
# ---------------------------------------------------------------------------
HVNH_NAVY = "#1F3864"
HVNH_ORANGE = "#ED7D31"
HVNH_BLUE = "#2E5496"
PALETTE_RISK = {"Low": "#2E7D32", "Medium": "#ED7D31", "High": "#C0392B"}
sns.set_theme(style="whitegrid", font_scale=1.0)
plt.rcParams["figure.dpi"] = 140
plt.rcParams["savefig.dpi"] = 200
plt.rcParams["font.family"] = "DejaVu Sans"  # hỗ trợ tiếng Việt có dấu

SKILL_COLS = [f"Skill_{i}" for i in range(1, 11)]
RISK_ORDER = ["Low", "Medium", "High"]

summary = {}

# ===========================================================================
# BƯỚC 1 — ĐỌC & KHÁM PHÁ DỮ LIỆU THÔ
# ===========================================================================
print("=" * 80)
print("BƯỚC 1. ĐỌC & KHÁM PHÁ DỮ LIỆU THÔ (Load and show first rows)")
print("=" * 80)

raw_path = BASE_DIR / "AI_ViecLam2030_Raw.csv"
df_raw = pd.read_csv(raw_path)
print("Kích thước dữ liệu thô:", df_raw.shape)
print(df_raw.head())
print(df_raw.dtypes)

summary["raw_shape"] = list(df_raw.shape)
summary["raw_columns"] = list(df_raw.columns)

# ===========================================================================
# BƯỚC 2 — TIỀN XỬ LÝ DỮ LIỆU
# ===========================================================================
print("\n" + "=" * 80)
print("BƯỚC 2. TIỀN XỬ LÝ DỮ LIỆU")
print("=" * 80)

df = df_raw.copy()

# 2.1. Dữ liệu thiếu
missing = df.isnull().sum()
missing_pct = (missing / len(df) * 100).round(2)
missing_report = missing[missing > 0]
print("Số ô thiếu theo cột (0 nếu dữ liệu đã sạch từ nguồn):")
print(missing_report if len(missing_report) else "Không có ô nào bị thiếu.")
summary["n_missing_cells_total"] = int(missing.sum())

# 2.2. Dữ liệu trùng lặp
n_dup = int(df.duplicated().sum())
df = df.drop_duplicates().reset_index(drop=True)
print(f"Số dòng trùng lặp phát hiện & loại bỏ: {n_dup}")
summary["n_duplicates_removed"] = n_dup

# 2.3. Kiểm tra miền giá trị hợp lệ (business rule validation)
# Các biến chỉ số (Index/Factor/Probability) và Skill_1..10 phải nằm trong [0, 1]
# (riêng Tech_Growth_Factor có thể > 1 vì là hệ số tăng trưởng, không phải xác suất)
bounded_0_1 = ["AI_Exposure_Index", "Automation_Probability_2030"] + SKILL_COLS
invalid_rows = pd.Series(False, index=df.index)
for col in bounded_0_1:
    invalid_rows |= ~df[col].between(0, 1)
n_invalid = int(invalid_rows.sum())
df = df.loc[~invalid_rows].reset_index(drop=True)
print(f"Số dòng vi phạm miền giá trị [0,1] của chỉ số bị loại: {n_invalid}")
summary["n_invalid_range_rows_removed"] = n_invalid

# 2.4. Ngoại lai (IQR) trên Average_Salary — chỉ ghi nhận, KHÔNG xoá (dữ liệu lương
# thực tế có thể trải dài theo ngành nghề, xoá sẽ làm mất thông tin nghiệp vụ)
q1, q3 = df["Average_Salary"].quantile([0.25, 0.75])
iqr = q3 - q1
lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
n_outliers_salary = int(((df["Average_Salary"] < lower) | (df["Average_Salary"] > upper)).sum())
print(f"Ngoại lai Average_Salary (quy tắc IQR): Q1={q1:.0f}, Q3={q3:.0f}, "
      f"cận dưới={lower:.0f}, cận trên={upper:.0f}, số hồ sơ ngoại lai={n_outliers_salary}")
summary["salary_iqr"] = {
    "Q1": float(q1), "Q3": float(q3), "IQR": float(iqr),
    "lower_bound": float(lower), "upper_bound": float(upper),
    "n_outliers": n_outliers_salary,
}

# 2.5. Kiểm tra tính nhất quán Risk_Category so với Automation_Probability_2030
# (đây là phát hiện quan trọng: Risk_Category là biến PHÁI SINH trực tiếp từ
#  Automation_Probability_2030 theo ngưỡng cố định -> phải loại bỏ biến này khỏi
#  tập đặc trưng khi huấn luyện mô hình phân loại Risk_Category để tránh rò rỉ dữ liệu)
risk_bins = df.groupby("Risk_Category")["Automation_Probability_2030"].agg(["min", "max", "count"])
print("\nNgưỡng Automation_Probability_2030 theo từng Risk_Category (kiểm tra rò rỉ dữ liệu):")
print(risk_bins)
summary["risk_category_thresholds"] = risk_bins.to_dict(orient="index")

# 2.6. Feature engineering
df["Skill_Diversity_Score"] = df[SKILL_COLS].mean(axis=1).round(4)
df["Skill_Std"] = df[SKILL_COLS].std(axis=1).round(4)
df["High_Value_Skill_Count"] = (df[SKILL_COLS] > 0.7).sum(axis=1)
df["Experience_Group"] = pd.cut(
    df["Years_Experience"], bins=[-1, 5, 10, 20, 100],
    labels=["0-5 năm", "6-10 năm", "11-20 năm", "Trên 20 năm"],
)
df["Salary_per_YearExp"] = (df["Average_Salary"] / df["Years_Experience"].replace(0, np.nan)).round(2)
df["Salary_per_YearExp"] = df["Salary_per_YearExp"].fillna(df["Average_Salary"])
df["Human_Edge_Score"] = ((1 - df["AI_Exposure_Index"]) * 0.5 + df["Skill_Diversity_Score"] * 0.5).round(4)
edu_order = {"High School": 0, "Bachelor's": 1, "Master's": 2, "PhD": 3}
df["Education_Level_Encoded"] = df["Education_Level"].map(edu_order)

print("\nĐã tạo 6 biến mới:",
      "Skill_Diversity_Score, Skill_Std, High_Value_Skill_Count,",
      "Experience_Group, Salary_per_YearExp, Human_Edge_Score, Education_Level_Encoded")

summary["clean_shape"] = list(df.shape)
summary["n_engineered_features"] = 7

cleaned_path = BASE_DIR / "AI_ViecLam2030_Cleaned.csv"
df.to_csv(cleaned_path, index=False, encoding="utf-8-sig")
print(f"\nĐã lưu dữ liệu sạch: {cleaned_path.name} — {df.shape[0]} dòng x {df.shape[1]} cột")

# ===========================================================================
# BƯỚC 3 — PHÂN TÍCH KHÁM PHÁ DỮ LIỆU (EDA)
# ===========================================================================
print("\n" + "=" * 80)
print("BƯỚC 3. PHÂN TÍCH KHÁM PHÁ DỮ LIỆU (EDA)")
print("=" * 80)

# Fig 01 — Phân bố nhóm rủi ro tự động hoá
fig, ax = plt.subplots(figsize=(7, 5))
order = df["Risk_Category"].value_counts().reindex(RISK_ORDER)
bars = ax.bar(order.index, order.values, color=[PALETTE_RISK[c] for c in order.index])
for b, v in zip(bars, order.values):
    ax.text(b.get_x() + b.get_width() / 2, v + 25, f"{v}\n({v/len(df)*100:.1f}%)",
            ha="center", fontsize=10, fontweight="bold")
ax.set_ylim(0, order.values.max() * 1.18)
ax.set_title("Phân bố số lượng nghề nghiệp theo Nhóm rủi ro tự động hoá 2030",
             fontweight="bold", pad=14)
ax.set_xlabel("Nhóm rủi ro (Risk_Category)")
ax.set_ylabel("Số lượng nghề nghiệp")
plt.tight_layout()
plt.savefig(FIG_DIR / "01_risk_category_distribution.png")
plt.close()

# Fig 02 — Phân bố xác suất tự động hoá 2030
fig, ax = plt.subplots(figsize=(7, 5))
sns.histplot(df["Automation_Probability_2030"], bins=30, kde=True, color=HVNH_BLUE, ax=ax)
ax.axvline(df["Automation_Probability_2030"].mean(), color=HVNH_ORANGE, ls="--",
           label=f"Trung bình = {df['Automation_Probability_2030'].mean():.2f}")
ax.set_title("Phân bố Xác suất tự động hoá công việc vào năm 2030", fontweight="bold")
ax.set_xlabel("Automation_Probability_2030")
ax.legend()
plt.tight_layout()
plt.savefig(FIG_DIR / "02_automation_probability_distribution.png")
plt.close()

# Fig 03 — Lương trung bình theo nhóm rủi ro (boxplot)
fig, ax = plt.subplots(figsize=(7, 5))
sns.boxplot(data=df, x="Risk_Category", y="Average_Salary", order=RISK_ORDER,
            palette=PALETTE_RISK, ax=ax)
ax.set_title("Mức lương trung bình theo Nhóm rủi ro tự động hoá", fontweight="bold")
ax.set_xlabel("Nhóm rủi ro")
ax.set_ylabel("Lương trung bình (USD/năm)")
plt.tight_layout()
plt.savefig(FIG_DIR / "03_salary_by_risk_category.png")
plt.close()

# Fig 04 — Trình độ học vấn theo nhóm rủi ro (stacked % bar)
fig, ax = plt.subplots(figsize=(8, 5))
ct = pd.crosstab(df["Education_Level"], df["Risk_Category"], normalize="index")[RISK_ORDER] * 100
ct = ct.reindex(["High School", "Bachelor's", "Master's", "PhD"])
ct.plot(kind="bar", stacked=True, color=[PALETTE_RISK[c] for c in RISK_ORDER], ax=ax)
ax.set_title("Cơ cấu Nhóm rủi ro theo Trình độ học vấn (%)", fontweight="bold")
ax.set_xlabel("Trình độ học vấn")
ax.set_ylabel("Tỷ lệ (%)")
ax.legend(title="Risk_Category")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(FIG_DIR / "04_education_vs_risk.png")
plt.close()

# Fig 05 — AI_Exposure_Index vs Automation_Probability_2030 (scatter, tô theo risk)
fig, ax = plt.subplots(figsize=(7.5, 5.5))
for cat in RISK_ORDER:
    sub = df[df["Risk_Category"] == cat]
    ax.scatter(sub["AI_Exposure_Index"], sub["Automation_Probability_2030"],
               s=14, alpha=0.55, color=PALETTE_RISK[cat], label=cat)
ax.set_title("Chỉ số Phơi nhiễm AI so với Xác suất tự động hoá 2030", fontweight="bold")
ax.set_xlabel("AI_Exposure_Index")
ax.set_ylabel("Automation_Probability_2030")
ax.legend(title="Risk_Category")
plt.tight_layout()
plt.savefig(FIG_DIR / "05_ai_exposure_vs_automation.png")
plt.close()

# Fig 06 — Ma trận tương quan
corr_cols = ["Average_Salary", "Years_Experience", "AI_Exposure_Index", "Tech_Growth_Factor",
             "Automation_Probability_2030", "Skill_Diversity_Score", "Human_Edge_Score"]
fig, ax = plt.subplots(figsize=(8, 6.5))
sns.heatmap(df[corr_cols].corr(), annot=True, fmt=".2f", cmap="RdBu_r", center=0,
            vmin=-1, vmax=1, ax=ax, cbar_kws={"label": "Hệ số tương quan"})
ax.set_title("Ma trận tương quan giữa các biến định lượng chính", fontweight="bold")
plt.tight_layout()
plt.savefig(FIG_DIR / "06_correlation_heatmap.png")
plt.close()

# Fig 07 — Kinh nghiệm làm việc vs Xác suất tự động hoá
fig, ax = plt.subplots(figsize=(7.5, 5.5))
sns.regplot(data=df, x="Years_Experience", y="Automation_Probability_2030",
            scatter_kws={"alpha": 0.25, "s": 12, "color": HVNH_BLUE},
            line_kws={"color": HVNH_ORANGE, "lw": 2}, ax=ax)
ax.set_title("Số năm kinh nghiệm và Xác suất tự động hoá 2030", fontweight="bold")
plt.tight_layout()
plt.savefig(FIG_DIR / "07_experience_vs_automation.png")
plt.close()

# Fig 08 — Xếp hạng đầy đủ 20 nghề theo xác suất tự động hoá TB (bằng chứng chính:
# phát hiện cấu trúc "3 tầng nghề nghiệp" — xem kiểm định eta^2 ngay bên dưới)
job_stats = df.groupby("Job_Title")["Automation_Probability_2030"].agg(["mean", "std", "count"]).sort_values("mean")


def _tier_color(v):
    if v < 0.30:
        return PALETTE_RISK["Low"]
    if v > 0.70:
        return PALETTE_RISK["High"]
    return PALETTE_RISK["Medium"]


colors_tier = [_tier_color(v) for v in job_stats["mean"]]
fig, ax = plt.subplots(figsize=(9, 8.5))
ax.barh(job_stats.index, job_stats["mean"], xerr=job_stats["std"], color=colors_tier,
        error_kw={"ecolor": "#555555", "elinewidth": 1, "capsize": 2})
ax.set_title("Xác suất tự động hoá TB theo Nghề nghiệp (20 nghề, ±1 độ lệch chuẩn)",
              fontweight="bold")
ax.set_xlabel("Automation_Probability_2030 (trung bình)")
ax.axvline(0.30, color="grey", ls=":", lw=1)
ax.axvline(0.70, color="grey", ls=":", lw=1)
plt.tight_layout()
plt.savefig(FIG_DIR / "08_jobtitle_automation_ranked.png")
plt.close()

# Kiểm định mức độ giải thích của Job_Title đối với Automation_Probability_2030 (eta^2 = SSB/SST)
overall_mean = df["Automation_Probability_2030"].mean()
ss_between = float(((job_stats["mean"] - overall_mean) ** 2 * job_stats["count"]).sum())
ss_total = float(((df["Automation_Probability_2030"] - overall_mean) ** 2).sum())
eta_squared_job = ss_between / ss_total
print(f"\nKiểm định eta^2: Job_Title giải thích {eta_squared_job*100:.1f}% phương sai của "
      f"Automation_Probability_2030 (SSB/SST) -> đây là biến quyết định chính, mạnh hơn hẳn "
      f"mọi đặc trưng cá nhân (kỹ năng/kinh nghiệm/học vấn/lương).")
summary["job_title_eta_squared"] = round(eta_squared_job, 4)
summary["job_risk_lowest10"] = job_stats["mean"].head(10).round(4).to_dict()
summary["job_risk_highest10"] = job_stats["mean"].tail(10).round(4).to_dict()

# Fig 09 — Tech_Growth_Factor theo nhóm rủi ro (violin)
fig, ax = plt.subplots(figsize=(7, 5))
sns.violinplot(data=df, x="Risk_Category", y="Tech_Growth_Factor", order=RISK_ORDER,
               palette=PALETTE_RISK, ax=ax)
ax.set_title("Hệ số tăng trưởng công nghệ (Tech_Growth_Factor) theo Nhóm rủi ro", fontweight="bold")
plt.tight_layout()
plt.savefig(FIG_DIR / "09_tech_growth_by_risk.png")
plt.close()

# Fig 10 — Heatmap kỹ năng trung bình theo nhóm rủi ro
skill_by_risk = df.groupby("Risk_Category")[SKILL_COLS].mean().reindex(RISK_ORDER)
fig, ax = plt.subplots(figsize=(10, 4))
sns.heatmap(skill_by_risk, annot=True, fmt=".2f", cmap="YlOrRd", ax=ax,
            cbar_kws={"label": "Điểm kỹ năng TB"})
ax.set_title("Điểm trung bình 10 nhóm kỹ năng (Skill_1..10) theo Nhóm rủi ro", fontweight="bold")
ax.set_xlabel("Nhóm kỹ năng")
ax.set_ylabel("Nhóm rủi ro")
plt.tight_layout()
plt.savefig(FIG_DIR / "10_skills_heatmap_by_risk.png")
plt.close()

# Fig 11 — Human_Edge_Score theo nhóm rủi ro
fig, ax = plt.subplots(figsize=(7, 5))
sns.boxplot(data=df, x="Risk_Category", y="Human_Edge_Score", order=RISK_ORDER,
            palette=PALETTE_RISK, ax=ax)
ax.set_title("Chỉ số Lợi thế con người (Human_Edge_Score) theo Nhóm rủi ro", fontweight="bold")
plt.tight_layout()
plt.savefig(FIG_DIR / "11_human_edge_score_by_risk.png")
plt.close()

print(f"Đã xuất 11 biểu đồ EDA vào thư mục: {FIG_DIR.relative_to(BASE_DIR)}/")

# ===========================================================================
# BƯỚC 4 — PHÂN CỤM K-MEANS TRÊN HỒ SƠ KỸ NĂNG
# ===========================================================================
print("\n" + "=" * 80)
print("BƯỚC 4. PHÂN CỤM K-MEANS (Skill Profile Clustering)")
print("=" * 80)

cluster_feats = SKILL_COLS + ["AI_Exposure_Index", "Tech_Growth_Factor"]
X_cluster = df[cluster_feats].copy()
scaler_c = StandardScaler()
X_cluster_scaled = scaler_c.fit_transform(X_cluster)

inertias, silhouettes = [], []
k_range = range(2, 9)
for k in k_range:
    km = KMeans(n_clusters=k, random_state=RANDOM_STATE, n_init=10)
    labels_k = km.fit_predict(X_cluster_scaled)
    inertias.append(km.inertia_)
    silhouettes.append(silhouette_score(X_cluster_scaled, labels_k))

fig, axes = plt.subplots(1, 2, figsize=(13, 5))
axes[0].plot(list(k_range), inertias, marker="o", color=HVNH_BLUE)
axes[0].set_title("Phương pháp Elbow — Inertia theo số cụm k", fontweight="bold")
axes[0].set_xlabel("Số cụm (k)")
axes[0].set_ylabel("Inertia (WCSS)")
axes[1].plot(list(k_range), silhouettes, marker="o", color=HVNH_ORANGE)
axes[1].set_title("Chỉ số Silhouette theo số cụm k", fontweight="bold")
axes[1].set_xlabel("Số cụm (k)")
axes[1].set_ylabel("Silhouette Score")
plt.tight_layout()
plt.savefig(FIG_DIR / "12_kmeans_elbow_silhouette.png")
plt.close()

sil_by_k = {k: round(s, 4) for k, s in zip(k_range, silhouettes)}
print("Silhouette Score theo từng k:", sil_by_k)
statistical_best_k = int(list(k_range)[int(np.argmax(silhouettes))])
print(f"k có Silhouette cao nhất (thống kê thuần tuý): k = {statistical_best_k} "
      f"(Silhouette = {max(silhouettes):.4f})")

# LƯU Ý PHƯƠNG PHÁP LUẬN: mọi giá trị Silhouette đều xấp xỉ 0.05-0.06 (gần 0), tức là
# CÁC CỤM KHÔNG TÁCH BIỆT RÕ RÀNG ở bất kỳ k nào — phù hợp với bản chất dữ liệu tổng hợp
# (các cột Skill_1..10 được sinh ngẫu nhiên độc lập, không có cấu trúc phân nhóm tự nhiên).
# Nhóm k=4 dưới đây được chọn vì mục đích DIỄN GIẢI NGHIỆP VỤ (phân khúc thành 4 hồ sơ dễ
# truyền thông trong báo cáo/slide), KHÔNG phải vì dữ liệu có cấu trúc phân cụm mạnh ở k=4.
# Đây là điểm cần nêu rõ trong báo cáo để tránh diễn giải sai (overclaim) mức độ tách biệt cụm.
optimal_k = 4
print(f"Số cụm sử dụng cho phân tích nghiệp vụ (business-driven, không phải statistical-optimal): "
      f"k = {optimal_k} (Silhouette = {sil_by_k[optimal_k]:.4f} — mức RẤT YẾU, gần 0)")
summary["statistical_best_k"] = statistical_best_k
summary["silhouette_by_k"] = sil_by_k
summary["clustering_caveat"] = (
    "Silhouette Score dao động chỉ trong khoảng 0.055-0.063 ở mọi k (2-8), gần 0, cho thấy "
    "các cụm không tách biệt rõ ràng do các biến kỹ năng (Skill_1..10) trong bộ dữ liệu tổng "
    "hợp được sinh ngẫu nhiên độc lập. k=4 được chọn cho mục đích diễn giải nghiệp vụ, không "
    "phải vì có cấu trúc phân cụm thống kê mạnh."
)

kmeans_final = KMeans(n_clusters=optimal_k, random_state=RANDOM_STATE, n_init=10)
df["Cluster"] = kmeans_final.fit_predict(X_cluster_scaled)
summary["optimal_k"] = optimal_k
summary["silhouette_at_optimal_k"] = float(max(silhouettes))

pca = PCA(n_components=2, random_state=RANDOM_STATE)
pcs = pca.fit_transform(X_cluster_scaled)
fig, ax = plt.subplots(figsize=(8, 6))
palette_cluster = sns.color_palette("tab10", optimal_k)
for c in range(optimal_k):
    mask = df["Cluster"] == c
    ax.scatter(pcs[mask, 0], pcs[mask, 1], s=16, alpha=0.6,
               color=palette_cluster[c], label=f"Cụm {c}")
ax.set_title(f"Trực quan hoá {optimal_k} cụm hồ sơ kỹ năng qua PCA (2 thành phần)", fontweight="bold")
ax.set_xlabel(f"PC1 ({pca.explained_variance_ratio_[0]*100:.1f}% phương sai)")
ax.set_ylabel(f"PC2 ({pca.explained_variance_ratio_[1]*100:.1f}% phương sai)")
ax.legend()
plt.tight_layout()
plt.savefig(FIG_DIR / "13_kmeans_clusters_pca.png")
plt.close()

cluster_profile = df.groupby("Cluster").agg(
    So_luong=("Job_Title", "count"),
    XacSuat_TuDongHoa_TB=("Automation_Probability_2030", "mean"),
    AI_Exposure_TB=("AI_Exposure_Index", "mean"),
    Luong_TB=("Average_Salary", "mean"),
    KinhNghiem_TB=("Years_Experience", "mean"),
    KyNang_TB=("Skill_Diversity_Score", "mean"),
).round(3)
print("\nHồ sơ đặc trưng từng cụm:")
print(cluster_profile)

# Đặt tên nghiệp vụ cho từng cụm — xếp hạng theo AI_Exposure_TB (biến có độ phân tán rõ
# nhất giữa 4 cụm) để đặt tên MÔ TẢ chứ không suy diễn quá mức, vì Silhouette rất yếu
# (xem clustering_caveat) nên đây là 4 PHÂN KHÚC MINH HOẠ, không phải nhóm tách biệt mạnh.
rank_by_exposure = cluster_profile["AI_Exposure_TB"].rank(method="first").astype(int)
descriptive_labels = {
    1: "Phơi nhiễm AI thấp nhất trong 4 cụm (minh hoạ)",
    2: "Phơi nhiễm AI trung bình-thấp (minh hoạ)",
    3: "Phơi nhiễm AI trung bình-cao (minh hoạ)",
    4: "Phơi nhiễm AI cao nhất trong 4 cụm (minh hoạ)",
}
cluster_names = {}
for c in cluster_profile.index:
    r = int(rank_by_exposure.loc[c])
    cluster_names[str(c)] = f"Cụm {c}: {descriptive_labels[r]}"
summary["cluster_names"] = cluster_names
summary["cluster_profile"] = cluster_profile.reset_index().to_dict(orient="records")

clustered_path = BASE_DIR / "AI_ViecLam2030_Clustered.csv"
df.to_csv(clustered_path, index=False, encoding="utf-8-sig")
print(f"Đã lưu dữ liệu đã gắn cụm: {clustered_path.name}")

# ===========================================================================
# BƯỚC 5 — MÔ HÌNH PHÂN LOẠI NHÓM RỦI RO (Risk_Category)
# ===========================================================================
print("\n" + "=" * 80)
print("BƯỚC 5. MÔ HÌNH PHÂN LOẠI NHÓM RỦI RO TỰ ĐỘNG HOÁ (Risk_Category)")
print("=" * 80)
print("Lưu ý quan trọng: KHÔNG đưa Automation_Probability_2030 vào tập đặc trưng")
print("vì Risk_Category được suy ra trực tiếp (rule-based) từ biến này -> rò rỉ dữ liệu.")
print(f"Đưa THÊM Job_Title (one-hot, drop_first) vào tập đặc trưng vì kiểm định eta^2 ở")
print(f"Bước 3 cho thấy nghề nghiệp giải thích {eta_squared_job*100:.1f}% phương sai của rủi ro.")

base_features = ["Average_Salary", "Years_Experience", "Education_Level_Encoded",
                  "AI_Exposure_Index", "Tech_Growth_Factor", "Skill_Diversity_Score",
                  "Skill_Std", "High_Value_Skill_Count", "Human_Edge_Score"] + SKILL_COLS

X = pd.get_dummies(df[base_features + ["Job_Title"]], columns=["Job_Title"], drop_first=True)
clf_features = list(X.columns)
job_title_dummy_cols = [c for c in clf_features if c.startswith("Job_Title_")]
le = LabelEncoder()
le.fit(RISK_ORDER)
y = le.transform(df["Risk_Category"])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=RANDOM_STATE, stratify=y
)
scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)

models = {
    "Logistic Regression": LogisticRegression(max_iter=2000, random_state=RANDOM_STATE),
    "Random Forest": RandomForestClassifier(n_estimators=300, max_depth=10,
                                             random_state=RANDOM_STATE),
    "XGBoost Classifier": XGBClassifier(n_estimators=300, max_depth=5, learning_rate=0.08,
                                         random_state=RANDOM_STATE, eval_metric="mlogloss"),
}

model_metrics = {}
roc_data = {}
fitted_models = {}
for name, model in models.items():
    Xtr = X_train_s if name == "Logistic Regression" else X_train
    Xte = X_test_s if name == "Logistic Regression" else X_test
    model.fit(Xtr, y_train)
    y_pred = model.predict(Xte)
    y_proba = model.predict_proba(Xte)
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred, average="macro")
    rec = recall_score(y_test, y_pred, average="macro")
    f1 = f1_score(y_test, y_pred, average="macro")
    auc = roc_auc_score(y_test, y_proba, multi_class="ovr", average="macro")
    model_metrics[name] = {"Accuracy": float(acc), "Precision_macro": float(prec),
                            "Recall_macro": float(rec), "F1_macro": float(f1),
                            "ROC_AUC_ovr": float(auc)}
    fitted_models[name] = (model, y_pred, y_proba, Xte)
    print(f"{name:22s} | Acc={acc:.4f}  Prec={prec:.4f}  Rec={rec:.4f}  F1={f1:.4f}  AUC={auc:.4f}")

summary["classification_model_metrics"] = model_metrics
best_model_name = max(model_metrics, key=lambda k: model_metrics[k]["F1_macro"])
summary["best_classification_model"] = best_model_name
print(f"\nMô hình phân loại tốt nhất (theo F1-macro): {best_model_name}")

# Fig 14 — So sánh mô hình (bar chart nhiều chỉ số)
metrics_df = pd.DataFrame(model_metrics).T[["Accuracy", "Precision_macro", "Recall_macro",
                                             "F1_macro", "ROC_AUC_ovr"]]
fig, ax = plt.subplots(figsize=(10, 5.5))
metrics_df.plot(kind="bar", ax=ax, color=["#4472C4", "#ED7D31", "#A5A5A5", "#FFC000", "#1F3864"])
ax.set_title("So sánh hiệu suất 3 mô hình phân loại Nhóm rủi ro tự động hoá", fontweight="bold")
ax.set_ylabel("Điểm số")
ax.set_ylim(0, 1.05)
ax.legend(loc="lower right")
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig(FIG_DIR / "14_ml_model_comparison.png")
plt.close()

# Fig 15 — Ma trận nhầm lẫn 3 mô hình
fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))
for ax, (name, (model, y_pred, y_proba, Xte)) in zip(axes, fitted_models.items()):
    ConfusionMatrixDisplay.from_predictions(y_test, y_pred, display_labels=le.classes_,
                                             ax=ax, colorbar=False, cmap="Blues")
    ax.set_title(name, fontsize=11, fontweight="bold")
plt.tight_layout()
plt.savefig(FIG_DIR / "15_confusion_matrices.png")
plt.close()

# Fig 16 — Feature importance, GỘP 19 biến giả Job_Title thành một mục duy nhất
# "Nghề nghiệp (Job_Title, gộp)" để biểu đồ dễ diễn giải nghiệp vụ.
# Dùng CỐ ĐỊNH mô hình cây (XGBoost) cho biểu đồ này thay vì "mô hình tốt nhất theo F1"
# vì Logistic Regression (đôi khi thắng do hoà điểm F1-macro) không có feature_importances_.
importance_model_name = "XGBoost Classifier"
importance_model = fitted_models[importance_model_name][0]
if hasattr(importance_model, "feature_importances_"):
    raw_importances = pd.Series(importance_model.feature_importances_, index=clf_features)
    job_title_total = raw_importances[job_title_dummy_cols].sum()
    other_importances = raw_importances.drop(index=job_title_dummy_cols)
    combined = pd.concat([
        pd.Series({"Nghề nghiệp (Job_Title, gộp 19 biến giả)": job_title_total}),
        other_importances,
    ]).sort_values(ascending=False).head(12)
    fig, ax = plt.subplots(figsize=(10.5, 6.2))
    colors_fi = [HVNH_ORANGE if "Job_Title" in i else HVNH_NAVY for i in combined.index]
    combined.sort_values().plot(kind="barh", color=colors_fi, ax=ax)
    ax.set_title(f"Mức độ quan trọng của biến — {importance_model_name} (Top 12, đã gộp Job_Title)",
                 fontweight="bold", fontsize=13)
    ax.set_xlabel("Feature importance")
    plt.tight_layout()
    plt.savefig(FIG_DIR / "16_feature_importance.png")
    plt.close()
    summary["top_features_classification"] = combined.round(4).to_dict()
    summary["job_title_total_importance"] = round(float(job_title_total), 4)

# ===========================================================================
# BƯỚC 6 — MÔ HÌNH HỒI QUY XÁC SUẤT TỰ ĐỘNG HOÁ (kiểm chứng độc lập)
# ===========================================================================
print("\n" + "=" * 80)
print("BƯỚC 6. MÔ HÌNH HỒI QUY XÁC SUẤT TỰ ĐỘNG HOÁ 2030 (đối chiếu độc lập)")
print("=" * 80)

reg_features = clf_features  # cùng tập đặc trưng (đã gồm Job_Title one-hot), khác biến mục tiêu (liên tục)
Xr = X[reg_features].copy()  # tái sử dụng ma trận X đã one-hot Job_Title ở Bước 5
yr = df["Automation_Probability_2030"].values

Xr_train, Xr_test, yr_train, yr_test = train_test_split(
    Xr, yr, test_size=0.25, random_state=RANDOM_STATE
)
reg_models = {
    "Linear Regression": LinearRegression(),
    "Random Forest Regressor": RandomForestRegressor(n_estimators=300, max_depth=10,
                                                       random_state=RANDOM_STATE),
    "XGBoost Regressor": XGBRegressor(n_estimators=300, max_depth=5, learning_rate=0.08,
                                       random_state=RANDOM_STATE),
}
reg_metrics = {}
reg_preds = {}
for name, model in reg_models.items():
    model.fit(Xr_train, yr_train)
    pred = model.predict(Xr_test)
    reg_metrics[name] = {
        "R2": float(r2_score(yr_test, pred)),
        "MAE": float(mean_absolute_error(yr_test, pred)),
        "RMSE": float(np.sqrt(np.mean((yr_test - pred) ** 2))),
    }
    reg_preds[name] = pred
    print(f"{name:24s} | R2={reg_metrics[name]['R2']:.4f}  MAE={reg_metrics[name]['MAE']:.4f}  "
          f"RMSE={reg_metrics[name]['RMSE']:.4f}")

summary["regression_model_metrics"] = reg_metrics
best_reg_name = max(reg_metrics, key=lambda k: reg_metrics[k]["R2"])
summary["best_regression_model"] = best_reg_name

# Fig 17 — Predicted vs Actual của mô hình hồi quy tốt nhất
fig, ax = plt.subplots(figsize=(6.5, 6.5))
best_pred = reg_preds[best_reg_name]
ax.scatter(yr_test, best_pred, alpha=0.35, s=14, color=HVNH_BLUE)
ax.plot([0, 1], [0, 1], color=HVNH_ORANGE, lw=2, ls="--", label="Đường dự báo hoàn hảo")
ax.set_xlabel("Automation_Probability_2030 thực tế")
ax.set_ylabel("Automation_Probability_2030 dự báo")
ax.set_title(f"Dự báo vs. Thực tế — {best_reg_name} (R²={reg_metrics[best_reg_name]['R2']:.3f})",
             fontweight="bold")
ax.legend()
plt.tight_layout()
plt.savefig(FIG_DIR / "17_regression_pred_vs_actual.png")
plt.close()

# ===========================================================================
# BƯỚC 7 — XUẤT PIPELINE_SUMMARY.JSON
# ===========================================================================
print("\n" + "=" * 80)
print("BƯỚC 7. XUẤT KẾT QUẢ TỔNG HỢP")
print("=" * 80)

summary["n_figures"] = len(list(FIG_DIR.glob("*.png")))
summary["dataset_topic"] = "Tác động của AI đến việc làm năm 2030"
summary["n_job_titles"] = int(df["Job_Title"].nunique())
summary["mean_automation_probability"] = float(df["Automation_Probability_2030"].mean())
summary["mean_ai_exposure_index"] = float(df["AI_Exposure_Index"].mean())
summary["risk_category_counts"] = df["Risk_Category"].value_counts().reindex(RISK_ORDER).to_dict()

with open(BASE_DIR / "pipeline_summary.json", "w", encoding="utf-8") as f:
    json.dump(summary, f, ensure_ascii=False, indent=2, default=str)

print(f"Tổng số biểu đồ đã xuất: {summary['n_figures']}")
print("Đã lưu pipeline_summary.json")
print("\nHOÀN TẤT PIPELINE.")
