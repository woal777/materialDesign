#%%

from MDAnalysis.core.universe import Universe
import os
import numpy as np
import matplotlib.pyplot as plt
# os.chdir('/home/jinho93/oxides/perobskite/lanthanum-aluminate/periodic_step/gulp/8.108/fix')
os.chdir('/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/periodic_step/gulp/015/0/thick/4')
# os.chdir('/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/my015/from-gulp/421/test')
p_arr = []
u = Universe('lao.xyz')

#%%
import math
b = 19.433719705500
fig = plt.figure(figsize=(19.433719705500 / 5*2, 28.686268947600 / 5), dpi=300)

xy = []
c = []
a = []
s = []
for t, trj in enumerate(u.trajectory[:180]):
    natom = 2
    for n, (atom, pos) in enumerate(zip(u.atoms, trj)):
        if t < 2:
            xy.append([pos[1], pos[2]])
            xy.append([pos[1] + b, pos[2]])
        else:            
            xy.append([pos[1], pos[2]])
            xy.append([pos[1] + b, pos[2]])
            # xy.append([(xy[-1][0] + pos[1]) / 2, (xy[-1][1] + pos[2]) / 2])
            # xy.append([(xy[-1][0] + pos[1]) / 2 + b, (xy[-1][1] + pos[2]) / 2])
            # dx = pos[1] - xy[0][0]
            # dy = pos[2] - xy[0][1]
            # dis = math.sqrt(dx ** 2 + dy ** 2)
        if n == 166 or n == 89:
            if t % 30 == 0:
                a.append(1)
                a.append(1)
            else:
                a.append(.05)
                a.append(.05)                
            c.extend([(1, 0.5 - t / 360, 0)] * 2)
            continue
        if n == 45 or n == 44:
            if t % 30 == 0:
                a.append(1)
                a.append(1)
            else:
                a.append(.05)
                a.append(.05)                
            c.extend([(0, 0.5 - t / 360, 1)] * 2)
            continue
        a.append(1 / 100)
        a.append(1 / 100)
        if atom.name == 'Al':
            c.extend(['green'] * natom)
        elif atom.name == 'La':
            c.extend(['blue'] * natom)
        elif atom.name == "O":
            c.extend(['red'] * natom)

xy = np.array(xy)

theta = -math.atan(1/5)
cos, sin = np.cos(theta), np.sin(theta)
R = np.array(((cos, -sin), (sin, cos)))
rxy = []

for r in xy:
    rxy.append(np.dot(R, r))

rxy = np.array(rxy)
plt.scatter(rxy[:,0], rxy[:,1], c=c, alpha=a, s=6)
plt.savefig('/home/jinho93/output.png')
# plt.xlim((0, b * 2))
# plt.ylim((0, 28.686268947600))
# plt.show()
# %%
