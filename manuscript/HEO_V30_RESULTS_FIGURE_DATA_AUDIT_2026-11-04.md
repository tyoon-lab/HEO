# HEO v30 Results/figures/data audit — 2026-11-04

Status: NON-DESTRUCTIVE PI-review note. The four-paragraph Introduction remains locked; v30 manuscript, working Abstract, and existing figure assets are unchanged. Sources: canonical v30 manuscript; `HEO_SI_V17_SourceEvidenceReview_2026-10-15.docx` (Tables S1–S3 and S2 provenance); archived four-material GITT descriptors; v30 review log.

## 1. Numerical consistency audit (passed)

Nominal GITT protocol: 100 mA g^-1 x 600 s -> 16.6667 mAh g^-1 per complete pulse. Four full-pulse counts 65, 76, 48, 56 correspond to totals 1083.3, 1266.7, 800.0, 933.3 mAh g^-1.

| Sample | R1 | R2 | R3 | R4 | Total | Inferred L1/L3/L4 pulse indices |
|---|---:|---:|---:|---:|---:|---|
| HEO | 100.0 | 316.7 | 516.7 | 150.0 | 1083.3 | 6/25/56 |
| BM-HEO | 150.0 | 483.3 | 366.7 | 266.7 | 1266.7 | 9/38/60 |
| Mg-HEO | 100.0 | 300.0 | 250.0 | 150.0 | 800.0 | 6/24/39 |
| BM-Mg-HEO | 150.0 | 433.3 | 83.3 | 266.7 | 933.3 | 9/35/40 |

| Matched comparison | ΔR1 | ΔR2 | ΔR3 | ΔR4 | Δtotal |
|---|---:|---:|---:|---:|---:|
| BM−HEO | +50.0 | +166.7 | −150.0 | +116.7 | +183.3 |
| BM-Mg−Mg | +50.0 | +133.3 | −166.7 | +116.7 | +133.3 |
| Mg−HEO | 0.0 | −16.7 | −266.7 | 0.0 | −283.3 |
| BM-Mg−BM | 0.0 | −50.0 | −283.3 | 0.0 | −333.3 |

Rounded decimal values may sum with 0.1 discrepancies. **Precise claim:** R2 has the largest *positive signed* milling increment in both matched comparisons. In the Mg-containing pair, the R3 loss (−166.7) is of greater absolute magnitude than the positive R2 gain (+133.3). Therefore avoid "largest overall effect in R2" without signed qualification. Mg's most negative change is R3 in both pairs.

Accepted SI Table S3 reports 100% preservation of core directional statements under its independent ±1-pulse landmark shifts. This is a *finite local sensitivity test*, not cell-to-cell reproducibility or a statistical confidence interval. Inferred pulse endpoints are reconstructed from region counts and should not be represented as newly verified graphical boundary picks.

## 2. Distinguish conventional GCD from GITT nominal charge

| Sample | First-lithiation 0.1-C GCD (mAh/g) | GITT nominal complete-pulse charge (mAh/g) | Difference (GITT−GCD) |
|---|---:|---:|---:|
| HEO | 901.25 | 1083.3 | +182.1 |
| BM-HEO | 1056.10 | 1266.7 | +210.6 |
| Mg-HEO | 731.15 | 800.0 | +68.9 |
| BM-Mg-HEO | 944.07 | 933.3 | −10.7 |

The **direction** of each matched processing/composition effect agrees across the two protocols, but **the magnitude of the signed effect differs substantially**. Figure 3 and Figure 5 axes/captions must explicitly identify GCD versus nominal GITT and avoid treating them as directly interchangeable. Do not describe the nominal GITT result as the actual first-cycle 0.1-C capacity.

## 3. Interpretation audit and paragraph-level recommendation

- **2.1:** BET increase is reliable gas-accessible surface evidence: HEO→BM 3.94→18.159 m²/g; Mg→BM-Mg 6.49→16.64 m²/g. Do not equate BET area with electrochemically active surface. Figure 1 HRTEM `CoGa2O4` notation is an unresolved indexing/provenance issue (Ga absent from declared reagents). Validate Mg bulk composition/site and figure labels before chemical assignment.
- **2.2:** Explicitly state the two paired GCD first-lithiation deltas: milling +154.85 (no Mg) and +212.92 (with Mg); Mg −170.10 (no BM) and −112.03 (with BM) mAh/g. These are *not* the nominal GITT deltas above. Cycling/rate data should not be used to claim the origin of initial capacity differences; verify electrolyte, loading and normalizations.
- **2.3:** L1, L3, L4 are protocol-defined *changes in trends*, not identical extrema of ΔErest/t63 or directly observed phase boundaries. The candidate physical interpretation is R1 early Li uptake/oxide evolution; R2 emerging multi-cation reduction with oxide destabilization/reconstruction; R3 continuing reduction and formation/evolution of metal/Li2O-derived interfaces; R4 post-plateau deep lithiation possibly including interfacial storage. Literature supports *plausibility*, not unique phase assignment to regions. Consider replacing the last 2.3 paragraph's repeated definitions/caveats with a concise explanation of why overlaid reaction processes can alter relaxation: changing voltage–composition slope, heterogeneous evolving reaction zones, and subsequent redistribution/interfacial equilibration. These are physical possible contributors, not a proven one-to-one map.
- **2.4:** The segmentation follows *each sample's own evolving GITT landmarks* rather than equal universal voltage cutoffs. Clearly explain this in Figure 4/5 and Method 4.4, because regional charge shifts include moving landmarks and cannot alone quantify the stoichiometric yield of an individual chemical phase. SI Table S3's ±1-pulse test supports directional robustness near accepted boundaries. Consider reporting a compact matched-pair signed-change table in Fig. 5 or Table S2 (already calculated), and ensure axis includes measurement protocol.
- **2.5:** Claim "milling enhances accessibility in R2" as a literature-supported hypothesis. R3 Mg loss is a measurement; Mg-rich residual oxide, reducible-cation dilution, shifted conversion potential, and polarization are alternative/concurrent interpretations. Mg in pristine powder XPS (even if verified) would not directly prove post-lithiation R3 products. t63 after a pulse is not the unique rate of chemical conversion *during* the pulse.
- **2.6/Conclusion:** Main contribution is **where the signed capacity/charge differences occur**, not identifying four isolated chemical phases or establishing mechanistic causation. Prevent redundant restatements. Consider concise explanatory endpoint: the processing benefit emerges early (R2 positive) but is partially offset later (R3 negative); the Mg-associated deficit is concentrated in later conversion (R3).

## 4. Mandatory evidence/source blockers before submission

1. **Methods 4.1–4.3 still contain many square-bracket placeholders:** Mg precursor/substitution/stoichiometry/calcination; BM-Mg milling conditions; XRD range; ICP digestion; XPS method only if accepted as genuine source evidence; BET fitting/degassing; electrode composition/loading/collector/drying; cell, electrolyte/FEC, electrolyte controls, glovebox, temperature, rate cycle count. These must be verified from original records, not inferred.
2. **XPS source status:** preliminary collaborator 2026-07-30 slide-8 Cr 2p fitting with unverified ~579 eV feature. Do not assert Cr(VI) or mechanism from this; if accepted final matched re-fit becomes available, place powder surface chemistry concisely in 2.1 and fitting in SI. Check whether Section 4.2 should claim XPS characterization at all in a main manuscript excluding unverified XPS interpretations.
3. **Figure 1:** check HRTEM `CoGa2O4` figure label and indexing. Do not quietly replace with conjectural phase.
4. **Figure 3:** confirm FEC concentration, test protocol and basis of normalized rate/cycling comparisons; archived source figure does not replace raw-data provenance.
5. **Figure 4/5 and SI:** reconcile boundary markers with actual plotted traces, all axes and rest-time definitions, Table S1–S3, and verify no implicit uncertainty claim from ±1-pulse test.
6. **Reference and citation sweep:** [22] He, [23] Triolo, [24] Ma, [27] Minouei are v29-aligned. Old v28 duplicate notices are historical; do not revert citation numbers by using those records.

## 5. Recommended immediate manuscript polishing sequence

1. Audit Figure 4/5 labeling and Section 2.3–2.4 physical interpretation, keeping all reported quantitative charges intact.
2. Resolve Methods placeholders using already acquired collaborator/student data; report unavailable fields explicitly as pending rather than fabricate.
3. Check Figures 1–3 source/micrograph references, XPS and Mg composition.
4. Tighten 2.5–2.6/Conclusion for clarity and reduced defensive repetition, then prepare PI review.
5. After substantive full-text review, prepare final Abstract; **do not modify the earlier working Abstract automatically**.

No original manuscript/SI files were modified in this audit.
## 6. Visual figure audit of archived v30 Word (pages 3–9, 10)

- **Figure 1 (page 3):** The four-material microscopy composite is present. Some HRTEM indexed text appears to read `CoGa2O4`; this requires checking source images and collaborator indexing before publication, not just an English caption correction. Small microscopy/SAED labels will require final-resolution QA.
- **Figure 2 (page 4):** Both BET adsorption and the four SEM panels are present. Caption and numerical BET trends are consistent with section 2.1. Re-check source panel arrangement/legends in final layout.
- **Figure 3 (page 5):** **Panel (e) is explicitly a large PLACEHOLDER for matched FEC cycling curves**, so this six-figure Word draft is not yet a complete figure-ready manuscript. First-cycle panel source plots and a reconstructed normalized rate panel (f) are present. **Priority: locate existing FEC cycling raw/export or remove/scope panel (e) after deliberation; do not describe panel (e) as empirical data in polished text until populated.** First-cycle panels (a–d) include 1st–3rd cycles although the caption emphasizes first cycle; clarify exactly what is shown.
- **Figure 4 (page 7):** Figure 4a normalized-charge landmarks visually near 6/65, 25/65, 56/65 of the pristine pulse record. ΔErest decreases strongly early, t63 is **nonmonotonic** (initial fall, secondary rise then central minimum, rise toward late lithiation); avoid describing as monotonic. Fig.4b four materials are plotted on *individually normalized* first-lithiation charge coordinates. Caption should state that curves at the same normalized x are not at the same absolute delivered charge or identical absolute potential.
- **Figure 5 (page 8):** Stacked charge bars and both signed-difference panels exist; the visual R2 positive and Mg R3 negative patterns match Table S2. The measured protocol is explicitly called nominal GITT and there is no claim of statistical confidence.
- **Figure 6 (page 10):** A conceptual schematic is present and correctly signals a plausible R2 access interpretation versus Mg R3 persistent-oxide/redox-window hypothesis. Ensure not to treat schematic as direct chemical-state evidence.
