import math
import os
import numpy as np
from MDAnalysis import Universe
from MDAnalysis.coordinates.XYZ import XYZWriter
from MDAnalysis.core.groups import Atom, AtomGroup
import matplotlib.pyplot as plt
os.chdir('/home/jinho93/oxides/cluster/zno')


def step_func(a, v):
    if a > v:
        return 1
    else:
        return 0


with open('POSCAR.xyz') as f,\
        XYZWriter('output2.xyz') as znw, \
        XYZWriter('output.xyz') as w:
    u = Universe(f)
    i: Atom
    rnd = np.random.rand(len(u.atoms))
    m = max(np.array(u.coord)[:, 2])
    n = 0
    ind = []
    oxy = []
    zinc = []
    for j, i in enumerate(u.atoms):
        if i.atomic_name == 'Zn':
            if rnd[j] > 0.1 * step_func(i.position[2], m / 2):
                zinc.append(j)
            else:
                n += 1
        else:
            oxy.append(j)
    ind.extend(oxy)
    ind.extend(zinc)
    a = AtomGroup(ind, u)
    zn = AtomGroup(zinc, u)
    o = AtomGroup(oxy, u)
    hist, _ = np.histogram(zn.positions[:, 2], bins=20)
    hist2, _ = np.histogram(o.positions[:, 2], bins=20)
    plt.plot(hist, '+')
    plt.plot(hist2, 'x')
    plt.ylim((0, 70))
    w.write(a)
    znw.write(zn)
    plt.show()
    # znw.write(zn)
