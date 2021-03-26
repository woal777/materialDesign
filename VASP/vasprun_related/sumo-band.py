#%%
import os
from pymatgen.io.vasp import Vasprun
from pymatgen.electronic_structure.plotter import BSDOSPlotter
from pymatgen.io.vasp.outputs import Procar

os.chdir('/home/jinho93/oxides/perobskite/strontium-vanadate')
os.chdir('/home/jinho93/oxides/perobskite/strontium-Molybdate')

plt = BSDOSPlotter()
bands = Vasprun("./band/vasprun.xml").get_band_structure("./band/KPOINTS", line_mode = True)


data = Procar("./band/PROCAR").data
# density of states
dosrun = Vasprun("./loptics/dos/prj/vasprun.xml")


plt.get_plot(bands, dosrun.complete_dos).show()


# %%
