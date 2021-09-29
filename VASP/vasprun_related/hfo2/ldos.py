
#%%
import functools
from operator import add
import os
from re import S
from pymatgen.core.periodic_table import Specie
from pymatgen.core.sites import Site
from pymatgen.electronic_structure.core import Spin
from pymatgen.electronic_structure.dos import add_densities
from pymatgen.io.vasp import Vasprun
import matplotlib.pyplot as plt
import numpy as np

# os.chdir('/home/jinho93/interface/tin-hfo2/2.strain2tin/1.Cdoped/3.down_carbon/dos')
os.chdir('/home/jinho93/interface/tin-hfo2/2.strain2tin/1.Cdoped/3.down_carbon/2.opti/2.dos/ismear0')
os.chdir('/home/jinho93/interface/tin-hfo2/2.strain2tin/1.Cdoped/2.carbon/2.dos/ismear0')
vrun = Vasprun('vasprun.xml')
s = vrun.final_structure
cdos = vrun.complete_dos
i: Site

# fig = plt.figure()

hf_start_point = .38

arr = []
tmp = []
atoms = []

for i in sorted(s.sites, key=lambda x: x.z):
    if i.c > hf_start_point and (i.species_string == 'Hf' 
                                 or i.species_string == 'O' 
                                 or i.species_string == 'C'
                                 ):
        adder = cdos.get_site_dos(i).densities[Spin.up]
        # adder[1590:] = adder[1512:len(adder) + 1512 - 1590]
        tmp.append(adder)
        atoms.append(i.species_string)
        if len(tmp) > 5:
            print(atoms)
            arr.append(tmp)
            tmp = []
            atoms = []
        # arr[int(-i.z // 2.45 - 6)] 
        # plt.plot(cdos.get_site_dos(i).densities[Spin.up], cdos.energies - cdos.efermi)
dos_arr = np.zeros((len(arr) + 1, len(cdos.energies)))
dos_arr[0] = vrun.tdos.energies - vrun.tdos.efermi

for n, a in enumerate(arr):
    dos_arr[n + 1] = np.sum(a, axis=0)  

np.savetxt('output.dat', dos_arr.transpose(), '%16.8E')

