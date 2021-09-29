#%%
from pymatgen import Structure
from pymatgen.core.sites import Site
import random
import os
import numpy as np

os.chdir('/home/jinho93/arsnide/ZnAs/circular')
nloop = 0
while True:
    nloop += 1
    s = Structure.from_file('POSCAR333')
    nzn = 0
    nas = 0
    site : Site
    for site in s.sites:
        if site.species_string == 'Zn':
            nzn += 1
        else:
            nas += 1

    ran = random.sample(range(nas, nas + nzn), nzn // 4)
    his = np.histogram(ran, 216 // 6, range=(nas, nas + nzn))[0]
    if 4 in his:
        continue
        # continue
    s.remove_sites(ran)

    nei = s.get_all_neighbors(2.7, sites=s.sites)
    nei_num = [len(r) for r in nei]
    if 3 in nei_num:
        continue
    if 2 in nei_num:
        continue
    print(his)
    print(nei_num)
    print(nloop)
    # for site in s.sites:
    #     if site.species_string == 'As':
    #         if len(s.get_neighbors(site, 2.8)) < 5:
    #             print(site)
    s.to('POSCAR', 'POSCAR_gen')
    break
# %%
print('ok')
# %%
