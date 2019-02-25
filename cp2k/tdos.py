from subprocess import check_output
from cp2k.pdos import pdos, sum_tpdos, tdos
import numpy as np
from functools import reduce
import os
os.chdir('/home/jinho93/oxides/amorphous/igzo/hydrogen-oxygen/dos/cp2k/lsd')
filename = [r for r in os.listdir(os.curdir) if r.__contains__('.pdos')]
element = [check_output(['head', '-n1', r]).split()[6].decode("utf-8") for r in filename]
dos = [pdos(i) for i in filename]
npts = len(dos[0].e)

tpdos = tdos(reduce(sum_tpdos, [r.tpdos for r in dos]), dos[0].efermi, dos[0].e)

smeared_dos = tpdos.smearing(npts, .02)
eigenvalues = np.linspace(min(dos[0].e), max(dos[0].e),npts)

smeared_dos = np.array(smeared_dos)
output = np.column_stack((eigenvalues.transpose(), smeared_dos.transpose()))

np.savetxt('total.dat', output, fmt='%13.9f', delimiter='    ', header=' '.join(element))
