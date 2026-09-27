# HEO Figure 3 Artwork Final Note — 2026-09-27

**Status:** panel logic frozen for the current manuscript round; full numerical-source reproducibility remains open and is tracked in `HEO_FIGURE3_SOURCE_PROVENANCE_AUDIT_2026-09-27.md`.

## Figure-level question

**How much electrochemical reaction is accessible in each material before any kinetic interpretation is imposed?**

Figure 3 must establish reaction extent only. It should not attempt to diagnose intrinsic conversion speed.

## Final main-panel architecture

### (a) First-cycle voltage profiles
Overlay HEO, BM-HEO, Mg-HEO, and BM-Mg-HEO on common axes.

Role:
show the directly measured first-cycle electrochemical response and the different accessible reaction extents without assigning the differences to faster or slower kinetics.

### (b) First-cycle capacity and ICE summary
Show the first- and second-half-cycle capacities for all four materials, with initial Coulombic efficiency as compact text/markers.

Current manuscript values:

| Sample | First half-cycle (mAh g^-1) | Second half-cycle (mAh g^-1) | ICE (%) |
|---|---:|---:|---:|
| HEO | 901.25 | 609.12 | 67.59 |
| BM-HEO | 1056.10 | 782.08 | 74.05 |
| Mg-HEO | 731.15 | 458.91 | 62.77 |
| BM-Mg-HEO | 944.07 | 580.83 | 61.52 |

Second-half-cycle perturbation sizes:
- HEO → BM-HEO: +28.4%
- HEO → Mg-HEO: -24.7%
- Mg-HEO → BM-Mg-HEO: +26.6%

Until the WonATech half-cycle convention is verified, retain the neutral first-/second-half-cycle terminology.

### (c) 0.1 C cycling
Plot absolute specific capacity under the common electrolyte condition.

Role:
show that the lower Mg accessibility is not only a first-cycle artifact and that BM-HEO retains the highest absolute capacity over the measured cycling window.

Keep Coulombic-efficiency evolution and the no-FEC comparison in the Supporting Information.

### (d) Absolute rate capability
Plot absolute specific capacity over the 0.1–5 C sequence and the return to 0.1 C.

Role:
separate absolute reaction accessibility from normalized retention. BM-HEO remains above HEO in absolute capacity through the rate sequence, whereas Mg-HEO can retain a larger fraction of a smaller starting capacity. This panel must not be used to infer intrinsic conversion speed from normalized retention alone.

Keep normalized rate-capacity retention in the Supporting Information.

## dQ/dV allocation

Cycle-resolved $dQ/dV$ is removed from main Figure 3.

Reason:
1. Section 2.2 is now intentionally limited to accessible reaction extent.
2. First-cycle cathodic $dQ/dV$ has a specific mechanistic role in Figure 5, where it localizes the GITT excess response to the conversion region.
3. Showing $dQ/dV$ already in Figure 3 weakens the Figure 5 question-answer sequence and duplicates evidence.

Allocation:
- first-cycle cathodic $dQ/dV$: Figure 5;
- cycle-resolved $dQ/dV$: Supporting Information.

## Figure 3 → Figure 4 transition

Figure 3 ends with:

**BM increases accessible capacity; Mg decreases it. Capacity alone does not establish intrinsic conversion speed.**

Figure 4 then asks:

**Does the higher accessible capacity after ball milling actually correspond to faster conversion-associated kinetics?**

This transition is the intended narrative hinge.

## Artwork rules

Use the Yoon Lab figure standard:
- normal font weight;
- panel labels (a)–(d), not bold;
- left/bottom ticks only;
- no redundant panel titles;
- common sample order and sample styling across all four panels;
- absolute capacities in the main figure;
- no normalized-retention panel in the main figure;
- avoid kinetic labels such as “fast” or “slow” anywhere in Figure 3.

## Remaining source/data checks before final artwork

Current source audit: `HEO_FIGURE3_SOURCE_PROVENANCE_AUDIT_2026-09-27.md`. The latest conventional electrochemistry plots are traceable to embedded Origin objects in `HEO 진행상황 (20260917).pptx`, but the independent raw cycling/rate acquisition files have not yet been recovered.

- verify the WonATech first-/second-half-cycle convention;
- freeze the exact rate sequence and number of cycles per rate;
- verify that all cycling/rate panels use the same intended electrolyte condition;
- archive the final numerical source tables or plotting script used for the publication artwork.

