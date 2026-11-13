# HEO — Broad-QOCV C2/C3 GITT relaxation control (0.5–1.3 V, 2026-11-13)

**STATUS: Internal exploratory analysis only. PI-locked C1 t63 regions R1–R4, original manuscript, Abstract/Introduction and Figure numbering NOT CHANGED.**

## Test and motivation
Previous analysis found near-invariant normalized raw 3–3500s GITT rest relaxation shape among four HEO electrodes at a fixed **0.90 V** end-of-rest QOCV, close to a common C2/C3 local QOCV-based |dQ/dV| peak and prior to a composition-dependent |ΔErest| hump. PI asked whether the 0.90 V similarity reflects a unique reaction landmark or is merely a general property of the GITT rest-voltage response. **This test scans the complete 0.5–1.3 V range with the same method.**

## Direct source and computation
- Read the **four original unmodified XLSX** reports (HEO, BM-HEO, Mg-HEO, BM-Mg-HEO), using streaming XLSX XML and current-sign based cycle segmentation with direct sign-reversal handling. Matched against the independent pulsewise audit `HEO_GITT_C1_C3_joined_lith_delith_throughput.csv`.
- For **C2 and C3 lithiation**, select the two fully rested pulses bracketing each requested rest-end QOCV `V=0.5, 0.6, …, 1.3 V`. Linearly interpolate **entire raw E(t) trajectories at fixed QOCV**, not just fitted t63. Common rest-time interval = **3–3500 s**, with log-spaced 220-point analysis grid.
- `F(t)=[E(t)-E(3s)]/[E(3500s)-E(3s)]`; `t63` from first crossing of `1−e^(−1)` on interpolated F(t); `F300=F(300s)`; relaxation amplitude = `|E(3500s)-E(3s)|`.
- Measure cross-material shape variation as mean of all six pairwise RMSEs between **each electrode's average C2/C3 F(t)** on the **interior 10–1200s** log-time range (not forced normalized endpoints). Compare with mean within-material **C2-vs-C3 RMSE** on the same range.
- 9 voltages × 2 cycles × 4 materials = **72 voltage-matched relaxation traces**, each interpolated between two measured GITT pulse responses.
- All 4 datasets covered voltage span, checks enforce both bracketing pulses, full ≥3500 s rest, normalized endpoints, and original pulse-index pairing. Derived scripts **`/mnt/data/HEO_C2C3_broad_voltage_relaxation_control.py`** and **`/mnt/data/HEO_broad_QOCV_aggregate.py`**, outputs `HEO_broad_QOCV_rawshape_{sample}.npz`, `HEO_broad_QOCV_rest_metrics_all4.csv`, `HEO_broad_QOCV_shape_similarity_summary.csv`, `HEO_broad_QOCV_relaxation_control_2x2.png/.svg`, `HEO_broad_QOCV_cross_sample_shapes.png`. These local binaries are **not committed to GitHub**.

## Main numerical observations

| Matched QOCV (V) | Between-material mean full-shape RMSE | Same-sample C2-vs-C3 RMSE | Between-material t63 SD (s) | Between-material t63 min–max (s) | Mean F(300 s) |
|---:|---:|---:|---:|---:|---:|
| 0.5 | 0.0182 | 0.0035 | 42.0 | 597–697 | 0.4749 |
| 0.6 | 0.0196 | 0.0028 | 45.3 | 569–679 | 0.4816 |
| 0.7 | 0.0162 | 0.0034 | 36.1 | 572–659 | 0.4840 |
| 0.8 | 0.0116 | 0.0032 | 23.9 | 566–625 | 0.4920 |
| 0.9 | **0.0079** | 0.0037 | **13.3** | 544–577 | 0.5048 |
| 1.0 | **0.0075** | 0.0034 | **11.4** | 529–561 | 0.5096 |
| 1.1 | 0.0130 | 0.0043 | 23.5 | 503–559 | 0.5169 |
| 1.2 | 0.0209 | 0.0052 | 38.5 | 448–551 | 0.5295 |
| 1.3 | 0.0264 | 0.0068 | 49.9 | 403–535 | 0.5464 |

**Core result:** Across the four electrodes, **normalized time-domain relaxation is most similar in a BROAD ~0.9–1.0 V interval**, rather than uniquely at 0.90 V. Between-material mean normalized curve RMSE 0.0075–0.0079 (7.5–7.9 percentage points **per 1000**, i.e. 0.75–0.79 percentage points of unit normalized recovery) vs ~0.018–0.020 around 0.5–0.6 V and ~0.026 at 1.3 V. Between-material t63 SD similarly smallest 11–13 s around 0.9–1.0 V vs 42–50 s at extremes.

**Control result:** Within each electrode, **C2 and C3 normalized rest relaxation stays highly similar over the entire 0.5–1.3 V scan**, not only 0.9 V. Thus C2/C3 resemblance **alone** cannot serve as a diagnostic of a unique hump-related reaction. C2/C3 is same-cell sequential history, not independent replication.

**Amplitude result:** `|ΔErest|` does **not** show the same universal shape collapse at 0.9–1.0 V as normalized traces: between-material amplitude SD remains ~5.7–7.8 mV around 0.9–1.0 V and has its smallest cross-material SD ~3.2 mV at 0.8 V. This reinforces that normalized kinetic-shape convergence and absolute voltage response are different phenomena.

**Cross-electrode shape concentration:** Average normalized cross-material full-curve RMSE at 0.9–1.0 V is roughly **2–3.5× smaller** than at outlying regions. It is not an artifact of trivial normalized endpoints because similarity metric only uses interior 10–1200 s, but **common finite-window normalization and shared generic kinetics still remain alternative explanations**.

## Revised interpretation and decision gate
1. Previous repeated **0.90 V QOCV-based dQ/dV local peak** remains a robust **electrochemical charge-response landmark**, within `~0.88–0.913 V` across four electrodes and C2/C3. A broader **0.9–1.0 V convergence of normalized GITT relaxation shape** is a second partly-independent descriptor from the same experimental current/voltage source, consistent with convergence of a dominant reaction or transport-coupled response **after the initial reconstruction**.
2. More careful wording: *A broad potential interval around 0.9–1.0 V exhibits similar normalized relaxation dynamics among the four modified oxides following first-cycle lithiation.* Do **not** claim a unique phase/process, reaction boundary, or invariant diffusion coefficient. The near-0.9V differential-charge maximum and amplitude hump remain distinct features offset by 1–4 GITT pulses.
3. C1 first lithiation R1–R4 remain empirical region assignments based on t63. Current later-cycle findings **do not refute** that segmentation but complicate the unique interpretation of the region as a single chemical reaction.
4. As a next discriminator, calculate **full normalized-rest shape differences across each C2/C3 voltage pair relative to the 0.9–1.0 V band**, inspect local changes in *un-normalized* ΔErest and |dQ/dV|, then evaluate whether this interval provides a **material modification-selective effect** larger than whole-capacity scaling and one-pulse anchor uncertainty. Potentially compare C1 dynamics at matched **hump-relative charge** as initial-history diagnostic.
5. Manuscript/supplement and native Word comments **untouched**. Keep finding **internally** until PI review.

