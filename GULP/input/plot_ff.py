from pymatgen.command_line.gulp_caller import GulpCaller, GulpIO
from pymatgen import Structure
import numpy as np
import matplotlib.pyplot as plt


def get_energy(dis):
    gin = f'''conv shell
cart
O  core 0 0 0
O  shel 0 0 0
O  core 0 0 {dis}
O  shel 0 0 {dis}

library whitmore2.lib
'''
    gout = gc.run(gin)
    return gio.get_energy(gout)


if __name__ == '__main__':
    gc = GulpCaller('/opt/gulp-5.1/Src/gulp')
    gio = GulpIO()
    arr = []
    for i in np.linspace(1.2, 3, 10):
        arr.append(get_energy(i))
        print(arr[-1])
    plt.plot(np.linspace(1.2, 3, 10), arr)
    plt.show()
