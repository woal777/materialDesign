import re
import os
from MDAnalysis import Universe
import numpy as np

os.chdir('/home/jinho93/oxides/cluster/zno/cp2k/2.wann')
z_eff = {'X': -2}
with open('report.cp2k') as f:
    r = re.compile("Atom  Kind  Element")
    v = re.compile(r'Volume \[angstrom')
    search = 0
    for l in f:
        if r.search(l):
            search = 2
        elif v.search(l):
            vol = float(l.split()[-1])
        elif search:
            arr = l.split()
            if len(arr) > 3:
                z_eff[arr[2]] = float(arr[-2])
            else:
                search -= 1

u = Universe('wannier-HOMO_centers_s1-1_0.xyz')
pol = np.zeros(3)
new_coord = []
print(z_eff)
for c, a in zip(u.coord, u.atoms):
    if c[2] < .162:
        c[2] += 5.1638688669733437
    if c[1] < -2.3:
        c[1] += 5.5572505783499953
    new_coord.append([a.name, *list(map(str, c))])
    pol += c * z_eff[a.name]
np.savetxt('new_pol.xyz', np.array(new_coord), '%12s', header='44\n', comments='')
print(pol[2] / vol * 1.6022e-19 * 1e+20)
