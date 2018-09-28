import pymatgen.command_line.gulp_caller as gc

gio = gc.GulpIO()
s:gc.Structure = gc.Structure.from_file('POSCAR')

gin = gio.buckingham_input(gc.Structure.from_file('POSCAR'), ['conv', 'opti'], library='woodley.lib',
                           valence_dict={gc.Element.Pb: 1, gc.Element.Ti: 4})
with open('gin', 'w') as f: f.write(gin)
