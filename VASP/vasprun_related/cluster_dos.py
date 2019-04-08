from pymatgen.electronic_structure.dos import add_densities
from pymatgen.io.vasp.outputs import Vasprun, Dos
from pymatgen.electronic_structure.plotter import DosPlotter
import six
import os
from VASP.vasprun_related.utiles import write_dos
import numpy as np

os.chdir('/home/jinho93/oxides/cluster/tio2/anatase/dos')
vrun = Vasprun('vasprun.xml')
cdos = vrun.complete_dos
arr = []
arr2 =[]
num = 0
num2 = 0
for i in vrun.final_structure.sites:
    if 0.425 < i.a < 0.575 and 0.425 < i.b < 0.575 and 0.42 < i.c < 0.58:
        arr.append(cdos.get_site_dos(i).densities)
        num += 1
    else:
        arr2.append(cdos.get_site_dos(i).densities)
        num2 += 1
dos = Dos(cdos.efermi, cdos.energies, six.moves.reduce(add_densities, arr))
dos2 = Dos(cdos.efermi, cdos.energies, six.moves.reduce(add_densities, arr2))
dos.densities = {k: np.array(d / num) for k, d in dos.densities.items()}
dos2.densities = {k: np.array(d / num2) for k, d in dos2.densities.items()}
dsp = DosPlotter()
dsp.add_dos('core', dos2)
write_dos(dos, filename='core.dat')
write_dos(dos2, filename='shell.dat')
dsp.show()