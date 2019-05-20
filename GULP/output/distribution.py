import os

import matplotlib.pyplot as plt
import numpy as np
from MDAnalysis import Universe
from MDAnalysis.coordinates.base import Timestep


class Anim:
    def __init__(self, u):
        self.u = u
        self.fig = plt.figure()
        self.ax = plt.axes(xlim=(0, 60), ylim=(0, 20))
        self.line, = self.ax.plot([], [], 'x', lw=2)
        self.line2, = self.ax.plot([], [], '+', lw=2)
        self.output = []

    @staticmethod
    def smearing(arr: list, sig):
        output = []
        for i in range(len(arr) - sig):
            output.append(sum(arr[i:i + sig]) / sig)
        return output

    def init(self):
        self.line.set_data([], [])
        return self.line,

    def animate(self, ind):
        i: Timestep = self.u.trajectory[ind]
        data = []
        data2 = []
        for j, k in zip(self.u.atoms, i.positions):
            if 0 < k[0] < 40 or -20 < k[1] < 20:
                if j.name == 'O':
                    data.append(k[2])
                else:
                    data2.append(k[2])
        hist, bin_edges = np.histogram(data, bins=np.arange(-0.00003, 60, 2.5984))
        oy = hist
        ox = np.linspace(0, 60, len(oy))
        self.output.append(ox)
        self.output.append(oy)
        self.line.set_data(ox, oy)
        hist, bin_edges = np.histogram(data2, bins=np.arange(-0.00003, 60, 2.5984))
        zny = hist
        znx = np.linspace(0, 60, len(zny))
        self.output.append(zny)
        self.line2.set_data(znx, zny)
        self.ax.set_ylim((0, max(zny) * 1.1))
        return self.line,


if __name__ == '__main__':
    os.chdir('/home/jinho93/oxides/cluster/zno/gulp/whitmore/line/conf4/')
    with open('output.xyz') as f:
        u = Universe(f)
        anim = Anim(u)
        anim.init()
        anim.animate(0)
        print(anim.output)
        np.savetxt('output.dat', np.array(anim.output).transpose())
        anim.fig.show()
