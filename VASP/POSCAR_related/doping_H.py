import shutil

from pymatgen import Structure
import copy
import os

os.chdir('/home/lgdisplay/1.oxides/1.quartz/1.same_as_igzo/4.hyd_inter')
s = Structure.from_file('CONTCAR')

for n, site in enumerate(s.sites):
    if site.species_string == 'O':
        s.replace(n, 'H', properties=s.sites[n].properties)
        if not os.path.exists(f'../4.hyd_inter/{n:02d}'):
            os.mkdir(f'../4.hyd_inter/{n:02d}')
        shutil.copy('../4.hyd_inter/INCAR', f'../4.hyd_inter/{n:02d}')
        shutil.copy('../4.hyd_inter/KPOINTS', f'../4.hyd_inter/{n:02d}')
        shutil.copy('../4.hyd_inter/POTCAR', f'../4.hyd_inter/{n:02d}')
        s2 = copy.deepcopy(s)
        s2.sort()
        s2.to('POSCAR', f'../4.hyd_inter/{n:02d}/POSCAR')
        s.replace(n, 'O', properties=s.sites[n].properties)


