#%%
from pymatgen.io.vasp import Chgcar
import os
import numpy as np
import matplotlib.pyplot as plt

os.chdir('/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/my015/from-gulp/lvhar')
chg = Chgcar.from_file('CHGCAR')

dat = chg.data['total']

plt.imshow(np.sum(dat, axis=0))
