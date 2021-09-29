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
for t, trj in enumerate(u.trajectory[:300]):
    natom = 2
    for atom, pos in zip(u.atoms, trj):
        if t < 2:
            xy.append([pos[1], pos[2]])
            xy.append([pos[1] + b, pos[2]])
            a.append(0)
            a.append(0)
        else:            
            xy.append([pos[1], pos[2]])
            xy.append([pos[1] + b, pos[2]])
            # xy.append([(xy[-1][0] + pos[1]) / 2, (xy[-1][1] + pos[2]) / 2])
            # xy.append([(xy[-1][0] + pos[1]) / 2 + b, (xy[-1][1] + pos[2]) / 2])
            # dx = pos[1] - xy[0][0]
            # dy = pos[2] - xy[0][1]
            # dis = math.sqrt(dx ** 2 + dy ** 2)
            a.append(1 / 5)
            a.append(1 / 5)
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
plt.scatter(rxy[:,0], rxy[:,1], c=c, alpha=a, s=0.3)
plt.savefig('/home/jinho93/output.png')
# plt.xlim((0, b * 2))
# plt.ylim((0, 28.686268947600))
# plt.show()
# %%
