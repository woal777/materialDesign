import numpy as np
from pymatgen.io.vasp import Locpot
from scipy import ndimage, signal, interpolate
import matplotlib.pyplot as plt
import os

loc = Locpot.from_file('LOCPOT')
dat = np.sum(loc.data['total'], axis=0) / loc.dim[0]
dat = np.swapaxes(dat, axis1=0, axis2=1)
rep = 3

if rep == 1:
    x = np.linspace(0, 1, dat.shape[1])
else:
    x = np.linspace(-1, 2, rep * dat.shape[1])
    dat = np.concatenate([dat] * rep, axis=1)

y = np.linspace(0, 1, dat.shape[0])
X, Y = np.meshgrid(x, y)

dat = np.concatenate([dat, dat])
img_45 = ndimage.rotate(dat, 11.3 - 180, reshape=False)
plt.imshow(img_45)

sdim = 32
scharr = np.zeros((sdim, sdim))
for x in range(sdim + 1):
    for y in range(sdim + 1):
        if (x - sdim / 2) ** 2 + (y - sdim / 2) ** 2 < (sdim / 2) ** 2:
            scharr[x, y] = 1
scharr /= np.sum(scharr)

conv = signal.convolve2d(img_45, scharr, mode='same', boundary='symm')
fig = plt.figure(dpi=500)

def discrete_region(dat):
    dat -= np.max(dat)
    mx = np.min(dat)
    new = np.zeros((dat.shape[0], dat.shape[1], 3))
    val = 22
    for i in range(dat.shape[0]):
        for j in range(dat.shape[1]):
            if dat[i, j] < -val:
                new[i, j, 0] = 1 + (dat[i, j] + val) / abs(mx + val)
                new[i, j, 1] = 0
                new[i, j, 2] = - (dat[i, j] + val) / abs(mx + val)
            else:
                new[i, j, 0] = 1
                new[i, j, 1] = 1
                new[i, j, 2] = 1 + dat[i, j] / val
    return new

n = discrete_region(conv)
fig = plt.figure(dpi=400)
plt.imshow(n, interpolation='quadric')

start = 271 + 55
disp = 55
plt.imshow(img_45[:,start:start+disp])
plt.show()
line = np.sum(img_45[:, start:start+disp], axis=1) / disp

fnew = interpolate.interp1d(np.linspace(0,1, len(line)), line)
ynew = fnew(np.linspace(0,1, int(len(line) * 0.75)))

plt.plot(ynew)
plt.show()

