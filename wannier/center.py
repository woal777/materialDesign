from pymatgen import Structure, Molecule
import os

os.chdir('/home/jinho93/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/stengel/001/4.wann')
os.chdir('/home/jinho93/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/stengel/001/4.wann/test')
p = 0
ion = 0
ele = 0
m = Molecule.from_file('wannier90_centres.xyz')
s = Structure.from_file('POSCAR')

for i in m.sites:
    # while i.x < 0:
    #     i.x += s.lattice.a
    # while i.x > s.lattice.a:
    #     i.x -= s.lattice.a
    # while i.y < 0:
    #     i.y += s.lattice.b
    # while i.y > s.lattice.b:
    #     i.y -= s.lattice.b
    while i.z < 0:
        i.z += s.lattice.c
    while i.z > s.lattice.c:
        i.z -= s.lattice.c
    if i.species_string == 'La':
        p += i.z * 11
        ion += 11
    elif i.species_string == 'Al':
        ion += 3
        p += i.z * 3
    elif i.species_string == 'O':
        ion += 6
        p += i.z * 6
    else:
        ele += 1
        p -= i.z

m.to('xyz', 're.xyz')