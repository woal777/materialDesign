import os, re
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
from pymatgen import Structure
import matplotlib.pyplot as plt
import numpy as np

os.chdir('/home/jinho93/metal/3.Fe16N2/phonon/2.Al/disp/007')
s1 = Structure.from_file('POSCAR')
s2 = Structure.from_file('../SPOSCAR')
pos = s1.cart_coords
pos2 = pos - s2.cart_coords
