# HEO Manuscript v3 — Polished Figure-Aligned Draft

**Date:** 2026-09-19  
**Status:** YL WRITE / STRICT MODE polished draft  
**Scientific backbone:** Figure 1 → Figure 5 locked  
**Literature basis:** `HEO_REFERENCE_MASTER_VERIFIED_2026-09-18.md`  
**Writing basis:** Yoon Lab Publication Toolkit — PI Writing Profile, PI Logic Profile, Results Writing, and Manuscript Architecture/Literature Gate

> Verified information is written directly. Missing experimental metadata are not inferred. Inputs expected from the Yoo group and Yoon Lab are marked separately.

---

# Recommended title

**Contrasting Roles of Mg Incorporation and Ball Milling in Spinel High-Entropy Oxide Anodes: Phase Evolution, Polarization, and Electrochemical Utilization**

Alternative, more compact title:

**Mg Incorporation and Ball Milling Regulate Phase-Transformation Polarization in Spinel High-Entropy Oxide Anodes**

---

# Abstract

Spinel high-entropy oxides (HEOs) can store large amounts of Li through conversion-type reactions, but synthesis-dependent changes in performance are difficult to interpret when transport and structural transformation evolve simultaneously. Here, Fe–Co–Ni–Cr–Mn spinel HEO, ball-milled HEO (BM-HEO), Mg-containing HEO (Mg-HEO), and ball-milled Mg-HEO (BM-Mg-HEO) are compared in a 2 × 2 composition/process design. Ball milling increases the BET surface area of the Mg-free HEO from 3.94 to 18.159 m² g⁻¹ and increases capacity across the tested rate range. The higher utilization, however, does not coincide with faster post-pulse relaxation. Over 200–800 mAh g⁻¹, HEO and BM-HEO show nearly identical apparent fast current-off resistances of ~106 Ω, whereas the model-free t63 increases from 8.68 to 11.57 min after milling. The late-stage transition-associated excess polarization simultaneously decreases from 70.8 to 44.1 mV and broadens from 354 to 430 mAh g⁻¹. Mg incorporation produces a different response: Mg-HEO shows lower accessible capacity and a strongly suppressed excess peak of 15.9 mV, while t63 increases to 11.01 min rather than becoming shorter. A reduced spatial phase-field model shows that these directional trends are physically compatible when transformation stabilization/extent and structural-mobility/transition-condition heterogeneity are treated as independent coordinates. Ball milling therefore primarily increases accessibility and redistributes the phase-transforming reaction, whereas Mg predominantly suppresses its extent through structural stabilization. Separating capacity, polarization magnitude, transition width, and relaxation time reveals synthesis–electrochemistry relationships that are hidden when the response is reduced to a single apparent diffusivity.

**Keywords:** high-entropy oxide; spinel anode; lithium-ion battery; ball milling; magnesium incorporation; phase transformation; GITT; current interruption; polarization relaxation

---

# 1. Introduction

High-entropy oxides (HEOs) use multication disorder to access oxide compositions and functional responses that are difficult to obtain in conventional single- or few-cation materials.[1,2] Lithium-ion battery anodes are a prominent example because several redox-active cations can participate in conversion-type storage while the multication environment can modify structural stability and reaction reversibility.[2] The five-cation (Fe,Co,Ni,Cr,Mn)₃O₄ family is particularly relevant: single-phase spinel formation has been established,[3] and the same composition class has delivered high reversible capacity as a lithium-storage anode.[4,6]

Lithiation of these spinel HEOs is not adequately described as diffusion through a structurally invariant host. Atomic-scale studies show extensive reconstruction during cycling,[5] and recent in-situ XRD/ex-situ TEM measurements on the same five-cation family directly resolved a spinel → mixed spinel/rock-salt → rock-salt sequence during lithiation.[7] Structural conversion therefore introduces additional degrees of freedom beyond Li transport, including nucleation, phase-boundary propagation, strain accommodation, and structural rearrangement. A synthesis change can consequently alter not only transport length or interfacial resistance, but also how much material transforms and how broadly the transformation is distributed over reaction state.

Ball milling and Mg incorporation provide two physically distinct perturbations of this phase-evolving reaction. In the same five-cation HEO family, ball-milled comparisons and conventional GITT analysis have already shown that mechanical processing strongly changes electrochemical response.[6] Related studies further show that high-energy milling can perturb the spinel/rock-salt balance,[11] while particle fragmentation increases conversion reversibility and interfacial storage during cycling.[12] Morphology also changes rate and cycling behavior in the same five-cation composition space.[13] Mg introduces a different constraint. Conversion-type Mg-containing HEO studies show that electrochemically inactive Mg-derived components can stabilize oxide-derived structures,[8–10] and operando imaging has linked higher Mg content with improved structural retention but lower accessible capacity.[9] These studies suggest that mechanical processing and Mg incorporation need not act on the same kinetic coordinate.

The distinction is difficult to resolve when GITT is reduced to a single apparent diffusion coefficient. Conventional GITT-derived diffusivity is sensitive to geometry, equilibrium assumptions, time-window selection, and the validity of the underlying diffusion model,[15] all of which become nontrivial in a structurally reconstructive conversion electrode. Several extensions already demonstrate that intermittent measurements contain information beyond one diffusivity. Staircase-GITT separates ohmic and charge-transfer parameters through their distinct current/time responses,[23] direct-pulse fitting can reproduce both the current pulse and subsequent relaxation with an electrochemical model,[24] and recent time-domain analysis explicitly separates fast and slow voltage-relaxation regimes.[29] Current-interruption analysis likewise uses the early E–√t response to quantify a fast relaxation contribution.[16]

Phase-transforming electrodes add a further layer because the relaxation itself can contain structural evolution. Phase-transformation GITT has been formulated to extract both Li diffusivity and interface mobility in the two-phase region of LiFePO4,[21] and GITT relaxation has been used to compare phase-transformation kinetics as a function of state and rate.[22] Operando diffraction more recently showed directly that structural relaxation continues after current interruption and can proceed through multiple stages.[26] Phase-field studies have long demonstrated that non-Fickian phase evolution can alter the interpretation of GITT/PITT,[27,28] while nucleation itself can contribute materially to phase-transition overpotential.[17] General phase-field theory also shows that coherent nucleation and phase-separation energetics can change strongly with particle/domain size and surface contribution,[18,19] and nanosized spinel HEOs can exhibit lower polarization together with more complete conversion.[20]

The relevant pieces of this problem have therefore been addressed separately in prior work: intermittent methods can separate kinetic contributions,[23,24,29] GITT can probe phase-transformation kinetics and interface mobility,[21,22] and phase-field models can represent non-Fickian phase evolution.[27,28] The unresolved question here is **which physical coordinate each synthesis variable changes in the same phase-evolving HEO system**. This study compares HEO, BM-HEO, Mg-HEO, and BM-Mg-HEO using structural characterization, galvanostatic performance, direct current-off analysis of 10 min GITT pulses followed by 60 min relaxation, and a reduced spatial mechanism-sufficiency model. The analysis separates accessible capacity, polarization amplitude, transition width, and relaxation time rather than collapsing them into one apparent transport parameter. The resulting 2 × 2 comparison shows that ball milling primarily increases accessibility and redistributes the phase-transforming reaction, whereas Mg primarily reduces transformation extent through structural stabilization.

---

# 2. Experimental Section

## 2.1. Materials and synthesis of high-entropy oxides

Nickel(II) chloride hexahydrate (NiCl₂·6H₂O, 99.9%), iron(III) chloride hexahydrate (FeCl₃·6H₂O, ≥98%), cobalt(II) chloride hexahydrate (CoCl₂·6H₂O, 98%), manganese(II) chloride tetrahydrate (MnCl₂·4H₂O, ≥98%), chromium(III) chloride hexahydrate (CrCl₃·6H₂O), sodium hydroxide (NaOH, ≥97.0%), and sodium carbonate monohydrate (Na₂CO₃·H₂O, ≥99.5%) were used as received.

The Mg-free HEO was prepared by precipitation of a mixed-metal precursor followed by calcination. NiCl₂·6H₂O, FeCl₃·6H₂O, CoCl₂·6H₂O, MnCl₂·4H₂O, and CrCl₃·6H₂O were dissolved in 20 mL of deionized water using 1.4 mmol of each metal precursor. Separately, 14 mmol of NaOH and 7 mmol of Na₂CO₃·H₂O were dissolved in 10 mL of deionized water. The alkaline solution was slowly added to the mixed-metal solution under stirring at 800 rpm, and precipitation was continued for 2 h at room temperature. The precipitate was collected by centrifugation, washed three times with water, and dried overnight at 70 °C. The dried precursor was calcined at 900 °C for 2 h using a heating rate of 5 °C min⁻¹.

BM-HEO was prepared from the calcined HEO powder. Two grams of HEO were milled for 12 h at 500 rpm in an 80 mL stainless-steel jar using 5 mm ZrO₂ balls and a powder-to-ball mass ratio of 1:10.

**[[YOO GROUP INPUT REQUIRED — Mg synthesis/composition: Mg precursor identity; Mg amount and metal ratio; whether Mg was added to or substituted into the five-cation composition; any precipitation/calcination conditions that differed from HEO; final nominal formula; final ICP-OES composition. Do not infer these values from related literature.]]**

## 2.2. Structural and physicochemical characterization

Powder X-ray diffraction (XRD) patterns were collected using a MiniFlex 600 diffractometer (Rigaku, Japan) with Cu Kα radiation (λ = 1.5406 Å). Elemental compositions were measured by inductively coupled plasma optical emission spectroscopy (ICP-OES; iCAP PRO, Thermo Fisher Scientific, USA). Surface chemical states were analyzed by X-ray photoelectron spectroscopy (XPS; K-Alpha, Thermo Electron, USA). Morphology was examined by field-emission scanning electron microscopy (FE-SEM; Gemini 360, Carl Zeiss, Germany). Microstructure, lattice fringes, and elemental distributions were examined using a Cs-corrected transmission electron microscope (JEM-ARM200F, JEOL, Japan). Specific surface areas were obtained from N₂ adsorption measurements at 77 K using a BELSORP-max system (MicrotracBEL, Japan) and the Brunauer–Emmett–Teller method.

**[[YOO GROUP INPUT REQUIRED — final structural dataset: refined XRD phase assignment and lattice parameters; final HRTEM/SAED indexing; ICP compositions; particle/domain-size statistics if available; final XPS dataset and fitting decision. The preliminary CoGa₂O₄ HRTEM label is chemically incompatible with the Ga-free synthesis and must not appear. The batch-dependent Cr⁶⁺ feature should not be used mechanistically unless the remeasurement/fitting supports it.]]**

## 2.3. Electrode preparation and electrochemical measurements

The active HEO powder, Super P conductive carbon, and poly(acrylic acid) (PAA) binder were mixed at a mass ratio of 8:1:1 using deionized water as the slurry solvent. The slurry was coated using a 100 μm bar-coater gap. CR2032-type half-cells were assembled with the HEO-based electrode as the working electrode and Li metal as the counter electrode. A polypropylene separator and 1.0 M LiPF₆ in EC/DEC (1:1 by volume) containing 10 wt% fluoroethylene carbonate (FEC) were used for the principal four-sample comparison.

**[[YOON LAB INPUT REQUIRED — cell metadata: current collector; vacuum-drying temperature/time; final active-material loading; final electrode thickness; separator manufacturer/model if available; electrolyte volume; glovebox H₂O/O₂ specification.]]**

Galvanostatic charge–discharge measurements were performed using a WonATech battery cycler between 0.005 and 2.5 V. The principal low-rate comparison was conducted at 0.1 C. Rate-capability measurements used a stepwise C-rate sequence extending from 0.1 C to 5 C followed by recovery at 0.1 C.

**[[YOON LAB INPUT REQUIRED — cycling metadata: verify the capacity basis defining 1 C; exact number of cycles at each rate; confirm WonATech charge/discharge label convention before assigning the two half-cycle capacities to lithiation and delithiation.]]**

GITT was performed at 100 mA g⁻¹ between 0.005 and 2.5 V using repeated 10 min current pulses followed by 60 min open-circuit relaxation. Current-off portions of the response were analyzed because the pulse-period voltage contains both polarization and the change in equilibrium potential associated with continued reaction.

For the early current interruption, the voltage between 3 and 30 s after switching the current off was represented as

[
E(t)=a+bsqrt{t},
]

and the intercept (a) was extrapolated to (tightarrow0). The corresponding current-off voltage jump was divided by the absolute applied current to define an apparent fast current-off resistance. This quantity is used as an operational descriptor and is not assigned uniquely to ohmic or charge-transfer resistance.

The finite-window relaxation amplitude was defined as

[
Delta E_{mathrm{relax}}=E_{60,mathrm{min}}-E_{mathrm{off},3,mathrm{s}},
]

with absolute magnitude used for comparison where appropriate. Model-free (t_{50}), (t_{63}), and (t_{90}) values were defined as the times required to reach 50%, 63.2%, and 90% of the observed 3 s-to-60 min relaxation amplitude. These quantities do not assume single-exponential relaxation; (t_{63}) equals a conventional time constant only for an ideal single exponential.

The late-stage excess relaxation feature was quantified after subtracting the same smooth background procedure from (Delta E_{mathrm{relax}}) for all four samples. Peak amplitude, FWHM-like capacity width, normalized excess area, and an absolute capacity-weighted excess metric were extracted. The latter is used only as a comparative quantity and is not interpreted as dissipated energy because (Delta E_{mathrm{relax}}) is sampled at discrete GITT states rather than measured as a continuous operating overpotential.

Cyclic voltammetry in the nominal non-faradaic region of 3.0–3.3 V was acquired at scan rates of 10, 20, 40, 60, 80, and 100 mV s⁻¹ for relative interfacial-capacitance comparison. A specific capacitance of 40 μF cm⁻² was used in the original conversion to a nominal interface area. Because this value is not independently established for the porous composite electrode, the manuscript uses the result only as a relative interfacial-accessibility metric rather than an absolute ECSA.

**[[YOON LAB INPUT REQUIRED — instrumentation metadata: potentiostat/model and final CV/EIS acquisition settings needed for reproducibility.]]**

## 2.4. Spatial mechanism-sufficiency model

A reduced radial phase-field model was used to test whether the experimentally required directions can arise from independent transport and structural coordinates. The model is not used for unique parameter identification or quantitative voltage fitting. A conserved Li-state variable, \(c(r,t)\), is coupled to a nonconserved structural order parameter, \(\phi(r,t)\), representing the late-stage transition-associated state. Values near \(\phi=0\) denote a parent-like/pre-transition state and values near \(\phi=1\) denote a transformed-like state. The modeled \(\phi\) is therefore an internal-state coordinate rather than a directly measured phase fraction.

Li transport follows

\[
\frac{\partial c}{\partial t}=-\nabla\cdot J,\qquad
J=-D_{\mathrm{eff}}\nabla\mu_c,
\]

with

\[
\mu_c=\ln\frac{c}{1-c}-K\phi.
\]

Structural evolution follows dissipative relaxation,

\[
\frac{\partial\phi}{\partial t}
=
-M_\phi\frac{\delta G}{\delta\phi},
\]

where the free-energy representation includes a double-well structural term, Li–structure coupling, a Mg-dependent stabilization term, and reduced surface/coherency terms. Detailed equations and parameter definitions are provided in the Supporting Information.

Mg-containing cases were represented by increased stabilization of the parent/intermediate state together with lower mobility of the residual structural transformation. Ball-milled cases were represented by distributions of local transition/surface conditions and structural mobilities. BM-HEO and BM-Mg-HEO used 11 equal-probability quantiles of the selected ensemble distribution rather than a single deterministic particle. The numerical protocol reproduced the experimental 600 s pulse and 3600 s zero-flux rest. No formal inverse parameter identification is claimed. The frozen parameter set was selected through constrained directional tests and was required only to reproduce the experimentally observed ordering of transition-polarization amplitude, response width, characteristic relaxation, and transformed-state proxy. Numerical convergence, sensitivity tests, parameter tables, and identifiability limitations are reported in the Supporting Information.

---

# 3. Results and Discussion

## 3.1. Mg incorporation and ball milling create distinct structural and interfacial perturbations

The four samples form a 2 × 2 comparison that separates composition from mechanical processing (Figure 1). HEO and BM-HEO isolate the effect of milling in the Mg-free composition, while Mg-HEO and BM-Mg-HEO provide the corresponding comparison after Mg incorporation. The parent material belongs to the established five-cation spinel HEO family,[3,4] allowing the electrochemical consequences of the two perturbations to be compared without changing the underlying material class.

The XRD patterns are dominated by reflections associated with the cubic spinel-type structure. Mg incorporation produces only a small shift of the principal reflection near 35.7° toward lower 2θ, whereas ball milling produces a much stronger broadening of the diffraction features. In the current working dataset, the principal peak shifts from approximately 35.76° for HEO to 35.70° for Mg-HEO and from approximately 35.68° for BM-HEO to 35.64° for BM-Mg-HEO. If indexed as the spinel (311) reflection, the shift corresponds to only ~0.1–0.2% expansion of the apparent cubic lattice parameter. The present XRD therefore supports a modest lattice-level perturbation after Mg incorporation but does not establish a unique Mg site.

**[[YOO GROUP INPUT REQUIRED — replace/confirm the provisional peak-position discussion with final refined lattice parameters, phase fractions, and composition once the XRD/ICP dataset is frozen.]]**

Ball milling broadens the diffraction peaks while preserving the dominant spinel-like pattern in the present data. The broadening is consistent with reduced coherent-domain size and/or increased microstrain and disorder. Such changes are physically relevant to the reaction rather than merely morphological: high-energy milling has been reported to perturb the spinel/rock-salt balance in a related Mg-containing spinel HEO,[11] and progressive fragmentation of (FeCoNiCrMn)₃O₄ increases conversion reversibility and interfacial storage during cycling.[12] Morphology-controlled studies of the same five-cation family likewise show that particle architecture influences electrochemical response.[13]

Electron microscopy shows nanoscale structural heterogeneity and spatially distributed multication chemistry. EDS maps contain Fe, Co, Ni, Cr, Mn, and O throughout the HEO particles and additionally detect Mg in the Mg-containing samples. The available HRTEM images are consistent with nanocrystalline spinel-related regions, but the final plane assignments and quantitative structural comparison remain dependent on collaborator verification.

**[[YOO GROUP INPUT REQUIRED — final HRTEM/SAED indexing, particle/domain-size statistics, and the specific microscopy evidence that will be used to support Mg incorporation and/or milling-induced disorder.]]**

The structural data therefore establish two qualitatively different perturbations before electrochemical cycling: Mg produces a comparatively modest lattice/compositional modification of the parent spinel-type material, whereas ball milling strongly changes surface area, coherent-domain/microstructural characteristics, and accessible interface. The electrochemical question is whether these perturbations alter the same kinetic quantity or different coordinates of the conversion reaction.

## 3.2. Ball milling increases electrochemical accessibility and utilization, whereas Mg limits accessible conversion

Ball milling produces the dominant increase in physical surface area (Figure 2a). The BET area rises from 3.94 to 18.159 m² g⁻¹ for HEO and BM-HEO, respectively, a 4.61-fold increase. Mg-HEO has a BET area of 6.49 m² g⁻¹, while BM-Mg-HEO reaches 16.64 m² g⁻¹. The two ball-milled samples therefore converge to similarly high surface areas despite their different compositions.

The interfacial-capacitance measurement shows the same qualitative response. Using the same nominal specific capacitance for all samples, the relative interface metric increases from 4.18 to 30.17 cm² in the Mg-free pair and from 6.56 to 39.68 cm² in the Mg-containing pair. These values are not interpreted as absolute ECSA; their role is to confirm that ball milling strongly increases electrochemically accessible interface.

The larger interface is accompanied by greater first-cycle utilization (Figure 2b,c). Under the instrument-reported half-cycle convention, the first-cycle capacity pairs are 901.25/609.12 mAh g⁻¹ for HEO, 1056.10/782.08 mAh g⁻¹ for BM-HEO, 731.15/458.91 mAh g⁻¹ for Mg-HEO, and 944.07/580.83 mAh g⁻¹ for BM-Mg-HEO. The corresponding initial Coulombic efficiencies are 67.59%, 74.05%, 62.77%, and 61.52%. Ball milling increases both reported half-cycle capacities in each composition, whereas Mg lowers capacity relative to the corresponding Mg-free material despite the larger BET area of Mg-HEO than HEO.

**[[YOON LAB INPUT REQUIRED — after confirming the WonATech convention, replace “instrument-reported half-cycle capacity pairs” with the correct lithiation/delithiation terminology throughout the manuscript and Figure 2 caption.]]**

The opposite effects of surface area and Mg on capacity are already mechanistically informative. The Mg-induced capacity decrease cannot be attributed to loss of external surface area or reduced electrode/electrolyte contact. It instead points to a change in how much of the conversion reaction is accessed. Ball milling, by contrast, increases both physical interface and electrochemical utilization, consistent with fragmentation- and interface-assisted conversion reported in the same five-cation family.[12]

Cycling and rate data support the same separation (Figure 2d,e). With 10 wt% FEC, BM-HEO maintains a higher absolute capacity than HEO over 100 cycles. In cells without FEC, however, BM-HEO shows stronger capacity loss, indicating that the additional interface also increases interphase burden. FEC is therefore treated as a common interphase-control condition rather than as a mechanistic variable of the four-sample comparison. This role is consistent with a recent spinel-HEO study showing that FEC content substantially changes interphase chemistry and long-term electrochemical response.[14]

BM-HEO also maintains higher absolute capacity than HEO across the tested rate sequence and recovers the higher capacity after returning to 0.1 C. Higher practical rate utilization therefore does not require faster long-time relaxation. Continuous galvanostatic utilization and post-pulse relaxation probe different aspects of the electrode response, which motivates direct analysis of the GITT current-off transient.

Post-cycle microscopy shows substantial surface reconstruction in both HEO and BM-HEO, while cycling EIS displays strong state/history dependence. These datasets are used as supporting evidence because the microscopy does not uniquely identify interphase chemistry and several EIS spectra do not support a stable equivalent-circuit parameter series.

## 3.3. Current interruption separates polarization magnitude from relaxation time

The increased capacity of BM-HEO does not coincide with uniformly lower current-off polarization or faster relaxation. Conventional GITT analysis often compresses the transient into an apparent diffusion coefficient, although the extracted value depends strongly on model assumptions and analysis window.[15] The present analysis therefore preserves the current-off voltage response itself. Once the 10 min current pulse is interrupted, imposed charge insertion stops and the subsequent voltage evolution directly reports relaxation of the nonequilibrium state created by the pulse.

The early 3–30 s response is highly linear with (sqrt{t}), with median (R^2) values of approximately 0.996–0.999 across the four samples. This behavior is consistent with the short-time current-interruption treatment used in intermittent current interruption analysis,[16] but the resulting intercept is used here only as an operational fast-response descriptor because the electrode is structurally evolving. This choice differs from approaches that fit the full pulse/rest transient to a transport model[24] or separate fast and slow voltage relaxation using multi-time-constant descriptions.[29] The early formation region shows a pronounced sample dependence, especially for BM-HEO, whereas the subsequent common-capacity interval provides a cleaner comparison of the four materials.

Over 200–800 mAh g⁻¹, HEO and BM-HEO show nearly identical median apparent fast current-off resistances of 106.4 and 106.5 Ω, respectively (Figure 3b). Mg-HEO and BM-Mg-HEO are much lower at 40.2 and 33.0 Ω. The higher capacity of BM-HEO therefore does not arise from a uniform reduction in the fast current-off response. Conversely, the lower fast polarization of the Mg-containing electrodes does not produce higher capacity.

The longer relaxation reveals an even stronger decoupling (Figure 3c,d). Median 3 s-to-60 min relaxation amplitudes over the same capacity interval are 160.9, 176.3, 109.5, and 144.3 mV for HEO, BM-HEO, Mg-HEO, and BM-Mg-HEO, respectively. The corresponding model-free (t_{63}) values are 8.68, 11.57, 11.01, and 12.99 min. Ball milling therefore increases utilization while lengthening post-pulse relaxation. More importantly, Mg-HEO decreases the relaxation amplitude by ~32% relative to HEO while increasing (t_{63}) by ~27%.

This combination directly challenges a single-diffusivity interpretation. Under otherwise comparable conditions, faster diffusion should reduce diffusion-associated concentration polarization and shorten the corresponding diffusion-relaxation time. Mg-HEO instead shows smaller polarization together with slower relaxation. Diffusion can still contribute to the transient, but a single changing (D) cannot account for the synthesis dependence. The current-off response therefore contains at least one additional synthesis-sensitive coordinate. The state dependence of (Delta E_{mathrm{relax}}) identifies where that additional contribution becomes most pronounced.

## 3.4. Ball milling redistributes the late-stage transformation, whereas Mg suppresses its extent

The state-resolved relaxation amplitude develops a pronounced late-stage feature in pristine HEO (Figure 4a). After the early first-lithiation response decreases, (Delta E_{mathrm{relax}}) rises again at high cumulative capacity, with the strongest excess response in the approximate 0.6–0.4 V region of the relaxed GITT trajectory. BM-HEO does not show the same concentrated hump, and the feature is strongly suppressed in both Mg-containing electrodes.

The voltage/state localization links this excess response to structural conversion. Atomic-scale work has established extensive reconstruction of five-cation spinel HEOs during lithiation,[5] and Jin et al. directly resolved a spinel → mixed spinel/rock-salt → rock-salt pathway in the same five-cation family.[7] GITT has previously been reformulated for phase-transforming LiFePO4 to extract interface mobility as well as diffusivity,[21] and rest-to-equilibrium behavior has been used to compare phase-transformation kinetics.[22] Phase-transforming battery materials can also exhibit substantial nucleation-related overpotential,[17] while operando XRD confirms that structural evolution can continue during current-off relaxation.[26] The present late-stage hump is therefore assigned primarily to the spinel-to-rock-salt/conversion transformation, while its magnitude is treated as an electrochemical signature of the transformation rather than a direct phase-fraction measurement.

A common background subtraction isolates the transition-associated excess response (Figure 4b). HEO exhibits a peak amplitude of 70.8 mV and an FWHM-like width of 354 mAh g⁻¹. Ball milling lowers the peak to 44.1 mV while broadening the width to 430 mAh g⁻¹. Mg-HEO suppresses the peak to 15.9 mV with a width of 250 mAh g⁻¹, whereas BM-Mg-HEO shows a modest re-emergence to 21.1 mV and 392 mAh g⁻¹. The normalized excess areas are approximately 22.1, 14.1, 4.94, and 7.58 mV, respectively. The corresponding capacity-weighted excess metric is used only for comparison and is not interpreted as dissipated energy.

The peak–width map summarizes two distinct synthesis responses (Figure 4c). Ball milling moves the response toward a **lower but broader** transition-associated feature. Mg moves it toward **strong suppression of the feature**, with only partial recovery after subsequent milling. These trends separate redistribution of the transformation from reduction of its extent.

The ball-milling response is consistent with increased accessibility together with broader local transition conditions. Higher BET area, larger relative interface, increased capacity, and broader transition-associated polarization all point in the same direction. Milling-induced disorder, strain, shorter coherent domains, and additional interfaces can create a wider population of local nucleation and structural-relaxation environments. This interpretation is consistent with reports that high-energy milling perturbs spinel/rock-salt balance,[11] that fragmentation increases conversion reversibility and interfacial capacity in the same five-cation family,[12] and that morphology affects electrochemical behavior.[13] A smaller effective domain also does not require a larger phase-transition overpotential. Coherent-nucleation theory predicts strong size/surface dependence of nucleation energetics,[18,19] and nanosized spinel HEOs have been reported to show lower GITT polarization and more complete conversion.[20] The present morphology does not establish ~15 nm primary particles, so these studies are used as physical precedent rather than as direct size equivalence.

Mg produces a different signature. The transition-associated peak and accessible capacity both decrease, but the characteristic relaxation time does not become shorter. Faster Li transport alone therefore does not explain the Mg response. The minimum interpretation consistent with the complete dataset contains two coordinates: Mg stabilizes the parent/intermediate oxide-derived state and reduces the fraction entering the late-stage conversion pathway, while the remaining structural rearrangement has lower mobility. This interpretation is consistent with Mg-containing conversion HEO studies in which electrochemically inactive Mg-derived components improve structural retention or stabilize oxide-derived states.[8–10] These papers provide mechanistic precedent rather than direct proof of a specific Mg site in the present spinel.

BM-Mg-HEO provides an internal test of this separation. Milling increases accessible interface and capacity within the Mg-containing composition and partially reopens the transition-associated response, but it does not restore the concentrated HEO-like peak. Mechanical processing can therefore increase accessibility without removing the stronger compositional constraint imposed by Mg on transformation extent.

## 3.5. Spatial modeling visualizes internal-state evolution compatible with the GITT constraints

The experimental results impose directional constraints that a physically useful model must satisfy simultaneously. BM-HEO must maintain high transformation accessibility while showing a lower, broader transition-associated polarization and slower ensemble relaxation. Mg-HEO must show a much smaller transition response and lower transformed-state fraction without faster relaxation. Changing only one diffusion coefficient or only one structural-mobility parameter cannot reproduce both combinations.

The reduced spatial model therefore tests a minimum working set of independent physical coordinates within the model family examined here (Figure 5a). The approach follows the broader phase-field precedent that coupled conserved transport and phase evolution can produce non-Fickian GITT behavior and transformation dynamics distinct from classical diffusion models.[27,28] Transport, transformation stabilization/extent, and local-transition/structural-mobility heterogeneity are allowed to vary independently. Mg requires stabilization of the parent/intermediate state together with slower residual structural mobility. BM requires a distribution of local transition conditions and structural mobilities rather than a uniform acceleration of transport. Unlike phase-transformation GITT methods that identify interface mobility within a specified two-phase model,[21] the present parameters are intentionally treated as effective, non-unique coordinates constrained only by the observed directional relationships.

The circular maps in Figure 5b visualize the resulting radial (phi) state at the end of the 600 s pulse across a common late-stage model window. HEO develops the transformed state over a comparatively concentrated interval. BM-HEO begins transforming earlier and progresses over a broader model-state interval. Mg-HEO remains predominantly parent-like over most of the same window, whereas BM-Mg-HEO shows partial reopening of the transformation pathway at higher state. For BM-HEO and BM-Mg-HEO, each circle represents the ensemble-averaged radial state over the selected 11-quantile distribution; it is not a simulated two-dimensional heterogeneous particle.

The mean structural-state trajectories in Figure 5c show the same distinction. Ball milling broadens progression toward the transformed state, Mg strongly suppresses transformation, and BM-Mg-HEO partially recovers transformation at high model state. The model therefore provides mechanistic rationalization rather than independent validation: it demonstrates that the experimental directions can coexist when transformation extent/stabilization and transition/mobility heterogeneity are separated. The numerical parameters remain non-unique, (phi) is not a measured phase fraction, and the model mean lithiation state (\bar c) is not directly calibrated to experimental normalized capacity.

The five-Figure sequence consequently separates three synthesis-sensitive coordinates: **accessibility**, **transformation extent/distribution**, and **relaxation time**. Ball milling primarily increases accessibility and redistributes the phase-transforming reaction. Mg primarily suppresses transformation extent through structural stabilization. Relaxation time follows neither capacity nor polarization amplitude monotonically. This separation explains why the electrochemical consequences of synthesis in a phase-evolving HEO electrode cannot be represented by one apparent GITT diffusivity.

---

# 4. Conclusions

A 2 × 2 comparison of HEO, BM-HEO, Mg-HEO, and BM-Mg-HEO separates the effects of mechanical processing and Mg incorporation on a phase-evolving spinel HEO anode. Ball milling strongly increases physical and electrochemically accessible interface and raises capacity, but this higher utilization is not accompanied by uniformly lower current-off polarization or faster relaxation. Instead, the late-stage transition-associated response becomes lower in peak amplitude and broader in capacity while the long-rest characteristic time increases. Ball milling therefore acts primarily by increasing accessibility and redistributing the phase-transforming reaction rather than by uniformly accelerating Li transport.

Mg incorporation produces a different trade-off. Accessible capacity and transition-associated polarization both decrease, whereas the characteristic relaxation time does not become shorter. The combined response supports reduced conversion extent through stabilization of the parent/intermediate oxide-derived state, together with slower residual structural mobility. Subsequent milling partially restores accessibility and transformation in BM-Mg-HEO but does not recover the concentrated HEO-like transition response.

The spatial model shows that these experimentally observed directions are physically compatible when transformation stabilization/extent and structural-mobility/transition-condition heterogeneity are treated as independent coordinates. Its role is mechanistic rationalization rather than unique parameter extraction. The central result is the experimental separation of accessibility, transformation extent/distribution, and relaxation time as distinct synthesis-sensitive coordinates. This distinction provides a more direct connection between synthesis and electrochemical response than interpretation based on a single apparent GITT diffusion coefficient.

---

# References

1. Rost, C. M.; Sachet, E.; Borman, T.; Moballegh, A.; Dickey, E. C.; Hou, D.; Jones, J. L.; Curtarolo, S.; Maria, J.-P. Entropy-stabilized oxides. **Nature Communications** 2015, 6, 8485. DOI: 10.1038/ncomms9485.

2. Sarkar, A.; Velasco, L.; Wang, D.; Wang, Q.; Talasila, G.; de Biasi, L.; Kübel, C.; Brezesinski, T.; Bhattacharya, S. S.; Hahn, H.; Breitung, B. High entropy oxides for reversible energy storage. **Nature Communications** 2018, 9, 3400. DOI: 10.1038/s41467-018-05774-5.

3. Dąbrowa, J.; Stygar, M.; Mikuła, A.; Knapik, A.; Mroczka, K.; Tejchman, W.; Danielewski, M.; Martin, M. Synthesis and microstructure of the (Co,Cr,Fe,Mn,Ni)3O4 high entropy oxide characterized by spinel structure. **Materials Letters** 2018, 216, 32–36. DOI: 10.1016/j.matlet.2017.12.148.

4. Wang, D.; Jiang, S.; Duan, C.; Mao, J.; Dong, Y.; Dong, K.; Wang, Z.; Luo, S.; Liu, Y.; Qi, X. Spinel-structured high entropy oxide (FeCoNiCrMn)3O4 as anode towards superior lithium storage performance. **Journal of Alloys and Compounds** 2020, 844, 156158. DOI: 10.1016/j.jallcom.2020.156158.

5. Huang, C.-Y.; Huang, C.-W.; Wu, M.-C.; Patra, J.; Nguyen, T. X.; Chang, M.-T.; Clemens, O.; Ting, J.-M.; Li, J.; Chang, J.-K.; Wu, W.-W. Atomic-scale investigation of lithiation/delithiation mechanism in high-entropy spinel oxide with superior electrochemical performance. **Chemical Engineering Journal** 2021, 420, 129838. DOI: 10.1016/j.cej.2021.129838.

6. Xiao, B.; Wu, G.; Wang, T.; Wei, Z.; Sui, Y.; Shen, B.; Qi, J.; Wei, F.; Zheng, J. High-entropy oxides as advanced anode materials for long-life lithium-ion batteries. **Nano Energy** 2022, 95, 106962. DOI: 10.1016/j.nanoen.2022.106962.

7. Jin, G.; Luo, C.; Wang, Z.; Jia, S.; Yu, H.; Zhang, C.; Wang, Q.; Zhang, B.; Wang, Z. Unraveling phase transition pathway of spinel (FeCoCrNiMn)3O4 high-entropy oxide anodes for long-life Li-ion batteries. **Materials Today Chemistry** 2025, 48, 102949. DOI: 10.1016/j.mtchem.2025.102949.

8. Qiu, N.; Chen, H.; Yang, Z.; Sun, S.; Wang, Y.; Cui, Y. A high entropy oxide (Mg0.2Co0.2Ni0.2Cu0.2Zn0.2O) with superior lithium storage performance. **Journal of Alloys and Compounds** 2019, 777, 767–774. DOI: 10.1016/j.jallcom.2018.11.049.

9. Wang, S.-Y.; Chen, T.-Y.; Kuo, C.-H.; Lin, C.-C.; Huang, S.-C.; Lin, M.-H.; Wang, C.-C.; Chen, H.-Y. Operando synchrotron transmission X-ray microscopy study on (Mg, Co, Ni, Cu, Zn)O high-entropy oxide anodes for lithium-ion batteries. **Materials Chemistry and Physics** 2021, 274, 125105. DOI: 10.1016/j.matchemphys.2021.125105.

10. Wang, K.; Hua, W.; Huang, X.; Stenzel, D.; Wang, J.; Ding, Z.; Cui, Y.; Wang, Q.; Ehrenberg, H.; Breitung, B.; Kübel, C.; Mu, X. Synergy of cations in high entropy oxide lithium ion battery anode. **Nature Communications** 2023, 14, 1487. DOI: 10.1038/s41467-023-37034-6.

11. Zheng, Y.; Wu, X.; Lan, X.; Hu, R. A Spinel (FeNiCrMnMgAl)3O4 High Entropy Oxide as a Cycling Stable Anode Material for Li-Ion Batteries. **Processes** 2022, 10, 49. DOI: 10.3390/pr10010049.

12. Zhai, F.; Zhu, X.; Zhang, W.; Cao, G.; Zhang, H.; Xing, Y.; Xiang, Y.; Zhang, S. Insight of the evolution of structure and energy storage mechanism of (FeCoNiCrMn)3O4 spinel high entropy oxide in life-cycle span as lithium-ion battery anode. **Journal of Power Sources** 2024, 603, 234418. DOI: 10.1016/j.jpowsour.2024.234418.

13. Wang, X. L.; Jin, E. M.; Sahoo, G.; Jeong, S. M. High-Entropy Metal Oxide (NiMnCrCoFe)3O4 Anode Materials with Controlled Morphology for High-Performance Lithium-Ion Batteries. **Batteries** 2023, 9, 147. DOI: 10.3390/batteries9030147.

14. Patra, J.; Nguyen, T. X.; Panda, A.; Ting, J. M.; Dhaka, R. S.; Liu, W. R.; Yang, C. C.; Chang, J. K. Fluoroethylene carbonate electrolyte additive for improved charge-discharge performance of Co-free high entropy spinel oxide anodes for lithium-ion batteries. **Ceramics International** 2025, 51, 22628–22638. DOI: 10.1016/j.ceramint.2024.12.003.

15. Jia, M.; Zhang, W.; Cai, X.; Zhan, X.; Hou, L.; Yuan, C.; Guo, Z. Re-understanding the galvanostatic intermittent titration technique: Pitfalls in evaluation of diffusion coefficients and rational suggestions. **Journal of Power Sources** 2022, 543, 231843. DOI: 10.1016/j.jpowsour.2022.231843.

16. Chien, Y.-C.; Liu, H.; Menon, A. S.; Brant, W. R.; Brandell, D.; Lacey, M. J. Rapid determination of solid-state diffusion coefficients in Li-based batteries via intermittent current interruption method. **Nature Communications** 2023, 14, 2289. DOI: 10.1038/s41467-023-37989-6.

17. Komayko, A. I.; Nazarov, E. E.; Tyablikov, O. A.; Fedotov, S. S.; Antipov, E. V.; Nikitina, V. A. Unraveling the contribution of nucleation to the intercalation energy barrier for phase-transforming Li-ion battery materials. **Journal of Power Sources** 2024, 624, 235589. DOI: 10.1016/j.jpowsour.2024.235589.

18. Cogswell, D. A.; Bazant, M. Z. Coherency Strain and the Kinetics of Phase Separation in LiFePO4 Nanoparticles. **ACS Nano** 2012, 6, 2215–2225. DOI: 10.1021/nn204177u.

19. Cogswell, D. A.; Bazant, M. Z. Theory of Coherent Nucleation in Phase-Separating Nanoparticles. **Nano Letters** 2013, 13, 3036–3041. DOI: 10.1021/nl400497t.

20. Li, K.; Shi, L.; An, J.; Zhang, M.; Du, Y.; Ma, Y.; Lou, S.; Yin, G.; Yu, Z.; Hua, X.; Huo, H. Stabilizing Configurational Entropy in Spinel-type High Entropy Oxides during Discharge–Charge by Overcoming Kinetic Sluggish Diffusion. **Angewandte Chemie International Edition** 2025, 64, e202518569. DOI: 10.1002/anie.202518569.

21. Zhu, Y.; Wang, C. Galvanostatic Intermittent Titration Technique for Phase-Transformation Electrodes. **The Journal of Physical Chemistry C** 2010, 114, 2830–2841. DOI: 10.1021/jp9113333.

22. Chen, Y.; Wang, L.; Anwar, T.; Zhao, Y.; Piao, N.; He, X.; Zhu, Q. Application of Galvanostatic Intermittent Titration Technique to Investigate Phase Transformation of LiFePO4 Nanoparticles. **Electrochimica Acta** 2017, 241, 132–140. DOI: 10.1016/j.electacta.2017.04.137.

23. Heubner, C.; Schneider, M.; Michaelis, A. SoC dependent kinetic parameters of insertion electrodes from StairCase – GITT. **Journal of Electroanalytical Chemistry** 2016, 767, 18–23. DOI: 10.1016/j.jelechem.2016.02.013.

24. Horner, J. S.; Whang, G.; Ashby, D. S.; Kolesnichenko, I. V.; Lambert, T. N.; Dunn, B. S.; Talin, A. A.; Roberts, S. A. Electrochemical Modeling of GITT Measurements for Improved Solid-State Diffusion Coefficient Evaluation. **ACS Applied Energy Materials** 2021, 4, 11460–11469. DOI: 10.1021/acsaem.1c02218.

25. Fath, M.; Heidebrecht, P.; Drechsler, C.; Kamlah, M. Impact of particle size distribution on the rest phase behavior of LIB cathodes – Model based analysis. **Journal of Power Sources** 2024, 596, 234100. DOI: 10.1016/j.jpowsour.2024.234100.

26. Skurtveit, A.; Tiberg North, E.; Park, H.; Chernyshov, D.; Wragg, D. S.; Koposov, A. Y. Stepwise Structural Relaxation in Battery Active Materials. **ACS Materials Letters** 2025, 7, 343–349. DOI: 10.1021/acsmaterialslett.4c02058.

27. Han, B. C.; Van der Ven, A.; Morgan, D.; Ceder, G. Electrochemical modeling of intercalation processes with phase field models. **Electrochimica Acta** 2004, 49, 4691–4699. DOI: 10.1016/j.electacta.2004.05.024.

28. Singh, G. K.; Ceder, G.; Bazant, M. Z. Intercalation dynamics in rechargeable battery materials: General theory and phase-transformation waves in LiFePO4. **Electrochimica Acta** 2008, 53, 7599–7613. DOI: 10.1016/j.electacta.2008.03.083.

29. Jorkesh, S.; Akbari, A.; Ahmed, R.; Habibi, S. SOC-dependent voltage relaxation and dual time-constant behavior in lithium-ion batteries: A time-domain analysis. **Journal of Power Sources** 2026, 682, 240338. DOI: 10.1016/j.jpowsour.2026.240338.

---

---

---

# Figure Captions

**Figure 1. Mg incorporation and ball milling introduce distinct structural and interfacial perturbations in spinel HEOs.** The four-sample matrix separates compositional and mechanical-processing effects. XRD, electron microscopy, elemental mapping, and surface-area measurements establish the parent spinel-type material, the comparatively modest structural modification associated with Mg incorporation, and the stronger microstructural/interface change produced by milling. **[[YOO GROUP INPUT REQUIRED — freeze final Figure 1 panel order after refined XRD/HRTEM/SAED/ICP data are finalized.]]**

**Figure 2. Ball milling increases electrochemical accessibility and utilization, whereas Mg limits accessible conversion.** (a) BET surface area and relative interfacial-capacitance metric. (b,c) First-cycle voltage/capacity comparison. (d) Cycling performance under the common FEC-containing electrolyte, with no-FEC control in the Supporting Information or inset as appropriate. (e) Rate capability. The Cdl-derived interface metric is comparative rather than an absolute ECSA. **[[YOON LAB INPUT REQUIRED — confirm lithiation/delithiation label convention and final rate-sequence metadata.]]**

**Figure 3. Current interruption separates polarization magnitude from relaxation time.** (a) Representative GITT pulse and 60 min current-off response defining the apparent fast current-off response, (Delta E_{mathrm{relax}}), and model-free (t_{63}). (b) Apparent fast current-off resistance, (c) 3 s-to-60 min relaxation amplitude, and (d) (t_{63}) as functions of reaction state/cumulative capacity. BM-HEO maintains nearly the same intermediate-capacity fast-response resistance as HEO but relaxes more slowly, while Mg-containing electrodes show much lower polarization amplitudes without shorter relaxation times. The opposite changes in amplitude and time are inconsistent with a simple single-diffusivity explanation.

**Figure 4. Ball milling redistributes the late-stage transition-associated polarization, whereas Mg suppresses its extent.** (a) State-resolved (Delta E_{mathrm{relax}}) with the relaxed-voltage trajectory identifying the low-voltage conversion region. (b) Background-subtracted transition-associated excess relaxation obtained using the same procedure for all four samples. (c) Peak-amplitude versus FWHM-like width map, with marker area proportional to normalized excess area. Ball milling produces a broader but less concentrated response, whereas Mg strongly suppresses the transition-associated amplitude; BM-Mg-HEO shows only partial recovery. The integrated excess metric is comparative and is not interpreted as dissipated energy.

**Figure 5. Spatial modeling visualizes late-stage internal-state evolution compatible with the experimental GITT constraints.** (a) Mechanism-sufficiency model linking the experimental constraints to independent coordinates for transport, transformation stabilization/extent, and local-transition/structural-mobility heterogeneity. (b) Circular radial maps of the pulse-end structural order parameter (phi) across a common late-stage model window for HEO, BM-HEO, Mg-HEO, and BM-Mg-HEO. For ball-milled samples, each circle is an ensemble-averaged radial state over the selected 11-quantile distribution. (c) Pulse-end mean structural state (\bar\phi) versus model mean lithiation state (\bar c). The model is directional and non-unique: (phi) is not a directly measured phase fraction and (\bar c) is not directly calibrated to experimental normalized capacity.
