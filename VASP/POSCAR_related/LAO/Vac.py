#%%
from typing import List, Tuple
from pymatgen import Structure
import os

from pymatgen.core.sites import Site

os.chdir('/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/slab/7/L2O1/input')

structure = Structure.from_file('POSCAR')
sites = structure.sites
la:List[Site] = []
o = []
# print(dir(structure.sites[0]))
for i, site in enumerate(sites):
    if site.c > .78 and site.species_string == "La":
        la.append(i)
    elif .74 >site.c > .73 and site.species_string == "O":
        o.append(i)

images1 = []
dis1 = []
for l in la[1:]:
    if round(sites[la[0]].distance(sites[l]), 2) not in dis1:
        dis1.append(round(sites[la[0]].distance(sites[l]), 2))
        images1.append([la[0], l])

# print(dis)

nei: Site
images2 = []
for i in images1:
    dis2 = []
    site: Site
    for j, site in enumerate(sites):
        dis = site.distance_from_point(sites[i[0]].coords + sites[i[1]].coords) / 2
        if 25 > site.z > 24 and site.species_string == "O":
            if round(dis, 2) not in dis2:
                dis2.append(round(dis, 2))
                images2.append([*i, j])
#%%
s: Site

for i, img in enumerate(images2):
    tmp = []
    for j, s in enumerate(sites):
        if s.z < 10:
            for sym in img:
                if s.x == sites[sym].x and s.y == sites[sym].y:
                    tmp.append(j)
    images2[i].extend(tmp)

print(len(images2))

# %%
import copy
import os
for i, img in enumerate(images2):
    s2 = copy.deepcopy(structure)
    s2.remove_sites(img)
    # os.mkdir(str(i))
    s2.to('POSCAR', f'{i}/POSCAR')
    print(img)
# %%

print(images2)