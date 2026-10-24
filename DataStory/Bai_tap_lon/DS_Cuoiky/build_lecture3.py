from pathlib import Path
import nbformat as nbf

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "lecture3.ipynb"

nb = nbf.v4.new_notebook()
nb["metadata"] = {
    "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
    "language_info": {"name": "python", "version": "3"},
}

def md(text):
    nb.cells.append(nbf.v4.new_markdown_cell(text.strip()))

def code(text):
    nb.cells.append(nbf.v4.new_code_cell(text.strip()))

md(r"""
# Design Freeze: chặn hiệu ứng domino từ thay đổi thiết kế
## Notebook phân tích phục vụ Project cuối kỳ môn Data Storytelling

**Vấn đề kinh doanh:** Các dự án xây dựng bị trượt tiến độ; doanh nghiệp cần biết yếu tố nào có khả năng dự báo độ trễ mạnh nhất và hành động nào có thể triển khai ngay.

**Đối tượng:** Ban Giám đốc, Ban Quản lý dự án và Phòng Kế hoạch.

**Main point:** Trong bộ dữ liệu mô phỏng này, thay đổi thiết kế là tín hiệu chi phối độ trễ. Mỗi vòng sửa bản vẽ làm số ngày chậm tăng theo kiểu “liều–đáp ứng”; vì vậy cần khóa thiết kế theo mốc và kiểm soát Change Order.

> **Lưu ý đạo đức dữ liệu:** Đây là dữ liệu mô phỏng phục vụ học tập, không phải dữ liệu vận hành thực tế. Kết quả mô tả logic của kịch bản giả định và không được trình bày như bằng chứng thực nghiệm ngoài doanh nghiệp.
""")

md(r"""
## 0. Bản đồ phân tích theo khung 4D

| Thành phần | Câu hỏi trọng tâm | Đầu ra |
|---|---|---|
| **Problem** | Vì sao dự án trượt tiến độ? | Xác định tác nhân nổi bật sau khi kiểm tra yếu tố nhiễu |
| **Outcome** | Doanh nghiệp muốn thay đổi điều gì? | Giảm tỷ lệ dự án trễ và tổng số ngày chậm |
| **Action** | Quyết định nào có thể thực hiện? | Design Freeze, Change Control Board, SLA phản hồi 48 giờ |
| **Measure** | Biết giải pháp có hiệu quả bằng cách nào? | Số vòng sửa, tỷ lệ thay đổi sau freeze, ngày chậm/vòng sửa, tỷ lệ đúng hạn |

### Câu hỏi nghiên cứu

1. Tỷ lệ dự án chậm tiến độ hiện tại là bao nhiêu?
2. Có/không thay đổi thiết kế tạo ra khác biệt gì về xác suất và mức độ chậm?
3. Độ trễ có tăng nhất quán theo số lần thay đổi thiết kế không?
4. Kết luận có còn giữ khi xem xét mưa, thiếu vật tư, quy mô hợp đồng và loại công trình?
5. Nếu giảm số vòng sửa thiết kế, tác động kinh doanh tiềm năng là bao nhiêu?
""")

md("## 1. Thiết lập môi trường và ngôn ngữ trực quan thống nhất")

code(r"""
from pathlib import Path
import re
import warnings

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
try:
    from IPython.display import display
except ImportError:
    def display(obj):
        print(obj)

warnings.filterwarnings("ignore")
pd.set_option("display.max_columns", 50)
pd.set_option("display.float_format", lambda x: f"{x:,.2f}")

# Một ngôn ngữ màu xuyên suốt toàn bộ câu chuyện
COLORS = {
    "baseline": "#A7B0B5",      # nhóm không đổi thiết kế / thông tin nền
    "design": "#C43D32",        # thay đổi thiết kế / rủi ro trung tâm
    "support": "#D69E2E",       # insight hỗ trợ
    "positive": "#2F6B5C",      # kết quả tốt / giải pháp
    "ink": "#213238",
    "grid": "#DCE3E5",
}

sns.set_theme(style="whitegrid", font_scale=1.05)
plt.rcParams.update({
    "figure.figsize": (12, 6),
    "figure.dpi": 120,
    "axes.titleweight": "bold",
    "axes.titlesize": 15,
    "axes.labelsize": 11,
    "axes.edgecolor": COLORS["grid"],
    "grid.color": COLORS["grid"],
    "grid.alpha": 0.55,
    "font.family": "DejaVu Sans",
})

def finish_chart(ax, title, subtitle=None, xlabel=None, ylabel=None):
    # Áp dụng cùng một chuẩn trình bày cho mọi biểu đồ.
    ax.set_title(title, loc="left", pad=20, color=COLORS["ink"])
    if subtitle:
        ax.text(0, 1.02, subtitle, transform=ax.transAxes, fontsize=10,
                color="#52636A", va="bottom")
    ax.set_xlabel(xlabel or "")
    ax.set_ylabel(ylabel or "")
    ax.spines[["top", "right"]].set_visible(False)
    return ax

def add_bar_labels(ax, fmt="{:.1f}"):
    for container in ax.containers:
        ax.bar_label(container, fmt=fmt, padding=3, fontsize=9, color=COLORS["ink"])
""")

md(r"""
## 2. Dữ liệu và nền tảng tin cậy

- **Nguồn:** bộ dữ liệu mô phỏng 6.000 dự án xây dựng.
- **Đơn vị phân tích:** một dự án.
- **Biến kết quả:** `Số ngày chậm` và trạng thái trễ/đúng hạn.
- **Biến trung tâm:** `Số lần thay đổi thiết kế`.
- **Yếu tố cần kiểm tra:** mưa, thiếu vật tư, giá trị hợp đồng, loại công trình, địa điểm và năm bắt đầu.

Hàm đọc dữ liệu bên dưới ưu tiên file đã giả lập, đồng thời hoạt động khi notebook được chạy từ thư mục dự án hoặc từ thư mục cha.
""")

code(r"""
def locate_data_file():
    candidates = [
        Path("output/data_synthetic_design_dominant.csv"),
        Path("DataStory/DS_Cuoiky/output/data_synthetic_design_dominant.csv"),
        Path("data_synthetic_design_dominant.csv"),
    ]
    for path in candidates:
        if path.exists():
            return path
    raise FileNotFoundError("Không tìm thấy data_synthetic_design_dominant.csv")

DATA_PATH = locate_data_file()
df_raw = pd.read_csv(DATA_PATH)
print(f"Đã đọc: {DATA_PATH.resolve()}")
print(f"Quy mô: {df_raw.shape[0]:,} dự án × {df_raw.shape[1]} trường")
display(df_raw.head(3))
""")

md("### 2.1. Hàm chuẩn hóa và tạo biến phân tích")

code(r"""
def parse_currency_billion(value):
    # Quy đổi chuỗi hợp đồng về tỷ VNĐ; hỗ trợ B, tỷ, triệu và dấu phẩy thập phân.
    if pd.isna(value):
        return np.nan
    text = str(value).strip().lower().replace(" ", "").replace(",", ".")
    is_million = "triệu" in text or "trieu" in text
    match = re.search(r"-?\d+(?:\.\d+)?", text)
    if not match:
        return np.nan
    number = float(match.group())
    return number / 1_000 if is_million or number > 1_000 else number

def prepare_data(raw):
    # Chuẩn hóa kiểu dữ liệu, kiểm tra quan hệ ngày và tạo feature phục vụ câu chuyện.
    df = raw.copy()
    df.columns = df.columns.str.strip()

    date_cols = ["Ngày bắt đầu", "Ngày kết thúc theo hợp đồng", "Ngày kết thúc thực tế"]
    for col in date_cols:
        df[col] = pd.to_datetime(df[col], dayfirst=True, errors="coerce")

    numeric_cols = ["Số ngày chậm", "Số lần thay đổi thiết kế", "Số ngày mưa", "Số lần thiếu vật tư"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df["Giá trị hợp đồng (Tỷ VNĐ)"] = df["Giá trị hợp đồng"].map(parse_currency_billion)
    df["Có thay đổi thiết kế"] = np.where(df["Số lần thay đổi thiết kế"] > 0, "Có thay đổi", "Không thay đổi")
    df["Trạng thái"] = np.where(df["Số ngày chậm"] > 0, "Trễ hạn", "Đúng/Sớm hạn")
    df["Năm bắt đầu"] = df["Ngày bắt đầu"].dt.year
    df["Độ lệch ngày kiểm tra"] = (
        (df["Ngày kết thúc thực tế"] - df["Ngày kết thúc theo hợp đồng"]).dt.days
        - df["Số ngày chậm"]
    )

    bins = [-0.1, 0, 1, 2, 5, 10, np.inf]
    labels = ["0", "1", "2", "3–5", "6–10", ">10"]
    df["Nhóm số lần thay đổi"] = pd.cut(
        df["Số lần thay đổi thiết kế"], bins=bins, labels=labels, include_lowest=True
    )
    return df

df = prepare_data(df_raw)
display(df.head(3))
""")

md("### 2.2. Kiểm tra chất lượng và tính nhất quán")

code(r"""
def data_quality_report(df):
    key_cols = [
        "STT", "Tên dự án", "Ngày kết thúc theo hợp đồng", "Ngày kết thúc thực tế",
        "Số ngày chậm", "Số lần thay đổi thiết kế", "Số ngày mưa", "Số lần thiếu vật tư"
    ]
    checks = {
        "Số dòng": len(df),
        "STT trùng": int(df["STT"].duplicated().sum()),
        "Thiếu ở trường trọng yếu": int(df[key_cols].isna().sum().sum()),
        "Số lần thay đổi âm": int((df["Số lần thay đổi thiết kế"] < 0).sum()),
        "Ngày thực tế không khớp số ngày chậm": int((df["Độ lệch ngày kiểm tra"].fillna(0) != 0).sum()),
    }
    return pd.DataFrame({"Kiểm tra": checks.keys(), "Kết quả": checks.values()})

quality = data_quality_report(df)
display(quality)

assert len(df) == 6000, "Quy mô dữ liệu khác kỳ vọng"
assert df["STT"].duplicated().sum() == 0, "STT bị trùng"
assert (df["Độ lệch ngày kiểm tra"].fillna(0) == 0).all(), "Ngày và số ngày chậm không nhất quán"
print("✓ Các kiểm tra trọng yếu đều đạt.")
""")

md(r"""
### 2.3. Relevance, trustworthiness và giới hạn

**Điểm phù hợp:** Dữ liệu có đầy đủ biến kết quả, biến thiết kế và các yếu tố vận hành thường được dùng để giải thích chậm tiến độ.

**Điểm đáng tin trong nội bộ bộ dữ liệu:** 6.000 quan sát, không trùng mã, kiểu dữ liệu đã chuẩn hóa và quan hệ giữa ngày kế hoạch–ngày thực tế–số ngày chậm được kiểm tra tự động.

**Giới hạn quan trọng:** Vì là dữ liệu mô phỏng, cường độ quan hệ được tạo theo kịch bản. Phân tích có thể chứng minh **tính nhất quán trong bộ dữ liệu**, nhưng không thể tự động suy rộng thành quan hệ nhân quả ở doanh nghiệp thật. Một thử nghiệm pilot hoặc dữ liệu thực trước–sau Design Freeze là bước xác nhận bắt buộc.
""")

md("## 3. Narrative Arc — Context: bức tranh tiến độ")

code(r"""
def make_kpi_table(df):
    late = df["Số ngày chậm"] > 0
    return pd.DataFrame({
        "Chỉ số": ["Tổng dự án", "Tỷ lệ trễ hạn", "Chậm TB của dự án trễ", "Dự án có đổi thiết kế"],
        "Giá trị": [
            f"{len(df):,}", f"{late.mean():.1%}",
            f"{df.loc[late, 'Số ngày chậm'].mean():.1f} ngày",
            f"{(df['Số lần thay đổi thiết kế'] > 0).mean():.1%}",
        ]
    })

display(make_kpi_table(df))

status = (
    df["Trạng thái"].value_counts(normalize=True)
      .reindex(["Đúng/Sớm hạn", "Trễ hạn"]).mul(100)
)
fig, ax = plt.subplots(figsize=(10, 4.8))
bars = ax.barh(status.index, status.values,
               color=[COLORS["positive"], COLORS["design"]], height=0.55)
ax.bar_label(bars, labels=[f"{v:.1f}%" for v in status.values], padding=5, fontsize=12, fontweight="bold")
ax.set_xlim(0, 105)
finish_chart(
    ax,
    "Context | Tiến độ chia thành hai trạng thái rất khác nhau",
    "Tỷ trọng dự án theo trạng thái; trục bắt đầu từ 0 để tránh phóng đại khác biệt",
    xlabel="Tỷ lệ dự án (%)",
)
plt.show()
""")

md(r"""
## 4. Hook: chỉ một lần đổi thiết kế cũng làm hồ sơ rủi ro đảo chiều

Hook không bắt đầu từ một hệ số khó hiểu. Ta đặt hai nhóm cạnh nhau trên cùng đường cơ sở: dự án **không đổi** và **có đổi** thiết kế.
""")

code(r"""
def compare_design_groups(df):
    return (
        df.groupby("Có thay đổi thiết kế", observed=True)
          .agg(
              Số_dự_án=("STT", "count"),
              Tỷ_lệ_trễ=("Số ngày chậm", lambda s: (s > 0).mean()),
              Chậm_trung_bình=("Số ngày chậm", "mean"),
              Trung_vị=("Số ngày chậm", "median"),
          )
          .reindex(["Không thay đổi", "Có thay đổi"])
    )

group_compare = compare_design_groups(df)
group_compare_display = group_compare.copy()
group_compare_display["Tỷ_lệ_trễ"] = group_compare_display["Tỷ_lệ_trễ"].map(lambda x: f"{x:.1%}")
display(group_compare_display.round(1))

fig, axes = plt.subplots(1, 2, figsize=(13, 5))
palette = [COLORS["baseline"], COLORS["design"]]

axes[0].bar(group_compare.index, group_compare["Tỷ_lệ_trễ"] * 100, color=palette, width=0.62)
axes[0].set_ylim(0, 110)
add_bar_labels(axes[0], "%.1f")
finish_chart(axes[0], "Xác suất trễ hạn", "Có thay đổi so với không thay đổi", ylabel="Tỷ lệ trễ (%)")

axes[1].bar(group_compare.index, group_compare["Chậm_trung_bình"], color=palette, width=0.62)
axes[1].axhline(0, color=COLORS["ink"], linewidth=0.8)
add_bar_labels(axes[1], "%.1f")
finish_chart(axes[1], "Mức độ trễ trung bình", "Giá trị âm nghĩa là hoàn thành sớm", ylabel="Số ngày chậm")

fig.suptitle("Hook | Có thay đổi thiết kế là một trạng thái rủi ro hoàn toàn khác", x=0.06, ha="left", fontsize=16, fontweight="bold")
plt.tight_layout()
plt.show()
""")

md(r"""
## 5. Rising Insight 1: tồn tại quan hệ “liều–đáp ứng”

Nếu thay đổi thiết kế thực sự là tín hiệu trung tâm, mức chậm không chỉ khác giữa hai nhóm; nó phải tăng có trật tự khi số vòng sửa tăng. Các mức hiếm được gộp thành nhóm để tránh chartjunk và giảm nguy cơ “Texas sharpshooter”.
""")

code(r"""
def dose_response_table(df):
    return (
        df.groupby("Nhóm số lần thay đổi", observed=False)
          .agg(
              Số_dự_án=("STT", "count"),
              Chậm_TB=("Số ngày chậm", "mean"),
              Tỷ_lệ_trễ=("Số ngày chậm", lambda s: (s > 0).mean()),
          )
          .reset_index()
    )

dose = dose_response_table(df)
dose_display = dose.copy()
dose_display["Tỷ_lệ_trễ"] = dose_display["Tỷ_lệ_trễ"].map(lambda x: f"{x:.1%}")
display(dose_display.round(1))

fig, ax = plt.subplots(figsize=(11, 5.5))
colors = [COLORS["baseline"]] + [COLORS["design"]] * (len(dose) - 1)
bars = ax.bar(dose["Nhóm số lần thay đổi"].astype(str), dose["Chậm_TB"], color=colors, width=0.68)
ax.axhline(0, color=COLORS["ink"], linewidth=0.8)
ax.bar_label(bars, labels=[f"{v:.1f}" for v in dose["Chậm_TB"]], padding=4, fontsize=10, fontweight="bold")
finish_chart(
    ax,
    "Rising Insight | Mỗi tầng thay đổi thiết kế kéo tiến độ trượt xa hơn",
    "Số ngày chậm trung bình theo nhóm số vòng sửa; cỡ mẫu được trình bày trong bảng phía trên",
    xlabel="Số lần thay đổi thiết kế", ylabel="Số ngày chậm trung bình",
)
plt.show()
""")

md(r"""
## 6. Rising Insight 2: kiểm tra yếu tố nhiễu và độ bền của insight

Để giảm **confirmation bias**, ta không chỉ nhìn biểu đồ thuận lợi cho giả thuyết. Hai kiểm tra được thực hiện:

1. So sánh hệ số chuẩn hóa của thay đổi thiết kế với mưa, thiếu vật tư và quy mô hợp đồng.
2. Kiểm tra tương quan thay đổi thiết kế–độ trễ trong từng loại công trình, tránh kết luận chỉ do một phân khúc đặc biệt.

Các hệ số dưới đây mang ý nghĩa dự báo trong dữ liệu, không tự động là tác động nhân quả.
""")

code(r"""
def standardized_regression(df):
    features = [
        "Số lần thay đổi thiết kế", "Số ngày mưa",
        "Số lần thiếu vật tư", "Giá trị hợp đồng (Tỷ VNĐ)"
    ]
    model_df = df[features + ["Số ngày chậm"]].dropna().copy()
    X = model_df[features]
    Xz = (X - X.mean()) / X.std(ddof=0)
    yz = (model_df["Số ngày chậm"] - model_df["Số ngày chậm"].mean()) / model_df["Số ngày chậm"].std(ddof=0)
    design = np.column_stack([np.ones(len(Xz)), Xz.values])
    beta = np.linalg.lstsq(design, yz.values, rcond=None)[0][1:]
    pred = design @ np.r_[np.linalg.lstsq(design, yz.values, rcond=None)[0][0], beta]
    r2 = 1 - ((yz.values - pred) ** 2).sum() / ((yz.values - yz.mean()) ** 2).sum()
    return pd.DataFrame({"Yếu tố": features, "Hệ số chuẩn hóa": beta}).sort_values("Hệ số chuẩn hóa"), r2

coef, r2 = standardized_regression(df)
display(coef.round(3))
print(f"R² của mô hình mô tả: {r2:.3f}")

fig, ax = plt.subplots(figsize=(10, 5))
bar_colors = [COLORS["design"] if x == "Số lần thay đổi thiết kế" else COLORS["baseline"] for x in coef["Yếu tố"]]
bars = ax.barh(coef["Yếu tố"], coef["Hệ số chuẩn hóa"], color=bar_colors)
ax.axvline(0, color=COLORS["ink"], linewidth=0.8)
ax.bar_label(bars, labels=[f"{v:.3f}" for v in coef["Hệ số chuẩn hóa"]], padding=4)
finish_chart(
    ax,
    "Kiểm tra yếu tố nhiễu | Tín hiệu thiết kế vẫn áp đảo",
    "Hệ số hồi quy chuẩn hóa; so sánh độ mạnh tương đối, không diễn giải là nhân quả",
    xlabel="Hệ số chuẩn hóa",
)
plt.show()
""")

code(r"""
def segment_robustness(df, min_n=80):
    rows = []
    for segment, part in df.groupby("Loại công trinh"):
        if len(part) >= min_n and part["Số lần thay đổi thiết kế"].nunique() > 1:
            rows.append({
                "Loại công trình": segment,
                "Số dự án": len(part),
                "Tương quan": part["Số lần thay đổi thiết kế"].corr(part["Số ngày chậm"]),
            })
    return pd.DataFrame(rows).sort_values("Tương quan")

robustness = segment_robustness(df)
display(robustness.round(3))

fig, ax = plt.subplots(figsize=(10, 5.5))
bars = ax.barh(robustness["Loại công trình"], robustness["Tương quan"], color=COLORS["support"])
ax.set_xlim(0, 1.05)
ax.bar_label(bars, labels=[f"{v:.2f}" for v in robustness["Tương quan"]], padding=4)
finish_chart(
    ax,
    "Kiểm tra phân khúc | Quan hệ cùng chiều xuất hiện ở mọi loại công trình đủ mẫu",
    "Tương quan Pearson trong từng phân khúc; chỉ hiển thị nhóm có ít nhất 80 dự án",
    xlabel="Tương quan với số ngày chậm",
)
plt.show()
""")

md(r"""
## 7. Aha Moment: thiết kế không chỉ “có liên quan” — nó tạo thành một thang trượt tiến độ

Ta lượng hóa đường xu hướng trên toàn bộ dữ liệu. Đây là khoảnh khắc cô đọng thông điệp để khán giả dễ nhớ: **mỗi vòng sửa thêm đi cùng khoảng bao nhiêu ngày chậm**.
""")

code(r"""
def linear_design_effect(df):
    x = df["Số lần thay đổi thiết kế"].to_numpy(float)
    y = df["Số ngày chậm"].to_numpy(float)
    slope, intercept = np.polyfit(x, y, 1)
    corr = np.corrcoef(x, y)[0, 1]
    return slope, intercept, corr

slope, intercept, corr = linear_design_effect(df)
summary_by_x = (
    df.groupby("Số lần thay đổi thiết kế")
      .agg(Chậm_TB=("Số ngày chậm", "mean"), Số_dự_án=("STT", "count"))
      .reset_index()
)

fig, ax = plt.subplots(figsize=(12, 6))
sizes = np.clip(np.sqrt(summary_by_x["Số_dự_án"]) * 7, 25, 220)
ax.scatter(
    summary_by_x["Số lần thay đổi thiết kế"], summary_by_x["Chậm_TB"],
    s=sizes, color=COLORS["design"], alpha=0.82, edgecolor="white", linewidth=0.8,
)
xline = np.linspace(df["Số lần thay đổi thiết kế"].min(), df["Số lần thay đổi thiết kế"].max(), 200)
ax.plot(xline, intercept + slope * xline, color=COLORS["ink"], linewidth=2, linestyle="--")
ax.axhline(0, color=COLORS["baseline"], linewidth=1)
ax.text(
    0.98, 0.08,
    f"Mỗi vòng sửa thêm ≈ {slope:.1f} ngày chậm\nTương quan r = {corr:.3f}",
    transform=ax.transAxes, ha="right", va="bottom", fontsize=13, fontweight="bold",
    color=COLORS["design"], bbox=dict(boxstyle="round,pad=0.5", facecolor="white", edgecolor=COLORS["design"]),
)
finish_chart(
    ax,
    "Aha Moment | Mỗi vòng sửa bản vẽ đẩy dự án xuống thêm một nấc tiến độ",
    "Mỗi điểm là một mức số lần thay đổi; kích thước điểm thể hiện số dự án",
    xlabel="Số lần thay đổi thiết kế", ylabel="Số ngày chậm trung bình",
)
plt.show()
""")

md(r"""
## 8. Solution: mô phỏng tác động của Design Freeze

Kịch bản hành động được diễn đạt thận trọng dưới dạng **what-if**, không phải dự báo đã được kiểm chứng:

- Mỗi dự án có thay đổi thiết kế được giảm tối đa **1 vòng sửa** nhờ Design Freeze và Change Control Board.
- Số ngày có thể tránh được ước tính bằng hệ số đường xu hướng, nhưng không làm độ trễ giảm dưới 0.
- Không quy đổi trực tiếp thành tiền khi chưa có dữ liệu chi phí chậm tiến độ đáng tin cậy.
""")

code(r"""
def simulate_design_freeze(df, slope, revisions_removed=1):
    result = df[["STT", "Số ngày chậm", "Số lần thay đổi thiết kế"]].copy()
    result["Số vòng sửa giảm"] = np.minimum(result["Số lần thay đổi thiết kế"], revisions_removed)
    result["Ngày chậm có thể tránh"] = np.minimum(
        result["Số ngày chậm"].clip(lower=0),
        result["Số vòng sửa giảm"] * max(slope, 0),
    )
    result["Số ngày chậm sau kịch bản"] = result["Số ngày chậm"] - result["Ngày chậm có thể tránh"]
    return result

scenario = simulate_design_freeze(df, slope=slope, revisions_removed=1)
before = df["Số ngày chậm"].clip(lower=0).sum()
after = scenario["Số ngày chậm sau kịch bản"].clip(lower=0).sum()
avoidable = scenario["Ngày chậm có thể tránh"].sum()

impact = pd.DataFrame({
    "Chỉ số": ["Tổng ngày chậm hiện tại", "Ngày chậm sau kịch bản", "Ngày chậm có thể tránh", "Tỷ lệ giảm tiềm năng"],
    "Giá trị": [f"{before:,.0f}", f"{after:,.0f}", f"{avoidable:,.0f}", f"{avoidable / before:.1%}"],
})
display(impact)

fig, ax = plt.subplots(figsize=(9, 5))
values = [before, after]
bars = ax.bar(["Hiện tại", "Sau Design Freeze\n(kịch bản)"], values,
              color=[COLORS["design"], COLORS["positive"]], width=0.58)
ax.bar_label(bars, labels=[f"{v:,.0f}" for v in values], padding=5, fontsize=11, fontweight="bold")
ax.set_ylim(0, max(values) * 1.18)
finish_chart(
    ax,
    "Solution | Giảm một vòng sửa có thể thu hồi một phần đáng kể quỹ tiến độ",
    "Mô phỏng what-if, không phải cam kết kết quả; tổng số ngày chậm dương của 6.000 dự án",
    ylabel="Tổng số ngày chậm",
)
plt.show()
""")

md(r"""
## 9. Next Steps và cơ chế đo lường

### Hành động đề xuất

1. **Design Freeze theo stage-gate:** chốt yêu cầu và bản vẽ tại mốc trước mua sắm/thi công.
2. **Change Control Board:** mọi thay đổi sau freeze phải có người phê duyệt, lý do, tác động thời gian và chi phí.
3. **SLA 48 giờ:** đánh giá tác động và quyết định xử lý trong 48 giờ từ khi phát sinh yêu cầu.
4. **Pilot có đối chứng:** áp dụng tại một nhóm dự án và so sánh với nhóm tương đồng chưa áp dụng.

### KPI đo lường

| KPI | Định nghĩa | Tần suất | Mục đích |
|---|---|---|---|
| Tỷ lệ thay đổi sau Design Freeze | Số change order sau freeze / tổng change order | Tuần | Đo kỷ luật thiết kế |
| Số vòng sửa mỗi dự án | Tổng lần thay đổi thiết kế / dự án | Tuần | Theo dõi tác nhân dẫn dắt |
| Ngày chậm trên mỗi vòng sửa | Tổng ngày chậm / số vòng sửa | Tháng | Đo khả năng hấp thụ thay đổi |
| Tỷ lệ phản hồi trong 48 giờ | Yêu cầu được xử lý đúng SLA / tổng yêu cầu | Tuần | Đo tốc độ quản trị |
| Tỷ lệ đúng hạn | Dự án có số ngày chậm ≤ 0 / tổng dự án | Tháng | Đo kết quả cuối cùng |

### Ngưỡng đánh giá pilot

- So sánh trước–sau và với nhóm đối chứng tương đồng về loại công trình/quy mô.
- Theo dõi ít nhất một chu kỳ dự án đủ dài.
- Chỉ tuyên bố hiệu quả khi số vòng sửa **và** số ngày chậm cùng giảm, không chọn riêng KPI thuận lợi.
""")

md(r"""
## 10. Kiểm soát bias và ngụy biện — checklist bảo vệ khi Q&A

| Rủi ro | Cách notebook xử lý | Điều chưa thể khẳng định |
|---|---|---|
| Confirmation bias | So sánh thêm mưa, vật tư, quy mô hợp đồng | Không loại trừ mọi biến ẩn |
| Correlation fallacy | Gọi kết quả là quan hệ dự báo; đề xuất pilot | Chưa chứng minh nhân quả ngoài dữ liệu mô phỏng |
| Texas sharpshooter | Nhóm mức thay đổi được định nghĩa trước, hiển thị cỡ mẫu | Các nhóm hiếm vẫn cần dữ liệu thực xác nhận |
| Hasty generalization | Kiểm tra theo loại công trình, nêu rõ phạm vi 6.000 dự án mô phỏng | Không suy rộng sang toàn ngành |
| Survivorship bias | Một dòng tương ứng một dự án trong bộ dữ liệu hoàn chỉnh | Chưa có dự án đang dở dang/hủy bỏ |
| Curse of knowledge | Tiêu đề biểu đồ viết thành câu kết luận, dùng cùng mã màu | Cần thử nghiệm với người nghe thực tế |

### Kết luận một câu

> **Đừng để mỗi vòng sửa bản vẽ trở thành một vòng trượt tiến độ: khóa thiết kế đúng mốc, kiểm soát mọi thay đổi sau freeze và đo hiệu quả bằng dữ liệu pilot.**
""")

md(r"""
## 11. Phụ lục: xuất bảng phân tích dùng cho báo cáo/slide

Cell dưới đây tạo các bảng CSV gọn để dùng lại. Mặc định không chạy ghi file ngoài ý muốn; đổi `EXPORT_TABLES = True` khi cần.
""")

code(r"""
EXPORT_TABLES = False

if EXPORT_TABLES:
    export_dir = Path("analysis_outputs")
    export_dir.mkdir(exist_ok=True)
    quality.to_csv(export_dir / "01_data_quality.csv", index=False, encoding="utf-8-sig")
    group_compare.reset_index().to_csv(export_dir / "02_design_group_comparison.csv", index=False, encoding="utf-8-sig")
    dose.to_csv(export_dir / "03_dose_response.csv", index=False, encoding="utf-8-sig")
    coef.to_csv(export_dir / "04_standardized_coefficients.csv", index=False, encoding="utf-8-sig")
    impact.to_csv(export_dir / "05_design_freeze_impact.csv", index=False, encoding="utf-8-sig")
    print(f"Đã xuất bảng tại: {export_dir.resolve()}")
else:
    print("EXPORT_TABLES=False — chưa ghi thêm file. Notebook đã sẵn sàng để trình bày.")
""")

with OUTPUT.open("w", encoding="utf-8") as f:
    nbf.write(nb, f)

print(f"Created {OUTPUT} with {len(nb.cells)} cells")
