from pymatgen.io.vasp.outputs import Vasprun, Dos, Structure, Spin
from pymatgen.electronic_structure.plotter import DosPlotter
from pymatgen.util.plotting import get_axarray_fig_plt, pretty_plot
import numpy as np
import os
os.chdir('/home/ksrc5/FTJ/bfo/111-dir/junction/sto/vasp/orig/new_vca/opti')
vrun = Vasprun('vasprun.xml')
s: Structure = vrun.final_structure
cdos = vrun.complete_dos
pdos = cdos.pdos
doss = dict()
num = 16
arr = np.linspace(0, 1, num, endpoint=False)
darr = arr[1] - arr[0]
for j in arr:
    densities = []
    for i in s.sites:
        if j + darr > i.c >= j:
            densities.append(cdos.get_site_dos(i).get_densities())
    densities = np.sum(densities, axis=0)
    doss[f'{j:.2f}'] = Dos(cdos.efermi, cdos.energies, {Spin.up: densities})
dsp = DosPlotter(sigma=0.1)
ax_array, fig, plt = get_axarray_fig_plt(None, nrows=num, sharex=True)
plt = pretty_plot(12, 6, plt=plt)
for i in range(num):
    dsp.__init__(sigma=0.05)
    a = doss.popitem()
    dsp.add_dos(*a)
    fig.add_subplot(num, 1, i + 1)
    subplt = dsp.get_plot(xlim=(-5, 3), plt=plt)
plt.savefig('figure.png')
plt.show()

