#%%

import numpy as np
from pymatgen.electronic_structure.core import Orbital, Spin
from pymatgen.electronic_structure.dos import Dos
from pymatgen.io.vasp import Vasprun

vrun = Vasprun('vasprun.xml')

cdos = vrun.complete_dos


ds = [Orbital.dxy, Orbital.dyz, Orbital.dxz, Orbital.dx2, Orbital.dz2]

dos = {}
for orb in ds:
    dos[orb] = Dos(cdos.efermi, cdos.energies, {Spin.up: np.zeros_like(cdos.energies)})

for i in vrun.final_structure.sites:
    if i.species_string == 'V':
        for key, values in dos.items():
            dos[key] = values.__add__(cdos.get_site_orbital_dos(i, key))
            

for d in dos.keys():
    dos[d].energies -= cdos.efermi

            
#%%
import matplotlib.pyplot as plt

plt.xlim((-2, 4))
n = 0
for d, j in dos.items():
    plt.plot(j.energies, j.densities[Spin.up] + n, label=d)
plt.legend()
plt.show()
# %%
for n, k in dos.items():
    with open(f'{n}.dat', 'w') as f:
        f.write(k.__str__())

#%%
dx = cdos.energies[1] - cdos.energies[0]
for d, j in dos.items():
    print(d, sum(j.densities[Spin.up][np.logical_and(j.energies < 0, -2 < j.energies)]) * dx)