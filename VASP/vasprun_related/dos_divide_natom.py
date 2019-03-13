import os
from pymatgen.electronic_structure.plotter import DosPlotter
from pymatgen.io.vasp.outputs import Vasprun, Element, Dos
os.chdir('/home/jinho93/molecule/ddt/vasp/2-sub/triplet/')
vrun = Vasprun('vasprun.xml')
# mpr = MPRester('DhmFQPuibZo8JtXn')
dos = vrun.complete_dos
# dos: CompleteDos = mpr.get_dos_by_material_id('mp-352')
eldos = dos.get_element_dos()
i: Element
j: Dos
print(vrun.final_structure.composition.element_composition)
#for i, j in eldos.items():
#    vrun.final_structure.num_sites
#eldos.pop(Element.Mo)
#eldos.pop(Element.S)
dsp = DosPlotter()
dsp.add_dos_dict(eldos)
dsp.show(xlim=(-3, 5))