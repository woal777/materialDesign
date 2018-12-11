from MDAnalysis.analysis.rms import rmsd
from MDAnalysis.coordinates.XYZ import XYZReader
import matplotlib.pyplot as plt

xyz = XYZReader('/home/jinho93/slab/LAO/grimes/nvt/300k/dense/frame2/final.xyz')
xyz2 = XYZReader('/home/jinho93/slab/LAO/grimes/nvt/600k/final/lao.xyz')
arr = []
arr2 = []
index = []
for i, j in enumerate(xyz[0].positions.copy()):
    if j[2] > 20:
        index.append(i)
for i in range(xyz.n_frames):
    arr.append(rmsd(xyz[0].positions.copy()[index[0]:index[-1]], xyz[i].positions.copy()[index[0]:index[-1]]))

for i in range(xyz2.n_frames):
    arr2.append(rmsd(xyz2[0].positions.copy()[index[0]:index[-1]], xyz2[i].positions.copy()[index[0]:index[-1]]))

fig = plt.Figure()
fig.add_subplot(211)
plt.plot(arr)
fig.add_subplot(212)
plt.plot(arr2)
plt.show()