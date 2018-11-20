from pymatgen import Structure
import numpy as np

path = '/home/jinho93/slab/LAO/opt/grimes/'
s: Structure = Structure.from_file(path + 'opt.cif')
arr = np.identity(3) * 14
arr[2][2] = 6
s.make_supercell(arr)
s.to('POSCAR', path + 'SPOSCAR')
