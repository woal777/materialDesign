from pymatgen import Structure, Element
import os
import numpy as np

if __name__ == '__main__':
    os.chdir('/home/jinho93/oxides/perobskite/lanthanum-aluminate/periodic_step/gulp/2.100/2.conf/modified')
    os.chdir('/home/jinho93/oxides/perobskite/lanthanum-aluminate/periodic_step/gulp/stengel/019')
    s = Structure.from_file('POSCAR')
    p = np.zeros(3)
    for i in s.sites:
        if i.specie == Element.Al:
            p += i.coords * 3
        elif i.specie == Element.La:
            p += i.coords * 3
        elif i.specie == Element.O:
            p += i.coords * -2

    print(p)