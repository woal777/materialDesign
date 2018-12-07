from scipy.io import FortranFile
import numpy as np
from pymatgen.command_line.gulp_caller import GulpIO
gio = GulpIO()
gio.get_iniitial_structure('/home/jinho93/slab/LAO/grimes/nvt/dense/report.gulp')
fortran = False
if fortran:
    with FortranFile('/home/jinho93/slab/LAO/bush/nvt/island/old/md.trg') as f:
        version = f.read_reals()[0]
        n_atoms, ndim = f.read_ints()
        print(f'Version is {version}\nn_atoms is {n_atoms}, ndim is {ndim}')
        n_frames = 3
        for _ in range(n_frames):
            tket = f.read_reals()
            tket = [f'{r:.02f}' for r in tket]
            print(f'Time/KE/E/T {tket}')
            for l in range(10):
                line = f.read_reals()
                print(len(line))
else:
    with open('/home/jinho93/slab/LAO/grimes/nvt/dense/lao.trg') as f:
        version = f.readline()
        n_atoms, ndim = [int(r) for r in f.readline().split()]
        print(f'Version is {version}\nn_atoms is {n_atoms}, ndim is {ndim}')
        n_frames = 1

        for _ in range(n_frames):
            x, y, z = np.zeros(n_atoms), np.zeros(n_atoms), np.zeros(n_atoms)
            vx, vy, vz = np.zeros(n_atoms), np.zeros(n_atoms), np.zeros(n_atoms)
            dx, dy, dz = np.zeros(n_atoms), np.zeros(n_atoms), np.zeros(n_atoms)
            de = f.readline()
            tket = f.readline().split()
            print(f'{de}{tket}')
            print(f.readline(), end='')
            for i in range(n_atoms):
                x[i], y[i], z[i] = [np.float16(r) for r in f.readline().split()]
            print(f.readline(), end='')
            for i in range(n_atoms):
                vx[i], vy[i], vz[i] = [np.float16(r) for r in f.readline().split()]
            print(f.readline(), end='')
            for i in range(n_atoms):
                dx[i], dy[i], dz[i] = [np.float16(r) for r in f.readline().split()]
            print(f.readline(), end='')
            se = [np.float32(f.readline()) for r in range(n_atoms)]
            print(vx[392])
            print(dx[0])
            print(se[-1])
