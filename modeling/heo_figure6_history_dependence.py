import pandas as pd
import matplotlib.pyplot as plt

DATA = "modeling/HEO_FIGURE6_PANEL_DATA_2026-09-27.csv"
OUT = "HEO_Figure6_history_dependence"

samples = ["HEO", "BM-HEO", "Mg-HEO", "BM-Mg-HEO"]
colors = {
    "HEO": "#1f77b4",
    "BM-HEO": "#ff7f0e",
    "Mg-HEO": "#2ca02c",
    "BM-Mg-HEO": "#d62728",
}

df = pd.read_csv(DATA)

fig, axs = plt.subplots(2, 2, figsize=(9.3, 7.2))
axa, axb, axc, axd = axs.ravel()

for sample in samples:
    d = df[df["sample"] == sample].sort_values("cycle")
    axa.plot(d["cycle"], d["z_peak"], marker="o", lw=1.7, ms=5,
             color=colors[sample], label=sample)
    axb.plot(d["cycle"], d["excess_peak_mV"], marker="o", lw=1.7, ms=5,
             color=colors[sample])
    axc.plot(d["cycle"], d["median_t63_min"], marker="o", lw=1.7, ms=5,
             color=colors[sample])

axa.set_ylabel(r"Peak state, $z_{\mathrm{peak}}$")
axb.set_ylabel("Excess peak amplitude (mV)")
axc.set_ylabel(r"Median $t_{63}$ (min)")

for ax in (axa, axb, axc):
    ax.set_xlim(0.85, 3.15)
    ax.set_xticks([1, 2, 3])
    ax.set_xlabel("Cycle")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(top=False, right=False)

axa.set_ylim(0.45, 0.83)
axb.set_ylim(0, 78)
axc.set_ylim(8.5, 13.7)
axa.legend(frameon=False, ncol=2, loc="upper right")

for sample in samples:
    d = df[df["sample"] == sample].sort_values("cycle")
    a_ratio = d.iloc[-1]["excess_peak_mV"] / d.iloc[0]["excess_peak_mV"]
    t_ratio = d.iloc[-1]["median_t63_min"] / d.iloc[0]["median_t63_min"]
    axd.plot(t_ratio, a_ratio, marker="o", ms=6.5, ls="None",
             color=colors[sample])
    axd.text(t_ratio + 0.008, a_ratio, sample, fontsize=8.5, va="center")

axd.axvline(1.0, ls="--", lw=0.9, color="0.45")
axd.axhline(1.0, ls="--", lw=0.9, color="0.45")
axd.set_xlim(0.81, 1.02)
axd.set_ylim(0.32, 1.82)
axd.set_xlabel(r"$t_{63,3}/t_{63,1}$")
axd.set_ylabel(r"$A_3/A_1$")
axd.spines["top"].set_visible(False)
axd.spines["right"].set_visible(False)
axd.tick_params(top=False, right=False)

for label, ax in zip(["(a)", "(b)", "(c)", "(d)"], [axa, axb, axc, axd]):
    ax.text(-0.16, 1.04, label, transform=ax.transAxes, fontsize=13)

fig.subplots_adjust(left=0.10, right=0.98, bottom=0.10, top=0.98,
                    wspace=0.32, hspace=0.34)
fig.savefig(OUT + ".pdf", bbox_inches="tight")
fig.savefig(OUT + ".png", dpi=320, bbox_inches="tight")
