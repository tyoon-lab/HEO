# HEO Manuscript — Microkinetic / Conversion-Mechanism Reference Candidates

**Date:** 2026-09-28  
**Purpose:** verified reference pool for the four-step homogeneous conversion-microkinetic section and later manuscript citation numbering.  
**Status:** bibliographic metadata checked against publisher / PubMed pages where available. Final citation numbering should be assigned only after the main reference list is frozen.

## A. Core mechanistic precedent — highest priority

### A1. Ng et al. — four-step metal-oxide conversion pathway + RDS/electrokinetic analysis
Benjamin Ng, Ehsan Faegh, Saheed Lateef, Stavros G. Karakalos, William E. Mustain,  
“Structure and chemistry of the solid electrolyte interphase (SEI) on a high capacity conversion-based anode: NiO,”  
**Journal of Materials Chemistry A** 2021, **9**, 523–537.  
DOI: **10.1039/D0TA09683K**

**Why this is central for the HEO paper**
- Directly analyzes a conversion-type NiO anode with GITT plus Butler–Volmer / Marcus–Hush–Chidsey electrokinetics.
- Uses effective transfer coefficient to discuss rate-determining steps along the reaction pathway.
- Table 3 gives a four-step generic metal-oxide conversion sequence:
  1. MO + Li+ + e− ⇌ MO–Li+ : first electron transfer (electrochemical)
  2. MO–Li+ ⇌ M+ + LiO− : dissociation (chemical)
  3. Li+ + LiO− ⇌ Li2O : Li2O recombination (chemical)
  4. M+ + e− ⇌ M0 : second electron transfer (electrochemical)
- This sequence is the principal literature basis for the present homogeneous four-effective-step HEO model.
- Use cautiously: it is a mechanistic precedent from NiO, not proof that identical atomistic intermediates are directly observed in the multication HEO.

## B. Direct conversion microkinetic / reaction-network precedents

### B1. Alsaç et al. — explicit conversion-reaction microkinetic modeling
Elif Pınar Alsaç, Arpan Kumar Sharma, Sun Geun Yoon, Bairav S. Vishnugopi, Congcheng Wang, Talia A. Thomas, Douglas Lars Nelson, Udochukwu D. Eze, Won Joon Jeong, John Harris, Partha P. Mukherjee, Matthew T. McDowell,  
“Linking Pressure to Electrochemical Evolution in Solid-State Conversion Cathode Composites,”  
**ACS Applied Materials & Interfaces** 2026, **18**(1), 1626–1640.  
DOI: **10.1021/acsami.5c20956**

**Why relevant**
- Uses mechanistic/electrokinetic modeling for sulfur, FeS2, and FeF3 conversion cathodes.
- Treats conversion as a coupled reaction network with intermediate-species evolution rather than a single scalar kinetic coefficient.
- Useful precedent for calling the HEO model a coarse-grained microkinetic/reaction-network model, while avoiding any “first microkinetic conversion model” claim.

## C. Conversion overpotential / GITT interpretation

### C1. Li et al. — GITT, multiple phases, overpotential, and voltage relaxation limitations
Linsen Li, Ryan Jacobs, Peng Gao, Liyang Gan, Feng Wang, Dane Morgan, Song Jin,  
“Origins of Large Voltage Hysteresis in High-Energy-Density Metal Fluoride Lithium-Ion Battery Conversion Electrodes,”  
**Journal of the American Chemical Society** 2016, **138**(8), 2838–2848.  
DOI: **10.1021/jacs.6b00061**

**Why relevant**
- Combines GITT, in situ XAS/TEM, and DFT for FeF3 conversion.
- Shows sequential multiple-step phase evolution and emphasizes that voltage hysteresis/relaxation contains contributions from ohmic drop, reaction overpotential, mass transport, interfacial penalties, and phase distribution.
- Important support for NOT treating the full experimental ΔE_relax as a pure conversion-microkinetic fitting target.

## D. Conversion nucleation / interfacial transformation precedents

### D1. Evmenenko et al. — interfacial lithiation and nucleation barrier in NiO
Guennadi Evmenenko, Robert E. Warburton, Handan Yildirim, Jeffrey P. Greeley, Timothy T. Fister,  
“Understanding the Role of Overpotentials in Lithium Ion Conversion Reactions: Visualizing the Interface,”  
**ACS Nano** 2019, **13**(7), 7825–7832.  
DOI: **10.1021/acsnano.9b02007**

**Why relevant**
- Operando X-ray reflectivity identifies interfacial Li accumulation and interfacial lithiation before bulk NiO conversion.
- DFT-based nucleation analysis shows that conversion overpotential is tied to interfacial/nucleation energetics.
- Supports separating local reconstruction/nucleation processes from a single lumped “conversion rate.”

### D2. Lin et al. — phase evolution and heterogeneous nucleation in NiO
Feng Lin, Dennis Nordlund, Tsu-Chien Weng, Ye Zhu, Chunmei Ban, Ryan M. Richards, Huolin L. Xin,  
“Phase evolution for conversion reaction electrodes in lithium-ion batteries,”  
**Nature Communications** 2014, **5**, 3358.  
DOI: **10.1038/ncomms4358**

**Why relevant**
- Direct 3D/spectroscopic visualization of NiO conversion phase evolution.
- Shows nucleation/propagation from multiple locations and identifies grain boundaries as favorable nucleation sites.
- Useful background for the physical complexity of conversion, but the present main model should remain homogeneous and should not invoke spatial heterogeneity unless needed.

---

# Recommended manuscript use

1. **Primary mechanistic citation for the four-step model:** Ng et al., DOI 10.1039/D0TA09683K.
2. **Primary precedent for conversion reaction-network/microkinetic modeling:** Alsaç et al., DOI 10.1021/acsami.5c20956.
3. **Primary support for bounded interpretation of GITT voltage relaxation / ΔE_relax:** Li et al., DOI 10.1021/jacs.6b00061.
4. **Background support for reconstruction/nucleation/interfacial complexity:** Evmenenko et al. and Lin et al.

# Current four-step HEO modeling interpretation

Use as a **literature-grounded coarse-grained four-effective-step sequence**, not as an experimentally proven atomistic HEO pathway:

[
O \rightleftharpoons I \rightleftharpoons J \rightleftharpoons K \rightleftharpoons C
]

- **R1:** initial lithiation / first electron transfer (electrochemical)
- **R2:** effective M–O dissociation / local structural reconstruction (chemical)
- **R3:** effective Li2O-forming/product-side reconstruction (chemical)
- **R4:** second electron transfer / metal reduction (electrochemical)

For HEO, (M) denotes an effective local metal–oxygen unit. Do not claim that (M^+), LiO−, or any one intermediate phase has been directly identified in the present electrode.

# Claim boundary

The model is intended to test whether a homogeneous multistep conversion network can produce different ordering of accessible reaction extent and post-interruption relaxation speed. It is not intended to fit atomistic rate constants, identify a unique RDS in the HEO, or reproduce the full experimental relaxation magnitude.
