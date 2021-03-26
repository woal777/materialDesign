#%%

import numpy as np
from pymatgen.electronic_structure.core import Orbital, Spin
from pymatgen.electronic_structure.plotter import DosPlotter
from pymatgen.io.vasp import Vasprun
from pymatgen import Site
from pymatgen.electronic_structure.dos import Dos
import os

dsp = DosPlotter()

vrun = Vasprun('vasprun.xml')

cdos = vrun.complete_dos

atoms = []
i: Site

dos = {'d_in': Dos(cdos.efermi, cdos.energies, {Spin.up: np.zeros_like(cdos.energies)}),
       'd_out': Dos(cdos.efermi, cdos.energies, {Spin.up: np.zeros_like(cdos.energies)})}


for i in vrun.final_structure.sites:
    if i.species_string == 'V':
        atoms.append(i)
for j in atoms:
    for n, k in dos.items():
        if n == 'd_in':
            dos[n] = k.__add__(cdos.get_site_orbital_dos(j, Orbital.dxy))
        else:
            dos[n] = k.__add__(cdos.get_site_orbital_dos(j, Orbital.dyz))
            dos[n] = k.__add__(cdos.get_site_orbital_dos(j, Orbital.dxz))        


dsp.add_dos_dict(dos)
dsp.show()    

    

# %%
for n, k in dos.items():
    with open(f'{n}.dat', 'w') as f:
        f.write(k.__str__())
