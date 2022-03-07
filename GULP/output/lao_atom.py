#%%
import os

os.chdir('/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/periodic_step/gulp/015/0/thick/4/output/new')

with open('new.xyz', 'w') as new:
    with open('orig.xyz') as orig:
        for n, l in enumerate(orig):
            if n % 202 == 0:
                new.write(l.replace('200', '400'))
                continue
            if n % 202 == 1:
                new.write(l)
                continue
            tmp = float(l[30:45]) + 19.433700000000
            newline = l[:30] + f'{tmp}' + l[45:]
            if n % 202 == 91 or n % 202 == 168:
                new.write(l.replace('O', 'F'))
                new.write(newline.replace('O', 'F'))
            elif n % 202 == 46 or n % 202 == 47:
                new.write(l.replace('La', 'Fe'))
                new.write(newline.replace('La', 'Fe'))
            else:
                new.write(l)
                new.write(newline)
            # tmp = float(l[30:45]) + 15
            # newline = l[:30] + f'{tmp}' + l[45:]

# %%
tmp = float(l[30:45]) + 19.433700000000
newline = l[:30] + f'{tmp}' + l[45:]

# %%
from pymatgen import Structure

from phonopy import Phonopy

p = Phonopy()

p.generate_displacements(distance=)

s = Structure.from_file()

s.tra