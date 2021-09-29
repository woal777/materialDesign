#%%
from pymatgen.core.lattice import Lattice
from pymatgen.io.xyz import XYZ
from pymatgen import Structure
from pymatgen.analysis.diffusion_analyzer import DiffusionAnalyzer
import os
import numpy as np

os.chdir('/home/jinho93/oxides/wurtzite/zno/cp2k/1.aimd/3.16A/30/3.fix')
x = XYZ.from_file('526.xyz')

lat = Lattice(np.diag([16.02, 16.67, 40.67]))
s = [Structure(lat, r.species, r.cart_coords,  coords_are_cartesian=True) for r in x.all_molecules]
#%%
from pymatgen.analysis.diffusion_analyzer import DiffusionAnalyzer

d = DiffusionAnalyzer.from_structures(s, 'Zn', 600, 500, 2)
d.get_msd_plot()