from pymatgen.io.pwscf import PWInput
from pymatgen import MPRester

mpr = MPRester()
s = mpr.get_structure_by_material_id('mp-20459')
# s.to('POSCAR', 'POSCAR')
PWInput.from_file()
pwin = PWInput(s, pseudo={'Pb': 'Pb.pbe-dn-kjpaw_psl.1.0.0.UPF', 'Ti': 'Ti.pbe-spn-kjpaw_psl.1.0.0.UPF',
                          'O': 'O.pbe-n-kjpaw_psl.1.0.0.UPF'}, kpoints_grid=(6, 6, 4), control={'outdir':'output', 'prefix':'scf'})
pwin.write_file('PTO-scf.in')
