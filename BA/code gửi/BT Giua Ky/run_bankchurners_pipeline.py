import os
import sys
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import (
    silhouette_score, accuracy_score, precision_score, recall_score,
    f1_score, roc_auc_score, roc_curve, confusion_matrix, classification_report
)
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

# Set random seed
np.random.seed(42)

# Set directories
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "BankChurners.csv")
FIG_DIR = os.path.join(BASE_DIR, "figures")
os.makedirs(FIG_DIR, exist_ok=True)

# Styling configurations
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 11
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['axes.titleweight'] = 'bold'
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['axes.labelweight'] = 'bold'
plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10
plt.rcParams['legend.fontsize'] = 10
plt.rcParams['figure.titlesize'] = 16
plt.rcParams['figure.titleweight'] = 'bold'

COLOR_EXISTING = '#1E3A8A'  # Navy Blue
COLOR_ATTRITED = '#EF4444'  # Coral Red
PALETTE = {'Existing Customer': COLOR_EXISTING, 'Attrited Customer': COLOR_ATTRITED}

print("="*70)
print("🚀 BẮT ĐẦU PIPELINE XỬ LÝ & KHAI PHÁ DỮ LIỆU BANKCHURNERS")
print("="*70)

# 1. Đọc dữ liệu
df_raw = pd.read_csv(DATA_PATH)
print(f"✅ Đã tải dữ liệu thô: {df_raw.shape[0]} dòng, {df_raw.shape[1]} cột")

# 2. Tiền xử lý & Làm sạch
# Loại bỏ 2 cột Naive Bayes thừa ở cuối bảng
cols_to_drop = [c for c in df_raw.columns if c.startswith('Naive_Bayes_Classifier')]
df = df_raw.drop(columns=cols_to_drop).copy()
print(f"✅ Đã loại bỏ các cột thừa Naive Bayes: {cols_to_drop}")

# Xử lý missing values nếu có (điền median cho các cột số bị khuyết lẻ tẻ)
num_cols_raw = df.select_dtypes(include=[np.number]).columns.tolist()
for col in num_cols_raw:
    if df[col].isnull().sum() > 0:
        df[col] = df[col].fillna(df[col].median())

# Feature Engineering
df['Age_Group'] = pd.cut(
    df['Customer_Age'],
    bins=[0, 35, 45, 55, 65, 100],
    labels=['<35', '35-44', '45-54', '55-64', '65+'],
    right=False
)
df['Avg_Trans_Value'] = df['Total_Trans_Amt'] / df['Total_Trans_Ct']
df['Churn_Binary'] = (df['Attrition_Flag'] == 'Attrited Customer').astype(int)
df['Trans_Per_Month'] = df['Total_Trans_Ct'] / df['Months_on_book']
df['Revolving_Ratio'] = df['Total_Revolving_Bal'] / (df['Credit_Limit'] + 1e-5)
df['Contact_Intensity'] = df['Contacts_Count_12_mon'] / (df['Months_Inactive_12_mon'] + 1)

# Lưu file cleaned
df.to_csv(os.path.join(BASE_DIR, "BankChurners_Cleaned.csv"), index=False)
print("✅ Đã tạo các biến mới & lưu BankChurners_Cleaned.csv")

# ==========================================
# 3. VẼ CÁC BIỂU ĐỒ EDA (HÌNH 1 -> HÌNH 8)
# ==========================================
print("\n📊 Đang vẽ các biểu đồ EDA...")

# Hình 1: Churn Distribution (Donut Chart)
fig, ax = plt.subplots(figsize=(8, 6))
counts = df['Attrition_Flag'].value_counts()
labels = [f"Ở lại (Existing)\n{counts['Existing Customer']:,} ({counts['Existing Customer']/len(df):.1%})",
          f"Rời bỏ (Attrited)\n{counts['Attrited Customer']:,} ({counts['Attrited Customer']/len(df):.1%})"]
colors = [COLOR_EXISTING, COLOR_ATTRITED]
wedges, texts, autotexts = ax.pie(
    counts, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors,
    wedgeprops=dict(width=0.4, edgecolor='w', linewidth=2),
    pctdistance=0.75, textprops={'fontsize': 12, 'weight': 'bold'}
)
for at in autotexts:
    at.set_color('white')
    at.set_fontsize(13)
ax.set_title("Phân bố Biến Mục tiêu: Tỷ lệ Khách hàng Rời bỏ (Attrition Rate)", pad=20)
plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, "01_churn_distribution.png"), dpi=300)
plt.close()

# Hình 2: Demographic Analysis (2x2 Grid)
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# 2.1 Giới tính
gender_churn = pd.crosstab(df['Gender'], df['Attrition_Flag'], normalize='index') * 100
gender_churn[['Existing Customer', 'Attrited Customer']].plot(
    kind='bar', stacked=True, color=[COLOR_EXISTING, COLOR_ATTRITED], ax=axes[0, 0], edgecolor='white'
)
axes[0, 0].set_title("A. Tỷ lệ Rời bỏ theo Giới tính (Gender)")
axes[0, 0].set_ylabel("Tỷ lệ phần trăm (%)")
axes[0, 0].set_xlabel("Giới tính (F: Nữ, M: Nam)")
axes[0, 0].tick_params(axis='x', rotation=0)
for p in axes[0, 0].patches:
    h, w, x, y = p.get_height(), p.get_width(), p.get_x(), p.get_y()
    if h > 5:
        axes[0, 0].annotate(f"{h:.1f}%", (x + w/2, y + h/2), ha='center', va='center', color='white', fontweight='bold')

# 2.2 Nhóm tuổi
age_churn = pd.crosstab(df['Age_Group'], df['Attrition_Flag'], normalize='index') * 100
age_churn[['Existing Customer', 'Attrited Customer']].plot(
    kind='bar', stacked=True, color=[COLOR_EXISTING, COLOR_ATTRITED], ax=axes[0, 1], edgecolor='white'
)
axes[0, 1].set_title("B. Tỷ lệ Rời bỏ theo Phân khúc Độ tuổi (Age Group)")
axes[0, 1].set_ylabel("Tỷ lệ phần trăm (%)")
axes[0, 1].set_xlabel("Nhóm tuổi")
axes[0, 1].tick_params(axis='x', rotation=0)
for p in axes[0, 1].patches:
    h, w, x, y = p.get_height(), p.get_width(), p.get_x(), p.get_y()
    if h > 5:
        axes[0, 1].annotate(f"{h:.1f}%", (x + w/2, y + h/2), ha='center', va='center', color='white', fontweight='bold')

# 2.3 Mức thu nhập
income_order = ['Less than $40K', '$40K - $60K', '$60K - $80K', '$80K - $120K', '$120K +', 'Unknown']
income_churn = pd.crosstab(df['Income_Category'], df['Attrition_Flag'], normalize='index').reindex(income_order) * 100
income_churn[['Existing Customer', 'Attrited Customer']].plot(
    kind='bar', stacked=True, color=[COLOR_EXISTING, COLOR_ATTRITED], ax=axes[1, 0], edgecolor='white'
)
axes[1, 0].set_title("C. Tỷ lệ Rời bỏ theo Mức thu nhập (Income Category)")
axes[1, 0].set_ylabel("Tỷ lệ phần trăm (%)")
axes[1, 0].set_xlabel("Mức thu nhập")
axes[1, 0].tick_params(axis='x', rotation=30)
for p in axes[1, 0].patches:
    h, w, x, y = p.get_height(), p.get_width(), p.get_x(), p.get_y()
    if h > 5:
        axes[1, 0].annotate(f"{h:.1f}%", (x + w/2, y + h/2), ha='center', va='center', color='white', fontweight='bold')

# 2.4 Trình độ học vấn
edu_order = ['Uneducated', 'High School', 'College', 'Graduate', 'Post-Graduate', 'Doctorate', 'Unknown']
edu_churn = pd.crosstab(df['Education_Level'], df['Attrition_Flag'], normalize='index').reindex(edu_order) * 100
edu_churn[['Existing Customer', 'Attrited Customer']].plot(
    kind='bar', stacked=True, color=[COLOR_EXISTING, COLOR_ATTRITED], ax=axes[1, 1], edgecolor='white'
)
axes[1, 1].set_title("D. Tỷ lệ Rời bỏ theo Trình độ học vấn (Education Level)")
axes[1, 1].set_ylabel("Tỷ lệ phần trăm (%)")
axes[1, 1].set_xlabel("Trình độ học vấn")
axes[1, 1].tick_params(axis='x', rotation=30)
for p in axes[1, 1].patches:
    h, w, x, y = p.get_height(), p.get_width(), p.get_x(), p.get_y()
    if h > 5:
        axes[1, 1].annotate(f"{h:.1f}%", (x + w/2, y + h/2), ha='center', va='center', color='white', fontweight='bold')

for ax in axes.flat:
    ax.legend(['Ở lại (Existing)', 'Rời bỏ (Attrited)'], loc='upper right')

plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, "02_demographic_churn.png"), dpi=300)
plt.close()

# Hình 3: Transaction Behavior Scatter & Density
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(
    data=df, x='Total_Trans_Ct', y='Total_Trans_Amt', hue='Attrition_Flag',
    palette=PALETTE, alpha=0.6, s=35, edgecolor='none', ax=ax
)
ax.set_title("Tương quan giữa Số lần giao dịch (Total_Trans_Ct) & Tổng giá trị chi tiêu (Total_Trans_Amt)")
ax.set_xlabel("Tổng số lần giao dịch (Total_Trans_Ct)")
ax.set_ylabel("Tổng giá trị giao dịch ($ USD)")
ax.axvline(55, color='black', linestyle='--', alpha=0.7, label='Ngưỡng báo động (< 55 lần)')
ax.axhline(3000, color='grey', linestyle=':', alpha=0.7, label='Ngưỡng chi tiêu thấp (< $3,000)')
ax.legend(title="Trạng thái khách hàng", loc='upper left')
plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, "03_transaction_behavior_churn.png"), dpi=300)
plt.close()

# Hình 4: Financial Ratios (Boxplots)
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
sns.boxplot(data=df, x='Attrition_Flag', y='Total_Revolving_Bal', palette=PALETTE, ax=axes[0], width=0.4)
axes[0].set_title("A. Dư nợ tín dụng quay vòng (Total_Revolving_Bal)")
axes[0].set_xlabel("Trạng thái")
axes[0].set_ylabel("Dư nợ quay vòng ($ USD)")

sns.boxplot(data=df, x='Attrition_Flag', y='Avg_Utilization_Ratio', palette=PALETTE, ax=axes[1], width=0.4)
axes[1].set_title("B. Tỷ lệ sử dụng hạn mức (Avg_Utilization_Ratio)")
axes[1].set_xlabel("Trạng thái")
axes[1].set_ylabel("Tỷ lệ sử dụng (0.0 - 1.0)")

plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, "04_financial_ratios_churn.png"), dpi=300)
plt.close()

# Hình 5: Customer Interaction Decay
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
contact_churn = pd.crosstab(df['Contacts_Count_12_mon'], df['Attrition_Flag'], normalize='index') * 100
contact_churn[['Existing Customer', 'Attrited Customer']].plot(
    kind='bar', stacked=True, color=[COLOR_EXISTING, COLOR_ATTRITED], ax=axes[0], edgecolor='white'
)
axes[0].set_title("A. Tỷ lệ Rời bỏ theo Số lần Liên hệ CSKH (Contacts Count)")
axes[0].set_xlabel("Số lần liên hệ trong 12 tháng")
axes[0].set_ylabel("Tỷ lệ (%)")
axes[0].tick_params(axis='x', rotation=0)

inactive_churn = pd.crosstab(df['Months_Inactive_12_mon'], df['Attrition_Flag'], normalize='index') * 100
inactive_churn[['Existing Customer', 'Attrited Customer']].plot(
    kind='bar', stacked=True, color=[COLOR_EXISTING, COLOR_ATTRITED], ax=axes[1], edgecolor='white'
)
axes[1].set_title("B. Tỷ lệ Rời bỏ theo Số tháng Ngủ đông (Months Inactive)")
axes[1].set_xlabel("Số tháng không hoạt động trong 12 tháng")
axes[1].set_ylabel("Tỷ lệ (%)")
axes[1].tick_params(axis='x', rotation=0)

for ax in axes:
    ax.legend(['Ở lại (Existing)', 'Rời bỏ (Attrited)'], loc='upper left')

plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, "05_interaction_decay_churn.png"), dpi=300)
plt.close()

# Hình 6: Change Metrics
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
sns.kdeplot(data=df, x='Total_Ct_Chng_Q4_Q1', hue='Attrition_Flag', palette=PALETTE, fill=True, common_norm=False, ax=axes[0])
axes[0].set_title("A. Phân phối Mức thay đổi Số lượng GD Q4/Q1")
axes[0].set_xlabel("Total_Ct_Chng_Q4_Q1")
axes[0].set_xlim(0, 2)

sns.kdeplot(data=df, x='Total_Amt_Chng_Q4_Q1', hue='Attrition_Flag', palette=PALETTE, fill=True, common_norm=False, ax=axes[1])
axes[1].set_title("B. Phân phối Mức thay đổi Giá trị GD Q4/Q1")
axes[1].set_xlabel("Total_Amt_Chng_Q4_Q1")
axes[1].set_xlim(0, 2)

plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, "06_change_metrics_churn.png"), dpi=300)
plt.close()

# Hình 7: Correlation Heatmap
num_features = [
    'Customer_Age', 'Dependent_count', 'Months_on_book', 'Total_Relationship_Count',
    'Months_Inactive_12_mon', 'Contacts_Count_12_mon', 'Credit_Limit',
    'Total_Revolving_Bal', 'Avg_Open_To_Buy', 'Total_Amt_Chng_Q4_Q1',
    'Total_Trans_Amt', 'Total_Trans_Ct', 'Total_Ct_Chng_Q4_Q1',
    'Avg_Utilization_Ratio', 'Avg_Trans_Value', 'Churn_Binary'
]
corr = df[num_features].corr()
fig, ax = plt.subplots(figsize=(14, 11))
mask = np.triu(np.ones_like(corr, dtype=bool))
sns.heatmap(corr, mask=mask, annot=True, fmt='.2f', cmap='Blues', vmin=-0.4, vmax=1.0, linewidths=0.5, ax=ax)
ax.set_title("Ma trận Tương quan Tuyến tính (Pearson Correlation Heatmap)")
plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, "07_correlation_heatmap.png"), dpi=300)
plt.close()

# Hình 8: Relationship Count & Card Category
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
rel_churn = pd.crosstab(df['Total_Relationship_Count'], df['Attrition_Flag'], normalize='index') * 100
rel_churn[['Existing Customer', 'Attrited Customer']].plot(
    kind='bar', stacked=True, color=[COLOR_EXISTING, COLOR_ATTRITED], ax=axes[0], edgecolor='white'
)
axes[0].set_title("A. Tỷ lệ Rời bỏ theo Số lượng Sản phẩm (Relationship Count)")
axes[0].set_xlabel("Số lượng sản phẩm sở hữu")
axes[0].set_ylabel("Tỷ lệ (%)")
axes[0].tick_params(axis='x', rotation=0)

card_order = ['Blue', 'Silver', 'Gold', 'Platinum']
card_churn = pd.crosstab(df['Card_Category'], df['Attrition_Flag'], normalize='index').reindex(card_order) * 100
card_churn[['Existing Customer', 'Attrited Customer']].plot(
    kind='bar', stacked=True, color=[COLOR_EXISTING, COLOR_ATTRITED], ax=axes[1], edgecolor='white'
)
axes[1].set_title("B. Tỷ lệ Rời bỏ theo Hạng thẻ (Card Category)")
axes[1].set_xlabel("Hạng thẻ")
axes[1].set_ylabel("Tỷ lệ (%)")
axes[1].tick_params(axis='x', rotation=0)

for ax in axes:
    ax.legend(['Ở lại (Existing)', 'Rời bỏ (Attrited)'], loc='upper left')

plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, "08_relationship_and_card.png"), dpi=300)
plt.close()

print("✅ Đã tạo xong 8 biểu đồ EDA ban đầu.")

# ==========================================
# 4. KHAI PHÁ DỮ LIỆU: PHÂN CỤM KHÁCH HÀNG (K-MEANS)
# ==========================================
print("\n🔍 Đang thực hiện Khai phá dữ liệu: Phân cụm K-Means & PCA...")

clustering_features = [
    'Customer_Age', 'Credit_Limit', 'Total_Revolving_Bal', 'Avg_Utilization_Ratio',
    'Total_Trans_Amt', 'Total_Trans_Ct', 'Total_Ct_Chng_Q4_Q1', 'Contacts_Count_12_mon',
    'Months_Inactive_12_mon', 'Total_Relationship_Count'
]

scaler_cluster = StandardScaler()
X_cluster_scaled = scaler_cluster.fit_transform(df[clustering_features])

# Elbow & Silhouette Analysis
k_range = range(2, 9)
inertias = []
silhouettes = []

for k in k_range:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X_cluster_scaled)
    inertias.append(km.inertia_)
    silhouettes.append(silhouette_score(X_cluster_scaled, km.labels_))

# Hình 9: K-Means Elbow & Silhouette
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
axes[0].plot(k_range, inertias, marker='o', color='#1E3A8A', linewidth=2.5, markersize=7)
axes[0].set_title("A. Phương pháp Điểm uốn (Elbow Method)")
axes[0].set_xlabel("Số cụm (k)")
axes[0].set_ylabel("Inertia (Tổng bình phương khoảng cách)")
axes[0].axvline(4, color='#EF4444', linestyle='--', label='k=4 tối ưu')
axes[0].legend()

axes[1].plot(k_range, silhouettes, marker='s', color='#10B981', linewidth=2.5, markersize=7)
axes[1].set_title("B. Chỉ số Silhouette Score theo k")
axes[1].set_xlabel("Số cụm (k)")
axes[1].set_ylabel("Silhouette Score")
axes[1].axvline(4, color='#EF4444', linestyle='--', label='k=4 tối ưu')
axes[1].legend()

plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, "09_kmeans_elbow_silhouette.png"), dpi=300)
plt.close()

# Huấn luyện K-Means với k=4
kmeans_final = KMeans(n_clusters=4, random_state=42, n_init=10)
df['Cluster'] = kmeans_final.fit_predict(X_cluster_scaled)

# PCA Giảm chiều xuống 2D
pca = PCA(n_components=2, random_state=42)
pca_transformed = pca.fit_transform(X_cluster_scaled)
df['PCA1'] = pca_transformed[:, 0]
df['PCA2'] = pca_transformed[:, 1]

# Đặt tên định danh nghiệp vụ cho 4 Cụm
cluster_names = {
    0: 'Cụm 0: Tiêu dùng phổ thông ổn định (Steady Transactors)',
    1: 'Cụm 1: Ngủ đông & Nguy cơ rời bỏ cao (Dormant & High-Risk)',
    2: 'Cụm 2: Khách hàng Cao cấp / Chi tiêu lớn (Affluent & High-Spenders)',
    3: 'Cụm 3: Tín dụng quay vòng / Vay tiêu dùng (Revolving Borrowers)'
}
df['Cluster_Name'] = df['Cluster'].map(cluster_names)

# Hình 10: Trực quan hóa Phân cụm PCA & Churn Rate
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

cluster_colors = ['#3B82F6', '#EF4444', '#10B981', '#F59E0B']
sns.scatterplot(
    data=df, x='PCA1', y='PCA2', hue='Cluster', palette=cluster_colors,
    alpha=0.6, s=30, edgecolor='none', ax=axes[0]
)
axes[0].set_title(f"A. Bản đồ 4 Phân cụm Khách hàng qua PCA (Giải thích {(pca.explained_variance_ratio_.sum()):.1%} phương sai)")
axes[0].set_xlabel(f"PCA 1 ({pca.explained_variance_ratio_[0]:.1%})")
axes[0].set_ylabel(f"PCA 2 ({pca.explained_variance_ratio_[1]:.1%})")
axes[0].legend(title="Phân cụm K-Means", labels=[cluster_names[i] for i in range(4)], loc='upper right', fontsize=8)

# Tỷ lệ Churn theo từng cụm
cluster_churn = df.groupby('Cluster')['Churn_Binary'].mean() * 100
bars = axes[1].bar(
    [f"Cụm {i}" for i in range(4)], cluster_churn,
    color=cluster_colors, edgecolor='black', linewidth=1
)
axes[1].set_title("B. Tỷ lệ Rời bỏ (%) theo từng Phân cụm Khách hàng")
axes[1].set_ylabel("Tỷ lệ Churn (%)")
axes[1].set_xlabel("Phân cụm hành vi")
for bar in bars:
    yval = bar.get_height()
    axes[1].text(bar.get_x() + bar.get_width()/2, yval + 0.5, f"{yval:.1f}%", ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, "10_kmeans_clusters_pca.png"), dpi=300)
plt.close()

# Lưu dataset phân cụm
df.to_csv(os.path.join(BASE_DIR, "BankChurners_Clustered.csv"), index=False)
print("✅ Đã hoàn thành phân cụm K-Means & lưu BankChurners_Clustered.csv")

# ==========================================
# 5. MÔ HÌNH HÓA DỰ BÁO RỜI BỎ (SUPERVISED LEARNING)
# ==========================================
print("\n🤖 Đang huấn luyện và đánh giá 4 Mô hình Máy học Phân loại...")

# Chuẩn bị dữ liệu cho ML
feature_cols = [
    'Customer_Age', 'Gender', 'Dependent_count', 'Education_Level', 'Marital_Status',
    'Income_Category', 'Card_Category', 'Months_on_book', 'Total_Relationship_Count',
    'Months_Inactive_12_mon', 'Contacts_Count_12_mon', 'Credit_Limit', 'Total_Revolving_Bal',
    'Avg_Open_To_Buy', 'Total_Amt_Chng_Q4_Q1', 'Total_Trans_Amt', 'Total_Trans_Ct',
    'Total_Ct_Chng_Q4_Q1', 'Avg_Utilization_Ratio', 'Avg_Trans_Value', 'Revolving_Ratio',
    'Contact_Intensity'
]

X = df[feature_cols].copy()
y = df['Churn_Binary'].values

categorical_cols = ['Gender', 'Education_Level', 'Marital_Status', 'Income_Category', 'Card_Category']
numerical_cols = [c for c in feature_cols if c not in categorical_cols]

# One-hot encoding cho categorical variables
X_encoded = pd.get_dummies(X, columns=categorical_cols, drop_first=True)

# Train/Test Split (80/20 Stratified)
X_train, X_test, y_train, y_test = train_test_split(
    X_encoded, y, test_size=0.2, random_state=42, stratify=y
)

# Standard Scaler cho các mô hình tuyến tính
scaler_ml = StandardScaler()
X_train_scaled = scaler_ml.fit_transform(X_train)
X_test_scaled = scaler_ml.transform(X_test)

# Định nghĩa 4 mô hình
models = {
    'Logistic Regression': LogisticRegression(class_weight='balanced', max_iter=1000, random_state=42),
    'Decision Tree': DecisionTreeClassifier(max_depth=6, class_weight='balanced', random_state=42),
    'Random Forest': RandomForestClassifier(n_estimators=200, max_depth=12, class_weight='balanced', random_state=42, n_jobs=-1),
    'XGBoost Classifier': XGBClassifier(n_estimators=200, max_depth=5, learning_rate=0.08, scale_pos_weight=5.22, random_state=42, eval_metric='logloss')
}

results = {}
fpr_dict = {}
tpr_dict = {}
auc_dict = {}
cm_dict = {}

for name, model in models.items():
    if name == 'Logistic Regression':
        model.fit(X_train_scaled, y_train)
        y_pred = model.predict(X_test_scaled)
        y_prob = model.predict_proba(X_test_scaled)[:, 1]
    else:
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        y_prob = model.predict_proba(X_test)[:, 1]
    
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred)
    rec = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    roc_auc = roc_auc_score(y_test, y_prob)
    
    results[name] = {
        'Accuracy': float(acc),
        'Precision': float(prec),
        'Recall': float(rec),
        'F1-Score': float(f1),
        'ROC-AUC': float(roc_auc)
    }
    
    fpr, tpr, _ = roc_curve(y_test, y_prob)
    fpr_dict[name] = fpr
    tpr_dict[name] = tpr
    auc_dict[name] = float(roc_auc)
    cm_dict[name] = confusion_matrix(y_test, y_pred).tolist()

metrics_df = pd.DataFrame(results).T
print("\n📈 BẢNG SO SÁNH HIỆU NĂNG CÁC MÔ HÌNH DỰ BÁO RỜI BỎ:")
print(metrics_df.to_string())

# Hình 11: So sánh Đường cong ROC-AUC & Bảng chỉ số
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

model_colors = {
    'Logistic Regression': '#6B7280',
    'Decision Tree': '#F59E0B',
    'Random Forest': '#3B82F6',
    'XGBoost Classifier': '#EF4444'
}

for name in models.keys():
    axes[0].plot(
        fpr_dict[name], tpr_dict[name],
        label=f"{name} (AUC = {auc_dict[name]:.4f})",
        color=model_colors[name], linewidth=2.5
    )
axes[0].plot([0, 1], [0, 1], 'k--', alpha=0.5, label='Random Baseline (AUC = 0.5000)')
axes[0].set_title("A. So sánh Đường cong ROC (Receiver Operating Characteristic)")
axes[0].set_xlabel("Tỷ lệ Dương tính Giả (False Positive Rate - FPR)")
axes[0].set_ylabel("Tỷ lệ Dương tính Thật (True Positive Rate - TPR / Recall)")
axes[0].legend(loc='lower right')

# Bảng biểu đồ cột so sánh F1, Recall, ROC-AUC
metrics_df[['Recall', 'Precision', 'F1-Score', 'ROC-AUC']].plot(
    kind='bar', ax=axes[1], colormap='viridis', edgecolor='black', width=0.8
)
axes[1].set_title("B. So sánh Chi tiết các Thước đo Hiệu năng Mô hình")
axes[1].set_ylabel("Điểm số (0.0 - 1.0)")
axes[1].set_ylim(0.5, 1.05)
axes[1].tick_params(axis='x', rotation=15)
axes[1].legend(loc='lower right')

plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, "11_ml_model_comparison_roc.png"), dpi=300)
plt.close()

# Hình 12: Ma trận nhầm lẫn (Confusion Matrices) 2x2 Grid
fig, axes = plt.subplots(2, 2, figsize=(14, 11))
for idx, (name, cm_list) in enumerate(cm_dict.items()):
    r, c = idx // 2, idx % 2
    cm_arr = np.array(cm_list)
    sns.heatmap(
        cm_arr, annot=True, fmt='d', cmap='Blues', cbar=False, ax=axes[r, c],
        annot_kws={'size': 14, 'weight': 'bold'}
    )
    axes[r, c].set_title(f"{name}\nRecall={results[name]['Recall']:.1%}, F1={results[name]['F1-Score']:.1%}")
    axes[r, c].set_xlabel("Nhãn Dự đoán (Predicted)")
    axes[r, c].set_ylabel("Nhãn Thực tế (Actual)")
    axes[r, c].set_xticklabels(['Ở lại (0)', 'Rời bỏ (1)'])
    axes[r, c].set_yticklabels(['Ở lại (0)', 'Rời bỏ (1)'])

plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, "12_ml_confusion_matrices.png"), dpi=300)
plt.close()

# Hình 13: Feature Importance (XGBoost)
xgb_model = models['XGBoost Classifier']
importances = xgb_model.feature_importances_
feature_names = X_encoded.columns
feat_imp = pd.Series(importances, index=feature_names).sort_values(ascending=False).head(12)

fig, ax = plt.subplots(figsize=(12, 7))
sns.barplot(x=feat_imp.values, y=feat_imp.index, palette='mako', ax=ax, edgecolor='black')
ax.set_title("Top 12 Đặc trưng quan trọng nhất dự báo Khách hàng Rời bỏ (XGBoost Feature Importance)")
ax.set_xlabel("Mức độ quan trọng tương đối (Relative Feature Importance)")
for p in ax.patches:
    w = p.get_width()
    ax.annotate(f"{w:.3f}", (w + 0.003, p.get_y() + p.get_height()/2), ha='left', va='center', fontweight='bold')

plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, "13_feature_importance_xgb.png"), dpi=300)
plt.close()

# Hình 14: Tối ưu hóa Ngưỡng xác suất & Bài toán Chi phí - Lợi ích
xgb_probs = xgb_model.predict_proba(X_test)[:, 1]
thresholds = np.linspace(0.05, 0.95, 100)
net_profits = []
recalls = []
precisions = []

for t in thresholds:
    preds = (xgb_probs >= t).astype(int)
    tn, fp, fn, tp = confusion_matrix(y_test, preds).ravel()
    # Lợi ích = TP * ($500 - $50) - FP * $50 - FN * $500
    profit = tp * 450 - fp * 50 - fn * 500
    net_profits.append(profit)
    recalls.append(recall_score(y_test, preds))
    precisions.append(precision_score(y_test, preds, zero_division=0))

opt_idx = int(np.argmax(net_profits))
opt_threshold = float(thresholds[opt_idx])
max_profit = float(net_profits[opt_idx])

fig, ax1 = plt.subplots(figsize=(12, 6))
color = '#1E3A8A'
ax1.set_xlabel('Ngưỡng Cắt Xác Suất Rời Bỏ (Classification Threshold)')
ax1.set_ylabel('Lợi Nhuận Ròng Thu Được ($ USD)', color=color, fontweight='bold')
line1 = ax1.plot(thresholds, net_profits, color=color, linewidth=3, label=f'Lợi nhuận ròng (Tối ưu tại t={opt_threshold:.2f})')
ax1.axvline(opt_threshold, color='#EF4444', linestyle='--', label=f'Ngưỡng Tối Ưu = {opt_threshold:.2f}')
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color2 = '#10B981'
ax2.set_ylabel('Recall & Precision', color=color2, fontweight='bold')
line2 = ax2.plot(thresholds, recalls, color='#10B981', linestyle=':', linewidth=2, label='Recall')
line3 = ax2.plot(thresholds, precisions, color='#F59E0B', linestyle='-.', linewidth=2, label='Precision')
ax2.tick_params(axis='y', labelcolor=color2)

lines = line1 + line2 + line3 + [ax1.lines[1]]
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='lower center')
plt.title(f"Tối Ưu Hóa Ngưỡng Xác Suất theo Bài Toán Kinh Tế Giữ Chân (Lợi nhuận tối đa: ${max_profit:,.0f})")
plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, "14_cost_benefit_threshold_optimization.png"), dpi=300)
plt.close()

# Cluster profiling summary
cluster_summary = df.groupby('Cluster').agg({
    'Customer_Age': 'mean',
    'Credit_Limit': 'mean',
    'Total_Revolving_Bal': 'mean',
    'Avg_Utilization_Ratio': 'mean',
    'Total_Trans_Amt': 'mean',
    'Total_Trans_Ct': 'mean',
    'Total_Ct_Chng_Q4_Q1': 'mean',
    'Contacts_Count_12_mon': 'mean',
    'Months_Inactive_12_mon': 'mean',
    'Total_Relationship_Count': 'mean',
    'Churn_Binary': ['count', 'mean']
})
cluster_summary.columns = [f"{c[0]}_{c[1]}" if isinstance(c, tuple) else str(c) for c in cluster_summary.columns]
cluster_summary_dict = cluster_summary.to_dict()

# Lưu metrics ra file json để tái sử dụng
summary_stats = {
    'total_customers': int(len(df)),
    'existing_customers': int(counts['Existing Customer']),
    'attrited_customers': int(counts['Attrited Customer']),
    'churn_rate': float(counts['Attrited Customer'] / len(df)),
    'optimal_k': 4,
    'optimal_threshold': float(opt_threshold),
    'max_retention_profit': float(max_profit),
    'model_metrics': results,
    'top_features': {str(k): float(v) for k, v in feat_imp.items()},
    'cluster_names': cluster_names
}

with open(os.path.join(BASE_DIR, "pipeline_summary.json"), 'w') as f:
    json.dump(summary_stats, f, indent=4)

print("="*70)
print("🎉 HOÀN THÀNH TOÀN BỘ PIPELINE PHÂN TÍCH & KHAI PHÁ DỮ LIỆU!")
print(f"📁 Đã xuất toàn bộ 14 biểu đồ độ phân giải 300 DPI vào thư mục: {FIG_DIR}")
print(f"📁 Đã lưu tệp tổng hợp: pipeline_summary.json")
print("="*70)
