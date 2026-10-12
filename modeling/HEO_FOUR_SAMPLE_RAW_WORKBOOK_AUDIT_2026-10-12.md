# All four first-lithiation HEO GITT workbooks — direct source audit, 2026-10-12

## Status and scope
**New:** the previously unavailable `BM HEO 3 GITT 로우 데이터.xlsx` original was recovered via collaborator-shared document access. Full first-lithiation raw GITT data from all four specimens were directly inspected on 2026-10-12. The direct pulse-count check closes the previous BM-workbook availability blocker but does **not** independently recover signed historical L1/L3/L4 segmentation annotations. Original accepted region fractions are unchanged. This is a source-file validation, not a new segmentation algorithm or reanalysis of GCD capacity.

## Source data
| Sample | Original source workbook | Sampling | Negative-current full pulses (first lithiation) | Non-full terminal pulse identified | Accepted nominal region pulse counts R1/R2/R3/R4 |
|---|---|---:|---:|---|---|
| HEO | `[GITT try 2_031].xlsx` (project source record; original HEO GITT workbook separately archived) | ~1 s | **65** | none in the audited first 65 | 6/19/31/9 |
| BM-HEO | `BM HEO 3 GITT 로우 데이터.xlsx` | ~1 s | **76** | subsequent negative pulse about 426 s; excluded | 9/29/22/16 |
| Mg-HEO | `HEO 3 Mg 로우 데이터.xlsx` | ~3 s | **48** | subsequent negative cutoff pulse; excluded | 6/18/15/9 |
| BM-Mg-HEO | `BM HEO 3 Mg 로우 데이터.xlsx` | ~3 s | **56** | subsequent negative cutoff pulse; excluded | 9/26/5/16 |

Absolute currents in the source files are about 0.17–0.21 mA depending on electrode active loading. The nominal normalized step current remains 100 mA g⁻¹ and the first-lithiation full step duration is approximately 600 s. The pulse-start spacing is ~4200 s, consistent with 600 s current + 3600 s rest. Gmail collaborator correspondence separately corrected the historical mistaken 60-second annotation to a 60-**minute** rest.

## Parsing and checks
- Two source workbook families have different XML/storage layouts. Mg-free first-lithiation source was read from the stored spreadsheet numeric/sample-index columns. Mg-containing workbook time is exported as elapsed `day:hour:minute:second.millisecond` text, not directly numeric.
- For each source, identify contiguous negative-current runs lasting about 600 s, followed by zero-current rest of about 3600 s. Exclude subsequent partial cutoff steps.
- Extract at least 3 s–3600 s of voltage recovery. Use the same shared 3 s reference across 1 s and 3 s sampling. The data support operational t63 and ΔErest; these are not phase-specific microscopic constants.
- Raw complete pulse totals are **65, 76, 48, 56**; these exactly match the arithmetic totals previously inferred from the accepted rounded four-sample original region-capacity table.
- With nominal `100 mA g⁻¹ × 600 s = 16.6667 mAh g⁻¹ per full pulse`, inferred total protocol charges are approximately HEO 1083.3, BM 1266.7, Mg 800.0 and BM-Mg 933.3 mAh g⁻¹. These values are deliberately distinguished from independently measured GCD first-lithiation capacities.

## Accepted boundary neighborhoods, **not newly measured boundaries**
Original working cumulative pulse endpoints inferred from accepted **rounded region-capacity partition** remain:
- HEO L1/L3/L4 = 6/25/56;
- BM-HEO = 9/38/60;
- Mg-HEO = 6/24/39;
- BM-Mg-HEO = 9/35/40.

At those original candidate landmark pulses, directly interpolated 60-min rest-end voltages from source workbooks are approximately:
- HEO L3 #25 0.6473 V, L4 #56 0.4315 V;
- BM-HEO L3 #38 0.7145 V, L4 #60 0.4718 V;
- Mg-HEO L3 #24 0.5154 V, L4 #39 0.3674 V;
- BM-Mg-HEO L3 #35 0.5292 V, L4 #40 0.4532 V.

These values confirm actual observations at the *working* indices but do not prove that those indices follow from a unique automated plateau-knee algorithm. A small range of plausible L4 positions must continue to be acknowledged. Do not silently import experimental broken-stick estimates in place of originally agreed region counts.

## Consequences for 2026-10-12 versioning
- Manuscript and SI review outputs advanced to `HEO_Manuscript_V24_RawVerified_2026-10-12.docx` and `HEO_SI_V16_RawVerified_Focused_Review_2026-10-12.docx`, both session artifacts, not GitHub binaries.
- The fixed PI-approved Abstract is unchanged.
- Methods now explicitly mention the four directly verified complete pulse counts and preserve the distinction between source verification and historical segmentation-marker provenance.
- Collaborator-supplied `Method and characterization_HEO (1).docx` contains a specific precursor/calcination/milling recipe **for the Mg-free parent** and instrument model names; those have been transferred cautiously as provisional source-backed Method text. It does NOT justify the Mg synthesis recipe, BM-Mg recipe, Mg site, final electrode metadata, or an asserted degree of amorphization.
- Region Table S1, signed contrasts Table S2 and ±1-pulse sensitivity Table S3 remain, with GITT-protocol values distinguished from GCD capacity.
- The separate pristine HEO EKF-GITT exploratory spectrum remains **excluded** from Main/SI, per the previous v23 go/no-go decision.

## Remaining genuine issues
1. Obtain signed final Mg-containing synthesis and compositional analysis and missing complete electrode/cell metadata; collaborator method draft is not final authorization.
2. If available, source the **original manual L1/L3/L4 label convention/plot code** and document a single defensible L4 plateau-end criterion across all four before submission. Raw pulse counts alone do not retrospectively prove the exact indices or the physics.
3. Confirm XRD/SEM/TEM/EDS/BET and all Figure1–2 claims and caption attribution.
4. Full 20-reference publisher metadata and per-claim support audit.
5. Revisit any accepted L1/L3/L4 location only if new independent evidence materially changes the actual dominant R2/R3 regional interpretation; do not silently replace accepted historical capacities.
