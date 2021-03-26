from itertools import chain

import math
from pandas import read_table as pandas_read_table
import numpy as np


def read(FILE):
    with open(FILE) as f:
        [f.readline() for _ in range(6)]
        lattice = np.zeros(shape=(3, 3))
        for row in range(3):
            lattice[row] = [float(x) for x in f.readline().split()]
        [f.readline() for _ in range(5)]
        num_atoms = int(f.readline().split()[0])
        [f.readline() for _ in range(num_atoms)]
        [f.readline() for _ in range(5)]

        NGX, NGY, NGZ = [int(x) for x in f.readline().split()]
        [f.readline() for _ in range(4)]

        # readrows = int(math.ceil(NGX * NGY * NGZ / 6))
        # skiprows = 25 + num_atoms
        Potential = (f.readline().split()
                     for i in range(int(math.ceil(NGX * NGY * NGZ / 6))))
        Potential = np.fromiter(chain.from_iterable(Potential), float)
        return Potential, Potential * Potential


def write(FILE):
    with open(FILE) as f:
        [f.readline() for _ in range(6)]
        lattice = []
        for row in range(3):
            lattice.append(f.readline())
        # lattice = np.array(lattice)
        # lattice = lattice.astype(np.float)
        # lattice *= 2
        # lattice = lattice.astype(str)
        # lattice_str = []
        # for i in range(3):
        #     lattice_str.append('\t'.join(lattice[i]) + '\n')
        [f.readline() for _ in range(5)]
        num_atoms = int(f.readline().split()[0])
        atoms = [f.readline().split() for _ in range(num_atoms)]
        atoms = np.array(atoms)

        [f.readline() for _ in range(5)]

        NGX, NGY, NGZ = [int(x) for x in f.readline().split()]
        [f.readline() for _ in range(4)]

        # readrows = int(math.ceil(NGX * NGY * NGZ / 6))
        # skiprows = 25 + num_atoms
        Potential = []
        for i in range(int(math.ceil(NGX * NGY * NGZ / 6))):
            Potential.extend(f.readline().split())
        Potential = np.array(Potential)
        Potential = Potential.reshape((NGZ, NGY, NGX))
        Potential = np.roll(Potential, -1, axis=0)
        Potential = np.roll(Potential, -1, axis=1)
        Potential = np.roll(Potential, -1, axis=2)

        Potential = Potential.reshape(NGX * NGY * NGZ)

        with open('CHGCAR_XSF', 'w') as f:
            header = ['from xsf\n', '  1.0\n']
            header.extend(lattice)
            f.writelines(header)
            for a in atoms:
                f.write(f' {a[0]}')
            f.write('\n')
            for _ in atoms:
                f.write(' 1')
            f.write('\n')
            f.write('Cart\n')
            for l in atoms:
                f.write(' '.join(l[1:]) + ' ' + l[0] + '\n')
            f.write('\n')
            f.write(f' {NGX} {NGY} {NGZ}\n')
            for i in range(int(math.ceil(NGX * NGY * NGZ / 5))):
                f.write(' '.join(Potential[i * 5:(i + 1) * 5]) + '\n')

            return Potential


if __name__ == '__main__':
    import os
    os.chdir('/home/jinho93/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/stengel/bulk/coarse/oxy')
    os.chdir('/home/jinho93/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/stengel/001/vca/AlO2/wann')
    p = write('wannier90_00004.xsf')
    p = np.array(p)
