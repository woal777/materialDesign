#%%
from pymatgen.electronic_structure.dos import Dos, Spin, add_densities
import numpy as np
from pymatgen.core.sites import Site
from pymatgen.io.vasp import Vasprun
import os

def write_dos(dos: Dos, filename='output.dat'):
    arr = np.zeros((len(dos.energies), 2))
    arr[:, 0] = dos.energies - dos.efermi
    arr[:, 1] = dos.densities[Spin.up]
    np.savetxt(filename, arr)

def ldos(vrun):
    structure = vrun.final_structure

    cdos = vrun.complete_dos
    num = 10
    cmin = .178
    cmax = .703
    dis = (cmax - cmin) / num
    sites = [site for site in structure.sites if cmin < site.c < cmax]
    # sites.pop(0)
    zdos = {}
    s: Site
    for i, s in enumerate(sorted(sites, key=lambda l: l.c)):
        num = (s.c - cmin) / dis
        num = int(num)
        print(num)
        if num not in zdos:
            zdos[num] = cdos.get_site_dos(s).densities
        else:
            zdos[num] = add_densities(zdos[num], cdos.get_site_dos(s).densities)

    arr = [cdos.energies - cdos.efermi]
    for num in zdos.values():
        arr.append(num[Spin.up])

    return arr

if __name__ == '__main__':
    
    os.chdir('/home/jinho93/new/oxides/wurtzite/zno/vasp/hse/normal/post-hse/sigma')
    vrun = Vasprun('vasprun.xml')
    arr = ldos(vrun)
    arr = np.transpose(arr)
    np.savetxt('/home/jinho93/arr.dat', arr)
# %%
