import numpy as np
from scipy.integrate import solve_ivp

# Reproducible validation for the capacity-relaxation logic used in HEO Figure 7.
# This script is an existence-proof calculation, not a fit to HEO or BM-HEO.

RTF = 8.314462618 * 298.15 / 96485.33212
JAPP = 2e-4
ECUT = 0.02
INIT = np.array([1e-4, 1e-4, 1e-4], dtype=float)

BASE = dict(
    k1=2.0e-2,
    k2f=8.483428982440717e-4,
    k2r=4.2417144912203585e-4,
    k3=1.0e-2,
    u3=-3.0,
)

def algebraic_u(states, japp, branches):
    A = 0.0
    B = 0.0
    for i, (weight, pars) in enumerate(branches):
        I, Istar, C = states[3*i:3*i+3]
        O = max(1.0 - I - Istar - C, 1e-14)
        I = max(I, 1e-14)
        Istar = max(Istar, 1e-14)
        C = max(C, 1e-14)
        A += weight * (
            pars["k1"] * O
            + pars["k3"] * Istar * np.exp(-pars["u3"] / 2.0)
        )
        B += weight * (
            pars["k1"] * I
            + pars["k3"] * C * np.exp(pars["u3"] / 2.0)
        )
    y = (japp + np.sqrt(japp*japp + 4.0*A*B)) / (2.0*A)
    return 2.0 * np.log(y)

def rhs(t, states, japp, branches):
    u = algebraic_u(states, japp, branches)
    out = []
    for i, (weight, pars) in enumerate(branches):
        I, Istar, C = states[3*i:3*i+3]
        O = max(1.0 - I - Istar - C, 1e-14)
        I = max(I, 1e-14)
        Istar = max(Istar, 1e-14)
        C = max(C, 1e-14)

        r1 = pars["k1"] * (
            O * np.exp(u/2.0) - I * np.exp(-u/2.0)
        )
        r2 = pars["k2f"] * I - pars["k2r"] * Istar
        r3 = pars["k3"] * (
            Istar * np.exp((u-pars["u3"])/2.0)
            - C * np.exp(-(u-pars["u3"])/2.0)
        )
        out.extend([r1-r2, r2-r3, r3])
    return np.asarray(out)

def potential(states, japp, branches):
    return -RTF * algebraic_u(states, japp, branches)

def initial_state(branches):
    return np.tile(INIT, len(branches))

def capacity_to_cutoff(branches):
    y0 = initial_state(branches)

    def event(t, y):
        return potential(y, JAPP, branches) - ECUT

    event.terminal = True
    event.direction = -1

    sol = solve_ivp(
        lambda t, y: rhs(t, y, JAPP, branches),
        [0.0, 10000.0],
        y0,
        events=event,
        method="LSODA",
        rtol=2e-8,
        atol=1e-10,
        max_step=5.0,
    )
    return JAPP * sol.t_events[0][0]

def relaxation_metrics(y0, branches):
    t_eval = np.r_[np.linspace(0.0, 60.0, 61), np.linspace(70.0, 3600.0, 354)]
    sol = solve_ivp(
        lambda t, y: rhs(t, y, 0.0, branches),
        [0.0, 3600.0],
        y0,
        t_eval=t_eval,
        method="LSODA",
        rtol=2e-8,
        atol=1e-10,
    )
    E = np.array([potential(sol.y[:, i], 0.0, branches) for i in range(sol.y.shape[1])])
    remaining = (E[-1] - E) * 1000.0
    amp3 = np.interp(3.0, sol.t, remaining)
    target = 0.368 * amp3
    idx = np.where((sol.t >= 3.0) & (remaining <= target))[0]
    t63 = (sol.t[idx[0]] - 3.0) / 60.0
    return amp3, t63, sol.y[:, -1]

def third_pulse_relaxation(branches):
    y = initial_state(branches)
    for _ in range(3):
        on = solve_ivp(
            lambda t, z: rhs(t, z, JAPP, branches),
            [0.0, 600.0],
            y,
            method="LSODA",
            rtol=2e-8,
            atol=1e-10,
            max_step=2.0,
        )
        amp3, t63, y = relaxation_metrics(on.y[:, -1], branches)
    return amp3, t63

print("Homogeneous global-rate control")
for scale in [0.5, 0.75, 1.0, 1.5, 2.0]:
    p = BASE.copy()
    for key in ["k1", "k2f", "k2r", "k3"]:
        p[key] *= scale
    branches = [(0.65, p)]
    Q = capacity_to_cutoff(branches)
    amp3, t63 = third_pulse_relaxation(branches)
    print(scale, Q, amp3, t63)

slow = BASE.copy()
slow["k2f"] *= 0.1
slow["k2r"] *= 0.1

reference = [(0.65, BASE)]
heterogeneous = [(0.65, BASE), (0.15, slow)]

print("\nHeterogeneous-accessibility existence proof")
for name, branches in [
    ("reference_fast_only", reference),
    ("fast_plus_added_slow", heterogeneous),
]:
    Q = capacity_to_cutoff(branches)
    amp3, t63 = third_pulse_relaxation(branches)
    print(name, Q, amp3, t63)
