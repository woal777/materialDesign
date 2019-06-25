import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.animation import FuncAnimation
from pymatgen.io.vasp.outputs import Xdatcar
import os


class anim:
    def __init__(self):
        self.structures = Xdatcar('XDATCAR').structures
        self.fig, self.ax = plt.subplots()
        self.xdata, self.ydata = [], []
        self.ln, = plt.plot([], [], 'ro', color='black')

    def init(self):
        self.ax.set_xlim(-.1, 1.1)
        self.ax.set_ylim(-.1, 1.1)
        self.ax.set_xlabel('c axis')
        self.ax.set_ylabel('concentration')
        return self.ln,

    def update(self, frame):
        oxy = [site.z for site in self.structures[frame].sites if site.species_string is 'Zn']
        hist, _ = np.histogram(oxy, bins=20, range=(0, 20 * 2.584843396))
        self.ln.set_data(np.linspace(0, 1, len(hist)), hist/32)
        return self.ln,

    def draw(self):
        self.ani = FuncAnimation(self.fig, self.update, frames=range(len(self.structures)),
                                 init_func=self.init, blit=True)
        Writer = animation.writers['ffmpeg']
        writer = Writer(fps=5, metadata=dict(artist='Me'), bitrate=1800)
        self.ani.save('zn.mp4', writer=writer)


if __name__ == '__main__':
    os.chdir('/home/jinho93/oxides/cluster/zno/vasp/1.aimd/3.16A/20')
    anim = anim()
    anim.draw()
