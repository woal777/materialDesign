#%%
from pymatgen.analysis.surface_analysis import SurfaceEnergyPlotter, SlabEntry, ComputedStructureEntry
from pymatgen import Structure
from pymatgen.io.vasp import Oszicar
import numpy as np
import matplotlib.pyplot as plt
from sympy import Symbol, symbols

def entry_from_path(path) -> ComputedStructureEntry:
    return ComputedStructureEntry(
    Structure.from_file(path + 'POSCAR'), 
    Oszicar(path + 'OSZICAR').final_energy)

def slab_entry_from_path(path, miller=None) -> SlabEntry:
    return SlabEntry(
    Structure.from_file(path + 'POSCAR'), 
    Oszicar(path + 'OSZICAR').final_energy, miller)

def plot_mu1_mu2(se, min, n):
    div = n // min
    space = np.zeros((n, n))

    for i in range(n):
        ii = i / div - min
        for j in range(n):
            jj = j / div - min
            seq = np.zeros(len(se))
            # if jj * 2 + ii * 3 < g_la2o3:
            #     space[i, j] = -1
            #     continue
            for k in range(len(se)):

                if type(se[k]) == float:
                    seq[k] = se[k]
                else:
                    seq[k] = (se[k].subs(o, ii).subs(la, jj))
            space[i, j] = np.argmin(seq)
            # else:
                # space[i, j] = 0
    plt.imshow(space, vmin=0, vmax=len(se))

def plot_mu1(se, el1, el2, mu1, lbound, ubound, write=False):
    xmin = (lbound - 3 * mu1) / 2
    xmax = (ubound - 3 * mu1) / 2
    x = np.linspace(xmin - 1, xmax + 1, 100)
    y = []
    for k in range(len(se)):
        tmp = np.zeros(len(x))
        for ind, xx in enumerate(x):
            if type(se[k]) == float:
                tmp[ind] = (se[k])
            else:
                tmp[ind] = (se[k].subs(el1, mu1).subs(el2, xx))
        y.append(tmp * 16)
    
    if write:
        output = np.zeros((len(y) + 1, len(x)))
        output[0,:] = x
        output[1:, :] = np.array(y)
        np.savetxt('output.dat', output.T)
    else:
        for i, yy in enumerate(y):
            plt.plot([xmin] * 2, [-50, 50], '--', color='grey')
            plt.plot([xmax] * 2, [-50, 50], '--', color='grey')
            plt.plot(x, yy, label=f'{i}')
        plt.legend()
        plt.ylim(np.min(y) - 0.1, np.max(y) + 0.1)
        plt.show()

def plot_mu2(se, el1, el2, min, max, n, bound, write=False):
    x = np.linspace(min, max, n)
    y = []
    for k in range(len(se)):
        tmp = np.zeros(len(x))
        for ind, xx in enumerate(x):
            mu1 = (bound - 3 * xx) / 2
            if type(se[k]) == float:
                tmp[ind] = (se[k])
            else:
                tmp[ind] = (se[k].subs(el1, mu1).subs(el2, xx))
        y.append(tmp * 16)
    
    if write:
        output = np.zeros((len(y) + 1, len(x)))
        output[0,:] = x
        output[1:, :] = np.array(y)
        np.savetxt('output.dat', output.T)
    else:
        for i, yy in enumerate(y):
            plt.plot(x, yy, label=f'{i}')
        plt.legend()
        plt.show()

if __name__ == '__main__':
    pass
    
# %%
