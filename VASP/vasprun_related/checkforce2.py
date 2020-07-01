#!/home/jinho93/miniconda3/bin/python
from xml.etree.ElementTree import iterparse
import sh
import numpy as np
import sys
out = str(sh.perl('/home/jinho93/bin/checkforce', '-v'))
arr = [r.split() for r in out.split('\n')[:-4]]

selective = []
for event, elem in iterparse('vasprun.xml', events=('end',)):
    if 'name' in elem.attrib.keys() and elem.attrib['name'] == 'selective':
        for i in elem:
            selective.append([True if r is 'T' else False
                              for r in str(i.text).split()])
        break

for i, j in zip(selective, arr):
    if j:
        for k in range(3):
            if not i[k]:
                j[3 + k] = 'conv'
        print(' '.join(j))
