#%%
from matplotlib.pyplot import xlim
import numpy as np
from pymatgen.core.sites import Site
from pymatgen.electronic_structure.core import Spin
from pymatgen.io.vasp.outputs import Vasprun, Element
from pymatgen.electronic_structure.plotter import DosPlotter
import os

os.chdir('/home/jinho93/oxides/perobskite/lanthanum-aluminate/slab/14/asym')
os.chdir('/home/jinho93/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/stengel/001/vca/AlO2')
os.chdir('/home/jinho93/oxides/perobskite/lanthanum-aluminate/slab/14/asym/to_Al')
# os.chdir('/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/slab/7')
vrun = Vasprun('vasprun.xml')
cdos = vrun.complete_dos
s = vrun.final_structure

dsp = DosPlotter()

dos_dict = {}
i: Site
for n, i in enumerate(s.sites):
    if i.species_string == 'La':
        dos_dict[f'{n}'] = cdos.get_site_dos(i)

dsp.add_dos_dict(dos_dict)

dsp.show(xlim=(-10, 5), ylim=(0, 2))

# %%

aldos = cdos.get_site_dos(s.sites[0])
dx = aldos.energies[1] - aldos.energies[0]
o = np.sum(aldos.get_densities(Spin.up)[np.logical_and(aldos.energies > -2, aldos.energies < 0)]) * dx
print(o)
# %%
