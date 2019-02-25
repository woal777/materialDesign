from subprocess import check_output
from cp2k.pdos import pdos, sum_tpdos
import numpy as np
from functools import reduce
import os
os.chdir('/home/jinho93/oxides/amorphous/igzo/hydrogen-oxygen/dos/cp2k/lsd')
filename = [r for r in os.listdir(os.curdir) if r.__contains__('.pdos')]
element = [check_output(['head', '-n1', r]).split()[6].decode("utf-8") for r in filename]
dos = [pdos(i) for i in filename]
npts = len(dos[0].e)

beta = [pdos(i) for i in filename if 'BETA' in i]
alpha = [pdos(i) for i in filename if 'ALPHA' in i]
all = [i.__add__(j) for i, j in zip(alpha, beta)]
smeared_dos = [r.smearing(npts, 0.02) for r in alpha]
eigenvalues = np.linspace(min(dos[0].e), max(dos[0].e),npts)

smeared_dos = np.array(smeared_dos)
output = np.column_stack((eigenvalues.transpose(), smeared_dos.transpose()))

np.savetxt('smeared.dat', output, fmt='%13.9f', delimiter='    ', header=' '.join(element))
