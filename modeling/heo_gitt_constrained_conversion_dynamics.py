"""
Reduced GITT-constrained distributed-threshold conversion-response model.

This script expects a state-resolved CSV with columns:
sample, z, excess_mV, t63_min

The experimental excess must already be calculated from the chosen
background definition. X is an effective conversion-response coordinate,
NOT a chemical phase fraction.
"""

import numpy as np
import pandas as pd

Z_MIN = 0.40
Z_MAX = 0.90

def build_inputs(df, sample, n=1200, z_min=Z_MIN, z_max=Z_MAX):
    d = (
        df[(df["sample"] == sample) & (df["z"] >= z_min) & (df["z"] <= z_max)]
        .sort_values("z")
        .copy()
    )
    if len(d) < 5:
        raise ValueError(f"Insufficient points for {sample}")

    zc = np.linspace(z_min, z_max, n)
    excess = np.interp(
        zc,
        d["z"].to_numpy(),
        np.clip(d["excess_mV"].to_numpy(), 0.0, None),
        left=0.0,
        right=0.0,
    )
    area = np.trapezoid(excess, zc)
    if area <= 0:
        raise ValueError(f"Non-positive excess area for {sample}")

    p = excess / area
    tau_s = np.interp(
        zc,
        d["z"].to_numpy(),
        d["t63_min"].to_numpy() * 60.0,
    )

    F = np.zeros_like(zc)
    F[1:] = np.cumsum((p[:-1] + p[1:]) * 0.5 * np.diff(zc))

    return zc, p, tau_s, F


def simulate(df, sample, c_rate, n=1200, z_min=Z_MIN, z_max=Z_MAX):
    zc, p, tau_s, F = build_inputs(
        df, sample, n=n, z_min=z_min, z_max=z_max
    )

    z = zc.copy()
    X = np.zeros_like(z)

    # z advances from 0 to 1 in 3600/C seconds.
    # Each effective domain begins responding once z exceeds its threshold zc.
    for i, zz in enumerate(z):
        dt_s = (zz - zc) * 3600.0 / c_rate
        active = dt_s >= 0
        xi = np.zeros_like(zc)
        xi[active] = 1.0 - np.exp(-dt_s[active] / tau_s[active])
        X[i] = np.trapezoid(p * xi, zc)

    lag = F - X
    integrated_dynamic_lag = (
        np.trapezoid(lag, z) / (z_max - z_min)
    )

    return {
        "z": z,
        "F": F,
        "X": X,
        "lag": lag,
        "endpoint_tracking": X[-1],
        "integrated_dynamic_lag": integrated_dynamic_lag,
    }


if __name__ == "__main__":
    csv_path = "HEO_GITT_state_resolved_rebuilt.csv"
    df = pd.read_csv(csv_path)

    samples = ["HEO", "BM-HEO", "Mg-HEO", "BM-Mg-HEO"]
    for sample in samples:
        out = simulate(df, sample, c_rate=1.0)
        print(
            sample,
            f"endpoint_tracking={out['endpoint_tracking']:.3f}",
            f"integrated_dynamic_lag={out['integrated_dynamic_lag']:.3f}",
        )
