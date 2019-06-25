import re
import os

import numpy

os.chdir('/home/jinho93/oxides/cluster/zno/gulp/reax/slab')
with open('report.gulp') as f:
    read = False
    read_char = False
    coord = []
    charge = []
    close = 0
    final = True
    for l in f:
        if re.search('Final', l):
            final = False
        if final:
            continue

        if close is 2:
            close = 0
            read = False
            read_char = False
        if re.search('Label', l):
            read = True
        elif read:
            if re.search('----', l):
                close += 1
                continue
            coord.append([float(r) for r in l.split()[3:6]])

        if re.search('Atom no.', l):
            read_char = True
        elif read_char:
            if re.search('----', l):
                close += 1
                continue
            charge.append(float(l.split()[-1]))
    coord = numpy.array(coord)
    charge = numpy.array(charge)
    output = []
    print(charge)
    for i, j in zip(coord, charge):
        output.append(i * j)
    print(numpy.sum(output, axis=0))
