from pymatgen import Structure
import os

os.chdir('/home/jinho93/oxides/cluster/tio2/anatase/vasp')

s = Structure.from_file('POSCAR')
for ind in s.sites:
    if str(ind.specie) is 'Ti' and len(s.get_neighbors(ind, 2.2)) < 6:
        ind._properties = {'selective_dynamics': [True] * 3}
    elif len(s.get_neighbors(ind, 2.2)) < 3:
        ind._properties = {'selective_dynamics': [True] * 3}
    else:
        ind._properties = {'selective_dynamics': [False] * 3}
s.to('POSCAR', 'POSCAR')