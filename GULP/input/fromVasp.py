from pymatgen import Structure
from pymatgen.command_line.gulp_caller import GulpIO, GulpCaller
import sys
path = '/home/jinho93/slab/LAO/nvt/line/'
path = '/home/jinho93/interface/tin-hfo2-tio2/gulp'
s: Structure = Structure.from_file(path + '/POSCAR')
gio = GulpIO()
sys.stdout = open(path + 'md.gin', 'w')
print(gio.buckingham_input(s, keywords=['conv', 'md', 'qok']))
gio.structure_lines(s, anion_shell_flg=False)