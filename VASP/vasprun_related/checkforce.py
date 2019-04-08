from xml.etree import ElementTree
import os
import numpy as np
os.chdir('/home/ksrc5/FTJ/bfo/sto-bfo')
elem: ElementTree.Element
selective = []
forces = []
try:
    for event, elem in ElementTree.iterparse('vasprun.xml', events=('end', )):
        if elem.tag == 'atoms':
            num = int(elem.text)
        try:
            if elem.attrib['name'] == 'selective':
                for i in elem:
                    selective.append([True if r is 'T' else False
                                      for r in str(i.text).split()])
            elif elem.attrib['name'] == 'forces':
                arr = []
                for i in elem:
                    arr.append([float(r) for r in str(i.text).split()])
                arr = np.array(arr)
                arr[selective] =
                forces.append(arr)
        except KeyError:
            pass
except ElementTree.ParseError:
    pass

print(selective)

print(forces)