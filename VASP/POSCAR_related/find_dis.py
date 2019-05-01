from pymatgen import Structure

with open('POSCAR') as s:
    lines = s.readlines()
    c = list(map(float, lines[4].split()))
    c[-1] += 1
