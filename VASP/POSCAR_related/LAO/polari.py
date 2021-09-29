from io import StringIO
from re import S
#%%
from pymatgen.core.sites import Site
from pymatgen.core.structure import Molecule
from pymatgen.io.vasp import Xdatcar
from pymatgen import Structure
import os

os.chdir('/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/my015/from-gulp/421/wan/same-nbands/post')
os.chdir('/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/my015/from-gulp/421/opti')
# os.chdir('/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/my015/4/lvhar')
# structure = Structure.from_file('CONTCAR')
structure = Molecule.from_file('re.xyz')
def polarization_wannier(s):
    site: Site
    p = 0
    for site in s.sites:
        if site.species_string == 'O':
            p += site.z * 2
        elif site.species_string == 'La':
            p += site.z * 7
        elif site.species_string == 'Al':
            p += site.z * 3
        else:
            p += site.z * -1
    return p

def polarization(s):
    site: Site
    p = 0
    for site in s.sites:
        if site.species_string == 'O':
            p += site.z * -2
        elif site.species_string == 'La':
            p += site.z * 3
        elif site.species_string == 'Al':
            p += site.z * 3
    return p

# P = polarization_wannier(structure)

# print(P)

P = polarization(structure)

print(P)