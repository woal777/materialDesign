#%%
import os
import shutil
import numpy as np
from pymatgen.analysis.eos import EOS
from pymatgen import Structure
#%%
os.chdir('/home/jinho93/battery/anode/silicon/1/eos/ml')
os.chdir('/home/jinho93/battery/anode/silicon/72/0/eos')
s: Structure
for i in np.linspace(0.95, 1.05, 11):
    os.makedirs(str(i), exist_ok=True)
    s = Structure.from_file('POSCAR')
    s.apply_strain(i - 1)
    s.to('POSCAR', 'POSCAR-NEW')
    for files in ['INCAR', 'KPOINTS', 'POSCAR-NEW', 'POTCAR', 'ML_FF']:
        shutil.copyfile(files, f'{i}/{files}')
    
    os.rename(f'{i}/POSCAR-NEW', f'{i}/POSCAR')

#%%
import re
os.chdir('/home/jinho93/battery/anode/silicon/72/42/eos')

volumes, energies = [], []
ene_line = re.compile('ML energy')

for i in np.linspace(0.95, 1.05, 11):
    os.system(f'sed -i "s/N\/A/0/g" {i}/OUTCAR')
    with open(f'{i}/OUTCAR') as outcar:
        for l in outcar:
            if ene_line.search(l):
                energies.append(float(l.split()[-1]))
    s = Structure.from_file(f'{i}/POSCAR')
    volumes.append(s.volume)

eos = EOS(eos_name='murnaghan')
eos_fit = eos.fit(volumes, energies)
eos_fit.plot()
print(eos_fit.b0_GPa)
# %%
