import re
import os
from pymatgen import Structure
os.chdir('/home/jinho93/oxides/cluster/zno/cp2k/bulk_opti/step2')
filename = 'zno-1.restart'
lat = []
coords = []
with open(filename) as f:
    coord = False
    for l in f:
        if re.search('A ', l) or re.search('B ', l) or re.search(' C ', l):
            lat.append([float(r) for r in l.split()[1:]])
        if re.search('COORD', l):
            coord = True
            continue
        if coord:
            if re.search('END', l):
                coord = False
                print('ok')
                continue
            elif re.search('SCALED', l):
                continue
            else:
                print(l)
                coords.append([float(r) for r in l.split()[1:]])
print(lat)
print(Structure(lat, ['O', 'Zn'], coords))