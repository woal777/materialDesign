import numpy as np


def plot_eigenval(filename='EIGENVAL', fermi=0):
    arr = np.genfromtxt(filename, skip_header=8)
    output = []
    for i in arr[:, 1]:
        print(i - fermi)
        output.append([i - fermi, 0])
        output.append([i - fermi, 1])
        output.append([i - fermi, 0])
