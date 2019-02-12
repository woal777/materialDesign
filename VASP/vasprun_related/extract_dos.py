from pymatgen import MPRester
from pymatgen.io.vasp.outputs import CompleteDos, Dos, Spin, Vasprun
import numpy as np
from pymatgen.electronic_structure.plotter import DosPlotter
import os
os.chdir('/home/jinho93/molecule/oep-sub_fe/110/cooep/1-mol/dos')
vrun = Vasprun('vasprun.xml')
# mpr = MPRester('DhmFQPuibZo8JtXn')
dos = vrun.complete_dos
# dos: CompleteDos = mpr.get_dos_by_material_id('mp-352')
eldos = dos.get_element_dos()
dsp = DosPlotter()
dsp.add_dos_dict(eldos)
dsp.show(xlim=(-20, 5))
arr = list()
if vrun.is_spin:
    arr.append(np.concatenate((dos.energies - dos.efermi,
                               np.flip(dos.energies) - dos.efermi)))
else:
    arr.append(dos.energies - dos.efermi)
j: Dos
items = []
for i, j in eldos.items():
    items.append(str(i))
    if vrun.is_spin:
        arr.append(np.concatenate((j.densities[Spin.up] / max(j.get_densities(Spin.up)),
                                   np.flip(-j.densities[Spin.down]) / max(j.get_densities(Spin.down)))))
    else:
        arr.append(j.densities[Spin.up] / max(j.get_densities(Spin.up)))
arr = np.array(arr)
np.savetxt('output.dat', arr.transpose(), fmt='%.9e', delimiter='    ', header=' '.join(items))
