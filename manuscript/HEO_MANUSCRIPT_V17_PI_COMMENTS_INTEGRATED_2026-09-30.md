# HEO Manuscript v17 — PI-Comment Integrated Capacity–Kinetics Draft

**Date:** 2026-09-30  
**Status:** Figure 4 conversion-window analysis, PI comments 0–54, Figure 5 relaxation-hump terminology, and revised four-step BM/Mg microkinetic interpretation integrated; Abstract, Introduction, and Conclusions re-aligned to the revised evidence chain
**Scientific backbone:** Figures 1–2 materials modifications → Figure 3 accessible capacity → Figure 4 capacity–relaxation mismatch + conventional-GITT conflict → Figure 5 conversion-region localization of the late-stage relaxation hump → Figure 6 distinct kinetic and thermodynamic perturbations within one four-step conversion network; cycle-resolved and numerical robustness remain in the Supporting Information
**Literature basis:** `HEO_REFERENCE_MASTER_VERIFIED_2026-09-18.md` + `HEO_REFERENCE_CANDIDATES_MICROKINETICS_2026-09-28.md` + `references/HEO_CONVERSION_GITT_LITERATURE_AUDIT_2026-09-26.md`

> Verified information is written directly. Missing experimental metadata are not inferred. Inputs expected from the Yoo group and Yoon Lab remain explicitly marked. The Figure 5 differential-capacity peak positions currently come from reconstruction of the latest vector voltage profiles; the underlying numerical first-cycle files should replace this source if recovered before submission.

---

# Working title

**Mismatch between Capacity and Conversion Kinetics in Spinel High-Entropy Oxide Anodes**

Alternative:

**Capacity–Kinetics Mismatch in Multistep Conversion of Spinel High-Entropy Oxide Anodes**

---


# Abstract

Faster conversion kinetics are generally expected to increase the capacity accessible at a given current within a fixed voltage window. However, conversion couples electron transfer, structural reconstruction, nucleation and phase growth, and cation/oxygen redistribution, complicating the relation between reaction extent and kinetic speed. This relation is examined in spinel high-entropy oxide (HEO) anodes modified by ball milling or Mg incorporation. Galvanostatic intermittent titration (GITT) relaxation is described directly by the voltage relaxation magnitude, $\Delta E_{\mathrm{relax}}$, and a characteristic relaxation time, $t_{63}$. Ball milling increases first-cycle reversible capacity while lengthening $t_{63}$, demonstrating that higher accessible capacity can coexist with slower relaxation. Mg incorporation decreases accessible capacity and markedly reduces $\Delta E_{\mathrm{relax}}$, while $t_{63}$ remains nearly unchanged. Conventional GITT-derived apparent diffusivity gives a conflicting kinetic ordering for the HEO/BM-HEO pair, ranking BM-HEO faster despite its longer relaxation time. A four-step conversion model shows that step-selective changes in internal reaction rates can produce higher accessible capacity with slower relaxation, whereas a product-side equilibrium shift can produce the Mg-like combination of lower capacity, smaller relaxation magnitude, and little change in $t_{63}$. These results distinguish accessible reaction extent, relaxation magnitude, relaxation timescale, and apparent diffusivity as related but non-equivalent observables in multistep conversion systems.

**Keywords:** high-entropy oxide; conversion anode; GITT; apparent diffusion coefficient; voltage relaxation; ball milling; Mg incorporation; microkinetics

# 1. Introduction

Conversion-type anodes can achieve high theoretical capacities by accommodating multiple Li ions and electrons through conversion reactions. This high capacity, however, comes with extensive structural and chemical reconstruction during conversion, involving bond rearrangement, nucleation and growth of new phases, and redistribution of cations and oxygen. These coupled processes can introduce substantial kinetic limitations, leading to polarization, incomplete reaction, and rate-dependent capacity. Understanding how material modifications affect these kinetics is therefore important for interpreting their influence on electrochemical performance.

The galvanostatic intermittent titration technique (GITT) is widely used to estimate apparent Li-ion diffusion coefficients, $D_{\mathrm{app}}$, from the voltage response to a current pulse and subsequent relaxation. These $D_{\mathrm{app}}$ values are often compared across compositions, structures, and processing conditions as kinetic descriptors, including for conversion-type electrodes and high-entropy oxides (HEOs).[1–5] However, conventional GITT diffusion analysis relies on assumptions that can be distorted by finite reaction kinetics, phase transformation, or other non-diffusive contributions.[6–9] For reconstructive conversion reactions, the resulting $D_{\mathrm{app}}$ may therefore not track the directly observed relaxation rate.

The GITT relaxation can also be examined directly without converting the measured voltage response into a diffusion coefficient. Two readily accessible quantities are the magnitude of the voltage relaxation, $\Delta E_{\mathrm{relax}}$, and a characteristic relaxation time, which quantify the extent and timescale of the relaxation after current interruption, respectively. Such quantities do not require specification of a solid-state diffusion model and can therefore provide complementary information when the transient is not purely diffusional. Accessible capacity provides a separate measure of how much conversion is reached under load. Together, accessible capacity, $\Delta E_{\mathrm{relax}}$, and the characteristic relaxation time provide complementary observables for examining the relationship between accessible reaction extent and conversion kinetics.

Spinel HEOs provide a useful material system for examining this relationship. Spinel (FeCoNiCrMn)₃O₄ is a conversion-type anode in which multiple redox-active cations share a common oxide structure.[1,10–13] Its lithiation involves substantial reconstruction, including progressive formation of metallic species, Li₂O, and rock-salt-like phases accompanied by cation and oxygen rearrangement.[14–16] Ball milling and Mg incorporation provide complementary modifications of this conversion behavior. Milling increases surface area and has been associated with enhanced conversion reversibility,[1,17] whereas Mg-containing HEOs have been reported to exhibit greater structural retention but lower accessible capacity.[18–20] Because these modifications change accessible conversion in opposite directions, they provide a useful basis for testing whether capacity changes are accompanied by corresponding changes in relaxation kinetics.

Here, pristine HEO, ball-milled HEO (BM-HEO), Mg-containing HEO (Mg-HEO), and BM-Mg-HEO are compared to examine the relationships among accessible conversion capacity, GITT relaxation, and conventional GITT-derived apparent diffusivity. The comparison reveals that accessible capacity and relaxation kinetics do not always vary in the conventionally expected direction. Differential-capacity analysis identifies whether the anomalous relaxation occurs in the conversion region, and a four-step microkinetic model shows how distinct kinetic and thermodynamic perturbations within a multistep conversion reaction can produce the observed capacity–relaxation relationships.

# 2. Results and Discussion# 2. Results and Discussion

## 2.1. Structural and morphological characteristics of the HEO series

Figures 1 and 2 are reserved for the structural, compositional, and morphological characterization of HEO, BM-HEO, Mg-HEO, and BM-Mg-HEO. The current working dataset indicates that all four materials retain a predominantly spinel-type HEO structure, while Mg incorporation and ball milling introduce distinct compositional, lattice, particle, and surface-level changes. Ball milling also produces a marked increase in BET surface area. These characterization results will be finalized using the collaborator-verified XRD/refinement, ICP-OES, TEM/SAED/EDS, SEM, BET, and, if retained, XPS datasets.

At this stage, Figures 1–2 are used only to establish that Mg incorporation and ball milling produce distinguishable materials-level perturbations before electrochemical testing. Detailed phase assignments, Mg-site interpretation, quantitative lattice changes, and XPS-based mechanistic claims are intentionally deferred until the final characterization package is frozen.

**[[YOO GROUP INPUT REQUIRED — finalize Figure 1–2 panel composition and the corresponding structural interpretation using the verified XRD/ICP/TEM/SAED/EDS/SEM/BET dataset; decide separately whether XPS remains in the Supporting Information or is promoted to a main characterization figure.]]**



## 2.2. Ball milling increases accessible capacity whereas Mg incorporation decreases it

Figure 3 establishes the differences in accessible capacity among the four materials. The first-cycle lithiation/delithiation capacities are 901.25/609.12 mAh g⁻¹ for pristine HEO, 1056.10/782.08 mAh g⁻¹ for BM-HEO, 731.15/458.91 mAh g⁻¹ for Mg-HEO, and 944.07/580.83 mAh g⁻¹ for BM-Mg-HEO, corresponding to initial Coulombic efficiencies of 67.59%, 74.05%, 62.77%, and 61.52%, respectively. Ball milling therefore increases accessible capacity in both the Mg-free and Mg-containing materials, whereas Mg incorporation decreases capacity relative to the corresponding Mg-free composition.

The milling effect is accompanied by a marked increase in surface area and reduced particle/domain dimensions, which can increase the fraction of material and interfaces participating electrochemically. Previous work on the same five-cation spinel family likewise showed that particle fragmentation can increase conversion reversibility and interfacial storage.[17] The higher capacity after milling is therefore consistent with these previous observations.

Mg incorporation produces the opposite low-rate capacity trend. Mg-containing electrodes exhibit lower absolute capacity, and the reduced reversible reaction extent persists beyond the first cycle. This trend is consistent with previous reports of lower accessible conversion in Mg-containing HEO compositions.[18–20] Milling partially recovers the lost utilization in BM-Mg-HEO, although its capacity remains below that of BM-HEO.

The rate-capability measurements further distinguish the four materials. BM-HEO retains higher absolute capacity than pristine HEO throughout the measured rate sequence, including approximately 193 versus 79 mAh g⁻¹ at 5 C. Mg-HEO, despite its lower low-rate capacity, retains approximately 185 mAh g⁻¹ at 5 C. These rate-dependent differences are not used here to assign intrinsic conversion kinetics. Figure 3 instead establishes the differences in accessible reaction extent that are subsequently compared with the GITT relaxation response.

These contrasting capacity changes provide two complementary comparisons in Figure 4. Ball milling tests whether an increase in accessible conversion is accompanied by faster relaxation, whereas Mg incorporation provides the corresponding lower-accessibility case. The GITT relaxation is then compared with conventional apparent diffusivity to determine whether the different measures give a consistent kinetic interpretation.

## 2.3. Ball milling reveals a capacity–kinetics mismatch and a conflicting apparent-diffusivity trend

GITT was used to compare the relaxation dynamics of the four materials (Figure 4a). Each step consists of a 10 min galvanostatic pulse followed by a 60 min open-circuit rest. The relaxation magnitude, $\Delta E_{\mathrm{relax}}$, is defined from 3 s after current interruption to the end of the 60 min rest, and $t_{63}$ is the time required to complete 63.2% of this observed relaxation. A longer $t_{63}$ therefore indicates slower relaxation. The value is determined directly from the measured voltage trajectory rather than from a fitted relaxation model. Full multi-cycle GITT profiles are provided in Figure S13.

Ball milling provides the primary contradiction to the conventional capacity–kinetics expectation. Over the common normalized first-lithiation window, $z=Q/Q_{\max}=0.40$–0.90, the median $t_{63}$ increases from 10.37 min for pristine HEO to 13.02 min for BM-HEO, while the first-cycle delithiation capacity increases from 609.12 to 782.08 mAh g$^{-1}$. Higher accessible capacity therefore coexists with slower relaxation after milling (Figure 4d). The same qualitative milling direction is observed for the Mg-containing pair: the delithiation capacity increases from 458.91 to 580.83 mAh g$^{-1}$ while the median $t_{63}$ increases from 10.53 to 12.70 min.

A conventional GITT diffusivity analysis of the compositionally identical pristine HEO/BM-HEO pair gives the opposite kinetic indication (Figure 4b). Across the state-matched 200–800 mAh g$^{-1}$ interval, the median $D_{\mathrm{app,BM}}/D_{\mathrm{app,HEO}}$ is 1.78, whereas the median direct relaxation-rate ratio, $t_{63,\mathrm{HEO}}/t_{63,\mathrm{BM}}$, is 0.762. Conventional $D_{\mathrm{app}}$ therefore ranks BM-HEO as faster, whereas $t_{63}$ shows that BM-HEO relaxes more slowly.

This disagreement matters because larger GITT-derived diffusion coefficients are commonly used to support faster-kinetics interpretations in HEO and other conversion-anode studies.[1–5] If only accessible capacity and conventional $D_{\mathrm{app}}$ were considered here, ball milling would be interpreted as accelerating the electrode kinetics. The directly measured relaxation gives the opposite ordering. Apparent diffusivity therefore does not preserve the observed fast–slow ordering of the GITT relaxation.

Mg incorporation provides a complementary comparison. Over the same normalized first-lithiation window, the median $t_{63}$ changes only slightly from 10.37 min for pristine HEO to 10.53 min for Mg-HEO, whereas the median $\Delta E_{\mathrm{relax}}$ decreases markedly from 168.5 to 111.3 mV. Mg incorporation therefore reduces accessible capacity and the magnitude of the relaxation response without producing a corresponding change in the characteristic relaxation time (Figure 4c,d). Across the four materials, relaxation magnitude and relaxation timescale do not collapse onto one scalar kinetic coordinate.

The disagreement between $D_{\mathrm{app}}$ and direct relaxation does not require dismissing Li transport or the operational use of GITT-derived apparent diffusivity. It shows that $D_{\mathrm{app}}$ cannot be assumed to represent the overall relaxation rate of a reconstructive conversion response. The Supporting Information shows that the HEO/BM-HEO ordering persists when $t_{50}$ and $t_{90}$ are used in place of $t_{63}$ and examines how the voltage changes entering the conventional GITT expression contribute to the resulting $D_{\mathrm{app}}$ (Figures S15–S17). Figure 5 next determines whether the late-stage relaxation feature occurs in the conversion region.

## 2.4. The late-stage relaxation hump is localized to the conversion region

Figure 5a first shows the full first-lithiation evolution of $\Delta E_{\mathrm{relax}}$ as a function of normalized lithiation capacity, $z$. An enlarged view of the later part of lithiation reveals a broad relaxation hump above a smooth sample-specific background. The hump is strongest in pristine HEO, becomes lower and broader after ball milling, and is strongly suppressed by Mg incorporation. Subtracting the background isolates this late-stage relaxation feature for comparison with the electrochemical conversion response.

For each GITT step, the background-subtracted relaxation hump was plotted at the voltage measured at the end of the 60 min rest. This rest-end voltage minimizes the polarization remaining from the preceding current pulse and allows direct comparison with the first-cycle cathodic $dQ/dV$ feature. The $dQ/dV$ maxima occur at approximately 0.545, 0.589, 0.419, and 0.485 V for pristine HEO, BM-HEO, Mg-HEO, and BM-Mg-HEO, respectively, whereas the corresponding relaxation-hump maxima occur at 0.527, 0.618, 0.387, and 0.503 V. Using the background shown in Figure 5a, the two peak positions differ by no more than 32 mV for the four materials (Figure 5b,c). Background/window sensitivity is retained in the Supporting Information; despite the broader uncertainty of the shallow BM-Mg-HEO feature, the material-induced peak shifts remain in the same direction as the corresponding $dQ/dV$ shifts.

The close correspondence with the cathodic $dQ/dV$ feature indicates that the late-stage relaxation hump is dominated by processes occurring in the conversion region. This region can involve coupled processes including nucleation and phase growth, phase-boundary motion, M–O bond rearrangement, cation/oxygen redistribution, and metal/Li$_2$O formation.[14–16] The longer $t_{63}$ of BM-HEO therefore represents slower relaxation in a lithiation region dominated by conversion. The hump amplitude and width are retained as response descriptors rather than interpreted as intrinsic kinetic rates; their background/window sensitivity is reported in the Supporting Information.

Figure 6 next examines whether the distinct BM and Mg capacity–relaxation trends can arise within the same multistep conversion network.

## 2.5. Distinct perturbations within a multistep conversion network can produce the BM and Mg trends

Based on established descriptions of metal-oxide conversion reactions,[21,22] the reaction is represented by four effective processes: initial electrochemical lithiation/electron transfer ($R_1$), M–O dissociation and local structural reconstruction ($R_2$), Li$_2$O-forming or product-side reconstruction ($R_3$), and subsequent electron transfer/metal reduction ($R_4$). For calculation, the corresponding effective states are denoted $O$, $I$, $J$, $K$, and $C$, progressing from an oxide-derived state through lithiated/reduced and reconstructed states to a metal/Li$_2$O-containing converted state. The reacting electrode is represented as a single kinetic population with one set of rate parameters; distributions among particles or reaction domains are not included. The purpose is to test relationships among accessible reaction extent and relaxation observables rather than to identify a unique atomistic HEO pathway.

A single-step rate-perturbation analysis first establishes the conventional kinetic response (Figure 6a). The kinetic rate of one effective step is changed while the remaining steps are held fixed; for the reversible internal steps, the forward and reverse rates are scaled together so that their equilibrium constants remain unchanged. Thus, the calculation changes a kinetic timescale without designating the perturbed step as an a priori rate-determining step. Slowing $R_2$ to 0.1 of its reference rate decreases the modeled capacity reached before the fixed voltage cutoff to $Q/Q_0=0.351$ and increases $t_{63}/t_{63,0}$ to 2.44. The corresponding values for $R_3$ are 0.495 and 1.57, whereas $R_1$ and $R_4$ exert substantially weaker control under the representative parameter set. A simple slowing of one internal step therefore gives the conventional combination of lower accessible capacity and slower relaxation.

A different response emerges when $R_2$ and $R_3$ change selectively (Figure 6b). Their rate scales are varied independently while the equilibrium constants and the electrochemical equilibrium parameters are kept fixed. The resulting map contains the conventional lower-capacity/slower-relaxation and higher-capacity/faster-relaxation regions, together with a finite region in which both $Q/Q_0>1$ and $t_{63}/t_{63,0}>1$. Thus, higher accessible capacity and slower relaxation do not require a separate reaction mechanism; they can arise when different internal steps of the same conversion network change in different directions.

The physical meaning of the relaxation modes can be understood from the redistribution of the intermediate populations after current interruption. The populations of $I$, $J$, and $K$ continue to change even though the external current is zero, because forward and reverse partial reactions remain coupled internally. Near the relaxed state, these coupled changes can be decomposed into a small number of natural exponential relaxation modes,
\[
\frac{d\,\delta\mathbf{x}}{dt}=\mathbf{J}\delta\mathbf{x},
\qquad
\delta E(t)=\sum_i B_i\exp(-t/\tau_i).
\]
Each $\tau_i$ therefore represents a collective relaxation of several coupled intermediates rather than the time constant of one elementary reaction. For a representative point in the higher-capacity/slower-relaxation region ($R_2\times0.465$, $R_3\times50$), $Q/Q_0=1.111$ and $t_{63}/t_{63,0}=1.087$, while the slowest finite relaxation mode increases from 15.35 to 17.68 min (Figure 6d). A slow internal mode can therefore lengthen while a different part of the network sustains greater reaction throughput before the voltage cutoff.

Figure 6c projects these model responses into the same observable space used for the experiments. For BM-HEO relative to pristine HEO, the experimental ratios are $Q/Q_0=1.284$ and $t_{63}/t_{63,0}=1.256$. The point lies in the same higher-capacity/slower-relaxation direction as the step-selective $R_2$–$R_3$ response, although the experimental changes are larger than those reached by the minimal two-parameter map. This magnitude difference is expected because the model omits distributions among particles and domains, spatial transport, interfacial polarization, and other contributions to the measured electrode response. The model result is therefore interpreted as a mechanistic-consistency test of the ordering rather than a quantitative reproduction of the experimental magnitude.

The revised Mg comparison follows a different direction. Relative to pristine HEO, Mg-HEO gives $Q/Q_0=0.753$ and $t_{63}/t_{63,0}=1.015$, together with a much smaller relaxation magnitude. This point is not reproduced by the fixed-thermodynamics $R_2$–$R_3$ kinetic map, because lowering capacity through slower $R_2$ or $R_3$ also lengthens $t_{63}$ too strongly. However, keeping the kinetic rates fixed and shifting the product-side electrochemical equilibrium offset generates a lower-capacity trajectory with almost unchanged $t_{63}$. An illustrative shift of the dimensionless product-side offset from $-3$ to $-1.5$ gives $Q/Q_0=0.764$, $t_{63}/t_{63,0}=0.998$, and a modeled relaxation-magnitude ratio of 0.755. The corresponding experimental Mg-HEO/pristine-HEO relaxation-magnitude ratio is 0.661. The voltage relaxation in the conversion region can also contain transport, interfacial polarization, and state-dependent thermodynamic contributions, so its absolute magnitude is compared only directionally. The calculation therefore shows that the Mg-like combination of lower capacity, smaller relaxation magnitude, and nearly unchanged timescale is also accessible within the same multistep conversion network. It does not assign Mg incorporation uniquely to the chosen equilibrium-offset change.

Together, the BM and Mg comparisons show that material modification need not move a conversion electrode along one global fast–slow axis. Step-selective kinetic changes can increase accessible reaction extent while slowing relaxation, whereas a thermodynamic shift can reduce accessible reaction extent and relaxation magnitude with little change in the characteristic relaxation time. Accessible capacity, relaxation magnitude, and relaxation timescale are therefore coupled through the same reaction network but remain distinct observables.

# 3. Conclusions

Ball milling reveals that higher accessible capacity can coexist with slower relaxation in the conversion region of spinel HEO anodes. Over the common normalized first-lithiation window, BM-HEO has a longer $t_{63}$ than pristine HEO even though its first-cycle reversible capacity is higher. The same milling direction is observed in the Mg-containing pair. Mg incorporation provides a different comparison: accessible capacity and $\Delta E_{\mathrm{relax}}$ both decrease substantially, whereas $t_{63}$ remains nearly unchanged. Differential-capacity analysis localizes the late-stage relaxation hump to the conversion region, and the cycle-resolved GITT analysis in the Supporting Information shows that the BM capacity–relaxation ordering is not restricted to the first cycle.

Conventional GITT analysis gives a conflicting kinetic indication for the compositionally identical pristine HEO/BM-HEO pair. Over the state-matched 200–800 mAh g$^{-1}$ interval, the median $D_{\mathrm{app,BM}}/D_{\mathrm{app,HEO}}$ is 1.78, whereas the median direct relaxation-rate ratio $t_{63,\mathrm{HEO}}/t_{63,\mathrm{BM}}$ is 0.762. A larger apparent GITT diffusion coefficient therefore does not necessarily indicate faster overall relaxation during conversion.

The four-step conversion model shows why the experimental observables need not follow one scalar kinetic coordinate. Slowing a single internal step gives the conventional lower-capacity/slower-relaxation response, whereas step-selective changes in $R_2$ and $R_3$ create a finite regime with higher accessible capacity and longer relaxation, reproducing the BM trend direction. A product-side equilibrium shift produces the Mg-like direction of lower capacity, smaller relaxation magnitude, and nearly unchanged $t_{63}$. These model perturbations are mechanistic consistency tests rather than unique assignments of ball milling or Mg incorporation. Accessible capacity, relaxation magnitude, relaxation timescale, and GITT-derived apparent diffusivity should therefore be treated as related but non-equivalent observables when evaluating materials modifications in multistep conversion electrodes.

# 4.# 4. Experimental Section

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

The late-stage relaxation hump was isolated by subtracting a smooth sample-specific background from the first-lithiation $\Delta E_{\mathrm{relax}}$ response. The nominal background was fitted using $z=0.20$–0.40 and 0.90–1.00, and the background-subtracted hump was evaluated over $z=0.40$–0.90. For voltage-localization analysis, each GITT step was assigned its 60 min rest-end voltage. Peak position, peak amplitude, and FWHM-like width were used as comparative response descriptors. Detailed background definitions, peak-position/window sensitivity, short-time post-interruption analysis, and additional relaxation descriptors are provided in the Supporting Information.

To audit the conventional diffusivity interpretation, a state-matched relative $D_{\mathrm{GITT,app}}$ comparison was performed for the compositionally identical HEO/BM-HEO pair over 200–800 mAh g⁻¹. The conventional finite-pulse form $D\propto (m_B/S)^2(\Delta E_s/\Delta E_\tau)^2/\tau$ was used only for relative ranking. $\Delta E_s$ was the relaxed voltage increment between consecutive rest endpoints, and $\Delta E_\tau$ was the voltage excursion from 3 s after pulse onset to the pulse end. The same 3 s reference suppresses the unresolved initial fast/ohmic contribution. The current relative comparison uses the same geometric electrode area for HEO and BM-HEO, consistent with the common electrode geometry used in these experiments. Absolute $D$ values are not used because the final active-mass and molar-volume metadata are not yet frozen; the full relative-analysis definition and sensitivity audit are given in the Supporting Information.

First-cycle differential-capacity curves were obtained from the corresponding galvanostatic voltage profiles using the same differentiation and smoothing procedure for all four materials. The current manuscript-development curves were reconstructed from the latest vector voltage profiles because the original numerical first-cycle source files have not yet been recovered; this source should be replaced by the original numerical data before submission if available.



## 4.4. Four-step conversion microkinetic model

A coarse-grained four-step model was used to test whether the experimentally observed capacity–relaxation relationships can arise within a single multistep metal-oxide conversion network.[21,22] The reacting electrode is represented as one kinetic population with one set of rate parameters; distributions among particles or reaction domains are not included. The effective sequence connects an oxide-derived state, a lithiated/reduced oxide state, an M–O-reconstructed state, a product-side reconstructed state, and a metal/Li$_2$O-containing converted state. These computational states are denoted $O$, $I$, $J$, $K$, and $C$, respectively.

$R_1$ represents initial electrochemical lithiation/electron transfer, $R_2$ effective M–O dissociation/local reconstruction, $R_3$ effective Li$_2$O-forming or product-side reconstruction, and $R_4$ subsequent electron transfer/metal reduction. $R_1$ and $R_4$ were represented by reversible Butler–Volmer-type kinetics with symmetric transfer coefficients, whereas the two internal steps were represented by reversible first-order rates,
\[
r_2=k_{2,f}a_I-k_{2,r}a_J,
\qquad
r_3=k_{3,f}a_J-k_{3,r}a_K.
\]
The state balances are
\[
\frac{dx_I}{dt}=r_1-r_2,\qquad
\frac{dx_J}{dt}=r_2-r_3,\qquad
\frac{dx_K}{dt}=r_3-r_4,\qquad
\frac{dx_C}{dt}=r_4,
\]
with $x_O=1-x_I-x_J-x_K-x_C$. The external Faradaic current is
\[
j_{\mathrm{ext}}=F(\nu_1r_1+\nu_4r_4).
\]

At each integration step during galvanostatic operation, the electrode potential is obtained by solving the current-balance relation for the imposed $j_{\mathrm{ext}}$ at the current set of state populations. The state balances are then integrated until the fixed model voltage cutoff is reached; the modeled accessible capacity is proportional to the charge passed before this cutoff. After current interruption, $j_{\mathrm{ext}}=0$ constrains the sum of the Faradaic partial currents but does not require all internal rates to vanish.[24] The same state equations are integrated during the 3600 s open-circuit relaxation, and $t_{63}$ is extracted using the experimental 3 s reference convention at a common normalized passed charge, $\Delta Q=0.30$.

In the single-step rate-perturbation analysis, one $R_i$ kinetic scale was changed while the remaining steps were held fixed. For $R_2$ and $R_3$, the forward and reverse rate constants were scaled together so that their equilibrium constants were unchanged. The two-dimensional kinetic map independently varied the $R_2$ and $R_3$ rate scales while holding the equilibrium constants and electrochemical equilibrium parameters fixed. For the Mg directional test, the kinetic rates were held fixed while the dimensionless product-side electrochemical equilibrium offset was varied. These calculations separate changes in kinetic timescale from changes in conversion thermodynamics; the illustrative parameter shifts are not assigned uniquely to the experimental materials.

After current interruption, the coupled internal populations can relax through several collective modes. Linearization near the relaxed state gives
\[
\frac{d\,\delta\mathbf{x}}{dt}=\mathbf{J}\delta\mathbf{x},
\qquad
E(t)-E_{\mathrm{eq}}=\sum_i B_i\exp(-t/\tau_i),
\]
where each $\tau_i$ is a collective relaxation timescale of the coupled reaction network rather than the time constant of a single elementary step. The experimental $\Delta E_{\mathrm{relax}}$ in the conversion region can also contain transport, interfacial polarization, and state-dependent thermodynamic contributions beyond the coarse-grained reaction sequence.[23] The modeled relaxation amplitude is therefore used only for directional comparison. Parameter values, detailed rate expressions, numerical integration procedures, state-perturbation equations, and sensitivity audits are provided in the Supporting Information.

# References# References

1. Xiao, B.; Wu, G.; Wang, T.; Wei, Z.; Sui, Y.; Shen, B.; Qi, J.; Wei, F.; Zheng, J. High-entropy oxides as advanced anode materials for long-life lithium-ion batteries. **Nano Energy** 2022, 95, 106962. DOI: 10.1016/j.nanoen.2022.106962.

2. Tian, K.-H.; Duan, C.-Q.; Ma, Q.; Li, X.-L.; Wang, Z.-Y.; Sun, H.-Y.; Luo, S.-H.; Wang, D.; Liu, Y.-G. High-entropy chemistry stabilizing spinel oxide (CoNiZnXMnLi)₃O₄ (X = Fe, Cr) for high-performance anode of Li-ion batteries. **Rare Metals** 2022, 41, 1265–1275. DOI: 10.1007/s12598-021-01872-4.

3. Yang, X.; Wang, H.; Song, Y.; Liu, K.; Huang, T.; Wang, X.; Zhang, C.; Li, J. Low-Temperature Synthesis of a Porous High-Entropy Transition-Metal Oxide as an Anode for High-Performance Lithium-Ion Batteries. **ACS Applied Materials & Interfaces** 2022, 14, 26873–26881. DOI: 10.1021/acsami.2c07576.

4. Xiao, B.; Wu, G.; Wang, T.; Wei, Z.; Xie, Z.; Sui, Y.; Qi, J.; Wei, F.; Zhang, X.; Tang, L.-B.; Zheng, J.-C. Enhanced Li-Ion Diffusion and Cycling Stability of Ni-Free High-Entropy Spinel Oxide Anodes with High-Concentration Oxygen Vacancies. **ACS Applied Materials & Interfaces** 2023, 15, 2792–2803. DOI: 10.1021/acsami.2c12374.

5. Zhu, S.; Nong, W.; Nicholas, L. J. J.; Cao, X.; Zhang, P.; Lu, Y.; Xiu, M.; Huang, K.; Wu, G.; Yang, S.-W.; Wu, J.; Liu, Z.; Srinivasan, M.; Hippalgaonkar, K.; Huang, Y. Rapid in situ growth of high-entropy oxide nanoparticles with reversible spinel structures for efficient Li storage. **Journal of Materials Chemistry A** 2024, 12, 11473–11486. DOI: 10.1039/D3TA08101J.

6. Jia, M.; Zhang, W.; Cai, X.; Zhan, X.; Hou, L.; Yuan, C.; Guo, Z. Re-understanding the galvanostatic intermittent titration technique: Pitfalls in evaluation of diffusion coefficients and rational suggestions. **Journal of Power Sources** 2022, 543, 231843. DOI: 10.1016/j.jpowsour.2022.231843.

7. Zhu, Y.; Wang, C. Galvanostatic Intermittent Titration Technique for Phase-Transformation Electrodes. **The Journal of Physical Chemistry C** 2010, 114, 2830–2841. DOI: 10.1021/jp9113333.

8. Horner, J. S.; Whang, G.; Ashby, D. S.; Kolesnichenko, I. V.; Lambert, T. N.; Dunn, B. S.; Talin, A. A.; Roberts, S. A. Electrochemical Modeling of GITT Measurements for Improved Solid-State Diffusion Coefficient Evaluation. **ACS Applied Energy Materials** 2021, 4, 11460–11469. DOI: 10.1021/acsaem.1c02218.

9. Deiss, E. Spurious chemical diffusion coefficients of Li⁺ in electrode materials evaluated with GITT. **Electrochimica Acta** 2005, 50, 2927–2932. DOI: 10.1016/j.electacta.2004.11.042.

10. Rost, C. M.; Sachet, E.; Borman, T.; Moballegh, A.; Dickey, E. C.; Hou, D.; Jones, J. L.; Curtarolo, S.; Maria, J.-P. Entropy-stabilized oxides. **Nature Communications** 2015, 6, 8485. DOI: 10.1038/ncomms9485.

11. Sarkar, A.; Velasco, L.; Wang, D.; Wang, Q.; Talasila, G.; de Biasi, L.; Kübel, C.; Brezesinski, T.; Bhattacharya, S. S.; Hahn, H.; Breitung, B. High entropy oxides for reversible energy storage. **Nature Communications** 2018, 9, 3400. DOI: 10.1038/s41467-018-05774-5.

12. Dąbrowa, J.; Stygar, M.; Mikuła, A.; Knapik, A.; Mroczka, K.; Tejchman, W.; Danielewski, M.; Martin, M. Synthesis and microstructure of the (Co,Cr,Fe,Mn,Ni)3O4 high entropy oxide characterized by spinel structure. **Materials Letters** 2018, 216, 32–36. DOI: 10.1016/j.matlet.2017.12.148.

13. Wang, D.; Jiang, S.; Duan, C.; Mao, J.; Dong, Y.; Dong, K.; Wang, Z.; Luo, S.; Liu, Y.; Qi, X. Spinel-structured high entropy oxide (FeCoNiCrMn)3O4 as anode towards superior lithium storage performance. **Journal of Alloys and Compounds** 2020, 844, 156158. DOI: 10.1016/j.jallcom.2020.156158.

14. Huang, C.-Y.; Huang, C.-W.; Wu, M.-C.; Patra, J.; Nguyen, T. X.; Chang, M.-T.; Clemens, O.; Ting, J.-M.; Li, J.; Chang, J.-K.; Wu, W.-W. Atomic-scale investigation of lithiation/delithiation mechanism in high-entropy spinel oxide with superior electrochemical performance. **Chemical Engineering Journal** 2021, 420, 129838. DOI: 10.1016/j.cej.2021.129838.

15. Jin, G.; Luo, C.; Wang, Z.; Jia, S.; Yu, H.; Zhang, C.; Wang, Q.; Zhang, B.; Wang, Z. Unraveling phase transition pathway of spinel (FeCoCrNiMn)3O4 high-entropy oxide anodes for long-life Li-ion batteries. **Materials Today Chemistry** 2025, 48, 102949. DOI: 10.1016/j.mtchem.2025.102949.

16. Li, K.; Shi, L.; An, J.; Zhang, M.; Du, Y.; Ma, Y.; Lou, S.; Yin, G.; Yu, Z.; Hua, X.; Huo, H. Stabilizing Configurational Entropy in Spinel-type High Entropy Oxides during Discharge–Charge by Overcoming Kinetic Sluggish Diffusion. **Angewandte Chemie International Edition** 2025, 64, e202518569. DOI: 10.1002/anie.202518569.

17. Zhai, F.; Zhu, X.; Zhang, W.; Cao, G.; Zhang, H.; Xing, Y.; Xiang, Y.; Zhang, S. Insight of the evolution of structure and energy storage mechanism of (FeCoNiCrMn)3O4 spinel high entropy oxide in life-cycle span as lithium-ion battery anode. **Journal of Power Sources** 2024, 603, 234418. DOI: 10.1016/j.jpowsour.2024.234418.

18. Qiu, N.; Chen, H.; Yang, Z.; Sun, S.; Wang, Y.; Cui, Y. A high entropy oxide (Mg0.2Co0.2Ni0.2Cu0.2Zn0.2O) with superior lithium storage performance. **Journal of Alloys and Compounds** 2019, 777, 767–774. DOI: 10.1016/j.jallcom.2018.11.049.

19. Wang, S.-Y.; Chen, T.-Y.; Kuo, C.-H.; Lin, C.-C.; Huang, S.-C.; Lin, M.-H.; Wang, C.-C.; Chen, H.-Y. Operando synchrotron transmission X-ray microscopy study on (Mg, Co, Ni, Cu, Zn)O high-entropy oxide anodes for lithium-ion batteries. **Materials Chemistry and Physics** 2021, 274, 125105. DOI: 10.1016/j.matchemphys.2021.125105.

20. Wang, K.; Hua, W.; Huang, X.; Stenzel, D.; Wang, J.; Ding, Z.; Cui, Y.; Wang, Q.; Ehrenberg, H.; Breitung, B.; Kübel, C.; Mu, X. Synergy of cations in high entropy oxide lithium ion battery anode. **Nature Communications** 2023, 14, 1487. DOI: 10.1038/s41467-023-37034-6.

21. Ng, B.; Faegh, E.; Lateef, S.; Karakalos, S. G.; Mustain, W. E. Structure and chemistry of the solid electrolyte interphase (SEI) on a high capacity conversion-based anode: NiO. **Journal of Materials Chemistry A** 2021, 9, 523–537. DOI: 10.1039/D0TA09683K.

22. Alsaç, E. P.; Sharma, A. K.; Yoon, S. G.; Vishnugopi, B. S.; Wang, C.; Thomas, T. A.; Nelson, D. L.; Eze, U. D.; Jeong, W. J.; Harris, J.; Mukherjee, P. P.; McDowell, M. T. Linking Pressure to Electrochemical Evolution in Solid-State Conversion Cathode Composites. **ACS Applied Materials & Interfaces** 2026, 18, 1626–1640. DOI: 10.1021/acsami.5c20956.

23. Li, L.; Jacobs, R.; Gao, P.; Gan, L.; Wang, F.; Morgan, D.; Jin, S. Origins of Large Voltage Hysteresis in High-Energy-Density Metal Fluoride Lithium-Ion Battery Conversion Electrodes. **Journal of the American Chemical Society** 2016, 138, 2838–2848. DOI: 10.1021/jacs.6b00061.

24. Parsons, R. Electrochemical nomenclature. **Pure and Applied Chemistry** 1974, 37, 499–516. DOI: 10.1351/pac197437040499.

# Figure Captions

**Figure 1. Mg incorporation and ball milling alter crystal structure, composition, and nanoscale microstructure of spinel HEOs.** The four materials are compared using the final XRD, ICP-OES, HRTEM/SAED, and elemental-mapping dataset. The figure establishes the parent spinel-type structure, the comparatively modest lattice/compositional perturbation associated with Mg incorporation, and milling-induced changes in coherent-domain/microstructural characteristics. No unique Mg site is assigned without final refinement, and the chemically incompatible preliminary CoGa₂O₄ indexing is excluded. **[[YOO GROUP INPUT REQUIRED — freeze final refined XRD/HRTEM/SAED/ICP dataset and panel order.]]**

**Figure 2. Ball milling primarily modifies particle morphology and physical surface characteristics.** SEM morphology, particle/domain-size statistics, and BET surface area are used to compare HEO, BM-HEO, Mg-HEO, and BM-Mg-HEO before cycling. XPS is included only if the final dataset is reproducible and mechanistically defensible. Electrochemically derived interface metrics are intentionally excluded from this characterization figure and are kept as supporting electrochemical context in the Supporting Information. **[[YOO GROUP INPUT REQUIRED — freeze final SEM/particle-size/BET package and final XPS inclusion decision.]]**

**Figure 3. Ball milling increases accessible capacity whereas Mg incorporation decreases it.** (a) First-cycle voltage profiles of pristine HEO, BM-HEO, Mg-HEO, and BM-Mg-HEO. (b) First-cycle lithiation and delithiation capacities with the corresponding initial Coulombic efficiencies. (c) Specific capacity during cycling at 0.1 C. (d) Absolute rate capability over the 0.1–5 C sequence followed by recovery at 0.1 C. The results establish the differences in accessible capacity among the four materials before comparison with the GITT relaxation response.

**Figure 4. GITT reveals distinct mismatches among accessible reaction extent, relaxation magnitude, relaxation timescale, and conventional apparent diffusivity.** (a) Representative first-lithiation GITT step consisting of a 10 min galvanostatic pulse followed by a 60 min open-circuit rest, defining the 3 s-to-60 min relaxation voltage change, $\Delta E_{\mathrm{relax}}$, and the characteristic relaxation time, $t_{63}$. (b) State-matched pristine-HEO/BM-HEO comparison of $D_{\mathrm{app,BM}}/D_{\mathrm{app,HEO}}$ and the direct relaxation-rate ratio $t_{63,\mathrm{HEO}}/t_{63,\mathrm{BM}}$ over 200–800 mAh g$^{-1}$. Both ratios are oriented so that values above unity indicate a faster BM-HEO response under the respective descriptor. (c) Median $\Delta E_{\mathrm{relax}}$ versus median $t_{63}$ over the common normalized first-lithiation window $z=0.40$–0.90 for all four materials. Mg incorporation markedly decreases the relaxation magnitude while leaving the characteristic timescale nearly unchanged. (d) First-cycle delithiation capacity versus median $t_{63}$ over the same normalized window. Ball milling increases accessible capacity while lengthening $t_{63}$ in both the Mg-free and Mg-containing pairs. Arrows indicate the corresponding material modifications.

**Figure 5. The late-stage relaxation hump is localized to the conversion region.** (a) Full first-lithiation relaxation magnitude, $\Delta E_{\mathrm{relax}}$, as a function of normalized lithiation capacity, $z$, together with an enlarged view of the late-stage hump. Dashed curves indicate the sample-specific backgrounds used to isolate the hump over $z=0.40$–0.90. (b) Normalized background-subtracted relaxation hump plotted at the 60 min rest-end voltage of each GITT step together with the corresponding first-cycle cathodic $dQ/dV$ response for pristine HEO, BM-HEO, Mg-HEO, and BM-Mg-HEO. Dotted lines mark the respective peak voltages. (c) Comparison of the relaxation-hump peak voltage with the cathodic $dQ/dV$ peak voltage. The dashed line represents one-to-one correspondence. The close peak correspondence and the matching material-induced shift directions localize the late-stage relaxation hump to the conversion region; background/window sensitivity is reported in the Supporting Information.

**Figure 6. Distinct kinetic and thermodynamic perturbations within a four-step conversion model produce the observed BM and Mg trend directions.** (a) Single-step rate-perturbation analysis in normalized accessible-capacity–$t_{63}$ space. Each effective step, $R_1$–$R_4$, is varied independently while the remaining kinetic parameters and the relevant equilibrium parameters are held fixed. (b) Two-dimensional $R_2$–$R_3$ kinetic-regime map at fixed thermodynamics. The regions are labeled by their observable response, including the finite higher-capacity/slower-relaxation region. (c) Observable-space projection showing the $R_2$–$R_3$ step-selective kinetic response together with the experimental BM-HEO/pristine-HEO point, and a separate product-side equilibrium-offset trajectory together with the experimental Mg-HEO/pristine-HEO point. The two trajectories test distinct perturbations within the same reaction network and are not microscopic assignments to the materials. (d) Representative open-circuit relaxation for the reference model and a point within the higher-capacity/slower-relaxation kinetic region ($R_2\times0.465$, $R_3\times50$). The slowest finite collective relaxation mode increases from 15.35 to 17.68 min while accessible capacity also increases.
