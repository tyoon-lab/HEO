# HEO current artifacts — 2026-09-20

## Authority order

1. Scientific/text authority: `manuscript/HEO_MANUSCRIPT_V4_AFM_CONVERSION_2026-09-20.md`
2. SI authority: `manuscript/HEO_SUPPORTING_INFORMATION_V2_CONVERSION_ALIGNED_2026-09-20.md`
3. Figure architecture authority: `manuscript/HEO_FIGURE_ARCHITECTURE_AND_CAPTIONS_V2_CONVERSION_2026-09-20.md`
4. Conversion-assignment data note: `FIGURE4_CONVERSION_ASSIGNMENT_CHECK_2026-09-20.md`
5. Numerical peak table: `manuscript/HEO_FIGURE4_LATEST_PPT_DQDV_GITT_PEAK_CHECK_2026-09-20.csv`

The Word file and review PNGs listed below are exports/development artifacts. They do not override the Markdown scientific authority.

## Final review Word export

File name:
`HEO_AFM_FinalDraft_ConversionCentered_2026-09-20.docx`

Purpose:
- sentence-by-sentence AFM manuscript review;
- contains Figures 1–5 in review form;
- 16-page rendered QA completed on 2026-09-20;
- line numbering enabled.

SHA256:
`a11c6af6386a944a446a8274725a33cb8ab38d636db8bcb371d3242d84a75f34`

Important:
- Figure 1 remains a collaborator-data placeholder/review summary.
- Figure 4 panel (a) remains a deliberate placeholder until the final state-resolved raw relaxation panel is frozen.
- Yellow-highlighted notes mark unresolved metadata/source items.
- This binary export is not currently stored in the repository; regenerate from the authoritative Markdown and current figure assets if needed.

## Figure 4 review composite

File name:
`HEO_Figure4_conversion_centered_4panel_review.png`

Purpose:
- development/review visualization of the compact four-panel Figure 4 architecture;
- panel (a): explicit placeholder for final state-resolved relaxation curves;
- panel (b): four-sample first-cycle dQ/dV versus GITT excess-peak comparison;
- panel (c): dQ/dV versus GITT peak-voltage correspondence;
- panel (d): excess peak-amplitude / width / area map.

SHA256:
`0ee3d3c7ebadbe4fa9d87d160bc262c21da63aa643c06f75dd38840224be5d09`

This is a review composite, not final publication artwork.

## Figure 5 review composite

File name:
`HEO_Figure5_conversion_centered_v6.png`

Purpose:
- conversion-centered review version of Figure 5;
- panel (a): mechanism-sufficiency logic;
- panel (b): 4 × 7 pulse-end radial effective conversion-state maps;
- panel (c): pulse-end mean internal state versus model mean lithiation state.

SHA256:
`f2ab2ad639c667c3e5756b6a2999e0a7dbcfa74c684eeb1b960ce892e9f561d1`

This review composite preserves the frozen-v4 model results. The model was not refitted after the conversion reassignment.

## Figure 4 numerical source

Repository CSV:
`manuscript/HEO_FIGURE4_LATEST_PPT_DQDV_GITT_PEAK_CHECK_2026-09-20.csv`

Current values:

| Sample | dQ/dV peak (V) | GITT excess peak (V) |
|---|---:|---:|
| HEO | 0.544575 | 0.527 |
| BM-HEO | 0.589146 | 0.618 |
| Mg-HEO | 0.418819 | 0.387 |
| BM-Mg-HEO | 0.484822 | 0.503 |

All peak pairs differ by no more than 32 mV.

## Source boundary

The latest four-sample continuous first-cycle numerical GCD files are not currently available. The present dQ/dV values were reconstructed from the user's own vector voltage-profile artwork in the 2026-09-17 progress presentation. The older first-cycle dataset affected by a power interruption is excluded from the conversion assignment. If the original numerical continuous profiles are recovered, they should replace the reconstructed source before submission.
