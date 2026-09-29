# HEO SI v12 — Figures S7–S14 Main/SI Redundancy Audit

**Date:** 2026-09-29  
**Status:** audit complete before final SI Word assembly.  
**Main-text authority:** `manuscript/HEO_MANUSCRIPT_V16_AFM_CAPACITY_KINETICS_2026-09-28.md`  
**SI architecture authority:** `manuscript/HEO_SI_V12_ARCHITECTURE_FREEZE_2026-09-29.md`

## Audit rule

A supplementary figure is retained only if it adds a control, history dependence, raw-data context, robustness test, or mechanistic audit that is not already visible in the main figures. Exact main-panel duplication is removed whenever the same scientific role can be served without repeating the artwork.

## Figure-by-figure decision

### Figure S7 — FEC control
**Current artwork:** two stacked cycling panels: principal 10 wt% FEC four-material cycling and corresponding no-FEC cycling.

**Overlap:** the FEC cycling panel substantially overlaps the role of main Figure 3c, which already presents the principal 0.1 C cycling comparison.

**Decision:** **REBUILD.**

Final S7 should retain the no-FEC control without reproducing the main FEC cycling panel as a second full trace set. Preferred layout:
- panel (a): no-FEC cycling of the four materials;
- panel (b): compact FEC-versus-no-FEC retention/control summary (for example selected-cycle retention or endpoint comparison), rather than a second copy of the full FEC cycling curves.

Scientific boundary: use the control to establish increased interphase/cycling burden under the no-FEC condition; do not assign a unique SEI chemistry from this comparison.

### Figure S8 — rate capability
**Current artwork:** absolute capacity versus rate-cycle sequence plus normalized retention/recovery.

**Overlap:** the upper absolute-capacity panel substantially repeats main Figure 3d.

**Decision:** **REBUILD.**

Final S8 should show the **normalized rate-retention/recovery analysis only**, optionally with a compact final 0.1 C recovery summary. The absolute rate-capability curves remain in main Figure 3d.

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
| S7 | rebuild — no-FEC control + compact FEC/no-FEC summary |
| S8 | rebuild — normalized rate retention/recovery only |
| S9 | keep |
| S10 | keep |
| S11 | keep |
| S12 | keep role; recheck image duplication after main Fig. 2 freeze |
| S13 | keep |
| S14 | rebuild — four-material early current-off fit audit |

## Consequence for final SI build

Do not assemble the final SI Word yet. First complete only the three electrochemical artwork revisions:
1. revised Figure S7;
2. revised Figure S8;
3. revised Figure S14.

Figures S9–S13 can remain as current working sources, subject to publication-style cleanup. Figures S15–S23 are already frozen under the later robustness/microkinetic audit sequence.
