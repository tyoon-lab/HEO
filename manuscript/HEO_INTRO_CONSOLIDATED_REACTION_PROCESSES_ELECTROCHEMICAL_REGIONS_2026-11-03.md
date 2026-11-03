# Consolidated HEO Introduction — PI review (2026-11-03)

**Editorial state:** New full PI-review candidate, not silently integrated into authoritative v29 Main or the PI-kept Abstract; SI v17 unchanged.

**Terminology lock:**
- **reaction processes** = physical/chemical actions (Li uptake, cation reduction, oxide reconstruction, metal/Li₂O development) that overlap during conversion;
- **electrochemical regions** = voltage/relaxation-defined lithiation intervals R1–R4, not four exclusive chemical steps;
- **dominant reaction processes** = literature-informed associations that may vary in relative prominence by region.

**Narrative:** P1 spinel HEO first, multi-cation reduction and intermediate reconstruction → P2 because contributions evolve, processing/composition can change contributions nonuniformly; existing work largely connects structural snapshots and overall capacity, not decomposed change → P3 flat voltage/dQdV, GITT relaxation voltage/time descriptors, electrochemical NiO precedent and D_app assumption caveat → P4 crossed BM/Mg, four-region nominal charge localization and design significance.

**Full English text:**

# 1. Introduction

Spinel high-entropy oxides (HEOs) combine multiple transition-metal cations within a common oxide lattice and have attracted interest as high-capacity conversion-type anodes. Although their lithium storage can be summarized by an overall oxide-to-metal/Li₂O conversion reaction, state-resolved studies reveal a more intricate evolution during lithiation. Operando X-ray absorption spectroscopy has shown that the constituent metal cations in spinel HEOs undergo reduction over different, partly overlapping ranges of lithiation [7]. Ex situ X-ray absorption and diffraction studies have identified Li uptake, cation migration, and intermediate oxide reconstruction before and during metal-forming conversion [23]. Similar intermediate oxide transformations have also been observed in conventional spinel oxides such as Fe₃O₄ [22]. Together, these studies show that HEO lithiation involves overlapping cation-reduction and structural transformation processes, with different processes becoming prominent as lithiation proceeds.

Because these processes evolve during lithiation, materials modification may affect them to different extents. Previous studies have shown that changes in particle size, cation composition, and Li₂O incorporation alter the capacity and conversion behavior of spinel HEOs [9,20,24]. These studies connect materials characteristics with electrochemical performance and structural changes observed at selected lithiation states. However, they do not generally quantify how much of the capacity change arises from different parts of the conversion reaction. A gain in charge storage in one part of lithiation may be accompanied by a loss in another, even when the total capacity increases. Distinguishing these contributions would reveal which reaction processes are most affected by a given modification and provide a basis for selecting processing and compositional changes that preferentially promote them.

If different reaction processes become prominent during lithiation, their changing contributions should also be reflected in the electrochemical response. The voltage profile contains information about the reaction potentials, but the broad plateaus characteristic of conversion electrodes can accommodate substantial charge without clearly distinguishing individual processes. Overlapping reduction and structural changes may also produce poorly resolved differential-capacity features [7,23]. Galvanostatic intermittent titration (GITT) provides additional information by measuring voltage relaxation after successive current pulses. GITT is commonly used to estimate apparent chemical diffusion coefficients, but interpreting the relaxation solely in terms of diffusion becomes problematic when reduction, structural reconstruction, and evolving interfaces contribute to the response [11–13]. Electrochemical regions with different dominant reactions have previously been distinguished in a NiO conversion anode using GITT-derived parameters [26]. The measured relaxation amplitude and characteristic recovery time, considered together with the rest-end voltage, offer a direct way to identify changes in the electrochemical response and define regions of lithiation without assigning a separate chemical step to each region.

In this study, first-lithiation GITT is used to compare pristine HEO, ball-milled HEO (BM-HEO), Mg-containing HEO (Mg-HEO), and ball-milled Mg-HEO (BM-Mg-HEO). Changes in rest-end voltage, relaxation amplitude, and characteristic recovery time distinguish four electrochemical regions, whose dominant reaction processes are interpreted using established HEO conversion chemistry. The characteristic sequence of electrochemical responses remains recognizable across the four materials, whereas the charge contributions of the individual regions differ substantially. Ball milling produces its largest positive regional GITT-charge increment during conversion onset and progression, while Mg incorporation causes its largest negative increment during later conversion. These contrasting responses show that processing and compositional modifications primarily affect different parts of lithiation, establishing a basis for targeting specific conversion processes in HEO anodes.

## Reference key (provisional v29 indices)
[7] Luo et al., *Advanced Science* (2022), DOI 10.1002/advs.202201219.
[9] Li et al., *Angew. Chem. Int. Ed.* (2025), DOI 10.1002/anie.202518569.
[11–13] Kang & Chueh, *JES* (2021), DOI 10.1149/1945-7111/ac3940; Jia et al., *JPS* (2022), DOI 10.1016/j.jpowsour.2022.231843; Zhu & Wang, *J. Phys. Chem. C* (2010), DOI 10.1021/jp9113333.
[20] Xiao et al., *ACS AMI* (2023), DOI 10.1021/acsami.2c12374.
[22] He et al., *Nature Communications* (2016), DOI 10.1038/ncomms11441.
[23] Triolo et al., *Small* (2023), DOI 10.1002/smll.202304585.
[24] Ma et al., *Energy Advances* (2023), DOI 10.1039/D3YA00326D.
[26] Ng et al., *J. Mater. Chem. A* (2021), DOI 10.1039/D0TA09683K.

## Internal only — QA for future manuscript integration
- Exact PI-preferred two opening sentences preserved; single non-HEO spinel Fe3O4 illustration remains.
- P1 and P2 connect directly through evolution of reaction-process contributions; no `multistep` as a defining result and no `region` before introducing electrochemical criteria in P3.
- Avoid claiming unique direct spectroscopic chemical phase identification. R2/R3 are overlapping reaction domains. Largest positive BM ΔR2 = +166.7/+133.3 mAh g⁻¹; largest negative Mg ΔR3 = −266.7/−283.3 mAh g⁻¹, nominal GITT protocol charge, not GCD capacity.
- Scientific caution: under current GITT, measured end-of-rest voltage ≠ certified OCV; plateau ≠ proof of perfect two-phase equilibrium. ΔErest 3–3600 s is finite window recovery, not pure ohmic/kinetic overpotential; t63 = observed 63.2% recovery time, not single fitted reaction rate or unique D. Nuance kept in Results and Methods, not repeatedly in main Introduction.
- Potential revision: ‘Changes in particle size, cation composition, and Li₂O incorporation alter...’ should remain supported by [9,20,24] in paper reference check. Retain material-interpretation emphasis over method novelty.
