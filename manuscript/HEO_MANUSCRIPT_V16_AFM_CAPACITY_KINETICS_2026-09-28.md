# HEO Manuscript v16 — AFM-Target Capacity–Kinetics / GITT Relaxation Draft

**Date:** 2026-09-28  
**Status:** PI line-by-line review integrated through Section 2.5 and Conclusions; main-text references audited and renumbered by first citation; cycle-resolved history analysis retained in Supporting Information; homogeneous four-step microkinetic analysis is the current model
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

The galvanostatic intermittent titration technique (GITT) is widely used to estimate apparent Li-ion diffusion coefficients, $D_{\mathrm{app}}$, from the voltage response to a current pulse and subsequent relaxation. These $D_{\mathrm{app}}$ values are often compared across compositions, structures, and processing conditions as kinetic descriptors, including for conversion-type electrodes and high-entropy oxides (HEOs).[1–5] However, conventional GITT diffusion analysis relies on assumptions that can be distorted by finite reaction kinetics, phase transformation, or other non-diffusive contributions.[6–9] For reconstructive conversion reactions, the resulting $D_{\mathrm{app}}$ may therefore not track the directly observed relaxation rate.

The GITT relaxation can also be examined directly without converting the measured voltage response into a diffusion coefficient. Two readily accessible quantities are the magnitude of the voltage relaxation, $\Delta E_{\mathrm{relax}}$, and a characteristic relaxation time, which quantify the extent and timescale of the current-off voltage response, respectively. Such quantities do not require specification of a solid-state diffusion model and can therefore provide complementary information when the origin of the transient is not purely diffusional. Accessible capacity provides a separate measure of how much conversion is reached under load. Comparing accessible capacity with these direct relaxation descriptors therefore provides a simple test of whether a modification that increases the accessible extent of conversion also produces faster relaxation kinetics.

Spinel HEOs provide a useful material system for examining this relationship. Spinel (FeCoNiCrMn)₃O₄ is a conversion-type anode in which multiple redox-active cations share a common oxide structure.[1,10–13] Its lithiation involves substantial reconstruction, including progressive formation of metallic species, Li₂O, and rock-salt-like phases accompanied by cation and oxygen rearrangement.[14–16] Ball milling and Mg incorporation provide complementary modifications of this conversion behavior. Milling increases surface area and has been associated with enhanced conversion reversibility,[1,17] whereas Mg-containing HEOs have been reported to exhibit greater structural retention but lower accessible capacity.[18–20] Because these modifications change accessible conversion in opposite directions, they provide a useful basis for testing whether capacity changes are accompanied by corresponding changes in relaxation kinetics.

Here, pristine HEO, ball-milled HEO (BM-HEO), Mg-containing HEO (Mg-HEO), and BM-Mg-HEO are compared to determine the relationships among accessible conversion capacity, GITT relaxation, and conventional GITT-derived apparent diffusivity. The apparent diffusivity is compared with the directly measured relaxation to determine whether the two indicate the same kinetic trend. Differential-capacity analysis identifies whether the anomalous relaxation is associated with conversion, and a literature-grounded four-step microkinetic model tests whether higher accessible capacity and slower relaxation can coexist within a homogeneous multistep conversion network.

# 2. Results and Discussion

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

GITT was used to compare the relaxation dynamics of the four materials (Figure 4a). Each step consists of a 10 min galvanostatic pulse followed by a 60 min open-circuit rest. The relaxation magnitude, $\Delta E_{\mathrm{relax}}$, is defined from 3 s after current interruption to the end of the 60 min rest, and $t_{63}$ is the time required to complete 63.2% of this observed relaxation. $t_{63}$ is used as a measure of relaxation speed, with a longer $t_{63}$ indicating slower relaxation, and is determined directly from the measured trajectory rather than from a fitted relaxation model.

Ball milling provides the primary contradiction to the conventional capacity–kinetics expectation. Over the common 200–800 mAh g⁻¹ interval, the median $t_{63}$ increases from 8.68 min for HEO to 11.57 min for BM-HEO even though ball milling increases the first-cycle accessible capacity. Higher accessible capacity therefore coexists with slower effective relaxation after milling (Figure 4d).

A conventional GITT diffusivity analysis of the compositionally identical HEO/BM-HEO pair gives the opposite kinetic indication (Figure 4b). Across 37 state-matched points spanning 200–800 mAh g⁻¹, $D_{\mathrm{app,BM}}/D_{\mathrm{app,HEO}}$ remains above unity at every point and has a median value of 1.78. In contrast, the direct relaxation-rate ratio, $t_{63,\mathrm{HEO}}/t_{63,\mathrm{BM}}$, has a median value of 0.762 and lies below unity at 35 of 37 points. Conventional $D_{\mathrm{app}}$ therefore indicates faster kinetics for BM-HEO over the same state range in which the directly measured relaxation is predominantly slower.

This inversion is consequential because larger GITT-derived diffusion coefficients are commonly used to support faster-kinetics interpretations in HEO and other conversion-anode studies.[1–5] If only capacity and conventional $D_{\mathrm{app}}$ were considered here, ball milling would naturally be interpreted as accelerating the electrode kinetics. The direct relaxation gives the opposite ordering. The discrepancy is therefore not limited to uncertainty in the numerical value of $D$; apparent diffusivity does not preserve the fast–slow ordering of the measured current-off response.

Mg incorporation provides a complementary constraint rather than a second capacity–rate contradiction. Accessible capacity decreases and the median $t_{63}$ increases from 8.68 to 11.01 min, a combination consistent with slower relaxation. Yet the median $\Delta E_{\mathrm{relax}}$ simultaneously decreases from 160.9 to 109.5 mV (Figure 4c). Thus, the magnitude of the nonequilibrium voltage response becomes smaller even as relaxation becomes slower. Capacity, response magnitude, and relaxation timescale do not collapse onto one scalar kinetic coordinate across the four materials.

These results do not show that Li transport is absent or that GITT-derived $D_{\mathrm{app}}$ lacks operational value. They show that apparent diffusivity cannot be assumed to represent the overall rate of a reconstructive conversion response. The voltage terms entering the conventional GITT expression change unequally after milling, and the full-pulse square-root-time audit in the Supporting Information provides an additional test of the single-diffusion approximation. Figure 5 next determines whether the anomalous relaxation is specifically associated with conversion rather than with a generic cell-relaxation process.

## 2.4. The excess current-off relaxation is localized to the conversion region

The state-resolved GITT relaxation develops a distinct excess feature during the first lithiation (Figure 5a). The feature is strongest in HEO, becomes lower and broader after ball milling, and is strongly suppressed in the Mg-containing materials. To determine whether this current-off response is associated with conversion rather than with a generic relaxation background, the background-subtracted GITT excess was compared with the independently derived first-cycle cathodic $dQ/dV$ response.

For voltage localization, each GITT excess value was assigned the 60 min rest-end voltage of the same state, providing a quasi-relaxed state coordinate without using the pulse polarization itself. Under the nominal background definition, the $dQ/dV$ maxima occur at approximately 0.545, 0.589, 0.419, and 0.485 V for HEO, BM-HEO, Mg-HEO, and BM-Mg-HEO, respectively, whereas the corresponding GITT excess maxima occur at 0.527, 0.618, 0.387, and 0.503 V; the four nominal pairs differ by no more than 32 mV (Figure 5b,c). Background/window variation leaves the HEO and Mg-HEO peak states unchanged and confines BM-HEO to a narrow higher-potential range, whereas the shallow BM-Mg-HEO feature has a broader peak-position sensitivity. Importantly, the direction of all three material-induced shifts—higher after HEO to BM-HEO, lower after HEO to Mg-HEO, and higher after Mg-HEO to BM-Mg-HEO—is preserved across the tested definitions and matches the corresponding $dQ/dV$ shifts. The excess relaxation can therefore be assigned conservatively as conversion-associated, although the present data do not identify a unique microscopic origin such as nucleation, phase-boundary motion, oxygen rearrangement, or metal/Li$_2$O formation.[14–16]

The main role of Figure 5 is intentionally limited to this localization. The nominal excess peak is lower and broader in BM-HEO than in HEO, and the Mg-containing responses are strongly suppressed, but the amplitude and width of the excess are not treated as direct kinetic rates. A 105-condition background/window sensitivity audit preserves the BM-HEO peak-down/width-up trend and the suppression of both Mg-containing peaks relative to HEO; the detailed amplitude-width map and sensitivity ranges are therefore retained in the Supporting Information rather than used as an additional main-text mechanistic coordinate. The shallow BM-Mg-HEO feature, in particular, gives a background-sensitive width and is not used as a quantitative discriminator.

Figure 5 therefore establishes the specific point required for the kinetic argument: the excess current-off response used to interpret the GITT behavior occurs in the same electrochemical region as first-cycle conversion. This supports the term **conversion-associated relaxation** without equating its magnitude, width, or $t_{63}$ with a unique microscopic rate constant. Figure 6 next tests whether the higher-capacity/slower-relaxation ordering is physically accessible within a homogeneous multistep conversion network.


## 2.5. Step-selective conversion kinetics can produce higher capacity with slower relaxation

Conversion is represented by a literature-grounded four-step kinetic sequence, $O\rightleftharpoons I\rightleftharpoons J\rightleftharpoons K\rightleftharpoons C$. Established metal-oxide conversion mechanisms separate initial electrochemical lithiation/electron transfer ($R_1$), M–O dissociation and local structural reconstruction ($R_2$), Li₂O-forming or product-side reconstruction ($R_3$), and subsequent electron transfer/metal reduction ($R_4$).[21,22] The intermediate states are treated as effective kinetic states rather than uniquely identified phases in the present HEO. This coarse-grained sequence is used to test whether the experimentally observed capacity–relaxation ordering is physically accessible within a homogeneous multistep conversion network.

The single-step limiting analysis first establishes the conventional kinetic response (Figure 6a). Each rate is varied independently while the other rates and all equilibrium parameters are held fixed. Slowing either internal step alone decreases the cutoff-limited capacity and lengthens the relaxation. Reducing the $R_2$ rate to 0.1 of its reference value gives $Q_{\mathrm{cutoff}}/Q_0=0.351$ and $t_{63}/t_{63,0}=2.44$, while the corresponding values for $R_3$ are 0.495 and 1.57. $R_1$ and $R_4$ exert substantially weaker control under the representative parameter set. Thus, the higher-capacity/slower-relaxation behavior observed after ball milling is not produced simply by making one conversion step uniformly slower or faster.

A different behavior emerges when the two internal conversion steps change selectively. Figure 6b maps the response obtained by independently varying the $R_2$ and $R_3$ rate scales while keeping the equilibrium parameters fixed. A finite region of this homogeneous parameter space gives both $Q_{\mathrm{cutoff}}/Q_0>1$ and $t_{63}/t_{63,0}>1$; 28 of 396 sampled parameter combinations fall in this higher-capacity/slower-relaxation regime. For example, at an $R_2$ rate scale of approximately 0.41, increasing the $R_3$ rate scale above approximately 8.5 produces higher cutoff capacity together with an approximately 20% longer $t_{63}$. The anomalous ordering is therefore not a single tuned point but occupies a finite step-selective kinetic region.

The origin of this behavior is clarified by the current-off eigenmodes (Figure 6d). Linearization of the relaxation dynamics gives
\[
\delta\dot{\mathbf{x}}=\mathbf{J}\delta\mathbf{x},
\qquad
\delta E(t)=\sum_i B_i\exp(-t/\tau_i),
\]
where $\tau_i$ is an internal relaxation timescale and $B_i$ is its voltage projection. For a representative point within the higher-capacity/slower-relaxation region ($R_2\times0.465$, $R_3\times50$), the cutoff capacity increases by approximately 11%, $t_{63}$ increases by approximately 9%, and the slowest finite eigenmode increases from 15.35 to 17.68 min. A slower internal mode can therefore govern the post-interruption relaxation while a different downstream step sustains greater reaction throughput before the voltage cutoff. Accessible reaction extent and relaxation speed remain coupled to the same conversion network, but they need not preserve the same fast–slow ordering.

The experimental ratios provide an additional constraint on this minimal model (Figure 6c). Mg-HEO lies close to the conventional lower-capacity/slower-relaxation region of the calculated response, consistent with reduced access to conversion accompanied by slower internal relaxation. BM-HEO lies in the higher-capacity/slower-relaxation quadrant predicted by the step-selective model, but the experimental changes are larger than those reached by the minimal two-parameter calculation. The model is therefore used as an existence proof for the observed ordering rather than as a quantitative fit or as an assignment of ball milling or Mg incorporation to specific rate constants. The experimental relaxation magnitude, $\Delta E_{\mathrm{relax}}$, is not used as a quantitative fitting target because the measured 3 s-to-60 min voltage change can contain conversion polarization together with transport, interfacial, and state-dependent thermodynamic contributions.[23] Its distinct behavior in Mg-HEO nevertheless provides a complementary experimental constraint, showing that relaxation magnitude and relaxation speed are not equivalent observables.

This result also provides context for the conventional-GITT analysis. The model does not calculate $D_{\mathrm{app}}$ and does not explain its numerical value. Instead, it shows that even within a homogeneous conversion network, no single kinetic coordinate need control both the amount of reaction accessed before cutoff and the subsequent current-off relaxation. The experimentally observed disagreement between $D_{\mathrm{app}}$ and direct relaxation is therefore consistent with a multistep conversion response in which different kinetic processes contribute differently to the measured observables.

# 3. Conclusions

Ball milling reveals that higher accessible capacity can coexist with slower conversion-associated kinetics in spinel HEO conversion anodes. Over the common first-lithiation interval, BM-HEO accesses more capacity than HEO while its effective current-off relaxation is slower. Mg incorporation provides a complementary constraint: accessible conversion decreases and relaxation remains slower, while the relaxation voltage change is also reduced. Differential-capacity analysis associates the excess relaxation with the conversion region, while cycle-resolved GITT in the Supporting Information shows that the capacity–relaxation mismatch is not explained by first-cycle irreversibility alone.

Conventional GITT analysis gives a conflicting kinetic indication for the compositionally identical HEO/BM-HEO pair. $D_{\mathrm{app}}$ is higher for BM-HEO at all 37 state-matched points between 200 and 800 mAh g⁻¹, whereas the direct current-off relaxation is slower at 35 of 37 points. A larger apparent GITT diffusion coefficient therefore does not necessarily indicate faster overall conversion kinetics. The result does not exclude Li transport; rather, it shows that the apparent diffusivity obtained during conversion need not preserve the fast–slow ordering of the full conversion-associated response.

Microkinetic analysis shows that this ordering is physically accessible within a homogeneous multistep conversion network. Slowing an individual internal step gives the conventional combination of lower cutoff capacity and slower relaxation, whereas step-selective changes in the internal rates create a finite kinetic regime in which cutoff capacity and $t_{63}$ both increase. Eigenmode analysis shows that a slow internal relaxation mode can lengthen while a different downstream step sustains greater reaction throughput. Overall conversion kinetics therefore cannot, in general, be inferred from apparent GITT diffusivity alone. Apparent $D$ can remain useful for operational comparison, but independent kinetic information is required before it is interpreted as the overall rate of a reconstructive conversion reaction.

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



## 4.4. Literature-grounded four-step conversion microkinetic model

A homogeneous coarse-grained model was used to test whether the observed capacity–relaxation ordering is physically accessible within an established multistep metal-oxide conversion motif rather than to fit unique microscopic rate constants or identify a unique rate-determining step.[21,22] The effective sequence is

\[
O\rightleftharpoons I\rightleftharpoons J\rightleftharpoons K\rightleftharpoons C.
\]

$R_1$ represents initial electrochemical lithiation/electron transfer, $R_2$ effective M–O dissociation/local reconstruction, $R_3$ effective Li₂O-forming or product-side reconstruction, and $R_4$ subsequent electron transfer/metal reduction. The states are effective kinetic states and are not assigned to uniquely identified HEO phases. $R_1$ and $R_4$ were represented by reversible Butler–Volmer-type kinetics with symmetric transfer coefficients, whereas the two internal steps were represented by reversible first-order rates,

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

After current interruption, $j_{\mathrm{ext}}=0$ constrains the sum of the Faradaic partial currents but does not require all internal rates to vanish.[24] In the normalized calculation with $\nu_1=\nu_4=1$, finite opposing $r_1$ and $r_4$ can coexist while $r_2$ and $r_3$ continue to redistribute the internal state.

Cutoff capacity was obtained by constant-current integration to a fixed model voltage cutoff. Relaxation was compared at a common normalized passed charge, $\Delta Q=0.30$, followed by a 3600 s current-off period, and $t_{63}$ was extracted using the same 3 s reference convention as in the experiment. In the single-step limiting audit, each $R_i$ rate was scaled independently while all other kinetic and equilibrium parameters were held fixed. The two-dimensional kinetic map independently varied the $R_2$ and $R_3$ rate scales while keeping the equilibrium constants, $R_1$, and $R_4$ fixed.

The current-off response was locally linearized as

\[
\frac{d\,\delta\mathbf{x}}{dt}=\mathbf{J}\delta\mathbf{x},
\qquad
E(t)-E_{\mathrm{eq}}=\sum_i B_i\exp(-t/\tau_i),
\]

to relate the measured effective relaxation to the finite internal eigen-timescales. The modeled voltage-relaxation amplitude was not used as a quantitative fitting target because the experimental $\Delta E_{\mathrm{relax}}$ can contain conversion, transport, interfacial, and state-dependent thermodynamic contributions beyond the coarse-grained conversion sequence.[23] All calculations are mechanistic-consistency tests; no modeled rate scale is assigned uniquely to ball milling or Mg incorporation. Parameter values and numerical audits are provided in the Supporting Information.

# References

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

**Figure 4. GITT reveals distinct mismatches among accessible reaction extent, relaxation magnitude, relaxation timescale, and conventional apparent diffusivity.** (a) Representative first-lithiation GITT step consisting of a 10 min galvanostatic pulse followed by a 60 min open-circuit rest, defining the 3 s-to-60 min relaxation voltage change, $\Delta E_{\mathrm{relax}}$, and the model-free relaxation timescale, $t_{63}$. (b) State-matched HEO/BM-HEO comparison of $D_{\mathrm{app,BM}}/D_{\mathrm{app,HEO}}$ and the direct relaxation-rate ratio $t_{63,\mathrm{HEO}}/t_{63,\mathrm{BM}}$. Both ratios are oriented so that values above unity indicate faster BM-HEO. The $D_{\mathrm{app}}$ ratio remains above unity at all 37 matched states, whereas the direct relaxation-rate ratio is below unity at 35 of 37 states. (c) Median $\Delta E_{\mathrm{relax}}$ versus median $t_{63}$ over the common 200–800 mAh g⁻¹ interval for all four materials. Mg incorporation decreases the relaxation voltage change while lengthening $t_{63}$. (d) First-cycle delithiation capacity versus median $t_{63}$. Ball milling increases accessible capacity while lengthening $t_{63}$, whereas Mg incorporation decreases accessible capacity while $t_{63}$ increases. Arrows indicate the corresponding material modifications.

**Figure 5. The excess current-off relaxation is localized to the conversion region.** (a) State-resolved relaxation magnitude, $\Delta E_{\mathrm{relax}}$, during the first lithiation as a function of normalized lithiation capacity, $z$. Dashed curves indicate the sample-specific relaxation backgrounds, and the shaded region denotes the common window used to evaluate the excess response. (b) Normalized background-subtracted GITT excess relaxation plotted against rest-end voltage together with the corresponding first-cycle cathodic $dQ/dV$ response for HEO, BM-HEO, Mg-HEO, and BM-Mg-HEO. Dotted lines mark the respective peak voltages. (c) Comparison of the GITT excess-peak voltage, $V_{\mathrm{peak,GITT}}$, with the cathodic $dQ/dV$ peak voltage, $V_{\mathrm{peak},dQ/dV}$. The dashed line represents $V_{\mathrm{peak,GITT}}=V_{\mathrm{peak},dQ/dV}$. The close correspondence between the two peak positions localizes the excess relaxation to the conversion region.

**Figure 6. Step-selective homogeneous conversion kinetics can produce higher cutoff capacity with slower relaxation.** (a) Single-step limiting audit in normalized $Q_{\mathrm{cutoff}}$–$t_{63}$ space. Each of the four effective kinetic steps, $R_1$–$R_4$, is varied independently from 0.1× to 10× while all other kinetic and equilibrium parameters are held fixed. (b) Two-dimensional $R_2$–$R_3$ kinetic-regime map. The solid and dashed boundaries denote $Q_{\mathrm{cutoff}}/Q_0=1$ and $t_{63}/t_{63,0}=1$, respectively; the finite region satisfying both inequalities represents higher cutoff capacity together with slower relaxation. (c) Observable-space projection of the same map with the experimental BM-HEO/HEO and Mg-HEO/HEO ratios overlaid. The experimental points are constraints on the model response and are not microscopic fits. (d) Representative current-off relaxation for the reference model and a point within the higher-capacity/slower-relaxation region ($R_2\times0.465$, $R_3\times50$). The corresponding slowest finite eigenmode increases from 15.35 to 17.68 min while cutoff capacity also increases, illustrating how a slow internal relaxation mode can coexist with greater downstream reaction throughput.
