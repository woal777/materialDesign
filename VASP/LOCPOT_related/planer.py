#%%
import numpy as np
from pymatgen.io.vasp import Locpot
import matplotlib.pyplot as plt
import os


os.chdir('/home/jinho93/oxides/perobskite/lanthanum-aluminate/slab/14/asym/to_Al/ldipol')
loc = Locpot.from_file('LOCPOT')

y = loc.get_average_along_axis(2)

np.savetxt('data.dat', range(len(y)))
plt.plot(range(len(y)), y)
plt.show()