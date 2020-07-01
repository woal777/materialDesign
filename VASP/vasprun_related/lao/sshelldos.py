from pymatgen import PeriodicSite, Spin, Site
from pymatgen.io.vasp import Vasprun
import os
import numpy as np


class ShellDos:
    def __init__(self):
        self.vasprun = Vasprun('vasprun.xml')
        self.s = self.vasprun.final_structure
        self.complete_dos = self.vasprun.complete_dos
        self.atom: PeriodicSite = self.s.sites[283]
        self.shells = 5

    def total_dos(self):
        dos_arr = np.zeros((self.shells + 1, len(self.complete_dos.energies)))
        dos_arr[0] = (self.vasprun.tdos.energies - self.vasprun.tdos.efermi)

        for j in range(self.shells):
            for i, _ in self.s.get_neighbors_in_shell(self.atom.coords, 2 * j + 3, 1):
                try:
                    dos_arr[j + 1] += self.complete_dos.get_site_dos(i).densities[Spin.up]
                    if self.vasprun.is_spin:
                        dos_arr[j + 1] += self.complete_dos.get_site_dos(i).densities[Spin.down]
                except KeyError:
                    pass
        np.savetxt('output.dat', dos_arr.transpose(), '%16.8E')

    def atomic_dos(self):
        dos_arr = dict()
        for i in self.s.types_of_specie:
            dos_arr[i] = np.zeros((self.shells + 1, len(self.complete_dos.energies)))
            dos_arr[i][0] = (self.vasprun.tdos.energies - self.vasprun.tdos.efermi)

        for j in range(self.shells):
            i: Site
            for i, _ in self.s.get_neighbors_in_shell(self.atom.coords, 2 * j + 3, 1):
                try:
                    dos_arr[i.specie][j + 1] += self.complete_dos.get_site_dos(i).densities[Spin.up]
                    if self.vasprun.is_spin:
                        dos_arr[i.specie][j + 1] += self.complete_dos.get_site_dos(i).densities[Spin.down]
                except KeyError:
                    pass
        for i in self.s.types_of_specie:
            np.savetxt(f'{i.name}.dat', dos_arr[i].transpose(), '%16.8E')


if __name__ == '__main__':
    os.chdir('/home/jinho93/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/from-2012/1.0ps')
    s = ShellDos()
    s.total_dos()