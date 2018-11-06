import numpy as np
from pymatgen.io.vasp import Chgcar
import matplotlib.pyplot as plt


class Mychg(Chgcar):
    def get_average_along_axis2(self, ind):
        m = self.data["diff"]
        ng = self.dim
        if ind == 0:
            total = np.sum(np.sum(m, axis=1), 1)
        elif ind == 1:
            total = np.sum(np.sum(m, axis=0), 1)
        else:
            total = np.sum(np.sum(m, axis=0), 0)
        return total / ng[(ind + 1) % 3] / ng[(ind + 2) % 3]


chg = Mychg.from_file('CHGCAR')
chg = Mychg(chg.poscar, chg.data, chg.data_aug)
z = chg.get_average_along_axis2(2)

plt.plot(z)
plt.show()
np.savetxt('z.dat', z)
