#!/home/jinho93/miniconda3/envs/my_pymatgen/bin/python
from pymatgen import Element
from pymatgen.electronic_structure.core import OrbitalType
from pymatgen.io.vasp.outputs import Vasprun, Spin
import os
import numpy as np

if __name__ == '__main__':
    os.chdir('/home/jinho93/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/from-2012/3.1ps')
    os.chdir('/home/jinho93/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/from-2012/1.0ps/full')
    os.chdir('/home/jinho93/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/from-2012/3.1ps/novac')
    os.chdir('/home/jinho93/oxides/perobskite/lanthanum-aluminate/periodic_step/gulp/6.106')
    os.chdir('/home/jinho93/oxides/wurtzite/zno/vasp/6.155/dense')
    vrun = Vasprun('vasprun.xml')
    cdos = vrun.complete_dos
    s = vrun.final_structure
    c_arr = np.linspace(.25, .686, 9)
    dos_arr = np.zeros((len(c_arr + 1), len(vrun.tdos.densities[Spin.up])))
    for i in s.sites:
        for j in range(len(c_arr) - 1):
            if c_arr[j] <= i.c < c_arr[j + 1] and i.specie == Element.O:
                dos_arr[j + 1] += cdos.get_site_spd_dos(i)[OrbitalType.p].densities[Spin.up]
    dos_arr[0] = (vrun.tdos.energies - vrun.tdos.efermi)
    np.savetxt('oxygen.dat', dos_arr.transpose(), '%16.8E')

    dos_arr = np.zeros((len(c_arr + 1), len(vrun.tdos.densities[Spin.up])))
    for i in s.sites:
        for j in range(len(c_arr) - 1):
            if c_arr[j] <= i.c < c_arr[j + 1] and i.specie == Element.Zn:
                dos_arr[j + 1] += cdos.get_site_spd_dos(i)[OrbitalType.s].densities[Spin.up]
    dos_arr[0] = (vrun.tdos.energies - vrun.tdos.efermi)
    np.savetxt('lantanum.dat', dos_arr.transpose(), '%16.8E')
