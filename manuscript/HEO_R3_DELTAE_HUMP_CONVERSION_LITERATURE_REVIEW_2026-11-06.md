# R3 ΔE_rest hump — non-HEO conversion literature assessment (2026-11-06)

**Status:** Evidence audit and recommended text; no modifications to v38 main manuscript or approved kinetic boundaries.

## What v38 actually states

R3 pulse-index series: pristine HEO ΔE_rest about 145 mV (R3 onset) → maximum 189 mV (near pulse 50) → decrease; Mg-HEO about 109→118 mV (weak +9 mV hump); both BM-HEO and BM-Mg-HEO show declining amplitude, lacking an interior R3 local maximum. R3 t63 increases in all four materials. ΔE_rest is the **finite-window voltage recovery amplitude between 3 seconds and the 3600-second rest endpoint**; hump means a peak *across successive pulse states*, not an overshoot inside one individual rest trace.

## Ranked external references

1. **L. Li et al., J. Am. Chem. Soc. 2016, 138, 2838–2848**, *Origins of Large Voltage Hysteresis in High-Energy-Density Metal Fluoride Lithium-Ion Battery Conversion Electrodes*, DOI: **10.1021/jacs.6b00061**, https://pubs.acs.org/doi/10.1021/jacs.6b00061. **Most directly comparable.** Fig. 4c displays *four-hour GITT voltage relaxation magnitude versus lithiation state*, contrasting FeF3 nanowires and microwires. Larger recovery in MWs is associated with heterogeneous progression of FeF3 → FeF2/LiF → Fe/LiF, where outer regions advance further than unreacted centers. Microstructure changes relaxation amplitude; spatial heterogeneity supplies a concrete testable physical mechanism. Does **not** establish the same-shaped hump or prove HEO-specific intermediate.
2. **K. W. Knehr et al., Electrochimica Acta 2017, 238, 384–396**, *Simulations of Lithium-Magnetite Electrodes Incorporating Phase Change*, DOI **10.1016/j.electacta.2017.04.041**. Reaction/phase-change kinetic model explains slow voltage recovery in Fe3O4 as ongoing α-LixFe3O4 → β-Li4Fe3O4 phase change; conversion towards Fe+Li2O is separate. Indirect support for continuing reaction/structural redistribution after interruption. Their model also suggests smaller Fe3O4 crystallites need not always convert faster: avoid assuming all milling effects = faster reaction.
3. **K. He et al., Nat. Commun. 2016, 7, 11441**, *Visualizing non-equilibrium lithiation of spinel oxide via in situ transmission electron microscopy*, https://www.nature.com/articles/ncomms11441. Direct visualization of overlapping intercalation and conversion in Fe3O4 nanocrystals, with phase coexistence and fronts. Supports multiple-process/heterogeneity idea, not ΔE_rest hump itself.
4. **X.-F. Luo et al., Adv. Sci. 2022, 9, 2201219**, *Charge–Discharge Mechanism of High-Entropy Co-Free Spinel Oxide Toward Li+ Storage Examined Using Operando Quick-Scanning XAS*, DOI **10.1002/advs.202201219**, https://pmc.ncbi.nlm.nih.gov/articles/PMC9313486/. Different (CrMnFeNiCu)3O4 spinel; species-specific multistage Mn/Fe/Cr reduction supports complexity of reaction-state distribution; does not establish any hump or direct oxidation-state assignment here.
5. **S. D. Kang & W. C. Chueh, JES 2021, 168, 120504**, *GITT Reinvented Part I. A Critical Review*, DOI **10.1149/1945-7111/ac3940**, https://doi.org/10.1149/1945-7111/ac3940. Relaxation mixed with composition-dependent overpotentials, particle heterogeneity and finite-window effects; crucial for limiting causal inference.
6. **Development of Experimental Techniques for Parameterization of Multi-scale Lithium-ion Battery Models**, JES 2020, https://doi.org/10.1149/1945-7111/AB9050; voltage variation couples concentration relaxation and local equilibrium-potential derivative U'(c) under linearization. Supports second mechanism as a theoretical factor, not validation of the particular hump.

## Credibility/claim calibration

**Directly observed:** finite-window R3 amplitude hump strong only for pristine, Mg weak, milled absent; all t63 increase in R3. R3 nominal charge experiences largest negative change in each material modification contrast (under operational region assignment).

**Plausible primary mechanism:** local reaction-state/phase heterogeneity (spatially nonuniform or overlapping conversion reactions) contributes to finite-window relaxation. Modification may alter the distribution and cause a smoother response. FeF3 JACS is the strongest direct analogue, and Fe3O4 phase studies support plausibility. The stronger hypothesis is **heterogeneity or changing population of relaxable states**, rather than identifying a particular atomic intermediate.

**Plausible secondary mechanism:** state-dependent QOCV–charge slope makes a similar Li redistribution appear as a different voltage amplitude. Without quantitative derivative normalization this is not independent evidence for hump's origin.

**Important caveats:** The 3 s reference excludes most instantaneous IR jump; 60 min does not prove full equilibrium. The observation is a hump across *pulse number*, not a non-monotonic curve in a *single rest*. Mg chemical substitution cannot be assumed to homogenize particles via the same route as milling. Same R3 operational label may correspond to different voltages/states across samples, so fixed-QOCV checks matter. ΔE_rest is not equivalent to diffusivity, reaction rate, or unique resistance.

## Suggested main text strategy

- Keep the observed numerical hump in §2.3.
- §2.5: two sentences on spatially heterogeneous multistep conversion as a **literature-supported mechanistic possibility** using Li 2016 and Knehr/He 2016/17; a concise sentence on QOCV slope as an alternative factor. Avoid “demonstrates an additional slow reaction” and any specific cation/phase assignment.
- Physical interpretation remains subordinate to **region-resolved nominal GITT charge**, the manuscript's primary discovery.
- Minimal validation from existing raw: (a) common-QOCV ΔErest curves, (b) per-pulse local dQOCV/dQ versus ΔErest, (c) normalized full rest curves and early/late amplitude split. These can discriminate simple voltage-slope amplification from extra relaxing modes; cannot alone uniquely prove phase identity.

**Decision:** Stronger external support now exists for a *reaction heterogeneity/phase-distribution* hypothesis. Keep both options as hypotheses. No changes made to manuscript in this literature-only review.
