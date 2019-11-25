from pymatgen.io.vasp.outputs import Structure, Element
import os
import numpy as np


def aver(arr:np.ndarray):
    return arr.sum() / len(arr)


if __name__ == '__main__':
    os.chdir('/home/jinho93/oxides/cluster/zno/vasp/3.slab/2.80')
    os.chdir('/home/jinho93/oxides/cluster/zno/vasp/3.slab/1.zn_vac/3.LDIPOL_from_ini')
    os.chdir('/home/jinho93/oxides/cluster/zno/cp2k/3.slab/2.wann')
    s = Structure.from_file('SPOSCAR')
    z_coords = []
    p = []
    for i in s.sites:
        if i.specie == Element.Zn:
            if len(s.get_neighbors(i, 2.5)) is 4:
                z = [_[0].z for _ in s.get_neighbors(i, 2.5)]
                z_coords.append(i.z)
                p.append(i.z - sum(z) / 4)

    arr = np.array([z_coords, p]).transpose()
    arr = arr[arr[:, 0].argsort()]
    n = 2
    for i in range(len(arr) // n):
        print(arr[n*i][0], aver(arr[n * i: n * (i + 1), 1]))
