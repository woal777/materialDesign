import os
from pymatgen.io.vasp.outputs import Outcar, Structure
import numpy as np
os.chdir('/home/ksrc5/FTJ/bfo/misfit-2p/test')
s1 = Structure.from_file('POSCAR')
s2 = Structure.from_file('POSCAR-sym')
out = Outcar('OUTCAR')
output = np.zeros(3)
for i, j, k in zip(s1.frac_coords, s2.frac_coords, out.born):
    output += np.dot(k, (i - j))
print(output)
