#%%
from pymatgen.io.vasp import Poscar

pos: Poscar
pos = Poscar.from_file('/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/mlff/1step/POSCAR')
pos.set_temperature(800)
frac = pos.structure.frac_coords
idx = sorted(range(len(frac)), key=lambda k: frac[k, 2])
ridx = sorted(range(len(idx)), key=idx.__getitem__)

#%%
import numpy as np
tmp = np.array(pos.velocities)[idx]
for i in range(len(tmp)):
    tmp[i] = tmp[-i - 1]
tmp =np.array(tmp)[ridx]
print(tmp[:,2][0])
print(tmp[:,2][17])
pos.velocities = tmp
path = '/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/mlff/1step/'
with open(path + 'POSCAR-NEW', 'w') as f:
    f.write(pos.get_string())
# %%
