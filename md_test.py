from pymatgen import MPRester, Structure
import sys
mpr = MPRester('DhmFQPuibZo8JtXn')
s: Structure = mpr.get_structure_by_material_id(sys.argv[1])
s.to('POSCAR', 'POSCAR')