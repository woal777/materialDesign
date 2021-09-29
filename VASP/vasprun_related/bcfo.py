#%%
from pymatgen.electronic_structure.core import Spin
from pymatgen.io.vasp import Vasprun
import numpy as np
import os

os.chdir('/home/jinho93/new/oxides/perobskite/bfo/bcfo/dos')
os.chdir('/home/jinho93/new/oxides/perobskite/bfo/bcfo/opti/222')
vrun = Vasprun('vasprun.xml')

cdos = vrun.complete_dos
sitedos = []
n = 0
arr = sorted(vrun.final_structure.sites, key=lambda site: site.c)
# arr = arr[-4:] + arr[:-4]
print(arr[:4])
for s in arr:
    sitedos.append(cdos.get_site_dos(s).densities)
    n += 1
    if n == 24:
        sitedos.append({Spin.up:np.zeros(len(cdos.energies)), Spin.down:np.zeros(len(cdos.energies))})

layerdos = []
tmp_dos = {Spin.up:np.zeros(len(cdos.energies)), Spin.down:np.zeros(len(cdos.energies))}
for s in range(len(sitedos)):
    tmp_dos[Spin.down] += sitedos[s][Spin.down]
    tmp_dos[Spin.up] += sitedos[s][Spin.up]
    if s % 20 == 19:
        layerdos.append(tmp_dos)
        tmp_dos = {Spin.up:np.zeros(len(cdos.energies)), Spin.down:np.zeros(len(cdos.energies))}
    

# %%



for en, l in enumerate(layerdos):
    output = [cdos.energies - cdos.efermi, (l[Spin.up] + layerdos2[en][Spin.up]) / 2, (-l[Spin.down] - layerdos2[en][Spin.down]) / 2]
    np.savetxt(f'{en}_2.dat', np.transpose(output))

# %%
