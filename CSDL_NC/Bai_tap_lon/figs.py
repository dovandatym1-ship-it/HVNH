import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
plt.rcParams["font.family"] = "DejaVu Sans"

# ---------- Figure 1: Kiến trúc luồng dữ liệu Blockchain trong chuỗi cung ứng ----------
fig, ax = plt.subplots(figsize=(9.2, 5.2))
ax.set_xlim(0, 12); ax.set_ylim(0, 8); ax.axis("off")

actors = [
    ("Nông trại\n(Farm)", 1.3, 6.4, "#2E7D32"),
    ("Nhà chế biến\n(Processor)", 4.0, 6.4, "#1565C0"),
    ("Logistics\n(Vận chuyển)", 6.7, 6.4, "#6A1B9A"),
    ("Nhà bán lẻ\n(Retailer)", 9.4, 6.4, "#E65100"),
]
for label, x, y, c in actors:
    box = FancyBboxPatch((x-0.95, y-0.55), 1.9, 1.1, boxstyle="round,pad=0.04,rounding_size=0.12",
                         linewidth=1.6, edgecolor=c, facecolor="white")
    ax.add_patch(box)
    ax.text(x, y, label, ha="center", va="center", fontsize=9.5, color=c, fontweight="bold")

# arrows between actors (physical + transaction flow)
for i in range(len(actors)-1):
    x0 = actors[i][1]+0.95; x1 = actors[i+1][1]-0.95
    ax.add_patch(FancyArrowPatch((x0, 6.4),(x1,6.4), arrowstyle="-|>", mutation_scale=16,
                                 lw=1.6, color="#555"))

ax.text(6.0, 7.35, "Luồng vật lý hàng hóa + Giao dịch (Transaction)", ha="center",
        fontsize=10, style="italic", color="#444")

# Each actor commits a transaction down to the ledger
for label, x, y, c in actors:
    ax.add_patch(FancyArrowPatch((x, y-0.55),(x, 4.55), arrowstyle="-|>", mutation_scale=12,
                                 lw=1.2, color=c, linestyle=(0,(4,2))))

# Ledger band
led = FancyBboxPatch((0.6, 2.7), 10.8, 1.7, boxstyle="round,pad=0.05,rounding_size=0.1",
                     linewidth=1.8, edgecolor="#37474F", facecolor="#ECEFF1")
ax.add_patch(led)
ax.text(6.0, 4.05, "SỔ CÁI PHÂN TÁN (Distributed Ledger) — Hyperledger Fabric / Ethereum",
        ha="center", fontsize=10, fontweight="bold", color="#263238")

# Blocks chained
bx = 1.2
for k in range(5):
    blk = FancyBboxPatch((bx, 2.95), 1.5, 0.75, boxstyle="round,pad=0.02,rounding_size=0.06",
                         linewidth=1.3, edgecolor="#00695C", facecolor="#B2DFDB")
    ax.add_patch(blk)
    ax.text(bx+0.75, 3.32, f"Block {k}\nHash", ha="center", va="center", fontsize=7.5, color="#004D40")
    if k < 4:
        ax.add_patch(FancyArrowPatch((bx+1.5, 3.32),(bx+2.0,3.32), arrowstyle="-|>",
                                     mutation_scale=11, lw=1.3, color="#00695C"))
    bx += 2.0

# Nodes (replication)
nodes = [(2.2,1.3),(4.6,1.0),(7.4,1.0),(9.8,1.3)]
for nx, ny in nodes:
    cir = plt.Circle((nx, ny), 0.42, edgecolor="#283593", facecolor="#C5CAE9", linewidth=1.4)
    ax.add_patch(cir)
    ax.text(nx, ny, "Node", ha="center", va="center", fontsize=7.5, color="#1A237E")
    ax.add_patch(FancyArrowPatch((nx, ny+0.42),(nx, 2.68), arrowstyle="-",
                                 lw=1.0, color="#7986CB", linestyle=(0,(2,2))))
# node-to-node consensus links
for i in range(len(nodes)-1):
    ax.add_patch(FancyArrowPatch(nodes[i], nodes[i+1], arrowstyle="<|-|>",
                                 mutation_scale=9, lw=1.0, color="#7986CB"))
ax.text(6.0, 0.35, "Nhân bản (Replication) trên các Node + Cơ chế đồng thuận (Consensus)",
        ha="center", fontsize=9.5, style="italic", color="#3949AB")

# Smart contract callout
sc = FancyBboxPatch((9.9, 4.55), 1.9, 0.9, boxstyle="round,pad=0.03,rounding_size=0.08",
                    linewidth=1.4, edgecolor="#C62828", facecolor="#FFEBEE")
ax.add_patch(sc)
ax.text(10.85, 5.0, "Smart\nContract", ha="center", va="center", fontsize=8.5,
        color="#B71C1C", fontweight="bold")
ax.add_patch(FancyArrowPatch((9.9,5.0),(7.6,4.4), arrowstyle="-|>", mutation_scale=11,
                             lw=1.2, color="#C62828"))

plt.tight_layout()
plt.savefig("hinh_kientruc.png", dpi=160, bbox_inches="tight", facecolor="white")
plt.close()

# ---------- Figure 2: So sánh Throughput (TPS) ----------
fig, ax = plt.subplots(figsize=(8.6, 4.4))
systems = ["Bitcoin\n(PoW)", "Ethereum\ncông khai", "Hyperledger\nFabric", "RDBMS\n(MySQL/PG)", "Visa\n(tham chiếu)"]
tps = [7, 30, 3500, 30000, 24000]
colors = ["#F9A825","#5C6BC0","#26A69A","#8D6E63","#455A64"]
bars = ax.bar(systems, tps, color=colors, edgecolor="black", linewidth=0.7)
ax.set_yscale("log")
ax.set_ylabel("Thông lượng — Throughput (TPS, thang log)", fontsize=10)
ax.set_title("Hình 2. So sánh thông lượng giao dịch giữa Blockchain và CSDL truyền thống",
             fontsize=10.5, fontweight="bold")
for b, v in zip(bars, tps):
    ax.text(b.get_x()+b.get_width()/2, v*1.15, f"~{v:,} TPS", ha="center", fontsize=9)
ax.set_ylim(1, 80000)
ax.grid(axis="y", linestyle=(0,(2,3)), alpha=0.5)
plt.tight_layout()
plt.savefig("hinh_throughput.png", dpi=160, bbox_inches="tight", facecolor="white")
plt.close()
print("figures done")
