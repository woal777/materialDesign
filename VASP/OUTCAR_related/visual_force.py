import os, re
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import matplotlib.pyplot as plt
import numpy as np

os.chdir('/home/jinho93/interface/lsmo-bto-pt/up/dense/dos')

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

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    x, y, z = pos[:, 0], pos[:, 1], pos[:, 2]
    u, v, w = force[:, 0], force[:, 1], force[:, 2]
    ax.quiver(x, y, z, u, v, w)
    plt.show()
