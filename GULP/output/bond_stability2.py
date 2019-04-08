from pymatgen import Structure
import os

os.chdir('/home/jinho93/oxides/cluster/tio2/rutile/gulp/matsui')


def write_pos(f):
    poscar = ''
    n = int(f.readline())
    _ = f.readline()
    lines = []
    for i in range(n):
        lines.append(f.readline())
    lines = sorted(lines, key=lambda x: x[0])
    n1 = 0
    n2 = 0
    for _ in lines:
        if _.__contains__('Ti'):
            n1 += 1
        else:
            n2 += 1
    poscar +=('''O Ti
    1.0
            36.0000000000         0.0000000000         0.0000000000
            0.0000000000         36.0000000000         0.0000000000
            0.0000000000         0.0000000000        70.0000000000
    ''')
    poscar += ('  O  Ti\n'.format(n1, n2))
    poscar += ('  {:02d}  {:02d}\n'.format(n2, n1))
    poscar += ('Cartesian\n')
    for l in lines:
        poscar += (l[3:])
    return poscar


with open('reduced.xyz') as f:
    with open('outout.dat', 'w') as g:
        frame = 0
        while True:
            pos = write_pos(f)
            s = Structure.from_str(pos, 'POSCAR')
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
            g.write(f'{frame} {sum(dis1)/ len(dis1)} {sum(dis2)/ len(dis2)}\n')
            print(sum(dis1)/ len(dis1))
            print(sum(dis2)/ len(dis2))
            frame += 1
