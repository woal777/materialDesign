from pymatgen.command_line.gulp_caller import GulpCaller, GulpIO
from matplotlib import pyplot
import numpy as np

gio = GulpIO()
gc = GulpCaller()
arr = []
for i in np.linspace(0.5, 1, 100):
    body = f'''conv
#cell
#1 1 10 90 90 90
cart
O core 0 0 -{i}
O core 0 0 {i}
Hf core 0 0 0
species
Hf core  2.4
O  core -1.2
general 0 12
Hf core O core 0 0 1.0 1.
'''
    gout = gc.run(body)
    e = gio.get_energy(gout)
    arr.append(e)
pyplot.plot(arr)
pyplot.show()