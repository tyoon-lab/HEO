import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

# Main quantitative values are read from:
# modeling/HEO_CAPACITY_RELAXATION_MICROKINETIC_VALIDATION_2026-09-25.csv
#
# The intended publication architecture is documented in:
# manuscript/HEO_FIGURE7_ARTWORK_FINAL_NOTE_2026-09-27.md
#
# Panel (a): O <-> I <-> I* <-> C effective-state schematic
# Panel (b): j_ext = 0 with finite opposing Faradaic partial currents
# Panel (c): homogeneous global-rate control, t63 vs Q_cutoff
# Panel (d): same axes as (c), with homogeneous control retained as a
#            dashed reference and the heterogeneous-accessibility existence
#            proof shown from the reference point.
#
# This script intentionally keeps the main artwork free of fitted-looking
# material labels such as "BM-like" and leaves illustrative weights/rate
# ratios in the SI/model audit.

RATE_SCALE = np.array([0.50, 0.75, 1.00, 1.50, 2.00])
Q_CUTOFF = np.array([0.29934431595, 0.41868111025, 0.55845433231,
                     0.73989909197, 0.83221385335])
T63 = np.array([22.45, 17.1166666667, 13.45, 9.1166666667, 6.95])

Q_REF, T_REF = 0.55845433231, 13.45
Q_HET, T_HET = 0.65714004678, 15.2833333333

# Use normal-weight panel labels and left/bottom axes only.
# For the final manuscript assembly, generate each chart as an independent
# axis/graphic and compose them into the four-panel figure.
