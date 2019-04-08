from pymatgen.io.vasp import Structure
from pymatgen.core.sites import PeriodicSite
import os
os.chdir('/home/share')
p: Structure = Structure.from_file('POSCAR')
i: PeriodicSite = None

for i in p.sites:
    if 0.42 < i.c < 0.58 and 0.42 < i.b < 0.58 and 0.42 < i.a < 0.58:
        i._properties = {'selective_dynamics': [False] * 3}
    else:
        i._properties = {'selective_dynamics': [True] * 3}

p.to('POSCAR', 'POSCAR')
