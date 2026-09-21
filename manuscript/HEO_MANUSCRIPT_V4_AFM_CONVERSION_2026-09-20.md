# HEO Manuscript v4 — AFM-Target Conversion-Centered Draft

**Date:** 2026-09-20  
**Status:** sentence-review draft; AFM-target positioning  
**Scientific backbone:** Figures 1–2 characterization → Figure 3 conventional electrochemistry → Figure 4 current-off decoupling → Figure 5 conversion assignment → Figure 6 reduced model  
**Literature basis:** \`HEO_REFERENCE_MASTER_VERIFIED_2026-09-18.md\`

> Verified information is written directly. Missing experimental metadata are not inferred. Inputs expected from the Yoo group and Yoon Lab remain explicitly marked. The Figure 4 differential-capacity peak positions currently come from reconstruction of the latest vector voltage profiles; the underlying numerical first-cycle files should replace this source if recovered before submission.

---

# Recommended title

**Mg Incorporation and Ball Milling Independently Regulate Electrochemical Accessibility and Conversion in Spinel High-Entropy Oxide Anodes**

Alternative:

**Contrasting Roles of Mg Incorporation and Ball Milling in Spinel High-Entropy Oxide Anodes: Accessibility, Conversion, and Relaxation**

---

# Abstract

Controlling conversion-type high-entropy oxide (HEO) anodes requires understanding how synthesis-induced structural changes affect both electrochemical performance and the underlying conversion reaction. Here, spinel Fe–Co–Ni–Cr–Mn HEO, ball-milled HEO (BM-HEO), Mg-containing HEO (Mg-HEO), and BM-Mg-HEO are compared to examine the effects of mechanical processing and compositional modification. Ball milling increases BET surface area from 3.94 to 18.159 m² g⁻¹ and raises accessible capacity, whereas Mg incorporation lowers accessible capacity. GITT analysis further distinguishes their electrochemical roles: ball milling primarily increases accessibility and redistributes the conversion-associated response over a broader reaction-state range, whereas Mg incorporation suppresses and delays accessible conversion while leaving the subsequent structural relaxation comparatively slow. These experimentally derived roles were tested using a reduced spatial model, which reproduced the observed ordering and response trends through separate structural-stabilization and relaxation contributions. The results connect synthesis-controlled structure and morphology with electrochemical performance and state-resolved conversion behavior in spinel HEO anodes.

**Keywords:** high-entropy oxide; conversion anode; ball milling; magnesium incorporation; GITT; electrochemical relaxation

# 1. Introduction

High-entropy oxides (HEOs) can accommodate several principal cations within a common oxide structure, creating broad distributions of local coordination and redox environments that are difficult to realize in conventional single- or few-cation oxides.[1,2] This compositional complexity is particularly attractive for electrochemical energy storage because multiple redox centers, local structural stability, and ion-transport pathways can be modified within the same material class.[2] Spinel (FeCoNiCrMn)₃O₄ is a representative conversion-type HEO anode: single-phase spinel formation has been established,[3] and reversible capacities of approximately 680 mAh g⁻¹ at low current density and 596.5 mAh g⁻¹ after 1200 cycles at 2.0 A g⁻¹ have been reported for this nominal composition.[4,6]

Lithium storage in spinel (FeCoNiCrMn)₃O₄ proceeds through substantial structural reconstruction and conversion rather than simple insertion into an intact host. Atomic-scale analysis has shown Mn nanocrystal formation already at 0.5 V lithiation and metallic Cr, Fe, Ni, and Co at deeper lithiation,[5] directly demonstrating progressive conversion. Complementary in-situ XRD/ex-situ TEM studies resolved a spinel → mixed spinel/rock-salt → rock-salt pathway,[7] while recent work describes rock-salt-like intermediates coexisting with Li₂O and metallic products and identifies oxygen migration as an important kinetic process during conversion.[20] Lithium storage in these HEOs therefore involves coupled nucleation, cation/oxygen rearrangement, phase-boundary motion, strain accommodation, and heterogeneous structural reconstruction over a broad reaction interval.

Ball milling and Mg incorporation provide two distinct ways to modify this conversion-type material. For the same nominal (FeCoNiCrMn)₃O₄ composition, mechanical processing and particle fragmentation have been reported to increase conversion reversibility and interfacial storage,[6,12] while high-energy milling can perturb the spinel/rock-salt balance in related spinel HEOs.[11] Mg-containing conversion HEOs show a different materials response: electrochemically inactive Mg-derived components can stabilize oxide-derived structures,[8–10], and operando imaging has associated higher Mg content with improved structural retention but lower accessible capacity.[9] These studies establish that both processing and composition can strongly alter HEO structure and battery performance. However, how the distinct materials changes induced by milling and Mg incorporation govern the progression and relaxation of conversion remains insufficiently resolved.

GITT provides a useful route to examine this connection. In HEO anode studies, GITT has generally been used to estimate and compare an apparent Li-ion diffusion coefficient, including in mechanically processed (FeCoNiCrMn)₃O₄.[6] Studies of other phase-transforming electrodes have shown that the pulse and relaxation response can also contain information on state-dependent kinetics, phase transformation, and structural relaxation beyond a single diffusivity.[21–24,26] Preserving the state-resolved polarization and current-off relaxation therefore offers a way to examine how synthesis-controlled structural changes are expressed during conversion.

Here, the effects of ball milling and Mg incorporation on spinel Fe–Co–Ni–Cr–Mn HEO are examined from structure and morphology to electrochemical performance and conversion behavior. Conventional cycling and rate measurements first establish how each modification changes accessible capacity and utilization. GITT is then used to distinguish polarization, conversion-associated relaxation, and characteristic relaxation time over reaction state. The analysis indicates that ball milling increases reaction accessibility while redistributing the conversion-associated response over a broader reaction range, whereas Mg incorporation suppresses and delays accessible conversion while the remaining structural relaxation stays comparatively slow. A reduced spatial model is subsequently used to test whether these experimentally inferred roles are physically consistent with separate structural-stabilization and relaxation contributions. Together, the results link synthesis-controlled materials characteristics to electrochemical performance and conversion behavior in spinel HEO anodes.

# 2. Results and Discussion

## 2.1. Structural and morphological characteristics of the HEO series

Figures 1 and 2 are reserved for the structural, compositional, and morphological characterization of HEO, BM-HEO, Mg-HEO, and BM-Mg-HEO. The current working dataset indicates that all four materials retain a predominantly spinel-type HEO structure, while Mg incorporation and ball milling introduce distinct compositional, lattice, particle, and surface-level changes. Ball milling also produces a marked increase in BET surface area. These characterization results will be finalized using the collaborator-verified XRD/refinement, ICP-OES, TEM/SAED/EDS, SEM, BET, and, if retained, XPS datasets.

At this stage, Figures 1–2 are used only to establish that Mg incorporation and ball milling produce distinguishable materials-level perturbations before electrochemical testing. Detailed phase assignments, Mg-site interpretation, quantitative lattice changes, and XPS-based mechanistic claims are intentionally deferred until the final characterization package is frozen.

**[[YOO GROUP INPUT REQUIRED — finalize Figure 1–2 panel composition and the corresponding structural interpretation using the verified XRD/ICP/TEM/SAED/EDS/SEM/BET dataset; decide separately whether XPS remains in the Supporting Information or is promoted to a main characterization figure.]]**


## 2.2. Ball milling and Mg incorporation produce distinct utilization and conversion-evolution trade-offs

The conventional electrochemical response first establishes how the two materials modifications alter accessible lithium storage (Figure 3). The first lithiation/delithiation capacities are 901.25/609.12 mAh g⁻¹ for HEO, 1056.10/782.08 mAh g⁻¹ for BM-HEO, 731.15/458.91 mAh g⁻¹ for Mg-HEO, and 944.07/580.83 mAh g⁻¹ for BM-Mg-HEO, giving initial Coulombic efficiencies of 67.59%, 74.05%, 62.77%, and 61.52%, respectively. Ball milling therefore increases both the first-lithiation and reversible first-cycle capacity in the Mg-free and Mg-containing compositions, whereas Mg incorporation lowers the accessible capacity relative to the corresponding Mg-free material. The higher utilization after milling is consistent with previous observations that fragmentation of (FeCoNiCrMn)₃O₄ increases conversion reversibility and interfacial storage,[12] while the lower capacity of the Mg-containing materials is consistent with the capacity–structural-retention trade-off reported for related Mg-containing HEO anodes.[8–10]

The same distinction persists during extended cycling. Under the common 10 wt% FEC condition, BM-HEO maintains the highest absolute capacity through 100 cycles, although its fractional retention is lower than that of the unmilled HEO. Mg-containing electrodes operate at lower absolute capacity, with milling partially recovering utilization in BM-Mg-HEO. The corresponding no-FEC data are retained in the Supporting Information because electrolyte formulation is not a primary variable in the present study. Those data show stronger fading, particularly for the ball-milled electrode, consistent with the increased interfacial sensitivity expected after particle refinement and with the known influence of FEC on HEO interphase stability.[12,14]

Rate capability reveals a complementary capacity–retention trade-off. BM-HEO provides the highest absolute capacity over most of the 0.1–5 C sequence and recovers its higher capacity when the rate returns to 0.1 C. The Mg-containing electrodes begin from lower low-rate capacities but retain a larger fraction of those capacities at the highest rates. Thus, the high-rate response cannot be interpreted from normalized retention alone: Mg incorporation reduces the total accessible reaction extent, whereas milling increases the amount of charge that can be accessed over the rate sequence. The absolute rate-capability data are therefore emphasized in Figure 3, while normalized capacity retention is provided in the Supporting Information.

The cycle-resolved differential-capacity response shows that the electrochemical reaction itself changes substantially after the first lithiation. All four materials exhibit a pronounced first-cycle cathodic feature in the low-voltage conversion region, which becomes markedly broader and less intense in subsequent cycles. This evolution is consistent with the reconstructive conversion reported for the five-cation spinel HEO family, in which the first lithiation generates metallic and oxide-derived nanoscale states that are not simply restored to the pristine spinel during subsequent cycling.[5,7,10] Ball milling and Mg incorporation also alter the shape and location of this first-cycle conversion response, but the peak positions are not assigned here; they are examined quantitatively together with the GITT excess response in Figure 5.

Figure 3 therefore establishes the materials-level electrochemical trade-offs before transient analysis: ball milling increases accessible utilization but introduces a larger cycling-retention penalty, whereas Mg incorporation lowers accessible capacity while preserving a comparatively larger fraction of capacity at high rate. At the same time, the strong first-cycle evolution of dQ/dV confirms that all four electrodes enter a reconstructed electrochemical state after initial conversion. The GITT analysis in Figure 4 is used next to determine how these differences are expressed in polarization and relaxation.


## 2.3. GITT separates relaxation magnitude from relaxation time

Figure 3 shows that ball milling and Mg incorporation alter accessible capacity and rate response in different ways. GITT is used here to determine whether those differences are accompanied by corresponding changes in the magnitude and timescale of post-pulse relaxation. Each step consists of a 10 min galvanostatic pulse followed by a 60 min open-circuit rest (Figure 4a). The relaxation magnitude is defined from 3 s after current interruption to the end of the 60 min rest, while $t_{63}$ denotes the time required to complete 63% of that relaxation.

The state-resolved relaxation amplitude, $\Delta E_{\mathrm{relax}}$, differs substantially among the four materials (Figure 4b). Over the common 200–800 mAh g⁻¹ capacity interval, the median values are 160.9 mV for HEO, 176.3 mV for BM-HEO, 109.5 mV for Mg-HEO, and 144.3 mV for BM-Mg-HEO. Thus, Mg incorporation markedly reduces the magnitude of the post-pulse voltage relaxation, whereas ball milling does not produce a comparable reduction and instead slightly increases the median amplitude in the Mg-free material.

The relaxation timescale evolves differently from the relaxation magnitude (Figure 4c). Median $t_{63}$ values over the same capacity interval are 8.68, 11.57, 11.01, and 12.99 min for HEO, BM-HEO, Mg-HEO, and BM-Mg-HEO, respectively. Ball milling therefore increases accessible utilization while lengthening the post-pulse relaxation. More importantly, Mg-HEO exhibits a substantially smaller relaxation amplitude than HEO but a longer, rather than shorter, relaxation time. The summary comparison in Figure 4d makes this decoupling explicit: the magnitude of the nonequilibrium voltage response and the time required for that response to relax do not vary together across the material series.

This behavior is difficult to describe using a single transport parameter alone. A change that simply accelerates diffusion would generally be expected to reduce diffusion-associated polarization together with its characteristic relaxation time. The Mg-containing electrode instead combines a smaller relaxation magnitude with a longer relaxation time, while milling increases utilization without accelerating relaxation. Diffusion can still contribute to the GITT transient, but the materials dependence requires an additional contribution associated with the evolving conversion state. Figure 5 therefore examines where the state-dependent excess relaxation occurs and whether it coincides with the electrochemical conversion response.

The short-time 3–30 s current-off analysis and the corresponding apparent fast-response resistance are retained in the Supporting Information as complementary evidence. They are not used as a primary mechanistic descriptor in the main text because the structurally evolving conversion electrode does not justify assigning the early response uniquely to a single resistance or intrinsic transport process.


## 2.4. Ball milling redistributes conversion whereas Mg incorporation suppresses it

The state-resolved GITT relaxation develops a distinct late-stage excess feature during the first lithiation (Figure 5a). The feature is strongest and relatively concentrated in HEO, becomes lower and broader after ball milling, and is strongly suppressed in both Mg-containing electrodes. Because this excess appears in the same low-voltage region in which the first-cycle conversion reaction develops, its electrochemical origin was examined directly against the first-cycle differential-capacity response.

The background-subtracted GITT excess and the independently derived cathodic dQ/dV response show closely matched peak positions for all four materials (Figure 5b,c). The dQ/dV maxima occur at approximately 0.545, 0.589, 0.419, and 0.485 V for HEO, BM-HEO, Mg-HEO, and BM-Mg-HEO, respectively, while the corresponding GITT excess maxima occur at 0.527, 0.618, 0.387, and 0.503 V. The peak pairs therefore remain within 32 mV across the full material series. This correspondence localizes the excess relaxation to the conversion-electrochemistry window, although it does not identify a unique microscopic step. The response is therefore described as conversion-associated and can include contributions from nucleation, cation/oxygen rearrangement, Li₂O/metal formation, phase-boundary motion, strain accommodation, and subsequent structural relaxation.[5,7,20]

Ball milling changes the character of this conversion-associated response rather than simply increasing its magnitude (Figure 5d). Relative to HEO, BM-HEO shows a lower peak amplitude but a broader response over reaction state, while Figure 3 shows that the same treatment increases accessible capacity. The combination of higher utilization with a broader and less concentrated conversion-associated response is consistent with conversion being distributed over a wider population of local reaction environments after particle refinement and milling-induced structural disorder. This interpretation is also directionally consistent with prior reports that fragmentation increases conversion reversibility and interfacial storage in (FeCoNiCrMn)₃O₄ and that milling can perturb spinel/rock-salt structural balance.[11,12]

Mg incorporation produces a qualitatively different response. Mg-HEO combines lower accessible capacity with a strongly reduced conversion-associated excess, and both the dQ/dV feature and GITT excess shift to lower potential relative to HEO. The lower-potential response is interpreted here as requiring greater electrochemical driving force before conversion becomes prominent rather than as a direct measurement of equilibrium thermodynamics. Together with the smaller conversion-associated response, the result is consistent with stabilization of an oxide-derived parent/intermediate state and reduced access to deeper conversion, in agreement with prior observations of enhanced structural retention in Mg-containing conversion HEOs.[8–10]

BM-Mg-HEO lies between these limiting behaviors. Milling partially restores accessible capacity within the Mg-containing composition, shifts the conversion feature back toward higher potential, and broadens the conversion-associated response, while the overall excess remains much smaller than in HEO. The small nominal increase in excess amplitude from Mg-HEO to BM-Mg-HEO is sensitive to the background definition and is therefore not used as a primary conclusion. The more robust result is that milling can reopen and redistribute accessible conversion without eliminating the stronger Mg-related suppression.

Figure 5 therefore provides the mechanistic link between the conventional electrochemistry in Figure 3 and the relaxation decoupling in Figure 4. Ball milling mainly changes how broadly conversion is accessed across reaction state, whereas Mg incorporation reduces and delays accessible conversion. These experimentally inferred roles are used in Figure 6 to test whether a reduced spatial model can reproduce the observed ordering of conversion-associated state evolution without treating the GITT response as a single transport process.

> **Internal data-source note for manuscript review:** the current differential-capacity curves were reconstructed from the vector first-cycle voltage profiles in the 2026-09-17 progress presentation because the corresponding numerical continuous-GCD source files are not currently available. The reconstruction reproduces the plotted first-cycle capacities to within ~0.03%. Regenerate the final dQ/dV artwork from the original numerical source if it is recovered before submission.


## 2.5. Reduced spatial modeling tests the proposed conversion roles of milling and Mg

The experimental results suggest two different materials effects. Ball milling increases accessible conversion while spreading the conversion-associated response over a broader reaction interval, whereas Mg incorporation reduces accessible conversion and leaves the remaining structural relaxation comparatively slow. A reduced spatial model was used to test whether these combinations can arise from physically distinct contributions rather than from a single changing transport parameter (Figure 6).

The model couples a conserved Li-state variable, $c(r,t)$, with a local conversion-progress variable, $\phi(r,t)$. Here, $\phi=0$ represents an oxide-derived parent/intermediate state, and increasing $\phi$ represents further local progression toward a more deeply converted state. It is a bookkeeping variable for conversion progress, not a measured rock-salt, metallic, Li₂O, or other microscopic phase fraction. Likewise, the model lithiation variable is not calibrated directly to experimental normalized capacity or voltage.

For Mg-containing materials, the experimentally observed combination of lower accessible conversion and slower residual relaxation cannot be reproduced in the tested model by stabilization or structural mobility alone. Stabilizing the oxide-derived state suppresses the extent of conversion, whereas lowering the structural mobility slows the relaxation of the fraction that does convert. Combining these two effects reproduces the qualitative Mg response: conversion is delayed and reduced, while the remaining structural evolution is slow. This result is consistent with the experimentally inferred role of Mg in Figure 5 but does not assign a unique stabilization energy or mobility to the real material.

Ball milling requires a different description. A single milled-particle condition can increase local accessibility but does not reproduce the experimentally observed combination of higher utilization with a broad, lower-amplitude conversion-associated response. Introducing a distribution of local conversion conditions and structural mobilities produces a broader ensemble response while preserving high overall conversion accessibility. The model therefore supports the interpretation that milling generates heterogeneous local environments—through particle refinement, defects, strain, interfaces, and related structural variations—rather than simply accelerating one uniform reaction process.

The simulated pulse-end state maps visualize these contrasting behaviors (Figure 6b). HEO evolves through a comparatively concentrated conversion interval; BM-HEO develops conversion over a broader range of local states; Mg-HEO remains predominantly in the oxide-derived state until later in the model progression; and BM-Mg-HEO shows partial reopening and broadening of the Mg-suppressed conversion pathway. The corresponding mean-state evolution preserves the experimental earlier-to-later ordering of the conversion response without refitting after the conversion-centered interpretation was adopted (Figure 6c). This agreement is evaluated only by ordering and qualitative response shape, not by numerical matching of model state to experimental capacity or voltage.

The model is therefore used as a consistency test for the materials interpretation established experimentally in Figures 3–5. It shows that the observed HEO, BM-HEO, Mg-HEO, and BM-Mg-HEO trends can be reproduced when conversion accessibility, structural stabilization, and heterogeneous structural relaxation are allowed to vary separately. The model does not uniquely determine microscopic parameters or individual conversion products. Its role is to support the conclusion that ball milling and Mg incorporation modify conversion through fundamentally different materials-level mechanisms.


# 3. Conclusions

Comparison of HEO, BM-HEO, Mg-HEO, and BM-Mg-HEO separates the electrochemical consequences of mechanical processing and Mg incorporation in a reconstructive spinel HEO anode. Ball milling strongly increases physical and electrochemically accessible interface and raises capacity, but this higher utilization is not accompanied by faster current-off relaxation. Instead, the late-stage excess response becomes lower in peak amplitude and broader in capacity while the long-rest characteristic time increases.

The strongest new constraint is the voltage correspondence between the GITT excess response and the first-cycle cathodic differential-capacity feature. Across all four samples, the two peak positions agree within 32 mV, and the Mg-induced shift to lower potential is reproduced independently in both observables. The late-stage GITT feature is therefore most consistently interpreted as conversion/transformation-associated rather than as an unspecified phase-transition signal.

Mg incorporation produces a different trade-off from ball milling. Accessible capacity and conversion-associated polarization both decrease, the conversion feature shifts to lower potential, and the characteristic relaxation time does not become shorter. The combined response supports stabilization of an oxide-derived parent/intermediate state that suppresses and delays deeper conversion, together with slow residual structural rearrangement. Subsequent milling partially reopens conversion in BM-Mg-HEO but does not recover the concentrated HEO-like response.

The frozen spatial model remains consistent with this revised interpretation without parameter refitting. Its role is mechanistic rationalization rather than unique parameter extraction. The central result is the experimental separation of accessibility, conversion extent/distribution, and relaxation time as distinct synthesis-sensitive coordinates. This materials-level distinction provides a more direct link between processing, composition, and electrochemical function than interpretation based on a single apparent GITT diffusion coefficient.

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

A reduced radial phase-field model was used to test whether the experimentally required directions can arise from independent transport and structural coordinates. The model is not used for unique parameter identification or quantitative voltage fitting. A conserved Li-state variable, $c(r,t)$, is coupled to a nonconserved structural order parameter, $\phi(r,t)$, representing an local conversion progress. Values near $\phi=0$ denote an oxide-derived parent/intermediate state and larger values denote progression toward a more deeply converted state. The modeled $\phi$ is therefore an internal-state coordinate rather than a directly measured crystallographic or chemical phase fraction.

Li transport follows

$$\frac{\partial c}{\partial t}=-\nabla\cdot J,\qquad J=-D_{\mathrm{eff}}\nabla\mu_c,$$

with

$$\mu_c=\ln\frac{c}{1-c}-K\phi.$$

Structural evolution follows dissipative relaxation,

$$\frac{\partial\phi}{\partial t}=-M_\phi\frac{\delta G}{\delta\phi},$$

where the free-energy representation includes a double-well structural term, Li–structure coupling, a Mg-dependent stabilization term, and reduced surface/coherency terms. Detailed equations and parameter definitions are provided in the Supporting Information.

Mg-containing cases were represented by increased stabilization of the unconverted oxide-derived parent/intermediate state together with lower mobility of the residual conversion-associated rearrangement. Ball-milled cases were represented by distributions of local conversion/surface conditions and structural mobilities. BM-HEO and BM-Mg-HEO used 11 equal-probability quantiles of the selected ensemble distribution rather than a single deterministic particle. The numerical protocol reproduced the experimental 600 s pulse and 3600 s zero-flux rest. Acceptance of the model was based on directional relationships among conversion-associated polarization amplitude, response width, characteristic relaxation, and converted-state proxy, not on numerical fitting of all microscopic parameters. Numerical convergence, sensitivity tests, parameter tables, and identifiability limitations are reported in the Supporting Information.

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

**Figure 1. Mg incorporation and ball milling alter crystal structure, composition, and nanoscale microstructure of spinel HEOs.** The four materials are compared using the final XRD, ICP-OES, HRTEM/SAED, and elemental-mapping dataset. The figure establishes the parent spinel-type structure, the comparatively modest lattice/compositional perturbation associated with Mg incorporation, and milling-induced changes in coherent-domain/microstructural characteristics. No unique Mg site is assigned without final refinement, and the chemically incompatible preliminary CoGa₂O₄ indexing is excluded. **[[YOO GROUP INPUT REQUIRED — freeze final refined XRD/HRTEM/SAED/ICP dataset and panel order.]]**

**Figure 2. Ball milling primarily modifies particle morphology and physical surface characteristics.** SEM morphology, particle/domain-size statistics, and BET surface area are used to compare HEO, BM-HEO, Mg-HEO, and BM-Mg-HEO before cycling. XPS is included only if the final dataset is reproducible and mechanistically defensible. Electrochemically derived interface metrics are intentionally excluded from this characterization figure and are introduced in Figure 3. **[[YOO GROUP INPUT REQUIRED — freeze final SEM/particle-size/BET package and final XPS inclusion decision.]]**

**Figure 3. Ball milling and Mg incorporation produce distinct utilization and conversion-evolution trade-offs.** (a) First-cycle voltage profiles of HEO, BM-HEO, Mg-HEO, and BM-Mg-HEO, with the corresponding first-cycle capacities and initial Coulombic efficiencies. (b) Specific capacity during 0.1 C cycling in the common 10 wt% FEC-containing electrolyte. (c) Absolute rate capability over the 0.1–5 C sequence and recovery after returning to 0.1 C. (d) Cycle-resolved differential-capacity response, highlighting the pronounced first-cycle cathodic conversion feature and its broadening/attenuation during subsequent cycling. Ball milling increases accessible utilization, whereas Mg incorporation lowers absolute capacity but retains a comparatively larger fraction of capacity at high rate. The no-FEC cycling comparison, Coulombic-efficiency evolution, normalized rate retention, and additional voltage-profile cycles are provided in the Supporting Information.

**Figure 4. GITT separates relaxation magnitude from relaxation time.** (a) Representative 10 min GITT pulse followed by a 60 min open-circuit rest, defining the 3 s-to-60 min relaxation magnitude, $\Delta E_{\mathrm{relax}}$, and characteristic relaxation time, $t_{63}$. (b) State-resolved $\Delta E_{\mathrm{relax}}$ for HEO, BM-HEO, Mg-HEO, and BM-Mg-HEO. (c) Corresponding $t_{63}$ values over reaction state. (d) Median $\Delta E_{\mathrm{relax}}$ versus median $t_{63}$ over the common 200–800 mAh g⁻¹ interval, illustrating that relaxation magnitude and timescale do not vary together across the four materials. Ball milling increases accessible utilization without accelerating relaxation, whereas Mg incorporation reduces the relaxation magnitude while leaving the relaxation comparatively slow. Short-time current-off fitting and apparent fast-response resistance are provided in the Supporting Information.

**Figure 5. Ball milling redistributes conversion whereas Mg incorporation suppresses it.** (a) State-resolved 3 s-to-60 min relaxation response showing the late-stage excess feature during first lithiation. (b) Background-subtracted GITT excess relaxation on a voltage axis together with the first-cycle cathodic dQ/dV response for HEO, BM-HEO, Mg-HEO, and BM-Mg-HEO. (c) Comparison of dQ/dV and GITT excess-peak voltages, showing localization of the excess response to the conversion-electrochemistry window. (d) Peak-amplitude versus FWHM-like width of the conversion-associated excess response, with marker area proportional to normalized excess area. Ball milling produces a broader, less concentrated response together with higher accessible utilization, whereas Mg incorporation strongly suppresses the response and shifts it to lower potential. Detailed background, smoothing, and window-sensitivity analyses are provided in the Supporting Information.

**Figure 6. Reduced spatial modeling tests the proposed conversion roles of ball milling and Mg incorporation.** (a) Schematic of the reduced spatial model coupling Li-state evolution with an local conversion-progress variable. Mg-containing cases include stabilization of the oxide-derived state and slower residual structural rearrangement, whereas ball-milled cases include a distribution of local conversion conditions and structural mobilities. (b) Representative pulse-end radial maps of the local conversion progress for HEO, BM-HEO, Mg-HEO, and BM-Mg-HEO over a common late-stage model window. For ball-milled samples, each map represents the ensemble-averaged radial state over the selected distribution. (c) Mean conversion-associated state versus model lithiation state, showing the same directional earlier-to-later ordering observed experimentally. The model is used only as a qualitative consistency test; neither the internal state variable nor the model lithiation coordinate is interpreted as a directly measured phase fraction or experimental normalized capacity.
