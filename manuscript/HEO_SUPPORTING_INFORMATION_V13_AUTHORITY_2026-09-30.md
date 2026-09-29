# HEO Supporting Information v13 — Current Authority, 2026-09-30

## Status

This file records the current SI scientific/figure authority after the staged non-redundancy audit and v13 Word assembly.

Final conversation export:
`HEO_SI_V13_FinalElectrochem_2026-09-29.docx`

The Word export is not stored in GitHub and does not override this repository state.

## SI design principle

The SI must add controls, robustness, numerical audit, or mechanistic detail not already visible in the main figures. Main panels are not duplicated as standalone SI figures.

## Sections

### S1. Structural/compositional characterization — pending collaborator freeze

Figures S1–S6 remain placeholders only until verified data arrive:
- S1 full XRD/refinement
- S2 additional SEM/TEM + size statistics
- S3 HRTEM/SAED indexing
- S4 EDS maps
- S5 XPS only if retained
- S6 N2 adsorption/BET fit

Do not infer missing values or crystallographic assignments.

### S2. Electrochemical controls and additional performance

- S7 no-FEC cycling control only
- S8 normalized rate retention/recovery only
- S9 cycles 1–3 voltage profiles
- S10 cycle-resolved dQ/dV
- S11 relative interfacial-capacitance audit
- S12 pristine/post-cycle SEM
- S13 full multi-cycle GITT

Main/SI boundaries:
- absolute FEC cycling remains main Figure 3c;
- absolute rate capability remains main Figure 3d;
- S7/S8 are therefore control/normalized-only figures.

### S3. Current-off / conventional-GITT robustness

- S14 four-material 3–30 s E–sqrt(t) audit at approximately 500 mAh g^-1
- S15 t50/t63/t90 robustness
- S16 Dapp versus direct-relaxation disagreement map
- S17 voltage-term decomposition

Key results:
- S14 R2 values: HEO 0.99931, BM 0.99877, Mg 0.99922, BM-Mg 0.99852
- S15 exact raw crossings: t50 ratio 0.7235, t63 ratio 0.7599, t90 ratio 0.8961; BM slower at 34/37, 35/37, 33/37 states
- S16 conflict quadrant: 35/37 states
- S17 median BM/HEO Delta Es ratio 1.8095, Delta Etau ratio 1.1758, Dapp ratio 1.7817

S14 is an operational fit-quality audit. Do not use the Mg-free versus Mg-containing raw-current columns to compare Roff directly because the raw current units differ between source workbooks.

### S4. Conversion-localization/history robustness

- S18 dQ/dV–GITT peak localization with sensitivity bars
- S19 105-condition background/window sensitivity
- S20 cycle-history robustness

Key interpretation:
- nominal peak offsets are <= about 32 mV for all four samples;
- BM-Mg GITT peak location is broad under the audit and should not be assigned a tightly determined unique peak voltage;
- BM peak < HEO and BM width > HEO in 105/105 tested background/window definitions;
- cycle history changes amplitude much more strongly than t63;
- BM retains higher reversible reaction extent with longer t63 after the first cycle.

### S5. Homogeneous four-step microkinetic audit

- S21 full R1–R4 single-step sweeps
- S22 fixed-R2 line cuts through the R2–R3 map
- S23 eigenmode spectrum + partial rates

Key boundaries:
- the four-step model is a mechanistic-consistency/existence proof;
- no unique BM or Mg microscopic rate scales are fitted;
- slowing a single R2 or R3 step alone gives the conventional Q down / t63 up response;
- selective R2/R3 changes create a finite Q up / t63 up region;
- representative R2 x 0.465, R3 x 50 case lengthens the slowest finite eigenmode from 15.35 to 17.68 min;
- at 3 s open circuit, r1+r4 is approximately zero while r2 and r3 remain finite;
- experimental Delta E_relax is not a quantitative model target.

## Numerical authority

See `modeling/si_v13/` for the current S14–S23 summary data.

## Table architecture

Current target numbering remains S1–S17:
- S1 final composition/structural refinement
- S2 XPS only if retained
- S3 BET/particle metrics
- S4 interfacial-capacitance regression
- S5 current-off descriptor summary
- S6 full 37-state HEO/BM GITT audit
- S7 compact conventional-GITT audit statistics
- S8 peak-voltage localization/sensitivity
- S9 105-condition background/window sensitivity
- S10 cycle-history descriptors
- S11 later-cycle background sensitivity
- S12 four-step model parameters
- S13 single-step limiting audit
- S14 R2–R3 regime/line-cut audit
- S15 experimental magnitude boundary
- S16 current-off eigenmodes
- S17 partial rates

Renumber only once at submission freeze if XPS is removed.

## Submission blockers

- insert verified structural S1–S6;
- decide XPS;
- recheck S12 pristine SEM against final main Figure 2;
- insert final methods metadata;
- recover numerical first-cycle profiles if available;
- run final cross-reference/reference/numbering audit.
