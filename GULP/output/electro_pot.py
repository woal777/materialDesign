#%%
import re
import os
import numpy as np
import matplotlib.pyplot as plt

os.chdir('/home/jinho93/oxides/perobskite/lanthanum-aluminate/slab/nvt.para.6/island/len-19/step1/ini_pot')
os.chdir('/home/jinho93/new/ini_pot')
os.chdir('/home/jinho93/oxides/perobskite/lanthanum-aluminate/slab/nvt.para.6/island/len-19/step2/fin_pot')
fr = re.compile('Electrostatic')
line = re.compile('-------------------------------------------------------------------------------')
with open('report.gulp') as f:
    n = 0
    to_print = False
    arr = []
    for l in f:
        if to_print:
            if line.findall(l):
                n += 1
            elif n == 2:
                arr.append(l.split()[3])
        if fr.findall(l):
            to_print = True
        if n > 2:
            to_print = False
    
    arr = np.array(arr, dtype=float)
    arr = arr.reshape((11, 11, -1))
    print(arr)
# %%

new = np.sum(arr, axis=0) / arr.shape[0]
new = np.sum(new, axis=0) / arr.shape[0]
plt.plot(np.linspace(-10, 25, 501), new)
plt.ylim(-100, 0)
plt.show()
# %%
