from functools import reduce
import macrodensity as md
import matplotlib.pyplot as plt
import numpy as np
import os


def slice(fr, end, density):
    vasp_pot, NGX, NGY, NGZ, Lattice = md.read_vasp_density('LOCPOT')
    grid_pot, electrons = md.density_2_grid(vasp_pot, NGX, NGY, NGZ)

    dim = [NGX, NGY, NGZ]
    dim = np.array(dim)

    start = np.array('0.55000  0.75926  0.33745'.split()).astype(float)
    to = np.array('0.55000  0.77161  0.46370'.split()).astype(float)

    # start = start * dim
    # to = to * dim
    new = []
    dis = []
    for n in np.linspace(fr, end, density):
        tmp = (to - start) * n + start
        new.append(tmp)
        dis.append(np.sqrt(sum((tmp * np.diagonal(Lattice)) ** 2)))

    new = np.array(new)
    # new = new.round()
    # new = new.astype(int)

    arr = []
    arr2 = []
    tmp = None
    size = 8
    for i, j in zip(new, dis):
        if reduce(lambda x, y: x * y, tmp == i):
            continue
        tmp = i
        a, _ = md.cube_potential(i, [0, 0, 0], [size, size, size], grid_pot, NGX, NGY, NGZ)
        arr.append(a)
        arr2.append(j)
    return arr2, arr


if __name__ == '__main__':
    os.chdir('/home/jinho93/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/from-2012/1.0ps/H')
    os.chdir('/home/jinho93/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/from-2012/3.1ps/H/again')
    x, y = slice(-2, 4.5, 200)
    macro = md.macroscopic_average(y, 32, 1)
    macro = md.macroscopic_average(macro, 32, 1)
    plt.plot(x, y)
    plt.plot(x, macro)
    output = [x, y, macro]
    output = np.array(output)
    output = np.transpose(output)
    np.savetxt('loc.dat', output)