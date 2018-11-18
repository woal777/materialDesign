from pymatgen import Structure

s = Structure.from_file('/home/jinho93/slab/LAO/opt/opt.cif')
s.to('POSCAR', '/home/jinho93/slab/LAO/opt/POSCAR')
