import numpy
from pymatgen.io.vasp.outputs import Vasprun, Spin, Element, Dos
import os
import six

os.chdir('/home/jinho93/molecule/ddt/vasp/2-sub/dipole/mole')
vrun = Vasprun('vasprun.xml')
densities = vrun.tdos.densities[Spin.up]
vbm = densities[vrun.tdos.energies < vrun.efermi]
print(sum(vbm) * (vrun.tdos.energies[1] - vrun.tdos.energies[0]))

os.chdir('/home/jinho93/molecule/ddt/vasp/2-sub/dipole/sub')
vrun = Vasprun('vasprun.xml')
densities = vrun.tdos.densities[Spin.up]
vbm = densities[vrun.tdos.energies < vrun.efermi]
print(sum(vbm) * (vrun.tdos.energies[1] - vrun.tdos.energies[0]))


os.chdir('/home/jinho93/molecule/ddt/vasp/2-sub/dos')
vrun = Vasprun('vasprun.xml')
densities = vrun.tdos.densities[Spin.up]
sub = []
mole = []
i: Element
j: Dos
for i, j in vrun.complete_dos.get_element_dos().items():
    if i == Element.Mo or i == Element.S:
        sub.append(j.densities[Spin.up])
    else:
        mole.append(j.densities[Spin.up])
mole = numpy.array(mole)
mole = numpy.sum(mole,axis=0)
sub = numpy.array(sub)
sub = numpy.sum(sub, axis=0)
print(sum(mole[vrun.tdos.energies < vrun.efermi]) * (vrun.tdos.energies[1] - vrun.tdos.energies[0]))
print(sum(sub[vrun.tdos.energies < vrun.efermi]) * (vrun.tdos.energies[1] - vrun.tdos.energies[0]))

