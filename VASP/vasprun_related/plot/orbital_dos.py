#%%

from matplotlib.pyplot import xlim
from pymatgen.io.vasp.outputs import Vasprun, Element
from pymatgen.electronic_structure.plotter import DosPlotter

path = '/home/jinho93/oxides/perobskite/lanthanum-aluminate/bulk/hse/dos/'
# path = '/home/jinho93/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/stengel/bulk/dos/'
vrun = Vasprun(path+'vasprun.xml')
dsp = DosPlotter(zero_at_efermi=True)
dsp.add_dos_dict(vrun.complete_dos.get_element_spd_dos(Element.La))
dsp.show(xlim=(-10, 8))

# %%
