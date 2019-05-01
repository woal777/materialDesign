import os

from MDAnalysis import Universe
from matplotlib import animation

from GULP.output.distribution import Anim

os.chdir('/home/jinho93/oxides/cluster/zno/line-defect/sub-defect/900k')
f = open('cluster.xyz')
u = Universe(f)


if __name__ == '__main__':

    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=5, metadata=dict(artist='Me'), bitrate=1800)
    Anim = Anim()
    anim = animation.FuncAnimation(Anim.fig, Anim.animate, init_func=Anim.init, frames=len(u.trajectory), interval=20)
    anim.save('exAnimation.mp4', writer=writer)
