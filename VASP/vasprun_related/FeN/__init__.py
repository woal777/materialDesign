from pymatgen.io.vasp import Vasprun
from pymatgen import Orbital, Spin
import os
import numpy as np

os.chdir('/home/jinho93/metal/3.Fe16N2/dos/m5.ismear/m1.isym/0.pure')

vrun = Vasprun('vasprun.xml')
cdos = vrun.complete_dos
structure = vrun.final_structure
ef = cdos.efermi
dx = cdos.energies[1] - cdos.energies[0]
dos_dict = {}
# Al
# h8, e4, d4 = 4, -4, -3
#  pure
h8, e4, d4 = 4, -5, -1

for orb in [Orbital.dxy, Orbital.dyz, Orbital.dz2, Orbital.dxz, Orbital.dx2]:
    dos_dict[orb.name] = cdos.get_site_orbital_dos(structure.sites[h8], orb)


#    dos_dict[orb.__str__()].densities = dos_dict[orb.__str__()].get_smeared_densities(0.1)

def save_dos_dict():
    arr = [np.concatenate([cdos.energies - cdos.efermi, (cdos.energies - cdos.efermi)[::-1]])]
    for i in dos_dict.values():
        tmp = np.concatenate([i.densities[Spin.up], -i.densities[Spin.down][::-1]])
        arr.append(tmp)
    arr = np.array(arr)
    np.savetxt('output.dat', arr.transpose(), delimiter='\t')


if __name__ == '__main__':
    from pymatgen.electronic_structure.plotter import DosPlotter
    from VASP.vasprun_related.FeN.MAE import Coupling
    dsp = DosPlotter()
    dsp.add_dos_dict(dos_dict)
    dsp.show(xlim=(-2, 1), ylim=(-1.5, 1.5))

    save_dos_dict()
