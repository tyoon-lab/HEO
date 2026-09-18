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

## Preferred final layout — refined against frozen v4

The previous prototype snapshot table is obsolete for final figure construction because its state/timing definition was not fully aligned with the frozen v4 implementation.

The final visualization should explicitly use the **end of the 600 s galvanostatic pulse**, immediately before the 60 min current-off relaxation. This provides a physically direct starting state for the experimentally analyzed GITT relaxation.

Use circular radial-state maps.

Rows:
1. HEO
2. BM-HEO
3. Mg-HEO
4. BM-Mg-HEO

Recommended displayed model mean-lithiation states, rounded from the frozen-v4 GITT state grid:
- 0.55
- 0.62
- 0.68
- 0.75
- 0.80
- 0.86
- 0.91

Color = phi.

For HEO and Mg-HEO, each map is the radial state of the single frozen parameter set.

For BM-HEO and BM-Mg-HEO, each map must be described as the **ensemble-averaged radial phi state** over the frozen 11-quantile distribution. It is not a directly simulated heterogeneous two-dimensional single particle.

Do not add random angular domains or patches unless a genuine 2D/3D heterogeneous model is later implemented.

### Frozen-v4 pulse-end phi-bar audit

The following values were regenerated from the frozen spatial equations and parameters for figure construction. Values are approximate and are intended for numerical auditing of the visualization, not as experimentally measured phase fractions.

| Sample | c-bar ~0.55 | ~0.62 | ~0.68 | ~0.75 | ~0.80 | ~0.86 | ~0.91 |
|---|---:|---:|---:|---:|---:|---:|---:|
| HEO | 0.000 | 0.042 | 0.633 | 0.790 | 0.935 | ~1.000 | ~1.000 |
| BM-HEO | 0.036 | 0.481 | 0.639 | 0.795 | 0.937 | ~1.000 | ~1.000 |
| Mg-HEO | 0.000 | 0.000 | 0.000 | 0.000 | ~0.000 | 0.054 | 0.150 |
| BM-Mg-HEO | 0.000 | 0.000 | 0.002 | 0.030 | 0.211 | 0.626 | 0.781 |

The important message is the ordering and evolution, not the exact decimal values.

### Rest-period structural-evolution panel

Pair the snapshot array with a second panel showing

Delta phi-bar_rest = phi-bar_(60 min rest end) - phi-bar_(pulse end)

as a function of model mean lithiation state.

This panel provides a direct model-side visualization of how much structural evolution occurs during the same 60 min interval used for the experimental current-off relaxation analysis.

Do not interpret Delta phi-bar_rest as numerically equal to the measured voltage relaxation. It is an internal-state descriptor that links the model dynamics to the GITT relaxation window.

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

## Refinement: Figure 5 should be an independent model-visualization figure

The current preferred manuscript architecture is now:
- Figure 4: experimental state-localized transition-associated polarization;
- Figure 5: spatial-model visualization of internal-state evolution consistent with the experimental directional constraints.

This separation preserves the distinction between experimental evidence and mechanism-sufficiency modeling.

### Important ensemble-visualization caveat

For HEO and Mg-HEO, the frozen spatial model uses a single radial parameter set.

For BM-HEO and BM-Mg-HEO, the frozen model uses an 11-quantile ensemble distribution of local transition/surface conditions and structural mobilities. Therefore a circular map for BM-containing samples must not be described as a directly simulated heterogeneous two-dimensional single particle.

Preferred options:
1. show an ensemble-averaged radial phi map and label it explicitly as an ensemble-averaged model state; or
2. show representative quantile particles when the distribution itself is the intended visual message.

For the compact 4 × 7 main-text array, option 1 is preferred. The caption should state that each circle represents the ensemble-averaged radial structural state at the selected model reaction-progress coordinate.

Do not add random angular patches to the circles unless a true 2D/3D heterogeneous model is later implemented.

### Column coordinate

Retain the model mean lithiation/reaction-progress coordinate rather than relabeling it directly as experimental normalized capacity. A direct capacity mapping would imply a quantitative model-to-experiment calibration that has not been established.

Recommended column title:
**Model mean lithiation state, c̄**

Add a small header:
**Late-stage transition window**

### Recommended Figure 5 panels

**Figure 5a.** Compact model schematic defining conserved Li state c(r,t), structural order parameter phi(r,t), Mg stabilization coordinate, and BM ensemble heterogeneity.

**Figure 5b.** 4 × 7 circular array of ensemble-averaged radial phi states at c̄ = 0.55, 0.62, 0.68, 0.74, 0.80, 0.86, and 0.92.

**Figure 5c.** Ensemble-averaged phi-bar versus c̄ for the four samples. This plot makes the BM broad/early progression, Mg suppression, and partial reopening in BM-Mg explicit.

Optional Figure 5d only if space allows: directional comparison of model outputs against the experimentally required trends. Avoid presenting this as a quantitative fit.

### Figure-level message

Figure 4 establishes the experimental contradiction to a one-parameter diffusion interpretation. Figure 5 then demonstrates that the observed directions are physically compatible with independent coordinates for transformation extent/stabilization and structural-mobility/transition-condition heterogeneity.

The model should be described as a mechanism-sufficiency visualization, not as a reconstruction of a uniquely identified microscopic pathway.
