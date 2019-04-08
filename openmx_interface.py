import seekpath
from pymatgen import Structure
import os


os.chdir('/home/ksrc5/FTJ/bfo/sto-bfo')
s = Structure.from_file('POSCAR')
skp = seekpath.get_explicit_k_path(s)
print(skp)