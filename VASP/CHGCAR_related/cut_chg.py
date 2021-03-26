#%%
from pymatgen.io.vasp.outputs import Chgcar
import os
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
import numpy as np



def sym(chg, n):
    data = []
    for j in range(chg.dim[1]):
        for i in range(chg.dim[0]):
            for k in range(chg.dim[2]):
                if int(35/90 *i - 55/90*k) == n:
                    data.append(chg.data['total'][i, j, k])
                    
    data = np.array(data)
    data = np.reshape(data, (chg.dim[1], len(data) // chg.dim[1]))
    return data.astype(float)

def asym(chg, n):
    data = []
    for j in range(chg.dim[1]):
        for i in range(chg.dim[0]):
            for k in range(chg.dim[2]):
                if i + k == int(chg.dim[0] + chg.dim[2]) / 2 + n:
                    data.append(chg.data['total'][i, j, k])
                    
    data = np.array(data)
    data = np.reshape(data, (chg.dim[1], len(data) // chg.dim[1]))
    return data.astype(float)


os.chdir('/home/jinho93/molecule/ddt/vasp/2020/bulk/sym/t1')
chgcar = Chgcar.from_file('SPIN.vasp')
dsym = sym(chgcar, 5)

os.chdir('/home/jinho93/molecule/ddt/vasp/2020/bulk/asym/t1')
chgcar = Chgcar.from_file('SPIN.vasp')
dasym = asym(chgcar, 5)


#%%
os.chdir('/home/jinho93/molecule/ddt/vasp/2020/bulk/sym/t1')
chgcar = Chgcar.from_file('SPIN.vasp')
mlist = []
for i in range(25):
    mlist.append(np.max(sym(chgcar, i)))
print(np.argmax(mlist), mlist[np.argmax(mlist)])

# %%
os.chdir('/home/jinho93/molecule/ddt/vasp/2020/bulk/sym/t1')
chgcar = Chgcar.from_file('SPIN.vasp')
dsym = sym(chgcar, 10)
plt.figure(figsize=(20, 20))
plt.axes([0,0,0.7,0.6])
plt.imshow(dsym, norm=Normalize(np.min(dsym), np.max(dsym) * 0.1), interpolation='quadric')
plt.savefig('sym.png')

os.chdir('/home/jinho93/molecule/ddt/vasp/2020/bulk/asym/t1')
chgcar = Chgcar.from_file('SPIN.vasp')
dasym = asym(chgcar, 20)
plt.figure(figsize=(20, 20))
plt.axes([0,0,0.7,0.6])
plt.imshow(dasym, norm=Normalize(np.min(dsym), np.max(dsym) * 0.1), interpolation='quadric')
plt.savefig('asym.png')

# %%
