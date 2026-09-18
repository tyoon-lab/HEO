# HEO Visual Simulation — Main-Figure Direction

**Date:** 2026-09-18
**Status:** Current preferred manuscript visualization direction.

## Decision

The model parameter table alone is not considered sufficient manuscript originality because the logic can become circular:
GITT shape -> hypothesized mechanism -> chosen equations -> extracted effective values.

Therefore:
- parameter tables and most fitting/sensitivity details belong mainly in SI;
- the main-text modeling value should be the visual transformation from GITT interpretation to an internal-state simulation.

## Physical variable visualized

The spatial model uses a radial structural order parameter phi(r).

Interpretation:
- phi ≈ 0: parent-like / pre-transition state
- phi ≈ 1: transformed-like state
- intermediate phi: local/coarse-grained partial transformation

Important: phi is not a directly measured phase fraction.

The current one-phi model represents the late-stage transition-associated transformation only. It does not claim to describe every earlier structural transition throughout lithiation.

## Why the visualization window is truncated

Earlier-stage structural transitions may exist and are not explicitly included in the present one-phi model.

Therefore the visualization should not start from model state 0 and imply complete reaction-history coverage.

The current visualization begins at approximately model mean lithiation state 0.55. This state was deliberately included so all four samples appear to start from a comparable low-transformation condition.

## Preferred final layout

Use circular particle cross sections.

Rows:
1. HEO
2. BM-HEO
3. Mg-HEO
4. BM-Mg-HEO

Columns / common target states:
- 0.55
- 0.62
- 0.68
- 0.74
- 0.80
- 0.86
- 0.92

Color = phi.

The circles are model visualizations of the radial state profile at selected reaction-progress states, not independent experimentally imaged particles.

## Current prototype matched states

| Sample | target | matched state | modeled phi_bar |
|---|---:|---:|---:|
| HEO | 0.55 | 0.532 | 0.000 |
| HEO | 0.62 | 0.604 | 0.023 |
| HEO | 0.68 | 0.676 | 0.643 |
| HEO | 0.74 | 0.748 | 0.837 |
| HEO | 0.80 | 0.784 | 0.953 |
| HEO | 0.86 | 0.856 | ~1.000 |
| HEO | 0.92 | 0.892 | ~1.000 |
| BM-HEO | 0.55 | 0.568 | 0.209 |
| BM-HEO | 0.62 | 0.604 | 0.454 |
| BM-HEO | 0.68 | 0.676 | 0.647 |
| BM-HEO | 0.74 | 0.748 | 0.841 |
| BM-HEO | 0.80 | 0.784 | 0.944 |
| BM-HEO | 0.86 | 0.856 | ~1.000 |
| BM-HEO | 0.92 | 0.892 | ~1.000 |
| Mg-HEO | 0.55 | 0.532 | 0.000 |
| Mg-HEO | 0.62 | 0.604 | 0.000 |
| Mg-HEO | 0.68 | 0.676 | 0.000 |
| Mg-HEO | 0.74 | 0.748 | 0.000 |
| Mg-HEO | 0.80 | 0.784 | 0.0004 |
| Mg-HEO | 0.86 | 0.856 | 0.063 |
| Mg-HEO | 0.92 | 0.892 | 0.128 |
| BM-Mg-HEO | 0.55 | 0.568 | 0.000 |
| BM-Mg-HEO | 0.62 | 0.604 | 0.000 |
| BM-Mg-HEO | 0.68 | 0.676 | 0.003 |
| BM-Mg-HEO | 0.74 | 0.748 | 0.042 |
| BM-Mg-HEO | 0.80 | 0.784 | 0.132 |
| BM-Mg-HEO | 0.86 | 0.856 | 0.542 |
| BM-Mg-HEO | 0.92 | 0.892 | 0.681 |

These are model outputs, not experimentally measured phase fractions.

## Visual message

HEO: concentrated, rapid development of the late-stage transformed state.

BM-HEO: transformation begins earlier / is distributed more broadly in reaction progress.

Mg-HEO: late-stage transformation is strongly suppressed over most of the window.

BM-Mg-HEO: ball milling partially reopens transformation accessibility, but Mg-related suppression/stabilization remains.

## Safe manuscript wording

> The circular snapshots visualize the modeled late-stage transition-associated state variable phi within a spherical particle across a common reaction-progress window. The visualization is intended as a mechanistic representation of the GITT-derived interpretation and should not be interpreted as a directly measured phase fraction or as a complete reconstruction of all structural transitions throughout lithiation.

## Next visual-development tasks

1. Publication-style cleanup of the 4 × 7 array.
2. Decide whether the column coordinate remains modeled mean lithiation state or is carefully mapped to normalized/experimental capacity.
3. Add a small legend: 0 = parent-like; 1 = transformed-like.
4. Consider pairing the snapshot array with the experimental transition-hump plot so the chain is explicit: GITT observable -> inferred transition window -> modeled internal-state evolution.
5. Keep detailed model parameters, sensitivity, and identifiability caveats in SI.