from math import ceil

from pymatgen import Spin
from pymatgen.io.vasp.outputs import Vasprun
import numpy as np
import os

if __name__ == '__main__':
    vrun = Vasprun('vasprun.xml')
    s = vrun.final_structure
    cdos = vrun.complete_dos
    n = 0
    for i in s.sites:
        if i.species_string == 'O':
            n += 1
    n = ceil(n / 3)
    repeat = 5
    if repeat == 4:
        n = 4
    if vrun.is_spin:
        dos_arr = np.zeros((n + 1, len(vrun.tdos.densities[Spin.up]) * 2))
        dos_arr[0] = np.concatenate(((vrun.tdos.energies - vrun.tdos.efermi), (vrun.tdos.energies - vrun.tdos.efermi)[::-1]))
    else:
        dos_arr = np.zeros((n + 1, len(vrun.tdos.densities[Spin.up])))
        dos_arr[0] = (vrun.tdos.energies - vrun.tdos.efermi)
    if n == 4:
        atoms = [r for r in s.sites if r.species_string == 'Pt'][2:]
    else:
        atoms = [r for r in s.sites if r.species_string != 'Pt' and r.species_string != 'Sr' and r.species_string != 'Ar']

    for i, j in enumerate(sorted(atoms, key=lambda site: site.z)):
        if i == 0:
            continue
        i -= 1
        # if not i % 5 == 0 or i % 5 == 1:
        if vrun.is_spin:
            dos_arr[i // repeat + 1] += np.concatenate((cdos.get_site_dos(j).densities[Spin.up], -cdos.get_site_dos(j).densities[Spin.down][::-1]))
            if i % repeat == repeat - 1:
                print(j.species_string, end='\n')
            else:
                print(j.species_string, end='\t')
        else:
            dos_arr[i // repeat + 1] += cdos.get_site_dos(j).densities[Spin.up]
            if i % repeat == repeat - 1:
                print(j.species_string, end='\n')
            else:
                print(j.species_string, end='\t')
    if repeat == 4:
        np.savetxt('pt.dat', dos_arr.transpose(), '%16.8E', delimiter='\t')
    else:
        np.savetxt('lsmo.dat', dos_arr.transpose(), '%16.8E', delimiter='\t')
    # oxygen = sorted([r for r in s.sites if r.species_string == 'O'], key= lambda site: site.z)
    # asite = sorted([r for r in s.sites if r.species_string == 'Ti' or r.species_string == 'Mn'], key= lambda site: site.z)
