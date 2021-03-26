from pymatgen.io.vasp.outputs import Structure
import os

os.chdir('/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/bulk/hse/polaron')
s = Structure.from_file('POSCAR')

s.translate_sites(range(len(s.sites)), [0.5, 0.5, 0], frac_coords=True)
s.to('POSCAR', 'POSCAR')