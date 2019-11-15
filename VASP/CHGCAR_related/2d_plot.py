from matplotlib import ticker
from pymatgen.io.vasp import Chgcar
import os
import matplotlib.pyplot as plt
import numpy as np

os.chdir('/home/jinho93/oxides/perobskite/strontium-titanate/slab/nbsto/0.superlattice/4.long/20uc/symm/4.one/2.parchg')
os.chdir('/home/jinho93/oxides/perobskite/strontium-titanate/slab/nbsto/0.superlattice/4.long/20uc/symm/3.pure/5.percent/2.fix/2.parchg')
chg = Chgcar.from_file('PARCHG')
data = np.sum(chg.data['total'], axis=0) / len(chg.data['total'])
x = np.linspace(0, 1, len(data[0]))
y = np.linspace(0, 1, len(data))
mx, my = np.meshgrid(x, y)
#plt.contourf(mx, my, data, levels=50, cmap='jet', locator=ticker.LogLocator())
data_log = np.log(data)
plt.imshow(data, cmap='jet')
plt.savefig(fname='parchg.png')
plt.show()
