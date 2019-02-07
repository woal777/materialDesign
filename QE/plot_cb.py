import numpy as np
from matplotlib import pyplot as plt


def PolyCoefficients(x, coeffs):
    """ Returns a polynomial for ``x`` values for the ``coeffs`` provided.

    The coefficients must be in ascending order (``x**0`` to ``x**o``).
    """
    o = len(coeffs)
    y = 0
    for i in range(o):
        y += coeffs[i] * x ** i

    return x[y < 0], y[y < 0]


x = np.linspace(-5, 2, 200)
coeffs = [-0.18983,
0.03621,
0.0417,
0.03046,
0.01394]
plt.plot(*PolyCoefficients(x, coeffs))
arr = PolyCoefficients(x, coeffs)
arr = np.array(arr)
arr = np.flip(arr, axis=0)
np.savetxt('output.dat', arr.transpose())
#plt.show()
