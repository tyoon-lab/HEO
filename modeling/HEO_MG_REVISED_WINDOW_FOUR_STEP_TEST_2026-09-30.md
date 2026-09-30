# HEO Mg revised-window four-step microkinetic test — 2026-09-30

## Purpose

Re-evaluate the Mg-HEO model comparison after Figure 4(c,d) was changed from the broad 200–800 mAh g^-1 summary to the common normalized first-lithiation window z = 0.40–0.90.

The revised experimental ratios relative to pristine HEO are:

- reversible first-cycle capacity: 458.91 / 609.12 = 0.75340
- median t63 over z = 0.40–0.90: 10.53 / 10.37 = 1.01543
- median Delta E_relax over z = 0.40–0.90: 111.3 / 168.5 = 0.66053

Thus the revised Mg signature is:

Q down strongly; Delta E_relax down strongly; t63 approximately unchanged.

## Four-step model reconstruction check

The current homogeneous five-state/four-step model O <-> I <-> J <-> K <-> C was reconstructed from the frozen SI parameter set:

- k1 = 0.02000
- k2,f = 0.00200
- k2,r = 0.00141421356
- k3,f = 0.00100
- k3,r = 0.00070710678
- k4 = 0.01000
- product-side electrochemical offset u4 = -3
- Japp = 2e-4
- fixed model cutoff voltage = 0.020
- matched-state relaxation at Delta Q = 0.30
- 3600 s rest; 3 s reference

The reconstructed model reproduces the frozen single-step audit to numerical precision. Examples:

- R2 x 0.1: Q/Q0 ≈ 0.3510; t63/t63,0 ≈ 2.44
- R3 x 10: Q/Q0 ≈ 1.325; t63/t63,0 ≈ 0.530
- R4 x 0.1: Q/Q0 ≈ 0.907; t63/t63,0 ≈ 1.057

The reconstructed partial rates at the matched-state pulse end and during current-off relaxation also reproduce the frozen SI values.

## Test 1: current R2–R3 kinetic map

The revised Mg point cannot be represented well by the current R2–R3 kinetic sweep at fixed thermodynamics.

Reason:
- lowering capacity through slower R2/R3 kinetics also lengthens t63 too strongly;
- within the current R2–R3 map, the combination Q/Q0 ≈ 0.753 with t63/t63,0 ≈ 1.015 is not reached.

Therefore Mg-HEO should not be forced into the same R2–R3 kinetic regime used to demonstrate the BM-HEO capacity-up / slower-relaxation ordering.

## Test 2: product-side thermodynamic offset within the same four-step network

Keeping all kinetic rate constants fixed and changing only the product-side electrochemical equilibrium offset u4 produces a Mg-like response.

Representative result:

u4 = -3.0 (reference):
- Q/Q0 = 1
- t63/t63,0 = 1
- Delta E_model/Delta E0 = 1

u4 = -1.5:
- Q/Q0 = 0.76373
- t63/t63,0 = 0.99753
- Delta E_model/Delta E0 = 0.75495

Experimental Mg-HEO / HEO:
- Q ratio = 0.75340
- t63 ratio = 1.01543
- Delta E_relax ratio = 0.66053

Thus a shift in conversion thermodynamics within the same multistep network reproduces the three experimental directions without requiring a slower overall relaxation:
- accessible capacity decreases;
- the modeled relaxation magnitude decreases;
- the characteristic relaxation time remains nearly unchanged.

The modeled relaxation magnitude is not a quantitative fitting target; its directional decrease is the relevant result.

## u4 trajectory

See:
modeling/HEO_MG_REVISED_WINDOW_U4_TRAJECTORY_2026-09-30.csv

Representative trajectory:
- u4 = -1.8: Q/Q0 0.8123; t63/t0 0.9954; Delta E/Delta E0 0.7900
- u4 = -1.7: 0.7958; 0.9961; 0.7776
- u4 = -1.6: 0.7796; 0.9968; 0.7659
- u4 = -1.5: 0.7637; 0.9975; 0.7549
- u4 = -1.4: 0.7482; 0.9983; 0.7446
- u4 = -1.3: 0.7332; 0.9991; 0.7350
- u4 = -1.2: 0.7187; 0.9999; 0.7260

## Figure 6 decision

Retain the Mg experimental marker.

Recommended Figure 6 architecture:

(a) Single-step rate-perturbation audit.

(b) R2–R3 kinetic-regime map at fixed thermodynamics. This panel remains the primary test for the BM-HEO capacity-up / slower-relaxation ordering.

(c) Observable-space projection containing BOTH experimental comparisons:
- the R2–R3 step-selective kinetic sweep / region and the BM-HEO/HEO marker;
- a separate u4 thermodynamic-shift trajectory from the same four-step network and the Mg-HEO/HEO marker.

The two model trajectories must be visually and textually distinguished. Mg should not be presented as lying on the BM-oriented R2–R3 kinetic map.

The representative u4 = -1.5 point may be indicated on the thermodynamic trajectory. Its modeled relaxation-amplitude ratio (0.755) can be stated in the caption or text as directionally consistent with the experimental decrease (0.661), without treating amplitude as a quantitative fit.

(d) Retain the representative current-off/eigenmode comparison for the BM-oriented step-selective kinetic case.

## Claim boundary

Supported:
- the same multistep conversion network can accommodate both experimental modification directions;
- BM-like Q up / t63 up requires step-selective kinetic changes in the current minimal model;
- Mg-like Q down / Delta E down / t63 approximately unchanged can arise from a change in conversion thermodynamics without requiring globally slower relaxation.

Not supported:
- Mg incorporation uniquely changes u4;
- u4 = -1.5 is a fitted Mg parameter;
- ball milling uniquely maps to R2/R3;
- the modeled Delta E quantitatively represents the full experimental voltage relaxation.
