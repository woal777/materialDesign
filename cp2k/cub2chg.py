#%%

from pymatgen.io.vasp.outputs import Chgcar
from pymatgen.io.cube import Cube
import os

os.chdir('/home/jinho93/molecule/ddt/cp2k/bulk/asym/t1')
cub = Cube('s1-SPIN_DENSITY-1_0.cube')
cub.NZ
for i in range(cub.NX):
    for j in range(cub.NY):
        for k in range(cub.NZ):
            if i + k > cub.NZ + 2 or i + k < cub.NZ / 2 + 5:
                cub.data[i, j, k] = 0
chg = Chgcar(cub.structure, {'total':cub.data})
chg.write_file('NEW_CHGCAR')

# chg = Chgcar(cub.structure, cub.data)


# %%
