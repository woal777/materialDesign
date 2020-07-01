#!/home/jinho93/miniconda3/envs/my_pymatgen/bin/python
from pymatgen.io.vasp.outputs import Vasprun, Spin
import os
import numpy as np

if __name__ == '__main__':
    vrun = Vasprun('vasprun.xml')
    s = vrun.final_structure
    cdos = vrun.complete_dos

#    spacing = 0.04
    dos_arr = np.zeros((13 + 1, len(vrun.tdos.densities[Spin.up])))
    dos_arr[0] = (vrun.tdos.energies - vrun.tdos.efermi)
    # l_ini = np.array([spacing * r - 1/ left / 2 for r in range(left)])
    l_ini = np.linspace(.12, .88, 13)[:-1]
    r_fin = np.linspace(.12, .88, 13)[1:]
#    l_ini = np.array([.19, .24, .29, .34, .40, .46, .52, .57, .62])
#     r_fin = l_ini + spacing
#     print(l_ini)
#     print(r_fin)
    for i in s.sites:
        for j in range(len(l_ini)):
            if l_ini[j] <= i.c < r_fin[j]:
                dos_arr[j + 1] += cdos.get_site_dos(i).densities[Spin.up]
                if vrun.is_spin:
                    dos_arr[j + 1] += cdos.get_site_dos(i).densities[Spin.down]
    np.savetxt('output.dat', dos_arr.transpose(), '%16.8E')
#    l_ini = np.array([spacing * r for r in range(right)]) + .499
#    l_ini = []
#    r_fin = l_ini + spacing
#    print(l_ini)
'''   for i in s.sites:
        for j in range(len(l_ini)):
            if l_ini[j] <= i.c < r_fin[j]:
                dos_arr[j + left + 1] += cdos.get_site_dos(i).densities[Spin.up]
                if vrun.is_spin:
                    dos_arr[j + left + 1] += cdos.get_site_dos(i).densities[Spin.down]
'''
