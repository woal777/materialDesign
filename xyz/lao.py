import os
import sys
from pymatgen import IStructure, Molecule, Element


def topmost():
    m = Molecule.from_file('snapshot4.xyz')
    for j, i in enumerate(m.sites):
        if i.z > 26.5 and i.species_string is 'La':
            m.remove_sites([j])
            m.insert(j, Element.Ag, i.coords)
        if i.z > 25 and i.species_string is 'Al':
            m.remove_sites([j])
            m.insert(j, Element.Mg, i.coords)
        if i.z > 25 and i.species_string is 'O':
            m.remove_sites([j])
            m.insert(j, Element.N, i.coords)
    print(m)



if __name__ == '__main__':
    sys.stdout = open('/home/jinho93/output.txt', 'w')
    os.chdir('/home/jinho93/oxides/perobskite/lanthanum-aluminate/periodic_step/gulp/3.2012/1.opti')
    topmost()
