from pymatgen.command_line.gulp_caller import GulpIO
gio = GulpIO()
with open('/home/jinho93/slab/LAO/grimes/nvt/dense/report.gulp') as f:
    s = gio.get_iniitial_structure(f.read())
    print(s)