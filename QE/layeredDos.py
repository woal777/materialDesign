import re

import numpy as np
import os

import six
from pymatgen.electronic_structure.core import Spin, OrbitalType
from pymatgen.electronic_structure.dos import Dos, CompleteDos
from pymatgen.core.structure import Site, Element, Structure
from collections import defaultdict


os.chdir('/home/ksrc5/FTJ/bfo/111-dir/sto-bfo/qe/projwfc')
orbital = ['s', 'p', 'd']
atoms = ['Sr', 'O', 'Fe', 'Bi']
pdoss = []


def fermi_fromfile(filename):
    with open(filename) as f:
        for l in f:
            if re.search('the Fermi energy', l):
                return l.split()[-2]

def add_densities(density1, density2):
    """
    Method to sum two densities.

    Args:
        density1: First density.
        density2: Second density.

    Returns:
        Dict of {spin: density}.
    """
    return {spin: np.array(density1[spin]) + np.array(density2[spin])
            for spin in density1.keys()}


def get_cdos():
    for n in range(1, 74):
        pdos = defaultdict(dict)
        atom = ''
        orb = ''
        for a in atoms:
            if os.path.exists(f'pwscf.pdos_atm#{n}({a})_wfc#{1}(s)'):
                atom = Element(a)
        if atom == '':
            continue
        for l, o in enumerate(orbital):
            if os.path.exists(f'pwscf.pdos_atm#{n}({str(atom)})_wfc#{l + 1}({o})'):
                orb = OrbitalType(l)
                data = np.genfromtxt(f'pwscf.pdos_atm#{n}({str(atom)})_wfc#{l + 1}({orb.name})')
                pdos[orb][Spin.up] = data[:, 1]
                pdos[orb][Spin.down] = data[:, 2]
                energies = data[:,0]
        pdoss.append(pdos)
    efermi = fermi_fromfile('report.scf')
    total_density= six.moves.reduce(add_densities, [six.moves.reduce(add_densities, p.values()) for p in pdoss])
    total_dos = Dos(efermi, energies, total_density)
    s = Structure.from_file('123.cif')
    return CompleteDos(s, total_dos, pdoss)


if __name__ == '__main__':
    cdos = get_cdos()
    for i in cdos.structure.sites:
        print(i)
