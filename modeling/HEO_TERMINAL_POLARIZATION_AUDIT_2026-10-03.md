# HEO first-lithiation terminal-polarization audit — 2026-10-03

## Purpose

Test whether the first-lithiation cutoff is approached because the pulse polarization grows progressively near the end of lithiation.

## Raw sources

The original GITT workbooks were recovered from the 2026-09-17 data package:
- HEO: `HEO GITT 로우 데이터.xlsx`
- BM-HEO: `BM HEO 3 GITT 로우 데이터.xlsx`
- Mg-HEO: `HEO 3 Mg 로우 데이터.xlsx`
- BM-Mg-HEO: `BM HEO 3 Mg 로우 데이터.xlsx`

Program: 600 s current pulse + 3600 s rest; electrochemical window 0.005–2.5 V.

The final partial pulse was excluded from terminal-window comparisons because its duration is shorter than 600 s.

## Definitions

For each first-lithiation pulse:

[
Delta E_{mathrm{inst}}=|E_{3s}-E_{mathrm{rest,prev}}|
]

[
Delta E_{	au}=|E_{mathrm{pulse,end}}-E_{3s}|
]

[
Delta E_{mathrm{total}}=|E_{mathrm{pulse,end}}-E_{mathrm{rest,prev}}|
]

The present audit uses these as operational pulse-voltage excursions. They are not identified as pure charge-transfer overpotential.

## Terminal-window result

Median fixed-duration pulse values:

| sample | z window | dE_inst (mV) | dE_tau (mV) | dE_total (mV) |
|---|---|---:|---:|---:|
| HEO | 0.80–0.90 | 25.23 | 185.61 | 210.84 |
| HEO | 0.90–0.98 | 23.70 | 147.85 | 171.55 |
| BM-HEO | 0.80–0.90 | 22.93 | 139.21 | 162.14 |
| BM-HEO | 0.90–0.98 | 21.02 | 119.26 | 140.28 |
| Mg-HEO | 0.80–0.90 | 16.36 | 136.23 | 152.59 |
| Mg-HEO | 0.90–0.98 | 16.05 | 128.12 | 144.18 |
| BM-Mg-HEO | 0.80–0.90 | 13.38 | 132.10 | 145.48 |
| BM-Mg-HEO | 0.90–0.98 | 13.00 | 119.87 | 132.79 |

All four samples show decreasing, not increasing, pulse-voltage excursion as the first lithiation approaches the cutoff.

Representative HEO:
- near z≈0.84: rest-end voltage ≈0.474 V and pulse-end voltage ≈0.258 V;
- near z≈0.99: rest-end voltage ≈0.168 V and pulse-end voltage ≈0.013 V.

Thus the terminal approach to 0.005 V is dominated by the downward evolution of the baseline/rest voltage rather than an obvious late-stage growth of the pulse excursion.

## Claim boundary

Supported:
- no evidence for a progressively increasing terminal pulse polarization that drives cutoff in these first-lithiation GITT traces;
- a polarization-driven-cutoff explanation should not be used as the main origin of the observed capacity differences.

Not supported:
- polarization is zero or irrelevant;
- the pulse excursion is a unique microscopic overpotential;
- the rest-end voltage is the exact equilibrium voltage.

## Consequence for Figure 6

The four-step model should not be interpreted as explaining experimental capacity through a growing terminal overpotential. Any use of modeled cutoff capacity must be checked for robustness to a realistic separation between the conversion voltage and the 0.005 V cutoff.

Numerical summary:
- `modeling/HEO_TERMINAL_POLARIZATION_SUMMARY_2026-10-03.csv`
