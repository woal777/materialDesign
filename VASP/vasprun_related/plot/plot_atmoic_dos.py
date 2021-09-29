import os
from pymatgen.electronic_structure.plotter import DosPlotter
from pymatgen.io.vasp.outputs import Vasprun, Element, Spin
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
        return pDos(self.efermi, self.energies, densities)

vrun = Vasprun('vasprun.xml')
# mpr = MPRester('DhmFQPuibZo8JtXn')
dos = vrun.complete_dos
# dos: CompleteDos = mpr.get_dos_by_material_id('mp-352')
eldos = dos.get_element_dos()
eldos['total'] = vrun.tdos

#eldos.pop(Element.Mo)
#eldos.pop(Element.S)
dsp = DosPlotter()
dsp.add_dos_dict(eldos)
dsp.show(xlim=(-3, 5))
for d in eldos.keys():
    eldos[d].energies -= dos.efermi

for n, k in eldos.items():
    k = Dos(k.efermi, k.energies, k.densities)
    with open(f'{n}.dat', 'w') as f:
        f.write(k.__str__())
