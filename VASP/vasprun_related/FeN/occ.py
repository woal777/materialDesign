from pymatgen import Spin, Element, Orbital
from pymatgen.io.vasp import Vasprun
import os

os.chdir('/home/jinho93/metal/3.Fe16N2/dos/m5.ismear/0.isym/0.pure')
vrun = Vasprun('vasprun.xml')
cdos = vrun.complete_dos
structure = vrun.final_structure

ef = cdos.energies < cdos.efermi
dx = cdos.energies[1] - cdos.energies[0]

dos_dict = {}
# Al
h8, e4, d4 = 4, -5, -1

arr = [[] for _ in range(16)]
for j in range(2, 18):
    for i in [Orbital.dxy, Orbital.dxz, Orbital.dyz, Orbital.dx2, Orbital.dz2]:
        arr[j - 2].append(sum(cdos.get_site_orbital_dos(structure.sites[j], i).get_densities(Spin.up)[ef]) * dx
                          - sum(cdos.get_site_orbital_dos(structure.sites[j], i).get_densities(Spin.down)[ef]) * dx)

for j in range(16):
    print(arr[j][0])
