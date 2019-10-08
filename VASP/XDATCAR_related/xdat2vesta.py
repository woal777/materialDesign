from pymatgen.io.vasp.outputs import Xdatcar

xdat = Xdatcar('XDATCAR')
vesta = open('CONTCAR.vesta').readlines()
struc = 0
for m, l in enumerate(vesta):
    if 'STRUC' in l:
        struc = m
for j, i in enumerate(xdat.structures):
    tmp_vesta = vesta
