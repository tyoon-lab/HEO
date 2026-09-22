# GITT-Constrained Conversion-Dynamics Model — 2026-09-22

## Purpose

Develop a reduced simulation that:
1. genuinely visualizes conversion dynamics;
2. is constrained by the measured GITT response rather than by hand-selected effective mobilities;
3. potentially yields a useful mechanistic quantity that can organize the paper;
4. remains subordinate to the experimental evidence in Figures 4–5.

This replaces the immediate need for the older spatial phase-field consistency model, which is currently removed from the revised Main/SI.

---

## Experimental inputs

### GITT protocol

- current pulse: 600 s
- open-circuit rest: 3600 s
- common current-off reference: 3 s
- current: 100 mA g^-1

### State coordinate

[
z = Q/Q_{max}
]

for first lithiation.

### Conversion-associated response

Use the positive, background-subtracted late-stage GITT excess response:

[
eta_{excess}(z)=max[Delta E_{relax}(z)-eta_{bg}(z),0]
]

Nominal background fit windows:
- z = 0.20–0.40
- z = 0.90–1.00

Nominal evaluation window:
- z = 0.40–0.90

This same excess response was independently localized to the first-cycle cathodic conversion region by dQ/dV.

### Experimental relaxation timescale

Use state-resolved:

[
tau(z) approximately t63(z)
]

where `t63` is the model-free time needed to complete 63.2% of the observed 3 s-to-3600 s voltage recovery.

Important caveat:
the experimental t63 is a voltage-relaxation descriptor. Mapping it to the reduced conversion-response state is a modeling assumption, though it is more directly data-constrained than the previous free effective mobility parameters.

---

## Model definition

### 1. Effective threshold distribution

Define an internally normalized threshold-weight distribution:

[
p(z_c)=
eta_{excess}(z_c)
/
integral eta_{excess}(z) dz
]

Interpretation:
- `p(z_c)` is a reduced distribution of where the conversion-associated response is expressed over reaction state;
- it is **not** a measured microscopic nucleation-threshold distribution;
- its normalization removes absolute response magnitude, so it cannot compare absolute conversion extent between samples.

### 2. Local state

Each effective local domain is assigned a threshold `z_c`.

After the applied state passes the threshold:

[
d xi/dt = (1-xi)/tau(z_c)
]

with `xi=0` before activation.

For a constant-rate drive:

[
dz/dt = C/3600
]

when C is expressed as a nominal C-rate-equivalent drive.

Thus for `z > z_c`:

[
xi(z;z_c)
=
1-exp[-(z-z_c)3600/(C tau(z_c))]
]

### 3. Ensemble state

[
X(z)=integral p(z_c) xi(z;z_c) dz_c
]

Interpretation:
- `X` = normalized effective conversion-response state;
- `X` is **not** a chemical phase fraction;
- `X` should only be used comparatively within the reduced model.

### 4. Quasi-static target response

The normalized cumulative target response is:

[
F(z)=integral_{z_1}^{z} p(z_c) dz_c
]

If local relaxation were instantaneous after threshold activation, `X(z)` would approach `F(z)`.

### 5. Dynamic lag

State-resolved lag:

[
L(z)=F(z)-X(z)
]

Exploratory integrated metric:

[
L_{int}
=
(1/(z_2-z_1))
integral_{z_1}^{z_2} [F(z)-X(z)] dz
]

This descriptor is **not yet physically validated**. Its meaning must be discussed before manuscript use.

---

## Raw-data recovery

Gmail thread:
- subject: `HEO 데이터입니다.`
- message ID: `1a0ae3f06335d881`
- date: 2026-09-17

Raw files:
- HEO: `HEO GITT 로우 데이터.xlsx`
  - Drive ID `1mYRsquXEmMg1beCvtOqrWXEoOdaU1YgR`
- BM-HEO: `BM HEO 3 GITT 로우 데이터.xlsx`
  - Drive ID `1VpWKWk85ubxYFVEzY_8UNkCZL0LszGQN`
- Mg-HEO: `HEO 3 Mg 로우 데이터.xlsx`
  - direct Gmail attachment
- BM-Mg-HEO: `BM HEO 3 Mg 로우 데이터.xlsx`
  - direct Gmail attachment

HEO and BM-HEO continue to sheet 2 because the raw export exceeded the Excel maximum column count.

---

## Raw reconstruction checks

Rebuilt GITT descriptors reproduced the existing manuscript values.

Key relaxed-voltage conversion-associated excess peak positions:
- HEO: ~0.5275 V
- BM-HEO: ~0.6175 V
- Mg-HEO: ~0.3870 V
- BM-Mg-HEO: ~0.5029 V

These agree with the existing Figure 5 values.

The reconstruction therefore appears consistent with the existing pulse/rest segmentation and analysis.

---

## Preliminary 1C-equivalent result

Using the distributed-threshold model:

| Sample | endpoint X at z=0.9 | integrated dynamic lag |
|---|---:|---:|
| HEO | 0.592 | 0.210 |
| BM-HEO | 0.633 | 0.269 |
| Mg-HEO | 0.601 | 0.216 |
| BM-Mg-HEO | 0.671 | 0.278 |

Related experimental first-cycle reversible capacities and conversion-response widths:

| Sample | reversible capacity (mAh g^-1) | excess width (mAh g^-1) |
|---|---:|---:|
| HEO | 609.12 | 354.13 |
| BM-HEO | 782.08 | 430.17 |
| Mg-HEO | 458.91 | 250.29 |
| BM-Mg-HEO | 580.83 | 391.78 |

---

## Preliminary interpretation

The potentially useful result is the decoupling between:
- local relaxation speed; and
- breadth / onset distribution of the conversion-associated response.

For BM-HEO:
- experimental t63 is longer than HEO;
- the conversion-associated response is broader;
- the reduced model can therefore produce greater endpoint tracking despite slower local relaxation;
- however the accumulated lag over the conversion interval can also be larger.

Potential paper-level implication:
**ball milling need not accelerate local conversion relaxation to increase finite-rate access; redistribution of the conversion response over a broader reaction-state interval can partly compensate for slower local relaxation.**

For Mg:
- absolute conversion-associated amplitude and accessible capacity are lower;
- internally normalized X must not be interpreted as greater absolute conversion;
- the residual response remains slow rather than becoming kinetically fast.

---

## Why this is potentially better than the old phase-field model

Old model:
- effective mobilities/stabilization parameters were chosen as hypotheses;
- experimental connection was directional/qualitative;
- no unique parameter extraction.

New reduced model:
- threshold weighting comes from measured GITT excess;
- local relaxation time comes from measured t63;
- simulation directly tests how conversion-state distribution and relaxation timescale combine under finite-rate driving.

Still not unique microscopic physics:
- no explicit Li2O formation;
- no explicit metal nanoparticle nucleation;
- no explicit sequential reduction of individual transition metals;
- no crystallographically calibrated phase fraction.

---

## Sensitivity already checked

Preliminary sensitivity tests varied:
- state window: approximately 0.35–0.90, 0.40–0.90, 0.45–0.90, 0.40–0.85;
- relaxation input: state-resolved t63(z) vs sample-level median t63.

The qualitative direction that BM-type samples can show both greater endpoint tracking and larger accumulated lag was preserved in the preliminary checks.

This is encouraging but not yet sufficient to freeze the metric.

---

## Candidate Figure 6

Possible panels:

### (a) Data-constrained model schematic
GITT excess -> effective threshold distribution  
GITT t63(z) -> local relaxation time

### (b) X(z) at selected drive rates
Show how finite-rate conversion-response tracking differs among HEO / BM / Mg / BM-Mg.

### (c) Lag vs drive rate
Only if the lag metric survives physical scrutiny.

### (d) Mechanistic summary map
Possible axes:
- experimental accessible capacity or absolute conversion-associated response
- model-derived dynamic lag / crossover-rate descriptor
- marker size = conversion-response breadth

Do not freeze this layout until the lag metric is understood.

---

## Critical open question

**What does “integrated dynamic lag” physically mean?**

Mathematically it is the mean state-domain deficit between the quasi-static cumulative target response F(z) and finite-rate response X(z).

It is not automatically:
- energy loss;
- polarization;
- missing capacity;
- phase fraction deficit;
- entropy production.

Before manuscript use, determine whether it has a defensible physical interpretation and whether a more intuitive descriptor would be better.

Candidate alternatives to evaluate:
1. endpoint missing response: `1-X(z_end)`
2. mean state shift / effective reaction-state delay
3. crossover C-rate at a chosen tracking threshold
4. time-integrated unrelaxed fraction
5. direct comparison to measured rate-capacity loss

**The next chat should begin here.**
