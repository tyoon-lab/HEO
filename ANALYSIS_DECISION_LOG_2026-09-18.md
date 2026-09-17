# Analysis Decision Log

**Date:** 2026-09-18

This short log records the current analysis decisions so that the manuscript does not drift back toward a conventional single-D GITT interpretation.

## Locked decisions

1. The manuscript is synthesis-centered; electrochemistry explains the roles of Mg incorporation and ball milling.
2. Main GITT interpretation will use current-off / relaxation data rather than current-on pulse evolution because pulse data mix equilibrium-potential evolution with polarization.
3. Use ICI-style early-rest fitting (`E = a + b sqrt(t)`) to estimate an apparent instantaneous current-off jump rather than treating the first 3 s point as pure IR.
4. Use model-free t50/t63/t90 descriptors; do not describe them as fitted single time constants.
5. Use cumulative specific capacity as the primary state coordinate and retain voltage as a secondary coordinate.
6. Assign the late-stage relaxation hump primarily to spinel-to-rock-salt/conversion phase evolution, supported by related spinel-HEO literature and the characteristic low-voltage window.
7. Ball milling: interpret as broadening/distribution of the transformation interval plus larger accessible low-rate capacity, not as simple diffusion enhancement.
8. Mg: interpret primarily as suppressing/stabilizing against the late-stage conversion/phase transformation, not as simple acceleration of Li diffusion.
9. Quantify the late-stage feature by peak height, capacity width, and capacity-weighted excess polarization area on both absolute and normalized-capacity axes.
10. Conventional `D_GITT` remains only an apparent comparator and should not drive the mechanistic story.
11. `D-only -> D + one compact relaxation mode -> distributed relaxation` is retained as an internal identifiability/model-sufficiency audit. It should not be elevated to a main HEO result unless a stable, synthesis-dependent parameter emerges.
12. Full pulse+rest joint EKF remains a future kinetic-fingerprint analysis, separate from the present synthesis manuscript.
