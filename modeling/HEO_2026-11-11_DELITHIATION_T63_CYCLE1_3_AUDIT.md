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
