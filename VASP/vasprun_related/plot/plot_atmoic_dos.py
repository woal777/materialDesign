import os
from pymatgen.electronic_structure.plotter import DosPlotter
from pymatgen.io.vasp.outputs import Vasprun, Element
os.chdir('/home/ksrc5/FTJ/1.bfo/001/2.vac/2.novca/dense')
vrun = Vasprun('vasprun.xml')
# mpr = MPRester('DhmFQPuibZo8JtXn')
dos = vrun.complete_dos
# dos: CompleteDos = mpr.get_dos_by_material_id('mp-352')
eldos = dos.get_element_dos()
#eldos.pop(Element.Mo)
#eldos.pop(Element.S)
dsp = DosPlotter()
dsp.add_dos_dict(eldos)
dsp.show(xlim=(-3, 5))