from pymatgen import Structure

import sys
from pymatgen.io.xyz import XYZ as xyz
s = xyz.from_file('/home/jinho93/slab/LAO/nvt/gulp.xyz')
out = ''
sys.stdout = open('output.xyz', 'w')
for i in str(s).split(sep='\n'):
    if i.__contains__('5.71') or i.__contains__('3.81127'):
        continue
    else:
        if i[0] == 'O':
            tmp = i.split()
            tmp.insert(1, 'core')
            print(' '.join(tmp))
            tmp = i.split()
            tmp.insert(1, 'shel')
            print(' '.join(tmp))
        else:
            tmp = i.split()
            tmp.insert(1, 'core')
            print(' '.join(tmp))
