import os
from pymatgen.io.vasp.outputs import BSVasprun,Vasprun
from pymatgen.electronic_structure.plotter import BSDOSPlotter

os.chdir('/home/jinho93/oxides/amorphous/igzo/band')
vrun = BSVasprun('vasprun.xml')
vrun2 = Vasprun('vasprun.xml')
bsp = BSDOSPlotter()
plt = bsp.get_plot(vrun.get_band_structure('KPOINTS', line_mode=True),dos=vrun2.complete_dos)
plt.show()