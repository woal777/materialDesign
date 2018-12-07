from pymatgen.io.pwscf import PWInput
from pymatgen import MPRester
mpr = MPRester()
s = mpr.get_structure_by_material_id('mp-550893')
s.to('POSCAR', 'POSCAR')
#pwin = PWInput(s, pseudo={'Hf':'Hf.pbe-spn-kjpaw_psl.1.0.0.UPF', 'O': 'O.pbe-n-kjpaw_psl.1.0.0.UPF'}, kpoints_grid=(6, 6, 6))
#pwin.write_file('Hf-scf.in')
