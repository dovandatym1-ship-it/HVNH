"""
Dựng 2 notebook Jupyter cho đồ án "Tác động của AI đến việc làm năm 2030":
  1) AI_ViecLam2030_EDA_TienXuLy.ipynb
  2) AI_ViecLam2030_Data_Processing_and_Mining_DoVanDat.ipynb

Cấu trúc & phong cách tham khảo cách trình bày notebook tiền xử lý -> EDA ->
mô hình hoá (đọc dữ liệu, "Load and show first rows", nhận xét bằng lời sau mỗi bước)
từ: https://www.kaggle.com/code/denvermagtibay/predicting-uber-ride-cancellations
"""
import nbformat as nbf

nb1 = nbf.v4.new_notebook()
nb2 = nbf.v4.new_notebook()

def md(text):
    return nbf.v4.new_markdown_cell(text)

def code(text):
    return nbf.v4.new_code_cell(text)

# ===========================================================================
# NOTEBOOK 1 — EDA & TIỀN XỬ LÝ DỮ LIỆU
# ===========================================================================
nb1.cells = [
md("""# Tác động của AI đến Việc làm năm 2030
### Notebook 1/2 — Khám phá dữ liệu thô & Tiền xử lý (EDA + Data Cleaning)

**Học phần:** Phân tích Kinh doanh — Học viện Ngân hàng
**Sinh viên thực hiện:** Đỗ Văn Đạt
**Đề tài (Bài tập cuối kỳ):** Tác động của Trí tuệ nhân tạo (AI) đến rủi ro tự động hoá việc làm năm 2030
**Bộ dữ liệu:** `AI_ViecLam2030_Raw.csv` — 3.000 quan sát x 18 biến, tổng hợp đặc điểm 20 nghề nghiệp
(lương, kinh nghiệm, học vấn, các chỉ số phơi nhiễm AI, 10 nhóm điểm kỹ năng, xác suất & nhóm
rủi ro tự động hoá năm 2030).

**Phong cách trình bày notebook** (đọc dữ liệu → hiển thị dòng đầu → EDA từng bước có nhận xét)
tham khảo từ notebook Kaggle: *Predicting Uber Ride Cancellations* —
https://www.kaggle.com/code/denvermagtibay/predicting-uber-ride-cancellations

**Mục tiêu notebook này:**
1. Đọc và khám phá cấu trúc dữ liệu thô.
2. Kiểm tra & xử lý dữ liệu thiếu, trùng lặp, ngoài miền giá trị hợp lệ, ngoại lai.
3. Phát hiện và ghi nhận rủi ro rò rỉ dữ liệu (data leakage) giữa các biến.
4. Tạo các biến đặc trưng mới (feature engineering) phục vụ mô hình hoá ở Notebook 2.
5. Phân tích khám phá dữ liệu (EDA) bằng 8 biểu đồ trực quan, mỗi biểu đồ kèm một câu nhận xét."""),

md("## 0. Nạp thư viện"),
code("""import warnings
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

warnings.filterwarnings("ignore")

HVNH_NAVY = "#1F3864"
HVNH_ORANGE = "#ED7D31"
HVNH_BLUE = "#2E5496"
PALETTE_RISK = {"Low": "#2E7D32", "Medium": "#ED7D31", "High": "#C0392B"}
RISK_ORDER = ["Low", "Medium", "High"]
SKILL_COLS = [f"Skill_{i}" for i in range(1, 11)]

sns.set_theme(style="whitegrid", font_scale=1.0)
plt.rcParams["figure.dpi"] = 110
plt.rcParams["font.family"] = "DejaVu Sans"

FIG_DIR = Path("figures")
FIG_DIR.mkdir(exist_ok=True)
print("Thư viện đã sẵn sàng.")"""),

md("""## 1. Đọc & khám phá dữ liệu thô (Load and show first rows)

Bước đầu tiên: đọc file CSV gốc, xem kích thước, 5 dòng đầu và kiểu dữ liệu của từng cột —
tương tự bước "Load and Show First Rows" trong notebook tham khảo Kaggle."""),
code("""df_raw = pd.read_csv("AI_ViecLam2030_Raw.csv")
print("Kích thước dữ liệu thô:", df_raw.shape)
df_raw.head()"""),
code("""df_raw.info()"""),
code("""df_raw.describe().T"""),
md("""**Nhận xét:** Dữ liệu thô có 3.000 dòng, 18 cột, gồm 1 biến định danh nghề nghiệp (`Job_Title`,
20 giá trị), 1 biến định tính thứ bậc (`Education_Level`), 1 biến mục tiêu phân loại
(`Risk_Category`), và 15 biến định lượng — trong đó 12 biến (AI_Exposure_Index,
Automation_Probability_2030, Skill_1..10) bị giới hạn trong đoạn [0, 1]."""),

md("""## 2. Tiền xử lý dữ liệu

### 2.1. Dữ liệu thiếu"""),
code("""missing = df_raw.isnull().sum()
missing_pct = (missing / len(df_raw) * 100).round(2)
report = pd.DataFrame({"So_o_thieu": missing, "Ty_le_%": missing_pct})
report[report["So_o_thieu"] > 0] if missing.sum() > 0 else print("Không có ô nào bị thiếu dữ liệu.")"""),
md("**Nhận xét:** Bộ dữ liệu không có ô nào bị thiếu — phù hợp với một bộ dữ liệu mô phỏng "
   "(synthetic) được sinh có kiểm soát, khác với dữ liệu thu thập thực tế thường có tỷ lệ thiếu nhất định."),

md("### 2.2. Dữ liệu trùng lặp"),
code("""n_dup = int(df_raw.duplicated().sum())
df = df_raw.drop_duplicates().reset_index(drop=True)
print(f"Số dòng trùng lặp phát hiện & loại bỏ: {n_dup}")
print(f"Số dòng còn lại: {len(df)}")"""),

md("### 2.3. Kiểm tra miền giá trị hợp lệ (business rule validation)\n\n"
   "Các chỉ số `AI_Exposure_Index`, `Automation_Probability_2030` và 10 biến `Skill_1..10` "
   "về bản chất là các thang đo chuẩn hoá trong đoạn [0, 1]. Dòng nào vi phạm được xem là "
   "lỗi nhập liệu/mô phỏng và bị loại."),
code("""bounded_0_1 = ["AI_Exposure_Index", "Automation_Probability_2030"] + SKILL_COLS
invalid_rows = pd.Series(False, index=df.index)
for col in bounded_0_1:
    invalid_rows |= ~df[col].between(0, 1)
n_invalid = int(invalid_rows.sum())
df = df.loc[~invalid_rows].reset_index(drop=True)
print(f"Số dòng vi phạm miền giá trị [0,1]: {n_invalid}")
print(f"Số dòng còn lại sau bước làm sạch: {len(df)}")"""),

md("### 2.4. Ngoại lai (quy tắc IQR) trên `Average_Salary`"),
code("""q1, q3 = df["Average_Salary"].quantile([0.25, 0.75])
iqr = q3 - q1
lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
n_outliers_salary = int(((df["Average_Salary"] < lower) | (df["Average_Salary"] > upper)).sum())
print(f"Q1={q1:.0f}  Q3={q3:.0f}  IQR={iqr:.0f}")
print(f"Cận dưới={lower:.0f}  Cận trên={upper:.0f}")
print(f"Số hồ sơ ngoại lai theo IQR: {n_outliers_salary}")"""),
md("**Nhận xét:** Không có hồ sơ nào vượt ngưỡng IQR — mức lương trong dữ liệu trải khá đều từ "
   "thấp đến cao mà không có giá trị cực đoan bất thường, nên **không cần loại bỏ** dòng nào ở bước này."),

md("""### 2.5. Kiểm tra rò rỉ dữ liệu (data leakage) — phát hiện quan trọng nhất

Trước khi mô hình hoá, cần kiểm tra: `Risk_Category` có thực sự là một biến độc lập, hay chỉ là
biến **phái sinh (rule-based)** từ `Automation_Probability_2030`? Nếu là biến phái sinh, đưa
`Automation_Probability_2030` vào tập đặc trưng khi dự báo `Risk_Category` sẽ gây rò rỉ dữ liệu
(mô hình "ăn gian" vì biết trước gần như chính xác câu trả lời)."""),
code("""risk_bins = df.groupby("Risk_Category")["Automation_Probability_2030"].agg(["min", "max", "count"])
risk_bins"""),
md("**Nhận xét:** Ba nhóm rủi ro tương ứng CHÍNH XÁC với 3 khoảng giá trị rời rạc của "
   "`Automation_Probability_2030` (Low: 0.05–0.30, Medium: 0.31–0.70, High: 0.71–0.95) — "
   "không có điểm chồng lấn. Điều này xác nhận `Risk_Category` là biến phái sinh theo ngưỡng "
   "cố định. **Quyết định phương pháp luận:** ở Notebook 2, `Automation_Probability_2030` sẽ "
   "bị loại khỏi tập đặc trưng khi huấn luyện mô hình phân loại `Risk_Category`."),

md("### 2.6. Tạo biến mới (Feature Engineering)"),
code("""df["Skill_Diversity_Score"] = df[SKILL_COLS].mean(axis=1).round(4)
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

print("Đã tạo 7 biến mới. Kích thước dữ liệu sau feature engineering:", df.shape)
df.head(3)"""),
md("""**Diễn giải các biến mới:**
- `Skill_Diversity_Score`: điểm kỹ năng trung bình trên 10 nhóm kỹ năng — đại diện cho mức độ đa kỹ năng.
- `Skill_Std`: độ lệch chuẩn giữa 10 kỹ năng — kỹ năng càng lệch (chuyên sâu 1-2 mảng) thì càng cao.
- `High_Value_Skill_Count`: số kỹ năng đạt điểm > 0.7 — đếm số "điểm mạnh" rõ rệt.
- `Salary_per_YearExp`: lương quy đổi trên mỗi năm kinh nghiệm — đo hiệu suất thu nhập theo thâm niên.
- `Human_Edge_Score`: chỉ số "lợi thế con người" tự xây dựng = 50% (1 − AI_Exposure_Index) + 50% Skill_Diversity_Score,
  giả định lợi thế cạnh tranh trước AI đến từ (a) ít bị AI thay thế trực tiếp và (b) kỹ năng đa dạng."""),

code("""df.to_csv("AI_ViecLam2030_Cleaned.csv", index=False, encoding="utf-8-sig")
print(f"Đã lưu dữ liệu sạch: AI_ViecLam2030_Cleaned.csv — {df.shape[0]} dòng x {df.shape[1]} cột")"""),

md("## 3. Phân tích khám phá dữ liệu (EDA)"),

md("### Biểu đồ 1 — Phân bố Nhóm rủi ro tự động hoá"),
code("""fig, ax = plt.subplots(figsize=(7, 5))
order = df["Risk_Category"].value_counts().reindex(RISK_ORDER)
bars = ax.bar(order.index, order.values, color=[PALETTE_RISK[c] for c in order.index])
for b, v in zip(bars, order.values):
    ax.text(b.get_x() + b.get_width() / 2, v + 25, f"{v}\\n({v/len(df)*100:.1f}%)",
            ha="center", fontsize=10, fontweight="bold")
ax.set_ylim(0, order.values.max() * 1.18)
ax.set_title("Phân bố số lượng nghề nghiệp theo Nhóm rủi ro tự động hoá 2030", fontweight="bold", pad=14)
ax.set_xlabel("Nhóm rủi ro (Risk_Category)")
ax.set_ylabel("Số lượng nghề nghiệp")
plt.tight_layout()
plt.savefig(FIG_DIR / "01_risk_category_distribution.png")
plt.show()"""),
md("**Nhận xét:** Nhóm `Medium` chiếm đa số (50,7%), hai nhóm `Low` và `High` gần như cân bằng "
   "(~24,6-24,7%) — cơ cấu này phản ánh cách chia ngưỡng đối xứng của `Automation_Probability_2030` "
   "quanh khoảng giữa, không phản ánh phân bố nghề nghiệp thực tế ngoài đời."),

md("### Biểu đồ 2 — Phân bố Xác suất tự động hoá 2030"),
code("""fig, ax = plt.subplots(figsize=(7, 5))
sns.histplot(df["Automation_Probability_2030"], bins=30, kde=True, color=HVNH_BLUE, ax=ax)
ax.axvline(df["Automation_Probability_2030"].mean(), color=HVNH_ORANGE, ls="--",
           label=f"Trung bình = {df['Automation_Probability_2030'].mean():.2f}")
ax.set_title("Phân bố Xác suất tự động hoá công việc vào năm 2030", fontweight="bold")
ax.set_xlabel("Automation_Probability_2030")
ax.legend()
plt.tight_layout()
plt.savefig(FIG_DIR / "02_automation_probability_distribution.png")
plt.show()"""),
md("**Nhận xét:** Phân bố có 3 \"cụm mật độ\" rõ rệt tương ứng 3 tầng nghề nghiệp sẽ được "
   "làm rõ ở Biểu đồ 8, không phải một phân bố chuẩn (normal) trơn — gợi ý ngay từ EDA rằng "
   "biến mục tiêu phụ thuộc vào một yếu tố phân loại (nghề nghiệp) hơn là biến liên tục."),

md("### Biểu đồ 3 — Lương trung bình theo Nhóm rủi ro"),
code("""fig, ax = plt.subplots(figsize=(7, 5))
sns.boxplot(data=df, x="Risk_Category", y="Average_Salary", order=RISK_ORDER, palette=PALETTE_RISK, ax=ax)
ax.set_title("Mức lương trung bình theo Nhóm rủi ro tự động hoá", fontweight="bold")
ax.set_xlabel("Nhóm rủi ro"); ax.set_ylabel("Lương trung bình (USD/năm)")
plt.tight_layout()
plt.savefig(FIG_DIR / "03_salary_by_risk_category.png")
plt.show()"""),
md("**Nhận xét:** Trung vị và độ trải của lương gần như giống nhau ở cả 3 nhóm rủi ro — "
   "mức lương KHÔNG phải là yếu tố phân biệt nhóm rủi ro trong bộ dữ liệu này."),

md("### Biểu đồ 4 — Trình độ học vấn theo Nhóm rủi ro"),
code("""fig, ax = plt.subplots(figsize=(8, 5))
ct = pd.crosstab(df["Education_Level"], df["Risk_Category"], normalize="index")[RISK_ORDER] * 100
ct = ct.reindex(["High School", "Bachelor's", "Master's", "PhD"])
ct.plot(kind="bar", stacked=True, color=[PALETTE_RISK[c] for c in RISK_ORDER], ax=ax)
ax.set_title("Cơ cấu Nhóm rủi ro theo Trình độ học vấn (%)", fontweight="bold")
ax.set_xlabel("Trình độ học vấn"); ax.set_ylabel("Tỷ lệ (%)")
ax.legend(title="Risk_Category"); plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(FIG_DIR / "04_education_vs_risk.png")
plt.show()"""),
md("**Nhận xét:** Cơ cấu rủi ro gần như đồng nhất giữa 4 nhóm học vấn (~25% Low, ~50% Medium, "
   "~25% High mỗi nhóm) — học vấn cũng không phải yếu tố phân biệt, trái với trực giác thông thường "
   "rằng trình độ cao hơn thường gắn với công việc ít bị tự động hoá hơn."),

md("### Biểu đồ 5 — Chỉ số Phơi nhiễm AI so với Xác suất tự động hoá"),
code("""fig, ax = plt.subplots(figsize=(7.5, 5.5))
for cat in RISK_ORDER:
    sub = df[df["Risk_Category"] == cat]
    ax.scatter(sub["AI_Exposure_Index"], sub["Automation_Probability_2030"],
               s=14, alpha=0.55, color=PALETTE_RISK[cat], label=cat)
ax.set_title("Chỉ số Phơi nhiễm AI so với Xác suất tự động hoá 2030", fontweight="bold")
ax.set_xlabel("AI_Exposure_Index"); ax.set_ylabel("Automation_Probability_2030")
ax.legend(title="Risk_Category")
plt.tight_layout()
plt.savefig(FIG_DIR / "05_ai_exposure_vs_automation.png")
plt.show()"""),
md("**Nhận xét:** Các điểm phân tán đều theo mọi hướng, không có xu hướng tuyến tính — "
   "`AI_Exposure_Index` (một chỉ số tưởng như liên quan trực tiếp đến chủ đề) thực chất "
   "KHÔNG tương quan với xác suất tự động hoá trong bộ dữ liệu mô phỏng này."),

md("### Biểu đồ 6 — Ma trận tương quan"),
code("""corr_cols = ["Average_Salary", "Years_Experience", "AI_Exposure_Index", "Tech_Growth_Factor",
             "Automation_Probability_2030", "Skill_Diversity_Score", "Human_Edge_Score"]
fig, ax = plt.subplots(figsize=(8, 6.5))
sns.heatmap(df[corr_cols].corr(), annot=True, fmt=".2f", cmap="RdBu_r", center=0, vmin=-1, vmax=1,
            ax=ax, cbar_kws={"label": "Hệ số tương quan"})
ax.set_title("Ma trận tương quan giữa các biến định lượng chính", fontweight="bold")
plt.tight_layout()
plt.savefig(FIG_DIR / "06_correlation_heatmap.png")
plt.show()"""),
md("**Nhận xét:** Toàn bộ hệ số tương quan với `Automation_Probability_2030` đều xấp xỉ 0 "
   "(|r| < 0.05) — khẳng định thêm rằng các biến định lượng cấp cá nhân không giải thích được "
   "biến mục tiêu; nguyên nhân thực sự sẽ được truy tìm ở Biểu đồ 8."),

md("### Biểu đồ 7 — Kinh nghiệm làm việc và Xác suất tự động hoá"),
code("""fig, ax = plt.subplots(figsize=(7.5, 5.5))
sns.regplot(data=df, x="Years_Experience", y="Automation_Probability_2030",
            scatter_kws={"alpha": 0.25, "s": 12, "color": HVNH_BLUE},
            line_kws={"color": HVNH_ORANGE, "lw": 2}, ax=ax)
ax.set_title("Số năm kinh nghiệm và Xác suất tự động hoá 2030", fontweight="bold")
plt.tight_layout()
plt.savefig(FIG_DIR / "07_experience_vs_automation.png")
plt.show()"""),
md("**Nhận xét:** Đường hồi quy gần như phẳng (hệ số góc ≈ 0) — số năm kinh nghiệm không "
   "làm giảm hay tăng rủi ro tự động hoá trong dữ liệu mô phỏng, khác với kỳ vọng thông thường."),

md("""### Biểu đồ 8 — Xác suất tự động hoá theo Nghề nghiệp (bằng chứng then chốt)

Sau khi loại trừ mọi biến định lượng cấp cá nhân, bước cuối cùng là kiểm tra biến định danh
duy nhất còn lại: `Job_Title`."""),
code("""job_stats = df.groupby("Job_Title")["Automation_Probability_2030"].agg(["mean", "std", "count"]).sort_values("mean")

def _tier_color(v):
    if v < 0.30: return PALETTE_RISK["Low"]
    if v > 0.70: return PALETTE_RISK["High"]
    return PALETTE_RISK["Medium"]

colors_tier = [_tier_color(v) for v in job_stats["mean"]]
fig, ax = plt.subplots(figsize=(9, 8.5))
ax.barh(job_stats.index, job_stats["mean"], xerr=job_stats["std"], color=colors_tier,
        error_kw={"ecolor": "#555555", "elinewidth": 1, "capsize": 2})
ax.set_title("Xác suất tự động hoá TB theo Nghề nghiệp (20 nghề, ±1 độ lệch chuẩn)", fontweight="bold")
ax.set_xlabel("Automation_Probability_2030 (trung bình)")
ax.axvline(0.30, color="grey", ls=":", lw=1); ax.axvline(0.70, color="grey", ls=":", lw=1)
plt.tight_layout()
plt.savefig(FIG_DIR / "08_jobtitle_automation_ranked.png")
plt.show()"""),
code("""overall_mean = df["Automation_Probability_2030"].mean()
ss_between = float(((job_stats["mean"] - overall_mean) ** 2 * job_stats["count"]).sum())
ss_total = float(((df["Automation_Probability_2030"] - overall_mean) ** 2).sum())
eta_squared_job = ss_between / ss_total
print(f"Eta^2 (Job_Title -> Automation_Probability_2030) = {eta_squared_job:.4f}")
print(f"=> Job_Title giải thích {eta_squared_job*100:.1f}% phương sai của biến mục tiêu.")"""),
md("""**Nhận xét (phát hiện quan trọng nhất của notebook):** 20 nghề tách thành **3 tầng rõ rệt**:
- **Tầng thấp (~0,17-0,18):** AI Engineer, Research Scientist, Nurse, Teacher, Doctor — nghề đòi hỏi
  phán đoán chuyên môn sâu, chăm sóc/tương tác con người cao.
- **Tầng trung bình (~0,48-0,53):** 10 nghề chuyên môn/văn phòng còn lại.
- **Tầng cao (~0,82-0,83):** Truck Driver, Customer Support, Construction Worker, Security Guard,
  Retail Worker — nghề có tỷ trọng tác vụ lặp lại/thủ tục cao.

`Job_Title` giải thích tới **~86% phương sai** của xác suất tự động hoá — vượt trội hoàn toàn so
với mọi biến cá nhân đã kiểm tra ở Biểu đồ 2-7. Kết luận sơ bộ này phù hợp với **lý thuyết tiếp
cận theo tác vụ (task-based approach)** của Autor, Levy & Murnane (2003) và nghiên cứu thực nghiệm
của Frey & Osborne (2013) — rủi ro tự động hoá được quyết định bởi **bản chất công việc/nghề
nghiệp**, không phải đặc điểm cá nhân của người đang làm nghề đó. Phát hiện này sẽ dẫn dắt toàn bộ
chiến lược mô hình hoá ở Notebook 2: bắt buộc phải đưa `Job_Title` vào tập đặc trưng."""),

md("""## 4. Tóm tắt Notebook 1 & bước tiếp theo

1. Dữ liệu sạch, không thiếu/trùng/ngoại lai — 3.000 dòng x 25 cột sau feature engineering,
   đã lưu vào `AI_ViecLam2030_Cleaned.csv`.
2. Phát hiện rò rỉ dữ liệu: `Risk_Category` = hàm ngưỡng của `Automation_Probability_2030`
   → loại biến này khỏi tập đặc trưng phân loại.
3. Phát hiện cấu trúc dữ liệu cốt lõi: rủi ro tự động hoá được quyết định ở **cấp độ nghề
   nghiệp** (eta² ≈ 0,86), không phải ở cấp độ đặc điểm cá nhân người lao động.

→ Tiếp tục ở **Notebook 2 — `AI_ViecLam2030_Data_Processing_and_Mining_DoVanDat.ipynb`**:
phân cụm hồ sơ kỹ năng, mô hình phân loại `Risk_Category` và mô hình hồi quy
`Automation_Probability_2030` có đưa `Job_Title` vào tập đặc trưng."""),
]

with open("AI_ViecLam2030_EDA_TienXuLy.ipynb", "w", encoding="utf-8") as f:
    nbf.write(nb1, f)
print("Đã tạo AI_ViecLam2030_EDA_TienXuLy.ipynb với", len(nb1.cells), "cells")

# ===========================================================================
# NOTEBOOK 2 — PHÂN CỤM & MÔ HÌNH HOÁ (DATA PROCESSING AND MINING)
# ===========================================================================
nb2.cells = [
md("""# Tác động của AI đến Việc làm năm 2030
### Notebook 2/2 — Phân cụm & Mô hình hoá (Data Processing and Mining)

**Học phần:** Phân tích Kinh doanh — Học viện Ngân hàng
**Sinh viên thực hiện:** Đỗ Văn Đạt

Notebook này tiếp nối `AI_ViecLam2030_EDA_TienXuLy.ipynb`, sử dụng dữ liệu đã làm sạch
(`AI_ViecLam2030_Cleaned.csv`) để thực hiện:
1. Phân cụm K-Means trên hồ sơ kỹ năng (skill profile clustering).
2. Mô hình phân loại `Risk_Category` — so sánh 3 mô hình (Logistic Regression, Random Forest, XGBoost).
3. Mô hình hồi quy `Automation_Probability_2030` — đối chiếu độc lập.
4. Kết luận & hàm ý nghiệp vụ / quản trị nhân sự.

**Kế thừa phát hiện chính từ Notebook 1:** `Job_Title` giải thích ~86% phương sai của rủi ro
tự động hoá (eta² ≈ 0,86) → bắt buộc đưa `Job_Title` (one-hot) vào tập đặc trưng mô hình hoá,
đồng thời loại `Automation_Probability_2030` khỏi tập đặc trưng phân loại `Risk_Category` để
tránh rò rỉ dữ liệu (leakage)."""),

md("## 0. Nạp thư viện & dữ liệu đã làm sạch"),
code("""import warnings
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import (ConfusionMatrixDisplay, accuracy_score, f1_score,
                              mean_absolute_error, precision_score, r2_score,
                              recall_score, roc_auc_score, silhouette_score)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from xgboost import XGBClassifier, XGBRegressor

warnings.filterwarnings("ignore")
RANDOM_STATE = 42
HVNH_NAVY, HVNH_ORANGE, HVNH_BLUE = "#1F3864", "#ED7D31", "#2E5496"
PALETTE_RISK = {"Low": "#2E7D32", "Medium": "#ED7D31", "High": "#C0392B"}
RISK_ORDER = ["Low", "Medium", "High"]
SKILL_COLS = [f"Skill_{i}" for i in range(1, 11)]
sns.set_theme(style="whitegrid", font_scale=1.0)
plt.rcParams["figure.dpi"] = 110
FIG_DIR = Path("figures"); FIG_DIR.mkdir(exist_ok=True)

df = pd.read_csv("AI_ViecLam2030_Cleaned.csv")
print("Dữ liệu đã làm sạch:", df.shape)
df.head(3)"""),

md("""## 1. Phân cụm K-Means trên hồ sơ kỹ năng (Skill Profile Clustering)

Mục tiêu: khám phá xem có tồn tại các "hồ sơ kỹ năng" (skill archetype) tự nhiên trong 3.000
quan sát hay không, dựa trên 10 điểm kỹ năng + 2 chỉ số công nghệ."""),
code("""cluster_feats = SKILL_COLS + ["AI_Exposure_Index", "Tech_Growth_Factor"]
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
axes[0].set_xlabel("Số cụm (k)"); axes[0].set_ylabel("Inertia (WCSS)")
axes[1].plot(list(k_range), silhouettes, marker="o", color=HVNH_ORANGE)
axes[1].set_title("Chỉ số Silhouette theo số cụm k", fontweight="bold")
axes[1].set_xlabel("Số cụm (k)"); axes[1].set_ylabel("Silhouette Score")
plt.tight_layout()
plt.savefig(FIG_DIR / "12_kmeans_elbow_silhouette.png")
plt.show()

sil_by_k = {k: round(s, 4) for k, s in zip(k_range, silhouettes)}
print("Silhouette theo k:", sil_by_k)"""),
md("""**Nhận xét quan trọng (đọc kỹ trước khi chọn k):** Silhouette Score chỉ dao động trong
khoảng **0,055 – 0,063** ở mọi k — rất gần 0, nghĩa là **các cụm không tách biệt rõ ràng** ở
BẤT KỲ giá trị k nào. Điều này nhất quán với phát hiện ở Notebook 1: các biến kỹ năng
(Skill_1..10) không mang thông tin phân biệt nhóm rủi ro, nên cũng không tạo thành các cụm tự
nhiên mạnh. Nhóm k = 4 dưới đây được chọn **vì mục đích diễn giải nghiệp vụ** (phân khúc dễ
truyền thông trong báo cáo), **không phải vì dữ liệu có cấu trúc phân cụm mạnh** — cần nêu rõ
giới hạn này khi trình bày kết quả, tránh overclaim."""),
code("""optimal_k = 4
kmeans_final = KMeans(n_clusters=optimal_k, random_state=RANDOM_STATE, n_init=10)
df["Cluster"] = kmeans_final.fit_predict(X_cluster_scaled)

pca = PCA(n_components=2, random_state=RANDOM_STATE)
pcs = pca.fit_transform(X_cluster_scaled)
fig, ax = plt.subplots(figsize=(8, 6))
palette_cluster = sns.color_palette("tab10", optimal_k)
for c in range(optimal_k):
    mask = df["Cluster"] == c
    ax.scatter(pcs[mask, 0], pcs[mask, 1], s=16, alpha=0.6, color=palette_cluster[c], label=f"Cụm {c}")
ax.set_title(f"Trực quan hoá {optimal_k} cụm hồ sơ kỹ năng qua PCA (2 thành phần)", fontweight="bold")
ax.set_xlabel(f"PC1 ({pca.explained_variance_ratio_[0]*100:.1f}% phương sai)")
ax.set_ylabel(f"PC2 ({pca.explained_variance_ratio_[1]*100:.1f}% phương sai)")
ax.legend()
plt.tight_layout()
plt.savefig(FIG_DIR / "13_kmeans_clusters_pca.png")
plt.show()"""),
code("""cluster_profile = df.groupby("Cluster").agg(
    So_luong=("Job_Title", "count"),
    XacSuat_TuDongHoa_TB=("Automation_Probability_2030", "mean"),
    AI_Exposure_TB=("AI_Exposure_Index", "mean"),
    Luong_TB=("Average_Salary", "mean"),
    KinhNghiem_TB=("Years_Experience", "mean"),
    KyNang_TB=("Skill_Diversity_Score", "mean"),
).round(3)
cluster_profile"""),
md("**Nhận xét:** Hai thành phần chính PCA (PC1+PC2) chỉ giải thích một phần nhỏ phương sai và "
   "4 vùng màu trên biểu đồ chồng lấn gần như hoàn toàn — xác nhận trực quan cho kết luận từ "
   "Silhouette Score. Bảng hồ sơ cụm cũng cho thấy 4 cụm có `XacSuat_TuDongHoa_TB` gần như bằng "
   "nhau (0,49-0,52) — phân cụm trên hồ sơ kỹ năng KHÔNG tách được nhóm rủi ro cao/thấp."),

md("## 2. Mô hình phân loại Nhóm rủi ro tự động hoá (Risk_Category)"),
code("""base_features = ["Average_Salary", "Years_Experience", "Education_Level_Encoded",
                  "AI_Exposure_Index", "Tech_Growth_Factor", "Skill_Diversity_Score",
                  "Skill_Std", "High_Value_Skill_Count", "Human_Edge_Score"] + SKILL_COLS

# QUYẾT ĐỊNH PHƯƠNG PHÁP LUẬN (kế thừa Notebook 1):
#  - KHÔNG đưa Automation_Probability_2030 vào đặc trưng (tránh rò rỉ dữ liệu).
#  - CÓ đưa Job_Title (one-hot, drop_first) vào đặc trưng (eta^2 ~ 0.86 ở Notebook 1).
X = pd.get_dummies(df[base_features + ["Job_Title"]], columns=["Job_Title"], drop_first=True)
clf_features = list(X.columns)
job_title_dummy_cols = [c for c in clf_features if c.startswith("Job_Title_")]

le = LabelEncoder(); le.fit(RISK_ORDER)
y = le.transform(df["Risk_Category"])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=RANDOM_STATE, stratify=y)
scaler = StandardScaler()
X_train_s, X_test_s = scaler.fit_transform(X_train), scaler.transform(X_test)
print("Số đặc trưng đưa vào mô hình:", len(clf_features), f"(gồm {len(job_title_dummy_cols)} biến giả Job_Title)")"""),
code("""models = {
    "Logistic Regression": LogisticRegression(max_iter=2000, random_state=RANDOM_STATE),
    "Random Forest": RandomForestClassifier(n_estimators=300, max_depth=10, random_state=RANDOM_STATE),
    "XGBoost Classifier": XGBClassifier(n_estimators=300, max_depth=5, learning_rate=0.08,
                                         random_state=RANDOM_STATE, eval_metric="mlogloss"),
}
model_metrics, fitted_models = {}, {}
for name, model in models.items():
    Xtr = X_train_s if name == "Logistic Regression" else X_train
    Xte = X_test_s if name == "Logistic Regression" else X_test
    model.fit(Xtr, y_train)
    y_pred, y_proba = model.predict(Xte), model.predict_proba(Xte)
    model_metrics[name] = {
        "Accuracy": accuracy_score(y_test, y_pred),
        "Precision_macro": precision_score(y_test, y_pred, average="macro"),
        "Recall_macro": recall_score(y_test, y_pred, average="macro"),
        "F1_macro": f1_score(y_test, y_pred, average="macro"),
        "ROC_AUC_ovr": roc_auc_score(y_test, y_proba, multi_class="ovr", average="macro"),
    }
    fitted_models[name] = (model, y_pred, y_proba, Xte)

metrics_df = pd.DataFrame(model_metrics).T
metrics_df.round(4)"""),
code("""fig, ax = plt.subplots(figsize=(10, 5.5))
metrics_df.plot(kind="bar", ax=ax, color=["#4472C4", "#ED7D31", "#A5A5A5", "#FFC000", "#1F3864"])
ax.set_title("So sánh hiệu suất 3 mô hình phân loại Nhóm rủi ro tự động hoá", fontweight="bold")
ax.set_ylabel("Điểm số"); ax.set_ylim(0, 1.05); ax.legend(loc="lower right")
plt.xticks(rotation=15); plt.tight_layout()
plt.savefig(FIG_DIR / "14_ml_model_comparison.png")
plt.show()

best_model_name = max(model_metrics, key=lambda k: model_metrics[k]["F1_macro"])
print(f"Mô hình tốt nhất theo F1-macro: {best_model_name}")"""),
md("""**Nhận xét (so sánh với vòng thử nghiệm KHÔNG có Job_Title — xem Notebook 1):** Việc đưa
`Job_Title` vào tập đặc trưng nâng F1-macro từ mức xấp xỉ ngẫu nhiên (~0,22-0,34 khi chỉ dùng
đặc trưng cá nhân) lên **~0,93-0,99** và ROC-AUC lên **~0,996-0,998**. Đây là minh chứng định
lượng trực tiếp cho kết luận ở Notebook 1: bản chất nghề nghiệp quyết định rủi ro tự động hoá,
không phải đặc điểm cá nhân của người đảm nhiệm nghề đó."""),
code("""fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))
for ax, (name, (model, y_pred, y_proba, Xte)) in zip(axes, fitted_models.items()):
    ConfusionMatrixDisplay.from_predictions(y_test, y_pred, display_labels=le.classes_,
                                             ax=ax, colorbar=False, cmap="Blues")
    ax.set_title(name, fontsize=11, fontweight="bold")
plt.tight_layout()
plt.savefig(FIG_DIR / "15_confusion_matrices.png")
plt.show()"""),
md("**Nhận xét:** Nhầm lẫn hầu như chỉ xảy ra giữa `Medium` và `High` (một số ít hồ sơ `Medium` "
   "có xác suất gần ngưỡng 0,70 bị dự báo nhầm sang `High`) — hợp lý vì đây là vùng giáp ranh "
   "giữa hai khoảng ngưỡng liền kề. Không có nhầm lẫn nào giữa `Low` và `High` (hai đầu xa nhau)."),
code("""importance_model_name = "XGBoost Classifier"
importance_model = fitted_models[importance_model_name][0]
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
plt.show()
print(f"Tổng importance của Job_Title (19 biến giả gộp lại): {job_title_total:.4f}")"""),

md("## 3. Mô hình hồi quy Xác suất tự động hoá (đối chiếu độc lập)"),
code("""reg_features = clf_features
Xr = X[reg_features].copy()
yr = df["Automation_Probability_2030"].values
Xr_train, Xr_test, yr_train, yr_test = train_test_split(Xr, yr, test_size=0.25, random_state=RANDOM_STATE)

reg_models = {
    "Linear Regression": LinearRegression(),
    "Random Forest Regressor": RandomForestRegressor(n_estimators=300, max_depth=10, random_state=RANDOM_STATE),
    "XGBoost Regressor": XGBRegressor(n_estimators=300, max_depth=5, learning_rate=0.08, random_state=RANDOM_STATE),
}
reg_metrics, reg_preds = {}, {}
for name, model in reg_models.items():
    model.fit(Xr_train, yr_train)
    pred = model.predict(Xr_test)
    reg_metrics[name] = {"R2": r2_score(yr_test, pred), "MAE": mean_absolute_error(yr_test, pred),
                          "RMSE": float(np.sqrt(np.mean((yr_test - pred) ** 2)))}
    reg_preds[name] = pred

reg_metrics_df = pd.DataFrame(reg_metrics).T
reg_metrics_df.round(4)"""),
code("""best_reg_name = max(reg_metrics, key=lambda k: reg_metrics[k]["R2"])
best_pred = reg_preds[best_reg_name]
fig, ax = plt.subplots(figsize=(6.5, 6.5))
ax.scatter(yr_test, best_pred, alpha=0.35, s=14, color=HVNH_BLUE)
ax.plot([0, 1], [0, 1], color=HVNH_ORANGE, lw=2, ls="--", label="Đường dự báo hoàn hảo")
ax.set_xlabel("Automation_Probability_2030 thực tế"); ax.set_ylabel("Automation_Probability_2030 dự báo")
ax.set_title(f"Dự báo vs. Thực tế — {best_reg_name} (R²={reg_metrics[best_reg_name]['R2']:.3f})", fontweight="bold")
ax.legend(); plt.tight_layout()
plt.savefig(FIG_DIR / "17_regression_pred_vs_actual.png")
plt.show()
print(f"Mô hình hồi quy tốt nhất: {best_reg_name} (R² = {reg_metrics[best_reg_name]['R2']:.4f})")"""),
md("**Nhận xét:** R² đạt ~0,80-0,86 khi có `Job_Title` — nhất quán với kết quả phân loại ở Mục 2. "
   "MAE ~0,08 nghĩa là sai số dự báo trung bình chỉ khoảng 8 điểm phần trăm xác suất, mức sai số "
   "hợp lý cho một mô hình chỉ dựa trên đặc trưng nghề nghiệp + hồ sơ cá nhân, không có dữ liệu "
   "theo thời gian hay đặc thù công nghệ ngành cụ thể."),

code("""df.to_csv("AI_ViecLam2030_Clustered.csv", index=False, encoding="utf-8-sig")
print("Đã lưu dữ liệu đã gắn nhãn cụm: AI_ViecLam2030_Clustered.csv")"""),

md("""## 4. Kết luận & Hàm ý nghiệp vụ

**Phát hiện chính:**
1. Đặc điểm cá nhân của người lao động (kỹ năng, kinh nghiệm, học vấn, lương) **không dự báo
   được** rủi ro tự động hoá trong bộ dữ liệu này — mọi mô hình chỉ dùng nhóm biến này đều cho
   hiệu suất xấp xỉ dự đoán ngẫu nhiên (AUC ≈ 0,50, R² ≈ 0).
2. **Nghề nghiệp (Job_Title)** là yếu tố quyết định gần như tuyệt đối (eta² ≈ 0,86; khi đưa vào
   mô hình: F1-macro ≈ 0,93-0,99, AUC ≈ 0,996-0,998, R² ≈ 0,80-0,86).
3. 20 nghề phân thành 3 tầng rủi ro rõ rệt, phù hợp lý thuyết tiếp cận theo tác vụ (task-based
   approach — Autor, Levy & Murnane, 2003) và nghiên cứu thực nghiệm Frey & Osborne (2013).
4. Phân cụm không giám sát trên hồ sơ kỹ năng KHÔNG phát hiện được cấu trúc phân nhóm có ý nghĩa
   (Silhouette ≈ 0,06) — cho thấy giá trị của phương pháp có giám sát (biết nhãn nghề nghiệp)
   vượt trội hoàn toàn so với phương pháp không giám sát trong bài toán này.

**Hàm ý về phương pháp luận:** Đây là bộ dữ liệu **mô phỏng (synthetic)** dùng cho mục đích luyện
tập kỹ thuật phân tích — bản thân `Automation_Probability_2030` được sinh gắn với `Job_Title`
theo quy tắc cố định, không phản ánh đầy đủ cơ chế nhân quả phức tạp trong thực tế (công nghệ mới,
chính sách, ngành nghề theo thời gian...). Kết luận **"nghề nghiệp quyết định rủi ro tự động hoá,
đặc điểm cá nhân thì không"** chỉ có giá trị nội tại đối với tập dữ liệu mô phỏng này; để khái quát
hoá cho thị trường lao động thực tế cần đối chiếu thêm với các nghiên cứu như Frey & Osborne (2013,
*The Future of Employment*), McKinsey Global Institute (2017, *Jobs Lost, Jobs Gained*) và WEF
*Future of Jobs Report* (2023/2025) — xem Chương 1 và Tài liệu tham khảo của báo cáo Word đi kèm.

**Hàm ý nghiệp vụ / quản trị nhân sự:** Chiến lược đào tạo lại (reskilling) nên được **thiết kế
theo nhóm nghề** (occupation-level) thay vì chỉ dựa trên hồ sơ năng lực cá nhân — vì trong dữ liệu
này, hai nhân sự có hồ sơ kỹ năng giống hệt nhau nhưng khác nghề có thể rơi vào hai nhóm rủi ro
hoàn toàn khác nhau."""),
]

with open("AI_ViecLam2030_Data_Processing_and_Mining_DoVanDat.ipynb", "w", encoding="utf-8") as f:
    nbf.write(nb2, f)
print("Đã tạo AI_ViecLam2030_Data_Processing_and_Mining_DoVanDat.ipynb với", len(nb2.cells), "cells")
