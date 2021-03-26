import math

from pymatgen import Structure, Element
from pymatgen.io.vasp import Oszicar, Xdatcar, Vasprun
import os
import numpy as np
os.chdir('/home/jinho93/interface/lsmo-bto-pt/2.vaccum/baobao/up/again')
dat = Xdatcar('XDATCAR')
zicar = Oszicar('OSZICAR')
vrun = Vasprun('vasprun.xml')
energies = zicar.ionic_steps
selective = [r.properties['selective_dynamics'][2] for r in vrun.final_structure.sites]
output = []
ionic = vrun.ionic_steps
for s, e, ion in zip(dat.structures, energies, ionic):
    sr = []
    ti = []
    z = []
    for i in s.sites:
        if i.specie == Element.O:
            z.append(i.z)
        elif i.specie == Element.Ti or i.specie == Element.Ti:
            ti.append(i.z)
        elif i.specie is Element.Ba or i.specie == Element.Ba:
            sr.append(i.z)

    arr_Sr = [x - y for x,y in zip(sorted(sr[1:]), sorted(z)[2::3])]
    arr_Ti = [x - y for x,y in zip(sorted(ti), sorted(z)[1::3])]
    if max(np.array(ion['forces'])[:, 2][selective]) < .2:
        print(np.array(ion['forces'])[:, 2][selective])
        output.append((2 * sum(arr_Ti) + sum(arr_Sr), e['E0']))

np.savetxt('output.dat', output)
