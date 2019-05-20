#!/home/jinho93/miniconda3/envs/my_pymatgen/bin/python
from pymatgen.io.vasp.outputs import Vasprun, Spin
import os
import numpy as np

if __name__ == '__main__':
    vrun = Vasprun('vasprun.xml')
    s = vrun.final_structure
    left = 9
    right = 8
    dos_arr = np.zeros((left + right + 1, len(vrun.tdos.densities[Spin.up])))
    dos_arr[0] = (vrun.tdos.energies - vrun.tdos.efermi)
    l_ini = np.array([0.0525 * r for r in range(left)])
    r_fin = l_ini + 0.06
    print(l_ini)
    print(r_fin)
    for i in s.sites:
        for j in range(left):
            if l_ini[j] <= i.c < r_fin[j]:
                dos_arr[j + 1] += vrun.complete_dos.get_site_dos(i).densities[Spin.up]
                dos_arr[j + 1] += vrun.complete_dos.get_site_dos(i).densities[Spin.down]

    l_ini = np.array([0.0545 * r for r in range(right)]) + .5059
    r_fin = l_ini + 0.0885
    print(l_ini)
    print(r_fin)
    for i in s.sites:
        for j in range(right):
            if l_ini[j] <= i.c < r_fin[j]:
                dos_arr[j + left + 1] += vrun.complete_dos.get_site_dos(i).densities[Spin.up]
                dos_arr[j + left + 1] += vrun.complete_dos.get_site_dos(i).densities[Spin.down]

    np.savetxt('output.dat', dos_arr.transpose(), '%16.8E')
