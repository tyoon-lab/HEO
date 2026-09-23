# HEO Project

## Start here

This repository is maintained so a new chat/session can resume **without a separate handoff message**.

Read first:

`START_HERE_CURRENT_STATE_2026-09-23.md`

That file is the single authoritative current-state entry point.

## Current paper story

Figure 1: structural/compositional/nanoscale characterization — provisional collaborator input  
→ Figure 2: morphology / physical characterization — provisional collaborator input  
→ Figure 3: conventional electrochemistry / absolute rate-capacity context  
→ Figure 4: GITT relaxation magnitude vs ensemble effective timescale  
→ Figure 5: first-cycle conversion-associated excess relaxation + dQ/dV localization  
→ Figure 6: **cycle-resolved evolution of conversion-associated relaxation**  
→ Figure 7: **minimal multi-step conversion microkinetic interpretation**

The paper remains an **HEO materials/mechanism paper**, not a GITT-method paper.

## Key 2026-09-23 decisions

- Figure 6 is no longer the 2026-09-22 distributed-threshold finite-rate simulation.
- Figure 6 is now experimental: 1st→2nd→3rd-cycle GITT evolution.
- Later-cycle background sensitivity passed: exponential and linear baselines give essentially identical C2/C3 hump amplitudes and peak positions.
- Figure 7 may use a minimal conversion microkinetic network to explain amplitude–timescale decoupling and cycle-history dependence.
- Figure 7 must **not** claim a unique RDS.
- Main text should not foreground “single-current non-identifiability” or invite extra experiments; the model is a mechanistic-consistency interpretation.
- A simple single-step RC description is insufficient, but charge transfer is not claimed to be absent.
- Current-dependent GITT and oxide-vs-sulfide comparison are strong follow-up directions.

## Current key files

Authoritative restart:
- `START_HERE_CURRENT_STATE_2026-09-23.md`

Figures 4–7 logic:
- `manuscript/HEO_FIGURES_4_7_CURRENT_LOGIC_2026-09-23.md`

Figure 6 evidence/audit:
- `modeling/HEO_CYCLE_RESOLVED_GITT_AND_BACKGROUND_AUDIT_2026-09-23.md`

Figure 7 microkinetics:
- `modeling/HEO_CONVERSION_MICROKINETICS_2026-09-23.md`
- `modeling/heo_conversion_microkinetics_electrochemical_growth.py`

Literature map:
- `modeling/HEO_CONVERSION_MICROKINETICS_LITERATURE_MAP_2026-09-23.md`

Current manuscript scientific authority before insertion of the new Figure 6–7 material:
- `manuscript/HEO_MANUSCRIPT_V4_AFM_CONVERSION_2026-09-20.md`
- `manuscript/HEO_SUPPORTING_INFORMATION_V3_REVIEW_READY_2026-09-20.md`

## Immediate next task

Freeze the Figure 6 and Figure 7 panel architectures/captions, then write the Results/Discussion transition through Figures 4–7.

Do not reopen the old distributed-threshold capacity-prediction model unless a specific scientific need emerges.
