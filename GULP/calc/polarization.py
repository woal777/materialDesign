#%%

from MDAnalysis.core.universe import Universe
import os
import numpy as np
import matplotlib.pyplot as plt

# os.chdir('/home/jinho93/oxides/perobskite/lanthanum-aluminate/periodic_step/gulp/8.108/fix')
os.chdir('/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/periodic_step/gulp/015/0/thick/4')
# os.chdir('/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/my015/from-gulp/421/test')
p_arr = []
u = Universe('lao.xyz')
for trj in u.trajectory:
    p = [0]
    for atom, pos in zip(u.atoms, trj):
        if atom.name == 'Al':
            p += pos * 3
        elif atom.name == 'La':
            p += pos * 3
        elif atom.name == "O":
            p += pos * -2
    p_arr.append(p)
p_arr = np.array(p_arr)


n = len(u.atoms)
n //= 5
pz = p_arr[:, 2]
e = 1.6e-19
a = 3.81127
vol = a ** 3
pz *= e / n / vol * 1e+20
np.savetxt('/home/jinho93/pz.dat', pz)



#%%
plt.plot(pz)
plt.xlim(1495, 1503)
plt.ylim(-0.1, 0.5)
plt.show()
plt.plot(pz)
plt.xlim(0, 15)
plt.ylim(-0.8, 0.8)

# %%
np.savetxt('/home/jinho93/n.dat', range(1500))
# %%
