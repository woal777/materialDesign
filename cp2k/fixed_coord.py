from pymatgen import Structure
import os
import numpy as np

os.chdir('/home/jinho93/oxides/cluster/tio2/anatase/vasp')

s = Structure.from_file('POSCAR')
with open('POSCAR.xyz', 'w') as f:
    f.write(str(s.num_sites) + '\n\n')
    for ind in s.sites:
        if str(ind.specie) is 'Ti' and len(s.get_neighbors(ind, 2.2)) < 6:
            f.write((f"{ind.specie}  " + "{:12.10f} "*3 + '\n').format(*ind.coords))
            np.array2string(ind.coords)
        elif len(s.get_neighbors(ind, 2.2)) < 3:
            f.write((f"{ind.specie}  " + "{:12.10f} "*3 + '\n').format(*ind.coords))
    for ind in s.sites:
        if str(ind.specie) is 'Ti' and len(s.get_neighbors(ind, 2.2)) == 6:
            f.write((f"{ind.specie}  " + "{:12.10f} "*3 + '\n').format(*ind.coords))
            np.array2string(ind.coords)
        elif len(s.get_neighbors(ind, 2.2))== 3:
            f.write((f"{ind.specie}  " + "{:12.10f} "*3 + '\n').format(*ind.coords))
