# HEO PI Comment Resolution — 2026-09-30

Source reviewed:
`HEO_Main_V16_ReferenceAudited_Tracked_2026-09-28(1).docx`

Total PI comments: **55 (IDs 0–54)**.

Purpose:
- preserve the agreed action for every comment group;
- retain the original Word comments in the final commented DOCX;
- append reply text to the original comments during the final Word assembly.

The fully integrated manuscript authority is:
`manuscript/HEO_MANUSCRIPT_V17_PI_COMMENTS_INTEGRATED_2026-09-30.md`

## Comments 0–4 — Introduction logic

- Recast accessible capacity, Delta E_relax, and characteristic relaxation time as complementary observables for studying the relation between accessible reaction extent and conversion kinetics.
- Do not introduce the specific “capacity up / slower relaxation” result too early.
- Delete “literature-grounded” wording in the Introduction.
- End the Introduction by stating that the experiments reveal non-conventional capacity–relaxation relations and the four-step model explains how such relations can arise in a multistep conversion reaction.

## Comments 5–15 — Figure 4 and Section 2.3

- Keep the representative GITT step in main Figure 4a; retain full multi-cycle GITT in SI Figure S13.
- Remove “model-free” from the Figure 4 caption.
- Add all-four state-resolved t63 versus normalized lithiation state to the SI; Delta E_relax state dependence is already shown in main Figure 5.
- Use “pristine HEO” at the requested locations.
- Remove 37/37 and 35/37 count repetition from main prose; keep detailed counts in the SI.
- State the Dapp/t63 conflict directly: conventional Dapp ranks BM-HEO faster, whereas t63 shows slower BM-HEO relaxation.
- Replace “consequential” with direct wording.
- Prefer GITT relaxation / voltage relaxation / after current interruption over repeated “current-off response.”
- Replace the old Mg “constraint” interpretation with the revised z = 0.40–0.90 result:
  - capacity decreases;
  - Delta E_relax decreases strongly;
  - t63 remains nearly unchanged.

## Comments 16–19 — Figure 4 closing paragraph / SI role

- Remove obsolete wording tied to the former Mg interpretation.
- Keep the key statement that Dapp cannot be assumed to represent the overall relaxation rate.
- Replace vague “voltage terms” with explicit Delta Es and Delta Etau interpretation in the SI.
- Remove the unclear full-pulse square-root-time claim.
- State directly that SI Figures S15–S17 provide t50/t63/t90 robustness and conventional-GITT voltage-term decomposition.

## Comments 20–35 — Figure 5 and Section 2.4

- Figure 5a should show the full first-lithiation Delta E_relax range plus a zoomed late-stage region.
- Remove “state-resolved” where it obscures meaning; use normalized lithiation capacity z and GITT step.
- Replace “excess” terminology with “relaxation hump” / “background-subtracted relaxation hump.”
- Use “pristine HEO.”
- Remove vague “generic relaxation” wording.
- Explain voltage mapping directly: the background-subtracted hump from each GITT step is plotted at that step’s 60 min rest-end voltage.
- Keep the nominal <=32 mV peak correspondence while moving background/window sensitivity to the SI.
- Interpret the hump directly as dominated by processes in the conversion region.
- Mention plausible coupled conversion processes: nucleation/phase growth, phase-boundary motion, M–O rearrangement, cation/oxygen redistribution, and metal/Li2O formation.
- Do not repeatedly defend against non-conversion interpretations.
- Do not assign a numerical fraction of polarization to conversion because the data do not establish such a fraction.

## Comments 36–54 — Figure 6 / four-step microkinetics

- Define the former “homogeneous” model explicitly as one kinetic population with one set of rate parameters and no particle/domain distribution.
- Remove “literature-grounded”; cite the relevant literature directly.
- Explain the physical sequence before the computational O–I–J–K–C symbols.
- Rename “single-step limiting analysis” to **single-step rate perturbation**.
- Clarify that the calculation does not designate an a priori RDS.
- Add the calculation chain to Methods:
  rate expressions -> state balances -> galvanostatic current balance -> voltage -> fixed-cutoff capacity -> zero-current relaxation.
- Clarify that forward/reverse rates are scaled together for reversible internal-step perturbations so equilibrium constants remain fixed.
- Replace vague “equilibrium parameters” with equilibrium constants and electrochemical equilibrium parameters.
- Label Figure 6b regions by physical observable response.
- Explain eigenmodes for a materials audience as collective natural relaxation modes of coupled intermediate populations, not elementary-reaction time constants.
- Explain the BM model/experiment magnitude difference using omitted particle/domain distributions, spatial transport, interfacial polarization, and other electrode-level contributions.
- Avoid unnecessary fit/fitting language.
- Compare modeled voltage-relaxation magnitude only directionally because the measured relaxation can contain conversion, transport, interfacial, and state-dependent thermodynamic contributions.
- Remove the indirect closing paragraph that only “provides context” for Dapp.
- Rename Methods 4.4 to **Four-step conversion microkinetic model** and define its exact purpose directly.

## Additional revision after Comment 36–54 review — revised Mg model test

The Figure 4 conversion-window revision changes the experimental Mg/HEO ratios to:

- Q ratio = 0.7534
- t63 ratio = 1.0154
- Delta E_relax ratio = 0.6605

The fixed-thermodynamics R2–R3 map does not reproduce this Mg direction well.

A separate product-side electrochemical equilibrium-offset trajectory within the same four-step network does reproduce the direction:

illustrative u4: -3 -> -1.5
- Q/Q0 = 0.7637
- t63/t0 = 0.9975
- modeled Delta E ratio = 0.755

Therefore:
- **retain the Mg experimental marker in Figure 6c**;
- show the BM marker against the step-selective R2–R3 kinetic response;
- show the Mg marker against a distinct product-side thermodynamic-shift trajectory;
- do not assign BM uniquely to R2/R3 or Mg uniquely to u4.

Detailed Mg audit:
- `modeling/HEO_MG_REVISED_WINDOW_FOUR_STEP_TEST_2026-09-30.md`
- `modeling/HEO_MG_REVISED_WINDOW_U4_TRAJECTORY_2026-09-30.csv`

## Word-stage rule

When the final Main DOCX is assembled:
1. preserve all original PI comments;
2. append concise replies reflecting the decisions above;
3. do not mark comments resolved unless explicitly requested;
4. render and inspect the full DOCX after comment insertion.
