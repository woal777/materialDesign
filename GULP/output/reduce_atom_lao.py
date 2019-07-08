import os
import re
from MDAnalysis import Universe, AtomGroup
import sys


def struc(k, u):
    n = 1
    m = 1
    atom = {'Al': 1, 'La': 1, 'O': 1, 'Nd': 1}
    for i, j in zip(u.atoms, k):
        m += 1
        if m == 1858 or m == 1893 or m == 1896:
            i.name = 'Nd'
        if j[2] > 25:
            continue
        print(f'{n:2d} {i.name}     {i.name}{atom[i.name]}  1.0000  {j[0]:2.9f}  {j[1]:2.9f}  {j[2]:2.9f}    1        -')
        print('                            0.000000   0.000000   0.000000  0.00')
        n += 1
        atom[i.name] += 1
    print(f'{n:2d} O     O{atom["O"]}  1.0000  0.000000  0.000000  25.000000    1        -')
    print('                            0.000000   0.000000   0.000000  0.00')


def theri(k, u):
    n = 1
    atom = {'Al': 1, 'La': 1, 'O': 1, 'Nd': 1}
    for i, j in zip(u.atoms, k):
        if j[2] > 25:
            continue
        print(f'{n}      {i.name}{atom[i.name]}  1.000000')
        n += 1
        atom[i.name] += 1
    print(f'{n}      O{atom["O"]}  1.000000')


def main():
    xyz = open('lao.xyz')
    u = Universe(xyz)
    for l, k in enumerate(u.trajectory):
        print(l)
        t = open(f'{l:03d}.vesta', 'w')
        sys.stdout = t
        with open('final_reduction_moving_test.vesta') as f:
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
    os.chdir('/home/jinho93/oxides/perobskite/lanthanum-aluminate/slab/nvt.para.6/island/len-19/step2/vesta')
    main()
