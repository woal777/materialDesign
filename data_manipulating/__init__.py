import numpy as np
import os

os.chdir('/home/jinho93/oxides/cluster/zno/cp2k/1.aimd/3.16A/30/3.fix/2.again/')
dat = []
for i in range(1, 10):
    arr = np.genfromtxt(f'rdf{i}.dat')
    if i is 1:
        dat.append(arr[:,0])
    dat.append(arr[:,1])

dat = np.array(dat)
np.savetxt('output.dat', dat.transpose())