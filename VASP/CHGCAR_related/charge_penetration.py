from pymatgen.io.vasp import Chgcar
import os
import matplotlib.pyplot as plt
import macrodensity
import numpy as np

os.chdir('/home/jinho93/interface/pzt-bso/loose/opti/dos/parchg-2')
chg = Chgcar.from_file('PARCHG')
structure = chg.poscar.structure
data: np.ndarray = chg.data['total']
z = chg.get_average_along_axis(2)
xaxis = np.linspace(0, chg.poscar.structure.lattice.c, len(z))
dz = xaxis[1] - xaxis[0]
z /= (chg.dim[2]) * dz
np.savetxt('z.dat', np.array([xaxis, z]).transpose())

macro = macrodensity.macroscopic_average(z, 4.1, chg.structure.lattice.c / chg.dim[2])
np.savetxt('macro.dat', np.array([xaxis, macro]).transpose())
