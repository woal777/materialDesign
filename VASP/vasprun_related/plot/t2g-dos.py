#%%

import numpy as np
from pymatgen.electronic_structure.core import Spin
from pymatgen.electronic_structure.plotter import DosPlotter
from pymatgen.io.vasp import Vasprun
from pymatgen import Site
from pymatgen.electronic_structure.dos import Dos


vrun = Vasprun('vasprun.xml')

cdos = vrun.complete_dos

atoms = []
i: Site

dos = {'t2g': Dos(cdos.efermi, cdos.energies, {Spin.up: np.zeros_like(cdos.energies)}),
       'e_g': Dos(cdos.efermi, cdos.energies, {Spin.up: np.zeros_like(cdos.energies)})}


for i in vrun.final_structure.sites:
    if i.species_string == 'V':
        for n, k in dos.items():
            dos[n] = k.__add__(cdos.get_site_t2g_eg_resolved_dos(i)[n])

for d in dos.keys():
    dos[d].energies -= cdos.efermi
    

# %%
for n, k in dos.items():
    with open(f'{n}.dat', 'w') as f:
        f.write(k.__str__())

#%%
import matplotlib.pyplot as plt

plt.xlim((-2, 4))
for d, j in dos.items():
    plt.plot(j.energies, j.densities[Spin.up], label=d)

plt.legend()
plt.show()