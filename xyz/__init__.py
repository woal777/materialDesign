import sys
from copy import deepcopy

import matplotlib.pyplot as plt
from MDAnalysis import Universe
from pymatgen import Structure, Lattice, IMolecule, Site
import os
import numpy as np
from pymatgen_diffusion.aimd.van_hove import RadialDistributionFunction
from MDAnalysis.analysis.rms import rmsd


class xyz_to_structure(Structure):

    def __str__(self):
        outs = []
        to_s = lambda x: "%0.6f" % x
        outs.append("{i}".format(i=len(self)))
        data = []
        props = self.site_properties
        keys = sorted(props.keys())
        for i, site in enumerate(self):
            row = [site.species_string]
            row.extend([to_s(j) for j in site.coords])
            for k in keys:
                row.append(props[k][i])
            data.append(row)
        from tabulate import tabulate
        outs.append(tabulate(data,
                             ))
        return "\n".join(outs)

    def to_xyz(self):
        u = Universe('reduced.xyz')
        name = []
        for a in u.atoms:
            name.append(a.name)
        a = [float(r) for r in '8.0136733451350004    2.7785351250530002    0.0000007466930000'.split()]
        b = [float(r) for r in '-1.6027324335730000    8.3356053751600001    0.0000022400790000'.split()]
        c = [float(r) for r in '0.0000000000000000    0.0000000000000000   25.3395087497430005'.split()]
        lat = Lattice([a, b, c])

        s = Structure(lat, name, u.trajectory[0], coords_are_cartesian=True)
        s.make_supercell([2, 2, 1])
        print(s)


def reduce_frame():
    with open(sys.argv[1]) as f:
        lines = f.readlines()
        n = int(lines[0]) + 2
        snapshot = []
        for a in range(len(lines) // n):
            snapshot.append(lines[a * n:(a + 1) * n])
        snapshot = np.array(snapshot)
        print(snapshot.shape)
        reduced = snapshot[::6]
        print(reduced.shape)
        with open('reduced.xyz', 'w') as g:
            for i in reduced:
                g.writelines(i)


def xyz_rdf(name):
    os.chdir('/home/jinho93/oxides/cluster/zno/cp2k/1.aimd/3.16A/30/3.fix/2.again')
    mole = IMolecule.from_file('tail.xyz')
    #    mole = IMolecule.from_str(out, fmt='xyz')
    s = mole.get_boxed_structure(1.6027345000000000E+01,
                                 1.6671211000000000E+01,
                                 6.0678892000000005E+01)
    structures = [s]
    ind = []
    ref = []
    print(name)
    for i, sp in enumerate(s.sites):
        print(sp.z)
        up = .7
        down = .66
        if sp.species_string == name and up > sp.c > down:
            ind.append(i)
        elif sp.species_string == 'O' and up + 0.05 > sp.c > down - 0.05:
            ref.append(i)
    r = RadialDistributionFunction(structures, ind, reference_indices=ref, ngrid=301, sigma=.1)
    print(r.peak_r[0])
    r.get_rdf_plot(plt=plt, ylim=[-0.005, max(r.rdf)], label=f'{name}-ref')
    r.export_rdf('rdf.dat')
    plt.show()


def distribution():
    os.chdir('/home/jinho93/oxides/cluster/zno/cp2k/1.aimd/3.16A/30/3.fix/2.again')
    s = IMolecule.from_file('tail.xyz')
    oxy = []
    zinc = []
    for i, site in enumerate(s.sites):
        if site.species_string == 'O':
            oxy.append(i)
        else:
            zinc.append(i)
    z = s.cart_coords[np.array(oxy), 2]
    z2 = s.cart_coords[np.array(zinc), 2]
    his = np.histogram(z, bins=15, range=(1, 2.65473 * 15))
    his2 = np.histogram(z2, bins=15, range=(1, 2.65473 * 15))
    print(his[0])
    print(his2[0])
    plt.scatter(range(len(his[0])),his[0] / (his[0] + his2[0]))
    plt.scatter(range(len(his[0])),his2[0] / (his[0] + his2[0]))
    plt.show()


def movement():
    os.chdir('/home/jinho93/oxides/cluster/zno/cp2k/1.aimd/3.16A/30/again/vesta')
    u = Universe('merged.xyz')
    pos = []
    init = True
    for t in u.trajectory:
        if init:
            pos = deepcopy(t[:][:, 2])
            init = False
        else:
            for i in range(401, 561):
                if (pos[i] - t[i][2]) > 1:
                    print(pos[i], t[i][2])


def polarization():
    os.chdir('/home/jinho93/oxides/cluster/zno/cp2k/1.aimd/3.16A/30')
    mole = IMolecule.from_file('POSCAR.xyz')
    arr = [[] for _ in range(int(max(mole.cart_coords[:, 2]) // 2.58486 + 1))]
    print(arr)
    for s in mole.sites:
        arr[int(s.z // 2.58486)].append(s)
    for i in arr:
        p = 0
        j: Site
        for j in i:
            if j.species_string == 'O':
                p += -2 * j.z
            else:
                p += 2 * j.z
        vol = 49.719 / 2
        ncell = len(i) // 2
        print(i)
        print(p / ncell / vol * 1.6022e-19 * 1e+20)


def wurzite_pol():
    os.chdir('/home/jinho93/oxides/cluster/zno/cp2k/1.aimd/3.16A/30/3.fix/2.again')
#    out = open('tail.xyz').readlines()
    #out = ''.join(out[:563])
#    print(out)
    mole = IMolecule.from_file('tail.xyz')
#    mole = IMolecule.from_str(out, fmt='xyz')
    s = mole.get_boxed_structure(1.6027345000000000E+01,
                                 1.6671211000000000E+01,
                                 6.0678892000000005E+01)
    s.to('POSCAR', 'POSCAR.vasp')
    layered_pol = []
    for site in s.sites:
        if .56 > site.c > .6 and site.species_string == 'O':
            dis_z = 0
            n = 0
            for neighbor in s.get_neighbors(site, 2.7):
                if neighbor[0].species_string is 'Zn':
                    dis_z += neighbor[0].z
                    n += 1
#                print(neighbor[0].c, end='_')
#            print(site.c)
            if (dis_z / n - site.z) < -0.5:
                print('%6.3f' % (dis_z / n - site.z))
                continue
            if n is not 4:
                continue
                print(n)
                print(site.frac_coords)
                print(s.get_neighbors(site, 2.7))
                raise ValueError('not 4')
            layered_pol.append((dis_z / n - site.z))
    print(layered_pol)
    plt.scatter(range(len(layered_pol)), layered_pol)
    print(sum(layered_pol) / len(layered_pol))
    plt.show()


def to_pos(name: str):
    s = IMolecule.from_file(name)
    arr = '''     6.0189552714770000    0.0000000000000000    0.0000000000000000
    -3.0094776357390001    5.2125681693410000    0.0000000000000000
     0.0000000000000000    0.0000000000000000   17.3716845998769998
'''.split()
    arr = np.array(arr)
    arr.reshape((3, 3))
    lat = Lattice(arr)
    s = Structure(lat, s.species, s.cart_coords, coords_are_cartesian=True)
    s.to('POSCAR',name.replace('xyz', 'vasp'))
    print('ok')


if __name__ == '__main__':
    distribution()
