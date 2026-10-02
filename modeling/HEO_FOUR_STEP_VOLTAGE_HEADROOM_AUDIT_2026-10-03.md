# HEO voltage-headroom audit — 2026-10-03

Purpose: test whether the representative R2x0.465/R3x50 capacity increase survives when the modeled conversion voltage is placed far above the experimental 0.005 V cutoff.

Method:
- Keep the four-step kinetic equations and all rate parameters unchanged.
- Add a constant voltage-reference offset so that the reference loaded voltage at DeltaQ=0.30 is assigned a selected conversion anchor voltage.
- Keep the experimental cutoff at 0.005 V.
- Compare reference and R2x0.465/R3x50 cases.

Key result:
At a 0.50 V conversion anchor:
- Qref = 1.650904
- Qpert = 1.775121
- Qpert/Qref = 1.075242
- terminal converted-state fraction Cref = 0.780904
- Cpert = 0.905121
- Cpert/Cref = 1.159068

The result saturates for conversion anchors >=0.2 V: Q ratio remains approximately 1.075 and converted-state ratio approximately 1.159.

Interpretation:
The higher-accessible-charge direction does not disappear when the conversion voltage is separated strongly from the cutoff. However, its origin changes. Under large voltage headroom, both cases nearly exhaust the oxide-derived state before cutoff. The remaining charge difference reflects how far the population progresses through the multistep sequence toward the final converted state, rather than a growing terminal polarization.

This audit does not establish that ball milling corresponds to R2 slowing and R3 acceleration. It only tests the internal consistency of the representative multistep model under a more realistic voltage-headroom condition.
