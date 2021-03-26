from numpy import array as npa
import numpy as np
import sys
import os
from pymatgen.io.vasp.outputs import Procar, Vasprun
from pymatgen import Structure
from pymatgen.electronic_structure.core import Spin, Orbital

from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.gridspec import GridSpec


def rgbline(ax, k, e, red, green, blue, KPOINTS, alpha=1.):
    # creation of segments based on
    # http://nbviewer.ipython.org/urls/raw.github.com/dpsanders/matplotlib-examples/master/colorline.ipynb
    pts = np.array([KPOINTS, e]).T.reshape(-1, 1, 2)
    seg = np.concatenate([pts[:-1], pts[1:]], axis=1)
    nseg = len(KPOINTS) - 1
    r = [0.5 * (red[i] + red[i + 1]) for i in range(nseg)]
    g = [0.5 * (green[i] + green[i + 1]) for i in range(nseg)]
    b = [0.5 * (blue[i] + blue[i + 1]) for i in range(nseg)]
    a = np.sum(np.array([r, g, b]), axis=0)
    a[a < .1] = 0.02
    a -= sys.float_info.epsilon
    color = [(i, j, kk, l) for i, j, kk, l in zip(r, g, b, a)]
    lc = LineCollection(seg, colors=color, linewidth=4)
    ax.add_collection(lc)


if __name__ == "__main__":

    os.chdir('/home/jinho93/interface/pzt-bso/loose/opti/')

    # Load Structure
    structure = Structure.from_file("./band/dense/POSCAR")
    # Load Band Structure Calculations
    bands_K = Vasprun("./band/dense/vasprun.xml")

    # Load Band Structure Calculations
    bands = bands_K.get_band_structure("./band/dense/KPOINTS", line_mode=True)

    # projected bands
    data = Procar("./band/dense/PROCAR").data
    # density of states
    dosrun = Vasprun("./dos/vasprun.xml")

    # labels

    # general options for plot

    # set up 2 graph with aspec ration 2/1
    # plot 1: bands diagram
    # plot 2: Density of States
    gs = GridSpec(1, 2, width_ratios=[1, 1])
    fig = plt.figure(figsize=(11.69, 8.27))
    #    fig.suptitle("$BN_2 Monolayer$")
    ax1 = plt.subplot(gs[0])
    ax2 = plt.subplot(gs[1])  # , sharey=ax1)

    # set ylim for the plot
    # ---------------------
    emin = 1e100
    emax = -1e100

    # Set both fermi levels equal to the band fermi level
    bands.efermi = dosrun.efermi  # = 0

    for spin in bands.bands.keys():
        for b in range(bands.nb_bands):
            emin = min(emin, min(bands.bands[spin][b]))
            emax = max(emax, max(bands.bands[spin][b]))

    emin -= bands.efermi + 1
    emax -= bands.efermi - 1
    #    emin = -20
    emax = 5
    emin = -5

    # makes an empty list with the length of the number of bands and kpoints
    contrib = np.zeros((bands.nb_bands, len(bands.kpoints), 3))
    # sum up atomic contributions and normalize contributions
    # Sum over all bands
    for b in range(bands.nb_bands):
        # Sum over all K-Points
        for k in range(len(bands.kpoints)):
            s = 0
            py_px = 0
            pz = 0
            # Sum over all atoms
            for i in range(len(bands.structure.species)):
                # Sum over the orbitals
                # Select which atom type they belong to
                # 0:s 1:py 2:pz 3:px 4:dxy 5:dyz 6:dz2 7:dxz 8:dx2_y2
                if i == 52:
                    s += data[Spin.up][k][b][i][0] ** 2
                elif i == 53:
                    py_px += data[Spin.up][k][b][i][0] ** 2
                elif i == 54:
                    pz += data[Spin.up][k][b][i][0] ** 2
            tot = s + py_px + pz
            if tot != 0.0:
                contrib[b, k, 0] = s / tot
                contrib[b, k, 1] = py_px / tot
                contrib[b, k, 2] = pz / tot

    recpirocal = bands.lattice_rec.matrix / (2 * 3.14)
    #    q_start, q_end, rec_lattice, num_points=51

    # Empty lists used for caculating the distances between K-Points
    KPOINTS = [0.0]
    DIST = 0.0
    # Create list with distances between Kpoints (Individual), corrects the spacing
    for k in range(len(bands.kpoints) - 1):
        Dist = np.subtract(bands.kpoints[k + 1].frac_coords, bands.kpoints[k].frac_coords)
        DIST += np.linalg.norm(np.dot(recpirocal, Dist))
        KPOINTS.append(DIST)


    # plot bands using rgb mapping
    def plotting(size):
        for b in range(bands.nb_bands):
            ax2.scatter(KPOINTS, [e - bands.efermi for e in bands.bands[Spin.up][b]], c=contrib[b, :, :],
                        s=np.sum(contrib[b, :, :], axis=1) * size)
            rgbline(ax1,
                    range(len(bands.kpoints)),
                    [e - bands.efermi for e in bands.bands[Spin.up][b]],
                    contrib[b, :, 0],
                    contrib[b, :, 1],
                    contrib[b, :, 2],
                    KPOINTS)


    plotting(40)
    # style
    # ax1.set_xlabel("K-points")
    # ax1.set_ylabel(r"$E$ (eV)")

    # fermi level line at 0
    ax2.hlines(y=0, xmin=0, xmax=len(bands.kpoints), color="k", lw=2, linestyle='--')

    TICKS = [0.0]

    ax1.set_xlim(0, .25)
    ax1.set_ylim(-1.5, 1)
    ax1.axes.get_xaxis().set_visible(False)
    ax1.axes.get_yaxis().set_visible(False)
    ax2.set_xlim(0, .25)
    ax2.set_ylim(-1.5, 1)
    ax2.axes.get_xaxis().set_visible(False)
    ax2.axes.get_yaxis().set_visible(False)

    # Density of states
    # -----------------

    # Plotting
    # -----------------
    plt.show()
    plt.savefig(sys.argv[0].strip(".py") + ".pdf", format="pdf")
