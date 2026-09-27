# HEO Figure 4 — Final Current Logic and Artwork Note

**Date:** 2026-09-27  
**Status:** current main-text Figure 4 architecture; integrated into the latest tracked Word export.

## Figure-level question

How do accessible reaction extent, relaxation magnitude, relaxation timescale, and conventional GITT apparent diffusivity relate across ball milling and Mg incorporation?

Figure 4 is designed so each panel answers a different part of that question without asking one descriptor to stand in for all kinetics.

## Panel (a): operational GITT definition

Use a representative measured HEO first-lithiation GITT step:

- 10 min galvanostatic pulse
- 60 min open-circuit rest
- common 3 s current-off reference
- define $\Delta E_{\mathrm{relax}}$ from 3 s after interruption to the 60 min rest endpoint
- define $t_{63}$ as the first time required to complete 63.2% of the observed 3 s-to-60 min relaxation

Authoritative compact source:
`modeling/HEO_FIGURE4_PANEL_A_PULSE48_COMPACT_2026-09-26.csv`

The representative trace is an operational definition only; manuscript statistics come from the full state-resolved analysis.

## Panel (b): conventional apparent diffusivity versus direct relaxation

Authoritative source:
`modeling/HEO_TY10_HEO_BM_STATE_MATCHED_RATIOS_2026-09-26.csv`

Plot:
- $D_{\mathrm{app,BM}}/D_{\mathrm{app,HEO}}$
- $t_{63,\mathrm{HEO}}/t_{63,\mathrm{BM}}$

Both are oriented so **values above 1 mean BM-HEO is faster**.

Common interval:
- 37 matched first-lithiation states
- approximately 200–800 mAh g⁻¹

Result:
- median $D_{\mathrm{app,BM}}/D_{\mathrm{app,HEO}}=1.7817$
- $D_{\mathrm{app,BM}}/D_{\mathrm{app,HEO}}>1$ at 37/37 states
- median $t_{63,\mathrm{HEO}}/t_{63,\mathrm{BM}}=0.7622$
- $t_{63,\mathrm{HEO}}/t_{63,\mathrm{BM}}<1$ at 35/37 states

Interpretation:
Conventional apparent diffusivity indicates faster BM behavior while the directly measured relaxation is predominantly slower.

## Panel (c): relaxation magnitude–timescale map

Plot median $\Delta E_{\mathrm{relax}}$ versus median $t_{63}$ over the common 200–800 mAh g⁻¹ interval.

| Sample | Median $\Delta E_{\mathrm{relax}}$ (mV) | Median $t_{63}$ (min) |
|---|---:|---:|
| HEO | 160.9 | 8.68 |
| BM-HEO | 176.3 | 11.57 |
| Mg-HEO | 109.5 | 11.01 |
| BM-Mg-HEO | 144.3 | 12.99 |

Primary use:
HEO → Mg-HEO shows that the relaxation voltage-change magnitude becomes smaller even though relaxation becomes slower.

This is the Mg complementary constraint. It is **not** a second capacity–rate contradiction.

## Panel (d): accessible capacity–timescale map

Use the neutral first-cycle second-half capacities until the WonATech half-cycle convention is finally frozen.

| Sample | First-cycle second-half capacity (mAh g⁻¹) | Median $t_{63}$ (min) |
|---|---:|---:|
| HEO | 609.12 | 8.68 |
| BM-HEO | 782.08 | 11.57 |
| Mg-HEO | 458.91 | 11.01 |
| BM-Mg-HEO | 580.83 | 12.99 |

Primary use:
HEO → BM-HEO directly shows the paper-creating contradiction: accessible capacity rises while relaxation becomes slower.

Directional arrows may be used as visual guides for material modifications. They are not regression lines.

## Current caption

**Figure 4. GITT reveals distinct mismatches among accessible reaction extent, relaxation magnitude, relaxation timescale, and conventional apparent diffusivity.** (a) Representative first-lithiation GITT step consisting of a 10 min galvanostatic pulse followed by a 60 min open-circuit rest, defining the 3 s-to-60 min relaxation voltage change, $\Delta E_{\mathrm{relax}}$, and the model-free relaxation timescale, $t_{63}$. (b) State-matched HEO/BM-HEO comparison of $D_{\mathrm{app,BM}}/D_{\mathrm{app,HEO}}$ and the direct relaxation-rate ratio $t_{63,\mathrm{HEO}}/t_{63,\mathrm{BM}}$. Both ratios are oriented so that values above unity indicate faster BM-HEO. The $D_{\mathrm{app}}$ ratio remains above unity at all 37 matched states, whereas the direct relaxation-rate ratio is below unity at 35 of 37 states. (c) Median $\Delta E_{\mathrm{relax}}$ versus median $t_{63}$ over the common 200–800 mAh g⁻¹ interval for all four materials. Mg incorporation decreases the relaxation voltage change while lengthening $t_{63}$. (d) First-cycle second-half capacity versus median $t_{63}$. Ball milling increases accessible capacity while lengthening $t_{63}$, whereas Mg incorporation decreases accessible capacity while $t_{63}$ increases. Arrows indicate the corresponding material modifications.

## Main-text interpretation lock

- BM = capacity ↑, $t_{63}$ ↑ → primary capacity–kinetics contradiction.
- Mg = capacity ↓, $t_{63}$ ↑ → directionally consistent with slower kinetics; simultaneously $\Delta E_{\mathrm{relax}}$ ↓ → magnitude–timescale mismatch.
- Conventional $D_{\mathrm{app}}$ = conflicting BM indication relative to direct relaxation.
- Do not infer that $\Delta E_{\mathrm{relax}}$ itself is a kinetic rate.
- Do not state that diffusion is absent or GITT is invalid.

## Main versus SI treatment of Mg apparent diffusivity

The main Figure 4(b) remains HEO/BM-HEO because the pair is compositionally identical and therefore provides the cleanest test of whether conventional $D_{\mathrm{app}}$ preserves the direct fast–slow ordering.

A preliminary HEO/Mg-HEO cross-composition calculation also gave a conflicting apparent-$D$ indication, but composition-dependent molar-mass/molar-volume prefactors enter that comparison. It is therefore a robustness/SI candidate rather than part of the decisive main panel.

## Reproducible artwork

Plotting authority:
`modeling/heo_figure4_capacity_kinetics_mismatch.py`

The script should generate:
- (a) measured GITT definition
- (b) HEO/BM $D_{\mathrm{app}}$ versus direct relaxation-rate ratio
- (c) $\Delta E_{\mathrm{relax}}$–$t_{63}$ map
- (d) first-cycle second-half capacity–$t_{63}$ map

Figure style follows the Yoon Lab publication standard: sans serif, normal-weight axes, left/bottom ticks only, compact legends, no redundant panel titles, and scientific meaning rather than decoration encoded by symbols/lines.
