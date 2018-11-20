path = '/home/jinho93/slab/LAO/grimes/opt/slab/'
g = open(path + 'SPOSCAR-reduced.xyz')
g2 = open(path + 'SPOSCAR-reduced')
lines = g.readlines()

atoms = [r.split() for r in lines[2:]]
atoms = sorted(atoms, key=lambda x: x[-2])
atoms = sorted(atoms, key=lambda x: x[-1])

polarize = True
if polarize:
    atoms = [r[0] + ' core ' + ' '.join(r[1:]) + '\n' for r in atoms]
    with open(path + 'md.gin', 'w') as f:
        f.write('vectors\n')
        f.writelines(g2.readlines()[2:5])
        f.write('cart\n')
        f.writelines(atoms)
        atoms = [r.replace('core', 'shel') for r in atoms if r.__contains__('O ')]
        f.writelines(atoms)
        f.write('''library grimes.lib

ensemble nvt 0.1
integrator verlet
temperature 300
equilbration 0.02 ps
produ 0.40 ps
timestep     0.001 ps
sample       0.010 ps
write        0.010 ps
dump every   1 example15.grs
output dcd lao
output movie xyz lao
tether 1-392

iterations 10
''')
else:
    atoms = [r[0] + ' core ' + ' '.join(r[1:]) + '\n'
             + r[0] + ' shel ' + ' '.join(r[1:]) + '\n' for r in atoms]
    with open(path + 'md.gin', 'w') as f:
        f.write('vectors\n')
        f.writelines(g2.readlines()[2:5])
        f.write('cart\n')
        f.writelines(atoms)
        f.write('''library grimes.lib

ensemble nvt 0.1
integrator verlet
temperature 300
equilbration 0.02 ps
produ 0.40 ps
timestep     0.001 ps
sample       0.010 ps
write        0.010 ps
dump every   1 example15.grs
output dcd lao
output movie xyz lao
tether 1-392

iterations 10
''')