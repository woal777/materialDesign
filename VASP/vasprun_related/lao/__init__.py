from pymatgen.io.vasp import Vasprun
import os
import numpy as np
from pymatgen.electronic_structure.core import Spin
from pymatgen import Structure, PeriodicSite


class getatom:
    def __init__(self):
        self.Structrue = Structure.from_file('POSCAR')
        self.atom: PeriodicSite = self.Structrue.sites[283]
        self.atom2: PeriodicSite = self.Structrue.sites[279]
        self.vec = self.atom.coords - self.atom2.coords

    def getatom(self):
        arr = []
        for i in range(0, 20, 2):
            a:PeriodicSite = self.Structrue.get_sites_in_sphere((self.atom.coords - i * self.vec), .1)[0][0]
            a.to_unit_cell(True)
            arr.append(a)
        return arr


class ToLine:
    def __init__(self):
        self.Vasprun = Vasprun('vasprun.xml')
        self.CompleteDos = self.Vasprun.complete_dos
        self.structure = self.Vasprun.final_structure
        cmax = 0
        top = None
        for i in self.structure.sites:
            if cmax < i.c:
                cmax = i.c
                top = i
        self.La = []
        for i in self.structure.sites:
            if abs(i.x - top.x) < 2 and abs(i.y - top.y) < 2 and i.species_string == 'La':
                self.La.append(i)
        self.Al = [[t for t in self.structure.get_neighbors(r, 4) if (t.species_string == 'Al' and t.c < r.c)] for r in self.La]
        self.O = [[r for r in self.structure.get_neighbors(atom, 3) if r.z < atom.z] for atom in self.La]

    def get_total(self):
        dos_arr = np.zeros((len(self.La) + 1, len(self.Vasprun.complete_dos.energies)))
        dos_arr[0] = self.Vasprun.complete_dos.energies - self.Vasprun.complete_dos.efermi

        for j, atom in enumerate(self.La):
            n = 0
            for i in self.O[j]:
                dos_arr[j + 1] += self.CompleteDos.get_site_dos(i).densities[Spin.up]
                n += 1
            dos_arr[j + 1] += self.CompleteDos.get_site_dos(atom).densities[Spin.up]

        np.savetxt('output.dat', dos_arr.transpose())

    def get_metal(self):
        dos_arr = np.zeros((len(self.La) + len(self.Al) + 1, len(self.Vasprun.complete_dos.energies)))
        dos_arr[0] = self.Vasprun.complete_dos.energies - self.Vasprun.complete_dos.efermi

        for j, atom in enumerate(self.La):
            n = 0
            for i in self.Al[j]:
                dos_arr[2*j + 2] += self.CompleteDos.get_site_dos(i).densities[Spin.up]
                n += 1
            dos_arr[2*j + 2] /= n
            dos_arr[2*j + 1] += self.CompleteDos.get_site_dos(atom).densities[Spin.up]

        np.savetxt('output.dat', dos_arr.transpose())

    def getFromgt(self):
        self.La = getatom().getatom()
        dos_arr = np.zeros((len(self.La) + 1, len(self.Vasprun.complete_dos.energies)))
        dos_arr[0] = self.Vasprun.complete_dos.energies - self.Vasprun.complete_dos.efermi

        for j, atom in enumerate(self.La):
            for i in [r for r in self.structure.get_neighbors(atom, 3) if r.z < atom.z]:
                try:
                    dos_arr[j + 1] += self.CompleteDos.get_site_dos(i).densities[Spin.up]
                except KeyError:
                    print(i, atom)
            dos_arr[j + 1] += self.CompleteDos.get_site_dos(atom).densities[Spin.up]

        np.savetxt('output.dat', dos_arr.transpose())


if __name__ == "__main__":
    os.chdir('/home/jinho93/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/from-2012/1.0ps')
    to = ToLine()
    to.getFromgt()