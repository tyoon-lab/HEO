# HEO — Current State, 2026-09-26

## Authoritative manuscript state

- Main: `manuscript/HEO_MANUSCRIPT_V9_AFM_CAPACITY_KINETICS_2026-09-26.md`
- SI: `manuscript/HEO_SUPPORTING_INFORMATION_V8_CAPACITY_KINETICS_2026-09-26.md`
- Figure logic: `manuscript/HEO_FIGURES_3_7_CURRENT_LOGIC_V3_2026-09-26.md`
- TY10 audit: `modeling/HEO_TY10_CONVENTIONAL_GITT_AUDIT_2026-09-26.md`
- TY10 compact data: `modeling/HEO_TY10_HEO_BM_STATE_MATCHED_RATIOS_2026-09-26.csv`
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

Abstract wording remains under PI review and was intentionally not frozen by the TY10 update.

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

**Ball milling reveals that higher accessible capacity can coexist with slower relaxation, while conventional GITT analysis gives the opposite kinetic ranking.**

Bounded mechanistic statement:

**Microkinetic analysis shows that this behavior can arise naturally from the multistep character of conversion.**

Manuscript hierarchy:
- BM contradiction = scientific event that creates the paper.
- Mg = complementary constraint, not a coequal headline contradiction.
- conventional $D_{\mathrm{app}}$ inversion = independent kinetic-ranking test.
- Figure 5 conversion localization + Figure 6 history dependence = experimental constraints.
- Figure 7 = existence proof / mechanistic consistency, not unique mechanism identification.
