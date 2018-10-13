from pymatgen.io.lammps.inputs import LammpsData
from pymatgen.io.lammps.data import LammpsBox ,ForceField
import numpy as np
ip = LammpsData.from_file('data.m-HfO2')
ip.structure.to('POSCAR', 'POSCAR')