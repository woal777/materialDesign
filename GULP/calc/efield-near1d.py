#%%
import matplotlib.pyplot as plt
import numpy as np
import macrodensity as md
import math


position = []
charge = []
n = 10
dy = 0.2
for i in range(n + 1):
    for j in range(2):
        position.append([i, dy * j])
        if i % n == 0:
            charge.append(0.5)
        else:
            if i % 2 == 0:
                charge.append(1)
            else:
                charge.append(-1)
                
def distance(p1, p2):
    return math.sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))

def pot(r):
    arr = [i / distance(r, j) for i, j in zip(charge, position)]
    return sum(arr)

print(sum(charge))

space = n * 0.5
x = np.linspace(-space, n + space, 200)
y = [pot([r,dy / 2]) for r in x]
res = 1 / 20
macro = md.macroscopic_average(y, 1, res)
double_macro = md.macroscopic_average(macro, 1, res)
# plt.plot(x, y)
plt.plot(x, macro)
plt.plot(x, double_macro)
plt.show()

np.savetxt('1d.dat', np.array([x, y]).transpose())
np.savetxt('1d-macro.dat', np.array([x, double_macro]).transpose())

# %%
