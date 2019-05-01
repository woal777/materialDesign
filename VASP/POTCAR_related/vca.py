import numpy as np
import re


path1 = '/opt/vasp/Potential/potpaw_PBE.54/Ti_sv/'
path2 = '/opt/vasp/Potential/potpaw_PBE.54/Nb_sv/'
percentage = 0.05


def read_zval(path):
    with open(path + 'POTCAR') as f:
        for l in f:
            if re.search('ZVAL', l):
                return float(l.split()[-4])


def read_loc(path):
    loc = []
    with open(path + 'POTCAR') as f:
        lp = re.compile('local part')
        gc = re.compile('gradient corrections')
        while True:
            line = f.readline()
            if line is '':
                break
            if lp.search(line):
                _ = f.readline()
                while True:
                    line = f.readline()
                    if gc.search(line):
                        break
                    else:
                        loc.append(list(map(float, line.split())))
    return np.array(loc)


def read_nl(path):
    nl = dict()
    with open(path + 'POTCAR') as f:
        nlp = re.compile('Non local Part')
        while True:
            line = f.readline()
            if line is '':
                break
            if nlp.search(line):
                line = f.readline()
                _ = [f.readline() for _ in range(2)]
                lines = []
                for _ in range(4):
                    f.readline()
                    lines.append([list(map(float, f.readline().split())) for _ in range(20)])
                    nl[' '.join(line.split()[:2])] = np.array(lines)
    return nl


def write_nl(file, key):
        for i, arr in enumerate(aver_nl[key]):
            if i % 2 is 0:
                file.write(' Reciprocal Space Part\n')
            else:
                file.write(' Real Space Part\n')
            np.savetxt(file, arr, fmt='%16.8E', delimiter='')


zval1 = read_zval(path1)
zval2 = read_zval(path2)

aver_zval = zval1 * (1 - percentage) + zval2 * percentage

loc1 = read_loc(path1)
loc2 = read_loc(path2)

aver_loc = np.sum([loc1 * (1 - percentage), loc2 * percentage], axis=0)
#print(aver_loc)

nl1 = read_nl(path1)
nl2 = read_nl(path2)

aver_nl = dict()
for key, val in nl1.items():
    aver_nl[key] = np.sum([nl1[key] * (1 - percentage), nl2[key] * percentage], axis=0)
with open('NewPseudo', 'w') as f:
    with open(path1 + 'POTCAR') as ref:
        nlp = re.compile('Non local Part')
        loc = re.compile('local part')
        while True:
            line = ref.readline()
            if line is '':
                break
            if re.search('ZVAL', line):
                f.write('   POMASS =   87.620; ZVAL   =   {:6.3f}    mass and valenz\n'.format(aver_zval))
            elif loc.search(line):
                f.write(line)
                f.write(ref.readline())
                np.savetxt(f, aver_loc,'%16.8E', delimiter='')
                [ref.readline() for _ in range(200)]
            elif nlp.search(line):
                f.write(line)
                line = ref.readline()
                f.write(line)
                [f.write(ref.readline()) for _ in range(2)]
                write_nl(f, ' '.join(line.split()[:2]))
                [ref.readline() for _ in range(84)]
            else:
                f.write(line)

