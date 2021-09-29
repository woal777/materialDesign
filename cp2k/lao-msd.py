#%%

import os
from MDAnalysis.analysis.rms import rmsd
from MDAnalysis.coordinates.XYZ import XYZReader
from MDAnalysis.coordinates.base import Timestep
import matplotlib.pyplot as plt
# os.chdir('/home/jinho93/oxides/wurtzite/zno/cp2k/1.aimd/3.16A/30/3.fix')
os.chdir('/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/slab/gulp/nonstochio/La-vac/one')

xyz = XYZReader('lao-one.xyz')
xyz2 = XYZReader('../zero/lao.xyz')

xyz3 = XYZReader('/home/jinho93/oxides/perobskite/lanthanum-aluminate/slab/gulp/nonstochio/La-vac/two/lao.xyz')

arr = []
arr2 = []
arr3 = []
index = []
index2 = []
index3 = []

for i, j in enumerate(xyz[0].positions.copy()):
    if 36 < j[2] and j[0] % 1.9 < 0.1:
        index.append(i)

for i in range(xyz.n_frames):
    arr.append(rmsd(xyz[0].positions.copy()[index[0]:index[-1]], xyz[i].positions.copy()[index[0]:index[-1]]))

for i, j in enumerate(xyz2[0].positions.copy()):
    if 36 < j[2] and j[0] % 1.9 < 0.1:
        index2.append(i)

for i in range(xyz2.n_frames):
    arr2.append(rmsd(xyz2[0].positions.copy()[index[0]:index[-1]], xyz2[i].positions.copy()[index[0]:index[-1]]))

for i, j in enumerate(xyz3[0].positions.copy()):
    if 36 < j[2] and j[0] % 1.9 < 0.1:
        index3.append(i)

for i in range(xyz3.n_frames):
    arr3.append(rmsd(xyz3[0].positions.copy()[index[0]:index[-1]], xyz3[i].positions.copy()[index[0]:index[-1]]))

fig = plt.Figure()
x = range(0, len(arr) * 10, 10)
plt.plot(x, arr, label='one')
plt.plot(x, arr2, label='zero')
plt.plot(x, arr3, label='two')
plt.legend()
plt.show()
# %%
