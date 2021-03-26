import os
import numpy as np
from pymatgen import Molecule
os.chdir('/home/jinho93/oxides/perobskite/lanthanum-aluminate/periodic_step/gulp/2.100/2.conf')
h = Molecule.from_file('head.xyz')
t = Molecule.from_file('300k/tail.xyz')
rms = np.array([np.sqrt(np.mean(y**2)) for y in (t.cart_coords - h.cart_coords)])
g = open('reg.xyz', 'w')

oxygen_list = np.array(range(540))[rms > 1.]
oxygen_list += 2
with open('lao.xyz') as f:
    for i in range(200):
        for j in range(542):
            if j in oxygen_list:
                tmp = f.readline()
                tmp = tmp.replace('O', 'F')
                g.write(tmp)
            else:
                g.write(f.readline())

g.close()
