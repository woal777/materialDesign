#%%
import numpy as np
import matplotlib.pyplot as plt


dxy = np.genfromtxt('dxy')
dyz = np.genfromtxt('dyz')
xi = np.linspace(-0.5, 0.5, 11)
x, y = np.meshgrid(xi, xi)
x = x.reshape(1, -1)[0]
y = y.reshape(1, -1)[0]
plt.scatter(x, y, dxy + dyz, c = dyz / (dxy + dyz), cmap='cool')
plt.colorbar()
# %%
x, y = np.meshgrid(xi, xi)
plt.contourf(x, y, dxy.reshape(11, -1), cmap='Reds', alpha=0.3)
plt.contourf(x, y, dyz.reshape(11, -1), cmap='Blues', alpha=0.3)
plt.show()