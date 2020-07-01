import os
import math
from pymatgen import Structure
from pymatgen.io.vasp import Potcar
from pymatgen.io.vasp.outputs import Xdatcar
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
import numpy as np
import pandas


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
            if len(s.get_neighbors(site, 1)) == 5:
                print(site.frac_coords, site.species_string)


def spg():
    s = Structure.from_file('POSCAR')
    spg = SpacegroupAnalyzer(s)
    print(spg.get_space_group_number())


def rumpling(filename):
    output = []
    s = Structure.from_file(filename)
    for site in s.sites:
        if site.species_string == 'Zn':
            tmp_z = 0
            n = 0
            for near in s.get_neighbors(site, 2.3):
                #                if abs(site.z - near.z) < 1:
                tmp_z += near.z
                n += 1
            if n == 4:
                # print(site.z, site.z - tmp_z / n)
                output.append([site.z, site.z - tmp_z / n])
    output = np.array(output)
    #    output = np.sort(output, axis=1)
    df = pandas.DataFrame(output)
    df.to_excel('output.xlsx', index=False)


def rumpling2(filename):
    output = [[] for _ in range(8)]
    s = Structure.from_file(filename)
    for site in s.sites:
        if site.species_string == 'Zn':
            tmp_z = 0
            n = 0
            for near in s.get_neighbors(site, 2.3):
                #                if abs(site.z - near.z) < 1:
                tmp_z += near.z
                n += 1
            if n == 4:
                # print(site.z, site.z - tmp_z / n)
                try:
                    output[2 * math.floor(site.b * 4)].append(site.z)
                    output[2 * math.floor(site.b * 4) + 1].append(site.z - tmp_z / n)
                except IndexError:
                    print(2 * int(round(site.a) + 4 * round(site.b)))
    output = np.array(output).transpose()
    #    output = np.sort(output, axis=1)
    #    df = pandas.DataFrame(output)
    #    df.to_excel('output.xlsx', index=False)
    np.savetxt('output.dat', output)


def rumpling3(filename):
    output = [[] for _ in range(8)]
    s = Structure.from_file(filename)
    for site in s.sites:
        if site.species_string == 'Zn':
            tmp_z = 0
            n = 0
            for near in s.get_neighbors(site, 2.3):
                #                if abs(site.z - near.z) < 1:
                tmp_z += near.z
                n += 1
            if n == 4:
                # print(site.z, site.z - tmp_z / n)
                try:
                    output[2 * math.floor(2 * site.a) + 4 * math.floor(2 * site.b)].append(site.z)
                    output[2 * math.floor(2 * site.a) + 4 * math.floor(2 * site.b) + 1].append(site.z - tmp_z / n)
                except IndexError:
                    print(2 * int(round(site.a) + 4 * round(site.b)))
    output = np.array(output).transpose()
    print(output)
    #    output = np.sort(output, axis=1)
    #    df = pandas.DataFrame(output)
    #    df.to_excel('output.xlsx', index=False)
    np.savetxt('output.dat', output)


def averaging():
    import pandas as pd
    output = pd.read_excel('output.xlsx')
    values = output.values
    s = values[values[:, 1].argsort()]


def layer_distance(filename):
    output = []
    s = Structure.from_file(filename)
    lz = [r.z for r in s.sites]
    n = 0
    tmp_z = 0
    for i in range(len(lz)):
        tmp_z += lz[i]
        n += 1
        if i == len(lz) - 1:
            output.append(tmp_z / n)
            break
        if abs(lz[i + 1] - lz[i]) > 0.1:
            output.append(tmp_z / n)
            tmp_z = 0
            n = 0
    for i in output:
        print(i)


def cation_spacing():
    s = Structure.from_file('CONTCAR')
    z = [r.z for r in s.sites if r.species_string == 'Sr']
    for i in sorted(z):
        print(i)


def layer_spacing_perobskite():
    from statistics import mean
    s = Structure.from_file('CONTCAR')
    sr = [r for r in s.sites if r.species_string == 'Sr']
    z = [mean([r.z, mean([i.z for i in s.get_neighbors(r, 3) if (i.species_string == 'O' and abs(i.z - r.z) < 0.5)])])
         for r in sr]
    z = sorted(z)
    for i in z:
        print(i)


def lao():
    s = Structure.from_file('POSCAR')
    for i in s.sites:
        print(s.cart_coords)


def inversion():
    s = Structure.from_file('POSCAR')
    s.translate_sites(range(len(s.sites)), (0, 0, 0.025))
    metal = [[r, ind] for ind, r in enumerate(s.sites) if r.species_string != 'O']
    for i, j in metal:
        if i.a > .1:
            continue
        oxy = [[r, ind] for ind, r in enumerate(s.sites) if (r.species_string == 'O' and abs(i.z - r.z) < 1 and abs(i.x - r.x) < 2)]
        inds = [r[1] for r in oxy]
        print(i, oxy)
        tvec = np.array((0, 0, i.c - oxy[0][0].c))
        s.translate_sites(inds, tvec)
        s.translate_sites([j], -tvec)
    s.to('POSCAR', 'TPOSCAR')

if __name__ == '__main__':
    os.chdir('/home/jinho93/oxides/perobskite/lead-titanate/paw/domain/afm')
#    os.chdir('/home/jinho93/oxides/perobskite/strontium-titanate/slab/nbsto/0.superlattice/4.long/20uc/symm/4.two/1.dos')
    inversion()
