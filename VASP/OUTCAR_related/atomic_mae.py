from re import search
import sys
import os


os.chdir('/home/backup/jinho93/metal/fe16n2/pbe/anisotropy/al/2')
argv = ['', 'x', 'z']
x = []
z = []
vol = 0
with open(argv[1]+'/OUTCAR') as f:
    for l in f:
        if search('E_soc', l):
            x.append(float(l.split()[-1]))
        elif search('volume of cell', l):
            vol = float(l.split()[-1])

with open(argv[2]+'/OUTCAR') as f:
    for l in f:
        if search('E_soc', l):
            z.append(float(l.split()[-1]))
output = []

for i, j in zip(x, z):
    output.append((i-j) / vol * 1.60218e-19 * 1e+30 / 1e+6 / 2)
    print(output[-1])

print(sum(output))
