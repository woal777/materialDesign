#%%
from pymatgen import Molecule, Site
import os
import numpy as np
import matplotlib.pyplot as plt

# os.chdir('/home/jinho93/oxides/perobskite/lanthanum-aluminate/slab/nvt.para.6/island/len-19/step2/fin_pot')
# os.chdir('/home/jinho93/oxides/perobskite/lanthanum-aluminate/slab/gulp/nonstochio/La-vac/880')
os.chdir('/home/jinho93/oxides/perobskite/lanthanum-aluminate/slab/gulp/stoichiometric/more')
# os.chdir('/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/slab/gulp')
with open('lao.xyz') as f:
    lines = f.readlines()


exper = '''-0.01289
-0.0017
-0.00536
-0.00199
-0.00234
-0.00173
1.04182E-4'''
exper = [float(r) * 10 for r in exper.split('\n')][::-1]

def get_output(mole):
    A, B, O = [], [], []
    i: Site
    for i in mole.sites:
        if i.species_string == "O":
            O.append(i.z)
        elif i.species_string == "Al":
            B.append(i.z)
        else:
            A.append(i.z)

    A.sort()
    # A = A[10:]
    # A.append(A[-1])
    # A.append(A[-1])
    B.sort()
    O.sort()
    # O = O[12:]
    inplane = 16
    A, B, O = np.array(A), np.array(B), np.array(O)
    B = B.reshape((-1, inplane))
    A = A.reshape((-1, inplane))
    O = O.reshape((-1, inplane * 3))
    O1 = O[:,:inplane * 2]
    O2 = O[:,inplane * 2:]


    Az = np.sum(A, axis=1) / inplane
    Bz = np.sum(B, axis=1) / inplane
    O1z = np.sum(O1, axis=1) / inplane / 2
    O2z = np.sum(O2, axis=1) / inplane

    output = np.zeros(len(Az) * 2)
    output[1::2] = (Az - O2z) / 2
    output[::2] = (Bz - O1z) / 2

    return output

outputs = []
atoms_number = 802
for i in range(680, 910, 10):
    mole = Molecule.from_str(''.join(lines[atoms_number * i:atoms_number * (i+1)]), fmt='xyz')
    outputs.append(get_output(mole))
outputs = np.array(outputs)
outputs = np.sum(outputs, axis=0) / outputs.shape[0]
np.savetxt('rumpling.dat', outputs[::-1] / 10)
plt.plot(outputs[11:])
plt.plot(exper)
plt.ylim((-0.2, 0.05))
plt.show()
#%%
# %%
