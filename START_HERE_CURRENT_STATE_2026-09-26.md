# HEO — Current State, 2026-09-26

## Authoritative manuscript state

- Main: `manuscript/HEO_MANUSCRIPT_V10_AFM_CAPACITY_KINETICS_2026-09-26.md`
- SI: `manuscript/HEO_SUPPORTING_INFORMATION_V9_CAPACITY_KINETICS_2026-09-26.md`
- Figure logic: `manuscript/HEO_FIGURES_3_7_CURRENT_LOGIC_V4_2026-09-26.md`
- TY10 audit: `modeling/HEO_TY10_CONVENTIONAL_GITT_AUDIT_2026-09-26.md`
- TY10 compact data: `modeling/HEO_TY10_HEO_BM_STATE_MATCHED_RATIOS_2026-09-26.csv`
- Microkinetic authority: `modeling/HEO_CONVERSION_MICROKINETICS_LITERATURE_INFORMED_2026-09-26.md`
- Mg-like directional audit: `modeling/HEO_MG_LIKE_MICROKINETIC_DIRECTIONAL_TEST_2026-09-26.md`
- Literature audit: `references/HEO_CONVERSION_GITT_LITERATURE_AUDIT_2026-09-26.md`
- Story lock: `manuscript/HEO_MANUSCRIPT_ARCHITECTURE_TOOLKIT_LOCK_2026-09-26.md`

## New result added on 2026-09-26

Raw GITT reanalysis of the compositionally identical HEO/BM-HEO pair shows that conventional apparent diffusivity and direct current-off relaxation give opposite kinetic rankings over the common 200–800 mAh g⁻¹ interval.

- median $D_{\mathrm{app,BM}}/D_{\mathrm{app,HEO}} = 1.78$
- conventional $D_{\mathrm{app}}$ ratio > 1 at 37/37 matched states
- median direct relaxation-rate ratio $t_{63,\mathrm{HEO}}/t_{63,\mathrm{BM}} = 0.762$
- direct relaxation-rate ratio < 1 at 35/37 states

Main interpretation: conventional apparent $D$ does not preserve the fast–slow ordering of the full conversion-associated relaxation. This does **not** show that diffusion is absent.

## Figure 4 revision

Current intended Figure 4:
- (a) GITT pulse/rest definition
- (b) relative conventional $D_{\mathrm{app}}$ versus direct relaxation-rate ratio for HEO/BM-HEO
- (c) median $t_{63}$ across four samples
- (d) first-cycle reversible capacity versus median $t_{63}$

The previous main-panel relaxation-magnitude bar is demoted to SI/supporting analysis.

## Abstract

The current v10 abstract includes the TY10 ranking inversion and states the BM result as higher accessible capacity with slower conversion-associated kinetics. Mg remains a complementary constraint. Final stylistic wording remains under PI review.

## Unresolved submission inputs

The prior unresolved collaborator/cell-metadata list remains active, especially:
- final Figure 1–2 Yoo-group structural/compositional package;
- Mg synthesis/composition;
- current collector, drying, loading, thickness, separator, electrolyte volume, glovebox metadata;
- exact electrode area/recorded masses for any final absolute $D_{\mathrm{GITT}}$ reporting.

Absolute $D$ is not required for the present scientific claim.


## Literature-positioning update

The current manuscript now explicitly distinguishes two facts:

1. Conventional GITT-derived apparent diffusion coefficients are commonly used as kinetic comparators in HEO/conversion-anode literature.
2. In the present HEO/BM-HEO pair, conventional $D_{\mathrm{app}}$ and direct current-off relaxation give opposite kinetic rankings.

Current bounded general statement:

**Conversion kinetics cannot, in general, be ranked by apparent GITT diffusivity alone.**

Do not broaden this to "GITT is invalid" or "diffusion is absent."


## Toolkit-aligned story lock

Primary experimental statement:

**Ball milling reveals that higher accessible capacity can coexist with slower conversion-associated kinetics, while conventional GITT analysis gives the opposite kinetic ranking.**

Bounded mechanistic statement:

**Microkinetic analysis shows that this behavior can arise naturally from the multistep character of conversion.**

Manuscript hierarchy:
- BM contradiction = scientific event that creates the paper.
- Mg = complementary constraint, not a coequal headline contradiction.
- conventional $D_{\mathrm{app}}$ inversion = independent kinetic-ranking test.
- Figure 5 conversion localization + Figure 6 history dependence = experimental constraints.
- Figure 7 = existence proof / mechanistic consistency, not unique mechanism identification.


## Decisions added after TY10

### EIS

Cycling EIS is excluded from the manuscript evidence chain. The available early-cycle spectra contain state-matching/outlier limitations and are not needed to support the central claim. The primary kinetic evidence remains GITT/current-off analysis together with dQ/dV localization.

### Mg-like microkinetic closure

A secondary directional calculation confirms that the experimentally observed Mg combination is physically admissible within the same multistep conversion network:

- lower cutoff-limited capacity;
- lower relaxation amplitude;
- longer effective $t_{63}$.

One illustrative, non-fitted case gives $Q_{\rm cutoff}$ 0.55845 → 0.39339, relaxation amplitude 33.02 → 28.64 mV, and $t_{63}$ 13.78 → 16.78 min. The matched-state calculation is now reproduced directly by `modeling/heo_capacity_relaxation_heterogeneous_validation.py` at common normalized passed charge $\Delta Q=0.30$.

These values supersede the earlier provisional Mg-like table; the directional result is unchanged. This test is retained in the SI/model audit. Main Figure 7 remains focused on the primary BM contradiction and the homogeneous-control / heterogeneous-accessibility existence proof.
