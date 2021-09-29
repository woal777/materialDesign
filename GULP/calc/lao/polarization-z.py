#%%
from ast import Str
from math import atan
import os
import numpy as np
import matplotlib.pyplot as plt
from pymatgen import Structure
from pymatgen.core.sites import Site
from pymatgen.core.structure import Molecule
from pymatgen.io.xyz import XYZ

# os.chdir('/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/periodic_step/gulp/013')
# os.chdir('/home/jinho93/oxides/perobskite/lanthanum-aluminate/periodic_step/gulp/3.2012/1.opti')
# os.chdir('/home/jinho93/oxides/perobskite/lanthanum-aluminate/periodic_step/gulp/8.108')
os.chdir('/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/periodic_step/gulp/015/0/thick/4')
# os.chdir('/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/periodic_step/gulp/015/stengel')
u = Universe('lao.xyz')
s = Structure.from_file('POSCAR')
m = Molecule.from_file('tail.xyz')
# i: Timestep
arr = []
e = 1.6e-19 * 1e+6


def atom(name):
    if name == 'La':
        return 3
    elif name == 'Al':
        return 3
    else:
        return -2

sites = []
indices = []

j: Site
for i, j in enumerate(s.sites):
    if j.species_string == 'Al':
        oxy = [ind for r, _, ind in s.get_neighbors_in_shell(j.coords, 1, 1.5, True) if r.z >= j.z and r.x >= j.x]
        la = [ind for r, _, ind in s.get_neighbors_in_shell(j.coords, 3, .5, True) if r.z >= j.z and r.x >= j.x and r.y >= j.y]
        oxy.extend(la)
        sites.append(oxy)

# print(sites)

p_arr = []
pos = []
for site_list in sites:
    p = [0, 0, 0]
    perob = np.array(m.sites)[np.array(site_list)]
    i: Site
    for i in perob:
        if (i.coords[1] - perob[3].coords[1]) > 10:
            p += atom(i.species_string) * i.coords
            p[1] += atom(i.species_string) * s.lattice.b
            print(i)
        elif i.coords[1] - perob[3].coords[1] < -10:
            p += atom(i.species_string) * i.coords
            p[1] += atom(i.species_string) * s.lattice.b
            print(i, perob[3])
        else:
            p += atom(i.species_string) * i.coords
    
    if abs(p[1]) > 10:
        continue
    p_arr.append(p)
    pos.append(perob[3].coords)


p_arr = np.array(p_arr)
pos = np.array(pos)

plt.quiver(pos[:,1], pos[:,2], p_arr[:,1], p_arr[:,2], scale=50)
pos[:,1] = pos[:,1] - s.lattice.b
plt.quiver(pos[:,1], pos[:,2], p_arr[:,1], p_arr[:,2], scale=50)
plt.ylim(8, 27)
plt.show()
# plt.plot(p_arr[:,1])
# plt.show()
# # plt.plot(angle)
# # plt.show()

# %%
