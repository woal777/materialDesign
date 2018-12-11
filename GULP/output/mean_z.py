from MDAnalysis.coordinates.XYZ import XYZReader
import matplotlib.pyplot as plt
xyz = XYZReader('/home/jinho93/slab/LAO/grimes/nvt/300k/dense/frame2/final.xyz')
xyz2 = XYZReader('/home/jinho93/slab/LAO/grimes/nvt/600k/final/lao.xyz')
arr = []
arr2 = []


def rmsd(a1, a2):
    return sum(a2 - a1)


for i in range(xyz.n_frames):
    arr.append(rmsd(xyz[0]._z.copy(), xyz[i]._z.copy()))

for i in range(xyz2.n_frames):
    arr2.append(rmsd(xyz2[0]._z.copy(), xyz2[i]._z.copy()))

fig = plt.Figure()
fig.add_subplot(211)
plt.plot(arr)

fig.add_subplot(212)
plt.plot(arr2)
plt.show()
