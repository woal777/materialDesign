#%%
from pymatgen.io.vasp import Locpot
import numpy as np
import matplotlib.pyplot as plt
import os

os.chdir('/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/my015/from-gulp/lvhar')
os.chdir('/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/stengel/015/4/lvhar')
loc = Locpot.from_file('LOCPOT')

#%%
dat = np.sum(loc.data['total'], axis=0) / loc.dim[0]
dat = np.roll(dat, int(loc.dim[1] * 0.8) // 2, axis=0)
dat = np.roll(dat, -10, axis=1)

# %%
import scipy.ndimage as nd
fft = np.fft.fft2(dat)

gaus = nd.gaussian_filter(fft.imag, sigma=10)
plt.imshow(gaus)

#%%
criteria = 1e-4
fft2 = np.where(np.abs(fft.real) > np.max(fft.real) * criteria, 0, fft)
fft2 = np.where(np.abs(fft.imag) > np.max(fft.imag) * criteria, 0, fft2)
# print(np.where(np.abs(fft.imag) > np.max(fft.imag) * 0.7))
ifft = np.fft.ifft2(fft2)

plt.imshow(ifft.real)

# %%
