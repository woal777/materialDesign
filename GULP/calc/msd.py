#%%

from pymatgen import Molecule, Structure, Lattice
from pymatgen.analysis.diffusion_analyzer import DiffusionAnalyzer
import os

os.chdir('/home/jinho93/oxides/perobskite/lanthanum-aluminate/slab/gulp/stoichiometric/more')
# os.chdir('/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/slab/gulp/nostochio/La-vac')
with open('lao.xyz') as f:
    lines = f.readlines()

ss = []

atoms_number = 802
for i in range(len(lines) // atoms_number // 5):
    mole = Molecule.from_str(''.join(lines[atoms_number * i:atoms_number * (i + 1)]), fmt='xyz')
    l = Lattice([[15.2882,0,0], [0,15.2882, 0], [0,0,50]])
    s = Structure(l, mole.species, mole.cart_coords, coords_are_cartesian=True)
    ss.append(s)


from pymatgen.core import Element, Specie
d = DiffusionAnalyzer.from_structures(ss, 'La', 300, len(ss) // 2, step_skip=2)

d.get_msd_plot()
#%%
import numpy as np

np.savetxt('msd.dat', d.dt)