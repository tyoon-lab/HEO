# HEO Four-Step Homogeneous Microkinetic Audit

**Date:** 2026-09-28  
**Purpose:** replace the earlier heterogeneous-accessibility existence proof with a homogeneous, literature-grounded four-effective-step conversion model and define the main-text/SI claim boundary.

## 1. Four-step sequence

Literature basis: Ng et al., J. Mater. Chem. A 2021, DOI 10.1039/D0TA09683K.

[
O \rightleftharpoons I \rightleftharpoons J \rightleftharpoons K \rightleftharpoons C
]

Interpretation:
- R1: initial lithiation / first electron transfer (electrochemical)
- R2: effective M–O dissociation / local structural reconstruction (chemical)
- R3: effective Li2O-forming / product-side reconstruction (chemical)
- R4: second electron transfer / metal reduction (electrochemical)

The states are coarse-grained effective states. Do not claim direct identification of M+, LiO−, or a unique atomistic HEO pathway.

## 2. Single-step limiting audit

Each step was scaled individually while the other steps and equilibrium constants were held fixed.

At 0.1× rate:
- R1-limited: Q/Q0 = 0.893, t63/t63,0 = 0.959
- R2-limited: Q/Q0 = 0.351, t63/t63,0 = 2.437
- R3-limited: Q/Q0 = 0.495, t63/t63,0 = 1.573
- R4-limited: Q/Q0 = 0.907, t63/t63,0 = 1.058

At 10× rate:
- R1: Q/Q0 = 1.010, t63/t63,0 = 0.997
- R2: Q/Q0 = 1.183, t63/t63,0 = 0.952
- R3: Q/Q0 = 1.325, t63/t63,0 = 0.530
- R4: Q/Q0 = 1.009, t63/t63,0 = 1.003

Main interpretation:
- R2 and R3 exert the strongest control on both accessible cutoff capacity and relaxation timescale.
- Slowing either R2 or R3 alone gives the conventional combination Q down / t63 up.
- Therefore the BM trend is not explained by simply making one step globally slower or faster.

## 3. Step-selective R2/R3 perturbation

A 2D parameter sweep was performed with only R2 and R3 rate scales varied; all thermodynamic/equilibrium parameters were fixed.

Grid:
- R2 scale: 0.12–1.20
- R3 scale: 0.8–50
- total points: 396

A finite region gives simultaneous:
[
Q/Q_0 > 1,qquad t_{63}/t_{63,0} > 1.
]

28/396 grid points (7.1%) fall in this Q-up / t63-up regime.

Grid-resolved Q-up / t63-up band:
- R2 ≈ 0.406 with R3 ≈ 8.50–50: Q/Q0 ≈ 1.005–1.042; t63/t63,0 ≈ 1.200–1.211
- R2 ≈ 0.465 with R3 ≈ 3.18–50: Q/Q0 ≈ 1.000–1.111; t63/t63,0 ≈ 1.076–1.097
- R2 ≈ 0.532 with R3 ≈ 2.14–2.61: Q/Q0 ≈ 1.003–1.034; t63/t63,0 ≈ 1.009–1.041

Thus the anomalous ordering is not a knife-edge numerical artifact, but it occupies a restricted step-selective kinetic window.

## 4. Physical interpretation

Linearization of the current-off dynamics gives

[
delta\dot{\mathbf{x}}=\mathbf{J}delta\mathbf{x},
qquad
delta E(t)=\sum_i B_i e^{-t/	au_i}.
]

For the representative R2×0.5 / R3×2.5 perturbation:
- slow eigenmode: 15.35 → 17.51 min
- magnitude of the slow voltage-mode weight: |B_slow| increases from 34.30 to 37.54 mV
- during the galvanostatic pulse, downstream R3/R4 flux increases while the slow internal mode becomes longer.

Interpretation:
- one internal step can dominate the slow current-off eigenmode;
- a different downstream step can sustain greater reaction throughput before the cutoff;
- therefore accessible capacity and post-interruption relaxation speed are coupled to the same reaction network but need not have the same fast/slow ordering.

## 5. Experimental mapping

Experimental first-cycle ratios:
- BM-HEO / HEO: Q = 1.284; t63 = 1.333
- Mg-HEO / HEO: Q = 0.753; t63 = 1.268

With only R2 and R3 rates varied:
- BM direction (Q up / t63 up) is reproduced, but the full experimental magnitude is outside the minimal two-parameter map. The closest broad-bound Q/t point tends toward very fast R3 and gives only ~Q 1.07 / t63 1.19.
- Mg lies much closer to the same model manifold. A representative near-Mg point is R2 ≈ 0.65, R3 ≈ 0.75, giving Q/Q0 ≈ 0.779 and t63/t63,0 ≈ 1.319.

Do not present either as a fitted microscopic parameter assignment.

## 6. Relaxation magnitude

The full experimental ΔE_relax is NOT a fitting target for the microkinetic model.

Reason:
- experimental 3 s-to-60 min voltage relaxation can contain conversion polarization plus transport, interfacial, thermodynamic/state-distribution, and other contributions;
- FeF3 GITT literature (Li et al., JACS 2016, DOI 10.1021/jacs.6b00061) explicitly supports this bounded interpretation.

ΔE_relax remains an experimental descriptor demonstrating that relaxation magnitude and relaxation speed are not equivalent observables.

## 7. Main-text claim boundary

Safe main claim:
> A homogeneous four-step conversion network can produce higher cutoff-limited capacity together with slower post-interruption relaxation when different internal steps change in opposite directions. Linearized current-off dynamics show that a slow internal eigenmode can lengthen while a different downstream step increases reaction throughput. Thus accessible reaction extent and relaxation speed need not collapse onto one scalar kinetic coordinate.

Do not claim:
- ball milling specifically slows R2 and accelerates R3;
- the model quantitatively fits BM-HEO;
- a unique HEO RDS has been identified;
- the full experimental ΔE_relax is generated only by the modeled conversion sequence;
- spatial/population heterogeneity is required.

## 8. Recommended Figure 6 architecture

(a) Literature-grounded four-step sequence R1–R4.  
(b) Single-step limiting audit / homogeneous global expectation.  
(c) R2–R3 2D kinetic-regime map highlighting the finite Q-up / t63-up region.  
(d) Representative current-off eigenmode / same-scale relaxation comparison showing why throughput and slow relaxation can move in different directions.

Mg can be marked in observable-space or mentioned textually as a complementary lower-Q / longer-t63 case; avoid mapping it to a unique R2/R3 pair.
