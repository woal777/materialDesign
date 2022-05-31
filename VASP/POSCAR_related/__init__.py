#%%
from pymatgen import Structure
from pymatgen.io.vasp import Xdatcar
import os
from pymatgen_diffusion.aimd.van_hove import RadialDistributionFunction, plt


def get_rdf(structures):
    structure:Structure = structures[0]
    
    oxy = []
    for i, j in enumerate(structure.sites):
        if j.specie == structure.types_of_specie[0]:
            oxy.append(i)
    zn = []
    for i, j in enumerate(structure.sites):
        if j.specie == structure.types_of_specie[1]:
            zn.append(i)
    rdf = RadialDistributionFunction(structures, oxy, zn,sigma=0.05, ngrid=301)
    return rdf


def fixed_by_defect():
    s = Structure.from_file('POSCAR')
    fixed = []
    al = None
    for j, i in enumerate(s.sites):
        if i.species_string == "Al":
            al = j
    for j, i in enumerate(s.sites):
        if s.get_distance(al, j) < 5:
            i.properties = {'selective_dynamics': [True] * 3}
        else:
            i.properties = {'selective_dynamics': [False] * 3}
    s.sort()
    s.to('POSCAR', 'POSCAR.OUT')
    # znw.write(zn)

if __name__ == '__main__':
    # os.chdir('/home/jinho93/new/oxides/wurtzite/zno/vasp/aimd/2000k/cooling')
    # os.chdir('/home/jinho93/new/oxides/wurtzite/zno/vasp/aimd/2000k')
    os.chdir('/home/jinho93/ml/hfo2/')
    os.chdir('/home/jinho93/ml/hfo2/schottky/cooling')
    os.chdir('/home/jinho93/new/oxides/wurtzite/zno/vasp/aimd/2000k/cooling')
    xdat = Xdatcar.from_file('XDATCAR')
# %%
    rdf = get_rdf(xdat.structures[950:1000:10])
    rdf.get_rdf_plot().show()
# %%
