from pymatgen.io.vasp.outputs import Outcar, Structure, Element
import os
os.chdir('/home/jinho93/molecule/ddt/vasp/ws2/ontop/en500/dense')
outcar = Outcar('OUTCAR')
s = Structure.from_file('POSCAR')
output = 0
for i, j in zip(s.sites, outcar.charge):
    if i.specie is Element.C or i.specie is Element.O or i.specie is Element.H:
        output += j['tot']
print(output)
os.chdir('/home/jinho93/molecule/ddt/vasp/ws2/ontop/en500/dipole/mole')
outcar = Outcar('OUTCAR')
s = Structure.from_file('POSCAR')
output = 0
for i, j in zip(s.sites, outcar.charge):
    if i.specie is Element.C or i.specie is Element.O or i.specie is Element.H:
        output += j['tot']
print(output)
