# HEO manuscript — experiment-free closure: claim/reference/figure/submission audit
**Date:** 2026-11-23  
**Decision:** No new experiments and no new FEM/physical simulation are required for the paper's current **electrochemical response-level story**. Strengthen interpretation using *composition-aware* previously published operando XAS, in situ XRD, TEM and GITT precedents. The 2026-11-11 PI-approved Abstract and four-paragraph Introduction are **unchanged**. Existing Word comments, figures, SI and Word binaries were **not edited**. This record is an actionable audit, not proof of full manuscript submission readiness.

## 1. Scientific thesis and what is measured
Four samples form a 2×2 design: HEO, BM-HEO, Mg-HEO, BM-Mg-HEO. First-lithiation GITT t63 profile defines **operational** R1–R4. The observed nominal charge changes and moving boundaries are quantitative comparisons of electrochemical intervals, **not** stoichiometric charges of four identified independent reactions.

**Central paper statement:** Ball milling and Mg incorporation affect different parts of the first-lithiation GITT charge trajectory. Both contract operational R3, but BM predominantly delays its start (L3), whereas Mg advances its end (L4). The modifications produce contrasting and persistent C2/C3 reversible capacity and voltage-relaxation responses. Morphological refinement, accessible reversible reaction states, active-cation inventory, and stabilization of reconstructed oxides are **literature-supported hypotheses**, not direct assignments to this study's R1–R4 bins.

**Novelty vs prior art:** The novelty claim is **paired, quantitatively region-resolved treatment effects + the distinct subsequent response fingerprints**, rather than the first use of GITT for conversion materials, phase-specific charge quantification, a newly discovered conversion mechanism, a unique BM-induced slower elementary reaction, or a battery-life predictor. In particular, Ng et al. 2021 already applied GITT along NiO conversion/SEI reactions.

## 2. Fixed raw-source accounting
- Protocol: nominal 100 mA g−1; 600 s current pulses, 3600 s rests; nominal 16.6667 mAh g−1 per complete pulse. Use end-of-rest **QOCV** (finite 3600 s) and 3–3600 s signed-recovery first-crossing **t63**, not equilibrium OCV or a unique D.
- Four original September-17 XLSX workbooks recovered from email/Drive for prior analyses. ~1,020 complete rested pulses over 24 halfcycles; each condition **one independent cell** with C1/C2/C3 sequential cycling. Negative current lithiation, positive delithiation. No independent cell replicates, statistical CI or reproducibility proof.
- C1 boundaries L1/L3/L4 (pulse indices): HEO 6/25/55; BM 9/38/60; Mg 7/24/42; BM-Mg 9/35/46.
- C1 R1/R2/R3/R4 nominal complete-pulse capacities (mAh g−1): HEO 100/316.7/500/166.7; BM 150/483.3/366.7/266.7; Mg 116.7/283.3/300/100; BM-Mg 150/433.3/183.3/166.7.
- BM ΔR2 +166.7/+150.0 and ΔR3 −133.3/−116.7 (without/with Mg). Mg ΔR3 −200.0/−183.3 (without/with BM). BM L3 delayed 13/11 pulses, Mg L4 earlier 13/14. These region boundaries change smoothly, so their moving locations contribute to regional ΔQ.
- Deterministic ±1-pulse 729 geometry combinations per pair: signs BM R2+ / R3− and Mg R3− persist in 729/729. Not experimental repeats. Unmilled Mg R3 is strict largest loss 729/729; milled Mg strict largest in 702/729 with 18 ties; do not assert universally unique rank.
- C1 nominal whole-halfcycle including terminal partial vs C2/C3 (mAh g−1):
  - HEO lith 1094.22/715.00/710.47, delith 762.28/746.28/742.92;
  - BM lith 1278.50/860.89/844.39, delith 858.53/840.81/827.58;
  - Mg lith 814.25/476.08/462.75, delith 515.67/495.17/478.50;
  - BM-Mg lith 948.17/577.58/549.58, delith 583.17/563.42/543.50.
  Whole-halfcycle GITT charge must NOT be substituted for separate 0.1C GCD first-cycle capacities (901.25/609.12 HEO, 1056.10/782.08 BM, 731.15/458.91 Mg, 944.07/580.83 BM-Mg).
- C1 pristine R3 ΔErest rise between pulses 26 and 50: 145.1→189.3 mV (+44.2mV); 3–60s −9.8mV, 1–10min +16.5mV, 10–60min +37.5mV. This is a change in voltage relaxation **amplitude by time window**, not a measured quantity of slow-reaction charge.

## 3. C2/C3 model results: claim ceiling
Two distinct analyses MUST remain separate:
1. **Potential-resolved charge distribution:** C2-calibrated matched-reference transformation transferred to C3 delithiation; RMSE capacity+voltage-shift-only → 2-potential-region phenomenological reweighting: BM/HEO 0.0144→0.0087; BM-Mg/Mg 0.0097→0.0042; Mg/no-BM 0.0063→0.0064. BM model improvement is robust across 12 chosen center/width variants. Parameter β does **not** represent a phase charge fraction. The C3 *reference* is supplied, so it is held-out **contrast** transfer, not wholly independent cycle performance prediction.
2. **Raw rest waveforms 10–3500s (20 Nov):** C2-derived one-parameter time stretch and one-parameter empirical nonlinear voltage curvature give nearly equivalent conditional C3 normalized-shape residuals, BM/HEO ~0.0083 vs ~0.0081, BM-Mg/Mg ~0.0043 vs ~0.0041 (compare unmodified reference 0.0213 / 0.0139). Their near-equality prevents interpreting BM's longer effective t63 as a uniquely identified slow physical component. This test uses **measured C3 treated-pulse QOCV and amplitude for conditioning**. Early F(300s) BM C3 delithiation is reduced by ~3.05 / 2.03 percentage points (without/with Mg) relative to potential-matched reference, under the 10–3500s convention. These differences are not identical to earlier 3–3600s definitions; always specify the window.
3. **Stricter voltage prediction:** using C3 reference plus only C2 transforms, **without treated C3 waveform input**, actual-voltage RMSE ~40.0 / 17.0 mV for baseline. Adding nonlinear curvature gives 42.5 /17.6mV, and time stretch 42.4/17.6mV: no predictive improvement. Endpoint registration drives most of the error. Never label the conditional normalization model as improved absolute-voltage prediction or future life prediction.
4. C2/C3 integrated capacities nearly satisfy Q_BM-Mg ≈ Q_BM×Q_Mg/Q_HEO, but this is algebra on contemporaneous cells, not evidence of chemically independent effects. Effective delithiation t63 BM shifts ~+81s without Mg vs ~+50s with Mg can coexist with near-factorized total capacity. Call this *modification-dependent voltage-time response*, not proven kinetic-element synergy.

**Main manuscript:** empirical capacities, normalized C3 delith potential-response and appropriate t63 observations. **SI:** detailed C2→C3 contrasts, sensitivity, nonlinear-voltage vs time-stretch identifiability, and method-dependent apparent GITT diffusivity. The latter even reverses BM/HEO D ordering under defensible analysis windows (pulse slope median ratio 0.162; rest sqrt(t) 2.46; finite-pulse descriptor 1.78): avoid calling any ranking a materials-intrinsic D result.

## 4. Composition-aware reference audit (the 11 Nov Word [1–24] numbers stay fixed)
| Existing/new | Verified work/DOI | What it can support; what it cannot |
|---|---|---|
| [4] Luo, *Adv Sci* 2022, 10.1002/advs.202201219 | Co-free (CrMnFeNiCu)3O4 operando XAS identifies Ni/Cu and two-step Fe/Mn paths; cannot map Fe/Mn in this exact sample to R2/R3 individually. |
| [5] Triolo, *Small* 2023, 10.1002/smll.202304585 | Zn-containing nanofiber spinel→rocksalt Li-insertion/cation-migration/conversion; no proof of our four phases. |
| [6] He, *Nat Commun* 2016, 10.1038/ncomms11441 | Fe3O4 in situ TEM shows insertion and conversion can coexist at different rates, not HEO-specific chemistry. |
| [7] Li, *Angew Chem Int Ed* 2025, 10.1002/anie.202518569 | Size-dependent HEO oxygen migration and incomplete conversion; particle-size-control analogy does not convert BET into our reactive area or true primary particle diffusion length. |
| [10–12] Kang/Chueh; Zhu/Wang; Horner, original Word | GITT limits, phase-transition/polarization dynamics; do not infer unique D or rate from t63. |
| [15] Wang, *Nat Commun* 2023, 10.1038/s41467-023-37034-6 | Rocksalt Mg0.2Co0.2Ni0.2Cu0.2Zn0.2O: Mg²⁺ redox-inactive Mg-rich residual oxide; not our spinel Mg site evidence. |
| [19] Liu, *Chem Sci* 2026, 10.1039/D5SC10185A | (CoCuMgCrFe)3O4: Cu/Mg structural roles vs Cr/Fe/Co active; different composition from ours. |
| [20–24] current Word analogs | Hysteresis (fluoride), Fe3O4 model, SiO-graphite voltage rest, structural relaxation; only specific support where directly relevant. |
| **[25]** Jin et al., *Mater Today Chem* **48** (2025), 102949, 10.1016/j.mtchem.2025.102949 | Near-composition (FeCoCrNiMn)3O4, **in situ XRD + ex situ TEM**, spinel→mixed spinel/rocksalt→rocksalt pathway in their HEO-950 material; cannot establish identical pathway in the present powders. |
| **[26]** Ng et al., *J Mater Chem A* **9** (2021), **523–537**, 10.1039/D0TA09683K | Prior use of GITT along NiO conversion/SEI reaction; honest novelty boundary. |
| **[27]** Ghigna et al., *ACS Appl Mater Interfaces* **12** (2020), **50344–50354**, 10.1021/acsami.0c13161 | First-lithiation/delithiation HEO operando XAS transition-metal reduction and conversion; a different oxide composition. |

The new citations [25–27] are appended to a *proposed* Word bibliography only after actual manuscript reassembly. Never renumber [1–24] without a complete citation and figure/SI cross-check.

## 5. Manuscript scope and figure status
- PI-locked Abstract and Introduction four paragraphs: exact 2026-11-11 text, no rewriting.
- §§2.1–2.2: author-approved latest Word text and current Fig1–3 retained; no spontaneous reformat.
- Proposed §2.3: electrochemical R1–R4 and evidence-qualified physical associations. §2.4: nominal ΔQ, boundary displacement, deterministic ±1-pulse robustness. §2.5: C1→C2/C3 successive cycle histories; BM/Mg reversible responses. §2.6: literature-supported interpretations + response-level design value. Conclusion: observable-first summary.
- Existing Fig4 and Fig5 preserved. Proposed *data* Fig6 is 4-panel C1–C3 nominal GITT charge + C3 delithiation normalized QOCV-based cumulative charge. Existing qualitative Figure6 should be moved to SI (preferred) or become Fig7 if PI approves. Figures/sections have **not** been modified in Word; proposed SVG/PNG remain a conversation-local artifact, not committed.
- The proposed Results draft previously contained Figure Sx/Table Sx placeholders. In the 23-Nov proposed text these are explicitly identified as **planned SI figures/tables, numbering pending**, not as existing verified items. Verify final Figure S4/Table S1–S3 numbering and reference order at assembly.
- The main text cannot claim no limitations: single-cell design, finite QOCV and phenomenological response models are factual scope disclosures; avoid repetitive disclaimers in every paragraph.

## 6. Submission-blocking SOURCE AUDITS — existing records only, no new experiments requested
**Priority A (must reconcile original sources, or delete unsupported statements):**
1. Figure 1 HRTEM label **CoGa2O4** conflicts with nominal Ga-free HEO. Correct with real lattice d-spacing/FFT/powder card only, or omit the label; do not silently invent a replacement indexing.
2. Methods Mg precursor and actual cation stoichiometry/nominal substitution recipe incomplete. Verify existing lab documentation; Mg 1s ~1303 eV proves near-surface Mg, not lattice site substitution.
3. Electrode composition, active mass loading, nominal vs actual current, electrolyte/FEC amount, test temperature/cutoffs and 1C definition incomplete. These are reproducibility requirements; avoid unverified precision claims.
4. XRD/ICP claims in Methods require source curves/data and actual measured stoichiometry; remove unperformed-method statements rather than claim absent supporting results.
5. Fig3 100-cycle/rate specific values are graph-read approximations, and 5C→0.1C recovery is substantial but **incomplete**. Confirm lab records or state approximate, and check true initial lith/delith label.
6. XPS high-BE O1s shoulder cannot establish a quantified vacancy concentration; Cr2p oxidation-state deconvolution/calibration unverified. Preserve restrained accepted section.
**Priority B:** final source-derived main/SI/caption citation order, individual SI figure panels, artwork provenance; avoid conflating GITT vs continuous GCD nominal mAh/g.

If any existing metadata cannot be recovered, choose reduced claims or transparent missing source documentation, and note that the paper is **scientifically narratable but not yet confirmed submission-ready**.

## 7. Explicit decisions and next chat
- No new experiments; no new FEM; no additional model fitting for manuscript closure unless a newly found consistency error demands it.
- Current completed artifact: [Results/Discussion proposed full text](HEO_2026-11-23_EXPERIMENT_FREE_RESULTS_DISCUSSION_PROPOSED.md). Its language was reviewed and improved, but it is **not PI-final wording** and **not in Word**.
- This audit + accompanying current-state entry provide all necessary continuity; future chat should **review §2.3 line by line**, then §2.4→2.5→2.6, compare with 11-Nov Word, and after PI approval integrate actual Word/SI preserving native comments.
- Do not update GitHub again unless explicitly requested by PI.
