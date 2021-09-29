#%%
from pymatgen.io.xyz import XYZ
import os

os.chdir('/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/periodic_step/gulp/015/2')
xyz = XYZ.from_file('lao.xyz')
with open('XDATCAR', 'w') as x:
    for m in xyz.all_molecules:
        for c in m.cart_coords:
            x.write(f'{c[0]}\t{c[1]}\t{c[2]}\n')