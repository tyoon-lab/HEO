# HEO Manuscript v5 — AFM-Target Capacity–Relaxation/Microkinetic Draft

**Date:** 2026-09-23  
**Status:** integrated electrochemistry rewrite; Figures 6–7 logic updated  
**Scientific backbone:** Figures 1–2 characterization → Figure 3 accessible capacity → Figure 4 capacity–relaxation mismatch → Figure 5 conversion localization → Figure 6 cycle-history evolution → Figure 7 minimal microkinetic interpretation  
**Literature basis:** \`HEO_REFERENCE_MASTER_VERIFIED_2026-09-18.md\`

> Verified information is written directly. Missing experimental metadata are not inferred. Inputs expected from the Yoo group and Yoon Lab remain explicitly marked. The Figure 5 differential-capacity peak positions currently come from reconstruction of the latest vector voltage profiles; the underlying numerical first-cycle files should replace this source if recovered before submission.

---

# Working title

**Structural Modification Reshapes Conversion and Relaxation in Spinel High-Entropy Oxide Anodes**

Alternative:

**Contrasting Effects of Ball Milling and Mg Incorporation on Conversion in Spinel High-Entropy Oxide Anodes**

---


# Abstract

Controlling conversion-type high-entropy oxide (HEO) anodes requires separating how much electrochemical reaction can be accessed from how rapidly the resulting conversion state relaxes. Here, spinel Fe–Co–Ni–Cr–Mn HEO, ball-milled HEO (BM-HEO), Mg-containing HEO (Mg-HEO), and BM-Mg-HEO are compared to examine how mechanical processing and compositional modification alter these two aspects of conversion behavior. Ball milling increases surface area and accessible capacity, whereas Mg incorporation lowers accessible capacity. GITT reveals an apparent kinetic paradox: the higher capacity produced by ball milling is not accompanied by faster current-off relaxation, while Mg suppresses accessible conversion without a proportional change in the effective relaxation timescale. The excess relaxation is independently localized to the conversion region by differential-capacity analysis and evolves strongly with cycling, primarily through its amplitude rather than its effective timescale. A minimal multi-step microkinetic model shows how increased reaction accessibility can coexist with slower ensemble relaxation because state population and relaxation eigen-timescales are not controlled by a single kinetic coordinate. These results identify distinct roles of ball milling and Mg incorporation and show that conversion capacity and conversion-associated relaxation cannot be reduced to one fast–slow descriptor in multicomponent HEO anodes.

**Keywords:** high-entropy oxide; conversion anode; ball milling; magnesium incorporation; GITT; electrochemical relaxation; microkinetics

# 1. Introduction

High-entropy oxides (HEOs) can accommodate several principal cations within a common oxide structure, creating broad distributions of local coordination and redox environments that are difficult to realize in conventional single- or few-cation oxides.[1,2] This compositional complexity is particularly attractive for electrochemical energy storage because multiple redox centers, local structural stability, and ion-transport pathways can be modified within the same material class.[2] Spinel (FeCoNiCrMn)₃O₄ is a representative conversion-type HEO anode: single-phase spinel formation has been established,[3] and reversible capacities of approximately 680 mAh g⁻¹ at low current density and 596.5 mAh g⁻¹ after 1200 cycles at 2.0 A g⁻¹ have been reported for this nominal composition.[4,6]

Lithium storage in spinel (FeCoNiCrMn)₃O₄ proceeds through substantial structural reconstruction and conversion rather than simple insertion into an intact host. Atomic-scale analysis has shown Mn nanocrystal formation already at 0.5 V lithiation and metallic Cr, Fe, Ni, and Co at deeper lithiation,[5] directly demonstrating progressive conversion. Complementary in-situ XRD/ex-situ TEM studies resolved a spinel → mixed spinel/rock-salt → rock-salt pathway,[7] while recent work describes rock-salt-like intermediates coexisting with Li₂O and metallic products and identifies oxygen migration as an important kinetic process during conversion.[20] Lithium storage in these HEOs therefore involves coupled nucleation, cation/oxygen rearrangement, phase-boundary motion, strain accommodation, and heterogeneous structural reconstruction over a broad reaction interval.

Ball milling and Mg incorporation provide two distinct ways to modify this conversion-type material. For the same nominal (FeCoNiCrMn)₃O₄ composition, mechanical processing and particle fragmentation have been reported to increase conversion reversibility and interfacial storage,[6,12] while high-energy milling can perturb the spinel/rock-salt balance in related spinel HEOs.[11] Mg-containing conversion HEOs show a different materials response: electrochemically inactive Mg-derived components can stabilize oxide-derived structures,[8–10] and operando imaging has associated higher Mg content with improved structural retention but lower accessible capacity.[9] These studies establish that both processing and composition can strongly alter HEO structure and battery performance. However, how the distinct materials changes induced by milling and Mg incorporation govern the progression and relaxation of conversion remains insufficiently resolved.

GITT provides a useful route to examine this connection. In HEO anode studies, GITT has generally been used to estimate and compare an apparent Li-ion diffusion coefficient, including in mechanically processed (FeCoNiCrMn)₃O₄.[6] Studies of other phase-transforming electrodes have shown that the pulse and relaxation response can also contain information on state-dependent kinetics, phase transformation, and structural relaxation beyond a single diffusivity.[21–24,26] Preserving the state-resolved polarization and current-off relaxation therefore offers a way to examine how synthesis-controlled structural changes are expressed during conversion.

Here, the effects of ball milling and Mg incorporation on spinel Fe–Co–Ni–Cr–Mn HEO are examined from structure and morphology to electrochemical performance and conversion dynamics. Conventional measurements first establish that ball milling increases accessible capacity whereas Mg incorporation lowers it. GITT then reveals that these capacity changes do not map directly onto the effective timescale of conversion-associated current-off relaxation: ball milling accesses more reaction without faster relaxation, while Mg suppresses accessible conversion without a proportional change in relaxation time. Differential-capacity analysis localizes this mismatch to the conversion region, and cycle-resolved GITT shows that the relaxation response itself evolves strongly with reaction history. A minimal multi-step microkinetic model is finally used to explain how reaction accessibility and internal relaxation can vary independently enough for greater conversion to coexist with slower relaxation. Although such decoupling is not unique to HEOs, the multication and structurally heterogeneous nature of HEO conversion provides a natural setting in which it becomes experimentally visible.[10,20]

# 2. Results and Discussion

## 2.1. Structural and morphological characteristics of the HEO series

Figures 1 and 2 are reserved for the structural, compositional, and morphological characterization of HEO, BM-HEO, Mg-HEO, and BM-Mg-HEO. The current working dataset indicates that all four materials retain a predominantly spinel-type HEO structure, while Mg incorporation and ball milling introduce distinct compositional, lattice, particle, and surface-level changes. Ball milling also produces a marked increase in BET surface area. These characterization results will be finalized using the collaborator-verified XRD/refinement, ICP-OES, TEM/SAED/EDS, SEM, BET, and, if retained, XPS datasets.

At this stage, Figures 1–2 are used only to establish that Mg incorporation and ball milling produce distinguishable materials-level perturbations before electrochemical testing. Detailed phase assignments, Mg-site interpretation, quantitative lattice changes, and XPS-based mechanistic claims are intentionally deferred until the final characterization package is frozen.

**[[YOO GROUP INPUT REQUIRED — finalize Figure 1–2 panel composition and the corresponding structural interpretation using the verified XRD/ICP/TEM/SAED/EDS/SEM/BET dataset; decide separately whether XPS remains in the Supporting Information or is promoted to a main characterization figure.]]**



## 2.2. Ball milling increases accessible capacity whereas Mg incorporation suppresses it

The conventional electrochemical response first establishes the simplest difference among the four materials: how much lithium-storage reaction can be accessed (Figure 3). The first lithiation/delithiation capacities are 901.25/609.12 mAh g⁻¹ for HEO, 1056.10/782.08 mAh g⁻¹ for BM-HEO, 731.15/458.91 mAh g⁻¹ for Mg-HEO, and 944.07/580.83 mAh g⁻¹ for BM-Mg-HEO, corresponding to initial Coulombic efficiencies of 67.59%, 74.05%, 62.77%, and 61.52%, respectively. Ball milling therefore increases the accessible capacity in both the Mg-free and Mg-containing materials, whereas Mg incorporation lowers it relative to the corresponding Mg-free composition.

The milling effect is readily understood at the materials level. Ball milling strongly increases surface area and reduces the characteristic particle/domain dimensions, increasing the fraction of material and interfaces that can participate electrochemically. Previous work on the same five-cation spinel family likewise showed that particle fragmentation can increase conversion reversibility and interfacial storage.[12] The higher capacity after milling therefore does not, by itself, imply faster intrinsic conversion kinetics; it can arise because a larger reaction population becomes accessible.

Mg incorporation produces the opposite capacity trend. Mg-containing electrodes operate at lower absolute capacity, and the lower reversible reaction extent remains evident after the first cycle. This behavior is consistent with previous HEO studies in which electrochemically inactive or weakly active cations stabilize oxide-derived states and reduce the fraction of material undergoing deep conversion.[8–10] Importantly, the capacity difference is not erased by milling: BM-Mg-HEO recovers part of the lost utilization but remains below BM-HEO.

The rate-capability data reinforce the need to separate absolute capacity from normalized retention. BM-HEO remains above HEO in absolute capacity throughout the measured rate sequence, including approximately 193 versus 79 mAh g⁻¹ at 5 C. Mg-HEO retains a larger fraction of its lower starting capacity at high rate and reaches approximately 185 mAh g⁻¹ at 5 C, but this normalized advantage does not demonstrate that Mg simply accelerates the conversion reaction. Figure 3 is therefore used to establish reaction accessibility and capacity, not to assign a kinetic rate.

The cycle-resolved differential-capacity response also shows that the reaction pathway changes substantially after the first lithiation. The pronounced first-cycle cathodic conversion feature broadens and attenuates in later cycles, consistent with the reconstructive conversion reported for spinel HEO anodes.[5,7,10] This observation becomes important below because the GITT relaxation cannot be treated as a stationary property of the pristine material.

Figure 3 thus sets up the central question of the electrochemical analysis. Ball milling enables more electrochemical reaction and higher capacity, whereas Mg incorporation suppresses accessible reaction. If capacity were controlled primarily by a single kinetic speed, the higher-capacity ball-milled material might be expected to relax more rapidly. Figure 4 tests this expectation directly.


## 2.3. Higher accessible capacity does not imply faster conversion-associated relaxation

GITT was used to compare the current-off dynamics of the four materials (Figure 4). Each step consists of a 10 min galvanostatic pulse followed by a 60 min open-circuit rest. The relaxation magnitude, $\Delta E_{\mathrm{relax}}$, is defined from 3 s after current interruption to the end of the 60 min rest, and $t_{63}$ is the time required to complete 63.2% of this observed relaxation. Because $t_{63}$ is extracted directly from the relaxation trajectory, it is used here as a model-free effective kinetic descriptor rather than as a microscopic time constant or a direct measurement of the forward conversion rate.

The first-cycle results expose an apparent paradox. Over the common 200–800 mAh g⁻¹ interval, the median $t_{63}$ increases from 8.68 min for HEO to 11.57 min for BM-HEO even though ball milling markedly increases accessible capacity. The same tendency is present in the Mg-containing pair, with median $t_{63}$ values of 11.01 min for Mg-HEO and 12.99 min for BM-Mg-HEO. Ball milling therefore enables more reaction without accelerating the subsequent current-off relaxation; if anything, the ensemble relaxation becomes slower.

Mg incorporation provides a complementary perturbation. The median $\Delta E_{\mathrm{relax}}$ decreases from 160.9 mV for HEO to 109.5 mV for Mg-HEO, yet the corresponding $t_{63}$ does not shorten and instead changes from 8.68 to 11.01 min. A smaller relaxation magnitude is therefore not evidence of faster kinetics. Mg reduces how strongly the system is displaced during the pulse without producing a proportional acceleration of the relaxation that follows.

These trends show why accessible capacity and $t_{63}$ cannot be placed on one fast–slow axis. A shorter $t_{63}$ would be consistent with faster conversion-related relaxation under otherwise comparable conditions, but the amount of reaction accessed during a pulse also depends on surface area, reaction accessibility, the population of available states, and the evolving conversion pathway. Ball milling can therefore increase capacity by opening additional reaction population even if that population includes slower-relaxing states. Conversely, Mg can reduce accessible conversion without causing the remaining states to relax proportionally faster or slower.

Diffusion and charge transfer remain part of the GITT response, but a single transport parameter does not explain the materials ordering observed here. The key question becomes whether the unusual relaxation is actually associated with conversion. Figure 5 addresses this point independently using the electrochemical conversion signature in $dQ/dV$.


## 2.4. The capacity–relaxation mismatch is localized to the conversion region

The state-resolved GITT relaxation develops a distinct excess feature during the first lithiation (Figure 5a). The feature is strongest in HEO, becomes lower and broader after ball milling, and is strongly suppressed in the Mg-containing materials. To determine whether this response belongs specifically to conversion rather than to a generic cell relaxation, the background-subtracted GITT excess was compared with the independently derived first-cycle cathodic $dQ/dV$ response.

The two observables localize to nearly the same voltage region for all four materials (Figure 5b,c). The $dQ/dV$ maxima occur at approximately 0.545, 0.589, 0.419, and 0.485 V for HEO, BM-HEO, Mg-HEO, and BM-Mg-HEO, respectively, whereas the corresponding GITT excess maxima occur at 0.527, 0.618, 0.387, and 0.503 V. All four pairs lie within 32 mV. The excess relaxation can therefore be assigned conservatively as conversion-associated, although the present data do not identify a unique microscopic step such as nucleation, phase-boundary motion, oxygen rearrangement, or metal/Li₂O formation.[5,7,20]

This localization makes the ball-milling result particularly informative. BM-HEO has higher accessible capacity than HEO, but its conversion-associated relaxation peak is lower and broader rather than simply larger or faster. The result is consistent with milling increasing the amount of material that can participate in conversion while distributing that reaction over a broader set of local environments. Because the ball-milled material also exhibits a longer $t_{63}$, the added reaction population is not equivalent to a uniformly accelerated conversion process.

Mg incorporation produces the complementary behavior. Mg-HEO has lower capacity and a strongly suppressed first-cycle conversion-associated excess, with the feature shifted to lower potential. This is consistent with reduced access to deep conversion and greater stabilization of oxide-derived states, as reported in related Mg-containing HEO systems.[8–10] However, the weak excess amplitude does not translate into a short $t_{63}$. Mg therefore primarily changes how much conversion-associated response is accessed or excited, not simply the rate at which every participating state relaxes.

BM-Mg-HEO combines both effects: milling partially restores accessible capacity and broadens the conversion-associated response, while the stronger Mg-related suppression remains evident. Across the four samples, Figure 5 therefore sharpens the central result from Figure 4: the amount of conversion that is electrochemically accessible and the effective rate of conversion-associated relaxation do not change in parallel.

The next question is whether this mismatch is a fixed property established by synthesis or whether it evolves as the conversion electrode itself evolves. Cycle-resolved GITT provides the answer.


## 2.5. Conversion-associated relaxation is history-dependent

The raw GITT sequence contains repeated lithiation and delithiation cycles, allowing the conversion-associated response to be tracked beyond the first cycle (Figure 6). This comparison reveals that the relaxation is not a stationary fingerprint of the pristine material. Instead, its magnitude and location evolve strongly as the cycled conversion state is established.

For lithiation over the common normalized reaction-state interval $z=0.4$–0.9, the conversion-associated excess peak changes markedly between cycles. HEO decreases from 71.2 mV in cycle 1 to 31.0 mV in cycle 3, and BM-HEO decreases from 44.8 to 22.4 mV. Mg-HEO shows the opposite evolution, increasing from 15.9 to 27.0 mV, whereas BM-Mg-HEO remains comparatively similar at 21.1 and 20.8 mV. At the same time, the peak position converges from the later first-cycle region, $z\approx0.66$–0.79, toward a common later-cycle region around $z\approx0.50$–0.56.

The effective relaxation timescale changes much less than the relaxation amplitude. From cycle 1 to cycle 3, the amplitude ratios $A_3/A_1$ span 0.435–1.698, whereas $t_{63,3}/t_{63,1}$ is confined to 0.845–0.923. Thus, cycling strongly redistributes how much conversion-associated relaxation is excited while producing only modest changes in its effective timescale. The first-cycle hump is therefore not a fixed kinetic fingerprint.

The later-cycle capacity provides an additional constraint on the interpretation. Approximate third-cycle GITT lithiation capacities are 700, 833, 450, and 533 mAh g⁻¹ for HEO, BM-HEO, Mg-HEO, and BM-Mg-HEO, respectively, and the corresponding delithiation capacities are similar. Ball milling therefore continues to provide a larger accessible reversible reaction extent while retaining a longer $t_{63}$ than the corresponding unmilled material. In contrast, Mg continues to suppress reversible capacity by approximately 35–36% in both unmilled and milled pairs even though the later-cycle $t_{63}$ values approach those of the Mg-free analogues. The separation between reaction extent and relaxation is therefore not restricted to an irreversible first-cycle event.

The cycle-dependent hump evolution is robust to the choice of later-cycle background. Exponential and linear backgrounds give peak amplitudes differing by less than 0.012%, identical peak positions, and maximum background differences below 0.0016 mV for cycles 2–3. The detailed sensitivity analysis is provided in the Supporting Information.

Figures 3–6 therefore establish the apparent contradiction in its simplest form. Ball milling enables more conversion-related reaction yet leaves a slower ensemble relaxation, while Mg suppresses accessible conversion without a proportional change in relaxation time. This behavior requires a kinetic picture in which reaction accessibility and internal relaxation are related but not identical quantities. Figure 7 introduces the minimal microkinetic description needed to make this possible.


## 2.6. Multi-step microkinetics resolves the apparent capacity–relaxation contradiction

Conversion reactions generally proceed through multiple intermediates and coupled electrochemical/structural steps rather than through a single elementary process. Microkinetic descriptions of conversion electrodes likewise require state evolution and multiple reactions rather than one effective rate constant.[30] For the present HEO system, the goal is not to identify a unique microscopic rate-limiting step, but to test whether a minimal multi-state network can physically reconcile the experimental observation of more accessible conversion with slower relaxation.

The effective network in Figure 7a contains an electrochemical activation step, $A+\mathrm{Li}^++e^- \rightleftharpoons B$, an internal nucleation/activity coordinate, $B\rightarrow N$, and an electrochemical conversion/growth step, $B+\mathrm{Li}^++e^- \rightleftharpoons P$. The labels $A$, $B$, $N$, and $P$ represent effective kinetic states and are not assigned to specific experimentally resolved phases. This distinction is important because the model is intended to capture the logic of a multi-step conversion network rather than to fit atomistic identities.

The current interruption provides the central physical point (Figure 7b). During the pulse, the external current is carried by the electrochemical steps, $j_{\mathrm{ext}}=r_1+r_3$. At open circuit, $j_{\mathrm{ext}}=0$, but this condition does not require $r_1=r_3=0$. The model permits an internal counter-current, $r_1=-r_3\neq0$, so conversion-state reorganization can continue even though no net current flows through the external circuit. In the illustrative simulation, the opposing rates remain finite immediately after interruption while their sum is numerically zero, and they decay together with the continuing voltage relaxation. Long current-off relaxation is therefore compatible with ongoing redistribution within a coupled conversion network.

The same model explains why relaxation amplitude and timescale need not co-vary (Figure 7c). Linearization about a local cycled state gives

\[
\frac{d\,\delta\mathbf{x}}{dt}=\mathbf{J}\delta\mathbf{x},
\]

and therefore

\[
E(t)-E_{\mathrm{eq}}=\sum_i B_i\exp(-t/\tau_i).
\]

The coefficients $B_i$ depend on which internal states are populated or excited and on their voltage sensitivity, whereas the $\tau_i$ values arise from the kinetic eigenvalues of the coupled network. Increasing the amount of accessible reaction can therefore increase or redistribute the state population without shortening the slow relaxation modes. In particular, ball milling can expose additional conversion-active material and thereby increase capacity while also increasing the contribution of heterogeneous or slower-relaxing states. Mg can instead suppress the accessible reaction population while leaving the dominant relaxation eigen-timescale comparatively unchanged.

This interpretation resolves the experimental trends without requiring conversion capacity and relaxation speed to be controlled by one parameter (Figure 7d). Ball milling primarily increases reaction accessibility, consistent with its increased surface area and higher capacity, but does not accelerate the conversion-associated relaxation. Mg primarily suppresses accessible conversion and the first-cycle relaxation amplitude, yet the later-cycle relaxation timescale approaches that of the Mg-free material. The three quantities—accessible reaction extent, relaxation amplitude, and effective relaxation timescale—are therefore coupled but distinct consequences of the conversion network.

This separation is not proposed as an HEO-exclusive phenomenon. Multi-step conversion electrodes in general can exhibit different controls over reaction extent and relaxation kinetics.[30] The HEO is nevertheless a particularly suitable system in which to observe the separation because multiple redox-active cations, chemically diverse local environments, and reconstructive phase evolution generate a broad set of possible internal conversion states. Recent studies further show that multication synergy can stabilize specific nanoscale oxide/metal states and that high-entropy spinel conversion can exhibit kinetically sluggish phase evolution that is altered by particle size.[10,20] The present results therefore position the HEO not as an exception to conversion kinetics, but as a multicomponent conversion system in which reaction accessibility and internal relaxation become experimentally separable.

The model is consequently used as a mechanistic-consistency test rather than as a unique rate-constant fit. Different microscopic parameter sets can generate similar relaxation at one pulse current, so no elementary rate-limiting step is assigned. The central conclusion is instead simpler: more conversion can coexist with slower relaxation because the amount of reaction accessed and the internal relaxation modes of the resulting conversion state are not the same kinetic coordinate.


# 3. Conclusions

Ball milling and Mg incorporation produce opposite changes in accessible capacity but do not produce corresponding monotonic changes in conversion-associated relaxation. Ball milling increases surface area and accessible reaction, giving higher capacity in both Mg-free and Mg-containing HEOs, yet the effective current-off relaxation remains slower rather than faster. Mg incorporation lowers accessible conversion-related capacity and strongly suppresses the first-cycle conversion-associated relaxation amplitude, while the relaxation timescale does not decrease in proportion.

Independent $dQ/dV$ localization places the excess GITT relaxation in the conversion region, and cycle-resolved analysis shows that this response is history-dependent: its amplitude changes much more strongly with cycling than its effective timescale. The apparent mismatch between conversion extent and relaxation is therefore an intrinsic feature of the evolving conversion network rather than a simple first-cycle artifact.

A minimal multi-step microkinetic model provides a physically consistent explanation. Reaction accessibility controls how much of the conversion network becomes populated, whereas the post-interruption relaxation is governed by the internal kinetic modes of that network. Ball milling can therefore access additional conversion population—including slower-relaxing states—while Mg can suppress accessible reaction without proportionally changing the dominant relaxation timescale. The results show that high capacity does not necessarily imply faster conversion-associated kinetics.

Although this separation is not unique to HEOs, multication disorder, multiple redox centers, and reconstructive phase evolution make spinel HEOs a natural platform in which reaction accessibility and internal relaxation can be independently revealed. These findings provide a mechanistic basis for designing conversion electrodes by controlling not only how much reaction is accessible, but also which kinetic states are populated during cycling.

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

Galvanostatic charge–discharge measurements were performed using a WonATech battery cycler between 0.005 and 2.5 V. The principal low-rate comparison was conducted at 0.1 C. Rate-capability measurements used a stepwise sequence from 0.1 C to 5 C followed by recovery at 0.1 C.

**[[YOON LAB INPUT REQUIRED — verify the capacity basis defining 1 C; exact number of cycles at each rate; confirm the WonATech charge/discharge convention before finalizing lithiation/delithiation labels.]]**

GITT was performed at 100 mA g⁻¹ between 0.005 and 2.5 V using repeated 10 min current pulses followed by 60 min open-circuit relaxation. A common 3 s post-interruption reference was used because the Mg-free and Mg-containing datasets were acquired at different time resolutions in the early current-off period. The relaxation magnitude was defined as

\[
\Delta E_{\mathrm{relax}}
=
E_{60\,\mathrm{min}}-E_{3\,\mathrm{s}},
\]

with absolute magnitude used for comparison where appropriate. The characteristic time $t_{63}$ was defined as the first time required to reach 63.2% of the observed 3 s-to-60 min voltage relaxation. This definition does not assume single-exponential relaxation.

The late-stage excess response was obtained by subtracting a smooth sample-specific background from the state-resolved $\Delta E_{\mathrm{relax}}$ response. Peak position, peak amplitude, and FWHM-like width were used as comparative descriptors. Detailed background definitions, window sensitivity, short-time current-off analysis, and additional relaxation descriptors are provided in the Supporting Information.

First-cycle differential-capacity curves were obtained from the corresponding galvanostatic voltage profiles using the same differentiation and smoothing procedure for all four materials. The current manuscript-development curves were reconstructed from the latest vector voltage profiles because the original numerical first-cycle source files have not yet been recovered; this source should be replaced by the original numerical data before submission if available.



## 4.4. Minimal conversion microkinetic model

A minimal multi-step microkinetic model was used to test whether the experimentally observed separation between accessible reaction extent and conversion-associated relaxation is physically consistent with a coupled conversion network. The model was not fitted to obtain unique microscopic rate constants and was not used to assign a unique elementary rate-limiting step.

The effective reaction network consists of three steps:

\[
A+\mathrm{Li}^{+}+e^{-}\rightleftharpoons B,
\]

\[
B\rightarrow N,
\]

and

\[
B+\mathrm{Li}^{+}+e^{-}\rightleftharpoons P.
\]

Here, $A$, $B$, $N$, and $P$ denote effective kinetic states rather than atomistically identified phases or chemical species. The first and third reactions carry Faradaic current, while the second describes an effective nucleation/activity coordinate.

During a galvanostatic pulse, the potential is determined from the current balance

\[
j_{\mathrm{ext}}=r_1+r_3.
\]

After current interruption, the external current is set to zero,

\[
j_{\mathrm{ext}}=r_1+r_3=0,
\]

while finite opposing internal rates, $r_1=-r_3\neq0$, are permitted. This allows the internal conversion state to continue evolving during open-circuit relaxation.

The coupled state equations were integrated numerically for a 600 s pulse followed by a 3600 s rest, matching the experimental GITT timing. A representative parameter set was used only to demonstrate current-off internal counter-current and prolonged voltage relaxation. Local linearization of the coupled state dynamics gives

\[
d(\delta\mathbf{x})/dt=\mathbf{J}\delta\mathbf{x},
\]

with a corresponding voltage response represented as a sum of relaxation modes,

\[
E(t)-E_{\mathrm{eq}}=\sum_i B_i\exp(-t/\tau_i).
\]

The coefficients $B_i$ and relaxation times $\tau_i$ are interpreted as model-level state-excitation/voltage-sensitivity weights and kinetic eigen-timescales, respectively; they are not treated as directly measured microscopic modes.

A synthetic current-dependence test was used only as an internal identifiability and future-discrimination analysis and is retained in the Supporting Information. The main-text use of the model is limited to testing mechanistic consistency of the experimentally observed capacity–relaxation decoupling.

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

30. Alsaç, E. P.; Sharma, A. K.; Yoon, S. G.; Vishnugopi, B. S.; Wang, C.; Thomas, T. A.; Nelson, D. L.; Eze, U. D.; Jeong, W. J.; Harris, J.; Mukherjee, P. P.; McDowell, M. T. Linking Pressure to Electrochemical Evolution in Solid-State Conversion Cathode Composites. **ACS Applied Materials & Interfaces** 2026, 18, 1626–1640. DOI: 10.1021/acsami.5c20956.

# Figure Captions

**Figure 1. Mg incorporation and ball milling alter crystal structure, composition, and nanoscale microstructure of spinel HEOs.** The four materials are compared using the final XRD, ICP-OES, HRTEM/SAED, and elemental-mapping dataset. The figure establishes the parent spinel-type structure, the comparatively modest lattice/compositional perturbation associated with Mg incorporation, and milling-induced changes in coherent-domain/microstructural characteristics. No unique Mg site is assigned without final refinement, and the chemically incompatible preliminary CoGa₂O₄ indexing is excluded. **[[YOO GROUP INPUT REQUIRED — freeze final refined XRD/HRTEM/SAED/ICP dataset and panel order.]]**

**Figure 2. Ball milling primarily modifies particle morphology and physical surface characteristics.** SEM morphology, particle/domain-size statistics, and BET surface area are used to compare HEO, BM-HEO, Mg-HEO, and BM-Mg-HEO before cycling. XPS is included only if the final dataset is reproducible and mechanistically defensible. Electrochemically derived interface metrics are intentionally excluded from this characterization figure and are introduced in Figure 3. **[[YOO GROUP INPUT REQUIRED — freeze final SEM/particle-size/BET package and final XPS inclusion decision.]]**

**Figure 3. Ball milling increases accessible capacity whereas Mg incorporation suppresses it.** (a) First-cycle voltage profiles of HEO, BM-HEO, Mg-HEO, and BM-Mg-HEO, with first-cycle capacities and initial Coulombic efficiencies. (b) Specific capacity during 0.1 C cycling under the common electrolyte condition. (c) Absolute rate capability over the 0.1–5 C sequence and recovery at 0.1 C. (d) Cycle-resolved differential-capacity response, highlighting the strong first-cycle conversion feature and its subsequent evolution. The figure establishes the amount of electrochemical reaction that is accessible before the relaxation kinetics are examined.

**Figure 4. Higher accessible capacity does not imply faster conversion-associated relaxation.** (a) Representative 10 min GITT pulse followed by a 60 min open-circuit rest, defining the 3 s-to-60 min relaxation magnitude, $\Delta E_{\mathrm{relax}}$, and model-free effective relaxation time, $t_{63}$. (b) State-resolved $\Delta E_{\mathrm{relax}}$. (c) Corresponding $t_{63}$ values. (d) Median $\Delta E_{\mathrm{relax}}$ versus median $t_{63}$ over the common 200–800 mAh g⁻¹ interval. Ball milling increases accessible capacity while lengthening, rather than shortening, the effective relaxation, whereas Mg incorporation lowers the relaxation magnitude without a proportional shortening of $t_{63}$.

**Figure 5. The anomalous current-off relaxation is localized to the conversion region.** (a) State-resolved first-cycle relaxation showing the conversion-associated excess feature. (b) Background-subtracted GITT excess relaxation on a voltage axis together with the first-cycle cathodic $dQ/dV$ response. (c) Comparison of $dQ/dV$ and GITT excess-peak voltages; all pairs lie within 32 mV. (d) Peak amplitude versus FWHM-like width of the excess response. Ball milling increases accessible capacity while broadening and lowering the concentrated conversion-associated response, whereas Mg incorporation suppresses accessible conversion and the corresponding excess relaxation.

**Figure 6. Conversion-associated relaxation evolves with cycle history.** (a) Background-subtracted conversion-associated relaxation profiles for cycles 1–3 over the common normalized lithiation coordinate, $z=0.4$–0.9. (b) Conversion-associated peak amplitude versus cycle. (c) Median ensemble/state-resolved $t_{63}$ versus cycle over the same state interval. (d) Normalized change map of $A_3/A_1$ versus $t_{63,3}/t_{63,1}$ with unity reference lines. The amplitude ratio spans 0.435–1.698 while the timescale ratio remains within 0.845–0.923, showing that cycling changes how strongly the conversion-associated response is populated or excited much more than it changes the effective relaxation timescale.

**Figure 7. Microkinetic interpretation of the capacity–relaxation mismatch.** (a) Effective multi-step conversion network containing electrochemical activation, internal nucleation/activity evolution, and electrochemical conversion/growth states. (b) Current-on and current-off balances. At open circuit, $j_{\mathrm{ext}}=r_1+r_3=0$ does not require $r_1=r_3=0$; finite opposing internal currents can persist while the voltage relaxes. (c) Local linearized multi-state response, $E(t)-E_{\mathrm{eq}}=\sum_i B_i\exp(-t/\tau_i)$, separating state-excitation/voltage-sensitivity amplitudes from kinetic eigen-timescales. (d) Experimental constraints on the model: ball milling accesses more reversible reaction while retaining slower relaxation, whereas Mg suppresses accessible reaction without a proportional change in later-cycle $t_{63}$. The model is used as a mechanistic-consistency interpretation rather than as a unique rate-limiting-step fit.
