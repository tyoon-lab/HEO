# HEO Manuscript v2 — Figure-Aligned Draft

**Date:** 2026-09-19  
**Status:** Figure-aligned integrated manuscript  
**Source priority:** verified structural/electrochemical draft + raw GITT reanalysis + frozen spatial-model logic  
**Writing mode:** broad materials/electrochemistry readership; mechanism-first; model parameters remain non-unique

> Verified information is written directly. Experimental details that remain unavailable are marked for collaborator/student confirmation rather than inferred.

---

# Recommended title

**Contrasting Roles of Mg Incorporation and Ball Milling in Spinel High-Entropy Oxide Anodes: Phase Evolution, Polarization, and Electrochemical Utilization**

Alternative, more compact title:

**Mg Incorporation and Ball Milling Regulate Phase-Transformation Polarization in Spinel High-Entropy Oxide Anodes**

---

---

# Abstract

Spinel high-entropy oxides (HEOs) provide high-capacity conversion-type lithium storage, but synthesis-dependent changes in utilization are difficult to interpret when transport and structural transformation evolve simultaneously. Here, spinel Fe–Co–Ni–Cr–Mn HEO, ball-milled HEO (BM-HEO), Mg-containing HEO (Mg-HEO), and ball-milled Mg-HEO (BM-Mg-HEO) are compared in a 2 × 2 composition/process design. Ball milling increases the BET surface area of the Mg-free HEO from 3.94 to 18.159 m² g−1 and increases capacity across the tested rate range, yet the higher utilization does not coincide with faster post-pulse relaxation. Over 200–800 mAh g−1, HEO and BM-HEO show nearly identical apparent fast current-off resistances of ~106 Ω, while the model-free t63 increases from 8.68 to 11.57 min after milling. The late-stage transition-associated excess polarization simultaneously decreases from 70.8 to 44.1 mV and broadens from 354 to 430 mAh g−1. Mg incorporation produces a different response: Mg-HEO shows lower accessible capacity and a strongly suppressed excess peak of 15.9 mV, while t63 increases to 11.01 min rather than becoming shorter. A reduced spatial phase-field model shows that these directional trends are compatible when transformation stabilization/extent and structural-mobility/transition-condition heterogeneity are treated as independent coordinates. Ball milling therefore primarily increases accessibility and redistributes the phase-transforming reaction, whereas Mg predominantly suppresses its extent through structural stabilization. Separating capacity, polarization magnitude, transition width, and relaxation time reveals synthesis–electrochemistry relationships that are obscured by a single apparent diffusivity.

**Keywords:** high-entropy oxide; spinel anode; lithium-ion battery; ball milling; magnesium incorporation; phase transformation; GITT; current interruption; polarization relaxation

---

# 1. Introduction

High-entropy oxides (HEOs) extend the high-entropy concept to multication ceramic compounds, where several principal cations share a crystallographic sublattice and create compositionally complex single-phase structures.[1] Since the initial demonstration of entropy-stabilized oxides, HEOs have been explored for ionic conduction, catalysis, and electrochemical energy storage.[1,2] Their relevance to lithium-ion battery anodes is particularly strong because multiple transition-metal cations can provide high conversion capacity while chemically diverse cations can modify structural stability, electronic connectivity, and the morphology of the reacted state.[2] Spinel (Co,Cr,Fe,Mn,Ni)3O4 and compositionally equivalent Fe–Co–Ni–Cr–Mn oxides have emerged as a representative HEO anode family with a single-phase Fd-3m structure and high reversible lithium-storage capacity.[3–6]

Lithium storage in these spinel HEOs is not adequately described as diffusion through an invariant host. Atomic-scale and in-situ structural studies show extensive reconstruction during lithiation and delithiation, including reduction of transition-metal species, formation of nanoscale metallic/oxide regions, and conversion between spinel- and rock-salt-related structures.[5,7] A recent in-situ XRD/ex-situ TEM study on the same five-cation spinel family directly resolved a lithiation sequence from spinel to mixed spinel/rock-salt and finally to a rock-salt-dominated state.[7] These transformations provide substantial charge storage but also introduce electrochemical penalties associated with nucleation, phase-boundary propagation, strain accommodation, and structural reorganization. Consequently, a synthesis change can alter capacity not only by modifying Li transport distance or interfacial resistance, but also by changing how much material undergoes conversion and how broadly the transformation is distributed over state of charge.

Ball milling and Mg incorporation provide two physically different ways to perturb this reaction. Ball milling enlarges surface area, generates fresh interfaces, and introduces strain and local structural disorder. In spinel HEOs, high-energy milling has been shown to perturb the spinel/rock-salt structural balance, while particle fragmentation during cycling increases conversion reversibility and interfacial storage before excessive interfacial reconstruction contributes to degradation.[11,12] Mg-containing conversion-type HEOs show a different role. Electrochemically inactive Mg-derived oxide can act as a spectator or stabilizing component,[8] operando transmission X-ray microscopy shows improved structural retention with increasing Mg content,[9] and atomic/nanoscale studies of rock-salt HEOs show that electrochemically inactive cations can stabilize an oxide nanophase during conversion.[10] These precedents suggest a potential trade-off: increasing accessibility may increase the fraction of material that reacts, whereas structural stabilization may reduce the extent of conversion and therefore reduce both polarization and capacity.

This distinction is difficult to resolve when galvanostatic intermittent titration technique (GITT) data are reduced only to an apparent Li-ion diffusion coefficient. Conventional GITT analysis remains useful as a comparative descriptor, but its physical interpretation depends on diffusion geometry, time-window selection, equilibrium assumptions, and the absence of major structural complications.[6,15] These conditions are nontrivial in a phase-evolving conversion electrode. Current interruption preserves additional information. The early voltage response after switching off the current can be represented through an intercept and a sqrt(t) contribution under the semi-infinite diffusion approximation,[16] whereas the subsequent relaxation amplitude and characteristic time can be measured without assuming a single exponential. Phase-transforming electrodes are especially relevant because nucleation itself can constitute a substantial material-level overpotential.[17] Separating polarization magnitude from relaxation time therefore provides a direct way to test whether a synthesis-induced decrease in polarization actually reflects faster transport or instead reflects a change in reaction extent.

This study uses a 2 × 2 material/process comparison—HEO, BM-HEO, Mg-HEO, and BM-Mg-HEO—to determine how ball milling and Mg incorporation modify lithium storage in a spinel HEO anode. Structural and surface characterization is combined with galvanostatic cycling, rate tests, and direct analysis of the current-off portions of 10 min GITT pulses followed by 60 min relaxation. Ball milling increases electrochemical accessibility and capacity while broadening the late-stage transformation-associated polarization and slowing the long-rest response. Mg incorporation instead suppresses the late-stage polarization feature and conversion capacity without shortening the relaxation time. A spatial mechanism-sufficiency model reproduces these directional trends when transformation extent/stabilization and structural-mobility/transition-condition heterogeneity are treated as independent coordinates, and visualizes their distinct late-stage internal-state evolution. The combined results distinguish two synthesis coordinates: ball milling regulates accessibility and the distribution of the phase-transforming reaction, whereas Mg predominantly reduces the extent of the transformation through structural stabilization.

This study uses a 2 × 2 material/process comparison—HEO, BM-HEO, Mg-HEO, and BM-Mg-HEO—to determine how mechanical processing and compositional stabilization modify a phase-evolving spinel HEO anode. Structural and surface characterization is combined with galvanostatic performance, direct analysis of the current-off portions of 10 min GITT pulses followed by 60 min relaxation, and a reduced spatial mechanism-sufficiency model. The analysis is organized around four observables that need not move together: accessible capacity, polarization amplitude, transition width, and relaxation time. This separation is used to distinguish increased reaction accessibility from suppressed transformation extent and to connect synthesis to the internal evolution of the conversion reaction without assigning the response to a single apparent diffusion coefficient.

---

# 2. Experimental Section

## 2.1. Materials and synthesis of high-entropy oxides

Nickel(II) chloride hexahydrate (NiCl2·6H2O, 99.9%), iron(III) chloride hexahydrate (FeCl3·6H2O, ≥98%), cobalt(II) chloride hexahydrate (CoCl2·6H2O, 98%), manganese(II) chloride tetrahydrate (MnCl2·4H2O, ≥98%), chromium(III) chloride hexahydrate (CrCl3·6H2O), sodium hydroxide (NaOH, ≥97.0%), and sodium carbonate monohydrate (Na2CO3·H2O, ≥99.5%) were used as received.

The Mg-free HEO was prepared through precipitation of a multication hydroxide precursor followed by calcination. NiCl2·6H2O, FeCl3·6H2O, CoCl2·6H2O, MnCl2·4H2O, and CrCl3·6H2O were dissolved in 20 mL of deionized water, with 1.4 mmol of each metal precursor. Separately, 14 mmol of NaOH and 7 mmol of Na2CO3·H2O were dissolved in 10 mL of deionized water. The alkaline solution was slowly added to the mixed-metal precursor solution under stirring at 800 rpm, and precipitation was continued for 2 h at room temperature. The precipitate was collected by centrifugation, washed three times with water, and dried overnight at 70 °C. The dried precursor was calcined at 900 °C for 2 h using a heating rate of 5 °C min−1 to obtain the spinel HEO.

BM-HEO was prepared from the calcined powder. Two grams of HEO were milled for 12 h at 500 rpm in an 80 mL stainless-steel jar using 5 mm ZrO2 balls and a powder-to-ball mass ratio of 1:10.

Mg-HEO and BM-Mg-HEO were prepared using the corresponding Mg-containing precursor composition and the same post-synthesis comparison scheme. **[[COLLABORATOR TO COMPLETE: Mg precursor identity, Mg amount/metal ratio, whether Mg was added or substituted relative to the five-cation composition, precipitation/calcination details if different from HEO, and final nominal formula. Final composition should be cross-checked against ICP-OES.]]**

## 2.2. Structural and physicochemical characterization

Powder X-ray diffraction (XRD) patterns were collected using a MiniFlex 600 diffractometer (Rigaku, Japan) with Cu Kα radiation (λ = 1.5406 Å). Elemental compositions were measured by inductively coupled plasma optical emission spectroscopy (ICP-OES; iCAP PRO, Thermo Fisher Scientific, USA). Surface chemical states were analyzed by X-ray photoelectron spectroscopy (XPS; K-Alpha, Thermo Electron, USA). Morphology was examined by field-emission scanning electron microscopy (FE-SEM; Gemini 360, Carl Zeiss, Germany). Microstructure, lattice fringes, and elemental distributions were examined using a Cs-corrected transmission electron microscope (JEM-ARM200F, JEOL, Japan). Specific surface areas were obtained from N2 adsorption measurements at 77 K using a BELSORP-max system (MicrotracBEL, Japan) and the Brunauer–Emmett–Teller method.

**[[COLLABORATOR TO FINALIZE: phase indexing/Rietveld refinement, final HRTEM/SAED indexing, ICP compositions, and the final XPS dataset. The preliminary CoGa2O4 HRTEM labels are chemically inapplicable to the Ga-free synthesis and must not appear in the final manuscript. The batch-dependent Cr6+ XPS feature should not be used mechanistically until the planned remeasurement/fitting is completed.]]**

## 2.3. Electrode preparation and electrochemical measurements

The active HEO powder, Super P conductive carbon, and poly(acrylic acid) (PAA) binder were mixed at a mass ratio of 8:1:1 using deionized water as the slurry solvent. The slurry was coated using a 100 μm bar-coater gap. CR2032-type half-cells were assembled with the HEO-based electrode as the working electrode and Li metal as the counter electrode. A polypropylene separator and 1.0 M LiPF6 in EC/DEC (1:1 by volume) containing 10 wt% fluoroethylene carbonate (FEC) were used for the principal four-sample comparison.

**[[STUDENT TO CONFIRM: current-collector material, vacuum-drying temperature/time, final electrode thickness and active-material loading, separator manufacturer/model if available, electrolyte volume, and glove-box H2O/O2 levels.]]**

Galvanostatic charge–discharge measurements were performed using a WonATech battery cycler between 0.005 and 2.5 V. The principal low-rate comparison was conducted at 0.1 C. Rate-capability measurements used a stepwise C-rate sequence extending from 0.1 C to 5 C followed by recovery at 0.1 C. **[[STUDENT TO CONFIRM the capacity basis used to define 1 C and the exact number of cycles at each rate.]]**

GITT was performed at 100 mA g−1 between 0.005 and 2.5 V using repeated 10 min current pulses followed by 60 min open-circuit relaxation. The current-off portions of the response were emphasized because the pulse-period voltage contains both polarization and the change in equilibrium potential associated with continued lithiation/delithiation.

For the early current interruption, the voltage between 3 and 30 s after switching the current off was represented as

E(t) = a + b√t,

and the intercept a was extrapolated to t → 0. The corresponding current-off voltage jump was divided by the absolute applied current to obtain an apparent instantaneous current-off resistance. This quantity is used as an experimental descriptor and is not assigned uniquely to ohmic resistance.

The finite-window relaxation amplitude was defined as

ΔErelax = E60min − Eoff,3s,

with absolute magnitude used for comparison where appropriate. Model-free t50, t63, and t90 values were defined as the times required to reach 50%, 63.2%, and 90% of the observed 3 s-to-60 min relaxation amplitude. These quantities do not assume single-exponential relaxation; t63 equals a conventional time constant only for an ideal single exponential.

The late-stage excess relaxation feature was quantified after subtracting a common smooth background from ΔErelax as a function of cumulative capacity. Peak amplitude, FWHM-like capacity width, and the capacity-weighted excess-polarization area were extracted using the same procedure for all samples. The integrated quantity is used only as a comparative descriptor and is not interpreted as rigorous dissipated energy because ΔErelax is sampled at discrete GITT states rather than measured as the continuous operating overpotential.

Cyclic voltammetry in the nominal non-faradaic region of 3.0–3.3 V was acquired at scan rates of 10, 20, 40, 60, 80, and 100 mV s−1 for relative interfacial-capacitance comparison. Previous calculations used a specific capacitance of 40 μF cm−2 to convert the double-layer capacitance to nominal electrochemically active surface area. Because this conversion is uncertain for a porous composite electrode, the present manuscript uses the result primarily as a relative interfacial-accessibility metric rather than an absolute physical ECSA.

**[[STUDENT TO CONFIRM: potentiostat model and detailed CV/EIS acquisition conditions before final Methods freeze.]]**

---

## 2.4. Spatial mechanism-sufficiency model

A reduced spatial phase-field model was used as a directional mechanism test rather than as a unique parameter-identification or quantitative voltage-fitting procedure. The model contains a conserved radial Li-state variable, c(r,t), and a nonconserved structural order parameter, phi(r,t), representing the late-stage transition-associated structural state. Values of phi near 0 denote a parent-like/pre-transition state and values near 1 denote a transformed-like state. The variable phi is therefore a modeled internal-state coordinate and is not interpreted as a directly measured experimental phase fraction.

Li transport was represented by diffusion driven by the Li chemical-potential gradient, while structural evolution followed dissipative relaxation of the phase-field free energy. Mg incorporation was represented through an explicit stabilization term for the parent/intermediate state together with reduced residual structural mobility. Ball-milled samples were represented using a distribution of local transition/surface conditions and structural mobilities. The BM-HEO and BM-Mg-HEO calculations used 11 equal-probability quantiles of the frozen ensemble distribution rather than a single deterministic particle.

The numerical protocol reproduced the experimental timing of 600 s galvanostatic perturbation followed by 3600 s zero-flux relaxation over a refined sequence of model states. Model outputs were evaluated through volume-averaged and surface chemical-potential readouts, and the accepted parameter set was required only to reproduce the experimentally observed directional relationships among transition-polarization amplitude, transformation width, characteristic relaxation, and final transformed-state proxy. Detailed equations, parameters, sensitivity tests, numerical convergence, and identifiability limitations are provided in the Supporting Information. The model is used in the main text only to test mechanistic sufficiency and to visualize internal-state evolution consistent with the experimental constraints.

---

# 3. Results and Discussion

---

## 3.1. Synthesis-dependent structure and morphology

The four samples form a 2 × 2 comparison that separates composition from mechanical processing. HEO and BM-HEO isolate the effect of milling in the Mg-free composition, whereas Mg-HEO and BM-Mg-HEO provide the corresponding comparison after Mg incorporation. This design is important because the two variables produce different electrochemical consequences rather than a common monotonic change in performance.

The XRD patterns are dominated by reflections characteristic of the cubic spinel-type HEO. Mg incorporation produces a small shift of the principal reflection near 35.7° toward lower 2θ. Before ball milling, the peak position changes from approximately 35.76° for HEO to 35.70° for Mg-HEO, while the corresponding ball-milled samples shift from approximately 35.68° to 35.64°. If indexed as the cubic spinel (311) reflection, these shifts correspond to only ~0.1–0.2% expansion of the apparent cubic lattice parameter. The magnitude is therefore consistent with modest lattice expansion after Mg incorporation but does not independently establish Mg occupancy at a unique crystallographic site. Final lattice parameters and phase fractions should be taken from the collaborator group's refined XRD and ICP analysis.

Ball milling broadens the diffraction features while preserving the dominant spinel-like peak positions in the current patterns. This response is consistent with reduced coherent-domain size and/or increased microstrain and structural disorder produced by prolonged high-energy milling. Mechanical processing of spinel HEOs can alter more than particle size: high-energy milling has been reported to induce a spinel-to-rock-salt-like structural change in a related Mg-containing spinel HEO,[11] and progressive particle fragmentation in (FeCoNiCrMn)3O4 increases conversion reversibility and interfacial storage during cycling.[12] Structural disorder is therefore treated as an active variable in BM-HEO rather than a geometric by-product of particle refinement.

Electron microscopy confirms nanoscale structural heterogeneity and spatially distributed multication chemistry. EDS maps show Fe, Co, Ni, Cr, Mn, and O throughout the HEO particles and additionally detect Mg in the Mg-containing samples. The current HRTEM images show nanocrystalline spinel-related fringes, although final plane indexing remains under collaborator review. **[[COLLABORATOR TO INSERT: final HRTEM/SAED indexing, particle-size statistics, and any refined structural comparison that directly supports Mg incorporation or milling-induced disorder.]]**

The structural characterization therefore establishes two distinct perturbations before electrochemical cycling: Mg introduces a comparatively modest lattice-level modification while preserving the spinel-type parent structure, whereas ball milling produces a much stronger change in microstructure and surface area.

---

## 3.2. Ball milling increases electrochemical accessibility and utilization, whereas Mg limits accessible conversion

The BET surface area increases from 3.94 m² g−1 for HEO to 18.159 m² g−1 after ball milling, corresponding to a 4.61-fold increase. Mg-HEO has a surface area of 6.49 m² g−1, while BM-Mg-HEO reaches 16.64 m² g−1, a 2.56-fold increase relative to Mg-HEO. Thus, ball milling produces the dominant increase in physical surface area in both compositions, although the final BET areas of BM-HEO and BM-Mg-HEO are similar.

The interfacial-capacitance measurements show the same qualitative ordering. When converted using the same assumed specific capacitance, the nominal accessible-interface values increase from 4.18 to 30.17 cm² in the Mg-free pair and from 6.56 to 39.68 cm² in the Mg-containing pair. These values are not treated as absolute ECSA; their function is to corroborate the strong relative increase in electrochemically accessible interface after milling.

The enlarged interface is accompanied by greater first-cycle utilization. In the latest 2026-09-17 dataset, the first-cycle values recorded under the WonATech charge/discharge convention are 901.25/609.12 mAh g−1 for HEO and 1056.10/782.08 mAh g−1 for BM-HEO, corresponding to initial Coulombic efficiencies of 67.59% and 74.05%, respectively. Ball milling therefore increases the two first-cycle capacity measures by approximately 17% and 28% in the Mg-free pair. Mg-HEO and BM-Mg-HEO deliver 731.15/458.91 and 944.07/580.83 mAh g−1, respectively, with initial Coulombic efficiencies of 62.77% and 61.52%. Ball milling also increases the first-cycle capacity measures in the Mg-containing pair by approximately 29% and 27%, whereas Mg incorporation lowers capacity relative to the Mg-free compositions. **[[Before submission, verify the WonATech charge/discharge labels against lithiation/delithiation direction and replace the terminology consistently.]]**

These data separate the primary effects of the two synthesis variables. Milling increases accessible capacity in both compositions, consistent with the substantially enlarged surface area and electrochemically accessible interface. Mg incorporation has the opposite effect on capacity despite increasing the BET area of the unmilled powder from 3.94 to 6.49 m² g−1. The capacity decrease after Mg incorporation therefore cannot be explained by loss of external surface area or reduced electrode/electrolyte contact and instead points to a change in reaction pathway or reaction extent.

The cycling data show that accessibility and interphase stability must be considered together. Under the common electrolyte containing 10 wt% FEC, BM-HEO maintains a higher absolute capacity than HEO over 100 cycles, while both Mg-containing electrodes operate at lower capacity. In control cells without FEC, BM-HEO shows stronger capacity decay than HEO. This sensitivity is consistent with the much larger surface area and interface created by milling, which can increase both conversion utilization and electrolyte-derived surface reactions. FEC mitigates this penalty and is therefore treated as a standardized interphase-control condition rather than as an independent mechanistic variable. The relevance of FEC-containing electrolytes to HEO anodes is also supported by recent systematic HEO studies showing that FEC composition can strongly alter interphase chemistry and long-term electrochemical response.[14]

The rate-capability data provide a second constraint. BM-HEO maintains a higher absolute capacity than HEO across the tested C-rate sequence and recovers the higher capacity when the rate returns to 0.1 C. The capacity enhancement produced by milling therefore does not require faster long-time relaxation. Rate capability under continuous galvanostatic drive and post-pulse relaxation during a 60 min current interruption probe different aspects of the electrode response. This distinction becomes central in the GITT analysis.

Post-cycle microscopy further shows substantial surface reconstruction in both HEO and BM-HEO, consistent with the fact that repeated conversion does not occur in a morphologically invariant composite. These images are used only as qualitative support because they do not establish interphase composition. Cycling EIS likewise shows strong state/history dependence, but several spectra are unstable or outlying and the dataset is therefore retained in the Supporting Information rather than reduced to a central equivalent-circuit parameter series.

---

## 3.3. Current interruption separates polarization magnitude from relaxation time

The larger capacity of BM-HEO does not coincide with uniformly lower current-off polarization or faster relaxation. During the 10 min GITT pulse, the measured voltage contains both polarization and the change in equilibrium potential associated with continued lithiation. Once the current is interrupted, additional imposed charge insertion stops and the subsequent voltage evolution provides a cleaner measure of relaxation of the nonequilibrium state created by the pulse. The current-off response was therefore analyzed directly rather than reduced only to a conventional apparent diffusion coefficient.

The early 3–30 s response is highly linear with √t, with median coefficients of determination of approximately 0.996–0.999 across the four samples. Extrapolation to t → 0 therefore provides a reproducible empirical current-interruption descriptor. Below 200 mAh g−1, the median apparent current-off resistance is 308 Ω for HEO and 593 Ω for BM-HEO, indicating a pronounced early first-lithiation penalty after milling. The corresponding values are much smaller for Mg-HEO and BM-Mg-HEO, 44 and 94 Ω, respectively. The large initial response of BM-HEO is therefore concentrated in the early formation/activation region rather than representing a persistent resistance penalty.

Over the common 200–800 mAh g−1 interval, HEO and BM-HEO exhibit nearly identical median apparent fast current-off resistances of 106.4 and 106.5 Ω, respectively. Mg incorporation reduces the same descriptor to 40.2 Ω for Mg-HEO and 33.0 Ω for BM-Mg-HEO. Thus, the additional capacity of BM-HEO does not originate from a uniform decrease in the fast current-off resistance, while the substantially lower fast polarization of the Mg-containing electrodes does not produce higher capacity.

The longer-time relaxation creates an even stronger contrast. Over 200–800 mAh g−1, the median 3 s-to-60 min relaxation amplitudes are 160.9, 176.3, 109.5, and 144.3 mV for HEO, BM-HEO, Mg-HEO, and BM-Mg-HEO, respectively. The corresponding model-free t63 values are 8.68, 11.57, 11.01, and 12.99 min. Ball milling therefore increases electrochemical utilization while lengthening the characteristic post-pulse relaxation. More importantly, Mg lowers the relaxation amplitude but does not shorten the characteristic time. Relative to HEO, Mg-HEO decreases the median relaxation amplitude by ~32% while increasing t63 by ~27%.

If a single diffusion coefficient were the dominant synthesis-dependent variable under otherwise comparable pulse conditions, polarization amplitude and relaxation time would be expected to change in the same direction: faster diffusion should reduce both diffusion-associated concentration polarization and the characteristic diffusion-relaxation time. Mg-HEO instead shows the opposite combination, with a much smaller relaxation amplitude but a longer t63 than HEO. Diffusion can still contribute to the transient, but a single-D interpretation cannot account for the synthesis dependence of the current-off response. The explicit scaling test used to illustrate this contradiction is retained in the Supporting Information.

---

## 3.4. Ball milling redistributes the late-stage transformation, whereas Mg suppresses its extent

The state dependence of ΔErelax provides a more specific mechanistic signature than an average kinetic parameter. In pristine HEO, the relaxation amplitude decreases after the early first-lithiation response and then develops a pronounced late-stage hump, with the strongest excess response occurring in the approximate 0.6–0.4 V range of the relaxed GITT trajectory (Figure 4a). A similarly concentrated feature is not observed after ball milling and is strongly suppressed in both Mg-containing electrodes.

The late-stage excess response is assigned primarily to the spinel-to-rock-salt/conversion transformation. Atomic-scale and in-situ studies establish extensive structural reconstruction of Fe–Co–Cr–Mn–Ni spinel HEOs during lithiation,[5] and a recent study on the same five-cation family directly resolved a sequence from spinel through mixed spinel/rock-salt to a rock-salt-dominated state.[7] Phase-transforming electrodes can exhibit additional overpotential associated with nucleation, phase-boundary propagation, strain accommodation, and structural reorganization.[17] The coincidence of the present excess response with the established low-voltage conversion region therefore supports a phase-transition contribution rather than a state-independent resistance alone.

A common background-subtraction procedure isolates the transition-associated excess response (Figure 4b). HEO exhibits a peak amplitude of 70.8 mV with an FWHM-like width of 354 mAh g−1. BM-HEO shows a lower peak of 44.1 mV but a broader width of 430 mAh g−1. Mg-HEO is strongly suppressed to 15.9 mV with a width of 250 mAh g−1, whereas BM-Mg-HEO shows a modest partial recovery to 21.1 mV and 392 mAh g−1. The corresponding normalized excess areas are approximately 22.1, 14.1, 4.94, and 7.58 mV, respectively. The capacity-weighted excess metric is used only for comparison and is not interpreted as dissipated energy. The peak–width map in Figure 4c makes the synthesis dependence explicit: ball milling moves the response toward a broader but less concentrated transition, whereas Mg moves it primarily toward strong suppression of the transition-associated amplitude.

The ball-milling response is consistent with increased accessibility together with a wider distribution of local transformation conditions. The large increase in BET area and relative interfacial capacitance, the higher capacity, and the broadened transition-associated response all point in the same direction. Milling-induced disorder, strain, shortened coherent domains, and additional interfaces can create a distribution of local nucleation and structural-relaxation environments. Particle refinement does not require a larger phase-transition overpotential; coherent phase-separation theory and recent HEO size-comparison studies instead show that increased surface contribution and reduced length scale can lower nucleation barriers or kinetic limitations.[18–20] Because the present BSE images do not establish ~15 nm primary particles, the present interpretation is limited to increased interface, reduced effective coherent-domain/transport length, and broader local transition conditions rather than a specific nanoscale particle size.

Mg incorporation produces a different electrochemical signature. The pronounced HEO transition feature is largely removed, accessible capacity decreases, and the characteristic current-off relaxation does not become faster. A simple transport-acceleration explanation is therefore incomplete. The minimum interpretation consistent with the data contains two coordinates: Mg stabilizes the parent/intermediate oxide-derived state and reduces the fraction entering the late-stage conversion pathway, while the residual transforming population retains slower structural mobility. This combination explains the lower conversion-associated capacity and much smaller transition polarization without requiring faster relaxation. The interpretation is consistent with prior reports in which electrochemically inactive Mg-containing components improve structural retention or stabilize oxide-derived states during conversion.[8–10]

BM-Mg-HEO provides an internal test of this separation. Milling increases the accessible interface and capacity of the Mg-containing composition and partially broadens/reopens the transition-associated response, but it does not restore the strong HEO-like peak. Processing can therefore increase accessibility without eliminating the stronger compositional constraint imposed by Mg on transformation extent.

---

## 3.5. Spatial modeling visualizes internal-state evolution compatible with the GITT constraints

The experimental data impose several directional constraints that a physically coherent model should satisfy simultaneously. BM-HEO must retain high transformation accessibility while showing a lower, broader transition-associated polarization and a longer ensemble relaxation. Mg-HEO must show a much smaller transition response and lower transformed fraction without a shorter relaxation time. These combinations cannot be represented coherently by changing only one diffusion coefficient or only one structural-mobility parameter.

A reduced spatial phase-field model was therefore used as a mechanism-sufficiency test rather than as a unique parameter-identification procedure (Figure 5a). The model couples a conserved radial Li-state variable c(r,t) to a nonconserved late-stage structural order parameter φ(r,t). Three physical coordinates are allowed to vary independently: the transport scale, transformation stabilization/extent, and the distribution of local transition conditions and structural mobilities. Mg is represented primarily through stabilization of the parent/intermediate state together with lower residual structural mobility. Ball-milled samples are represented by an ensemble distribution of local transition/surface conditions and structural mobilities.

The frozen model reproduces the required four-sample ordering without assigning the fitted coordinates as unique material constants. The circular maps in Figure 5b show the radial φ state at the end of the 600 s pulse across a common late-stage model window. HEO develops the transformed state over a comparatively concentrated interval. BM-HEO begins the transition earlier and distributes it more broadly in model state. Mg-HEO remains predominantly parent-like over most of the same window, whereas BM-Mg-HEO shows partial reopening of the transformation pathway at higher state. For the ball-milled samples, each circle is an ensemble-averaged radial state over the frozen 11-quantile distribution and is not a simulated two-dimensional heterogeneous particle.

The mean structural-state trajectories in Figure 5c summarize the same distinction. Ball milling broadens the progression toward the transformed state, Mg strongly suppresses the transformation, and BM-Mg-HEO partially recovers transformation at high model state while remaining below the Mg-free response over much of the window. The model therefore demonstrates that the experimental observations are mutually compatible when transformation extent/stabilization and structural-mobility/transition-condition heterogeneity are treated as independent coordinates. The modeled φ is not a measured phase fraction, c̄ is not directly calibrated to experimental normalized capacity, and the parameter set is non-unique. Detailed parameter values, numerical convergence, sensitivity tests, and the modeled structural change during the subsequent 60 min rest are therefore retained in the Supporting Information.

Taken together, Figures 1–5 separate three experimentally distinct synthesis consequences: accessibility, transformation extent/distribution, and relaxation time. Ball milling primarily increases accessibility and redistributes the phase-transforming reaction, whereas Mg primarily suppresses its extent through structural stabilization. Relaxation time follows neither capacity nor polarization amplitude monotonically. This separation explains why the electrochemical consequences of synthesis in a phase-evolving HEO electrode cannot be reduced to a single apparent GITT diffusivity.

---

# 4. Conclusions

Spinel Fe–Co–Ni–Cr–Mn HEO anodes and their ball-milled and Mg-containing derivatives were compared using a 2 × 2 composition/process design. Ball milling strongly increases physical and electrochemically accessible interface and raises capacity, but the higher utilization is not accompanied by uniformly lower current-off polarization or faster relaxation. Instead, the late-stage transformation-associated response becomes lower in peak amplitude and broader in capacity while the long-rest characteristic time increases. Ball milling therefore acts primarily by increasing accessibility and redistributing the phase-transforming reaction rather than by producing a simple uniform increase in Li diffusivity.

Mg incorporation produces a different trade-off. Accessible capacity and the late-stage transition-associated polarization both decrease, whereas the characteristic relaxation time does not become shorter. This combination is inconsistent with a simple transport-acceleration picture and instead supports reduced conversion extent through stabilization of the parent/intermediate oxide-derived state, together with slower residual structural mobility. BM-Mg-HEO partially recovers accessibility and transformation under milling but does not restore the concentrated Mg-free transition response.

The spatial mechanism-sufficiency model shows that these experimentally observed directions are physically compatible when transformation stabilization/extent and structural-mobility/transition-condition heterogeneity are allowed to vary independently. The central result is therefore not a unique microscopic parameter set, but the separation of accessibility, transformation extent/distribution, and relaxation time as distinct coordinates of a phase-evolving electrode. This distinction provides a more direct synthesis–electrochemistry connection than interpretation based on a single apparent GITT diffusion coefficient.

---

# References

1. Rost, C. M.; Sachet, E.; Borman, T.; Moballegh, A.; Dickey, E. C.; Hou, D.; Jones, J. L.; Curtarolo, S.; Maria, J.-P. Entropy-stabilized oxides. **Nature Communications** 2015, 6, 8485. DOI: 10.1038/ncomms9485.

2. Sarkar, A.; Velasco, L.; Wang, D.; Wang, Q.; Talasila, G.; de Biasi, L.; Kübel, C.; Brezesinski, T.; Bhattacharya, S. S.; Hahn, H.; Breitung, B. High entropy oxides for reversible energy storage. **Nature Communications** 2018, 9, 3400. DOI: 10.1038/s41467-018-05774-5.

3. Dąbrowa, J.; Stygar, M.; Mikuła, A.; Knapik, A.; et al. Synthesis and microstructure of the (Co,Cr,Fe,Mn,Ni)3O4 high entropy oxide characterized by spinel structure. **Materials Letters** 2018, 216, 32–36. DOI: 10.1016/j.matlet.2017.12.148.

4. Wang, D.; Jiang, S.; Duan, C.; Mao, J.; Dong, Y.; Dong, K.; Wang, Z.; Luo, S.; Liu, Y.; Qi, X. Spinel-structured high entropy oxide (FeCoNiCrMn)3O4 as anode towards superior lithium storage performance. **Journal of Alloys and Compounds** 2020, 844, 156158. DOI: 10.1016/j.jallcom.2020.156158.

5. Huang, C.-Y.; Huang, C.-W.; Wu, M.-C.; Patra, J.; Nguyen, T. X.; Chang, M.-T.; Clemens, O.; Ting, J.-M.; Li, J.; Chang, J.-K.; Wu, W.-W. Atomic-scale investigation of lithiation/delithiation mechanism in high-entropy spinel oxide with superior electrochemical performance. **Chemical Engineering Journal** 2021, 420, 129838. DOI: 10.1016/j.cej.2021.129838.

6. Xiao, B.; Wu, G.; Wang, T.; Wei, Z.; Sui, Y.; Shen, B.; Qi, J.; Wei, F.; Zheng, J. High-entropy oxides as advanced anode materials for long-life lithium-ion batteries. **Nano Energy** 2022, 95, 106962. DOI: 10.1016/j.nanoen.2022.106962.

7. Jin, G.; Luo, C.; Wang, Z.; Jia, S.; Yu, H.; Zhang, C.; Wang, Q.; Zhang, B.; Wang, Z. Unraveling phase transition pathway of spinel (FeCoCrNiMn)3O4 high-entropy oxide anodes for long-life Li-ion batteries. **Materials Today Chemistry** 2025, 48, 102949. DOI: 10.1016/j.mtchem.2025.102949.

8. Qiu, N.; Chen, H.; Yang, Z.; Sun, S.; Wang, Y.; Cui, Y. A high entropy oxide (Mg0.2Co0.2Ni0.2Cu0.2Zn0.2O) with superior lithium storage performance. **Journal of Alloys and Compounds** 2019, 777, 767–774. DOI: 10.1016/j.jallcom.2018.11.049.

9. Wang, S.-Y.; Chen, T.-Y.; Kuo, C.-H.; Lin, C.-C.; Huang, S.-C.; Lin, M.-H.; Wang, C.-C.; Chen, H.-Y. Operando synchrotron transmission X-ray microscopy study on (Mg, Co, Ni, Cu, Zn)O high-entropy oxide anodes for lithium-ion batteries. **Materials Chemistry and Physics** 2021, 274, 125105. DOI: 10.1016/j.matchemphys.2021.125105.

10. Wang, K.; Hua, W.; Huang, X.; Stenzel, D.; Wang, J.; Ding, Z.; Cui, Y.; Wang, Q.; Ehrenberg, H.; Breitung, B.; Kübel, C.; Mu, X. Synergy of cations in high entropy oxide lithium ion battery anode. **Nature Communications** 2023, 14, 1487. DOI: 10.1038/s41467-023-37034-6.

11. Zheng, Y.; Wu, X.; Lan, X.; Hu, R. A Spinel (FeNiCrMnMgAl)3O4 High Entropy Oxide as a Cycling Stable Anode Material for Li-Ion Batteries. **Processes** 2022, 10, 49. DOI: 10.3390/pr10010049.

12. Zhai, F.; Zhu, X.; Zhang, W.; Cao, G.; Zhang, H.; Xing, Y.; Xiang, Y.; et al. Insight of the evolution of structure and energy storage mechanism of (FeCoNiCrMn)3O4 spinel high entropy oxide in life-cycle span as lithium-ion battery anode. **Journal of Power Sources** 2024, 603, 234418. DOI: 10.1016/j.jpowsour.2024.234418.

13. Wang, X. L.; Jin, E. M.; Sahoo, G.; Jeong, S. M. High-Entropy Metal Oxide (NiMnCrCoFe)3O4 Anode Materials with Controlled Morphology for High-Performance Lithium-Ion Batteries. **Batteries** 2023, 9, 147. DOI: 10.3390/batteries9030147.

14. Patra, J.; Nguyen, T. X.; Panda, A.; Ting, J. M.; Dhaka, R. S.; Liu, W. R.; Yang, C. C.; Chang, J. K. Fluoroethylene carbonate electrolyte additive for improved charge-discharge performance of Co-free high entropy spinel oxide anodes for lithium-ion batteries. **Ceramics International** 2025, 51, 22628–22638. DOI: 10.1016/j.ceramint.2024.12.003.

15. Jia, M.; Zhang, W.; Cai, X.; Zhan, X.; Hou, L.; Yuan, C.; Guo, Z. Re-understanding the galvanostatic intermittent titration technique: Pitfalls in evaluation of diffusion coefficients and rational suggestions. **Journal of Power Sources** 2022, 543, 231843. DOI: 10.1016/j.jpowsour.2022.231843.

16. Chien, Y.-C.; Liu, H.; Menon, A. S.; Brant, W. R.; Brandell, D.; Lacey, M. J. Rapid determination of solid-state diffusion coefficients in Li-based batteries via intermittent current interruption method. **Nature Communications** 2023, 14, 2289. DOI: 10.1038/s41467-023-37989-6.

17. Komayko, A. I.; Nazarov, E. E.; Tyablikov, O. A.; Fedotov, S. S.; Antipov, E. V.; Nikitina, V. A. Unraveling the contribution of nucleation to the intercalation energy barrier for phase-transforming Li-ion battery materials. **Journal of Power Sources** 2024, 624, 235589. DOI: 10.1016/j.jpowsour.2024.235589.

18. Cogswell, D. A.; Bazant, M. Z. Coherency Strain and the Kinetics of Phase Separation in LiFePO4 Nanoparticles. **ACS Nano** 2012, 6, 2215–2225. DOI: 10.1021/nn204177u.

19. Cogswell, D. A.; Bazant, M. Z. Theory of Coherent Nucleation in Phase-Separating Nanoparticles. **Nano Letters** 2013, 13, 3036–3041. DOI: 10.1021/nl400497t.

20. Li, K.; Shi, L.; An, J.; Zhang, M.; Du, Y.; Ma, Y.; Lou, S.; Yin, G.; Yu, Z.; Hua, X.; Huo, H. Stabilizing Configurational Entropy in Spinel-type High Entropy Oxides during Discharge–Charge by Overcoming Kinetic Sluggish Diffusion. **Angewandte Chemie International Edition** 2025, 64, e202518569. DOI: 10.1002/anie.202518569.

---

---

# Figure Captions

**Figure 1. Structural and microstructural perturbations introduced by Mg incorporation and ball milling.** The four-sample matrix separates compositional and mechanical-processing effects. X-ray diffraction, microscopy, elemental analysis, and surface-area measurements establish the parent spinel-type structure, Mg-associated structural modification, and the strong increase in interface/microstructural disorder produced by ball milling. Final panel assignments should follow the collaborator-verified XRD/HRTEM/SAED/ICP dataset.

**Figure 2. Electrochemical accessibility and utilization of HEO, BM-HEO, Mg-HEO, and BM-Mg-HEO.** BET area and relative interfacial-capacitance metrics are compared with first-cycle capacity, cycling behavior, and rate capability. Ball milling increases accessible interface and capacity in both compositions, whereas Mg lowers accessible conversion capacity despite not reducing external surface area. The Cdl-derived interface metric is used comparatively and is not interpreted as absolute ECSA.

**Figure 3. Current interruption separates polarization magnitude from relaxation time.** A representative GITT pulse/rest defines the apparent fast current-off response, the 3 s-to-60 min relaxation amplitude ΔErelax, and the model-free t63. State-resolved comparisons show that BM-HEO maintains nearly the same intermediate-capacity apparent fast current-off resistance as HEO but relaxes more slowly, while Mg-containing electrodes show much lower polarization amplitudes without shorter relaxation times. The opposite changes in amplitude and time rule out a simple single-diffusivity explanation of the synthesis dependence.

**Figure 4. Ball milling redistributes the late-stage transition-associated polarization, whereas Mg suppresses its extent.** (a) State-resolved ΔErelax with the relaxed-voltage trajectory identifying the low-voltage conversion region. (b) Background-subtracted transition-associated excess relaxation obtained using a common procedure for all four samples. (c) Peak-amplitude versus FWHM-like width map, with marker area proportional to the normalized excess area. Ball milling produces a broader but less concentrated response, whereas Mg strongly suppresses the transition-associated amplitude; BM-Mg-HEO shows only partial recovery. The integrated excess metric is comparative and is not interpreted as dissipated energy.

**Figure 5. Spatial modeling visualizes distinct late-stage internal-state evolution compatible with the experimental GITT constraints.** (a) Mechanism-sufficiency model linking the experimental constraints to independent coordinates for transport, transformation stabilization/extent, and local-transition/structural-mobility heterogeneity. (b) Circular radial maps of the pulse-end structural order parameter φ across a common late-stage model window for HEO, BM-HEO, Mg-HEO, and BM-Mg-HEO. For ball-milled samples, each circle is an ensemble-averaged radial state over the frozen 11-quantile distribution. (c) Pulse-end mean structural state φ̄ versus model mean lithiation state c̄. The model is directional and non-unique: φ is not a directly measured phase fraction and c̄ is not directly calibrated to experimental normalized capacity.