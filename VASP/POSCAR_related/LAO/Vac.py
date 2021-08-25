#%%
from typing import List, Tuple
from pymatgen import Structure
import os

from pymatgen.core.sites import Site

os.chdir('/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/slab/7/L2O1/input')

structure = Structure.from_file('POSCAR')

la:List[Site] = []
o = []
# print(dir(structure.sites[0]))
for site in structure.sites:
    if site.c > .78 and site.species_string == "La":
        la.append(site)
    elif .74 >site.c > .73 and site.species_string == "O":
        o.append(site)

images1 = []
dis = []
for l in la[1:]:
    if round(la[0].distance(l), 2) not in dis:
        dis.append(round(la[0].distance(l), 2))
        images1.append([la[0], l])

# print(dis)

nei: Site
for nei, dis in structure.get_neighbors_in_shell(
    (la[0].coords + la[1].coords) / 2, 0, 5):
    if 25 > nei.z > 24 and nei.species_string == "O":
        print(dis)