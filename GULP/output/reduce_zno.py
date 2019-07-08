import os
import re
from MDAnalysis import Universe, AtomGroup
import sys


def struc(k, u):
    n = 1
    m = 1
    atom = {'Zn': 1, 'O': 1}
    for i, j in zip(u.atoms, k):
        m += 1
        if 70 > j[2] > -20 and 35 > j[1] > -35 and 35 > j[0] > -35:
            print(f'{n:2d} {i.name}     {i.name}{atom[i.name]}  1.0000  {j[0]:2.9f}  {j[1]:2.9f}  {j[2]:2.9f}    1        -')
            print('                            0.000000   0.000000   0.000000  0.00')
            n += 1
            atom[i.name] += 1
    print(f'{n:2d} O     O{atom["O"]}  1.0000  35.000000 -35.000000  -20.000000    1        -')
    print('                            0.000000   0.000000   0.000000  0.00')
    n += 1
    atom[i.name] += 1
    print(f'{n:2d} O     O{atom["O"]}  1.0000  35.000000  35.000000  -20.000000    1        -')
    print('                            0.000000   0.000000   0.000000  0.00')
    n += 1
    atom[i.name] += 1
    print(f'{n:2d} O     O{atom["O"]}  1.0000 -35.000000  35.000000  -20.000000    1        -')
    print('                            0.000000   0.000000   0.000000  0.00')
    n += 1
    atom[i.name] += 1
    print(f'{n:2d} O     O{atom["O"]}  1.0000 -35.000000 -35.000000  -20.000000    1        -')
    print('                            0.000000   0.000000   0.000000  0.00')
    n += 1
    atom[i.name] += 1
    print(f'{n:2d} O     O{atom["O"]}  1.0000  35.000000 -35.000000   70.000000    1        -')
    print('                            0.000000   0.000000   0.000000  0.00')
    n += 1
    atom[i.name] += 1
    print(f'{n:2d} O     O{atom["O"]}  1.0000  35.000000  35.000000   70.000000    1        -')
    print('                            0.000000   0.000000   0.000000  0.00')
    n += 1
    atom[i.name] += 1
    print(f'{n:2d} O     O{atom["O"]}  1.0000 -35.000000  35.000000   70.000000    1        -')
    print('                            0.000000   0.000000   0.000000  0.00')
    n += 1
    atom[i.name] += 1
    print(f'{n:2d} O     O{atom["O"]}  1.0000 -35.000000 -35.000000   70.000000    1        -')
    print('                            0.000000   0.000000   0.000000  0.00')


def theri(k, u):
    n = 1
    atom = {'Zn': 1, 'O': 1}
    for i, j in zip(u.atoms, k):
        if 70 > j[2] > -20 and 35 > j[1] > -35 and 35 > j[0] > -35:
            print(f'{n}      {i.name}{atom[i.name]}  1.000000')
            n += 1
            atom[i.name] += 1
    print(f'{n}      O{atom["O"]}  1.000000')
    n += 1
    atom[i.name] += 1
    print(f'{n}      O{atom["O"]}  1.000000')
    n += 1
    atom[i.name] += 1
    print(f'{n}      O{atom["O"]}  1.000000')
    n += 1
    atom[i.name] += 1
    print(f'{n}      O{atom["O"]}  1.000000')
    n += 1
    atom[i.name] += 1
    print(f'{n}      O{atom["O"]}  1.000000')
    n += 1
    atom[i.name] += 1
    print(f'{n}      O{atom["O"]}  1.000000')
    n += 1
    atom[i.name] += 1
    print(f'{n}      O{atom["O"]}  1.000000')
    n += 1
    atom[i.name] += 1
    print(f'{n}      O{atom["O"]}  1.000000')
    n += 1
    atom[i.name] += 1


def main():
    xyz = open('cluster.xyz')
    u = Universe(xyz)
    for l, k in enumerate(u.trajectory):
        t = open(f'{l:03d}.vesta', 'w')
        sys.stdout = t
        with open('final.vesta') as f:
            p = True
            for l in f:
                if p:
                    t.write(l)
                elif re.search('  0 0 0', l) or re.search('  0 0 0 0 0 0 0', l):
                    print(l)
                    p = True
                if re.search('STRUC', l):
                    p = False
                    struc(k, u)
                if re.search('THERI', l):
                    p = False
                    theri(k, u)


if __name__ == '__main__':
    os.chdir('/home/jinho93/oxides/cluster/zno/gulp/whitmore/line/conf4/vesta')
    main()
