from matplotlib import pyplot as plt
import numpy as np
from pymatgen.electronic_structure.plotter import DosPlotter
from pymatgen.util.plotting import get_axarray_fig_plt, pretty_plot

arr = np.genfromtxt('output.dat')
num = len(arr[0])
ax_array, fig, plt = get_axarray_fig_plt(None, ncols=num, sharex=True)
plt = pretty_plot(12, 12, plt=plt)
for i in range(1, num):
    fig.add_subplot(1, num, i + 1)
    plt.plot(arr[:, i], arr[:, 0])
    plt.ylim((-5, 5))
plt.savefig('figure.png')
plt.show()
