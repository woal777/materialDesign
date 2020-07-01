import math

from pymatgen import Structure, Element
import os
import numpy as np

os.chdir('/home/jinho93/interface/pzt-bso/loose/opti/dos')
s = Structure.from_file('CONTCAR')
sr = []
ti = []
z = []
for i in s.sites:
    if i.specie == Element.O:
        z.append(i.z)
    elif i.specie == Element.Ti or i.specie == Element.Sn:
        ti.append(i.z)
    elif i.specie is Element.Pb or i.specie == Element.Ba:
        sr.append(i.z)

arr_Sr = [(x, x - y) for x,y in zip(sorted(sr), sorted(z)[::3])]
arr_Ti = [(x, x - y) for x,y in zip(sorted(ti), sorted(z)[1::3])]
print(arr_Sr)
print(arr_Ti)
np.savetxt('sr.dat', arr_Sr, delimiter='\t')
np.savetxt('ti.dat', arr_Ti, delimiter='\t')