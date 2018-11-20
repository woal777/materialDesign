from pymatgen import Structure


s = Structure.from_file('/home/jinho93/slab/LAO/grimes/opt/SPOSCAR')
arr = []
a = 0.30
b = 1 - a
t1 = True
if t1:
    for ind, j in enumerate(s.sites):
        if j.c >= 0.8 and (j.b > b or j.b < a or j.a < a or j.a > b):
            arr.append(ind)
else:
    for ind, j in enumerate(s.sites):
        if j.c >= 0.8 and j.b > a:
            arr.append(ind)
s.remove_sites(arr)
s.to('POSCAR', '/home/jinho93/slab/LAO/grimes/opt/SPOSCAR-reduced')