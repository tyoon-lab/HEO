# HEO — C2/C3 selectivity in common-QOCV window after whole-capacity and uniform-amplitude controls (2026-11-13)

**STATUS: internal exploratory analysis; not author-approved manuscript inference.** HEO manuscript, locked Abstract/Introduction, Word native comments and first-cycle (t_{63})-based R1–R4 assignments were **not changed**. This continues:
- [Hump-anchored C1–C3 study](HEO_2026-11-13_HUMP_ANCHORED_CYCLE_COMPARISON_INTERNAL.md)
- [Broad 0.5–1.3 V normalized-rest control](HEO_2026-11-13_BROAD_QOCV_REST_SHAPE_CONTROL.md)
- [Same-voltage 0.9 V C1–C3 raw-rest test](HEO_2026-11-13_COMMON_QOCV_REST_RELAXATION_CONTROL.md).

## Question
Does a **specific, material-modification-driven electrochemical change remain near the recurring 0.9–1.0 V after-formation feature**, over and above the trivial scaling of total C2/C3 lithiation charge? Moreover, does the voltage-rest amplitude display a localized modification effect when scaled by a **single uniform amplitude gain factor** over the 0.5–1.3 V range? This is a comparison of empirical observables, **not** proof of unique chemical reaction or phase identity.

## Inputs, units, methods
- Inputs **already extracted and audited from original four GITT XLSX raw files**, available in conversation container:
  - `HEO_GITT_C1_C3_joined_lith_delith_throughput.csv` (lithiation C2/C3, pulsewise QOCV and nominal 100mA/g × 600s full-pulse charge; 16.667 mAh/g per completed pulse).
  - `HEO_broad_QOCV_rest_metrics_all4.csv` (72 raw-rest derived responses, 4 electrodes × 2 later cycles × QOCV=0.5:0.1:1.3 V, 3–3500s voltage recovery; |ΔErest|, t63, F300).
- For each material/cycle, interpolate **Q(QOCV)** with shape-preserving cubic PCHIP after sorting by voltage (Q decreases monotonically with QOCV, checked). Compare total full-rest nominal lithiation Q and the fixed-voltage-window charge `Qwin(Vlo,Vhi)=Q(Vlo)-Q(Vhi)`. Normalize `fwin=Qwin/Qtotal`. Uniform whole-capacity-scaling null model: if only total charge scales, `fwin` should be unchanged under modification at fixed voltage. Residual percentage points = 100×(ftreatment−freference); predicted-window charge under uniform capacity scaling = reference Qwin×(treatment Qtotal/reference Qtotal). Test 0.85–0.95V (selected), 0.80–1.00V, 0.875–0.925V, 0.90–1.00V, neighboring windows and full 0.5–1.3V with ±0.05V moving windows.
- Independently test **absolute rest-voltage recovery amplitude** A(V)=|E(3500s)-E(3s)|. For each matched treatment/reference pair, fit a single nonnegative-free scalar `k = Σ_V A_treatment(V) A_reference(V) / Σ_V A_reference(V)^2` over 0.5:0.1:1.3V; residual `R(V)=A_treatment(V)-k*A_reference(V)`. This **uniform-AMPlITUDE-gain control is distinct from whole-CAPACITY scaling**; it does not assume absolute A is proportional to Q. Evaluate separately for C2/C3 and alternative fit ranges to assess stability. No microscopic kinetic model is asserted.
- Full pulse GITT capacity calculations exclude terminal partial cutoff pulse. C2 and C3 are **successive cycles of the same single cell**, not independent replicates. No frequentist error bars, reaction-specific capacity, or causal R2/R3 mapping can be claimed.
- Source/derived local script `/mnt/data/HEO_C2C3_0p9V_selectivity_control.py`. Generated local files (not committed as binary GitHub files) listed below.

## 1. Capacity normalized by total charge

C2/C3 averaged `Qwin` and fraction of full lithiation `Qtotal` for **QOCV=0.85–0.95 V**:

| Sample | Mean Qwin mAh/g | Qwin/Qtotal |
|---|---:|---:|
| HEO | 79.36 | 11.34% |
| BM-HEO | 97.39 | 11.57% |
| Mg-HEO | 46.27 | 10.10% |
| BM-Mg-HEO | 57.76 | 10.51% |

Matched modification contrasts in fractional charge, treatment minus reference:
- Ball milling in Mg-free pair **+0.24 percentage points**, extra window charge beyond proportional scaling **+1.97 mAh/g**.
- Ball milling in Mg-containing pair **+0.41 pp**, excess **+2.24 mAh/g**.
- Mg incorporation unmilled **−1.24 pp**, excess **−5.70 mAh/g**.
- Mg incorporation after ball milling **−1.06 pp**, excess **−5.88 mAh/g**.

**Interpretation:** for the **selected** voltage region, BM's larger absolute Qwin mostly follows higher *total* lithiation capacity, whereas Mg shows additional relative depletion of the window by approximately 1.0–1.2 pp. This relative effect amounts to only ~6 mAh/g at 0.85–0.95V, **below a single GITT full pulse of 16.7 mAh/g**, and cannot be equated with an independently quantified reaction capacity.

Sensitivity to window width/position:
- For **0.80–1.00 V**, extra window charge beyond proportional scaling: BM Mg-free **+0.6**, BM Mg **+2.8**, Mg unmilled **−10.3**, Mg BM **−9.9 mAh/g**.
- For **0.875–0.925 V**, BM +1.2/+1.4 and Mg −3.0/−3.0 mAh/g.
- For **0.90–1.00 V**, BM +1.2/+2.1 and Mg −5.7/−5.5 mAh/g.
- Mg relative depletion persists roughly 0.8–1.1V (depending upon matched condition); it is **not just one isolated 0.90V data point**. The ball-milling relative effect is comparatively small and changes sign across adjacent voltage bins.
- PCHIP vs straight linear QOCV interpolation changes raw Qwin in the selected 0.85–0.95V window by only ~0.06–0.17 mAh/g per sample-cycle; numerical interpolation choice does not explain the directional trend. But coarse 16.7mAh/g pulse spacing, protocol history, no independent cell replication, and limited GITT-window equilibration remain uncertainty sources.
- Despite strong same-cell cycle-to-cycle consistency, the local Mg deficit alone does **not prove** selective inhibition of one particular chemical conversion process. Modified QOCV(Q) topology and polarization history can cause it.

## 2. Rest-voltage recovery magnitude after *global amplitude* scaling

Fit `A_mod(V)≈k×A_ref(V)` across 0.5–1.3V to ask whether a local departure remains.

| Matched comparison | Global amplitude gain k (C2/C3 pooled average) | Residual at 0.90 V, mV | Residual at 1.00 V, mV |
|---|---:|---:|---:|
| BM-HEO minus HEO | 1.057 | −2.84 | +1.41 |
| BM-Mg-HEO minus Mg-HEO | 1.105 | +0.05 | +6.77 |
| Mg-HEO minus HEO | 1.028 | **−13.04** | **−11.31** |
| BM-Mg-HEO minus BM-HEO | 1.077 | **−11.60** | **−7.53** |

**Crucial cycle-level check:** At 0.90 V, independently fitted C2 and C3 amplitude-shape residuals for Mg-HEO vs HEO are **−12.05 and −13.93 mV**, respectively (−8.6% and −9.2% versus the scaled reference local amplitude); for BM-Mg vs BM they are **−11.57 and −11.64 mV** (−7.5% and −7.2%). This local Mg-associated depression therefore repeats despite C2/C3 having different absolute A values, and arises with or without ball milling. BM comparisons have no comparable consistent local 0.90V deficit.

**Amplitude-control sensitivity:** Excluding 0.9 and 1.0V from the gain fit makes the Mg 0.9V deficit even more negative; fitting only 0.7–1.2V still yields ~−9mV Mg deficits in each C2/C3. Hence the sign is not a direct artifact of using the target band to derive the global gain. This is **support for a localized effect on the *shape of amplitude-vs-voltage*, not standalone proof of a particular reaction.**

The earlier broad-voltage raw rest test found **the four materials' normalized relaxation shapes and t63 values converge around ~0.9–1.0V** while the absolute recovery amplitudes differ; this can coexist with a material-dependent distribution of stored charge and voltage recovery amplitudes. It would be premature to call it proof of changed kinetics of a unique transition-metal reduction process, since QOCV and finite-window polarization can influence both observables.

## 3. Relation to the first-cycle R1–R4 claim
The initial C1 (t_{63})-defined regional electrochemical charge differences remain:
- BM largest positive R2 effect ~+166.7 mAh/g (Mg-free), +150 mAh/g (Mg-containing);
- Mg largest negative R3 effect ~−200 mAh/g (unmilled), −183.3 mAh/g (after BM).

The **later** Mg-specific ~0.9V *local normalized charge loss* and *local voltage-rest amplitude suppression* are directionally **compatible** with the R3 loss being reflected in subsequent electrochemistry, while ball milling's later effects are largely total-capacity scaling in that **particular** voltage window. But **C1 R3 and C2/C3 QOCV≈0.9V are not established as the same reaction state or a causal mapping**. First-cycle R3 hump is at markedly lower QOCV (~0.39–0.54V for clear C1 peaks); C2/C3 initial state and Li stoichiometry differ. Four intervention contrasts from four conditions do not establish independent statistical replication.

## 4. Decision and next discriminator
- Present `Qwin/Qtotal` and the global-amplitude-gain-controlled `A(V)` shape as **exploratory two-metric evidence** that Mg changes later-cycle voltage-dependent response beyond simple total capacity scaling. A 10–20% *relative* change in a local normalized descriptor is **not a direct molecular-step share**.
- Since the Mg-related local charge fraction dip and A(V) dip occur near the stable ~0.9V QOCV-derivative peak, the joint pattern is promising. However full shape convergence may also result from generic dominant time scales rather than common phase identity.
- Next scientific control should test whether the observed voltage-region effects survive **GITT rest-time truncation** (for example redefining Erest endpoint at 600, 1800, 3500 s) and alternative short-time reference (3/10s), because ΔErest amplitude may strongly depend on observation window. If stable, the trend is more defensible. Also assess concentration-versus-polarization possibility using the local QOCV slope; do not infer active material phase without spectroscopy.
- Manuscript/Word and R1–R4 **unchanged**.

## Artifacts from same workspace (not committed binaries)
- `HEO_normalized_dQdV_vs_QOCV_C2C3_2x2.png`, `HEO_charge_selectivity_residual_QOCV_2x2.png`, `HEO_relaxation_amplitude_shape_residuals_2x2.png`
- `HEO_later_cycles_normalized_charge_vs_QOCV.csv`, `HEO_normalized_charge_modification_contrasts.csv`, `HEO_local_feature_selectivity_window_sensitivity.csv`, `HEO_voltage_relaxation_amplitude_residuals.csv`, `HEO_amplitude_residual_cyclewise_sensitivity.csv`
- `HEO_C2C3_0p9V_selectivity_control.py`
