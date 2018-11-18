from pymatgen import Structure


s = Structure.from_file('/home/jinho93/slab/LAO/opt/SPOSCAR')
arr = []
a = 0.33
b = 1 - a
for ind, j in enumerate(s.sites):
    if j.c >= 0.6 and (j.b > b or j.b < a or j.a < a or j.a > b):
        print(ind)
        arr.append(ind)
s.remove_sites(arr)
s.to('POSCAR', '/home/jinho93/slab/LAO/opt/SPOSCAR-reduced')
