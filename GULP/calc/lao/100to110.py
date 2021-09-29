#%%

import math
from pymatgen import Structure, Molecule, Lattice
import os

os.chdir('/home/jinho93/oxides/perobskite/lanthanum-aluminate/slab/gulp/nonstochio/La-vac/two')

m = Molecule.from_file('tail.xyz')
l = Lattice.from_lengths_and_angles([11.46615, 15.2882, 50], [90, 90, 90])

s = Structure(l, m.species, m.cart_coords, coords_are_cartesian=True)
s.make_supercell([[4, 0, 0], [0, 3, 0], [0, 0, 1]])
s.make_supercell([[1, 1, 0], [1, -1, 0], [0, 0, 1]])
s.sort()
# ll = Lattice.from_lengths_and_angles([s.lattice.a / 2, s.lattice.b / 2, s.lattice.c], s.lattice.angles)
ll = Lattice.from_lengths_and_angles(s.lattice.abc, s.lattice.angles)
s = Structure(ll, s.species, s.cart_coords, coords_are_cartesian=True)

indi = []
for i, site in enumerate(s.sites):
    if site.x + site.y < ll.b / math.sqrt(2):
        indi.append(i)


# s.remove_sites(indi)

# s = Structure(ll, s.species, s.cart_coords, coords_are_cartesian=True)

# s.to('POSCAR', 'POSCAR')
s.to('POSCAR', 'CONTCAR')

