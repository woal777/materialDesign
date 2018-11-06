from pymatgen.io.vasp.outputs import Xdatcar

xdat = Xdatcar('XDATCAR')
for j, i in enumerate(xdat.structures):
    i.to('POSCAR', f'POSCAR{j:02d}')