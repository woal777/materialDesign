from pymatgen.command_line.gulp_caller import GulpIO, Structure
gio = GulpIO()
gio.specie_potential_lines()
with open('gin', 'w') as f:
    f.write(
        gio.buckingham_input(Structure.from_file('hfo2-amor.cif'), ['conv', 'qok'])
    )
    f.write('''''')
