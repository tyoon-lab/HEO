# Figure 4 conversion-assignment check — 2026-09-20

## Purpose

Test whether the late-stage GITT excess-relaxation feature is localized to the same voltage region as the first-cycle cathodic conversion feature, and check whether the frozen spatial model remains directionally consistent after the interpretation is changed from a generic late-stage phase transition to conversion-associated state evolution.

## Authoritative data sources

### GITT
Raw first-lithiation GITT datasets from the 2026-09-17 HEO package:
- HEO
- BM-HEO
- Mg-HEO
- BM-Mg-HEO

Protocol:
- 600 s current pulse
- 3600 s rest
- common current-off reference: 3 s
- excess background fit windows: normalized capacity z = 0.20–0.40 and 0.90–1.00
- excess evaluated over z = 0.40–0.90.

### First-cycle voltage profile
A separate continuous first-cycle Excel export is not available for the latest four-sample comparison.

The older first-cycle dataset is not used because a power interruption produced an obvious profile artifact.

The preferred present cross-check therefore uses the latest first-cycle voltage profiles in Park Seong Hyeon's **HEO 진행상황 (20260917).pptx**, slide 10. The voltage profiles are embedded as vector artwork derived from Origin and were reconstructed at high resolution.

Reconstructed terminal first-cycle capacities:
- HEO: 901.14 mAh g^-1
- BM-HEO: 1055.84 mAh g^-1
- Mg-HEO: 731.05 mAh g^-1
- BM-Mg-HEO: 943.87 mAh g^-1

These agree with the values printed in the same slide (901.25, 1056.10, 731.15, and 944.07 mAh g^-1) to within approximately 0.03%, confirming faithful vector reconstruction.

## Preferred dQ/dV–GITT voltage comparison

A common Savitzky–Golay differentiation/smoothing procedure was applied to all four reconstructed first-cycle voltage profiles.

Using a 40 mAh g^-1 smoothing window:

| Sample | Profile-derived cathodic dQ/dV peak (V) | GITT excess peak (V) | GITT - dQ/dV (V) |
|---|---:|---:|---:|
| HEO | 0.545 | 0.527 | -0.018 |
| BM-HEO | 0.589 | 0.618 | +0.029 |
| Mg-HEO | 0.419 | 0.387 | -0.032 |
| BM-Mg-HEO | 0.485 | 0.503 | +0.018 |

All four peak pairs are localized within **32 mV** of one another.

Mean absolute difference: approximately 24 mV.

Smoothing sensitivity over 20–60 mAh g^-1:
- HEO: 0.544–0.547 V
- BM-HEO: ~0.589 V
- Mg-HEO: 0.408–0.419 V
- BM-Mg-HEO: 0.485–0.486 V

These values supersede the earlier direct digitization of the already-plotted dQ/dV curves.

## Interpretation

The voltage correspondence provides stronger evidence for a conversion-associated origin than voltage localization alone.

Safe current language:
- **conversion-associated excess relaxation** or
- **conversion/transformation-associated excess relaxation** when a broader structural label is useful.

The evidence localizes the GITT excess to the same conversion-electrochemistry window as the first-cycle cathodic feature. It does **not** uniquely identify one microscopic step.

Possible contributors remain:
- rock-salt-like intermediate evolution
- cation/oxygen rearrangement
- nucleation and growth of reduced/metallic products
- Li2O-associated conversion
- phase-boundary motion
- strain accommodation
- heterogeneous structural relaxation.

Do not claim that GITT directly measures metallic-product fraction, Li2O fraction, or one unique conversion event.

## Four-sample mechanistic implication

### HEO
Conversion-associated response is relatively concentrated and appears near ~0.53–0.55 V.

### BM-HEO
Conversion feature occurs at relatively high potential, while the GITT excess is lower and broader. This is consistent with increased accessibility and redistribution over heterogeneous local conversion environments rather than uniform acceleration of one diffusivity.

### Mg-HEO
Both the first-cycle cathodic feature and the GITT excess move to lower potential, and the excess amplitude is strongly suppressed. This supports stabilization of the oxide-derived parent/intermediate state: a larger lithiation driving force is required before conversion becomes prominent, and the accessible conversion extent is reduced.

### BM-Mg-HEO
Milling shifts the Mg-containing conversion feature back toward higher potential and partially restores/broadens the conversion-associated response, but it does not recover the concentrated Mg-free response.

## Figure 4 main-text direction

Preferred main Figure 4 is now a compact four-panel experimental figure:

1. **(a)** state-resolved 3 s-to-60 min relaxation response showing the late-stage excess feature;
2. **(b)** background-subtracted GITT excess relaxation on a voltage axis together with the independently derived first-cycle cathodic dQ/dV response for all four samples;
3. **(c)** one-to-one comparison of dQ/dV peak voltage versus GITT excess peak voltage;
4. **(d)** peak-amplitude / FWHM-like width / normalized-area map.

The four individual sample overlays remain useful as development/diagnostic plots but are no longer the preferred main-text panel architecture.

Detailed background fits, subtraction details, and smoothing/background sensitivity remain in SI.

### Submission-source boundary

The current dQ/dV panel is reconstructed from the user's own latest vector voltage-profile artwork, not from a raster image. It is appropriate for manuscript development and the present mechanistic cross-check.

Before final submission, regenerate the dQ/dV curves from the original Origin/source numerical profile if that file can be recovered. The older power-interrupted first-cycle dataset should not be substituted.

## Figure 5 frozen-v4 cross-check after conversion reassignment

The frozen spatial model was recalculated **without refitting** after the conversion-centered interpretation was adopted.

For the model, phi is interpreted as an **effective conversion-associated structural-state coordinate**, not a measured crystallographic or metallic phase fraction.

### Relaxation-peak model state

| Sample | Model c-bar at relaxation peak |
|---|---:|
| BM-HEO | 0.5860 |
| HEO | 0.6184 |
| BM-Mg-HEO | 0.7966 |
| Mg-HEO | 0.9100 |

Earlier-to-later model ordering:

**BM-HEO -> HEO -> BM-Mg-HEO -> Mg-HEO**

Experimental conversion-feature voltage ordering from higher to lower potential gives the same direction:

**BM-HEO -> HEO -> BM-Mg-HEO -> Mg-HEO**

The BM-HEO/HEO voltage separation is modest relative to the larger Mg-related shifts and should not be overinterpreted quantitatively.

### Conversion-onset robustness

Pulse-end mean-phi thresholds give:

| Mean-phi threshold | BM-HEO | HEO | BM-Mg-HEO | Mg-HEO |
|---|---:|---:|---:|---:|
| 0.02 | 0.545 | 0.606 | 0.735 | 0.834 |
| 0.05 | 0.557 | 0.619 | 0.763 | 0.859 |
| 0.10 | 0.570 | 0.620 | 0.779 | 0.889 |

The same ordering is preserved for all three onset definitions.

## Revised Figure 5 interpretation

Use:
**Reduced spatial model of conversion-associated state evolution**

Parameter meanings:
- phi: effective conversion-associated internal-state coordinate
- G_Mg: stabilization of the unconverted oxide-derived parent/intermediate state
- M_phi: effective mobility of conversion-associated structural rearrangement
- S_surf / BM distribution: local surface/defect coordinate affecting conversion onset and its heterogeneity.

The model is not a stoichiometrically complete conversion-reaction model. It does not explicitly resolve:
- Li2O formation
- metallic nanoparticle nucleation
- sequential reduction of individual transition metals
- oxygen redistribution.

## Important model boundary

Do not map model c-bar directly to experimental Q/Qmax or voltage.

The four samples have different accessible capacities, and the model state coordinate was not calibrated to an absolute experimental reaction coordinate. Agreement is therefore assessed through **directional onset/peak ordering and qualitative redistribution/suppression**, not numerical state matching.

## Current conclusion

The conversion-centered reinterpretation strengthens rather than invalidates the current HEO story:

- Figure 4 now provides an independent electrochemical localization of the excess relaxation to the conversion window.
- Figure 5 remains directionally consistent without parameter refitting.
- BM is best described as increasing accessibility and redistributing conversion.
- Mg is best described as stabilizing the oxide-derived parent/intermediate state and suppressing/shifting conversion.
- relaxation time remains a separate coordinate and should not be collapsed into one apparent diffusivity.

Completed robustness gate:
- Figure 4 background/window sensitivity audit tested 105 combinations.
- BM peak < HEO, BM width > HEO, Mg peak < HEO, and BM-Mg peak < HEO each held in 105/105 cases.
- The small nominal BM-Mg > Mg peak-amplitude difference held in 80/105 cases and is therefore treated as background-sensitive rather than a robust required trend.

Remaining gates:
1. Recover original numerical first-cycle source if possible for final dQ/dV artwork.
2. Freeze final structural/ICP/TEM metadata.
3. Runtime-check the MATLAB spatial port or describe only the verified Python implementation in the submission SI.
