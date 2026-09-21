# HEO current artifacts — 2026-09-21

## Authority order

1. Scientific/text authority: `manuscript/HEO_MANUSCRIPT_V4_AFM_CONVERSION_2026-09-20.md`
2. SI authority: `manuscript/HEO_SUPPORTING_INFORMATION_V3_REVIEW_READY_2026-09-20.md`
3. Figure architecture: `manuscript/HEO_FIGURE_ARCHITECTURE_AND_CAPTIONS_V2_CONVERSION_2026-09-20.md`
4. Current project state: `START_HERE_CURRENT_STATE_2026-09-21.md`
5. Collaborator-clean Main: `manuscript/HEO_MANUSCRIPT_COLLABORATOR_REVIEW_2026-09-21.md`
6. Collaborator-clean SI: `manuscript/HEO_SUPPORTING_INFORMATION_COLLABORATOR_REVIEW_2026-09-21.md`
7. Yoo-group review checklist: `manuscript/YOO_GROUP_COLLABORATOR_REVIEW_NOTES_2026-09-21.md`

Word files and review PNGs are exports. They never override the Markdown scientific authority.

## Current collaborator Word exports

Generated and visually QA’d on 2026-09-21:

- `HEO_Main_Collaborator_Review_2026-09-21.docx`
- `HEO_SI_Collaborator_Review_2026-09-21.docx`
- `HEO_Yoo_Group_Review_Notes_2026-09-21.docx`

These binaries were generated in the ChatGPT runtime and are not stored in GitHub. If unavailable in a future session, regenerate them from the collaborator-clean Markdown files.

## Current working title

**Structural Modification Reshapes Conversion and Relaxation in Spinel High-Entropy Oxide Anodes**

The older “Independently Regulate” title is obsolete.

## Current Figure numbering

- Figure 1: collaborator structural/compositional/nanoscale characterization
- Figure 2: collaborator morphology/physical surface characterization
- Figure 3: conventional electrochemistry
- Figure 4: GITT relaxation magnitude vs timescale
- Figure 5: conversion-associated excess relaxation + first-cycle dQ/dV
- Figure 6: reduced spatial model consistency test

Historical filenames containing “Figure4 conversion assignment” or “Figure5 model” preserve provenance only; their numbering is no longer current.

## Current clean delivery package logic

The collaborator-clean Main/SI:
- retain Yoo-group / collaborator requests;
- remove Yoon-Lab-only metadata reminders;
- remove internal dQ/dV source-development notes from the delivery-facing text;
- retain scientific claim boundaries;
- preserve Figures 3–6 as already organized.

The one-page Yoo-group notes file summarizes only the inputs required from Prof. Yoo’s group.

## Key numerical source boundary

Latest four-sample continuous first-cycle numerical GCD files are not available.

Current Figure 5 dQ/dV development values were reconstructed from the user’s own vector voltage profiles in:
- Park Seong Hyeon, `HEO 진행상황 (20260917).pptx`, slide 10.

The older profile affected by a power interruption is excluded.

If the original continuous numerical profiles are recovered, use them to regenerate the final Figure 5 artwork while preserving the present claim boundary unless the new result materially changes it.

## Current model authority

Verified scientific reference:
- `modeling/HEO_FINAL_PYTHON_PHYSICS_GATE_2026-09-18.md`
- `modeling/heo_spatial_phase_field_frozen_v4.py`

MATLAB translation:
- `modeling/HEO_Spatial_PhaseField_Model_Final.m`

Do not claim independent MATLAB validation until actually runtime-verified.

## Previous 2026-09-20 binaries

The earlier files
- `HEO_AFM_FinalDraft_ConversionCentered_2026-09-20.docx`
- `HEO_Supporting_Information_V3_Final_2026-09-20.docx`
- old Figure 4/5 review composites

are superseded for collaborator handoff by the 2026-09-21 clean review package.

They may be retained for provenance but should not be used as the starting point for new edits.
