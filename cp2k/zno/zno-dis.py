#%%
from pymatgen.core.sites import Site
from pymatgen.io.xyz import XYZ
import os

os.chdir('/home/jinho93/oxides/wurtzite/zno/cp2k/1.aimd/3.16A/30/3.fix/output')
xyz = XYZ.from_file('zno-pos-1.xyz')


coords = []
for m in xyz.all_molecules:
    s: Site
    tmp = []
    for s in m.sites:
        if s.species_string == 'Zn':
            tmp.append(s.z)
    coords.append(tmp)
    

# %%
import numpy as np

coords = np.array(coords)
print(coords.shape)

#%%
import matplotlib.pyplot as plt

for i in range(coords.shape[1]):
    plt.plot(coords[:,i], color='black')

plt.ylim((18, 30))
plt.xlim((0, 200))
