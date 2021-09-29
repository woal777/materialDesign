#%%
from matplotlib import cm
import numpy as np
from pymatgen.core.sites import Site
from pymatgen.io.vasp import Locpot
import matplotlib.pyplot as plt
import os

os.chdir('/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/my015/4/lvhar')
loc = Locpot.from_file('LOCPOT')
os.chdir('/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/my015/from-gulp/421/locpot')
# os.chdir('/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/my015/from-gulp/421/opti/loc')
loc2 = Locpot.from_file('LOCPOT')
os.chdir('/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/stengel/015/4/lvhar')
loc3 = Locpot.from_file('LOCPOT')
tloc = [loc, loc2, loc3]
# tloc = [loc, loc2]

#%%
def charge(pot):
    dat = np.sum(pot.data['total'], axis=0) / pot.dim[0]
    dat = np.roll(dat, int(pot.dim[1] * 0.8) // 2, axis=0)
    dat = np.swapaxes(dat, 0, 1)
    grad = np.gradient(dat)
    u = grad[0]
    v = grad[1]
    uu = np.gradient(u)
    vv = np.gradient(v)
    return(uu, vv)

u, v = charge(loc)
plt.imshow(u[0] + v[1])
#%%
def ampNphase(pot, n):
    dat = np.sum(pot.data['total'], axis=0) / pot.dim[0]
    dat = np.roll(dat, int(pot.dim[1] * 0.8) // 2, axis=0)
    dat = np.swapaxes(dat, 0, 1)
    grad = np.gradient(dat)
    u = grad[0]
    v = grad[1]
    np.savetxt(f'/home/jinho93/v{n}.dat', v)
    np.savetxt(f'/home/jinho93/u{n}.dat', u)
    amp =np.sqrt(u ** 2 + v ** 2)
    # u, v = u / np.max(amp), v / np.max(amp)
    phase = np.arctan(v / u)
    phase[u < 0] = phase[u < 0] + np.pi 
    phase -= np.pi / 2
    return amp, phase

amp = []
phase = []
for e, i in enumerate(tloc):
    a, p = ampNphase(i, e)
    amp.append(a)
    phase.append(p)
# amp2, phase2 = ampNphase(loc2)
# amp3, phase3 = ampNphase(loc3)
# amp = [amp1, amp2, amp3]
# phase = [phase1, phase2, phase3]
rolling = 0

#%%
factor = 2

def hsv_plot(rgb, alpha):
    cmap_hsv = cm.get_cmap('hsv')
    new = np.zeros([rgb.shape[0], rgb.shape[1], 4])
    for i in range(rgb.shape[0]):
        for j in range(rgb.shape[1]):
            new[i, j] += cmap_hsv(rgb[i, j] / (2 * np.pi) + 0.5)
            if alpha[i, j] > 1 / factor:
                new[i, j, 3] = 1
            else:
                new[i, j, 3] = factor * alpha[i, j]
    return new

hsv = [hsv_plot(p, a) for p, a in zip(phase, amp)]

#%%

def roll(n):
    hsv[n] = np.roll(hsv[n], -30, axis=0)
    amp[n] = np.roll(amp[n], -30, axis=0)
    phase[n] = np.roll(phase[n], -30, axis=0)

rolling -= 30
roll(1)
#%%

def lineplot(n):
    os.chdir('/home/jinho93')
    
    pos_x = []
    pos_y = []
    size  = []
    for s in tloc[n].structure.sites:
        shift_x = int(tloc[n].dim[1] * 0.8) // 2 + tloc[n].dim[1] * s.b
        if shift_x > tloc[n].dim[1]:
            pos_x.append(shift_x - tloc[n].dim[1])
        else:
            pos_x.append(shift_x)
        pos_y.append(tloc[n].dim[2] * s.c + rolling)
        if s.species_string == 'O':
            size.append(2)
        elif s.species_string == 'La':
            size.append(5)
        else:
            size.append(3.5)
    size = np.array(size) * 10
    # new_hsv = np.roll(hsv[n], 30, axis=0)
    fig = plt.figure(dpi=300)
    plt.imshow(hsv[n], interpolation='gaussian')
    u = -np.cos(phase[n])
    v = -np.sin(phase[n])
    lw = np.where(amp[n] > .1, 0, amp[n] * factor)
    X, Y = np.meshgrid(range(phase[n].shape[1]), range(phase[n].shape[0]))
    plt.streamplot(X, Y, u, v, linewidth=lw, density=0.82)
    # plt.scatter(pos_x, pos_y, c='gray', s=size)
    plt.ylim((0, amp[n].shape[0]))
    plt.xlim((0, amp[n].shape[1]))
    plt.savefig(f'hsv{n}.png')
    plt.show()

lineplot(1)
#%%
def ampplot(n):
    fig = plt.figure(dpi=300)
    X, Y = np.meshgrid(range(phase[n].shape[1]), range(phase[n].shape[0]))
    u = np.cos(phase[n])
    v = np.sin(phase[n])
    lw = np.where(amp[n] > .1, 1, amp[n] * 10)
    plt.imshow(lw, cmap='hot_r')
    plt.streamplot(X, Y, u, v, linewidth=lw, density=0.6)
    plt.show()
    
ampplot(0)
#%%

def scatter_plot(n):
    os.chdir('/home/jinho93')
    pos_x = []
    pos_y = []
    size  = []
    s: Site
    for s in tloc[n].structure.sites:
        shift_x = int(tloc[n].dim[1] * 0.8) // 2 + tloc[n].dim[1] * s.b
        if shift_x > tloc[n].dim[1]:
            pos_x.append(shift_x - tloc[n].dim[1])
        else:
            pos_x.append(shift_x)
        pos_y.append(tloc[n].dim[2] * s.c + rolling)
        if s.species_string == 'O':
            size.append(2)
        elif s.species_string == 'La':
            size.append(5)
        else:
            size.append(3.5)
        
    # new_hsv = np.roll(hsv[n], 30, axis=0)
    fig = plt.figure(dpi=300, figsize=(amp[n].shape[1] / 100, amp[n].shape[0] / 100))
    size = np.array(size) * 10
    print(size)
    plt.scatter(pos_x, pos_y, c='gray', s=size)
    plt.ylim((0, amp[n].shape[0]))
    plt.xlim((0, amp[n].shape[1]))
    plt.savefig(f'scatter{n}.png')
    plt.show()

scatter_plot(0)
# %%


os.chdir('/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/my015/4/lvhar')
os.chdir('/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/stengel/015/4/from_gulp')
loc = Locpot.from_file('LOCPOT')
amp, phase = ampNphase(loc)
hsv = hsv_plot(phase, amp)

fig = plt.figure(dpi=300, figsize=(amp.shape[1] / 100, amp.shape[0] / 100))
plt.imshow(hsv, interpolation='gaussian')
u = -np.cos(phase)
v = -np.sin(phase)
lw = np.where(amp > .1, 0, amp * factor)
X, Y = np.meshgrid(range(phase.shape[1]), range(phase.shape[0]))
plt.streamplot(X, Y, u, v, linewidth=lw, density=0.82)
plt.scatter(pos_x, pos_y, c='gray', s=size)
plt.ylim((0, amp.shape[0]))
plt.xlim((0, amp.shape[1]))
plt.show()