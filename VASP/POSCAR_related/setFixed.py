from pymatgen.io.vasp import Structure
from pymatgen.core.sites import PeriodicSite

p: Structure = Structure.from_file('POSCAR')
i: PeriodicSite = None

for i in p.sites:
    if 0.16 < i.c < 0.37 or 0.53 < i.c < 0.77:
        i._properties = {'selective_dynamics': [True] * 3}
    else:
        i._properties = {'selective_dynamics': [False] * 3}
p.to('POSCAR', 'POSCAR')

