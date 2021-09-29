#%%
def direct2cart(directpos,basis):
    cart=[]
    for atdirect in directpos:
        cart.append(np.dot(np.transpose(basis),atdirect))
    return np.array(cart)

import numpy as np
import phonopy
from math import sqrt
import sys
import argparse
import os

os.chdir('/home/jinho93/metal/3.Fe16N2/phonon/2.Al/disp/test')

sc=np.array([2,0,0,0,2,0,0,0,1]).reshape(3,3)
pm=np.array([1,0,0,0,1,0,0,0,1]).reshape(3,3)


ph = phonopy.load(supercell_matrix=sc,
                  primitive_matrix=pm,
                  unitcell_filename='POSCAR',
                  calculator='vasp',
                  force_constants_filename='FORCE_CONSTANTS')

basis=ph.get_unitcell().get_cell()
xred=ph.get_unitcell().get_scaled_positions()

natom=len(xred)
masses=ph.get_unitcell().get_masses()
chemel=ph.get_unitcell().get_chemical_symbols()


cartpos=direct2cart(xred,basis)

dynmat_data = ph.get_dynamical_matrix_at_q([0,0,0])

dynmat = []
#i = 0
for row in dynmat_data:
    dynmat.append(row.real + row.imag)
dm = np.array(dynmat, dtype='double')
eigvals, eigvecs, = np.linalg.eigh(dm)

frequencies=[]

ph.unit_conversion_factor
frequencies=np.sqrt(np.abs(eigvals)) * np.sign(eigvals)

#%%
for i in frequencies:
    print(i * 16.6333)
# %%
