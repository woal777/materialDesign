#%%
import os
from pymatgen.core.sites import Site
from pymatgen.io.vasp.outputs import Outcar, Structure
import numpy as np
# os.chdir('/home/jinho93/oxides/perobskite/barium-titanate/vasp/2.pbesol/sto-strained/born')

#%%
os.chdir('/home/jinho93/new/oxides/fluorite/hfo2/enct/350')
s1 = Structure.from_file('CONTCAR')

out = Outcar('OUTCAR')

coulomb = 1.6e-19

output = np.zeros(3)
for i, j in zip(s1.frac_coords, out.born):
   vec = np.around(i * 4) / 4
   if 0.37 <i[1] < 0.375:
      vec[1] = 0.5
   if 0.87 <i[1] < 0.875:
          vec[1] = 1
   output += np.dot(j, (i - vec)) / s1.volume * coulomb *1e+20
   print(vec[1], i[1])
print(output[1] * s1.lattice.b)
