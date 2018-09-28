from pymatgen.command_line.gulp_caller import GulpIO, Structure

gio = GulpIO()
with open('gin', 'w') as f:
    f.write(
        gio.buckingham_input(Structure.from_file('hfo2-amor.cif'), ['conv', 'md'])
    )
    f.write('''ensemble nvt 0.1
temperature 300
equil 0.5 ps
produ 0.5 ps
timestep 0.001 ps
sample 0.0050 ps
iterations 5
''')
