#! /usr/bin/env python
import macrodensity as md
import math
import numpy as np
import matplotlib.pyplot as plt
import os

os.chdir('/home/jinho93/molecule/ddt/vasp/2-sub/dos/decomposed/cond')
output_file = 'planar.dat'
arr = []
for i in range(626, 653):
    input_file = f'PARCHG.0{i}.ALLK'
    vasp_pot, NGX, NGY, NGZ, Lattice = md.read_vasp_density(input_file)
    vector_a,vector_b,vector_c,av,bv,cv = md.matrix_2_abc(Lattice)
    resolution_x = vector_a/NGX
    resolution_y = vector_b/NGY
    resolution_z = vector_c/NGZ
    grid_pot, electrons = md.density_2_grid(vasp_pot,NGX,NGY,NGZ)
    planar = md.planar_average(grid_pot,NGX,NGY,NGZ)
    arr.append(planar)
    plt.plot(planar)
plt.savefig('Planar.eps')
arr = np.array(arr)
np.savetxt(output_file, arr)
plt.show()
