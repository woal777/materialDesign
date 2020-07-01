from pymatgen import Structure
import os

def fixed_by_defect():
    s = Structure.from_file('POSCAR')
    fixed = []
    al = None
    for j, i in enumerate(s.sites):
        if i.species_string == "Al":
            al = j
    for j, i in enumerate(s.sites):
        if s.get_distance(al, j) < 5:
            i.properties = {'selective_dynamics': [True] * 3}
        else:
            i.properties = {'selective_dynamics': [False] * 3}
    s.sort()
    s.to('POSCAR', 'POSCAR.OUT')
    # znw.write(zn)

if __name__ == '__main__':
    os.chdir('/home/jinho93/oxides/perobskite/strontium-titanate/2.supc/vasp/1.defect/3.TiSrAnti/2.large')
    fixed_by_defect()
