#%%
import matplotlib.pyplot as plt
from pymatgen.core.sites import Site
from pymatgen.io.vasp import Locpot
import os

os.chdir('/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/stengel/015/4/lvhar')

loc = Locpot.from_file('LOCPOT')

s = loc.structure

from scipy.interpolate import griddata
import numpy as np
#%%

dat = loc.data['total']
x = []
y = []
z = []
site : Site
on = False
for site in sorted(s.sites, key=lambda x: x.c):
    if site.species_string == "O":
    # or site.species_string == "Al":
        x.append(site.b)
        y.append(site.c)
        z.append(dat[int(dat.shape[0] * site.a)
                    , int(dat.shape[1] * site.b)
                    , int(dat.shape[2] * site.c)])
    # else:
        # if on:
        #     z[-1] += (dat[int(dat.shape[0] * site.a)
        #                 , int(dat.shape[1] * site.b)
        #                 , int(dat.shape[2] * site.c)] / 2)
        #     on = False
        #     continue
        # if site.species_string == 'Al':
        #     x.append(site.b)
        #     y.append(site.c)
        #     z.append(dat[int(dat.shape[0] * site.a)
        #                 , int(dat.shape[1] * site.b)
        #                 , int(dat.shape[2] * site.c)] / 2)
        #     on = True
        # else:
        #     x.append(site.b)
        #     y.append(site.c)
        #     z.append(dat[int(dat.shape[0] * site.a)
        #                 , int(dat.shape[1] * site.b)
        #                 , int(dat.shape[2] * site.c)] / 2)
        
# x = x[::2]
# y = y[::2]
# z = [(i + j) / 2 for i, j in zip(z[::2], z[1::2])]
x.extend(np.array(x) - 1)
y.extend(np.array(y))
z.extend(z)
x.extend(np.array(x) + 1)
y.extend(np.array(y))
z.extend(z)
xi, yi = np.linspace(min(x), max(x),100), np.linspace(min(y), max(y), 100)
zi = griddata((x, y), z, (xi[None,:], yi[:,None]), method='cubic', fill_value=min(z))
print(np.max(zi), np.min(zi))
# plt.contourf(xi, yi, zi, levels=np.linspace(-108, -98, 51), cmap='inferno')
plt.contourf(xi, yi, zi, cmap='inferno')
plt.colorbar()
plt.scatter(x, y, s=50, color='#00b0f0')
plt.xlim((0, 1))
plt.axis('off')
plt.savefig('/home/jinho93/output.png', dpi=200)

# plt.imshow(np.sum(dat, axis=0))
# %%
