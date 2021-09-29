
from pymatgen import Structure, Molecule
from pymatgen.command_line.gulp_caller import GulpIO, GulpCaller
import os
import sys
from pymatgen.core.lattice import Lattice

for i in range(680, 920, 10):
    os.chdir(f'/home/jinho93/oxides/perobskite/lanthanum-aluminate/slab/gulp/nonstochio/La-vac/{i}')
    m = Molecule.from_file('lao.xyz')
    s = Structure(Lattice.from_parameters(11.46615, 15.2882, 50, 90,90,90), m.species, m.cart_coords, coords_are_cartesian=True)
    gio = GulpIO()
    with open('md.gin', 'w') as f:
        f.write('conv\n')
        f.write('''svectors
 11.466150000000   0.000000000000   0.000000000000
  0.000000000000  15.288200000000   0.000000000000
''')
        f.write(gio.structure_lines(s, symm_flg=False, frac_flg=False, cell_flg=False))
        f.write('''
species   4
La     core    3.000000
O      core    0.040000
Al     core    3.000000
O      shel   -2.040000
buck
O     shel O     shel  9547.96000     0.219200  32.00000      0.00 16.00
buck
Al    core O     shel  1725.20000     0.289710  0.000000      0.00 16.00
buck
La    core O     shel  2088.79000     0.346000  23.25000      0.00 16.00
spring
O      6.3000000

potgrid 0 1 0 1 -10 50 25 25 250
''')