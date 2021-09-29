#%%
from pymatgen import Element
from pymatgen.io.xyz import XYZ
import matplotlib.pyplot as plt

import os
os.chdir('/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/periodic_step/cp2k/015_thick4/2000k')
xyz = XYZ.from_file('lao-pos-1.xyz')
output = []
for structure in xyz.all_molecules:
    p = 0
    la = []
    al = []
    o = []
    for i in structure.sites:
        if i.specie == Element.O:
            p -= 2 * i.z
        elif i.specie == Element.Al:
            p += 3 * i.z
        elif i.specie is Element.La:
            p += 3 * i.z
    
    output.append(p)    

plt.plot(output)