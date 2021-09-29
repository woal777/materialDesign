#%%
from pymatgen.io.xyz import XYZ
import os
import numpy as np
import matplotlib.pyplot as plt

os.chdir('/home/jinho93/oxides/wurtzite/zno/cp2k/1.aimd/3.16A/30/3.fix')
x = XYZ.from_file('526.xyz')


ini = x.all_molecules[0 // 3].cart_coords
fin = x.all_molecules[800 // 3].cart_coords


vec = (fin - ini)[:,1:]

o_pos = 300
zn_pos = 527
plt.quiver(ini[o_pos:zn_pos,1], ini[o_pos:zn_pos,2], vec[o_pos:zn_pos,0], vec[o_pos:zn_pos,1])
plt.ylim(0, 40)
plt.show()