#%%
from pymatgen.io.xyz import XYZ
from pymatgen import Molecule
import os

os.chdir('/home/jinho93/oxides/wurtzite/zno/cp2k/1.aimd/3.16A/30/3.fix/output')
xyz = XYZ.from_file('526.xyz')

m: Molecule
for i, m in enumerate(xyz.all_molecules):
    if i % 30 == 0:
        m.to('xyz', f'{i}.xyz')
