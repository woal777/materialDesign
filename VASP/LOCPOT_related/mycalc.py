#%%
from pymatgen.io.vasp import Chgcar
import os
import matplotlib.pyplot as plt
from joblib import Parallel, delayed

os.chdir('/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/slab/3uc/efield/2/delta')

chg = Chgcar.from_file('CHGCAR')

#%%

def distance(p1, p2):
    return math.sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2)+((p1[2]-p2[2])**2))

def potential(z):
    pot = 0
    for i, a in enumerate(chg.data['total']):
        for j, b in enumerate(a):
            for k, c in enumerate(b):
                d = distance([chg.dim[0] // 2, 0, z], [i, j, k])
                if d > 0:
                    pot += c / d
    return pot

res = Parallel(n_jobs=12)(delayed(potential)(r) for r in range(0, chg.dim[2], 5))

plt.plot(res)
plt.show()