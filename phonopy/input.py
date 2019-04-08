import os
import shutil

for i in [f'{r:03d}' for r in range(1, 49)]:
    os.mkdir(i)
    shutil.copy('INCAR', i)
    shutil.copy('KPOINTS', i)
    shutil.copy('POTCAR', i)
    shutil.move(f'POSCAR-{i}', f'{i}/POSCAR')
