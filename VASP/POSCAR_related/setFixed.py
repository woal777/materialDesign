from pymatgen.io.vasp import Structure
from pymatgen.core.sites import PeriodicSite
import os
p: Structure = Structure.from_file('POSCAR')
i: PeriodicSite = None

for i in p.sites:
    if 0.5 < i.c :
        i._properties = {'selective_dynamics': [True] * 3}
    else:
        i._properties = {'selective_dynamics': [False] * 3}

p.to('POSCAR', 'POSCAR')
