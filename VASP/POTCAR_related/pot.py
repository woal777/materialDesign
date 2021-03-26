#!/home/jinho93/miniconda3/bin/python
from pymatgen.io.vasp.inputs import Potcar
import os

site_symbols = []
with open('POSCAR') as f:
    site_symbols.extend(f.readline().split())
    try:
        if site_symbols == []:
            raise OSError()
        potcar = Potcar(site_symbols)
    except OSError:
        print('not first line')
        site_symbols = f.readlines()[4].split()
        potcar = Potcar(site_symbols)
print(site_symbols)
potcar.write_file('POTCAR')
