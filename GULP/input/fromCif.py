from pymatgen.command_line.gulp_caller import GulpIO, Structure
from pymatgen.io.xyz import XYZ
gio = GulpIO()
name = 'C'
path = f'/home/share/SiCOH/{name}'
with open(path + '/md.gin', 'w') as f:
    s = Structure.from_file(path + f'/{name}.cif')
    f.write(
        gio.structure_lines(s)
    )
