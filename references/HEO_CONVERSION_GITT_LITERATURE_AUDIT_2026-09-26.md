# Literature Audit — Conventional GITT Apparent Diffusivity in Conversion-Type Anodes

**Date:** 2026-09-26  
**Purpose:** position the HEO TY10 result against prior conversion-anode practice and GITT methodology literature.  
**Scope:** representative, targeted audit rather than a formal systematic review. The wording "all prior studies" is not supported and should not be used.

## 1. Main finding of the audit

A recurring pattern in performance-oriented conversion-anode literature is:

1. calculate a conventional GITT-derived apparent Li-ion diffusion coefficient;
2. compare the magnitude of (D_{\mathrm{Li}}) between materials;
3. interpret the larger (D) as faster Li transport / better reaction kinetics;
4. use that interpretation to rationalize higher rate capability, capacity, or cycling performance.

This pattern is especially common in spinel HEO anode literature. However, methodological literature has long shown that conventional GITT (D) requires restrictive assumptions and can mix transport with finite reaction kinetics, non-ideal thermodynamics, particle-size effects, and phase-transformation dynamics.

The new HEO result adds a direct experimental counterexample: for compositionally identical HEO/BM-HEO, conventional (D_{\mathrm{app}}) ranks BM-HEO as faster at 37/37 state-matched points, while direct current-off relaxation ranks it as slower at 35/37 points.

## 2. Representative HEO / conversion-anode papers using (D) as a kinetic comparator

### A. Tian et al., Rare Metals (2022)
**Title:** High-entropy chemistry stabilizing spinel oxide (CoNiZnXMnLi)3O4 (X = Fe, Cr) for high-performance anode of Li-ion batteries  
**DOI:** 10.1007/s12598-021-01872-4

- Conventional GITT is used to calculate Li-ion diffusion coefficients.
- Average discharge/charge diffusion coefficients are reported.
- The paper explicitly interprets the values as indicating "outstanding charge transport kinetics" and states that the GITT result provides a basis for excellent rate performance.
- This is a direct example of (D_{\mathrm{GITT}}ightarrow) kinetic-performance interpretation.

### B. Low-temperature porous HEO, ACS Applied Materials & Interfaces (2022)
**Title:** Low-Temperature Synthesis of a Porous High-Entropy Transition-Metal Oxide as an Anode for High-Performance Lithium-Ion Batteries  
**DOI:** 10.1021/acsami.2c07576

- Conventional simplified GITT expression is used.
- HEO-450 is reported to have the largest (D_{\mathrm{Li}}) across the charge/discharge process.
- Higher apparent diffusion is attributed to high disorder / improved ionic transport and used together with EIS to explain electrochemical performance.

### C. Xiao et al., ACS Applied Materials & Interfaces (2023)
**Title:** Enhanced Li-Ion Diffusion and Cycling Stability of Ni-Free High-Entropy Spinel Oxide Anodes with High-Concentration Oxygen Vacancies  
**DOI:** 10.1021/acsami.2c12374

- GITT protocol: 100 mA g(^{-1}), 10 min pulse, 60 min rest.
- (D_{\mathrm{Li}}) of (FeCoCrMnZn)3O4 is reported higher than that of (FeCoCrMnMg)3O4.
- The higher (D) is linked to oxygen-vacancy content, higher discharge capacity, and cycling stability.
- This is especially relevant because the protocol is very close to the present HEO experiment.

### D. Zhu et al., Journal of Materials Chemistry A (2024)
**Title:** Rapid in situ growth of high-entropy oxide nanoparticles with reversible spinel structures for efficient Li storage  
**DOI:** 10.1039/D3TA08101J

- GITT-derived (D_{\mathrm{Li}}) is plotted against potential for several HEO compositions.
- Local values near redox plateaus are compared between samples.
- Apparent-diffusivity ordering is compared with calculated migration barriers and used as a transport-kinetics descriptor.
- The authors note composition / Li-content dependence of the prefactor, which is an important caution but still use (D) for ranking.

### E. Zhai et al., RSC Advances (2024)
**Title:** Surface-modified spinel high entropy oxide with hybrid coating-layer for enhanced cycle stability and lithium-ion storage performance  
**DOI:** 10.1039/D4RA06878E

- GITT is used to calculate Li-ion diffusion coefficients for HEO and HEO@LTO/C.
- HEO@LTO/C is reported to have significantly higher (D_{\mathrm{Li}}).
- Higher (D), smaller EIS resistance, and pseudocapacitive contribution are used together to support improved electrochemical dynamics.

### F. Chen et al., Advanced Science (2025/2026 issue)
**Title:** Co-Stabilization of High-Entropy Oxides by Entropy and Polyanionic Units toward High-Capacity Zero-Strain Anodes for Advanced Lithium-Ion Batteries  
**DOI:** 10.1002/advs.202516795

- GITT-derived diffusion coefficients are compared directly between PHEO and HEO.
- PHEO is reported to show higher (D_{\mathrm{Li}}) during lithiation and delithiation.
- The result is used together with EIS and other kinetic analyses to support improved Li transport.

### G. Li-pre-doped HEO, Journal of Energy Storage (2026)
**Title:** Oxygen vacancy engineering via lattice lithium pre-doping enhanced Li-ion diffusion and cycling stability in high-entropy spinel anodes  
**DOI:** 10.1016/j.est.2026.121132

- GITT is used to state that Li-HEO has approximately twice the Li-ion diffusion coefficient of undoped HEO.
- The higher apparent diffusion coefficient is directly connected to improved reaction kinetics and electrochemical performance.

### H. ZnFe2O4 conversion anode, Crystals (2026)
**Title:** In Situ Growth of ZnFe2O4 Nanoparticle Hybridized with rGO for High-Performance Lithium-Ion Battery Anodes

- GITT is explicitly used to "clarify Li+ diffusion kinetics."
- Larger (D_{\mathrm{Li}}) in the rGO hybrid is interpreted as accelerated interfacial charge-transfer / Li insertion-extraction kinetics.
- This shows that the same interpretive practice extends beyond HEOs to conventional conversion oxides.

### I. MoO2 conversion-type anode, Rare Metals (2023)
**Title:** Necklace-like carbon nanofibers encapsulating MoO2 nanospheres with Mo-C bonding for stable lithium-ion storage  
**DOI:** 10.1007/s12598-022-02253-1

- GITT is introduced "to gain insights on electrochemical reaction kinetics."
- The composite's higher diffusion coefficient is explicitly linked to better rate capability.
- Again, (D_{\mathrm{GITT}}) is used as a scalar kinetic comparator.

### J. Co3O4 conversion anode, Sustainability (2023)
**Title:** Synthesis and Electrochemical Properties of Co3O4@Reduced Graphene Oxides Derived from MOF as Anodes for Lithium-Ion Battery Applications

- GITT-derived diffusion coefficients are compared between Co3O4/C and Co3O4/rGO/C.
- Higher (D) is treated as consistent with improved ionic conductivity / electrochemical behavior.

## 3. Important counterexample within recent HEO literature

### Li et al., Angewandte Chemie International Edition (2025)
**Title:** Stabilizing Configurational Entropy in Spinel-type High Entropy Oxides during Discharge-Charge by Overcoming Kinetic Sluggish Diffusion  
**DOI:** 10.1002/anie.202518569

This paper is important because it does **not** simply reduce the conversion kinetics to one conventional (D_{\mathrm{GITT}}).

- GITT polarization / quasi-equilibrium profiles are compared between large and small HEO particles and Fe3O4.
- The insertion stage is discussed in terms of Li diffusion and phase-boundary propagation.
- The conversion stage is explicitly distinguished: the authors state that the conversion-boundary velocity is not governed simply by Li diffusion in the product phase; intrinsic reaction kinetics / oxygen migration also become important.
- DFT/AIMD and structural measurements are combined with GITT.

This paper supports the premise that conversion involves multiple kinetic coordinates, but it does not provide the present state-matched demonstration that conventional apparent (D) can invert the kinetic ranking given by direct relaxation.

## 4. Methodological literature that limits a single-(D) interpretation

### Deiss, Electrochimica Acta (2005)
**Title:** Spurious chemical diffusion coefficients of Li+ in electrode materials evaluated with GITT  
**DOI:** 10.1016/j.electacta.2004.11.042

- Demonstrates theoretically that neglecting finite heterogeneous reaction kinetics can generate spurious potential dependence in GITT-derived (D).
- Even a constant true diffusion coefficient can produce apparent minima near electrochemical peaks.
- Strong precedent for the statement that conventional (D_{\mathrm{GITT}}) can mix reaction kinetics into an apparent transport parameter.

### Zhu & Wang, Journal of Physical Chemistry C (2010)
**Title:** Galvanostatic Intermittent Titration Technique for Phase-Transformation Electrodes  
**DOI:** 10.1021/jp9113333

- Develops phase-transformation GITT because traditional GITT is not sufficient in two-phase regions.
- Separates ion diffusion coefficient from phase-interface mobility.
- Explicitly states that traditional GITT/PITT is reliable in single-phase regions; phase-transforming regions require additional physics.

### Horner et al., ACS Applied Energy Materials (2021)
**Title:** Electrochemical Modeling of GITT Measurements for Improved Solid-State Diffusion Coefficient Evaluation  
**DOI:** 10.1021/acsaem.1c02218

- Identifies restrictive assumptions in common GITT analysis: diffusion timescale vs pulse time, short-time square-root behavior, removal of ohmic/kinetic overpotentials, and ideal-solution/Fickian assumptions.
- Shows that diffusion coefficients obtained from conventional ideal methods can differ greatly from values validated through direct-pulse fitting and independent discharge prediction.
- Particularly useful because even the studied intercalation regime exhibits large analysis-dependent differences; conversion should be treated at least as cautiously.

### Jia et al., Journal of Power Sources (2022)
**Title:** Re-understanding the galvanostatic intermittent titration technique: Pitfalls in evaluation of diffusion coefficients and rational suggestions  
**DOI:** 10.1016/j.jpowsour.2022.231843

- Reviews assumptions, parameter-selection errors, model mismatch, and phase-change limitations in GITT.
- Notes that phase-change / flat-OCV materials can make the standard formula problematic.

### Chien et al., Nature Communications (2023)
**Title:** Rapid determination of solid-state diffusion coefficients in Li-based batteries via intermittent current interruption method  
**DOI:** 10.1038/s41467-023-37989-6

- Derives GITT/ICI from the same semi-infinite diffusion basis.
- Explicitly states that the method inherits assumptions including dominance of solid-state diffusion and a single-phase solid-solution electrode.
- This assumption is directly incompatible with treating a reconstructive multistep conversion region as a simple one-coordinate diffusion problem without additional validation.

## 5. Positioning of the present HEO result

The literature supports a stronger but bounded message:

> Conventional GITT-derived apparent diffusion coefficients are widely used to rank the kinetics of conversion-type anodes, including HEOs, but the underlying GITT assumptions are not generally satisfied during reconstructive multiphase conversion.

The present experiment adds something more direct:

> For the same HEO composition before and after ball milling, conventional (D_{\mathrm{app}}) and an independently extracted current-off relaxation timescale give opposite state-resolved kinetic rankings.

This is stronger than a generic methodological warning because the contradiction is observed experimentally in the same electrode chemistry and same GITT dataset.

## 6. Recommended manuscript wording

### Introduction gap

Avoid:
> Previous studies have incorrectly used GITT diffusion coefficients to analyze conversion kinetics.

Prefer:
> Conventional GITT-derived apparent diffusion coefficients are widely used to compare ion-transport kinetics in conversion-type anodes, including HEOs. Such comparisons implicitly compress the pulse response into a single transport parameter, even though conversion proceeds through coupled charge transfer, structural reconstruction, phase-boundary motion, and species redistribution.

Then:
> Whether the resulting apparent diffusivity preserves the actual fast-slow ordering of a reconstructive conversion electrode has rarely been tested against an independent kinetic observable.

"Rarely" is safer than "never" or "first."

### Results / Discussion

> The present HEO/BM-HEO comparison provides a direct counterexample to a one-dimensional diffusivity ranking: conventional (D_{\mathrm{app}}) is larger for BM-HEO at all 37 matched states, whereas the direct current-off relaxation is slower at 35 of 37 states.

### General implication

Strong but defensible:
> Apparent GITT diffusivity can therefore be useful as an operational transport descriptor, but it should not be interpreted as a standalone measure of overall conversion kinetics.

Stronger version, if retained after final review:
> Conversion kinetics cannot, in general, be ranked by apparent GITT diffusivity alone.

Avoid:
> GITT diffusion coefficients are meaningless in conversion electrodes.
> GITT should not be used for conversion electrodes.
> All previous conversion-anode studies are wrong.

## 7. Novelty boundary

A targeted search did not identify a prior conversion-anode study that performs the same state-matched comparison between conventional GITT (D_{\mathrm{app}}) and an independent current-off relaxation timescale and experimentally demonstrates an inversion of their kinetic ordering.

This is **not** sufficient to claim "first report" without a formal exhaustive search. The manuscript should present the result as a direct experimental demonstration rather than as a priority claim.
