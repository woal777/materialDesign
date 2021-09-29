#%%
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib as mpl
from ase.io import read
from pyqstem.util import atoms_plot
from pyqstem import PyQSTEM
from pyqstem.potentials import poisson_solver,create_potential_slices
from pymatgen.io.vasp import Chgcar
# import os
# os.chdir('/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/my015/from-gulp')

c = Chgcar.from_file('CHGCAR')
rho = c.data['total']
atoms=read('CONTCAR.cif',index=0) # atomic configuration
cell=atoms.get_cell()

Lx,Ly,Lz=np.diag(atoms.get_cell())
Nx,Ny,Nz=rho.shape
res_x,res_y=Lx/Nx,Ly/Ny

fig,(ax1,ax2)=plt.subplots(1,2,figsize=(10,5))
atoms_plot(atoms,ax=ax1,scale_atoms=.5)
im=ax2.imshow(np.trapz(rho,dx=Lz/Nz,axis=2).T,extent=[0,Lx,0,Ly],cmap='inferno')
ax2.set_xlabel('x [Angstrom]')
ax2.set_ylabel('y [Angstrom]')
divider = make_axes_locatable(ax2)
cax2 = divider.append_axes("right", size="5%", pad=0.05)
plt.colorbar(im,cax=cax2,label='e/Angstrom**2')
plt.tight_layout()
plt.show()

print('Total charge (in elementary charges):',np.sum(rho*Lx*Ly*Lz/(Nx*Ny*Nz)))
# %%
