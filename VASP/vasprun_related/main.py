#%%
from pymatgen import Structure
import numpy as np
from pymatgen.io.vasp import Vasprun
from pymatgen.io.vasp.outputs import Spin
from pymatgen.util.plotting import get_axarray_fig_plt, pretty_plot


def layer_dos(vrun: Vasprun, n, frm=None, to=None):
    s: Structure
    c = vrun.complete_dos
    s = c.structure
    sites = s.sites
    if frm and to:
        sites = [site for site in sites if frm < site.c < to]
    dos = [None] * (n + 1)
    dos[0] = c.energies - c.efermi
    for site in sorted(sites, key=lambda x: x.c):
        ind = int((site.c - frm) * n / (to - frm) - 1e-9) + 1
        if dos[ind] is None:
            dos[ind] = c.get_site_dos(site).densities[Spin.up]
        else:
            dos[ind] += c.get_site_dos(site).densities[Spin.up]
    dos = np.array(dos).transpose()
    return(dos)
    
def ldos_plot(arr, xlim=None, frm=None, to=None):
    num = len(arr[0])
    num -= 1
    ax_array, fig, plt = get_axarray_fig_plt(None, ncols=num, sharey=True)
    # pretty_plot(12, 12, plt=plt)
    if frm and to:
        ymin = min(np.argwhere(arr[:, 0] > frm))[0]
        ymax = max(np.argwhere(arr[:, 0] < to))[0]
    for i in ax_array:
        i.axes.get_xaxis().set_visible(False)
        i.axes.get_yaxis().set_visible(False)
    for i in range(num):
        fig.add_subplot(1, num, i + 1)
        plt.plot(arr[:, i + 1], arr[:, 0])
        if frm and to:
            plt.ylim((frm, to))
            if xlim:
                plt.xlim(xlim)
            else:
                plt.xlim(0, int(np.max(arr[ymin:ymax,1:]) * 1.2))
        plt.xticks([])
        plt.yticks([])
        plt.axis('off')
    plt.subplots_adjust(wspace=0)
    # plt.savefig('figure.png')
    # plt.show()


if __name__ == '__main__':
    import os
    path = '/home/jinho93/new/oxides/wurtzite/zno/vasp/hse/normal/post-hse/sigma/'
    # vrun = Vasprun(path + 'vasprun.xml')
    # dos = layer_dos(vrun, 10, .178, 0.703)
    np.savetxt('/home/jinho93/dos.dat', dos)
    dos = np.genfromtxt('/home/jinho93/dos.dat')
    ldos_plot(dos,(0, 10), -5, 5)
    # ldos_plot(dos)
    
# %%
