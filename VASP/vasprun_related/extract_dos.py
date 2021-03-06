#!/home/jinho93/miniconda3/envs/my_pymatgen/bin/python
from pymatgen.io.vasp.outputs import CompleteDos, Dos, Spin, Vasprun
import numpy as np

normalize = False
vrun = Vasprun('vasprun.xml')
# mpr = MPRester('DhmFQPuibZo8JtXn')
dos = vrun.complete_dos
# dos: CompleteDos = mpr.get_dos_by_material_id('mp-352')
eldos = dos.get_element_dos()
arr = list()
if vrun.is_spin:
    arr.append(np.concatenate((dos.energies - dos.efermi,
                               np.flip(dos.energies) - dos.efermi)))
    arr.append(np.concatenate((vrun.tdos.densities[Spin.up],
                               np.flip(-vrun.tdos.densities[Spin.down]))))
else:
    arr.append(dos.energies - dos.efermi)
    arr.append(vrun.tdos)

j: Dos
items = ['tot']

for i, j in eldos.items():
    items.append(str(i))
    if vrun.is_spin:
        if normalize:
            arr.append(np.concatenate((j.densities[Spin.up] / max(j.get_densities(Spin.up)),
                                   np.flip(-j.densities[Spin.down]) / max(j.get_densities(Spin.down)))))
        else:
            arr.append(np.concatenate((j.densities[Spin.up],
                                       np.flip(-j.densities[Spin.down]))))
    else:
        if normalize:
            arr.append(j.densities[Spin.up] / max(j.get_densities(Spin.up)))
        else:
            arr.append(j.densities[Spin.up])
arr = np.array(arr)
np.savetxt('output.dat', arr.transpose(), fmt='%.9e', delimiter='    ', header=' '.join(items))
