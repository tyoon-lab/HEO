# HEO consolidation audit — 2026-09-20

## Scope
Checked the 2026-09-20 discussion against the HEO GitHub repository after the AFM/conversion reinterpretation.

## Items that were missing and are now updated
1. AFM as current first target and the materials-centered positioning.
2. New authoritative Main manuscript v4 with AFM section order and conversion-centered Figure 4/5 language.
3. Conversion-aligned SI v2.
4. Latest first-cycle voltage-profile reconstruction and common dQ/dV processing:
   - HEO 0.545 V;
   - BM-HEO 0.589 V;
   - Mg-HEO 0.419 V;
   - BM-Mg-HEO 0.485 V.
5. GITT excess peak comparison:
   - HEO 0.527 V;
   - BM-HEO 0.618 V;
   - Mg-HEO 0.387 V;
   - BM-Mg-HEO 0.503 V.
6. All four dQ/dV–GITT peak pairs are within 32 mV.
7. Figure 4 redesign: dQ/dV/GITT correspondence + peak-voltage correlation + amplitude/width/area map; raw/background analysis moved toward SI.
8. Figure 5 reinterpretation: reduced spatial model of conversion-associated state evolution.
9. Frozen-model cross-check without refitting: BM 0.5860 < HEO 0.6184 < BM-Mg 0.7966 < Mg 0.9100.
10. Explicit claim boundary that phi is not a measured rock-salt/metal/Li2O fraction and cbar is not experimental Q/Qmax.

## Still open before submission
- Recover original numerical continuous first-cycle GCD profiles if possible. Current dQ/dV peaks are reconstructed from the user's own vector voltage-profile plots.
- Complete Figure 4 background/window sensitivity freeze.
- Collaborator structural/compositional metadata: Mg recipe, ICP, refined XRD, HRTEM/SAED, final XPS decision.
- Local electrochemical metadata: current collector, drying, loading/thickness, separator/electrolyte volume, glovebox, 1C/rate sequence, instrumentation, WonATech half-cycle convention.
- Runtime verification of the MATLAB spatial port or removal of any claim that it was independently verified.
- Replace provisional review figures in the Word draft with final publication figures after the above items are frozen.

## Current claim boundary
The strongest supported experimental statement is that the late-stage GITT excess-relaxation feature is localized to and shifts with the first-cycle cathodic conversion feature. This supports a conversion/transformation-associated assignment but does not identify one unique elementary conversion step.
