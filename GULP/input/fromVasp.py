from pymatgen import Structure
from pymatgen.command_line.gulp_caller import GulpIO, GulpCaller
import sys

s: Structure = Structure.from_file(sys.argv[1] + '/POSCAR')
gio = GulpIO()
gout = GulpCaller().run(gio.buckingham_input(s, keywords=['conv', 'qok', 'shell', 'opti']))
with open(sys.argv[1] + '/energy', 'w') as f: f.write(str(gio.get_energy(gout)))
