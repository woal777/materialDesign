#%%
import macrodensity as md
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
import os


os.chdir('/home/jinho93/new/oxides/perobskite/lanthanum-aluminate/periodic_step/vasp/my015/from-gulp/2ps')
potential_file = 'LOCPOT' # The file with VASP output for potential
coordinate_file = 'POSCAR' # The coordinates file NOTE NOTE This must be in vasp 4 format 
species = "La"  # The species whose on-site potential you are interested in 
sample_cube = [1,1,1] # The size of the sampling cube in units of mesh points (NGX/Y/Z)

# Nothing below here should require changing
#------------------------------------------------------------------
# Get the potential
# This section should not be altered
#------------------------------------------------------------------
vasp_pot, NGX, NGY, NGZ, Lattice = md.read_vasp_density(potential_file)
vector_a,vector_b,vector_c,av,bv,cv = md.matrix_2_abc(Lattice)
resolution_x = vector_a/NGX
resolution_y = vector_b/NGY
resolution_z = vector_c/NGZ
grid_pot, electrons = md.density_2_grid(vasp_pot,NGX,NGY,NGZ)
## Get the gradiens (Field), if required.
## Comment out if not required, due to compuational expense.
grad_x,grad_y,grad_z = np.gradient(grid_pot[:,:,:],resolution_x,resolution_y,resolution_z)
#------------------------------------------------------------------

##------------------------------------------------------------------
## Getting the potentials for a group of atoms, in this case the Os
## NOTE THIS REQUIRES ASE to be available https://wiki.fysik.dtu.dk/ase/index.html
##------------------------------------------------------------------
##------------------------------------------------------------------
import ase                # Only add this if want to read in coordinates
from ase.io import write  # Only add this if want to read in coordinates
from ase.io import vasp   # Only add this if want to read in coordinates

coords = ase.io.vasp.read_vasp(coordinate_file)
scaled_coords = coords.get_scaled_positions()
symbols = coords.get_chemical_symbols()
ox_coords = []

for i, atom in enumerate(coords):
    if symbols[i] == species:
        ox_coords.append(scaled_coords[i])


grid_position = np.zeros(shape=(3))
potentials_list = []
i = 0
num_bins = 20
x, y = [], []
for coord in ox_coords:
    i = i + 1
    grid_position[0] = coord[0]
    grid_position[1] = coord[1]
    grid_position[2] = coord[2]
    cube = sample_cube    # The size of the cube x,y,z in units of grid resolution.
    origin = [grid_position[0]-2,grid_position[1]-2,grid_position[2]-1]
    x.append(grid_position[1]-2)
    y.append(grid_position[2]-1)
    volume_average, cube_var = md.volume_average(origin, cube, grid_pot, NGX, NGY, NGZ)
    potentials_list.append(volume_average)
    
x = x[::2]
y = y[::2]
z = [(i + j) / 2 for i, j in zip(potentials_list[::2], potentials_list[1::2])]
x.extend(np.array(x) - 1)
y.extend(np.array(y))
z.extend(z)
x.extend(np.array(x) + 1)
y.extend(np.array(y))
z.extend(z)
xi, yi = np.linspace(min(x), max(x),100), np.linspace(min(y), max(y), 100)
zi = griddata((x, y), z, (xi[None,:], yi[:,None]), method='cubic')
#%%
print(round(min(potentials_list), -1), round(max(potentials_list), -1))
plt.contourf(xi, yi, zi, levels=np.linspace(round(min(potentials_list), -1), round(max(potentials_list), -1), 51), cmap='inferno')
plt.colorbar()
plt.xlim((-2, -1))
plt.scatter(x, y, s=50, color='#00b0f0')
plt.axis('off')

# %%
