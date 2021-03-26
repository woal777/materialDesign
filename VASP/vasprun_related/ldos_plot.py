#%%

from matplotlib import pyplot as plt
import numpy as np
from pymatgen.electronic_structure.plotter import DosPlotter
from pymatgen.util.plotting import get_axarray_fig_plt, pretty_plot
import os
os.chdir('/home/jinho93/oxides/perobskite/lanthanum-aluminate/slab/14')

arr = np.genfromtxt('lsmo.dat')
num = len(arr[0])
num -= 1
ax_array, fig, plt = get_axarray_fig_plt(None, ncols=num, sharey=True)
plt = pretty_plot(12, 12, plt=plt)
for i in range(1, num):
    fig.add_subplot(1, num, i)
    plt.plot(arr[:, i], arr[:, 0])
    plt.ylim((-5, 3))
    plt.xlim(0,3)
    plt.xticks([])
    plt.yticks([])
    plt.axis('off')
plt.subplots_adjust(wspace=0)
plt.savefig('figure.png')
plt.show()

# %%
