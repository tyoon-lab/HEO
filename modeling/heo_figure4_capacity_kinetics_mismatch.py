"""Generate the current Figure 4 artwork for the HEO manuscript.

Panels
(a) representative measured HEO GITT pulse/rest definition using pulse 48;
(b) state-matched mismatch between conventional D_app and direct relaxation ordering;
(c) relaxation-magnitude versus relaxation-timescale map for all four materials;
(d) first-cycle second-half capacity versus relaxation-timescale map.

The script does not refit the authoritative state-matched HEO/BM ratios. Panel (b)
reads the committed audit CSV. Panels (c,d) use the frozen summary values documented
in the SI and Figure-4 logic note.
"""

from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "figure4_artwork"
OUT.mkdir(exist_ok=True)

PULSE_CSV = ROOT / "HEO_FIGURE4_PANEL_A_PULSE48_COMPACT_2026-09-26.csv"
RATIO_CSV = ROOT / "HEO_TY10_HEO_BM_STATE_MATCHED_RATIOS_2026-09-26.csv"

plt.rcParams.update(
    {
        "font.family": "DejaVu Sans",
        "font.size": 8.2,
        "axes.labelsize": 8.9,
        "xtick.labelsize": 8.2,
        "ytick.labelsize": 8.2,
        "legend.fontsize": 7.3,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.linewidth": 0.8,
    }
)


def read_csv(path: Path):
    with path.open(newline="") as f:
        return list(csv.DictReader(f))


def save(fig, name: str):
    fig.savefig(OUT / f"{name}.png", dpi=600, bbox_inches="tight", pad_inches=0.06)
    fig.savefig(OUT / f"{name}.svg", bbox_inches="tight", pad_inches=0.06)
    plt.close(fig)


pulse = read_csv(PULSE_CSV)
pulse_t = np.array([float(r["Time_from_pulse_on_s"]) for r in pulse]) / 60.0
pulse_v = np.array([float(r["Voltage_V"]) for r in pulse])

ratio = read_csv(RATIO_CSV)
capacity = np.array([float(r["Capacity_mAh_g"]) for r in ratio])
dapp_ratio = np.array([float(r["Dapp_ratio_BM_over_HEO"]) for r in ratio])
t63_bm_over_heo = np.array([float(r["t63_ratio_BM_over_HEO"]) for r in ratio])
relax_rate_ratio = 1.0 / t63_bm_over_heo

samples = ["HEO", "BM-HEO", "Mg-HEO", "BM-Mg-HEO"]
t63_med = np.array([8.68, 11.57, 11.01, 12.99])
dE_relax_med = np.array([160.9, 176.3, 109.5, 144.3])
second_half_capacity = np.array([609.12, 782.08, 458.91, 580.83])
markers = ["o", "s", "^", "D"]


# Panel (a): measured GITT definition.
fig = plt.figure(figsize=(3.7, 3.0), dpi=300)
ax = fig.add_axes([0.17, 0.17, 0.78, 0.75])
ax.plot(pulse_t, pulse_v, lw=1.15)
ax.axvline(0, lw=0.8, ls="--")
ax.axvline(10, lw=0.8, ls="--")

ref_time = 10.0 + 3.0 / 60.0
ref_idx = np.argmin(np.abs(pulse_t - ref_time))
end_idx = np.argmax(pulse_t)
E3 = pulse_v[ref_idx]
Eend = pulse_v[end_idx]
target = E3 + 0.632 * (Eend - E3)
rest_idx = np.where(pulse_t >= ref_time)[0]
cross_idx = rest_idx[pulse_v[rest_idx] >= target][0]
t63_time = pulse_t[cross_idx]

ax.scatter([ref_time, pulse_t[end_idx], t63_time], [E3, Eend, pulse_v[cross_idx]], s=18, zorder=4)
ax.hlines(target, ref_time, t63_time, linestyles=":", linewidth=0.9)
ax.annotate(
    "",
    xy=(t63_time, target - 0.005),
    xytext=(ref_time, target - 0.005),
    arrowprops=dict(arrowstyle="<->", lw=0.9),
)
ax.text((ref_time + t63_time) / 2, target - 0.014, r"$t_{63}$", ha="center", va="top")

xbr = 66.5
ax.annotate("", xy=(xbr, Eend), xytext=(xbr, E3), arrowprops=dict(arrowstyle="<->", lw=0.9))
ax.text(
    xbr - 1.0,
    (E3 + Eend) / 2,
    r"$\Delta E_{\rm relax}$",
    rotation=90,
    ha="right",
    va="center",
)
ax.text(5.0, 0.546, "10 min pulse", ha="center", va="top")
ax.text(40.0, 0.546, "60 min rest", ha="center", va="top")
ax.text(0.03, 0.08, "HEO; representative pulse 48", transform=ax.transAxes, fontsize=7.2)
ax.set_xlim(-1, 70.5)
ax.set_ylim(0.30, 0.565)
ax.set_xlabel("Time from pulse onset (min)")
ax.set_ylabel("Voltage (V)")
ax.text(-0.17, 1.05, "(a)", transform=ax.transAxes, fontsize=11, va="top")
save(fig, "panel_a")


# Panel (b): conventional D_app versus direct relaxation rate.
fig = plt.figure(figsize=(3.7, 3.0), dpi=300)
ax = fig.add_axes([0.17, 0.17, 0.78, 0.75])
ax.plot(
    capacity,
    dapp_ratio,
    marker="o",
    ms=3.0,
    lw=1.0,
    markevery=4,
    label=r"$D_{\rm app,BM}/D_{\rm app,HEO}$",
)
ax.plot(
    capacity,
    relax_rate_ratio,
    marker="s",
    ms=3.0,
    lw=1.0,
    ls="--",
    markevery=4,
    label=r"$t_{63,\rm HEO}/t_{63,\rm BM}$",
)
ax.axhline(1, lw=0.9, ls=":")
ax.text(0.03, 0.94, ">1: BM faster", transform=ax.transAxes, va="top", fontsize=7.2)
ax.set_xlim(190, 810)
ax.set_ylim(0.5, 3.35)
ax.set_xlabel(r"Matched capacity (mAh g$^{-1}$)")
ax.set_ylabel("Relative kinetic descriptor")
ax.legend(frameon=False, loc="upper right")
ax.text(-0.17, 1.05, "(b)", transform=ax.transAxes, fontsize=11, va="top")
save(fig, "panel_b")


# Panel (c): relaxation magnitude versus relaxation timescale.
fig = plt.figure(figsize=(3.7, 3.0), dpi=300)
ax = fig.add_axes([0.17, 0.17, 0.78, 0.75])
for sample, xv, yv, mk in zip(samples, dE_relax_med, t63_med, markers):
    ax.plot(xv, yv, marker=mk, ms=5, ls="None", label=sample)

# Directional guides: milling in Mg-free, Mg addition to HEO, milling in Mg-containing.
for i, j in [(0, 1), (0, 2), (2, 3)]:
    ax.annotate(
        "",
        xy=(dE_relax_med[j], t63_med[j]),
        xytext=(dE_relax_med[i], t63_med[i]),
        arrowprops=dict(arrowstyle="->", lw=0.8),
    )

ax.set_xlim(100, 185)
ax.set_ylim(8.0, 13.7)
ax.set_xlabel(r"Median $\Delta E_{\rm relax}$ (mV)")
ax.set_ylabel(r"Median $t_{63}$ (min)")
ax.legend(frameon=False, loc="lower right")
ax.text(-0.17, 1.05, "(c)", transform=ax.transAxes, fontsize=11, va="top")
save(fig, "panel_c")


# Panel (d): accessible capacity versus relaxation timescale.
fig = plt.figure(figsize=(3.7, 3.0), dpi=300)
ax = fig.add_axes([0.17, 0.17, 0.78, 0.75])
for sample, xv, yv, mk in zip(samples, second_half_capacity, t63_med, markers):
    ax.plot(xv, yv, marker=mk, ms=5, ls="None", label=sample)

for i, j in [(0, 1), (0, 2), (2, 3)]:
    ax.annotate(
        "",
        xy=(second_half_capacity[j], t63_med[j]),
        xytext=(second_half_capacity[i], t63_med[i]),
        arrowprops=dict(arrowstyle="->", lw=0.8),
    )

ax.set_xlim(430, 810)
ax.set_ylim(8.0, 13.7)
ax.set_xlabel(r"First-cycle second-half capacity (mAh g$^{-1}$)")
ax.set_ylabel(r"Median $t_{63}$ (min)")
ax.legend(frameon=False, loc="lower right")
ax.text(-0.17, 1.05, "(d)", transform=ax.transAxes, fontsize=11, va="top")
save(fig, "panel_d")


# Combine PNG panels for review.
paths = [OUT / "panel_a.png", OUT / "panel_b.png", OUT / "panel_c.png", OUT / "panel_d.png"]
imgs = [Image.open(p).convert("RGB") for p in paths]
cell_w = max(im.width for im in imgs)
cell_h = max(im.height for im in imgs)
gap = 30
canvas = Image.new("RGB", (2 * cell_w + gap, 2 * cell_h + gap), "white")
for i, im in enumerate(imgs):
    x0 = (i % 2) * (cell_w + gap)
    y0 = (i // 2) * (cell_h + gap)
    canvas.paste(im, (x0 + (cell_w - im.width) // 2, y0 + (cell_h - im.height) // 2))

canvas.save(OUT / "HEO_Figure4_capacity_kinetics_mismatch.png", dpi=(600, 600))

print(
    {
        "Dapp_ratio_median": float(np.median(dapp_ratio)),
        "relaxation_rate_ratio_median": float(np.median(relax_rate_ratio)),
        "Dapp_above_1": int(np.sum(dapp_ratio > 1)),
        "relaxation_below_1": int(np.sum(relax_rate_ratio < 1)),
        "pulse48_deltaE_mV": float((Eend - E3) * 1000),
        "pulse48_t63_min": float(t63_time - ref_time),
    }
)
