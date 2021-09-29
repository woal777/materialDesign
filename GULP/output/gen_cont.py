import subprocess
from pymatgen import Structure, Molecule

lnum = int(subprocess.check_output(['head','-n 1', 'lao.xyz']).split()[0])

content = subprocess.check_output(['tail', f'-n {lnum + 2}', 'lao.xyz'])
    
m = Molecule.from_str(content.decode('utf-8'), fmt='xyz')
pos = Structure.from_file('POSCAR')

s = Structure(pos.lattice, m.species, m.cart_coords, coords_are_cartesian=True)

s.to('POSCAR', 'CONTCAR')