# HEO Relaxation-Distribution Audit — 2026-10-07

## Purpose

Test the proposed causal link

> ball milling → broader/distributed conversion → larger slow-relaxing fraction → longer t63

directly against the raw first-lithiation GITT rest transients, rather than inferring a slow component only from t63.

## Raw data

- HEO: `HEO GITT 로우 데이터.xlsx`
- BM-HEO: `BM HEO 3 GITT 로우 데이터.xlsx`
- Mg-HEO: `HEO 3 Mg 로우 데이터.xlsx`
- BM-Mg-HEO: `BM HEO 3 Mg 로우 데이터.xlsx`
- pulse/rest: 600 s / 3600 s
- Mg-free sampling: 1 s
- Mg-containing sampling: 3 s
- common current-off reference: 3 s
- primary comparison window: normalized first-lithiation state z = 0.40–0.90

## Model-free relaxation-shape result

Median times required to complete a fixed fraction of the observed 3 s–60 min relaxation:

| sample | t50 (s) | t63 (s) | t80 (s) | t90 (s) |
|---|---:|---:|---:|---:|
| HEO | 340 | 622 | 1328 | 2145 |
| BM-HEO | 432 | 780 | 1576 | 2384 |
| Mg-HEO | 327 | 631 | 1425 | 2280 |
| BM-Mg-HEO | 410 | 760 | 1582 | 2397 |

Ball milling therefore shifts the relaxation to longer times in both composition pairs:
- HEO → BM-HEO: t50 +27%, t63 +25%, t80 +19%, t90 +11%
- Mg-HEO → BM-Mg-HEO: t50 +25%, t63 +21%, t80 +11%, t90 +5%

At 10 min, the median fraction of the 60-min relaxation completed is:
- HEO 0.624
- BM-HEO 0.573
- Mg-HEO 0.620
- BM-Mg-HEO 0.580

Thus the BM effect is not restricted to one arbitrary t63 threshold.

## Single-exponential test

A finite-window single-exponential relaxation gives poor normalized fits to the median conversion-region rest curves (RMSE approximately 0.08), whereas distributed/two-component representations reduce RMSE to approximately 0.01.

A normalized stretched-exponential representation gives:

| sample | tau* (s) | beta |
|---|---:|---:|
| HEO | 790 | 0.598 |
| BM-HEO | 1121 | 0.591 |
| Mg-HEO | 975 | 0.547 |
| BM-Mg-HEO | 1207 | 0.577 |

All beta values are well below 1, supporting a distributed, non-single-exponential relaxation shape.

### Important correction to the working hypothesis

HEO → BM-HEO does **not** show a clear decrease in beta. Therefore the data do not support the simple statement that ball milling primarily broadens the temporal relaxation-time distribution.

Instead, ball milling predominantly **shifts the distributed relaxation toward longer times** while preserving a similar degree of stretching in the Mg-free pair.

## Operational two-component representation

A two-component finite-window representation is used only as a compact shape descriptor, not as assignment of microscopic elementary steps.

Median state-wise fit values:

| sample | fast weight | tau_fast (s) | slow weight | tau_slow (s) |
|---|---:|---:|---:|---:|
| HEO | 0.327 | 82 | 0.673 | 1177 |
| BM-HEO | 0.300 | 92 | 0.700 | 1437 |
| Mg-HEO | 0.371 | 90 | 0.629 | 1422 |
| BM-Mg-HEO | 0.334 | 104 | 0.666 | 1556 |

Ball milling produces the same directional response in both composition pairs:
- longer fast apparent time
- longer slow apparent time
- modestly larger slow-window contribution

This supports a more precise wording:

> Ball milling makes the conversion-associated current-off recovery more persistent; it does not simply broaden the temporal distribution.

## Materials-level interpretation now favored

### Ball milling

Working causal chain:

ball milling
→ partial amorphization / increased structural and interfacial disorder
→ conversion proceeds through more disordered reconstructed local states and over a broader potential range
→ post-interruption structural re-equilibration is more persistent
→ dQ/dV broadening plus right-shifted normalized GITT relaxation (t50, t63, t80, t90 all longer)

The current GITT data support the final electrochemical arrows. The first structural arrow must be frozen against the final XRD/BET/microscopy package. The intermediate structural-re-equilibration statement is a mechanistic interpretation, not a directly imaged elementary step.

### Mg incorporation

Working causal chain:

Mg incorporation
→ electrochemically inactive/stabilizing Mg-containing oxide component
→ reduced accessibility / altered energetics of active-metal conversion
→ lower conversion voltage and smaller conversion-associated nonequilibrium response
→ lower dQ/dV conversion potential and smaller relaxation magnitude

The first-cycle scalar t63 changes little HEO → Mg-HEO, but the full relaxation shape is not identical: Mg-HEO has a lower stretched beta and a longer fitted slow component. Therefore avoid claiming that Mg leaves the entire relaxation kinetics unchanged. The safer mechanistic distinction is that Mg has a much stronger effect on conversion voltage and response amplitude than on t63.

## Conversion-specific interpretation

The key physical concept should be **distributed reconstructive conversion**, not a literal four-step reaction sequence.

Conversion destroys/reorganizes the parent oxide into nanoscale metal/oxide-derived states and interfaces. Consequently:
- entry into conversion can be altered by lattice/oxide stability and local reaction energetics;
- the converted/reconstructed state can exhibit distributed post-interruption structural re-equilibration;
- these two aspects need not respond identically to a material modification.

This provides the manuscript-level separation:

- Mg predominantly alters **conversion accessibility/energetics**.
- Ball milling predominantly alters the **persistence of post-conversion/reconstructive recovery**.

GITT relaxation fingerprinting is then the diagnostic used to distinguish these perturbations.

## Role of the old four-step model

Do not use the old O↔I↔J↔K↔C model to assign BM or Mg to one elementary step.

If retained, its only defensible role is an SI/existence test that a multistate reconstructive reaction can generate distributed relaxation and non-equivalent amplitude/timescale descriptors.

## Next figure concept

A final schematic should be reducible to two horizontal causal chains:

**Ball milling**
material disorder/interface increase
→ more disordered reconstructed conversion state
→ more persistent structural recovery
→ broader dQ/dV in potential + slower normalized GITT recovery

**Mg incorporation**
inactive/stabilizing Mg-containing oxide
→ conversion less energetically accessible
→ smaller converted/nonequilibrium population
→ lower conversion potential + smaller GITT relaxation amplitude

The common footer should read:

> Different material modifications perturb different dimensions of a distributed reconstructive conversion reaction, producing distinct GITT relaxation fingerprints.
