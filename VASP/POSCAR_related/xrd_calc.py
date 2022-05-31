#%%
import os
from pymatgen.analysis.diffraction.xrd import XRDCalculator
from pymatgen import Structure

# os.chdir('/home/jinho93/arsnide/ZnAs/15700/opti/dos')
os.chdir('/home/jinho93/ml/hfo2/schottky')
calc = XRDCalculator(symprec=1e-1)
s = Structure.from_file('POSCAR')
pat = calc.get_pattern(s, two_theta_range=(10, 90))
# calc.show_plot(s)
# %%
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.ndimage import gaussian_filter1d
f = interp1d(pat.x, pat.y, kind='linear')
xnew = np.linspace(20, 80, 1000)
plt.plot(pat.x, pat.y)
# plt.plot(xnew, f(xnew))
# ynew = gaussian_filter1d(pat.y, 2)
# plt.plot(pat.x, ynew)
plt.xlim(20, 80)
# np.savetxt('/home/jinho93/xrd.dat', np.transpose([pat.x, pat.y]))
# %%
