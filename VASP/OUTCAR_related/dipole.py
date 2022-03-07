#%%
import re
import os

# os.chdir('/home/jinho93/tmdc/WTe2/mo-alloy/nonpolar/lien/md/small/194')
os.chdir('/home/jinho93/tmdc/WTe2/mo-alloy/nonpolar/lien/md/small/70')
os.chdir('/home/jinho93/tmdc/WTe2/mo-alloy/nonpolar/conf1/ps/md/small')
os.chdir('/home/jinho93/tmdc/WTe2/mo-alloy/nonpolar/lien/md/11')
os.chdir('/home/jinho93/tmdc/WTe2/mo-alloy/nonpolar/conf1/ps/md/uc/200')
os.chdir('/home/jinho93/tmdc/WTe2/mo-alloy/nonpolar/conf1/ps/md/uc/200/conf4')
os.chdir('/home/jinho93/tmdc/WTe2/mo-alloy/nonpolar/s4_new/t0')
os.chdir('/home/jinho93/tmdc/WTe2/mo-alloy/nonpolar/lien/md')
os.chdir('/home/jinho93/tmdc/WTe2/mo-alloy/nonpolar/lien/md/small/')
# os.chdir('/home/jinho93/tmdc/WTe2/mo-alloy/nonpolar/conf1/ps/md/uc')
# os.chdir('/home/jinho93/tmdc/WTe2/Td/ps/md/conf2')
# os.chdir('/home/jinho93/tmdc/WTe2/mo-alloy/nonpolar/lien/md/small')
# os.chdir('/home/jinho93/tmdc/WTe2/mo-alloy/nonpolar/lien/md/small/high-t/132')
loop = []
energy = []
lp = re.compile('LOOP:')
lpp = re.compile('LOOP\+')
en = re.compile('ETOTAL')
with open('OUTCAR') as f:
    num = 0
    for l in f:
        if lpp.search(l):
            loop.append(num)
            # print(l)
            # num = 0
        if lp.search(l):
            num += 1
        if en.search(l):
            energy.append(l.split()[-2])
# %%
dip = []
rdip = re.compile('dipolm')
with open('OUTCAR') as f:
    for l in f:
        if rdip.search(l):
            dip.append(float(l.split()[3]))

# %%
import numpy as np
dip = np.array(dip)
loop = np.array(loop)
loop -= 1
# %%
import matplotlib.pyplot as plt
fig, ax1 = plt.subplots()
ax1.plot(dip[loop] / 0.005)
ax2 = ax1.twinx()
# plt.plot(energy)
arr = np.genfromtxt('energy.dat')
arr = arr[:,[0,8]]
# arr = arr[:,[0,4]]
ax2.plot(arr[:,1], c='red')

# ax1.set_xlim((120,140))

# %%
from pymatgen.io.vasp import Xdatcar

xdat = Xdatcar.from_file('XDATCAR')

xdat.structures[70].to('POSCAR', 'NEWPOSCAR')

# %%
from pymatgen import Structure
coords = []
s: Structure
for s in xdat.structures[70:]:
    coords.append(s.frac_coords)
    
coords = np.array(coords)
#%%
aver = np.sum(coords, axis=0) / coords.shape[0]
print(aver.shape)
poscar = Structure.from_file('POSCAR')
new = Structure(poscar.lattice, poscar.species, aver)
new.to('POSCAR', 'NEWPOSCAR')
# np.sum(coords)
# %%
new = dip[loop]
new = new[280:]
plt.scatter(range(len(new)), new)
# %%
