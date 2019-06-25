from pymatgen import Structure, Spin
from pymatgen.io.vasp.outputs import Vasprun
import os

os.chdir('/home/jinho93/oxides/amorphous/igzo/1.from_jaejin/1.orig')
s = Structure.from_file('POSCAR')
for i in s.sites:
    print(len(s.get_neighbors(i, 2.5)), i.species_string)

vrun = Vasprun("vasprun.xml")
for i in vrun.eigenvalues[Spin.up][0]:
    print(i)
