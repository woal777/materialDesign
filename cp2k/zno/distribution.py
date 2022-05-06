#%%
import numpy as np
import os

path = '/home/jinho93/oxides/wurtzite/zno/cp2k/1.aimd/3.16A/30/3.fix/output/'
arr = np.genfromtxt(path + 'i.dat')[:,-1]
arr = arr - np.min(arr)
arr = arr[:527]
# %%
from matplotlib import pyplot as plt
n = 400
p, x = np.histogram(arr, bins=n) # bin it into n = N//10 bins

plt.plot(x[1:], p)
plt.show()


def spectrum(E,osc,sigma,x):
    gE=[]
    for Ei in x:
        tot=0
        for Ej,os in zip(E,osc):
            tot+=os*np.exp(-((((Ej-Ei)/sigma)**2)))
        gE.append(tot)
    return gE

sigma = 0.008
newx= np.linspace(min(x), max(x), 500)
gE=spectrum(arr, np.ones(len(arr)),sigma, newx)

gE /= np.sum(gE) * (newx[1] - newx[0])
plt.plot(newx, gE)
plt.show()
np.savetxt('/home/jinho93/spec.dat', np.transpose([newx, gE]))

#%%
arr2 = []
cumul = 0
for g in gE:
    cumul += g * (newx[1] - newx[0])
    arr2.append(cumul)

plt.plot(arr2)
# %%
np.savetxt('/home/jinho93/spec.dat', np.transpose([newx, arr2]))

# %%

with open('/home/jinho93/ener.dat', 'w') as f:
    for i in range(len(arr)):
        f.write(f'{arr[i]} 0\n')
        f.write(f'{arr[i]} 1\n\n')

with open('/home/jinho93/x.dat', 'w') as f:
    for i in range(len(arr)):
        f.write(f'0\n')
        f.write(f'1\n\n')

# %%
