#%%
from pymatgen import Structure
import os

from pymatgen.core.sites import Site

os.chdir('/home/jinho93/new/oxides/wurtzite/gan/pbe/from_samsung/VGa/far/test')

s = Structure.from_file('POSCAR')

i: Site
for n, i in enumerate(s.sites):
    if i.species_string == 'N':
        if s.get_distance(0,n) > 8:
            print(s.get_distance(0,n), i.coords)