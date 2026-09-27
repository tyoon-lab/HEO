# HEO/Mg-HEO Conventional GITT Cross-Composition Check

**Date:** 2026-09-27  
**Role:** manuscript-development robustness check; **not** the decisive main-text apparent-diffusivity comparison.

## Why this check was done

After the Figure 4 and abstract review, the Mg result was clarified as follows:

- Mg-HEO has lower accessible capacity than HEO.
- Mg-HEO also has a longer $t_{63}$, so the capacity decrease and slower relaxation are directionally consistent.
- The unusual Mg constraint is that the relaxation voltage-change magnitude decreases at the same time.

The question was then whether conventional GITT-derived apparent diffusivity also reproduces the direct HEO/Mg relaxation ordering.

## Composition information recovered

Historical ICP mole ratios for the HEO3 set, normalized to Ni = 1:

| Sample | Ni | Co | Mn | Fe | Cr | Mg |
|---|---:|---:|---:|---:|---:|---:|
| HEO3 | 1.00 | 1.02 | 1.03 | 1.00 | 1.27 | – |
| BM-HEO3 | 1.00 | 1.01 | 1.07 | 1.00 | 1.02 | – |
| Mg-HEO3 | 1.00 | 1.01 | 1.01 | 0.990 | 0.994 | 1.10 |
| BM-Mg-HEO3 | 1.00 | 1.00 | 1.02 | 1.01 | 1.01 | 1.07 |

Source recovered from the older HEO composition slide deck:
`241010_HEO for battery_유태경 (2).pptx`.

Interpretation boundary:
Mg-HEO3 should not be described as a trace-Mg-doped material based on this ICP table. Mg is approximately equimolar with the other principal cations. The final synthesis description still requires collaborator confirmation of nominal composition and precursor amounts.

## Preliminary cross-composition result

Using the same conventional finite-pulse GITT structure as the HEO/BM audit, with common geometric electrode area and composition-dependent prefactors included, the development check gave approximately:

- median $D_{\mathrm{app,Mg}}/D_{\mathrm{app,HEO}} \approx 13.36$
- $D_{\mathrm{app,Mg}}/D_{\mathrm{app,HEO}}>1$ at 36/37 matched states
- median direct relaxation-rate ratio $t_{63,\mathrm{HEO}}/t_{63,\mathrm{Mg}} \approx 0.772$
- direct relaxation-rate ratio <1 at 36/37 matched states

A nominal-equimolar composition treatment gave a nearly identical median apparent-$D$ ratio (~13.27), so the direction was insensitive to that specific composition choice in the development check.

Thus the conventional apparent diffusivity also points toward faster Mg-HEO behavior, whereas the directly measured relaxation is slower.

## Why this is not in main Figure 4(b)

The HEO/BM-HEO pair is compositionally identical. Its relative apparent-$D$ comparison is therefore much cleaner because composition-dependent molar-mass/molar-volume factors cancel.

HEO/Mg-HEO is a cross-composition comparison. Even though the development result is strongly directional, the result depends on:
- final composition definition;
- molar-mass/molar-volume or density treatment;
- active-mass metadata;
- final confirmation that the common geometric electrode area applies to the exact cells used.

Therefore:

**Main Figure 4(b) remains HEO/BM-HEO only.**

The Mg cross-composition result is retained as a robustness/SI candidate and should be promoted only after the prefactor calculation is frozen in a fully reproducible audit.

## Claim boundary

This check does not prove that diffusion is absent and does not establish a unique Mg mechanism. It only suggests that the mismatch between conventional apparent diffusivity and direct current-off relaxation is not unique to the milling perturbation.

## Next action if promoted to SI

Before publication use:
1. recover/freeze exact active masses for the HEO and Mg-HEO GITT cells;
2. freeze final nominal and ICP compositions;
3. freeze the molar-volume/density treatment;
4. commit a state-by-state HEO/Mg CSV analogous to `HEO_TY10_HEO_BM_STATE_MATCHED_RATIOS_2026-09-26.csv`;
5. rerun the calculation from raw workbooks and document the exact prefactor.
