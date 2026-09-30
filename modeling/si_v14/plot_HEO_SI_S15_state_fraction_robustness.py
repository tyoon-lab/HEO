import pandas as pd
import matplotlib.pyplot as plt

ALL4 = "modeling/si_v14/HEO_SI_S15_ALLFOUR_T63_BINNED_2026-09-30.csv"
ROBUST = "modeling/si_v13/HEO_SI_S15_T50_T63_T90_RAW_EXACT_2026-09-29.csv"
OUT = "HEO_SI_Figure_S15_state_and_fraction_robustness"

samples = ["HEO", "BM-HEO", "Mg-HEO", "BM-Mg-HEO"]

a = pd.read_csv(ALL4)
b = pd.read_csv(ROBUST)

fig, axs = plt.subplots(1, 2, figsize=(9.2, 3.8))
ax1, ax2 = axs

for sample in samples:
    d = a[a["sample"] == sample].sort_values("z_median")
    ax1.plot(d["z_median"], d["t63_median_min"], marker="o", lw=1.6, ms=4.5, label=sample)

ax1.set_xlabel(r"Normalized lithiation capacity, $z$")
ax1.set_ylabel(r"$t_{63}$ (min)")
ax1.set_xlim(0.19, 0.64)
ax1.legend(frameon=False, fontsize=8)
ax1.spines["top"].set_visible(False)
ax1.spines["right"].set_visible(False)
ax1.tick_params(top=False, right=False)

ax2.plot(b["Capacity_mAh_g"], b["t50_rate_ratio_HEO_over_BM"], lw=1.5, label=r"$t_{50}$")
ax2.plot(b["Capacity_mAh_g"], b["t63_rate_ratio_HEO_over_BM"], lw=1.5, label=r"$t_{63}$")
ax2.plot(b["Capacity_mAh_g"], b["t90_rate_ratio_HEO_over_BM"], lw=1.5, label=r"$t_{90}$")
ax2.axhline(1.0, ls="--", lw=0.9)
ax2.set_xlabel(r"Matched lithiation capacity (mAh g$^{-1}$)")
ax2.set_ylabel("HEO/BM-HEO relaxation-rate ratio")
ax2.legend(frameon=False)
ax2.spines["top"].set_visible(False)
ax2.spines["right"].set_visible(False)
ax2.tick_params(top=False, right=False)

for label, ax in zip(["(a)", "(b)"], axs):
    ax.text(-0.14, 1.04, label, transform=ax.transAxes, fontsize=12)

fig.tight_layout()
fig.savefig(OUT + ".pdf", bbox_inches="tight")
fig.savefig(OUT + ".png", dpi=320, bbox_inches="tight")
