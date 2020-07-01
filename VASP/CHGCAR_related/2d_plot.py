from pymatgen.io.vasp import Chgcar
import os
import matplotlib.pyplot as plt
import numpy as np

os.chdir('/home/jinho93/interface/pzt-bso/loose/opti/band/parchg-195')
chg = Chgcar.from_file('PARCHG')
data = np.sum(chg.data['total'], axis=0)


def plotting(m):
    norm = plt.Normalize(0, np.max(data) * m)
    print(np.max(data))
    # plt.contourf(mx, my, data, levels=50, cmap='jet', locator=ticker.LogLocator())
    # data_log = np.log(data)
    plt.imshow(data, cmap='jet', interpolation='spline36', norm=norm)
    plt.axis('off')
    plt.colorbar()
    # plt.savefig(fname='parchg.png')
    plt.show()

plotting(1e+5)