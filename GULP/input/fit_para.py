import math
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(2.5e-1, 12, 500)
k = 8.99e+9 * 6241506479963200000 * 1e+10 / 6.24150975e+18 ** 2
print(k * 4)
a, rho, c = list(map(float, '0.99628741     2.439887   0.4742'.split()))
y = a * np.exp(-x / rho) - c / np.power(x, 6)  # 5.76e+1 / x
plt.plot(x, y, label='tot')
plt.xlim(0,12)
plt.ylim(-15,30)
plt.legend()
plt.show()
