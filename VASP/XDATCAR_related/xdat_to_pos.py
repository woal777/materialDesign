#%%
import os
from pymatgen.io.vasp.outputs import Xdatcar
os.chdir('/home/jinho93/battery/anode/TiO2/nvt/struct')
xdat = Xdatcar.from_file('XDATCAR')
#%%
for j, i in enumerate(xdat.structures[::100]):
    i.to('POSCAR', f'POSCAR{j:03d}')