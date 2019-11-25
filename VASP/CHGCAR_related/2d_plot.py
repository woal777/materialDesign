from matplotlib import ticker
from pymatgen.io.vasp import Chgcar
import os
import matplotlib.pyplot as plt
import numpy as np

os.chdir('/home/jinho93/molecule/oep-sub_fe/110-oxygen/4-third/30_amin/gr')
chg = Chgcar.from_file('CHGCAR')
data = np.sum(chg.data['diff'][146:156], axis=2) #/ (len(chg.data['diff'][0][0]) - int(len(chg.data['diff'][0][0]) * .649))
#plt.contourf(mx, my, data, levels=50, cmap='jet', locator=ticker.LogLocator())
data_log = np.log(data)
plt.imshow(data, cmap='jet')
plt.savefig(fname='parchg.png')
plt.show()
