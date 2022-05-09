#%%
import six
import numpy as np
from pymatgen import Structure, Spin, Site, Element
from pymatgen.io.vasp import Vasprun, BSVasprun
from pymatgen.util.plotting import get_axarray_fig_plt
from pymatgen.electronic_structure.dos import add_densities, Dos
from pymatgen.electronic_structure.plotter import BSDOSPlotter, BSPlotterProjected

def integrate_dos(dos: Dos):
    inte_densities = {}
    de = dos.energies[1] - dos.energies[0]
    for k, d in dos.densities.items():
        densities = [0]
        for i in d:
            densities.append(sum(densities[0]) + i * de)
        densities.pop(0)
        inte_densities[k] = np.array(densities)
    return Dos(dos.efermi, dos.energies, inte_densities)

def layer_dos_numsites(vrun: Vasprun, n):
    s: Structure
    c = vrun.complete_dos
    s = c.structure
    sites = s.sites
    dos = [None] * (n + 1)
    dos[0] = c.energies - c.efermi
    for i, site in enumerate(sorted(sites, key=lambda x: x.c)):
        ind = int(i / len(sites) * n) + 1
        print(ind)
        if dos[ind] is None:
            dos[ind] = c.get_site_dos(site).densities[Spin.up]
        else:
            dos[ind] += c.get_site_dos(site).densities[Spin.up]
    dos = np.array(dos).transpose()
    return(dos)


def layer_dos_coords(vrun: Vasprun, n, coords_range, sites=None):
    frm, to = coords_range
    s: Structure
    c = vrun.complete_dos
    s = c.structure
    if sites == None:
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
    
def ldos_plot(arr, xlim=None, frm=None, to=None, filled=False):
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
        if filled:
            plt.fill_between(arr[:, i + 1], arr[:, 0], facecolor='orange', alpha=.5)
        else:
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
    return plt

def write_dos(dos: Dos, filename='output.dat'):

    arr = np.zeros((len(dos.energies) * 2, 2))

    if len(dos.densities.keys()) > 1:
        arr[:, 0] = np.concatenate([dos.energies - dos.efermi, (dos.energies - dos.efermi)[::-1]])
        arr[:, 1] = np.concatenate([dos.densities[Spin.up], -dos.densities[Spin.down][::-1]])
    else:
        arr[:, 0] = dos.energies - dos.efermi
        arr[:, 1] = dos.densities[Spin.up]

    np.savetxt(filename, arr)

def summing_dos(cdos, sites, is_spin=False):
    arr = []
    pdos = cdos.pdos
    for i, j in pdos.items():
        if i in sites:
            arr.append(six.moves.reduce(add_densities, j.values()))  # reduced from atoms
    arr = six.moves.reduce(add_densities, arr)  # reduced from orbitals
    up = arr[Spin.up]
    if is_spin:
        down = arr[Spin.down]
    step = cdos.energies[1] - cdos.energies[0]
    if is_spin:
        return (sum(up[cdos.energies < cdos.efermi]) - sum(down[cdos.energies < cdos.efermi])) * step
    else:
        return sum(up[cdos.energies < cdos.efermi]) * step


def bsdos_plot_simple(bandpath, dospath):
    plt = BSDOSPlotter()
    bands = Vasprun(f"{bandpath}/vasprun.xml").get_band_structure(f"{bandpath}/KPOINTS", line_mode = True)
    dosrun = Vasprun(f"{dospath}/vasprun.xml")
    plt.get_plot(bands, dosrun.complete_dos).show()

def bscolorplt(path, el_ordered):
    vrun = BSVasprun(path+'/vasprun.xml', True, True)
    bs = vrun.get_band_structure(path+'/KPOINTS')
    plotter = BSPlotterProjected(bs)
    plt = plotter.get_elt_projected_plots_color(elt_ordered=el_ordered)
    plt.show()


if __name__ == '__main__':
    # path = '/home/jinho93/new/oxides/wurtzite/zno/vasp/hse/normal/post-hse/sigma/'
    path = '/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/bulk/hse/dos/'
    path = '/home/jinho93/new/oxides/fluorite/hfo2/kp/888/dos/'
    path = '/home/jinho93/new/oxides/perobskite/bfo/bcfo/dos/'
    # path = '/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/bulk/hse/dos/'
    vrun = Vasprun(path + 'vasprun.xml')
    # sites = [s for s in vrun.final_structure.sites if s.species_string == 'O']
    # sites = vrun.final_structure.sites
    # print(summing_dos(vrun.complete_dos, sites, True))
    dos = layer_dos_numsites(vrun, 2)
    print(dos)
    # np.savetxt('/home/jinho93/dos.dat', dos)
    # dos = np.genfromtxt('/home/jinho93/dos.dat')
    ldos_plot(dos,(0, 5), -8, 8)
    write_dos(vrun.tdos, '/home/jinho93/out.dat')
    # ldos_plot(dos)
    
# %%

# %%
