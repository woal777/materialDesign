#%%
import os, re
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import matplotlib.pyplot as plt
import numpy as np

os.chdir('/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/stengel/013')
os.chdir('/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/stengel/013/from_gulp')
# os.chdir('/home/jinho93/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/from-2012/1.0ps')

with open('OUTCAR') as f:
    p = re.compile('POSITION')
    pos, force = [], []
    for l in f:
        if p.search(l):
            f.__next__()
            for l in f:
                if l.__contains__('--'):
                    break
                tmp = [float(r) for r in l.split()]
                pos.append(tmp[:3])
                force.append(tmp[3:])
    pos = np.array(pos)
    force = np.array(force)
    force = force / np.max(abs(force))

    if os.path.basename(os.getcwd()) == '013':
        fig = plt.figure(figsize=(12, 21))
        plt.plot([0, 0], [0, 22])
        plt.plot([12, 12], [0, 22])
        c = []
        c.extend([0] * 9)
        c.extend([1] * 9)
        c.extend([2] * 9)

    else:
        fig = plt.figure(figsize=(12, 40.8))
        c = []
        c.extend([0] * 18)
        c.extend([1] * 18)
        c.extend([2] * 54)
        
    # ax = fig.gca(projection='3d')
    x, y, z = pos[:, 0], pos[:, 1], pos[:, 2]
    u, v, w = force[:, 0], force[:, 1], force[:, 2]
    # ax.quiver(x, y, z, u, v, w)
    plt.quiver(x, z, u, w, c, scale=10)
    plt.scatter(x, z)
    plt.xlim(0, 12)
    plt.ylim(0, 40.8)
    plt.show()
