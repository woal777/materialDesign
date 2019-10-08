from pymatgen import Structure
import os


def case1():
    s = Structure.from_file('POSCAR')
    for ind in s.sites:
        if ind.species_string is 'Ti' and len(s.get_neighbors(ind, 2.2)) < 6:
            ind._properties = {'selective_dynamics': [True] * 3}
        elif len(s.get_neighbors(ind, 2.2)) < 3:
            ind._properties = {'selective_dynamics': [True] * 3}
        else:
            ind._properties = {'selective_dynamics': [False] * 3}
    s.to('POSCAR', 'POSCAR')


def case2():
    strucgture = Structure.from_file('POSCAR')
    for s in strucgture.sites:
        if 0.08 < s.c < .45:
            s.properties = {'selective_dynamics': [False] * 3}
        else:
            s.properties = {'selective_dynamics': [True] * 3}
    strucgture.to('POSCAR', 'POSCAR')


if __name__ == '__main__':
    os.chdir('/home/jinho93/oxides/perobskite/lanthanum-aluminate/periodic_step/opti')
    case2()
