#%%
import os
from pymatgen.analysis.diffraction.xrd import XRDCalculator
from pymatgen import Structure

os.chdir('/home/jinho93/arsnide/ZnAs/15700/opti/dos')
calc = XRDCalculator(symprec=1e-1)
s = Structure.from_file('POSCAR')
pat = calc.get_pattern(s, two_theta_range=(0, 90))
calc.show_plot(s)
# %%
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.ndimage import gaussian_filter1d
f = interp1d(pat.x, pat.y, kind='linear')
xnew = np.linspace(20, 70, 1000)
plt.plot(xnew, f(xnew))
ynew = gaussian_filter1d(f(xnew), 10)
plt.plot(xnew, ynew)
plt.xlim(20, 70)
np.savetxt('/home/jinho93/xrd.dat', np.transpose([pat.x, pat.y]))
# %%
