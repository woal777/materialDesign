from MDAnalysis import Universe
from MDAnalysis.coordinates.base import Timestep
from MDAnalysis.core.groups import Atom
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from scipy.ndimage.filters import gaussian_filter

os.chdir('/home/jinho93/oxides/cluster/zno/line-defect/sub-defect/900k')
f = open('cluster.xyz')
u = Universe(f)


def smearing(arr: list, sig):
    output = []
    for i in range(len(arr) - sig):
        output.append(sum(arr[i:i + sig]) / sig)
    return output


def init():
    line.set_data([], [])
    return line,


def animate(ind):
    i: Timestep = u.trajectory[ind]
    data = []
    for j, k in zip(u.atoms, i.positions):
        if j.name == 'O':
            data.append(k[2])
    hist, bin_edges = np.histogram(data, bins=np.linspace(0, 60, 600))
    y = smearing(hist, 5)
    x = np.linspace(0, 60, len(y))
    line.set_data(x, y)
    print('ani')
    return line,


if __name__ == '__main__':
    fig = plt.figure()
    ax = plt.axes(xlim=(0, 60), ylim=(0, 20))
    line, = ax.plot([], [], lw=2)
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=5, metadata=dict(artist='Me'), bitrate=1800)

    anim = animation.FuncAnimation(fig, animate, init_func=init, frames=len(u.trajectory), interval=20)
    anim.save('exAnimation.mp4', writer=writer)
