#%%
from pymatgen.analysis.surface_analysis import SurfaceEnergyPlotter, SlabEntry, ComputedStructureEntry
from pymatgen import Structure
from pymatgen.io.vasp import Oszicar
slab_001_path = r'/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/new-conf/nonstochio/NOSTEP/VAC/'
slab_015_path = r'/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/new-conf/nonstochio/1STEP/VAC/'
bulk_path = r'/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/bulk/'
o2_path = r'/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/new-conf/nonstochio/O2/'
La_path = r'/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/new-conf/nonstochio/La/'
Al_path = r'/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/new-conf/nonstochio/Al/'

def entry_from_path(path):
    return ComputedStructureEntry(
    Structure.from_file(path + 'POSCAR'), 
    Oszicar(path + 'OSZICAR').final_energy)

def slab_entry_from_path(path, miller=None):
    return SlabEntry(
    Structure.from_file(path + 'POSCAR'), 
    Oszicar(path + 'OSZICAR').final_energy, miller)


bulk = entry_from_path(bulk_path)
slab = []
refs = []

refs.append(entry_from_path(o2_path))
refs.append(entry_from_path(La_path))
refs.append(entry_from_path(Al_path))

slab.append(slab_entry_from_path(slab_001_path, (0, 0, 1)))
slab.append(slab_entry_from_path(slab_015_path, (0, 1, 5)))
sep = SurfaceEnergyPlotter(slab, bulk, refs)


print(sep)



# %%

from sympy import Symbol
sep.area_frac_vs_chempot_plot(Symbol('delu_O'), [-5, 5], increments=100)
# %%
sep.stable_u_range_dict([-5, 0], {Symbol('delu_O'):0})
# %%
sep.get_stable_entry_at_u((0, 0,1), )

# %%
