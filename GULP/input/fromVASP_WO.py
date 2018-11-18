path = '/home/jinho93/slab/LAO/nvt/'
g = open(path + 'SPOSCAR-reduced.xyz')
g2 = open(path + 'SPOSCAR-reduced')
lines = g.readlines()

atoms = [r.split() for r in lines[2:]]
atoms = sorted(atoms, key=lambda x: x[-1])
atoms = [r[0] + ' core ' + ' '.join(r[1:]) + '\n'
         +r[0] + ' shel ' + ' '.join(r[1:]) + '\n' for r in atoms]
with open(path + 'md.gin', 'w') as f:
    f.write('vectors\n')
    f.writelines(g2.readlines()[2:5])
    f.write('cart\n')
    f.writelines(atoms)
