import numpy as np
import os

os.chdir('/home/jinho93/molecule/ddt/cp2k/1-molecule/triplet/restart')
arr = np.genfromtxt('k1.dat')
print(arr)
