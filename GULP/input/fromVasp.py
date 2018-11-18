from pymatgen import Structure
from pymatgen.command_line.gulp_caller import GulpIO, GulpCaller
import sys
path = '/home/jinho93/slab/LAO/nvt/'
s: Structure = Structure.from_file(path + '/SPOSCAR-reduced')
gio = GulpIO()
sys.stdout = open(path + 'md.gin', 'w')
print(gio.buckingham_input(s, keywords=['conv', 'md', 'qok']))
