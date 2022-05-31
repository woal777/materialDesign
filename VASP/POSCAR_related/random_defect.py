#%%
from pymatgen import Structure
import numpy as np

path = '/home/jinho93/ml/hfo2/schottky/'
# path = '/home/jinho93/new/oxides/wurtzite/zno/vasp/aimd/2000k/schottky/'
s:Structure = Structure.from_file(path + 'POSCAR')
a_site = int(s.composition.as_dict()['Hf'])
b_site = int(s.composition.as_dict()['O'])
n = a_site // 10
print(n)
m = 2
arr_a = np.random.randint(0, a_site - 1, n)
arr_b = np.random.randint(a_site - 1, a_site + b_site - 1, m * n)
s.remove_sites(np.concatenate((arr_a, arr_b)))
s.to('POSCAR', path + 'POSCAR-NEW')
# %%
