#%%
from numpy.lib.npyio import genfromtxt
from pymatgen import Structure
from pymatgen.core.periodic_table import Element
from pymatgen.core.sites import Site
import os
os.chdir('/home/share/14_after/structure')
os.chdir('/home/jinho93/molecule/dems/25/120/ela')
s = Structure.from_file(f'POSCAR')
bondings = []
i:Site
j:Site
for i in s.sites:
    if i.species_string == 'O':
        n = 0
        m = 0
        for j in s.get_neighbors(i, 1.99):
            if j.species_string == 'Si':
                n += 1
            elif j.species_string == 'C':
                m += 1
        bondings.append([n, m])
        
ter, brig = 0, 0
for b in bondings:
    if b[0] == 1 and b[1] == 0:
        ter += 1
    elif b[0] == 2 and b[1] == 0:
        brig += 1

print(ter, brig)
#%%
from pymatgen import Structure
from pymatgen.core.sites import Site
import os
os.chdir('/home/share/14_after/structure')
for n in range(1, 9):
    s = Structure.from_file(f'POSCAR{n}')
    bondings = []
    i:Site
    j:Site
    for i in s.sites:
        if i.species_string == 'O':
            n = 0
            m = 0
            for j in s.get_neighbors(i, 1.99):
                if j.species_string == 'C':
                    n += 1
                elif j.species_string == 'Si':
                    m += 1
            bondings.append([n, m])
            
    ter, brig = 0, 0
    for b in bondings:
        if b[0] == 1 and b[1] == 0:
            ter += 1
        elif b[0] == 2 and b[1] == 0:
            brig += 1

    print(ter, brig)
# %%

import numpy as np
import macrodensity as md
arr = np.genfromtxt('/home/jinho93/molecule/dems/25/100/temp.dat')
arr = arr[:,3]
mac = md.macroscopic_average(arr, 1, 0.1)
import matplotlib.pyplot as plt

plt.plot(mac)

np.savetxt('/home/jinho93/mac.dat', mac)
# %%
a = np.genfromtxt('mac.dat')
# %%
print(a)
# %%
from pymatgen.io.vasp import Vasprun
from pymatgen import Element
from pymatgen.electronic_structure.plotter import DosPlotter
dsp = DosPlotter()
vrun = Vasprun('vasprun.xml')
dsp.add_dos('total', vrun.tdos)
dsp.show(xlim=(-1, 1.5))