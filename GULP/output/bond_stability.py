from pymatgen import Structure
import os

os.chdir('/home/jinho93/oxides/cluster/tio2/anatase/gulp/19.5/data')
poscar = open('POSCAR', 'w')
with open('head.xyz') as f:
    n = int(f.readline())
    _ = f.readline()
    lines = f.readlines()
    lines = sorted(lines, key=lambda  x: x[0])
    n1 = 0
    n2 = 0
    for _ in lines:
        if _.__contains__('Ti'):
            n1 += 1
        else:
            n2 += 1
    poscar.write('''O Ti
1.0
        36.0000000000         0.0000000000         0.0000000000
        0.0000000000         36.0000000000         0.0000000000
        0.0000000000         0.0000000000        70.0000000000
''')
    poscar.write('  O  Ti\n'.format(n1, n2))
    poscar.write('  {:02d}  {:02d}\n'.format(n2, n1))
    poscar.write('Cartesian\n')
    for l in lines:
        poscar.write(l[3:])
poscar.close()

s = Structure.from_file('POSCAR')
s.translate_sites(range(s.num_sites), (15, 15, 30), frac_coords=False)
s.to('POSCAR', 'POSCAR')
dis1 = []
dis2 = []
for site in s.sites:
    if str(site.specie) is 'Ti':
        for i in s.get_neighbors(site, 2.2):
            if i[1] > 2:
                dis1.append(i[1])
            else:
                dis2.append(i[1])
print(sum(dis1)/ len(dis1))
print(sum(dis2)/ len(dis2))
