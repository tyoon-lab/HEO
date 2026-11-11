# HEO — Same-cell delithiation GITT t63, cycles 1–3 (2026-11-11)

**Status: exploratory source-level analysis for PI discussion; not yet incorporated into manuscript.** Current user request: inspect changes in t63 during delithiation ("방전") before attempting any region assignment or complicated first-cycle-to-later-cycle reaction mapping. **No DOCX or manuscript wording altered.**

## Provenance and extraction
- Four raw GITT workbooks available locally: `HEO GITT 로우 데이터.xlsx`, `BM HEO 3 GITT 로우 데이터.xlsx`, `HEO 3 Mg 로우 데이터.xlsx`, `BM HEO 3 Mg 로우 데이터.xlsx`; cross-check [`[GITT try 2_031].xlsx`] for pristine. Data have 3 full cycles + incomplete fourth lithiation; **use cycles 1–3 only**.
- Positive-current pulse blocks are assigned to delithiation. Negative-current blocks are lithiation; the positive pulse is after the first lithiation in cycle 1. Verify instrument program naming (earlier source slide calls the negative-current halfcycle `Charging`).
- For each **fully rested positive pulse**, define signed `ΔE = E_rest,end − E_rest,3s` (generally negative during delithiation), and compute the first interpolation crossing of `E_rest,3s + (1−e^{−1})×ΔE`, measuring elapsed time from the 3 s reference. Rest window ~3600 s; sampling 1 s for HEO/BM-HEO, 3 s for Mg variants.
- Exclude terminal cutoff pulses without a complete 3600s rest from the t63 figures. Figure source data were extracted and independently inspected from actual XLSX XML via local Python and conserved in `/mnt/data/heo_gitt_pulsewise_audit.json` (runtime artifact, not uploaded binary to GitHub). t63 is an **effective finite-window relaxation time**, not a unique interfacial exchange or solid diffusion rate.
- **Do not propagate first-lithiation R1–R4 pulse boundaries into delithiation.** Hysteresis and phase-path nonidentity prohibit treating matched voltage as matched reaction identity.

## Robust cycle summary — pulsewise t63 median in seconds

| Material | Delith C1 | Delith C2 | Delith C3 | Full-rest pulses C1/C2/C3 |
|---|---:|---:|---:|---|
| HEO | 417.0 | 423.6 | 430.3 | 45/44/44 |
| BM-HEO | 539.2 | 531.8 | 531.9 | 51/50/49 |
| Mg-HEO | 455.8 | 427.9 | 418.1 | 30/29/28 |
| BM-Mg-HEO | 482.1 | 471.7 | 462.4 | 34/33/32 |

**Interpretation:** ball milling increases the effective delithiation relaxation time in both compositional matched pairs and this contrast is retained C1–C3. HEO median rises slightly (+13 s), BM-HEO is nearly unchanged (−7 s), Mg-HEO decreases (−38 s), BM-Mg-HEO decreases (−20 s). Because samples have different delithiation charge span/pulse counts, pulsewise medians alone are **not** matched-state kinetic comparisons.

## Potential-matched test (interpolation at identical rest-end QOCV = 0.90 V)

| Material | C1 (s) | C2 (s) | C3 (s) | C3−C1 (s) |
|---|---:|---:|---:|---:|
| HEO | 440.3 | 464.2 | 469.2 | +28.9 |
| BM-HEO | 571.8 | 564.2 | 563.9 | −7.9 |
| Mg-HEO | 495.2 | 461.6 | 446.1 | −49.1 |
| BM-Mg-HEO | 534.8 | 516.7 | 504.2 | −30.6 |

**At 0.90 V third delithiation:**
- Milling increases t63 by **+94.7 s** (BM−HEO) and **+58.1 s** (BM-Mg−Mg).
- Mg incorporation reduces t63 by **−23.1 s** (Mg−HEO), **−59.7 s** (BM-Mg−BM).
- Evolution differs between Mg-free and Mg-containing powders: HEO becomes somewhat slower while Mg-HEO becomes faster in operational t63. A single overall cycle average understates these contrasts.
- In the common QOCV 0.3–1.6 V interval, most of the HEO t63 C3−C1 curve is positive, Mg-HEO and BM-Mg-HEO curves are negative, and BM-HEO is close to unchanged except near low potential. `QOCV` after 60 min rest is a comparable **measured potential**, but cannot be equated with the same Li fraction or same reaction/phase across converted oxides, so this is an observational comparison rather than causal matched-state identification.
- At 0.30 V t63 is especially cycle sensitive: HEO ~151→257→286 s, BM ~413→358→345 s, Mg ~419→337→276 s, BM-Mg ~438→390→302 s. Early delithiation t63 is particularly affected by prior first lithiation/first current reversal; use extra caution in assigning mechanisms or phase reorganization.

## Shape of pulsewise delithiation curves

- All materials have a steep rise in t63 over the initial low-potential delithiation, a broad middle region at several hundred seconds, and a final decrease approaching the upper end of their respective delithiation windows (some features or upturns near endpoint may vary).
- HEO C3 t63 increases to ~496 s near 1.24 V and decreases at higher voltage; first-cycle maximum ~470 s near 1.30 V.
- BM-HEO C3 reaches ~596 s near 1.08 V, substantially above HEO, and has broad elevated t63 at higher potentials as well.
- Mg-HEO C3 reaches ~446 s near 0.90 V and declines particularly at high QOCV; BM-Mg C3 reaches ~522 s near 1.07 V.
- C2 and C3 curves have similar shapes within each sample; compare exact Δt63 after interpolation rather than visual pulse-position shifts.
- For same 0.90 V QOCV, measured **absolute recovery amplitude** `|ΔErest|` is 3rd cycle HEO ~85.1 mV, BM ~90.4, Mg ~96.0, BM-Mg ~102.8. Thus differences in t63 cannot be reduced to a simple proportional amplitude change. Their assignment to interfacial, diffusion, or phase transformation remains unproven.

## Proposal: low-complexity presentation and evidence gate

- Core early observation: **BM maintains longer delithiation t63 across 3 cycles, whereas Mg-containing cases show declining t63 with cycling.**
- If this is useful to paper, show **one concise four-material t63-vs-QOCV plot for C3** and optionally **C3−C1 vs QOCV** as SI; do not introduce arbitrary four-region segments in delithiation or a heavy kinetic-model inference.
- Keep C1/C2/C3 numeric metrics, reference-3s algebra, potential interpolation, cutoff flags, and no-replicate caveats in this internal note.
- Mechanistic test still pending: `t63` effective response vs fraction of reversible charge or SOC, and paired `ΔErest` shape; potential-defined bins alone cannot uniquely transfer the first-lithiation R2/R3 process labels into later delithiation.
- **No new experimental request or manuscript draft yet.** No replicated-cell inference from one cell's three sequential cycles.


## Addendum 2026-11-11 — first delithiation, three-observable joint review (PI request)

Scope: exactly four materials' **first** positive-current halfcycle; original first-delith pulsewise XLSX extraction, 45/51/30/34 **fully rested** pulses. Compare t63 (time after 3s reference), signed ΔErest = E(rest 3600s)−E(rest 3s) (negative on delithiation, display its **magnitude**), and QOCV (rest-end voltage). Graph x is normalized ordinal index of included, fully rested GITT pulses, **not equal absolute charge across materials** and does not include terminal cutoff partial pulse. Three independent single-axis charts and one vertical viewing sheet generated as local conversation artifacts: `HEO_first_delith_C1_t63_normalized.png`, `HEO_first_delith_C1_dE_normalized.png`, `HEO_first_delith_C1_QOCV_normalized.png`, `HEO_first_delith_C1_t63_dErest_QOCV_overview.png`. Original pulsewise calculations preserved in `first_delithiation_gitt_t63_pulsewise.csv` within local conversation; **those binaries are not in GitHub**.

| Sample | t63 peak (s) / QOCV (V) | t63 median (s) | |ΔErest| first→last full-rest pulse (mV) | QOCV first→last (V) |
|---|---|---:|---|---|
| HEO | 471 / 1.298 | ~418 | 20.2→370.2 | 0.219→1.902 |
| BM-HEO | 587 / 1.080 | ~540 | 16.7→342.8 | 0.190→2.076 |
| Mg-HEO | 500 / 0.756 | ~459 | 26.9→379.6 | 0.200→1.756 |
| BM-Mg-HEO | 546 / 1.024 | ~485 | 23.1→419.5 | 0.196→1.853 |

**Direct observational trends:** (1) Rapid initial increase in t63 (notably over pulses ~1–5), then broad intermediate high/plateau or slowly declining t63; peak voltage differs substantially among materials; late delithiation t63 decreases. (2) |ΔErest| generally rises through delithiation and increases more sharply at the high-voltage/terminal pulses, despite decreasing t63. (3) QOCV rises smoothly and differently across samples; there is no obvious universal mid-cycle jump that independently establishes a common physical boundary. ΔE amplitude and t63 are distinct, and the three signals do **not** deliver coincident universal transition points.

**Exploratory 2-knot continuous linear fit** to the three observables simultaneously after centering/normalizing each observable, with shared sample-specific knot positions but independent slopes, finds early knot around pulse 5–6 and QOCV ~0.56–0.64 V, late knot at HEO pulse41 (1.77 V), BM pulse47 (1.92 V), Mg pulse26 (1.60 V), BM-Mg pulse29 (1.64 V). **Importantly this is a *forced* two-breakpoint model, not proof of meaningful boundaries**. Stability audit demonstrates endpoints drive the knots: deleting the last two fully rested pulses in HEO and BM moves the nominal late knot from ~1.77/1.92 V to ~1.27/1.12 V; deleting the first two pulses moves early knots to ~1.05 V HEO, ~0.89 V BM, ~1.04 V Mg, ~1.02 V BM-Mg. Therefore **DO NOT publish these values as robust delithiation region boundaries** or import first-lithiation R1–R4 labels into delithiation. A defensible description is an early fast-rise, middle broad response and late large-polarization region, keeping thresholds provisional.

**Interpretation/decision:** first delithiation 3-observable overview is physically informative, but the change points are cutoff/current-reversal sensitive; keep the quantitative knot search internal until challenged by common-voltage analysis, alternative window choices, and independent physical evidence. In particular, terminal high-voltage |ΔErest| increases while t63 decreases and should not be read as globally slower delithiation. No manuscript/Word file, abstract, figure numbering or locked first-lithiation segmentation modified.


## Addendum — PI provisional three-region basis + QOCV differential-charge test (2026-11-11)

### PI decision
For **first delithiation only**, **provisionally adopt THREE operational t63-response regimes** as a working analysis structure:
- **D1, early:** steep t63 increase after first current reversal;
- **D2, middle:** broad high, quasi-plateau or smooth maximum t63;
- **D3, late:** falling t63 while often rising |ΔErest|.

The labels D1–D3 are **internal placeholders**, not yet named in the paper. **No adopted numeric breakpoints**, no assertion of three distinct chemical phases, and no mapping to first-lithiation R1–R4. t63 is the primary proposed boundary descriptor; QOCV and |ΔErest| are independent supporting observables. Earlier joint forced two-knot model was highly endpoint-sensitive; do not reuse fitted voltages as confirmed boundaries. The PI specifically requested examining a *QOCV-based dQ/dV*, not rewriting manuscripts, a DOCX, or redrawing existing publication figures.

### Computation — first delithiation
Using the prior first-positive-current, fully-rested pulsewise CSV (`first_delithiation_gitt_t63_pulsewise.csv`, from four real XLSX workbooks, n=45/51/30/34), calculate local discrete differential capacity from adjacent **full** 600-s pulses at nominal 100 mA g−1:

`dQ/dV at (QOCV_i + QOCV_{i+1})/2 = (100 mA/g * 600s / 3600s) / (QOCV_{i+1} - QOCV_i)`.

- The 60-min rest-end `QOCV_i` monotonically increases in all four sequences (strictly positive first differences); no negative or zero denominator.
- This is **GITT QOCV-derived finite-step quasi-equilibrium differential charge**, **NOT** ordinary continuous GCD dQ/dV, true equilibrium OCV differential capacity, or a direct unique chemical reaction fingerprint.
- Direct unsmoothed midpoint differences in 60-minute QOCV; optional weak Savitzky–Golay windows 5,7,9 (degree 2) were only used for *peak-stability diagnostics* and do not alter the plotted curve.

| Sample | n full-rest pulses | Peak dQ/dV QOCV (V) | Peak height (mAh g−1 V−1) | t63 maximum QOCV (V) | weak-smoothing peak QOCV (5/7/9-point windows, V) |
|---|---:|---:|---:|---:|---|
| HEO | 45 | 1.534 | 813.8 | 1.298 | 1.534 / 1.555 / 1.555 |
| BM-HEO | 51 | 1.307 | 801.7 | 1.080 | 1.307 / 1.328 / 1.328 |
| Mg-HEO | 30 | 1.527 | 545.0 | 0.756 | 1.557 / 1.557 / 1.557 |
| BM-Mg-HEO | 34 | 1.305 | 547.9 | 1.024 | 1.305 / 1.305 / 1.305 |

Interpretation at observation level:
1. **Ball milling** shifts the *global maximum of the QOCV-derived dQ/dV curve* to a lower QOCV in both matched comparisons (~1.53→~1.30 V). The **BM-HEO shoulder** at ~1.56–1.60 V is detectable as a second weak local maximum using 5- and 7-point smoothers, but it merges into one broad feature at 9 points. **Do not** claim two uniquely identified reactions.
2. **Mg incorporation** substantially reduces raw dQ/dV peak magnitude (~814→545 and ~802→548 mAh g−1 V−1) without similarly large peak-voltage shifts at matched milling condition. Magnitude depends on total accessed charge, voltage profile, rest kinetics and protocol, so mechanistic attribution is premature.
3. The **t63 maxima and dQ/dV maxima are systematically separated** (~0.23 V in both Mg-free samples; ~0.77 V Mg-HEO; ~0.28 V BM-Mg). This argues AGAINST setting a single delithiation boundary at a dQ/dV peak or assuming voltage-relaxation time traces the differential-capacity maximum. dQ/dV can help identify distinct *potential-dependent storage features* while t63 provides an independent time-response descriptor.
4. Do not lock first-delithiation region voltages from these peak values. Check later whether each D1–D3 boundary remains stable under leave-endpoint-out sensitivity analysis and whether sharp dQ/dV features (versus broad maxima) have independent physical meaning.

Visualization created as current-chat analysis artifact (not committed as binaries): `HEO_first_delithiation_QOCV_dQdV.png`. Numeric derived curve: `HEO_first_delithiation_QOCV_dQdV.csv`. No manuscript/Word changes or new experiments.
