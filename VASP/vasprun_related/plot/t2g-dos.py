#%%

import numpy as np
from pymatgen.electronic_structure.core import Spin
from pymatgen.electronic_structure.plotter import DosPlotter
from pymatgen.io.vasp import Vasprun
from pymatgen import Site
from pymatgen.electronic_structure.dos import Dos as preDos

class Dos(preDos):
    def __init__(self, efermi, energies, densities):
        super().__init__(efermi, energies, densities)
        
    def __str__(self):
        print('overriding')
        if Spin.down in self.densities:
            stringarray= []
            for i, energy in enumerate(self.energies):
                stringarray.append("{:.5f} {:.5f} {:.5f}"
                                   .format(energy, self.densities[Spin.up][i],
                                           self.densities[Spin.down][i]))
        else:
            stringarray= []
            for i, energy in enumerate(self.energies):
                stringarray.append("{:.5f} {:.5f}"
                                   .format(energy, self.densities[Spin.up][i]))
        return "\n".join(stringarray)

    def __add__(self, other):
        """
        Adds two DOS together. Checks that energy scales are the same.
        Otherwise, a ValueError is thrown.

        Args:
            other: Another DOS object.

        Returns:
            Sum of the two DOSs.
        """
        if not all(np.equal(self.energies, other.energies)):
            raise ValueError("Energies of both DOS are not compatible!")
        densities = {spin: self.densities[spin] + other.densities[spin]
                     for spin in self.densities.keys()}
        return Dos(self.efermi, self.energies, densities)


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