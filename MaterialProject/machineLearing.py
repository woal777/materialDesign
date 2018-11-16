import math
import numpy as np
import matplotlib.pyplot as plt
from pymatgen import MPRester, Structure
norm = np.linalg.norm


class Functional:
    def __init__(self):
        self.R = 3
        self.D = 0.2
        self.A = 3264.7
        self.B = 95.373
        self.lambda1 = 3.2394
        self.lambda2 = 1.3258

    def fc(self, x):
        if x < self.R - self.D:
            return 1
        elif x > self.R + self.D:
            return 0
        else:
            return 0.5 - 0.5 * math.sin(math.pi / 2 * (x - self.R) / self.D)

    def fr(self, r):
        return self.A * math.exp(- self.lambda1 * r)

    def fa(self, r):
        return - self.B * math.exp(- self.lambda2 * r)

    @staticmethod
    def get_angle(a, b, c):
        ba = a - b
        bc = c - b
        cosine_angle = np.dot(ba, bc) / (norm(ba) * norm(bc))
        angle = np.arccos(cosine_angle)
        return angle

    def v_ij(self, ri, rj, arr):
        a_ij = 1
        beta = 0.33675
        n = 22.956
        c = 4.8381
        d = 2.0417
        r_ij = np.linalg.norm(ri, rj)
        ksi = lambda: sum([self.fc(norm(ri, rk)) * g_theta(Functional.get_angle(ri, rj, rk)) *
                           math.exp(self.lambda2 ** 3 * (norm(ri, rj) - norm(ri, rk)) ** 3) for rk in arr])
        b_ij = lambda: 1 + beta ** n * ksi() ** n
        g_theta = lambda theta: 1 + c ** 2 / d ** 2 - c ** 2 / (d ** 2 + (math.cos(theta)) ** 2)

        return self.fc(r_ij) * (a_ij * b_ij() * self.fa(r_ij))


mpr = MPRester('DhmFQPuibZo8JtXn')
s: Structure = mpr.get_structure_by_material_id('mp-149')
for i in s.get_all_neighbors(3, True):
    for j in i:
        print(j)
#f = Functional()
#x = np.logspace(-5, 2, 1000)
#y = [f.fc(r) for r in x]
#plt.plot(x, y)
#plt.show()
