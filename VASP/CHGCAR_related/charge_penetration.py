from pymatgen.io.vasp import Chgcar
import os
import matplotlib.pyplot as plt
import macrodensity
import numpy as np

os.chdir('/home/jinho93/oxides/perobskite/strontium-titanate/slab/nbsto/0.superlattice/4.long/20uc/symm/3.pure/1.percent/norel/vac/parchg')
chg = Chgcar.from_file('PARCHG')
structure = chg.poscar.structure
data: np.ndarray = chg.data['total']
z = chg.get_average_along_axis(2)
xaxis = np.linspace(0, chg.poscar.structure.lattice.c, len(z))
dz = xaxis[1] - xaxis[0]
z /= (chg.dim[2]) * dz
macro = macrodensity.macroscopic_average(z, 44.8, 1)
np.savetxt('z.dat', np.array([xaxis, z]).transpose())
np.savetxt('macro.dat', np.array([xaxis, macro]).transpose())


# macro = macrodensity.macroscopic_average(z, 4.1, chg.structure.lattice.c / chg.dim[2])
# np.savetxt('macro.dat', np.array([xaxis, macro]).transpose())
