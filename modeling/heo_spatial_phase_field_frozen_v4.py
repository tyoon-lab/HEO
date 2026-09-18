# HEO spatial phase-field model — frozen Python specification v4
# Date: 2026-09-18
#
# Authoritative equation/parameter snapshot for MATLAB translation.
# Mechanism-sufficiency model only; parameters are non-unique.
#
# Free energy:
# f = c*ln(c) + (1-c)*ln(1-c)
#   + W*phi^2*(1-phi)^2
#   + K*(cstar-c)*phi
#   + Gmg*phi
#   + 0.5*Bel*qel(r)*phi^2
#   - Ssurf*wsurf(r)*phi
#   + 0.5*kappa*|grad(phi)|^2
#
# qel(r)   = 1-exp(-(1-r)/ell_relief)
# wsurf(r) = exp(-(1-r)/ell_wet)
#
# mu = ln(c/(1-c)) - K*phi
# dc/dt   = -div(J), J = -Ddim*grad(mu)
# dphi/dt = -Mphi*deltaG/deltaphi
#
# Protocol:
# pulse = 600 s
# rest = 3600 s
# ncycles = 50
# jin = 9e-6
# kappa = 0.002
# radial finite-volume mesh N=18 for the frozen directional gate.
#
# Voltage readouts:
# Vvol  = -volume_average(mu)
# Vsurf = -mu(surface)
#
# HEO:
# Ddim=0.0015, Mphi=0.015, W=0.60, K=1.80,
# Gmg=0, Bel=0.20, ell_relief=0.08, Ssurf=0.08, ell_wet=0.06
#
# Mg-HEO:
# Ddim=0.0015, Mphi=0.0006, W=0.80, K=1.80,
# Gmg=0.38, Bel=0.20, ell_relief=0.08, Ssurf=0.08, ell_wet=0.06
#
# BM-HEO latent x~N(0,1), 11 equal-probability quantiles:
# Ddim=0.003, W=0.50, K=1.60, Gmg=0, Bel=0.25, ell_relief=0.20
# Ssurf = 0.15 + 0.06*x
# Mphi  = 0.008*exp(-0.6*x)
# ell_wet = 0.12
#
# BM-Mg-HEO:
# Ddim=0.003, W=0.70, K=1.70, Gmg=0.30, Bel=0.25, ell_relief=0.20
# Ssurf = 0.22 + 0.075*x
# Mphi  = 0.0008*exp(-0.6*x)
# ell_wet = 0.12
#
# Numerical convergence for heterogeneous ensembles should use a
# polarization-weighted second-moment width in state, not FWHM.
