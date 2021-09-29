#%%
from pymatgen import Structure
import os
import numpy as np
import matplotlib.pyplot as plt


from pymatgen.core.sites import Site

os.chdir('/home/jinho93/oxides/wurtzite/zno/vasp/6.155')

def smear(x_in, y_in, fwhm=0.5, n=2000):
    s = fwhm/(2.0*np.sqrt(2.0*np.log(2.0)))

    x0 = np.min(x_in)
    x1 = np.max(x_in)
    x = np.linspace(x0,x1,n)

    y = np.zeros(n)
    y[0] = y_in[0]
    y[-1] = y_in[-1]

    for i in range(1,len(x_in)-1):
        dx = 0.5*(x_in[i+1]-x_in[i-1])
        for j in range(1,n-1):
            y[j] += y_in[i]*np.exp(-0.5*((x[j]-x_in[i])/s)**2)/(s*np.sqrt(2.0*np.pi))*dx

    return x, y


s = Structure.from_file('POSCAR')

z_O = []
z_Zn = []
site : Site
for site in s.sites:
    if site.species_string == 'O':
        z_O.append(site.z)
    else:
        z_Zn.append(site.z)
        
        
dx = -0.1
yO, x = np.histogram(z_O, 9, (9.01 + dx, 34.6 + dx))
yZ, x = np.histogram(z_Zn, 9, (9.01 + dx, 34.6 + dx))
# xi, yi = smear(x[:-1], y, 1, len(x) * 20)
plt.plot(x[:-1], yZ / yO)
# plt.plot(x[:-1] / 50.22, yO / (yO + yZ))
# plt.plot(x[:-1] / 50.22, yZ / (yO + yZ))
print((x + dx) / 50.22)
np.savetxt('den-O.dat', yO)
np.savetxt('den-Zn.dat', yZ)
# np.savetxt('pos-zn.dat', x)