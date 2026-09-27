# HEO Figure 3 Source Provenance Audit — 2026-09-27

**Purpose:** freeze what is currently known about the numerical/graphical sources underlying the Figure 3 conventional electrochemistry panels.

## Current conclusion

Figure 3 panel logic is scientifically frozen, but **full artwork reproducibility is not yet closed** because the latest conventional cycling/rate plots are available as embedded Origin objects rather than as a separately archived raw numerical source.

Do not reconstruct publication curves from approximate visual digitization while the original acquisition files may still be recoverable.

## Current latest electrochemistry deck

Latest working source inspected:

`HEO 진행상황 (20260917).pptx`

The deck contains the relevant conventional electrochemistry on slides 9–10.

### Slide 9 — cycleability/rate information

The PPTX package contains embedded Origin OLE objects rather than native PowerPoint charts or embedded Excel workbooks.

Recovered object-level content shows:

- `oleObject4.bin`: four-material FEC cycling plot with specific capacity and Coulombic-efficiency labels;
- `oleObject5.bin`: additional cycling/control plot retained in the working deck;
- `oleObject6.bin`: four-material **absolute specific-capacity rate** plot;
- `oleObject7.bin`: four-material **normalized specific-capacity ratio** plot.

The Origin objects explicitly contain dataset labels corresponding to HEO, BM-HEO, Mg-HEO, and BM-Mg-HEO.

Main-manuscript allocation:
- absolute 0.1 C cycling → Figure 3(c);
- absolute rate capability → Figure 3(d);
- Coulombic-efficiency evolution/control cycling → SI;
- normalized rate retention → SI.

### Slide 10 — voltage-profile / dQ/dV information

The slide contains eight embedded Origin OLE objects.

Object inspection separates them into:
- four voltage-profile objects;
- four cycle-resolved dQ/dV objects.

Main-manuscript allocation:
- first-cycle voltage profiles → Figure 3(a);
- first-cycle cathodic dQ/dV → Figure 5 conversion-localization panel;
- cycle-resolved dQ/dV → SI.

## First-cycle profile version warning

A May 8, 2026 collaborator-transfer email explicitly noted that an earlier first-cycle specific-capacity/voltage-profile dataset contained an interruption artifact associated with a campus power outage and measurement restart.

Therefore:
- the May 8 profile should **not** be treated automatically as the final Figure 3(a) authority;
- the current September working deck / manuscript-facing profile should be used unless a cleaner raw acquisition file is recovered;
- final Figure 3(a) provenance must identify the exact acquisition file used.

## Raw-file search result

### Project Drive

The current HEO `Data` folder contains the GITT source workbook:
- `[GITT try 2_031].xlsx`

It does not currently contain the conventional four-material cycling/rate raw files used for Figure 3.

### Email audit

The September 17 HEO-data email contains:
- `HEO 3 Mg 로우 데이터.xlsx`
- `BM HEO 3 Mg 로우 데이터.xlsx`

Inspection shows these are **Mg-containing GITT raw datasets**, not the conventional Figure 3 cycling/rate datasets.

Searches for separate HEO/BM-HEO conventional `.xlsx` or `.wrd` raw files in the relevant HEO email history did not recover a matching source.

Historical electrochemistry was commonly shared as PowerPoint/Origin artwork rather than as the raw acquisition files.

## What is already numerically frozen

The first-cycle half-cycle summary used in Main v12 is:

| Sample | First half-cycle (mAh g^-1) | Second half-cycle (mAh g^-1) | ICE (%) |
|---|---:|---:|---:|
| HEO | 901.25 | 609.12 | 67.59 |
| BM-HEO | 1056.10 | 782.08 | 74.05 |
| Mg-HEO | 731.15 | 458.91 | 62.77 |
| BM-Mg-HEO | 944.07 | 580.83 | 61.52 |

These values are consistent with the current manuscript/SI summary and can support Figure 3(b).

Until the WonATech convention is explicitly verified, retain neutral **first-half-cycle / second-half-cycle** wording.

## Remaining provenance blockers before publication-quality redraw

1. Recover the exact raw acquisition/source files for the four-material first-cycle voltage profiles if available.
2. Recover the raw cycle-by-cycle capacity table/source for the common 0.1 C FEC cycling comparison.
3. Recover the raw rate-capability source and verify:
   - exact C-rate sequence;
   - number of cycles at each rate;
   - return-to-0.1-C segment;
   - capacity basis used to define 1 C.
4. Confirm that all four curves in the chosen Figure 3(c,d) sources use the same intended electrolyte condition.
5. Export/commit compact numerical tables and a reproducible Figure 3 plotting script after the raw source is frozen.

## Submission policy

Until those raw files are recovered, the embedded Origin objects can serve as **traceable working graphical sources**, but they should not be treated as the final reproducible numerical authority.

The scientific conclusion supported by Figure 3 does not depend on resolving a microscopic kinetic parameter:

**BM increases accessible capacity, Mg decreases accessible capacity, and capacity alone is not used to infer intrinsic conversion speed.**
