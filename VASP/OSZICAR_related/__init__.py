from pymatgen.io.vasp.outputs import Oszicar


def energies():
    arr = dict()
    for i in range(0, 21):
        o = Oszicar(f'{i:02d}/OSZICAR')
        arr[i] = o.final_energy
    for k, v in arr.items():
        if v <= min(arr.values()):
            print(k, v)


if __name__ == '__main__':
    energies()