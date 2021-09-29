#%%
import re
import os
import numpy as np
import matplotlib.pyplot as plt
from macrodensity import macroscopic_average
# os.chdir('/home/jinho93/oxides/perobskite/lanthanum-aluminate/slab/gulp/stoichiometric/more/pot/990')
os.chdir('/home/jinho93/oxides/perobskite/lanthanum-aluminate/slab/gulp/nonstochio/partial/ini/center')
os.chdir('/home/jinho93/oxides/perobskite/lanthanum-aluminate/slab/gulp/nonstochio/La-vac/770/longer')
os.chdir('/home/jinho93/oxides/perobskite/lanthanum-aluminate/slab/gulp/nonstochio/partial/ini/no-vande')
os.chdir('/home/jinho93/oxides/perobskite/lanthanum-aluminate/slab/gulp/nonstochio/La-vac/first/noelect')
# os.chdir('/home/jinho93/oxides/perobskite/lanthanum-aluminate/slab/gulp/nonstochio/La-vac/890')
fr = re.compile('Electrostatic')
line = re.compile('-------------------------------------------------------------------------------')
grid = re.compile('Grid size')
star = re.compile("[*****]")
size = []
with open('report.gulp') as f:
    n = 0
    to_print = False
    arr = []
    for l in f:
        if grid.search(l):
            size = [int(r) for r in l[20:].split('X')]
        if to_print:
            if line.findall(l):
                n += 1
            elif n == 2:
                if star.search(l):
                    arr.append('0')
                else:
                    arr.append(l.split()[3])
        if fr.findall(l):
            to_print = True
        if n > 2:
            to_print = False
    
    arr = np.array(arr, dtype=float)
    arr = arr.reshape(size)

new = np.sum(arr, axis=0) / arr.shape[0]
new = np.sum(new, axis=0) / arr.shape[0]

def five_point(arr, dx):
    return (-arr[3:] + 8 * arr[2:-1] - 8 * arr[1:-2] + arr[:-3]) / 12 / dx

def two_point(arr, dx):

    return (arr[1:] - arr[:-1]) / dx

macro = macroscopic_average(new, 3.822, 0.24)
macro = macroscopic_average(macro, 3.822, 0.12)
# macro = macroscopic_average(macro, 3.822, 0.24)
x = np.linspace(-10, 50, size[2])
diff = five_point(macro[::2], x[1] - x[0])
plt.plot(np.linspace(-10, 50, size[2]), new)
plt.plot(np.linspace(-10, 50, size[2]), macro)
plt.show()
plt.plot(np.linspace(-10, 50, size[2] //2 - 2), diff)
plt.show()
np.savetxt('x.dat', np.linspace(-10, 50, size[2]))
np.savetxt('x.dat', np.linspace(-10, 50, size[2] // 2 -2))
np.savetxt('planar.dat', new)
np.savetxt('macro.dat', macro)
np.savetxt('diff.dat', -diff)
# plt.ylim(-100, 0)

# %%

os.chdir('/home/jinho93/oxides/perobskite/lanthanum-aluminate/slab/gulp/stoichiometric/more/pot')
# os.chdir('/home/jinho93/oxides/perobskite/lanthanum-aluminate/slab/gulp/nonstochio/La-vac')
output = []
for i in range(950, 1000, 10):
   output.append(np.genfromtxt(f'{i}/macro.dat'))

output = np.array(output)
np.savetxt('macroaver.dat',output.sum(axis=0) / output.shape[0])