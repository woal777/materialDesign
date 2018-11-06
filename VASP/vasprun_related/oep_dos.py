from pymatgen.io.vasp import Structure, Vasprun, Dos, Spin, OrbitalType
from pymatgen.core import PeriodicSite
import numpy as np
from typing import Tuple
from pymatgen.electronic_structure.plotter import DosPlotter


def find_ind(structure: Structure, start, end):
    arr = []
    sites: Tuple[PeriodicSite] = structure.sites
    for j in sites:
        if end > j.c > start:
            arr.append(j)

    return arr


def sum_spin(dos: Dos):
    dos.densities[Spin.up] -= dos.densities.pop(Spin.down)


def integrate(dos):
    den = {}
    de = dos.energies[1] - dos.energies[0]
    for k, d in dos.densities.items():
        densities = []
        for i in range(len(d)):
            if dos.energies[i] - dos.efermi > 0:
                densities.append(0)
            else:
                densities.append(sum(d[0:i]) * de)
        den[k] = np.array(densities)
    dos.__setattr__('densities', den)
    return dos


def write_dos(name, dos: Dos):
    with open(name, 'w') as f:
        for i, j in zip(dos.energies - dos.efermi, dos.get_densities(Spin.up)):
            f.write(f'{i:.6}\t{j:6.6}\n')

        if vrun.is_spin:
            f.write('#Spin down\n')
            for i, j in zip(reversed(dos.energies - dos.efermi), reversed(dos.get_densities(Spin.down))):
                f.write(f'{i:6}\t{-j:6.6}\n')


def sum_orbital(dos: Dos, dos2: Dos):
    dos.densities[Spin.up] += dos2.densities[Spin.up]
    if dos.densities.keys().__contains__(Spin.down):
        dos.densities[Spin.down] += dos2.densities[Spin.down]


if __name__ == "__main__":
    vrun = Vasprun('vasprun.xml')
    cdos = vrun.complete_dos
    dp = DosPlotter()
    en = {'first': (0.25, 0.31),
          }
    for key, val in en.items():
        dosN = Dos(cdos.efermi, cdos.energies, {k: np.zeros(d.shape) for k, d in cdos.densities.items()})
        dosMetal = Dos(cdos.efermi, cdos.energies, {k: np.zeros(d.shape) for k, d in cdos.densities.items()})
        for s in find_ind(cdos.structure, *val):
            if s.specie.__str__() == 'N':
                sum_orbital(dosN, cdos.get_site_spd_dos(s)[OrbitalType.p])
            elif s.specie.__str__() == 'Cu':
                sum_orbital(dosMetal, cdos.get_site_spd_dos(s)[OrbitalType.d])

        dosN.densities = dosN.get_densities()
        dosMetal.densities = dosMetal.get_densities()

        sum_spin(dosN)
        sum_spin(dosMetal)

        dosN = integrate(dosN)
        dosMetal = integrate(dosMetal)

        dp.add_dos_dict({key+"dosN": dosN, key + "dosM": dosMetal})
    dp.show()
    # write_dos(key + '_N_mag.dat', integrate(dosN))
    # write_dos(key + '_Cu_mag.dat', integrate(dosMetal))
