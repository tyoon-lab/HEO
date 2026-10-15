# HEO — Figure 1–2 primary-art audit and mechanism evidence gate (2026-10-15)

**Status:** Scientific source review and **proposed wording only**. Not a newly analyzed XRD/Rietveld, BET fitting or confirmed microscopic conversion-product analysis. Do not imply this note was merged into v25 Word or that Figure 1 was corrected. The HEO Manuscript v25 and Figure1–2 art stay as archived working artifacts pending collaborator correction.

## Actual sources inspected

1. Six-image Main source: `HEO_Manuscript_V25_DominantStageMechanism_2026-10-15.docx` (embedded `/word/media/image1.png` = Figure 1, `image2.png` = Figure 2), generated 2026-10-15; current GitHub full-text mirror: [v25 Main](HEO_MANUSCRIPT_V25_STAGE_MECHANISM_INTEGRATED_2026-10-15.md).
2. **Collaborator source slide deck:** `HEO 진행상황 (20260917).pptx`, in project Drive [HEO preparation folder](https://drive.google.com/drive/folders/1XDR9lDWPqqMHbzTey0hReALhABgqpCs3). Its original TEM HEO/BM/Mg/BM-Mg slides **already label HRTEM reflections “CoGa2O4”**; this did not first arise during Word editing. Slide SEM mapping: (a) HEO, (b) BM-HEO, (c) Mg-HEO, (d) BM-Mg-HEO.
3. `Method and characterization_HEO (1).docx` (2026-09-17 original collaborator email): Mg-free five-metal **Ni/Fe/Co/Mn/Cr** chloride precursor route, BM recipe and instrument list. **No Ga precursor** appears; **no verified Mg recipe or site** appears.
4. 2026-07-30 collaborator communication and 2026-09-17 slide source state that the new XPS Cr6+ (~579 eV) signal in a recently synthesized sample is atypical relative to earlier samples and that follow-up Mg-sample XPS/refitting is needed. It is not a validated composition-independent trend.

## Figure 2: quantitatively extractable *printed* BET numbers

**These values are visually read from the labels on Figure 2 (and derived from original collaborator slide artwork), not independently refitted from N2 adsorption raw data.**

| Sample | Reported BET specific surface area (m²/g) | Compared with untreated corresponding composition |
|---|---:|---|
| HEO | **3.94** | baseline |
| BM-HEO | **18.159** | higher after milling |
| Mg-HEO | **6.49** | baseline for Mg series |
| BM-Mg-HEO | **16.64** | higher after milling |

Interpretation:
- Both matched milling pairs show increased **gas-accessible specific surface area**; this independently corroborates a material physical perturbation relevant to greater reaction accessibility, but does **not** measure oxide-reconstruction yield, Li-ion diffusivity, true electrochemical reactive area, or charge specifically associated with R2.
- In the Mg-free pair, HEO → Mg-HEO increases BET **3.94 → 6.49** while nominal GITT R3 contribution strongly decreases. Therefore, a **simple lack of BET surface area** is inadequate to explain Mg's R3 decrease in this pair.
- Mg also strongly decreases R3 in the milled pair, where BET is 18.159 (BM-HEO) vs 16.64 (BM-Mg-HEO). Modest BET difference alone does not mechanistically identify R3 conversion suppression or rule out electrode-level factors.
- The original `Va / cm³(STP) g⁻¹` vs approximate relative-pressure adsorption curve is **not itself a BET-fit plot**; before publication verify full adsorption/desorption source, linear BET fitting interval, consistency and uncertainty/replicate values, units and legend. Do not infer pore dimensions or surface area directly from the plotted endpoint.

## Figure 1: microscopy and critical indexing gate

- TEM/HRTEM, SAED and EDS map panels exist for all four materials. Mg maps **qualitatively show Mg signal** in Mg-HEO and BM-Mg-HEO, but these are not quantified bulk incorporation, spinel lattice occupancy or equal-Mg loading measurements.
- The HRTEM figure labels multiple reflections **“CoGa₂O₄ (311)/(400)/(440)/(511)”**, **while the actual parent preparation includes no Ga precursor**. The collaborator's original 2026-09-17 TEM slides also contain these exact labels. Ask whether CoGa₂O₄ was an *isostructural PDF/indexing reference*, a copied presentation label, or reflects specimen-identity confusion. **Do not replace the labels blindly with a declared new phase**, and do not report experimental formation of CoGa₂O₄ without elemental evidence. Correct annotations only after crystallographic indexing against the actual Ni/Fe/Co/Mn/Cr/(Mg) spinel samples.
- The SAED reported spinel-like d spacings plausibly support a spinel lattice family, but do not independently establish identical phase composition, a single-phase high-entropy solid solution, or quantitative structural stability.
- Four-panel TEM/SEM fields reveal heterogeneous primary grains and agglomerates. The **source slide's post-electrode BSE mean particle/agglomerate sizes (n≥20)** are HEO **1.95 μm**, BM-HEO **2.12 μm**, Mg-HEO **1.93 μm**, BM-Mg-HEO **1.99 μm**. They do **not** show smaller electrode-scale aggregates after BM. This is a different size metric from visible nanoscale primary particles; avoid unconditional statements “ball milling reduces particle size” based only on the images. Particle size-distribution measurements need to specify primary crystallite vs secondary aggregate and the measurement context.
- Figure 1 panel artwork also mixes CoGa2O4-specific labels, generic spinel Miller indices and EDS elemental maps; check indexed reflection table + XRD pattern before finalizing caption or Section 2.1.

## Other original structural/electrochemical supporting metadata

- The original September slide lists exploratory ECSA-like values for HEO / BM / Mg / BM-Mg as **4.18 / 30.17 / 6.56 / 39.68 cm²**, with `Cs = 40 μF/cm` printed (dimension not written as cm²) and CV window **3.0–3.3 V**. These must NOT yet be used as a calibrated electrochemically active area in the new Main text without raw non-Faradaic CV slopes, correct capacitance units, geometric electrode normalization, confirmation of cell potential scale/window relative to the manuscript 0.005–2.5 V and the reference-source citation.
- The original 2026-09-17 deck has “60-second rest” text for GITT, BUT the author's same-day follow-up explicitly corrected the protocol to **10-min current on/60-min rest**, and raw workbook pulse timing independently supports 600-s/3600-s. Keep the corrected values only in Methods.

## Mechanistic interpretation warranted by this evidence

**BM → R2 (stronger conditional support):** Two matched pairs demonstrate increased BET after milling. This directly supports **greater gas-accessible surface and potentially increased interfacial exposure**, compatible with—but not proof of—the enlarged R2 nominal GITT charge. R2→R4 prolonged t63 is an observed electrical response, not proof that defect density or diffusion resistance increases. Prefer surface/contact accessibility as the evidence-tied mechanism; present defect introduction, particle refinement, oxide destabilization **as further hypotheses pending independent XRD/TEM quantitative evidence**.

**Mg → R3 (electrochemical localization strong; structural origin open):** Mg EDS maps and stage-dependent signed nominal charge support an Mg-bearing material with a larger negative R3 regional change. In the untreated matched pair, BET increases rather than decreases with Mg; therefore **surface area shortage by itself cannot account for the effect**. Plausible explanations include altered redox-active transition-metal inventory, changed local oxygen/cation coordination, or later-conversion reaction energetics/accessible voltage window. Bulk Mg concentration, phase purity, lattice occupancy and chemical conversion products are **unconfirmed**. Prefer wording like “consistent with a modification of accessible late-conversion reaction states rather than uniform surface-area limitation”; never assert specific Mg–O stabilization, lowered metal/Li2O yield, or cation site without evidence.

### Insert-ready Section 2.1 paragraph (provisional, based on printed Figure2 values)

> The microscopy and adsorption data establish distinguishable material responses to milling and Mg incorporation (Figures 1 and 2). The reported BET specific surface area increases from 3.94 to 18.159 m² g⁻¹ for HEO and BM-HEO, respectively, and from 6.49 to 16.64 m² g⁻¹ for Mg-HEO and BM-Mg-HEO. Thus, milling increases the gas-accessible surface area in both compositions. TEM/SAED and elemental mapping indicate spinel-like diffraction features and an Mg signal in the Mg-containing samples; the specific lattice indexing, phase identity and quantitative Mg content remain subject to verification. These observations support changes in accessible surface and particle morphology but do not independently establish which conversion products are formed at the later lithiation stages.

### Insert-ready Section 2.4 qualification (after milling paragraph)

> The greater BET surface area in both milled materials is compatible with a larger area of oxide accessible to electrolyte-mediated charge transfer during conversion onset. The increase in R2 capacity nevertheless cannot be ascribed uniquely to interfacial area, because mechanical processing can also alter disorder, connectivity and the distribution of reconstructed reaction environments. The longer observed post-pulse t63 after milling indicates that improved charge accessibility and slower measured voltage recovery can coexist.

### Insert-ready Section 2.5 qualification (after Mg paragraph)

> Notably, Mg-HEO exhibits a larger BET specific surface area than untreated HEO (6.49 versus 3.94 m² g⁻¹), despite the pronounced reduction in its R3 GITT charge. The dominant late-conversion loss is therefore difficult to explain by a simple reduction in accessible surface area. The response is more consistent with modification of the redox-active inventory or the accessibility/energetics of later conversion states, although direct assignment of this effect to Mg-dependent oxide stability requires additional structural and chemical evidence.

## Actions before next Word integration

1. **Urgent, Fig. 1:** obtain confirmed HRTEM/SAED indexing and exact reason for “CoGa₂O₄”; cross-check 5-metal spinel XRD and actual raw reference cards. If this is a reference spinel, label it as *reference used for indexing*, not as the isolated product phase.
2. **Fig. 2:** request original N₂ adsorption/isotherm and BET regression output and sample-by-sample SEM labels/primary vs aggregate-size quantification.
3. **Mg:** obtain actual Mg precursor recipe, ICP measured metal ratios, Mg-site or structural inference evidence, and XPS replacement dataset avoiding anomalous Cr6+ provenance.
4. **ECSA and BSE:** verify the original electrode BSE particle sizes/definition and recalibrate ECSA method before using those numbers to claim reactive electrochemical area or particle refinement.
5. **Only then** merge numerical characterization prose into the v25 integrated full Main and Word; do not overwrite the v25 main body by assuming these **figure-printed values** are final collaborator-certified. Preserve the BM R2 / Mg R3 electrochemical mapping and first-lithiation provenance.

**Publication claim gate:** At present there is useful empirical support for milling-related surface accessibility and a meaningful argument against Mg acting solely through reduced BET surface area, **not direct evidence for a particular oxide reconstruction pathway or metal/Li₂O conversion yield in R2/R3.** The full physical discussion remains partly hypothesized rather than independently proven.
