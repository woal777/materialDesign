#%%
import os
import numpy as np
from pymatgen.io.vasp import Xdatcar
from pymatgen_diffusion.aimd.van_hove import RadialDistributionFunction, plt

if __name__ == '__main__':
    os.chdir('/home/jinho93/oxides/cluster/zno/vasp/1.aimd/2.10A/2.02/3fs')
    structures = Xdatcar('XDATCAR').structures[-1:]
    # rdf = RadialDistributionFunction(structures, indices=range(100), reference_indices=range(100))
    num = 4
    fig = plt.figure(0)
    output = np.zeros((201, num))
    output[:, 0] = np.linspace(0.0, 10, 201)
    for c in range(num - 1):
        oxy = []
        for i, j in enumerate(structures[0].sites):
            if j.species_string == "O" and c / num < j.c < (c + 1) / num:
                oxy.append(i)
        zn = []
        print(c, oxy)
        for i, j in enumerate(structures[0].sites):
            if j.species_string == "O":
                zn.append(i)
        ax = fig.add_subplot(221 + c)
        rdf = RadialDistributionFunction(structures, oxy, zn, ngrid=201)
        rdf.get_rdf_plot(ylim=(0, max(rdf.rdf)), plt=plt)
        output[:, c + 1] = rdf.rdf
    np.savetxt('output.dat', output)
    plt.show()
