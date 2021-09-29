#%%

import numpy as np
from pymatgen.electronic_structure.core import Orbital, Spin
from pymatgen.electronic_structure.dos import Dos as preDos
from pymatgen.io.vasp import Vasprun

class pDos(preDos):
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
        return pDos(self.efermi, self.energies, densities)

vrun = Vasprun('vasprun.xml')

cdos = vrun.complete_dos


ds = [Orbital.dxy, Orbital.dyz, Orbital.dxz, Orbital.dx2, Orbital.dz2]

dos = {}
for orb in ds:
    dos[orb] = pDos(cdos.efermi, cdos.energies, {Spin.up: np.zeros_like(cdos.energies)})

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
    print(d, sum(j.densities[Spin.up][j.energies < 0]) * dx)