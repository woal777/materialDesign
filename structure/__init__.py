import os

from pymatgen import Structure
from pymatgen.io.vasp import Potcar
from pymatgen.io.vasp.outputs import Xdatcar
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer


def xdat_rdf_speices(name):
    import matplotlib.pyplot as plt
    from pymatgen_diffusion.aimd.van_hove import RadialDistributionFunction
    s = Xdatcar('XDATCAR').structures[-1:]
    ind = []
    ref = []
    for i, sp in enumerate(s[0].species):
        if sp.name == name:
            ind.append(i)
        elif sp.name == 'O':
            ref.append(i)
    r = RadialDistributionFunction(s, ind, reference_indices=ref, ngrid=501, sigma=.1)
    print(r.peak_r[0])
    r.get_rdf_plot(plt=plt, ylim=[-0.005, max(r.rdf)], label=f'{name}-ref')
    r.export_rdf('/home/jinho93/rdf.dat')
    plt.show()


def valence_state(name):
    s = Structure.from_file(name)
    for site in s.sites:
        if site.species_string != 'X0+':
            print(len(s.get_neighbors(site, 1)))
            if len(s.get_neighbors(site, 1)) is 5:
                print(site.frac_coords, site.species_string)


def spg():
    s = Structure.from_file('POSCAR')
    spg = SpacegroupAnalyzer(s)
    print(spg.get_space_group_number())


def rumpling():
    s = Structure.from_file('CONTCAR')
    for site in s.sites:
        if site.species_string is 'Hf':
            tmp_z = 0
            n = 0
            print(s.get_neighbors(site, 2.3))
            for near, dis in s.get_neighbors(site, 2.3):
#                if abs(site.z - near.z) < 1:
                tmp_z += near.z
                n += 1
            print(site.z - tmp_z / n)


if __name__ == '__main__':
    os.chdir('/home/jinho93/oxides/fluorite/hafnia/pca21/vasp/2.constrained')
    rumpling()
