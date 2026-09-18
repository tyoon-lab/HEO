# HEO Mechanistic Logic Update — Diffusion vs Phase-Transition Polarization

**Date:** 2026-09-18

## 1. Core diagnostic logic

The current GITT result is most useful when phrased as a test of a single-diffusivity explanation rather than as a claim that diffusion must always produce a fixed mathematical relation between polarization amplitude and relaxation time.

For an otherwise comparable electrode under the same pulse current, pulse duration, geometry, and thermodynamic factor:
- a lower Li diffusivity produces a larger concentration gradient during the pulse;
- this increases diffusion-associated polarization;
- the same lower diffusivity also increases the characteristic diffusion relaxation time, approximately through tau_D ~ L^2/D.

Therefore, if one varying diffusion coefficient were the dominant origin of both observables, larger diffusion polarization and slower relaxation should move in the same direction.

The Mg-containing HEO does not follow this expectation: current-off polarization decreases strongly, the late-stage excess polarization is suppressed, but t63/t90 do not become shorter and are instead comparable or longer. This weakens a D-only / diffusion-overpotential explanation and motivates a distinct origin of the late-stage polarization.

## 2. Preferred phase-transition interpretation

The voltage range of the late-stage hump overlaps the known conversion / spinel-to-rock-salt phase-evolution regime of related Fe-Co-Cr-Ni-Mn spinel HEOs.

For a phase transition, polarization amplitude and relaxation time need not be uniquely coupled:
- polarization amplitude can depend on transformed fraction, nucleation barrier, interfacial energy, strain energy, and local thermodynamic driving force;
- relaxation time can depend on phase-boundary mobility, oxygen/cation rearrangement, structural mobility, and the distribution of local transition kinetics.

Therefore a material can show a smaller transformation-associated polarization but slower residual relaxation.

## 3. Mg interpretation: two effects are required

A pure kinetic-barrier argument is insufficient. If Mg only reduced phase-boundary mobility while the same amount of transformation still had to carry the same current, the required transformation overpotential would generally be expected to increase, not decrease.

The present data are more consistent with two coupled Mg effects:
1. Thermodynamic / structural stabilization: stabilizes the spinel- or oxide-derived state; reduces the fraction of material entering the late-stage conversion pathway; lowers conversion-associated capacity and the transition-polarization amplitude.
2. Reduced structural mobility of the residual transforming population: slows oxygen/cation rearrangement or phase-boundary motion; gives a longer t63/t90 for the polarization that remains.

Working summary:
Mg incorporation -> parent/intermediate structural stabilization + smaller transformed fraction + slower residual structural relaxation -> smaller hump, lower conversion capacity, longer or unchanged relaxation time.

## 4. Ball-milling interpretation: nanosizing does not necessarily raise phase-transition overpotential

The initial intuition that smaller particles must require a larger phase-transition overpotential because nanoscale deformation is harder is not generally valid.

Phase-field theory for coherent phase-separating nanoparticles shows elastic relaxation near surfaces, nucleation barriers that decrease with increasing surface-to-volume ratio, and possible disappearance of the nucleation barrier below a critical particle size.

More directly relevant, a 2025 study of spinel-type HEOs compared ~150 nm and ~15 nm particles: the smaller HEO showed lower GITT polarization, shortened diffusion lengths mitigated kinetic sluggishness, conversion was more complete, and voltage plateaus became less pronounced / more sloped.

This is qualitatively consistent with the present BM-HEO result.

Ball milling can simultaneously reduce coherent-domain / effective transport length, increase BET area and accessible interface, introduce defects and heterogeneous nucleation sites, relax some coherency strain at surfaces/interfaces, and broaden the distribution of local transition potentials.

Therefore:
Ball milling -> lower local nucleation/transport penalty + more heterogeneous local transition energies -> lower peak polarization + broader capacity interval + higher accessible capacity.

The longer t63 can still arise because the electrode now contains a broader distribution of structural relaxation rates. Peak amplitude and ensemble relaxation time are therefore not required to change in the same direction.

## 5. MATLAB simulation strategy

### Level 1 — Minimal mechanistic discriminator

Use a lumped pulse/rest model:
E(t) = E_eq(q) + eta_D(t) + eta_PT(t) + R_ohm I(t)

Diffusion contribution:
- tau_D ~ L^2 / D
- eta_D amplitude coupled monotonically to D under the same pulse condition.

Phase-transition contribution:
- transformed fraction phi;
- local transition free-energy offset DeltaG_PT;
- structural mobility M_phi;
- optional distribution of local transition potentials / barriers.

Test four cases:
A. D-only variation: lower D -> larger eta + longer tau; should fail for Mg.
B. Mg structural stabilization only: smaller transformed fraction -> smaller hump and lower capacity; relaxation time need not increase enough.
C. Mg mobility reduction only: slower relaxation but tends to require more transformation overpotential if the same reaction current is maintained; should fail to explain smaller hump by itself.
D. Mg stabilization + lower structural mobility: smaller hump + lower conversion capacity + longer t63; expected to reproduce the observed direction of all three quantities.

For BM:
- decrease effective L / transport length;
- decrease mean nucleation barrier;
- increase distribution width sigma_Etr of local transition potentials;
- increase accessible fraction;
- optionally broaden the distribution of structural mobilities.

Expected BM outcome: peak down, width up, capacity up, while ensemble t63 can increase.

### Level 2 — 1D radial phase-field model

Use spherical radius r and two state variables:
- c(r,t): Li concentration, conserved;
- phi(r,t): structural phase order parameter, non-conserved.

A suitable free energy is:
G = integral [ f(c,phi) + W phi^2(1-phi)^2 + (kappa_phi/2)|grad phi|^2 + f_elastic(phi) + DeltaG_Mg phi ] dV

with dynamics:
dc/dt = div( M_c grad mu_c )
dphi/dt = -M_phi deltaG/deltaphi

Boundary condition: galvanostatic Li flux for 600 s, then zero flux for 3600 s relaxation.

Recommended MATLAB implementation: radial finite difference with 50–100 nodes, method of lines, ode15s for the stiff coupled dynamics. A custom finite-difference implementation is easier than pdepe when concentration, structural order parameter, elastic terms, and heterogeneous barriers are all included.

## 6. Parameter roles

| Parameter | Physical role | Mg hypothesis | BM hypothesis |
|---|---|---|---|
| D or M_c | Li/ionic transport | not primary explanation | effective transport length decreases |
| DeltaG_Mg | spinel/intermediate stabilization | increase | unchanged |
| M_phi | structural/phase mobility | decrease | distributed / heterogeneous |
| W | local phase barrier | possibly increase | mean may decrease locally |
| kappa_phi / gamma | phase-boundary energy | possible change | interfaces/defects reduce effective nucleation penalty |
| R or L | particle/coherent-domain size | similar | decrease |
| sigma_Etr | distribution of local transition potentials | modest | increase strongly |
| accessible fraction | reacting volume/interface fraction | decrease for conversion | increase |

## 7. Recommended manuscript logic

If the current-off response were governed predominantly by a single diffusion coefficient, a larger diffusion-associated polarization would be expected to coincide with a slower relaxation under otherwise comparable pulse conditions. Mg incorporation instead strongly decreases the polarization amplitude while leaving the characteristic relaxation time unchanged or longer. This opposite movement rules out a simple diffusion-only explanation for the late-stage response.

The voltage range and literature-established phase evolution of related spinel HEOs instead identify the late-stage excess polarization with the conversion-associated phase transformation. Unlike diffusion polarization, the magnitude of a phase-transition overpotential and the rate of its relaxation need not be uniquely coupled because the transformed fraction, nucleation/strain energy, and phase-boundary mobility represent distinct physical variables.

Mg is therefore interpreted as suppressing the extent of the conversion transition through structural stabilization while slowing the residual structural relaxation, whereas ball milling broadens the distribution of local transition conditions and lowers the concentrated peak barrier while increasing electrochemical accessibility.

## 8. Literature anchors

- Cogswell & Bazant, Nano Letters 2013: coherent nucleation barrier decreases with surface/volume ratio and can vanish below a critical particle size.
- Cogswell & Bazant, ACS Nano 2012: coherency strain and size-dependent phase separation.
- Li et al., Angewandte Chemie International Edition 2025, DOI 10.1002/anie.202518569: spinel HEO ~150 nm vs ~15 nm; smaller particles show lower GITT polarization and more complete conversion by overcoming kinetic sluggish diffusion.
- Komayko et al., Journal of Power Sources 2024, 624, 235589: nucleation contributes substantially to overpotential in phase-transforming battery materials.
- Jin et al., Materials Today Chemistry 2025, 48, 102949: Fe-Co-Cr-Ni-Mn spinel HEO phase path spinel -> mixed spinel/rock-salt -> rock-salt.