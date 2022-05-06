def plot():
    import matplotlib.pyplot as plt
    import numpy as np
    from cmath import sqrt
    eg = 4.9
    h = 6.582e-16  # ev * s
    c = 2.9979e+8  # m / s
    me = .511e+6 / c ** 2  # eV / c ** 2
    mc = 1.365 * me
    mv = 1.401 * me
    v = 1.38e+6  # m / s
    v = 0
    def eigen(k):
        k /= 1e-10
        b = h ** 2 * k ** 2 / 4 / (1 / mc + 1 / mv)
        c = sqrt((eg / 2) ** 2 + (h * k * v) ** 2 + h ** 4 * k ** 4 / 16 * (1 / mc - 1 / mv) ** 2)
        return b + c, b - c

    x = np.linspace(0, .5, 100)
    y = []
    y.extend([eigen(1j * r) for r in x])
    y = np.array(y)
    plt.scatter(x[y[:, 0] > 1e-3], y[:, 0][y[:, 0] > 1e-3])
    plt.scatter(x[y[:, 1] < -1e-3], y[:, 1][y[:, 1] < -1e-3])
    output = np.array([np.concatenate((x[y[:, 0] > 1e-3], x[y[:, 1] < -1e-3][::-1])),
                       np.concatenate((y[:, 0][y[:, 0] > 1e-3], y[:, 1][y[:, 1] < -1e-3][::-1]))], dtype=np.float)
    np.savetxt('cb.dat', output.transpose())
#    plt.show()


if __name__ == '__main__':
    plot()
