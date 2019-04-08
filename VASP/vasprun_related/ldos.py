from pymatgen.io.vasp.outputs import Vasprun, Spin
import os
import numpy as np
os.chdir('/home/ksrc5/FTJ/bto/bto-sto/centro')

if __name__ == '__main__':
    vrun = Vasprun('vasprun.xml')
    s = vrun.final_structure
    c_arr = np.linspace(0, 1, 16)
    dos_arr = np.zeros((len(c_arr + 1), len(vrun.tdos.densities[Spin.up])))
    for i in s.sites:
        for j in range(len(c_arr)):
            if c_arr[j] < i.c <= c_arr[j +1]:
                dos_arr[j + 1] += vrun.complete_dos.get_site_dos(i).densities[Spin.up]
    dos_arr[0] = (vrun.tdos.energies - vrun.tdos.efermi)
    np.savetxt('output.dat', dos_arr.transpose())
