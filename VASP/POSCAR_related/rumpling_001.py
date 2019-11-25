import math

from pymatgen import Structure, Element
import os

os.chdir('/home/jinho93/oxides/perobskite/strontium-titanate/slab/nbsto/0.superlattice/4.long/20uc/symm/3.pure/5.percent/2.fix/2.parchg')

s = Structure.from_file('POSCAR')
sr = []
ti = []
z = []
for i in s.sites:
    if i.specie == Element.O:
        z.append(i.z)
    elif i.specie == Element.Ti:
        ti.append(i.z)
    elif i.specie is Element.Sr:
        sr.append(i.z)

print([x - y for x,y in zip(sorted(sr), sorted(z)[::3])])
print([x - y for x,y in zip(sorted(ti), sorted(z)[1::3])])
print(sorted(ti))
print(sorted(z)[1::3])
