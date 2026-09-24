import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from pathlib import Path

# Literature-informed coarse-grained conversion microkinetic model.
#
# Purpose:
#   Mechanistic-consistency test for GITT current-off relaxation.
#   NOT a unique atomistic mechanism, microscopic-rate fit, or RDS assignment.
#
# Effective conversion network:
#
#   R1: O + nu1 Li+ + nu1 e- <-> I
#   R2: I <-> I*
#   R3: I* + nu3 Li+ + nu3 e- <-> C
#
# O  : oxide-derived state
# I  : reduced/lithiated oxide intermediate
# I* : structurally reconstructed / conversion-active intermediate
# C  : metal/Li2O-containing converted state
#
# R1 and R3 are Faradaic. R2 is a non-Faradaic structural/reconstruction step.
# The network is coarse-grained from established conversion-reaction motifs:
# electron transfer / lithiation -> M-O reconstruction / nucleation ->
# deeper conversion and metal/Li2O formation.
#
# At current interruption:
#
#   j_ext = F (nu1*r1 + nu3*r3) = 0
#
# does NOT require r1 = r3 = 0. With nu1 = nu3 = 1 in the normalized
# illustrative calculation, r1 = -r3 != 0 is allowed, while R2 can also
# continue. Thus internal state redistribution and voltage relaxation can
# persist at zero external current.
#
# Literature motivation (not atomistic identification for this HEO):
#   Ng et al., J. Mater. Chem. A 2021, 9, 523. DOI: 10.1039/D0TA09683K
#   Alsaç et al., ACS Appl. Mater. Interfaces 2026, 18, 1626.
#       DOI: 10.1021/acsami.5c20956
#
# The parameter set below is illustrative and selected only to reproduce the
# experimental-style timescale/amplitude range. It is not fitted to a sample.

OUT = Path(".")
RTF = 8.314462618 * 298.15 / 96485.33212


def algebraic_u(state, japp, pars):
    """Solve the normalized current balance for u = F*eta/(R*T).

    States are [I, Istar, C], with O = 1 - I - Istar - C.
    For alpha1 = alpha3 = 0.5 and nu1 = nu3 = 1:

        japp = r1 + r3 = A*exp(u/2) - B*exp(-u/2)

    which gives a quadratic in y = exp(u/2).
    """
    I, Istar, C = state
    O = max(1.0 - I - Istar - C, 1e-14)
    I = max(I, 1e-14)
    Istar = max(Istar, 1e-14)
    C = max(C, 1e-14)

    k1 = pars["k1"]
    k3 = pars["k3"]
    K1 = pars.get("K1", 1.0)
    K3 = pars.get("K3", 1.0)
    u3 = pars.get("u3", 0.0)

    A = k1 * O + k3 * Istar * np.exp(-u3 / 2.0)
    B = k1 * (I / K1) + k3 * (C / K3) * np.exp(u3 / 2.0)

    y = (japp + np.sqrt(japp * japp + 4.0 * A * B)) / (2.0 * A)
    return 2.0 * np.log(y)


def rates(state, japp, pars):
    I, Istar, C = state
    O = max(1.0 - I - Istar - C, 1e-14)
    Ipos = max(I, 1e-14)
    Istarpos = max(Istar, 1e-14)
    Cpos = max(C, 1e-14)

    k1 = pars["k1"]
    k2f = pars["k2f"]
    k2r = pars["k2r"]
    k3 = pars["k3"]
    K1 = pars.get("K1", 1.0)
    K3 = pars.get("K3", 1.0)
    u3 = pars.get("u3", 0.0)

    u = algebraic_u(state, japp, pars)

    r1 = k1 * (
        O * np.exp(u / 2.0)
        - (Ipos / K1) * np.exp(-u / 2.0)
    )

    # Non-Faradaic structural reconstruction / conversion activation.
    r2 = k2f * Ipos - k2r * Istarpos

    r3 = k3 * (
        Istarpos * np.exp((u - u3) / 2.0)
        - (Cpos / K3) * np.exp(-(u - u3) / 2.0)
    )

    return r1, r2, r3, u


def rhs(state, japp, pars):
    r1, r2, r3, _ = rates(state, japp, pars)

    # O <-> I <-> I* <-> C
    dI = r1 - r2
    dIstar = r2 - r3
    dC = r3
    return np.array([dI, dIstar, dC])


def simulate(
    pars,
    jref=2e-4,
    pulse_s=600.0,
    rest_s=3600.0,
    initial=(0.01, 0.01, 0.05),
):
    initial = np.asarray(initial, dtype=float)

    on = solve_ivp(
        lambda t, y: rhs(y, jref, pars),
        [0.0, pulse_s],
        initial,
        method="LSODA",
        rtol=1e-8,
        atol=1e-10,
    )

    # Dense early sampling preserves the experimental-style 3 s reference.
    t_eval = np.unique(
        np.r_[np.linspace(0.0, 60.0, 121), np.linspace(60.0, rest_s, 355)]
    )

    off = solve_ivp(
        lambda t, y: rhs(y, 0.0, pars),
        [0.0, rest_s],
        on.y[:, -1],
        method="LSODA",
        rtol=1e-8,
        atol=1e-10,
        t_eval=t_eval,
    )

    Eon = -RTF * np.array(
        [algebraic_u(on.y[:, i], jref, pars) for i in range(on.y.shape[1])]
    )
    Eoff = -RTF * np.array(
        [algebraic_u(off.y[:, i], 0.0, pars) for i in range(off.y.shape[1])]
    )

    return on, off, Eon, Eoff


def relaxation_metrics(off, Eoff):
    """Experimental-style 3 s -> 3600 s relaxation metrics."""
    remaining = (Eoff[-1] - Eoff) * 1000.0
    amp3 = float(np.interp(3.0, off.t, remaining))

    target = 0.368 * amp3
    idx = np.where((off.t >= 3.0) & (remaining <= target))[0]
    t63 = np.nan if len(idx) == 0 else float((off.t[idx[0]] - 3.0) / 60.0)

    return amp3, t63, remaining


def numerical_jacobian(fun, x, eps=1e-7):
    x = np.asarray(x, dtype=float)
    J = np.zeros((len(x), len(x)))

    for i in range(len(x)):
        h = eps * max(1.0, abs(x[i]))
        xp = x.copy()
        xm = x.copy()
        xp[i] += h
        xm[i] -= h
        J[:, i] = (fun(xp) - fun(xm)) / (2.0 * h)

    return J


# Representative illustrative parameter set.
# Gives ~24 mV residual relaxation and ~14 min t63 for the reference pulse.
representative = dict(
    k1=2.0e-2,
    k2f=8.483428982440717e-4,
    k2r=4.2417144912203585e-4,
    k3=1.0e-2,
    u3=-3.0,
    K1=1.0,
    K3=1.0,
)

JREF = 2e-4

# -------------------------------------------------------------------------
# 1) Reference pulse/rest and current-off partial-current balance
# -------------------------------------------------------------------------
on_ref, off_ref, Eon_ref, Eoff_ref = simulate(representative, jref=JREF)
amp3_ref, t63_ref, remaining_ref = relaxation_metrics(off_ref, Eoff_ref)

sample_times = np.array(
    [0.0, 3.0, 10.0, 30.0, 60.0, 180.0, 600.0, 900.0, 1800.0, 3600.0]
)

off_rows = []
for t in sample_times:
    state = np.array(
        [np.interp(t, off_ref.t, off_ref.y[j, :]) for j in range(off_ref.y.shape[0])]
    )
    r1, r2, r3, u = rates(state, 0.0, representative)
    E = -RTF * u

    off_rows.append(
        [
            t,
            state[0],
            state[1],
            state[2],
            max(1.0 - state.sum(), 0.0),
            (Eoff_ref[-1] - E) * 1000.0,
            r1,
            r2,
            r3,
            r1 + r3,
        ]
    )

pd.DataFrame(
    off_rows,
    columns=[
        "rest_time_s",
        "I",
        "Istar",
        "C",
        "O",
        "residual_relaxation_to_3600s_mV",
        "r1",
        "r2",
        "r3",
        "r1_plus_r3",
    ],
).to_csv(
    OUT / "HEO_MICROKINETIC_CURRENT_OFF_BALANCE_LITERATURE_INFORMED_2026-09-25.csv",
    index=False,
)

# -------------------------------------------------------------------------
# 2) Pulse-current sweep: amplitude can change strongly while t63 changes little
# -------------------------------------------------------------------------
factors = np.array([0.25, 0.5, 1.0, 2.0, 4.0])
sweep_rows = []

for fac in factors:
    on, off, Eon, Eoff = simulate(representative, jref=JREF * fac)
    amp3, t63, remaining = relaxation_metrics(off, Eoff)

    sweep_rows.append(
        [
            fac,
            amp3,
            t63,
            on.y[0, -1],
            on.y[1, -1],
            on.y[2, -1],
        ]
    )

sweep_df = pd.DataFrame(
    sweep_rows,
    columns=[
        "relative_pulse_current",
        "residual_relaxation_at_3s_mV",
        "t63_min",
        "I_at_pulse_end",
        "Istar_at_pulse_end",
        "C_at_pulse_end",
    ],
)

sweep_df.to_csv(
    OUT / "HEO_MICROKINETIC_CURRENT_SWEEP_LITERATURE_INFORMED_2026-09-25.csv",
    index=False,
)

# -------------------------------------------------------------------------
# 3) Local relaxation eigenmodes at the same conserved state-of-charge manifold
# -------------------------------------------------------------------------
# Extend the rest to practical equilibrium.
long_off = solve_ivp(
    lambda t, y: rhs(y, 0.0, representative),
    [0.0, 100000.0],
    on_ref.y[:, -1],
    method="LSODA",
    rtol=1e-9,
    atol=1e-11,
)

eq_state = long_off.y[:, -1]
J = numerical_jacobian(lambda y: rhs(y, 0.0, representative), eq_state)
eigvals = np.linalg.eigvals(J)

mode_rows = []
for lam in sorted(eigvals, key=lambda z: np.real(z)):
    if abs(np.real(lam)) < 1e-10:
        tau_s = np.inf
        interpretation = "conserved-state/SOC mode"
    else:
        tau_s = -1.0 / np.real(lam)
        interpretation = "finite relaxation mode"

    mode_rows.append(
        [
            np.real(lam),
            np.imag(lam),
            tau_s,
            np.inf if not np.isfinite(tau_s) else tau_s / 60.0,
            interpretation,
        ]
    )

pd.DataFrame(
    mode_rows,
    columns=[
        "eigenvalue_real_s-1",
        "eigenvalue_imag_s-1",
        "tau_s",
        "tau_min",
        "interpretation",
    ],
).to_csv(
    OUT / "HEO_MICROKINETIC_EIGENMODES_LITERATURE_INFORMED_2026-09-25.csv",
    index=False,
)

# -------------------------------------------------------------------------
# 4) Compact diagnostic figure
# -------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(7.2, 5.0))
ax.plot(sweep_df["relative_pulse_current"], sweep_df["t63_min"], marker="o")
ax.set_xscale("log", base=2)
ax.set_xlabel(r"Relative pulse current, $J/J_{ref}$")
ax.set_ylabel(r"$t_{63}$ (min)")
ax.tick_params(direction="out")
fig.tight_layout()
fig.savefig(
    OUT / "HEO_literature_informed_microkinetic_current_dependence_t63.png",
    dpi=220,
    bbox_inches="tight",
)

print(
    "Reference pulse: "
    f"relaxation@3s = {amp3_ref:.2f} mV, "
    f"t63 = {t63_ref:.2f} min"
)
print(sweep_df)
