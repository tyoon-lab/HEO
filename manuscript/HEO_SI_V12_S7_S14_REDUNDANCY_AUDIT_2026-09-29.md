# HEO SI v12 — Figures S7–S14 Main/SI Redundancy Audit

**Date:** 2026-09-29  
**Status:** audit complete before final SI Word assembly.  
**Main-text authority:** `manuscript/HEO_MANUSCRIPT_V16_AFM_CAPACITY_KINETICS_2026-09-28.md`  
**SI architecture authority:** `manuscript/HEO_SI_V12_ARCHITECTURE_FREEZE_2026-09-29.md`

## Audit rule

A supplementary figure is retained only if it adds a control, history dependence, raw-data context, robustness test, or mechanistic audit that is not already visible in the main figures. Exact main-panel duplication is removed whenever the same scientific role can be served without repeating the artwork.

## Figure-by-figure decision

### Figure S7 — no-FEC cycling control
**Final artwork:** no-FEC 0.1 C cycling of HEO, BM-HEO, Mg-HEO, and BM-Mg-HEO only.

**Overlap:** removed. The FEC-containing full cycling comparison remains in main Figure 3c and is not repeated in the SI.

**Decision:** **FROZEN.**

Final role:
- Figure S7 contains only the no-FEC control trace set;
- the main-text FEC cycling panel provides the corresponding principal condition;
- no approximate digitized FEC/no-FEC summary is introduced because the original numerical control export is not independently frozen.

Scientific boundary: use the control to show the stronger cycling/interphase burden without FEC, especially for BM-HEO, but do not assign a unique SEI chemistry from this comparison.

Final artwork:
- `Figure_S7_no_FEC_cycling_control_final.png`

### Figure S8 — rate capability
**Current artwork:** final SI artwork now retains only normalized capacity retention/recovery across the rate sequence.

**Overlap:** the upper absolute-capacity panel substantially repeats main Figure 3d.

**Decision:** **FROZEN.**

Final S8 shows the **normalized rate-retention/recovery analysis only**. The absolute rate-capability curves remain exclusively in main Figure 3d.

### Figure S9 — cycles 1–3 voltage profiles
**Current artwork:** cycles 1, 2, and 3 for all four materials.

**Overlap:** main Figure 3a contains only the compact first-cycle comparison.

**Decision:** **KEEP, minor style cleanup only.**

The first-cycle trace is retained as the baseline needed to visualize cycle-to-cycle evolution; the figure adds cycles 2–3 and therefore has a distinct SI role.

### Figure S10 — cycle-resolved dQ/dV evolution
**Current artwork:** selected dQ/dV curves from cycle 1 through extended cycling for all four materials.

**Overlap:** main Figure 5 uses only the first-cycle conversion-region localization.

**Decision:** **KEEP.**

S10 adds long-term electrochemical evolution and is not a duplicate. Final artwork should retain a limited, readable selected-cycle set and consistent labeling.

### Figure S11 — relative interfacial-capacitance audit
**Current artwork:** non-faradaic-window CVs at multiple scan rates plus scan-rate regressions.

**Overlap:** none. Main Figure 2 intentionally excludes electrochemically derived interface metrics.

**Decision:** **KEEP.**

Interpret only as a **relative interfacial-accessibility / capacitance comparison**. Do not present the historical 40 μF cm⁻² conversion as an independently validated absolute electrochemical area.

### Figure S12 — post-cycle SEM
**Current artwork:** pristine and 100-cycle HEO/BM-HEO SEM comparisons at two magnifications.

**Overlap:** potential overlap with pristine SEM panels in main Figure 2, depending on the final collaborator-selected fields.

**Decision:** **KEEP THE ROLE, RECHECK THE PRISTINE PANELS AFTER MAIN FIGURE 2 IS FROZEN.**

Preferred final implementation:
- use additional pristine fields not identical to main Figure 2 when available; or
- if no distinct pristine fields exist, show post-cycle images as the SI artwork and reference the main-text pristine morphology.

The before/after comparison is scientifically useful, but exact image duplication should be avoided if possible.

### Figure S13 — full multi-cycle GITT traces
**Current artwork:** full GITT histories for HEO/BM-HEO and Mg-HEO/BM-Mg-HEO.

**Overlap:** none. Main Figure 4a shows only one representative pulse/rest definition, and Figures 4–5 use derived descriptors rather than the full raw history.

**Decision:** **KEEP.**

This is the appropriate raw-data/context figure supporting the GITT analysis.

### Figure S14 — early current-off E–sqrt(t) fit
**Current artwork:** one representative HEO short-time fit.

**Overlap:** none, but the current single-sample panel is incomplete relative to the four-sample Roff,app summary.

**Decision:** **REBUILD.**

Final S14 should show a compact four-material representative audit, preferably at a comparable normalized first-lithiation state, using the same 3–30 s fitting window. The purpose is to demonstrate the quality and operational definition of the early current-off fit across all four materials, not to assign the slope/intercept to one unique physical resistance.

## Frozen disposition after audit

| Figure | Final status |
|---|---|
| S7 | frozen — no-FEC cycling control only; FEC counterpart remains in main Fig. 3c |
| S8 | rebuild — normalized rate retention/recovery only |
| S9 | keep |
| S10 | keep |
| S11 | keep |
| S12 | keep role; recheck image duplication after main Fig. 2 freeze |
| S13 | keep |
| S14 | rebuild — four-material early current-off fit audit |

## Consequence for final SI build

Do not assemble the final SI Word yet. Figure S7 is now frozen. Complete only the remaining two electrochemical artwork revisions:
1. revised Figure S8;
2. revised Figure S14.

Figures S9–S13 can remain as current working sources, subject to publication-style cleanup. Figures S15–S23 are already frozen under the later robustness/microkinetic audit sequence.
