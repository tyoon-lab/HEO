# HEO — C1–C3 GITT intervention mechanism and minimum-model discrimination (2026-11-18)

**Status:** Internal, reproducible research record. PI explicitly requested GitHub archival and a presentation on 2026-11-18. This is **not** a manuscript revision or a phase-identification claim. The PI-approved Abstract and four Introduction paragraphs (2026-11-11), original first-lithiation R1–R4 definitions, all Word comments, existing figures and SI remain unchanged. **Read this record first when continuing the BM/Mg/C1-to-C3 discussion.**

## A. Research question and conclusion

**Question:** Why do BM and Mg both reduce the operational first-lithiation R3 GITT charge, yet have opposite total capacity effects, and *where/how do those effects persist* during subsequent lithiation and delithiation?

**Strongest empirical conclusion:** Both treatments reduce **C1 R3 as defined by moving t63 boundaries**, but change those boundaries, first-cycle voltage response, and subsequent reversible electrochemistry differently. BM increases accessible charge and produces (i) a reproducible lower-potential redistribution of **C2/C3 delithiation** charge and (ii) a larger long-time/slow-fraction voltage recovery with longer effective t63. Mg decreases overall accessible charge and shifts the voltage–charge relation; under the tested minimal models, an independent Mg-specific blocked-redox-population term is unnecessary to reproduce C3 delithiation. Total capacity effects nearly factorize whereas kinetic effects depend on BM×Mg background. A specific C1 R2/R3 reaction cannot be uniquely traced to a later-cycle voltage interval.

**Working physical hypothesis:** BM broadens/reweights the accessible ensemble of conversion-related states, including slower-relaxing/reconstructed populations, while Mg primarily modifies accessible redox inventory and the potential landscape; Mg-rich/oxide stabilization remains a plausible but **unproven** alternative to active-metal dilution. The observed relaxation effects could also reflect voltage slope, electrode morphology/transport, polarization and history: do not equate a t63 shift with an intrinsic reaction-rate constant.

## B. Raw-data/protocol and boundaries

Four original September-17 student XLSX reports:
- HEO GITT 로우 데이터.xlsx
- BM HEO 3 GITT 로우 데이터.xlsx
- HEO 3 Mg 로우 데이터.xlsx
- BM HEO 3 Mg 로우 데이터.xlsx

Raw exports are NOT committed to GitHub. Recovered from user's Gmail/Drive in the November 17–18 working container. Complete cycle 1/2/3 **negative-current lithiation** and **positive-current delithiation**; nominal 600 s pulse / 3600 s rest / 100 mA g−1 (=16.6667 mAh g−1/full pulse). Split-sheet de-duplication, direct sign reversal at cutoff, and incomplete C4 exclusion are mandatory. Approximately **1,020 fully rested pulses in 24 complete halfcycles**; terminal partial pulses enter whole-halfcycle Q but NOT t63 or original C1 regional full-pulse bins. Some unit/active-mass/source-calibration metadata still require verification. Each treatment is one cell with C1–C3 as *sequential histories*, not independent replicates.

C1 after-pulse region boundaries **fixed and unchanged**, from first-lithiation t63 only: HEO 6/25/55; BM-HEO 9/38/60; Mg-HEO 7/24/42; BM-Mg 9/35/46.

| sample | R1 | R2 | R3 | R4 | C1 complete-pulse total |
|---|---:|---:|---:|---:|---:|
| HEO | 100.0 | 316.7 | 500.0 | 166.7 | 1083.3 |
| BM-HEO | 150.0 | 483.3 | 366.7 | 266.7 | 1266.7 |
| Mg-HEO | 116.7 | 283.3 | 300.0 | 100.0 | 800.0 |
| BM-Mg-HEO | 150.0 | 433.3 | 183.3 | 166.7 | 933.3 |

Units mAh g−1, nominal charge. BM change R2 +166.7/+150.0 and R3 −133.3/−116.7 (no-Mg/with-Mg); Mg change R3 −200.0/−183.3 (no-BM/with-BM). R3 fraction of first lithiation: HEO 46.15%, BM 28.95%, Mg 37.50%, BM-Mg 19.64%. BM shifts L3 later (+13 or +11 pulses), Mg shifts L4 earlier (−13 or −14), although R3 shrinks in both interventions. Adjacent full normalized rest waveforms vary smoothly at L3, and these are electrochemical response regions, **not individually identified chemical phases**.

C1 extra nominal lithiation charge vs C2/C3 ~342–425 mAh g−1; C1 delithiation QOCV topology already resembles later delithiation more than C1 lithiation, though t63 and amplitude still evolve. C2/C3 `|ΔErest|` hump persists despite first-cycle t63 hump largely fading. Recurring ~0.90V lithiation differential-charge feature and subsequent amplitude hump are **two distinct empirical landmarks**, not one proven reaction.

## C. Whole-halfcycle C1–C3 nominal GITT capacity (including terminal partial pulse)

| sample | C1 lith | C1 delith | C2 lith | C2 delith | C3 lith | C3 delith |
|---|---:|---:|---:|---:|---:|---:|
| HEO | 1094.22 | 762.28 | 715.00 | 746.28 | 710.47 | 742.92 |
| BM-HEO | 1278.50 | 858.53 | 860.89 | 840.81 | 844.39 | 827.58 |
| Mg-HEO | 814.25 | 515.67 | 476.08 | 495.17 | 462.75 | 478.50 |
| BM-Mg-HEO | 948.17 | 583.17 | 577.58 | 563.42 | 549.58 | 543.50 |

All mAh g−1, nominal. Independent conventional GCD 0.1C first-cycle values differ and must not be conflated. C2/C3 total capacity contrasts remain BM positive, Mg negative in both current directions. Nearly factorial total relation:
`Q_BM-Mg ≈ Q_BM*Q_Mg/Q_HEO`. C3 predicted/observed BM-Mg lith: 550.0/549.6; delith 533.0/543.5 mAh g−1. This uses *contemporaneous other-sample data* rather than wholly independent prediction. Applying C2-calibrated capacity factors to C3 gives ~1.1–3.7% errors. Integrated-capacity factorization does NOT demonstrate independence of kinetics or chemistry.

## D. Descriptive potential-resolved and kinetic differences

First delithiation GITT-QOCV-derived dQ/dV peaks: HEO 1.534 V, BM 1.307, Mg 1.527, BM-Mg 1.305. Later C2/C3 unsmoothed peak positions sometimes follow this pattern BUT smoothing can change which of multiple broad maxima is global. **Do not claim a universally robust singular peak voltage displacement.** Robust BM sign is increased normalized C2/C3 delithiation charge in a broad lower-voltage window (~1.05–1.40 V) and reduced normalized contribution in a higher window (~1.40–1.70 V), after total-capacity scaling.

For C3 delithiation, potential-matched effective t63 BM enhancement ~+81s with no Mg and ~+50s with Mg (model-aligned comparisons); the fraction of normalized recovery during the first 300s decreases by approximately −0.035 and −0.024 with BM. t63 increase and larger accessible reversible charge coexist. This is **not** equivalent to intrinsically slower elementary conversion or uniquely increased diffusive resistance. In C2/C3 lithiation at ~0.90 V, t63 values across four samples lie near ~542–586s, distinct from delithiation modification response: do not force symmetric kinetics in both directions.

A previous Mg-local `|ΔErest|` residual at 0.90V after amplitude-only correction (~−12 to −14mV, C2/C3 lithiation) becomes ~1–3mV when a jointly fitted global voltage shift is also allowed. Therefore **do not present the earlier residual as proof of a selectively blocked Mg conversion band.** Likewise post-hump capacity fraction is anchor-sensitive; first-cycle R2 gain cannot be mapped one-to-one onto later post-hump charge.

## E. Actual minimal-model hierarchy and held-out tests

Define normalized cumulative potential-resolved charge `u(V)=Q(V)/Q_total`; QOCV is finite-time rest voltage, not verified equilibrium OCV. Fit the intervention effect using C2 and predict **C3** using the C3 reference-material baseline (a held-out-cycle *contrast* transfer, not a completely independent battery forecast).

- **C0 capacity factor only:** `Q_tot,treat=A_Q Q_tot,ref`; normalized potential-response shape unchanged.
- **C1 capacity factor + potential translation:** `u_treat(V)=u_ref(V−ΔV)`.
- **C2 two potential populations:** `u_treat(V)=u_ref(V−ΔV)+β[Φ((V−μL)/σ)−Φ((V−μH)/σ)]`; for delithiation, nominal `μL=1.18 V, μH=1.56 V, σ=0.13 V`. **β is a model-equivalent reweighting, not a directly measured chemical/phase fraction.**
- **C2a matched-complexity alternative:** global affine potential warp `V→V−ΔV−γ(V−1.0 V)`, controls for a potential-axis stretch.
- **K0/K1:** first fit voltage shift, then test whether a single C2-derived `Δt63` must also be carried to C3. This is a descriptive dynamic offset, not an elementary kinetic rate.
- **2-τ demonstrator:** finite-window normalized fast/slow exponential mixture tuned on HEO C2. Fits partial curve features but not independent t63 precisely (MAE ~40–47s), so **τ~200/3100 s and model-inferred slow weights are NOT uniquely identified physical modes.**

**C2→C3 delithiation normalized cumulative-capacity RMSE** (units: fraction of Q_total):

| pair | C1 shift-only | C2 population | C2a affine warp | β fitted on C2 |
|---|---:|---:|---:|---:|
| BM−HEO | 0.0144 | **0.0087** | 0.0144 | **+0.051** |
| BM-Mg−Mg | 0.0097 | **0.0042** | 0.0096 | **+0.044** |
| Mg−HEO | **0.0063** | 0.0064 | 0.0082 | −0.021 |
| BM-Mg−BM | 0.0141 | 0.0140 | 0.0137 | −0.014 |

Population correction improves held-out C3 delithiation for BM by ~40% and ~57% vs translation-only, and beats equal-complexity affine voltage stretch. In 12 predetermined `μL/μH/σ` sensitivity settings (centers shifted ±0.06V; width 0.09–0.21V), BM β positive in 12/12 and held-out error lower in 12/12 for *both Mg backgrounds*. C3→C2 reverse direction also preserves improvement. For Mg-only, population correction is not robustly justified. **Lithiation does NOT exhibit the same universal redistribution model benefit; BM lithiation is better described by potential-affine warp in these tested families.**

**C3 t63 shift-only vs shift+Δt63 held-out RMSE (s):**
- BM−HEO lith 101.5→39.4; delith **84.5→23.9**
- BM-Mg−Mg lith 49.6→22.9; delith **52.0→13.4**

The dynamic Δt63 effect is more background-dependent than the integrated capacity effect. BM delithiation mean t63 +~81s no-Mg vs +~50s Mg (C3 after potential alignment); naive BM offset transferred from no-Mg to Mg overpredicts. This is BM×Mg interaction in response time despite near-factorizable overall Q.

**Entire BM-Mg treatment held out from C2 shape fitting:** 
- BM/noMg C2 population model on Mg reference predicts C3 BM-Mg delith shape RMSE **0.0063** vs Mg reference-only **0.0091**.
- Mg/noBM C2 potential-shift effect on BM reference predicts C3 BM-Mg delith shape RMSE **0.0102** vs BM reference-only **0.0485**.
- BM/noMg effect transferred to Mg-containing **lithiation** worsens shape (RMSE ~0.027 vs ~0.0095 for unchanged Mg baseline), emphasizing direction-specific interactions. These are contrast transfers, not mechanism-unique validation.

## F. Competing mechanism interpretation and publication claim gate

**Hypothesis H1 (accessibility/heterogeneous populations; favored as *working model*):** BM refines morphology and enables additional/reweighted reversible conversion-related states over a wider voltage range; their relative slow voltage-recovery contribution grows. A transition from pristine spinel to a reconstructed/residual metal/Li2O network during C1 may shape C2/C3 responses. Mg changes accessible active-reduction inventory and QOCV potential, potentially stabilizing residual intermediate oxides or diluting active metal fraction.

**Rival H0:** changes arise from cation dilution/mass reference, electrode resistance/contact/wetting or active surface, cycle-dependent potential slope/hysteresis, cutoff/SEI, plus generic finite-window polarization; kinetic regions move continuously. Some H0 terms were tested (global capacity shift/potential warp/amplitude scaling), but independent phase-specific proof is absent.

**Evidence hierarchy:** observation (pulsewise C1 region and C2/C3 curves) > restricted-family held-out model discrimination > mechanistic hypothesis supported by external studies. C1 R2/R3 → C2/C3 causal chemical inheritance **unproven**. Mg 1s XPS is not proof of substitution site. Exact Mg recipe/site/actual ICP, electrode mass/area/current normalization, sample-state structural data and independent cell repeats remain open.

**Literature context (validate exact composition when citing):**
- Luo et al., *Adv. Sci.* 2022 DOI 10.1002/advs.202201219 — operando XAS overlapping TM-specific reduction.
- Triolo et al., *Small* 2023 DOI 10.1002/smll.202304585 — insertion/cation migration/spinel–rocksalt conversion.
- Li et al., *Angew. Chem. Int. Ed.* 2025 DOI 10.1002/anie.202518569 — size/oxygen-migration/partial conversion, GITT voltage features already known.
- Jin et al., *Mater. Today Chem.* 2025 DOI 10.1016/j.mtchem.2025.102949 — composition-nearest structural history/spinel–rocksalt.
- Wang et al., *Nat. Commun.* 2023 DOI 10.1038/s41467-023-37034-6 — Mg residual oxide **different rock-salt composition**.
- Liu et al., *Chem. Sci.* 2026 DOI 10.1039/D5SC10185A — structurally associated Mg in different spinel; use only as hypothesis support.
- Ng et al., *J. Mater. Chem. A* 2021 DOI 10.1039/D0TA09683K — prior GITT-based trend segmentation of conversion NiO; do NOT claim four-region GITT method-first novelty.

## G. Exact local artifact/coding inventory and reproducibility note

On 2026-11-18 an analyzed ZIP was created at the conversation's local runtime: `HEO_minimal_mechanistic_model_2026-11-18.zip` (reports, raw-extracted pulsewise and capacity CSV, source *.py, model scores, sensitivity test, figures). Companion `HEO_C1_C3_mechanistic_comparison_2026-11-18.zip`, and C1 `HEO_R3_C1_reanalysis_2026-11-17.zip` document the preceding stages. **These binaries/scripts/data are local downloadable conversation artifacts; this GitHub documentation commit does not by itself upload ZIP, original XLSX, numerical CSVs, PNGs, PPTX or Python scripts.** Re-run numerical studies by obtaining four original workbooks and local ZIP, preserving fixed interpretation and endpoint conventions. Do not assert files are in GitHub unless uploaded and verified.

## H. Manuscript and next scientific action

- Keep original accepted first-lithiation R1–R4 analysis, exact locked Abstract/Intro and 6 existing figures **unchanged** unless explicitly reopened.
- Candidate *additional* Results subsection: “Persistence and divergence of morphology- and composition-dependent electrochemical responses in later cycles.” Show (1) first R3 boundary contraction mechanism differs, (2) C2/C3 factorization in whole Q, (3) C3 held-out delithiation model + t63, (4) hypotheses and alternative causes.
- Candidate graphical comparison: C1 R2/R3 ΔQ; C2/C3 normalized delith potential charge redistribution; C3 model RMSE; paired lith/delith t63 differences. All supported by local plots but presentation visuals are **not automatically approved manuscript figures**.
- Future test to separate **Mg active fraction vs oxide stabilization**: verify exact Mg stoichiometry/cation population and loading, state-resolved XRD/XAS (C1 R2/R3, post-first-delithiation), independent electrode repeats; optional changed GITT rest/pulse protocol for out-of-sample time-domain predictive discrimination. No FEM until 0D alternatives are falsified with held-out waveforms.
- Journal strategy remains unresolved; no manuscript submission.
