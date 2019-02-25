import os
from pymatgen.electronic_structure.plotter import DosPlotter
from pymatgen.io.vasp.outputs import Vasprun
os.chdir('/home/jinho93/oxides/amorphous/igzo/hydrogen-oxygen/dos/ismear0/lorbit')
vrun = Vasprun('vasprun.xml')
# mpr = MPRester('DhmFQPuibZo8JtXn')
dos = vrun.complete_dos
# dos: CompleteDos = mpr.get_dos_by_material_id('mp-352')
eldos = dos.get_element_dos()

dsp = DosPlotter()
dsp.add_dos_dict(eldos)
dsp.show(xlim=(-2, 3), ylim=(0,8))