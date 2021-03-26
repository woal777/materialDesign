from pymatgen.electronic_structure.dos import add_densities
from pymatgen.io.vasp.outputs import Vasprun, Dos
from pymatgen.electronic_structure.plotter import DosPlotter
import six
import os
from VASP.vasprun_related.utiles import write_dos
import numpy as np

os.chdir('/home/jinho93/oxides/cluster/tio2/rutile')
vrun = Vasprun('vasprun.xml')
cdos = vrun.complete_dos
arr = []
arr2 =[]
num = 0
num2 = 0
s = vrun.final_structure
for ind in s.sites:
    if ind.c > 0.68 or ind.c < 0.32:
        arr2.append(cdos.get_site_dos(ind).densities)
        print(ind)
        num2 += 1
#    if (str(ind.specie) is 'Ti' and len(s.get_neighbors(ind, 2.2)) < 6)\
#            or len(s.get_neighbors(ind, 2.2)) < 3:
#        arr2.append(complete_dos.get_site_dos(ind).densities)
#        num2 += 1
#    else:
#        arr.append(complete_dos.get_site_dos(ind).densities)
#        num += 1
#dos = Dos(complete_dos.efermi, complete_dos.energies, six.moves.reduce(add_densities, arr))
dos2 = Dos(cdos.efermi, cdos.energies, six.moves.reduce(add_densities, arr2))
#dos.densities = {k: np.array(d / num) for k, d in dos.densities.items()}
dos2.densities = {k: np.array(d / num2) for k, d in dos2.densities.items()}
dsp = DosPlotter()
dsp.add_dos('core', dos2)
#write_dos(dos, filename='core.dat')
write_dos(dos2, filename='101.dat')
dsp.show()