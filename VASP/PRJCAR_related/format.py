#%%
import re
import os
import math
import numpy as np
import matplotlib.pyplot as plt
from pymatgen.io.vasp import Procar, Outcar
from pymatgen import Spin
import scipy

os.chdir('/home/jinho93/new/oxides/perobskite/sto/b4vasp/input/dense2')

orb = 'd'

procar = Procar('PROCAR')
dat = np.array(procar.data[Spin.up])
dat = np.sum(dat, axis=2)

if orb == 's':
    dat = dat[:,:,0]
elif orb == 'p':
    dat = dat[:,:,1:4]
    dat = np.sum(dat, axis=2)
elif orb == 'd':
    dat = dat[:,:,4:9]
    dat = np.sum(dat, axis=2)
elif orb == 'dxy':
    dat = dat[:,:,4]
elif orb == 'dyz':
    dat = dat[:,:,5]

spin = []
band = []
ikp = []

with open('PRJCAR') as f:
    re_vkpt = re.compile('vkpt')
    re_spin = re.compile('spin')
    re_band = re.compile('band:')
    re_numberofk  = re.compile('IBZ of POSCAR.prim')
    bands_read = False
    nkp = 0
    for l in f:
        if re_numberofk.search(l):
            nkp = int(l.split()[-1])
            _ = f.readline()
            _ = f.readline()
            for _ in range(nkp):
                ikp.append([float(r) for r in f.readline().split()[1:4]])

        if re_spin.search(l):
            spin = []
            for _ in range(dat.shape[0]):
                _ = f.readline()
                kpoint = []
                for _ in range(dat.shape[1]):
                    band = []
                    l = f.readline()
                    energy = l.split()[-1]
                    for _ in range(math.ceil(nkp / 10)):
                        l = f.readline()
                        band.extend(l.split())
                    kpoint.append([energy, band])
                spin.append(kpoint)
    # s = np.array(s)
        
ikp = np.array(ikp)
area = []
ef = 4.68
z0 = [True if r[2] == 0 else False for r in ikp ]
x = [r[0] for r in ikp if r[2] == 0]
y = [r[1] for r in ikp if r[2] == 0]
x, y = np.array(x), np.array(y)
print(dat.shape, len(spin))

for dx, ik in zip(dat, spin):
    for dy, ib in zip(dx, ik):
        if  ef - 0.2 < float(ib[0]) <ef + 0.2:
            if area == []:
                area = np.array(ib[1], dtype=float)[z0] * 40 * dy
            else:
                area += np.array(ib[1], dtype=float)[z0] * 40 * dy

new = x + 100 * y
anew = np.argsort(new)
x = x[anew]
y = y[anew]
area = area[anew]

# xi = np.linspace(-0.5,0.5,100)
# yi = np.linspace(-0.5,0.5,100)
# X, Y = np.meshgrid(xi,yi)

# from scipy.interpolate import griddata
# dat = griddata((x, y), area,(X,Y) , method='linear')

# y = y[np.argsort(y)]
# area = area[np.argsort(y)]

plt.scatter(x, y, s=area)
plt.show()
x = x.reshape(20, -1)[0]
y = y.reshape(20, -1)[:,0]
x = np.append(x, -x[0])
y = np.append(y, -y[0])


# f = interp2d(x, y, area, kind='cubic')
# xnew = np.arange(-0.5, 0.5, 1e-2)
# ynew = np.arange(-0.5, 0.5, 1e-2)


area = area.reshape(20,-1)
area = np.concatenate([area, [area[0]]], axis=0)
area = np.concatenate([area, np.transpose([area[:,0]])], axis=1)

np.savetxt(orb, area.reshape(1,-1))

plt.contourf(x, y, area, levels=100, cmap='magma')
plt.show()
# plt.contourf(xi, yi, dat, levels=100, cmap='Reds')
# plt.show()
# with open('newPRJCAR', 'w') as g:
#     for k in s:
#         for 
# %%

from scipy.ndimage.filters import gaussian_filter
dat = gaussian_filter(area, 0.5)
from scipy.interpolate import griddata
dat2 = griddata((np.linspace(-0.5, 0.5, 100), np.linspace(-0.5, 0.5, 100)), dat,(x,y) , method='cubic')
plt.contourf(dat2,levels=100, cmap='Reds')
plt.show()
