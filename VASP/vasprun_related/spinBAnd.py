from pymatgen.io.vasp.outputs import BSVasprun
from pymatgen.electronic_structure.plotter import BSPlotter
import os

os.chdir('/home/jinho93/half-metal/1.CrO2/3.band')
vrun = BSVasprun('vasprun.xml')
bs = vrun.get_band_structure('KPOINTS', line_mode=True)
bsp = BSPlotter(bs)
bsp.show()
