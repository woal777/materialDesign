from pymatgen.io.vasp import Vasprun
import os

os.chdir('/home/seohuigim79/sto/sto05/1')
vrun = Vasprun('vasprun.xml')

gap = vrun.complete_dos.get_gap()

print(gap)