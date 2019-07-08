import re
import os
from MDAnalysis import Universe
import numpy as np
from MDAnalysis.coordinates.XYZ import XYZReader

XYZReader.trajectory

os.chdir('/home/jinho93/tmdc/mos2/2h/2.wannier')
os.chdir('/home/jinho93/oxides/fluorite/hafnia/pca21/2.cp2k')
z_eff = {'X': -2}
with open('report.cp2k') as f:
    r = re.compile("Atom  Kind  Element")
    search = 0
    for l in f:
        if r.search(l):
            search = 2
        elif search:
            arr = l.split()
            if len(arr) > 3:
                z_eff[arr[2]] = float(arr[-2])
            else:
                search -= 1

u = Universe('wannier-HOMO_centers_s1-1_0.xyz')
pol = np.zeros(3)
new_coord = []
for c, a in zip(u.coord, u.atoms):
    if c[1] < -.25:
        c[1] += 5.074451
    new_coord.append([a.name, *list(map(str, c))])
    pol += c * z_eff[a.name]
np.savetxt('new_pol.xyz', np.array(new_coord), '%12s', header='60\n', comments='')
vol = 134.767
print(pol / vol * 1.6022e-19 * 1e+20 * 100)
