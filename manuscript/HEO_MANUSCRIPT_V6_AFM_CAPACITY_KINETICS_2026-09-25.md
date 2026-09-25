# HEO Manuscript v6 — AFM-Target Capacity–Kinetics/Conversion Microkinetic Draft

**Date:** 2026-09-25  
**Status:** full narrative reorganization around capacity–kinetics relation; Figures 3–7 logic aligned  
**Scientific backbone:** Figures 1–2 materials perturbations → Figure 3 accessible capacity → Figure 4 GITT kinetic mismatch → Figure 5 conversion localization → Figure 6 history dependence → Figure 7 conversion microkinetic resolution  
**Literature basis:** \`HEO_REFERENCE_MASTER_VERIFIED_2026-09-18.md\`

> Verified information is written directly. Missing experimental metadata are not inferred. Inputs expected from the Yoo group and Yoon Lab remain explicitly marked. The Figure 5 differential-capacity peak positions currently come from reconstruction of the latest vector voltage profiles; the underlying numerical first-cycle files should replace this source if recovered before submission.

---

# Working title

**Structural Modification Reshapes Capacity and Conversion Kinetics in Spinel High-Entropy Oxide Anodes**

Alternative:

**Capacity and Conversion Kinetics Do Not Follow a Single Rate Axis in Spinel High-Entropy Oxide Anodes**

---


# Abstract

Conversion-type high-entropy oxide (HEO) anodes are commonly evaluated in terms of capacity and kinetics, yet the relationship between these two characteristics remains insufficiently understood. Higher accessible capacity is often associated with improved reaction kinetics, but whether this correspondence holds for HEOs undergoing multistep conversion reactions is unclear. Here, ball milling and Mg incorporation are used as complementary perturbations to examine the relationship between accessible capacity and conversion-associated kinetics probed by GITT relaxation. Ball milling increases accessible capacity while slowing the effective relaxation kinetics, whereas Mg incorporation suppresses accessible conversion without a proportional change in kinetic timescale. The anomalous kinetic response is localized to the conversion region and evolves strongly with cycling. A literature-informed microkinetic model first recovers the expected homogeneous behavior in which faster kinetics increases cutoff-limited capacity and accelerates relaxation, and then shows how a heterogeneous multistep conversion network can instead produce higher accessible capacity together with slower internal relaxation. These results show that capacity and relaxation are kinetically linked but not kinetically equivalent, and that conversion performance cannot be reduced to a single fast–slow kinetic descriptor in multicomponent electrodes.

**Keywords:** high-entropy oxide; conversion anode; ball milling; magnesium incorporation; GITT; electrochemical relaxation; microkinetics

# 1. Introduction

Electrode performance is commonly discussed in terms of how much electrochemical reaction can be accessed and how rapidly that reaction proceeds. Under finite-rate operation, higher accessible capacity or improved rate capability is often associated with faster reaction kinetics because lower kinetic polarization allows a larger fraction of the thermodynamically available reaction to be reached before the voltage cutoff. In a simple homogeneous reaction, the kinetic processes that govern reaction progress under current also influence the return toward equilibrium after current interruption. Higher accessible capacity would therefore generally be expected to accompany faster relaxation. Whether this correspondence remains valid for reconstructive conversion electrodes is less clear.

Conversion reactions are not single-step processes. Electron transfer and Li incorporation occur together with metal–oxygen bond rearrangement, nucleation and phase growth, cation/oxygen redistribution, and product formation, often across spatially heterogeneous regions of the electrode. These coupled processes can operate over different characteristic times and may respond differently to structural or compositional modification. The relationship between the amount of conversion accessed under load and the kinetic response observed after current interruption therefore needs to be established experimentally rather than assumed from capacity alone.

High-entropy oxides (HEOs) provide a useful platform for testing this relationship. HEOs accommodate several principal cations within a common oxide structure, producing broad distributions of local coordination and redox environments that are difficult to realize in conventional single- or few-cation oxides.[1,2] Spinel (FeCoNiCrMn)₃O₄ is a representative conversion-type HEO anode for which single-phase spinel formation and high reversible capacity have been reported.[3,4,6] Its lithiation proceeds through substantial structural reconstruction rather than simple insertion into an intact host. Atomic-scale analysis has shown Mn nanocrystal formation already at 0.5 V and metallic Cr, Fe, Ni, and Co at deeper lithiation,[5] while complementary diffraction and microscopy studies have resolved spinel-to-rock-salt-like evolution, Li₂O/metal formation, and oxygen/cation rearrangement during conversion.[7,20] The multication and reconstructive nature of this chemistry makes HEOs a natural system in which to test whether accessible capacity and kinetic response necessarily evolve together.

Ball milling and Mg incorporation offer complementary perturbations of this conversion landscape. For the same nominal (FeCoNiCrMn)₃O₄ composition, mechanical processing and particle fragmentation have been reported to increase conversion reversibility and interfacial storage,[6,12] while high-energy milling can alter the spinel/rock-salt balance in related spinel HEOs.[11] Mg-containing conversion HEOs show a different response: electrochemically inactive or weakly active Mg-derived components can stabilize oxide-derived structures,[8–10] and operando imaging has associated higher Mg content with greater structural retention but lower accessible capacity.[9] These contrasting modifications provide a way to vary reaction accessibility and structural stability without assuming a uniform change in all kinetic processes. GITT is particularly useful in this context. Although GITT in HEO anodes has largely been used to estimate an apparent Li-ion diffusion coefficient,[6] studies of phase-transforming electrodes show that the pulse and relaxation response also contains information on state-dependent kinetics, phase transformation, and structural relaxation beyond a single diffusivity.[21–24,26] GITT relaxation can therefore serve as a state-resolved probe of conversion-associated kinetics.

Here, spinel Fe–Co–Ni–Cr–Mn HEO, ball-milled HEO (BM-HEO), Mg-containing HEO (Mg-HEO), and BM-Mg-HEO are compared to determine how accessible capacity and conversion-associated kinetics are related. Conventional electrochemical measurements first establish that ball milling increases accessible capacity whereas Mg incorporation suppresses it. GITT relaxation then reveals that these capacity changes do not follow a single fast–slow kinetic trend. Differential-capacity analysis localizes the anomalous relaxation to the conversion region, and cycle-resolved GITT shows that the kinetic response evolves strongly with reaction history. A literature-informed microkinetic model is finally used to test whether the observed capacity–kinetics mismatch is physically consistent with a heterogeneous multistep conversion network.

# 2. Results and Discussion

## 2.1. Structural and morphological characteristics of the HEO series

Figures 1 and 2 are reserved for the structural, compositional, and morphological characterization of HEO, BM-HEO, Mg-HEO, and BM-Mg-HEO. The current working dataset indicates that all four materials retain a predominantly spinel-type HEO structure, while Mg incorporation and ball milling introduce distinct compositional, lattice, particle, and surface-level changes. Ball milling also produces a marked increase in BET surface area. These characterization results will be finalized using the collaborator-verified XRD/refinement, ICP-OES, TEM/SAED/EDS, SEM, BET, and, if retained, XPS datasets.

At this stage, Figures 1–2 are used only to establish that Mg incorporation and ball milling produce distinguishable materials-level perturbations before electrochemical testing. Detailed phase assignments, Mg-site interpretation, quantitative lattice changes, and XPS-based mechanistic claims are intentionally deferred until the final characterization package is frozen.

**[[YOO GROUP INPUT REQUIRED — finalize Figure 1–2 panel composition and the corresponding structural interpretation using the verified XRD/ICP/TEM/SAED/EDS/SEM/BET dataset; decide separately whether XPS remains in the Supporting Information or is promoted to a main characterization figure.]]**



## 2.2. Ball milling increases accessible capacity whereas Mg incorporation suppresses it

The conventional electrochemical response first establishes the principal performance difference among the four materials: how much lithium-storage reaction can be accessed (Figure 3). The first lithiation/delithiation capacities are 901.25/609.12 mAh g⁻¹ for HEO, 1056.10/782.08 mAh g⁻¹ for BM-HEO, 731.15/458.91 mAh g⁻¹ for Mg-HEO, and 944.07/580.83 mAh g⁻¹ for BM-Mg-HEO, corresponding to initial Coulombic efficiencies of 67.59%, 74.05%, 62.77%, and 61.52%, respectively. Ball milling therefore increases accessible capacity in both the Mg-free and Mg-containing materials, whereas Mg incorporation lowers it relative to the corresponding Mg-free composition.

The milling effect is accompanied by a marked increase in surface area and reduced particle/domain dimensions, which can increase the fraction of material and interfaces that participate electrochemically. Previous work on the same five-cation spinel family likewise showed that particle fragmentation can increase conversion reversibility and interfacial storage.[12] The capacity increase after milling is therefore consistent with improved reaction accessibility, but capacity alone does not establish whether the underlying conversion kinetics are faster.

Mg incorporation produces the opposite capacity trend. Mg-containing electrodes exhibit lower absolute capacity, and the lower reversible reaction extent persists beyond the first cycle. This behavior is consistent with previous HEO studies in which electrochemically inactive or weakly active cations stabilize oxide-derived states and reduce the fraction of material undergoing deep conversion.[8–10] Milling recovers part of the lost utilization in BM-Mg-HEO, but the capacity remains below that of BM-HEO.

The rate-capability data reinforce the distinction between absolute capacity and kinetic interpretation. BM-HEO remains above HEO in absolute capacity throughout the measured rate sequence, including approximately 193 versus 79 mAh g⁻¹ at 5 C. Mg-HEO retains a larger fraction of its lower starting capacity at high rate and reaches approximately 185 mAh g⁻¹ at 5 C, but this normalized advantage does not by itself establish faster intrinsic conversion kinetics. Figure 3 therefore defines the accessible reaction extent that must be compared independently with the GITT kinetic response.

The central question is consequently straightforward: does the higher capacity produced by ball milling correspond to faster conversion-associated kinetics, and does the lower capacity produced by Mg correspond to slower kinetics? Figure 4 tests this expectation using GITT relaxation.

## 2.3. Higher accessible capacity does not imply faster conversion-associated kinetics

GITT was used to compare the relaxation dynamics of the four materials (Figure 4). Each step consists of a 10 min galvanostatic pulse followed by a 60 min open-circuit rest. The relaxation magnitude, $\Delta E_{\mathrm{relax}}$, is defined from 3 s after current interruption to the end of the 60 min rest, and $t_{63}$ is the time required to complete 63.2% of this observed relaxation. Because $t_{63}$ is extracted directly from the relaxation trajectory without assuming a single exponential, it is used here as a model-free effective kinetic descriptor. It reflects conversion-associated relaxation kinetics but is not identified with one microscopic rate constant or with the forward conversion rate alone.

The first-cycle results reveal a clear mismatch between capacity and kinetic response. Over the common 200–800 mAh g⁻¹ interval, the median $t_{63}$ increases from 8.68 min for HEO to 11.57 min for BM-HEO even though ball milling markedly increases accessible capacity. The same tendency is present in the Mg-containing pair, with median $t_{63}$ values of 11.01 min for Mg-HEO and 12.99 min for BM-Mg-HEO. Thus, the capacity increase produced by ball milling is not accompanied by faster relaxation; the effective kinetic response instead becomes slower.

Mg incorporation provides a complementary constraint. The median $\Delta E_{\mathrm{relax}}$ decreases from 160.9 mV for HEO to 109.5 mV for Mg-HEO, yet $t_{63}$ does not shorten and instead changes from 8.68 to 11.01 min. A smaller relaxation magnitude therefore cannot be interpreted as faster kinetics. Mg strongly alters the magnitude of the nonequilibrium response without producing a proportional change in its effective relaxation timescale.

These observations do not imply that capacity and kinetics are unrelated. In a simple homogeneous system, faster reaction kinetics would generally reduce polarization, increase the reaction accessible before cutoff, and accelerate relaxation. The present data instead show that ball milling and Mg incorporation cannot be described as uniform acceleration or deceleration of a single conversion-rate coordinate. The key remaining question is whether the kinetic mismatch is specifically associated with conversion rather than with a generic transport or interfacial process. Figure 5 addresses this by comparing the GITT relaxation with the independent differential-capacity signature of conversion.

## 2.4. The capacity–kinetics mismatch is localized to the conversion region

The state-resolved GITT relaxation develops a distinct excess feature during the first lithiation (Figure 5a). The feature is strongest in HEO, becomes lower and broader after ball milling, and is strongly suppressed in the Mg-containing materials. To determine whether this kinetic response is associated with conversion rather than with generic cell relaxation, the background-subtracted GITT excess was compared with the independently derived first-cycle cathodic $dQ/dV$ response.

The two observables localize to nearly the same voltage region for all four materials (Figure 5b,c). The $dQ/dV$ maxima occur at approximately 0.545, 0.589, 0.419, and 0.485 V for HEO, BM-HEO, Mg-HEO, and BM-Mg-HEO, respectively, whereas the corresponding GITT excess maxima occur at 0.527, 0.618, 0.387, and 0.503 V. All four pairs lie within 32 mV. The excess relaxation can therefore be assigned conservatively as conversion-associated, although the present data do not identify a unique microscopic origin such as nucleation, phase-boundary motion, oxygen rearrangement, or metal/Li₂O formation.[5,7,20]

This localization makes the ball-milling result particularly significant. BM-HEO accesses more capacity than HEO, yet the conversion-associated relaxation is not accelerated. The excess feature is also lower and broader after milling, indicating that the conversion-associated nonequilibrium response is redistributed rather than simply amplified. These observations rule out a simple interpretation in which milling uniformly accelerates the conversion reaction.

Mg incorporation provides the complementary behavior. Mg-HEO has lower capacity and a strongly suppressed first-cycle conversion-associated excess, with the feature shifted to lower potential. This is consistent with reduced access to deep conversion and greater stabilization of oxide-derived states reported in related Mg-containing HEO systems.[8–10] However, the weak excess amplitude is not accompanied by a short $t_{63}$, again separating the magnitude of the conversion-associated response from its effective relaxation rate.

Across the four materials, Figure 5 therefore establishes that the capacity–kinetics mismatch is tied to the conversion region itself. The next question is whether this relationship is fixed by the pristine material or evolves as the conversion electrode changes with cycling.

## 2.5. Conversion-associated kinetics evolves with cycle history

The repeated lithiation/delithiation sequence in the GITT dataset allows the conversion-associated response to be tracked beyond the first cycle (Figure 6). The relaxation is not a stationary fingerprint of the pristine material. Instead, its magnitude and location evolve strongly as the cycled conversion state is established.

For lithiation over the common normalized reaction-state interval $z=0.4$–0.9, the conversion-associated excess peak changes markedly between cycles. HEO decreases from 71.2 mV in cycle 1 to 31.0 mV in cycle 3, and BM-HEO decreases from 44.8 to 22.4 mV. Mg-HEO shows the opposite evolution, increasing from 15.9 to 27.0 mV, whereas BM-Mg-HEO remains comparatively similar at 21.1 and 20.8 mV. At the same time, the peak position converges from the later first-cycle region, $z\approx0.66$–0.79, toward a common later-cycle region around $z\approx0.50$–0.56.

The effective relaxation timescale changes much less than the relaxation amplitude. From cycle 1 to cycle 3, the amplitude ratios $A_3/A_1$ span 0.435–1.698, whereas $t_{63,3}/t_{63,1}$ is confined to 0.845–0.923. Cycling therefore changes how strongly the conversion-associated response is excited much more than it changes the effective kinetic timescale. The first-cycle relaxation feature is consequently not a fixed material kinetic fingerprint.

Later-cycle capacity provides an additional constraint. Approximate third-cycle GITT lithiation capacities are 700, 833, 450, and 533 mAh g⁻¹ for HEO, BM-HEO, Mg-HEO, and BM-Mg-HEO, respectively, with similar corresponding delithiation capacities. Ball milling therefore continues to provide a larger accessible reversible reaction extent while retaining a longer $t_{63}$ than the corresponding unmilled material. Mg, in contrast, continues to suppress reversible capacity by approximately 35–36% in both unmilled and milled pairs even though later-cycle $t_{63}$ values approach those of the Mg-free analogues. The mismatch between accessible reaction extent and effective kinetic response is therefore not restricted to the irreversible first cycle.

The cycle-dependent excess is robust to the choice of later-cycle background: exponential and linear backgrounds give peak amplitudes differing by less than 0.012%, identical peak positions, and maximum background differences below 0.0016 mV for cycles 2–3. The detailed sensitivity analysis is provided in the Supporting Information.

Figures 3–6 thus impose three experimental constraints on any mechanistic explanation: capacity and relaxation kinetics do not vary monotonically together; the anomalous relaxation is localized to the conversion region; and the response evolves strongly with reaction history. Figure 7 asks whether a multistep conversion network can satisfy all three constraints without treating capacity and relaxation as independent phenomena.

## 2.6. Multistep conversion microkinetics explains the capacity–kinetics mismatch

A valid explanation must first preserve the ordinary kinetic expectation rather than assume that capacity and relaxation are unrelated. In a homogeneous version of the model, all kinetic rates were scaled together while the equilibrium parameters and voltage cutoff were held fixed (Figure 7c). Increasing the global rate scale from 0.5 to 2.0 increases the normalized cutoff capacity from 0.299 to 0.832 while shortening matched-state $t_{63}$ from 22.45 to 6.95 min. The model therefore reproduces the conventional coupling: uniformly faster kinetics gives both greater cutoff-limited capacity and faster relaxation.

Conversion, however, need not behave as one homogeneous reaction. Established conversion mechanisms contain coupled electrochemical and structural steps,[30,31] which are represented here by the coarse-grained sequence $O\rightleftharpoons I\rightleftharpoons I^*\rightleftharpoons C$ (Figure 7a). The labels denote effective oxide-derived, reduced/lithiated, structurally reconstructed, and more deeply converted states rather than uniquely assigned phases. During current flow, the state populations evolve under the coupled electrochemical and reconstruction rates. After current interruption, zero external current constrains the sum of the Faradaic partial currents but does not require every internal reaction rate to vanish.[32] The overall lithiation state can therefore remain conserved while internal populations continue to redistribute and the voltage relaxes (Figure 7b).

This multistate structure also permits the capacity and relaxation observables to respond differently to heterogeneity. As an illustrative existence proof, the reference calculation retains its original fast accessible population while an additional smaller population with a slower reconstruction step is made electrochemically accessible (Figure 7d). The normalized cutoff capacity then increases from 0.558 to 0.657 (+17.7%), while the matched-state $t_{63}$ increases from 13.45 to 15.28 min (+13.6%). Higher accessible capacity and slower relaxation can therefore coexist within the same kinetic network when a modification changes both the amount of material entering the conversion pathway and the distribution of internal kinetic timescales.

The heterogeneous calculation is not a fit to BM-HEO and does not establish that ball milling specifically creates a population with a ten-times-slower reconstruction step. Its role is narrower: it demonstrates that the experimentally observed direction of change is physically consistent with multistep conversion kinetics and cannot be reduced to a uniform increase or decrease in one rate constant. Ball milling is therefore interpreted experimentally as an accessibility-enhancing perturbation whose higher capacity does not imply uniform kinetic acceleration. Mg incorporation acts differently, suppressing accessible conversion and strongly altering the first-cycle relaxation amplitude without proportionally shifting the later-cycle timescale.

The underlying principle is thus not that capacity and relaxation are independent. They are kinetically linked through the same conversion network but are not kinetically equivalent observables. The finite-current capacity reflects how much of the heterogeneous network can be traversed before cutoff, whereas the GITT relaxation probes how the populated nonequilibrium state redistributes after interruption. Conversion chemistry supplies the multistep kinetic structure, while the multication and structurally heterogeneous HEO system provides a materials platform in which the resulting mismatch becomes experimentally visible.

# 3. Conclusions

Ball milling and Mg incorporation reveal that accessible capacity and conversion-associated kinetics do not follow a single fast–slow trend in spinel HEO anodes. Ball milling increases surface area and accessible reaction, giving higher capacity in both Mg-free and Mg-containing materials, yet the GITT relaxation becomes slower rather than faster. Mg incorporation suppresses accessible conversion and strongly reduces the first-cycle conversion-associated relaxation amplitude without a proportional change in the effective kinetic timescale.

Differential-capacity analysis localizes the anomalous GITT response to the conversion region, while cycle-resolved measurements show that its amplitude and position evolve much more strongly than its characteristic relaxation time. The capacity–kinetics mismatch is therefore a history-dependent feature of the conversion process rather than a generic first-cycle polarization effect.

A literature-informed microkinetic model clarifies the origin of this behavior. The model first recovers the conventional homogeneous limit in which faster kinetics increases cutoff-limited capacity and accelerates relaxation. It then shows that a heterogeneous multistep conversion network can produce higher accessible capacity together with slower relaxation when reaction accessibility and internal kinetic timescales are modified simultaneously. Capacity and relaxation are therefore kinetically linked but not kinetically equivalent. For conversion electrodes, improved capacity should not automatically be interpreted as uniform kinetic acceleration; both the accessible reaction population and the internal relaxation of the converted state must be considered.

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



## 4.4. Literature-informed coarse-grained conversion microkinetic model

A minimal conversion microkinetic model was used to test whether the experimentally observed capacity–kinetics mismatch is physically consistent with established conversion-reaction motifs. The model is not fitted to obtain unique microscopic rate constants and is not used to assign a unique elementary rate-limiting step.

The effective reaction network is

\[
O+\nu_1\mathrm{Li}^{+}+\nu_1e^{-}\rightleftharpoons I,
\]

\[
I\rightleftharpoons I^*,
\]

and

\[
I^*+\nu_3\mathrm{Li}^{+}+\nu_3e^{-}\rightleftharpoons C.
\]

Here, \(O\), \(I\), \(I^*\), and \(C\) denote an oxide-derived state, a reduced/lithiated oxide intermediate, a structurally reconstructed conversion-active intermediate, and a metal/Li₂O-containing converted state, respectively. The network is a coarse-grained representation motivated by established multistep conversion mechanisms and does not assign these states to unique experimentally identified phases.[30,31]

The first and third reactions are represented by reversible Butler–Volmer-type rates. For the illustrative calculation, symmetric transfer coefficients were used,

\[
r_1=k_1\left[a_O\exp(u/2)-\frac{a_I}{K_1}\exp(-u/2)\right],
\]

\[
r_3=k_3\left[a_{I^*}\exp((u-u_3)/2)-\frac{a_C}{K_3}\exp(-(u-u_3)/2)\right],
\]

where \(u\) is the dimensionless electrochemical driving force and \(u_3\) is the relative driving-force offset of the second Faradaic step. The structural/reconstruction step is represented as

\[
r_2=k_{2,f}a_I-k_{2,r}a_{I^*}.
\]

The state balances are

\[
\frac{dx_I}{dt}=r_1-r_2,
\]

\[
\frac{dx_{I^*}}{dt}=r_2-r_3,
\]

\[
\frac{dx_C}{dt}=r_3,
\]

with \(x_O=1-x_I-x_{I^*}-x_C\).

During a galvanostatic pulse, the potential is obtained from the Faradaic current balance

\[
j_{\mathrm{ext}}=F(\nu_1r_1+\nu_3r_3).
\]

After current interruption,

\[
j_{\mathrm{ext}}=F(\nu_1r_1+\nu_3r_3)=0.
\]

This zero-net-current condition does not require the individual partial currents to vanish.[32] In the normalized illustrative calculation, \(\nu_1=\nu_3=1\), so finite opposing rates \(r_1=-r_3\neq0\) are allowed while \(r_2\) can also continue to redistribute the internal conversion state.

The coupled state equations were integrated for a 600 s pulse followed by a 3600 s rest, matching the experimental GITT timing. The representative parameter set gives approximately 24.0 mV residual relaxation at the 3 s reference and \(t_{63}\approx13.8\) min. These values were selected only to place the illustrative calculation in the experimental timescale and amplitude range; they are not a fit to HEO, BM-HEO, Mg-HEO, or BM-Mg-HEO.

Local linearization of the open-circuit dynamics gives

\[
\frac{d\,\delta\mathbf{x}}{dt}=\mathbf{J}\delta\mathbf{x},
\]

with a corresponding voltage response

\[
E(t)-E_{\mathrm{eq}}=\sum_i B_i\exp(-t/\tau_i).
\]

The representative parameter set yields two finite model relaxation modes near 0.50 and 14.3 min and a conserved-state mode associated with fixed overall state of charge at open circuit. The amplitudes \(B_i\) and timescales \(\tau_i\) are model-level state-excitation/voltage-sensitivity weights and kinetic eigen-timescales, respectively; they are not interpreted as directly measured microscopic modes.

A pulse-current sweep was retained as a diagnostic rather than as a fitted experimental result. Increasing the relative pulse current from 0.25 to 4 increases the illustrative 3 s relaxation magnitude from approximately 11.9 to 45.8 mV, while \(t_{63}\) remains within approximately 13.8–14.1 min. This synthetic result demonstrates, within the same reaction network and rate constants, that state excitation amplitude can vary strongly without a proportional change in the dominant relaxation timescale.

A separate cutoff-capacity test was used to preserve the expected coupling between capacity and kinetics. In a homogeneous population, scaling all rates together from 0.5 to 2.0 increases normalized cutoff capacity from 0.299 to 0.832 while shortening matched-state \(t_{63}\) from 22.45 to 6.95 min. An illustrative heterogeneous extension then retains the same fast population while adding a smaller accessible population with a ten-times-slower structural/reconstruction step; this increases cutoff capacity from 0.558 to 0.657 and increases matched-state \(t_{63}\) from 13.45 to 15.28 min. The latter calculation is used only as a mechanistic-consistency existence proof and is not fitted to the ball-milled sample. The homogeneous and heterogeneous tests are therefore used to distinguish a global kinetic-speed change from a change in accessible population and internal kinetic-timescale distribution.

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

31. Ng, B.; Faegh, E.; Lateef, S.; Karakalos, S. G.; Mustain, W. E. Structure and chemistry of the solid electrolyte interphase (SEI) on a high capacity conversion-based anode: NiO. **Journal of Materials Chemistry A** 2021, 9, 523. DOI: 10.1039/D0TA09683K.

32. Parsons, R. Electrochemical nomenclature. **Pure and Applied Chemistry** 1974, 37, 499–516. DOI: 10.1351/pac197437040499.

# Figure Captions

**Figure 1. Mg incorporation and ball milling alter crystal structure, composition, and nanoscale microstructure of spinel HEOs.** The four materials are compared using the final XRD, ICP-OES, HRTEM/SAED, and elemental-mapping dataset. The figure establishes the parent spinel-type structure, the comparatively modest lattice/compositional perturbation associated with Mg incorporation, and milling-induced changes in coherent-domain/microstructural characteristics. No unique Mg site is assigned without final refinement, and the chemically incompatible preliminary CoGa₂O₄ indexing is excluded. **[[YOO GROUP INPUT REQUIRED — freeze final refined XRD/HRTEM/SAED/ICP dataset and panel order.]]**

**Figure 2. Ball milling primarily modifies particle morphology and physical surface characteristics.** SEM morphology, particle/domain-size statistics, and BET surface area are used to compare HEO, BM-HEO, Mg-HEO, and BM-Mg-HEO before cycling. XPS is included only if the final dataset is reproducible and mechanistically defensible. Electrochemically derived interface metrics are intentionally excluded from this characterization figure and are introduced in Figure 3. **[[YOO GROUP INPUT REQUIRED — freeze final SEM/particle-size/BET package and final XPS inclusion decision.]]**

**Figure 3. Ball milling increases accessible capacity whereas Mg incorporation suppresses it.** (a) First-cycle voltage profiles of HEO, BM-HEO, Mg-HEO, and BM-Mg-HEO, with first-cycle capacities and initial Coulombic efficiencies. (b) Specific capacity during 0.1 C cycling under the common electrolyte condition. (c) Absolute rate capability over the 0.1–5 C sequence and recovery at 0.1 C. (d) Cycle-resolved differential-capacity response. Figure 3 establishes the accessible reaction extent without assigning a kinetic rate from capacity alone.

**Figure 4. Higher accessible capacity does not imply faster conversion-associated kinetics.** (a) Representative 10 min GITT pulse followed by a 60 min open-circuit rest, defining the 3 s-to-60 min relaxation magnitude, $\Delta E_{\mathrm{relax}}$, and model-free effective kinetic timescale, $t_{63}$. (b) State-resolved $\Delta E_{\mathrm{relax}}$. (c) Corresponding $t_{63}$ values. (d) Median $\Delta E_{\mathrm{relax}}$ versus median $t_{63}$ over the common 200–800 mAh g⁻¹ interval. Ball milling increases capacity while lengthening the effective relaxation, whereas Mg lowers the relaxation magnitude without a proportional shortening of $t_{63}$.

**Figure 5. The capacity–kinetics mismatch is localized to the conversion region.** (a) State-resolved first-cycle relaxation showing the conversion-associated excess feature. (b) Background-subtracted GITT excess relaxation on a voltage axis together with the first-cycle cathodic $dQ/dV$ response. (c) Comparison of $dQ/dV$ and GITT excess-peak voltages; all pairs lie within 32 mV. (d) Peak amplitude versus FWHM-like width of the excess response. The conversion localization establishes that the anomalous kinetic response is tied to conversion rather than to a generic cell-relaxation background.

**Figure 6. Conversion-associated kinetics evolves with cycle history.** (a) Background-subtracted conversion-associated relaxation profiles for cycles 1–3 over the common normalized lithiation coordinate, $z=0.4$–0.9. (b) Conversion-associated peak amplitude versus cycle. (c) Median ensemble/state-resolved $t_{63}$ versus cycle over the same interval. (d) Normalized change map of $A_3/A_1$ versus $t_{63,3}/t_{63,1}$ with unity reference lines. The amplitude ratio spans 0.435–1.698 while the timescale ratio remains within 0.845–0.923, showing that reaction history alters the conversion-associated response much more strongly than its effective timescale.

**Figure 7. Multistep conversion microkinetics explains the capacity–kinetics mismatch.** (a) Literature-informed coarse-grained conversion network, $O\rightleftharpoons I\rightleftharpoons I^*\rightleftharpoons C$, containing two reversible Faradaic steps separated by a structural reconstruction/conversion-activation step. (b) Current-on and current-off balances showing that zero external current can coexist with finite internal redistribution at conserved overall lithiation. (c) Homogeneous kinetic-speed control: scaling all rates together increases cutoff-limited capacity and shortens matched-state $t_{63}$. (d) Heterogeneous-accessibility existence proof: retaining the original fast population while adding an accessible slower-reconstructing population produces both higher cutoff capacity and longer matched-state $t_{63}$. The model demonstrates that capacity and relaxation are kinetically linked but not kinetically equivalent without assigning a unique microscopic mechanism to ball milling.
