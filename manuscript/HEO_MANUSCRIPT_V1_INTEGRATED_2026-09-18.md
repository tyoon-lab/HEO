# HEO Manuscript v1 — Integrated Draft

**Date:** 2026-09-18  
**Status:** Integrated working manuscript  
**Source priority:** 2026-09-17 electrochemical summary + raw GITT reanalysis + Yoo-group synthesis/characterization draft  
**Writing mode:** Yoon Lab Publication Toolkit / STRICT MODE

> Verified information is written directly. Experimental details that remain unavailable are marked for collaborator/student confirmation rather than inferred from literature.

---

# Recommended title

**Contrasting Roles of Mg Incorporation and Ball Milling in Spinel High-Entropy Oxide Anodes: Phase Evolution, Polarization, and Electrochemical Utilization**

Alternative, more compact title:

**Mg Incorporation and Ball Milling Regulate Phase-Transformation Polarization in Spinel High-Entropy Oxide Anodes**

---

# Abstract

Spinel high-entropy oxides (HEOs) provide high-capacity conversion-type lithium storage, but synthesis-dependent changes in electrochemical utilization are often interpreted through a single apparent transport parameter even when the host structure evolves during reaction. Here, spinel Fe–Co–Ni–Cr–Mn HEO, ball-milled HEO (BM-HEO), Mg-containing HEO (Mg-HEO), and ball-milled Mg-HEO (BM-Mg-HEO) are compared to separate the effects of mechanical processing and compositional stabilization. Ball milling increases the BET surface area of the Mg-free HEO from 3.94 to 18.159 m² g⁻¹ and increases capacity across the tested rate range. However, this higher utilization does not coincide with faster post-pulse relaxation: over 200–800 mAh g⁻¹, HEO and BM-HEO show nearly identical apparent fast current-off resistances of 106.4 and 106.5 Ω, whereas the model-free t63 increases from 8.68 to 11.57 min after milling. The late-stage excess polarization assigned primarily to the spinel-to-rock-salt/conversion transformation simultaneously decreases in peak amplitude from 70.8 to 44.1 mV and broadens from 354 to 430 mAh g⁻¹. Mg incorporation produces the opposite electrochemical trade-off. Mg-HEO exhibits lower accessible capacity and a strongly suppressed transition-associated excess peak of ~16 mV, while t63 increases to 11.01 min rather than becoming shorter. The reduced polarization therefore cannot be explained by uniformly faster Li transport and is instead attributed predominantly to suppression of the conversion-phase transformation through structural stabilization. Ball milling thus regulates electrochemical accessibility and the distribution of the phase-transforming reaction, whereas Mg primarily regulates its extent. Separating polarization magnitude, relaxation time, and capacity reveals synthesis–electrochemistry relationships that are obscured when the response is reduced to a single apparent diffusivity.

**Keywords:** high-entropy oxide; spinel anode; lithium-ion battery; ball milling; magnesium incorporation; phase transformation; GITT; current interruption; polarization relaxation

---

# 1. Introduction

High-entropy oxides (HEOs) extend the high-entropy concept to multication ceramic compounds, where several principal cations share a crystallographic sublattice and create compositionally complex single-phase structures.[1] Since the initial demonstration of entropy-stabilized oxides, HEOs have been explored for ionic conduction, catalysis, and electrochemical energy storage.[1,2] Their relevance to lithium-ion battery anodes is particularly strong because multiple transition-metal cations can provide high conversion capacity while chemically diverse cations can modify structural stability, electronic connectivity, and the morphology of the reacted state.[2] Spinel (Co,Cr,Fe,Mn,Ni)3O4 and compositionally equivalent Fe–Co–Ni–Cr–Mn oxides have emerged as a representative HEO anode family with a single-phase Fd-3m structure and high reversible lithium-storage capacity.[3–6]

Lithium storage in these spinel HEOs is not adequately described as diffusion through an invariant host. Atomic-scale and in-situ structural studies show extensive reconstruction during lithiation and delithiation, including reduction of transition-metal species, formation of nanoscale metallic/oxide regions, and conversion between spinel- and rock-salt-related structures.[5,7] A recent in-situ XRD/ex-situ TEM study on the same five-cation spinel family directly resolved a lithiation sequence from spinel to mixed spinel/rock-salt and finally to a rock-salt-dominated state.[7] These transformations provide substantial charge storage but also introduce electrochemical penalties associated with nucleation, phase-boundary propagation, strain accommodation, and structural reorganization. Consequently, a synthesis change can alter capacity not only by modifying Li transport distance or interfacial resistance, but also by changing how much material undergoes conversion and how broadly the transformation is distributed over state of charge.

Ball milling and Mg incorporation provide two physically different ways to perturb this reaction. Ball milling enlarges surface area, generates fresh interfaces, and introduces strain and local structural disorder. In spinel HEOs, high-energy milling has been shown to perturb the spinel/rock-salt structural balance, while particle fragmentation during cycling increases conversion reversibility and interfacial storage before excessive interfacial reconstruction contributes to degradation.[11,12] Mg-containing conversion-type HEOs show a different role. Electrochemically inactive Mg-derived oxide can act as a spectator or stabilizing component,[8] operando transmission X-ray microscopy shows improved structural retention with increasing Mg content,[9] and atomic/nanoscale studies of rock-salt HEOs show that electrochemically inactive cations can stabilize an oxide nanophase during conversion.[10] These precedents suggest a potential trade-off: increasing accessibility may increase the fraction of material that reacts, whereas structural stabilization may reduce the extent of conversion and therefore reduce both polarization and capacity.

This distinction is difficult to resolve when galvanostatic intermittent titration technique (GITT) data are reduced only to an apparent Li-ion diffusion coefficient. Conventional GITT analysis remains useful as a comparative descriptor, but its physical interpretation depends on diffusion geometry, time-window selection, equilibrium assumptions, and the absence of major structural complications.[6,15] These conditions are nontrivial in a phase-evolving conversion electrode. Current interruption preserves additional information. The early voltage response after switching off the current can be represented through an intercept and a sqrt(t) contribution under the semi-infinite diffusion approximation,[16] whereas the subsequent relaxation amplitude and characteristic time can be measured without assuming a single exponential. Phase-transforming electrodes are especially relevant because nucleation itself can constitute a substantial material-level overpotential.[17] Separating polarization magnitude from relaxation time therefore provides a direct way to test whether a synthesis-induced decrease in polarization actually reflects faster transport or instead reflects a change in reaction extent.

This study uses a 2 × 2 material/process comparison—HEO, BM-HEO, Mg-HEO, and BM-Mg-HEO—to determine how ball milling and Mg incorporation modify lithium storage in a spinel HEO anode. Structural and surface characterization is combined with galvanostatic cycling, rate tests, and direct analysis of the current-off portions of 10 min GITT pulses followed by 60 min relaxation. Ball milling increases electrochemical accessibility and capacity while broadening the late-stage transformation-associated polarization and slowing the long-rest response. Mg incorporation instead suppresses the late-stage polarization feature and conversion capacity without shortening the relaxation time. A spatial mechanism-sufficiency model reproduces these directional trends when transformation extent/stabilization and structural-mobility/transition-condition heterogeneity are treated as independent coordinates, and visualizes their distinct late-stage internal-state evolution. The combined results distinguish two synthesis coordinates: ball milling regulates accessibility and the distribution of the phase-transforming reaction, whereas Mg predominantly reduces the extent of the transformation through structural stabilization.

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

# 3. Results and Discussion

## 3.1. Synthesis-dependent structure and morphology

The four samples form a 2 × 2 comparison that separates composition from mechanical processing. HEO and BM-HEO isolate the effect of milling in the Mg-free composition, whereas Mg-HEO and BM-Mg-HEO provide the corresponding comparison after Mg incorporation. This design is important because the two variables produce different electrochemical consequences rather than a common monotonic change in performance.

The XRD patterns are dominated by reflections characteristic of the cubic spinel-type HEO. Mg incorporation produces a small shift of the principal reflection near 35.7° toward lower 2θ. Before ball milling, the peak position changes from approximately 35.76° for HEO to 35.70° for Mg-HEO, while the corresponding ball-milled samples shift from approximately 35.68° to 35.64°. If indexed as the cubic spinel (311) reflection, these shifts correspond to only ~0.1–0.2% expansion of the apparent cubic lattice parameter. The magnitude is therefore consistent with modest lattice expansion after Mg incorporation but does not independently establish Mg occupancy at a unique crystallographic site. Final lattice parameters and phase fractions should be taken from the collaborator group's refined XRD and ICP analysis.

Ball milling broadens the diffraction features while preserving the dominant spinel-like peak positions in the current patterns. This response is consistent with reduced coherent-domain size and/or increased microstrain and structural disorder produced by prolonged high-energy milling. Mechanical processing of spinel HEOs can alter more than particle size: high-energy milling has been reported to induce a spinel-to-rock-salt-like structural change in a related Mg-containing spinel HEO,[11] and progressive particle fragmentation in (FeCoNiCrMn)3O4 increases conversion reversibility and interfacial storage during cycling.[12] Structural disorder is therefore treated as an active variable in BM-HEO rather than a geometric by-product of particle refinement.

Electron microscopy confirms nanoscale structural heterogeneity and spatially distributed multication chemistry. EDS maps show Fe, Co, Ni, Cr, Mn, and O throughout the HEO particles and additionally detect Mg in the Mg-containing samples. The current HRTEM images show nanocrystalline spinel-related fringes, although final plane indexing remains under collaborator review. **[[COLLABORATOR TO INSERT: final HRTEM/SAED indexing, particle-size statistics, and any refined structural comparison that directly supports Mg incorporation or milling-induced disorder.]]**

The structural characterization therefore establishes two distinct perturbations before electrochemical cycling: Mg introduces a comparatively modest lattice-level modification while preserving the spinel-type parent structure, whereas ball milling produces a much stronger change in microstructure and surface area.

## 3.2. Ball milling increases electrochemical accessibility, whereas Mg lowers accessible conversion capacity

The BET surface area increases from 3.94 m² g−1 for HEO to 18.159 m² g−1 after ball milling, corresponding to a 4.61-fold increase. Mg-HEO has a surface area of 6.49 m² g−1, while BM-Mg-HEO reaches 16.64 m² g−1, a 2.56-fold increase relative to Mg-HEO. Thus, ball milling produces the dominant increase in physical surface area in both compositions, although the final BET areas of BM-HEO and BM-Mg-HEO are similar.

The interfacial-capacitance measurements show the same qualitative ordering. When converted using the same assumed specific capacitance, the nominal accessible-interface values increase from 4.18 to 30.17 cm² in the Mg-free pair and from 6.56 to 39.68 cm² in the Mg-containing pair. These values are not treated as absolute ECSA; their function is to corroborate the strong relative increase in electrochemically accessible interface after milling.

The enlarged interface is accompanied by greater first-cycle utilization. In the latest 2026-09-17 dataset, the first-cycle values recorded under the WonATech charge/discharge convention are 901.25/609.12 mAh g−1 for HEO and 1056.10/782.08 mAh g−1 for BM-HEO, corresponding to initial Coulombic efficiencies of 67.59% and 74.05%, respectively. Ball milling therefore increases the two first-cycle capacity measures by approximately 17% and 28% in the Mg-free pair. Mg-HEO and BM-Mg-HEO deliver 731.15/458.91 and 944.07/580.83 mAh g−1, respectively, with initial Coulombic efficiencies of 62.77% and 61.52%. Ball milling also increases the first-cycle capacity measures in the Mg-containing pair by approximately 29% and 27%, whereas Mg incorporation lowers capacity relative to the Mg-free compositions. **[[Before submission, verify the WonATech charge/discharge labels against lithiation/delithiation direction and replace the terminology consistently.]]**

These data separate the primary effects of the two synthesis variables. Milling increases accessible capacity in both compositions, consistent with the substantially enlarged surface area and electrochemically accessible interface. Mg incorporation has the opposite effect on capacity despite increasing the BET area of the unmilled powder from 3.94 to 6.49 m² g−1. The capacity decrease after Mg incorporation therefore cannot be explained by loss of external surface area or reduced electrode/electrolyte contact and instead points to a change in reaction pathway or reaction extent.

The cycling data show that accessibility and interphase stability must be considered together. Under the common electrolyte containing 10 wt% FEC, BM-HEO maintains a higher absolute capacity than HEO over 100 cycles, while both Mg-containing electrodes operate at lower capacity. In control cells without FEC, BM-HEO shows stronger capacity decay than HEO. This sensitivity is consistent with the much larger surface area and interface created by milling, which can increase both conversion utilization and electrolyte-derived surface reactions. FEC mitigates this penalty and is therefore treated as a standardized interphase-control condition rather than as an independent mechanistic variable. The relevance of FEC-containing electrolytes to HEO anodes is also supported by recent systematic HEO studies showing that FEC composition can strongly alter interphase chemistry and long-term electrochemical response.[14]

The rate-capability data provide a second constraint. BM-HEO maintains a higher absolute capacity than HEO across the tested C-rate sequence and recovers the higher capacity when the rate returns to 0.1 C. The capacity enhancement produced by milling therefore does not require faster long-time relaxation. Rate capability under continuous galvanostatic drive and post-pulse relaxation during a 60 min current interruption probe different aspects of the electrode response. This distinction becomes central in the GITT analysis.

## 3.3. Current interruption separates polarization magnitude from relaxation time

The larger capacity of BM-HEO does not coincide with uniformly lower current-off polarization or faster relaxation. During the 10 min GITT pulse, the measured voltage contains both polarization and the change in equilibrium potential associated with continued lithiation. Once the current is interrupted, additional imposed charge insertion stops and the subsequent voltage evolution provides a cleaner measure of relaxation of the nonequilibrium state created by the pulse. The current-off response was therefore analyzed directly rather than reduced only to a conventional apparent diffusion coefficient.

The early 3–30 s response is highly linear with √t, with median coefficients of determination of approximately 0.996–0.999 across the four samples. Extrapolation to t → 0 therefore provides a reproducible empirical current-interruption descriptor. Below 200 mAh g−1, the median apparent current-off resistance is 308 Ω for HEO and 593 Ω for BM-HEO, indicating a pronounced early first-lithiation penalty after milling. The corresponding values are much smaller for Mg-HEO and BM-Mg-HEO, 44 and 94 Ω, respectively. The large initial response of BM-HEO is therefore concentrated in the early formation/activation region rather than representing a persistent resistance penalty.

Over the common 200–800 mAh g−1 interval, HEO and BM-HEO exhibit nearly identical median apparent fast current-off resistances of 106.4 and 106.5 Ω, respectively. Mg incorporation reduces the same descriptor to 40.2 Ω for Mg-HEO and 33.0 Ω for BM-Mg-HEO. Thus, the additional capacity of BM-HEO does not originate from a uniform decrease in the fast current-off resistance, while the substantially lower fast polarization of the Mg-containing electrodes does not produce higher capacity.

The longer-time relaxation creates an even stronger contrast. Over 200–800 mAh g−1, the median 3 s-to-60 min relaxation amplitudes are 160.9, 176.3, 109.5, and 144.3 mV for HEO, BM-HEO, Mg-HEO, and BM-Mg-HEO, respectively. The corresponding model-free t63 values are 8.68, 11.57, 11.01, and 12.99 min. Ball milling therefore increases electrochemical utilization while lengthening the characteristic post-pulse relaxation. More importantly, Mg lowers the relaxation amplitude but does not shorten the characteristic time. Relative to HEO, Mg-HEO decreases the median relaxation amplitude by ~32% while increasing t63 by ~27%.

If the current-off response were governed predominantly by a single diffusion coefficient under otherwise comparable pulse conditions, the polarization amplitude and relaxation time would be expected to move in the same direction. A lower diffusivity produces a larger concentration gradient and therefore a larger diffusion-associated polarization, while the characteristic diffusion-relaxation time increases approximately with L²/D. Conversely, a higher diffusivity should reduce both the concentration-gradient polarization and the relaxation time. Mg-HEO shows the opposite combination: the median relaxation amplitude decreases from 160.9 to 109.5 mV, whereas t63 increases from 8.68 to 11.01 min. Using the common short-time scaling ηdiff ∝ D^−1/2 only as an illustrative limit, matching the Mg-induced amplitude decrease would require D/DHEO ≈ 2.16 and would predict t63 ≈ 4.0 min, while matching the observed t63 would require D/DHEO ≈ 0.79 and would predict a larger polarization of ≈181 mV. The contradiction in direction does not depend on the exact power-law exponent: any single-D description in which larger D reduces both diffusion polarization and diffusion-relaxation time cannot reproduce smaller polarization together with slower relaxation. Diffusion can still contribute to the transient, but it cannot by itself account for the late-stage synthesis dependence.

## 3.4. The late-stage polarization hump is assigned primarily to the spinel-to-rock-salt/conversion transition

The state dependence of ΔErelax provides a more specific mechanistic signature than an average kinetic parameter. In pristine HEO, the relaxation amplitude decreases after the early first-lithiation response and then rises progressively at high cumulative capacity, reaching approximately 189–193 mV near 800–830 mAh g−1 before decreasing again toward the lower voltage cutoff. The strongest excess response occurs in the approximate 0.6–0.4 V range of the relaxed GITT trajectory. A similarly concentrated late-stage hump is not observed in BM-HEO and is strongly suppressed in both Mg-containing electrodes.

The HEO hump is assigned primarily to the spinel-to-rock-salt/conversion phase transformation. Atomic-scale and in-situ studies establish substantial structural reconstruction of Fe–Co–Cr–Mn–Ni spinel HEOs during lithiation,[5] and a recent study on the same five-cation family directly resolved a sequence from spinel through mixed spinel/rock-salt to a rock-salt-dominated state.[7] In phase-transforming electrodes, nucleation and phase-boundary motion can contribute additional overpotential beyond simple diffusion through an invariant host.[17] The coincidence of the present excess polarization with the known low-voltage conversion region therefore makes phase evolution a more coherent explanation than a state-independent resistance or a monotonic change in a single solid-state diffusivity.

A common background-subtraction procedure was used to compare the shape of this excess feature. HEO exhibits an excess peak amplitude of 70.8 mV with an FWHM-like capacity width of 354 mAh g−1. After ball milling, the peak decreases to 44.1 mV while the width increases to 430 mAh g−1. The capacity-weighted excess-polarization metric decreases from 2.39 × 10⁴ to 1.79 × 10⁴ mV·mAh g−1. This integrated quantity is a comparative metric, not a thermodynamic energy. The lower peak and broader width show that milling does not simply remove the conversion transition. Instead, the transformation-associated polarization is distributed over a broader lithiation interval and becomes less concentrated at one state.

This response is consistent with the large increase in interface and with milling-induced disorder and local structural heterogeneity. Related spinel HEO literature shows that high-energy milling can directly perturb the spinel/rock-salt balance,[11] while particle refinement increases conversion reversibility and interfacial capacity in (FeCoNiCrMn)3O4.[12] The present data therefore support a picture in which milling increases the fraction of material that can be electrochemically accessed and broadens the population of local states participating in conversion. The result is higher capacity under load together with slower long-rest structural/electrochemical relaxation.

Particle refinement does not necessarily increase the phase-transition overpotential. Phase-field theory for coherent phase-separating nanoparticles predicts that surface-assisted elastic relaxation can reduce the coherent nucleation barrier as the area-to-volume ratio increases, with the barrier approaching zero below a critical particle size.[18,19] More directly, a recent study of spinel-type HEOs comparing ~150 nm and ~15 nm particles found that the smaller HEO exhibits reduced GITT polarization, shortened effective diffusion lengths, and more complete conversion, together with less pronounced conversion plateaus.[20] These results make the lower peak polarization of BM-HEO physically plausible despite its stronger microstructural refinement. The present BSE aggregate dimensions do not establish a true nanoscale particle size after milling, so the comparison is used only as mechanistic precedent. The safer interpretation is that milling reduces effective coherent-domain/transport lengths, increases interfaces and heterogeneous nucleation sites, and broadens the distribution of local transition conditions. This combination can lower the concentrated transition peak while spreading the transformation over a wider capacity interval.

## 3.5. Mg suppresses conversion-phase extent rather than simply accelerating transport

Mg incorporation produces a fundamentally different response. In Mg-HEO, the pronounced late-stage excess feature observed in HEO is reduced to 15.9 mV, and the capacity-weighted excess metric decreases to 3.96 × 10³ mV·mAh g−1. BM-Mg-HEO shows only a modest re-emergence of the broad feature, with a peak of 21.1 mV and an excess metric of 7.08 × 10³ mV·mAh g−1. Ball milling therefore increases accessibility within the Mg-containing material but does not restore the strong HEO-like transition response.

The most coherent interpretation is that Mg stabilizes the oxide/spinel-derived structure and suppresses the extent of late-stage conversion. This assignment simultaneously explains three observations: lower accessible capacity, strongly reduced transformation-associated polarization, and the absence of faster relaxation. A reduction in phase-boundary mobility alone would not be sufficient: if the same amount of transformation still had to proceed under the same imposed current, slower transformation kinetics would generally require a larger driving overpotential rather than the much smaller hump observed here. A more consistent two-coordinate interpretation is therefore that Mg first stabilizes the parent/intermediate oxide-derived state and reduces the fraction of material entering the late-stage conversion pathway, which lowers both conversion capacity and transition-associated polarization, while the residual transforming population has lower structural mobility and therefore relaxes more slowly. In this interpretation, polarization amplitude reflects transformation extent and local nucleation/strain energetics, whereas relaxation time reflects phase-boundary/structural mobility; the two quantities need not be uniquely coupled. The interpretation is consistent with several independent Mg-containing HEO studies. MgO has been identified as an electrochemically inactive stabilizing component in conversion-type HEOs,[8] operando synchrotron transmission X-ray microscopy shows that Mg contributes to structural retention while Mg-free material reaches higher capacity,[9] and detailed atomic/nanoscale analysis shows that electrochemically inactive cations stabilize an oxide nanophase during conversion.[10]

Alternative explanations are less complete. Faster Li diffusion could lower polarization but should also tend to shorten the current-off relaxation; t63 and t90 do not show this behavior. Lower purely ohmic or electronic resistance can explain a smaller fast jump but not the selective disappearance of the late-stage feature together with capacity loss. Reduced external surface area is inconsistent with the BET result because Mg-HEO has a larger surface area than HEO. SEI differences can influence the earliest first-cycle response but do not naturally explain the state-localized suppression of the low-voltage transition feature. Suppression of the conversion extent therefore provides the strongest explanation of the combined data, while the exact local Mg configuration remains to be finalized by the structural characterization.

## 3.6. Spatial modeling visualizes distinct late-stage internal-state evolution

The current-interruption analysis provides a set of directional constraints that a physically coherent model should satisfy simultaneously. For BM-HEO, the transformation-associated peak must decrease and broaden while the accessible transformed fraction remains high and the long-rest response becomes slower. For Mg-HEO, the transition-associated response and transformed fraction must decrease strongly even though the characteristic relaxation does not become faster. These combinations cannot be represented coherently by changing a single diffusion coefficient or a single structural-mobility parameter.

A reduced spatial phase-field model was therefore used as a mechanism-sufficiency test. The model couples a conserved radial Li-state variable c(r,t) to a nonconserved late-stage structural order parameter phi(r,t). The purpose is not to identify unique microscopic constants or reconstruct the complete lithiation pathway. Instead, the model asks whether independent coordinates for transport, transformation stability/extent, and structural mobility/local transition conditions can reproduce the experimentally required directions.

The frozen model reproduces the four-sample ordering when Mg and ball milling are assigned different physical roles. Mg-HEO requires both stabilization of the parent/intermediate state and slower mobility of the residual transforming population. Stabilization suppresses the transformed fraction and transition-associated polarization, while the reduced residual structural mobility prevents the remaining response from becoming artificially fast. BM-HEO instead requires a distribution of local transition conditions together with a distribution of structural mobilities. This ensemble description lowers the concentrated transition peak, broadens the reaction-progress interval over which transformation occurs, retains a high final transformed-state proxy, and produces a slower ensemble relaxation. BM-Mg-HEO retains Mg-related stabilization but partially reopens the transformation pathway under milling, giving an intermediate transformed-state response.

Figure 5 visualizes these differences over a common late-stage model reaction-progress window. The circular maps show the radial phi state at the end of the 600 s galvanostatic pulse, immediately before the 60 min current-off relaxation. For BM-containing samples, each map is an ensemble average over the frozen 11-quantile distribution and should not be interpreted as a directly simulated heterogeneous two-dimensional single particle. HEO develops the transformed state over a comparatively concentrated interval, whereas BM-HEO begins transformation earlier and distributes it more broadly. Mg-HEO remains predominantly parent-like over most of the same window, while BM-Mg-HEO shows partial recovery of transformation at high model state. The accompanying Delta phi-bar_rest trace reports the additional change in the structural order parameter during the subsequent 60 min rest. This internal-state descriptor is not numerically equated with the measured voltage relaxation, but it connects the model dynamics directly to the experimental GITT relaxation window. The visualization therefore provides a physically constrained representation of the experimental GITT interpretation rather than a direct measurement of phase fraction.

The value of the model is consequently directional rather than parametric. The experiment establishes that polarization amplitude, transformation width, accessible capacity, and long-rest relaxation do not move together as one kinetic variable. The spatial calculation shows that these observations are mutually compatible when transformation extent/stabilization and structural-mobility/transition-condition heterogeneity are allowed to vary independently. Detailed parameter values remain hypothesis-level and non-unique and are therefore retained primarily in the Supporting Information.

## 3.7. Cycling behavior reflects the balance between accessible interface and interphase stability

The electrochemical consequences of milling persist beyond the first cycle. Under the standardized FEC-containing electrolyte, BM-HEO maintains a higher absolute capacity than HEO during the 100-cycle test. Without FEC, however, BM-HEO shows stronger capacity fade. The same enlarged interface that exposes more active material to conversion also creates more area for electrolyte decomposition and repeated interphase reconstruction. The cycling result therefore reveals a trade-off rather than a uniformly beneficial milling effect: interface enlargement increases electrochemical utilization but also increases interphase burden.

Post-cycle SEM provides qualitative support for substantial surface reconstruction in both HEO and BM-HEO. The images confirm that the composite surface is not morphologically invariant during repeated conversion. Because these images do not establish interphase composition or reaction chemistry, they are used as corroborating evidence rather than as a unique degradation assignment.

The EIS series acquired during cycling also shows pronounced state/history dependence, but several spectra contain unstable or outlying responses and the present dataset has not yet been reduced to a uniquely defensible equivalent-circuit parameter series. EIS is therefore retained as Supporting Information rather than used to define the central mechanism.

## 3.8. Ball milling and Mg incorporation regulate different coordinates of the conversion reaction

The combined results distinguish the roles of processing and composition. Ball milling primarily changes **electrochemical accessibility and reaction distribution**. It increases physical surface area, enlarges the electrochemically accessible interface, increases capacity over the tested rate range, and broadens the late-stage transformation-associated polarization while lengthening the post-pulse relaxation. Mg incorporation primarily changes **conversion extent and structural stability**. It lowers accessible capacity and strongly suppresses the late-stage excess polarization even though the external surface area does not decrease and the characteristic relaxation time does not become shorter.

BM-Mg-HEO provides an internal test of this separation. Milling increases capacity and accessible interface in the Mg-containing composition, but it does not restore the strong Mg-free transition hump. Processing can therefore increase how much of the Mg-containing electrode is accessed without reversing the stronger compositional constraint imposed by Mg on the structural conversion pathway.

The four-sample matrix can consequently be described along three experimentally distinct coordinates: accessibility, transformation extent, and relaxation time. Ball milling shifts accessibility upward and distributes the phase-transforming response over a wider capacity interval. Mg shifts transformation extent downward. Relaxation time follows neither capacity nor polarization amplitude monotonically. These orthogonal trends explain why a single apparent GITT diffusion coefficient cannot represent the electrochemical consequences of synthesis in a phase-evolving HEO electrode.

---

# 4. Conclusions

Spinel Fe–Co–Ni–Cr–Mn high-entropy oxide anodes and their ball-milled and Mg-containing derivatives were compared using a 2 × 2 composition/process design. Ball milling increased the BET surface area from 3.94 to 18.159 m² g−1 in the Mg-free material and substantially increased the electrochemically accessible interface and specific capacity. This higher utilization did not coincide with uniformly faster current-off kinetics. HEO and BM-HEO showed nearly identical apparent fast current-off resistances of 106.4 and 106.5 Ω over 200–800 mAh g−1, while t63 increased from 8.68 to 11.57 min after milling. The late-stage transformation-associated excess polarization simultaneously decreased in peak amplitude and broadened in capacity. Ball milling is therefore assigned primarily to increased reaction accessibility and redistribution of the conversion transition rather than to a simple increase in Li diffusivity.

Mg incorporation produced a different trade-off. Accessible capacity and the late-stage transition-associated polarization were both reduced, whereas the characteristic relaxation time did not become shorter. Mg-HEO also exhibited a larger BET area than HEO, excluding loss of external surface area as the origin of the lower capacity. Together with literature evidence for the stabilizing role of Mg in conversion-type HEOs, this response is attributed predominantly to suppression of the extent of the spinel-to-rock-salt/conversion transformation. Ball milling of the Mg-containing material increased utilization but did not restore the pronounced Mg-free transition response, indicating that processing changes accessibility while composition imposes a stronger constraint on transformation extent.

A spatial mechanism-sufficiency model independently supports this separation: the observed directions are reproduced when Mg-related transformation stabilization and residual structural mobility are separated from the heterogeneous transition conditions and structural mobilities introduced by milling. The modeled internal-state maps are not direct phase-fraction measurements, but they provide a constrained visualization of how these independent coordinates can generate the experimentally observed GITT response.

The combined results show that accessible capacity, polarization amplitude, practical rate utilization, and post-pulse relaxation time are distinct observables of a phase-evolving HEO electrode. Separating these quantities resolves the contrasting roles of Mg incorporation and mechanical processing and provides a more direct synthesis–electrochemistry connection than interpretation based on a single apparent GITT diffusion coefficient.

---

# 5. Proposed Main-Figure Architecture

## Figure 1. Synthesis and structural perturbations

Suggested panels:

- synthesis route / four-sample 2 × 2 design;
- XRD comparison of HEO, BM-HEO, Mg-HEO, and BM-Mg-HEO;
- SEM/TEM morphology;
- final HRTEM/SAED after collaborator re-indexing;
- representative elemental maps;
- BET comparison, if panel count permits.

**Question answered:** What structural and interfacial perturbations are introduced by Mg and ball milling before electrochemical testing?

## Figure 2. Electrochemical accessibility and performance

Suggested panels:

- BET and relative Cdl/interfacial-accessibility comparison;
- first-cycle voltage profiles;
- FEC-containing cycling performance;
- rate capability;
- optional compact no-FEC control inset.

**Question answered:** How do Mg and ball milling change the amount of charge that can be accessed under common electrochemical conditions?

## Figure 3. Direct current-off polarization and relaxation

Suggested panels:

- representative GITT pulse/rest with definitions;
- apparent instantaneous current-off resistance vs cumulative capacity;
- ΔErelax vs cumulative capacity;
- t63 vs cumulative capacity;
- optional numerical summary of the 200–800 mAh g−1 medians.

**Question answered:** Does lower polarization mean faster relaxation, and does higher capacity mean lower resistance?

## Figure 4. Experimental phase-transition polarization

Suggested panels:

- **(a)** late-stage raw Delta E_relax versus normalized first-lithiation capacity z = Q/Qmax, with the relaxed-voltage trajectory shown only as a light reference if it remains readable;
- **(b)** background-subtracted transition-associated excess polarization using the common declared background procedure;
- **(c)** peak-amplitude versus FWHM-like-width map, with marker area proportional to normalized excess area.

Keep Figure 4 experimental-only. The previous mechanistic summary schematic is removed because Figure 5a now provides the explicit model-side interpretation.

**Draft caption — Figure 4. State-resolved current-off relaxation isolates a synthesis-dependent late-stage transition-associated polarization.** (a) Late-stage relaxation amplitude plotted against normalized first-lithiation capacity. Pristine HEO develops a concentrated high-state response in the voltage/state region associated in related spinel HEO literature with spinel-to-rock-salt/conversion evolution, whereas the feature is broadened after ball milling and strongly suppressed after Mg incorporation. (b) Background-subtracted excess polarization obtained using the same fitting windows and functional form for all four samples. Ball milling lowers the local maximum while distributing the excess response over a wider capacity interval; Mg incorporation strongly suppresses the excess response. (c) Peak-amplitude versus FWHM-like-width map, with marker area representing normalized excess area. The three descriptors separate a concentrated HEO response, a broader/lower BM-HEO response, strong Mg suppression, and partial re-emergence in BM-Mg-HEO. The excess area is a comparative polarization descriptor derived from discrete GITT states and is not interpreted as dissipated energy.

**Question answered:** What experimentally observed features distinguish redistribution of the transformation-associated response from suppression of its extent?

## Figure 5. Modeled late-stage internal-state evolution

Suggested panels:

- **(a)** compact broad-audience logic schematic linking the experimental constraints to independent model coordinates for transport scale, transformation stabilization/extent, local-transition heterogeneity, and structural-mobility heterogeneity;
- **(b)** 4 × 7 circular array of pulse-end radial phi states for HEO, BM-HEO, Mg-HEO, and BM-Mg-HEO at model mean lithiation states c-bar ≈ 0.55, 0.62, 0.68, 0.75, 0.80, 0.86, and 0.91;
- **(c)** pulse-end mean structural state phi-bar versus c-bar for all four samples.

For BM-HEO and BM-Mg-HEO, the circular maps and phi-bar trajectory are ensemble averages over the frozen 11-quantile distributions. Do not depict unmodeled random angular patches within a particle. Use a common phi color scale with 0 = parent-like/pre-transition and 1 = transformed-like, and label the displayed range explicitly as the late-stage transition window. The model mean lithiation coordinate c-bar must not be relabeled directly as experimental normalized capacity without an explicit quantitative calibration.

**Draft caption — Figure 5. Spatial mechanism-sufficiency model visualizes distinct late-stage internal-state evolution.** (a) Experimental GITT constraints are evaluated against independent model coordinates for transport scale, transformation stabilization/extent, local-transition heterogeneity, and structural-mobility heterogeneity. (b) Pulse-end radial maps of the late-stage structural order parameter phi at selected values of the model mean lithiation state c-bar. HEO and Mg-HEO use the single frozen radial parameter set, whereas BM-HEO and BM-Mg-HEO are shown as ensemble-averaged radial states over the frozen 11-quantile distributions. phi near 0 denotes a parent-like/pre-transition state and phi near 1 a transformed-like state. (c) Pulse-end mean structural state phi-bar versus c-bar. Ball milling advances and distributes the modeled transformation over a broader reaction-progress interval, Mg strongly suppresses the late-stage transformed state, and BM-Mg-HEO partially recovers transformation while retaining Mg-related suppression. The model is used as a mechanism-sufficiency visualization and does not represent a unique parameter identification, a directly measured phase fraction, or a complete reconstruction of all structural transitions during lithiation.

**Question answered:** What internal-state evolution is physically compatible with the experimentally observed combinations of polarization amplitude, transition width, transformed fraction, and relaxation time?


---

# 6. Supporting Information Architecture

Recommended SI order:

1. additional XRD/refinement and ICP tables;
2. complete SEM/TEM/EDS datasets and final indexing support;
3. final XPS fits, with batch comparison if Cr6+ is discussed at all;
4. full N2 adsorption/desorption and BET fitting;
5. Cdl determination and the effect of the assumed specific capacitance on nominal ECSA;
6. full first-cycle and selected-cycle voltage profiles;
7. no-FEC cycling control;
8. detailed rate-capability data;
9. dQ/dV evolution;
10. full GITT traces;
11. representative E vs √t current-off fits and R² statistics;
12. t50 and t90 vs capacity;
13. early- and terminal-slope descriptors;
14. transition-hump background sensitivity / peak-width-area robustness;
15. conventional apparent DGITT as a comparator, explicitly not used as the central causal descriptor;
16. cycling EIS series and outlier/state-matching note;
17. additional post-cycle SEM;
18. spatial-model equations and full effective-parameter table;
19. 7-versus-11-quantile convergence and volume-versus-surface chemical-potential readout comparison;
20. model sensitivity / identifiability boundaries and directional unit-test table;
21. model-predicted Delta phi-bar_rest during the 60 min zero-flux interval, explicitly labeled as an internal-state descriptor rather than a voltage fit.

The exploratory `D-only → D + compact relaxation → distributed relaxation` comparison remains outside this HEO manuscript and is reserved for the separate GITT/EKF study unless a later robustness analysis yields a uniquely useful synthesis-dependent descriptor.

---

# 7. References — integrated working list

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

# 8. Final unresolved items before manuscript freeze

## Collaborator-dependent

- exact Mg synthesis recipe and final nominal/ICP composition;
- final XRD refinement and lattice parameters;
- HRTEM/SAED re-indexing;
- final XPS dataset and decision on the anomalous Cr6+ feature.

## Student/electrochemistry metadata

- current collector;
- vacuum drying conditions;
- active loading and final electrode thickness;
- separator model and electrolyte volume;
- glovebox specifications;
- exact 1 C definition and rate-test sequence;
- potentiostat/model details;
- definitive lithiation/delithiation terminology for the WonATech half-cycle labels.

## Analysis freeze checks

- transition-hump background sensitivity and final peak/width/area values;
- final overlay of hump location with relaxed voltage;
- verify all first-cycle/cycling/rate values against the latest source or raw export;
- keep EIS in SI unless a reproducible state-matched analysis is completed;
- consolidate final figure numbering after collaborator structural panels are delivered.
