#%%

from pymatgen import Molecule, Structure
import os
import numpy as np
from pymatgen.core.lattice import Lattice

os.chdir('/home/jinho93/oxides/perobskite/lanthanum-aluminate/slab/nvt.para.6/island/len-19/step1')

s = Molecule.from_file('POSCAR.xyz')
sp = []
coords = []
for i in s.sites:
    if i.x < 7 and i.y < 7:
        sp.append(i.specie)
        coords.append(i.coords)
        
new = Structure(Lattice(np.identity(3) * 7.648200),sp, coords, coords_are_cartesian=True)
new.to('POSCAR', 'ini_pot/reduced')

# %%

#%%

from pymatgen.command_line.gulp_caller import GulpIO
gio = GulpIO()
gio.buckingham_input(new, keywords=['conv'], uc=False)

# %%
