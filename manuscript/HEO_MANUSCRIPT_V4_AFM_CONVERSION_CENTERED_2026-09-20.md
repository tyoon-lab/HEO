# HEO Manuscript v4 — AFM-Targeted Conversion-Centered Draft

**Date:** 2026-09-20  
**Status:** Current authoritative main-text draft for sentence-by-sentence review  
**Target journal:** Advanced Functional Materials  
**Scientific identity:** HEO materials/mechanism paper; GITT/current-off analysis is supporting diagnostic evidence, not the primary method contribution.

> Verified information is written directly. Missing experimental metadata are not inferred. Inputs expected from the Yoo group and Yoon Lab remain marked explicitly.

---

# Recommended title

**Contrasting Roles of Mg Incorporation and Ball Milling in Spinel High-Entropy Oxide Anodes: Electrochemical Accessibility and Conversion Dynamics**

---

# Abstract

Spinel high-entropy oxides (HEOs) offer multication redox chemistry for conversion-type lithium storage, yet processing- and composition-induced changes are difficult to interpret when accessibility, polarization, and conversion evolve simultaneously. Here, Fe–Co–Ni–Cr–Mn spinel HEO, ball-milled HEO (BM-HEO), Mg-containing HEO (Mg-HEO), and ball-milled Mg-HEO (BM-Mg-HEO) are compared in a 2 × 2 design. Ball milling increases the BET surface area of the Mg-free HEO from 3.94 to 18.159 m² g⁻¹ and increases electrochemical utilization, while the model-free post-pulse t63 increases from 8.68 to 11.57 min. The late-stage excess polarization decreases from 70.8 to 44.1 mV and broadens from 354 to 430 mAh g⁻¹. Across all four samples, the GITT excess-relaxation maximum occurs within 32 mV of the first-cycle cathodic dQ/dV maximum, localizing the excess response to the conversion-electrochemistry window. Mg shifts this conversion feature to lower potential and strongly suppresses its amplitude without accelerating relaxation. A reduced spatial model of conversion-associated state evolution reproduces the relative onset/peak ordering without refitting after this assignment. Ball milling therefore primarily increases accessibility and redistributes conversion, whereas Mg stabilizes the oxide-derived parent/intermediate state and suppresses conversion extent.

**Keywords:** high-entropy oxide; conversion anode; ball milling; magnesium stabilization; GITT relaxation; phase-field modeling

---

# 1. Introduction

High-entropy oxides (HEOs) use multication disorder to access compositions and functional responses that are difficult to obtain in conventional single- or few-cation oxides.[1,2] For lithium-ion battery anodes, this compositional complexity is attractive because several transition metals can participate in conversion-type storage while the multication environment can alter structural stability and reaction reversibility.[2] The five-cation (Fe,Co,Ni,Cr,Mn)₃O₄ family is particularly relevant because single-phase spinel formation has been established and high reversible lithium-storage capacity has been reported.[3,4,6]

Lithiation of these spinel HEOs is not adequately described as Li diffusion through a structurally invariant host. Atomic-scale studies show extensive reconstruction during cycling,[5] and recent structural measurements on the same five-cation family resolve a spinel → mixed spinel/rock-salt → rock-salt sequence during lithiation.[7] Because these materials store Li through conversion-type chemistry, this crystallographic sequence is better viewed as part of a broader conversion-associated structural evolution rather than as a single isolated phase transition. Synthesis can therefore change not only transport length and interfacial resistance, but also the potential at which conversion becomes favorable, the fraction of material that converts, and how broadly that reaction is distributed over state.

Ball milling and Mg incorporation provide two physically different perturbations of this conversion-evolving HEO. Ball milling increases surface area, fragments particles and coherent domains, and can modify the spinel/rock-salt balance.[6,11,12] Morphology changes also alter electrochemical utilization in the same five-cation composition space.[13] Mg introduces a different constraint: Mg-containing conversion-type HEOs show improved retention of oxide-derived structures but often lower accessible capacity, consistent with stabilization by an electrochemically inactive or weakly active component.[8–10] These observations suggest that mechanical processing and Mg incorporation need not alter lithium storage through the same physical coordinate.

The distinction is difficult to resolve when galvanostatic intermittent titration technique (GITT) data are reduced to a single apparent diffusion coefficient. Apparent GITT diffusivity depends on geometry, equilibrium assumptions, and analysis window,[15] while current-interruption and extended GITT studies show that pulse and relaxation transients can contain separable kinetic information.[16,23,24] For phase-transforming electrodes, intermittent titration has also been used to examine phase-interface mobility and transformation kinetics,[21,22], and structural relaxation after current interruption has been observed directly.[26] Phase-field studies further show that non-Fickian phase evolution can alter GITT/PITT interpretation.[27,28] These precedents provide the basis for using the transient as a diagnostic of conversion-associated nonequilibrium response rather than treating it as one transport parameter.

The central question is therefore how ball milling and Mg incorporation alter electrochemical accessibility and conversion dynamics in the same spinel HEO system. HEO, BM-HEO, Mg-HEO, and BM-Mg-HEO are compared by structural characterization, galvanostatic performance, direct current-off analysis, and reduced spatial modeling. The 2 × 2 comparison shows that ball milling primarily increases accessibility and redistributes the conversion response, whereas Mg shifts conversion to lower potential and suppresses its extent through stabilization of the oxide-derived parent/intermediate state.

---

# 2. Results and Discussion

## 2.1. Mg incorporation and ball milling create distinct structural and interfacial perturbations

The four samples form a 2 × 2 comparison that separates composition from mechanical processing (Figure 1). HEO and BM-HEO isolate the effect of milling in the Mg-free composition, while Mg-HEO and BM-Mg-HEO provide the corresponding comparison after Mg incorporation. The parent material belongs to the established five-cation spinel HEO family,[3,4] allowing the electrochemical consequences of the two perturbations to be compared without changing the underlying material class.

The XRD patterns are dominated by reflections associated with the cubic spinel-type structure. Mg incorporation produces only a small shift of the principal reflection near 35.7° toward lower 2θ, whereas ball milling produces a much stronger broadening of the diffraction features. In the current working dataset, the principal peak shifts from approximately 35.76° for HEO to 35.70° for Mg-HEO and from approximately 35.68° for BM-HEO to 35.64° for BM-Mg-HEO. If indexed as the spinel (311) reflection, the shift corresponds to only ~0.1–0.2% expansion of the apparent cubic lattice parameter. The present XRD therefore supports a modest lattice-level perturbation after Mg incorporation but does not establish a unique Mg site.

**[[YOO GROUP INPUT REQUIRED — replace/confirm the provisional peak-position discussion with final refined lattice parameters, phase fractions, and composition once the XRD/ICP dataset is frozen.]]**

Ball milling broadens the diffraction peaks while preserving the dominant spinel-like pattern in the present data. The broadening is consistent with reduced coherent-domain size and/or increased microstrain and disorder. Such changes are physically relevant to the reaction rather than merely morphological: high-energy milling has been reported to perturb the spinel/rock-salt balance in a related Mg-containing spinel HEO,[11] and progressive fragmentation of (FeCoNiCrMn)₃O₄ increases conversion reversibility and interfacial storage during cycling.[12] Morphology-controlled studies of the same five-cation family likewise show that particle architecture influences electrochemical response.[13]

Electron microscopy shows nanoscale structural heterogeneity and spatially distributed multication chemistry. EDS maps contain Fe, Co, Ni, Cr, Mn, and O throughout the HEO particles and additionally detect Mg in the Mg-containing samples. The available HRTEM images are consistent with nanocrystalline spinel-related regions, but the final plane assignments and quantitative structural comparison remain dependent on collaborator verification.

**[[YOO GROUP INPUT REQUIRED — final HRTEM/SAED indexing, particle/domain-size statistics, and the specific microscopy evidence that will be used to support Mg incorporation and/or milling-induced disorder.]]**

The structural data therefore establish two qualitatively different perturbations before electrochemical cycling: Mg produces a comparatively modest lattice/compositional modification of the parent spinel-type material, whereas ball milling strongly changes surface area, coherent-domain/microstructural characteristics, and accessible interface. The electrochemical question is whether these perturbations alter the same kinetic quantity or different coordinates of the conversion reaction.

## 2.2. Ball milling increases electrochemical accessibility and utilization, whereas Mg limits accessible conversion

Ball milling produces the dominant increase in physical surface area (Figure 2a). The BET area rises from 3.94 to 18.159 m² g⁻¹ for HEO and BM-HEO, respectively, a 4.61-fold increase. Mg-HEO has a BET area of 6.49 m² g⁻¹, while BM-Mg-HEO reaches 16.64 m² g⁻¹. The two ball-milled samples therefore converge to similarly high surface areas despite their different compositions.

The interfacial-capacitance measurement shows the same qualitative response. Using the same nominal specific capacitance for all samples, the relative interface metric increases from 4.18 to 30.17 cm² in the Mg-free pair and from 6.56 to 39.68 cm² in the Mg-containing pair. These values are not interpreted as absolute ECSA; their role is to confirm that ball milling strongly increases electrochemically accessible interface.

The larger interface is accompanied by greater first-cycle utilization (Figure 2b,c). Under the instrument-reported half-cycle convention, the first-cycle capacity pairs are 901.25/609.12 mAh g⁻¹ for HEO, 1056.10/782.08 mAh g⁻¹ for BM-HEO, 731.15/458.91 mAh g⁻¹ for Mg-HEO, and 944.07/580.83 mAh g⁻¹ for BM-Mg-HEO. The corresponding initial Coulombic efficiencies are 67.59%, 74.05%, 62.77%, and 61.52%. Ball milling increases both reported half-cycle capacities in each composition, whereas Mg lowers capacity relative to the corresponding Mg-free material despite the larger BET area of Mg-HEO than HEO.

**[[YOON LAB INPUT REQUIRED — after confirming the WonATech convention, replace “instrument-reported half-cycle capacity pairs” with the correct lithiation/delithiation terminology throughout the manuscript and Figure 2 caption.]]**

The opposite effects of surface area and Mg on capacity are already mechanistically informative. The Mg-induced capacity decrease cannot be attributed to loss of external surface area or reduced electrode/electrolyte contact. It instead points to a change in how much of the conversion reaction is accessed. Ball milling, by contrast, increases both physical interface and electrochemical utilization, consistent with fragmentation- and interface-assisted conversion reported in the same five-cation family.[12]

Cycling and rate data support the same separation (Figure 2d,e). With 10 wt% FEC, BM-HEO maintains a higher absolute capacity than HEO over 100 cycles. In cells without FEC, however, BM-HEO shows stronger capacity loss, indicating that the additional interface also increases interphase burden. FEC is therefore treated as a common interphase-control condition rather than as a mechanistic variable of the four-sample comparison. This role is consistent with a recent spinel-HEO study showing that FEC content substantially changes interphase chemistry and long-term electrochemical response.[14]

BM-HEO also maintains higher absolute capacity than HEO across the tested rate sequence and recovers the higher capacity after returning to 0.1 C. Higher practical rate utilization therefore does not require faster long-time relaxation. Continuous galvanostatic utilization and post-pulse relaxation probe different aspects of the electrode response, which motivates direct analysis of the GITT current-off transient.

Post-cycle microscopy shows substantial surface reconstruction in both HEO and BM-HEO, while cycling EIS displays strong state/history dependence. These datasets are used as supporting evidence because the microscopy does not uniquely identify interphase chemistry and several EIS spectra do not support a stable equivalent-circuit parameter series.

## 2.3. Current interruption separates polarization magnitude from relaxation time

The increased capacity of BM-HEO does not coincide with uniformly lower current-off polarization or faster relaxation. Conventional GITT analysis often compresses the transient into an apparent diffusion coefficient, although the extracted value depends strongly on model assumptions and analysis window.[15] The present analysis therefore preserves the current-off voltage response itself. Once the 10 min current pulse is interrupted, imposed charge insertion stops and the subsequent voltage evolution directly reports relaxation of the nonequilibrium state created by the pulse.

The early 3–30 s response is highly linear with (sqrt{t}), with median (R^2) values of approximately 0.996–0.999 across the four samples. This behavior is consistent with short-time current-interruption analysis,[16] but the resulting intercept is used here only as an operational fast-response descriptor because the HEO electrode is structurally evolving. The early formation region shows a pronounced sample dependence, especially for BM-HEO, whereas the subsequent common-capacity interval provides a cleaner comparison of the four materials.

Over 200–800 mAh g⁻¹, HEO and BM-HEO show nearly identical median apparent fast current-off resistances of 106.4 and 106.5 Ω, respectively (Figure 3b). Mg-HEO and BM-Mg-HEO are much lower at 40.2 and 33.0 Ω. The higher capacity of BM-HEO therefore does not arise from a uniform reduction in the fast current-off response. Conversely, the lower fast polarization of the Mg-containing electrodes does not produce higher capacity.

The longer relaxation reveals an even stronger decoupling (Figure 3c,d). Median 3 s-to-60 min relaxation amplitudes over the same capacity interval are 160.9, 176.3, 109.5, and 144.3 mV for HEO, BM-HEO, Mg-HEO, and BM-Mg-HEO, respectively. The corresponding model-free (t_{63}) values are 8.68, 11.57, 11.01, and 12.99 min. Ball milling therefore increases utilization while lengthening post-pulse relaxation. More importantly, Mg-HEO decreases the relaxation amplitude by ~32% relative to HEO while increasing (t_{63}) by ~27%.

This combination directly challenges a single-diffusivity interpretation. Under otherwise comparable conditions, faster diffusion should reduce diffusion-associated concentration polarization and shorten the corresponding diffusion-relaxation time. Mg-HEO instead shows smaller polarization together with slower relaxation. Diffusion can still contribute to the transient, but a single changing (D) cannot account for the synthesis dependence. The current-off response therefore contains at least one additional synthesis-sensitive coordinate. The state dependence of (Delta E_{mathrm{relax}}) identifies where that additional contribution becomes most pronounced.

## 2.4. Ball milling redistributes the conversion-associated response, whereas Mg suppresses and shifts it

The state-resolved relaxation amplitude develops a pronounced late-stage feature in pristine HEO. After the early first-lithiation response decreases, ΔErelax rises again at high cumulative capacity, with the strongest excess response in the low-voltage region of the relaxed GITT trajectory. BM-HEO shows a less concentrated response, whereas both Mg-containing electrodes strongly suppress the excess amplitude.

An independent first-cycle electrochemical cross-check localizes this excess response to the same voltage window as the cathodic conversion feature. Using the latest first-cycle voltage profiles and a common differentiation procedure, the cathodic dQ/dV maxima occur at approximately 0.545, 0.589, 0.419, and 0.485 V for HEO, BM-HEO, Mg-HEO, and BM-Mg-HEO, respectively. The corresponding GITT excess-relaxation maxima occur at 0.527, 0.618, 0.387, and 0.503 V. The absolute mismatch is only 18–32 mV across all four samples, and the peak positions remain stable over the tested smoothing range.

This voltage correspondence is stronger evidence for a conversion-associated origin than voltage localization alone. Atomic-scale work has established extensive reconstruction of five-cation spinel HEOs during lithiation,[5] while the same material family exhibits a spinel → mixed spinel/rock-salt → rock-salt pathway.[7] Phase-transforming battery materials can also exhibit additional nucleation- and phase-boundary-related polarization,[17], and structural relaxation can continue after current interruption.[26] The GITT excess is therefore interpreted as a conversion/transformation-associated electrochemical response. The correspondence does not identify one microscopic step uniquely and should not be read as direct measurement of metallic-product or Li₂O phase fraction.

Applying the same background-fitting procedure independently to each sample isolates the conversion-associated excess response. HEO exhibits a peak amplitude of 70.8 mV and an FWHM-like width of 354 mAh g⁻¹. Ball milling lowers the peak to 44.1 mV while broadening the width to 430 mAh g⁻¹. Mg-HEO suppresses the peak to 15.9 mV with a width of 250 mAh g⁻¹, whereas BM-Mg-HEO shows a modest re-emergence to 21.1 mV and 392 mAh g⁻¹. The normalized excess areas are approximately 22.1, 14.1, 4.94, and 7.58 mV, respectively. The capacity-weighted excess quantity remains a comparative polarization descriptor and is not interpreted as dissipated energy.

The ball-milling response is characterized by higher accessibility, a higher-potential conversion feature, and a lower but broader excess-relaxation response. Higher BET area, larger relative interface, increased capacity, and broader conversion-associated polarization all point toward conversion being distributed over a wider population of local environments rather than being uniformly accelerated. Milling-induced disorder, strain, shorter coherent domains, and additional interfaces can broaden local nucleation and structural-relaxation conditions. Particle-size distributions can also delay GITT equilibration relative to a single-particle description,[25] while coherent nucleation depends strongly on particle/domain size and surface contribution.[18,19] Nanosized spinel HEOs have likewise been reported to show lower polarization together with more complete conversion.[20]

Mg produces a different signature: the first-cycle cathodic feature shifts from approximately 0.545 V in HEO to 0.419 V in Mg-HEO, while the GITT excess maximum shifts from 0.527 to 0.387 V and its amplitude falls sharply. The lower potential indicates that a larger lithiation driving force is required before the conversion-associated response becomes prominent. At the same time, the characteristic relaxation time does not become shorter. Faster Li transport alone therefore cannot explain the Mg response. The minimum interpretation consistent with the complete dataset is stabilization of the oxide-derived parent/intermediate state, which reduces conversion extent, together with lower mobility of the residual structural rearrangement. This interpretation is consistent with Mg-containing conversion HEO studies in which Mg-derived components improve structural retention or stabilize oxide-derived states.[8–10]

BM-Mg-HEO provides an internal test of this separation. Milling shifts the Mg-containing conversion feature back toward higher potential, increases accessible capacity, and partially restores the excess-relaxation response, but it does not recover the concentrated HEO/BM-HEO conversion response. Mechanical processing can therefore reopen and redistribute a conversion pathway without eliminating the stronger compositional stabilization imposed by Mg.

**[[FINAL FIGURE SOURCE CHECK — the current dQ/dV cross-check was reconstructed from the latest 2026-09-17 vector voltage-profile artwork because a separate continuous first-cycle Excel file is not available. The older first-cycle dataset affected by a power interruption is not used. Before submission, regenerate the dQ/dV panel from the original Origin/source profile if it can be recovered.]]**

## 2.5. Reduced spatial modeling rationalizes conversion-associated state evolution

The experimental results impose directional constraints that a physically useful description of the HEO system must satisfy simultaneously. BM-HEO must maintain high conversion accessibility while showing a lower, broader excess response and slower ensemble relaxation. Mg-HEO must show a strongly suppressed conversion response and lower accessible conversion without faster relaxation. A single changing diffusion coefficient cannot reproduce both combinations.

The reduced spatial model therefore tests a minimum working set of independent physical coordinates needed to rationalize these trends. Phase-field descriptions provide established precedent for coupling conserved Li transport with nonconserved structural evolution in electrochemical materials.[27,28] Here, φ is redefined explicitly as an effective conversion-associated structural-state coordinate: φ ≈ 0 denotes an oxide-derived parent/intermediate-like state and φ ≈ 1 a more converted-like state. Mg stabilization, structural mobility, transport scale, and milling-induced distributions of local conversion conditions are allowed to vary independently. The model is not a stoichiometrically complete conversion-reaction model and does not explicitly resolve Li₂O formation, metallic nanoparticle nucleation, sequential transition-metal reduction, or oxygen redistribution.

The circular maps in Figure 5b visualize the radial φ state at the end of the 600 s pulse across a common late-stage model window. HEO develops the converted-like state over a comparatively concentrated interval. BM-HEO begins this evolution earlier and progresses over a broader model-state interval. Mg-HEO remains predominantly oxide-derived over most of the same window, whereas BM-Mg-HEO shows partial reopening of the conversion-associated pathway at higher state. For BM-containing samples, each circle represents an ensemble-averaged radial state rather than a simulated two-dimensional heterogeneous particle.

The conversion-centered interpretation does not require refitting the frozen model. Recalculation with the existing parameter set places the relaxation-peak model states at c̄ = 0.586 for BM-HEO, 0.618 for HEO, 0.797 for BM-Mg-HEO, and 0.910 for Mg-HEO. Because c̄ increases as lithiation proceeds whereas the experimental potential falls, this earlier-to-later model ordering matches the higher-to-lower experimental conversion-feature ordering. The same ordering is preserved when conversion onset is defined by φ̄ thresholds from 0.02 to 0.10. Only this directional correspondence is used: model c̄ is not numerically calibrated to experimental Q/Qmax or voltage.

The model therefore provides mechanistic rationalization rather than independent phase identification. Together, Figures 1–5 separate three synthesis-sensitive coordinates: accessibility, conversion extent/distribution, and relaxation time. Ball milling primarily increases accessibility and redistributes conversion over heterogeneous local environments. Mg primarily stabilizes the oxide-derived state, shifts the conversion response to lower potential, and suppresses conversion extent. Relaxation time follows neither capacity nor polarization amplitude monotonically.

---

# 3. Conclusions

A 2 × 2 comparison of HEO, BM-HEO, Mg-HEO, and BM-Mg-HEO separates the effects of mechanical processing and Mg incorporation on conversion-type lithium storage. Ball milling strongly increases physical and electrochemically accessible interface and raises capacity, but this higher utilization is not accompanied by faster long-time relaxation. Instead, the conversion-associated excess response becomes lower in peak amplitude and broader in capacity, while its first-cycle cathodic feature occurs at relatively high potential. Ball milling therefore acts primarily by increasing accessibility and redistributing conversion rather than by uniformly accelerating Li transport.

Mg incorporation produces a different trade-off. The cathodic conversion feature shifts to lower potential, accessible capacity and conversion-associated excess polarization both decrease, and the characteristic relaxation time does not become shorter. The combined response supports stabilization of the oxide-derived parent/intermediate state, which suppresses conversion extent, together with slower residual structural mobility. Subsequent milling partially reopens the Mg-containing conversion pathway but does not recover the concentrated Mg-free response.

The reduced spatial model remains compatible with this reassignment without parameter refitting and reproduces the relative conversion-onset/peak ordering. Its role is to test mechanistic sufficiency rather than to identify unique microscopic conversion constants. The central result is the experimental separation of accessibility, conversion extent/distribution, and relaxation time as distinct synthesis-sensitive responses, together with the direct voltage correspondence between the first-cycle conversion feature and the GITT excess relaxation. This materials-level distinction explains why Mg incorporation and ball milling alter lithium storage through fundamentally different physical routes in the same spinel HEO.

---

# 4. Experimental Section

## 4.1. Materials and synthesis of high-entropy oxides

Nickel(II) chloride hexahydrate (NiCl₂·6H₂O, 99.9%), iron(III) chloride hexahydrate (FeCl₃·6H₂O, ≥98%), cobalt(II) chloride hexahydrate (CoCl₂·6H₂O, 98%), manganese(II) chloride tetrahydrate (MnCl₂·4H₂O, ≥98%), chromium(III) chloride hexahydrate (CrCl₃·6H₂O), sodium hydroxide (NaOH, ≥97.0%), and sodium carbonate monohydrate (Na₂CO₃·H₂O, ≥99.5%) were used as received.

The Mg-free HEO was prepared by precipitation of a mixed-metal precursor followed by calcination. NiCl₂·6H₂O, FeCl₃·6H₂O, CoCl₂·6H₂O, MnCl₂·4H₂O, and CrCl₃·6H₂O were dissolved in 20 mL of deionized water using 1.4 mmol of each metal precursor. Separately, 14 mmol of NaOH and 7 mmol of Na₂CO₃·H₂O were dissolved in 10 mL of deionized water. The alkaline solution was slowly added to the mixed-metal solution under stirring at 800 rpm, and precipitation was continued for 2 h at room temperature. The precipitate was collected by centrifugation, washed three times with water, and dried overnight at 70 °C. The dried precursor was calcined at 900 °C for 2 h using a heating rate of 5 °C min⁻¹.

BM-HEO was prepared from the calcined HEO powder. Two grams of HEO were milled for 12 h at 500 rpm in an 80 mL stainless-steel jar using 5 mm ZrO₂ balls and a powder-to-ball mass ratio of 1:10.

**[[YOO GROUP INPUT REQUIRED — Mg synthesis/composition: Mg precursor identity; Mg amount and metal ratio; whether Mg was added to or substituted into the five-cation composition; any precipitation/calcination conditions that differed from HEO; final nominal formula; final ICP-OES composition. Do not infer these values from related literature.]]**

## 4.2. Structural and physicochemical characterization

Powder X-ray diffraction (XRD) patterns were collected using a MiniFlex 600 diffractometer (Rigaku, Japan) with Cu Kα radiation (λ = 1.5406 Å). Elemental compositions were measured by inductively coupled plasma optical emission spectroscopy (ICP-OES; iCAP PRO, Thermo Fisher Scientific, USA). Surface chemical states were analyzed by X-ray photoelectron spectroscopy (XPS; K-Alpha, Thermo Electron, USA). Morphology was examined by field-emission scanning electron microscopy (FE-SEM; Gemini 360, Carl Zeiss, Germany). Microstructure, lattice fringes, and elemental distributions were examined using a Cs-corrected transmission electron microscope (JEM-ARM200F, JEOL, Japan). Specific surface areas were obtained from N₂ adsorption measurements at 77 K using a BELSORP-max system (MicrotracBEL, Japan) and the Brunauer–Emmett–Teller method.

**[[YOO GROUP INPUT REQUIRED — final structural dataset: refined XRD phase assignment and lattice parameters; final HRTEM/SAED indexing; ICP compositions; particle/domain-size statistics if available; final XPS dataset and fitting decision. The preliminary CoGa₂O₄ HRTEM label is chemically incompatible with the Ga-free synthesis and must not appear. The batch-dependent Cr⁶⁺ feature should not be used mechanistically unless the remeasurement/fitting supports it.]]**

## 4.3. Electrode preparation and electrochemical measurements

The active HEO powder, Super P conductive carbon, and poly(acrylic acid) (PAA) binder were mixed at a mass ratio of 8:1:1 using deionized water as the slurry solvent. The slurry was coated using a 100 μm bar-coater gap. CR2032-type half-cells were assembled with the HEO-based electrode as the working electrode and Li metal as the counter electrode. A polypropylene separator and 1.0 M LiPF₆ in EC/DEC (1:1 by volume) containing 10 wt% fluoroethylene carbonate (FEC) were used for the principal four-sample comparison.

**[[YOON LAB INPUT REQUIRED — cell metadata: current collector; vacuum-drying temperature/time; final active-material loading; final electrode thickness; separator manufacturer/model if available; electrolyte volume; glovebox H₂O/O₂ specification.]]**

Galvanostatic charge–discharge measurements were performed using a WonATech battery cycler between 0.005 and 2.5 V. The principal low-rate comparison was conducted at 0.1 C. Rate-capability measurements used a stepwise C-rate sequence extending from 0.1 C to 5 C followed by recovery at 0.1 C.

**[[YOON LAB INPUT REQUIRED — cycling metadata: verify the capacity basis defining 1 C; exact number of cycles at each rate; confirm WonATech charge/discharge label convention before assigning the two half-cycle capacities to lithiation and delithiation.]]**

GITT was performed at 100 mA g⁻¹ between 0.005 and 2.5 V using repeated 10 min current pulses followed by 60 min open-circuit relaxation. Current-off portions of the response were analyzed because the pulse-period voltage contains both polarization and the change in equilibrium potential associated with continued reaction.

For the early current interruption, the voltage between 3 and 30 s after switching the current off was represented as

\[
E(t)=a+b\sqrt{t},
\]

and the intercept \(a\) was extrapolated to \(t\rightarrow0\). The corresponding current-off voltage jump was divided by the absolute applied current to define an apparent fast current-off resistance. This quantity is used as an operational descriptor and is not assigned uniquely to ohmic or charge-transfer resistance.

The finite-window relaxation amplitude was defined as

\[
\Delta E_{\mathrm{relax}}
=
E_{60\,\mathrm{min}}-E_{\mathrm{off},3\,\mathrm{s}},
\]

with absolute magnitude used for comparison where appropriate. Model-free \(t_{50}\), \(t_{63}\), and \(t_{90}\) values were defined as the times required to reach 50%, 63.2%, and 90% of the observed 3 s-to-60 min relaxation amplitude. These quantities do not assume single-exponential relaxation; \(t_{63}\) equals a conventional time constant only for an ideal single exponential.

The late-stage excess relaxation feature was quantified after applying the same background-fitting procedure to each sample independently. Peak amplitude, FWHM-like capacity width, normalized excess area, and an absolute capacity-weighted excess metric were extracted. The latter is used only as a comparative quantity and is not interpreted as dissipated energy because \(\Delta E_{\mathrm{relax}}\) is sampled at discrete GITT states rather than measured as a continuous operating overpotential.

Cyclic voltammetry in the nominal non-faradaic region of 3.0–3.3 V was acquired at scan rates of 10, 20, 40, 60, 80, and 100 mV s⁻¹ for relative interfacial-capacitance comparison. A specific capacitance of 40 μF cm⁻² was used in the original conversion to a nominal interface area. Because this value is not independently established for the porous composite electrode, the manuscript uses the result only as a relative interfacial-accessibility metric rather than an absolute ECSA.

**[[YOON LAB INPUT REQUIRED — instrumentation metadata: potentiostat/model and final CV/EIS acquisition settings needed for reproducibility.]]**

## 4.4. Reduced spatial model of conversion-associated state evolution

A reduced radial phase-field model was used to test whether the experimentally required HEO trends can arise from independent transport and conversion-associated structural coordinates. The model is not used for unique parameter identification or quantitative voltage fitting. A conserved Li-state variable, (c(r,t)), is coupled to a nonconserved effective conversion-associated order parameter, (phi(r,t)). Values near (phi=0) denote an oxide-derived parent/intermediate-like state and values near (phi=1) denote a more converted-like state. The variable (phi) is therefore an internal-state coordinate, not a directly measured crystallographic or metallic-product phase fraction.

Li transport follows

[
rac{partial c}{partial t}=-
ablacdot J,qquad
J=-D_{mathrm{eff}}
ablamu_c,
]

with

[
mu_c=lnrac{c}{1-c}-Kphi.
]

Structural evolution follows

[
rac{partialphi}{partial t}
=
-M_phirac{delta G}{deltaphi}.
]

The reduced free-energy representation includes a double-well structural term, Li–structure coupling, an Mg-dependent stabilization term, and reduced surface/coherency terms. The formulation is intended to represent effective conversion-associated state evolution and does not explicitly resolve the full stoichiometry of metallic-product/Li₂O formation. Detailed equations and parameter definitions are provided in the Supporting Information.

Mg-containing cases were represented by increased stabilization of the oxide-derived parent/intermediate state together with lower mobility of the residual structural rearrangement. Ball-milled cases were represented by distributions of local conversion/surface conditions and structural mobilities. BM-HEO and BM-Mg-HEO used 11 equal-probability quantiles of the selected ensemble distribution. The numerical protocol reproduced the experimental 600 s pulse and 3600 s zero-flux rest. After the experimental conversion assignment was strengthened by the dQ/dV–GITT voltage correspondence, the frozen model was recalculated without parameter refitting; only directional ordering is compared with experiment. Numerical convergence, sensitivity tests, parameter tables, and identifiability limitations are reported in the Supporting Information.

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

**Figure 4. The late-stage excess relaxation tracks the first-cycle cathodic conversion feature.** (a–d) Normalized first-cycle cathodic dQ/dV response and GITT excess-relaxation peak position for HEO, BM-HEO, Mg-HEO, and BM-Mg-HEO, respectively. (e) Correspondence between dQ/dV and GITT peak voltages; the absolute mismatch is 18–32 mV across the four samples. (f) Excess-polarization peak amplitude versus FWHM-like capacity width, with marker area proportional to normalized excess area. The voltage correspondence localizes the excess response to the conversion window but does not assign a unique microscopic conversion step.

**Figure 5. Reduced spatial modeling of conversion-associated state evolution compatible with the experimental constraints.** (a) Mechanism-sufficiency logic separating transport, Mg stabilization/conversion extent, and milling-induced local-conversion/structural-mobility heterogeneity. (b) Pulse-end radial maps of the effective conversion-associated structural-state variable φ across a common late-stage model window. BM-containing maps are ensemble-averaged radial states. (c) Pulse-end mean φ versus model mean lithiation state c̄. The model is directional and non-unique: φ is not a directly measured phase fraction, and c̄ is not directly calibrated to experimental normalized capacity or voltage.
