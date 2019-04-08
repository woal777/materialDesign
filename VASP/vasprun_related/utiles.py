from pymatgen.electronic_structure.dos import Dos, Spin
import numpy as np


def write_dos(dos: Dos, filename='output.dat'):
    arr = np.zeros((len(dos.energies), 2))
    arr[:, 0] = dos.energies - dos.efermi
    arr[:, 1] = dos.densities[Spin.up]
    np.savetxt(filename, arr)
