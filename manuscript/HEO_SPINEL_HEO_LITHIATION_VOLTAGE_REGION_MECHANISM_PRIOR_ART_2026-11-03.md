# Spinel HEO lithiation voltage/capacity regions — focused prior-art audit (2026-11-03)

**Question:** Have prior reports separated the lithiation-voltage/capacity profile of spinel HEO or conversion anodes and assigned mechanisms by electrochemical criteria or state-specific characterization? **YES, including directly in spinel HEO.** This literature is important for the Intro first paragraph and the physical assignment of HEO GITT regions R1–R4. Main v28 and the PI-kept Abstract remain unchanged pending editorial review.

## High-priority direct spinel HEO evidence

### A. Luo et al., Advanced Science 2022 — metal-specific redox over capacity/voltage during first lithiation
- Title: “Charge–Discharge Mechanism of High-Entropy Co-Free Spinel Oxide Toward Li+ Storage Examined Using Operando Quick-Scanning X-Ray Absorption Spectroscopy”
- DOI https://doi.org/10.1002/advs.202201219
- Material (CrMnFeNiCu)3O4 (Co-free, user manuscript contains Co and lacks Cu).
- Operando quick-scanning XAS records each metal K-edge continuously vs *same cell* capacity-voltage profile. **Fig. 6** overlays capacity-specific shifts and voltage, **Fig. 8a** summarizes the lithiation pathway.
- Initial sloping region: Mn2+/3+ → Mn2+ and Cu2+ → Cu0; ~0.5 V plateau: overlapping Mn metalization, Cr3+ → Cr2+, Fe2+/3+ → Fe2+ → Fe0, Ni2+ → Ni0; >~900 mAh/g late capacity: Cr2+ → Cr0 becomes important (roughly capacity 675–1200 mAh/g, not a unique step boundary).
- Strongest cited example for **different dominant reduction processes across a long, overlapping lithiation profile**, but NOT a priori electrochemically segmented four-regime GITT study. Metal sequence **must not be transplanted** to FeCoCrNiMn.

### B. Triolo et al., Small 2023 — fixed voltage states and element-specific ex situ XAS/XRD
- Title: “Charge Storage Mechanism in Electrospun Spinel-Structured High-Entropy (Mn0.2Fe0.2Co0.2Ni0.2Zn0.2)3O4 Oxide Nanofibers as Anode Material for Li-Ion Batteries”
- DOI https://doi.org/10.1002/smll.202304585
- **Fig. 3** samples lithiation endpoints: OCP 3.0 V, 0.9, 0.7, 0.01 V, later delithiation states and second cycle. **Fig. 4** EXAFS local coordination; SI XRD shows at 0.9 V coexisting spinel/rock-salt (approx. 1:2 mass ratio).
- Result: Li insertion, transition-metal cation migration, spinel→rock-salt rearrangement and partially irreversible metal-forming conversion; metals Fe/Co/Ni reduced to different extent, Mn partially and Zn2+ structurally migrates with limited electrochemical reduction.
- Strong direct state-resolved reaction support; cannot infer a universal four-region electrochemical boundary.

### C. Ma et al., Energy Advances 2023 — two voltage-plateau regions with ex situ XRD sampling
- Title: “Understanding the lithiation mechanism of Li2O-doped spinel high-entropy oxides as anode materials for Li-ion batteries”
- DOI https://doi.org/10.1039/D3YA00326D
- Materials base (FeMgNiCrMn)3O4 SHEO and Li2O-doped Li-SHEO, **Co-free and Mg-bearing**.
- **Fig. 4a** two lithiation-voltage plateaus ~0.5–1.0 V and <0.5 V; earlier plateau interpreted as Li insertion/intercalation, later as conversion; CV peaks comparable. **Fig. 5** ex situ XRD in voltage-sampled D1=1.0, D2=0.8, D3=0.5, D4=0.1 V, with charge endpoints, supports early rearrangement. Authors note SHEO without Li addition has weak/absent insertive feature by their structural criteria.
- Important demonstration that **processing/doping can alter prominence/accessibility of a specific lithiation part**, though not GITT rest amplitude/t63 segmentation nor BM/Mg crossed comparison. Interpret the 2-process labels cautiously and avoid direct R1–R4 numeric alignment.

### D. Li et al., Angew. Chem. Int. Ed. 2025, 64, e202518569 — GITT plateau + complete structural validation + size modification
- Title “Stabilizing Configurational Entropy in Spinel-type High Entropy Oxides during Discharge–Charge by Overcoming Kinetic Sluggish Diffusion”
- DOI https://doi.org/10.1002/anie.202518569 ; first online Nov 6 2025
- Large L-HEO primary particles ~150 nm; small S-HEO ~15 nm; difference in specific surface area ~1.4 versus 62.5 m2/g. **Fig. 1g-i:** first-cycle voltage and first lithiation GITT with 5h pulse / 5h rest. L-HEO quasi-rest voltages show ~1.0 V insertion and ~0.6 V conversion plateau; S-HEO ~1.5/~0.75 V corresponding features; overpotential and shapes differ by size.
- **Fig. 2** XRD/7Li MAS NMR/FTIR at distinct states; **Fig. 3** PDF; **Fig. 4** HRTEM; **Fig. 6** phase model: pristine M3O4 (I) → Li_x M3O4 (II) → Li_x M3O4 + (Li2O + metallic phases) (III). Large sample retains partially unconverted intermediate even at 0.01 V while nanosized sample converts more completely; increased interfacial side reactions in small sample. Evidence ties size to kinetics and conversion extent; does **not prove ball milling specifically boosts the user's R2** or define 4 GITT amplitude/time regions.
- Importantly **pre-existing GITT-based HEO insertion-versus-conversion voltage regime assignment**, so do not claim method-first attribution simply from rested GITT voltage.

### E. Jin et al., Materials Today Chemistry 2025 — composition nearest user's parent, but limited voltage-specific evidence
- Title “Unraveling phase transition pathway of spinel (FeCoCrNiMn)3O4 high-entropy oxide anodes for long-life Li-ion batteries”
- DOI https://doi.org/10.1016/j.mtchem.2025.102949
- In situ XRD / ex situ TEM: spinel → spinel/rock-salt coexistence → rock-salt. The accessible published abstract/section snippets **do not establish independently verifiable precise voltage stage boundaries or metal/Li2O amount**; use as composition-matched structural context not proof R2/R3.

## Conversion oxide (non-HEO) methodology precedents

### F. Ng et al., J. Mater. Chem. A 2021 NiO, DOI https://doi.org/10.1039/D0TA09683K
- **Fig. 3:** GITT apparent S²D, apparent exchange current and OCP vs SOC explicitly define 4 regions (I–IV) from changes in **electrochemical parameter trends**.
- I >1 V early interface/SEI, II 0.7–1 V and III 0.5–0.7 V predominantly conversion and evolving interfacial pathways, IV <0.5 V additional strong SEI competition with conversion.
- Most direct **methodological** analogy to trend-defined four regions; they use inferred D and exchange current, **not user's finite-window ΔErest, t63, rest-end voltage** and do not compare a crossed four-material modifier set.

### G. He et al., Nature Communications 2016 Fe3O4, DOI https://doi.org/10.1038/ncomms11441
- In situ TEM + GITT OCV: insertion intermediate can precede/overlap Fe+Li2O conversion, initial low-current plateau obscured by overpotential in ordinary cycling. Spatial coexistence; qualitative relevance to transition-zone rather than exact phase boundary.

### H. Hu et al., ACS Materials Letters 2024 Co3O4, DOI https://doi.org/10.1021/acsmaterialslett.4c00714
- In situ TEM/electron diffraction, theoretical calculation: spinel Co3O4 → rock-salt Li_xCo3O4 → Li2O + Co, local moving reaction fronts.
- Morphology/structure analogue not a quantitatively voltage-mapped HEO study.

## Mechanism confidence versus user's 4 GITT electrochemical regimes
| User GITT region | Prior-art physical associations | Strongest literature | Important limits |
|---|---|---|---|
| R1 early | Initial Li uptake, partly reduction/cation migration before main conversion | Li 2025 GITT ~1 V insertion; Ma 2023 0.5–1 V insertion; Triolo 2023 0.9 V rearrangement | Some early capacity may be SEI/cation metalization; composition-specific |
| R2 onset and progression | Conversion begins, parent spinel destabilizes / rocksalt-like intermediates, metal/Li2O may already form | Li 2025; Triolo 2023; Hu 2024; Luo 2022 | Overlap with R3; no direct user's structural time point |
| R3 continuing conversion | Further reduction of metal centers and growth of metal/Li2O-derived domains | Luo 2022 >900mAh/g late Cr; Li 2025 conversion progression | Can't say specifically Cr, Co, Mn or amount at R3; Mg phase hypothetical |
| R4 post plateau | Additional deep lithiation, nonideal interfacial/SEI process, and residual conversion might continue | Ng 2021 IV SEI competition; Li 2025 side reactions; Luo 2022 late Cr | Avoid assigning all R4 as pure SEI or all conversion completed at L4 |

## Implications for Introduction paragraph 1 and study novelty
- Replace overly implicit reaction-sequence presupposition with **evidence-backed**: prior operando XAS/XRD/NMR studies resolve heterogeneous metal reductions and spinel-to-lithiated-intermediate-to-metal/Li2O chemical progression along lithiation. The mapping is material-dependent and overlapping, not four universal conversion steps. Cite Luo 2022 and Li 2025, optionally Triolo 2023 and Ma 2023.
- Importantly prior GITT in spinel HEO **already distinguishes insertion versus conversion voltage regions** (Li 2025), and prior GITT in NiO **already isolates 4 regions from parameter trends** (Ng 2021). Not novel per se. Unresolved in user's specific experiments is whether different *processing/composition* perturbations (BM vs Mg) change the accessible charge in the *same or distinct* regions of the HEO lithiation response, using ΔErest and t63 as robust characteristic landmarks.
- It is a **literature-guided, not direct proof** to label user's R2 reconstruction and R3 later metalization. If user seeks strong per-region phase identification, would require ex situ/operando XAS/XRD at selected GITT boundaries.
- Comparisons must not transplant absolute voltage/Q boundaries from a material (CrMnFeNiCu or MnFeCoNiZn etc) to user's FeCoCrNiMn, nor imply Li2O begins only after R2 or late response purely conversion.
- Preserve PI-kept Abstract and Main v28 for deliberate wording review, no silent manuscript edits.
