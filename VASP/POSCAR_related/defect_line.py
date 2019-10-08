import matplotlib.pyplot as plt
import numpy as np
from pymatgen import Structure


def step_func(a, v):
    if a > v:
        return 1
    else:
        return 0


if __name__ == '__main__':
    s = Structure.from_file('POSCAR.ini')
    rnd = np.random.rand(len(s.sites))
    s.density
    m = .48
    n = 0
    ind = []
    oxy = []
    zinc = []
    for j, i in enumerate(s.sites):
        if i.species_string == 'Zn':
            if rnd[j] < 0.4 * step_func(i.c, m):
                zinc.append(j)
            else:
                n += 1
    ind.extend(zinc)
    s.remove_sites(ind)
    for i in s.sites:
        if 0.26 < i.c:
            i._properties = {'selective_dynamics': [True] * 3}
        else:
            i._properties = {'selective_dynamics': [False] * 3}

    s.to('POSCAR', 'POSCAR.OUT')
    hist, _ = np.histogram(s.cart_coords[:, 2], bins=20, range=(0, 20*2.584843396))
    plt.plot(hist, '+')
    plt.show()
    # znw.write(zn)
