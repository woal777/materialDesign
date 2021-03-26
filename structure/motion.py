import matplotlib.pyplot as plt
import os

mole = False
os.chdir('/home/jinho93/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/from-100/')
# os.chdir('/home/jinho93/oxides/wurtzite/zno/cp2k/1.aimd/3.16A/30/3.fix')
if mole:
    from pymatgen import Molecule
    s = Molecule.from_file('tail.xyz')
    s2 = Molecule.from_file('113th.xyz')
else:
    from pymatgen import Structure

    s = Structure.from_file('POSCAR')
    s2 = Structure.from_file('ini/POSCAR')


x = []
y = []
fx = []
fy = []
for site, site2 in zip(s.sites, s2.sites):
    if site.species_string == 'O':
        x.append(site.y)
        y.append(site.z)
        fx.append(site.y - site2.y)
        fy.append(site.z - site2.z)
    if site.c < 0.305:
        print(site.z, site2.z)
# fig = plt.figure(figsize=(5.46, 8.56))
plt.quiver(x, y, fx, fy)

plt.savefig('/home/jinho93/arrow.png')
plt.show()