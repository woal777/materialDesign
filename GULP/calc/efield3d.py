#%%
import matplotlib.pyplot as plt
import numpy as np
import macrodensity as md
import math


position = []
charge = []
n = 20
for i in range(n + 1):
    for j in range(n):
        for k in range(n):
            if i % n == 0:
                if j % 2 == 1 and k % 2 == 0:
                    charge.append(2)
                    position.append([i, j, k])
                elif j % 2 == 0 and k % 2 == 1:
                    charge.append(-1.5)
                    position.append([i, j, k])
            else:
                if i % 2 == 0:
                    if j % 2 == 1 and k % 2 == 0:
                        charge.append(3)
                        position.append([i, j, k])
                    elif j % 2 == 0 and k % 2 == 1:
                        charge.append(-2)
                        position.append([i, j, k])
                else:
                    if (j % 2 + k % 2) % 2 == 0:
                        charge.append(-2)
                        position.append([i, j, k])
                    elif j % 2 == 0 and k % 2 == 1:
                        charge.append(3)
                        position.append([i, j, k])
                
def distance(p1, p2):
    return math.sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2)+((p1[2]-p2[2])**2))

def pot(r):
    arr = [i / distance(r, j) for i, j in zip(charge, position)]
    return sum(arr)

print(sum(charge))

space = n * 0.7
x = np.linspace(-space - 0.1, n + space + 0.1, 200)
y = [pot([r, (n - 1) / 2, (n - 1) / 2]) for r in x]
res = 0.05
macro = md.macroscopic_average(y, 1, res)
double_macro = md.macroscopic_average(macro, 1, res)
plt.plot(x, y)
plt.plot(x, macro)
plt.plot(x, double_macro)
plt.show()

np.savetxt('1d.dat', np.array([x, y]).transpose())
np.savetxt('1d-macro.dat', np.array([x, double_macro]).transpose())
