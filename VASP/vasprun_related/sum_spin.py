import six
from pymatgen.electronic_structure.core import Spin
from pymatgen import PeriodicSite
from pymatgen.electronic_structure.dos import add_densities
from pymatgen.io.vasp import Vasprun

vrun = Vasprun('vasprun.xml')
cdos = vrun.complete_dos
pdos: dict = cdos.pdos
arr = []
for i, j in pdos.items():

    if .55 < i.c < 0.65:
        arr.append(six.moves.reduce(add_densities, j.values()))  # reduced from atoms

arr = six.moves.reduce(add_densities, arr)  # reduced from orbitals

up = arr[Spin.up]
down = arr[Spin.down]
step = cdos.energies[1] - cdos.energies[0]
print((sum(up[cdos.energies < cdos.efermi]) - sum(down[cdos.energies < cdos.efermi])) * step)
