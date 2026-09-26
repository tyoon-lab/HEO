import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from PIL import Image
from pathlib import Path

# Reproducible draft artwork for Main Figure 7.
# Run from the repository root.
# Uses only committed HEO model outputs; no fitted experimental parameters are introduced.

ROOT = Path(".")
OUT = ROOT / "manuscript" / "figure7_draft"
OUT.mkdir(parents=True, exist_ok=True)

plt.rcParams.update({
    "font.family": "Arial",
    "font.size": 8.2,
    "axes.labelsize": 8.9,
    "xtick.labelsize": 8.2,
    "ytick.labelsize": 8.2,
    "legend.fontsize": 8.2,
    "axes.spines.top": False,
    "axes.spines.right": False,
})

# Panel a: literature-informed coarse-grained network.
fig = plt.figure(figsize=(3.55, 3.0), dpi=300)
ax = fig.add_axes([0.04, 0.10, 0.93, 0.82])
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")

xs = [0.10, 0.37, 0.63, 0.90]
labels = ["O", "I", "I*", "C"]
sublabels = [
    "oxide-\nderived",
    "reduced /\nlithiated",
    "structurally\nreconstructed",
    "deeply\nconverted",
]

for x, lab, sub in zip(xs, labels, sublabels):
    box = FancyBboxPatch(
        (x - 0.072, 0.50), 0.144, 0.17,
        boxstyle="round,pad=0.018,rounding_size=0.024",
        fill=False, linewidth=1.1
    )
    ax.add_patch(box)
    ax.text(x, 0.585, lab, ha="center", va="center", fontsize=10.5)
    ax.text(x, 0.39, sub, ha="center", va="top", fontsize=7.2, linespacing=1.05)

for x1, x2 in zip(xs[:-1], xs[1:]):
    ax.annotate("", xy=(x2 - 0.083, 0.61), xytext=(x1 + 0.083, 0.61),
                arrowprops=dict(arrowstyle="->", lw=0.95))
    ax.annotate("", xy=(x1 + 0.083, 0.555), xytext=(x2 - 0.083, 0.555),
                arrowprops=dict(arrowstyle="->", lw=0.95))

mid = [(xs[i] + xs[i + 1]) / 2 for i in range(3)]
ax.text(mid[0], 0.75, "R1\nFaradaic", ha="center", va="bottom", fontsize=7.4)
ax.text(mid[1], 0.75, "R2\nreconstruction", ha="center", va="bottom", fontsize=7.4)
ax.text(mid[2], 0.75, "R3\nFaradaic", ha="center", va="bottom", fontsize=7.4)
ax.text(0.50, 0.14, "Effective kinetic states; no unique phase assignment",
        ha="center", va="center", fontsize=7.3)
ax.text(-0.015, 1.015, "(a)", transform=ax.transAxes, fontsize=11, va="top")
fig.savefig(OUT / "panel_a_network.png", bbox_inches="tight", pad_inches=0.06)
plt.close(fig)

# Panel b: current-off redistribution.
off = pd.read_csv(
    ROOT / "modeling" / "HEO_MICROKINETIC_CURRENT_OFF_BALANCE_LITERATURE_INFORMED_2026-09-25.csv"
)
off = off.loc[off["rest_time_s"] >= 3].copy()

fig, ax = plt.subplots(figsize=(3.55, 3.0), dpi=300)
t_min = off["rest_time_s"] / 60.0
ax.plot(t_min, off["r1"] * 1e5, marker="o", ms=3, label=r"$r_1$")
ax.plot(t_min, off["r2"] * 1e5, marker="s", ms=3, label=r"$r_2$")
ax.plot(t_min, off["r3"] * 1e5, marker="^", ms=3, label=r"$r_3$")
ax.axhline(0, lw=0.8)
ax.set_xscale("log")
ax.set_xlim(0.045, 70)
ax.set_xlabel("Rest time (min)")
ax.set_ylabel(r"Internal rate ($\\times 10^{-5}$ s$^{-1}$)")
ax.legend(frameon=False, loc="upper right")
ax.text(0.04, 0.08, r"$r_1+r_3\\approx0$ while $r_2\\neq0$",
        transform=ax.transAxes, fontsize=7.3)
ax.text(-0.13, 1.045, "(b)", transform=ax.transAxes, fontsize=11, va="top")
fig.tight_layout()
fig.savefig(OUT / "panel_b_current_off.png", bbox_inches="tight", pad_inches=0.08)
plt.close(fig)

# Panels c and d: capacity-relaxation validation.
validation = pd.read_csv(
    ROOT / "modeling" / "HEO_CAPACITY_RELAXATION_MICROKINETIC_VALIDATION_2026-09-25.csv"
)

hom = validation.loc[validation["test_type"] == "homogeneous_global_scaling"].copy()
fig, ax = plt.subplots(figsize=(3.55, 3.0), dpi=300)
ax.plot(hom["Q_cutoff_normalized"], hom["t63_min_at_matched_state"], marker="o", ms=4)
offsets = [(4, 4), (4, 4), (4, 4), (4, -12), (4, 4)]
for (_, row), offxy in zip(hom.iterrows(), offsets):
    ax.annotate(
        f'{row["global_rate_scale"]:g}×',
        (row["Q_cutoff_normalized"], row["t63_min_at_matched_state"]),
        xytext=offxy, textcoords="offset points", fontsize=7.2
    )
ax.set_xlabel(r"Normalized cutoff capacity, $Q_{\\rm cutoff}$")
ax.set_ylabel(r"Matched-state $t_{63}$ (min)")
ax.text(0.05, 0.08, "faster uniform kinetics  →", transform=ax.transAxes, fontsize=7.4)
ax.text(-0.13, 1.045, "(c)", transform=ax.transAxes, fontsize=11, va="top")
fig.tight_layout()
fig.savefig(OUT / "panel_c_homogeneous.png", bbox_inches="tight", pad_inches=0.08)
plt.close(fig)

het = validation.loc[validation["test_type"] == "heterogeneous_accessibility"].copy()
q = het["Q_cutoff_normalized"].to_numpy()
t63 = het["t63_min_at_matched_state"].to_numpy()

fig, ax = plt.subplots(figsize=(3.55, 3.0), dpi=300)
ax.scatter(q, t63, s=38)
ax.annotate("", xy=(q[1], t63[1]), xytext=(q[0], t63[0]),
            arrowprops=dict(arrowstyle="->", lw=1.1))
ax.annotate("reference", (q[0], t63[0]), xytext=(0, -16),
            textcoords="offset points", ha="center", fontsize=7.4)
ax.annotate("fast + accessible\nslower-R2 population", (q[1], t63[1]), xytext=(5, 3),
            textcoords="offset points", fontsize=7.3)
ax.text(0.06, 0.91, r"$Q_{\\rm cutoff}$  +17.7%", transform=ax.transAxes, fontsize=7.4)
ax.text(0.06, 0.82, r"$t_{63}$  +13.6%", transform=ax.transAxes, fontsize=7.4)
ax.set_xlim(0.53, 0.69)
ax.set_ylim(12.8, 15.9)
ax.set_xlabel(r"Normalized cutoff capacity, $Q_{\\rm cutoff}$")
ax.set_ylabel(r"Matched-state $t_{63}$ (min)")
ax.text(-0.13, 1.045, "(d)", transform=ax.transAxes, fontsize=11, va="top")
fig.tight_layout()
fig.savefig(OUT / "panel_d_heterogeneous.png", bbox_inches="tight", pad_inches=0.08)
plt.close(fig)

# Combine separately rendered panels into a 2x2 draft without using matplotlib subplots.
panel_paths = [
    OUT / "panel_a_network.png",
    OUT / "panel_b_current_off.png",
    OUT / "panel_c_homogeneous.png",
    OUT / "panel_d_heterogeneous.png",
]
imgs = [Image.open(p).convert("RGB") for p in panel_paths]
cell_w = max(im.width for im in imgs)
cell_h = max(im.height for im in imgs)
gap = 36
canvas = Image.new("RGB", (2 * cell_w + gap, 2 * cell_h + gap), "white")

for i, im in enumerate(imgs):
    x0 = (i % 2) * (cell_w + gap)
    y0 = (i // 2) * (cell_h + gap)
    x = x0 + (cell_w - im.width) // 2
    y = y0 + (cell_h - im.height) // 2
    canvas.paste(im, (x, y))

canvas.save(OUT / "HEO_Figure7_microkinetic_existence_proof_DRAFT.png", dpi=(300, 300))
