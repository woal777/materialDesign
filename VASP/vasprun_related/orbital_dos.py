from pymatgen.io.vasp.outputs import Vasprun, Element
from pymatgen.electronic_structure.plotter import DosPlotter
from pymatgen import MPRester

vrun = Vasprun('/home/jinho93/metal/fe16n2/pbe/dos/pure/3001/'+'vasprun.xml')
dsp = DosPlotter()
dsp.add_dos_dict(vrun.complete_dos.get_element_spd_dos(Element.Fe))
dsp.show()
