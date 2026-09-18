# heo_phase_transition_model_v2.py
# Python mechanistic-discrimination model for HEO GITT
# Date: 2026-09-18
#
# This script implements the final Python-v2 model architecture:
# - D-only negative control
# - state-distributed phase-transition polarization
# - distributed structural relaxation
# - actual 600 s pulse + 3600 s rest
#
# NOTE: parameters are phenomenological and non-unique.

import numpy as np
import pandas as pd
from scipy.stats import norm
from scipy.optimize import brentq

PULSE_S = 600.0
REST_END_S = 3600.0

def tau_modes(tau_median, sigma_ln, n=501):
    p = (np.arange(n) + 0.5) / n
    return tau_median * np.exp(sigma_ln * norm.ppf(p))

def pulse_rest_kernel(t_rest, tau_median, sigma_ln):
    tau = tau_modes(tau_median, sigma_ln)
    build = 1.0 - np.exp(-PULSE_S / tau)
    t_rest = np.asarray(t_rest)
    return np.mean(build * np.exp(-t_rest[..., None] / tau), axis=-1)

def finite_window_t63(tau_median, sigma_ln, t0=3.0, tend=3600.0):
    k0 = float(pulse_rest_kernel(np.array([t0]), tau_median, sigma_ln)[0])
    ke = float(pulse_rest_kernel(np.array([tend]), tau_median, sigma_ln)[0])

    def f(t):
        kt = float(pulse_rest_kernel(np.array([t]), tau_median, sigma_ln)[0])
        return (k0 - kt) / (k0 - ke) - 0.632

    return brentq(f, t0, tend)

def asym_gauss(z, A, mu, sigma_left, sigma_right):
    z = np.asarray(z)
    sigma = np.where(z < mu, sigma_left, sigma_right)
    return A * np.exp(-0.5 * ((z - mu) / sigma)**2)

def d_only_prediction(Drel, amp_ref, t63_ref):
    # Illustrative semi-infinite / finite-length scaling pair.
    amplitude = amp_ref / np.sqrt(Drel)
    t63 = t63_ref / Drel
    return amplitude, t63

# Frozen v2 hypothesis-level heterogeneity widths.
SIGMA_LN_TAU = {
    "HEO": 0.25,
    "BM-HEO": 0.65,
    "Mg-HEO": 0.40,
    "BM-Mg-HEO": 0.75,
}

# Raw-derived target values used on 2026-09-18.
TARGET_T63_MIN = {
    "HEO": 8.6807,
    "BM-HEO": 11.5714,
    "Mg-HEO": 11.0061,
    "BM-Mg-HEO": 12.9945,
}

TARGET_EXCESS_PEAK_MV = {
    "HEO": 70.7686,
    "BM-HEO": 44.0711,
    "Mg-HEO": 15.9050,
    "BM-Mg-HEO": 21.0968,
}

def solve_v2_parameters():
    rows = []
    for sample in SIGMA_LN_TAU:
        sig = SIGMA_LN_TAU[sample]
        target_t63_s = TARGET_T63_MIN[sample] * 60.0

        tau_med = brentq(
            lambda tm: finite_window_t63(tm, sig) - target_t63_s,
            10.0, 10000.0
        )

        k3 = float(pulse_rest_kernel(np.array([3.0]), tau_med, sig)[0])
        k3600 = float(pulse_rest_kernel(np.array([3600.0]), tau_med, sig)[0])
        window = k3 - k3600
        scale = TARGET_EXCESS_PEAK_MV[sample] / window

        rows.append({
            "Sample": sample,
            "Median structural tau (s)": tau_med,
            "ln(tau) width": sig,
            "Transition scale (mV)": scale,
            "Modeled t63 (min)": finite_window_t63(tau_med, sig) / 60.0,
        })
    return pd.DataFrame(rows)

if __name__ == "__main__":
    print(solve_v2_parameters().to_string(index=False))
