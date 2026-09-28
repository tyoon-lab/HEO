# HEO Manuscript v15 — AFM-Target Capacity–Kinetics / GITT Relaxation Draft

**Date:** 2026-09-28  
**Status:** PI line-by-line review integrated through Section 2.5 and Conclusions; cycle-resolved history analysis moved to Supporting Information; homogeneous four-step microkinetic analysis replaces the earlier heterogeneous-accessibility model
**Scientific backbone:** Figures 1–2 materials modifications → Figure 3 accessible capacity → Figure 4 capacity–relaxation mismatch + conventional-GITT conflict → Figure 5 conversion localization → Figure 6 homogeneous four-step microkinetic feasibility; cycle-resolved robustness is retained in the Supporting Information
**Literature basis:** `HEO_REFERENCE_MASTER_VERIFIED_2026-09-18.md` + `HEO_REFERENCE_CANDIDATES_MICROKINETICS_2026-09-28.md` + `references/HEO_CONVERSION_GITT_LITERATURE_AUDIT_2026-09-26.md`

> Verified information is written directly. Missing experimental metadata are not inferred. Inputs expected from the Yoo group and Yoon Lab remain explicitly marked. The Figure 5 differential-capacity peak positions currently come from reconstruction of the latest vector voltage profiles; the underlying numerical first-cycle files should replace this source if recovered before submission.

---

# Working title

**Mismatch between Capacity and Conversion Kinetics in Spinel High-Entropy Oxide Anodes**

Alternative:

**Capacity–Kinetics Mismatch in Multistep Conversion of Spinel High-Entropy Oxide Anodes**

---


# Abstract

Faster conversion kinetics are generally expected to raise accessible capacity in conversion-type anodes. However, conversion couples electron transfer, structural reconstruction, nucleation/phase growth, and cation/oxygen redistribution, complicating the link between capacity and overall kinetics. This relationship is examined in spinel high-entropy oxide (HEO) anodes modified by ball milling or Mg incorporation. Galvanostatic intermittent titration (GITT) is used to characterize current-off relaxation in terms of the voltage relaxation magnitude and a characteristic relaxation time, $t_{63}$. Ball-milled HEO (BM-HEO) exhibits higher accessible conversion capacity but slower relaxation, contrary to the conventional expectation. Mg-containing HEO (Mg-HEO) shows lower accessible capacity and slower relaxation, as expected, while its voltage relaxation magnitude also decreases. Conventional GITT-derived apparent diffusivity, widely used to compare Li-ion transport kinetics, fails to preserve the observed kinetic ordering: $D_{\mathrm{app}}$ ranks BM-HEO faster even though its relaxation is slower. Microkinetic analysis recovers the conventional capacity–rate coupling under uniform kinetic acceleration but shows that step-selective changes within a homogeneous four-step conversion network can produce higher accessible capacity with slower relaxation. These results distinguish reaction accessibility from kinetic speed and show that neither capacity gains nor apparent diffusivity alone establishes improved overall conversion kinetics, providing a basis for evaluating materials modifications in multistep conversion systems.

**Keywords:** high-entropy oxide; conversion anode; GITT; apparent diffusion coefficient; voltage relaxation; ball milling; Mg incorporation; microkinetics

# 1. Introduction

Conversion-type anodes can achieve high theoretical capacities by accommodating multiple Li ions and electrons through conversion reactions. This high capacity, however, comes with extensive structural and chemical reconstruction during conversion, involving bond rearrangement, nucleation and growth of new phases, and redistribution of cations and oxygen. These coupled processes can introduce substantial kinetic limitations, leading to polarization, incomplete reaction, and rate-dependent capacity. Understanding how material modifications affect these kinetics is therefore important for interpreting their influence on electrochemical performance.

The galvanostatic intermittent titration technique (GITT) is widely used to estimate apparent Li-ion diffusion coefficients, $D_{\mathrm{app}}$, from the voltage response to a current pulse and subsequent relaxation. These $D_{\mathrm{app}}$ values are often compared across compositions, structures, and processing conditions as kinetic descriptors, including for conversion-type electrodes and high-entropy oxides (HEOs).[6,33–36] However, the interpretation of $D_{\mathrm{app}}$ is most straightforward when the transient response is governed predominantly by solid-state diffusion. For reconstructive conversion reactions, the resulting $D_{\mathrm{app}}$ may therefore not track the directly observed relaxation rate.

The GITT relaxation can also be examined directly without converting the measured voltage response into a diffusion coefficient. Two readily accessible quantities are the magnitude of the voltage relaxation, $\Delta E_{\mathrm{relax}}$, and a characteristic relaxation time, which quantify the extent and timescale of the current-off voltage response, respectively. Such quantities do not require specification of a solid-state diffusion model and can therefore provide complementary information when the origin of the transient is not purely diffusional. Accessible capacity provides a separate measure of how much conversion is reached under load. Comparing accessible capacity with these direct relaxation descriptors therefore provides a simple test of whether a modification that increases the accessible extent of conversion also produces faster relaxation kinetics.

Spinel HEOs provide a useful material system for examining this relationship. Spinel (FeCoNiCrMn)₃O₄ is a conversion-type anode in which multiple redox-active cations share a common oxide structure.[1–4,6] Its lithiation involves substantial reconstruction, including progressive formation of metallic species, Li₂O, and rock-salt-like phases accompanied by cation and oxygen rearrangement.[5,7,20] Ball milling and Mg incorporation provide complementary modifications of this conversion behavior. Milling increases surface area and has been associated with enhanced conversion reversibility,[6,12] whereas Mg-containing HEOs have been reported to exhibit greater structural retention but lower accessible capacity.[8–10] Because these modifications change accessible conversion in opposite directions, they provide a useful basis for testing whether capacity changes are accompanied by corresponding changes in relaxation kinetics.

Here, pristine HEO, ball-milled HEO (BM-HEO), Mg-containing HEO (Mg-HEO), and BM-Mg-HEO are compared to determine the relationships among accessible conversion capacity, GITT relaxation, and conventional GITT-derived apparent diffusivity. The apparent diffusivity is compared with the directly measured relaxation to determine whether the two indicate the same kinetic trend. Differential-capacity analysis identifies where the capacity–relaxation mismatch emerges during lithiation, cycle-resolved GITT examines whether it persists with reaction history, and a multistep microkinetic model tests whether the observed behavior can arise from a heterogeneous conversion network.

# 2. Results and Discussion

## 2.1. Structural and morphological characteristics of the HEO series

Figures 1 and 2 are reserved for the structural, compositional, and morphological characterization of HEO, BM-HEO, Mg-HEO, and BM-Mg-HEO. The current working dataset indicates that all four materials retain a predominantly spinel-type HEO structure, while Mg incorporation and ball milling introduce distinct compositional, lattice, particle, and surface-level changes. Ball milling also produces a marked increase in BET surface area. These characterization results will be finalized using the collaborator-verified XRD/refinement, ICP-OES, TEM/SAED/EDS, SEM, BET, and, if retained, XPS datasets.

At this stage, Figures 1–2 are used only to establish that Mg incorporation and ball milling produce distinguishable materials-level perturbations before electrochemical testing. Detailed phase assignments, Mg-site interpretation, quantitative lattice changes, and XPS-based mechanistic claims are intentionally deferred until the final characterization package is frozen.

**[[YOO GROUP INPUT REQUIRED — finalize Figure 1–2 panel composition and the corresponding structural interpretation using the verified XRD/ICP/TEM/SAED/EDS/SEM/BET dataset; decide separately whether XPS remains in the Supporting Information or is promoted to a main characterization figure.]]**



## 2.2. Ball milling increases accessible capacity whereas Mg incorporation decreases it

Figure 3 first compares the accessible capacities of the four materials. The first-cycle lithiation/delithiation capacities are 901.25/609.12 mAh g⁻¹ for pristine HEO, 1056.10/782.08 mAh g⁻¹ for BM-HEO, 731.15/458.91 mAh g⁻¹ for Mg-HEO, and 944.07/580.83 mAh g⁻¹ for BM-Mg-HEO, corresponding to initial Coulombic efficiencies of 67.59%, 74.05%, 62.77%, and 61.52%, respectively. Ball milling therefore increases accessible capacity in both the Mg-free and Mg-containing materials, whereas Mg incorporation decreases the capacity relative to the corresponding Mg-free composition.

The milling effect is accompanied by a marked increase in surface area and reduced particle/domain dimensions, which can increase the fraction of material and interfaces participating electrochemically. Previous work on the same five-cation spinel family likewise showed that particle fragmentation can increase conversion reversibility and interfacial storage.[12] The capacity increase after milling is therefore consistent with improved reaction accessibility.

Mg incorporation produces the opposite capacity trend. Mg-containing electrodes exhibit lower absolute capacity, and the lower reversible reaction extent persists beyond the first cycle. This behavior is consistent with previous HEO studies in which electrochemically inactive or weakly active cations stabilize oxide-derived states and reduce the fraction of material undergoing deep conversion.[8–10] Milling recovers part of the lost utilization in BM-Mg-HEO, but its capacity remains below that of BM-HEO.

The rate-capability data show that these capacity differences persist across the measured current range. BM-HEO remains above pristine HEO in absolute capacity throughout the rate sequence, including approximately 193 versus 79 mAh g⁻¹ at 5 C. Mg-HEO reaches approximately 185 mAh g⁻¹ at 5 C despite its lower low-rate capacity. Figure 3 therefore establishes the differences in accessible reaction extent that are subsequently compared with the GITT relaxation response.

These contrasting capacity changes provide two complementary comparisons in Figure 4. Ball milling tests whether an increase in accessible conversion is accompanied by faster relaxation, whereas Mg incorporation provides the corresponding lower-accessibility case. The GITT relaxation is then compared with conventional apparent diffusivity to determine whether the different measures give a consistent kinetic interpretation.

## 2.3. Ball milling reveals a capacity–kinetics mismatch and a conflicting apparent-diffusivity trend

GITT was used to compare the relaxation dynamics of the four materials (Figure 4a). Each step consists of a 10 min galvanostatic pulse followed by a 60 min open-circuit rest. The relaxation magnitude, $\Delta E_{\mathrm{relax}}$, is defined from 3 s after current interruption to the end of the 60 min rest, and $t_{63}$ is the time required to complete 63.2% of this observed relaxation. Because $t_{63}$ is extracted directly from the relaxation trajectory without assuming a single exponential, it is used as a model-free effective relaxation timescale. It describes the effective current-off response but is not identified with one microscopic rate constant or with the forward conversion rate alone.

Ball milling provides the primary contradiction to the conventional capacity–kinetics expectation. Over the common 200–800 mAh g⁻¹ interval, the median $t_{63}$ increases from 8.68 min for HEO to 11.57 min for BM-HEO even though ball milling increases the first-cycle accessible capacity. Higher accessible capacity therefore coexists with slower effective relaxation after milling (Figure 4d).

A conventional GITT diffusivity analysis of the compositionally identical HEO/BM-HEO pair gives the opposite kinetic indication (Figure 4b). Across 37 state-matched points spanning 200–800 mAh g⁻¹, $D_{\mathrm{app,BM}}/D_{\mathrm{app,HEO}}$ remains above unity at every point and has a median value of 1.78. In contrast, the direct relaxation-rate ratio, $t_{63,\mathrm{HEO}}/t_{63,\mathrm{BM}}$, has a median value of 0.762 and lies below unity at 35 of 37 points. Conventional $D_{\mathrm{app}}$ therefore indicates faster kinetics for BM-HEO over the same state range in which the directly measured relaxation is predominantly slower.

This inversion is consequential because larger GITT-derived diffusion coefficients are commonly used to support faster-kinetics interpretations in HEO and other conversion-anode studies.[6,33–36] If only capacity and conventional $D_{\mathrm{app}}$ were considered here, ball milling would naturally be interpreted as accelerating the electrode kinetics. The direct relaxation gives the opposite ordering. The discrepancy is therefore not limited to uncertainty in the numerical value of $D$; apparent diffusivity does not preserve the fast–slow ordering of the measured current-off response.

Mg incorporation provides a complementary constraint rather than a second capacity–rate contradiction. Accessible capacity decreases and the median $t_{63}$ increases from 8.68 to 11.01 min, a combination consistent with slower relaxation. Yet the median $\Delta E_{\mathrm{relax}}$ simultaneously decreases from 160.9 to 109.5 mV (Figure 4c). Thus, the magnitude of the nonequilibrium voltage response becomes smaller even as relaxation becomes slower. Capacity, response magnitude, and relaxation timescale do not collapse onto one scalar kinetic coordinate across the four materials.

These results do not show that Li transport is absent or that GITT-derived $D_{\mathrm{app}}$ lacks operational value. They show that apparent diffusivity cannot be assumed to represent the overall rate of a reconstructive conversion response. The voltage terms entering the conventional GITT expression change unequally after milling, and the full-pulse square-root-time audit in the Supporting Information provides an additional test of the single-diffusion approximation. Figure 5 next determines whether the anomalous relaxation is specifically associated with conversion rather than with a generic cell-relaxation process.

## 2.4. The excess current-off relaxation is localized to the conversion region

The state-resolved GITT relaxation develops a distinct excess feature during the first lithiation (Figure 5a). The feature is strongest in HEO, becomes lower and broader after ball milling, and is strongly suppressed in the Mg-containing materials. To determine whether this current-off response is associated with conversion rather than with a generic relaxation background, the background-subtracted GITT excess was compared with the independently derived first-cycle cathodic $dQ/dV$ response.

For voltage localization, each GITT excess value was assigned the 60 min rest-end voltage of the same state, providing a quasi-relaxed state coordinate without using the pulse polarization itself. Under the nominal background definition, the $dQ/dV$ maxima occur at approximately 0.545, 0.589, 0.419, and 0.485 V for HEO, BM-HEO, Mg-HEO, and BM-Mg-HEO, respectively, whereas the corresponding GITT excess maxima occur at 0.527, 0.618, 0.387, and 0.503 V; the four nominal pairs differ by no more than 32 mV (Figure 5b,c). Background/window variation leaves the HEO and Mg-HEO peak states unchanged and confines BM-HEO to a narrow higher-potential range, whereas the shallow BM-Mg-HEO feature has a broader peak-position sensitivity. Importantly, the direction of all three material-induced shifts—higher after HEO to BM-HEO, lower after HEO to Mg-HEO, and higher after Mg-HEO to BM-Mg-HEO—is preserved across the tested definitions and matches the corresponding $dQ/dV$ shifts. The excess relaxation can therefore be assigned conservatively as conversion-associated, although the present data do not identify a unique microscopic origin such as nucleation, phase-boundary motion, oxygen rearrangement, or metal/Li$_2$O formation.[5,7,20]

The main role of Figure 5 is intentionally limited to this localization. The nominal excess peak is lower and broader in BM-HEO than in HEO, and the Mg-containing responses are strongly suppressed, but the amplitude and width of the excess are not treated as direct kinetic rates. A 105-condition background/window sensitivity audit preserves the BM-HEO peak-down/width-up trend and the suppression of both Mg-containing peaks relative to HEO; the detailed amplitude-width map and sensitivity ranges are therefore retained in the Supporting Information rather than used as an additional main-text mechanistic coordinate. The shallow BM-Mg-HEO feature, in particular, gives a background-sensitive width and is not used as a quantitative discriminator.

Figure 5 therefore establishes the specific point required for the kinetic argument: the excess current-off response used to interpret the GITT behavior occurs in the same electrochemical region as first-cycle conversion. This supports the term **conversion-associated relaxation** without equating its magnitude, width, or $t_{63}$ with a unique microscopic rate constant. The next question is whether the capacity-relaxation relation is confined to the first conversion or persists as the electrode evolves with cycling.


## 2.5. Conversion-associated relaxation evolves with cycle history

Cycle-resolved GITT shows that the conversion-associated relaxation is not a stationary fingerprint of the pristine material (Figure 6). Over the common lithiation interval $z=0.4$–0.9, the excess peak decreases strongly from cycle 1 to cycle 3 for HEO and BM-HEO, increases for Mg-HEO, and changes little for BM-Mg-HEO. The peak position simultaneously converges from the later first-cycle region ($z\approx0.66$–0.79) toward a common later-cycle region near $z\approx0.50$–0.56.

The amplitude evolves much more strongly than the effective timescale: $A_3/A_1$ spans 0.435–1.698, whereas $t_{63,3}/t_{63,1}$ remains within 0.845–0.923. Thus, cycling strongly changes the magnitude and state location of the conversion-associated response while only modestly changing its effective relaxation time. The first-cycle feature is therefore not a fixed material relaxation fingerprint.

The capacity–relaxation mismatch also persists after the first cycle. Third-cycle GITT lithiation capacities are approximately 700, 833, 450, and 533 mAh g⁻¹ for HEO, BM-HEO, Mg-HEO, and BM-Mg-HEO, respectively. Ball milling retains a larger reversible capacity together with a longer $t_{63}$, whereas Mg suppresses reversible capacity by approximately 35–36% even as later-cycle $t_{63}$ approaches Mg-free values. The result is therefore not explained by first-cycle irreversibility alone. Later-cycle background sensitivity is negligible and is documented in the Supporting Information.

Figures 3–6 therefore impose three constraints on any explanation: higher accessible capacity can coexist with slower relaxation, the mismatch is localized to conversion, and the conversion-associated response evolves with reaction history. Figure 7 asks whether these observations can arise within a multistep conversion network without treating capacity and relaxation as independent phenomena.

## 2.6. Microkinetic analysis shows how the mismatch can arise from multistep conversion

The microkinetic analysis first reproduces the conventional kinetic limit. When all rates in a homogeneous population are varied together (Figure 7c), the normalized cutoff capacity increases from 0.299 to 0.832 as the global rate factor rises from 0.5 to 2.0, while matched-state $t_{63}$ decreases from 22.45 to 6.95 min. Uniformly faster kinetics therefore gives both greater cutoff-limited capacity and faster relaxation. The experimental ball-milling trend is not obtained by a simple global acceleration.

Conversion, however, contains coupled electrochemical and structural steps.[30,31] The coarse-grained sequence $O\rightleftharpoons I\rightleftharpoons I^*\rightleftharpoons C$ (Figure 7a) represents effective kinetic states rather than uniquely assigned phases. After current interruption, zero external current constrains the sum of the Faradaic partial currents but does not require every internal rate to vanish.[32] Overall lithiation can therefore remain conserved while internal populations continue to redistribute and the voltage relaxes (Figure 7b).

An illustrative heterogeneous calculation then changes reaction accessibility together with one internal timescale. The reference accessible model branch is retained while an additional branch with a slower reconstruction step becomes electrochemically accessible (Figure 7d). The cutoff capacity increases from 0.558 to 0.657 (+17.7%), while matched-state $t_{63}$ increases from 13.45 to 15.28 min (+13.6%). Higher accessible capacity and slower relaxation can therefore coexist within the same multistep kinetic network. The branch weights and rate contrast are illustrative model parameters rather than measured material fractions or fitted microscopic rates.

A secondary directional test reported in the Supporting Information addresses the Mg combination. Within the same coarse-grained network, a perturbation that suppresses deeper conversion while lengthening an internal reconstruction timescale produces lower cutoff capacity, lower relaxation amplitude, and longer $t_{63}$ simultaneously. This calculation is also an existence proof and is not used to map Mg incorporation onto specific model parameters.

Microkinetic analysis thus shows that the experimental behavior can arise naturally from the multistep character of conversion. The calculation is an existence proof, not a fit to BM-HEO, and it does not identify the microscopic step altered by milling or assign the illustrative population weights to measured phase fractions. Its role is narrower: it demonstrates that reaction accessibility and internal relaxation timescales need not change in parallel even though both remain kinetically coupled to the same conversion network.

This distinction also clarifies the conventional-GITT result. The model does not calculate $D_{\mathrm{app}}$ and therefore does not explain the numerical value of the apparent diffusion coefficient. Instead, it shows why a composite conversion response need not be representable by one fast–slow kinetic coordinate. The experimentally observed inversion between $D_{\mathrm{app}}$ and direct relaxation is consistent with that multistep picture. Capacity, apparent diffusivity, and relaxation are therefore related to the same conversion process but are not kinetically equivalent observables.

# 3. Conclusions

Ball milling reveals that higher accessible capacity can coexist with slower conversion-associated kinetics in spinel HEO conversion anodes. Over the common first-lithiation interval, BM-HEO accesses more capacity than HEO while its effective current-off relaxation is slower. Mg incorporation provides a complementary constraint: accessible conversion decreases and relaxation remains slower, while the relaxation voltage change is also reduced. Differential-capacity analysis localizes the anomalous relaxation to the conversion region, and cycle-resolved GITT shows that the capacity–relaxation mismatch is not explained by first-cycle irreversibility alone.

Conventional GITT analysis gives a conflicting kinetic indication for the compositionally identical HEO/BM-HEO pair. $D_{\mathrm{app}}$ is higher for BM-HEO at all 37 state-matched points between 200 and 800 mAh g⁻¹, whereas the direct current-off relaxation is slower at 35 of 37 points. A larger apparent GITT diffusion coefficient therefore does not necessarily indicate faster overall conversion kinetics. The result does not exclude Li transport; it shows that apparent diffusivity can combine transport, thermodynamic, and transformation contributions without preserving the fast–slow ordering of the full conversion-associated response.

Microkinetic analysis shows that this behavior can arise naturally from the multistep character of conversion. A homogeneous acceleration produces the conventional combination of higher cutoff capacity and faster relaxation, whereas a multistep network can produce higher accessible capacity together with slower relaxation when reaction accessibility and internal timescales change together. Overall conversion kinetics therefore cannot, in general, be inferred from apparent GITT diffusivity alone. Apparent $D$ can remain useful as an operational transport descriptor, but independent kinetic information is required before it is interpreted as the overall rate of a reconstructive conversion reaction.

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

The late-stage excess response was obtained by subtracting a smooth sample-specific background from the state-resolved $\Delta E_{\mathrm{relax}}$ response. For voltage-localization analysis, each GITT state was assigned its 60 min rest-end voltage; this rest-end value is used as a quasi-relaxed state coordinate and is not identified with an exact equilibrium potential. Peak position, peak amplitude, and FWHM-like width were used as comparative descriptors. Detailed background definitions, peak-position/window sensitivity, short-time current-off analysis, and additional relaxation descriptors are provided in the Supporting Information.

To audit the conventional diffusivity interpretation, a state-matched relative $D_{\mathrm{GITT,app}}$ comparison was performed for the compositionally identical HEO/BM-HEO pair over 200–800 mAh g⁻¹. The conventional finite-pulse form $D\propto (m_B/S)^2(\Delta E_s/\Delta E_\tau)^2/\tau$ was used only for relative ranking. $\Delta E_s$ was the relaxed voltage increment between consecutive rest endpoints, and $\Delta E_\tau$ was the voltage excursion from 3 s after pulse onset to the pulse end. The same 3 s reference suppresses the unresolved initial fast/ohmic contribution. The current relative comparison uses the same geometric electrode area for HEO and BM-HEO, consistent with the common electrode geometry used in these experiments. Absolute $D$ values are not used because the final active-mass and molar-volume metadata are not yet frozen; the full relative-analysis definition and sensitivity audit are given in the Supporting Information.

First-cycle differential-capacity curves were obtained from the corresponding galvanostatic voltage profiles using the same differentiation and smoothing procedure for all four materials. The current manuscript-development curves were reconstructed from the latest vector voltage profiles because the original numerical first-cycle source files have not yet been recovered; this source should be replaced by the original numerical data before submission if available.



## 4.4. Literature-informed coarse-grained conversion microkinetic model

A minimal coarse-grained model was used to test whether the capacity–kinetics mismatch is consistent with established multistep conversion motifs rather than to fit unique microscopic rate constants or identify a single rate-limiting step.[30,31] The effective network is

\[
O+\nu_1\mathrm{Li}^{+}+\nu_1e^{-}\rightleftharpoons I,
\]

\[
I\rightleftharpoons I^*,
\]

\[
I^*+\nu_3\mathrm{Li}^{+}+\nu_3e^{-}\rightleftharpoons C,
\]

where \(O\), \(I\), \(I^*\), and \(C\) are effective oxide-derived, reduced/lithiated, structurally reconstructed, and more deeply converted states. \(R_1\) and \(R_3\) were represented by reversible Butler–Volmer-type kinetics with symmetric transfer coefficients, and the reconstruction step by

\[
r_2=k_{2,f}a_I-k_{2,r}a_{I^*}.
\]

The state balances are

\[
\frac{dx_I}{dt}=r_1-r_2,\qquad
\frac{dx_{I^*}}{dt}=r_2-r_3,\qquad
\frac{dx_C}{dt}=r_3,
\]

with \(x_O=1-x_I-x_{I^*}-x_C\). The external Faradaic current is

\[
j_{\mathrm{ext}}=F(\nu_1r_1+\nu_3r_3).
\]

Thus, after current interruption, \(j_{\mathrm{ext}}=0\) constrains the sum of the Faradaic partial currents but does not require each internal rate to vanish.[32] For the normalized illustrative case \(\nu_1=\nu_3=1\), finite opposing rates \(r_1=-r_3\) are allowed while \(r_2\) can continue to redistribute the internal state.

The reference current-off calculation and pulse-current sweep used the experimental 600 s pulse/3600 s rest timing. For the capacity–relaxation tests, cutoff capacity was obtained from constant-current integration to a fixed model voltage cutoff, whereas matched-state $t_{63}$ was evaluated after an identical three-pulse sequence so that the externally passed charge was common across the compared cases. The separate Mg-like Supporting Information test used a common initial state and a matched normalized passed charge of $\Delta Q=0.30$. The model response was also linearized locally as

\[
\frac{d\,\delta\mathbf{x}}{dt}=\mathbf{J}\delta\mathbf{x},
\qquad
E(t)-E_{\mathrm{eq}}=\sum_i B_i\exp(-t/\tau_i),
\]

to distinguish state-dependent response amplitudes from kinetic eigen-timescales. Two illustrative tests were then performed: (i) a homogeneous global-rate scaling at fixed equilibrium parameters and voltage cutoff, and (ii) a heterogeneous-accessibility test in which the reference accessible model branch was retained and an additional slower-reconstructing branch was made accessible. Both tests are mechanistic-consistency calculations rather than fits to an individual HEO sample; the parameter set and numerical diagnostics are provided in the Supporting Information.

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


30. Alsaç, E. P.; Sharma, A. K.; Yoon, S. G.; Vishnugopi, B. S.; Wang, C.; Thomas, T. A.; Nelson, D. L.; Eze, U. D.; Jeong, W. J.; Harris, J.; Mukherjee, P. P.; McDowell, M. T. Linking Pressure to Electrochemical Evolution in Solid-State Conversion Cathode Composites. **ACS Applied Materials & Interfaces** 2026, 18, 1626–1640. DOI: 10.1021/acsami.5c20956.

31. Ng, B.; Faegh, E.; Lateef, S.; Karakalos, S. G.; Mustain, W. E. Structure and chemistry of the solid electrolyte interphase (SEI) on a high capacity conversion-based anode: NiO. **Journal of Materials Chemistry A** 2021, 9, 523. DOI: 10.1039/D0TA09683K.

32. Parsons, R. Electrochemical nomenclature. **Pure and Applied Chemistry** 1974, 37, 499–516. DOI: 10.1351/pac197437040499.

33. Tian, K.-H.; Duan, C.-Q.; Ma, Q.; Li, X.-L.; Wang, Z.-Y.; Sun, H.-Y.; Luo, S.-H.; Wang, D.; Liu, Y.-G. High-entropy chemistry stabilizing spinel oxide (CoNiZnXMnLi)₃O₄ (X = Fe, Cr) for high-performance anode of Li-ion batteries. **Rare Metals** 2022, 41, 1265–1275. DOI: 10.1007/s12598-021-01872-4.

34. Yang, X.; Wang, H.; Song, Y.; Liu, K.; Huang, T.; Wang, X.; Zhang, C.; Li, J. Low-Temperature Synthesis of a Porous High-Entropy Transition-Metal Oxide as an Anode for High-Performance Lithium-Ion Batteries. **ACS Applied Materials & Interfaces** 2022, 14, 26873–26881. DOI: 10.1021/acsami.2c07576.

35. Xiao, B.; Wu, G.; Wang, T.; Wei, Z.; Xie, Z.; Sui, Y.; Qi, J.; Wei, F.; Zhang, X.; Tang, L.-B.; Zheng, J.-C. Enhanced Li-Ion Diffusion and Cycling Stability of Ni-Free High-Entropy Spinel Oxide Anodes with High-Concentration Oxygen Vacancies. **ACS Applied Materials & Interfaces** 2023, 15, 2792–2803. DOI: 10.1021/acsami.2c12374.

36. Zhu, S.; Nong, W.; Nicholas, L. J. J.; Cao, X.; Zhang, P.; Lu, Y.; Xiu, M.; Huang, K.; Wu, G.; Yang, S.-W.; Wu, J.; Liu, Z.; Srinivasan, M.; Hippalgaonkar, K.; Huang, Y. Rapid in situ growth of high-entropy oxide nanoparticles with reversible spinel structures for efficient Li storage. **Journal of Materials Chemistry A** 2024, 12, 11473–11486. DOI: 10.1039/D3TA08101J.

37. Deiss, E. Spurious chemical diffusion coefficients of Li⁺ in electrode materials evaluated with GITT. **Electrochimica Acta** 2005, 50, 2927–2932. DOI: 10.1016/j.electacta.2004.11.042.


# Figure Captions

**Figure 1. Mg incorporation and ball milling alter crystal structure, composition, and nanoscale microstructure of spinel HEOs.** The four materials are compared using the final XRD, ICP-OES, HRTEM/SAED, and elemental-mapping dataset. The figure establishes the parent spinel-type structure, the comparatively modest lattice/compositional perturbation associated with Mg incorporation, and milling-induced changes in coherent-domain/microstructural characteristics. No unique Mg site is assigned without final refinement, and the chemically incompatible preliminary CoGa₂O₄ indexing is excluded. **[[YOO GROUP INPUT REQUIRED — freeze final refined XRD/HRTEM/SAED/ICP dataset and panel order.]]**

**Figure 2. Ball milling primarily modifies particle morphology and physical surface characteristics.** SEM morphology, particle/domain-size statistics, and BET surface area are used to compare HEO, BM-HEO, Mg-HEO, and BM-Mg-HEO before cycling. XPS is included only if the final dataset is reproducible and mechanistically defensible. Electrochemically derived interface metrics are intentionally excluded from this characterization figure and are kept as supporting electrochemical context in the Supporting Information. **[[YOO GROUP INPUT REQUIRED — freeze final SEM/particle-size/BET package and final XPS inclusion decision.]]**

**Figure 3. Ball milling increases accessible capacity whereas Mg incorporation decreases it.** (a) First-cycle voltage profiles of pristine HEO, BM-HEO, Mg-HEO, and BM-Mg-HEO. (b) First-cycle lithiation and delithiation capacities with the corresponding initial Coulombic efficiencies. (c) Specific capacity during cycling at 0.1 C. (d) Absolute rate capability over the 0.1–5 C sequence followed by recovery at 0.1 C. The results establish the differences in accessible capacity among the four materials before comparison with the GITT relaxation response.

**Figure 4. GITT reveals distinct mismatches among accessible reaction extent, relaxation magnitude, relaxation timescale, and conventional apparent diffusivity.** (a) Representative first-lithiation GITT step consisting of a 10 min galvanostatic pulse followed by a 60 min open-circuit rest, defining the 3 s-to-60 min relaxation voltage change, $\Delta E_{\mathrm{relax}}$, and the model-free relaxation timescale, $t_{63}$. (b) State-matched HEO/BM-HEO comparison of $D_{\mathrm{app,BM}}/D_{\mathrm{app,HEO}}$ and the direct relaxation-rate ratio $t_{63,\mathrm{HEO}}/t_{63,\mathrm{BM}}$. Both ratios are oriented so that values above unity indicate faster BM-HEO. The $D_{\mathrm{app}}$ ratio remains above unity at all 37 matched states, whereas the direct relaxation-rate ratio is below unity at 35 of 37 states. (c) Median $\Delta E_{\mathrm{relax}}$ versus median $t_{63}$ over the common 200–800 mAh g⁻¹ interval for all four materials. Mg incorporation decreases the relaxation voltage change while lengthening $t_{63}$. (d) First-cycle delithiation capacity versus median $t_{63}$. Ball milling increases accessible capacity while lengthening $t_{63}$, whereas Mg incorporation decreases accessible capacity while $t_{63}$ increases. Arrows indicate the corresponding material modifications.

**Figure 5. The excess current-off relaxation is localized to the conversion region.** (a) State-resolved relaxation magnitude, $\Delta E_{\mathrm{relax}}$, during the first lithiation as a function of normalized lithiation capacity, $z$. Dashed curves indicate the sample-specific relaxation backgrounds, and the shaded region denotes the common window used to evaluate the excess response. (b) Normalized background-subtracted GITT excess relaxation plotted against rest-end voltage together with the corresponding first-cycle cathodic $dQ/dV$ response for HEO, BM-HEO, Mg-HEO, and BM-Mg-HEO. Dotted lines mark the respective peak voltages. (c) Comparison of the GITT excess-peak voltage, $V_{\mathrm{peak,GITT}}$, with the cathodic $dQ/dV$ peak voltage, $V_{\mathrm{peak},dQ/dV}$. The dashed line represents $V_{\mathrm{peak,GITT}}=V_{\mathrm{peak},dQ/dV}$. The close correspondence between the two peak positions localizes the excess relaxation to the conversion region.

**Figure 6. Conversion-associated relaxation evolves with cycle history.** (a) Cycle dependence of the normalized lithiation state at the excess-relaxation peak, $z_{\mathrm{peak}}$. (b) Corresponding excess-peak amplitude during cycles 1–3. (c) Median characteristic relaxation time, $t_{63}$, over the common lithiation-state interval. (d) Relative change in excess-peak amplitude, $A_3/A_1$, plotted against the corresponding change in relaxation timescale, $t_{63,3}/t_{63,1}$, from cycle 1 to cycle 3. Dashed lines denote unity. Cycling produces substantially larger changes in the magnitude and state location of the conversion-associated response than in its characteristic relaxation timescale.

**Figure 7. Microkinetic analysis shows how the capacity–kinetics mismatch can arise from multistep conversion.** (a) Literature-informed coarse-grained conversion network, $O\rightleftharpoons I\rightleftharpoons I^*\rightleftharpoons C$, with R1 and R3 representing reversible Faradaic steps and R2 an effective structural/reconstruction coordinate. The states are effective kinetic states rather than uniquely assigned phases. (b) Current-off balance showing that $j_{\mathrm{ext}}=0$ can coexist with finite opposing Faradaic partial currents and finite internal redistribution. (c) Homogeneous kinetic-speed control: scaling all rates together increases cutoff-limited capacity and shortens matched-state $t_{63}$. (d) Heterogeneous-accessibility existence proof on the same axes as panel (c): retaining the reference accessible branch while adding an illustrative accessible branch with a slower reconstruction step produces both higher cutoff capacity and longer matched-state $t_{63}$. The dashed trajectory is the homogeneous control. The calculation is an existence proof and does not assign the illustrated branch, population weights, or rate contrast uniquely to ball milling.
