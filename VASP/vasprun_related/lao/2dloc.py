#%%
from pymatgen.io.vasp import Locpot
import os
import numpy as np
import matplotlib.pyplot as plt

os.chdir('/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/stengel/013/lreal')

loc = Locpot.from_file('LOCPOT')

dat = np.sum(loc.data['total'], axis=0)

class Circular:
    periodic = True

    def __init__(self, r):
        self.radius = r
        self.fil = np.zeros((2*r+1, 2*r+1))
        a, b = np.arange(-r,r+1,1), np.arange(-r,r+1,1)
        for i in a:
            for j in b:
                if np.sqrt(i**2 + j**2) <= r:
                    self.fil[i+ r,j + r] = 1

    def filtering(self, arr):
        if self.periodic:        
            result = np.zeros([arr.shape[0], arr.shape[1]],dtype=float)
            new_arr = np.concatenate([arr[-self.radius:,:], arr, arr[:self.radius,:]])
            new_arr = np.transpose(new_arr)
            new_arr = np.concatenate([new_arr[-self.radius:,:], new_arr, new_arr[:self.radius,:]])
            new_arr = np.transpose(new_arr)
            for i in range(result.shape[0]):
                for j in range(result.shape[1]):
                    result[i, j] = np.sum(self.fil * new_arr[i:i+2 * self.radius + 1, j:j+2 * self.radius + 1])
        else:
            result = np.zeros([arr.shape[0] - 2 * self.radius, arr.shape[1] - 2 * self.radius],dtype=float)     
            for i in range(result.shape[0]):
                for j in range(result.shape[1]):
                    result[i, j] = np.sum(self.fil * arr[i:i+2 * self.radius + 1, j:j+2 * self.radius + 1])
        
        return result
import time

#%%

t = time.time()
c = Circular(40)
smo = c.filtering(dat)
plt.imshow(smo)

print(time.time() - t)
# %%
