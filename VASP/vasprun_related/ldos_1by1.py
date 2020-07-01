from math import ceil

from pymatgen import Spin
from pymatgen.io.vasp.outputs import Vasprun
import numpy as np
import os

if __name__ == '__main__':
    os.chdir('/home/jinho93/interface/pzt-bso/loose/opti/dos')
    vrun = Vasprun('vasprun.xml')
    s = vrun.final_structure
    cdos = vrun.complete_dos
    n = 0
    for i in s.sites:
        if i.species_string == 'O':
            n += 1
    n = ceil(n / 3)
    if vrun.is_spin:
        dos_arr = np.zeros((n + 1, len(vrun.tdos.densities[Spin.up]) * 2))
        dos_arr[0] = np.concatenate(((vrun.tdos.energies - vrun.tdos.efermi), (vrun.tdos.energies - vrun.tdos.efermi)[::-1]))
    else:
        dos_arr = np.zeros((n + 1, len(vrun.tdos.densities[Spin.up])))
        dos_arr[0] = (vrun.tdos.energies - vrun.tdos.efermi)
    for i, j in enumerate(sorted([r for r in s.sites if r.species_string != 'Zr'], key=lambda site: site.z)):
        # if not i % 5 == 0 or i % 5 == 1:
        if vrun.is_spin:
            dos_arr[i // 5 + 1] += np.concatenate((cdos.get_site_dos(j).densities[Spin.up], -cdos.get_site_dos(j).densities[Spin.down][::-1]))
        else:
            if i % 5 == 4:
                print(j.species_string, end='\n')
            else:
                print(j.species_string, end='\t')
            dos_arr[i // 5 + 1] += cdos.get_site_dos(j).get_smeared_densities(.15)[Spin.up]

    np.savetxt('output.dat', dos_arr.transpose(), '%16.8E', delimiter='\t')

    # oxygen = sorted([r for r in s.sites if r.species_string == 'O'], key= lambda site: site.z)
    # asite = sorted([r for r in s.sites if r.species_string == 'Ti' or r.species_string == 'Mn'], key= lambda site: site.z)
