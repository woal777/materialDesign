#%%
import numpy
from pymatgen.core.sites import Site
from pymatgen.electronic_structure.core import Spin
from pymatgen.electronic_structure.dos import add_densities
from pymatgen.io.vasp import Vasprun
import os


os.chdir('/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/my015/from-gulp/421/locpot')
# os.chdir('/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/my015/4/lvhar')
vrun = Vasprun('vasprun.xml')
structure = vrun.final_structure

cdos = vrun.complete_dos

sites = []
cdos.get_element_dos()
site: Site
for site in structure.sites:
    if .111 < site.b < .3:
    # if .16 < site.b < .35:
        sites.append(site)
        
sites.sort(key=lambda s: s.z, reverse=True)
sites = sites[4:-2]
print(len(sites))
zdos = {}
s: Site
for i, s in enumerate(sites):
    if i // 10 not in zdos:
        print(i)
        zdos[i // 10] = cdos.get_site_dos(s).densities
    else:
        zdos[i // 10] = add_densities(zdos[i // 10], cdos.get_site_dos(s).densities)
    print(s.z / structure.lattice.c, s.species_string)

arr = [cdos.energies - cdos.efermi]
for i in zdos.values():
    arr.append(i[Spin.up])

numpy.savetxt('/home/jinho93/dos-z.dat', numpy.transpose(arr))

# cdos.get_site_dos(s.sites)
# %%
