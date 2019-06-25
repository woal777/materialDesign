from pymatgen.io.vasp.outputs import Outcar, Structure
import os
import numpy as np

os.chdir('/home/jinho93/molecule/oep-sub_fe/110-oxygen/4-third/30_amin/gr')
outcar = Outcar('OUTCAR')
s = Structure.from_file('POSCAR')

mag = np.zeros(3)
for i, j in zip(s.sites, outcar.magnetization):
    if i.c < .2:
        mag[0] += j['tot']
    elif i.c < .3:
        mag[1] += j['tot']
    elif i.c < .34:
        mag[2] += j['tot']
print(mag/48)

c = np.zeros(4)
num = np.zeros(4)
for i, j in zip(s.sites, outcar.magnetization):
    if i.c < .2:
        c[0] += i.z
        num[0] += 1
    elif i.c < .3:
        c[1] += i.z
        num[1] += 1
    elif i.c < .34:
        c[2] += i.z
        num[2] += 1
    elif i.c < .4:
        c[3] += i.z
        num[3] += 1
c /= num
print(c[3] - c[2], c[1] - c[0])
