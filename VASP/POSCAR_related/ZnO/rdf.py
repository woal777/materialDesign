import os
import numpy as np
from pymatgen.io.vasp import Xdatcar
from pymatgen_diffusion.aimd.van_hove import RadialDistributionFunction, plt
from pymatgen import Structure

if __name__ == '__main__':
    structure = Structure.from_file('POSCAR')
    num = 4
    fig = plt.figure(0)
    output = np.zeros((201, num))
    output[:, 0] = np.linspace(0.0, 10, 201)
    for c in range(num - 1):
        oxy = []
        for i, j in enumerate(structure.sites):
            if j.species_string == "O" and c / num < j.c < (c + 1) / num:
                oxy.append(i)
        zn = []
        for i, j in enumerate(structure.sites):
            if j.species_string == "Zn":
                zn.append(i)
        ax = fig.add_subplot(221 + c)
        rdf = RadialDistributionFunction([structure], oxy, zn, ngrid=201)
        rdf.get_rdf_plot(ylim=(0, max(rdf.rdf)))
        output[:, c + 1] = rdf.rdf
    np.savetxt('output.dat', output)
    plt.show()
