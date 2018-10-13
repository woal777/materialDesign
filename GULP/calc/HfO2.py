from pymatgen import MPRester, Structure
from pymatgen.command_line.gulp_caller import GulpCaller, GulpIO
from matplotlib import pyplot


mpr = MPRester()
mono: Structure = mpr.get_structure_by_material_id('mp-352')
ortho: Structure = mpr.get_structure_by_material_id('mp-685097')
tetra: Structure = mpr.get_structure_by_material_id('mp-1018721')

gio = GulpIO()
gc = GulpCaller()
for i in [mono, ortho, tetra]:
    arr = []
    arr2 = []
    for j in range(20):
        gin = gio.buckingham_input(i, ['conv'], library='morse.lib', alib=True)
        gout = gc.run(gin)
        arr.append(i.volume)
        arr2.append(gio.get_energy(gout))
        i.apply_strain(-.01)
    i.to('POSCAR', i.get_space_group_info()[0].replace('/', '_') + '.vasp')
    if i.get_space_group_info()[0] == 'P4_2/nmc':
        pyplot.plot([r *2 for r in arr],[r * 2 for r in arr2], label=i.get_space_group_info()[0])
    else:
        pyplot.plot(arr, arr2, label=i.get_space_group_info()[0])
pyplot.legend()
pyplot.show()