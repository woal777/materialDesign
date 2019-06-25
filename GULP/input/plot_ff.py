from pymatgen.command_line.gulp_caller import GulpCaller, GulpIO
from pymatgen import Structure
import numpy as np
import matplotlib.pyplot as plt


def get_energy(dis):
    gin = f'''conv
cart
Zn core 0 0 0
O  core 0 0 {dis}

library ABOP.lib
'''
    gout = gc.run(gin)
    return gio.get_energy(gout)


if __name__ == '__main__':
    gc = GulpCaller('/opt/gulp-5.1/Src/gulp')
    gio = GulpIO()
    arr = []
    for i in np.linspace(1, 2.5, 20):
        arr.append(get_energy(i))
        print(arr[-1])
    plt.plot(np.linspace(1, 2.5, 20), arr)
    plt.show()
