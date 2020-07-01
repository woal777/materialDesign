from pymatgen import Spin
from pymatgen.io.vasp import Vasprun
import numpy as np

vrun = Vasprun('vasprun.xml')
s = vrun.final_structure
cdos = vrun.complete_dos
arr = [np.concatenate((cdos.energies - cdos.efermi, (cdos.energies - cdos.efermi)[::-1]))]
for i in s.sites:
    tmp = np.concatenate((cdos.get_site_dos(i).densities[Spin.up], -cdos.get_site_dos(i).densities[Spin.down][::-1]))
    arr.append(tmp)

arr = np.array(arr)
np.savetxt('output.dat', arr.transpose())
