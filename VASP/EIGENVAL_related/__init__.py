import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import macrodensity as md


def plot_eigenval(filename='EIGENVAL', fermi=0):
    arr = np.genfromtxt(filename, skip_header=8)
    output = []
    for i in arr[:, 1]:
        print(i - fermi)
        output.append([i - fermi, 0])
        output.append([i - fermi, 1])
        output.append([i - fermi, 0])


def plot(path, lattice_vector):
    vasp_pot, NGX, NGY, NGZ, Lattice = md.read_vasp_density(path + '/LOCPOT')
    vector_a, vector_b, vector_c, av, bv, cv = md.matrix_2_abc(Lattice)
    resolution_x = vector_a / NGX
    resolution_y = vector_b / NGY
    resolution_z = vector_c / NGZ
    grid_pot, electrons = md.density_2_grid(vasp_pot, NGX, NGY, NGZ)
    # POTENTIAL
    planar = md.planar_average(grid_pot, NGX, NGY, NGZ)
    # MACROSCOPIC AVERAGE
    macro = md.macroscopic_average(planar, lattice_vector, resolution_z)
    x = np.linspace(0, 1, len(planar))
    fig, ax1 = plt.subplots(1, 1, sharex=True)

    textsize = 22
    mpl.rcParams['xtick.labelsize'] = textsize
    mpl.rcParams['ytick.labelsize'] = textsize
    mpl.rcParams['figure.figsize'] = (10, 6)
    ax1.plot(x, planar,label="Planar",lw=3)
    ax1.plot(x, macro, label="Macroscopic", lw=3)
    ax1.set_xlim(0, 1)
    ax1.grid(True)
    ax1.legend(fontsize=22)
    plt.show('loc.png')
