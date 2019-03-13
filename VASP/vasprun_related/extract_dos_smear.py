from pymatgen.io.vasp.outputs import CompleteDos, Dos, Spin, Vasprun
import numpy as np
import os

normalize = False
os.chdir('/home/backup/jinho93/molecule/DDT/moli/top/relax/re/dos/dense/morebands')
vrun = Vasprun('vasprun.xml')
# mpr = MPRester('DhmFQPuibZo8JtXn')
dos = vrun.complete_dos
# dos: CompleteDos = mpr.get_dos_by_material_id('mp-352')
eldos = dos.get_element_dos()
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
        if normalize:
            arr.append(np.concatenate((j.get_smeared_densities(0.05)[Spin.up] / max(j.get_smeared_densities(0.05)[Spin.up]),
                                   np.flip(-j.get_smeared_densities(0.05)[Spin.down]) / max(j.get_smeared_densities(0.05)[Spin.down]))))
        else:
            arr.append(np.concatenate((j.get_smeared_densities(0.05)[Spin.up],
                                       np.flip(-j.get_smeared_densities(0.05)[Spin.up]))))
    else:
        if normalize:
            arr.append(j.get_smeared_densities(0.05)[Spin.up] / max(j.get_smeared_densities(0.05)[Spin.up]))
        else:
            arr.append(j.get_smeared_densities(0.05)[Spin.up])
arr = np.array(arr)
np.savetxt('output.dat', arr.transpose(), fmt='%.9e', delimiter='    ', header=' '.join(items))
