# HEO consolidation audit — 2026-09-20

## Scope
Checked the 2026-09-20 discussion against the HEO GitHub repository after the AFM/conversion reinterpretation.

## Items that were missing and are now updated
1. AFM as current first target and the materials-centered positioning.
2. New authoritative Main manuscript v4 with AFM section order and conversion-centered Figure 4/5 language.
3. Review-ready conversion-aligned SI v3 with explicit background/window robustness and no-refit model-ordering validation.
4. Latest first-cycle voltage-profile reconstruction and common dQ/dV processing:
   - HEO 0.545 V;
   - BM-HEO 0.589 V;
   - Mg-HEO 0.419 V;
   - BM-Mg-HEO 0.485 V.
5. GITT excess peak comparison:
   - HEO 0.527 V;
   - BM-HEO 0.618 V;
   - Mg-HEO 0.387 V;
   - BM-Mg-HEO 0.503 V.
6. All four dQ/dV–GITT peak pairs are within 32 mV.
7. Figure 4 redesign: compact four-panel logic = state-resolved relaxation → dQ/dV/GITT voltage correspondence → peak-voltage correlation → amplitude/width/area map; detailed background/sensitivity analysis remains in SI.
8. Figure 5 reinterpretation: reduced spatial model of conversion-associated state evolution.
9. Frozen-model cross-check without refitting: BM 0.5860 < HEO 0.6184 < BM-Mg 0.7966 < Mg 0.9100.
10. Explicit claim boundary that phi is not a measured rock-salt/metal/Li2O fraction and cbar is not experimental Q/Qmax.

## Still open before submission
- Recover original numerical continuous first-cycle GCD profiles if possible. Current dQ/dV peaks are reconstructed from the user's own vector voltage-profile plots.
- Collaborator structural/compositional metadata: Mg recipe, ICP, refined XRD, HRTEM/SAED, final XPS decision.
- Local electrochemical metadata: current collector, drying, loading/thickness, separator/electrolyte volume, glovebox, 1C/rate sequence, instrumentation, WonATech half-cycle convention.
- Runtime verification of the MATLAB spatial port or removal of any claim that it was independently verified.
- Replace provisional review figures in the Word draft with final publication figures after the above items are frozen.

## Current claim boundary
The strongest supported experimental statement is that the late-stage GITT excess-relaxation feature is localized to and shifts with the first-cycle cathodic conversion feature. This supports a conversion/transformation-associated assignment but does not identify one unique elementary conversion step.

## Step 3 repository audit — completed 2026-09-20

The current-state files were cross-checked after the AFM/conversion-centered Word export.

Corrections made during the audit:
- SI v2 metadata now points to the authoritative Main v4 rather than Main v3.
- `START_HERE_CURRENT_STATE_2026-09-18.md` no longer uses the preliminary direct-digitization peak values (0.531/0.539/0.365/0.425 V) as current values.
- START_HERE immediate-next-action links now point to Main v4, SI v2, and this consolidation audit rather than the older v3/v1 files.
- START_HERE model interpretation now defines phi as an effective conversion-associated state coordinate rather than a generic transition-only variable.
- Figure 4 conversion-assignment note and Figure architecture now use the compact four-panel main-text design.
- The modeling development log now carries an explicit 2026-09-20 current-interpretation banner while preserving historical phase-transition terminology in the development history.
- The duplicate `HEO_MANUSCRIPT_V4_AFM_CONVERSION_CENTERED_2026-09-20.md` is marked superseded; the authoritative Main remains `HEO_MANUSCRIPT_V4_AFM_CONVERSION_2026-09-20.md`.
- Current review artifacts are recorded in `manuscript/HEO_CURRENT_ARTIFACTS_2026-09-20.md`.

Current review Word export:
- `HEO_AFM_FinalDraft_ConversionCentered_2026-09-20.docx`
- 16 rendered pages checked for overflow, clipping, and figure placement.
- Word is a review/export artifact; Markdown Main v4 remains the scientific text authority.

Current review figures:
- `HEO_Figure4_conversion_centered_4panel_review.png`
- `HEO_Figure5_conversion_centered_v6.png`

These binary review artifacts are not repository files at present; their names, roles, and SHA256 hashes are preserved in the artifact manifest so they can be regenerated/verified without confusing them with the authoritative Markdown state.

## SI Step 2 — completed 2026-09-20

Authoritative SI is now:
`manuscript/HEO_SUPPORTING_INFORMATION_V3_REVIEW_READY_2026-09-20.md`

Changes relative to SI v2:
- repaired the finite-window relaxation equations/notation;
- added a 105-case Figure 4 background/window sensitivity audit;
- robust directions: BM peak < HEO, BM width > HEO, Mg peak < HEO, BM-Mg peak < HEO in 105/105 cases;
- nominal BM-Mg peak > Mg is not fully robust (80/105) and is no longer a required mechanistic trend;
- retained the latest dQ/dV/GITT peak-voltage cross-check with smoothing sensitivity;
- removed the planned standalone conventional apparent-DGITT figure;
- added the frozen-model no-refit conversion-ordering validation and phi-onset-threshold table;
- renumbered the final SI figure plan to S1–S21 and tables to S1–S7;
- kept collaborator-dependent structural/compositional items explicitly open rather than inferring missing values.

