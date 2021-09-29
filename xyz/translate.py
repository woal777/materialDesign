import os
from pymatgen.io.xyz import XYZ

os.chdir('/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/periodic_step/gulp/015/0/thick/4')

xyz = XYZ.from_file('lao.xyz')

XYZ.from