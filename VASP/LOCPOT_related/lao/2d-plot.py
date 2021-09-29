#%%
import enum
from math import sqrt
import numpy as np
from pymatgen.io.vasp import Locpot
import matplotlib.pyplot as plt
import os


os.chdir('/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/my015/4/lvhar')
os.chdir('/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/my015/half-half/sten-my')
# os.chdir('/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/my015/from-gulp/421/locpot')
# os.chdir('/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/my013/lao2/opti')
# os.chdir('/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/my013/lao2')
# os.chdir('/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/my015/symm')
# os.chdir('/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/my015/from-gulp/421/opti/loc')
# os.chdir('/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/stengel/015/4/lvhar')
# os.chdir('/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/stengel/013/lvhar')
# os.chdir('/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/my015/4/lvhar')
# os.chdir('/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/my015/from-gulp/421/opti/loc')
# os.chdir('/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/my015/7')
# os.chdir('/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/stengel/015/7')
loc = Locpot.from_file('LOCPOT')

#%%
dat = np.sum(loc.data['total'], axis=0) / loc.dim[0]
dat = np.swapaxes(dat, axis1=0, axis2=1)
# dat = np.roll(dat, int(loc.dim[1] * 0.6), axis=0)
# dat = np.roll(dat, -60, axis=1)
# grad = np.gradient(dat)
# dat = dat[::4,::4]
# u = grad[0]
# v = grad[1]
# u = u[::4, ::4]
# v = v[::4, ::4]
# u /= np.sqrt(u ** 2 + v ** 2)
# v /= np.sqrt(u ** 2 + v ** 2)

rep = 3
if rep == 1:
    x = np.linspace(0, 1, dat.shape[1])
else:
    x = np.linspace(-1, 2, rep * dat.shape[1])
    dat = np.concatenate([dat] * rep, axis=1)

y = np.linspace(0, 1, dat.shape[0])
X, Y = np.meshgrid(x, y)


#%%
# plt.imshow(dat, cmap='viridis_r')
plt.figure(figsize=(len(x) / 30, len(y) / 30))

plt.contourf(X, Y, dat, levels=np.linspace(-50, 11, 60), cmap='viridis_r')
# plt.plot([0, 1], [0.387, 0.087], color='orange')
# xs, ys = np.array([0.65754, .40053]), np.array([0.62561, .71076]) - 0.4
# 015my
# xs, ys = np.array([0.40637, .65912]), np.array([0.71007, .62709])
# xs, ys = np.array([.82692, .05769]), np.array([0.66195, .56229])
xs, ys = np.array([-0.32668, 0.62561 ]), np.array([0.52742  , .65754])
slope = (ys[1] - ys[0]) / (xs[1] - xs[0])
y0 = ys[0] - slope * xs[0]
plt.plot([-1, 2], [y0 - slope, y0 + 2 * slope], color='orange')

# plt.scatter(xs, ys, c='yellow')

# plt.tick_params(top=True, right=True)
plt.tick_params(bottom=False, left=False)

plt.savefig('/home/jinho93/locpot.png', dpi=500)
# plt.quiver(X, Y, u, v)

#%%
line = []
# newx = np.linspace(0.05482, 0.05482 + 1.513732345,dat.shape[0])
newx = np.linspace(-1, 2,dat.shape[1])
# newx = np.linspace(-1, 2, rep * dat.shape[1])
for i, dx in enumerate(newx):
    line.append(dat[int((y0 + slope * dx) * dat.shape[0]), i])
        # newx.append(dx)
        # if line[-1] < -44:
            # print(i)
np.savetxt('/home/jinho93/line.dat', line)
np.savetxt('/home/jinho93/x.dat', newx)
plt.plot(newx, line)

#%%

from scipy import interpolate
xmin = min(newx[-int(576 / 1.947562338):])
xmax = max(newx[-int(576 / 1.947562338):])
f = interpolate.interp1d(newx[-int(576 / 1.947562338):], line[-int(576 / 1.947562338):])
xnew = np.linspace(xmin, xmax, 392)
fnew = f(xnew)
plt.plot(xnew, fnew)
np.savetxt('/home/jinho93/line.dat', fnew)
# %%

from scipy import ndimage, signal
dat = np.concatenate([dat, dat])
# img_45 = ndimage.rotate(dat, 18.4 - 180, reshape=False)
img_45 = ndimage.rotate(dat, 11.3 - 180, reshape=False)
xmin = 80
ymin = 209
plt.imshow(img_45)
# plt.show()
# plt.imshow(img_45[xmin:xmin + 41, ymin:ymin + 38])
plt.tick_params(bottom=None, left=None)
plt.show()
#%%

sdim = 28
scharr = np.zeros((sdim, sdim))
for x in range(sdim + 1):
    for y in range(sdim + 1):
        if (x - sdim / 2) ** 2 + (y - sdim / 2) ** 2 < (sdim / 2) ** 2:
            scharr[x, y] = 1
scharr /= np.sum(scharr)
plt.imshow(scharr)
plt.xlim((0, sdim - 1))
plt.ylim((0, sdim - 1))

#%%
# sdim = 38
# scharr = np.ones((sdim, sdim))
conv = signal.convolve2d(img_45, scharr, mode='same', boundary='symm')
fig = plt.figure(dpi=500)
# plt.imshow(conv[250:550,150:450], interpolation='spline36')
plt.imshow(conv, interpolation='spline36')
plt.show()
plt.imshow(img_45[250:550,150:450])
plt.show()
print(np.min(conv), np.max(conv))
#%%
def discrete_region(dat):
    dat -= np.max(dat)
    mx = np.min(dat)
    print(mx, np.max(dat))
    new = np.zeros((dat.shape[0], dat.shape[1], 3))
    val = 15
    print(val)
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
print(np.min(n), np.max(n))
fig = plt.figure(dpi=400)
# plt.imshow(n[300:750,50:500], interpolation='quadric')
plt.imshow(n, interpolation='quadric')
plt.tick_params(left=None, bottom=None)
plt.savefig('/home/jinho93/stengel.png')
# %%

import numpy as np
import matplotlib.pyplot as plt
new = np.zeros((100,100,3))
for i in range(100):
    for j in range(100):
        new[i, j, 0] = 1-float(i / 100)
        new[i, j, 1] = 0
        new[i, j, 2] = float(i / 100)

plt.imshow(new)

# %%

plt.imshow(dat)
m_range = 155
# dis = 190 // 2
dis = 256 // 2
plt.plot([0, dat.shape[1]], [m_range,m_range])
plt.plot([0, dat.shape[1]], [m_range + dis,m_range + dis])
# arr = dat[200:200+51,:]
arr = dat[m_range:m_range+dis,:]
line = np.sum(arr, axis=0) / arr.shape[9]
plt.imshow(dat)
plt.show()
plt.imshow(arr)
# %%
import macrodensity as md
# plt.plot(line)
plt.subplot(211)
macro = md.macroscopic_average(line, 1, 1/ dat.shape[1] * 5 * 3)
plt.plot(line)
plt.plot(macro)
plt.xlim((0, len(line)))
plt.subplot(212)
plt.imshow(arr)

#%%
from scipy import interpolate
start = 300
disp = 40
plt.imshow(img_45[:,start:start+disp])
plt.show()
line = np.sum(img_45[:, start:start+disp], axis=1) / disp

fnew = interpolate.interp1d(np.linspace(0,1, len(line)), line)
ynew = fnew(np.linspace(0,1, int(len(line) * 0.75)))

plt.plot(ynew[240:])
np.savetxt('/home/jinho93/line.dat', ynew[195:])
# interpolate.interp1d(np.range(np.sum(img_45[start:start+disp,:], axis=0) / disp))

# %%
plt.imshow(img_45[start:start+disp,150:150 + 302])

# %%
