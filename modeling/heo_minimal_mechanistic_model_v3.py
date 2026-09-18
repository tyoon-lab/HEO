import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# HEO minimal mechanism-discrimination model v3
# Semi-phenomenological; NOT a unique parameter-identification model.
# Purpose: discriminate D-only, structural-stabilization, structural-mobility,
# and ball-milling distribution hypotheses.

OUT = Path(".")
t = np.linspace(0, 3600, 1201)
TREF = 3.0
i3 = np.argmin(np.abs(t-TREF))
zgrid = np.linspace(0.05, 0.98, 95)
late = (zgrid >= 0.40) & (zgrid <= 0.90)

def gauss(z, mu, sigma):
    return np.exp(-0.5*((z-mu)/sigma)**2)

def decay(A_mV, tau_s):
    return (A_mV/1000.0)*np.exp(-t/tau_s)

def t63_from_curve(y):
    e3, eend = y[i3], y[-1]
    amp = e3-eend
    target = e3 - 0.632*amp
    ids = np.where(y[i3:] <= target)[0]
    if len(ids) == 0:
        return np.nan, amp*1000
    j = ids[0]
    tt, yy = t[i3:], y[i3:]
    if j == 0:
        tc = tt[0]
    else:
        t1,t2,y1,y2 = tt[j-1],tt[j],yy[j-1],yy[j]
        tc = t1+(target-y1)*(t2-t1)/(y2-y1)
    return (tc-TREF)/60.0, amp*1000

# eta(t,z) = eta_D + eta_BG + eta_PT
# eta_D: diffusion-like branch
# eta_BG: broad non-transition relaxation background
# eta_PT: localized phase-transition excess
params = {
    "HEO":       dict(A_D=35,tau_D=350,A_BG=110,tau_BG=550,A_PT=70.8,tau_PT=800,sigma=0.070,Qrel=1.00),
    "BM-HEO":    dict(A_D=30,tau_D=300,A_BG=125,tau_BG=770,A_PT=44.1,tau_PT=1200,sigma=0.115,Qrel=1.23),
    "Mg-HEO":    dict(A_D=25,tau_D=350,A_BG=82,tau_BG=800,A_PT=15.9,tau_PT=1500,sigma=0.070,Qrel=0.75),
    "BM-Mg-HEO": dict(A_D=25,tau_D=320,A_BG=110,tau_BG=900,A_PT=21.1,tau_PT=1600,sigma=0.115,Qrel=0.95)
}

def response_at_z(p, z):
    return (
        decay(p["A_D"],p["tau_D"]) +
        decay(p["A_BG"],p["tau_BG"]) +
        decay(p["A_PT"]*gauss(z,0.72,p["sigma"]),p["tau_PT"])
    )

def summarize(p):
    amps, times, ptamps = [], [], []
    for z in zgrid:
        y = response_at_z(p,z)
        tv,av = t63_from_curve(y)
        amps.append(av); times.append(tv)
        yp = decay(p["A_PT"]*gauss(z,0.72,p["sigma"]),p["tau_PT"])
        ptamps.append((yp[i3]-yp[-1])*1000)
    amps=np.array(amps); times=np.array(times); ptamps=np.array(ptamps)
    peak = np.max(ptamps[late])
    ids = np.where(late & (ptamps >= peak/2))[0]
    width = zgrid[ids[-1]]-zgrid[ids[0]] if len(ids)>1 else np.nan
    return {
        "median_amp_mV": np.median(amps[late]),
        "median_t63_min": np.median(times[late]),
        "peak_PT_mV": peak,
        "FWHM_z": width
    }

# D-only directional test:
# A_D ~ D^(-1/2), tau_D ~ D^(-1)
Dvals = np.geomspace(0.3,3.0,80)
Drows=[]
for D in Dvals:
    y = decay(35/np.sqrt(D),350/D)
    tv,av = t63_from_curve(y)
    Drows.append([D,av,tv])
pd.DataFrame(Drows,columns=["D_relative","Diffusion_amplitude_mV","Diffusion_t63_min"]).to_csv(
    OUT/"HEO_D_only_direction_test_v3.csv",index=False
)

# Four-sample summary
rows=[]
for name,p in params.items():
    s=summarize(p)
    rows.append([name,s["median_amp_mV"],s["median_t63_min"],s["peak_PT_mV"],s["FWHM_z"],p["Qrel"]])
pd.DataFrame(rows,columns=["Sample","median_DeltaErelax_mV","median_t63_min","peak_PT_mV","FWHM_z","Qrel"]).to_csv(
    OUT/"HEO_model_v3_summary.csv",index=False
)

# NOTE:
# Working values were chosen to reproduce the observed directions and approximate scale.
# They must not be interpreted as uniquely identified physical parameters.
# Translation to MATLAB should occur only after sensitivity/identifiability checks and
# after deciding whether the model remains a main-text or SI mechanistic discriminator.
