#%%
import numpy as np
import os
from pymatgen import Structure
os.chdir('/home/jinho93')

s1 = Structure.from_file('POSCAR_C1')
s2 = Structure.from_file('POSCAR_C2')
sp = []
coords = np.zeros(s1.cart_coords.shape)


for j, i in enumerate(s1.sites):
    r = 1.1
    ne = s2.get_sites_in_sphere(i.coords, r)
    while len(ne) < 1:
        r += .01
        ne = s2.get_sites_in_sphere(i.coords, r)
    print(len(ne))  
    sp.append(ne[0][0].specie)
    coords[j] = ne[0][0].frac_coords
# %%
s3 = Structure(s1.lattice, species=sp, coords=coords)
s1.to('POSCAR', 'ini')
s3.to('POSCAR', 'final')
# %%
