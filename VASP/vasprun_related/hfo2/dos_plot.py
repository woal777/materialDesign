#%%
from ast import Str
import os
import numpy as np
import matplotlib.pyplot as plt

# os.chdir('/home/jinho93/interface/tin-hfo2/2.strain2tin/1.Cdoped/2.carbon/2.dos/ismear0')
os.chdir('/home/jinho93/interface/tin-hfo2/2.strain2tin/1.Cdoped/3.down_carbon/2.opti/2.dos/ismear0')
arr = np.genfromtxt('output.dat')

fig, ax = plt.subplots(1, arr.shape[1] - 1, sharex='all', sharey='all')

for i in range(1, arr.shape[1]):
    ax[i - 1].plot(arr[:,i], arr[:,0])

plt.xlim((0, 1))
plt.ylim((-1, 4))
plt.subplots_adjust(hspace=0, wspace=0)
plt.show()

#%%
from pymatgen import Structure

s = Structure.from_file('POSCAR')
print([r for r in s.sites if r.species_string=='C'])