# HEO — START HERE / Current Project State

**Last consolidated:** 2026-09-20  
**Purpose:** single entry point for resuming the HEO manuscript/project in a new chat without a separate handoff.  
**Rule:** read this file first. The linked Main/SI Markdown files are the scientific authority. Historical files are preserved only for provenance.

---

# 0. Restart protocol for a new chat

A new chat should be able to resume from this repository alone.

Read, in this order:

1. **Main manuscript — authoritative**
   - \`manuscript/HEO_MANUSCRIPT_V4_AFM_CONVERSION_2026-09-20.md\`
2. **Supporting Information — authoritative**
   - \`manuscript/HEO_SUPPORTING_INFORMATION_V3_REVIEW_READY_2026-09-20.md\`
3. **Figure architecture**
   - \`manuscript/HEO_FIGURE_ARCHITECTURE_AND_CAPTIONS_V2_CONVERSION_2026-09-20.md\`
4. **Conversion-assignment / Figure 4 audit**
   - \`FIGURE4_CONVERSION_ASSIGNMENT_CHECK_2026-09-20.md\`
5. **Consolidation audit**
   - \`manuscript/HEO_CONSOLIDATION_AUDIT_2026-09-20.md\`
6. **Current exported-artifact manifest**
   - \`manuscript/HEO_CURRENT_ARTIFACTS_2026-09-20.md\`

Do not ask for a separate handoff unless new experimental files are required.

Current status:
- Main scientific draft: **complete review draft**
- SI scientific draft: **complete review draft**
- Main Word review export: completed and rendered
- SI Word review export: completed and rendered
- Figure 4 conversion reassignment: locked at current evidence level
- Figure 4 background/window sensitivity audit: completed
- Figure 5 no-refit conversion-ordering validation: completed
- remaining work is primarily final experimental metadata, collaborator structural data, final publication artwork, and optional MATLAB runtime verification.

---

# 1. Manuscript identity

## Current title

**Mg Incorporation and Ball Milling Independently Regulate Electrochemical Accessibility and Conversion in Spinel High-Entropy Oxide Anodes**

## Target journal

**Advanced Functional Materials (AFM)** is the current first target.

Keep the paper materials-centered:

**synthesis/composition perturbation → accessibility and conversion dynamics → electrochemical function**

This is **not** a GITT-method paper. GITT/current-off analysis is supporting diagnostics used to distinguish material-level mechanisms.

## Central material message

The 2 × 2 matrix is:

- HEO
- BM-HEO
- Mg-HEO
- BM-Mg-HEO

The experimentally distinct coordinates are:

1. **electrochemical accessibility**
2. **conversion extent/distribution**
3. **relaxation time**

### Ball milling

Ball milling primarily:
- increases physical/electrochemical accessibility;
- increases capacity/utilization;
- redistributes conversion over heterogeneous local conditions;
- lowers the concentrated conversion-associated excess peak;
- broadens the conversion-associated response;
- does **not** make long-rest relaxation uniformly faster.

Do not reduce the BM story to “faster diffusion.”

### Mg incorporation

Mg primarily:
- stabilizes the oxide-derived parent/intermediate state;
- shifts the conversion-associated feature to lower potential;
- suppresses accessible conversion and capacity;
- strongly suppresses conversion-associated excess polarization;
- does not shorten relaxation and can leave residual structural relaxation slower.

Do not describe Mg as a simple diffusion accelerator.

### BM-Mg

BM-Mg remains strongly suppressed relative to HEO. Milling shifts the Mg-containing conversion feature back toward higher potential and increases accessibility/capacity. Its nominal excess amplitude is slightly larger than Mg-HEO, but **BM-Mg > Mg peak amplitude is background-sensitive and is not a required mechanistic trend**.

---

# 2. Current authoritative files

## Main

\`manuscript/HEO_MANUSCRIPT_V4_AFM_CONVERSION_2026-09-20.md\`

## Supporting Information

\`manuscript/HEO_SUPPORTING_INFORMATION_V3_REVIEW_READY_2026-09-20.md\`

## Figure architecture

\`manuscript/HEO_FIGURE_ARCHITECTURE_AND_CAPTIONS_V2_CONVERSION_2026-09-20.md\`

## Conversion-assignment audit

\`FIGURE4_CONVERSION_ASSIGNMENT_CHECK_2026-09-20.md\`

## Numerical Figure 4 peak table

\`manuscript/HEO_FIGURE4_LATEST_PPT_DQDV_GITT_PEAK_CHECK_2026-09-20.csv\`

## Model authority

Read:
- \`modeling/HEO_FINAL_PYTHON_PHYSICS_GATE_2026-09-18.md\`
- \`modeling/HEO_MODELING_DEVELOPMENT_LOG_2026-09-18.md\`
- \`modeling/heo_spatial_phase_field_frozen_v4.py\`

MATLAB translation:
- \`modeling/HEO_Spatial_PhaseField_Model_Final.m\`

The Python frozen-v4 model is the verified scientific reference. The MATLAB translation has not yet been independently runtime-verified.

## Reference authority

\`manuscript/HEO_REFERENCE_MASTER_VERIFIED_2026-09-18.md\`

Historical drafts are not authoritative.

---

# 3. Key experimental numbers

## GITT protocol

- first-lithiation GITT
- current: 100 mA g⁻¹
- voltage window: 0.005–2.5 V
- pulse: 600 s = 10 min
- rest: 3600 s = 60 min
- common current-off reference: 3 s
- early fit: 3–30 s, \(E=a+b\sqrt t\)

**Do not revert to 60 s rest. The correct rest is 60 min.**

## Current-off medians, approximately 200–800 mAh g⁻¹

| Sample | apparent current-off R (Ω) | ΔErelax (mV) | t63 (min) |
|---|---:|---:|---:|
| HEO | 106.4 | 160.9 | 8.68 |
| BM-HEO | 106.5 | 176.3 | 11.57 |
| Mg-HEO | 40.2 | 109.5 | 11.01 |
| BM-Mg-HEO | 33.0 | 144.3 | 12.99 |

Key contradiction:
- Mg strongly lowers polarization amplitude but does not shorten relaxation.
- BM increases utilization while long-rest relaxation becomes slower.

Therefore one varying apparent diffusion coefficient cannot explain all trends.

## BET

- HEO: 3.94 m² g⁻¹
- BM-HEO: 18.159
- Mg-HEO: 6.49
- BM-Mg-HEO: 16.64

## Relative interfacial-capacitance metric

Nominal Cdl/Cs with 40 µF cm⁻²:
- HEO 4.18 cm²
- BM-HEO 30.17
- Mg-HEO 6.56
- BM-Mg-HEO 39.68

Comparative only. Do not call this absolute ECSA.

## First-cycle instrument-reported capacity pairs

- HEO: 901.25 / 609.12 mAh g⁻¹; ICE 67.59%
- BM-HEO: 1056.10 / 782.08; ICE 74.05%
- Mg-HEO: 731.15 / 458.91; ICE 62.77%
- BM-Mg-HEO: 944.07 / 580.83; ICE 61.52%

WonATech half-cycle convention still requires final verification before assigning lithiation/delithiation wording.

---

# 4. Figure 4 — conversion assignment is current interpretation

## Nominal excess metrics

| Sample | peak excess (mV) | FWHM-like width (mAh g⁻¹) | normalized excess area (mV) |
|---|---:|---:|---:|
| HEO | 70.77 | 354.13 | 22.07 |
| BM-HEO | 44.07 | 430.17 | 14.13 |
| Mg-HEO | 15.91 | 250.29 | 4.94 |
| BM-Mg-HEO | 21.10 | 391.78 | 7.58 |

Capacity-weighted excess is a comparative polarization metric, **not energy**.

## Latest first-cycle dQ/dV cross-check

The latest continuous numerical first-cycle export is not available. The older first-cycle dataset is excluded because a power interruption produced an obvious profile artifact.

Current preferred source:
Park Seong Hyeon, \`HEO 진행상황 (20260917).pptx\`, slide 10, vector Origin artwork.

Reconstructed cathodic dQ/dV peaks:

| Sample | dQ/dV peak (V) | GITT excess peak (V) | mismatch |
|---|---:|---:|---:|
| HEO | 0.545 | 0.527 | 18 mV |
| BM-HEO | 0.589 | 0.618 | 29 mV |
| Mg-HEO | 0.419 | 0.387 | 32 mV |
| BM-Mg-HEO | 0.485 | 0.503 | 18 mV |

All four pairs lie within 32 mV.

Safe language:
- **conversion-associated excess relaxation**
- or **conversion/transformation-associated excess relaxation**

Do not claim the signal directly measures metallic-product fraction, Li₂O fraction, or one unique conversion step.

## Background/window robustness

105 combinations of early-background, late-background, and excess-evaluation windows were tested.

Robust in **105/105**:
- BM peak < HEO
- BM width > HEO
- Mg peak < HEO
- BM-Mg peak < HEO

BM-Mg peak > Mg held in **80/105** only.

Therefore:
- the key BM redistribution and Mg suppression claims are robust;
- the small nominal BM-Mg-versus-Mg amplitude recovery is **background-sensitive** and should not be elevated into a core claim.

Preferred Figure 4 layout:
1. state-resolved relaxation / excess feature
2. dQ/dV–GITT voltage correspondence
3. one-to-one peak-voltage comparison
4. peak-amplitude / width / area map

Detailed background fitting and sensitivity remain in SI.

---

# 5. Figure 5 — reduced spatial model of conversion-associated state evolution

## Meaning of φ

\(\phi\) is an **effective conversion-associated structural-state coordinate**.

- \(\phi\approx0\): oxide-derived parent/intermediate-like state
- larger \(\phi\): progression toward a more deeply converted-like state

It is **not**:
- a measured rock-salt fraction;
- a metallic-product fraction;
- a Li₂O fraction;
- a full stoichiometric conversion model.

## Frozen model, no refit after conversion reassignment

Relaxation-peak model states:

| Sample | c̄ at model relaxation maximum |
|---|---:|
| BM-HEO | 0.5860 |
| HEO | 0.6184 |
| BM-Mg-HEO | 0.7966 |
| Mg-HEO | 0.9100 |

The same earlier-to-later sequence is obtained from pulse-end \(\bar\phi\) thresholds 0.02, 0.05, and 0.10.

This matches the experimental higher-to-lower conversion-feature voltage ordering directionally.

Do **not** map model \(\bar c\) numerically onto experimental \(Q/Q_{\max}\) or voltage.

## Current parameter meaning

- \(G_{\mathrm{Mg}}\): stabilization of the unconverted oxide-derived parent/intermediate state
- \(M_\phi\): effective mobility of conversion-associated structural rearrangement
- \(S_{\mathrm{surf}}\) / BM ensemble: local conversion/surface condition and its heterogeneity

BM-containing maps are ensemble-averaged radial states, not heterogeneous 2D single-particle simulations.

Main Figure 5:
- mechanism-sufficiency schematic
- 4 × 7 pulse-end circular state array
- pulse-end mean \(\bar\phi\) vs model \(\bar c\)

SI:
- model convergence/readout robustness
- no-refit conversion-ordering table
- 60 min \(\Delta\bar\phi_{\mathrm{rest}}\)

---

# 6. SI current state

Authoritative SI:
\`manuscript/HEO_SUPPORTING_INFORMATION_V3_REVIEW_READY_2026-09-20.md\`

Scientific SI structure is fixed for review.

Key completed additions:
- repaired current-off equations;
- 105-case Figure 4 background/window sensitivity audit;
- latest dQ/dV/GITT peak correspondence + smoothing robustness;
- single-D algebraic comparator;
- frozen effective-coordinate table;
- model convergence/readout robustness;
- no-refit conversion-ordering cross-check;
- pulse-end \(\bar\phi\) onset thresholds;
- final SI figure plan S1–S21 and tables S1–S7;
- standalone conventional apparent \(D_{\mathrm{GITT}}\) figure intentionally omitted.

Current figure readiness:
- S17–S21: actual review figures generated
- S14–S16: underlying GITT analysis/raw data available; final publication plots still to be generated
- S6–S13: current progress-material versions exist, but source/provenance should be frozen
- S1–S5: collaborator-dependent

---

# 7. Current review exports

See:
\`manuscript/HEO_CURRENT_ARTIFACTS_2026-09-20.md\`

Current Main review Word:
- \`HEO_AFM_FinalDraft_ConversionCentered_2026-09-20.docx\`
- SHA256: \`a11c6af6386a944a446a8274725a33cb8ab38d636db8bcb371d3242d84a75f34\`
- 16-page rendered QA completed

Current SI review Word:
- \`HEO_Supporting_Information_V3_Final_2026-09-20.docx\`
- SHA256: \`a387a8d3c7f6a6a97971a1b0c2924186ba62936c717c18e1bbee9ce76befb75f\`
- 14-page rendered QA completed
- S17–S21 actual review figures inserted
- unresolved/pending figure sources marked explicitly

These Word files are review/export artifacts. The Markdown Main/SI files remain scientific authority. If the binary files are not available in a future runtime, regenerate them from the authoritative Markdown rather than reconstructing scientific content from memory.

---

# 8. Unresolved items before submission

## Collaborator-dependent

- exact Mg synthesis recipe
- final nominal composition / ICP-OES
- final XRD refinement / lattice parameters / phase fractions
- HRTEM/SAED re-indexing
- final XPS decision and reproducible fitting if retained

Do not include the preliminary chemically impossible CoGa₂O₄ assignment in the Ga-free material.

## Local electrochemical metadata

Confirm:
- current collector
- drying conditions
- active loading
- electrode thickness
- separator
- electrolyte volume
- glovebox conditions
- exact 1C definition
- rate sequence / cycles per rate
- instrumentation
- WonATech half-cycle label convention

## Data/source cleanup

- recover original numerical continuous first-cycle GCD/Origin source if possible;
- if recovered, regenerate final dQ/dV artwork from the numerical source;
- freeze final S6–S13 source provenance;
- generate final publication-quality S14–S16 plots;
- replace review/placeholder main figures with final publication artwork.

## Modeling

Either:
- runtime-verify \`HEO_Spatial_PhaseField_Model_Final.m\` locally in MATLAB and confirm directional unit tests,

or:
- describe only the verified Python implementation in the submission SI.

---

# 9. Decisions that must not be reversed accidentally

1. GITT rest is **60 min**, not 60 s.
2. This is an **HEO materials/mechanism paper**, not a GITT-method paper.
3. Do not center the paper on conventional apparent \(D_{\mathrm{GITT}}\).
4. Do not claim diffusion is absent; claim one varying \(D\) cannot explain all trends.
5. Do not say Mg simply accelerates diffusion.
6. Do not say BM simply accelerates transport.
7. Do not interpret apparent current-off resistance as uniquely ohmic or charge-transfer resistance.
8. Do not interpret excess-area metric as energy.
9. Do not interpret \(\phi\) as a measured phase fraction.
10. Do not map model \(\bar c\) directly to experimental \(Q/Q_{\max}\).
11. Do not assign the Figure 4 excess uniquely to spinel→rock-salt.
12. Use conversion-associated wording unless stronger direct phase evidence is added.
13. BM-Mg > Mg excess-amplitude recovery is not a robust required trend.
14. The frozen spatial model is a mechanism-sufficiency model; parameters are effective and non-unique.
15. Main Figures 3–5 are experimental/electrochemical; modeling begins in Figure 6.
16. Parameter tables and most sensitivity details stay in SI.
17. The old power-interrupted first-cycle profile must not replace the latest vector-derived profile for conversion assignment.

---

# 10. Immediate next actions

Unless new data arrive, the next useful work is **manuscript review and finalization**, not more model development.

Recommended order:

1. Review the final Main Word sentence-by-sentence against the authoritative Main Markdown.
2. Review the final SI Word and decide which pending structural/electrochemical source figures should be requested from collaborators/students.
3. Freeze final Figure 1 structural package and methods metadata.
4. Freeze final publication Figure 4a/S14–S16 using the raw GITT-derived data already available.
5. If original first-cycle numerical profile is recovered, regenerate dQ/dV; otherwise retain the vector-source boundary explicitly.
6. Decide whether XPS is retained.
7. Verify MATLAB port locally or remove any independent-MATLAB-verification implication.
8. After all metadata/artwork are frozen, make the submission-ready Main + SI export.

Do not reopen the core Figure 1→5 scientific story unless new data directly contradict it.

---

# 11. Future work kept outside this paper

Sulfide-system extension:
\`FUTURE_DIRECTION_SULFIDE_EXTENSION_2026-09-18.md\`

The separate GITT/EKF methodological project should remain separate from this HEO paper.
