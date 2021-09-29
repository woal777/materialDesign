#%%

from pymatgen import Structure, Molecule
from pymatgen.io.xyz import XYZ

import os

os.chdir('/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/stengel/013/from_gulp/all')
os.chdir('/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/periodic_step/gulp/013/all')
xyz = XYZ.from_file('lao.xyz')

tmp = Structure.from_file('POSCAR')

for m in xyz.all_molecules[:1]:
    s = Structure(tmp.lattice, m.species, m.cart_coords, coords_are_cartesian=True)
    prim = s.get_primitive_structure(1e-1)
    if len(prim.sites) < 540:
        print(len(prim.sites))
        out_str = s


s.to('POSCAR', 'NPOSCAR')

print(len(s.sites))
print(len(prim.sites))