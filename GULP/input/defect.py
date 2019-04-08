import math
import os
import numpy as np
from MDAnalysis import Universe
from MDAnalysis.coordinates.XYZ import XYZWriter
from MDAnalysis.core.groups import Atom, AtomGroup

os.chdir('/home/jinho93/oxides/cluster/zno')
w = XYZWriter('output.xyz')
with open('POSCAR.xyz') as f:
    u = Universe(f)
    i: Atom
    rnd = np.random.rand(len(u.atoms))
    m = 0
    for i in u.atoms:
        if i.atomic_name == 'Zn':
            if m < i.position[2]:
                m = i.position[2]
    n = 0
    ind = []
    for j, i in enumerate(u.atoms):
        if i.atomic_name == 'Zn':
            if rnd[j] > 0.1 * math.exp((i.position[2] - m) * 0.1):
                ind.append(j)
            else:
                n += 1
        else:
            ind.append(j)
    a = AtomGroup(ind, u)
    print(len(a), (len(u.atoms) - len(a)))
    w.write(a)
w.close()


