from matplotlib import pyplot as plt
import numpy as np
from pymatgen.electronic_structure.plotter import DosPlotter
from pymatgen.util.plotting import get_axarray_fig_plt, pretty_plot

arr = np.genfromtxt('/home/jinho93/materials/oxides/fluorite/2.zirconia/5.vac_in_center/dos/output.dat')
print(arr)
num = len(arr[0])
ax_array, fig, plt = get_axarray_fig_plt(None, nrows=num, sharex=True)
plt = pretty_plot(12, 6, plt=plt)
for i in range(1, num):
    fig.add_subplot(num, 1, i + 1)
    plt.plot(arr[:,0], arr[:,i])
    plt.xlim((-5, 5))
plt.savefig('figure.png')
plt.show()
