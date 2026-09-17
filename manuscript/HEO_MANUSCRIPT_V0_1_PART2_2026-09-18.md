# HEO Manuscript Draft v0.1 — Part 2

**Scope:** Experimental section + early Results and Discussion (synthesis/structure/surface area/basic electrochemistry)  
**Date:** 2026-09-18

> Drafting rule: verified information is written directly. Unverified historical details are marked for collaborator/student confirmation rather than inferred. Electrochemical values in the Results section use the latest 2026-09-17 dataset when it supersedes earlier May 2026 summary values.

---

# 2. Experimental Section

## 2.1. Materials and synthesis of high-entropy oxides

Nickel(II) chloride hexahydrate (NiCl2·6H2O, 99.9%), iron(III) chloride hexahydrate (FeCl3·6H2O, ≥98%), cobalt(II) chloride hexahydrate (CoCl2·6H2O, 98%), manganese(II) chloride tetrahydrate (MnCl2·4H2O, ≥98%), chromium(III) chloride hexahydrate (CrCl3·6H2O), sodium hydroxide (NaOH, ≥97.0%), and sodium carbonate monohydrate (Na2CO3·H2O, ≥99.5%) were used as received.

The Mg-free high-entropy oxide (HEO) was prepared through precipitation of a high-entropy hydroxide precursor followed by calcination. NiCl2·6H2O, FeCl3·6H2O, CoCl2·6H2O, MnCl2·4H2O, and CrCl3·6H2O were dissolved in 20 mL of deionized water, with 1.4 mmol of each metal precursor. Separately, 14 mmol of NaOH and 7 mmol of Na2CO3·H2O were dissolved in 10 mL of deionized water. The alkaline solution was slowly added to the mixed-metal precursor solution under stirring at 800 rpm, and precipitation was continued for 2 h at room temperature. The precipitate was collected by centrifugation, washed three times with water, and dried overnight at 70 °C. The dried precursor was calcined at 900 °C for 2 h using a heating rate of 5 °C min−1 to obtain the spinel HEO.

Ball-milled HEO (BM-HEO) was prepared from the calcined powder. Two grams of HEO were milled for 12 h at 500 rpm in an 80 mL stainless-steel jar using 5 mm ZrO2 balls and a powder-to-ball mass ratio of 1:10.

The Mg-containing samples (Mg-HEO and BM-Mg-HEO) were prepared using the corresponding Mg-containing precursor composition and the same post-synthesis comparison scheme. **[[COLLABORATOR TO COMPLETE: Mg precursor identity, Mg amount/metal ratio, whether Mg was added or substituted relative to the five-cation composition, precipitation/calcination details if different from HEO, and final nominal formula. Final composition should be cross-checked against ICP-OES.]]**

## 2.2. Structural and physicochemical characterization

Powder X-ray diffraction (XRD) patterns were collected using a MiniFlex 600 diffractometer (Rigaku, Japan) with Cu Kα radiation (λ = 1.5406 Å). Elemental compositions were measured by inductively coupled plasma optical emission spectroscopy (ICP-OES; iCAP PRO, Thermo Fisher Scientific, USA). Surface chemical states were analyzed by X-ray photoelectron spectroscopy (XPS; K-Alpha, Thermo Electron, USA). Morphology was examined by field-emission scanning electron microscopy (FE-SEM; Gemini 360, Carl Zeiss, Germany). Microstructure, lattice fringes, and elemental distributions were examined using a Cs-corrected transmission electron microscope (JEM-ARM200F, JEOL, Japan). Specific surface areas were obtained from N2 adsorption measurements at 77 K using a BELSORP-max system (MicrotracBEL, Japan) and the Brunauer–Emmett–Teller method.

**[[COLLABORATOR TO FINALIZE BEFORE SUBMISSION: phase indexing/Rietveld refinement, final TEM plane indexing, ICP compositions, and the XPS dataset selected for the manuscript. The current Cr6+ feature near 579 eV is batch-dependent and should not be used mechanistically until the collaborator group completes the planned remeasurement/fitting.]]**

## 2.3. Electrode preparation and electrochemical measurements

The active HEO powder, Super P conductive carbon, and poly(acrylic acid) (PAA) binder were mixed at a mass ratio of 8:1:1 using deionized water as the slurry solvent. The slurry was coated using a 100 μm bar-coater gap. CR2032-type half-cells were assembled with the HEO-based electrode as the working electrode and Li metal as the counter electrode. A polypropylene separator and 1.0 M LiPF6 in EC/DEC (1:1 by volume) containing 10 wt% fluoroethylene carbonate (FEC) were used for the cells.

**[[STUDENT TO CONFIRM: current-collector material, vacuum-drying temperature/time, final electrode thickness and active-material loading, separator manufacturer/model if available, electrolyte volume, and glove-box H2O/O2 levels.]]**

Galvanostatic charge–discharge measurements were performed using a WonATech battery cycler between 0.005 and 2.5 V. The principal low-rate comparison was conducted at 0.1 C. Rate-capability tests were performed by stepwise increasing the C-rate from 0.1 C to 5 C followed by recovery at 0.1 C. **[[STUDENT TO CONFIRM the capacity basis used to define 1 C.]]**

The galvanostatic intermittent titration technique (GITT) was performed at 100 mA g−1 between 0.005 and 2.5 V using repeated 10 min current pulses followed by 60 min open-circuit relaxation. The current-off portions of the GITT response were emphasized because the pulse-period voltage contains both polarization and the change in equilibrium potential associated with continued lithiation/delithiation.

For early current interruption, the voltage between 3 and 30 s after switching the current off was represented as

E(t) = a + b√t,

and the intercept a was extrapolated to t -> 0. The corresponding current-off voltage jump was divided by the applied current to obtain an apparent instantaneous current-off resistance. This quantity is used as an experimental descriptor and is not assigned uniquely to ohmic resistance.

The finite-window relaxation amplitude was defined as

ΔE_relax = E_60min − E_off,3s,

with the sign interpreted according to the current direction and absolute magnitude used for comparison when appropriate. Model-free relaxation times t50, t63, and t90 were defined as the times required to reach 50%, 63.2%, and 90% of the total observed 3 s-to-60 min relaxation, respectively. These quantities do not assume single-exponential relaxation; t63 equals a conventional time constant only for an ideal single exponential. The initial relaxation slope over 3–30 s and the terminal slope over the final 10 min of the 60 min rest were additionally evaluated as early- and unresolved-slow-response descriptors.

Cyclic voltammetry in the nominal non-faradaic region of 3.0–3.3 V was acquired at scan rates of 10, 20, 40, 60, 80, and 100 mV s−1 for relative interfacial-capacitance comparison. Previous calculations used a specific capacitance of 40 μF cm−2 to convert the double-layer capacitance to nominal electrochemically active surface area. Because this conversion depends on the assumed specific capacitance for a porous composite electrode, the manuscript uses these data primarily as a relative interfacial-accessibility metric rather than as an absolute physical surface area.

**[[STUDENT TO CONFIRM: potentiostat model and detailed CV/EIS acquisition conditions before final Methods freeze.]]**

---

# 3. Results and Discussion

## 3.1. Synthesis-dependent structure and morphology

The four samples were designed as a 2 × 2 comparison that separates the effects of composition and mechanical processing: HEO and BM-HEO isolate the effect of ball milling in the Mg-free material, whereas Mg-HEO and BM-Mg-HEO provide the corresponding comparison after Mg incorporation. This design is central to the electrochemical interpretation because Mg and ball milling modify the electrode response in different directions rather than producing a common monotonic change in kinetic performance.

The XRD patterns of the as-prepared samples are dominated by reflections characteristic of the cubic spinel-type HEO. Mg incorporation produces a small but reproducible shift of the principal reflection near 35.7° toward lower 2θ. Before ball milling, the peak position changes from approximately 35.76° for HEO to 35.70° for Mg-HEO, while the corresponding ball-milled samples shift from approximately 35.68° to 35.64°. If this reflection is indexed as the cubic spinel (311) plane, the observed shifts correspond to only ~0.1–0.2% expansion of the apparent cubic lattice parameter. The magnitude is therefore consistent with a modest lattice expansion after Mg incorporation but is not, by itself, sufficient to establish Mg occupancy at a specific crystallographic site. Final lattice parameters and phase fractions should be taken from the collaborator group's refined XRD/ICP analysis.

Ball milling broadens the diffraction features while preserving the dominant spinel-like peak positions in the current patterns. This response is consistent with reduced coherent-domain size and/or increased microstrain and structural disorder produced by prolonged high-energy milling. The literature indicates that mechanical processing of spinel HEOs can do more than decrease particle size: high-energy milling has been shown to perturb the spinel/rock-salt structural balance, and long-term particle fragmentation during cycling alters conversion reversibility and interfacial storage. These precedents make structural disorder an important variable when interpreting the electrochemical response of BM-HEO rather than treating ball milling only as a geometric particle-size reduction.

Electron microscopy further confirms nanoscale structural heterogeneity and spatially distributed multication chemistry in the four materials. EDS maps show Fe, Co, Ni, Cr, Mn, and O throughout the HEO particles and additionally detect Mg in the Mg-containing samples. The current HRTEM images show lattice fringes compatible with nanocrystalline spinel-related domains, although the plane labels in the preliminary collaborator slides require re-indexing before final publication. In particular, phase labels based on CoGa2O4 are not chemically applicable to the present Ga-free synthesis and are therefore not used in the manuscript. **[[COLLABORATOR TO INSERT: final HRTEM/SAED indexing, particle-size statistics, and any refined structural comparison that directly supports Mg incorporation or milling-induced disorder.]]**

The structural measurements therefore establish two distinct perturbations before electrochemical cycling: Mg produces a small lattice-level change without eliminating the parent spinel-type structure, whereas ball milling introduces a much stronger microstructural perturbation and peak broadening. The surface-area measurements show that this mechanical perturbation also changes the available electrode/electrolyte interface substantially.

## 3.2. Surface accessibility and baseline electrochemical response

The BET surface area increases from 3.94 m2 g−1 for HEO to 18.159 m2 g−1 after ball milling, corresponding to a 4.61-fold increase. Mg-HEO has a somewhat larger initial surface area of 6.49 m2 g−1, while BM-Mg-HEO reaches 16.64 m2 g−1, a 2.56-fold increase relative to Mg-HEO. Thus, ball milling produces the dominant increase in physical surface area in both compositions, although the final surface areas of BM-HEO and BM-Mg-HEO are similar. The interfacial-capacitance measurements show the same qualitative ordering: the nominal capacitance-derived accessible-interface values rise strongly after milling, from 4.18 to 30.17 cm2 in the Mg-free pair and from 6.56 to 39.68 cm2 in the Mg-containing pair when converted using the same assumed specific capacitance. These values are not treated as absolute ECSA because the conversion relies on an uncertain specific capacitance for the porous composite electrode; their role is to corroborate the large relative increase in electrochemically accessible interface after milling.

The increase in interface is accompanied by greater first-cycle electrochemical utilization. In the latest 2026-09-17 dataset, the first-cycle values recorded under the WonATech charge/discharge convention are 901.25/609.12 mAh g−1 for HEO and 1056.10/782.08 mAh g−1 for BM-HEO, with initial Coulombic efficiencies of 67.59% and 74.05%, respectively. Ball milling therefore increases the two first-cycle capacity measures by approximately 17% and 28% in the Mg-free pair. Mg-HEO and BM-Mg-HEO deliver 731.15/458.91 and 944.07/580.83 mAh g−1, respectively, with initial Coulombic efficiencies of 62.77% and 61.52%. Ball milling also increases the first-cycle capacity measures in the Mg-containing pair by approximately 29% and 27%, whereas Mg incorporation lowers the corresponding capacities relative to the Mg-free compositions. **[[Before final manuscript submission, verify whether the WonATech labels 'charge' and 'discharge' correspond to lithiation/delithiation in the half-cell and replace the terminology consistently throughout the manuscript.]]**

These first-cycle data separate the effects of the two synthesis variables. Ball milling increases accessible capacity in both compositions, consistent with the substantially enlarged surface area and electrochemically accessible interface. Mg incorporation has the opposite effect on capacity despite increasing, rather than decreasing, the BET surface area of the unmilled powder from 3.94 to 6.49 m2 g−1. The lower capacity of Mg-HEO therefore cannot be explained simply by loss of geometric surface area or reduced electrode/electrolyte contact. This contrast points instead to a change in the reaction pathway or in the fraction of the oxide that participates in conversion-type storage.

The cycling data show that interfacial accessibility and interphase stability must be considered together. Under the common electrolyte containing 10 wt% FEC, BM-HEO maintains a higher absolute capacity than HEO over 100 cycles, while both Mg-containing electrodes operate at lower capacity. The corresponding control cells without FEC show a stronger capacity decay for BM-HEO than for HEO, indicating that the larger interface created by milling also increases sensitivity to surface reactions. FEC substantially mitigates this penalty and was therefore used as the common electrolyte additive for the four-sample comparison. The present manuscript treats FEC as a standardized interphase-control condition rather than as a third synthesis variable.

The rate-capability data provide a second constraint. BM-HEO retains a higher absolute capacity than HEO across the tested C-rate sequence and recovers the higher capacity when the rate returns to 0.1 C. The capacity enhancement produced by milling therefore coexists with, rather than requires, faster long-time relaxation. This distinction becomes important in the GITT analysis below: a material can sustain higher galvanostatic utilization over the tested rate range while exhibiting a slower structural/electrochemical recovery during a 60 min current interruption. Rate capability and relaxation time are consequently related but non-equivalent observables.

The opposite trend after Mg incorporation is equally informative. Mg decreases accessible capacity while simultaneously reducing the current-off polarization observed in GITT, as developed in the following section. If the lower polarization were caused simply by faster Li diffusion, the relaxation should also become faster. The measured characteristic relaxation times do not show this behavior. The combination of lower capacity, lower polarization amplitude, and unchanged or longer relaxation time therefore motivates a phase-evolution interpretation rather than a single-diffusivity explanation.

The subsequent current-interruption analysis directly tests this interpretation by separating the magnitude of the current-off polarization from the time required for that polarization to relax. This distinction reveals that ball milling and Mg incorporation alter the late-stage conversion response through different physical routes.

---

# Drafting notes for Part 2

## Data/metadata still required

- Mg precursor, amount, and final nominal/ICP composition.
- Current collector.
- Vacuum drying temperature/time and active loading.
- Separator model and electrolyte volume if available.
- Definition of 1 C.
- Potentiostat/model details for CV/EIS/GITT if not all performed on WonATech.
- Final TEM/SAED indexing and XPS dataset.
- Final terminology for first half-cycle vs second half-cycle capacity according to the cycler convention.

## Data-lineage correction introduced on 2026-09-18

- The 2026-09-17 progress deck is treated as the latest authoritative electrochemical summary when it conflicts with the May 2026 presentation.
- Earlier first-cycle values (858.8/558.8, 1030.2/699.2, 814.8/514.0, and 934.9/590.3 mAh g−1 pairs) are preserved in project history but are not used in the current manuscript draft.
- The latest rate plot does not support the earlier simplified note that ball milling necessarily worsens rate capability. The manuscript now states only what the plotted data support: BM-HEO maintains higher absolute capacity across the tested rate sequence despite slower GITT relaxation.

## Interpretation boundaries fixed in this draft

- XRD low-angle shift is described as consistent with modest lattice expansion, not proof of Mg substitution at a unique site.
- BET/Cdl changes are used as relative accessibility evidence; nominal ECSA is not treated as absolute surface area.
- Ball milling is not described as improving Li diffusion.
- Mg-induced capacity loss is not attributed to lower surface area.
- Rate capability and long-rest relaxation time are treated as distinct observables.
- The phase-transition mechanism is introduced as the question generated by the basic electrochemistry; the stronger phase-transition assignment is reserved for the GITT section in Part 3.

## Literature to be integrated during reference-number consolidation

- Wang et al., J. Alloys Compd. 2020, 844, 156158, DOI 10.1016/j.jallcom.2020.156158.
- Nguyen et al., J. Mater. Chem. A 2020, 8, 18963-18973, DOI 10.1039/D0TA04844E.
- Huang et al., Chem. Eng. J. 2021, 420, 129838, DOI 10.1016/j.cej.2021.129838.
- Wang et al., Mater. Chem. Phys. 2021, 274, 125105, DOI 10.1016/j.matchemphys.2021.125105.
- Xiao et al., Nano Energy 2022, 95, 106962, DOI 10.1016/j.nanoen.2022.106962.
- Zheng et al., Processes 2022, 10, 49, DOI 10.3390/pr10010049.
- Zhai et al., J. Power Sources 2024, 603, 234418, DOI 10.1016/j.jpowsour.2024.234418.
- Jin et al., Mater. Today Chem. 2025, 102949, DOI 10.1016/j.mtchem.2025.102949.