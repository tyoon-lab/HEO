import pandas as pd
import matplotlib.pyplot as plt

DATA = "modeling/si_v14/HEO_SI_S24_MG_U4_TRAJECTORY_2026-09-30.csv"
OUT = "HEO_SI_Figure_S24_Mg_thermodynamic_trajectory"

df = pd.read_csv(DATA)
exp = df[df["u4"].astype(str) == "experimental_Mg_over_HEO"].iloc[0]
m = df[df["u4"].astype(str) != "experimental_Mg_over_HEO"].copy()
m["u4"] = pd.to_numeric(m["u4"])

fig, axs = plt.subplots(1, 3, figsize=(10.2, 3.4))

metrics = [
    ("Q_ratio", r"$Q/Q_0$", float(exp["Q_ratio"])),
    ("t63_ratio", r"$t_{63}/t_{63,0}$", float(exp["t63_ratio"])),
    ("DeltaE_model_ratio", r"$\Delta E_{model}/\Delta E_0$", float(exp["DeltaE_model_ratio"])),
]

for ax, (col, ylabel, expval), label in zip(axs, metrics, ["(a)", "(b)", "(c)"]):
    ax.plot(m["u4"], m[col], marker="o", lw=1.6, ms=4.5)
    ax.axhline(expval, ls="--", lw=0.9)
    ax.axvline(-3.0, ls=":", lw=0.8)
    ax.set_xlabel(r"Product-side equilibrium offset, $u_4$")
    ax.set_ylabel(ylabel)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(top=False, right=False)
    ax.text(-0.18, 1.04, label, transform=ax.transAxes, fontsize=12)

fig.tight_layout()
fig.savefig(OUT + ".pdf", bbox_inches="tight")
fig.savefig(OUT + ".png", dpi=320, bbox_inches="tight")
