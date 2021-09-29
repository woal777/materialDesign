
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

# os.chdir('/home/jinho93/interface/tin-hfo2-tio2/vasp/ag/dos')
# os.chdir('/home/jinho93/interface/tin-hfo2-tio2/vasp/ag/vac/dos')
os.chdir('/home/jinho93/interface/tin-hfo2-tio2/vasp/ag/dos')
os.chdir('/home/jinho93/interface/tin-hfo2-tio2/vasp/ag/vac/dos')
os.chdir('/home/jinho93/interface/tin-hfo2-tio2/vasp/ag/dos')
os.chdir('/home/jinho93/interface/tin-hfo2-tio2/vasp/ag/dn/ag')
vrun = Vasprun('vasprun.xml')
s = vrun.final_structure
cdos = vrun.complete_dos
i: Site

# fig = plt.figure()

hf_start_point = .31

arr = []
tmp = []
for i in s.sites:
    if i.c < hf_start_point and (i.species_string == 'Ti' or i.species_string == 'Hf'):
        if len(tmp) > 3:
            arr.append(tmp)
            tmp = []
        adder = cdos.get_site_dos(i).densities[Spin.up]
        adder[76:] = adder[:-76]
        tmp.append(adder)
        # arr[int(-i.z // 2.45 - 6)] 
        # plt.plot(cdos.get_site_dos(i).densities[Spin.up], cdos.energies - cdos.efermi)
dos_arr = np.zeros((len(arr) + 1, len(cdos.energies)))
dos_arr[0] = vrun.tdos.energies - vrun.tdos.efermi

for n, a in enumerate(arr):
    dos_arr[n + 1] = np.sum(a, axis=0)

np.savetxt('output.dat', dos_arr.transpose(), '%16.8E')

