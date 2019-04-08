from pymatgen.io.vasp.outputs import Element, Structure
import os
import numpy as np

os.chdir('/home/ksrc5/FTJ/bfo')

s = Structure.from_file('r3c_gaf_relaxed.vasp')
output2 = np.zeros(3)
for i in s.sites:
    if i.specie == Element.Fe or i.specie == Element.Bi:
        output = np.zeros(3)
        n = 0
        for j in s.get_neighbors(i, 2.7):
            output += j[0].coords
            n += 1
        output2 += (output / n - i.coords)
print(output2)