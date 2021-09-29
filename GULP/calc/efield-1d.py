#%%
import matplotlib.pyplot as plt
import numpy as np
import macrodensity as md


position = [0, 1, 2, 3, 4]
charge = [0.5, -1, 1, -1, 0.5]

def pot(r):
    arr = [i / abs(r - j) for i, j in zip(charge, position)]
    
    return sum(arr)


x = np.linspace(-2.1, 6.1, 100)
y = [pot(r) for r in x]
macro = md.macroscopic_average(y, 1, 0.1)
double_macro = md.macroscopic_average(macro, 1, 0.05)
double_macro = md.macroscopic_average(double_macro, 1, 0.05)
plt.plot(x, y)
# plt.plot(x, macro)
plt.plot(x, double_macro)

np.savetxt('1d.dat', np.array([x, y]).transpose())
np.savetxt('1d-macro.dat', np.array([x, double_macro]).transpose())
plt.show()