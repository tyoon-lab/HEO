import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from pathlib import Path

# Minimal electrochemical-growth conversion microkinetic model.
# Purpose: mechanistic-consistency test, NOT unique RDS fitting.
#
# R1: A + Li+ + e- <-> B
# R2: B -> N
# R3: B + Li+ + e- <-> P
#
# At open circuit: r1 + r3 = 0, but r1 = -r3 != 0 is allowed.

OUT = Path(".")
RTF = 8.314462618 * 298.15 / 96485.33212

def algebraic_u(state, japp, pars):
    b, p, n = state
    a = max(1.0 - b - p, 1e-14)
    b = max(b, 1e-14)
    p = max(p, 1e-14)
    n = max(n, 0.0)

    k1 = pars["k1"]
    kg = pars["kg"]
    K1 = pars.get("K1", 1.0)
    K3 = pars.get("K3", 1.0)
    u3 = pars.get("u3", 0.0)

    A = k1*a + kg*n*b*max(1.0-p,1e-14)*np.exp(-u3/2.0)
    B = k1*b/K1 + kg*n*(p/K3)*np.exp(u3/2.0)

    y = (japp + np.sqrt(japp*japp + 4.0*A*B)) / (2.0*A)
    return 2.0*np.log(y)

def rates(state, japp, pars):
    b, p, n = state
    a = max(1.0 - b - p, 1e-14)
    bpos = max(b, 1e-14)
    ppos = max(p, 1e-14)
    npos = max(n, 0.0)

    k1 = pars["k1"]
    kg = pars["kg"]
    kn = pars["kn"]
    m = pars.get("m", 2.0)
    kd = pars.get("kd", 0.0)
    K1 = pars.get("K1", 1.0)
    K3 = pars.get("K3", 1.0)
    u3 = pars.get("u3", 0.0)

    u = algebraic_u(state, japp, pars)

    r1 = k1*(a*np.exp(u/2.0) - (bpos/K1)*np.exp(-u/2.0))
    r3 = kg*npos*(
        bpos*max(1.0-ppos,1e-14)*np.exp((u-u3)/2.0)
        - (ppos/K3)*np.exp(-(u-u3)/2.0)
    )
    rn = kn*(bpos**m)*(1.0-npos) - kd*npos
    return r1, r3, rn, u

def simulate(pars, jref=2e-4, pulse_s=600.0, rest_s=3600.0,
             initial=(0.01,0.05,0.01)):
    initial = np.asarray(initial, dtype=float)

    def rhs(t, y, jnow):
        r1, r3, rn, _ = rates(y, jnow, pars)
        return [r1-r3, r3, rn]

    on = solve_ivp(
        lambda t,y: rhs(t,y,jref), [0,pulse_s], initial,
        rtol=1e-9, atol=1e-11, max_step=0.5
    )
    off = solve_ivp(
        lambda t,y: rhs(t,y,0.0), [0,rest_s], on.y[:,-1],
        rtol=1e-9, atol=1e-11, max_step=0.5
    )

    def potential(sol, jnow):
        u = np.array([
            algebraic_u(sol.y[:,i], jnow, pars)
            for i in range(sol.y.shape[1])
        ])
        return -RTF*u

    return on, off, potential(on,jref), potential(off,0.0)

def relaxation_metrics(off, Eoff):
    rem = (Eoff[-1] - Eoff)*1000.0
    amp3 = float(np.interp(3.0, off.t, rem))
    target = 0.368*amp3
    idx = np.where((off.t >= 3.0) & (rem <= target))[0]
    t63 = np.nan if len(idx)==0 else (off.t[idx[0]]-3.0)/60.0
    return amp3, t63, rem

nucleation_dom = dict(
    k1=0.02, kg=0.02, kn=3e-4, m=2.0,
    u3=-4.0, K1=1.0, K3=1.0
)

growth_dom = dict(
    k1=0.02, kg=2.32e-4, kn=0.5, m=1.0,
    u3=-4.0, K1=1.0, K3=1.0
)

scenarios = {
    "Nucleation-dominant": nucleation_dom,
    "Electrochemical-growth-dominant": growth_dom,
}

JREF = 2e-4
factors = np.array([0.25,0.5,1.0,2.0,4.0])

rows = []
for name, pars in scenarios.items():
    for fac in factors:
        on, off, Eon, Eoff = simulate(pars, jref=JREF*fac)
        amp3, t63, rem = relaxation_metrics(off, Eoff)
        rows.append([
            name, fac, amp3, t63,
            on.y[0,-1], on.y[1,-1], on.y[2,-1]
        ])

df = pd.DataFrame(rows, columns=[
    "Scenario","Relative pulse current",
    "Residual relaxation at 3 s (mV)","t63 (min)",
    "B at pulse end","P at pulse end","N at pulse end"
])

df.to_csv(OUT/"HEO_electrochemical_growth_current_sweep.csv", index=False)

# Compact current-off diagnostic for the main-text Figure 7 concept.
# This uses one illustrative parameter regime only; it is not a fit to a specific sample.
# The residual voltage is referenced to the end of the experimental-style 3600 s rest.
rep_pars = nucleation_dom
on_rep, off_rep, Eon_rep, Eoff_rep = simulate(rep_pars, jref=JREF)
sample_times = np.array([0.0, 3.0, 10.0, 30.0, 60.0, 180.0, 600.0, 1800.0, 3600.0])
off_rows = []
for t in sample_times:
    state = np.array([
        np.interp(t, off_rep.t, off_rep.y[j,:])
        for j in range(off_rep.y.shape[0])
    ])
    r1, r3, rn, u = rates(state, 0.0, rep_pars)
    E = -RTF*u
    off_rows.append([
        t,
        (Eoff_rep[-1] - E)*1000.0,
        r1,
        r3,
        r1+r3,
        rn,
    ])

pd.DataFrame(off_rows, columns=[
    "rest_time_s",
    "residual_relaxation_to_3600s_mV",
    "r1",
    "r3",
    "r1_plus_r3",
    "rn",
]).to_csv(
    OUT/"HEO_MICROKINETIC_CURRENT_OFF_BALANCE_2026-09-23.csv",
    index=False
)

fig, ax = plt.subplots(figsize=(7.2,5.0))
for name in scenarios:
    d = df[df["Scenario"]==name]
    ax.plot(d["Relative pulse current"], d["t63 (min)"],
            marker="o", label=name)
ax.set_xscale("log", base=2)
ax.set_xlabel(r"Relative pulse current, $J/J_{ref}$")
ax.set_ylabel(r"$t_{63}$ (min)")
ax.legend(frameon=False)
ax.tick_params(direction="out")
fig.tight_layout()
fig.savefig(OUT/"HEO_electrochemical_growth_current_dependence_t63.png",
            dpi=220, bbox_inches="tight")
plt.show()
