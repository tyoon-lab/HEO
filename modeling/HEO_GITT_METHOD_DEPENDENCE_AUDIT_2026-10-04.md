
# HEO GITT method-dependence audit — 2026-10-04

## Purpose

Resolve the apparent contradiction between Park Seonghyeon's earlier HEO GITT plot, which showed lower apparent diffusion coefficient after ball milling, the later September 2026 analysis, which showed higher first-lithiation D for BM-HEO, and the current manuscript audit, which gives D_app,BM > D_app,HEO.

The same HEO and BM-HEO raw first-lithiation GITT data were reprocessed over the same state-matched interval (pulses 12–48, approximately 200–800 mAh g^-1).

Raw protocol:
- 100 mA g^-1
- 600 s current pulse
- 3600 s rest
- HEO/BM sampling: approximately 1 s
- 65 full first-lithiation HEO pulses and 76 full BM-HEO pulses; cutoff-truncated final pulse excluded

## Historical source check

### May 2026 student analysis

`HEO_2026_05_08 (3).pptx`, slide 5:
- states that ball milling decreases the GITT-derived diffusion coefficient;
- the plotted first-lithiation HEO/BM ordering has BM-HEO below HEO over most of the normalized SOC interval;
- the slide does not document the exact equation or fitting window used for that original calculation.

Therefore the May result is a historical observation, but its exact numerical processing cannot be claimed to have been reproduced from the slide alone.

### September 2026 student analysis

`HEO 진행상황 (20260917).pptx`, slides 11–13:
- explicitly adopts the analytical equation from Ali et al., Journal of Energy Storage 132 (2025) 117628;
- uses a sqrt(t) fit in the early relaxation region ("Case 4");
- uses measured active-material sizes directly as R_s:
  - HEO 1.95 μm
  - BM-HEO 2.12 μm
  - Mg-HEO 1.93 μm
  - BM-Mg-HEO 1.99 μm;
- the resulting first-lithiation plot ranks BM-HEO above HEO.

The equation is

D_s = (4 / 9π) [ (R_s / τ) (dU / (dV/dsqrt(t))) ]^2.

For Case 4, the fit interval is 10.7–14 min from pulse start for a 10 min pulse, i.e. approximately 42–240 s after current interruption.

## Same-raw-data comparison

### Method A — pulse-region slope fit (Case 1 control)

Use the same spherical analytical equation, but fit V versus sqrt(t) from one-third of the 600 s pulse to pulse end (200–600 s), corresponding to Case 1 in Ali et al.

This is not claimed to be the exact undocumented May processing. It is a controlled pulse-region analytical reduction that reproduces the same qualitative direction as the May slide.

Over pulses 12–48:
- median D_BM / D_HEO = 0.162
- D_BM / D_HEO > 1 at only 10/37 states
- median linear-fit R^2:
  - HEO 0.614
  - BM-HEO 0.846

Thus the pulse-region slope treatment predominantly ranks BM-HEO as lower D.

### Method B — rest-region slope fit (Case 4; September method)

Use the same equation and measured R_s, but fit the relaxation from 42–240 s after current interruption.

Over pulses 12–48:
- median D_BM / D_HEO = 2.460
- D_BM / D_HEO > 1 at 37/37 states
- median linear-fit R^2:
  - HEO 0.973
  - BM-HEO 0.982

Thus changing the fitted part of the same transient reverses the HEO/BM apparent-diffusivity ordering.

### Method C — current manuscript finite-pulse relative D_app

Current manuscript definition uses

D_app proportional to m_B^2 (Delta E_s / Delta E_tau)^2

for the compositionally identical HEO/BM pair with common electrode area. Delta E_s is the relaxed voltage increment between consecutive rest endpoints and Delta E_tau is the pulse excursion from 3 s after pulse onset to pulse end.

The active-mass ratio is inferred from the nominal 100 mA g^-1 programmed current, as in the current TY10 audit.

Over pulses 12–48:
- median D_app,BM / D_app,HEO = 1.7817
- ratio >1 at 37/37 states

This exactly reproduces the existing manuscript authority.

Direct relaxation over the same matched states:
- median t63,HEO / t63,BM = 0.763
- ratio <1 at 35/37 states

Thus Method C ranks BM-HEO as larger D_app, while the direct current-off relaxation is slower.

## Main conclusion

The earlier and later Park GITT results are not contradictory raw-data sets. They arise from different analytical reductions of the same type of GITT transient.

The HEO/BM ranking is not invariant:

- pulse-region slope analysis → predominantly D_BM < D_HEO
- early-rest Case 4 analysis → D_BM > D_HEO
- finite-pulse Delta E_s / Delta E_tau analysis → D_app,BM > D_app,HEO

Therefore the manuscript should not present "BM has the larger conventional GITT diffusivity" as a processing-independent material property.

A stronger and more defensible conclusion is:

**The inferred HEO/BM diffusivity ordering itself depends on how the GITT transient is reduced.**

This is especially important because the region of interest is a conversion/phase-transformation region, where the analytical assumptions underlying a single solid-state diffusion coefficient are not expected to remain valid.

## Manuscript implication

Recommended:
- keep t63 and raw relaxation as the primary direct transient observables;
- if GITT-derived D is retained, present the processing dependence as a limitation/audit rather than one unique kinetic ranking;
- do not build the central paper claim solely on "current D_app says BM faster while t63 says BM slower," because another defensible analytical window can reverse the D ordering;
- consider moving the full D-method comparison to SI unless the manuscript is intentionally repositioned as a GITT-method paper.
