from pymatgen import Structure
from pymatgen.io.vasp import Vasprun
import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


def dos2dat():
    vrun = Vasprun('vasprun.xml')
    dos = []
    cdos = vrun.complete_dos
    dos.append(cdos.energies - cdos.efermi)
    for s in vrun.final_structure.sites:
        dos.append(cdos.get_site_dos(s).densities)
    np.savetxt(dos)


def divide():
    s = Structure.from_file('CONTCAR')


def plot():
    os.chdir('/home/jinho93/interface/lsmo-bto/2.interface/11.5uc/up/isif2/dos')
    os.chdir('/home/jinho93/interface/pt-bto/up')
    arr = np.genfromtxt('output.dat')
    print(arr[:, 0].shape)
    plt.figure(figsize=(4, 2))
    gs1 = gridspec.GridSpec(1, len(arr[0, :]) // 2)
    gs1.update(wspace=0.0, hspace=0.05)  # set the spacing between axes.

    for i in range(len(arr[0, :]) // 2):
        # i = i + 1 # grid spec indexes from 0
        ax1 = plt.subplot(gs1[i])
        plt.axis('on')
        if i != 0:
            ax1.set_yticklabels([])
        else:
            ax1.tick_params(axis="y", labelsize=20)
        ax1.set_xticklabels([])
        ax1.fill_between(arr[:, 2 * i + 2], arr[:, 0], facecolor='orange', alpha=.2)
        plt.ylim(-5, 5)
        plt.xlim(0, 5)
    plt.show()


def test():
    from pymatgen import MPRester, Composition
    m = MPRester('DhmFQPuibZo8JtXn')
    results = m.query("**O", ['density', 'task_id', 'structure'])
    print(len(results))
#    print(sorted(results, key=lambda x: x['density']))


if __name__ == '__main__':
    test()
