import numpy as np
import os
import matplotlib.pyplot as plt

os.chdir('/home/jinho93/molecule/ddt/vasp/2-sub/dos/smear')
arr = np.genfromtxt('EIGENVAL', skip_header=8)
fermi = -2.14731223
output = []
for i in arr[:, 1]:
    print(i - fermi)
    output.append([i - fermi, 0])
    output.append([i - fermi, 1])
    output.append([i - fermi, 0])
np.savetxt('output.dat', output)