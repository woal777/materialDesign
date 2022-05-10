from re import search
import matplotlib.pyplot as plt
import re
from pymatgen import Structure
import numpy as np


def chg_sum(outcar, structure, species):
    output = 0
    for i, j in zip(structure.sites, outcar.charge):
        if  i.specie in species:
            output += j['tot']
    return(output)

def mae(easy_path, hard_path):
    x = []
    z = []
    with open(hard_path+'/OUTCAR') as f:
        for l in f:
            if search('E_soc', l):
                x.append(float(l.split()[-1]))
            elif search('volume of cell', l):
                vol = float(l.split()[-1])

    with open(easy_path+'/OUTCAR') as f:
        for l in f:
            if search('E_soc', l):
                z.append(float(l.split()[-1]))
    output = []

    for i, j in zip(x, z):
        output.append((i-j) / vol * 1.60218e-19 * 1e+30 / 1e+6 / 2)

    return output

def visualize_force(path, scale=10):
    with open(path+'/OUTCAR') as f:
        struct: Structure
        struct = Structure.from_file(path+'/POSCAR')
        p = re.compile('POSITION')
        pos, force = [], []
        for l in f:
            if p.search(l):
                f.__next__()
                for l in f:
                    if l.__contains__('--'):
                        break
                    tmp = [float(r) for r in l.split()]
                    force.append(tmp[3:])
        force = np.array(force)
        force = force / np.max(abs(force))
        pos = struct.cart_coords
        c = [s.specie for s in struct.sites]
        for ind, i in enumerate(struct.composition):
            c = [ind if x==i else x for x in c]
        # ax = fig.gca(projection='3d')
        x, y, z = pos[:, 0], pos[:, 1], pos[:, 2]
        u, v, w = force[:, 0], force[:, 1], force[:, 2]
        # ax.quiver(x, y, z, u, v, w)
        plt.quiver(x, z, u, w, c, scale=scale)
        plt.scatter(x, z)
        # plt.xlim(0, 12)
        # plt.ylim(0, 40.8)
        plt.show()