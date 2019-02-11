from pymatgen import MPRester
from pymatgen.io.vasp.outputs import CompleteDos, Dos, Spin
import numpy as np
from pymatgen.electronic_structure.plotter import DosPlotter
mpr = MPRester('DhmFQPuibZo8JtXn')
dos: CompleteDos = mpr.get_dos_by_material_id('mp-352')
eldos = dos.get_element_dos()
dsp = DosPlotter()
dsp.add_dos_dict(eldos)
dsp.show(ylim=(0, 5))
arr = list()
arr.append(dos.energies - dos.efermi)
j: Dos
for i, j in eldos.items():
    arr.append(j.densities[Spin.up])
arr = np.array(arr)
np.savetxt('output.dat', arr.transpose(), fmt='%.9e', delimiter='    ')
