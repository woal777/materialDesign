#%%
import numpy
from pymatgen.core.sites import Site
from pymatgen.electronic_structure.core import Spin
from pymatgen.electronic_structure.dos import add_densities
from pymatgen.io.vasp import Vasprun
import os


os.chdir('/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/stengel/015/4/lvhar/dense')
os.chdir('/home/jinho93/new/oxides/wurtzite/zno/vasp/hse/normal/post-hse/sigma')
# os.chdir('/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/my015/4/lvhar/dense')
vrun = Vasprun('vasprun.xml')
structure = vrun.final_structure

cdos = vrun.complete_dos
sites = [site for site in structure.sites if .178 < site.b < .703]
# sites.pop(0)
zdos = {}
s: Site
for i, s in enumerate(sorted(sites, key=lambda l: l.c)):
    num = i // 10
    print(num)
    if num not in zdos:
        zdos[num] = cdos.get_site_dos(s).densities
    else:
        zdos[num] = add_densities(zdos[num], cdos.get_site_dos(s).densities)

arr = [cdos.energies - cdos.efermi]
for num in zdos.values():
    arr.append(num[Spin.up])

numpy.savetxt('/home/jinho93/dos-z.dat', numpy.transpose(arr))

# %%
