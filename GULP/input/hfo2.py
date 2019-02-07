from pymatgen import MPRester, Structure, Specie
from pymatgen.command_line.gulp_caller import GulpCaller, GulpIO
from matplotlib import pyplot


mpr = MPRester()
mono: Structure = mpr.get_structure_by_material_id('mp-352')
s = mpr.get_structures('ZrO2')
ortho: Structure = mpr.get_structure_by_material_id('mp-685097')
tetra: Structure = mpr.get_structure_by_material_id('mp-1018721')
for j, i in enumerate(mono.sites):
    if str(i.specie) == 'Hf':
        print(i.specie)
        mono.replace(j, species=Specie('Zr'))
        break
for j, i in enumerate(mono.sites):
    if str(i.specie) == 'Hf':
        mono.replace(j, species=Specie('Zr'))
        break
for j, i in enumerate(tetra.sites):
    if str(i.specie) == 'Hf':
        tetra.replace(j, species=Specie('Zr'))
        break
for j, i in enumerate(ortho.sites):
    if str(i.specie) == 'Hf':
        ortho.replace(j, species=Specie('Zr'))
        break
for j, i in enumerate(ortho.sites):
    if str(i.specie) == 'Hf':
        ortho.replace(j, species=Specie('Zr'))
        break


gio = GulpIO()
gc = GulpCaller()
for i in [mono, ortho, tetra]:
    arr = []
    arr2 = []
    i.apply_strain(.05)
    for j in range(10):
        gin = gio.buckingham_input(i, ['conv'], library='morse.lib', alib=True)
        gout = gc.run(gin)
        print(gout)
        arr.append(i.density)
        arr2.append(gio.get_energy(gout) / i.volume)
        i.apply_strain(-.01)
    i.to('POSCAR', i.get_space_group_info()[0].replace('/', '_') + '.vasp')
    if i.get_space_group_info()[0] == 'P4_2/nmc':
        pyplot.plot(arr, [r * 2 for r in arr2], label=i.get_space_group_info()[0])
    else:
        pyplot.plot(arr, arr2, label=i.get_space_group_info()[0])
pyplot.legend()
pyplot.show()
