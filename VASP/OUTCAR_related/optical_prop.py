import os
import xml.etree.ElementTree as ET
import numpy as np

os.chdir('/home/jinho93/oxides/perobskite/strontium-niobate/loptics/dense-k/loptics')

conductivity = []
with open('vasprun.xml') as stream:
    for event, elem in ET.iterparse(stream):
        tag = elem.tag
        if tag == "conductivity":
            for arr in elem.find('array').find('set').findall('r'):
                conductivity.append(arr.text.split())

conductivity = np.array(conductivity, dtype=float)
np.savetxt('cond.dat', conductivity, delimiter='\t', fmt='%.14e')
