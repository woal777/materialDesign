from subprocess import check_output
from cp2k.pdos import pdos
import numpy as np
import os
import matplotlib.pyplot as plt

os.chdir('/home/jinho93/molecule/ddt/cp2k/1-molecule/triplet/restart')
filename = [r for r in os.listdir(os.curdir) if r.__contains__('.pdos')]
print(filename)
element = [check_output(['head', '-n1', r]).split()[6].decode("utf-8") for r in filename]
dos = [pdos(i) for i in filename]
npts = len(dos[0].e)
if any(['BETA' in r for r in filename]):
    beta = [pdos(i) for i in filename if 'BETA' in i]
    alpha = [pdos(i) for i in filename if 'ALPHA' in i]
    smeared_dos = [np.append(i.smearing(npts, 0.01), -np.flip(j.smearing(npts, .01))) for i, j in zip(alpha, beta)]
    eigenvalues = np.linspace(min(dos[0].e), max(dos[0].e),npts)
    eigenvalues = np.append(eigenvalues, np.flip(eigenvalues))
else:
    smeared_dos = [i.smearing(npts, .05) for i in dos]
    eigenvalues = np.linspace(min(dos[0].e), max(dos[0].e),npts)

smeared_dos = np.array(smeared_dos)
output = np.column_stack((eigenvalues.transpose(), smeared_dos.transpose()))
for i in range(1, output.shape[1]):
    plt.plot(output[:,0], output[:,i])
plt.xlim((-100, 100))
plt.show()
np.savetxt('smeared.dat', output, fmt='%13.9f', delimiter='    ', header=' '.join(element))
