# HEO SI v17 — source-evidence audited review text (2026-10-15)

**Status:** Text+table mirror of v17 Word review. Three supplemental images remain embedded only in Word/archived SI v14; their captions are reproduced. This is not submission-ready.

**Source:** `HEO_SI_V17_SourceEvidenceReview_2026-10-15.docx`.

# Supporting Information

GITT Relaxation Fingerprints Resolve Material-Specific Perturbations of Conversion Lithiation in Spinel High-Entropy Oxide Anodes

Stage-origin-focused review draft v17 | Figure 1–2 source audit | 15 October 2026

This source-audited review companion retains the accepted region-charge accounting and supplemental electrochemical context. The Figure 1 HRTEM CoGa₂O₄ index labels conflict with the documented no-Ga Mg-free synthesis; BET area values are transcribed from Figure 2 labels and await original regression verification. Final structural characterization and Mg/electrode methods are pending. SI v14 remains an archived extended version.

## S1. Material characterization — collaborator verification pending

Reported N₂ BET specific surface areas shown in the collaborator Figure 2 are 3.94 (HEO), 18.159 (BM-HEO), 6.49 (Mg-HEO) and 16.64 m² g⁻¹ (BM-Mg-HEO). Milling increases these values in both matched material pairs. Mg-HEO has greater BET area than HEO despite its substantial reduction in late-conversion GITT regional charge, so a simple BET-area shortage alone does not account for the Mg effect. These areas originate from the supplied annotated figure; verify the adsorption raw data and original fitting output before treating them as independently audited numbers. For Figure 1, resolve the collaborator-origin CoGa₂O₄ indexing labels, check XRD and Mg/EDS/ICP specimen identifiers, and verify Mg location rather than inferring lattice substitution from elemental maps.

## S2. GITT measurement definitions and source provenance

The first lithiation was recorded using nominal 100 mA g⁻¹, 600 s pulses and 3600 s rest intervals. Mg-free records were sampled at approximately 1 s intervals and Mg-containing records at approximately 3 s; relaxation comparisons use the common 3 s–60 min window. The 60 min potential is a defined rest-end quantity rather than a verified equilibrium voltage. t63 is the time to complete 63.2% of the measured 3 s–60 min relaxation; ΔErest is its total absolute voltage change. All four original workbooks were independently recovered and inspected. The respective full first-lithiation pulse counts are 65/76/48/56 for HEO/BM-HEO/Mg-HEO/BM-Mg-HEO, and measured negative-current full pulses have approximately 600 s duration. Subsequent short cutoff pulses were not treated as full pulses. Raw source files differ in time resolution and exported layout, so the common post-interruption times are interpolated within each source record.

The accepted R1–R4 segmentation is inherited from the original GITT landmark audit: L1 early transition, L3 central relaxation/voltage landmark and L4 end of the broad rest-end-voltage plateau. Alternative broken-stick knee estimates are exploratory and are not substituted into these reported allocations.

## S3. Original region-charge accounting

Table S1. Original accepted first-lithiation GITT region allocations. Rounded nominal protocol charge (mAh g⁻¹) is followed by the share of each material’s nominal GITT total in parentheses. These entries do not reconstruct GCD capacity.

| Material | R1 | R2 | R3 | R4 | Total nominal |
|---|---|---|---|---|---|
| HEO | 100 (9.2%) | 317 (29.2%) | 517 (47.7%) | 150 (13.8%) | 1083.3 |
| BM-HEO | 150 (11.8%) | 483 (38.2%) | 367 (28.9%) | 267 (21.1%) | 1266.7 |
| Mg-HEO | 100 (12.5%) | 300 (37.5%) | 250 (31.2%) | 150 (18.8%) | 800.0 |
| BM-Mg-HEO | 150 (16.1%) | 433 (46.4%) | 83 (8.9%) | 267 (28.6%) | 933.3 |

Note: The per-region rounded charges in Table S1 derive from 16.6667 mAh g⁻¹ per nominal full pulse; ±1 mAh g⁻¹ differences from exact pulse arithmetic arise from rounding. Inferred original cumulative L1/L3/L4 pulse indices are HEO 6/25/56, BM-HEO 9/38/60, Mg-HEO 6/24/39 and BM-Mg-HEO 9/35/40. These are inferred endpoints from accepted rounded capacities, not directly re-read original boundary markers.

Table S2. Signed contrasts calculated from the original nominal GITT pulse allocations (mAh g⁻¹), with all regional changes summing to Δtotal.

| Comparison | ΔR1 | ΔR2 | ΔR3 | ΔR4 | ΔTotal |
|---|---|---|---|---|---|
| BM-HEO − HEO | +50.0 | +166.7 | −150.0 | +116.7 | +183.3 |
| BM-Mg-HEO − Mg-HEO | +50.0 | +133.3 | −166.7 | +116.7 | +133.3 |
| Mg-HEO − HEO | 0.0 | −16.7 | −266.7 | 0.0 | −283.3 |
| BM-Mg-HEO − BM-HEO | 0.0 | −50.0 | −283.3 | 0.0 | −333.3 |

The phrase “largest positive BM increment” means the largest positive signed ΔR among regions, not necessarily the largest change in absolute magnitude: BM-Mg-HEO − Mg-HEO has ΔR3 = −166.7 mAh g⁻¹. Both Mg contrasts show their largest negative changes in R3.

Table S3. Directional sensitivity outcomes from the previously accepted independent ±1-pulse shift of the L1/L3/L4 assignments. This table summarizes an archived finite sensitivity check, not uncertainty derived from replicate electrochemical cells.

| Audited conclusion | Pass across tested boundary shifts |
|---|---|
| BM: R2 nominal regional increment positive | 100% |
| BM: R1+, R2+, R3−, R4+ nominal pattern | 100% |
| BM: t63 signs R1−, R2+, R3+, R4+ | 100% |
| Mg: R3 most negative nominal regional change | 100% |
| Mg: R3 median t63 change small (≤1.5 min) | 100% |

## S4. Supplemental electrochemical traces and relaxation robustness

Figure S1. Cycles 1–3 galvanostatic voltage profiles for the four related HEO electrodes (adapted from original SI v14 Figure S9). These profiles provide cycling context but are not used to identify a unique microscopic conversion phase.

Figure S2. Original multi-cycle GITT responses for the Mg-free and Mg-containing pairs (reused from original SI v14 Figure S13). Current pulse/rest intervals and the present first-lithiation segmentation are defined independently in Section S2.

Figure S3. Percentile-based relaxation robustness from the original SI v14 Figure S15. The slower observed post-interruption BM recovery is not limited to a particular t63 threshold; the state-matched results do not establish an individual elementary reaction step.

## S5. Interpretational limits and open records

The current voltage-relaxation observables do not uniquely quantify Li diffusivity, conversion-product phase fractions, M–O bond breaking or a Mg-specific local coordination environment. Structural associations are derived from the joint electrochemical segmentation and prior published characterization of related spinel oxides.

The original BM-HEO GITT workbook has now been directly recovered, and the total 76 complete first-lithiation pulses independently agree with the old region partition. However, the exact original L1/L3/L4 boundary-label provenance and its plateau-end marking method have not been independently recovered as signed annotations. Separate pristine-HEO distributed-relaxation EKF analysis remains with the EKF-GITT comparison study, not this materials-paper SI.

Pending before submission: verify Figure 1 HRTEM spinel indexing, Mg stoichiometry/site/composition, original BET fitting/isotherms, XRD/refinement and XPS Cr⁶⁺ sample provenance; complete electrode/cell metadata, historical L1/L3/L4 boundary-marker rationale and final across-four-sample robustness; reconcile captions and publisher-verified references. The cycle 2–3 GITT source data remain available but are not automatically included in the present first-lithiation regional accounting.


> SI Figures S1–S3 are preserved in the Word review proof and older SI v14. The pictures are not embedded in this textual mirror.