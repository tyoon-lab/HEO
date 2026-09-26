import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Figure 4 production draft for the HEO capacity-kinetics manuscript.
# Panel (a) is intentionally schematic and should be replaced by a raw
# representative GITT pulse/rest trace before submission if the source trace
# is recovered. Panels (b-d) use the current authoritative numerical summaries.

HERE = Path(__file__).resolve().parent
OUT = HERE / "figure4_output"
OUT.mkdir(exist_ok=True)

state = pd.read_csv(HERE / "HEO_TY10_HEO_BM_STATE_MATCHED_RATIOS_2026-09-26.csv")
summary = pd.read_csv(HERE / "HEO_FIGURE4_SUMMARY_DATA_2026-09-26.csv")

capacity = state["Capacity_mAh_g"].to_numpy()
dapp_ratio = state["Dapp_ratio_BM_over_HEO"].to_numpy()
relax_rate_ratio = 1.0 / state["t63_ratio_BM_over_HEO"].to_numpy()

samples = summary["Sample"].tolist()
rev_capacity = summary["First_cycle_reversible_capacity_mAh_g"].to_numpy()
median_t63 = summary["Median_t63_200_800_mAh_g_min"].to_numpy()

plt.rcParams.update({
    "font.family": "Arial",
    "font.size": 9.2,
    "axes.labelsize": 10.2,
    "xtick.labelsize": 9.0,
    "ytick.labelsize": 9.0,
    "legend.fontsize": 8.6,
    "axes.spines.top": False,
    "axes.spines.right": False,
})

fig = plt.figure(figsize=(7.25, 6.25), dpi=300)
gs = fig.add_gridspec(
    2, 2,
    left=0.10, right=0.98, bottom=0.10, top=0.97,
    wspace=0.33, hspace=0.35
)

# (a) Operational definition of the current-off descriptors.
ax = fig.add_subplot(gs[0, 0])
t1 = np.linspace(-10, 0, 100)
E1 = np.linspace(1.00, 0.70, 100)
t2 = np.linspace(0, 60, 500)
E2 = 0.70 + 0.23 * (1 - np.exp(-t2 / 12.0))
E3 = 0.70 + 0.23 * (1 - np.exp(-(3/60) / 12.0))
E60 = E2[-1]
target = E3 + 0.632 * (E60 - E3)
t63_schematic = t2[np.argmin(np.abs(E2 - target))]

ax.plot(t1, E1, linewidth=1.4)
ax.plot(t2, E2, linewidth=1.4)
ax.axvline(0, linestyle=":", linewidth=0.9)
ax.axvline(t63_schematic, linestyle="--", linewidth=0.9)
ax.plot([3/60, 60], [E3, E60], linestyle="None", marker="o", markersize=4)
ax.annotate(
    "3 s reference",
    xy=(3/60, E3), xytext=(6, 0.735),
    arrowprops=dict(arrowstyle="->", linewidth=0.8),
    fontsize=8.2,
)
ax.annotate(
    r"$t_{63}$",
    xy=(t63_schematic, target),
    xytext=(t63_schematic + 7, target - 0.055),
    arrowprops=dict(arrowstyle="->", linewidth=0.8),
    fontsize=8.5,
)
ax.annotate(
    "", xy=(49, E60), xytext=(49, E3),
    arrowprops=dict(arrowstyle="<->", linewidth=0.9),
)
ax.text(50.5, (E3 + E60)/2, r"$\Delta E_{\rm relax}$", va="center", fontsize=8.4)
ax.text(-5, 0.97, "10 min pulse", ha="center", va="top", fontsize=8.3)
ax.text(29, 0.97, "60 min rest", ha="center", va="top", fontsize=8.3)
ax.text(0.04, 0.08, "schematic definition", transform=ax.transAxes, fontsize=8.0)
ax.set_xlim(-10, 60)
ax.set_ylim(0.66, 1.02)
ax.set_xlabel("Time relative to interruption (min)")
ax.set_ylabel("Potential (a.u.)")
ax.set_yticks([])
ax.text(-0.16, 1.04, "(a)", transform=ax.transAxes, fontsize=12, va="top")

# (b) State-matched ranking inversion. Both ratios are oriented so that
# values above unity mean that BM-HEO is ranked as faster.
ax = fig.add_subplot(gs[0, 1])
ax.plot(capacity, dapp_ratio, marker="o", markersize=3.2, linewidth=1.2)
ax.plot(
    capacity, relax_rate_ratio,
    marker="s", markersize=3.0, linewidth=1.2, linestyle="--"
)
ax.axhline(1.0, linestyle=":", linewidth=0.9)
ax.set_xlim(190, 810)
ax.set_ylim(0.45, 3.35)
ax.set_xlabel(r"State-matched capacity (mAh g$^{-1}$)")
ax.set_ylabel("Ranking ratio  (>1: faster BM-HEO)")
ax.text(0.04, 0.93, r"$D_{\rm app,BM}/D_{\rm app,HEO}$", transform=ax.transAxes, fontsize=8.7)
ax.text(0.04, 0.84, r"median = 1.78; 37/37 > 1", transform=ax.transAxes, fontsize=8.0)
ax.text(0.47, 0.16, r"$t_{63,\rm HEO}/t_{63,\rm BM}$", transform=ax.transAxes, fontsize=8.7)
ax.text(0.47, 0.075, r"median = 0.762; 35/37 < 1", transform=ax.transAxes, fontsize=8.0)
ax.text(-0.16, 1.04, "(b)", transform=ax.transAxes, fontsize=12, va="top")

# (c) Pairwise milling effect on the model-free relaxation timescale.
ax = fig.add_subplot(gs[1, 0])
x = np.array([0, 1])
ax.plot(x, median_t63[[0, 1]], marker="o", markersize=5, linewidth=1.3)
ax.plot(
    x, median_t63[[2, 3]],
    marker="s", markersize=5, linewidth=1.3, linestyle="--"
)
for xi, yi, label in [
    (0, median_t63[0], "HEO"),
    (1, median_t63[1], "BM-HEO"),
    (0, median_t63[2], "Mg-HEO"),
    (1, median_t63[3], "BM-Mg-HEO"),
]:
    ax.annotate(label, (xi, yi), xytext=(4, 4), textcoords="offset points", fontsize=8.1)
ax.set_xticks([0, 1], ["Unmilled", "Ball-milled"])
ax.set_xlim(-0.18, 1.18)
ax.set_ylim(7.7, 13.8)
ax.set_ylabel(r"Median $t_{63}$ (min)")
ax.text(-0.16, 1.04, "(c)", transform=ax.transAxes, fontsize=12, va="top")

# (d) Accessible capacity versus direct relaxation timescale.
ax = fig.add_subplot(gs[1, 1])
ax.plot(
    rev_capacity[[0, 1]], median_t63[[0, 1]],
    linestyle="None", marker="o", markersize=6
)
ax.plot(
    rev_capacity[[2, 3]], median_t63[[2, 3]],
    linestyle="None", marker="s", markersize=6
)
offsets = {
    "HEO": (-20, -17),
    "BM-HEO": (5, 4),
    "Mg-HEO": (-30, 5),
    "BM-Mg-HEO": (5, 4),
}
for x0, y0, label in zip(rev_capacity, median_t63, samples):
    ax.annotate(label, (x0, y0), xytext=offsets[label], textcoords="offset points", fontsize=8.1)

ax.annotate(
    "", xy=(rev_capacity[1], median_t63[1]),
    xytext=(rev_capacity[0], median_t63[0]),
    arrowprops=dict(arrowstyle="->", linewidth=1.0),
)
ax.annotate(
    "", xy=(rev_capacity[3], median_t63[3]),
    xytext=(rev_capacity[2], median_t63[2]),
    arrowprops=dict(arrowstyle="->", linewidth=1.0),
)
ax.text(0.55, 0.10, "ball milling", transform=ax.transAxes, fontsize=8.2)
ax.set_xlim(420, 820)
ax.set_ylim(7.7, 13.8)
ax.set_xlabel(r"First-cycle reversible capacity (mAh g$^{-1}$)")
ax.set_ylabel(r"Median $t_{63}$ (min)")
ax.text(-0.16, 1.04, "(d)", transform=ax.transAxes, fontsize=12, va="top")

fig.savefig(
    OUT / "HEO_Figure4_capacity_kinetics_ranking_DRAFT.png",
    dpi=300, bbox_inches="tight"
)
fig.savefig(
    OUT / "HEO_Figure4_capacity_kinetics_ranking_DRAFT.svg",
    bbox_inches="tight"
)
plt.close(fig)
