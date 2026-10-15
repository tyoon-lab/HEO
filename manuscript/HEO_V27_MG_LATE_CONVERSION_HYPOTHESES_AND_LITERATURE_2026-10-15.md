# HEO v27 — ranked Mg-related late-conversion hypotheses (PI-review, 2026-10-15)

**Status:** A mechanism-strengthening proposal grounded in current regional GITT charge, reported BET and external primary literature. This note **does not prove an Mg lattice site, MgO formation, stabilization free energy, reaction-specific kinetic parameter or Li₂O yield**. Do not confuse a strong stage-localization observation with a phase-specified mechanism. v26 Word and SI unchanged.

## Why a mechanistic ranking is warranted

The original nominal protocol-derived first-lithiation GITT region charge (mAh g−1) is:

| Sample | R1 | R2 | R3 | R4 | Total |
|---|---:|---:|---:|---:|---:|
| HEO | 100.0 | 316.7 | 516.7 | 150.0 | 1083.3 |
| Mg-HEO | 100.0 | 300.0 | 250.0 | 150.0 | 800.0 |
| BM-HEO | 150.0 | 483.3 | 366.7 | 266.7 | 1266.7 |
| BM-Mg-HEO | 150.0 | 433.3 | 83.3 | 266.7 | 933.3 |

- HEO→Mg: R2 −16.7/316.7 = **−5.3%**, R3 −266.7/516.7 = **−51.6%**; R3 accounts for ~94% of nominal total loss (−283.3 mAh/g).
- BM→BM-Mg: R2 −50/483.3 = **−10.3%**, R3 −283.3/366.7 = **−77.3%**; qualitatively reproduced concentration in R3, not full independent confirmation of a specific reaction.
- The **finite GITT pulse partition** and inherited L1/L3/L4 boundary positions are working regional evidence; original boundary annotations not independently recovered. Nominal GITT is not GCD, and the region values are coarse pulse increments.
- Mg-HEO BET is **6.49 versus HEO 3.94 m²/g** (source Figure2 labels). Simple reduced gas-accessible area is therefore **not sufficient** to explain strong Mg-associated R3 charge loss, though electrode kinetics/connectivity remain possible.
- The remaining R3 `t63` changes much less than the regional charge; `t63` describes **post-pulse voltage recovery**, **not the on-pulse conversion rate, overpotential, microscopic diffusion constant or thermodynamic stabilization energy**. A potential shift toward lower voltage could reflect thermodynamic and/or polarization changes.

## Ranked mechanistic hypotheses

### H1 — PREFERRED: Mg as a largely redox-inactive structural spectator, decreasing accessibility of late conversion
Mg-containing oxide environments may remain comparatively resistant to *further reduction/reconstruction* while redox-active transition metals undergo initial conversion. This could preserve an Mg-bearing oxide-like scaffold or alter later conversion energetics, limiting the charge attainable in the R3 region within the measured potential window. This is **not** a claim that the present specimens contain isolated MgO, retain their original spinel framework, or possess an experimentally measured particular Mg–O stabilization energy.

**Why favored:** (i) Mg-associated charge loss is strongly *late-stage selective* in both matched pairs instead of uniform, (ii) higher untreated Mg BET excludes smaller gas-accessible surface as a sufficient reason, (iii) R3 remaining t63 changes modestly, compatible with reduced accessible reaction extent, (iv) the conversion-related voltage response shifts lower, consistent with changed *accessibility under cutoff* but not diagnostic of its exact source, (v) literature supports the spectator/structural-stabilizer role of Mg in related HEOs, including spinel.

### H2 — CONTRIBUTING: fewer reducible metal centers / dilution of active transition metals
If Mg replaces reducible cations or adds inactive oxide mass, gravimetric capacity and redox-site inventory can decrease. **Uniform dilution alone**, however, predicts approximately common proportional reduction across R2 and R3, in tension with the observed −5.3% vs −51.6% in untreated materials and −10.3% vs −77.3% in milled materials. **Important:** non-uniform dilution is possible if Mg substitution changes which cations occupy sites or which redox couples dominate R3; this can be the principal true mechanism, cannot be ruled out without the actual Mg stoichiometry, ICP and cation site distribution. Avoid categorical claims that dilution is ruled out.

### H3 — COMPETING: conversion moved to a less accessible potential/kinetic window
Mg could shift the equilibrium potential for later conversion or increase charge-transfer/nucleation/solid-state overpotential during the GITT current pulse. A fixed low-voltage cutoff would then terminate R3-like conversion earlier, with similar *remaining post-pulse t63* even though the pulse-stage conversion capacity is smaller. The current GITT rest-end potential and t63 alone do not separate kinetic versus thermodynamic origins. Test by cutoff-window, current-rate, temperature and voltage-hold recovery after GITT; do not assert electrochemical equilibrium of a 60-min rest endpoint.

### H4 — LOWER-PRIORITY / ALTERNATIVE: segregation, contact/SEI effects, and altered phase purity
An Mg-rich secondary oxide, contact/polarization changes or parasitic reactions could modify accessible charge and region landmarks. EDS Mg signal is not ICP-quantified spinel substitution; Figure1 CoGa2O4 labels require phase reindexing. Surface-area trends argue against an explanation based **solely** on decreasing BET, not all interface/contact effects. These possibilities currently lack direct supporting characterization.

**Preferred integrated physical picture:** **Mg acts as a redox-poor structural component that changes the accessibility of the remaining late conversion, combined with a reduction/reorganization of available redox-active cations.** The data strongly establish **where**, not uniquely **how**, Mg changes the conversion profile. Do not distinguish ‘stabilized oxide free energy’ from a ‘shift below voltage cutoff’ without further measurements.

## Literature directly checked, with applicability conditions

1. **Liu et al.**, *Chemical Science* **17** (2026), 6116–6124, DOI [10.1039/D5SC10185A](https://doi.org/10.1039/D5SC10185A) — spinel **(CoCuMgCrFe)3O4**, DFT + experiments; Mg/Cu serve structural roles while Cr/Co/Fe support conversion-related chemistry. **Closest same-structure mechanistic comparator**, but lacks Ni/Mn of our sample and has Cu.
2. **Wang et al.**, *Nature Communications* **14** (2023), 1487, DOI [10.1038/s41467-023-37034-6](https://doi.org/10.1038/s41467-023-37034-6) — rock-salt **MgCoNiCuZnO**, Mg-rich oxide nanoenvironment coexists with reduced metals; strong spectator/oxide-scaffold example, **different starting crystal family** and transition-metal set. Does not prove Mg-specific R3 behavior here.
3. **Sarkar et al.**, *Nature Communications* **9** (2018), 3400, DOI [10.1038/s41467-018-05774-5](https://doi.org/10.1038/s41467-018-05774-5) — rock-salt Mg-containing HEO, partial cation conversion and spectator matrix proposal. Hypothesis consistency, not direct spinel chemistry proof.
4. **Jin et al.**, *Materials Today Chemistry* **48** (2025), 102949, DOI [10.1016/j.mtchem.2025.102949](https://doi.org/10.1016/j.mtchem.2025.102949) — five-cation **Mg-free FeCoCrNiMn spinel** reports spinel → mixed spinel/rock-salt → rock-salt sequence. Supports progressive reconstruction of related parent oxide, **not a Mg-substitution mechanism by itself**.
5. **Permien et al.**, *J. Mater. Chem. A* **3** (2015), 1549–1561, DOI [10.1039/C4TA05054A](https://doi.org/10.1039/C4TA05054A) — MgFe2O4 spinel Li-insertion mechanism, related binary spinel comparison.

Check final bibliography formatting and which references are already present in the 20-entry v26 list before adding any new numbered reference.

## Ready-to-insert Section 2.5 discussion (replace current third paragraph with two paragraphs)

The pronounced loss of nominal GITT charge in R3, compared with the smaller change in R2, points to a modification of the accessibility or energetics of later conversion rather than a uniform reduction in charge throughout the lithiation sequence. The most plausible physical explanation is that Mg behaves primarily as a redox-inactive structural component within the examined voltage window, favoring the persistence of Mg-containing oxide environments as other metal species undergo reduction. Such a spectator role could alter the subsequent reduction and structural reorganization associated with R3, restricting the extent of late conversion accessible under the applied potential cutoff. A related role for Mg as an oxide-structure stabilizer has been reported for multication oxides, including spinel high-entropy anodes [REF Liu et al., Chem. Sci. 2026] and rock-salt counterparts [REF Wang et al., Nat. Commun. 2023]. This interpretation is consistent with the preferential loss of R3 charge in both matched comparisons and the modest change in the remaining R3 relaxation timescale; it does not establish a distinct MgO phase or directly quantify conversion products in the present samples.

Other effects may contribute to the same response. The replacement of reducible transition-metal centers by Mg can decrease theoretical charge inventory, but approximately uniform compositional dilution alone is difficult to reconcile with the much larger proportional R3 decrease than R2 decrease. Selective replacement of later-reducing cations, changes in local coordination and a shift of subsequent conversion toward lower potential remain possible, particularly because the actual Mg content and site occupancy have yet to be established. Likewise, the post-pulse metric t63 cannot rule out slower conversion during current application or a kinetic limitation imposed by the low-voltage cutoff. The larger reported BET specific surface area of Mg-HEO relative to HEO (6.49 versus 3.94 m² g−1) further argues against simple loss of gas-accessible area as the dominant explanation. The present data therefore favor altered **late-conversion accessibility involving an Mg-associated persistent oxide environment**, potentially combined with redox-site dilution, while the precise chemical origin remains open to compositional and operando structural verification.

## Minimal next discriminating analysis with existing data
1. Audit actual Mg amount, which metal is displaced, and normalized formula-based theoretical charge from collaborator ICP/synthesis. Compare with the R2/R3 changes. These source details are currently **not available**; do not simulate them.
2. From the four existing GITT time traces compare on-pulse polarization `E_{pulse-end}−E_{rest,end}` at matched reference potentials and after fixed elapsed-charge conditions; disentangle rest response `ΔErest` from on-current polarization.
3. Check how much R3-related capacity could be reallocated below the observed cutoff by applying a longer potentiostatic hold / lower-current step near the nominal R3/R4 transition; new experiment if raw data do not include sufficient information.
4. Structural/chemical: discharged/partially lithiated XAS or XPS/EELS/XRD near electrochemically *matched* R2/R3 states to determine if Mg-rich oxide and reduced-metal product proportions change. Do not compare unmatched raw voltages across materials because Mg shifts potentials.
5. Acknowledge archived L1/L3/L4 region boundaries are inferred retrospectively from the working regional charge table; an independent signed landmark analysis strengthens quantitative localization.

## Integration state
This note records the **ranked manuscript-ready mechanism proposal**. It does not yet change the PI-reviewed v26 Word, SI, Abstract, phase labels, or region boundaries. Upon user approval, merge the two-paragraph discussion into Section 2.5 and harmonize Section 2.6/Conclusion, with these primary-source citations inserted into the manuscript bibliography after final index verification.
