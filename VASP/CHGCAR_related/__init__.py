from pymatgen.io.vasp import Chgcar
import numpy as np


class Mychg(Chgcar):
    def get_average_along_axis_spin(self, ind):
        m = self.data["diff"]
        ng = self.dim
        if ind == 0:
            total = np.sum(np.sum(m, axis=1), 1)
        elif ind == 1:
            total = np.sum(np.sum(m, axis=0), 1)
        else:
            total = np.sum(np.sum(m, axis=0), 0)
        return total / ng[(ind + 1) % 3] / ng[(ind + 2) % 3]

def cut_chg_along_ax(chg, a, n):
    data = []
    for j in range(chg.dim[1]):
        for i in range(chg.dim[0]):
            for k in range(chg.dim[2]):
                if int(a * i - (1 - a) * k) == n:
                    data.append(chg.data['total'][i, j, k])
                    
    data = np.array(data)
    data = np.reshape(data, (chg.dim[1], len(data) // chg.dim[1]))
    return data.astype(float)

def cut_chg_along_diag(chg, n):
    data = []
    for j in range(chg.dim[1]):
        for i in range(chg.dim[0]):
            for k in range(chg.dim[2]):
                if i + k == int(chg.dim[0] + chg.dim[2]) / 2 + n:
                    data.append(chg.data['total'][i, j, k])
                    
    data = np.array(data)
    data = np.reshape(data, (chg.dim[1], len(data) // chg.dim[1]))
    return data.astype(float)