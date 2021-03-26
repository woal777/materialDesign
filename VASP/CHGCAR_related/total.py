#%%
from pymatgen.io.vasp import Chgcar
import numpy as np
import os

os.chdir('/home/share')
chg = Chgcar.from_file('PARCHG')

print(np.sum(chg.data['total']) / chg.ngridpts)

#%%
import matplotlib.pyplot as plt
plt.plot(chg.get_average_along_axis(2))
# plt.imshow(np.sum(chg.data['total'], axis=0))
#%%
n = chg.ngridpts
k = 0
while n > 96:
    n -= 96
    k += 1
    
    
#%%
chg.structure.to('POSCAR', 'POSCAR')