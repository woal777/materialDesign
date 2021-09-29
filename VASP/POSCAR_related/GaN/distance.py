#%%
from pymatgen import Structure
import os

from pymatgen.core.sites import Site

os.chdir('/home/jinho93/nitrides/gan/pbe/pair')
s = Structure.from_file('POSCAR')

site: Site
dis = []
for i, site in enumerate(s.sites):
    if site.species_string == 'N':
        dis.append([s.get_distance(i, 0), site])
        # print(s.get_distance(i, 0),site.coords)
        
print(max(dis, key= lambda x: x[0]))