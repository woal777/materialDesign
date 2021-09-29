#%%
import os
import numpy as np

os.chdir('/home/jinho93/new/oxides/wurtzite/gan/pbe/2hon/all-opti/eels/3')
arr = np.genfromtxt('CORE_DIELECTRIC_IMAG.dat')

arr[:,1] = arr[:,1] / max(arr[:np.argmax(arr[:,0] > 400),1])

np.savetxt('new.dat', arr)