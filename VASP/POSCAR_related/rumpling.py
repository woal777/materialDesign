import math

from pymatgen import Structure, Element
import os

os.chdir('/home/ksrc5/FTJ/bfo/111-dir/junction/sto/vasp/vac/conf3/4.node03/dense_k_dos/again')
os.chdir('/home/ksrc5/FTJ/bfo/111-dir/born')
s = Structure.from_file('POSCAR')
area = s.lattice.a * s.lattice.b * math.sin(s.lattice.gamma) * 1e-20
born = 4.35270
bi = []
fe = []
for i in s.sites:
    if i.specie == Element.Bi:
        mean_z = 0
        mean_z_plus = 0
        num1 = 0
        num2 = 0
        for j in s.get_neighbors(i, 3):
            if j[0].c < i.c:
                mean_z += j[0].z
                num1 += 1
            else:
                mean_z_plus += j[0].z
                num2 += 1
        mean_z /= num1
        mean_z_plus /= num2
        bi.append(born * (i.z - mean_z_plus) / (mean_z_plus - mean_z) / area * 1.6e-19 * 100)
        print(mean_z_plus, mean_z, i.z)
    elif i.specie == Element.Fe:
        mean_z = 0
        mean_z_plus = 0
        num1 = 0
        num2 = 0
        for j in s.get_neighbors(i, 3):
            if j[0].c < i.c:
                mean_z += j[0].z
                num1 += 1
            else:
                mean_z_plus += j[0].z
                num2 += 1
        mean_z /= num1
        mean_z_plus /= num2
        fe.append(born * ((i.z - mean_z) - (mean_z_plus - mean_z) / 2) / (mean_z_plus - mean_z) / area * 1.6e-19)
for i in bi:
    print(-i)