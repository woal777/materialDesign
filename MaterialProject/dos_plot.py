from pymatgen import MPRester
from pymatgen.electronic_structure.plotter import DosPlotter
mpr = MPRester('DhmFQPuibZo8JtXn')
dsp = DosPlotter()
cdos = mpr.get_dos_by_material_id('mp-352')
dsp.add_dos_dict(cdos.get_element_dos())
dsp.show()
