import os
from pymatgen import Structure, Specie


def main():
    for i in range(8):
        s: Structure = Structure.from_file('POSCAR')
        s.replace(i, species=Specie('Ca'), properties={'selective_dynamics': [True] * 3})
        for j in range(7, i, -1):
            s.replace(j, species=Specie('Ca'), properties={'selective_dynamics': [True] * 3})
            os.mkdir(f'{i}{j}')
            s.to('POSCAR', f'{i}{j}/POSCAR')
            s.copy()
            s.replace(j, species=Specie('Bi'), properties={'selective_dynamics': [True] * 3})


def sort():
    s = Structure.from_file('POSCAR')
    s.sort()
    s.to('POSCAR', 'POSCAR')


if __name__ == '__main__':
    sort()
