from pymatgen.command_line.gulp_caller import GulpIO, Structure
from pymatgen.io.xyz import XYZ
gio = GulpIO()
path = '/home/jinho93/slab/LAO/surf/'
with open(path + 'gin', 'w') as f:
    s = Structure.from_file(path + 'POSCAR')

    s.make_supercell([[1, 0, 0], [0, 1, 0], [0, 0, 2]])
    f.write(
        gio.structure_lines(s)
    )
