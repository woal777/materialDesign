#%%
import os
from matplotlib.pyplot import bar_label
import numpy as np
from pymatgen.io.vasp import Xdatcar
from pymatgen_diffusion.aimd.van_hove import RadialDistributionFunction, plt
from sympy import Indexed

def get_rdf(a, b, structures, nblock):
    output = np.zeros((201, num))
    output[:, 0] = np.linspace(0.0, 10, 201)
    for n in range(len(structures) // nblock):
        rdf = RadialDistributionFunction(structures[n*nblock:(n+1)*nblock], a, b, ngrid=201)
        rdf.get_rdf_plot(ylim=(0, max(rdf.rdf)))
        output[:,n + 1] = rdf.raw_rdf
    return output
#%%
if __name__ == '__main__':
    os.chdir('/home/jinho93/battery/anode/TiO2/npt/li-diff/1')
    os.chdir('/home/jinho93/battery/anode/silicon/72/126')
    xdat = Xdatcar.from_file('XDATCAR').structures[::10]
    nb = 10
    num = len(xdat) // nb + 1
    fig = plt.figure(0)
    a = []
    for i, j in enumerate(xdat[0].sites):
        # if j.species_string == "Li":
        a.append(i)
    b = a
    # for i, j in enumerate(xdat[0].sites):
    #     if j.species_string == "Li":
    #         b.append(i)
            
    output = get_rdf(a, b, xdat, nb)
    np.savetxt('output.dat', output)
    plt.show()

# %%
