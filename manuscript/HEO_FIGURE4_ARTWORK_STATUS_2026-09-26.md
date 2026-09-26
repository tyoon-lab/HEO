# HEO Figure 4 Artwork Status — 2026-09-26

**Role:** decisive experimental Figure for the capacity–kinetics manuscript.

## Current panel architecture

### (a) GITT pulse/rest definition

Current production script uses a schematic trace only to define:
- 10 min galvanostatic pulse;
- 60 min open-circuit rest;
- common 3 s reference;
- $\Delta E_{\rm relax}$;
- model-free $t_{63}$.

**Before submission:** replace the schematic with one raw representative GITT pulse/rest trace from the authoritative HEO dataset if the source trace is recovered. The definitions and panel role should not change.

### (b) State-matched kinetic-ranking inversion

Uses `HEO_TY10_HEO_BM_STATE_MATCHED_RATIOS_2026-09-26.csv`.

Both quantities are oriented so that values above unity rank BM-HEO as faster:
- conventional $D_{\rm app,BM}/D_{\rm app,HEO}$;
- direct relaxation-rate ratio $t_{63,\rm HEO}/t_{63,\rm BM}$.

Current result:
- median apparent-diffusivity ratio = 1.78;
- 37/37 points above unity;
- median direct relaxation-rate ratio = 0.762;
- 35/37 points below unity.

This is the decisive panel.

### (c) Four-sample median $t_{63}$

Pairs unmilled and ball-milled materials:
- HEO 8.68 min → BM-HEO 11.57 min;
- Mg-HEO 11.01 min → BM-Mg-HEO 12.99 min.

Panel purpose: show that milling lengthens the direct relaxation timescale in both composition pairs.

### (d) Accessible capacity versus median $t_{63}$

First-cycle reversible capacities:
- HEO 609.12 mAh g−1;
- BM-HEO 782.08 mAh g−1;
- Mg-HEO 458.91 mAh g−1;
- BM-Mg-HEO 580.83 mAh g−1.

Panel purpose: make the experimental contradiction visible without inferring kinetics from capacity itself. In both composition pairs, milling moves the electrode toward higher accessible capacity and longer $t_{63}$.

## Remaining pre-submission gate

The HEO/BM relative conventional-$D_{\rm app}$ comparison currently assumes the same geometric electrode area. Final electrode geometry and recorded active masses must be verified before the 37/37 ranking statement is frozen for submission.

## Production files

- `modeling/plot_heo_figure4_capacity_kinetics.py`
- `modeling/HEO_TY10_HEO_BM_STATE_MATCHED_RATIOS_2026-09-26.csv`
- `modeling/HEO_FIGURE4_SUMMARY_DATA_2026-09-26.csv`

The scientific architecture is locked; styling and the raw-trace replacement in panel (a) can proceed without changing the Figure-level conclusion.
