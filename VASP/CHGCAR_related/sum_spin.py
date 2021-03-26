import numpy as np
from pymatgen.io.vasp import Chgcar
import matplotlib.pyplot as plt
import os

class Mychg(Chgcar):
    def get_average_along_axis2(self, ind):
        m = self.data["total"]
        ng = self.dim
        if ind == 0:
            total = np.sum(np.sum(m, axis=1), 1)
        elif ind == 1:
            total = np.sum(np.sum(m, axis=0), 1)
        else:
            total = np.sum(np.sum(m, axis=0), 0)
        return total / ng[(ind + 1) % 3] / ng[(ind + 2) % 3]

os.chdir('/home/jinho93/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/stengel/001/vca/AlO2/parchg')
os.chdir('/home/jinho93/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/stengel/001/vca/LaO/parchg')
chg = Mychg.from_file('PARCHG')
chg = Mychg(chg.poscar, chg.data, chg.data_aug)
z = chg.get_average_along_axis2(2)

plt.plot(z)
plt.show()
np.savetxt('z.dat', z)
