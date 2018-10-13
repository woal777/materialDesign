from pymatgen import Structure, Specie

for i in range(3):
    s: Structure = Structure.from_file('POSCAR')
    s.replace(i, species=Specie('Hf'))
    for j in range(i, 4):
        s.replace(j, species=Specie('Hf'))
        print(s.get_space_group_info()[0])
        s.replace(j, species=Specie('Zr'))

