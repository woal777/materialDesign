#%%
from pymatgen.core.structure import Structure
from pymatgen.io.vasp import Xdatcar
import numpy as np
import os


os.chdir('/home/jinho93/tmdc/WTe2/noelect/novdw/from_paper/MD')
xdat = Xdatcar.from_file('XDATCAR')

coords = [s.frac_coords for s in xdat.structures]

coords = np.array(coords)
coords = np.sum(coords, axis=0) / 100
print(coords.shape)

si: Structure = xdat.structures[0]
s = Structure(si.lattice, si.species, coords)

s.to('POSCAR', 'new-POSCAR')
