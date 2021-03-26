from pymatgen.io.vasp import Vasprun
from pymatgen import Element, Spin
import os
from pymatgen.electronic_structure.plotter import DosPlotter
import numpy as np

os.chdir('/home/jinho93/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/from-2012/1.0ps/full')
os.chdir('/home/jinho93/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/from-100/300k')
os.chdir('/home/jinho93/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/from-100/ini')
vrun = Vasprun('vasprun.xml')
cdos = vrun.complete_dos

dsp = DosPlotter()

dsp.add_dos_dict(cdos.get_element_dos())

dsp.show()

eldos = cdos.get_element_dos()
for i, j in eldos.items():
    if i == Element.La:
        tmp = [cdos.energies - cdos.efermi, j.densities[Spin.up]]
        tmp = np.transpose(np.array(tmp))
        np.savetxt('La.dat', tmp)
    elif i == Element.O:
        tmp = [cdos.energies - cdos.efermi, j.densities[Spin.up]]
        tmp = np.transpose(np.array(tmp))
        np.savetxt('O.dat', tmp)
