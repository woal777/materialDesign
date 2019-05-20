from MDAnalysis.coordinates.XYZ import XYZReader
from MDAnalysis import Universe
import os
import numpy as np
from MDAnalysis.coordinates.base import Timestep

os.chdir('/home/jinho93/oxides/perobskite/lanthanum-aluminate/slab/nvt.para.6/island/len-19/step1')

u = Universe('POSCAR.xyz')
i: Timestep
arr = []
e = 1.6e-19 * 1E+6


def atom(name):
    if name == 'La':
        return 3
    elif name == 'Al':
        return 3
    else:
        return -2


for i in u.trajectory:
    for j, k in zip(u.atoms, i.positions):
        arr.append(np.insert(k, 0, atom(j.name)))

arr = sorted(arr, key=lambda row: row[2])
arr = sorted(arr, key=lambda row: row[3])
arr = np.array(arr)
print(arr)
z = 0.1
y = min(arr[:, 2])
p_arr = []
p = 0
num_la = 0
vol = 3.82409999997323e-8 ** 3
for j in arr:
    if j[3] < 1:
        continue
    if j[3] - z > 3:
        z = j[3]
        p_arr.append(p / num_la * 2)
        p = 0
    if j[0] == 3:
        num_la += 1
    p += (j[3] - z) * j[0] * e * 1e-8

for i in p_arr:
    print(i/ vol)
