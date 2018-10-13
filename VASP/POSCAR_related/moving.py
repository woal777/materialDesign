from pymatgen.io.vasp.outputs import Structure

s = Structure.from_file('POSCAR')
indices = []
for j, i in enumerate(s.sites):
    if 0.8 < i.c:
        indices.append(j)

s.translate_sites(indices, [0, 0, -0.1], frac_coords=False)
s.to('POSCAR', 'POSCAR')