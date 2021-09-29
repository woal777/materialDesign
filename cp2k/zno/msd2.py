#%%

from MDAnalysis.analysis.rms import rmsd
from MDAnalysis.coordinates.XYZ import XYZReader
import matplotlib.pyplot as plt
# os.chdir('/home/jinho93/oxides/wurtzite/zno/cp2k/1.aimd/3.16A/30/3.fix')
os.chdir('/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/slab/gulp/nonstochio/La-vac/zero')

xyz = XYZReader('lao.xyz')
arr = []
arr2 = []
arr3 = []
arr4 = []
index = []
index2 = []
index3 = []
for i, j in enumerate(xyz[0].positions.copy()):
    if i < 300:
        continue
    if 12 < j[2] < 17:
        index.append(i)
    elif 17< j[2] < 19:
        index2.append(i)
    elif 19< j[2] > 21:
        index3.append(i)
for i in range(xyz.n_frames):
    arr.append(rmsd(xyz[0].positions.copy()[index[0]:index[-1]], xyz[i].positions.copy()[index[0]:index[-1]]))

for i in range(xyz.n_frames):
    arr2.append(rmsd(xyz[0].positions.copy()[index2[0]:index2[-1]], xyz[i].positions.copy()[index2[0]:index2[-1]]))

for i in range(xyz.n_frames):
    arr3.append(rmsd(xyz[0].positions.copy()[index3[0]:index3[-1]], xyz[i].positions.copy()[index3[0]:index3[-1]]))

fig = plt.Figure()
x = range(0, len(arr) * 3, 3)
plt.plot(x, arr, label='bulk')
plt.plot(x, arr2, label='b2')
plt.plot(x, arr3, label='VZn')
plt.legend()
plt.show()
# %%
