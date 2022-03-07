#%%
import numpy
from pymatgen.core.sites import Site
from pymatgen.electronic_structure.core import Spin
from pymatgen.electronic_structure.dos import add_densities
from pymatgen.io.vasp import Vasprun
import os


os.chdir('/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/stengel/015/4/lvhar')

vrun = Vasprun('vasprun.xml')
structure = vrun.final_structure

cdos = vrun.complete_dos

zdos = {}
s: Site
for i, s in enumerate(sorted(structure.sites, key=lambda l: l.c)):
    num = (s.c - 0.23) // 0.13
    print(s.c, num)
    if num not in zdos:
        zdos[num] = cdos.get_site_dos(s).densities
    else:
        zdos[num] = add_densities(zdos[num], cdos.get_site_dos(s).densities)

arr = [cdos.energies - cdos.efermi]
for i in zdos.values():
    arr.append(i[Spin.up])

numpy.savetxt('/home/jinho93/dos-z.dat', numpy.transpose(arr))

# %%
