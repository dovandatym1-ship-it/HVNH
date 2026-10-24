from pathlib import Path
import inspect
import json
import shutil
import re

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "output" / "du_lieu_tien_do_du_an.csv"
SOURCE_XLSX = ROOT / "output" / "du_lieu_tien_do_du_an.xlsx"
NOTEBOOK = ROOT / "lecture3.ipynb"
REPORT_V1 = ROOT / "final_submission" / "Bao_cao_Data_Storytelling.md"
OUT = ROOT / "final_submission_v2"
CHARTS = OUT / "charts"

RED = "#B83A32"
NAVY = "#23363D"
GREEN = "#2F6B5C"
GRAY = "#AEB7BB"
MUTED = "#617178"

sns.set_theme(style="white", font_scale=1.04)
plt.rcParams.update({
    "figure.dpi": 160,
    "font.family": "DejaVu Sans",
    "axes.titleweight": "bold",
    "axes.titlesize": 15,
    "axes.labelsize": 11,
    "axes.edgecolor": "#D6DEE1",
    "xtick.color": NAVY,
    "ytick.color": NAVY,
    "text.color": NAVY,
})

def currency(v):
    if pd.isna(v): return np.nan
    s = str(v).lower().replace(" ", "").replace(",", ".")
    m = re.search(r"\d+(?:\.\d+)?", s)
    if not m: return np.nan
    n = float(m.group())
    return n / 1000 if "triệu" in s or n > 1000 else n

def vi_num(v, digits=1):
    """Định dạng số theo quy ước tiếng Việt: dấu phẩy thập phân, dấu chấm hàng nghìn."""
    return f"{v:,.{digits}f}".replace(",", "_").replace(".", ",").replace("_", ".")

def vi_int(v):
    return f"{v:,.0f}".replace(",", ".")

def load_data():
    d = pd.read_csv(SOURCE)
    for c in ["Ngày bắt đầu", "Ngày kết thúc theo hợp đồng", "Ngày kết thúc thực tế"]:
        d[c] = pd.to_datetime(d[c], dayfirst=True, errors="coerce")
    d["Giá trị hợp đồng (Tỷ VNĐ)"] = d["Giá trị hợp đồng"].map(currency)
    d["Trạng thái"] = np.where(d["Số ngày chậm"] > 0, "Trễ hạn", "Đúng/Sớm hạn")
    d["Thiết kế"] = np.where(d["Số lần thay đổi thiết kế"] > 0, "Có thay đổi", "Không thay đổi")
    d["Năm bắt đầu"] = d["Ngày bắt đầu"].dt.year
    d["Nhóm thay đổi"] = pd.cut(
        d["Số lần thay đổi thiết kế"], [-.1, 0, 1, 2, 4, 6, 8],
        labels=["0", "1", "2", "3–4", "5–6", "7–8"], include_lowest=True
    )
    d["Nhóm phân phối"] = pd.cut(
        d["Số lần thay đổi thiết kế"], [-.1, 0, 2, 5, np.inf],
        labels=["0", "1–2", "3–5", ">5"], include_lowest=True
    )
    return d

def title(ax, main, sub=""):
    ax.set_title(main, loc="left", pad=22, color=NAVY)
    if sub:
        ax.text(0, 1.015, sub, transform=ax.transAxes, color=MUTED, fontsize=10, va="bottom")

def clean(ax, grid="x"):
    ax.spines[["top", "right"]].set_visible(False)
    if grid:
        ax.grid(axis=grid, color="#DFE6E8", linewidth=.8, alpha=.9)
        ax.set_axisbelow(True)

def save(fig, filename):
    fig.tight_layout()
    fig.savefig(CHARTS / filename, bbox_inches="tight", facecolor="white")
    plt.close(fig)

def coefficients(d):
    features = ["Số lần thay đổi thiết kế", "Số ngày mưa", "Số lần thiếu vật tư", "Giá trị hợp đồng (Tỷ VNĐ)"]
    m = d[features + ["Số ngày chậm"]].dropna()
    X = (m[features] - m[features].mean()) / m[features].std(ddof=0)
    y = (m["Số ngày chậm"] - m["Số ngày chậm"].mean()) / m["Số ngày chậm"].std(ddof=0)
    A = np.column_stack([np.ones(len(X)), X])
    beta = np.linalg.lstsq(A, y, rcond=None)[0]
    pred = A @ beta
    r2 = 1 - ((y - pred) ** 2).sum() / ((y - y.mean()) ** 2).sum()
    return pd.DataFrame({"Yếu tố": features, "Hệ số": beta[1:]}).sort_values("Hệ số"), r2

def make_charts(d):
    # 01 — thanh tỷ lệ tổng thể
    late_pct = int(round((d["Số ngày chậm"] > 0).mean() * 100))
    fig, ax = plt.subplots(figsize=(11, 4.6))
    ax.barh([0], [late_pct], color=RED, height=.5, label="Trễ hạn")
    ax.barh([0], [100-late_pct], left=[late_pct], color=GREEN, height=.5, label="Đúng hoặc sớm hạn")
    ax.text(late_pct/2, 0, f"Trễ hạn\n{late_pct}%", ha="center", va="center", color="white", fontsize=16, fontweight="bold")
    ax.text(late_pct+(100-late_pct)/2, 0, f"Đúng hoặc sớm hạn\n{100-late_pct}%", ha="center", va="center", color="white", fontsize=13, fontweight="bold")
    ax.set_xlim(0, 100); ax.set_yticks([]); ax.set_xlabel("Tỷ lệ dự án (%)")
    title(ax, f"{late_pct}% dự án hoàn thành sau thời hạn hợp đồng", "Tỷ lệ được tính trên toàn bộ 6.000 dự án")
    clean(ax, "x")
    save(fig, "01_thanh_ty_le_tien_do.png")

    # 02 — hai biểu đồ cột so sánh hai nhóm
    g = d.groupby("Thiết kế").agg(
        ty_le_tre=("Số ngày chậm", lambda s: (s > 0).mean() * 100),
        cham_tb=("Số ngày chậm", "mean")
    ).reindex(["Không thay đổi", "Có thay đổi"])
    fig, axes = plt.subplots(1, 2, figsize=(13, 4.8))
    specs = [("ty_le_tre", "Tỷ lệ trễ hạn", "%", (0, 100)), ("cham_tb", "Số ngày chậm trung bình", " ngày", (-3, 12))]
    for ax, (col, ttl, unit, lim) in zip(axes, specs):
        vals = g[col].values
        bars = ax.bar(["Không thay đổi", "Có thay đổi"], vals, color=[GRAY, RED], width=.6)
        for bar, val in zip(bars, vals):
            ax.text(bar.get_x()+bar.get_width()/2, val + (.8 if val >= 0 else -.8), f"{vi_num(val)}{unit}", ha="center", va="bottom" if val >= 0 else "top", fontweight="bold")
        ax.set_ylim(*lim); ax.set_ylabel(ttl); ax.axhline(0, color=NAVY, lw=.8)
        clean(ax, "y")
    fig.suptitle("Dự án có thay đổi thiết kế trễ nhiều hơn", x=.06, ha="left", fontsize=16, fontweight="bold")
    save(fig, "02_cot_so_sanh_hai_nhom.png")

    # 03 — đường xu hướng theo mức thay đổi
    level_summary = d.groupby("Nhóm thay đổi", observed=False).agg(cham_tb=("Số ngày chậm", "mean"), n=("STT", "count")).reset_index()
    x = np.arange(len(level_summary))
    fig, ax = plt.subplots(figsize=(11.5, 5.8))
    ax.plot(x, level_summary.cham_tb, color=RED, lw=3, marker="o", markersize=9)
    for xi, y, n in zip(x, level_summary.cham_tb, level_summary.n):
        ax.text(xi, y + 5, vi_num(y), ha="center", fontweight="bold")
        ax.text(xi, y - 9, f"n={vi_int(n)}", ha="center", fontsize=9, color=MUTED)
    ax.set_xticks(x, level_summary["Nhóm thay đổi"].astype(str)); ax.axhline(0, color=NAVY, lw=.8); ax.set_ylim(-10, 45)
    ax.set_ylabel("Số ngày chậm trung bình"); ax.set_xlabel("Số lần thay đổi thiết kế")
    title(ax, "Độ trễ tăng theo từng mức thay đổi thiết kế", "Số dự án ở từng nhóm được ghi ngay dưới điểm dữ liệu")
    clean(ax, "y")
    save(fig, "03_duong_muc_thay_doi.png")

    # 04 — biểu đồ phân tán với đường xu hướng
    slope, intercept = np.polyfit(d["Số lần thay đổi thiết kế"], d["Số ngày chậm"], 1)
    corr = d["Số lần thay đổi thiết kế"].corr(d["Số ngày chậm"])
    fig, ax = plt.subplots(figsize=(11.5, 6))
    max_design = int(d["Số lần thay đổi thiết kế"].max())
    jitter = np.random.default_rng(17).normal(0, .07, len(d))
    ax.scatter(d["Số lần thay đổi thiết kế"] + jitter, d["Số ngày chậm"], s=10, alpha=.12, color=RED, edgecolors="none")
    xx = np.linspace(0, max_design, 200); ax.plot(xx, intercept + slope * xx, color=NAVY, lw=2.2, linestyle="--")
    ax.text(.97, .08, f"Độ dốc: {vi_num(slope)} ngày/lần\nr = {vi_num(corr, 3)}", transform=ax.transAxes,
            ha="right", fontweight="bold", color=RED, bbox=dict(facecolor="white", edgecolor=RED, boxstyle="round,pad=.45"))
    ax.set_xlabel("Số lần thay đổi thiết kế"); ax.set_ylabel("Số ngày chậm")
    title(ax, "Số ngày chậm có xu hướng tăng khi số lần thay đổi tăng", "Mỗi điểm là một dự án; đường nét đứt thể hiện xu hướng trung bình")
    clean(ax, "y")
    save(fig, "04_phan_tan_xu_huong.png")

    # 05 — thanh ngang hệ số chuẩn hóa
    coef, r2 = coefficients(d)
    fig, ax = plt.subplots(figsize=(10.5, 5.5))
    colors = [RED if name == "Số lần thay đổi thiết kế" else GRAY for name in coef["Yếu tố"]]
    bars = ax.barh(coef["Yếu tố"], coef["Hệ số"], color=colors, height=.58)
    for bar, val, name in zip(bars, coef["Hệ số"], coef["Yếu tố"]):
        ax.text(val + .012, bar.get_y()+bar.get_height()/2, vi_num(val, 3), va="center", fontweight="bold" if name == "Số lần thay đổi thiết kế" else "normal")
    ax.axvline(0, color=NAVY, lw=.8)
    ax.set_xlim(min(-.06, coef["Hệ số"].min() - .04), max(.45, coef["Hệ số"].max() + .08))
    ax.set_xlabel("Hệ số hồi quy chuẩn hóa")
    ax.xaxis.set_major_formatter(lambda x, pos: vi_num(x, 1))
    title(ax, "Thay đổi thiết kế có hệ số chuẩn hóa lớn nhất", f"Mô hình có R² = {vi_num(r2, 3)}; kết quả không được dùng để khẳng định quan hệ nhân quả")
    clean(ax, "x")
    save(fig, "05_thanh_he_so_chuan_hoa.png")

    # 06 — cột ngang theo loại công trình và trạng thái thay đổi
    seg = d.pivot_table(index="Loại công trinh", columns="Thiết kế", values="Số ngày chậm", aggfunc="mean").reindex(columns=["Không thay đổi", "Có thay đổi"])
    seg = seg.sort_values("Có thay đổi")
    fig, ax = plt.subplots(figsize=(11.5, 6.2))
    y = np.arange(len(seg)); h=.34
    b1=ax.barh(y-h/2, seg["Không thay đổi"], height=h, color=GRAY, label="Không thay đổi")
    b2=ax.barh(y+h/2, seg["Có thay đổi"], height=h, color=RED, label="Có thay đổi")
    for bars in [b1,b2]:
        for bar in bars: ax.text(bar.get_width()+.2, bar.get_y()+bar.get_height()/2, vi_num(bar.get_width()), va="center", fontsize=9)
    ax.set_yticks(y, seg.index); ax.axvline(0,color=NAVY,lw=.8); ax.set_xlabel("Số ngày chậm trung bình")
    ax.legend(frameon=False, ncol=2, loc="lower right")
    title(ax, "Nhóm có thay đổi thiết kế trễ hơn ở mọi loại công trình", "So sánh số ngày chậm trung bình trong từng loại công trình")
    clean(ax, "x")
    save(fig, "06_cot_nhom_loai_cong_trinh.png")

    # 07 — year trends by design status
    yr = d.groupby(["Năm bắt đầu", "Thiết kế"]).agg(cham_tb=("Số ngày chậm", "mean")).reset_index()
    fig, ax = plt.subplots(figsize=(10.5, 5.5))
    for label, color, marker in [("Không thay đổi", GRAY, "o"), ("Có thay đổi", RED, "s")]:
        p = yr[yr["Thiết kế"] == label]
        ax.plot(p["Năm bắt đầu"], p.cham_tb, color=color, marker=marker, lw=2.6, markersize=7, label=label)
        for xv, yv in zip(p["Năm bắt đầu"], p.cham_tb):
            ax.text(xv, yv + (.75 if label == "Có thay đổi" else -.75), vi_num(yv), ha="center", va="bottom" if label == "Có thay đổi" else "top", color=color, fontsize=9)
    ax.axhline(0, color=NAVY, lw=.8); ax.set_xticks(sorted(d["Năm bắt đầu"].dropna().unique()))
    ax.set_ylim(-2.8, 10.7)
    ax.set_xlabel("Năm bắt đầu"); ax.set_ylabel("Số ngày chậm trung bình")
    ax.legend(frameon=False, ncol=2, loc="center", bbox_to_anchor=(.5, .47))
    title(ax, "Khoảng cách giữa hai nhóm được duy trì qua các năm", "Các dự án được nhóm theo năm bắt đầu")
    clean(ax, "y")
    save(fig, "07_duong_theo_nam.png")

    # 08 — ranked cause bars; design is largest without erasing other causes
    cause = d[d["Số ngày chậm"] > 0]["Nguyên nhân chậm tiến độ"].fillna("Chưa xác định").value_counts()
    cause = cause[cause > 0].sort_values(ascending=False)
    shares = cause / cause.sum()
    fig, ax = plt.subplots(figsize=(11.5, 6.2))
    plot = shares.sort_values()
    colors = [RED if name == "Thay đổi thiết kế" else "#BCC6CA" for name in plot.index]
    bars = ax.barh(plot.index, plot.values * 100, color=colors, height=.62)
    for bar, name, share in zip(bars, plot.index, plot.values):
        ax.text(
            bar.get_width() + .7, bar.get_y() + bar.get_height()/2,
            f"{vi_num(share * 100)}% · {vi_int(cause[name])} dự án", va="center",
            color=RED if name == "Thay đổi thiết kế" else NAVY,
            fontweight="bold" if name == "Thay đổi thiết kế" else "normal",
        )
    ax.set_xlim(0, max(45, shares.max() * 100 + 7)); ax.set_xlabel("Tỷ trọng trong các dự án bị trễ")
    design_cause_share = shares.get("Thay đổi thiết kế", 0)
    title(
        ax, "Thay đổi thiết kế là nguyên nhân đơn lẻ lớn nhất",
        f"Chiếm {vi_num(design_cause_share * 100)}% số dự án trễ; {vi_num((1-design_cause_share) * 100)}% còn lại đến từ sáu nhóm nguyên nhân khác",
    )
    clean(ax, "x")
    save(fig, "08_thanh_nguyen_nhan.png")

    # 09 — cột tỷ lệ trễ theo mức thay đổi
    fig, ax = plt.subplots(figsize=(11.5, 6))
    order = ["0", "1–2", "3–5", ">5"]
    rate = d.groupby("Nhóm phân phối", observed=False).agg(ty_le=("Số ngày chậm", lambda s:(s>0).mean()*100), n=("STT","count")).reindex(order)
    bars=ax.bar(order, rate.ty_le, color=[GRAY,"#D8AAA5","#CC746B",RED], width=.65)
    for bar, val, n in zip(bars, rate.ty_le, rate.n):
        ax.text(bar.get_x()+bar.get_width()/2, val+2, f"{vi_num(val)}%\nn={vi_int(n)}", ha="center", fontweight="bold")
    ax.set_ylim(0,105); ax.set_xlabel("Số lần thay đổi thiết kế"); ax.set_ylabel("Tỷ lệ dự án bị trễ (%)")
    title(ax, "Tỷ lệ trễ tăng theo số lần thay đổi thiết kế", "Tỷ lệ được tính riêng trong từng nhóm; cỡ mẫu ghi trên mỗi cột")
    clean(ax, "y")
    save(fig, "09_cot_ty_le_tre_theo_muc.png")

    # 10 — cột trước và sau
    positive = d["Số ngày chậm"].clip(lower=0)
    recovered = np.minimum(positive, np.minimum(d["Số lần thay đổi thiết kế"], 1) * max(slope, 0)).sum()
    before = positive.sum(); after = before - recovered
    fig, ax = plt.subplots(figsize=(10.5, 5.7))
    bars=ax.bar([0,1], [before,after], color=[RED,GREEN], width=.58)
    for bar,val in zip(bars,[before,after]): ax.text(bar.get_x()+bar.get_width()/2,val+1800,vi_int(val),ha="center",fontweight="bold",fontsize=13)
    ax.annotate(f"Giảm {vi_int(recovered)} ngày\n({vi_num(recovered/before*100)}%)", xy=(1,after), xytext=(.5,before*1.06), ha="center", color=NAVY, fontweight="bold", arrowprops=dict(arrowstyle="->",color=NAVY,lw=1.5))
    ax.set_xticks([0,1], ["Hiện tại", "Sau khi giảm\nmột lần thay đổi"])
    ax.set_ylabel("Tổng số ngày chậm"); ax.set_ylim(0, before*1.16)
    title(ax, "Giảm một lần thay đổi có thể làm giảm tổng số ngày chậm", "Phân tích độ nhạy, không phải dự báo hoặc cam kết hiệu quả")
    clean(ax, "y")
    save(fig, "10_cot_truoc_sau.png")
    return slope, corr, r2, before, recovered, after

def rewrite_report(stats):
    slope, corr, r2, before, recovered, after = stats
    d = load_data()
    late_rate = (d["Số ngày chậm"] > 0).mean()
    design_rate = (d["Số lần thay đổi thiết kế"] > 0).mean()
    no_design = d["Số lần thay đổi thiết kế"] == 0
    mean_no = d.loc[no_design, "Số ngày chậm"].mean()
    mean_design = d.loc[~no_design, "Số ngày chậm"].mean()
    late_no = (d.loc[no_design, "Số ngày chậm"] > 0).mean()
    late_design = (d.loc[~no_design, "Số ngày chậm"] > 0).mean()
    cause_share = (
        d.loc[d["Số ngày chậm"] > 0, "Nguyên nhân chậm tiến độ"]
        .value_counts(normalize=True).get("Thay đổi thiết kế", 0)
    )
    text = REPORT_V1.read_text(encoding="utf-8")

    # Giữ độ dài và bố cục 20+ trang, nhưng bỏ cách gọi mang tính quảng cáo hoặc công thức.
    text = re.sub(r"Trang \d+ — ", "", text)
    replacements = {
        "Aha Moment": "Kết luận chính",
        "Aha": "kết luận chính",
        "Rising Insight": "Bằng chứng tiếp theo",
        "Hook": "Điểm mở đầu",
        "hook": "điểm mở đầu",
        "nhân vật chính": "biến trọng tâm",
        "mắt xích quan trọng nhất": "bước kiểm tra quan trọng",
        "Một câu chuyện thuyết phục": "Một phân tích có cơ sở",
        "câu chuyện chuyển sang": "phân tích chuyển sang",
        "câu chuyện không nên": "phân tích không nên",
        "toàn bộ câu chuyện": "toàn bộ kết quả",
        "kẻ": "yếu tố",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)

    metric_replacements = {
        "78.0%": f"{late_rate:.1%}",
        "78%": f"{late_rate:.0%}",
        "100% ở nhóm có thay đổi": f"{late_design:.1%} ở nhóm có thay đổi",
        "-4.8": f"{mean_no:.1f}",
        "31.9": f"{mean_design:.1f}",
        "7.0%": f"{late_no:.1%}",
        "100.0%": f"{late_design:.1%}",
        "8.9": f"{slope:.1f}",
        "0.989": f"{corr:.3f}",
        "0.986": f"{r2:.3f}",
        "146,669": f"{before:,.0f}",
        "106,485": f"{after:,.0f}",
        "40,184": f"{recovered:,.0f}",
        "27.4%": f"{recovered/before:.1%}",
        "27,4%": f"{recovered/before:.1%}".replace(".", ","),
        "gần chín ngày": "gần năm ngày",
        "0, 1, 2, 3–5, 6–10 và trên 10": "0, 1, 2, 3–4, 5–6 và 7–8",
        "các mức 19–20 lần": "các mức 7–8 lần",
        "tín hiệu chi phối độ trễ": "tín hiệu nổi bật nhất liên quan đến độ trễ",
        "tín hiệu dự báo chi phối": "tín hiệu dự báo nổi bật nhất",
        "hồ sơ rủi ro thay đổi hoàn toàn": "hồ sơ rủi ro khác nhau rõ rệt",
        "hai hồ sơ tiến độ hoàn toàn khác": "hai hồ sơ tiến độ khác nhau đáng kể",
        "quan hệ gần tuyến tính": "mối liên hệ dương ở mức vừa",
        "hệ số của thay đổi thiết kế vượt xa các yếu tố còn lại": "hệ số của thay đổi thiết kế cao nhất, nhưng thiếu vật tư và mưa vẫn có tín hiệu đáng kể",
        "Kết quả cùng chiều và rất mạnh": "Kết quả nhìn chung cùng chiều",
        "“Thay đổi thiết kế” chiếm phần lớn dự án trễ, đúng với quy tắc tạo dữ liệu": f"“Thay đổi thiết kế” là nhóm nguyên nhân đơn lẻ lớn nhất với {cause_share:.1%}; các nguyên nhân khác cộng lại chiếm {1-cause_share:.1%}",
        "**Vì sao tương quan cao như vậy?** Vì bộ dữ liệu được xây dựng để thể hiện insight trung tâm; do đó cần pilot thực tế trước khi suy rộng.": "**Vì sao tương quan chỉ ở mức vừa?** Vì tiến độ còn chịu tác động đồng thời của vật tư, thời tiết, loại công trình và nhiễu vận hành; đây cũng là đặc điểm giúp dữ liệu bớt cực đoan hơn.",
    }
    for old, new in metric_replacements.items():
        text = text.replace(old, new)

    image_map = {
        "01_buc_tranh_tien_do.png": "01_thanh_ty_le_tien_do.png",
        "02_hook_co_khong_thay_doi.png": "02_cot_so_sanh_hai_nhom.png",
        "02_điểm mở đầu_co_khong_thay_doi.png": "02_cot_so_sanh_hai_nhom.png",
        "03_lieu_dap_ung.png": "03_duong_muc_thay_doi.png",
        "04_aha_moment.png": "04_phan_tan_xu_huong.png",
        "05_kiem_soat_yeu_to_nhieu.png": "05_thanh_he_so_chuan_hoa.png",
        "06_do_ben_theo_loai_cong_trinh.png": "06_cot_nhom_loai_cong_trinh.png",
        "07_on_dinh_theo_nam.png": "07_duong_theo_nam.png",
        "08_co_cau_nguyen_nhan.png": "08_thanh_nguyen_nhan.png",
        "09_phan_phoi_theo_muc_thay_doi.png": "09_cot_ty_le_tre_theo_muc.png",
        "10_tac_dong_design_freeze.png": "10_cot_truoc_sau.png",
    }
    for old, new in image_map.items():
        text = text.replace(old, new)

    # Các đoạn mô tả loại biểu đồ được cập nhật để khớp bộ v2.
    text = text.replace(
        "Biểu đồ sử dụng thanh ngang trên đường cơ sở 0, thay vì donut hoặc trục bị cắt. Lựa chọn này giúp người đọc so sánh tỷ lệ chính xác và tránh phóng đại.",
        "Biểu đồ thanh ngang chia tổng thể thành hai phần: dự án trễ hạn và dự án đúng hoặc sớm hạn. Trục từ 0% đến 100% giúp người đọc nhận biết ngay tỷ lệ của từng nhóm."
    )
    text = text.replace(
        "Hai biểu đồ đặt cạnh nhau để người đọc nhìn đồng thời xác suất xảy ra và mức độ hậu quả.",
        "Hai biểu đồ cột đặt cạnh nhau trình bày tỷ lệ trễ và số ngày chậm trung bình. Cùng một thứ tự nhóm được giữ ở cả hai hình để người đọc đối chiếu trực tiếp."
    )
    text = text.replace(
        "Biểu đồ dùng cùng một thang 0–1 cho tất cả thanh, giúp so sánh chính xác.",
        "Biểu đồ cột ngang theo nhóm đặt hai trạng thái thiết kế cạnh nhau trong từng loại công trình. Cách trình bày này cho phép so sánh trực tiếp mà không cần giải thích thang màu."
    )
    text = text.replace(
        "Biểu đồ theo năm cho thấy độ trễ trung bình tương đối ổn định giữa các cohort.",
        "Hai đường theo năm cho thấy khoảng cách giữa nhóm có và không thay đổi thiết kế được duy trì ở các cohort."
    )
    text = text.replace(
        "Biểu đồ nguyên nhân cho thấy “Thay đổi thiết kế” chiếm phần lớn dự án trễ, đúng với quy tắc tạo dữ liệu.",
        "Biểu đồ xếp hạng cho thấy “Thay đổi thiết kế” là nguyên nhân đơn lẻ lớn nhất, nhưng sáu nhóm nguyên nhân còn lại vẫn chiếm phần lớn tổng số dự án trễ."
    )
    text = text.replace(
        "Vì vậy, báo cáo bổ sung boxplot theo nhóm số lần thay đổi.",
        "Vì vậy, báo cáo tính thêm tỷ lệ trễ trong từng nhóm số lần thay đổi thiết kế."
    )
    text = text.replace(
        "Các điểm ngoại lệ được ẩn khỏi phần hiển thị để chart dễ đọc, nhưng không bị loại khỏi dữ liệu phân tích.",
        "Mỗi cột thể hiện tỷ lệ dự án bị trễ trong một nhóm số lần thay đổi; cỡ mẫu được ghi ngay trên cột để tránh đánh giá quá cao các nhóm có ít dự án."
    )
    text = text.replace(
        "Mỗi loại biểu đồ phục vụ đúng câu hỏi. Bar chart dùng cho so sánh chính xác; line chart dùng để kiểm tra cohort năm; scatter/bubble và trend line dùng cho Kết luận chính; boxplot dùng để xem phân phối; hệ số hồi quy dùng để so sánh độ mạnh tương đối. Không dùng biểu đồ 3D, trục kép hoặc màu cầu vồng vì chúng tăng tải nhận thức và dễ gây hiểu sai.",
        "Mỗi hình trả lời một câu hỏi cụ thể bằng các dạng biểu đồ quen thuộc. Biểu đồ thanh thể hiện tỷ lệ và so sánh nhóm; biểu đồ đường thể hiện thay đổi theo mức và theo năm; biểu đồ phân tán thể hiện mối liên hệ giữa hai biến. Bộ hình không dùng 3D, trục kép hoặc thang màu phức tạp."
    )

    page_break = '<div style="page-break-after: always;"></div>'
    data_trailer = f"""
## Data trailer — nội dung cần nắm trong một phút

Nếu người nghe chỉ có một phút, phần trình bày có thể bắt đầu từ năm ý sau:

- Bộ dữ liệu gồm **6.000 dự án**, trong đó khoảng **{late_rate:.1%} dự án bị trễ**.
- Khoảng **{design_rate:.1%} dự án có ít nhất một lần thay đổi thiết kế**. Nhóm không thay đổi có độ lệch tiến độ trung bình **{mean_no:.1f} ngày**, trong khi nhóm có thay đổi chậm trung bình **{mean_design:.1f} ngày**.
- Mỗi lần thay đổi thiết kế đi kèm mức tăng trung bình khoảng **{slope:.1f} ngày chậm** trong bộ dữ liệu này.
- Trong các dự án trễ, thay đổi thiết kế là nguyên nhân đơn lẻ lớn nhất với **{cause_share:.1%}**, không phải nguyên nhân của toàn bộ trường hợp.
- Đề xuất trước mắt là thử nghiệm **Design Freeze**, đi cùng Change Control Board và thời hạn phản hồi thay đổi trong **48 giờ**.
- Theo kịch bản giảm được một vòng sửa, quy mô thời gian có thể thu hồi là **{recovered:,.0f} ngày**, tương đương **{recovered/before:.1%}** tổng số ngày chậm hiện tại. Đây là phép tính what-if, không phải cam kết hiệu quả.

Người cần ra quyết định chính là **Trưởng Ban Quản lý dự án**. Ban điều hành và bộ phận Kế hoạch là nhóm theo dõi, phản biện và cung cấp nguồn lực cho pilot.

Thông điệp một câu: **Cần chặn thay đổi thiết kế muộn ở điểm kiểm soát trước thi công, thay vì chỉ xử lý độ trễ sau khi lịch đã trượt.**
"""
    text = text.replace(
        "## Vấn đề kinh doanh và tính cấp thiết",
        data_trailer + "\n\n" + page_break + "\n\n## Vấn đề kinh doanh và tính cấp thiết",
    )

    big_idea = """
## Big Idea và người ra quyết định

**Nếu doanh nghiệp tiếp tục cho phép thay đổi thiết kế sau mốc chốt mà không có cơ chế kiểm soát, lịch bàn giao sẽ tiếp tục tích lũy độ trễ; vì vậy Trưởng Ban Quản lý dự án nên phê duyệt một pilot Design Freeze có Change Control Board và SLA 48 giờ trước khi áp dụng rộng.**

Câu trên là Big Idea của báo cáo. Nó là một câu hoàn chỉnh, thể hiện quan điểm của nhóm, cho biết điều gì đang bị đe dọa và nêu rõ quyết định mong muốn. Toàn bộ phần phân tích phía sau chỉ giữ lại những bằng chứng giúp kiểm tra hoặc làm rõ câu này.

### Phân tầng người nghe

- **Người ra quyết định chính:** Trưởng Ban Quản lý dự án, người có quyền duyệt pilot và chỉ định đầu mối kiểm soát thay đổi.
- **Người nghe thứ cấp:** Ban điều hành và bộ phận Kế hoạch, quan tâm đến rủi ro bàn giao, nguồn lực và cách đo hiệu quả.
- **Nhân vật trong quá trình:** quản lý dự án, kỹ sư kế hoạch và nhóm thiết kế, là những người trực tiếp tạo, xem xét hoặc tiếp nhận yêu cầu thay đổi.

Báo cáo được đặt ở phía **giải thích** trên continuum của data storytelling: có một kết luận trung tâm, phạm vi hữu hạn, trình tự tuyến tính và dữ liệu đã được chọn lọc. Các bảng kiểm tra chi tiết vẫn được giữ ở lớp phụ lục để phục vụ người đọc muốn đi sâu.
"""
    text = text.replace(
        "## Khung 4D giữ phân tích tập trung",
        big_idea + "\n\n" + page_break + "\n\n## Khung 4D giữ phân tích tập trung",
    )

    storyboard = """
## Sơ đồ nội dung trình bày

Nhóm xác định kết luận cần truyền đạt trước, sau đó lựa chọn các bước dẫn dắt đến kết luận này. Nhờ đó, mỗi biểu đồ đều phục vụ một câu hỏi cụ thể thay vì trình bày toàn bộ kết quả phân tích.

| Cảnh | Hình chính | Câu hỏi mà cảnh trả lời |
|---|---|---|
| Bối cảnh | Thanh tỷ lệ 100% | Vấn đề trễ tiến độ có đủ lớn để cần hành động không? |
| Điểm mở đầu | Hai biểu đồ cột | Kết quả tiến độ khác nhau thế nào giữa nhóm có và không thay đổi thiết kế? |
| Bằng chứng 1 | Biểu đồ đường theo mức thay đổi | Khi số lần thay đổi tăng, độ trễ có tăng theo không? |
| Bằng chứng 2 | Biểu đồ thanh hệ số, cột theo loại công trình và đường theo năm | Kết quả có còn nhất quán khi xét các yếu tố khác, loại công trình và thời gian không? |
| Kết luận chính | Biểu đồ phân tán và đường xu hướng | Mức liên hệ trung bình giữa số lần thay đổi và số ngày chậm là bao nhiêu? |
| Giải pháp | Biểu đồ cột trước–sau | Nếu giảm được một vòng sửa, quy mô tác động tiềm năng là bao nhiêu? |

Mỗi bước chỉ truyền đạt một ý chính. Biểu đồ theo loại công trình, theo năm và theo nguyên nhân được dùng để kiểm tra tính nhất quán; chúng không làm thay đổi hướng lập luận. Khi cần rút ngắn thời gian, người trình bày vẫn có thể giữ trình tự Bối cảnh → Điểm mở đầu → Bằng chứng → Kết luận → Hành động.
"""
    text = text.replace(
        "## Context: quy mô vấn đề tiến độ",
        storyboard + "\n\n" + page_break + "\n\n## Context: quy mô vấn đề tiến độ",
    )

    # Chèn phần tài liệu tham khảo đã đọc thêm, gồm học liệu trong DataStory/data.
    sources = f"""
## Tài liệu tham khảo và ghi chú sử dụng

1. Bộ bài giảng môn *Kể chuyện bằng dữ liệu*, Chương 1–6, thư mục `DataStory/data`. Các chương được dùng để rà soát chuỗi data → insight → decision → action, continuum khám phá–giải thích, khung 4D, Data Storytelling Arc, storyboard và nguyên tắc trực quan.
2. Knaflic, C. N. *Storytelling with Data: Let's Practice!*. Nguồn tham khảo cho việc thu hẹp người nghe, viết Big Idea thành một câu hoàn chỉnh và dựng storyboard trước khi hoàn thiện biểu đồ.
3. Knaflic, C. N. *Storytelling with Data*. Nguồn tham khảo cho việc loại bỏ chi tiết thừa, sử dụng đường cơ sở phù hợp, nhấn bằng tương phản và ưu tiên cách thể hiện dễ đọc.
4. Duarte, N. và cộng sự. *Effective Data Storytelling*. Nguồn tham khảo cho sáu thành phần của một câu chuyện dữ liệu, khung 4D và cách chuyển insight thành hành động.
5. Project Management Institute. *Practice Standard for Scheduling – Third Edition*. Tài liệu này được dùng để tham khảo cách duy trì và truyền thông mô hình tiến độ: https://www.pmi.org/standards/scheduling-third-edition
6. U.S. Government Accountability Office. *Schedule Assessment Guide: Best Practices for Project Schedules (GAO-16-89G)*. Báo cáo sử dụng nguyên tắc baseline, cập nhật thay đổi và phân tích tác động lịch: https://www.gao.gov/products/gao-16-89g
7. Project Management Institute. *Practice Standard for Project Configuration Management*. Nguồn tham khảo cho kiểm soát baseline và yêu cầu: https://www.pmi.org/standards/project-configuration-management
8. Bộ dữ liệu `du_lieu_tien_do_du_an.csv` và notebook `lecture3_v2.ipynb` trong thư mục nộp bài.
"""
    text = text.replace("## Phụ lục A — Danh mục hình ảnh", sources + "\n\n<div style=\"page-break-after: always;\"></div>\n\n## Phụ lục A — Danh mục hình ảnh")

    text = text.replace("Bao_cao_Data_Storytelling", "Bao_cao_Data_Storytelling_v2")
    text = text.replace("`lecture3.ipynb`", "`lecture3_v2.ipynb`")
    text = text.replace("`data_synthetic_design_dominant.csv`", "`du_lieu_tien_do_du_an.csv`")

    # Trình bày nguồn dữ liệu theo phạm vi bài nghiên cứu, không gắn nguồn doanh nghiệp khi đề bài không cung cấp.
    text = re.sub(
        r"### Tuyên bố sử dụng dữ liệu\n\n.*?(?=\n\n<div style=)",
        "### Phạm vi sử dụng dữ liệu\n\nBáo cáo sử dụng bộ dữ liệu tiến độ gồm 6.000 dự án và 15 trường thông tin được cung cấp trong phạm vi Project cuối kỳ. Nhóm kiểm tra tính đầy đủ, tính nhất quán của mã dự án, ngày kế hoạch, ngày hoàn thành và số ngày chậm trước khi phân tích. Mọi kết luận trong báo cáo được giới hạn trong phạm vi bộ dữ liệu này; quan hệ thống kê không được diễn giải thay cho quan hệ nhân quả.",
        text,
        count=1,
        flags=re.S,
    )
    neutral_replacements = {
        "6,000 dự án mô phỏng": "6.000 dự án",
        "6,000 dự án": "6.000 dự án",
        "6.000 dự án mô phỏng": "6.000 dự án",
        "Bộ dữ liệu mô phỏng": "Bộ dữ liệu",
        "bộ dữ liệu mô phỏng": "bộ dữ liệu",
        "dữ liệu mô phỏng": "bộ dữ liệu",
        "Dữ liệu được mô phỏng với insight trung tâm đã xác định, nên cường độ quan hệ phản ánh kịch bản thiết kế.": "Cường độ của các mối liên hệ được đánh giá bằng tương quan, hồi quy chuẩn hóa và kiểm tra theo phân khúc.",
        "cơ chế tạo bộ dữ liệu": "cấu trúc quan sát của dữ liệu",
        "logic mô phỏng": "logic dữ liệu",
        "tình huống kinh doanh giả định có độ phức tạp tương đương thực tế": "vấn đề kinh doanh có phạm vi và độ phức tạp phù hợp với yêu cầu môn học",
        "Mô phỏng tác động kinh doanh": "Phân tích tác động kinh doanh",
        "mô phỏng what-if": "phân tích độ nhạy",
        "Kịch bản what-if giả định": "Phân tích độ nhạy xem xét trường hợp",
        "Kịch bản này": "Phương án phân tích này",
        "kịch bản tác động": "phương án tác động",
        "Trong dự án thật": "Trong giai đoạn triển khai",
        "ngoài thực địa": "trong giai đoạn triển khai",
        "dữ liệu thật": "dữ liệu vận hành",
        "dữ liệu thực": "dữ liệu theo dõi sau pilot",
        "Mô phỏng tác động.": "Phân tích tác động.",
        "mô phỏng đầu vào": "đầu vào phân tích",
        "what-if": "phân tích độ nhạy",
        "Nó giả định quan hệ tuyến tính và các yếu tố khác không đổi.": "Phép tính giữ quan hệ tuyến tính và các yếu tố khác không đổi.",
        "Báo cáo phải nói rõ điều này ngay từ đầu để tránh tạo ấn tượng đây là bằng chứng thu thập tại doanh nghiệp thật. Cách trình bày trung thực không làm yếu câu chuyện; ngược lại, nó thể hiện năng lực phân biệt bộ dữ liệu, phân tích mô tả và kiểm chứng thực nghiệm.": "Báo cáo vì vậy giới hạn kết luận trong phạm vi quan sát và dùng pilot có đối chứng làm bước kiểm tra trước khi mở rộng chính sách.",
        "Phạm vi dữ liệu phù hợp để xây dựng một vấn đề kinh doanh có phạm vi và độ phức tạp phù hợp với yêu cầu môn học, đúng yêu cầu môn học.": "Phạm vi dữ liệu phù hợp với vấn đề tối ưu tiến độ và yêu cầu của Project cuối kỳ.",
        "đây cũng là đặc điểm giúp dữ liệu bớt cực đoan hơn": "điều này phù hợp với thực tế tiến độ thường chịu tác động đồng thời của nhiều nguyên nhân",
        "năm ý sau": "sáu ý sau",
    }
    for old, new in neutral_replacements.items():
        text = text.replace(old, new)
    text = text.replace(
        "**Dữ liệu có phải dữ liệu vận hành không?** Không. Đây là bộ dữ liệu phục vụ học tập; báo cáo không che giấu nguồn gốc.",
        "**Nguồn và phạm vi dữ liệu được xác định thế nào?** Nhóm sử dụng file dữ liệu dự án được cung cấp trong phạm vi Project, kiểm tra 6.000 dòng và giới hạn kết luận trong đúng phạm vi quan sát.",
    )
    text = text.replace(
        "Đồng thời, tính trung thực yêu cầu ghi rõ bộ dữ liệu và không biến tương quan thành tuyên bố nhân quả.",
        "Đồng thời, nhóm không biến tương quan thành tuyên bố nhân quả và giữ kết luận trong phạm vi dữ liệu đã phân tích.",
    )

    def move_page(document, heading, before_heading):
        start = document.find(heading)
        target = document.find(before_heading)
        if start < 0 or target < 0:
            return document
        end = document.find(page_break, start)
        if end < 0:
            return document
        end += len(page_break)
        block = document[start:end].strip()
        document = (document[:start] + document[end:]).strip()
        target = document.find(before_heading)
        return document[:target] + block + "\n\n" + document[target:]

    # Phần 1 cần trình bày dữ liệu trước khi chuyển sang đối tượng và mục tiêu.
    text = move_page(text, "## Mô tả dữ liệu và phạm vi", "## Đối tượng mục tiêu và câu hỏi họ quan tâm")
    # Phần kiểm soát bias thuộc Phần 2 theo barem, không để sau phần giải pháp.
    text = move_page(text, "## Kiểm soát bias và ngụy biện", "## Storyboard của phần trình bày chính")

    rubric_toc = f"""
## Mục lục theo cấu trúc chấm điểm

| Phần | Nội dung | Trọng số |
|---|---|---:|
| Phần 1 | Giới thiệu và Bối cảnh | 5 điểm |
| Phần 2 | Dữ liệu và Phân tích Insight | 15 điểm |
| Phần 3 | Xây dựng Cấu trúc Câu chuyện | 20 điểm |
| Phần 4 | Thiết kế Trực quan | 20 điểm |

Phần nội dung chính bám trực tiếp bốn nhóm tiêu chí trong hướng dẫn Project cuối kỳ. Phụ lục chỉ dùng để liệt kê hình ảnh, notebook và file dữ liệu tái lập; các lập luận chính không được đẩy xuống phụ lục.
"""
    text = text.replace("## Tóm tắt điều hành", rubric_toc + "\n\n" + page_break + "\n\n## Tóm tắt điều hành", 1)

    part1 = """
# PHẦN 1 — GIỚI THIỆU VÀ BỐI CẢNH

Phần này xác định vấn đề kinh doanh, giới thiệu bộ dữ liệu và phạm vi, chỉ rõ người ra quyết định chính và chốt mục tiêu phân tích. Điểm kết thúc của Phần 1 là một câu hỏi quản trị cụ thể: doanh nghiệp nên can thiệp vào đâu để giảm độ trễ mà không dàn trải nguồn lực?
"""
    text = text.replace("## Vấn đề kinh doanh và tính cấp thiết", part1 + "\n\n" + page_break + "\n\n## Vấn đề kinh doanh và tính cấp thiết", 1)
    text = text.replace("## Đối tượng mục tiêu và câu hỏi họ quan tâm", "## Đối tượng mục tiêu", 1)
    objective_page = """
## Mục tiêu phân tích và câu hỏi nghiên cứu

Mục tiêu của phân tích là xác định một tín hiệu có thể theo dõi sớm và chuyển thành hành động quản trị cụ thể nhằm giảm độ trễ dự án. Nhóm không đặt mục tiêu giải thích toàn bộ nguyên nhân chậm tiến độ hoặc xây dựng mô hình dự báo hoàn chỉnh. Phạm vi được giữ ở câu hỏi: thay đổi thiết kế liên hệ thế nào với số ngày chậm và cơ chế nào có thể giảm rủi ro phát sinh sau mốc chốt thiết kế?

Năm câu hỏi nghiên cứu được sử dụng xuyên suốt báo cáo:

1. Tỷ lệ dự án trễ và tổng quy mô ngày chậm hiện tại là bao nhiêu?
2. Hồ sơ tiến độ khác nhau thế nào giữa dự án có và không thay đổi thiết kế?
3. Khi số vòng sửa tăng, độ trễ có tăng theo một trình tự rõ ràng hay không?
4. Tín hiệu này có còn xuất hiện khi xét thêm mưa, thiếu vật tư, giá trị hợp đồng, loại công trình và năm bắt đầu?
5. Nếu giảm được một vòng sửa, quy mô tác động tiềm năng và hệ KPI cần theo dõi là gì?

Đầu ra mong muốn không chỉ là insight thống kê. Phân tích phải dẫn đến một đề xuất có người chịu trách nhiệm, thời hạn xử lý, phạm vi pilot và tiêu chí đánh giá. Đây là cơ sở để lựa chọn Design Freeze, Change Control Board và SLA 48 giờ làm trọng tâm của phần giải pháp.
"""
    text = text.replace("## Big Idea và người ra quyết định", objective_page + "\n\n" + page_break + "\n\n## Big Idea và người ra quyết định", 1)
    text = text.replace("## Mô tả dữ liệu và phạm vi", "## Dữ liệu và nguồn dữ liệu", 1)

    part2 = f"""
# PHẦN 2 — DỮ LIỆU VÀ PHÂN TÍCH INSIGHT

Phần 2 trình bày nền tảng dữ liệu, quy trình làm sạch và khám phá, khung 4D, cách kiểm soát bias và ngụy biện, cùng chuỗi bằng chứng dẫn đến insight trung tâm. Trọng tâm không phải tìm một tương quan đẹp, mà kiểm tra xem thay đổi thiết kế có còn là tín hiệu nổi bật khi đặt cạnh thời tiết, vật tư, quy mô hợp đồng, loại công trình và thời gian hay không.
"""
    text = text.replace("## Khung 4D giữ phân tích tập trung", part2 + "\n\n" + page_break + "\n\n## Khung 4D giữ phân tích tập trung", 1)

    insight_page = f"""
## Khám phá insight trung tâm

Quá trình khám phá bắt đầu từ biến kết quả là `Số ngày chậm`. Trong 6.000 dự án, **{late_rate:.1%}** bị trễ. Nhóm tiếp tục tách dữ liệu theo trạng thái thay đổi thiết kế, số vòng sửa, loại công trình và năm bắt đầu để kiểm tra liệu kết quả chung có che giấu khác biệt quan trọng hay không.

Kết quả cho thấy **{design_rate:.1%}** dự án có ít nhất một lần thay đổi thiết kế. Nhóm không thay đổi có độ lệch tiến độ trung bình **{mean_no:.1f} ngày**, trong khi nhóm có thay đổi chậm trung bình **{mean_design:.1f} ngày**. Tỷ lệ trễ tương ứng là **{late_no:.1%}** và **{late_design:.1%}**. Khi chuyển từ so sánh hai nhóm sang số vòng sửa, độ trễ tăng theo từng mức và đường xu hướng có độ dốc khoảng **{slope:.1f} ngày cho mỗi vòng sửa**.

Nhóm không dừng ở một biểu đồ hai biến. Mô hình chuẩn hóa đưa thêm số ngày mưa, số lần thiếu vật tư và giá trị hợp đồng vào cùng phép tính. Thay đổi thiết kế có hệ số lớn nhất, nhưng vật tư và mưa vẫn có ảnh hưởng nhìn thấy được; R² của mô hình là **{r2:.3f}**. Kết quả này phù hợp với cách diễn giải thận trọng: thay đổi thiết kế là tín hiệu nổi bật nhất trong mẫu, không phải lời giải thích duy nhất cho độ trễ.

Insight trả lời đủ ba câu hỏi của barem. Trưởng Ban Quản lý dự án quan tâm vì thay đổi thiết kế xuất hiện trước khi dự án hoàn thành và có thể dùng làm chỉ báo cảnh báo. Hành động phù hợp là thí điểm Design Freeze, Change Control Board và SLA 48 giờ. Phân tích độ nhạy cho thấy nếu giảm tối đa một vòng sửa ở các dự án có thay đổi, quy mô thời gian có thể thu hồi là **{recovered:,.0f} ngày**, tương đương **{recovered/before:.1%}** tổng ngày chậm dương.
"""
    text = text.replace("## Storyboard của phần trình bày chính", insight_page + "\n\n" + page_break + "\n\n## Storyboard của phần trình bày chính", 1)

    part3 = """
# PHẦN 3 — XÂY DỰNG CẤU TRÚC CÂU CHUYỆN

Câu chuyện được tổ chức theo Data Storytelling Arc gồm Context, Hook, Rising Insights, Aha Moment, Solution và Next Steps. Trình tự này giúp người nghe hiểu quy mô vấn đề trước, thấy điểm bất thường, kiểm tra các bằng chứng tăng dần rồi mới tiếp nhận đề xuất thay đổi quản trị.
"""
    text = text.replace("## Storyboard của phần trình bày chính", part3 + "\n\n" + page_break + "\n\n## Storyboard của phần trình bày chính", 1)
    heading_replacements = {
        "## Điểm mở đầu: hai trạng thái rủi ro trái ngược": "## Hook: hai trạng thái rủi ro khác nhau rõ rệt",
        "## Bằng chứng tiếp theo: quan hệ liều–đáp ứng": "## Rising Insights: quan hệ liều–đáp ứng",
        "## Kết luận chính: mỗi vòng sửa là một nấc trượt": "## Aha Moment: mỗi vòng sửa là một nấc trượt",
        "## Từ insight đến giải pháp Design Freeze": "## Solution & Next Steps: Design Freeze và cơ chế thực hiện",
    }
    for old, new in heading_replacements.items():
        text = text.replace(old, new)

    part4 = """
# PHẦN 4 — THIẾT KẾ TRỰC QUAN

Phần 4 đối chiếu trực tiếp các biểu đồ với hai nhóm nguyên tắc trong hướng dẫn: Setting the Scenes và Polishing the Scenes. Mỗi lựa chọn trực quan phải trả lời được ba câu hỏi: dữ liệu nào cần đưa lên, loại biểu đồ nào phù hợp và cách bố trí nào giúp người xem đọc đúng thông điệp.
"""
    visual_pages = f"""
## Setting the Scenes: trực quan hóa đúng dữ liệu

Chỉ số được lựa chọn theo câu hỏi quyết định, không theo mức độ sẵn có của cột dữ liệu. Ở phần Context, tỷ lệ dự án trễ được tính trên toàn bộ 6.000 dự án để xác định quy mô. Ở phần Hook, cùng một định nghĩa trễ hạn được dùng cho hai nhóm có và không thay đổi thiết kế. Việc giữ chung mẫu số giúp chênh lệch **{late_no:.1%} so với {late_design:.1%}** có ý nghĩa so sánh.

Giá trị trung bình được đặt cạnh tỷ lệ trễ để tránh phụ thuộc vào một thước đo duy nhất. Số vòng sửa được nhóm thành 0, 1–2, 3–5 và trên 5 khi tính tỷ lệ trễ. Mỗi cột ghi rõ cỡ mẫu n, giúp người đọc nhận biết các nhóm có ít dự án và diễn giải thận trọng hơn.

Phần tác động sử dụng tổng ngày chậm dương thay vì cộng cả ngày hoàn thành sớm và ngày trễ. Cách tính này phù hợp với câu hỏi “bao nhiêu thời gian trễ có thể được thu hồi”. Báo cáo không quy đổi ngày thành tiền vì bộ dữ liệu không có chi phí ngày công, thiết bị, phạt hợp đồng hoặc chi phí cơ hội. Đây là ranh giới cần giữ để không tạo ra một con số tài chính thiếu căn cứ.
""" + "\n\n" + page_break + f"""

## Choose the Right Visualizations: chọn biểu đồ theo mục đích

| Câu hỏi | Biểu đồ | Lý do lựa chọn |
|---|---|---|
| Quy mô trễ hạn là bao nhiêu? | Thanh tỷ lệ 100% | Cho biết trực tiếp tỷ lệ trễ và đúng hạn |
| Hai nhóm khác nhau thế nào? | Hai biểu đồ cột | So sánh tỷ lệ trễ và số ngày chậm trung bình bằng cùng thứ tự nhóm |
| Độ trễ thay đổi theo số vòng sửa ra sao? | Biểu đồ đường | Thể hiện sự thay đổi theo các mức có thứ tự |
| 6.000 dự án phân bố thế nào? | Biểu đồ phân tán | Mỗi điểm là một dự án; đường xu hướng cho biết chiều liên hệ chung |
| Yếu tố nào có liên hệ mạnh hơn? | Thanh ngang hệ số chuẩn hóa | So sánh các hệ số trên cùng một trục |
| Kết quả có nhất quán theo loại công trình? | Cột ngang theo nhóm | Đặt hai trạng thái thiết kế cạnh nhau trong từng loại công trình |
| Nguyên nhân nào đứng đầu? | Thanh ngang xếp hạng | Sắp xếp tỷ trọng và giữ tên nguyên nhân dễ đọc |
| Tỷ lệ trễ thay đổi theo số vòng sửa ra sao? | Biểu đồ cột | Hiển thị tỷ lệ và cỡ mẫu của từng nhóm |
| Quy mô tác động tiềm năng là bao nhiêu? | Hai cột trước–sau | So sánh trực tiếp tổng ngày chậm trước và sau phép tính độ nhạy |

Bộ biểu đồ có chủ ý thay đổi hình thức theo câu hỏi, nhưng vẫn dùng chung hệ màu và cách viết tiêu đề. Sự đa dạng này phục vụ chức năng đọc dữ liệu, không nhằm trang trí.
""" + "\n\n" + page_break + f"""

## Calibrate the Visuals to Your Message: hiệu chỉnh theo thông điệp

Các yếu tố cần so sánh được đặt gần nhau. Hai cột có và không thay đổi thiết kế luôn xuất hiện theo cùng thứ tự. Biểu đồ theo loại công trình đặt hai trạng thái cạnh nhau trong từng hàng; biểu đồ theo năm đặt hai đường trên cùng hệ trục. Cách bố trí này giảm số bước đối chiếu mà người đọc phải thực hiện.

Đường cơ sở 0 được giữ ở các biểu đồ cột, hệ số và số ngày chậm. Với biểu đồ đường theo mức thay đổi, vùng dưới 0 được tô nhẹ để phân biệt dự án hoàn thành sớm; vùng trên 0 thể hiện số ngày trễ. Không biểu đồ nào cắt trục theo cách làm phóng đại chênh lệch.

Màu đỏ được dành cho thay đổi thiết kế hoặc rủi ro cần chú ý. Xám là tham chiếu, xanh là đúng hoặc sớm hạn, vàng là lớp bằng chứng hỗ trợ. Quy tắc màu không thay đổi giữa các trang. Tiêu đề biểu đồ được viết thành kết luận, phụ đề nói rõ mẫu số hoặc giới hạn, nhãn số được đặt ngay gần điểm cần đọc. Nhờ vậy, người xem không phải dựa vào chú giải dài hoặc tự suy ra thông điệp từ tên biến.
""" + "\n\n" + page_break + """

## Polishing the Scenes: loại bỏ nhiễu và tập trung chú ý

Các biểu đồ không sử dụng 3D, bóng đổ, nền trang trí, màu cầu vồng hoặc đường lưới đậm. Khung trên và phải được bỏ khi không mang thông tin. Nhãn lặp lại được giảm, nhưng những con số cần cho quyết định như tỷ lệ, độ dốc, cỡ mẫu và quy mô tác động vẫn được giữ. Đây là cách loại bỏ nhiễu mà không làm mất khả năng kiểm tra con số.

Sự chú ý được điều khiển bằng tương phản có giới hạn. Chỉ biến thay đổi thiết kế dùng đỏ đậm; các yếu tố còn lại dùng xám. Ở biểu đồ nguyên nhân, thanh thay đổi thiết kế được nhấn nhưng sáu nguyên nhân khác vẫn hiển thị đầy đủ. Biểu đồ hệ số vẫn giữ biến thiếu vật tư và số ngày mưa để thể hiện đây là bài toán đa yếu tố.

Ngôn ngữ trên biểu đồ ưu tiên cách nói quen thuộc với quản lý dự án: “ngày chậm”, “vòng sửa”, “tỷ lệ trễ”, “tổng ngày có thể thu hồi”. Thuật ngữ thống kê như R² hoặc hệ số chuẩn hóa chỉ xuất hiện ở nơi cần kiểm tra độ bền và luôn có câu diễn giải đi kèm. Cách làm này hỗ trợ người nghe có mức độ hiểu dữ liệu khác nhau mà không làm đơn giản hóa quá mức.
""" + "\n\n" + page_break + f"""

## Instill Trust in Your Numbers: xây dựng sự tin cậy

Mỗi hình đều ghi nguồn thống nhất: bộ dữ liệu tiến độ 6.000 dự án và phần tính toán của nhóm. Các tỷ lệ dùng mẫu số rõ ràng; các nhóm ít quan sát có nhãn cỡ mẫu; các phép tính trước–sau nêu công thức và không được trình bày như cam kết. Notebook đi kèm tạo lại toàn bộ hình từ cùng một file dữ liệu, nhờ đó số liệu trong báo cáo, biểu đồ và bảng tổng hợp không bị lệch nhau.

Sự tin cậy còn đến từ việc trình bày các bằng chứng không thuận tiện cho thông điệp. Tương quan **r = {corr:.3f}** chỉ ở mức vừa; R² **{r2:.3f}** cho thấy mô hình chưa giải thích toàn bộ biến động tiến độ. Thiếu vật tư và thời tiết có ảnh hưởng đáng kể. Báo cáo giữ các kết quả này thay vì chỉ chọn phần làm cho thay đổi thiết kế trông mạnh nhất.

Cuối cùng, báo cáo tách rõ quan sát, diễn giải và hành động. Quan sát là sự khác biệt giữa các nhóm và độ dốc trong mẫu. Diễn giải là thay đổi thiết kế có thể dùng như chỉ báo quản trị sớm. Hành động là pilot Design Freeze có KPI dẫn dắt, KPI kết quả và KPI cân bằng. Cấu trúc này giúp người đọc hiểu con số hỗ trợ quyết định đến đâu và phần nào vẫn cần được kiểm chứng trong quá trình triển khai.
"""
    text = text.replace(
        "## Nguyên tắc thiết kế trực quan",
        part4 + "\n\n" + page_break + "\n\n" + visual_pages + "\n\n" + page_break + "\n\n## Nguyên tắc thiết kế trực quan",
        1,
    )

    # Biên tập ngôn ngữ: ưu tiên câu văn học thuật, thuật ngữ tiếng Việt và mức độ kết luận phù hợp.
    editorial_replacements = {
        "# DESIGN FREEZE: CHẶN HIỆU ỨNG DOMINO TỪ THAY ĐỔI THIẾT KẾ": "# QUẢN LÝ THAY ĐỔI THIẾT KẾ ĐỂ HẠN CHẾ CHẬM TIẾN ĐỘ",
        "**Insight trung tâm:** Thay đổi thiết kế là tín hiệu nổi bật nhất liên quan đến độ trễ": "**Phát hiện chính:** Thay đổi thiết kế là yếu tố có liên hệ mạnh nhất với số ngày chậm trong các biến được phân tích",
        "> **Thông điệp điều hành:** Đừng để mỗi vòng sửa bản vẽ trở thành một vòng trượt tiến độ. Hãy khóa thiết kế đúng mốc, kiểm soát mọi thay đổi sau freeze và chứng minh hiệu quả bằng pilot có đối chứng.": "> **Đề xuất điều hành:** Thiết lập mốc chốt thiết kế, kiểm soát các yêu cầu thay đổi phát sinh sau mốc và đánh giá hiệu quả bằng một chương trình thí điểm có nhóm so sánh.",
        "## Data trailer — nội dung cần nắm trong một phút": "## Tóm tắt dành cho người ra quyết định",
        "## Big Idea và người ra quyết định": "## Thông điệp trung tâm và người ra quyết định",
        "Câu trên là Big Idea của báo cáo. Nó là một câu hoàn chỉnh, thể hiện quan điểm của nhóm, cho biết điều gì đang bị đe dọa và nêu rõ quyết định mong muốn.": "Đây là thông điệp trung tâm của báo cáo. Câu này nêu rõ vấn đề, hệ quả và quyết định mà nhóm đề xuất.",
        "### Phân tầng người nghe": "### Nhóm người đọc",
        "Báo cáo được đặt ở phía **giải thích** trên continuum của data storytelling:": "Báo cáo tập trung vào mục tiêu **giải thích** trong quá trình khám phá và trình bày dữ liệu:",
        "Sau khi đưa mưa, thiếu vật tư và giá trị hợp đồng vào mô hình mô tả,": "Sau khi bổ sung các biến số ngày mưa, số lần thiếu vật tư và giá trị hợp đồng vào mô hình,",
        "sau khi xét mưa, vật tư, quy mô hợp đồng và phân khúc": "sau khi xét số ngày mưa, số lần thiếu vật tư, giá trị hợp đồng và loại công trình",
        "khi xét thêm mưa, thiếu vật tư, giá trị hợp đồng": "khi xét thêm số ngày mưa, số lần thiếu vật tư, giá trị hợp đồng",
        "mưa và thiếu vật tư": "số ngày mưa và số lần thiếu vật tư",
        "thiếu vật tư và mưa": "số lần thiếu vật tư và số ngày mưa",
        "**Confirmation bias**": "**Thiên lệch xác nhận (confirmation bias)**",
        "**Correlation fallacy**": "**Ngụy biện đồng nhất tương quan với quan hệ nhân quả (correlation fallacy)**",
        "**Texas sharpshooter**": "**Ngụy biện chọn điểm thuận lợi (Texas sharpshooter)**",
        "**Hasty generalization**": "**Khái quát vội vàng (hasty generalization)**",
        "**Survivorship bias**": "**Thiên lệch sống sót (survivorship bias)**",
        "**Curse of knowledge**": "**Lời nguyền kiến thức (curse of knowledge)**",
        "## Kiểm soát bias và ngụy biện": "## Kiểm soát sai lệch nhận thức và ngụy biện",
        "sa vào EDA vô tận": "mở rộng phân tích khám phá vượt quá câu hỏi nghiên cứu",
        "## Hook: hai trạng thái rủi ro khác nhau rõ rệt": "## Hook: khác biệt giữa dự án có và không thay đổi thiết kế",
        "Hai thước đo được trình bày dưới dạng Cleveland dot plot. Khoảng cách giữa hai điểm cho thấy đồng thời sự khác biệt về xác suất trễ và số ngày chậm trung bình.": "Hai biểu đồ cột lần lượt thể hiện tỷ lệ trễ và số ngày chậm trung bình. Cùng một thứ tự nhóm được sử dụng ở cả hai biểu đồ để hỗ trợ đối chiếu.",
        "chúng tạo ra hai hồ sơ tiến độ khác nhau đáng kể": "kết quả tiến độ của hai nhóm khác nhau đáng kể",
        "Nó chỉ mở ra xung đột và tạo động lực để xem xét": "Kết quả này là cơ sở để tiếp tục kiểm tra",
        "## Rising Insights: quan hệ liều–đáp ứng": "## Rising Insights: độ trễ tăng theo mức thay đổi thiết kế",
        "Quan hệ liều–đáp ứng là bước kiểm tra quan trọng giữa điểm mở đầu và Kết luận chính.": "Bước tiếp theo là kiểm tra số ngày chậm theo từng mức thay đổi thiết kế.",
        "Insight này có ý nghĩa vận hành:": "Kết quả này có ý nghĩa quản lý:",
        "nó là leading indicator phù hợp cho cảnh báo": "số vòng sửa có thể được sử dụng như một chỉ báo cảnh báo sớm",
        "tái lập baseline": "cập nhật tiến độ cơ sở",
        "## Aha Moment: mỗi vòng sửa là một nấc trượt": "## Aha Moment: mỗi lần thay đổi đi kèm trung bình 4,9 ngày chậm",
        "Biểu đồ kết luận chính cô đọng toàn bộ kết quả thành một thông điệp:": "Biểu đồ phân tán cho thấy kết quả chính:",
        "Kích thước điểm đại diện cho số dự án ở mỗi mức, giúp người đọc không đánh đồng mức có hàng nghìn dự án với mức chỉ có vài quan sát.": "Mỗi điểm đại diện cho một dự án. Độ trong suốt của điểm giúp người đọc nhận biết vùng có nhiều quan sát.",
        "Chú thích đặt trực tiếp trong vùng trống của chart": "Chú thích được đặt trực tiếp trong vùng trống của biểu đồ",
        "người nói nên dừng tại chart này": "người trình bày nên dừng tại biểu đồ này",
        "Cách trình bày từ hình ảnh đến con số giúp insight dễ hiểu và dễ nhớ hơn việc đọc hệ số trước.": "Trình tự này giúp người nghe quan sát xu hướng trước khi tiếp nhận hệ số thống kê.",
        "Một phân tích có cơ sở phải chủ động đối diện với lời giải thích cạnh tranh.": "Để kiểm tra các cách giải thích khác, nhóm xây dựng một mô hình hồi quy chuẩn hóa.",
        "Kết quả cho thấy hệ số của thay đổi thiết kế cao nhất, nhưng thiếu vật tư và mưa vẫn có tín hiệu đáng kể": "Kết quả cho thấy hệ số của thay đổi thiết kế cao nhất; số lần thiếu vật tư và số ngày mưa cũng có hệ số dương",
        "Điều này chứng minh insight không biến mất": "Điều này cho thấy mối liên hệ với thay đổi thiết kế vẫn còn",
        "ba yếu tố cạnh tranh": "ba biến giải thích khác",
        "không chỉ chọn một scatter plot thuận lợi": "không chỉ dựa vào một biểu đồ phân tán",
        "thời điểm change order": "thời điểm phát sinh yêu cầu thay đổi",
        "## Kiểm tra độ bền theo loại công trình": "## Kiểm tra tính nhất quán theo loại công trình",
        "Để tránh hasty generalization": "Để tránh khái quát vội vàng",
        "Kiểm tra phân khúc làm tăng độ tin cậy nội bộ của insight:": "Kết quả theo loại công trình giúp kiểm tra tính nhất quán:",
        "Heatmap đặt loại công trình theo hàng và nhóm thay đổi theo cột. Người đọc có thể kiểm tra tính nhất quán của mẫu hình mà không phải xem nhiều biểu đồ lặp lại.": "Biểu đồ cột ngang đặt nhóm có và không thay đổi thiết kế cạnh nhau trong từng loại công trình, giúp người đọc so sánh trực tiếp.",
        "độ bền trong bộ dữ liệu": "tính nhất quán trong bộ dữ liệu",
        "Trong pilot": "Trong chương trình thí điểm",
        "Design Freeze": "mốc chốt thiết kế",
        "Change Control Board": "tổ kiểm soát thay đổi",
        "SLA 48 giờ": "thời hạn xử lý 48 giờ",
        "stage-gate": "từng cổng phê duyệt",
        "change order": "yêu cầu thay đổi",
        "baseline": "tiến độ cơ sở",
        "business case": "phương án kinh doanh",
        "escalation": "trình cấp có thẩm quyền",
        "forecast tài chính": "dự báo tài chính",
        "Pilot": "Chương trình thí điểm",
        "pilot": "chương trình thí điểm",
        "chart": "biểu đồ",
        "cohort": "nhóm dự án theo năm bắt đầu",
        "## Phân phối và rủi ro ngoài giá trị trung bình": "## Tỷ lệ trễ theo mức thay đổi thiết kế",
        "Giá trị trung bình có thể bị kéo bởi một số dự án cực đoan. Vì vậy, báo cáo bổ sung raincloud plot, kết hợp phân phối, hộp tứ phân vị và một mẫu điểm quan sát. Biểu đồ cho thấy toàn bộ phân phối dịch chuyển lên khi số vòng sửa tăng, không chỉ riêng trung bình. Trung vị, khoảng tứ phân vị và vùng biến thiên đều thay đổi theo cùng hướng.": "Để bổ sung cho số ngày chậm trung bình, nhóm tính tỷ lệ dự án bị trễ trong bốn nhóm số lần thay đổi: 0, 1–2, 3–5 và trên 5. Kết quả cho thấy tỷ lệ trễ tăng cùng số lần thay đổi thiết kế.",
        "Phần violin giữ hình dạng phân phối; boxplot cho biết trung vị và khoảng tứ phân vị; các điểm chỉ là mẫu ngẫu nhiên để tránh hình bị quá dày. Không quan sát nào bị loại khỏi phép tính. Cách làm này được ghi rõ trong phụ đề nhằm tránh hiểu nhầm. Trong báo cáo thực tế, nên cung cấp thêm phụ lục về ngoại lệ, đặc biệt các dự án có thay đổi cao nhưng độ trễ thấp hoặc ngược lại. Những trường hợp lệch khỏi xu hướng thường chứa bài học về khả năng phục hồi tiến độ.": "Mỗi cột ghi cả tỷ lệ trễ và số dự án trong nhóm. Việc công bố cỡ mẫu đặc biệt quan trọng với nhóm trên 5 lần thay đổi, vì nhóm này có ít dự án hơn các nhóm còn lại.",
        "Thông điệp quản trị từ phân phối là: không nên chỉ tập trung vào vài dự án thảm họa. Ngay cả dự án “điển hình”, rủi ro cũng tăng theo số vòng sửa. Do đó, mốc chốt thiết kế là chính sách hệ thống, còn cơ chế trình cấp có thẩm quyền theo ngưỡng là cách tập trung nguồn lực vào nhóm có rủi ro cao nhất.": "Kết quả cho thấy số vòng sửa có thể được dùng để phân nhóm theo dõi. Dự án có nhiều vòng sửa cần được rà soát sớm hơn và trình cấp có thẩm quyền khi vượt ngưỡng đã quy định.",
        "## Solution & Next Steps: mốc chốt thiết kế và cơ chế thực hiện": "## Solution & Next Steps: mốc chốt thiết kế và các bước triển khai",
        "Tổng quỹ ngày chậm dương": "Tổng số ngày chậm dương",
        "định cỡ cơ hội": "ước lượng quy mô tác động",
        "## KPI, chương trình thí điểm và cơ chế đo lường": "## KPI và kế hoạch thí điểm",
        "## Kết luận và lời kêu gọi hành động": "## Kết luận và đề xuất triển khai",
        "> **Kết luận một câu:** Đừng để mỗi vòng sửa bản vẽ trở thành một vòng trượt tiến độ — khóa thiết kế đúng mốc, kiểm soát thay đổi và đo hiệu quả bằng dữ liệu theo dõi sau chương trình thí điểm.": "> **Đề xuất:** Áp dụng mốc chốt thiết kế, kiểm soát yêu cầu thay đổi sau mốc và đánh giá hiệu quả bằng dữ liệu thu thập trong chương trình thí điểm.",
        "hồ sơ rủi ro khác nhau rõ rệt": "kết quả tiến độ của hai nhóm khác nhau rõ rệt",
        "Quan hệ không dừng ở khác biệt nhị phân. Số ngày chậm tăng đều theo số vòng sửa, tạo thành một quan hệ “liều–đáp ứng”.": "Khác biệt không chỉ xuất hiện khi so sánh hai nhóm. Số ngày chậm còn tăng theo số lần thay đổi thiết kế.",
        "Báo cáo chọn thay đổi thiết kế làm insight trung tâm không phải vì tên biến nghe thuyết phục, mà vì dữ liệu tạo thành chuỗi bằng chứng nhất quán: khác biệt giữa hai trạng thái, quan hệ tăng theo số vòng sửa, ưu thế sau kiểm soát yếu tố nhiễu, sự ổn định theo loại công trình và tác động phân tích độ nhạy có thể lượng hóa. Mạch kể chuyện vì vậy hướng người đọc từ bức tranh chung đến một quyết định quản trị cụ thể.": "Báo cáo tập trung vào thay đổi thiết kế vì kết quả so sánh hai nhóm, phân tích theo số lần thay đổi, hồi quy nhiều biến và kiểm tra theo loại công trình đều cho cùng một hướng. Trình tự trình bày dẫn từ quy mô vấn đề đến đề xuất quản lý.",
        "Mỗi nhóm nhìn cùng một dữ liệu qua một lăng kính khác nhau.": "Mỗi nhóm sử dụng kết quả phân tích cho một mục đích khác nhau.",
        "khả năng chuyển insight thành thay đổi quản trị": "khả năng chuyển kết quả phân tích thành biện pháp quản lý",
        "insight có bền trước các lời giải thích cạnh tranh không": "kết quả có còn nhất quán khi bổ sung các biến khác hay không",
        "quan hệ liều–đáp ứng": "xu hướng theo số lần thay đổi",
        "độ bền sau khi xét": "tính nhất quán sau khi xét",
        "đảm bảo khán giả không bị dẫn thẳng": "bảo đảm người đọc không bị dẫn thẳng",
        "xác định một tín hiệu có thể theo dõi sớm": "xác định một chỉ báo có thể theo dõi sớm",
        "không chỉ là insight thống kê": "không chỉ là một kết quả thống kê",
        "cách kiểm soát bias và ngụy biện, cùng chuỗi bằng chứng dẫn đến insight trung tâm": "cách kiểm soát sai lệch nhận thức và ngụy biện, cùng các kết quả làm cơ sở cho phát hiện chính",
        "Trọng tâm không phải tìm một tương quan đẹp, mà kiểm tra xem thay đổi thiết kế có còn là tín hiệu nổi bật khi đặt cạnh thời tiết, vật tư, quy mô hợp đồng, loại công trình và thời gian hay không.": "Trọng tâm là kiểm tra mối liên hệ giữa thay đổi thiết kế và tiến độ sau khi đã xem xét thêm thời tiết, vật tư, giá trị hợp đồng, loại công trình và thời gian.",
        "số ngày số ngày mưa": "số ngày mưa",
        "kiểm tra insight": "kiểm tra kết quả",
        "4D cũng giúp giữ liên kết từ insight đến giải pháp. Nếu insight là số vòng sửa,": "Khung 4D cũng giúp bảo đảm sự thống nhất giữa kết quả và giải pháp. Nếu kết quả chính liên quan đến số lần thay đổi,",
        "tín hiệu dự báo nổi bật nhất": "biến có liên hệ mạnh nhất trong số các biến được phân tích",
        "Con số này tạo cảm giác cấp bách nhưng chưa đủ để hành động, bởi": "Con số này cho thấy quy mô vấn đề nhưng chưa đủ để xác định hành động, vì",
        "Vai trò của biểu đồ context là thiết lập quy mô và đưa khán giả vào vấn đề, không phải cố chứng minh insight trung tâm ngay lập tức.": "Biểu đồ mở đầu chỉ dùng để xác định quy mô chậm tiến độ; kết luận chính được kiểm tra ở các phần sau.",
        "Từ context, phân tích chuyển sang câu hỏi điểm mở đầu:": "Từ kết quả tổng thể, phân tích chuyển sang câu hỏi tiếp theo:",
        "![Context: quy mô vấn đề tiến độ]": "![Quy mô chậm tiến độ của toàn bộ dự án]",
        "![Điểm mở đầu: hai trạng thái rủi ro trái ngược]": "![So sánh dự án có và không thay đổi thiết kế]",
        "![Bằng chứng tiếp theo: xu hướng theo số lần thay đổi]": "![Số ngày chậm theo mức thay đổi thiết kế]",
        "![Kết luận chính: mỗi vòng sửa là một nấc trượt]": "![Mối liên hệ giữa số lần thay đổi và số ngày chậm]",
        "![Kiểm tra độ bền theo loại công trình]": "![Kiểm tra tính nhất quán theo loại công trình]",
        "vẫn có tín hiệu đáng kể": "cũng có hệ số dương",
        "Giá trị hợp đồng gần như không tạo tín hiệu đáng kể": "Hệ số của giá trị hợp đồng gần 0",
        "correlation fallacy": "ngụy biện đồng nhất tương quan với quan hệ nhân quả",
        "nhóm dự án theo năm bắt đầu năm bắt đầu": "nhóm dự án theo năm bắt đầu",
        "mức độ chậm không bị một năm bất thường chi phối": "kết quả không bị chi phối bởi một năm bất thường",
        "Đây cũng là nơi cần minh bạch nhất: nhãn nguyên nhân không phải bằng chứng độc lập nếu nó được sinh từ cùng quy tắc đã dùng để tạo độ trễ. Vì vậy, báo cáo không dùng biểu đồ nguyên nhân làm Kết luận chính. Bằng chứng chính vẫn là quan hệ theo số vòng sửa và các kiểm tra định lượng. Nhãn nguyên nhân chỉ được dùng như phép kiểm tra cấu trúc dữ liệu.": "Nhãn nguyên nhân phản ánh nguyên nhân được ghi nhận trong hồ sơ dự án. Do một dự án có thể chịu nhiều tác động đồng thời, biểu đồ này chỉ dùng để mô tả cơ cấu nguyên nhân, không được sử dụng riêng lẻ để kết luận quan hệ nhân quả.",
        "chuyển insight thành quy mô hành động": "chuyển kết quả phân tích thành quy mô tác động có thể theo dõi",
        "Nó cũng không tính chi phí": "Phép tính này cũng chưa bao gồm chi phí",
        "Cách làm này bám trực tiếp vào xu hướng theo số lần thay đổi": "Cách làm này dựa trực tiếp trên xu hướng tăng của số ngày chậm theo số lần thay đổi",
        "đưa mưa, thiếu vật tư và quy mô hợp đồng vào mô hình": "bổ sung các biến số ngày mưa, số lần thiếu vật tư và giá trị hợp đồng vào mô hình",
        "gọi kết quả là quan hệ dự báo trong bộ dữ liệu": "không diễn giải tương quan thành quan hệ nhân quả",
        "Chuỗi biểu đồ giữ logic thống nhất: context mô tả quy mô; điểm mở đầu tạo đối lập; dose response tăng bằng chứng; confounder và segment kiểm tra phản biện; kết luận chính cô đọng insight; scenario chuyển sang hành động. Không biểu đồ nào đưa ra một biến trọng tâm mới làm đứt mạch câu chuyện.": "Chuỗi biểu đồ đi từ quy mô vấn đề, so sánh hai nhóm, xu hướng theo số lần thay đổi, kiểm tra các biến khác, đến phân tích tác động và đề xuất triển khai. Không biểu đồ nào đưa thêm một chủ đề ngoài câu hỏi nghiên cứu.",
        "dẫn qua xu hướng theo số lần thay đổi": "trình bày xu hướng theo số lần thay đổi",
        "Vì tiến độ còn chịu tác động đồng thời của vật tư, thời tiết, loại công trình và nhiễu vận hành; điều này phù hợp với thực tế tiến độ thường chịu tác động đồng thời của nhiều nguyên nhân.": "Vì tiến độ đồng thời chịu ảnh hưởng của thiếu vật tư, thời tiết, loại công trình và các yếu tố chưa quan sát.",
        "Các biến này đã được đưa vào mô hình chuẩn hóa và có tín hiệu nhỏ hơn trong kịch bản.": "Các biến này đã được bổ sung vào mô hình và có hệ số thấp hơn thay đổi thiết kế.",
        "và tín hiệu vẫn mạnh khi xem xét các yếu tố vận hành cạnh tranh": "và mối liên hệ vẫn xuất hiện khi bổ sung các biến vận hành khác",
        "Kịch bản giảm một vòng sửa cho thấy tiềm năng thu hồi 18,8% quỹ ngày chậm.": "Phân tích độ nhạy cho trường hợp giảm một lần thay đổi cho thấy số ngày chậm có thể giảm 18,8%.",
        "Insight không nên kết thúc ở câu “thay đổi thiết kế gây chậm”. Giá trị kinh doanh nằm ở việc biến insight thành cơ chế:": "Kết quả phân tích cần được chuyển thành cơ chế quản lý cụ thể:",
        "Quan hệ liều–đáp ứng.": "Số ngày chậm theo mức thay đổi.",
        "trong phạm vi Project cuối kỳ": "trong phạm vi bài tập cuối kỳ",
        "trong phạm vi Project": "trong phạm vi bài tập",
        "Bước đúng tiếp theo": "Bước tiếp theo phù hợp",
        "Đây là phép tính phân tích độ nhạy": "Đây là kết quả của phép phân tích độ nhạy",
        "Hồ sơ tiến độ khác nhau thế nào": "Kết quả tiến độ khác nhau thế nào",
        "Tín hiệu này có còn xuất hiện": "Mối liên hệ này có còn xuất hiện",
        "một chương trình thí điểm mốc chốt thiết kế có tổ kiểm soát thay đổi và thời hạn xử lý 48 giờ": "một chương trình thí điểm áp dụng mốc chốt thiết kế, kèm tổ kiểm soát thay đổi và thời hạn xử lý 48 giờ",
        "**Người nghe thứ cấp:**": "**Nhóm sử dụng kết quả:**",
        "**Nhân vật trong quá trình:**": "**Nhóm trực tiếp thực hiện:**",
        "ba cột ngày được chuẩn hóa về datetime": "ba cột ngày được chuẩn hóa về cùng kiểu ngày tháng",
        "Các assert trong notebook biến những điều kiện này thành kiểm tra tự động": "Các điều kiện này được kiểm tra tự động trong notebook",
        "các yếu tố vận hành cạnh tranh": "các biến vận hành khác",
        "kiểm tra theo phân khúc": "kiểm tra theo loại công trình",
        "Điểm mở đầu hiệu quả vì nó chuyển một khái niệm kỹ thuật thành sự đối lập dễ nhớ:": "So sánh hai nhóm giúp thể hiện khác biệt một cách trực tiếp:",
        "Tuy nhiên, khác biệt nhị phân vẫn có thể bị phản biện.": "Tuy nhiên, kết quả so sánh hai nhóm vẫn cần được kiểm tra thêm.",
        "quan hệ theo số vòng sửa, các yếu tố nhiễu và độ bền theo phân khúc": "xu hướng theo số lần thay đổi, các biến khác và tính nhất quán theo loại công trình",
        "Nếu thay đổi thiết kế chỉ là nhãn phân loại ngẫu nhiên": "Nếu số lần thay đổi thiết kế không liên hệ với tiến độ",
        "rủi ro thay đổi ra sao khi dự án bước từ ít vòng sửa sang vùng thay đổi nhiều": "số ngày chậm thay đổi ra sao khi dự án chuyển từ ít sang nhiều lần thay đổi",
        "“Mỗi lần bản vẽ quay lại bàn thiết kế, lịch bàn giao trượt thêm một nấc.” Sau đó mới nêu con số 4,9 ngày.": "“Trong bộ dữ liệu, số ngày chậm có xu hướng tăng cùng số lần thay đổi thiết kế.” Sau đó, người trình bày nêu mức tăng trung bình 4,9 ngày cho mỗi lần thay đổi.",
        "Để kiểm tra các cách giải thích khác, nhóm xây dựng một mô hình hồi quy chuẩn hóa. Báo cáo xây dựng mô hình hồi quy chuẩn hóa gồm": "Để kiểm tra các cách giải thích khác, nhóm xây dựng mô hình hồi quy chuẩn hóa gồm",
        "hiệu ứng theo khách hàng": "đặc điểm riêng của từng khách hàng",
        "Một quan hệ tổng thể có thể bị chi phối bởi một phân khúc lớn hoặc đặc thù. Để tránh khái quát vội vàng, báo cáo tính tương quan thay đổi thiết kế–số ngày chậm riêng trong từng loại công trình. Kết quả nhìn chung cùng chiều ở các nhóm bảo trì, cải tạo, lắp đặt, mở rộng, nâng cấp, sửa chữa và xây dựng mới.": "Một kết quả tổng thể có thể bị chi phối bởi một loại công trình chiếm tỷ trọng lớn. Vì vậy, báo cáo so sánh số ngày chậm trung bình giữa nhóm có và không thay đổi thiết kế trong từng loại công trình. Nhóm có thay đổi thiết kế đều chậm hơn ở các nhóm bảo trì, cải tạo, lắp đặt, mở rộng, nâng cấp, sửa chữa và xây dựng mới.",
        "khoảng cách giữa nhóm có và không thay đổi thiết kế được duy trì ở các nhóm dự án theo năm bắt đầu": "khoảng cách giữa nhóm có và không thay đổi thiết kế xuất hiện ở các năm bắt đầu khác nhau",
        "vì khoảng thời gian ngắn và bộ dữ liệu": "do khoảng thời gian quan sát còn ngắn",
        "Giá trị trung bình có thể bị kéo bởi một số dự án cực đoan. Vì vậy, báo cáo tính thêm tỷ lệ trễ trong từng nhóm số lần thay đổi thiết kế. Biểu đồ cho thấy toàn bộ phân phối dịch chuyển lên khi số vòng sửa tăng, không chỉ riêng trung bình. Trung vị, khoảng tứ phân vị và vùng biến thiên đều thay đổi theo cùng hướng.": "Để bổ sung cho số ngày chậm trung bình, báo cáo tính tỷ lệ dự án bị trễ trong bốn nhóm số lần thay đổi: 0, 1–2, 3–5 và trên 5. Tỷ lệ trễ tăng dần theo số lần thay đổi thiết kế.",
        "Cách làm này được ghi rõ trong phụ đề nhằm tránh hiểu nhầm. Trong báo cáo thực tế, nên cung cấp thêm phụ lục về ngoại lệ, đặc biệt các dự án có thay đổi cao nhưng độ trễ thấp hoặc ngược lại. Những trường hợp lệch khỏi xu hướng thường chứa bài học về khả năng phục hồi tiến độ.": "Cỡ mẫu được ghi trực tiếp trên mỗi cột, đặc biệt để người đọc thận trọng với nhóm có ít dự án.",
        "![Phân phối và rủi ro ngoài giá trị trung bình]": "![Tỷ lệ trễ theo mức thay đổi thiết kế]",
        "mốc chốt thiết kế là mốc": "Mốc chốt thiết kế là thời điểm",
        "một chu kỳ từ freeze đến nghiệm thu": "một chu kỳ từ mốc chốt thiết kế đến nghiệm thu",
        "phát sinh sau freeze": "phát sinh sau mốc chốt thiết kế",
        "số vòng sửa sau freeze giảm": "số vòng sửa sau mốc chốt thiết kế giảm",
        "đây là trường cần bổ sung trong triển khai thực tế": "đây là trường dữ liệu cần được bổ sung khi triển khai thực tế",
        "**Ngụy biện đồng nhất tương quan với quan hệ nhân quả (ngụy biện đồng nhất tương quan với quan hệ nhân quả)**": "**Ngụy biện đồng nhất tương quan với quan hệ nhân quả (correlation fallacy)**",
        "kiểm tra độ bền": "kiểm tra tính nhất quán",
        "6.000 dự án phân bố thế nào?": "Số lần thay đổi liên hệ thế nào với số ngày chậm?",
        "Nếu một vòng sửa bản vẽ chỉ là thay đổi trên giấy, vì sao lịch bàn giao lại trượt gần năm ngày?": "Số ngày chậm thay đổi thế nào khi dự án phát sinh thêm một lần thay đổi thiết kế?",
        "biểu đồ yếu tố nhiễu và phân khúc": "biểu đồ hệ số và kết quả theo loại công trình",
        "lỗi phát hiện sau freeze": "lỗi phát hiện sau mốc chốt thiết kế",
        "Kịch bản giảm một vòng sửa cho thấy tiềm năng thu hồi 18,8% quỹ ngày chậm.": "Phân tích độ nhạy cho thấy tổng số ngày chậm có thể giảm 18,8% nếu mỗi dự án có thay đổi giảm được tối đa một lần thay đổi.",
        "chọn một nhóm dự án mới để chương trình thí điểm": "chọn một nhóm dự án mới để triển khai chương trình thí điểm",
        "Nếu chương trình thí điểm xác nhận quan hệ, doanh nghiệp có cơ sở mở rộng chính sách; nếu không,": "Nếu nhóm thí điểm cải thiện đồng thời các chỉ số đã xác định, doanh nghiệp có thể xem xét mở rộng chính sách; nếu không,",
        "`01_thanh_ty_le_tien_do.png` — Context tiến độ": "`01_thanh_ty_le_tien_do.png` — Tỷ lệ dự án trễ và đúng hạn",
        "`04_phan_tan_xu_huong.png` — Đường xu hướng trung tâm": "`04_phan_tan_xu_huong.png` — Quan hệ giữa số lần thay đổi và số ngày chậm",
        "`06_cot_nhom_loai_cong_trinh.png` — Kiểm tra phân khúc": "`06_cot_nhom_loai_cong_trinh.png` — So sánh theo loại công trình",
        "`09_cot_ty_le_tre_theo_muc.png` — Phân phối độ trễ": "`09_cot_ty_le_tre_theo_muc.png` — Tỷ lệ trễ theo mức thay đổi",
        "`biểu đồs/`": "`charts/`",
        "49,887": "49.887",
        "40,500": "40.500",
        "9,387": "9.387",
    }
    for old, new in editorial_replacements.items():
        text = text.replace(old, new)

    # Không dịch tên thư mục ảnh khi chuẩn hóa từ "chart" trong phần nội dung.
    text = text.replace("(biểu đồs/", "(charts/")

    # Phần 3 là cấu trúc câu chuyện theo đúng bố cục chấm điểm.
    if "# PHẦN 3 — XÂY DỰNG CẤU TRÚC CÂU CHUYỆN" not in text:
        text = text.replace(
            "## Context: quy mô vấn đề tiến độ",
            "# PHẦN 3 — XÂY DỰNG CẤU TRÚC CÂU CHUYỆN\n\nPhần này trình bày lần lượt bối cảnh, khác biệt giữa hai nhóm, các bằng chứng kiểm tra, kết luận chính và đề xuất triển khai. Mỗi bước sử dụng một biểu đồ dễ đọc và trả lời một câu hỏi cụ thể.\n\n<div style=\"page-break-after: always;\"></div>\n\n## Context: quy mô vấn đề tiến độ",
            1,
        )

    # Chuẩn hóa dấu thập phân trong phần nội dung tiếng Việt.
    for old, new in {
        "58.0%": "58,0%", "49.2%": "49,2%", "46.2%": "46,2%", "70.2%": "70,2%",
        "39.0%": "39,0%", "61.0%": "61,0%", "18.8%": "18,8%",
        "-0.2": "-0,2", "8.8": "8,8", "4.9": "4,9", "0.396": "0,396", "0.257": "0,257",
    }.items():
        text = text.replace(old, new)

    # Rà soát cuối sau khi chuẩn hóa số để xử lý các câu có chứa số thập phân.
    for old, new in {
        "Project cuối kỳ": "bài tập cuối kỳ",
        "tín hiệu cảnh báo": "chỉ báo cảnh báo",
        "vòng sửa": "lần thay đổi",
        "Theo kịch bản giảm được một lần thay đổi, quy mô thời gian có thể thu hồi là": "Theo trường hợp giả định giảm được một lần thay đổi, tổng số ngày chậm có thể giảm là",
        "Thời gian trễ có thể được thu hồi": "Số ngày chậm có thể giảm",
        "bao nhiêu thời gian trễ có thể được thu hồi": "tổng số ngày chậm có thể giảm bao nhiêu",
        "tổng ngày có thể thu hồi": "tổng số ngày chậm có thể giảm",
        "“Mỗi lần bản vẽ quay lại bàn thiết kế, lịch bàn giao trượt thêm một nấc.” Sau đó mới nêu con số 4,9 ngày.": "“Trong bộ dữ liệu, số ngày chậm có xu hướng tăng cùng số lần thay đổi thiết kế.” Sau đó, người trình bày nêu mức tăng trung bình 4,9 ngày cho mỗi lần thay đổi.",
        "quan hệ không chỉ xuất hiện vì một loại công trình chiếm ưu thế": "khác biệt giữa hai nhóm không chỉ xuất hiện ở một loại công trình",
        "Màu vàng được dùng cho bằng chứng hỗ trợ, không cạnh tranh với màu đỏ của biến trọng tâm.": "Màu xám thể hiện nhóm không thay đổi; màu đỏ thể hiện nhóm có thay đổi thiết kế.",
        "Sự tin cậy còn đến từ việc trình bày các bằng chứng không thuận tiện cho thông điệp.": "Báo cáo trình bày cả những kết quả cho thấy mô hình còn giới hạn.",
        "Báo cáo giữ các kết quả này thay vì chỉ chọn phần làm cho thay đổi thiết kế trông mạnh nhất.": "Các kết quả này được giữ lại để người đọc đánh giá đúng mức độ giải thích của mô hình.",
        "Chúng ta không thể loại bỏ mọi thay đổi, nhưng có thể ngăn một lần thay đổi nhỏ trở thành một vòng trượt tiến độ lớn. Hãy khóa thiết kế đúng mốc, kiểm soát thay đổi trong 48 giờ và đo kết quả bằng chương trình thí điểm.": "Không thể loại bỏ mọi thay đổi thiết kế, nhưng có thể kiểm soát thời điểm phát sinh và tác động của từng yêu cầu. Nhóm đề xuất áp dụng mốc chốt thiết kế, xử lý yêu cầu trong 48 giờ và đánh giá kết quả qua chương trình thí điểm.",
        "Kịch bản giảm một lần thay đổi cho thấy tiềm năng thu hồi 18,8% quỹ ngày chậm.": "Phân tích độ nhạy cho thấy tổng số ngày chậm có thể giảm 18,8% nếu mỗi dự án có thay đổi giảm được tối đa một lần thay đổi.",
        "một chương trình thí điểm mốc chốt thiết kế có KPI": "một chương trình thí điểm áp dụng mốc chốt thiết kế, với các chỉ số đánh giá (KPI)",
        "Cohort": "Nhóm dự án",
        "độ tin cậy nội bộ không đồng nghĩa với giá trị ngoại suy": "độ tin cậy trong bộ dữ liệu không đồng nghĩa với khả năng áp dụng rộng",
        "Hành động là chương trình thí điểm mốc chốt thiết kế có KPI dẫn dắt, KPI kết quả và KPI cân bằng.": "Hành động là chương trình thí điểm áp dụng mốc chốt thiết kế, với KPI dẫn dắt, KPI kết quả và KPI cân bằng.",
        "Xám là tham chiếu, xanh là đúng hoặc sớm hạn, vàng là lớp bằng chứng hỗ trợ.": "Xám là nhóm tham chiếu; xanh là trạng thái đúng hoặc sớm hạn và kết quả sau cải thiện.",
        "đỏ cho thay đổi thiết kế và rủi ro, xám cho tham chiếu, vàng cho bằng chứng hỗ trợ, xanh cho kết quả tốt hoặc giải pháp": "đỏ cho thay đổi thiết kế và rủi ro, xám cho nhóm tham chiếu, xanh cho trạng thái đúng hoặc sớm hạn và kết quả sau cải thiện",
    }.items():
        text = text.replace(old, new)
    return text

def write_v2_notebook():
    """Tạo notebook tự chứa để tái lập đúng bộ biểu đồ v2 trong thư mục nộp bài."""
    def md(source):
        return {"cell_type": "markdown", "metadata": {}, "source": source.splitlines(keepends=True)}

    def code(source):
        return {
            "cell_type": "code", "execution_count": None, "metadata": {},
            "outputs": [], "source": source.splitlines(keepends=True),
        }

    setup = """from pathlib import Path
import re
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

ROOT = Path.cwd()
SOURCE = ROOT / "du_lieu_tien_do_du_an.csv"
CHARTS = ROOT / "charts"
CHARTS.mkdir(parents=True, exist_ok=True)

RED = "#B83A32"
NAVY = "#23363D"
GREEN = "#2F6B5C"
GRAY = "#AEB7BB"
MUTED = "#617178"

sns.set_theme(style="white", font_scale=1.04)
plt.rcParams.update({
    "figure.dpi": 160, "font.family": "DejaVu Sans",
    "axes.titleweight": "bold", "axes.titlesize": 15,
    "axes.labelsize": 11, "axes.edgecolor": "#D6DEE1",
    "xtick.color": NAVY, "ytick.color": NAVY, "text.color": NAVY,
})
"""
    helpers = "\n\n".join(inspect.getsource(fn) for fn in [
        currency, vi_num, vi_int, load_data, title, clean, save, coefficients, make_charts
    ])
    audit = """d = load_data()
print(f"Số dòng: {vi_int(len(d))}")
print(f"Tỷ lệ trễ hạn: {vi_num((d['Số ngày chậm'] > 0).mean() * 100)}%")
print(f"Thiếu dữ liệu ở biến trọng tâm: {d['Số lần thay đổi thiết kế'].isna().sum()}")
display(d[['Số lần thay đổi thiết kế', 'Số ngày chậm', 'Số ngày mưa',
           'Số lần thiếu vật tư', 'Giá trị hợp đồng (Tỷ VNĐ)']].describe().round(2))
"""
    run = """stats = make_charts(d)
slope, corr, r2, before, recovered, after = stats
print(f"Độ dốc mô tả: {vi_num(slope)} ngày/lần thay đổi")
print(f"Tương quan: {vi_num(corr, 3)}; R² mô tả: {vi_num(r2, 3)}")
print(f"Phân tích độ nhạy: số ngày chậm có thể giảm {vi_int(recovered)} ngày ({vi_num(recovered/before*100)}%)")
print(f"Đã lưu {len(list(CHARTS.glob('*.png')))} hình vào: {CHARTS}")
"""
    notebook = {
        "cells": [
            md("""# Quản lý thay đổi thiết kế để hạn chế chậm tiến độ

Notebook v2 phục vụ bài tập cuối kỳ môn Data Storytelling. Các kết quả được diễn giải trong phạm vi bộ dữ liệu dự án đi kèm.

**Thông điệp trung tâm:** Các yêu cầu thay đổi thiết kế phát sinh sau mốc chốt có liên hệ với số ngày chậm cao hơn. Nhóm đề xuất Trưởng Ban Quản lý dự án phê duyệt chương trình thí điểm gồm mốc chốt thiết kế, tổ kiểm soát thay đổi và thời hạn xử lý 48 giờ trước khi áp dụng rộng.

**Người ra quyết định chính:** Trưởng Ban Quản lý dự án.
"""),
            md("""## Storyboard

1. Bối cảnh — quy mô trễ tiến độ.
2. Điểm mở đầu — khác biệt giữa nhóm có và không thay đổi thiết kế.
3. Bằng chứng — xu hướng theo số lần thay đổi và các kiểm tra tính nhất quán.
4. Kết luận chính — mức tăng ngày chậm đi cùng mỗi lần thay đổi.
5. Hành động — chương trình thí điểm và phân tích tác động.

Mỗi biểu đồ trả lời một câu hỏi; các hình kiểm tra chi tiết không tạo thêm hướng kể chuyện mới.
"""),
            md("## 1. Thiết lập môi trường và ngôn ngữ trực quan"),
            code(setup),
            md("## 2. Hàm xử lý dữ liệu và tạo bộ biểu đồ v2"),
            code(helpers),
            md("## 3. Kiểm tra dữ liệu đầu vào"),
            code(audit),
            md("## 4. Tạo 10 biểu đồ và tóm tắt kết quả"),
            code(run),
            md("""## 5. Giới hạn diễn giải

- Hồi quy, tương quan và phân tích độ nhạy là các công cụ mô tả, không tự động chứng minh quan hệ nhân quả.
- Hiệu quả của mốc chốt thiết kế cần được đánh giá bằng chương trình thí điểm, sử dụng số liệu trước triển khai và nhóm so sánh phù hợp.
"""),
        ],
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }
    (OUT / "lecture3_v2.ipynb").write_text(json.dumps(notebook, ensure_ascii=False, indent=1), encoding="utf-8")

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    CHARTS.mkdir(parents=True, exist_ok=True)
    d = load_data()
    stats = make_charts(d)
    report = rewrite_report(stats)
    (OUT / "Bao_cao_Data_Storytelling_v2.md").write_text(report, encoding="utf-8")
    shutil.copy2(SOURCE, OUT / SOURCE.name)
    shutil.copy2(SOURCE_XLSX, OUT / SOURCE_XLSX.name)
    write_v2_notebook()
    current_charts = {
        "01_thanh_ty_le_tien_do.png", "02_cot_so_sanh_hai_nhom.png",
        "03_duong_muc_thay_doi.png", "04_phan_tan_xu_huong.png",
        "05_thanh_he_so_chuan_hoa.png", "06_cot_nhom_loai_cong_trinh.png",
        "07_duong_theo_nam.png", "08_thanh_nguyen_nhan.png",
        "09_cot_ty_le_tre_theo_muc.png", "10_cot_truoc_sau.png",
    }
    for obsolete_chart in CHARTS.glob("*.png"):
        if obsolete_chart.name not in current_charts:
            obsolete_chart.unlink()
    for obsolete in [
        OUT / "lecture3.ipynb", OUT / "Bao_cao_Data_Storytelling_v2.html", OUT / ".DS_Store",
        OUT / "data_synthetic_design_dominant.csv", OUT / "data_synthetic_project_schedule.csv",
        OUT / "data_synthetic_project_schedule.xlsx",
    ]:
        obsolete.unlink(missing_ok=True)
    print(f"Output: {OUT}")
    print(f"Charts: {len(list(CHARTS.glob('*.png')))}")
    print(f"Words: {len(report.split()):,}")
    print(f"Page breaks: {report.count('page-break-after')}")

if __name__ == "__main__":
    main()
