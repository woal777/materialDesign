# Python code to generate Li K-edge EELS from multiple DFT calculations
# This code should be run inside one of the Li_x folders (i.e. Li4, Li5, Li6, or Li7)
import time
import sys
import numpy as np
import os
import matplotlib.pyplot as plt

try:
    from pymatgen import Element
    from pymatgen.io.vasp import Vasprun
    from pymatgen.electronic_structure.core import Spin, OrbitalType, Orbital
except ImportError:
    sys.stderr.write("Error: could not import `pymatgen' (pymatgen.org/installation.html).\n")
    sys.exit()


def smear(x_in, y_in, fwhm=0.5, n=2000):
    s = fwhm / (2.0 * np.sqrt(2.0 * np.log(2.0)))

    x0 = np.min(x_in)
    x1 = np.max(x_in)
    x = np.linspace(x0, x1, n)

    y = np.zeros(n)
    y[0] = y_in[0]
    y[-1] = y_in[-1]

    for i in range(1, len(x_in) - 1):
        dx = 0.5 * (x_in[i + 1] - x_in[i - 1])
        for j in range(1, n - 1):
            if abs(x[j] - x_in[i]) > 1e0:
                continue
            y[j] += y_in[i] * np.exp(-0.5 * ((x[j] - x_in[i]) / s) ** 2) / (s * np.sqrt(2.0 * np.pi)) * dx
    return x, y


# pdos = cdos.get_element_spd_dos(Element('O'))[OrbitalType.p]

def get_eels(n):
    pdos = cdos.get_site_spd_dos(s.sites[n])[OrbitalType.p]
    aligned_energies = pdos.energies - v.efermi
    energies, densities = [], []
    # for i in range(len(aligned_energies)):
    #     if round(aligned_energies[i] + 10 ** (-2 * 6), 2) >= -1 and len(energies) <= 2100:
    #         energies.append(round(aligned_energies[i] + 10 ** (-2 * 6), 2))
    #         densities.append(pdos.densities[Spin.up][i])
    return smear(np.asarray(aligned_energies), np.asarray(pdos.densities[Spin.up]), fwhm=.8, n=2000)


def get_eels_orb(n, orb):
    pdos = cdos.get_site_orbital_dos(s.sites[n], orb)
    aligned_energies = pdos.energies - v.efermi
    return smear(np.asarray(aligned_energies), np.asarray(pdos.densities[Spin.up]), fwhm=.8, n=2000)


def get_center(n):
    pos = np.zeros(3)
    num = 0
    for i in s.get_neighbors(s.sites[n], 2.5):
        pos += i.coords
        num += 1
    print(num)
    pos /= num
    print(pos)
    return s.sites[n].coords - pos


def myplot_orb(i, orb=False):
    if orb:
        x, y = get_eels_orb(i, orb)
    else:
        x, y = get_eels(i)
    plt.plot(x, y)
    np.savetxt(f'{i}.dat', y)
    plt.xlim(1, 40)
    plt.ylim(0, .4)
    plt.plot([6.8, 6.8], [0, 1])
    plt.plot([8.3, 8.3], [0, 1])
    plt.plot([10.3, 10.3], [0, 1])
    plt.show()
    return x, y


def spatial_dos():
    x = cdos.energies - cdos.efermi
    for j in range(6):
        y = np.zeros(len(cdos.energies))
        for i in range(5 * j + 210, 5 * (j + 1) + 210):
            x, yi = get_eels(i)
            y += yi
            np.savetxt(f'y{j}.dat', y)
        y /= 30
        plt.plot(x, y)
    plt.show()


if __name__ == '__main__':
    os.chdir('/home/jinho93/oxides/wurtzite/zno/vasp/6.155/dense/nbands/4')
    # os.chdir('/home/jinho93/oxides/wurtzite/zno/vasp/7.eels/rec/High/core_hole/in_tuto/hyd/supc/O-k/far/maximal/6')
    v = Vasprun(filename='vasprun.xml')
    s = v.final_structure
    cdos = v.complete_dos
    y = np.zeros(len(cdos.energies))
    n = 0
    for i in range(17, 17 + 16):
        name = [r.species_string for r in s.get_neighbors(s.sites[i], 2)]
        if 'O' in name:
            print(i)
            continue
        x, yi = get_eels(i)
        y += yi
        n += 1
    y /= n
    plt.plot(x, y)
    np.savetxt(f'zn.dat', y)
    plt.show()
