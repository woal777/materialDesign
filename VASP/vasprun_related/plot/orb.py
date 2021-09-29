from pymatgen.io.vasp import Vasprun
from pymatgen.electronic_structure.plotter import DosPlotter

dsp = DosPlotter()

vrun = Vasprun('vasprun.xml')

dsp.add_dos_dict(vrun.complete_dos.get_site_spd_dos(vrun.final_structure.sites[0]))

dsp.show()